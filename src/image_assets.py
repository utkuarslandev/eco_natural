import json
from functools import lru_cache
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent.parent
SOURCE_IMG_DIR = ROOT / "img"
DERIVED_IMG_DIR = ROOT / "generated" / "img"
MANIFEST_PATH = ROOT / "data" / "image_adjustments.json"
PRODUCT_THUMBNAIL_DIR = DERIVED_IMG_DIR / "products" / "thumbnails"
PRODUCT_HERO_DIR = DERIVED_IMG_DIR / "products" / "heroes"
SCENE_VARIANT_DIR = DERIVED_IMG_DIR / "scenes"
BRANDING_VARIANT_DIR = DERIVED_IMG_DIR / "branding"

PRODUCT_THUMBNAIL_WIDTHS = (160, 320)
PRODUCT_HERO_WIDTHS = (480, 960)
SCENE_CARD_WIDTHS = (480, 960)
SCENE_PAGE_WIDTHS = (960, 1600)
LOGO_WIDTHS = (128, 256)

# Scenes are always rendered under heavy gradient/overlay tinting (card backgrounds,
# darkened hero/section backgrounds), so a lower WebP quality is visually lossless here
# while meaningfully cutting transfer weight. Shared by every scene width so the 960px
# variant (used by both card and page contexts) never collides at two different qualities.
SCENE_QUALITY = 64

SCENE_SOURCE_PATHS = (
    "img/avocado-basket-farm.png",
    "img/black-seed-farm-handful.png",
    "img/carob-tree-handpicking-basket.png",
    "img/fig-tree-hand-picking-sunset.png",
    "img/hemp-seed-farm-ladder-sunset.png",
    "img/hero-aegean-field.png",
    "img/hero-green-salad-olive-oil.png",
    "img/olive-elixir-bottle-pouring-pan.png",
    "img/olive-tree-sunset.png",
    "img/pomegranate-tree.png",
    "img/poppy-field-harvesters-blue-sky.png",
    "img/pumpkin-farm-night.png",
    "img/safflower-field-crescent-moon.png",
    "img/salad-dressing-dark-red-salad.png",
    "img/thistle-field-farmers-sun.png",
)

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


def _variant_output_path(asset_path: str, output_dir: Path, width: int, suffix: str = "webp") -> Path:
    stem = Path(asset_path).stem
    return output_dir / f"{stem}-{width}.{suffix}"


def _variant_is_current(source_path: Path, output_path: Path) -> bool:
    if (
        not output_path.exists()
        or output_path.stat().st_size == 0
        or output_path.stat().st_mtime < source_path.stat().st_mtime
    ):
        return False
    try:
        with Image.open(output_path) as image:
            image.verify()
    except Exception:
        return False
    return True


def _ensure_webp_variant(
    asset_path: str,
    output_dir: Path,
    width: int,
    *,
    quality: int,
    preserve_alpha: bool,
) -> tuple[str, int, int]:
    source_path = ROOT / asset_path
    output_path = _variant_output_path(asset_path, output_dir, width)

    source_width, source_height = asset_dimensions(asset_path)
    target_height = max(1, round((source_height / source_width) * width))

    if not _variant_is_current(source_path, output_path):
        output_dir.mkdir(parents=True, exist_ok=True)
        with Image.open(source_path) as image:
            mode = "RGBA" if preserve_alpha else "RGB"
            resized = image.convert(mode).resize(
                (width, target_height),
                resample=Image.Resampling.LANCZOS,
            )
            resized.save(
                output_path,
                format="WEBP",
                quality=quality,
                method=6,
            )

    return output_path.relative_to(ROOT).as_posix(), width, target_height


def _ensure_png_variant(asset_path: str, width: int) -> str:
    source_path = ROOT / asset_path
    output_path = _variant_output_path(asset_path, BRANDING_VARIANT_DIR, width, suffix="png")

    if not _variant_is_current(source_path, output_path):
        BRANDING_VARIANT_DIR.mkdir(parents=True, exist_ok=True)
        with Image.open(source_path) as image:
            resized = image.convert("RGBA").resize((width, width), resample=Image.Resampling.LANCZOS)
            resized.save(output_path, format="PNG", optimize=True)

    return output_path.relative_to(ROOT).as_posix()


def _responsive_sources(
    asset_path: str,
    output_dir: Path,
    widths: tuple[int, ...],
    *,
    quality: int,
    preserve_alpha: bool,
    sizes: str,
) -> tuple[str, str, str]:
    variants = [
        _ensure_webp_variant(
            asset_path,
            output_dir,
            width,
            quality=quality,
            preserve_alpha=preserve_alpha,
        )
        for width in widths
    ]
    srcset = ", ".join(f"{path} {width}w" for path, width, _ in variants)
    return variants[-1][0], srcset, sizes


def product_thumbnail_sources(product_id: str) -> tuple[str, str, str]:
    asset_path, _ = resolved_asset(product_id)
    return _responsive_sources(
        asset_path,
        PRODUCT_THUMBNAIL_DIR,
        PRODUCT_THUMBNAIL_WIDTHS,
        quality=82,
        preserve_alpha=True,
        sizes="(max-width: 768px) 96px, 160px",
    )


def product_hero_sources(product_id: str) -> tuple[str, str, str]:
    asset_path, _ = resolved_asset(product_id)
    return _responsive_sources(
        asset_path,
        PRODUCT_HERO_DIR,
        PRODUCT_HERO_WIDTHS,
        quality=82,
        preserve_alpha=True,
        sizes="(max-width: 899px) 78vw, 460px",
    )


def page_scene_image_sources(asset_path: str, *, sizes: str) -> tuple[str, str, str]:
    cleaned_path = asset_path.removeprefix("./")
    return _responsive_sources(
        cleaned_path,
        SCENE_VARIANT_DIR,
        SCENE_PAGE_WIDTHS,
        quality=SCENE_QUALITY,
        preserve_alpha=False,
        sizes=sizes,
    )


def scene_image_set(asset_path: str) -> str:
    cleaned_path = asset_path.removeprefix("./")
    stem = Path(cleaned_path).stem
    return (
        "image-set("
        f'url("./generated/img/scenes/{stem}-960.webp") 1x, '
        f'url("./generated/img/scenes/{stem}-1600.webp") 2x'
        ")"
    )


def scene_card_image_set(asset_path: str) -> str:
    """Ensure the card-scale (480/960) scene variants exist and return a CSS
    image-set() for use as a product-card background. Paths are root-relative
    ("./generated/..."); localize for subdir locales at the call site."""
    cleaned_path = asset_path.removeprefix("./")
    variants = [
        _ensure_webp_variant(
            cleaned_path,
            SCENE_VARIANT_DIR,
            width,
            quality=SCENE_QUALITY,
            preserve_alpha=False,
        )
        for width in SCENE_CARD_WIDTHS
    ]
    # Single-quoted URLs so the value is safe to drop into a double-quoted
    # HTML style="..." attribute without terminating it early.
    small, large = variants[0][0], variants[1][0]
    return f"image-set(url('./{small}') 1x, url('./{large}') 2x)"


def logo_image_sources() -> tuple[str, str]:
    source_path = "logo.png"
    variants = [
        _ensure_webp_variant(
            source_path,
            BRANDING_VARIANT_DIR,
            width,
            quality=82,
            preserve_alpha=True,
        )
        for width in LOGO_WIDTHS
    ]
    srcset = ", ".join(f"{path} {width}w" for path, width, _ in variants)
    return variants[-1][0], srcset


def branding_icon_sources() -> tuple[str, str]:
    return _ensure_png_variant("logo.png", 64), _ensure_png_variant("logo.png", 180)


def prepare_generated_assets(product_ids: list[str]) -> None:
    logo_image_sources()
    branding_icon_sources()
    for product_id in product_ids:
        product_thumbnail_sources(product_id)
        product_hero_sources(product_id)
    scene_widths = sorted(set(SCENE_CARD_WIDTHS) | set(SCENE_PAGE_WIDTHS))
    for asset_path in SCENE_SOURCE_PATHS:
        for width in scene_widths:
            _ensure_webp_variant(
                asset_path,
                SCENE_VARIANT_DIR,
                width,
                quality=SCENE_QUALITY,
                preserve_alpha=False,
            )
