import json
from html import escape
from urllib.parse import quote

from enrichment import ENRICHMENT, _category
from image_assets import inline_adjustment_vars, resolved_asset
from styles import FONTS_LINK, CSS_PRODUCT, CSS_INDEX

WA_NUMBER = "+900000000000"  # placeholder — replace with real number before going live

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
  var io = new IntersectionObserver(function(entries){
    entries.forEach(function(e){
      if(e.isIntersecting){
        e.target.classList.add('revealed');
        io.unobserve(e.target);
      }
    });
  }, {threshold: 0.12});
  els.forEach(function(el, i){
    el.style.transitionDelay = (i * 100) + 'ms';
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


def _wa_href(product_name: str) -> str:
    num = WA_NUMBER.replace("+", "").replace(" ", "")
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
            f'{escape(name)}'
            f'</div>'
        )
    return "\n          ".join(parts)


def _use_tiles_html(uses: list[tuple]) -> str:
    parts = []
    for emoji, label in uses:
        parts.append(
            f'<div class="use-tile" data-reveal>'
            f'<div class="use-label">{escape(label)}</div>'
            f'</div>'
        )
    return "\n        ".join(parts)


def _quality_cards_html(badges: list[tuple]) -> str:
    parts = []
    for emoji, name, desc in badges:
        parts.append(
            f'<div class="quality-card" data-reveal>'
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


def _related_html(related: list[tuple], img_dir) -> str:
    parts = []
    for slug, title, pid in related[:4]:
        image_path, adjustments = resolved_asset(pid)
        style_attr = inline_adjustment_vars(adjustments)
        parts.append(
            f'<a class="related-card" href="{escape(slug)}">'
            f'<div class="related-img-stage" style="{style_attr}">'
            f'<img class="product-asset" src="{escape(image_path)}" alt="{escape(title)}" loading="lazy">'
            f'</div>'
            f'<div class="related-name">{escape(title)}</div>'
            f'</a>'
        )
    return "\n        ".join(parts)


# ── Product page template ──────────────────────────────────────────────────

def page_template(row: dict, related: list | None, img_dir) -> str:
    product_id   = row["product_id"].strip()
    page_title   = row["page_title"].strip()
    meta_desc    = row["meta_description"].strip()
    seo_title    = row["seo_title"].strip()
    full_desc    = row["full_description"].strip()
    short_desc   = row["short_description"].strip()

    image_path, adjustments = resolved_asset(product_id)
    image_style = inline_adjustment_vars(adjustments)

    enrich       = ENRICHMENT.get(product_id, {})
    origin_place = enrich.get("origin_place", "Turkey")
    story_paras  = enrich.get("story", [full_desc])
    how_to_use   = enrich.get("how_to_use", [
        ("🍽️", "Cooking"),  ("🥗", "Salads"),
        ("🫙", "Finishing"), ("🎁", "Gifting"),
        ("🍞", "Serving"),   ("🧴", "Daily Use"),
    ])
    badges       = enrich.get("badges", [
        ("✅", "Natural",      "Pure natural ingredients"),
        ("🌱", "Plant-Based",  "100% plant origin"),
        ("🚫", "No Additives", "Nothing synthetic"),
        ("📍", "Turkish Origin","Made in Turkey"),
        ("⭐", "Premium",      "Curated quality range"),
    ])
    is_gift      = enrich.get("is_gift", False)
    product_line = enrich.get("product_line", "Eco Natural")
    tagline      = enrich.get("tagline", short_desc)
    ghost_word   = _category_ghost_word(product_id)

    gift_banner = (
        '<div class="gift-banner" data-reveal>Makes a beautiful gift — perfect for food lovers</div>'
        if is_gift else ""
    )

    json_ld = json.dumps({
        "@context": "https://schema.org",
        "@type": "Product",
        "name": page_title,
        "description": meta_desc,
        "sku": product_id,
        "image": image_path,
        "brand": {"@type": "Brand", "name": "Eco Natural"},
    }, ensure_ascii=False, indent=2)

    related_items = related or []
    related_html_block = ""
    if related_items:
        related_html_block = f"""
    <div class="section" data-reveal>
      <div class="eyebrow">More Like This</div>
      <div class="related-grid">
        {_related_html(related_items, img_dir)}
      </div>
    </div>"""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(seo_title or page_title)} | Eco Natural</title>
  <meta name="description" content="{escape(meta_desc)}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS_LINK}" rel="stylesheet">
  <link rel="stylesheet" href="style.css">
  <script type="application/ld+json">
{json_ld}
  </script>
</head>
<body>

  <nav class="topbar">
    <div class="topbar-left">
      <img class="topbar-logo" src="./logo.png" alt="Eco Natural">
      <span class="topbar-brand">ECO NATURAL</span>
    </div>
    <a class="topbar-back" href="./index.html">&#8592; All Products</a>
  </nav>

  <nav class="breadcrumb" aria-label="Breadcrumb">
    <div class="breadcrumb-inner">
      <a href="./index.html">All Products</a>
      <span aria-hidden="true">›</span>
      <span aria-current="page">{escape(_category(product_id))}</span>
    </div>
  </nav>

  <a class="sticky-wa" id="sticky-wa" aria-hidden="true">
    {_WA_SVG}
    <span>Order via WhatsApp</span>
  </a>

  <section class="hero">
    <div class="hero-ghost" aria-hidden="true">{escape(ghost_word)}</div>
    <div class="hero-img-wrap">
      <div class="hero-img-stage" style="{image_style}">
        <img class="product-asset" src="{image_path}" alt="{escape(page_title)}">
      </div>
    </div>
    <div class="hero-copy">
      <div class="hero-eyebrow">{escape(product_line)}</div>
      <h1>{escape(page_title)}</h1>
      <p class="tagline">{escape(tagline)}</p>
      <a class="btn-wa" href="{_wa_href(page_title)}">
        {_WA_SVG}
        Inquire on WhatsApp
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

  <div class="trust-strip">
    <div class="trust-strip-inner">
      {_trust_strip_html(badges)}
    </div>
  </div>

  {_torn("#F6FAF4")}

  <div class="wrap">

    <div class="section" data-reveal>
      <div class="eyebrow">Origin &amp; Story</div>
      <div class="story-card">
        <div class="origin-chip">&#128205; {escape(origin_place)}</div>
        {_story_html(story_paras)}
      </div>
    </div>

    <div class="section" data-reveal>
      <div class="eyebrow">How to Enjoy</div>
      <div class="section-heading">Six ways to use it at home</div>
      <div class="use-grid">
        {_use_tiles_html(how_to_use)}
      </div>
    </div>

    <div class="section" data-reveal>
      <div class="eyebrow">Quality &amp; Standards</div>
      <div class="section-heading">What makes it exceptional</div>
      <div class="quality-grid">
        {_quality_cards_html(badges)}
      </div>
    </div>

    {related_html_block}

  </div>

  <footer class="footer">
    <p class="footer-tagline">Lasting Taste of Earth</p>
    <a href="./index.html">&#8592; Back to All Products</a>
    <p class="footer-sub">Eco Natural</p>
  </footer>

  {_REVEAL_JS}
  {_STICKY_WA_JS}

</body>
</html>
"""


# ── Index / landing page template ─────────────────────────────────────────

def index_template(items: list[tuple[str, str, str]], enrichment_map: dict, img_dir) -> str:
    from pathlib import Path

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
        f'<a href="#{_cat_slug(cat)}">{escape(cat)}</a>'
        for cat, _ in ordered_groups
    )

    sections_html = ""
    for cat, entries in ordered_groups:
        cards = ""
        for fn, title, pid in entries:
            image_path, adjustments = resolved_asset(pid)
            image_style = inline_adjustment_vars(adjustments)
            enrich  = enrichment_map.get(pid, {})
            desc    = enrich.get("tagline", "")
            is_gift = enrich.get("is_gift", False)
            gift_chip = '<div class="card-gift">Gift</div>' if is_gift else ""
            cards += f"""
        <a class="product-card" href="{escape(fn)}" data-reveal>
          <div class="card-img-wrap" style="{image_style}">
            <div class="card-img-stage">
              <img class="product-asset" src="{escape(image_path)}" alt="{escape(title)}" loading="lazy">
            </div>
          </div>
          <div class="card-body">
            <div class="card-category">{escape(cat)}</div>
            <div class="card-name">{escape(title)}</div>
            <div class="card-desc">{escape(desc)}</div>
            {gift_chip}
            <div class="card-cta">Learn More &#8594;</div>
          </div>
        </a>"""

        sections_html += f"""
    <div class="catalog-section" id="{_cat_slug(cat)}">
      <div class="eyebrow">{escape(cat)}</div>
      <div class="product-grid">
        {cards}
      </div>
    </div>"""

    wa_href_index = f"https://wa.me/{WA_NUMBER.replace('+','').replace(' ','')}?text=Hello%2C%20I%27d%20like%20to%20order%20Eco%20Natural%20products"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Eco Natural — Lasting Taste of Earth</title>
  <meta name="description" content="Village-origin cold-pressed natural food extracts from B&uuml;y&uuml;k &Ccedil;alt&#305;cak, Aegean Turkey. {len(items)} artisan products.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="{FONTS_LINK}" rel="stylesheet">
  <style>{CSS_INDEX}</style>
</head>
<body>

  <nav class="topbar">
    <div class="topbar-left">
      <img class="topbar-logo" src="./logo.png" alt="Eco Natural">
      <div class="topbar-lockup">
        <span class="topbar-brand">ECO NATURAL</span>
        <span class="topbar-sub">B&uuml;y&uuml;k &Ccedil;alt&#305;cak &middot; Ayd&#305;n</span>
      </div>
    </div>
  </nav>

  <section class="hero">
    <div class="hero-ghost" aria-hidden="true">ECO</div>
    <div class="hero-content">
      <img class="hero-logo" src="./logo.png" alt="Eco Natural">
      <h1 data-reveal>Eco Natural</h1>
      <p class="hero-tagline" data-reveal><em>Lasting Taste of Earth</em></p>
      <div class="stamp-row" data-reveal>
        <div class="stamp">%100 Natural</div>
        <div class="stamp">Cold Press</div>
        <div class="stamp">Katkısız</div>
        <div class="stamp">Büyük Çaltıcak</div>
        <div class="stamp">Glass Bottle</div>
      </div>
    </div>
  </section>

  {_torn("#F6FAF4")}

  <nav class="cat-nav" aria-label="Product categories">
    {cat_nav_html}
  </nav>

  {sections_html}

  <section class="find-us">
    <div class="find-us-inner">
      <div class="eyebrow" style="justify-content:center;">Find Us</div>
      <h2 class="find-us-heading" data-reveal>Order Direct</h2>
      <p class="find-us-body" data-reveal>
        Scan a product barcode to learn more, or reach us directly on WhatsApp to place an order,
        ask about availability, or get help choosing the right product for you.
      </p>
      <a class="btn-wa" href="{wa_href_index}" data-reveal>
        {_WA_SVG}
        Chat on WhatsApp
      </a>
      <p class="find-us-note" data-reveal>We speak Turkish, English and can help in Russian.</p>
    </div>
  </section>

  <footer class="footer">
    <p class="footer-tagline"><em>Lasting Taste of Earth</em></p>
    <p class="footer-sub">Eco Natural &middot; Aegean Turkey</p>
  </footer>

  {_REVEAL_JS}

</body>
</html>
"""
