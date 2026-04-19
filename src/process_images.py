"""
Build normalized transparent product assets for the static site.

Usage:
    pip install rembg pillow
    python3 src/process_images.py
    python3 src/process_images.py --product-id EN-HEMP-SEED-OIL-250ML --force
    python3 src/process_images.py --dry-run
"""

from __future__ import annotations

import argparse
import csv
import io
import sys
from dataclasses import dataclass
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(Path(__file__).parent))

from image_assets import DEFAULT_ADJUSTMENTS, DERIVED_IMG_DIR, MANIFEST_PATH, SOURCE_IMG_DIR, adjustments_for

CSV_PATH = ROOT / "data" / "ids.csv"
DEFAULT_CANVAS = 1600


def remove_background(payload: bytes) -> bytes:
    try:
        from rembg import remove
    except ImportError as exc:  # pragma: no cover - runtime dependency
        raise SystemExit("rembg not installed. Run: pip install rembg pillow") from exc

    return remove(payload)


@dataclass
class ProcessResult:
    product_id: str
    status: str
    detail: str = ""


def load_product_ids() -> list[str]:
    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        return [row["product_id"].strip() for row in csv.DictReader(fh)]


def source_path_for(product_id: str) -> Path | None:
    for ext in (".JPG", ".jpg", ".jpeg", ".JPEG", ".png"):
        path = SOURCE_IMG_DIR / f"{product_id}{ext}"
        if path.exists():
            return path
    return None


def needs_rebuild(src: Path, dst: Path, force: bool) -> bool:
    if force or not dst.exists():
        return True
    latest_input = max(src.stat().st_mtime, MANIFEST_PATH.stat().st_mtime if MANIFEST_PATH.exists() else 0)
    return dst.stat().st_mtime < latest_input


def trim_subject(image: Image.Image) -> Image.Image:
    alpha = image.getchannel("A")
    bbox = alpha.getbbox()
    if bbox is None:
        raise ValueError("background removal produced an empty subject")
    return image.crop(bbox)


def normalize_canvas(subject: Image.Image, adjustments: dict, canvas_size: int) -> Image.Image:
    rotation = float(adjustments.get("rotation_deg", DEFAULT_ADJUSTMENTS["rotation_deg"]))
    scale = float(adjustments.get("scale", DEFAULT_ADJUSTMENTS["scale"]))
    offset_x = int(adjustments.get("offset_x", DEFAULT_ADJUSTMENTS["offset_x"]))
    offset_y = int(adjustments.get("offset_y", DEFAULT_ADJUSTMENTS["offset_y"]))
    subject_padding = int(adjustments.get("subject_padding", DEFAULT_ADJUSTMENTS["subject_padding"]))

    rotated = subject.rotate(-rotation, expand=True, resample=Image.Resampling.BICUBIC)
    rotated = trim_subject(rotated)

    safe_size = max(1, canvas_size - (subject_padding * 2))
    fit_ratio = min(safe_size / rotated.width, safe_size / rotated.height)
    final_ratio = fit_ratio * scale
    resized = rotated.resize(
        (
            max(1, round(rotated.width * final_ratio)),
            max(1, round(rotated.height * final_ratio)),
        ),
        resample=Image.Resampling.LANCZOS,
    )

    canvas = Image.new("RGBA", (canvas_size, canvas_size), (0, 0, 0, 0))
    x = round((canvas_size - resized.width) / 2 + offset_x)
    y = round((canvas_size - resized.height) / 2 + offset_y)
    canvas.alpha_composite(resized, (x, y))
    return canvas


def process_product(product_id: str, canvas_size: int, dry_run: bool, force: bool) -> ProcessResult:
    src = source_path_for(product_id)
    if src is None:
        return ProcessResult(product_id, "failed", "missing source image")

    dst = DERIVED_IMG_DIR / f"{product_id}.png"
    if not needs_rebuild(src, dst, force):
        return ProcessResult(product_id, "skipped", "up to date")

    adjustments = adjustments_for(product_id)
    if not adjustments.get("enabled", True):
        return ProcessResult(product_id, "skipped", "disabled in manifest")

    if dry_run:
        return ProcessResult(product_id, "planned", f"{src.name} -> {dst.relative_to(ROOT)}")

    with src.open("rb") as fh:
        result = remove_background(fh.read())

    cutout = Image.open(io.BytesIO(result)).convert("RGBA")
    subject = trim_subject(cutout)
    normalized = normalize_canvas(subject, adjustments, canvas_size=canvas_size)

    DERIVED_IMG_DIR.mkdir(parents=True, exist_ok=True)
    normalized.save(dst, format="PNG", optimize=True)
    return ProcessResult(product_id, "processed", dst.relative_to(ROOT).as_posix())


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate normalized transparent product assets.")
    parser.add_argument("--product-id", action="append", dest="product_ids", help="Only process the given product ID.")
    parser.add_argument("--force", action="store_true", help="Rebuild outputs even if they look up to date.")
    parser.add_argument("--dry-run", action="store_true", help="Report what would be processed without writing files.")
    parser.add_argument("--canvas-size", type=int, default=DEFAULT_CANVAS, help="Transparent canvas width/height in pixels.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    product_ids = args.product_ids or load_product_ids()

    results = [
        process_product(product_id, canvas_size=args.canvas_size, dry_run=args.dry_run, force=args.force)
        for product_id in product_ids
    ]

    buckets: dict[str, list[ProcessResult]] = {}
    for result in results:
        buckets.setdefault(result.status, []).append(result)

    for status in ("processed", "planned", "skipped", "failed"):
        for result in buckets.get(status, []):
            print(f"{status:9} {result.product_id} {result.detail}".rstrip())

    print(
        "\nSummary: "
        f"processed={len(buckets.get('processed', []))} "
        f"planned={len(buckets.get('planned', []))} "
        f"skipped={len(buckets.get('skipped', []))} "
        f"failed={len(buckets.get('failed', []))}"
    )

    if buckets.get("failed"):
        raise SystemExit(1)


if __name__ == "__main__":
    main()
