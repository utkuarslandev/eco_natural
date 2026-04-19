import json
from functools import lru_cache
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent.parent
SOURCE_IMG_DIR = ROOT / "img"
DERIVED_IMG_DIR = ROOT / "generated" / "img"
MANIFEST_PATH = ROOT / "data" / "image_adjustments.json"
CARD_VARIANT_DIR = DERIVED_IMG_DIR / "cards"
CARD_VARIANT_WIDTHS = (480, 960)

DEFAULT_ADJUSTMENTS = {
    "enabled": True,
    "rotation_deg": 0.0,
    "scale": 1.0,
    "offset_x": 0,
    "offset_y": 0,
    "subject_padding": 140,
}


@lru_cache(maxsize=1)
def load_adjustments() -> dict:
    if not MANIFEST_PATH.exists():
        return {"_default": DEFAULT_ADJUSTMENTS.copy()}

    data = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"{MANIFEST_PATH} must contain a JSON object")
    return data


def adjustments_for(product_id: str) -> dict:
    manifest = load_adjustments()
    merged = DEFAULT_ADJUSTMENTS.copy()
    merged.update(manifest.get("_default", {}))
    merged.update(manifest.get(product_id, {}))
    return merged


def resolved_asset(product_id: str) -> tuple[str, dict]:
    adjustments = adjustments_for(product_id)

    derived_path = DERIVED_IMG_DIR / f"{product_id}.png"
    if derived_path.exists():
        return derived_path.relative_to(ROOT).as_posix(), DEFAULT_ADJUSTMENTS.copy()

    source_png = SOURCE_IMG_DIR / f"{product_id}.png"
    if source_png.exists():
        return source_png.relative_to(ROOT).as_posix(), adjustments

    source_jpg = SOURCE_IMG_DIR / f"{product_id}.JPG"
    if source_jpg.exists():
        return source_jpg.relative_to(ROOT).as_posix(), adjustments

    source_jpg_lower = SOURCE_IMG_DIR / f"{product_id}.jpg"
    if source_jpg_lower.exists():
        return source_jpg_lower.relative_to(ROOT).as_posix(), adjustments

    return f"img/{product_id}.JPG", adjustments


def inline_adjustment_vars(adjustments: dict) -> str:
    rotation = float(adjustments.get("rotation_deg", 0.0))
    scale = float(adjustments.get("scale", 1.0))
    offset_x = int(adjustments.get("offset_x", 0))
    offset_y = int(adjustments.get("offset_y", 0))
    return (
        f"--img-scale:{scale:.4f};"
        f"--img-offset-x:{offset_x}px;"
        f"--img-offset-y:{offset_y}px;"
        f"--img-rotation:{rotation:.2f}deg;"
    )


@lru_cache(maxsize=None)
def asset_dimensions(asset_path: str) -> tuple[int, int]:
    path = ROOT / asset_path
    with Image.open(path) as image:
        return image.size


def _variant_output_path(asset_path: str, width: int) -> Path:
    stem = Path(asset_path).stem
    return CARD_VARIANT_DIR / f"{stem}-{width}.webp"


def _ensure_variant(asset_path: str, width: int) -> tuple[str, int, int]:
    source_path = ROOT / asset_path
    output_path = _variant_output_path(asset_path, width)

    source_width, source_height = asset_dimensions(asset_path)
    target_height = max(1, round((source_height / source_width) * width))

    needs_rebuild = (
        not output_path.exists()
        or output_path.stat().st_size == 0
        or output_path.stat().st_mtime < source_path.stat().st_mtime
    )

    if not needs_rebuild:
        try:
            with Image.open(output_path) as image:
                image.verify()
        except Exception:
            needs_rebuild = True

    if needs_rebuild:
        CARD_VARIANT_DIR.mkdir(parents=True, exist_ok=True)
        with Image.open(source_path) as image:
            resized = image.convert("RGBA").resize(
                (width, target_height),
                resample=Image.Resampling.LANCZOS,
            )
            resized.save(
                output_path,
                format="WEBP",
                quality=82,
                method=6,
            )

    return output_path.relative_to(ROOT).as_posix(), width, target_height


def card_image_sources(product_id: str) -> tuple[str, str, str]:
    asset_path, _ = resolved_asset(product_id)
    variants = [_ensure_variant(asset_path, width) for width in CARD_VARIANT_WIDTHS]
    srcset = ", ".join(f"{path} {width}w" for path, width, _ in variants)
    fallback_path = variants[-1][0]
    sizes = "(max-width: 768px) 44vw, (max-width: 1200px) 28vw, 320px"
    return fallback_path, srcset, sizes
