# Agent instructions

How AI agents (Claude, Codex, etc.) should work in this repo. **Read this before editing.**

This site shares its theme with the sibling repos `cybersecurity` and `skyejen.github.io`.
`cybersecurity` is where the theme and most conventions originate, so if something here looks
thin, check that repo's `AGENTS.md` before inventing a new approach.

> **Theme JS is shared — don't edit it here.** `extra.js` is not in this repo; it comes
> from the **sj-theme** submodule at `docs/sj-theme/`. Edit the theme in the sj-theme repo,
> never inside `docs/sj-theme/` (edits there are detached and get lost). Pull updates with
> `git submodule update --remote docs/sj-theme`. See sj-theme's README.

## Golden rules

1. **Reuse before building.** Grep for the existing pattern first (`sj-card`, an existing
   landing, an existing day page) and match it. Don't invent new components or styles.
2. **Scope custom tweaks, never touch globals.** If one place needs a unique look, add a
   modifier class or id and style that (e.g. `.sj-cards--compact`). Editing `.sj-card` /
   `.md-header` / etc. directly breaks every other instance across the site.
3. **Build before you're done:** `mkdocs build --strict` must pass with no warnings.
4. **Jen commits.** Don't run git commits or pushes. Leave staging and commit messages to Jen.
5. **Keep this doc current.** If you introduce a new element, pattern, or system, document it
   here in the same pass, and flag whether it should be ported to the sibling repos. This file
   is only useful if it stays true.

## Writing in Jen's voice (drafts she will "jenify")

Applies to anything public-facing written as Jen: page copy, intros, tile descriptions. (Not
agent docs like this one, and not the AI-assisted learning notes, which are tagged as such.)

- **No em dashes. Ever.** Use commas, brackets, or full stops.
- **No AI-speak / LLM tics.** Avoid: "Honestly?", "at the intersection of", "spearheaded", the
  "it's not X, it's Y" antithesis, "delve", "leverage", "seamless", "testament to", "it's worth
  noting", "in today's world", rhetorical "But here's the thing", and the tidy rule-of-three
  cadence. Write like a person, not a landing page.
- **No bold or italics.** Leave `**bold**` and `_italics_` out. Jen adds emphasis herself.
- **Match her tone first.** Before drafting, read `docs/index.md` and a couple of recent pages
  under `docs/days/` to catch her wording, rhythm and humour.
- **Draft, don't finalise.** Assume she rewrites every line. Keep it plain and short.

## Page skeleton (every content page)

    # :material-ICON: Page Title

    One or two intro sentences.

    ---

    ...content...

- H1 always opens with a `:material-…:` icon.
- Always put a **`---`** after the intro, before the first section. (Jen shouldn't have to add
  it every time.)
- Blue lead-in under the title: `_text_{ .sj-lead }`.

## Exercise pages (the day pages)

Code is **never pasted into the markdown**. Pages pull the real source file in via
`pymdownx.snippets`, so the repo stays the single source of truth:

    # :material-language-python: Tip Calculator

    _Day 2 - split a bill and its tip between diners._{ .sj-lead }

    ```python
    --8<-- "day_002/tip-calculator.py"
    ```

- `snippets.base_path` is the **repo root**, so the include path is the real one
  (`day_012/is_prime.py`), not a docs-relative path.
- `check_paths: true` is on, so a wrong path fails the build rather than rendering blank.
- Exercise source lives in `day_0NN/` at the repo root; the page lives in
  `docs/days/day-NN-slug.md`. Edit the `.py`, not a copy.

## Learning notes

- The note bodies live in `learning-notes/` at the **repo root** and are pulled into
  `docs/learning-notes/*.md` with the same `--8<--` snippet mechanism.
- Every AI-assisted note opens with the banner, so it's clear what's a study aid and not
  Jen's own writing:

      !!! note "AI-assisted"
          Drafted with AI while I studied - tagged so it's clear it's a study aid, not my own writing.

- The nav nests these under a collapsible "Learning Notes (AI-assisted)" group. A "Jen-written"
  group alongside it is planned.

## Tiles

Use the `sj-cards` grid + `sj-card` tiles, never a bespoke card.

    <div class="sj-cards" markdown>

    <a class="sj-card" href="URL/" markdown="span">
    <span class="sj-card-icon">:material-ICON:</span>
    <span class="sj-card-title">Title</span>
    <span class="sj-card-desc" title="Full text, shown on hover.">Short desc (2 lines max).</span>
    <span class="sj-card-meta">meta <span class="sj-dot">·</span> chip</span>
    </a>

    </div>

- Tile `href` is the **final directory URL** (`.../slug/`, trailing slash). Raw HTML isn't
  rewritten by mkdocs, so don't use the `.md` path.
- **Compact / index tiles** (icon + title only): add the `sj-cards--compact` modifier to the
  grid. Narrower, same height. Feature tiles with descriptions stay plain `sj-cards`.
- `sj-card-desc` and `sj-card-meta` are optional. Omit them for title-only tiles.

## Typography

- **Non-breaking hyphen** `&#8209;` for compounds that must not split: AI&#8209;assisted,
  write&#8209;ups.
- **Non-breaking space** `&nbsp;` to bind a short connector word to the next so it can't wrap
  alone: `The&nbsp;Days`, `Getting&nbsp;Started`. Only small words (the, a, of, to, and…),
  never glue long words together (it overflows the narrow tiles).

## Landings

- A nav section with an `index.md` as its **first child** renders as a grey clickable landing
  (Material `navigation.indexes`); a pure grouping with no index stays a white label.
- Landings here are plain pages: intro, `---`, then a `sj-cards` grid. See `docs/index.md`,
  `docs/days/index.md`, `docs/learning-notes/index.md`.
- This repo has **no** no-left-nav "doors" landing. The `cybersecurity` repo does it with an
  `overrides/home.html` template plus `template: home.html` front matter. If one is ever wanted
  here, port that template rather than writing a new one.

## Editing safety (this drive silently truncates long lines)

- The in-app editor truncates long single lines when saving to this drive. **Edit long lines in
  VS Code** (native, safe) or write them via the shell. Don't trust the in-app editor for a
  long line.
- **Always end files with a trailing newline.** A no-newline final line is the one most likely
  to get chopped.
- One editor per file at a time. Concurrent saves have collided and corrupted content.

## Local dev & deploy

    pip install "mkdocs-material>=9.7,<10" "pymdown-extensions>=10,<11"
    mkdocs serve            # live-reload dev server (dev_addr in mkdocs.yml: 127.0.0.1:8002)

- The three sites use different ports so they can run side by side: cybersecurity `8001`,
  this repo `8002`.
- `extra.css` / `extra.js` changes hot-reload (hard-refresh, Ctrl/Cmd+Shift+R, if a JS change
  seems cached). `mkdocs.yml`, templates and new pages need a **serve restart**.
- Deploy is automatic: `.github/workflows/deploy.yml` runs `mkdocs gh-deploy --force` on every
  push to `main`. Just push. The workflow pins mkdocs-material 9.x and pymdown-extensions 10.x
  (material 2.0 rewrote the theming system and would break the overrides), so keep those in
  sync locally.

## Jen's working preferences

- **Tone with Jen:** warm, friendly, a bit playful. Concise and direct, cut filler.
- **Fix typos proactively** (standing permission), unless you're unsure of the intended word,
  then ask.
- **Verify before claiming done.** When you can't see the rendered result, say so and ask her
  to check. Don't claim a visual fix works if you haven't verified it. She values the honesty.
- **Root cause over guess-and-check.** She wants to know *why* something broke, not just that
  it's fixed. One change at a time, explained.
- She pastes screenshots (often with DevTools). Use them.
- When you stop to ask (question tool), wait for her reply. Don't go ahead with changes without
  giving her a chance to answer.

## Commit messages

Follow **Conventional Commits**:

    <type>: <imperative summary>

Examples: `exercise: add Tip Calculator`, `project: add Malware Race`, `docs: add README`,
`fix: correct output formatting in Tip Calculator`, `chore: update .gitignore`.

Rules: imperative mood ("add" not "added"), subject under 72 characters, lowercase everything
including names and exercise titles, one logical change per commit.

Type reference: `exercise` (new exercise file from the course), `project`, `docs` (README or
documentation), `fix` (bug fix or correction), `notes` (personal notes or reflections),
`chore` (config, tooling, maintenance), `refactor` (restructuring without behaviour change),
`style` (visual/CSS only).

## Theme internals

The theme is `docs/stylesheets/extra.css` (authoritative) and `docs/javascripts/extra.js`,
shared with the sibling repos. It took many rounds of pixel-tuning, so be surgical. Keep any
change that isn't repo-specific in sync across all three.

**Palette (CSS vars in `:root`):**

    --sj-bg #080b13   --sj-bg-deep #04060a   --sj-surface #141b2b   --sj-border #232d40
    --sj-blue #1e88ff --sj-gold #f2c14e      --sj-text #b9c3d2       --sj-text-dim #78839a
    --sj-heading #dee5f0

Fonts: **Inter** (text), **JetBrains Mono** (code), **Space Grotesk** (accents/titles).
Headings h3/h4 `#d8bd7e`, h5 `#cbb277` (pale gold); tooltip text `#e6cf94`.

**Header:** one uniform full-width bottom line (`.md-header::before`) plus a faint faded brand
separator (`.sj-brand::after`), identical across the site. (The `cybersecurity` repo adds a
`.sj-home` rule to hide the nav-column divider on its no-nav landing; not needed here.)

**Custom JS systems (`extra.js`):** themed tooltips (native `title` to `data-sj-tip`, styled via
`::after/::before`; variants `sj-tip--up`, `sj-tip--left`); night-mode toggle (warm sepia
`feColorMatrix` filter, saved to `localStorage`); a contained scroller (on desktop the page
scrolls inside `.md-container`, not `window`, so scroll-spy and back-to-top account for that);
gold active-nav bar; sidebar feather via `mask-image`; phantom-line trim for code
blocks; a cursor-following card tooltip (`.sj-cursor-tip`, driven by `data-sj-cardtip`) that
shows a clipped tile's full text on hover.

**Hard-won gotchas (don't re-learn these):**

- The code copy button is `<button class="md-code__button" data-md-type="copy">` (not
  `.md-clipboard`), and its icon is drawn with its own `::after` + `mask-image`. You **cannot**
  put `data-sj-tip` on it (the tooltip's `::after` would erase the icon). Wrap it in
  `<span class="sj-tip-wrap">` instead; the JS dedupe flag is `data-sj-wrapped`, not
  `data-sj-tip`, for the same reason.
- `opacity < 1` on hover creates a stacking context that trapped header tooltips behind the
  header line. Material's `.md-source:hover{opacity:.7}` and
  `.md-header__button:hover{opacity:.7}` are overridden to `opacity:1`.
- `.md-source` (the GitHub link) is given `height: 2rem; display: flex` so its tooltip lines up
  with the other header icons.
- Material's `.md-dialog` (the bottom "Copied to clipboard" snackbar) is hidden. We show our own
  themed feedback on the copy button instead.
- `content.tooltips` is intentionally NOT enabled, so plain `title` attrs are converted in JS
  (otherwise the ugly native browser tooltip shows). The search input's `required` attr is
  stripped in JS to kill the browser "please fill in this field" popup.
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       