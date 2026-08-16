!!! note "AI-assisted"
    Drafted with AI while I studied - tagged so it's clear it's a study aid, not my own writing.

# Make it work, then make it nice (Day 12: number guessing game)

> I mostly solved the number guessing game, then spent far longer than the code deserved fighting my own head. The bugs were never hard. What was hard was noticing *why* I kept re-introducing them. This note is about that, not about the loop.

## The two traps I kept falling into

Every bug I hit came from one of these, not from the coding being difficult:

**1. Cargo-culting from bad memory.** I was sure Angela had crammed both end-conditions into one `is_game_over` function, so I kept trying to reproduce that shape — from a half-remembered video. She hadn't. I was copying the *silhouette* of a solution without its reasoning, and you can't debug a silhouette. When I finally looked at my own Blackjack code, I'd already done the right thing there (`is_round_over` decides, `define_winner` announces — two separate jobs). The pattern I needed was in my own repo, not in my memory of someone else's.

**2. Premature optimization.** I had it in my head that checking "out of lives?" in more than one place was *wrong*, so I kept trying to be clever and collapse it. That hunt is what produced every bug: the double-print, the extra guess at zero lives, the `None`. I was optimizing something that didn't work yet.

## The fix is boring and it's the whole point

**Make it work, then make it nice.** Write it as I actually think, even if it's dumb and repetitive. Get it correct first. *Then*, if it's genuinely ugly, tidy it. Trying to skip straight to elegant just generates bugs in something that doesn't exist yet.

And the thing that unlocked it: **repetition is not automatically a code smell.** Checking lives in two places, or printing a result from two branches, is often just fine. I treated a tiny repeat like a crime, and the crusade to remove it broke everything.

## The one real technical lesson underneath it all

Whatever loop style I use (flag or `break`), the rule is the same: **detect the ending and stop in the same place.** My bugs came from checking "is the game over?" at the *top* of the loop while I changed the state (spent a life, read the guess) at the *bottom* — a full lap apart. Put the check right next to the thing it depends on and both the flag version and the `break` version come out clean.

- Flag version stays clean when I set `game_over = True` exactly where I detect the end, and put the "still playing" work in an `else` so nothing else runs that iteration.
- The `break` version stays clean because it stops mid-body, on the spot, the instant it finds the ending.

Flag vs `break` was never the bug. Placement was.

## What I missed in Angela's walkthrough (and where mine held up)

I watched the walkthrough at 2x with a pint in me, so I caught almost nothing live. Going back over it properly, here's what's actually worth taking — and, being fair to myself for once, where my version came out cleaner.

### Worth stealing

- **Wrap the whole game in a `game()` function and call it at the bottom.** Encapsulation, and it lets me end the game with `return` instead of `break`. It also sets up a "play again?" loop almost for free later — just wrap it in `while play_again: game()`.
- **`from random import randint`** — import the one name I use instead of the whole module, so it's `randint(1, 100)` rather than `random.randint(...)`. Small and tidy.
- **A temporary `print(f"the answer is {answer}")` while developing**, so I can test without guessing blind — then delete it before it's "done." (Fits my reachable-vs-latent note: dev scaffolding is fine as long as it doesn't ship.)
- The good ideas I'd already grabbed on my own: named constants for the levels, and driving the loop with `while guess != answer` off a sentinel value. So my half-memory of "Angela did something smart with globals and the loop" was actually correct — that part I got right.

### Where mine came out better (so I stop assuming hers is the "real" one)

- **My feedback function returns on every path.** Her `check_answer` returns `turns - 1` on a wrong guess but falls off the end on a win, so it returns `None`. It's harmless only because the loop exits right after — but it's the exact "return on every path" trap I documented in the Blackjack note. Mine returns a string in all three branches.
- **My feedback function returns a message; hers prints inside itself and also secretly decrements the turns** (`return turns - 1`). That's two responsibilities crammed into one function — the very thing I spent this whole exercise learning to split. Returning the string and letting the caller print is easier to test and keeps the function doing one job.
- **I used `lives <= 0`; she used `turns == 0`.** Both work, but `<= 0` is the more defensive check.

Two valid solutions, again. I keep expecting Angela's to be the professional version and mine to be the amateur one, and both times it's been a wash — sometimes mine is tidier. Noted, hopefully for good this time.

## Note to self

The gap between "I could not produce this" and "this is trivial to read" is not a measure of how bad I am. It's just what learning feels like from the inside. If it had felt easy while I was building it, I wouldn't have been learning anything. Write as I think. Fix it after it runs. Stop trying to match a memory.
