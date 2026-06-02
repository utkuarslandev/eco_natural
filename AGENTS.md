# Repository Guidelines

## Project Structure & Module Organization

This repository is a Python static-site generator for a multilingual product catalog. Edit generator sources under `src/`: `generate.py` orchestrates builds, `html/` renders pages, `css/` composes the stylesheet, and `enrichment.py` holds canonical English product content. Locale UI strings live in `locales/{en,tr,ru}.json`; translated enrichment is in `locales/enrichment_{tr,ru}.py`. Product metadata is stored in `data/ids*.csv`, with image adjustments in `data/image_adjustments.json`.

Generated artifacts are committed: root and locale HTML files (`*.html`, `tr/`, `ru/`), `style.css`, and optimized card images under `generated/img/cards/`. Source images belong in `img/`.

## Build, Test, and Development Commands

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 src/generate.py
python3 src/validate.py
python3 -m http.server 8000
```

`generate.py` rebuilds all EN/TR/RU pages, shared CSS, and responsive card images. `validate.py` checks locale key parity, product IDs and slugs, enrichment coverage, assets, generated page counts, local links, and forbidden tokens. The HTTP server is optional for browser review. Install `requirements-image.txt` only for background-removal work.

## Coding Style & Naming Conventions

Use Python 3.8+ conventions: four-space indentation, type hints where they clarify interfaces, `snake_case` for functions and variables, and `UPPER_CASE` for constants. Keep renderers small and place shared HTML in `src/html/components.py`; place CSS in the matching `src/css/` module. Preserve identical product slugs and IDs across locales. Update all three translations together when changing user-facing text.

## Testing Guidelines

There is no separate unit-test suite or coverage threshold. Before submitting changes, run:

```bash
python3 src/generate.py
python3 src/validate.py
git status --short
```

Review the regenerated diff and spot-check affected pages in each locale. For visual changes, include screenshots of desktop and mobile layouts.

## Commit & Pull Request Guidelines

Follow the existing concise, imperative commit style: `Fix hero CSS regression for index page`, `Add dependency manifests`, or `Update homepage design and product styling`. Keep source changes and their regenerated artifacts in the same commit. Pull requests should summarize the affected content or UI, list verification commands, link any issue, and attach screenshots for visible changes.
