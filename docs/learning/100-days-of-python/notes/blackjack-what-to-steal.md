!!! note "AI-assisted"
    Drafted with AI while I studied - tagged so it's clear it's a study aid, not my own writing.

# Blackjack (Day 11): what to steal from Angela's solution

> I compared my working solution to Angela's walkthrough. I did NOT rewatch it attentively, because I'd already solved and understood it (that's the learning, not the video). These are the techniques worth carrying forward.

## The big one: derive from the source, don't track a copy

Angela recomputes the score fresh from the cards on every loop (`user_score = calculate_score(user_cards)` each time), instead of tracking it incrementally (`score += card`, then adjust) like I did. Her score is always **derived from the source of truth (the cards)**, so it can never drift out of sync.

My entire ace/score tangle came from tracking-and-adjusting two things (a running score and the card list) that could disagree. Lesson to carry forward: **when a value can be computed from something you already have, compute it fresh, don't keep a separate copy in sync by hand.**

## Small Pythonic hacks worth pocketing

- `sum(cards)` totals a list in one call. I wrote a manual `for` loop in `calculate_score` to do the same thing.
- `for _ in range(2):` uses `_` as the name for a loop variable you don't actually use (signals "I'm ignoring this"). I wrote `for card in range(0, 2)` but never used `card`.
- One flat `while not is_game_over:` loop with a single flag is simpler than my two nested loops (`game_session` + `continue_dealing`). Worth knowing the pattern; not worth rewriting a working game for.
- She returns `0` as a secret code for "blackjack" (natural 21 on the first two cards) to tell it apart from a regular 21. It works, but a magic number like that is the kind of "clever" that reads worse. Know the trick, don't copy the style.

## Where mine was as good or better (so I don't discount my own work)

- Mine is more readable in places: real function names, split display functions.
- My `update_ace_points` is more robust as a standalone function than hers: I added the stop-when-safe `break`, whereas hers reduces only one ace per call and leans on being called repeatedly.

Two valid solutions, different trade-offs. I didn't do it wrong.
