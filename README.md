# Eco Natural — Lasting Taste of Earth

A premium artisan food product website for Eco Natural, a Turkish village-origin producer of cold-pressed oils, extracts, and specialty foods. Built as a static site with comprehensive internationalization support for English, Turkish, and Russian markets.

**Live Site:** [eco-natural.com](https://eco-natural.com)  
**Repository:** [utkuarslandev/eco_natural](https://github.com/utkuarslandev/eco_natural)

---

## Overview

This is a **Python-based static site generator** that creates a fully-localized e-commerce catalog website. It combines elegant design, performance optimization, and multi-language support.

### Key Features

- **🌍 Multilingual** — English, Turkish, Russian with complete translations
- **⚡ Static Site** — No server required, fast CDN-friendly delivery
- **🎨 Premium Design** — Elegant typography, sophisticated visual hierarchy
- **📱 Responsive** — Mobile-first, works across all devices
- **🔍 SEO-Ready** — Meta tags, structured data (JSON-LD), hreflang alternates
- **🛍️ Product Catalog** — 28 artisan products across 8 categories
- **🌐 Localized URLs** — `/en/`, `/tr/`, `/ru/` with identical slugs

---

## Project Structure

```
eco_natural/
├── src/                          # Python source code
│   ├── generate.py              # Main static site generator
│   ├── templates.py             # HTML template functions
│   ├── enrichment.py            # Product content (English)
│   ├── image_assets.py          # Image handling & optimization
│   ├── styles.py                # CSS definitions
│   └── ...other modules
├── locales/                      # Internationalization files
│   ├── en.json                  # English UI strings (44 keys)
│   ├── tr.json                  # Turkish UI strings
│   ├── ru.json                  # Russian UI strings
│   ├── enrichment_tr.py         # Turkish product content (29 products)
│   └── enrichment_ru.py         # Russian product content
├── data/
│   ├── ids.csv                  # English product metadata
│   ├── ids_tr.csv               # Turkish product metadata
│   └── ids_ru.csv               # Russian product metadata
├── img/                          # Original product images
├── generated/                    # Generated image assets
│   └── img/                     # Optimized images, cards
├── style.css                     # Generated stylesheet
├── index.html                    # English homepage
├── [product-slug].html           # English product pages (28)
├── tr/                           # Turkish pages
│   ├── index.html
│   └── [product-slug].html      # 28 product pages
├── ru/                           # Russian pages
│   ├── index.html
│   └── [product-slug].html      # 28 product pages
├── design-system.md             # Design documentation
├── I18N.md                       # Internationalization guide
└── WORKFLOWS.md                  # Development workflows
```

---

## Getting Started

### Prerequisites

- Python 3.8+
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/utkuarslandev/eco_natural.git
cd eco_natural

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Optional: install background-removal tooling for src/process_images.py
pip install -r requirements-image.txt
```

### Generate Site

```bash
# Regenerate all pages for all locales (en/tr/ru)
python3 src/generate.py
```

This creates:
- `/index.html` and 28 product pages in English
- `/tr/index.html` and 28 product pages in Turkish
- `/ru/index.html` and 28 product pages in Russian

---

## File Organization

### Python Source Code (`src/`)

| File | Purpose |
|------|---------|
| `generate.py` | Main generator; loops through locales, creates pages |
| `templates.py` | HTML template functions for pages; uses `Ctx` for translations |
| `enrichment.py` | Product content (stories, badges, taglines) — English source |
| `image_assets.py` | Image path resolution, optimization metadata |
| `styles.py` | CSS definitions (inline in Python) |
| `process_images.py` | Image processing utilities |
| `remove_bg.py` | Background removal for product photos |

### Locale Files (`locales/`)

| File | Purpose |
|------|---------|
| `en.json` | 44 UI strings (navigation, CTAs, labels) in English |
| `tr.json` | Turkish UI strings (same keys as en.json) |
| `ru.json` | Russian UI strings |
| `enrichment_tr.py` | Turkish product enrichment (29 products) |
| `enrichment_ru.py` | Russian product enrichment |

**Note:** `enrichment.py` is the source of truth for English product content. Turkish and Russian versions in `locales/` override specific fields.

### Data Files (`data/`)

| File | Purpose |
|------|---------|
| `ids.csv` | English: product metadata (page title, description, slugs, etc.) |
| `ids_tr.csv` | Turkish: same structure, translated metadata |
| `ids_ru.csv` | Russian: same structure, translated metadata |

**CSV Columns:**
- `filename` — Image file (non-translated)
- `product_id` — Product ID (non-translated)
- `page_title` — Product name shown on page
- `slug` — URL slug (non-translated; same across locales)
- `short_description` — One-line summary
- `full_description` — Multi-sentence description
- `seo_title` — Page `<title>` tag
- `meta_description` — Page meta description

---

## How It Works

### Generation Flow

```
generate.py (main loop)
  ↓
For each locale (en, tr, ru):
  ├─ Load locale strings (locales/{locale}.json)
  ├─ Load product enrichment (enrichment.py or enrichment_{locale}.py)
  ├─ Read CSV (data/ids_{locale}.csv or ids.csv for en)
  ├─ Create Ctx object (locale context for translations)
  │
  ├─ For each product:
  │   └─ Call page_template(..., ctx) → Write {slug}.html
  │
  └─ Call index_template(..., ctx) → Write index.html
```

### Template Context (`Ctx`)

All templates receive a `Ctx` dataclass containing:

```python
@dataclass
class Ctx:
    locale: str              # "en", "tr", or "ru"
    strings: dict            # Loaded from locales/{locale}.json
    enrichment: dict         # Product content (localized)
    is_subdir: bool          # True for tr/ and ru/ pages
    
    def t(key: str, **fmt)   # Translate: ctx.t("back_link")
    def asset_prefix()       # Path prefix: "./" for en, "../" for tr/ru
```

### URL Structure

All product pages use **identical slugs** across locales:

```
/eco-natural-hemp-seed-oil-250ml.html          (English)
/tr/eco-natural-hemp-seed-oil-250ml.html       (Turkish)
/ru/eco-natural-hemp-seed-oil-250ml.html       (Russian)
```

This makes `hreflang` alternates and cross-language navigation simple.

---

## Internationalization (i18n)

See **[I18N.md](./I18N.md)** for complete i18n documentation.

### Quick Reference

**UI Strings** — 44 translated keys in `locales/{en|tr|ru}.json`:
- Navigation: "All Products", "Back to All Products"
- CTAs: "Order via WhatsApp", "Chat on WhatsApp"
- Section labels: "Origin & Story", "How to Enjoy", "Quality & Standards"
- Meta: "Find Us", "Order Direct"

**Product Content** — Per-product translations in `locales/enrichment_{tr|ru}.py` and `data/ids_{tr|ru}.csv`:
- Stories (2 paragraphs per product)
- Taglines, product lines, origin place
- How-to-use labels (6 usage scenarios)
- Badges (4–5 feature badges per product)

**Language Switcher** — Rendered in topbar; links to same page in other languages.

---

## Development Workflow

See **[WORKFLOWS.md](./WORKFLOWS.md)** for detailed instructions on:

- Regenerating pages after content changes
- Adding new products
- Updating translations
- Modifying templates and styles
- Building and deploying

### Common Tasks

```bash
# Regenerate all pages
python3 src/generate.py

# Check generated files
ls -la *.html tr/ ru/

# View git status
git status

# Commit changes
git add -A
git commit -m "Update product content"

# Push to remote
git push origin main
```

---

## Technical Stack

| Component | Technology |
|-----------|-----------|
| **Generator** | Python 3.8+ |
| **Templates** | Python f-strings (built-in, no deps) |
| **Styling** | CSS 3 (embedded in Python, compiled to style.css) |
| **Images** | Pillow for dimensions and generated WebP card variants |
| **i18n** | JSON + Python dicts (no external i18n lib) |
| **Data** | CSV for product metadata |
| **Hosting** | Static files (GitHub Pages, AWS S3, Netlify, etc.) |

### No External Dependencies

The generator uses only Python standard library. Image optimization uses PIL/Pillow (optional, for processing only).

---

## Performance & SEO

### Optimizations

- **Static HTML** — No database, no server requests; instant delivery
- **Image Optimization** — WebP variants, lazy loading, responsive `srcset`
- **CSS** — Single stylesheet shared across all locales
- **Preload/Prefetch** — Links preloaded for faster navigation
- **Minification-Ready** — Can be minified by CDN or build step

### SEO

- **Meta Tags** — Unique title, description per page and locale
- **Structured Data** — JSON-LD product schema on each product page
- **hreflang** — Language alternates declared for search engines
- **Open Graph** — Social sharing metadata
- **Canonical** — Proper canonicalization across locales

---

## Customization

### Adding a New Product

1. Add row to `data/ids.csv` (English):
   ```csv
   BRD_XXXX.JPG,EN-PRODUCT-ID,"Product Name","slug-name","short desc","long description","SEO Title","meta desc"
   ```

2. Duplicate row to `data/ids_tr.csv` and `data/ids_ru.csv`, translate columns 3–8

3. Add product entry to `src/enrichment.py`:
   ```python
   "EN-PRODUCT-ID": {
       "origin_place": "...",
       "story": ["paragraph 1", "paragraph 2"],
       "how_to_use": [("emoji", "Label"), ...],
       "badges": [("emoji", "Title", "Description"), ...],
       "product_line": "...",
       "tagline": "...",
       "is_gift": False,
   }
   ```

4. Duplicate entry to `locales/enrichment_tr.py` and `locales/enrichment_ru.py`, translate all text

5. Place product image at `img/BRD_XXXX.JPG`

6. Run `python3 src/generate.py`

### Updating UI Text

1. Edit `locales/en.json`, `locales/tr.json`, `locales/ru.json`
2. Update the corresponding string keys (e.g., `"back_link"`, `"learn_more"`)
3. Run `python3 src/generate.py`

### Updating Styles

1. Edit `src/styles.py` (CSS is defined in Python strings)
2. Modify `CSS_PRODUCT` or `CSS_INDEX` sections
3. Run `python3 src/generate.py` — CSS is compiled to `style.css`

---

## Deployment

The generated site is **fully static** and can be deployed anywhere:

### GitHub Pages (Free)

```bash
git push origin main
# Pages auto-publishes from the root directory
```

### AWS S3 + CloudFront

```bash
aws s3 sync . s3://your-bucket/ --exclude ".git/*" --exclude ".venv/*"
```

### Netlify

```bash
# Connect repo, auto-deploys on push
# All generated .html files are served as static assets
```

### Any HTTP Server

```bash
# Copy all files to your web server
scp -r . user@server:/var/www/eco-natural/
```

---

## Maintenance

### Backup & Version Control

- All content is version-controlled in Git
- Product images are tracked (use Git LFS for large binaries if needed)
- Generated HTML files are committed (or gitignored and regenerated on deploy)

### Updating Content

```bash
# Edit data files or translation files
nano data/ids.csv
nano locales/en.json
# Etc.

# Regenerate
python3 src/generate.py

# Commit
git add -A
git commit -m "Update product content"
git push
```

---

## Support & Documentation

- **Design System** — [design-system.md](./design-system.md)
- **Internationalization** — [I18N.md](./I18N.md)
- **Workflows** — [WORKFLOWS.md](./WORKFLOWS.md)
- **GitHub Issues** — [utkuarslandev/eco_natural/issues](https://github.com/utkuarslandev/eco_natural/issues)

---

## License

© 2024 Eco Natural. All rights reserved.

**Trademarked:** "Eco Natural" is a registered trademark. All product names and branding are proprietary.

---

## Contributors

Built and maintained by the Eco Natural team.

Generated with [Claude Code](https://claude.com/claude-code).
