#!/usr/bin/env python3
"""Dependency-free sanity checks for the static portfolio."""
from __future__ import annotations

import json
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
HTML_FILE = PUBLIC / "index.html"


class PortfolioParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: list[str] = []
        self.hrefs: list[str] = []
        self.assets: list[str] = []
        self.project_categories: list[set[str]] = []
        self.filter_categories: set[str] = set()
        self._project_stack: list[set[str]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if values.get("id"):
            self.ids.append(values["id"] or "")
        href = values.get("href")
        if href:
            self.hrefs.append(href)
        src = values.get("src")
        if src:
            self.assets.append(src)
        if tag == "meta" and values.get("property") == "og:image" and values.get("content"):
            self.assets.append(values["content"] or "")
        if "data-filter" in values:
            category = values.get("data-filter") or ""
            if category != "all":
                self.filter_categories.add(category)
        classes = set((values.get("class") or "").split())
        if tag == "article" and "project-card" in classes:
            categories = set((values.get("data-category") or "").split())
            self.project_categories.append(categories)


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    global failures
    failures += 1


failures = 0
if not HTML_FILE.is_file():
    print("FAIL: public/index.html is missing")
    sys.exit(1)

source = HTML_FILE.read_text(encoding="utf-8")
parser = PortfolioParser()
parser.feed(source)
parser.close()

for identifier, count in Counter(parser.ids).items():
    if count > 1:
        fail(f"duplicate id: {identifier}")

id_set = set(parser.ids)
for href in parser.hrefs:
    if href.startswith("#") and href[1:] and href[1:] not in id_set:
        fail(f"broken in-page anchor: {href}")

for asset in parser.assets:
    if asset.startswith(("https://", "http://", "data:")):
        continue
    if not (PUBLIC / asset).is_file():
        fail(f"missing local asset: {asset}")

for expected in ("assets/styles.css", "assets/script.js", "assets/favicon.svg", "https://furkhad-portfolio.pages.dev/assets/og-image.png"):
    if expected not in parser.assets and expected not in parser.hrefs:
        fail(f"expected asset is not referenced in HTML: {expected}")

for expected in ("work", "approach", "about", "contact"):
    if expected not in id_set:
        fail(f"expected section is missing: #{expected}")

if len(parser.project_categories) < 3:
    fail("portfolio should contain at least three project cards")
all_categories = set().union(*parser.project_categories) if parser.project_categories else set()
missing_filters = parser.filter_categories - all_categories
if missing_filters:
    fail(f"filter categories without projects: {sorted(missing_filters)}")

try:
    ld_text = source.split('<script type="application/ld+json">', 1)[1].split("</script>", 1)[0]
    ld = json.loads(ld_text)
    if ld.get("@type") != "Person":
        fail("JSON-LD should describe a Person")
except (IndexError, json.JSONDecodeError) as error:
    fail(f"JSON-LD is missing or invalid: {error}")

for required in ("public/assets/styles.css", "public/assets/script.js"):
    if not (ROOT / required).is_file():
        fail(f"required site file is missing: {required}")

if failures:
    print(f"\n{failures} check(s) failed.")
    sys.exit(1)

print("PASS: unique IDs, internal anchors, local assets, expected sections, project filters, and JSON-LD.")
print(f"PASS: found {len(parser.project_categories)} project cards and {len(parser.filter_categories)} non-default filters.")
print("Note: this is a dependency-free static sanity check; it does not replace browser, accessibility, or deployed-site testing.")
