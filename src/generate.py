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
    products: list[dict] = []
    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            products.append(dict(row))

    by_category: dict[str, list] = {}
    for row in products:
        slug  = row["slug"].strip()
        title = row["page_title"].strip()
        pid   = row["product_id"].strip()
        by_category.setdefault(_category(pid), []).append((f"{slug}.html", title, pid))

    (OUTPUT_DIR / "style.css").write_text(CSS_SITE, encoding="utf-8")

    index_items: list[tuple[str, str, str]] = []
    for row in products:
        slug       = row["slug"].strip()
        page_title = row["page_title"].strip()
        product_id = row["product_id"].strip()
        filename   = f"{slug}.html"
        cat        = _category(product_id)
        related    = [(fn, t, pid) for fn, t, pid in by_category.get(cat, []) if pid != product_id]
        (OUTPUT_DIR / filename).write_text(
            page_template(row, related=related, img_dir=IMG_DIR),
            encoding="utf-8",
        )
        index_items.append((filename, page_title, product_id))

    index_items.sort(key=lambda x: x[0])
    (OUTPUT_DIR / "index.html").write_text(
        index_template(index_items, enrichment_map=ENRICHMENT, img_dir=IMG_DIR),
        encoding="utf-8",
    )

    missing   = [pid for _, _, pid in index_items if not (ROOT / resolved_asset(pid)[0]).exists()]

    print(f"Generated {len(index_items)} product pages + index.html + style.css → {OUTPUT_DIR}")
    if missing:
        print("Missing images:")
        for img in missing:
            print(f"  - {img}")
    else:
        print("All product images found.")


if __name__ == "__main__":
    main()
