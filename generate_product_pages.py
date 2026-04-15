"""
Eco Natural product page generator.
Produces one mobile-first HTML page per product from ids.csv,
enriched with origin stories, how-to-use tiles, and quality badges.
Target audience: tourists scanning barcodes in-store.
"""

import csv
from html import escape
from pathlib import Path


ROOT       = Path(__file__).parent
CSV_PATH   = ROOT / "ids.csv"
IMG_DIR    = ROOT / "img"
OUTPUT_DIR = ROOT


# ── Per-product enrichment ─────────────────────────────────────────────────────
# Each entry: origin_place, story (list of paragraphs), how_to_use (list of
# (emoji, label) pairs), badges (list of (emoji, label) pairs), is_gift bool.

ENRICHMENT: dict[str, dict] = {

    # ── Şirince Infused EVOOs ──────────────────────────────────────────────────

    "SH-EVOO-ROSEMARY-250ML": {
        "origin_place": "Şirince, Aegean Turkey",
        "story": [
            "Şirince is a small whitewashed village tucked into the hills above ancient Ephesus — "
            "where olive trees have been tended for centuries and wild rosemary grows between the "
            "groves. The oil here carries the character of that land: clean, aromatic, alive.",
            "Fresh rosemary is cold-pressed alongside hand-picked olives to create a botanical "
            "infusion with no artificial flavoring. Just the herb and the olive, as they have "
            "grown side by side in these hills for generations.",
        ],
        "how_to_use": [
            ("🥕", "Roasted Vegetables"), ("🍞", "Bread & Focaccia"),
            ("🥩", "Grilled Meats"),      ("🥔", "Potato Dishes"),
            ("🍝", "Pasta Finishing"),    ("🫙", "Dipping & Serving"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "No heat — full flavor and nutrients preserved"),
            ("🫒", "Extra Virgin",    "Highest global olive oil classification"),
            ("🌿", "Natural Infusion","Real rosemary — zero artificial flavoring"),
            ("🚫", "No Additives",    "Clean label, nothing synthetic"),
            ("📍", "Single Origin",   "Traceable provenance — Şirince, Aegean Turkey"),
        ],
        "is_gift": False,
        "product_line": "Şirince Infused Oils · 250 ml",
        "tagline": "Cold pressed with wild rosemary from the Aegean hills",
    },

    "SH-EVOO-GARLIC-250ML": {
        "origin_place": "Şirince, Aegean Turkey",
        "story": [
            "In village kitchens across the Aegean, garlic has always been pressed with olive oil "
            "as the essential flavour base. This bottle captures that tradition: fresh garlic "
            "cold-infused into extra virgin oil, creating a savory foundation you can reach for "
            "every day.",
            "Its aromatic depth comes from a natural pairing — no extraction, no concentrates. "
            "Just garlic and oil, the way it has always been done.",
        ],
        "how_to_use": [
            ("🥗", "Salad Dressings"),  ("🍞", "Bread & Dipping"),
            ("🥩", "Marinades"),        ("🍝", "Pasta & Sauces"),
            ("🫑", "Sautéed Veg"),      ("🫙", "Table Serving"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "No heat — full flavour and nutrients preserved"),
            ("🫒", "Extra Virgin",    "Highest global olive oil classification"),
            ("🧄", "Natural Infusion","Real garlic — zero artificial flavouring"),
            ("🚫", "No Additives",    "Clean label, nothing synthetic"),
            ("📍", "Single Origin",   "Traceable provenance — Şirince, Aegean Turkey"),
        ],
        "is_gift": False,
        "product_line": "Şirince Infused Oils · 250 ml",
        "tagline": "Cold pressed with fresh garlic — a savory Aegean kitchen staple",
    },

    "SH-EVOO-CHILI-250ML": {
        "origin_place": "Şirince, Aegean Turkey",
        "story": [
            "Chili brings heat. Olive oil carries it. The two have been companions on Mediterranean "
            "tables since traders brought capsicum through the ancient port at Ephesus. This "
            "cold-pressed infusion delivers that warmth: bold enough to notice, measured enough "
            "to finish a dish rather than fight it.",
            "Especially at home on pizza, pasta, grilled vegetables, and meze — anywhere a lively, "
            "warm note can lift the whole plate.",
        ],
        "how_to_use": [
            ("🍕", "Pizza Drizzle"),    ("🍝", "Pasta Finishing"),
            ("🥦", "Grilled Vegetables"),("🥚", "Egg Dishes"),
            ("🫙", "Meze & Dipping"),   ("🐟", "Seafood"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "No heat — full flavour and nutrients preserved"),
            ("🫒", "Extra Virgin",    "Highest global olive oil classification"),
            ("🌶️", "Natural Infusion","Real chili — zero artificial flavouring"),
            ("🚫", "No Additives",    "Clean label, nothing synthetic"),
            ("📍", "Single Origin",   "Traceable provenance — Şirince, Aegean Turkey"),
        ],
        "is_gift": False,
        "product_line": "Şirince Infused Oils · 250 ml",
        "tagline": "A bold chili infusion — warm, lively, and deeply Mediterranean",
    },

    "SH-EVOO-MANDARIN-250ML": {
        "origin_place": "Bodrum & Şirince, Aegean Turkey",
        "story": [
            "The Bodrum mandarin grows on Turkey's southwestern coast, where the Aegean meets the "
            "Mediterranean and the citrus is small, fragrant, and deeply aromatic. Cold-pressing "
            "these mandarins alongside Şirince olives creates something genuinely unusual — "
            "brightness and olive character in the same pour.",
            "Light, distinctive, and beautifully suited to seafood, fresh salads, and any dish "
            "that benefits from a clean citrus finish.",
        ],
        "how_to_use": [
            ("🥗", "Fresh Salads"),    ("🐟", "Seafood & Fish"),
            ("🍋", "Citrus Dressings"),("🫙", "Appetizers"),
            ("🥩", "Light Marinades"), ("🍨", "Dessert Drizzle"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "No heat — full flavour and nutrients preserved"),
            ("🫒", "Extra Virgin",    "Highest global olive oil classification"),
            ("🍊", "Natural Infusion","Real Bodrum mandarin — zero artificial flavouring"),
            ("🚫", "No Additives",    "Clean label, nothing synthetic"),
            ("📍", "Single Origin",   "Traceable provenance — Aegean Turkey"),
        ],
        "is_gift": True,
        "product_line": "Şirince Infused Oils · 250 ml",
        "tagline": "Bright citrus meets Aegean olive — a rare cold pressed infusion",
    },

    "SH-EVOO-PLAIN-250ML": {
        "origin_place": "Şirince, Aegean Turkey",
        "story": [
            "Şirince sits on the slopes above ancient Ephesus, where olive groves have shaped the "
            "landscape for millennia. The olives pressed for this oil come from these hillside "
            "trees — harvested and cold pressed at peak freshness to preserve the clean, bright "
            "character of Aegean olive oil at its most honest.",
            "A single drop on bread. A drizzle over salad. The plain extra virgin is the truest "
            "expression of the olive itself — no distraction, just the fruit and its land.",
        ],
        "how_to_use": [
            ("🥗", "Salads & Greens"),  ("🍳", "Breakfast Table"),
            ("🍞", "Bread & Dipping"),  ("🫙", "Daily Cooking"),
            ("🥦", "Roasting"),         ("🍝", "Pasta Finishing"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "No heat — full flavour and nutrients preserved"),
            ("🫒", "Extra Virgin",    "Highest global olive oil classification"),
            ("✅", "Pure & Natural",  "Nothing added — 100% Aegean olive oil"),
            ("🚫", "No Additives",    "Clean label, nothing synthetic"),
            ("📍", "Single Origin",   "Traceable provenance — Şirince, Aegean Turkey"),
        ],
        "is_gift": False,
        "product_line": "Şirince Classic Oils · 250 ml",
        "tagline": "Pure cold pressed extra virgin from the hillside groves of Şirince",
    },

    # ── Eco Natural EVOO Tins ──────────────────────────────────────────────────

    "EN-EVOO-500ML-TIN": {
        "origin_place": "Aegean Turkey",
        "story": [
            "This tin holds an extra virgin olive oil built for daily kitchen life, with quality "
            "credentials you rarely find at everyday price points. At 0.2% acidity and 349 "
            "polyphenols, it sits well above the minimum standard for extra virgin classification.",
            "The classic tin format is a mark of authenticity in Aegean olive oil culture — "
            "durable, light-protective, and unmistakably honest about what's inside.",
        ],
        "how_to_use": [
            ("🍳", "Everyday Cooking"), ("🥗", "Salads"),
            ("🍞", "Bread & Dipping"),  ("🫙", "Finishing Drizzle"),
            ("🥦", "Roasting"),         ("🍝", "Pasta"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",      "First cold press — maximum quality"),
            ("🫒", "Extra Virgin",      "Highest global olive oil classification"),
            ("📊", "0.2% Acidity",      "Well below the 0.8% extra virgin limit"),
            ("💚", "349 Polyphenols",   "Exceptional antioxidant content"),
            ("📍", "Aegean Origin",     "Traceable single-origin provenance"),
        ],
        "is_gift": False,
        "product_line": "Eco Natural Extra Virgin Olive Oil · 500 ml",
        "tagline": "First cold press · 0.2% acidity · 349 polyphenols",
    },

    "EN-EVOO-1L-TIN": {
        "origin_place": "Aegean Turkey",
        "story": [
            "The 1-litre format is for kitchens where olive oil is a daily essential, not an "
            "occasional luxury. First cold pressed to preserve every quality marker, this tin "
            "brings 0.2% acidity and 349 polyphenols to your table in a practical volume that "
            "holds up to regular use.",
            "The tin's light-protective seal ensures quality from the first pour to the last — "
            "an Aegean extra virgin made to live on the counter, not the shelf.",
        ],
        "how_to_use": [
            ("🍳", "Daily Cooking"),   ("🥗", "Salads"),
            ("🍞", "Bread & Dipping"), ("🫙", "Finishing Drizzle"),
            ("🥦", "Roasting"),        ("🍝", "Pasta"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "First cold press — maximum quality"),
            ("🫒", "Extra Virgin",    "Highest global olive oil classification"),
            ("📊", "0.2% Acidity",    "Well below the 0.8% extra virgin limit"),
            ("💚", "349 Polyphenols", "Exceptional antioxidant content"),
            ("📍", "Aegean Origin",   "Traceable single-origin provenance"),
        ],
        "is_gift": False,
        "product_line": "Eco Natural Extra Virgin Olive Oil · 1 L",
        "tagline": "First cold press · 0.2% acidity · 349 polyphenols — family size",
    },

    # ── Early Harvest EVOOs ────────────────────────────────────────────────────

    "EN-EH-EVOO-50CL-RECT": {
        "origin_place": "Aegean Turkey",
        "story": [
            "Early harvest olive oil is pressed before the olives fully ripen — at the green "
            "stage, when polyphenol levels peak and the oil carries its most intense, grassy, "
            "and peppery character. At 0.1% acidity and 500+ polyphenols, this is Aegean olive "
            "oil at its most vibrant.",
            "The bottle you hold is evidence of a specific moment: late October, hillside groves, "
            "trees harvested days earlier than conventional wisdom suggests — for the sake of "
            "flavour and quality above everything else.",
        ],
        "how_to_use": [
            ("🥗", "Premium Salads"),  ("🍞", "Raw Dipping"),
            ("🍅", "Cold Dishes"),     ("🧀", "Cheese & Charcuterie"),
            ("🎁", "Gift Giving"),     ("🫙", "Finishing Drizzle"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",      "First cold press — maximum quality"),
            ("🫒", "Extra Virgin",      "Highest global olive oil classification"),
            ("🌱", "Early Harvest",     "Pressed at peak polyphenol content"),
            ("📊", "0.1% Acidity",      "Exceptionally low — finest grade"),
            ("💚", "500+ Polyphenols",  "Premium antioxidant benchmark"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Early Harvest EVOO · 50 cl",
        "tagline": "Early harvest · 0.1% acidity · 500+ polyphenols",
    },

    "EN-EH-EVOO-NA-SLIM": {
        "origin_place": "Aegean Turkey",
        "story": [
            "Early harvest olive oil is pressed before the olives fully ripen — at the green "
            "stage, when polyphenol levels peak and the oil carries its most intense character. "
            "At 0.1% acidity and 500+ polyphenols, this is among the finest Aegean olive oil "
            "classifications available.",
            "The slim bottle is designed for elegant table presentation and gifting — a refined "
            "format that makes the quality inside easy to communicate at a glance.",
        ],
        "how_to_use": [
            ("🥗", "Premium Salads"), ("🍞", "Raw Dipping"),
            ("🍅", "Cold Dishes"),    ("🧀", "Cheese Pairing"),
            ("🎁", "Gift Giving"),    ("🫙", "Finishing Drizzle"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",     "First cold press — maximum quality"),
            ("🫒", "Extra Virgin",     "Highest global olive oil classification"),
            ("🌱", "Early Harvest",    "Pressed at peak polyphenol content"),
            ("📊", "0.1% Acidity",     "Exceptionally low — finest grade"),
            ("💚", "500+ Polyphenols", "Premium antioxidant benchmark"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Early Harvest EVOO · Slim Bottle",
        "tagline": "Early harvest · 0.1% acidity · 500+ polyphenols — gift edition",
    },

    "EN-EH-EVOO-NA-OVAL": {
        "origin_place": "Aegean Turkey",
        "story": [
            "Early harvest olive oil is pressed at the green stage of ripening — the moment when "
            "polyphenols are highest and flavour is at its most vivid. 0.1% acidity and 500+ "
            "polyphenols mark this as a benchmark expression of Aegean early harvest quality.",
            "The oval decorative bottle gives this oil a distinctive artisanal character — made "
            "to stand on the gift table as confidently as it stands on the kitchen shelf.",
        ],
        "how_to_use": [
            ("🥗", "Premium Salads"), ("🍞", "Raw Dipping"),
            ("🍅", "Cold Dishes"),    ("🧀", "Cheese Pairing"),
            ("🎁", "Gift Giving"),    ("🫙", "Finishing Drizzle"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",     "First cold press — maximum quality"),
            ("🫒", "Extra Virgin",     "Highest global olive oil classification"),
            ("🌱", "Early Harvest",    "Pressed at peak polyphenol content"),
            ("📊", "0.1% Acidity",     "Exceptionally low — finest grade"),
            ("💚", "500+ Polyphenols", "Premium antioxidant benchmark"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Early Harvest EVOO · Oval Bottle",
        "tagline": "Early harvest · artisanal oval bottle · premium gift edition",
    },

    "EN-EH-EVOO-70CL-TEARDROP": {
        "origin_place": "Aegean Turkey",
        "story": [
            "Early harvest olive oil is pressed before the olives fully ripen, capturing peak "
            "polyphenol content and the most expressive flavour the Aegean grove can produce. "
            "0.1% acidity and 500+ polyphenols place this firmly in the premium tier.",
            "The sculpted teardrop bottle gives a sense of occasion — suited to gourmet tables, "
            "elevated gifting, and shelves where presentation is as important as provenance.",
        ],
        "how_to_use": [
            ("🥗", "Gourmet Salads"),  ("🍞", "Premium Dipping"),
            ("🍅", "Cold Dishes"),     ("🧀", "Cheese & Charcuterie"),
            ("🎁", "Gift Giving"),     ("🫙", "Finishing Drizzle"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",     "First cold press — maximum quality"),
            ("🫒", "Extra Virgin",     "Highest global olive oil classification"),
            ("🌱", "Early Harvest",    "Pressed at peak polyphenol content"),
            ("📊", "0.1% Acidity",     "Exceptionally low — finest grade"),
            ("💚", "500+ Polyphenols", "Premium antioxidant benchmark"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Early Harvest EVOO · 70 cl",
        "tagline": "Early harvest · teardrop bottle · 0.1% acidity · 500+ polyphenols",
    },

    "EN-EH-EVOO-NA-DECO-SQUARE": {
        "origin_place": "Aegean Turkey",
        "story": [
            "At 0.1% acidity and 500+ polyphenols, this early harvest extra virgin olive oil "
            "represents the finest quality tier within the Eco Natural range — pressed while the "
            "olives are still green, at the moment of peak flavour and antioxidant richness.",
            "The decorative square bottle gives it a strong gift identity: angular, modern, "
            "and unmistakably premium — designed to be given as confidently as it is used.",
        ],
        "how_to_use": [
            ("🥗", "Gourmet Salads"),  ("🍞", "Premium Dipping"),
            ("🍅", "Cold Dishes"),     ("🧀", "Cheese Pairing"),
            ("🎁", "Gift Giving"),     ("🫙", "Finishing Drizzle"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",     "First cold press — maximum quality"),
            ("🫒", "Extra Virgin",     "Highest global olive oil classification"),
            ("🌱", "Early Harvest",    "Pressed at peak polyphenol content"),
            ("📊", "0.1% Acidity",     "Exceptionally low — finest grade"),
            ("💚", "500+ Polyphenols", "Premium antioxidant benchmark"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Early Harvest EVOO · Decorative Square",
        "tagline": "Early harvest · decorative square bottle · premium gift edition",
    },

    "EN-EH-EVOO-70CL-ROUND": {
        "origin_place": "Aegean Turkey",
        "story": [
            "Early harvest olive oil is pressed at the green stage — the moment when polyphenol "
            "content peaks and Aegean olive oil expresses its most vivid character. 0.1% acidity "
            "and 500+ polyphenols mark this as a benchmark quality.",
            "The ornamental round bottle turns it into a statement piece: a 70 cl format designed "
            "for the table, the shelf, or the gift set — wherever first impressions matter.",
        ],
        "how_to_use": [
            ("🥗", "Gourmet Salads"),  ("🍞", "Premium Dipping"),
            ("🍅", "Cold Dishes"),     ("🧀", "Cheese & Charcuterie"),
            ("🎁", "Gift Giving"),     ("🫙", "Finishing Drizzle"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",     "First cold press — maximum quality"),
            ("🫒", "Extra Virgin",     "Highest global olive oil classification"),
            ("🌱", "Early Harvest",    "Pressed at peak polyphenol content"),
            ("📊", "0.1% Acidity",     "Exceptionally low — finest grade"),
            ("💚", "500+ Polyphenols", "Premium antioxidant benchmark"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Early Harvest EVOO · 70 cl",
        "tagline": "Early harvest · ornamental round bottle · 0.1% acidity",
    },

    # ── Specialty Seed & Plant Oils ────────────────────────────────────────────

    "EN-HEMP-SEED-OIL-250ML": {
        "origin_place": "Turkey",
        "story": [
            "Hemp seed has been cultivated in Anatolia for thousands of years — one of the oldest "
            "crop plants in human history. Pressed cold from whole seeds to preserve every nuance "
            "of its mild nutty character, this oil carries that ancient lineage in a clean, "
            "modern format.",
            "Light on the palate, versatile in the kitchen — best kept for cold applications "
            "where its gentle flavour and natural character can come through without heat.",
        ],
        "how_to_use": [
            ("🥗", "Salads & Bowls"),   ("🫙", "Finishing Drizzle"),
            ("🥑", "Grain Bowls"),      ("🧁", "Cold Baking"),
            ("🥤", "Smoothies"),        ("🍽️", "Table Dressing"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",   "No heat — full nutrition and flavour preserved"),
            ("🌱", "Plant-Based",    "100% plant origin, nothing else"),
            ("🚫", "No Additives",   "Clean label, nothing synthetic"),
            ("✅", "Natural",        "Minimally processed, whole-seed pressed"),
            ("🌰", "Nutty Profile",  "Distinctive mild flavour — not for cooking"),
        ],
        "is_gift": False,
        "product_line": "Eco Natural Specialty Oils · 250 ml",
        "tagline": "Cold pressed from whole hemp seeds — mild, nutty, and purely natural",
    },

    "EN-AVOCADO-OIL-250ML": {
        "origin_place": "Turkey",
        "story": [
            "Avocado oil crossed into the premium kitchen from the world's finest culinary "
            "traditions. Cold-extracted to maintain its exceptionally clean profile, Eco Natural's "
            "version is designed for the modern table: a polished, versatile oil that brings "
            "quiet refinement without declaring itself.",
            "Its neutral-to-delicate flavour makes it a natural companion to everything from "
            "simple green salads to more composed finishing moments.",
        ],
        "how_to_use": [
            ("🥗", "Salads"),           ("🫙", "Finishing Drizzle"),
            ("🍳", "Light Cooking"),    ("🥑", "Cold Dishes"),
            ("🍞", "Bread & Dipping"),  ("🎁", "Gift Giving"),
        ],
        "badges": [
            ("❄️", "Cold Extracted",  "No heat — full nutrition and flavour preserved"),
            ("🌱", "Plant-Based",     "100% plant origin"),
            ("🚫", "No Additives",    "Clean label, nothing synthetic"),
            ("✅", "Premium Grade",   "Refined for clean, delicate flavour"),
            ("🥑", "Avocado Origin",  "Pure avocado — nothing else"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Specialty Oils · 250 ml",
        "tagline": "Clean, delicate, cold extracted — a refined everyday oil",
    },

    "EN-PUMPKIN-SEED-OIL-250ML": {
        "origin_place": "Turkey",
        "story": [
            "Pumpkin seed oil is one of the great character oils — dark, intensely flavoured, "
            "and unmistakably itself. Cold-pressed from roasted seeds, it transforms salads, "
            "cold plates, and finishing applications into something memorable.",
            "Use it sparingly over soups, salads, or fresh cheese — its bold roasted profile "
            "rewards restraint and makes a strong impression in small amounts.",
        ],
        "how_to_use": [
            ("🥗", "Salads"),          ("🍲", "Soups & Drizzle"),
            ("🧀", "Fresh Cheese"),    ("🫙", "Finishing Drizzle"),
            ("🥙", "Meze Plates"),     ("🎁", "Gourmet Gift"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",   "No heat — full flavour and nutrition preserved"),
            ("🌱", "Plant-Based",    "100% plant origin"),
            ("🚫", "No Additives",   "Clean label, nothing synthetic"),
            ("🌰", "Rich Flavour",   "Bold roasted seed character"),
            ("⭐", "Gourmet Grade",  "Specialty oil for discerning kitchens"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Specialty Oils · 250 ml",
        "tagline": "Bold roasted seed character — a gourmet cold pressed specialty oil",
    },

    "EN-POMEGRANATE-SEED-OIL-250ML": {
        "origin_place": "Turkey",
        "story": [
            "Pomegranate has been revered across Anatolia and the Levant since antiquity — a "
            "symbol of abundance painted on palace walls and served at every celebration. "
            "Extracting oil from its seeds is a laborious process, which is why pomegranate "
            "seed oil remains rare. This bottle contains something genuinely precious.",
            "A specialty product for curated collections and discerning kitchens — its elegant "
            "presentation reflects the rarity of what is inside.",
        ],
        "how_to_use": [
            ("🥗", "Premium Salads"),  ("🫙", "Finishing Drizzle"),
            ("🧀", "Cheese Pairing"),  ("🍓", "Fruit Dishes"),
            ("🎁", "Gourmet Gift"),    ("🍽️", "Fine Dining"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",   "No heat — full nutrition and flavour preserved"),
            ("🌱", "Plant-Based",    "100% plant origin"),
            ("🚫", "No Additives",   "Clean label, nothing synthetic"),
            ("💎", "Rare Specialty", "Premium laborious extraction — limited volumes"),
            ("📍", "Anatolian",      "Rooted in the pomegranate heartland of Turkey"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Specialty Oils · 250 ml",
        "tagline": "A rare cold pressed specialty oil from the pomegranate heartland",
    },

    "EN-BLACK-SEED-OIL-250ML": {
        "origin_place": "Turkey",
        "story": [
            "Nigella sativa — black seed — has been used in Anatolian kitchens and medicine for "
            "over 3,000 years. Referenced in ancient texts and traded across old spice routes, "
            "its intense aroma and distinctive bitter-warm character make it one of the most "
            "storied ingredients in this part of the world.",
            "With a bold heritage identity and premium presentation, this oil is a strong "
            "addition to natural product collections and traditional pantries alike.",
        ],
        "how_to_use": [
            ("🍶", "Wellness Ritual"), ("🥗", "Salad Drizzle"),
            ("🍞", "Bread Dipping"),   ("🫙", "Small Doses"),
            ("🌿", "Natural Kitchen"), ("🎁", "Thoughtful Gift"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "No heat — full nutrition and flavour preserved"),
            ("🌱", "Plant-Based",     "100% plant origin"),
            ("🚫", "No Additives",    "Clean label, nothing synthetic"),
            ("🕌", "Ancient Heritage","Used in Anatolia for 3,000+ years"),
            ("⭐", "Specialty Grade", "Premium presentation and heritage identity"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Specialty Oils · 250 ml",
        "tagline": "3,000 years of Anatolian tradition — bold, aromatic, cold pressed",
    },

    "EN-THISTLE-SEED-OIL-250ML": {
        "origin_place": "Aegean Turkey",
        "story": [
            "Milk thistle has grown wild across the Aegean hills long before it was cultivated — "
            "a plant with deep roots in traditional natural food culture. Its seeds yield an oil "
            "with a clean, botanical identity, pressed cold to preserve the qualities that have "
            "made it a favourite in natural and wellness product collections.",
            "A niche specialty product for customers drawn to traditional seed-based oils and "
            "distinctive, nature-forward ingredients.",
        ],
        "how_to_use": [
            ("🥗", "Salad Drizzle"),  ("🫙", "Finishing Oil"),
            ("🌿", "Natural Kitchen"),("🍶", "Wellness Use"),
            ("🍞", "Bread Dipping"),  ("🎁", "Specialty Gift"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",   "No heat — full nutrition and flavour preserved"),
            ("🌱", "Plant-Based",    "100% plant origin"),
            ("🚫", "No Additives",   "Clean label, nothing synthetic"),
            ("🌾", "Botanical",      "Traditional Aegean wild thistle seed"),
            ("⭐", "Specialty Grade","Niche product for curated natural ranges"),
        ],
        "is_gift": False,
        "product_line": "Eco Natural Specialty Oils · 250 ml",
        "tagline": "Wild Aegean thistle seed — a botanical cold pressed specialty oil",
    },

    "EN-POPPY-SEED-OIL-250ML": {
        "origin_place": "Turkey",
        "story": [
            "Poppy seed oil occupies a rare corner of the gourmet world — light, smooth, and "
            "subtle in ways that most oils are not. Cold-pressed from untreated seeds, it is the "
            "kind of ingredient that gourmet cooks discover and keep for finishing moments when "
            "nothing else quite works.",
            "Its smooth, elegant character suits delicate dishes, premium salads, and gift "
            "assortments built around uncommon ingredients.",
        ],
        "how_to_use": [
            ("🥗", "Delicate Salads"), ("🫙", "Finishing Drizzle"),
            ("🧀", "Cheese Pairing"),  ("🍽️", "Fine Dining"),
            ("🎁", "Gourmet Gift"),    ("🥗", "Cold Dressings"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",   "No heat — full flavour and nutrition preserved"),
            ("🌱", "Plant-Based",    "100% plant origin"),
            ("🚫", "No Additives",   "Clean label, nothing synthetic"),
            ("💎", "Rare Specialty", "Uncommon oil for discerning collections"),
            ("✨", "Elegant",        "Light, smooth, refined character"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Specialty Oils · 250 ml",
        "tagline": "A rare, smooth specialty oil for gourmet kitchens and fine gifting",
    },

    "EN-FIG-SEED-OIL-NA": {
        "origin_place": "Turkey",
        "story": [
            "The fig is one of the oldest cultivated fruits — domesticated in the Fertile Crescent "
            "before wheat. Its seeds yield an exceptionally rare oil, delicate and rich in "
            "bioactive compounds, extracted in small quantities because the process demands it.",
            "Fig seed oil exists at the outer edge of the gourmet world — the kind of ingredient "
            "found in single-origin natural collections and on tables where the obvious is "
            "never enough.",
        ],
        "how_to_use": [
            ("🍽️", "Fine Dining"),    ("🥗", "Premium Salads"),
            ("🧀", "Cheese Pairing"), ("🫙", "Finishing Drizzle"),
            ("🎁", "Rare Gift"),      ("🌿", "Gourmet Kitchen"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "No heat — full nutrition and flavour preserved"),
            ("🌱", "Plant-Based",     "100% plant origin"),
            ("🚫", "No Additives",    "Clean label, nothing synthetic"),
            ("💎", "Rare Specialty",  "Small-batch extraction — genuinely uncommon"),
            ("🌿", "Ancient Fruit",   "From one of the world's oldest cultivated plants"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Specialty Oils",
        "tagline": "One of the rarest cold pressed oils in the world — from the ancient fig",
    },

    # ── Metis Hierapolis ───────────────────────────────────────────────────────

    "MH-SAFFLOWER-OIL-250ML": {
        "origin_place": "Hierapolis (Pamukkale), Turkey",
        "story": [
            "The safflower has been cultivated in Anatolia since Roman times — Hierapolis, "
            "now known as Pamukkale, was an ancient city where agriculture and trade defined "
            "daily life. Metis Hierapolis takes its name from that heritage: a refined, clean "
            "oil made in the tradition of a region that has long valued quality ingredients.",
            "Light, clean, and pleasingly neutral — suited to modern kitchens that value "
            "versatility alongside natural credentials.",
        ],
        "how_to_use": [
            ("🥗", "Salads"),          ("🍳", "Light Cooking"),
            ("🫙", "Finishing Oil"),   ("🥦", "Cold Dishes"),
            ("🍞", "Bread Dipping"),   ("🎁", "Natural Gift"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "No heat — full nutrition and flavour preserved"),
            ("🌱", "Plant-Based",     "100% plant origin"),
            ("🚫", "No Additives",    "Clean label, nothing synthetic"),
            ("✅", "Versatile",       "Light neutral flavour for everyday use"),
            ("📍", "Anatolian",       "Named after ancient Hierapolis, Pamukkale"),
        ],
        "is_gift": False,
        "product_line": "Metis Hierapolis · 250 ml",
        "tagline": "A light, versatile specialty oil from ancient Anatolian heritage",
    },

    # ── Extracts & Condiments ──────────────────────────────────────────────────

    "EN-CAROB-EXTRACT-680G": {
        "origin_place": "Turkey",
        "story": [
            "The carob tree is one of the oldest cultivated trees in the eastern Mediterranean. "
            "Its sweet pods were traded along ancient routes as a natural sweetener long before "
            "cane sugar reached these shores. In Anatolia, carob extract — keçiboynuzu pekmezi — "
            "remains a deeply traditional pantry staple, spread on bread at breakfast and stirred "
            "into milk.",
            "This 680 g format is made for regular home use: slow-cooked, naturally sweet, and "
            "built to outlast more fleeting food trends. No added sugar, no artificial anything.",
        ],
        "how_to_use": [
            ("🍞", "Breakfast Spread"), ("🥛", "Stirred in Milk"),
            ("🍨", "Dessert Topping"),  ("🍵", "With Tea"),
            ("🫙", "By the Spoon"),     ("🎁", "Traditional Gift"),
        ],
        "badges": [
            ("🌱", "Plant-Based",       "100% plant origin"),
            ("🚫", "No Added Sugar",    "Natural sweetness from the carob itself"),
            ("🚫", "No Artificial",     "Clean label — nothing synthetic"),
            ("🕌", "Ancient Heritage",  "Traded in Anatolia for thousands of years"),
            ("✅", "Traditional Recipe","Made as it has always been made"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Extracts · 680 g",
        "tagline": "Ancient Anatolian sweetness — naturally rich carob extract",
    },

    "EN-CAROB-EXTRACT-340G": {
        "origin_place": "Turkey",
        "story": [
            "The carob tree is one of the oldest cultivated trees in the eastern Mediterranean. "
            "Its sweet pods were traded along ancient routes as a natural sweetener long before "
            "cane sugar reached these shores. In Anatolia, carob extract — keçiboynuzu pekmezi — "
            "remains a deeply traditional pantry staple.",
            "The 340 g size delivers the same richly traditional taste in a compact, practical "
            "format — ideal for discovering the product or for everyday use at a smaller scale.",
        ],
        "how_to_use": [
            ("🍞", "Breakfast Spread"), ("🥛", "Stirred in Milk"),
            ("🍨", "Dessert Topping"),  ("🍵", "With Tea"),
            ("🫙", "By the Spoon"),     ("🎁", "Traditional Gift"),
        ],
        "badges": [
            ("🌱", "Plant-Based",      "100% plant origin"),
            ("🚫", "No Added Sugar",   "Natural sweetness from the carob itself"),
            ("🚫", "No Artificial",    "Clean label — nothing synthetic"),
            ("🕌", "Ancient Heritage", "Traded in Anatolia for thousands of years"),
            ("✅", "Traditional Recipe","Made as it has always been made"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Extracts · 340 g",
        "tagline": "Ancient Anatolian sweetness — compact everyday carob extract",
    },

    "EN-POMEGRANATE-SOUR-340G": {
        "origin_place": "Aegean & Southern Turkey",
        "story": [
            "Pomegranate sour — nar ekşisi in Turkish — is one of the essential condiments of "
            "Anatolian cooking. Made by reducing pomegranate juice to a concentrated sweet-sour "
            "liquid, it has been used for centuries to finish salads, dress grilled vegetables, "
            "and bring balance to meat dishes.",
            "The pomegranates for this version come from Aegean and southern Turkey, where the "
            "fruit grows at its best — large, ruby-red, and intensely flavoured by long, "
            "warm growing seasons.",
        ],
        "how_to_use": [
            ("🥗", "Salad Dressing"),  ("🥩", "Meat Marinades"),
            ("🫑", "Grilled Vegetables"),("🫙", "Meze Finishing"),
            ("🍚", "Grain Dishes"),    ("🎁", "Gourmet Gift"),
        ],
        "badges": [
            ("🌱", "Plant-Based",       "100% plant origin"),
            ("🚫", "No Artificial",     "Clean label — nothing synthetic"),
            ("🕌", "Ancient Condiment", "Used in Anatolian kitchens for centuries"),
            ("🍎", "Aegean Pomegranate","Sourced from Turkey's finest-growing regions"),
            ("✅", "Versatile",         "Sweet-sour balance for dozens of dishes"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Condiments · 340 g",
        "tagline": "Sweet-sour Anatolian classic — the essential pomegranate condiment",
    },

    # ── Olive Elixir ───────────────────────────────────────────────────────────

    "EN-OLIVE-ELIXIR-NA": {
        "origin_place": "Şirince, Aegean Turkey",
        "story": [
            "Zeytin sütü — literally 'olive milk' — is the cloudy, protein-rich liquid that "
            "emerges from olives during the first moments of cold pressing, before the oil fully "
            "separates. It has been consumed in olive-growing regions for centuries as a raw, "
            "unprocessed expression of the olive at peak freshness.",
            "What ends up in this bottle is the closest thing to standing in a Şirince press "
            "house at harvest time. A boutique product in every sense: rare, seasonal, and built "
            "around a single fleeting moment in the olive year.",
        ],
        "how_to_use": [
            ("🍵", "Drink Raw"),        ("🥗", "Salad Finishing"),
            ("🍞", "Bread Pairing"),    ("🧴", "Skin & Wellness"),
            ("🫙", "Premium Serving"),  ("🎁", "Rare Gift"),
        ],
        "badges": [
            ("❄️", "Cold Pressed",    "Unprocessed — captured at the very first press"),
            ("🫒", "Olive Elixir",    "Rare zeytin sütü — not standard olive oil"),
            ("🚫", "No Additives",    "Nothing added — purely the olive"),
            ("📍", "Şirince Origin",  "Traceable Aegean provenance"),
            ("💎", "Boutique",        "Small batch, seasonal, genuinely rare"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Zeytin Sütü",
        "tagline": "The rarest expression of the Aegean olive — cold pressed, unfiltered",
    },

    # ── Salad Dressing ─────────────────────────────────────────────────────────

    "EN-SALAD-DRESSING-NA": {
        "origin_place": "Turkey",
        "story": [
            "The Aegean kitchen has always dressed its salads simply — good oil, a sharp note, "
            "clean herbs. No elaborate processes, no long ingredient lists. This ready-made "
            "dressing is built on that same principle: an olive oil foundation with a balanced "
            "seasoning that does the work so you don't have to.",
            "Practical, clean-label, and built for everyday use across salads, cold vegetables, "
            "and light plates.",
        ],
        "how_to_use": [
            ("🥗", "Green Salads"),     ("🥦", "Vegetable Dishes"),
            ("🍅", "Tomato Salads"),    ("🥙", "Wraps & Plates"),
            ("🍽️", "Quick Meals"),     ("🫙", "Table Dressing"),
        ],
        "badges": [
            ("🫒", "Olive Oil Base",  "Built on quality Aegean olive oil"),
            ("🚫", "No Artificial",   "Clean label — nothing synthetic"),
            ("✅", "Ready to Use",    "No preparation needed"),
            ("🌿", "Mediterranean",   "Balanced Aegean flavour profile"),
            ("⚡", "Everyday",        "Made for daily convenient use"),
        ],
        "is_gift": False,
        "product_line": "Eco Natural Condiments",
        "tagline": "Aegean-style salad dressing — clean ingredients, ready to pour",
    },

    # ── Turkish Delight ────────────────────────────────────────────────────────

    "EN-TURKISH-DELIGHT-GIFT-BOX-NA": {
        "origin_place": "Antalya, Turkey",
        "story": [
            "Lokum — Turkish delight — has been made in Anatolia since the Ottoman court "
            "perfected the art of confectionery in the 18th century. The original, made with "
            "rose water, sugar, and starch, was so influential it eventually gave the English "
            "language its most famous sweet name.",
            "This Antalya-made gift box carries that heritage in a modern, curated format — "
            "vibrant, polished, and designed for those who want to take a genuine piece of this "
            "place home with them.",
        ],
        "how_to_use": [
            ("☕", "With Turkish Tea"),  ("🎁", "Gift Giving"),
            ("🍽️", "Dessert Table"),    ("🧀", "With Cheese"),
            ("✈️", "Travel Souvenir"),  ("🎊", "Festive Occasions"),
        ],
        "badges": [
            ("🕌", "Ottoman Heritage", "A confectionery tradition since the 18th century"),
            ("🌹", "Rose Water",       "Traditional flavoring — authentic recipe"),
            ("🚫", "No Artificial",    "Natural ingredients, traditional process"),
            ("📍", "Antalya Made",     "Crafted in Turkey's premium confectionery region"),
            ("🎁", "Gift Ready",       "Designed for gifting from first look"),
        ],
        "is_gift": True,
        "product_line": "Eco Natural Confectionery",
        "tagline": "An Ottoman tradition in a modern gift box — made in Antalya, Turkey",
    },
}


# ── CSS & HTML template ────────────────────────────────────────────────────────

CSS = """
    *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
    :root {
      --cream:    #faf8f2;
      --white:    #ffffff;
      --olive:    #3d6b41;
      --olive-l:  #eef5ec;
      --terra:    #b5763a;
      --terra-l:  #fdf3e8;
      --dark:     #1c2b1e;
      --text:     #2c2c2c;
      --muted:    #72716a;
      --border:   #e4e0d6;
      --radius:   14px;
      --radius-sm: 8px;
      --amber:    #c8883a;
      --amber-l:  #f5e6cc;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: var(--cream);
      color: var(--text);
      line-height: 1.55;
      -webkit-font-smoothing: antialiased;
    }
    .topbar {
      background: var(--dark);
      color: #c4d4bb;
      padding: 10px 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      font-size: 13px;
      position: sticky;
      top: 0;
      z-index: 100;
      border-bottom: 2px solid var(--amber);
    }
    .topbar a { color: inherit; text-decoration: none; }
    .topbar-left {
      display: flex;
      align-items: center;
      gap: 10px;
    }
    .topbar-logo { height: 24px; width: auto; display: block; }
    .topbar-brand {
      font-size: 14px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #ffffff;
    }
    .topbar-back { opacity: 0.7; }
    .topbar-back:hover { opacity: 1; }
    .hero {
      background: radial-gradient(ellipse at 50% 65%, #c8883a22 0%, #3d6b4133 35%, #1c2b1e 75%);
      min-height: 85vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: flex-end;
      padding: 40px 20px 32px;
      text-align: center;
      position: relative;
    }
    @media (min-width: 768px) {
      .hero { min-height: 70vh; }
    }
    .hero-img-wrap {
      width: 100%;
      display: flex;
      justify-content: center;
      margin-bottom: 28px;
    }
    .hero-img-wrap img {
      max-height: 420px;
      max-width: 90%;
      width: auto;
      display: block;
      filter: drop-shadow(0 24px 64px rgba(197, 133, 58, 0.55));
      animation: riseIn 0.7s ease-out both;
    }
    @keyframes riseIn {
      from { transform: translateY(32px); opacity: 0; }
      to   { transform: translateY(0);    opacity: 1; }
    }
    .hero-copy {
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 14px;
      max-width: 540px;
    }
    .product-line {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: #8fba88;
    }
    h1 {
      font-family: Georgia, 'Times New Roman', serif;
      font-size: clamp(1.6rem, 6vw, 2.4rem);
      font-weight: 700;
      line-height: 1.2;
      color: #ffffff;
      text-shadow: 0 2px 16px rgba(0,0,0,0.4);
    }
    .tagline { font-size: 1rem; color: rgba(255,255,255,0.72); font-style: italic; }
    .badge-strip { display: flex; flex-wrap: wrap; gap: 7px; justify-content: center; }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      background: rgba(255,255,255,0.12);
      border: 1px solid rgba(255,255,255,0.20);
      color: #ffffff;
      font-size: 12px;
      font-weight: 600;
      padding: 5px 11px;
      border-radius: 99px;
      white-space: nowrap;
    }
    .gift-banner {
      background: rgba(181,118,58,0.20);
      border: 1px solid rgba(197,133,58,0.45);
      border-radius: var(--radius-sm);
      padding: 10px 16px;
      font-size: 13px;
      font-weight: 600;
      color: #f5d49a;
      display: flex;
      align-items: center;
      gap: 8px;
    }
    .scroll-hint {
      position: absolute;
      bottom: 18px;
      left: 50%;
      transform: translateX(-50%);
      color: rgba(255,255,255,0.45);
      font-size: 20px;
      animation: pulse 2s ease-in-out infinite;
      line-height: 1;
    }
    @keyframes pulse {
      0%, 100% { opacity: 0.45; transform: translateX(-50%) translateY(0); }
      50%       { opacity: 0.9;  transform: translateX(-50%) translateY(4px); }
    }
    .trust-strip {
      background: var(--white);
      border-bottom: 1px solid var(--border);
      padding: 20px 16px;
    }
    .trust-strip-inner {
      max-width: 960px;
      margin: 0 auto;
      display: flex;
      overflow-x: auto;
      -webkit-overflow-scrolling: touch;
    }
    .trust-item {
      flex: 1 0 140px;
      display: flex;
      flex-direction: column;
      align-items: center;
      text-align: center;
      padding: 12px 16px;
      border-right: 1px solid var(--border);
      gap: 6px;
    }
    .trust-item:last-child { border-right: none; }
    .trust-icon { font-size: 32px; line-height: 1; }
    .trust-label { font-size: 12px; font-weight: 700; color: var(--dark); }
    .trust-desc  { font-size: 11px; color: var(--muted); line-height: 1.4; }
    .wrap { max-width: 960px; margin: 0 auto; padding: 0 16px 64px; }
    .section { padding-top: 40px; }
    .section-eyebrow {
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.15em;
      text-transform: uppercase;
      color: var(--terra);
      margin-bottom: 6px;
    }
    .section-heading {
      font-size: 1.2rem;
      font-weight: 700;
      color: var(--dark);
      margin-bottom: 16px;
      line-height: 1.3;
    }
    .story-card {
      background: var(--dark);
      color: #cee0c5;
      border-radius: var(--radius);
      padding: 32px 28px 34px;
      position: relative;
      overflow: hidden;
    }
    .story-card::before {
      content: '\\201C';
      position: absolute;
      top: -18px;
      left: 14px;
      font-size: 130px;
      color: #3d6b41;
      opacity: 0.2;
      font-family: Georgia, serif;
      line-height: 1;
      pointer-events: none;
    }
    .origin-chip {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255,255,255,0.09);
      border: 1px solid rgba(255,255,255,0.14);
      border-radius: 99px;
      font-size: 12px;
      font-weight: 600;
      padding: 5px 12px;
      color: #9fbf96;
      margin-bottom: 18px;
    }
    .story-card p { font-size: 0.97rem; line-height: 1.8; position: relative; }
    .story-card p + p { margin-top: 12px; }
    .use-grid {
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 10px;
    }
    @media (min-width: 720px) {
      .use-grid { grid-template-columns: repeat(6, 1fr); }
    }
    .use-tile {
      background: var(--white);
      border: 1px solid var(--border);
      border-top: 3px solid var(--olive);
      border-radius: var(--radius-sm);
      padding: 18px 10px 14px;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 8px;
      transition: border-top-color 0.2s;
    }
    .use-tile:hover { border-top-color: #2e5230; }
    .use-icon { font-size: 28px; line-height: 1; }
    .use-label { font-size: 11px; font-weight: 600; color: var(--text); line-height: 1.35; }
    .quality-grid {
      display: grid;
      grid-template-columns: repeat(2, 1fr);
      gap: 10px;
    }
    @media (min-width: 480px) {
      .quality-grid { grid-template-columns: repeat(3, 1fr); }
    }
    @media (min-width: 720px) {
      .quality-grid { grid-template-columns: repeat(5, 1fr); }
    }
    .quality-card {
      background: var(--olive-l);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 18px 14px 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 7px;
      text-align: center;
    }
    .quality-icon {
      width: 38px;
      height: 38px;
      border-radius: 50%;
      background: var(--white);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 19px;
    }
    .quality-name { font-size: 11px; font-weight: 700; color: var(--dark); line-height: 1.3; }
    .quality-desc { font-size: 10px; color: var(--muted); line-height: 1.4; }
    .divider { border: none; border-top: 1px solid var(--border); margin-top: 40px; }
    .product-meta { margin-top: 20px; font-size: 12px; color: var(--muted); }
    .product-meta code { font-size: 11.5px; }
    .footer {
      background: var(--dark);
      color: #7a927a;
      text-align: center;
      padding: 26px 16px;
      font-size: 12px;
      margin-top: 56px;
    }
    .footer a { color: #9fbf96; text-decoration: none; }
    .footer-sub { margin-top: 7px; opacity: 0.6; }
"""


def _badges_html(badges: list[tuple]) -> str:
    # Hero strip — first 4 badges, white-glass style on dark background
    parts = []
    for badge in badges[:4]:
        parts.append(f'<span class="badge">{escape(badge[0])} {escape(badge[1])}</span>')
    return "\n          ".join(parts)


def _use_tiles_html(uses: list[tuple]) -> str:
    parts = []
    for emoji, label in uses:
        parts.append(
            f'<div class="use-tile">'
            f'<div class="use-icon">{escape(emoji)}</div>'
            f'<div class="use-label">{escape(label)}</div>'
            f"</div>"
        )
    return "\n        ".join(parts)


def _quality_cards_html(badges: list[tuple]) -> str:
    parts = []
    for emoji, name, desc in badges:
        parts.append(
            f'<div class="quality-card">'
            f'<div class="quality-icon">{escape(emoji)}</div>'
            f'<div class="quality-name">{escape(name)}</div>'
            f'<div class="quality-desc">{escape(desc)}</div>'
            f"</div>"
        )
    return "\n        ".join(parts)


def _story_html(paragraphs: list[str]) -> str:
    return "\n        ".join(f"<p>{escape(p)}</p>" for p in paragraphs)


def _trust_strip_html(badges: list[tuple]) -> str:
    parts = []
    for emoji, name, desc in badges[:3]:
        parts.append(
            f'<div class="trust-item">'
            f'<div class="trust-icon">{escape(emoji)}</div>'
            f'<div class="trust-label">{escape(name)}</div>'
            f'<div class="trust-desc">{escape(desc)}</div>'
            f'</div>'
        )
    return "\n        ".join(parts)


def page_template(row: dict) -> str:
    product_id   = row["product_id"].strip()
    page_title   = row["page_title"].strip()
    short_desc   = row["short_description"].strip()
    full_desc    = row["full_description"].strip()
    seo_title    = row["seo_title"].strip()
    meta_desc    = row["meta_description"].strip()
    img_ext    = "png" if (ROOT / "img" / f"{product_id}.png").exists() else "JPG"
    image_path = f"img/{product_id}.{img_ext}"

    enrich = ENRICHMENT.get(product_id, {})

    # ── Enrichment fields with fallbacks ──────────────────────────────────────
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

    gift_banner = (
        '<div class="gift-banner">&#127873; Makes a beautiful gift &mdash; perfect for food lovers</div>'
        if is_gift else ""
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(seo_title or page_title)} | Eco Natural</title>
  <meta name="description" content="{escape(meta_desc)}">
  <style>{CSS}</style>
</head>
<body>

  <nav class="topbar">
    <div class="topbar-left">
      <img class="topbar-logo" src="./logo.png" alt="Eco Natural">
      <span class="topbar-brand">ECO NATURAL</span>
    </div>
    <a class="topbar-back" href="./index.html">&#8592; All Products</a>
  </nav>

  <section class="hero">
    <div class="hero-img-wrap">
      <img src="{image_path}" alt="{escape(page_title)}">
    </div>
    <div class="hero-copy">
      <div class="product-line">{escape(product_line)}</div>
      <h1>{escape(page_title)}</h1>
      <p class="tagline">{escape(tagline)}</p>
      <div class="badge-strip">
        {_badges_html(badges)}
      </div>
      {gift_banner}
    </div>
    <div class="scroll-hint">&#9660;</div>
  </section>

  <div class="trust-strip">
    <div class="trust-strip-inner">
      {_trust_strip_html(badges)}
    </div>
  </div>

  <div class="wrap">

    <div class="section">
      <div class="section-eyebrow">Origin &amp; Story</div>
      <div class="story-card">
        <div class="origin-chip">&#128205; {escape(origin_place)}</div>
        {_story_html(story_paras)}
      </div>
    </div>

    <div class="section">
      <div class="section-eyebrow">How to Enjoy</div>
      <div class="section-heading">Six ways to use it at home</div>
      <div class="use-grid">
        {_use_tiles_html(how_to_use)}
      </div>
    </div>

    <div class="section">
      <div class="section-eyebrow">Quality &amp; Standards</div>
      <div class="section-heading">What makes it exceptional</div>
      <div class="quality-grid">
        {_quality_cards_html(badges)}
      </div>
    </div>

    <hr class="divider">
    <div class="product-meta">
      Product ID:&nbsp;<code>{escape(product_id)}</code>
    </div>

  </div>

  <footer class="footer">
    <a href="./index.html">&#8592; Back to Eco Natural Product Catalog</a>
    <div class="footer-sub">Eco Natural &middot; Artisan Natural Products &middot; Aegean Turkey</div>
  </footer>

</body>
</html>
"""


def index_template(items: list[tuple[str, str, str]]) -> str:
    def _category(pid: str) -> str:
        if pid.startswith("SH-"):
            return "Şirince Infused Oils"
        if pid.startswith("EN-EH-EVOO-"):
            return "Early Harvest Olive Oils"
        if pid.startswith("EN-EVOO-"):
            return "Eco Natural Olive Oils"
        if pid.startswith("EN-OLIVE-"):
            return "Olive Elixir"
        if pid.startswith(("EN-CAROB-", "EN-POMEGRANATE-SOUR-", "EN-SALAD-")):
            return "Condiments & Extracts"
        if pid.startswith("EN-TURKISH-"):
            return "Confectionery & Gifts"
        if pid.startswith("MH-"):
            return "Metis Hierapolis"
        return "Specialty Oils"

    groups: dict[str, list] = {}
    for fn, title, pid in items:
        cat = _category(pid)
        groups.setdefault(cat, []).append((fn, title, pid))

    sections_html = ""
    for cat, entries in groups.items():
        links = "\n".join(
            f'      <li><a href="{escape(fn)}">{escape(title)}</a>'
            f' <span>&#x2014; {escape(pid)}</span></li>'
            for fn, title, pid in entries
        )
        sections_html += f"""
    <div class="cat-header">{escape(cat)}</div>
    <div class="card">
      <ul>
{links}
      </ul>
    </div>"""

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Eco Natural — Product Catalog</title>
  <style>
    *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #faf8f2;
      color: #2c2c2c;
      line-height: 1.55;
    }}
    .topbar {{
      background: #1c2b1e;
      color: #c4d4bb;
      padding: 12px 20px;
      display: flex;
      align-items: center;
      gap: 12px;
      border-bottom: 2px solid #c8883a;
    }}
    .topbar-logo {{ height: 24px; width: auto; display: block; }}
    .topbar-brand {{
      font-size: 15px;
      font-weight: 700;
      letter-spacing: 0.1em;
      text-transform: uppercase;
      color: #ffffff;
    }}
    .wrap {{ max-width: 760px; margin: 0 auto; padding: 32px 16px 60px; }}
    h1 {{ font-size: 1.5rem; color: #1c2b1e; margin-bottom: 4px; }}
    .sub {{ font-size: 14px; color: #72716a; margin-bottom: 28px; }}
    .cat-header {{
      font-size: 11px;
      font-weight: 700;
      letter-spacing: 0.14em;
      text-transform: uppercase;
      color: #b5763a;
      margin: 28px 0 8px;
    }}
    .card {{
      background: #fff;
      border: 1px solid #e4e0d6;
      border-radius: 14px;
      padding: 20px 24px;
    }}
    ul {{ list-style: none; }}
    li {{
      padding: 9px 0;
      border-bottom: 1px solid #f0ece3;
      display: flex;
      align-items: baseline;
      justify-content: space-between;
      gap: 12px;
    }}
    li:last-child {{ border-bottom: none; }}
    a {{ color: #3d6b41; font-weight: 600; text-decoration: none; font-size: 15px; }}
    a:hover {{ text-decoration: underline; }}
    span {{ color: #72716a; font-size: 12px; white-space: nowrap; }}
  </style>
</head>
<body>
  <div class="topbar">
    <img class="topbar-logo" src="./logo.png" alt="Eco Natural">
    <span class="topbar-brand">Eco Natural</span>
  </div>
  <div class="wrap">
    <h1>Product Catalog</h1>
    <p class="sub">{len(items)} artisan products &mdash; scan a barcode or browse below</p>
    {sections_html}
  </div>
</body>
</html>
"""


def main() -> None:
    index_items: list[tuple[str, str, str]] = []

    with CSV_PATH.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            slug       = row["slug"].strip()
            page_title = row["page_title"].strip()
            product_id = row["product_id"].strip()
            filename   = f"{slug}.html"
            (OUTPUT_DIR / filename).write_text(page_template(row), encoding="utf-8")
            index_items.append((filename, page_title, product_id))

    index_items.sort(key=lambda x: x[0])
    (OUTPUT_DIR / "index.html").write_text(index_template(index_items), encoding="utf-8")

    available = {p.name for p in IMG_DIR.glob("*.JPG")} | {p.name for p in IMG_DIR.glob("*.png")}
    missing   = [pid for _, _, pid in index_items
                 if f"{pid}.JPG" not in available and f"{pid}.png" not in available]

    print(f"Generated {len(index_items)} product pages → {OUTPUT_DIR}")
    if missing:
        print("Missing images:")
        for img in missing:
            print(f"  - {img}")
    else:
        print("All product images found.")


if __name__ == "__main__":
    main()
