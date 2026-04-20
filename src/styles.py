GRAIN_SVG = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='300' height='300'%3E"
    "%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.75' "
    "numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E"
    "%3Crect width='300' height='300' filter='url(%23n)' opacity='1'/%3E%3C/svg%3E"
)

FONTS_LINK = (
    "https://fonts.googleapis.com/css2?"
    "family=Cinzel:wght@400;600&"
    "family=Abril+Fatface&"
    "family=EB+Garamond:ital@1&"
    "family=Raleway:wght@300;400;600&display=swap"
)

CSS_PRODUCT = f"""
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --parch:      #F6FAF4;
  --parch-lt:   #FFFFFF;
  --parch-dk:   #D4E8CC;
  --bark:       #1A3520;
  --bark-mid:   #243D2A;
  --terra:      #2E5E38;
  --terra-lt:   #5D9B3A;
  --terra-dk:   #1A3520;
  --olive:      #1A3520;
  --olive-lt:   #2E5E38;
  --gold:       #C09010;
  --gold-lt:    #D4A820;
  --gold-pale:  #EDD87A;
  --text:       #1A2E1A;
  --text-mid:   #2D4E30;
  --text-soft:  #5A7A5C;
  --section-pad: clamp(5rem, 8vw, 9rem);
  --container:   min(100% - 3rem, 1200px);
  --card-pad:    1.8rem;
  --grid-gap:    2rem;
  --eyebrow-mb:  1.2rem;
}}

body {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  background: var(--parch);
  color: var(--text-mid);
  line-height: 1.9;
  -webkit-font-smoothing: antialiased;
}}

body::before {{
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.4;
  mix-blend-mode: soft-light;
  background-image: url("{GRAIN_SVG}");
  background-repeat: repeat;
}}

/* ── Navigation ─────────────────────────────────────────────────────────── */

.topbar {{
  background: var(--bark);
  padding: 12px 20px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 2px solid var(--gold);
}}
.topbar-home {{ display: flex; align-items: center; gap: 12px; text-decoration: none; }}
.topbar-logo {{
  width: 44px;
  height: 44px;
  display: block;
  object-fit: contain;
  object-position: center center;
}}
.topbar-brand {{
  font-family: 'Cinzel', serif;
  font-weight: 400;
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  color: var(--gold-pale);
}}
.topbar-sub {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: 0.58rem;
  letter-spacing: 0.15em;
  color: rgba(240,216,152,0.5);
  line-height: 1;
}}
.topbar-back {{
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gold-pale);
  opacity: 0.65;
  text-decoration: none;
  transition: opacity 0.2s;
}}
.topbar-back:hover {{ opacity: 1; }}

.lang-switcher {{
  display: flex;
  gap: 0.4rem;
  margin-left: auto;
  align-items: center;
}}
.lang-item {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.6rem;
  letter-spacing: 0.1em;
  color: var(--gold-pale);
  opacity: 0.6;
  text-decoration: none;
  padding: 0.2rem 0.3rem;
  transition: opacity 0.2s;
}}
.lang-item:hover {{
  opacity: 1;
}}
.lang-item--active {{
  opacity: 1;
  border-bottom: 1px solid currentColor;
}}

.breadcrumb {{
  background: var(--parch-lt);
  border-bottom: 1px solid var(--parch-dk);
  padding: 9px 20px;
}}
.breadcrumb-inner {{
  max-width: var(--container);
  margin: 0 auto;
  display: flex;
  align-items: center;
  gap: 6px;
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--text-soft);
}}
.breadcrumb-inner a {{ color: var(--terra); text-decoration: none; }}
.breadcrumb-inner a:hover {{ text-decoration: underline; }}
.breadcrumb-inner [aria-current="page"] {{ color: var(--text-mid); }}

/* ── Eyebrow ─────────────────────────────────────────────────────────────── */

.eyebrow {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.62rem;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: var(--terra);
  margin-bottom: var(--eyebrow-mb);
  display: flex;
  align-items: center;
  gap: 0.5em;
}}
.eyebrow::before {{
  content: '──';
  color: var(--gold);
  letter-spacing: -0.05em;
}}

/* ── Hero ────────────────────────────────────────────────────────────────── */

.hero {{
  background: var(--bark);
  min-height: 85vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-end;
  padding: 40px 20px 48px;
  text-align: center;
  position: relative;
  overflow: hidden;
}}
@media (min-width: 768px) {{ .hero {{ min-height: 70vh; }} }}

.hero-ghost {{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'Abril Fatface', serif;
  font-size: clamp(10rem, 20vw, 28rem);
  color: var(--gold-pale);
  opacity: 0.04;
  user-select: none;
  pointer-events: none;
  white-space: nowrap;
  line-height: 1;
}}

.hero-img-wrap {{
  width: 100%;
  display: flex;
  justify-content: center;
  margin-bottom: 32px;
  position: relative;
  z-index: 1;
}}
.hero-img-stage {{
  width: min(85%, 520px);
  display: flex;
  align-items: center;
  justify-content: center;
  animation: riseIn 0.75s cubic-bezier(0.16,1,0.3,1) both;
}}
.hero-img-wrap img {{
  max-height: 420px;
  max-width: 100%;
  width: auto;
  display: block;
  filter: drop-shadow(0 20px 40px rgba(0,0,0,0.6)) drop-shadow(0 0 30px rgba(196,144,16,0.15));
}}

.product-asset {{
  transform:
    translate(var(--img-offset-x, 0px), var(--img-offset-y, 0px))
    rotate(var(--img-rotation, 0deg))
    scale(var(--img-scale, 1));
  transform-origin: center center;
}}

@keyframes riseIn {{
  from {{ transform: translateY(32px); opacity: 0; }}
  to   {{ transform: translateY(0);    opacity: 1; }}
}}

.hero-copy {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 16px;
  max-width: 580px;
  position: relative;
  z-index: 1;
}}

.hero-eyebrow {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.62rem;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: var(--terra-lt);
}}

.hero h1 {{
  font-family: 'Cinzel', serif;
  font-size: clamp(1.4rem, 5vw, 2.4rem);
  font-weight: 400;
  line-height: 1.2;
  color: var(--gold-pale);
}}

.hero .tagline {{
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: clamp(1rem, 1.8vw, 1.3rem);
  color: var(--gold-pale);
  opacity: 0.85;
}}

/* ── Rubber Stamp Badges ─────────────────────────────────────────────────── */

.stamp-row {{
  display: flex;
  flex-wrap: wrap;
  gap: 12px;
  justify-content: center;
}}

.stamp {{
  width: 82px;
  height: 82px;
  border-radius: 50%;
  border: 2px solid var(--gold);
  outline: 2px dashed var(--gold);
  outline-offset: -9px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-family: 'Raleway', sans-serif;
  font-size: 0.52rem;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gold-pale);
  padding: 16px 8px;
  line-height: 1.3;
  gap: 3px;
  flex-shrink: 0;
}}

/* ── Gift Banner ─────────────────────────────────────────────────────────── */

.gift-banner {{
  background: rgba(196,144,16,0.15);
  border: 1px solid rgba(196,144,16,0.35);
  border-radius: 6px;
  padding: 10px 18px;
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.72rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gold-pale);
  display: flex;
  align-items: center;
  gap: 8px;
}}

/* ── WhatsApp CTA Button ─────────────────────────────────────────────────── */

.btn-wa {{
  display: inline-flex;
  align-items: center;
  gap: 9px;
  background: var(--terra);
  color: var(--parch-lt);
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  padding: 14px 32px;
  border-radius: 99px;
  text-decoration: none;
  position: relative;
  overflow: hidden;
  transition: background 0.35s cubic-bezier(0.16,1,0.3,1), transform 0.2s;
}}
.btn-wa:hover {{
  background: var(--terra-lt);
  transform: translateY(-2px);
}}
.btn-wa:active {{ background: var(--terra-dk); transform: none; }}
.btn-wa svg {{ flex-shrink: 0; }}

/* ── Torn Paper Dividers ─────────────────────────────────────────────────── */

.torn {{
  display: block;
  width: 100%;
  height: 28px;
  overflow: hidden;
  line-height: 0;
}}
.torn svg {{ width: 100%; height: 100%; display: block; }}

/* ── Trust Strip ─────────────────────────────────────────────────────────── */

.trust-strip {{
  background: var(--olive);
  padding: 28px 20px;
}}
.trust-strip-inner {{
  max-width: var(--container);
  margin: 0 auto;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  overflow-x: visible;
  gap: 0;
}}
.trust-item {{
  flex: 1 0 140px;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  padding: 14px 18px;
  border-right: 1px solid rgba(240,216,152,0.15);
  gap: 7px;
}}
.trust-item:last-child {{ border-right: none; }}
.trust-label {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.62rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--gold-pale);
}}
.trust-desc {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: 0.72rem;
  color: rgba(240,216,152,0.7);
  line-height: 1.5;
}}

/* ── Main Wrap ───────────────────────────────────────────────────────────── */

.wrap {{
  max-width: var(--container);
  margin: 0 auto;
  padding: 0 20px clamp(4rem, 8vw, 7rem);
}}

.section {{
  padding-top: clamp(3rem, 6vw, 5rem);
}}

.section-heading {{
  font-family: 'Abril Fatface', serif;
  font-size: clamp(1.2rem, 2.5vw, 1.8rem);
  font-weight: 400;
  color: var(--bark);
  margin-bottom: 1.5rem;
  line-height: 1.2;
}}

/* ── Story Card ──────────────────────────────────────────────────────────── */

.story-card {{
  background: var(--bark);
  color: var(--gold-pale);
  border-radius: 12px;
  padding: clamp(1.8rem, 4vw, 2.8rem);
  position: relative;
  overflow: hidden;
}}
.story-card::before {{
  content: '\\201C';
  position: absolute;
  top: -24px;
  left: 16px;
  font-size: 140px;
  color: var(--gold);
  opacity: 0.12;
  font-family: 'EB Garamond', serif;
  line-height: 1;
  pointer-events: none;
}}
.origin-chip {{
  display: inline-flex;
  align-items: center;
  gap: 6px;
  background: rgba(240,216,152,0.1);
  border: 1px solid rgba(240,216,152,0.2);
  border-radius: 99px;
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  padding: 5px 14px;
  color: var(--gold-pale);
  margin-bottom: 20px;
}}
.story-card p {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: clamp(0.88rem, 1.1vw, 0.98rem);
  line-height: 1.9;
  position: relative;
  color: var(--gold-pale);
  opacity: 0.9;
}}
.story-card p + p {{ margin-top: 1.2rem; }}

/* ── How To Use Grid ─────────────────────────────────────────────────────── */

.use-grid {{
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
}}
@media (min-width: 600px) {{ .use-grid {{ grid-template-columns: repeat(6, 1fr); }} }}

.use-tile {{
  background: var(--parch-lt);
  border: 1px solid var(--parch-dk);
  border-top: 3px solid var(--terra);
  border-radius: 8px;
  padding: 18px 10px 14px;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  transition: border-top-color 0.2s, transform 0.2s;
  justify-content: center;
}}
.use-tile:hover {{
  border-top-color: var(--terra-dk);
  transform: translateY(-3px);
}}
.use-label {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.6rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--text-mid);
  line-height: 1.35;
}}

/* ── Quality Grid ────────────────────────────────────────────────────────── */

.quality-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 10px;
}}
@media (min-width: 480px) {{ .quality-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
@media (min-width: 720px) {{ .quality-grid {{ grid-template-columns: repeat(5, 1fr); }} }}

.quality-card {{
  background: var(--parch-lt);
  border: 1px solid var(--parch-dk);
  border-radius: 8px;
  padding: 18px 14px 16px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  text-align: center;
}}
.quality-name {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.62rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--bark);
  line-height: 1.3;
}}
.quality-desc {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: 0.72rem;
  color: var(--text-soft);
  line-height: 1.5;
}}

/* ── Related Products ────────────────────────────────────────────────────── */

.related-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 12px;
}}
@media (min-width: 480px) {{ .related-grid {{ grid-template-columns: repeat(4, 1fr); }} }}

.related-card {{
  background: var(--parch-lt);
  border: 1px solid var(--parch-dk);
  border-radius: 8px;
  padding: 16px;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 10px;
  transition: border-color 0.2s, transform 0.2s;
}}
.related-card:hover {{
  border-color: var(--terra);
  transform: translateY(-3px);
}}
.related-card img {{
  width: 80px;
  height: 80px;
  object-fit: contain;
}}
.related-img-stage {{
  width: 80px;
  height: 80px;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.related-name {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.62rem;
  letter-spacing: 0.1em;
  color: var(--text-mid);
  text-align: center;
  line-height: 1.4;
}}

/* ── Credentials Strip ───────────────────────────────────────────────────── */

.credentials-strip {{
  background: var(--bark);
  padding: 24px 20px 28px;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 14px;
}}

/* ── Sticky WhatsApp Bar ─────────────────────────────────────────────────── */

.sticky-wa {{
  position: fixed;
  bottom: 0; left: 0; right: 0;
  background: var(--terra);
  color: var(--parch-lt);
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.72rem;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  padding: 14px 24px;
  display: none;
  align-items: center;
  justify-content: center;
  gap: 10px;
  z-index: 200;
  text-decoration: none;
  border-top: 1px solid var(--terra-lt);
}}
.sticky-wa.visible {{ display: flex; }}
@media (min-width: 768px) {{ .sticky-wa {{ display: none !important; }} }}

/* ── Footer ──────────────────────────────────────────────────────────────── */

.footer {{
  background: var(--bark-mid);
  text-align: center;
  padding: clamp(2.5rem, 5vw, 4rem) 20px;
  margin-top: 0;
}}
.footer-logo {{
  width: 76px;
  height: 76px;
  display: block;
  object-fit: contain;
  object-position: center center;
  margin: 0 auto 1rem;
  filter: drop-shadow(0 4px 16px rgba(0,0,0,0.28));
}}
.footer-tagline {{
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: clamp(1.1rem, 1.8vw, 1.4rem);
  color: var(--gold-pale);
  margin-bottom: 1.2rem;
}}
.footer a {{
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  font-size: 0.65rem;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--terra-lt);
  text-decoration: none;
  opacity: 0.8;
  transition: opacity 0.2s;
}}
.footer a:hover {{ opacity: 1; }}

/* ── Scroll hint ─────────────────────────────────────────────────────────── */

.scroll-hint {{
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  color: rgba(240,216,152,0.4);
  font-size: 18px;
  animation: pulse 2.5s ease-in-out infinite;
  z-index: 1;
}}
@keyframes pulse {{
  0%, 100% {{ opacity: 0.4; transform: translateX(-50%) translateY(0); }}
  50%       {{ opacity: 0.85; transform: translateX(-50%) translateY(5px); }}
}}

/* ── Reveal animation ────────────────────────────────────────────────────── */

[data-reveal] {{
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 750ms cubic-bezier(0.16,1,0.3,1),
              transform 750ms cubic-bezier(0.16,1,0.3,1);
}}
[data-reveal].revealed {{ opacity: 1; transform: none; }}

/* ── Stamp emoji display ─────────────────────────────────────────────────── */

.stamp {{ padding: 10px 6px; }}
.stamp-emoji {{ font-size: 1.4rem; line-height: 1; display: block; }}
.stamp-name {{
  font-family: 'Raleway', sans-serif;
  font-size: 0.48rem;
  font-weight: 600;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--gold-pale);
  line-height: 1.2;
  text-align: center;
}}

/* ── Use tile emoji ──────────────────────────────────────────────────────── */

.use-emoji {{ font-size: 1.8rem; line-height: 1; display: block; }}

/* ── Quality card emoji ──────────────────────────────────────────────────── */

.quality-emoji {{ font-size: 1.6rem; line-height: 1; display: block; margin-bottom: 2px; }}

/* ── Related card tagline ────────────────────────────────────────────────── */

.related-tagline {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: 0.6rem;
  color: var(--text-soft);
  line-height: 1.4;
  text-align: center;
  font-style: italic;
}}

/* ── Flavor profile chips (inside .story-card dark bg) ───────────────────── */

.flavor-chips {{
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin: 10px 0 16px;
}}
.flavor-chip {{
  background: rgba(240,216,152,0.12);
  border: 1px solid rgba(240,216,152,0.25);
  border-radius: 99px;
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.58rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--gold-pale);
  padding: 4px 12px;
  white-space: nowrap;
}}

/* ── Storage callout ─────────────────────────────────────────────────────── */

.storage-callout {{
  display: flex;
  align-items: flex-start;
  gap: 12px;
  background: var(--parch-lt);
  border: 1px solid var(--parch-dk);
  border-left: 3px solid var(--terra);
  border-radius: 6px;
  padding: 16px 20px;
}}
.storage-icon {{
  font-size: 1.2rem;
  line-height: 1;
  flex-shrink: 0;
  margin-top: 2px;
}}
.storage-text {{
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  font-size: 0.78rem;
  color: var(--text-mid);
  line-height: 1.7;
}}

/* ── Hero desktop split layout ───────────────────────────────────────────── */

@media (min-width: 900px) {{
  .hero {{
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    padding: 60px 48px 48px;
    gap: 48px;
    min-height: 75vh;
  }}
  .hero-img-wrap {{
    flex: 0 0 auto;
    width: 40%;
    max-width: 480px;
    margin-bottom: 0;
    order: 1;
  }}
  .hero-copy {{
    flex: 1 1 340px;
    max-width: 500px;
    align-items: flex-start;
    text-align: left;
    order: 2;
  }}
  .hero-ghost {{ display: none; }}
  .scroll-hint {{ order: 3; flex: 0 0 100%; }}
  .hero h1, .hero .tagline {{ text-align: left; }}
}}
"""


CSS_INDEX = f"""
*, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}

:root {{
  --parch:      #F6FAF4;
  --parch-lt:   #FFFFFF;
  --parch-dk:   #D4E8CC;
  --bark:       #1A3520;
  --bark-mid:   #243D2A;
  --terra:      #2E5E38;
  --terra-lt:   #5D9B3A;
  --terra-dk:   #1A3520;
  --olive:      #1A3520;
  --olive-lt:   #2E5E38;
  --gold:       #C09010;
  --gold-lt:    #D4A820;
  --gold-pale:  #EDD87A;
  --text:       #1A2E1A;
  --text-mid:   #2D4E30;
  --text-soft:  #5A7A5C;
  --section-pad: clamp(5rem, 8vw, 9rem);
  --container:   min(100% - 3rem, 1200px);
}}

body {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  background: var(--parch);
  color: var(--text-mid);
  line-height: 1.9;
  -webkit-font-smoothing: antialiased;
}}

body::before {{
  content: '';
  position: fixed;
  inset: 0;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.4;
  mix-blend-mode: soft-light;
  background-image: url("{GRAIN_SVG}");
  background-repeat: repeat;
}}

/* ── Nav ─────────────────────────────────────────────────────────────────── */

.topbar {{
  background: var(--bark);
  padding: 14px 24px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  position: sticky;
  top: 0;
  z-index: 100;
  border-bottom: 2px solid var(--gold);
}}
.topbar-home {{ display: flex; align-items: center; gap: 14px; text-decoration: none; }}
.topbar-logo {{
  width: 48px;
  height: 48px;
  display: block;
  object-fit: contain;
  object-position: center center;
}}
.topbar-lockup {{
  display: flex;
  flex-direction: column;
  gap: 1px;
}}
.topbar-brand {{
  font-family: 'Cinzel', serif;
  font-weight: 400;
  font-size: 0.65rem;
  letter-spacing: 0.12em;
  color: var(--gold-pale);
  line-height: 1;
}}
.topbar-sub {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: 0.58rem;
  letter-spacing: 0.15em;
  color: rgba(240,216,152,0.5);
  line-height: 1;
}}

/* ── Hero ────────────────────────────────────────────────────────────────── */

.hero {{
  background: var(--bark);
  min-height: 60vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: clamp(4rem, 8vw, 7rem) 24px;
  text-align: center;
  position: relative;
  overflow: hidden;
}}

.hero-ghost {{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'Abril Fatface', serif;
  font-size: clamp(10rem, 20vw, 28rem);
  color: var(--gold-pale);
  opacity: 0.04;
  user-select: none;
  pointer-events: none;
  white-space: nowrap;
  line-height: 1;
}}

.hero-content {{
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;
  max-width: 700px;
}}

.hero h1 {{
  font-family: 'Cinzel', serif;
  font-size: clamp(3rem, 7vw, 7rem);
  font-weight: 400;
  line-height: 1.05;
  color: var(--gold-pale);
  letter-spacing: 0.06em;
}}

.hero-tagline {{
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: clamp(1.2rem, 2vw, 1.5rem);
  color: var(--gold-pale);
  opacity: 0.8;
}}

.hero-sub {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: 0.82rem;
  letter-spacing: 0.1em;
  color: rgba(240,216,152,0.55);
  text-transform: uppercase;
}}

.stamp-row {{
  display: flex;
  flex-wrap: wrap;
  gap: 14px;
  justify-content: center;
  margin-top: 8px;
}}

.stamp {{
  width: 82px;
  height: 82px;
  border-radius: 50%;
  border: 2px solid var(--gold);
  outline: 2px dashed var(--gold);
  outline-offset: -9px;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  font-family: 'Raleway', sans-serif;
  font-size: 0.5rem;
  font-weight: 600;
  letter-spacing: 0.15em;
  text-transform: uppercase;
  color: var(--gold-pale);
  padding: 16px 8px;
  line-height: 1.3;
  gap: 3px;
  flex-shrink: 0;
}}

/* ── Hero logo ───────────────────────────────────────────────────────────── */

.hero-logo {{
  width: clamp(96px, 13vw, 132px);
  height: clamp(96px, 13vw, 132px);
  display: block;
  object-fit: contain;
  object-position: center center;
  filter: drop-shadow(0 4px 16px rgba(0,0,0,0.4));
  margin-bottom: 8px;
}}

/* ── Torn paper divider ──────────────────────────────────────────────────── */

.torn {{
  display: block;
  width: 100%;
  height: 28px;
  overflow: hidden;
  line-height: 0;
}}
.torn svg {{ width: 100%; height: 100%; display: block; }}

/* ── Eyebrow ─────────────────────────────────────────────────────────────── */

.eyebrow {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.62rem;
  letter-spacing: 0.35em;
  text-transform: uppercase;
  color: var(--terra);
  margin-bottom: 1.5rem;
  display: flex;
  align-items: center;
  gap: 0.5em;
}}
.eyebrow::before {{
  content: '──';
  color: var(--gold);
  letter-spacing: -0.05em;
}}

/* ── Product Grid ────────────────────────────────────────────────────────── */

.catalog-section {{
  padding: clamp(3rem, 6vw, 5rem) 24px 0;
  max-width: var(--container);
  margin: 0 auto;
}}

.product-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}}
@media (min-width: 600px) {{ .product-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
@media (min-width: 960px) {{ .product-grid {{ grid-template-columns: repeat(4, 1fr); }} }}

.product-card {{
  background: linear-gradient(160deg, var(--bark-mid) 0%, var(--bark) 100%);
  border: 1px solid rgba(196,144,16,0.15);
  border-radius: 12px;
  overflow: hidden;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  transition: transform 0.35s cubic-bezier(0.16,1,0.3,1), border-color 0.2s;
  position: relative;
}}
.product-card::after {{
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 3px;
  background: var(--terra);
  transform: scaleX(0);
  transform-origin: left;
  transition: transform 0.35s cubic-bezier(0.16,1,0.3,1);
}}
.product-card:hover {{ transform: translateY(-6px); border-color: rgba(196,144,16,0.35); }}
.product-card:hover::after {{ transform: scaleX(1); }}

.card-img-wrap {{
  padding: 24px 24px 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 160px;
}}
.card-img-stage {{
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}}
.card-img-wrap img {{
  max-height: 140px;
  max-width: 100%;
  width: auto;
  object-fit: contain;
  filter: drop-shadow(0 8px 20px rgba(0,0,0,0.5)) drop-shadow(0 0 12px rgba(196,144,16,0.1));
  transition: transform 0.35s cubic-bezier(0.16,1,0.3,1);
}}
.product-card:hover .card-img-wrap img {{
  transform:
    translate(var(--img-offset-x, 0px), calc(var(--img-offset-y, 0px) - 4px))
    rotate(var(--img-rotation, 0deg))
    scale(var(--img-scale, 1));
}}

.card-body {{
  padding: 0 18px 20px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
}}

.card-category {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.55rem;
  letter-spacing: 0.3em;
  text-transform: uppercase;
  color: var(--terra-lt);
}}

.card-name {{
  font-family: 'Abril Fatface', serif;
  font-size: clamp(0.9rem, 1.5vw, 1.05rem);
  font-weight: 400;
  line-height: 1.2;
  color: var(--gold-pale);
}}

.card-desc {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: 0.72rem;
  color: rgba(240,216,152,0.6);
  line-height: 1.6;
  flex: 1;
}}

.card-cta {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.62rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--terra-lt);
  margin-top: 4px;
}}

/* ── Find Us / WhatsApp section ──────────────────────────────────────────── */

.find-us {{
  background: var(--bark-mid);
  padding: clamp(4rem, 8vw, 7rem) 24px;
  text-align: center;
  margin-top: clamp(4rem, 8vw, 7rem);
}}
.find-us-inner {{
  max-width: 560px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 24px;
}}
.find-us-heading {{
  font-family: 'Abril Fatface', serif;
  font-size: clamp(1.6rem, 3vw, 2.4rem);
  font-weight: 400;
  color: var(--gold-pale);
  line-height: 1.2;
}}
.find-us-body {{
  font-family: 'Raleway', sans-serif;
  font-weight: 300;
  font-size: clamp(0.88rem, 1.1vw, 0.98rem);
  color: rgba(240,216,152,0.7);
  line-height: 1.9;
}}
.find-us-note {{
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: 1rem;
  color: rgba(240,216,152,0.5);
}}

.btn-wa {{
  display: inline-flex;
  align-items: center;
  gap: 10px;
  background: var(--terra);
  color: var(--parch-lt);
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.72rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  padding: 16px 36px;
  border-radius: 99px;
  text-decoration: none;
  transition: background 0.35s cubic-bezier(0.16,1,0.3,1), transform 0.2s;
}}
.btn-wa:hover {{ background: var(--terra-lt); transform: translateY(-2px); }}
.btn-wa:active {{ background: var(--terra-dk); transform: none; }}
.btn-wa svg {{ flex-shrink: 0; }}

/* ── Footer ──────────────────────────────────────────────────────────────── */

.footer {{
  background: var(--bark-mid);
  border-top: 1px solid rgba(196,144,16,0.12);
  text-align: center;
  padding: clamp(2.5rem, 5vw, 4rem) 24px;
}}
.footer-logo {{
  width: 82px;
  height: 82px;
  display: block;
  object-fit: contain;
  object-position: center center;
  margin: 0 auto 1rem;
  filter: drop-shadow(0 4px 16px rgba(0,0,0,0.4));
}}
.footer-tagline {{
  font-family: 'EB Garamond', serif;
  font-style: italic;
  font-size: clamp(1.2rem, 2vw, 1.5rem);
  color: var(--gold-pale);
  margin-bottom: 1rem;
}}

/* ── Category Nav ────────────────────────────────────────────────────────── */

.cat-nav {{
  position: sticky;
  top: 54px;
  z-index: 90;
  background: var(--parch-lt);
  border-bottom: 1px solid var(--parch-dk);
  padding: 10px 24px;
  display: flex;
  gap: 8px;
  overflow-x: auto;
  -webkit-overflow-scrolling: touch;
  scrollbar-width: none;
}}
.cat-nav::-webkit-scrollbar {{ display: none; }}
.cat-nav a {{
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.6rem;
  letter-spacing: 0.2em;
  text-transform: uppercase;
  color: var(--text-mid);
  text-decoration: none;
  white-space: nowrap;
  padding: 6px 14px;
  border-radius: 99px;
  border: 1px solid var(--parch-dk);
  transition: background 0.2s, color 0.2s;
}}
.cat-nav a:hover {{
  background: var(--terra);
  color: var(--parch-lt);
  border-color: var(--terra);
}}

/* ── Gift chip on cards ──────────────────────────────────────────────────── */

.card-gift {{
  display: inline-block;
  font-family: 'Raleway', sans-serif;
  font-weight: 600;
  font-size: 0.52rem;
  letter-spacing: 0.25em;
  text-transform: uppercase;
  color: var(--gold);
  border: 1px solid var(--gold);
  border-radius: 99px;
  padding: 3px 10px;
  margin-top: 4px;
  align-self: flex-start;
}}

/* ── Reveal animation ────────────────────────────────────────────────────── */

[data-reveal] {{
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 750ms cubic-bezier(0.16,1,0.3,1),
              transform 750ms cubic-bezier(0.16,1,0.3,1);
}}
[data-reveal].revealed {{ opacity: 1; transform: none; }}
"""


CSS_SITE = "\n\n".join([CSS_PRODUCT, CSS_INDEX])
