!!! note "AI-assisted"
    Drafted with AI while I studied - tagged so it's clear it's a study aid, not my own writing.

# Loop control

> The loop-control keywords: `pass`, `continue`, `break`, and `for`/`while` with `else`.

## `pass` vs `continue` vs `break`

Three keywords that are easy to mix up. `continue` and `break` live inside loops; `pass` works anywhere a statement is required.

- **`pass`** does nothing. A placeholder for when Python's syntax needs a statement but you want no action. Execution just falls through and the loop carries on as normal.
- **`continue`** skips the rest of the current iteration and jumps straight to the next one.
- **`break`** exits the loop entirely, right now.

```python
for n in [1, 2, 3, 4]:
    if n == 2:
        pass       # does nothing, execution falls through
    if n == 3:
        continue   # skip the rest of THIS iteration, go to next n
    if n == 4:
        break      # leave the loop entirely
    print(n)

# Output:
# 1
# 2
# (3 is skipped by continue before it can print; 4 never prints because break exits first)
```

Rule of thumb: `pass` = "do nothing, keep going", `continue` = "skip to the next lap", `break` = "stop the loop".

## `for...else` (and `while...else`)

A loop can have its own `else`. It's real syntax, not a mistake. **The `else` runs only if the loop finished WITHOUT hitting a `break`.** If a `break` fired, the `else` is skipped.

So `break` and the loop's `else` are a pair: `break` = "stop, I found it / I'm done", `else` = "the thing to do only if nobody ever broke out".

```python
for n in [1, 2, 3]:
    if n == 9:
        break
else:
    print("finished without a break")   # RUNS (no 9, so no break)

for n in [1, 2, 3]:
    if n == 2:
        break
else:
    print("finished without a break")   # SKIPPED (n == 2 broke the loop)
```

**When it's actually useful:** searching. Loop looking for something, `break` the moment you find it, and the `else` runs only if you got all the way through and never found it.

**When it's NOT worth it:** if you `return` out of the loop instead of `break`ing (like in the prime checker), the loop just completes normally when nothing is found, so a plain `return`/statement *after* the loop does the same job and reads clearer. No `break` in play = `else` buys you nothing.
