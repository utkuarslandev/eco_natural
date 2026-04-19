"""
Eco Natural static site generator.
Run from repo root:  python src/generate.py
"""

import csv
import sys
from pathlib import Path

ROOT       = Path(__file__).parent.parent
CSV_PATH   = ROOT / "data" / "ids.csv"
IMG_DIR    = ROOT / "img"
DERIVED_IMG_DIR = ROOT / "generated" / "img"
OUTPUT_DIR = ROOT

sys.path.insert(0, str(Path(__file__).parent))

from enrichment import ENRICHMENT, _category
from image_assets import resolved_asset
from templates import page_template, index_template
from styles import CSS_PRODUCT


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

    (OUTPUT_DIR / "style.css").write_text(CSS_PRODUCT, encoding="utf-8")

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
