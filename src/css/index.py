from css.tokens import GRAIN_SVG

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
