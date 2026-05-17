from __future__ import annotations

import re
from enrichment import ENRICHMENT, _category
from context import Ctx, localize_path
from html.escaping import escape
from image_assets import asset_dimensions, inline_adjustment_vars, resolved_asset

def _product_scene_background(slug: str) -> str | None:
    if "olive-oil" in slug:
        return "./img/olive-tree-sunset.png"

    scene_backgrounds = {
        "eco-natural-pumpkin-seed-oil-250ml": "./img/pumpkin-farm-night.png",
        "eco-natural-pomegranate-seed-oil-250ml": "./img/pomegranate-tree.png",
        "eco-natural-pomegranate-sour-340g": "./img/pomegranate-tree.png",
        "eco-natural-avocado-oil-250ml": "./img/avocado-basket-farm.png",
        "eco-natural-black-seed-oil-250ml": "./img/black-seed-farm-handful.png",
        "eco-natural-hemp-seed-oil-250ml": "./img/hemp-seed-farm-ladder-sunset.png",
        "metis-hierapolis-safflower-oil-250ml": "./img/safflower-field-crescent-moon.png",
        "eco-natural-poppy-seed-oil-250ml": "./img/poppy-field-harvesters-blue-sky.png",
        "eco-natural-fig-seed-oil": "./img/fig-tree-hand-picking-sunset.png",
        "eco-natural-carob-extract-680g": "./img/carob-tree-handpicking-basket.png",
        "eco-natural-carob-extract-340g": "./img/carob-tree-handpicking-basket.png",
        "eco-natural-salad-dressing": "./img/salad-dressing-dark-red-salad.png",
        "eco-natural-zeytin-sutu-cold-pressed-olive-elixir": "./img/olive-elixir-bottle-pouring-pan.png",
    }
    return scene_backgrounds.get(slug)

def _cat_slug(cat: str) -> str:
    slug = cat.lower().replace("ş", "s").replace("ı", "i").replace("&", "")
    slug = re.sub(r'[^a-z0-9]+', '-', slug).strip('-')
    return f"cat-{slug}"


def _category_ghost_word(pid: str) -> str:
    cat = _category(pid)
    words = {"Şirince Infused Oils": "ŞİRİNCE",
             "Early Harvest Olive Oils": "HARVEST",
             "Eco Natural Olive Oils": "OLIVE",
             "Olive Elixir": "ELIXIR",
             "Condiments & Extracts": "HARNUP",
             "Confectionery & Gifts": "LOKUM",
             "Metis Hierapolis": "METIS",
             "Specialty Oils": "ECO"}
    return words.get(cat, "ECO")

def _stamps_html(badges: list[tuple]) -> str:
    parts = []
    for emoji, name, *_ in badges[:4]:
        parts.append(
            f'<div class="stamp" data-reveal>'
            f'<span class="stamp-emoji" aria-hidden="true">{emoji}</span>'
            f'<span class="stamp-name">{escape(name)}</span>'
            f'</div>'
        )
    return "\n          ".join(parts)


def _use_tiles_html(uses: list[tuple]) -> str:
    parts = []
    for emoji, label in uses:
        parts.append(
            f'<div class="use-tile">'
            f'<div class="use-emoji" aria-hidden="true">{emoji}</div>'
            f'<div class="use-label">{escape(label)}</div>'
            f'</div>'
        )
    return "\n        ".join(parts)


def _quality_cards_html(badges: list[tuple]) -> str:
    parts = []
    for emoji, name, desc in badges:
        parts.append(
            f'<div class="quality-card">'
            f'<div class="quality-emoji" aria-hidden="true">{emoji}</div>'
            f'<div class="quality-copy">'
            f'<div class="quality-name">{escape(name)}</div>'
            f'<div class="quality-desc">{escape(desc)}</div>'
            f'</div>'
            f'</div>'
        )
    return "\n        ".join(parts)


def _story_html(paragraphs: list[str]) -> str:
    return "\n        ".join(f"<p>{escape(p)}</p>" for p in paragraphs)


def _trust_strip_html(badges: list[tuple]) -> str:
    parts = []
    for emoji, name, desc in badges[:3]:
        parts.append(
            f'<div class="trust-item">'
            f'<div class="trust-label">{escape(name)}</div>'
            f'<div class="trust-desc">{escape(desc)}</div>'
            f'</div>'
        )
    return "\n        ".join(parts)


def _related_html(related: list[tuple], img_dir, ctx: Ctx | None = None) -> str:
    parts = []
    for slug, title, pid in related[:4]:
        image_path, adjustments = resolved_asset(pid)
        localized_image_path = localize_path(image_path, ctx) if ctx else image_path
        style_attr = inline_adjustment_vars(adjustments)
        width, height = asset_dimensions(image_path)
        en_enrich = ENRICHMENT.get(pid, {})
        locale_enrich = ctx.enrichment.get(pid, {}) if ctx else {}
        rel_enrich = {**en_enrich, **locale_enrich}
        tagline = rel_enrich.get("tagline", "")
        tagline_html = f'<div class="related-tagline">{escape(tagline)}</div>' if tagline else ""
        parts.append(
            f'<a class="related-card" href="{escape(slug)}" data-prefetch-route>'
            f'<div class="related-img-stage" style="{style_attr}">'
            f'<img class="product-asset" src="{escape(localized_image_path)}" alt="{escape(title)}" '
            f'loading="lazy" decoding="async" width="{width}" height="{height}">'
            f'</div>'
            f'<div class="related-name">{escape(title)}</div>'
            f'{tagline_html}'
            f'</a>'
        )
    return "\n        ".join(parts)


def _flavor_chips_html(notes: list[str]) -> str:
    if not notes:
        return ""
    chips = "".join(
        f'<span class="flavor-chip">{escape(note)}</span>'
        for note in notes
    )
    return f'<div class="flavor-chips">{chips}</div>'


def _storage_callout_html(tip: str) -> str:
    if not tip:
        return ""
    return (
        f'<div class="storage-callout">'
        f'<span class="storage-icon" aria-hidden="true">&#128274;</span>'
        f'<span class="storage-text">{escape(tip)}</span>'
        f'</div>'
    )
