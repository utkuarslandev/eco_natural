# Development Workflows

Standard workflows for maintaining and updating the Eco Natural site.

## Setup & Installation

### Initial Setup

```bash
# Clone repository
git clone https://github.com/utkuarslandev/eco_natural.git
cd eco_natural

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Optional: install only when regenerating transparent product cutouts
pip install -r requirements-image.txt

# Verify setup works
python3 src/generate.py
```

### Verify Installation

```bash
# Check Python version (should be 3.8+)
python3 --version

# Check dependencies
python3 -m pip show Pillow

# Test generator
python3 src/generate.py
# Should output:
# [EN] Generated 28 pages → /path/to/eco_natural
# [TR] Generated 28 pages → /path/to/eco_natural/tr
# [RU] Generated 28 pages → /path/to/eco_natural/ru
```

---

## Content Updates

### Editing Product Information

When updating product details (name, description, images):

```bash
# 1. Edit English source
nano data/ids.csv
# Change: page_title, short_description, full_description, seo_title, meta_description

# 2. Update Turkish version
nano data/ids_tr.csv
# Translate the same columns

# 3. Update Russian version
nano data/ids_ru.csv
# Translate the same columns

# 4. Regenerate pages
python3 src/generate.py

# 5. Verify output
grep "Updated Title" *.html
grep "Updated Title" tr/*.html
grep "Updated Title" ru/*.html

# 6. Commit
git add data/ids*.csv
git commit -m "Update product information"
git push
```

### Editing Product Stories & Enrichment

When updating product stories, taglines, badges, or how-to-use:

```bash
# 1. Edit English enrichment
nano src/enrichment.py
# Update: story, tagline, how_to_use, badges, product_line

# 2. Update Turkish enrichment
nano locales/enrichment_tr.py
# Translate all text fields

# 3. Update Russian enrichment
nano locales/enrichment_ru.py
# Translate all text fields

# 4. Regenerate
python3 src/generate.py

# 5. Verify (check for your product in generated pages)
grep -l "PRODUCT_NAME" tr/*.html | head -1 | xargs grep "story content"

# 6. Commit
git add src/enrichment.py locales/enrichment*.py
git commit -m "Update product enrichment for [product name]"
git push
```

### Updating UI Text & Navigation

When changing button labels, section headings, etc.:

```bash
# 1. Edit English strings
nano locales/en.json
# Update: back_link, learn_more, origin_story_eyebrow, etc.

# 2. Update Turkish strings
nano locales/tr.json
# Translate same keys

# 3. Update Russian strings
nano locales/ru.json
# Translate same keys

# 4. Regenerate
python3 src/generate.py

# 5. Verify (check for your new text in pages)
grep "New Button Text" index.html
grep "Turkish Translation" tr/index.html
grep "Russian Translation" ru/index.html

# 6. Commit
git add locales/*.json
git commit -m "Update UI text: [description]"
git push
```

### Updating Styles & CSS

When modifying layout, colors, or fonts:

```bash
# 1. Edit CSS definitions
nano src/css/product.py
# Modify: CSS_PRODUCT or CSS_INDEX sections

# 2. Regenerate (re-compiles CSS)
python3 src/generate.py

# 3. Verify (check generated style.css)
grep "new-style-name" style.css

# 4. View in browser
# Open index.html, tr/index.html, ru/index.html in browser
# Check that styles apply correctly across all pages

# 5. Commit
git add src/css src/styles.py style.css
git commit -m "Update styles: [description]"
git push
```

---

## Adding a New Product

### Complete Workflow

```bash
# 1. Prepare image
# Place product image at: img/BRD_XXXX.JPG (or your naming convention)
# Recommended: ~1600×1600px, PNG or JPG

# 2. Add to English CSV (data/ids.csv)
# Format: filename,product_id,page_title,slug,short_description,full_description,seo_title,meta_description

# Example:
# BRD_9999.JPG,EN-NEW-OIL-250ML,"Eco Natural New Product – 250 ml","eco-natural-new-oil-250ml","A description of the new product","Full description here...","Eco Natural New Product 250 ml","Meta description for search"

# You can use a text editor or command line:
cat >> data/ids.csv << 'EOF'
BRD_9999.JPG,EN-NEW-OIL-250ML,"Eco Natural New Product – 250 ml","eco-natural-new-oil-250ml","A smooth oil with unique properties","This product combines...","Eco Natural New Product 250 ml | Premium Oil","Shop the new Eco Natural oil with unique properties and premium quality"
EOF

# 3. Add to Turkish CSV (data/ids_tr.csv)
# Same product_id and slug, but translate columns 3-8

# 4. Add to Russian CSV (data/ids_ru.csv)
# Same product_id and slug, but translate columns 3-8

# 5. Add to English enrichment (src/enrichment.py)
cat >> src/enrichment.py << 'EOF'

    "EN-NEW-OIL-250ML": {
        "origin_place": "Aegean Turkey",
        "story": [
            "First paragraph describing the product heritage and origin...",
            "Second paragraph describing taste, characteristics, and uses..."
        ],
        "how_to_use": [
            ("🥗", "Salads"),
            ("🍞", "Bread"),
            ("🍝", "Pasta"),
            ("🫙", "Finishing"),
            ("🧀", "Cheese"),
            ("🍳", "Cooking")
        ],
        "badges": [
            ("❄️", "Cold Pressed", "No heat — full flavor preserved"),
            ("🌱", "Plant-Based", "100% plant origin"),
            ("🚫", "No Additives", "Clean label"),
            ("📍", "Turkish Origin", "Made in Turkey"),
            ("⭐", "Premium", "Highest quality tier")
        ],
        "product_line": "Eco Natural New Oils · 250 ml",
        "tagline": "A concise marketing line describing the unique qualities",
        "is_gift": False
    }
EOF

# 6. Add to Turkish enrichment (locales/enrichment_tr.py)
# Same structure, translate all text fields

# 7. Add to Russian enrichment (locales/enrichment_ru.py)
# Same structure, translate all text fields

# 8. Regenerate
python3 src/generate.py

# 9. Verify new product pages exist
ls -la *.html | grep new-oil
ls -la tr/*.html | grep new-oil
ls -la ru/*.html | grep new-oil

# 10. Check product is on homepage
grep "New Product" index.html
grep "Turkish Title" tr/index.html

# 11. Commit
git add .
git commit -m "Add new product: Eco Natural New Oil

- Add product to all three languages (en/tr/ru)
- Include full enrichment data (stories, badges, taglines)
- Update category listings
- Verify pages generated correctly

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>"

# 12. Push
git push origin main
```

### Checklist for New Products

- [ ] Image placed at `img/BRD_XXXX.JPG`
- [ ] Row added to `data/ids.csv` (English)
- [ ] Row added to `data/ids_tr.csv` (Turkish, translated)
- [ ] Row added to `data/ids_ru.csv` (Russian, translated)
- [ ] Entry added to `src/enrichment.py` (English)
- [ ] Entry added to `locales/enrichment_tr.py` (Turkish, translated)
- [ ] Entry added to `locales/enrichment_ru.py` (Russian, translated)
- [ ] Generator run: `python3 src/generate.py`
- [ ] New product pages verified in `*.html`, `tr/*.html`, `ru/*.html`
- [ ] Product appears on homepage in all three languages
- [ ] Changes committed and pushed

---

## Deploying the Site

### To GitHub Pages

```bash
# Commit and push
git add -A
git commit -m "Update content"
git push origin main

# GitHub Pages auto-publishes from main branch
# Pages available at: https://utkuarslandev.github.io/eco_natural
```

### To AWS S3 + CloudFront

```bash
# Configure AWS credentials
aws configure

# Sync all files to S3 bucket
aws s3 sync . s3://your-bucket-name/ \
  --delete \
  --exclude ".git/*" \
  --exclude ".venv/*" \
  --exclude "*.pyc" \
  --exclude "__pycache__/*"

# Invalidate CloudFront cache
aws cloudfront create-invalidation \
  --distribution-id YOUR_DIST_ID \
  --paths "/*"
```

### To Netlify

```bash
# Connect repo to Netlify via web interface
# Settings:
#   - Build command: (none, or just "echo done")
#   - Publish directory: .

# Netlify auto-deploys on push to main
```

### To Any Web Server (rsync)

```bash
# Sync to remote server
rsync -avz \
  --delete \
  --exclude ".git" \
  --exclude ".venv" \
  --exclude ".gitignore" \
  . user@server:/var/www/eco-natural/

# Set permissions
ssh user@server "chmod -R 755 /var/www/eco-natural"
```

---

## Maintenance Tasks

### Weekly: Content Review

```bash
# Check for broken links in generated HTML
grep -h 'href=' *.html tr/*.html ru/*.html | grep -v 'http' | sort | uniq

# Verify all images are present
python3 -c "
import re
from pathlib import Path
htmls = list(Path('.').glob('*.html')) + list(Path('.').glob('*/*.html'))
for html in htmls:
    imgs = re.findall(r'src=\"([^\"]+)\"', html.read_text())
    for img in imgs:
        if not Path(img).exists() and not img.startswith('http'):
            print(f'{html}: Missing {img}')
"
```

### Monthly: Content Audit

```bash
# Check that all locales have matching content
echo "English products:"
grep -c 'class="product-card"' index.html

echo "Turkish products:"
grep -c 'class="product-card"' tr/index.html

echo "Russian products:"
grep -c 'class="product-card"' ru/index.html

# Should all be 28 (same count)
```

### Before Major Release

```bash
# Full regeneration from source
python3 src/generate.py

# Validate all HTML files
python3 -c "
from pathlib import Path
import re
for html in Path('.').glob('**/*.html'):
    content = html.read_text()
    if not re.search(r'<html[^>]*lang=', content):
        print(f'{html}: Missing lang attribute')
    if not re.search(r'<meta name=\"description\"', content):
        print(f'{html}: Missing meta description')
"

# Check Git status is clean
git status

# Create signed commit/tag
git tag -a v$(date +%Y.%m.%d) -m "Release $(date)"
git push origin main --tags
```

---

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'enrichment'"

**Solution:**
```bash
# Make sure you're running from the repo root
cd /path/to/eco_natural

# Activate virtual environment
source .venv/bin/activate

# Run generator from repo root
python3 src/generate.py
```

### Issue: Pages not regenerating after edits

**Solution:**
```bash
# Delete generated HTML files and regenerate
rm *.html tr/*.html ru/*.html
python3 src/generate.py

# Verify files were recreated
ls -la *.html | wc -l  # Should show 29
```

### Issue: Images not showing in generated pages

**Solution:**
```bash
# Verify image exists
ls -la img/BRD_*.JPG

# Check image is referenced correctly in CSV
grep "BRD_XXXX" data/ids.csv

# Regenerate and check generated HTML
python3 src/generate.py
grep "src=\"img/" index.html | head -3

# Verify path prefix is correct for locale
grep "src=\"../img/" tr/index.html | head -3  # TR should use ../
```

### Issue: Git push fails

**Solution:**
```bash
# Check branch status
git status
git log --oneline -5

# Ensure you're on main
git branch -v

# Pull latest changes first
git pull origin main

# Then push
git push origin main
```

---

## Git Workflow

### Standard Commit Message Format

```
Short summary (under 70 chars)

Detailed explanation of what changed and why. Mention:
- What was updated (product names, UI strings, etc.)
- Why the change was needed (typo fix, translation update, etc.)
- Any affected locales (en/tr/ru)

Co-Authored-By: Claude Haiku 4.5 <noreply@anthropic.com>
```

### Example Commits

```
# Product update
git commit -m "Update Hemp Seed Oil product information

- Update English description in ids.csv
- Translate to Turkish and Russian
- Regenerate pages for all three locales
- Verify product appears correctly on homepage"

# Translation update
git commit -m "Add Russian translations for new UI strings

- Add 5 new keys to locales/ru.json
- Update corresponding Turkish translations
- Regenerate all pages
- Verify translations appear in generated HTML"

# Content addition
git commit -m "Add new product: Eco Natural Avocado Oil

- Add avocado oil to all three locales (en/tr/ru)
- Include full product enrichment (stories, badges)
- Add to product CSV and category listings
- Verify product pages generate and appear on homepage"
```

### Branching Strategy

For major features, use feature branches:

```bash
# Create feature branch
git checkout -b feature/add-new-products
# ... make changes ...
git push origin feature/add-new-products

# Create pull request on GitHub
# After review, merge to main
git checkout main
git pull origin main
git merge feature/add-new-products
git push origin main
```

---

## Monitoring & Analytics

### Check Site Health

```bash
# Verify all 87 pages exist
find . -name "*.html" | grep -v ".venv" | wc -l  # Should be 87

# Check for broken links
grep -h 'href=' *.html tr/*.html ru/*.html | \
  grep -v 'http' | \
  sed 's/.*href="\([^"]*\)".*/\1/' | \
  sort | uniq > links.txt

# Verify each link exists
while read link; do
  [ ! -f "$link" ] && echo "Broken: $link"
done < links.txt
```

### Monitor Translation Completeness

```bash
# Count translated strings
echo "EN strings: $(jq 'keys | length' locales/en.json)"
echo "TR strings: $(jq 'keys | length' locales/tr.json)"
echo "RU strings: $(jq 'keys | length' locales/ru.json)"

# All should be equal
```

---

For additional help, see:
- **[README.md](./README.md)** — Project overview
- **[I18N.md](./I18N.md)** — Internationalization guide
- **[design-system.md](./design-system.md)** — Design documentation
