# skyejen / python

Python portfolio and learning write-ups, part of **[skyejen.github.io](https://skyejen.github.io)**. Apps and projects, plus learning notes and the 100 Days of Code course.

Live at **https://skyejen.github.io/python**

## Local development

This site shares a design system with my other repos via the `sj-theme` git submodule.

```bash
git clone https://github.com/skyejen/python.git
cd python
git submodule update --init            # pull in sj-theme
pip install "mkdocs-material>=9.7,<10" "pymdown-extensions>=10,<11"
mkdocs serve                           # http://127.0.0.1:8002
```

## Structure

- `docs/portfolio/` — Python apps & projects
- `docs/learning/` — learning notes and the 100 Days of Code course
- `day_00X/` — course exercise source (embedded into the learning pages)
- `docs/sj-theme/` — shared theme (git submodule)
- `overrides/` — theme customisations

Deploys automatically to GitHub Pages on push to `main` (see `.github/workflows/deploy.yml`).
