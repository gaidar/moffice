#!/usr/bin/env python3
"""Check the built site for faults that only appear after Jekyll runs. Standard library only.

Run after the build: python3 scripts/check-site.py [SITE_FOLDER]
Exit code 0 means zero errors.
"""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
RELATIVE_MD_LINK = re.compile(r'<a [^>]*href="(?![a-z]+:)[^"]*\.md(?:#[^"]*)?"')
ID_ATTR = re.compile(r'\s(?:id|name)="([^"]+)"')
STYLESHEET = re.compile(r'href="([^"]*)/assets/css/site\.css"')


class LinkCollector(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("a", "link") and attrs.get("href"):
            self.links.append(attrs["href"])
        elif tag in ("script", "img") and attrs.get("src"):
            self.links.append(attrs["src"])


def check_internal_links(site, pages):
    """Every internal link and #fragment must land on a built file and an existing id.

    A file whose URL differs from its name, such as agent-roles.md at /agents.html, breaks
    links that only swap .md for .html, and the other checks cannot see that.
    """
    errors = []
    home = site / "index.html"
    found = STYLESHEET.search(home.read_text(encoding="utf-8")) if home.exists() else None
    base = found.group(1) if found else ""
    ids = {}

    def ids_in(path):
        if path not in ids:
            ids[path] = set(ID_ATTR.findall(path.read_text(encoding="utf-8")))
        return ids[path]

    for page in pages:
        collector = LinkCollector()
        collector.feed(page.read_text(encoding="utf-8"))
        for href in collector.links:
            parts = urlsplit(href)
            if parts.scheme or href.startswith("//") or href.startswith("data:"):
                continue
            if parts.path == "":
                target = page
            elif parts.path.startswith("/"):
                if base and not (parts.path == base or parts.path.startswith(base + "/")):
                    errors.append(f"{page.relative_to(site)}: link outside the site base {base!r}: {href}")
                    continue
                target = site / unquote(parts.path[len(base):]).lstrip("/")
            else:
                target = page.parent / unquote(parts.path)
            target = Path(target)
            if target.is_dir():
                target = target / "index.html"
            if not target.resolve().is_file():
                errors.append(f"{page.relative_to(site)}: broken link: {href}")
                continue
            fragment = unquote(parts.fragment)
            if fragment and target.suffix == ".html" and fragment not in ids_in(target.resolve()):
                errors.append(f"{page.relative_to(site)}: no #{fragment} in {target.resolve().relative_to(site.resolve())}: {href}")
    return errors


def main():
    site = Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "_site"
    errors = []

    pages = sorted(site.rglob("*.html"))
    if not pages:
        errors.append(f"{site}: no built pages found")
    for page in pages:
        for match in RELATIVE_MD_LINK.finditer(page.read_text(encoding="utf-8")):
            errors.append(f"{page.relative_to(site)}: link still points at a .md file: {match.group(0)}")

    # Link rewriting once changed this file name inside the prompts people copy.
    guide = site / "guides" / "fill-the-context-pack.html"
    if guide.exists():
        text = guide.read_text(encoding="utf-8")
        found = len(re.findall(r'(?:"|&quot;)# company\.md(?:"|&quot;)', text))
        if found != 3:
            errors.append(f'{guide.relative_to(site)}: expected 3 prompts naming "# company.md", found {found}')

    # The footer links here, and the source file must not be named agents.md.
    if not (site / "agents.html").exists():
        errors.append("agents.html: missing")
    if not (site / "run-my-week.html").exists():
        errors.append("run-my-week.html: missing")

    # The prompt and its button must stay together on every skill and charter.
    for folder in ("skills", "agents"):
        for page in sorted((site / folder).rglob("*.html")) if (site / folder).exists() else []:
            text = page.read_text(encoding="utf-8")
            panel = text[text.find('class="prompt-panel"'):] if 'class="prompt-panel"' in text else ""
            if "office-copy-prompt" not in panel or "prompt-preview" not in panel:
                errors.append(f"{page.relative_to(site)}: no prompt panel with its Copy prompt button and preview")

    # These left the top bar, so the footer must keep them one click away on every page.
    home = site / "index.html"
    if home.exists():
        text = home.read_text(encoding="utf-8")
        footer = text[text.rfind('<footer class="site">'):]
        for target in ("playbooks.html", "setup.html", "context-pack.html", "agents.html"):
            if f'{target}"' not in footer:
                errors.append(f"index.html: footer has no link to {target}")

    errors.extend(check_internal_links(site, pages))

    for line in errors:
        print(f"ERROR {line}")
    print(f"Summary: {len(errors)} errors, {len(pages)} pages checked.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
