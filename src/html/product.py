from __future__ import annotations

import json

from context import Ctx, localize_path
from enrichment import ENRICHMENT, _category
from html.base import _REVEAL_JS, _ROUTE_PREFETCH_JS, _document_head, _footer, _topbar, _torn
from html.components import (
    _category_ghost_word,
    _flavor_chips_html,
    _quality_cards_html,
    _related_html,
    _stamps_html,
    _storage_callout_html,
    _story_html,
    _use_tiles_html,
)
from html.escaping import escape
from image_assets import asset_dimensions, inline_adjustment_vars, resolved_asset

def page_template(row: dict, related: list | None, img_dir, *, ctx: Ctx | None = None) -> str:
    product_id   = row["product_id"].strip()
    page_title   = row["page_title"].strip()
    slug         = row["slug"].strip()
    meta_desc    = row["meta_description"].strip()
    seo_title    = row["seo_title"].strip()
    full_desc    = row["full_description"].strip()
    short_desc   = row["short_description"].strip()

    image_path, adjustments = resolved_asset(product_id)
    localized_image_path = localize_path(image_path, ctx) if ctx else image_path
    image_style = inline_adjustment_vars(adjustments)
    image_width, image_height = asset_dimensions(image_path)

    # Merge enrichment: English base + locale-specific overrides
    en_enrich = ENRICHMENT.get(product_id, {})
    locale_enrich = ctx.enrichment.get(product_id, {}) if ctx else {}
    enrich = {**en_enrich, **locale_enrich}

    origin_place  = enrich.get("origin_place", "Turkey")
    story_paras   = enrich.get("story", [full_desc])
    how_to_use    = enrich.get("how_to_use", [
        ("🍽️", "Cooking"),  ("🥗", "Salads"),
        ("🫙", "Finishing"), ("🎁", "Gifting"),
        ("🍞", "Serving"),   ("🧴", "Daily Use"),
    ])
    badges        = enrich.get("badges", [
        ("✅", "Natural",      "Pure natural ingredients"),
        ("🌱", "Plant-Based",  "100% plant origin"),
        ("🚫", "No Additives", "Nothing synthetic"),
        ("📍", "Turkish Origin","Made in Turkey"),
        ("⭐", "Premium",      "Curated quality range"),
    ])
    is_gift       = enrich.get("is_gift", False)
    product_line  = enrich.get("product_line", "Eco Natural")
    tagline       = enrich.get("tagline", short_desc)
    flavor_notes  = enrich.get("flavor_notes", [])
    storage_tip   = enrich.get("storage_tip", "")
    ghost_word    = _category_ghost_word(product_id)

    gift_banner_text = ctx.t("gift_banner") if ctx else "Makes a beautiful gift — perfect for food lovers"
    gift_banner = (
        f'<div class="gift-banner" data-reveal>{gift_banner_text}</div>'
        if is_gift else ""
    )

    json_ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Product",
        "name": page_title,
        "description": meta_desc,
        "sku": product_id,
        "image": localized_image_path,
        "brand": {"@type": "Brand", "name": "Eco Natural"},
    }, ensure_ascii=False, indent=2)

    lang_attr = ctx.locale if ctx else "en"
    all_products_text = ctx.t("all_products") if ctx else "All Products"
    breadcrumb_label = ctx.t("breadcrumb_label") if ctx else "Breadcrumb"
    origin_story_eyebrow = ctx.t("origin_story_eyebrow") if ctx else "Origin & Story"
    how_to_enjoy_eyebrow = ctx.t("how_to_enjoy_eyebrow") if ctx else "How to Enjoy"
    how_to_enjoy_heading = ctx.t("how_to_enjoy_heading") if ctx else "Six ways to use it at home"
    quality_eyebrow = ctx.t("quality_eyebrow") if ctx else "Quality & Standards"
    quality_heading = ctx.t("quality_heading") if ctx else "What makes it exceptional"
    storage_eyebrow = ctx.t("storage_eyebrow") if ctx else "Storage"

    storage_block = ""
    if storage_tip:
        storage_block = f"""
    <div class="section storage-section" data-reveal>
      <div class="eyebrow">{escape(storage_eyebrow)}</div>
      {_storage_callout_html(storage_tip)}
    </div>"""

    related_items = related or []
    head_links = [
        f'<link rel="preload" as="image" href="{escape(localized_image_path)}">'
    ]
    related_html_block = ""
    if related_items:
        more_like_this_text = ctx.t("more_like_this") if ctx else "More Like This"
        related_html_block = f"""
    <div class="section" data-reveal>
      <div class="eyebrow">{more_like_this_text}</div>
      <div class="related-grid">
        {_related_html(related_items, img_dir, ctx=ctx)}
      </div>
    </div>"""

    all_products_link = localize_path("./index.html", ctx) if ctx else "./index.html"
    product_body_classes = ["page-product", f"product-{slug}"]
    if "olive-oil" in slug:
        product_body_classes.append("product-olive-oil-bg")
    if "carob" in slug:
        product_body_classes.append("product-carob-bg")
    body_classes = " ".join(escape(class_name) for class_name in product_body_classes)

    return f"""<!doctype html>
<html lang="{lang_attr}">
{_document_head(f"{seo_title or page_title} | Eco Natural", meta_desc, ctx=ctx, json_ld=json_ld, extra_links=head_links)}
<body class="{body_classes}">

{_topbar(ctx=ctx, slug=slug)}

  <nav class="breadcrumb" aria-label="{breadcrumb_label}">
    <div class="breadcrumb-inner">
      <a href="{all_products_link}">{all_products_text}</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">{escape(ctx.cat_name(_category(product_id)) if ctx else _category(product_id))}</span>
    </div>
  </nav>


  <section class="hero">
    <div class="hero-ghost" aria-hidden="true">{escape(ghost_word)}</div>
    <div class="hero-img-wrap">
      <div class="hero-img-stage" style="{image_style}">
        <img class="product-asset" src="{localized_image_path}" alt="{escape(page_title)}"
          width="{image_width}" height="{image_height}" loading="eager" decoding="async" fetchpriority="high">
      </div>
    </div>
    <div class="hero-copy">
      <div class="hero-eyebrow">{escape(product_line)}</div>
      <h1>{escape(page_title)}</h1>
      <p class="tagline">{escape(tagline)}</p>
    </div>
    <div class="scroll-hint" aria-hidden="true">&#9660;</div>
  </section>

  {_torn("#1A3520")}

  <div class="credentials-strip">
    <div class="stamp-row">
      {_stamps_html(badges)}
    </div>
    {gift_banner}
  </div>

  {_torn("#F6FAF4")}

  <div class="wrap">

    <div class="section section-origin" data-reveal>
      <div class="eyebrow">{escape(origin_story_eyebrow)}</div>
      <div class="story-card">
        <div class="origin-chip">&#128205; {escape(origin_place)}</div>
        {_flavor_chips_html(flavor_notes)}
        {_story_html(story_paras)}
      </div>
    </div>

    <div class="details-columns">
      <div class="section section-uses">
        <div class="eyebrow">{escape(how_to_enjoy_eyebrow)}</div>
        <div class="section-heading">{escape(how_to_enjoy_heading)}</div>
        <div class="use-grid">
          {_use_tiles_html(how_to_use)}
        </div>
      </div>

      <div class="section section-quality">
        <div class="eyebrow">{escape(quality_eyebrow)}</div>
        <div class="section-heading">{escape(quality_heading)}</div>
        <div class="quality-grid">
          {_quality_cards_html(badges)}
        </div>
      </div>
    </div>

    {storage_block}

    <div class="experience-line" data-reveal>
      Our products may come from Mother Nature, but the experience feels out of this world.
    </div>

    {related_html_block}

  </div>

{_footer(ctx=ctx, show_back_link=True)}

  {_REVEAL_JS}
  {_ROUTE_PREFETCH_JS}

</body>
</html>
"""
