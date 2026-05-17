from css.index import CSS_INDEX
from css.product import CSS_PRODUCT
from css.shared import CSS_SHARED
from css.tokens import FONTS_LINK, GRAIN_SVG

CSS_SITE = "\n\n".join(part for part in [CSS_SHARED, CSS_PRODUCT, CSS_INDEX] if part.strip())
