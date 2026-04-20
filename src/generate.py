"""
Eco Natural static site generator.
Run from repo root:  python src/generate.py
"""

import csv
import importlib.util
import json
import sys
from pathlib import Path

ROOT       = Path(__file__).parent.parent
IMG_DIR    = ROOT / "img"
DERIVED_IMG_DIR = ROOT / "generated" / "img"

sys.path.insert(0, str(Path(__file__).parent))

from enrichment import ENRICHMENT, _category
from image_assets import resolved_asset
from templates import page_template, index_template, Ctx
from styles import CSS_SITE

LOCALES = [
    ("en", ROOT,         ROOT / "data" / "ids.csv"),
    ("tr", ROOT / "tr",  ROOT / "data" / "ids_tr.csv"),
    ("ru", ROOT / "ru",  ROOT / "data" / "ids_ru.csv"),
]
BASE_URL = ""


def load_locale_strings(locale: str) -> dict:
    """Load locale-specific strings from JSON file."""
    path = ROOT / "locales" / f"{locale}.json"
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_locale_enrichment(locale: str) -> dict:
    """Load locale-specific enrichment data."""
    if locale == "en":
        return ENRICHMENT
    path = ROOT / "locales" / f"enrichment_{locale}.py"
    spec = importlib.util.spec_from_file_location(f"enrichment_{locale}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, f"ENRICHMENT_{locale.upper()}")


def main() -> None:
    # Write style.css once (shared across all locales)
    (ROOT / "style.css").write_text(CSS_SITE, encoding="utf-8")

    # Loop through each locale
    for locale, output_dir, csv_path in LOCALES:
        # Create output directory
        output_dir.mkdir(parents=True, exist_ok=True)

        # Load locale-specific data
        strings = load_locale_strings(locale)
        enrichment = load_locale_enrichment(locale)

        # Create context object
        ctx = Ctx(
            locale=locale,
            strings=strings,
            enrichment=enrichment,
            is_subdir=(locale != "en")
        )

        # Read CSV for this locale
        products: list[dict] = []
        with csv_path.open(newline="", encoding="utf-8") as fh:
            for row in csv.DictReader(fh):
                products.append(dict(row))

        # Group by category
        by_category: dict[str, list] = {}
        for row in products:
            slug  = row["slug"].strip()
            title = row["page_title"].strip()
            pid   = row["product_id"].strip()
            by_category.setdefault(_category(pid), []).append((f"{slug}.html", title, pid))

        # Generate product pages
        index_items: list[tuple[str, str, str]] = []
        for row in products:
            slug       = row["slug"].strip()
            page_title = row["page_title"].strip()
            product_id = row["product_id"].strip()
            filename   = f"{slug}.html"
            cat        = _category(product_id)
            related    = [(fn, t, pid) for fn, t, pid in by_category.get(cat, []) if pid != product_id]
            (output_dir / filename).write_text(
                page_template(row, related=related, img_dir=IMG_DIR, ctx=ctx),
                encoding="utf-8",
            )
            index_items.append((filename, page_title, product_id))

        # Generate index page
        index_items.sort(key=lambda x: x[0])
        (output_dir / "index.html").write_text(
            index_template(index_items, enrichment_map=enrichment, img_dir=IMG_DIR, ctx=ctx),
            encoding="utf-8",
        )

        # Check for missing images
        missing = [pid for _, _, pid in index_items if not (ROOT / resolved_asset(pid)[0]).exists()]

        print(f"[{locale.upper()}] Generated {len(index_items)} pages → {output_dir}")
        if missing:
            print("  Missing images:")
            for img in missing:
                print(f"    - {img}")

    print(f"\nAll locales complete. style.css → {ROOT / 'style.css'}")


if __name__ == "__main__":
    main()
