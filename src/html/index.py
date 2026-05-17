from __future__ import annotations

from context import Ctx, localize_path, localize_srcset
from enrichment import ENRICHMENT, _category
from html.base import _REVEAL_JS, _ROUTE_PREFETCH_JS, _document_head, _footer, _topbar, _torn
from html.components import _cat_slug, _product_scene_background
from html.escaping import escape
from image_assets import asset_dimensions, card_image_sources, inline_adjustment_vars, resolved_asset

def index_template(items: list[tuple[str, str, str]], enrichment_map: dict, img_dir, *, ctx: Ctx | None = None) -> str:
    groups: dict[str, list] = {}
    for fn, title, pid in items:
        cat = _category(pid)
        groups.setdefault(cat, []).append((fn, title, pid))

    cat_order = [
        "Early Harvest Olive Oils",
        "Eco Natural Olive Oils",
        "Şirince Infused Oils",
        "Specialty Oils",
        "Condiments & Extracts",
        "Olive Elixir",
        "Metis Hierapolis",
        "Confectionery & Gifts",
    ]
    ordered_groups = []
    for cat in cat_order:
        if cat in groups:
            ordered_groups.append((cat, groups[cat]))
    for cat, entries in groups.items():
        if cat not in cat_order:
            ordered_groups.append((cat, entries))

    cat_nav_html = "\n    ".join(
        f'<a href="#{_cat_slug(cat)}">{escape(ctx.cat_name(cat) if ctx else cat)}</a>'
        for cat, _ in ordered_groups
    )

    sections_html = ""
    logo_src = localize_path("./logo.png", ctx) if ctx else "./logo.png"
    hero_bg_src = localize_path("./img/hero-green-salad-olive-oil.png", ctx) if ctx else "./img/hero-green-salad-olive-oil.png"
    preload_links: list[str] = [
        f'<link rel="preload" as="image" href="{logo_src}">',
        f'<link rel="preload" as="image" href="{hero_bg_src}">',
    ]
    eager_card_limit = 4
    eager_card_index = 0
    learn_more_text = ctx.t("learn_more") if ctx else "Learn More →"
    gift_chip_text = ctx.t("gift_chip") if ctx else "Gift"

    for cat, entries in ordered_groups:
        cards = ""
        for fn, title, pid in entries:
            image_path, adjustments = resolved_asset(pid)
            card_image_path, card_srcset, card_sizes = card_image_sources(pid)
            localized_card_image_path = localize_path(card_image_path, ctx) if ctx else card_image_path
            localized_card_srcset = localize_srcset(card_srcset, ctx) if ctx else card_srcset
            image_style = inline_adjustment_vars(adjustments)
            image_width, image_height = asset_dimensions(image_path)
            product_slug = fn.rsplit(".", 1)[0]
            scene_background = _product_scene_background(product_slug)
            card_style = image_style
            if scene_background:
                localized_scene_background = localize_path(scene_background, ctx) if ctx else scene_background
                card_style = f"{card_style};--card-bg:url('{escape(localized_scene_background)}')"

            # Merge enrichment: English base + locale-specific
            en_enrich = ENRICHMENT.get(pid, {})
            locale_enrich = ctx.enrichment.get(pid, {}) if ctx else {}
            enrich = {**en_enrich, **locale_enrich}

            desc    = enrich.get("tagline", "")
            is_gift = enrich.get("is_gift", False)
            gift_chip = f'<div class="card-gift">{gift_chip_text}</div>' if is_gift else ""
            should_eager_load = eager_card_index < eager_card_limit
            if should_eager_load:
                preload_links.append(
                    f'<link rel="preload" as="image" href="{escape(localized_card_image_path)}" '
                    f'imagesrcset="{escape(localized_card_srcset)}" imagesizes="{escape(card_sizes)}">'
                )
            loading = "eager" if should_eager_load else "lazy"
            fetchpriority = ' fetchpriority="high"' if should_eager_load else ""
            eager_card_index += 1
            cards += f"""
        <a class="product-card" href="{escape(fn)}" style="{card_style}" data-reveal data-prefetch-route>
          <div class="card-img-wrap">
            <div class="card-img-stage">
              <img class="product-asset" src="{escape(localized_card_image_path)}" srcset="{escape(localized_card_srcset)}" sizes="{escape(card_sizes)}" alt="{escape(title)}" loading="{loading}" decoding="async"{fetchpriority} width="{image_width}" height="{image_height}">
            </div>
          </div>
          <div class="card-body">
            <div class="card-category">{escape(ctx.cat_name(cat) if ctx else cat)}</div>
            <div class="card-name">{escape(title)}</div>
            <div class="card-desc">{escape(desc)}</div>
            {gift_chip}
            <div class="card-cta">{learn_more_text}</div>
          </div>
        </a>"""

        cat_display_name = ctx.cat_name(cat) if ctx else cat
        sections_html += f"""
    <div class="catalog-section" id="{_cat_slug(cat)}">
      <div class="eyebrow">{escape(cat_display_name)}</div>
      <div class="product-grid">
        {cards}
      </div>
    </div>"""

    # Localized strings
    index_title = ctx.t("index_title") if ctx else "Eco Natural — Lasting Taste of Earth"
    index_meta_desc = ctx.t("index_meta_description", count=len(items)) if ctx else f"Village-origin cold-pressed natural food extracts from Büyük Çaltıcak, Aegean Turkey. {len(items)} artisan products."
    hero_tagline = ctx.t("hero_tagline") if ctx else "Lasting Taste of Earth"
    cat_nav_label = ctx.t("cat_nav_label") if ctx else "Product categories"
    footer_tagline = ctx.t("footer_tagline") if ctx else "Lasting Taste of Earth"

    # Stamps from locales
    stamps = ctx.strings.get("stamps", ["%100 Natural", "Cold Press", "Katkısız", "Büyük Çaltıcak", "Glass Bottle"]) if ctx else ["%100 Natural", "Cold Press", "Katkısız", "Büyük Çaltıcak", "Glass Bottle"]
    stamps_html = "\n        ".join(f'<div class="stamp">{escape(s)}</div>' for s in stamps)

    lang_attr = ctx.locale if ctx else "en"

    return f"""<!doctype html>
<html lang="{lang_attr}">
{_document_head(index_title, index_meta_desc, ctx=ctx, extra_links=preload_links)}
<body class="page-index">

{_topbar(ctx=ctx, slug="index")}

  <section class="hero">
    <div class="hero-ghost" aria-hidden="true">ECO</div>
    <div class="hero-content">
      <img class="hero-logo" src="{logo_src}" alt="Eco Natural" width="2000" height="2000" loading="eager" decoding="async" fetchpriority="high">
      <h1 data-reveal>Eco Natural</h1>
      <p class="hero-tagline" data-reveal><em>{escape(hero_tagline)}</em></p>
      <div class="stamp-row" data-reveal>
        {stamps_html}
      </div>
    </div>
  </section>

  {_torn("#F6FAF4")}

  <nav class="cat-nav" aria-label="{escape(cat_nav_label)}">
    {cat_nav_html}
  </nav>

  {sections_html}


{_footer(ctx=ctx)}

  {_REVEAL_JS}
  {_ROUTE_PREFETCH_JS}

</body>
</html>
"""
