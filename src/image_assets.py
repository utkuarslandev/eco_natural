import json
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).parent.parent
SOURCE_IMG_DIR = ROOT / "img"
DERIVED_IMG_DIR = ROOT / "generated" / "img"
MANIFEST_PATH = ROOT / "data" / "image_adjustments.json"

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
