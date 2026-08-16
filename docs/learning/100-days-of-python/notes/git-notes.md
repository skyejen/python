!!! note "AI-assisted"
    Drafted with AI while I studied - tagged so it's clear it's a study aid, not my own writing.

# Git learning notes

Personal reference for git commands and situations encountered while learning.

---

## Splitting one commit into multiple (interactive rebase with edit)

Use when you accidentally put multiple unrelated changes in one commit.

```
git rebase -i HEAD~N        # N = how many commits back to go
```

- Change `pick` to `e` on the commit you want to split, save and quit
- Git pauses on that commit and hands control back to you
- Run `git reset HEAD~1` to unstage all its files (keeps files, removes commit)
- Recommit each file separately:

```
git add filename
git commit -m "type: description"
```

- Repeat for each file, then:

```
git rebase --continue       # tells git the rebase is done
git push --force-with-lease # push the rewritten history
```

**NEVER do this on a shared branch.** Rebase rewrites commit history (changes SHA hashes). Anyone who already pulled those commits will have a diverged branch. Solo repos only.

---

## Amending the most recent commit message

When the last commit message has a typo or needs changing:

```
git commit --amend -m "your corrected message here"
git push --force-with-lease
```

`--force-with-lease` is safer than `--force` -- it refuses to push if someone else has pushed to the same branch in the meantime.

---

## Changing older commit messages (interactive rebase)

When you need to fix a message that is NOT the most recent commit:

```
git rebase -i HEAD~N
```

Replace `N` with how many commits back you want to go. For example, `HEAD~2` covers the last 2 commits.

This opens vim showing the commits. Change `pick` to `r` (reword) on any commit you want to rename, then save and quit.

### Vim quick reference

- You are in NORMAL mode by default
- Press `i` to enter INSERT mode (for editing text)
- Press `Escape` to go back to NORMAL mode
- Type `:wq` in NORMAL mode to save and quit
- If `:wq` is typing into the file instead of the command bar, you are still in INSERT mode -- press `Escape` first

Git will pause on each `r` commit and open another editor for you to type the new message. Save and quit each one the same way.

When the rebase is done, force push:

```
git push --force-with-lease
```

### `--force-with-lease` vs `--force`

`--force` overwrites the remote no questions asked. `--force-with-lease` first checks whether anyone else has pushed to the branch since you last fetched -- if yes, it refuses. Same result on a solo repo, but the right habit to build.

### What is rebase?

Rebase lets you rewrite commit history -- change messages, reorder commits, squash multiple into one, or split one into many. It changes the SHA hashes of commits, which is why you need a force push after. Powerful, and solo-only for the same reason.

### Vim: replacing a single character (normal mode)

`r` then `<character>` replaces the character under the cursor without entering insert mode. So to change `pick` to `edit`, move cursor to `p` and press `r` then `e`. The `r` says "replace mode for one character," the next key is the replacement.

### Classic mistake

Typing `:wq` while still in INSERT mode saves the literal text `:wq` into the commit message. Fix it with:

```
git commit --amend -m "your actual message"
git push --force-with-lease
```

---

## Commit message convention (this repo)

Format: `type: short description`

- Lowercase everything, including names and exercise titles
- Imperative mood -- "add" not "added"
- No emojis (have to copy-paste them, not worth it)
- Keep it under 72 characters

Types used in this repo: `exercise`, `docs`, `fix`, `notes`, `chore`, `refactor`

Examples:
- `exercise: add tip calculator`
- `exercise: add treasure island`
- `docs: add README`

---

## Concepts

### What is rebase?

Rebase lets you rewrite commit history -- change messages, reorder commits, squash multiple into one, or split one into many. It physically changes the SHA hash (the unique ID) of each affected commit, which is why the remote no longer recognises them and you need a force push after. Powerful and slightly dangerous -- solo repos only.

### `--force-with-lease` vs `--force`

`--force` overwrites whatever is on the remote, no questions asked. `--force-with-lease` first checks whether anyone else has pushed to the branch since you last fetched -- if yes, it refuses to push and protects their work. On a solo repo the result is the same, but `--force-with-lease` is the right habit to build for when you eventually work in a team.

### SHA hashes

Every commit in git gets a unique fingerprint called a SHA hash (e.g. `a151ae3`). It's calculated from the content of the commit, its message, its timestamp, and its parent commit. Rebase changes the message or content, so the hash changes too -- the old commit and the new commit are technically different objects. This is why git sees your local and remote branches as "diverged" after a rebase.

### Vim: modes

Vim has two main modes. Normal mode is the default -- keys do commands, not typing. Insert mode is for editing text (press `i` to enter, `Escape` to exit). The `:wq` save-and-quit command only works in normal mode. Classic trap: trying to type `:wq` while still in insert mode, which just adds those characters to your file.
