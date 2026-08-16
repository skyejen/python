!!! note "AI-assisted"
    Drafted with AI while I studied - tagged so it's clear it's a study aid, not my own writing.

# File naming: `_` vs `-`

> When to use underscores vs hyphens in filenames.

- **Python files (`.py`) use underscores** (`snake_case`, e.g. `higher_lower_game.py`). PEP 8, and the hard reason: hyphens are illegal in imports. `import higher-lower-game` reads the `-` as a minus sign and errors, so any file you might `import` has to use underscores. That is why Angela's `game_data.py` and `art.py` use them, and why my imports work. Use underscores even for run-only scripts, for consistency.
- **Docs, markdown, and web pages use hyphens** (`day-14-higher-lower-game.md`). The URL/web convention.

Rule of thumb: **underscores for code, hyphens for docs.**
