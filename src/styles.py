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
    "family=Caveat:wght@500;600&"
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

.page-index {{
  background:
    linear-gradient(180deg, rgba(26,53,32,0.72) 0%, rgba(26,53,32,0.82) 52%, rgba(26,53,32,0.9) 100%),
    linear-gradient(90deg, rgba(26,53,32,0.72) 0%, rgba(26,53,32,0.38) 52%, rgba(26,53,32,0.68) 100%),
    url("./img/hero-aegean-field.png");
  background-size: cover;
  background-position: center top;
  background-attachment: fixed;
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

body.product-eco-natural-pumpkin-seed-oil-250ml .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-eco-natural-pomegranate-seed-oil-250ml .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-eco-natural-pomegranate-sour-340g .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-eco-natural-avocado-oil-250ml .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-eco-natural-black-seed-oil-250ml .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-olive-oil-bg .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-eco-natural-hemp-seed-oil-250ml .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-metis-hierapolis-safflower-oil-250ml .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-eco-natural-poppy-seed-oil-250ml .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-eco-natural-fig-seed-oil .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-carob-bg .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-eco-natural-salad-dressing .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
}}

body.product-eco-natural-zeytin-sutu-cold-pressed-olive-elixir .breadcrumb {{
  background: rgba(246,250,244,0.9);
  backdrop-filter: blur(10px);
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

body.product-eco-natural-pumpkin-seed-oil-250ml .hero {{
  background:
    linear-gradient(180deg, rgba(8,16,22,0.24) 0%, rgba(8,16,22,0.78) 100%),
    url("./img/pumpkin-farm-night.png");
  background-size: cover;
  background-position: center top;
}}

body.product-eco-natural-pomegranate-seed-oil-250ml .hero {{
  background:
    linear-gradient(180deg, rgba(18,35,22,0.34) 0%, rgba(18,35,22,0.82) 100%),
    linear-gradient(90deg, rgba(18,35,22,0.78) 0%, rgba(18,35,22,0.42) 52%, rgba(18,35,22,0.7) 100%),
    url("./img/pomegranate-tree.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-pomegranate-sour-340g .hero {{
  background:
    linear-gradient(180deg, rgba(18,35,22,0.34) 0%, rgba(18,35,22,0.82) 100%),
    linear-gradient(90deg, rgba(18,35,22,0.78) 0%, rgba(18,35,22,0.42) 52%, rgba(18,35,22,0.7) 100%),
    url("./img/pomegranate-tree.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-avocado-oil-250ml .hero {{
  background:
    linear-gradient(180deg, rgba(20,42,24,0.34) 0%, rgba(20,42,24,0.82) 100%),
    linear-gradient(90deg, rgba(20,42,24,0.78) 0%, rgba(20,42,24,0.42) 52%, rgba(20,42,24,0.7) 100%),
    url("./img/avocado-basket-farm.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-black-seed-oil-250ml .hero {{
  background:
    linear-gradient(180deg, rgba(24,32,21,0.34) 0%, rgba(24,32,21,0.82) 100%),
    linear-gradient(90deg, rgba(24,32,21,0.78) 0%, rgba(24,32,21,0.42) 52%, rgba(24,32,21,0.7) 100%),
    url("./img/black-seed-farm-handful.png");
  background-size: cover;
  background-position: center center;
}}

body.product-olive-oil-bg .hero {{
  background:
    linear-gradient(180deg, rgba(25,38,20,0.28) 0%, rgba(25,38,20,0.82) 100%),
    linear-gradient(90deg, rgba(25,38,20,0.74) 0%, rgba(25,38,20,0.34) 52%, rgba(25,38,20,0.68) 100%),
    url("./img/olive-tree-sunset.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-hemp-seed-oil-250ml .hero {{
  background:
    linear-gradient(180deg, rgba(22,42,22,0.28) 0%, rgba(22,42,22,0.82) 100%),
    linear-gradient(90deg, rgba(22,42,22,0.72) 0%, rgba(22,42,22,0.32) 52%, rgba(22,42,22,0.68) 100%),
    url("./img/hemp-seed-farm-ladder-sunset.png");
  background-size: cover;
  background-position: center center;
}}

body.product-metis-hierapolis-safflower-oil-250ml .hero {{
  background:
    linear-gradient(180deg, rgba(50,43,18,0.26) 0%, rgba(50,43,18,0.82) 100%),
    linear-gradient(90deg, rgba(50,43,18,0.7) 0%, rgba(50,43,18,0.3) 52%, rgba(50,43,18,0.66) 100%),
    url("./img/safflower-field-crescent-moon.png");
  background-size: cover;
  background-position: center bottom;
}}

body.product-eco-natural-poppy-seed-oil-250ml .hero {{
  background:
    linear-gradient(180deg, rgba(45,33,24,0.18) 0%, rgba(45,33,24,0.8) 100%),
    linear-gradient(90deg, rgba(45,33,24,0.66) 0%, rgba(45,33,24,0.26) 52%, rgba(45,33,24,0.64) 100%),
    url("./img/poppy-field-harvesters-blue-sky.png");
  background-size: 120% auto;
  background-position: center bottom;
}}

body.product-eco-natural-fig-seed-oil .hero {{
  background:
    linear-gradient(180deg, rgba(35,44,20,0.24) 0%, rgba(35,44,20,0.82) 100%),
    linear-gradient(90deg, rgba(35,44,20,0.72) 0%, rgba(35,44,20,0.34) 52%, rgba(35,44,20,0.68) 100%),
    url("./img/fig-tree-hand-picking-sunset.png");
  background-size: cover;
  background-position: center center;
}}

body.product-carob-bg .hero {{
  background:
    linear-gradient(180deg, rgba(45,35,20,0.24) 0%, rgba(45,35,20,0.82) 100%),
    linear-gradient(90deg, rgba(45,35,20,0.72) 0%, rgba(45,35,20,0.34) 52%, rgba(45,35,20,0.68) 100%),
    url("./img/carob-tree-handpicking-basket.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-salad-dressing .hero {{
  background:
    linear-gradient(180deg, rgba(42,22,26,0.22) 0%, rgba(42,22,26,0.82) 100%),
    linear-gradient(90deg, rgba(42,22,26,0.72) 0%, rgba(42,22,26,0.3) 52%, rgba(42,22,26,0.68) 100%),
    url("./img/salad-dressing-dark-red-salad.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-zeytin-sutu-cold-pressed-olive-elixir .hero {{
  background:
    linear-gradient(180deg, rgba(37,35,19,0.2) 0%, rgba(37,35,19,0.82) 100%),
    linear-gradient(90deg, rgba(37,35,19,0.72) 0%, rgba(37,35,19,0.3) 52%, rgba(37,35,19,0.68) 100%),
    url("./img/olive-elixir-bottle-pouring-pan.png");
  background-size: cover;
  background-position: center center;
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

.details-columns {{
  display: grid;
  grid-template-columns: 1fr;
  gap: clamp(2rem, 4vw, 3.5rem);
  align-items: start;
}}

@media (min-width: 860px) {{
  .details-columns {{
    grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  }}

  .details-columns .section {{
    padding-top: clamp(3.5rem, 6vw, 5.5rem);
  }}
}}

body.product-eco-natural-pumpkin-seed-oil-250ml .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-pomegranate-seed-oil-250ml .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-pomegranate-sour-340g .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-avocado-oil-250ml .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-black-seed-oil-250ml .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-olive-oil-bg .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-hemp-seed-oil-250ml .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-metis-hierapolis-safflower-oil-250ml .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-poppy-seed-oil-250ml .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-fig-seed-oil .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-carob-bg .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-salad-dressing .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-zeytin-sutu-cold-pressed-olive-elixir .section-origin {{
  width: 100vw;
  max-width: none;
  margin-left: calc(50% - 50vw);
  padding: clamp(3rem, 6vw, 5rem) max(20px, calc((100vw - 1200px) / 2)) clamp(4rem, 7vw, 6rem);
  position: relative;
  overflow: hidden;
  isolation: isolate;
}}

body.product-eco-natural-pumpkin-seed-oil-250ml .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(8,16,22,0.52) 0%, rgba(8,16,22,0.68) 100%),
    url("./img/pumpkin-farm-night.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-pomegranate-seed-oil-250ml .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(18,35,22,0.58) 0%, rgba(18,35,22,0.72) 100%),
    url("./img/pomegranate-tree.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-pomegranate-sour-340g .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(18,35,22,0.58) 0%, rgba(18,35,22,0.72) 100%),
    url("./img/pomegranate-tree.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-avocado-oil-250ml .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(20,42,24,0.58) 0%, rgba(20,42,24,0.72) 100%),
    url("./img/avocado-basket-farm.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-black-seed-oil-250ml .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(24,32,21,0.58) 0%, rgba(24,32,21,0.72) 100%),
    url("./img/black-seed-farm-handful.png");
  background-size: cover;
  background-position: center center;
}}

body.product-olive-oil-bg .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(25,38,20,0.56) 0%, rgba(25,38,20,0.72) 100%),
    url("./img/olive-tree-sunset.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-hemp-seed-oil-250ml .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(22,42,22,0.56) 0%, rgba(22,42,22,0.72) 100%),
    url("./img/hemp-seed-farm-ladder-sunset.png");
  background-size: cover;
  background-position: center center;
}}

body.product-metis-hierapolis-safflower-oil-250ml .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(50,43,18,0.54) 0%, rgba(50,43,18,0.72) 100%),
    url("./img/safflower-field-crescent-moon.png");
  background-size: cover;
  background-position: center bottom;
}}

body.product-eco-natural-poppy-seed-oil-250ml .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(45,33,24,0.48) 0%, rgba(45,33,24,0.68) 100%),
    url("./img/poppy-field-harvesters-blue-sky.png");
  background-size: cover;
  background-position: center bottom;
}}

body.product-eco-natural-fig-seed-oil .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(35,44,20,0.52) 0%, rgba(35,44,20,0.72) 100%),
    url("./img/fig-tree-hand-picking-sunset.png");
  background-size: cover;
  background-position: center center;
}}

body.product-carob-bg .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(45,35,20,0.52) 0%, rgba(45,35,20,0.72) 100%),
    url("./img/carob-tree-handpicking-basket.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-salad-dressing .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(42,22,26,0.5) 0%, rgba(42,22,26,0.72) 100%),
    url("./img/salad-dressing-dark-red-salad.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-zeytin-sutu-cold-pressed-olive-elixir .section-origin::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    linear-gradient(180deg, rgba(37,35,19,0.5) 0%, rgba(37,35,19,0.72) 100%),
    url("./img/olive-elixir-bottle-pouring-pan.png");
  background-size: cover;
  background-position: center center;
}}

body.product-eco-natural-pumpkin-seed-oil-250ml .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-eco-natural-pomegranate-seed-oil-250ml .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-eco-natural-pomegranate-sour-340g .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-eco-natural-avocado-oil-250ml .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-eco-natural-black-seed-oil-250ml .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-olive-oil-bg .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-eco-natural-hemp-seed-oil-250ml .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-metis-hierapolis-safflower-oil-250ml .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-eco-natural-poppy-seed-oil-250ml .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-eco-natural-fig-seed-oil .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-carob-bg .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-eco-natural-salad-dressing .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

body.product-eco-natural-zeytin-sutu-cold-pressed-olive-elixir .section-origin .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.6);
}}

.section-heading {{
  font-family: 'Caveat', 'EB Garamond', cursive;
  font-size: clamp(2.2rem, 4vw, 3.4rem);
  font-weight: 600;
  color: var(--bark);
  margin-bottom: 1.2rem;
  line-height: 0.95;
  letter-spacing: 0;
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
  grid-template-columns: 1fr;
  gap: 12px;
}}

.use-tile {{
  background:
    linear-gradient(135deg, rgba(255,255,255,0.96), rgba(246,250,244,0.9));
  border: 1px solid rgba(192,144,16,0.18);
  border-left: 3px solid var(--gold);
  border-radius: 8px;
  padding: 14px 18px;
  text-align: left;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 16px;
  min-height: 82px;
  box-shadow:
    0 10px 24px rgba(26,53,32,0.06),
    inset 0 1px 0 rgba(255,255,255,0.82);
  transition: border-left-color 0.2s, transform 0.2s, box-shadow 0.2s;
  justify-content: flex-start;
}}
.use-tile:hover {{
  border-left-color: var(--gold-lt);
  transform: translateX(3px);
  box-shadow:
    0 14px 28px rgba(26,53,32,0.1),
    inset 0 1px 0 rgba(255,255,255,0.9);
}}
.use-label {{
  font-family: 'Cinzel', serif;
  font-weight: 600;
  font-size: clamp(0.72rem, 0.95vw, 0.86rem);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bark);
  line-height: 1.25;
}}

/* ── Quality Grid ────────────────────────────────────────────────────────── */

.quality-grid {{
  display: grid;
  grid-template-columns: 1fr;
  gap: 12px;
}}

.quality-card {{
  background:
    linear-gradient(135deg, rgba(255,255,255,0.97), rgba(246,250,244,0.92));
  border: 1px solid rgba(192,144,16,0.18);
  border-left: 3px solid var(--gold);
  border-radius: 8px;
  padding: 16px 18px;
  display: flex;
  flex-direction: row;
  align-items: center;
  gap: 16px;
  text-align: left;
  min-height: 96px;
  box-shadow:
    0 10px 24px rgba(26,53,32,0.06),
    inset 0 1px 0 rgba(255,255,255,0.82);
}}
.quality-copy {{
  display: flex;
  flex-direction: column;
  gap: 6px;
  min-width: 0;
}}
.quality-name {{
  font-family: 'Cinzel', serif;
  font-weight: 600;
  font-size: clamp(0.72rem, 0.95vw, 0.86rem);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--bark);
  line-height: 1.25;
}}
.quality-desc {{
  font-family: 'Raleway', sans-serif;
  font-weight: 400;
  font-size: clamp(0.74rem, 0.9vw, 0.82rem);
  color: rgba(45,78,48,0.78);
  line-height: 1.55;
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

body.product-eco-natural-pumpkin-seed-oil-250ml .credentials-strip {{
  background: rgba(11,22,31,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-pomegranate-seed-oil-250ml .credentials-strip {{
  background: rgba(18,35,22,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-pomegranate-sour-340g .credentials-strip {{
  background: rgba(18,35,22,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-avocado-oil-250ml .credentials-strip {{
  background: rgba(20,42,24,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-black-seed-oil-250ml .credentials-strip {{
  background: rgba(24,32,21,0.78);
  backdrop-filter: blur(2px);
}}

body.product-olive-oil-bg .credentials-strip {{
  background: rgba(25,38,20,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-hemp-seed-oil-250ml .credentials-strip {{
  background: rgba(22,42,22,0.78);
  backdrop-filter: blur(2px);
}}

body.product-metis-hierapolis-safflower-oil-250ml .credentials-strip {{
  background: rgba(50,43,18,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-poppy-seed-oil-250ml .credentials-strip {{
  background: rgba(45,33,24,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-fig-seed-oil .credentials-strip {{
  background: rgba(35,44,20,0.78);
  backdrop-filter: blur(2px);
}}

body.product-carob-bg .credentials-strip {{
  background: rgba(45,35,20,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-salad-dressing .credentials-strip {{
  background: rgba(42,22,26,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-zeytin-sutu-cold-pressed-olive-elixir .credentials-strip {{
  background: rgba(37,35,19,0.78);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-pumpkin-seed-oil-250ml .torn path {{
  fill: rgba(11,22,31,0.78);
}}

body.product-eco-natural-pomegranate-seed-oil-250ml .torn path {{
  fill: rgba(18,35,22,0.78);
}}

body.product-eco-natural-pomegranate-sour-340g .torn path {{
  fill: rgba(18,35,22,0.78);
}}

body.product-eco-natural-avocado-oil-250ml .torn path {{
  fill: rgba(20,42,24,0.78);
}}

body.product-eco-natural-black-seed-oil-250ml .torn path {{
  fill: rgba(24,32,21,0.78);
}}

body.product-olive-oil-bg .torn path {{
  fill: rgba(25,38,20,0.78);
}}

body.product-eco-natural-hemp-seed-oil-250ml .torn path {{
  fill: rgba(22,42,22,0.78);
}}

body.product-metis-hierapolis-safflower-oil-250ml .torn path {{
  fill: rgba(50,43,18,0.78);
}}

body.product-eco-natural-poppy-seed-oil-250ml .torn path {{
  fill: rgba(45,33,24,0.78);
}}

body.product-eco-natural-fig-seed-oil .torn path {{
  fill: rgba(35,44,20,0.78);
}}

body.product-carob-bg .torn path {{
  fill: rgba(45,35,20,0.78);
}}

body.product-eco-natural-salad-dressing .torn path {{
  fill: rgba(42,22,26,0.78);
}}

body.product-eco-natural-zeytin-sutu-cold-pressed-olive-elixir .torn path {{
  fill: rgba(37,35,19,0.78);
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

body.product-eco-natural-pumpkin-seed-oil-250ml .footer {{
  background: rgba(11,22,31,0.86);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-pomegranate-seed-oil-250ml .footer {{
  background: rgba(18,35,22,0.86);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-pomegranate-sour-340g .footer {{
  background: rgba(18,35,22,0.86);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-avocado-oil-250ml .footer {{
  background: rgba(20,42,24,0.86);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-black-seed-oil-250ml .footer {{
  background: rgba(24,32,21,0.86);
  backdrop-filter: blur(2px);
}}

body.product-olive-oil-bg .footer {{
  background: rgba(25,38,20,0.86);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-hemp-seed-oil-250ml .footer {{
  background: rgba(22,42,22,0.86);
  backdrop-filter: blur(2px);
}}

body.product-metis-hierapolis-safflower-oil-250ml .footer {{
  background: rgba(50,43,18,0.86);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-poppy-seed-oil-250ml .footer {{
  background: rgba(45,33,24,0.86);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-fig-seed-oil .footer {{
  background: rgba(35,44,20,0.86);
  backdrop-filter: blur(2px);
}}

body.product-carob-bg .footer {{
  background: rgba(45,35,20,0.86);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-salad-dressing .footer {{
  background: rgba(42,22,26,0.86);
  backdrop-filter: blur(2px);
}}

body.product-eco-natural-zeytin-sutu-cold-pressed-olive-elixir .footer {{
  background: rgba(37,35,19,0.86);
  backdrop-filter: blur(2px);
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

.use-emoji {{
  width: 3.2rem;
  height: 3.2rem;
  display: grid;
  place-items: center;
  font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
  font-size: 2rem;
  line-height: 1;
  border-radius: 50%;
  background:
    radial-gradient(circle at 32% 24%, rgba(255,255,255,0.96), rgba(255,255,255,0.28) 33%, rgba(212,168,32,0.18) 72%),
    rgba(246,250,244,0.82);
  border: 1px solid rgba(192,144,16,0.28);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.72),
    0 8px 18px rgba(26,53,32,0.12);
}}

/* ── Quality card emoji ──────────────────────────────────────────────────── */

.quality-emoji {{
  width: 3rem;
  height: 3rem;
  display: grid;
  place-items: center;
  font-family: "Apple Color Emoji", "Segoe UI Emoji", "Noto Color Emoji", sans-serif;
  font-size: 1.85rem;
  line-height: 1;
  border-radius: 50%;
  margin-bottom: 2px;
  background:
    radial-gradient(circle at 32% 24%, rgba(255,255,255,0.95), rgba(255,255,255,0.24) 34%, rgba(93,155,58,0.16) 74%),
    rgba(246,250,244,0.86);
  border: 1px solid rgba(93,155,58,0.24);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.7),
    0 8px 16px rgba(26,53,32,0.1);
}}

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

/* ── Experience catchphrase ──────────────────────────────────────────────── */

.experience-line {{
  max-width: 820px;
  margin: clamp(3.5rem, 6vw, 5rem) auto 0;
  text-align: center;
  font-family: 'Caveat', 'EB Garamond', cursive;
  font-weight: 600;
  font-size: clamp(2rem, 4vw, 3.2rem);
  line-height: 1.02;
  letter-spacing: 0;
  color: var(--bark);
  position: relative;
  padding: 0 20px;
}}

.experience-line::before,
.experience-line::after {{
  content: '';
  display: block;
  width: 72px;
  height: 1px;
  background: var(--gold);
  opacity: 0.75;
  margin: 0 auto 1rem;
}}

.experience-line::after {{
  margin: 1rem auto 0;
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
  .scroll-hint {{ order: 3; flex: 0 0 100%; }}
  .hero-copy h1, .hero-copy .tagline {{ text-align: left; }}
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

.page-index .hero {{
  min-height: 72vh;
  background:
    linear-gradient(90deg, rgba(26,53,32,0.9) 0%, rgba(26,53,32,0.62) 44%, rgba(26,53,32,0.5) 100%),
    linear-gradient(180deg, rgba(26,53,32,0.24) 0%, rgba(26,53,32,0.82) 100%),
    url("./img/hero-green-salad-olive-oil.png");
  background-size: cover;
  background-position: center;
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
  margin-top: clamp(2rem, 8vw, 4rem);
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
  scroll-margin-top: clamp(120px, 15vw, 300px);
}}

.page-index .catalog-section .eyebrow {{
  color: var(--gold-pale);
  text-shadow: 0 2px 14px rgba(0,0,0,0.55);
}}

.product-grid {{
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}}
@media (min-width: 600px) {{ .product-grid {{ grid-template-columns: repeat(3, 1fr); }} }}
@media (min-width: 960px) {{ .product-grid {{ grid-template-columns: repeat(4, 1fr); }} }}

.product-card {{
  background:
    linear-gradient(180deg, rgba(11,24,15,0.52) 0%, rgba(11,24,15,0.82) 100%),
    linear-gradient(90deg, rgba(11,24,15,0.62) 0%, rgba(11,24,15,0.28) 52%, rgba(11,24,15,0.58) 100%),
    var(--card-bg, linear-gradient(160deg, var(--bark-mid) 0%, var(--bark) 100%));
  background-size: cover;
  background-position: center center;
  border: 1px solid rgba(196,144,16,0.15);
  border-radius: 12px;
  overflow: hidden;
  text-decoration: none;
  display: flex;
  flex-direction: column;
  transition: transform 0.35s cubic-bezier(0.16,1,0.3,1), border-color 0.2s;
  position: relative;
  isolation: isolate;
}}
.product-card::before {{
  content: '';
  position: absolute;
  inset: 0;
  z-index: -1;
  background:
    radial-gradient(circle at 50% 14%, rgba(240,216,152,0.16), transparent 42%),
    linear-gradient(180deg, transparent 0%, rgba(26,53,32,0.36) 58%, rgba(26,53,32,0.7) 100%);
  opacity: 0.95;
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
  z-index: 2;
}}
.product-card:hover {{ transform: translateY(-6px); border-color: rgba(196,144,16,0.35); }}
.product-card:hover::after {{ transform: scaleX(1); }}

.card-img-wrap {{
  padding: 24px 24px 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 160px;
  position: relative;
  z-index: 1;
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
  padding: 12px 18px 20px;
  display: flex;
  flex-direction: column;
  gap: 6px;
  flex: 1;
  position: relative;
  z-index: 1;
  background: linear-gradient(180deg, rgba(13,32,18,0) 0%, rgba(13,32,18,0.58) 20%, rgba(13,32,18,0.78) 100%);
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
