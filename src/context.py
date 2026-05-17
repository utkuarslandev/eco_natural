from __future__ import annotations

from dataclasses import dataclass


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


def localize_path(path: str, ctx: Ctx | None) -> str:
    if ctx and ctx.is_subdir and not path.startswith(("http://", "https://")):
        cleaned = path.lstrip("./") if path.startswith("./") else path
        return "../" + cleaned
    return path


def localize_srcset(srcset: str, ctx: Ctx | None) -> str:
    if not ctx or not ctx.is_subdir:
        return srcset
    localized_parts = []
    for part in srcset.split(", "):
        path_and_width = part.rsplit(" ", 1)
        if len(path_and_width) == 2:
            path, width = path_and_width
            localized_parts.append(f"{localize_path(path, ctx)} {width}")
        else:
            localized_parts.append(part)
    return ", ".join(localized_parts)
