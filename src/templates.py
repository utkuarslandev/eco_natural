import json
from dataclasses import dataclass
from html import escape
from urllib.parse import quote

from enrichment import ENRICHMENT, _category
from image_assets import asset_dimensions, card_image_sources, inline_adjustment_vars, resolved_asset
from styles import FONTS_LINK

WA_NUMBER = "+900000000000"  # placeholder — replace with real number before going live


@dataclass
class Ctx:
    locale: str
    strings: dict
    enrichment: dict
    is_subdir: bool

    def t(self, key: str, **fmt) -> str:
        val = self.strings.get(key, f"[MISSING:{key}]")
        return val.format(**fmt) if fmt else val

    def asset_prefix(self) -> str:
        return "../" if self.is_subdir else "./"

    def cat_name(self, cat: str) -> str:
        return self.strings.get("categories", {}).get(cat, cat)


def _localize_path(path: str, ctx: Ctx) -> str:
    if ctx.is_subdir and not path.startswith(("http://", "https://")):
        # Remove leading ./ if present, then add ../
        cleaned = path.lstrip("./") if path.startswith("./") else path
        return "../" + cleaned
    return path


def _localize_srcset(srcset: str, ctx: Ctx) -> str:
    """Localize all paths in a srcset string (format: 'path widthw, path widthw, ...')"""
    if not ctx or not ctx.is_subdir:
        return srcset
    parts = srcset.split(", ")
    localized_parts = []
    for part in parts:
        path_and_width = part.rsplit(" ", 1)
        if len(path_and_width) == 2:
            path, width = path_and_width
            localized_path = _localize_path(path, ctx)
            localized_parts.append(f"{localized_path} {width}")
        else:
            localized_parts.append(part)
    return ", ".join(localized_parts)

_WAVE = (
    "M0,14 C36,8 64,8 100,14 C136,20 164,20 200,14 "
    "C236,8 264,8 300,14 C336,20 364,20 400,14 "
    "C436,8 464,8 500,14 C536,20 564,20 600,14 "
    "C636,8 664,8 700,14 C736,20 764,20 800,14 "
    "C836,8 864,8 900,14 C936,20 964,20 1000,14 "
    "C1036,8 1064,8 1100,14 C1136,20 1164,20 1200,14 "
    "L1200,28 L0,28 Z"
)


def _torn(fill: str) -> str:
    return (
        f'<div class="torn" aria-hidden="true">'
        f'<svg viewBox="0 0 1200 28" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'
        f'<path d="{_WAVE}" fill="{fill}"/>'
        f'</svg></div>'
    )


_TORN_PARCH = _torn("#F6FAF4")
_TORN_BARK  = _torn("#1A3520")

_WA_SVG = (
    '<svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15'
    '-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475'
    '-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52'
    '.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207'
    '-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372'
    '-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2'
    ' 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719'
    ' 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347z"/>'
    '<path d="M12 0C5.373 0 0 5.373 0 12c0 2.096.537 4.067 1.479 5.785L0 24l6.385-1.455'
    'A11.945 11.945 0 0 0 12 24c6.627 0 12-5.373 12-12S18.627 0 12 0zm0 21.818'
    'a9.807 9.807 0 0 1-5.031-1.383l-.361-.214-3.737.979.997-3.645-.235-.374'
    'A9.795 9.795 0 0 1 2.182 12C2.182 6.57 6.57 2.182 12 2.182S21.818 6.57 21.818 12'
    ' 17.43 21.818 12 21.818z"/>'
    '</svg>'
)

_REVEAL_JS = """
<script>
(function(){
  var els = document.querySelectorAll('[data-reveal]');
  if(!els.length) return;

  var ordered = Array.prototype.slice.call(els);
  var indexMap = new Map();
  ordered.forEach(function(el, index){ indexMap.set(el, index); });

  var io = new IntersectionObserver(function(entries){
    entries
      .filter(function(entry){ return entry.isIntersecting; })
      .sort(function(a, b){ return indexMap.get(a.target) - indexMap.get(b.target); })
      .forEach(function(entry, batchIndex){
        var delay = Math.min(batchIndex, 5) * 70;
        entry.target.style.transitionDelay = delay + 'ms';
        entry.target.classList.add('revealed');
        io.unobserve(entry.target);
      });
  }, {threshold: 0.12});
  els.forEach(function(el){
    el.style.transitionDelay = '0ms';
    io.observe(el);
  });
})();
</script>
"""

_STICKY_WA_JS = """
<script>
(function(){
  var heroCta = document.querySelector('.hero .btn-wa');
  var bar = document.getElementById('sticky-wa');
  if (!heroCta || !bar) return;
  bar.href = heroCta.href;
  var io = new IntersectionObserver(function(entries){
    bar.classList.toggle('visible', !entries[0].isIntersecting);
  });
  io.observe(heroCta);
})();
</script>
"""

_ROUTE_PREFETCH_JS = """
<script>
(function(){
  var seen = new Set();

  function prefetch(href) {
    if (!href || seen.has(href)) return;
    seen.add(href);
    var link = document.createElement('link');
    link.rel = 'prefetch';
    link.href = href;
    link.as = 'document';
    document.head.appendChild(link);
  }

  function bind(anchor) {
    if (!anchor || !anchor.href) return;
    var href = anchor.href;
    anchor.addEventListener('mouseenter', function(){ prefetch(href); }, {passive:true});
    anchor.addEventListener('focus', function(){ prefetch(href); }, {passive:true});
    anchor.addEventListener('touchstart', function(){ prefetch(href); }, {passive:true, once:true});
  }

  var anchors = document.querySelectorAll('a[data-prefetch-route]');
  anchors.forEach(bind);

  var eager = Array.prototype.slice.call(anchors, 0, 4);
  if ('requestIdleCallback' in window) {
    requestIdleCallback(function(){ eager.forEach(function(a){ prefetch(a.href); }); }, {timeout: 1200});
  } else {
    setTimeout(function(){ eager.forEach(function(a){ prefetch(a.href); }); }, 800);
  }
})();
</script>
"""


def _document_head(title: str, description: str, *, ctx: Ctx | None = None, json_ld: str | None = None, extra_links: list[str] | None = None) -> str:
    json_ld_block = ""
    if json_ld:
        json_ld_block = f"""
  <script type="application/ld+json">
{json_ld}
  </script>"""
    extra_link_block = ""
    if extra_links:
        extra_link_block = "\n" + "\n".join(f"  {link}" for link in extra_links)

    stylesheet_href = "style.css"
    favicon_href = "logo.png"
    if ctx:
        stylesheet_href = _localize_path(stylesheet_href, ctx)
        favicon_href = _localize_path(favicon_href, ctx)

    return f"""<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <link rel="icon" href="{favicon_href}" type="image/png">
  <link rel="apple-touch-icon" href="{favicon_href}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS_LINK}" rel="stylesheet">
  <link rel="stylesheet" href="{stylesheet_href}">{extra_link_block}{json_ld_block}
</head>"""


def _topbar(*, ctx: Ctx | None = None, show_back_link: bool = False, slug: str | None = None) -> str:
    back_link = ""
    if show_back_link:
        if ctx:
            back_link_text = ctx.t("back_link")
            back_link_href = _localize_path("./index.html", ctx)
        else:
            back_link_text = "&#8592; All Products"
            back_link_href = "./index.html"
        back_link = f'\n    <a class="topbar-back" href="{back_link_href}">{back_link_text}</a>'

    logo_src = _localize_path("./logo.png", ctx) if ctx else "./logo.png"
    home_href = _localize_path("./index.html", ctx) if ctx else "./index.html"

    lang_switcher = ""
    if ctx and slug:
        slug_file = f"{slug}.html"
        if ctx.locale == "en":
            en_url = slug_file
            tr_url = f"tr/{slug_file}"
            ru_url = f"ru/{slug_file}"
        elif ctx.locale == "tr":
            en_url = f"../{slug_file}"
            tr_url = slug_file
            ru_url = f"../ru/{slug_file}"
        else:  # ru
            en_url = f"../{slug_file}"
            tr_url = f"../tr/{slug_file}"
            ru_url = slug_file

        en_class = "lang-item--active" if ctx.locale == "en" else ""
        tr_class = "lang-item--active" if ctx.locale == "tr" else ""
        ru_class = "lang-item--active" if ctx.locale == "ru" else ""

        lang_switcher = f"""
    <div class="lang-switcher" aria-label="Language selection">
      <a href="{en_url}" class="lang-item {en_class}" hreflang="en">EN</a>
      <a href="{tr_url}" class="lang-item {tr_class}" hreflang="tr">TR</a>
      <a href="{ru_url}" class="lang-item {ru_class}" hreflang="ru">RU</a>
    </div>"""

    return f"""  <nav class="topbar">
    <a class="topbar-home" href="{home_href}" aria-label="Eco Natural home">
      <img class="topbar-logo" src="{logo_src}" alt="Eco Natural">
      <div class="topbar-lockup">
        <span class="topbar-brand">ECO NATURAL</span>
        <span class="topbar-sub">B&uuml;y&uuml;k &Ccedil;alt&#305;cak</span>
      </div>
    </a>{back_link}{lang_switcher}
  </nav>"""


def _footer(*, ctx: Ctx | None = None, show_back_link: bool = False) -> str:
    back_link = ""
    if show_back_link:
        back_footer_text = ctx.t("back_footer") if ctx else "← Back to All Products"
        back_link_href = _localize_path("./index.html", ctx) if ctx else "./index.html"
        back_link = f'\n    <a href="{back_link_href}">{back_footer_text}</a>'

    footer_logo_src = _localize_path("./logo.png", ctx) if ctx else "./logo.png"
    footer_tagline = ctx.t("footer_tagline") if ctx else "Lasting Taste of Earth"

    return f"""  <footer class="footer">
    <img class="footer-logo" src="{footer_logo_src}" alt="Eco Natural">
    <p class="footer-tagline">{escape(footer_tagline)}</p>{back_link}
  </footer>"""


def _wa_href(product_name: str, ctx: Ctx | None = None) -> str:
    num = WA_NUMBER.replace("+", "").replace(" ", "")
    if ctx:
        msg_template = ctx.t("wa_product_message")
        msg = quote(msg_template.format(product_name=product_name))
    else:
        msg = quote(f"Hello, I'm interested in {product_name}")
    return f"https://wa.me/{num}?text={msg}"


def _cat_slug(cat: str) -> str:
    import re
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


# ── HTML helper builders ───────────────────────────────────────────────────

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
            f'<div class="use-tile" data-reveal>'
            f'<div class="use-emoji" aria-hidden="true">{emoji}</div>'
            f'<div class="use-label">{escape(label)}</div>'
            f'</div>'
        )
    return "\n        ".join(parts)


def _quality_cards_html(badges: list[tuple]) -> str:
    parts = []
    for emoji, name, desc in badges:
        parts.append(
            f'<div class="quality-card" data-reveal>'
            f'<div class="quality-emoji" aria-hidden="true">{emoji}</div>'
            f'<div class="quality-name">{escape(name)}</div>'
            f'<div class="quality-desc">{escape(desc)}</div>'
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
        localized_image_path = _localize_path(image_path, ctx) if ctx else image_path
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


# ── Product page template ──────────────────────────────────────────────────

def page_template(row: dict, related: list | None, img_dir, *, ctx: Ctx | None = None) -> str:
    product_id   = row["product_id"].strip()
    page_title   = row["page_title"].strip()
    slug         = row["slug"].strip()
    meta_desc    = row["meta_description"].strip()
    seo_title    = row["seo_title"].strip()
    full_desc    = row["full_description"].strip()
    short_desc   = row["short_description"].strip()

    image_path, adjustments = resolved_asset(product_id)
    localized_image_path = _localize_path(image_path, ctx) if ctx else image_path
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
    inquire_on_whatsapp = ctx.t("inquire_on_whatsapp") if ctx else "Inquire on WhatsApp"
    order_via_whatsapp = ctx.t("order_via_whatsapp") if ctx else "Order via WhatsApp"
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

    all_products_link = _localize_path("./index.html", ctx) if ctx else "./index.html"

    return f"""<!doctype html>
<html lang="{lang_attr}">
{_document_head(f"{seo_title or page_title} | Eco Natural", meta_desc, ctx=ctx, json_ld=json_ld, extra_links=head_links)}
<body>

{_topbar(ctx=ctx, slug=slug)}

  <nav class="breadcrumb" aria-label="{breadcrumb_label}">
    <div class="breadcrumb-inner">
      <a href="{all_products_link}">{all_products_text}</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">{escape(_category(product_id))}</span>
    </div>
  </nav>

  <a class="sticky-wa" id="sticky-wa" aria-hidden="true">
    {_WA_SVG}
    <span>{order_via_whatsapp}</span>
  </a>

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
      <a class="btn-wa" href="{_wa_href(page_title, ctx=ctx)}">
        {_WA_SVG}
        {inquire_on_whatsapp}
      </a>
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

    <div class="section" data-reveal>
      <div class="eyebrow">{escape(origin_story_eyebrow)}</div>
      <div class="story-card">
        <div class="origin-chip">&#128205; {escape(origin_place)}</div>
        {_flavor_chips_html(flavor_notes)}
        {_story_html(story_paras)}
      </div>
    </div>

    <div class="section" data-reveal>
      <div class="eyebrow">{escape(how_to_enjoy_eyebrow)}</div>
      <div class="section-heading">{escape(how_to_enjoy_heading)}</div>
      <div class="use-grid">
        {_use_tiles_html(how_to_use)}
      </div>
    </div>

    <div class="section" data-reveal>
      <div class="eyebrow">{escape(quality_eyebrow)}</div>
      <div class="section-heading">{escape(quality_heading)}</div>
      <div class="quality-grid">
        {_quality_cards_html(badges)}
      </div>
    </div>

    {storage_block}

    {related_html_block}

  </div>

{_footer(ctx=ctx, show_back_link=True)}

  {_REVEAL_JS}
  {_STICKY_WA_JS}
  {_ROUTE_PREFETCH_JS}

</body>
</html>
"""


# ── Index / landing page template ─────────────────────────────────────────

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
    logo_src = _localize_path("./logo.png", ctx) if ctx else "./logo.png"
    preload_links: list[str] = [f'<link rel="preload" as="image" href="{logo_src}">']
    eager_card_limit = 4
    eager_card_index = 0
    learn_more_text = ctx.t("learn_more") if ctx else "Learn More →"
    gift_chip_text = ctx.t("gift_chip") if ctx else "Gift"

    for cat, entries in ordered_groups:
        cards = ""
        for fn, title, pid in entries:
            image_path, adjustments = resolved_asset(pid)
            card_image_path, card_srcset, card_sizes = card_image_sources(pid)
            localized_card_image_path = _localize_path(card_image_path, ctx) if ctx else card_image_path
            localized_card_srcset = _localize_srcset(card_srcset, ctx) if ctx else card_srcset
            image_style = inline_adjustment_vars(adjustments)
            image_width, image_height = asset_dimensions(image_path)

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
        <a class="product-card" href="{escape(fn)}" data-reveal data-prefetch-route>
          <div class="card-img-wrap" style="{image_style}">
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

    wa_num = WA_NUMBER.replace('+','').replace(' ','')
    if ctx:
        wa_msg = ctx.t("wa_index_message")
        wa_href_index = f"https://wa.me/{wa_num}?text={quote(wa_msg)}"
    else:
        wa_href_index = f"https://wa.me/{wa_num}?text=Hello%2C%20I%27d%20like%20to%20order%20Eco%20Natural%20products"

    # Localized strings
    index_title = ctx.t("index_title") if ctx else "Eco Natural — Lasting Taste of Earth"
    index_meta_desc = ctx.t("index_meta_description", count=len(items)) if ctx else f"Village-origin cold-pressed natural food extracts from Büyük Çaltıcak, Aegean Turkey. {len(items)} artisan products."
    hero_tagline = ctx.t("hero_tagline") if ctx else "Lasting Taste of Earth"
    cat_nav_label = ctx.t("cat_nav_label") if ctx else "Product categories"
    find_us_eyebrow = ctx.t("find_us_eyebrow") if ctx else "Find Us"
    find_us_heading = ctx.t("find_us_heading") if ctx else "Order Direct"
    find_us_body = ctx.t("find_us_body") if ctx else "Scan a product barcode to learn more, or reach us directly on WhatsApp to place an order, ask about availability, or get help choosing the right product for you."
    chat_on_whatsapp = ctx.t("chat_on_whatsapp") if ctx else "Chat on WhatsApp"
    find_us_note = ctx.t("find_us_note") if ctx else "We speak Turkish, English and can help in Russian."
    footer_tagline = ctx.t("footer_tagline") if ctx else "Lasting Taste of Earth"
    footer_sub = ctx.t("footer_sub") if ctx else "Eco Natural · Aegean Turkey"

    # Stamps from locales
    stamps = ctx.strings.get("stamps", ["%100 Natural", "Cold Press", "Katkısız", "Büyük Çaltıcak", "Glass Bottle"]) if ctx else ["%100 Natural", "Cold Press", "Katkısız", "Büyük Çaltıcak", "Glass Bottle"]
    stamps_html = "\n        ".join(f'<div class="stamp">{escape(s)}</div>' for s in stamps)

    lang_attr = ctx.locale if ctx else "en"

    return f"""<!doctype html>
<html lang="{lang_attr}">
{_document_head(index_title, index_meta_desc, ctx=ctx, extra_links=preload_links)}
<body>

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

  <section class="find-us">
    <div class="find-us-inner">
      <div class="eyebrow" style="justify-content:center;">{escape(find_us_eyebrow)}</div>
      <h2 class="find-us-heading" data-reveal>{escape(find_us_heading)}</h2>
      <p class="find-us-body" data-reveal>
        {find_us_body}
      </p>
      <a class="btn-wa" href="{wa_href_index}" data-reveal>
        {_WA_SVG}
        {chat_on_whatsapp}
      </a>
      <p class="find-us-note" data-reveal>{escape(find_us_note)}</p>
    </div>
  </section>

{_footer(ctx=ctx)}

  {_REVEAL_JS}
  {_ROUTE_PREFETCH_JS}

</body>
</html>
"""
