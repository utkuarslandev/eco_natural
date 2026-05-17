

## BRAND IDENTITY & DESIGN SYSTEM

---

### THE BRAND

**Name:** ECO NATURAL
**Village:** Büyük Çaltıcak · Mediterranean Turkey
**Tagline:** *Lasting Taste of Earth*
**Category:** Village-origin cold-pressed natural food extracts

---

### THE ONE TRUE SENTENCE

> *We bring what the Earth gifts, as it is.*

This replaces "nothing to hide." It is declarative, not defensive. It is about the land, not about the competition. Everything in the brand — visual, verbal, digital — flows from it.

---

### BRAND PERSONALITY

Five words, in order of weight:

| | |
|---|---|
| **Rooted** | Everything traces to a specific place and a specific process. No abstractions. |
| **Unhurried** | This has been done this way for decades. There is no trend to chase. |
| **Generous** | The product gives something real — flavour, nutrition, story. The brand gives information freely. |
| **Specific** | Büyük Çaltıcak, not "Anatolia." Harnup özü, not "natural extract." Cold-pressed, not "artisan." |
| **Quietly proud** | The village doesn't need to shout. The carob speaks. |

**What we are not:** Wellness-brand clinical. Luxury-brand exclusive. Health-food preachy. Tourist-trap generic.

---

### TAGLINE USAGE RULES

*Lasting Taste of Earth* — always italic, always EB Garamond, always in the display weight.

**Where it appears:**
- Hero section, beneath the main headline — the anchor
- Footer, centred alone on one line — the closing statement
- Bottle neck label (physical) — below the village name
- Every product detail page hero

**What it never does:**
- Never appears in all-caps — it must breathe and curve
- Never appears in terracotta — it lives in gold-pale on dark, or bark on light
- Never appears with an exclamation mark
- Never broken across two lines — it is one complete thought

**The three-word breakdown for design use:**
- *Lasting* — time, heritage, memory
- *Taste* — sensory, immediate, honest
- *Earth* — origin, village, Anatolia, soil, the carob tree itself

---

### LOGO SYSTEM

The existing emblem — wheat wreath, five stars, Eco Natural, Büyük Çaltıcak, `%100 NATURAL` ribbon — is preserved completely. It already works. We build a lockup system around it.

**Full lockup (website header, packaging):**
```
        ⟨ EMBLEM ⟩
     ECO NATURAL
  Büyük Çaltıcak · Aydın
  ─────────────────────
  Lasting Taste of Earth
```

**Horizontal lockup (nav bar):**
```
ECO NATURAL  |  Büyük Çaltıcak · Aydın
```

**Stamp only:** The circular emblem alone, used as a trust seal on product pages, printed receipts, and social media.

**Minimum clear space:** Equal to the height of the letter E in ECO NATURAL on all sides.

---

### TYPOGRAPHY

Three fonts. Roles are absolute and never swapped.

---

**ABRIL FATFACE** — *The Landmark*

Used for: Hero headlines, section titles, product card names, large numerals
Never used for: Body copy, captions, labels, buttons

This font carries the weight of the brand name. It has the character of a carved market sign, a wine label from 1920, a wooden stamp pressed into paper. It says *this has been here a long time.* At large sizes it becomes a visual texture, not just text.

Scale:
- Hero: `clamp(3.5rem, 7vw, 7.5rem)`
- Section title: `clamp(2.2rem, 5vw, 4rem)`
- Product card: `clamp(1.3rem, 2vw, 1.6rem)`
- Decorative background: `clamp(10rem, 20vw, 28rem)` at 4% opacity

---

**EB GARAMOND ITALIC** — *The Voice*

Used for: The tagline, blockquotes, sub-headlines, Turkish product names beneath English names, captions, the founder quote in the story section
Never used: Roman weight, never as primary headline

This is the font that says *"Lasting Taste of Earth."* It sounds like someone sitting across from you at a table, speaking carefully. It is the warmth beneath Abril Fatface's permanence. Italic only — the roman weight loses all character.

Scale:
- Tagline: `clamp(1.2rem, 2vw, 1.5rem)`
- Sub-headlines: `clamp(1rem, 1.5vw, 1.3rem)`
- Quotes: `clamp(1.1rem, 1.8vw, 1.4rem)`
- Captions: `0.85rem`

---

**RALEWAY 300/400/600** — *The Ground*

Used for: All body copy, navigation, labels, eyebrows, buttons, UI text
Never used: 700 or above — this brand does not shout

300 for reading, 400 for interface, 600 for calls to action and eyebrow labels. The brand's credibility comes from measured confidence. Heavy weight breaks that.

Scale:
- Body: `clamp(0.88rem, 1.1vw, 0.98rem)`, line-height 1.9
- Navigation: `0.65rem`, letter-spacing 0.2em, uppercase
- Eyebrow labels: `0.62rem`, letter-spacing 0.35em, uppercase, weight 600
- Button text: `0.72rem`, letter-spacing 0.2em, uppercase, weight 600
- Micro labels: `0.55rem–0.62rem`, letter-spacing 0.2–0.3em

---

### COLOUR PALETTE — FINAL

All colours are extracted from the label (cream, red, gold, dark glass) and the Aegean landscape (terracotta soil, olive grove, sun-bleached stone).

**The rule before the palette:** 70% parchment warmth, 20% earth depth, 10% gold accent. If any page breaks this ratio, it breaks the brand.

| Token | Hex | Name | Role |
|---|---|---|---|
| `--parch` | `#F5EDD8` | Parchment | Dominant background — every page begins here |
| `--parch-lt` | `#FBF7EE` | Light Parchment | Card surfaces, elevated UI |
| `--parch-dk` | `#EAE0C6` | Deep Parchment | Borders, dividers, subtle depth |
| `--bark` | `#271608` | Deep Bark | Hero backgrounds, dark section fill, primary text on light |
| `--bark-mid` | `#3D240E` | Mid Bark | How To section, footer, secondary dark fill |
| `--terra` | `#B85428` | Terracotta | **The only action colour.** CTAs, underlines, badges |
| `--terra-lt` | `#D4784A` | Light Terracotta | Hover states only |
| `--terra-dk` | `#8B3A18` | Dark Terracotta | Active states, pressed buttons |
| `--olive` | `#2C3A1A` | Deep Olive | Trust band background, certification section |
| `--olive-lt` | `#485E2C` | Olive | Positive indicators, "ours" comparison column |
| `--gold` | `#C49010` | Aged Gold | Stamp badges, kicker lines, eyebrow rules |
| `--gold-lt` | `#DDB040` | Light Gold | Italic headline accents on dark, hover on gold elements |
| `--gold-pale` | `#F0D898` | Pale Gold | Body text on bark backgrounds |
| `--text` | `#271608` | Deep Brown | Primary text — same as bark for visual unity |
| `--text-mid` | `#5C3D20` | Mid Brown | Body copy on parchment |
| `--text-soft` | `#8A6A4A` | Soft Brown | Captions, secondary labels, supporting text |

**Absolute colour rules:**
- Never pure `#000000` or `#FFFFFF` — they break the paper warmth
- Terracotta appears on no more than one CTA per section
- Gold is an accent — if it covers more than 10% of a section, reduce it
- Dark bark sections (hero, story, how-to) provide contrast breathing room — maximum two consecutive dark sections before returning to parchment
- Background colours never use blue, purple, or cool grey — every colour in this palette comes from warm earth

---

### TEXTURE LAYER

**Paper grain** — Always applied. `body::before`, fixed position, SVG `feTurbulence` fractalNoise, `baseFrequency 0.75`, `opacity 0.4`, `mix-blend-mode: multiply`. This single layer makes the entire site feel printed rather than glowing. It is non-negotiable.

**Torn paper dividers** — Every transition between sections. Never a straight horizontal rule. The SVG path is a gentle irregular edge that reads as torn or cut paper. This matches the *handmade, village, market* language of the physical labels.

**Warm drop shadows** — All product bottles: `drop-shadow(0 20px 40px rgba(0,0,0,0.6))` + `drop-shadow(0 0 30px rgba(196,144,16,0.15))`. The warm secondary shadow simulates shelf lighting. Never use cool grey shadows.

**Decorative ghost text** — Section-specific large Abril Fatface text at 4% opacity in the background. Hero: "ECO". Carob section: "HARNUP". Village section: "ÇALTICAK". Adds depth without adding noise.

---

### SPACING SYSTEM

```
--section-pad:  clamp(5rem, 8vw, 9rem)   ← top/bottom of every section
--container:    min(100% - 3rem, 1200px)  ← max content width
--card-pad:     1.8rem                    ← all card interiors
--grid-gap:     2rem                      ← between cards and grid items
--eyebrow-mb:   1.2rem                    ← below every section eyebrow
--para-gap:     1.5rem                    ← between body paragraphs
--element-gap:  0.75rem                   ← between small UI elements
```

**Spacing logic:** Section padding scales with viewport. Cards stay fixed. Never use `px` units for layout — only `rem`, `clamp()`, `%`, and `min()`.

---

### COMPONENT SYSTEM

**Eyebrow** — Opens every section without exception. Raleway 600, 0.62rem, letter-spacing 0.35em, all-caps, terracotta. Left-aligned rule `──` in gold before the text. This creates visual rhythm across the page — every section breathes the same way.

**Rubber Stamp Badges** — Circular, 88px diameter, border + dashed inner ring, text centred. Used for the five truths: `%100 NATURAL`, `COLD PRESS`, `KATKISIZ`, `BÜYÜK ÇALTICAK`, `GLASS BOTTLE`. They match the circular certification stamp on the physical label exactly — when a tourist opens the website while holding the bottle, they see the same language twice. This is the deepest trust signal on the page.

**Product Cards** — Dark gradient background, full portrait bottle image with `object-fit: contain` and internal padding (the bottle is never cropped). Bottom terracotta accent line on hover. Structure: category in terracotta → English name in Abril Fatface → Turkish name in EB Garamond italic → one-sentence description in Raleway 400 → size/format in soft brown → "Learn More →" in terracotta. No price. They buy in the shop.

**Cold-Press Comparison** — Two columns, VS circle between. Ours: olive-tinted, Raleway 600 header in olive, bullet dots in olive. Theirs: terracotta-tinted, 75% opacity — not aggressive, just honest. This component answers the question every informed tourist asks: "I can get carob extract anywhere — why this one?"

**Tagline Display** — On dark bark backgrounds: EB Garamond italic, `gold-pale`, centred, generous vertical spacing. Used at end of hero section, start of footer. Never decorated. Never boxed. It breathes.

**Product Browsing CTA** — Product cards use a restrained text call-to-action with terracotta emphasis. The catalog is informational first: no direct messaging order UI is part of the page system.

---

### MOTION SYSTEM

**Founding principle:** The product has been made the same way for decades. The animation should feel the same way — deliberate, unhurried, never surprising for the sake of surprise.

| Element | Animation | Duration | Easing |
|---|---|---|---|
| Section content | `opacity 0→1` + `translateY 24px→0` | 750ms | `cubic-bezier(0.16,1,0.3,1)` |
| Group stagger | +100ms per child | — | — |
| Product bottles | `translateY 0→-12px→0` infinite | 7s, 8s, 6s | `ease-in-out` |
| Card hover lift | `translateY -6px` + shadow | 350ms | Same expo |
| Button fill | Slide from left | 350ms | Same expo |
| Marquee | Horizontal scroll | 30s | `linear` |
| Torn paper dividers | Static — no animation | — | — |

**Strict rules:**
- No parallax — mobile customers, one thumb, outdoor light
- No auto-playing video
- All animations wrapped in `@media (prefers-reduced-motion: reduce)`
- The floating bottles pause on reduced-motion without removing them

---

### LANGUAGE & COPY SYSTEM

**Hierarchy:** English primary. Russian toggle. Turkish as texture.

Turkish product names (`Harnup Keçiboynuzu Özü`, `Salata Sosu`, `Büyük Çaltıcak`) are never translated — they are proper nouns and brand identifiers. Translating them would make them feel invented. Their presence signals authenticity to tourists more powerfully than any claim we could write.

**Copy voice — four rules:**
1. One true specific sentence beats three vague marketing sentences
2. Describe what it *is* before describing what it *does*
3. Name the place, name the process, name the ingredient — every time, not once
4. The tagline *Lasting Taste of Earth* works because it is both literal and resonant — all copy should aim for that same quality

**What we never write:** "artisanally crafted," "premium quality," "wellness journey," "superfood," "ancient wisdom." These are the phrases of brands that don't have a real story. We have a real story.

---

### THE TOURIST MOMENT — HOW IT ALL CONNECTS

A tourist is standing in a shop in Aydın. They are holding a dark glass bottle with a gold foil label, a wheat wreath emblem, and the words `%100 NATURAL · BÜYÜK ÇALTICAK`.

They scan a QR code. Their phone opens a warm parchment page that looks exactly like the label in their hand — same stamp, same colours, same warmth. The first thing they read is:

> **ECO NATURAL**
> *Lasting Taste of Earth*

In ten seconds they know: this is from a real village, it has one ingredient, it has been pressed this way for decades, and the people who make it changed nothing because they had no reason to.

They buy the bottle. They take it home to Moscow or Berlin or Tokyo. Someone at their table asks what it is. They tell the story of Büyük Çaltıcak.

**That story, told by a stranger in another country — that is the lasting impression. That is the entire purpose of this brand.**

