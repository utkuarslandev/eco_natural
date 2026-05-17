from __future__ import annotations

from context import Ctx, localize_path
from css.tokens import FONTS_LINK
from html.escaping import escape

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
_TORN_BARK = _torn("#1A3520")

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
        stylesheet_href = localize_path(stylesheet_href, ctx)
        favicon_href = localize_path(favicon_href, ctx)

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
            back_link_href = localize_path("./index.html", ctx)
        else:
            back_link_text = "&#8592; All Products"
            back_link_href = "./index.html"
        back_link = f'\n    <a class="topbar-back" href="{back_link_href}">{back_link_text}</a>'

    logo_src = localize_path("./logo.png", ctx) if ctx else "./logo.png"
    home_href = localize_path("./index.html", ctx) if ctx else "./index.html"

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
        back_link_href = localize_path("./index.html", ctx) if ctx else "./index.html"
        back_link = f'\n    <a href="{back_link_href}">{back_footer_text}</a>'

    footer_logo_src = localize_path("./logo.png", ctx) if ctx else "./logo.png"
    footer_tagline = ctx.t("footer_tagline") if ctx else "Lasting Taste of Earth"

    return f"""  <footer class="footer">
    <img class="footer-logo" src="{footer_logo_src}" alt="Eco Natural">
    <p class="footer-tagline">{escape(footer_tagline)}</p>{back_link}
  </footer>"""

