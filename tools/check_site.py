#!/usr/bin/env python3
"""Check the built EGP site's local links, assets and branding."""

from __future__ import annotations

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class Links(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.targets: list[str] = []
        self.title = ""
        self.in_title = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.in_title = tag == "title" or self.in_title
        for key, value in attrs:
            if key in {"href", "src"} and value:
                self.targets.append(value)

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title += data


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, default=Path("_site"))
    parser.add_argument("--baseurl", default="/EGP-website")
    args = parser.parse_args()
    site = args.site.resolve()
    failures: list[str] = []
    for name in ("index.html", "features/index.html", "download/index.html", "community/index.html", "license/index.html", "404.html"):
        path = site / name
        if not path.is_file():
            failures.append(f"Missing page: {name}")
            continue
        html = path.read_text(encoding="utf-8")
        links = Links()
        links.feed(html)
        if not links.title.endswith("— EGP"):
            failures.append(f"Incorrect title: {name}")
        if "plausible.godot.foundation" in html or "fund.godotengine.org" in html:
            failures.append(f"Upstream service embedded: {name}")
        for target in links.targets:
            parts = urlsplit(target)
            if parts.scheme or parts.netloc or not parts.path:
                continue
            route = unquote(parts.path)
            if route.startswith("/"):
                if args.baseurl and not route.startswith(args.baseurl + "/"):
                    failures.append(f"Missing deployment prefix: {name}: {target}")
                    continue
                route = route.removeprefix(args.baseurl).lstrip("/")
                destination = site / route
            else:
                destination = path.parent / route
            if destination.is_dir():
                destination = destination / "index.html"
            if not destination.is_file():
                failures.append(f"Broken local link: {name}: {target}")
    if (site / "article").exists() or (site / "download/3.x").exists():
        failures.append("Upstream editorial/download pages entered the EGP build")
    if failures:
        print("\n".join(failures))
        return 1
    print("EGP site: six pages, deployment prefixes, local assets and branding verified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
