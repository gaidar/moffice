#!/usr/bin/env python3
"""Check the built site for faults that only appear after Jekyll runs. Standard library only.

Run after the build: python3 scripts/check-site.py [SITE_FOLDER]
Exit code 0 means zero errors.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RELATIVE_MD_LINK = re.compile(r'<a [^>]*href="(?![a-z]+:)[^"]*\.md(?:#[^"]*)?"')


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

    # These left the top bar, so the footer must keep them one click away on every page.
    home = site / "index.html"
    if home.exists():
        text = home.read_text(encoding="utf-8")
        footer = text[text.rfind('<footer class="site">'):]
        for target in ("playbooks.html", "setup.html", "context-pack.html", "agents.html"):
            if f'{target}"' not in footer:
                errors.append(f"index.html: footer has no link to {target}")

    for line in errors:
        print(f"ERROR {line}")
    print(f"Summary: {len(errors)} errors, {len(pages)} pages checked.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
