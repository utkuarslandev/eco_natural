import csv
from html import escape
from pathlib import Path


ROOT = Path(__file__).parent
CSV_PATH = ROOT / "ids.csv"
IMG_DIR = ROOT / "img"
OUTPUT_DIR = ROOT / "product_pages"


def page_template(row: dict) -> str:
    product_id = row["product_id"].strip()
    page_title = row["page_title"].strip()
    short_description = row["short_description"].strip()
    full_description = row["full_description"].strip()
    seo_title = row["seo_title"].strip()
    meta_description = row["meta_description"].strip()
    image_name = f"{product_id}.JPG"
    image_path = f"../img/{escape(image_name)}"

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{escape(seo_title or page_title)}</title>
  <meta name="description" content="{escape(meta_description)}">
  <style>
    :root {{
      color-scheme: light dark;
      --bg: #ffffff;
      --fg: #1d1d1f;
      --muted: #5d6470;
      --card: #f5f7fb;
      --maxw: 960px;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg: #0f1115;
        --fg: #f3f4f6;
        --muted: #adb3bd;
        --card: #171a21;
      }}
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      background: var(--bg);
      color: var(--fg);
      line-height: 1.55;
    }}
    .wrap {{
      max-width: var(--maxw);
      margin: 0 auto;
      padding: 28px 16px 40px;
    }}
    .crumbs {{
      margin-bottom: 14px;
      font-size: 14px;
      color: var(--muted);
    }}
    .card {{
      background: var(--card);
      border-radius: 14px;
      padding: 18px;
    }}
    .hero {{
      display: grid;
      gap: 22px;
      grid-template-columns: 1fr;
    }}
    @media (min-width: 840px) {{
      .hero {{
        grid-template-columns: 1fr 1fr;
      }}
    }}
    img {{
      width: 100%;
      height: auto;
      border-radius: 10px;
      background: #fff;
    }}
    h1 {{
      margin: 0 0 10px;
      line-height: 1.25;
    }}
    .short {{
      font-weight: 600;
      margin-bottom: 14px;
    }}
    .meta {{
      margin-top: 18px;
      color: var(--muted);
      font-size: 14px;
    }}
    .meta code {{
      font-size: 13px;
    }}
    a {{
      color: inherit;
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="crumbs"><a href="./index.html">All products</a></div>
    <article class="card hero">
      <div>
        <img src="{image_path}" alt="{escape(page_title)}">
      </div>
      <div>
        <h1>{escape(page_title)}</h1>
        <p class="short">{escape(short_description)}</p>
        <p>{escape(full_description)}</p>
        <div class="meta">
          <div><strong>Product ID:</strong> <code>{escape(product_id)}</code></div>
        </div>
      </div>
    </article>
  </div>
</body>
</html>
"""


def index_template(items: list[tuple[str, str, str]]) -> str:
    links = "\n".join(
        f'      <li><a href="{escape(filename)}">{escape(page_title)}</a> <span>- {escape(product_id)}</span></li>'
        for filename, page_title, product_id in items
    )
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Eco Natural Product Pages</title>
  <style>
    body {{
      margin: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
      background: #f6f8fc;
      color: #1d1d1f;
      line-height: 1.5;
    }}
    .wrap {{
      max-width: 900px;
      margin: 0 auto;
      padding: 28px 16px 40px;
    }}
    .card {{
      background: #fff;
      border-radius: 14px;
      padding: 18px 20px;
    }}
    h1 {{
      margin: 0 0 10px;
    }}
    ul {{
      margin: 0;
      padding-left: 20px;
    }}
    li {{
      margin: 8px 0;
    }}
    span {{
      color: #5d6470;
      font-size: 14px;
    }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="card">
      <h1>Eco Natural Product Pages</h1>
      <p>{len(items)} product pages generated from <code>ids.csv</code>.</p>
      <ul>
{links}
      </ul>
    </div>
  </div>
</body>
</html>
"""


def main() -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)

    index_items: list[tuple[str, str, str]] = []

    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            slug = row["slug"].strip()
            page_title = row["page_title"].strip()
            product_id = row["product_id"].strip()
            html_filename = f"{slug}.html"
            html_path = OUTPUT_DIR / html_filename

            html_path.write_text(page_template(row), encoding="utf-8")
            index_items.append((html_filename, page_title, product_id))

    index_items.sort(key=lambda x: x[0])
    (OUTPUT_DIR / "index.html").write_text(index_template(index_items), encoding="utf-8")

    available_images = {p.name for p in IMG_DIR.glob("*.JPG")}
    missing_images = [f"{item[2]}.JPG" for item in index_items if f"{item[2]}.JPG" not in available_images]

    print(f"Generated {len(index_items)} product pages in: {OUTPUT_DIR}")
    print(f"Index page: {OUTPUT_DIR / 'index.html'}")
    if missing_images:
        print("Missing referenced images:")
        for img in missing_images:
            print(f" - {img}")
    else:
        print("All referenced images found in img/.")


if __name__ == "__main__":
    main()
