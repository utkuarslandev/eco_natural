from __future__ import annotations

import csv
import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
SRC = ROOT / "src"
sys.path.insert(0, str(SRC))

from enrichment import ENRICHMENT
from image_assets import SCENE_SOURCE_PATHS, resolved_asset

LOCALES = ("en", "tr", "ru")
CSV_FILES = {
    "en": ROOT / "data" / "ids.csv",
    "tr": ROOT / "data" / "ids_tr.csv",
    "ru": ROOT / "data" / "ids_ru.csv",
}
HTML_DIRS = {
    "en": ROOT,
    "tr": ROOT / "tr",
    "ru": ROOT / "ru",
}
FORBIDDEN_TOKENS = (
    "Whats" + "App",
    "whats" + "app",
    "wa" + ".me",
    "btn" + "-wa",
    "sticky" + "-wa",
    "WA" + "_NUMBER",
    "_WA" + "_SVG",
    "_STICKY" + "_WA_JS",
    "900" + "000000000",
)


def fail(message: str) -> None:
    raise SystemExit(f"validate: {message}")


def load_json(path: Path) -> dict:
    try:
        with path.open(encoding="utf-8") as fh:
            return json.load(fh)
    except Exception as exc:
        fail(f"invalid JSON: {path.relative_to(ROOT)} ({exc})")


def load_csv(path: Path) -> list[dict]:
    with path.open(newline="", encoding="utf-8") as fh:
        return [dict(row) for row in csv.DictReader(fh)]


def load_locale_enrichment(locale: str) -> dict:
    if locale == "en":
        return ENRICHMENT
    path = ROOT / "locales" / f"enrichment_{locale}.py"
    spec = importlib.util.spec_from_file_location(f"enrichment_{locale}", path)
    if not spec or not spec.loader:
        fail(f"cannot import {path.relative_to(ROOT)}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return getattr(mod, f"ENRICHMENT_{locale.upper()}")


def validate_locale_keys() -> None:
    strings = {locale: load_json(ROOT / "locales" / f"{locale}.json") for locale in LOCALES}
    base_keys = set(strings["en"])
    base_categories = set(strings["en"].get("categories", {}))
    for locale in ("tr", "ru"):
        keys = set(strings[locale])
        if keys != base_keys:
            fail(f"locale key mismatch for {locale}: missing={sorted(base_keys - keys)} extra={sorted(keys - base_keys)}")
        categories = set(strings[locale].get("categories", {}))
        if categories != base_categories:
            fail(f"category key mismatch for {locale}: missing={sorted(base_categories - categories)} extra={sorted(categories - base_categories)}")


def validate_products() -> dict[str, list[dict]]:
    rows = {locale: load_csv(CSV_FILES[locale]) for locale in LOCALES}
    base_ids = [row["product_id"].strip() for row in rows["en"]]
    base_slugs = {row["product_id"].strip(): row["slug"].strip() for row in rows["en"]}
    if len(base_ids) != len(set(base_ids)):
        fail("duplicate product_id in data/ids.csv")
    for locale in LOCALES:
        ids = [row["product_id"].strip() for row in rows[locale]]
        slugs = [row["slug"].strip() for row in rows[locale]]
        if len(ids) != len(set(ids)):
            fail(f"duplicate product_id in {CSV_FILES[locale].relative_to(ROOT)}")
        if len(slugs) != len(set(slugs)):
            fail(f"duplicate slug in {CSV_FILES[locale].relative_to(ROOT)}")
        if ids != base_ids:
            fail(f"product order/id mismatch for {locale}")
        for row in rows[locale]:
            product_id = row["product_id"].strip()
            if row["slug"].strip() != base_slugs[product_id]:
                fail(f"slug mismatch for {locale}:{product_id}")
    return rows


def validate_enrichment(rows: dict[str, list[dict]]) -> None:
    csv_ids = {row["product_id"].strip() for row in rows["en"]}
    for locale in LOCALES:
        enrichment_ids = set(load_locale_enrichment(locale))
        if enrichment_ids != csv_ids:
            fail(f"enrichment mismatch for {locale}: missing={sorted(csv_ids - enrichment_ids)} extra={sorted(enrichment_ids - csv_ids)}")


def validate_assets(rows: dict[str, list[dict]]) -> None:
    for row in rows["en"]:
        product_id = row["product_id"].strip()
        asset_path, _ = resolved_asset(product_id)
        if not (ROOT / asset_path).exists():
            fail(f"missing resolved asset for {product_id}: {asset_path}")


def iter_html_files() -> list[Path]:
    files: list[Path] = []
    for directory in HTML_DIRS.values():
        files.extend(sorted(directory.glob("*.html")))
    return files


def validate_local_reference(source_file: Path, ref: str) -> None:
    if ref.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#")):
        return
    path = ref.split("#", 1)[0].split("?", 1)[0]
    if path and not (source_file.parent / path).exists():
        fail(f"broken local reference in {source_file.relative_to(ROOT)}: {ref}")


def validate_generated_html(rows: dict[str, list[dict]]) -> None:
    expected_product_count = len(rows["en"])
    for locale, directory in HTML_DIRS.items():
        html_files = sorted(directory.glob("*.html"))
        product_files = [path for path in html_files if path.name != "index.html"]
        if len(product_files) != expected_product_count:
            fail(f"{locale} generated product page count is {len(product_files)}, expected {expected_product_count}")

    attr_pattern = re.compile(r"""(?:href|src)=["']([^"']+)["']""")
    srcset_pattern = re.compile(r"""(?:srcset|imagesrcset)=["']([^"']+)["']""")
    for html_file in iter_html_files():
        text = html_file.read_text(encoding="utf-8")
        if "[MISSING:" in text:
            fail(f"missing translation marker in {html_file.relative_to(ROOT)}")
        for ref in attr_pattern.findall(text):
            validate_local_reference(html_file, ref)
        for srcset in srcset_pattern.findall(text):
            for candidate in srcset.split(","):
                validate_local_reference(html_file, candidate.strip().split(" ", 1)[0])


def validate_optimized_assets() -> None:
    html_files = iter_html_files()
    stylesheet = ROOT / "style.css"
    generated_text = "\n".join(
        [stylesheet.read_text(encoding="utf-8")]
        + [path.read_text(encoding="utf-8") for path in html_files]
    )

    for scene_path in SCENE_SOURCE_PATHS:
        if scene_path in generated_text:
            fail(f"original decorative scene referenced in generated output: {scene_path}")
    if "generated/img/cards/" in generated_text:
        fail("removed generated/img/cards path referenced in generated output")
    if re.search(r"""src=["'](?:\.\./|\./)?logo\.png["']""", generated_text):
        fail("full-size logo.png used as a visible image")

    css_url_pattern = re.compile(r"""url\(["']([^"']+)["']\)""")
    for ref in css_url_pattern.findall(stylesheet.read_text(encoding="utf-8")):
        validate_local_reference(stylesheet, ref)

    for locale, directory in HTML_DIRS.items():
        index_text = (directory / "index.html").read_text(encoding="utf-8")
        high_priority_preloads = re.findall(
            r"""<link rel=["']preload["'][^>]*fetchpriority=["']high["'][^>]*>""",
            index_text,
        )
        if len(high_priority_preloads) != 1:
            fail(f"{locale} homepage high-priority preload count is {len(high_priority_preloads)}, expected 1")


def validate_forbidden_tokens() -> None:
    scan_roots = [
        ROOT / "src",
        ROOT / "locales",
        ROOT / "README.md",
        ROOT / "WORKFLOWS.md",
        ROOT / "I18N.md",
        ROOT / "design-system.md",
        ROOT / "style.css",
        *iter_html_files(),
    ]
    files: list[Path] = []
    for root in scan_roots:
        if root.is_dir():
            files.extend(path for path in root.rglob("*") if path.is_file() and "__pycache__" not in path.parts)
        elif root.exists():
            files.append(root)
    for path in files:
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in FORBIDDEN_TOKENS:
            if token in text:
                fail(f"forbidden token {token!r} in {path.relative_to(ROOT)}")


def main() -> None:
    load_json(ROOT / "data" / "image_adjustments.json")
    validate_locale_keys()
    rows = validate_products()
    validate_enrichment(rows)
    validate_assets(rows)
    validate_generated_html(rows)
    validate_optimized_assets()
    validate_forbidden_tokens()
    print("validate: ok")


if __name__ == "__main__":
    main()
