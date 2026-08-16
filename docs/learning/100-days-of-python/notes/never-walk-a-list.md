!!! note "AI-assisted"
    Drafted with AI while I studied - tagged so it's clear it's a study aid, not my own writing.

# Never walk a list you're changing (and everything the Blackjack ace bug taught me)

> From the Day 11 Blackjack capstone. This one bug opened up four real lessons, so they all live here.

## The bug

The original ace-adjuster looped over `card_list` while removing from and appending to that same `card_list`:

```python
# BUGGY
for card in card_list:
    if card == 11:
        card_list.remove(11)   # mutating the list...
        card_list.append(1)    # ...that we're looping over
        score = score - 10
```

Tested in isolation, `update_ace_points(32, [11, 11, 10])` returned **22** when it should be 12. It only reduced ONE of the two aces.

## Why it happened

When you remove from and append to a list **while a for-loop is walking it**, the loop's internal position drifts out of sync with the shifting contents, so it silently skips items. Removing the first `11` shifts the second `11` back into an index the loop already passed, so the loop never sees it.

**Rule: never change the length of a list while iterating over that same list.**

## The fix

Walk over a stable **copy**, mutate the **real** list, and stop the moment the hand is safe:

```python
def update_ace_points(score, card_list):
    if score > 21 and 11 in card_list:
        temp_list = card_list.copy()   # walk this (stable snapshot)
        for card in temp_list:
            if score <= 21:
                break                  # stop once safe (don't over-reduce)
            elif card == 11:
                card_list.remove(11)   # change the REAL list (caller sees it)
                card_list.append(1)
                score = score - 10
    return score                       # return on EVERY path, not just inside the if
```

## The four lessons this one bug surfaced

**1. Mutable vs immutable (why the list changes leak out but the score doesn't).**
Variables are labels pointing at objects. Passing to a function hands over a copy of the label, so both point at the same object.
- A list is mutable: `.append` / `.remove` edit the shared object in place, so the caller sees it, no `return` needed.
- An int is immutable: `score = score - 10` can't change the number, so it builds a NEW int and repoints only the local label. The caller sees nothing unless you `return` it.
- So: mutate-in-place leaks out; rebind-a-local stays local. (This is exactly why `card_list = temp_list` did NOT work, it only moved a local label.)

**2. Reachable vs latent defects.**
The original bug was real at the function level but **unreachable in the actual game**, because the score entering the function is capped at 31 (rest score max 20 plus one card max 11), and a single reduction always gets you to 21 or under. A unit test caught it with an input the game can never produce. Lesson: "unreachable today" is a fact about today's code, not a guarantee. A robust function is correct on its own terms, not because its callers happen to be polite.

**3. Reduce only as much as needed.**
Once the score is safe (21 or under), STOP. Reducing every ace turns `[11, 11]` (should be 12) into `[1, 1]` (2). `break` the instant you're safe, keeping remaining aces as 11 for the highest legal score.

**4. Return on every path.**
A function that falls off the end without hitting a `return` gives back `None`. If the `return` lived only inside the `if`, every hand that needed no adjustment returned `None`. Put the `return` where all paths reach it (the end of the function).
