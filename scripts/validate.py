#!/usr/bin/env python3
"""Validate Marketing Office content. Standard library only.

Run from anywhere: python3 scripts/validate.py [--only PATH_PREFIX ...]

--only limits per-file errors to the given paths, for checking one batch of
files while others are still being written. Whole-repo counts are skipped then.
Exit code 0 means zero errors. Warnings do not fail the run.
"""
import argparse
import os
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FUNCTIONS = [
    "positioning-and-messaging",
    "segmentation-icp-and-personas",
    "competitive-intelligence",
    "go-to-market-and-launches",
    "campaign-design",
    "content",
    "seo",
    "paid-demand-gen",
    "events-and-webinars",
    "pr-and-comms",
    "product-marketing-and-sales-enablement",
    "partner-and-channel-marketing",
    "brand-and-design-briefs",
    "analytics-and-campaign-evaluation",
    "marketing-ops",
    "budget-and-planning",
]

AGENTS = [
    "head-of-marketing",
    "product-marketing-manager",
    "insights-analyst",
    "demand-generation-manager",
    "content-lead",
    "seo-specialist",
    "paid-media-manager",
    "events-and-webinar-manager",
    "pr-and-communications-manager",
    "partner-marketing-manager",
    "brand-and-creative-director",
    "marketing-analyst",
    "marketing-operations-manager",
    "marketing-reviewer",
]
REVIEWER = "marketing-reviewer"

CONTEXT_FILES = [
    "company",
    "product",
    "icp-and-segments",
    "personas",
    "messaging",
    "competitors",
    "proof-points",
    "brand-voice",
    "goals-and-kpis",
    "channels-and-tools",
]

SKILL_HEADINGS = [
    "When to use",
    "Inputs",
    "Procedure",
    "Output format",
    "Quality checklist",
    "Example (fictional company)",
    "How to run it",
]
AGENT_HEADINGS = [
    "Mission",
    "Owns",
    "Reads",
    "Decides versus escalates",
    "Standard outputs",
    "Quality checklist",
    "Working with other roles",
    "How to invoke",
]
GUIDE_HEADINGS = ["Who it is for", "What you need", "Steps", "What success looks like", "Troubleshooting"]
PLAYBOOK_FILES = ["weekly", "monthly", "quarterly", "first-week", "launch", "campaign-lifecycle"]
GUIDE_FILES = [
    "start-here",
    "setup-claude",
    "setup-chatgpt-codex",
    "setup-grok",
    "setup-google",
    "fill-the-context-pack",
    "use-a-skill",
    "invoke-an-agent",
    "write-your-own-skill",
    "maintain-and-update",
    "faq",
    "judge-an-output",
    "hard-situations",
]
VENDOR_GUIDES = ["setup-claude", "setup-chatgpt-codex", "setup-grok", "setup-google"]
OFFICE_FILES = ["office-manual", "output-conventions", "glossary", "agent-roster"]
TYPES = ["skill", "agent", "playbook", "guide", "office", "context-template", "context-example", "index"]
CONTENT_DIRS = ["skills", "agents", "playbooks", "guides", "context-pack", "office"]
ROOT_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "CHANGELOG.md",
    "VERSION",
    "DEPLOY.md",
    "TEST-WALKTHROUGH.md",
    "ASSUMPTIONS.md",
    "_config.yml",
    "Gemfile",
    "index.md",
    "assets/js/toolbar.js",
    "scripts/build-pdf.sh",
    "scripts/build-bundles.sh",
    "bundles/all-skills.md",
    "bundles/all-agent-roles.md",
    "bundles/context-pack-templates.md",
    "bundles/try-it.md",
    ".github/workflows/pages.yml",
]

# Folders never scanned. dev/ holds the owner's development documents and is not committed.
SKIP_DIRS = {"dev", "bundles", ".playwright-mcp", ".git", ".venv", "vendor", "_site", "pdf", ".jekyll-cache", ".bundle", "node_modules", ".tools"}
SKIP_FILES = set()

BANNED = [
    r"certainly", r"happy to", r"great question", r"absolutely", r"interesting point",
    r"delv(?:e|es|ed|ing)", r"landscapes?", r"leverag(?:e|es|ed|ing)", r"utili[sz](?:e|es|ed|ing|ation)",
    r"foster(?:s|ed|ing)?", r"facilitat(?:e|es|ed|ing|or|ors)", r"holistic(?:ally)?", r"synerg(?:y|ies|istic)",
    r"paradigms?", r"robust(?:ly|ness)?", r"scalab(?:le|ility)", r"ecosystems?", r"stakeholders?",
    r"alignment", r"deep[- ]dives?", r"unpack(?:s|ed|ing)?", r"at the end of the day",
    r"it['’]s important to note", r"it['’]s worth mentioning", r"needless to say",
]
BANNED_RE = re.compile(r"\b(?:" + "|".join(BANNED) + r")\b", re.I)

# Real companies and products that tend to slip into marketing writing. Vendor
# names allowed by the quality bar, and the author, are not in this list.
REAL_NAMES = [
    "HubSpot", "Salesforce", "Marketo", "Mailchimp", "Pardot", "LinkedIn", "Facebook", "Instagram", "TikTok",
    "YouTube", "Twitter", "Reddit", "Semrush", "Ahrefs", "Moz", "Gartner", "Forrester", "IDC", "G2", "Capterra",
    "Slack", "Notion", "Canva", "Figma", "Webflow", "WordPress", "Zoom", "Airtable", "Asana", "Trello", "Looker",
    "Tableau", "Mixpanel", "Zapier", "Calendly", "Gong", "Intercom", "Zendesk", "Stripe",
    "Microsoft", "Amazon", "Meta Ads", "Bing", "Adobe", "Oracle", "SAP", "ServiceNow", "Atlassian", "Jira",
    "Dropbox", "Shopify", "Wix", "Squarespace", "Hootsuite", "Sprout Social", "PR Newswire", "Cision",
    "Acronis",
]
REAL_NAMES_RE = re.compile(r"\b(?:" + "|".join(re.escape(n) for n in REAL_NAMES) + r")\b")
# "Google" and "Gemini" are real names allowed only where the Google guide needs them.
GOOGLE_RE = re.compile(r"\b(?:Google|Gemini)\b")
GOOGLE_ALLOWED = {
    "guides/setup-google.md", "guides/start-here.md", "guides/faq.md", "guides/index.md", "setup.md", "index.md",
    "guides/maintain-and-update.md", "guides/fill-the-context-pack.md", "README.md", "ASSUMPTIONS.md", "CHANGELOG.md",
    "TEST-WALKTHROUGH.md", "CONTRIBUTING.md", "office/glossary.md",
}
PROJECT_INFRA_ALLOW = {"DEPLOY.md"}

# Names from an earlier example company. They must not come back.
RETIRED_RE = re.compile(r"\b(?:Ostrel|Quernwell|Marlowtask|Tallowbrook|Birchmoor|Halvane|Cresthollow)\b")
DOMAIN_RE = re.compile(r"\b(?:technicians?|work orders?|maintenance managers?|plant managers?|production lines?|food and beverage)\b", re.I)

DRAFT_SENTENCE = "you decide"
FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---\n", re.S)
H2_RE = re.compile(r"^## +(.+?)[ \t]*$", re.M)
CTX_RE = re.compile(r"\[\[context-pack:([^\]]*)\]\]")
LINK_RE = re.compile(r"(?<!\!)\[[^\]\n]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


class Report:
    def __init__(self, only):
        self.errors, self.warnings, self.only = [], [], only

    def _in_scope(self, path):
        return not self.only or path is None or any(str(path).startswith(p) for p in self.only)

    def error(self, path, msg):
        if self._in_scope(path):
            self.errors.append(f"{path or 'repo'}: {msg}")

    def warn(self, path, msg):
        if self._in_scope(path):
            self.warnings.append(f"{path or 'repo'}: {msg}")


def parse_frontmatter(text):
    """Parse the flat YAML subset the repo uses: key: value and key: [a, b]."""
    match = FRONTMATTER_RE.match(text)
    if not match:
        return None, text
    data = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line or line[0] in " \t-":
            data.setdefault("_bad", []).append(line)
            continue
        key, value = line.split(":", 1)
        value = value.strip()
        if ": " in value and value[0] not in "\"'[":
            data.setdefault("_bad", []).append(line + "  (unquoted colon breaks YAML)")
            continue
        if value.startswith("[") and value.endswith("]"):
            data[key.strip()] = [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
        else:
            data[key.strip()] = value.strip("\"'")
    return data, text[match.end():]


def strip_code(text):
    text = re.sub(r"^```.*?^```", "", text, flags=re.S | re.M)
    return re.sub(r"`[^`\n]*`", "", text)


def sections(body):
    """Return ordered (heading, content) pairs for H2 headings outside code fences."""
    masked = re.sub(r"^```.*?^```", lambda m: re.sub(r"[^\n]", " ", m.group(0)), body, flags=re.S | re.M)
    matches = list(H2_RE.finditer(masked))
    out = []
    for i, m in enumerate(matches):
        end = matches[i + 1].start() if i + 1 < len(matches) else len(body)
        out.append((m.group(1), body[m.end():end]))
    return out


def word_count(text):
    return len(re.findall(r"\S+", text))


def check_order(rep, rel, body, required):
    found = [h for h, _ in sections(body)]
    if found != required:
        rep.error(rel, f"H2 headings must be exactly {required}, found {found}")


def check_common_frontmatter(rep, rel, fm, version):
    if "_bad" in fm:
        rep.error(rel, f"frontmatter lines not understood: {fm['_bad']}")
    for key in ["title", "type", "version", "updated", "summary"]:
        if not fm.get(key):
            rep.error(rel, f"frontmatter missing {key}")
    if fm.get("type") and fm["type"] not in TYPES:
        rep.error(rel, f"frontmatter type {fm['type']!r} not allowed")
    if fm.get("version") and version and fm["version"] != version:
        rep.error(rel, f"version {fm['version']} does not match VERSION {version}")
    if fm.get("updated") and not DATE_RE.match(fm["updated"]):
        rep.error(rel, f"updated must be YYYY-MM-DD, found {fm['updated']}")
    title = fm.get("title", "")
    words = title.split()
    capitalized = [w for w in words[1:] if re.match(r"^[A-Z][a-z]+$", w) and w not in ("Google", "Gemini", "Marketing", "Office", "Ostrel", "Systems", "Claude", "Grok", "Codex")]
    if len(capitalized) >= 2:
        rep.warn(rel, f"title may not be sentence case: {title}")


def check_reads(rep, rel, fm, body, section_text):
    reads = fm.get("reads")
    if not isinstance(reads, list) or not reads:
        rep.error(rel, "frontmatter reads must be a non-empty list")
        return
    for name in reads:
        if name not in CONTEXT_FILES:
            rep.error(rel, f"reads names unknown context pack file {name!r}")
    refs = set(CTX_RE.findall(section_text))
    for name in reads:
        if name not in refs:
            rep.error(rel, f"reads lists {name} but the section does not reference [[context-pack:{name}]]")
    for name in refs - set(reads):
        rep.error(rel, f"[[context-pack:{name}]] referenced in the section but missing from reads")


def check_skill(rep, rel, fm, body):
    parts = Path(rel).parts
    for key in ["function", "owner", "you_bring", "also_for"]:
        if not fm.get(key):
            rep.error(rel, f"frontmatter missing {key}")
    if fm.get("function") not in FUNCTIONS:
        rep.error(rel, f"function {fm.get('function')!r} is not one of the 16")
    elif len(parts) != 3 or parts[1] != fm["function"]:
        rep.error(rel, "file must sit in skills/<function>/ matching its function field")
    if fm.get("owner") not in AGENTS:
        rep.error(rel, f"owner {fm.get('owner')!r} is not one of the 14 agent roles")
    check_order(rep, rel, body, SKILL_HEADINGS)
    secs = dict(sections(body))
    if DRAFT_SENTENCE not in body:
        rep.error(rel, f"must state the draft rule containing: {DRAFT_SENTENCE}")
    check_reads(rep, rel, fm, body, secs.get("Inputs", ""))
    words = word_count(body)
    if not 500 <= words <= 1200:
        rep.error(rel, f"skill body is {words} words, must be 500-1200")
    when = strip_code(secs.get("When to use", "")).strip()
    if when and len(re.findall(r"[.!?](?:\s|$)", when)) > 4:
        rep.warn(rel, "When to use should be two or three sentences")
    if when and not re.search(r"\b(not|instead)\b", when, re.I):
        rep.error(rel, "When to use must say when not to use it and which skill to use instead")
    proc = secs.get("Procedure", "")
    steps = re.findall(r"^\d+\. ", proc, re.M)
    if len(steps) < 3:
        rep.error(rel, "Procedure must be numbered steps")
    if not re.search(r"^\d+\. .*context pack", proc, re.M | re.I):
        rep.error(rel, "Procedure needs a numbered step that checks the draft against the context pack")
    if not re.search(r"^\d+\. .*assum", proc, re.M | re.I):
        rep.error(rel, "Procedure needs a numbered step that lists what was assumed")
    out = secs.get("Output format", "")
    if "Assumptions and open questions" not in out:
        rep.error(rel, "Output format must end with Assumptions and open questions")
    else:
        tail = out[out.rindex("Assumptions and open questions"):]
        if re.search(r"^(#+ |\*\*[A-Z])", tail.split("\n", 1)[1] if "\n" in tail else "", re.M):
            rep.error(rel, "Assumptions and open questions must be the last section of the output")
    check_items = re.findall(r"^(?:- \[ \]|-|\d+\.) ", secs.get("Quality checklist", ""), re.M)
    if not 5 <= len(check_items) <= 10:
        rep.error(rel, f"Quality checklist has {len(check_items)} items, must be 5-10")
    example_words = word_count(secs.get("Example (fictional company)", ""))
    if not 150 <= example_words <= 300:
        rep.error(rel, f"Example is {example_words} words, must be 150-300")
    run = secs.get("How to run it", "")
    expected = f'Use the skill "{fm.get("title")}". Read the context pack. Task:'
    if expected not in re.sub(r"\s+", " ", run):
        rep.error(rel, f"How to run it must contain: {expected}")


def check_agent(rep, rel, fm, body):
    check_order(rep, rel, body, AGENT_HEADINGS)
    if not fm.get("bring_it"):
        rep.error(rel, "frontmatter missing bring_it")
    secs = dict(sections(body))
    if DRAFT_SENTENCE not in body:
        rep.error(rel, f"must state the draft rule containing: {DRAFT_SENTENCE}")
    check_reads(rep, rel, fm, body, secs.get("Reads", ""))
    title = fm.get("title", "")
    # Lowercase the first letter for running text, but keep SEO and PR as written.
    role = title if title.split(" ")[0].isupper() else title[:1].lower() + title[1:]
    expected = f"Act as the {role} from the Marketing Office. Follow your charter. Read the context pack. Today's task:"
    if expected not in secs.get("How to invoke", ""):
        rep.error(rel, f"How to invoke must contain: {expected}")
    if not 3 <= len(re.findall(r"^(?:- \[ \]|-|\d+\.) ", secs.get("Quality checklist", ""), re.M)):
        rep.error(rel, "Quality checklist needs at least 3 items")


def check_guide(rep, rel, fm, body):
    stem = Path(rel).stem
    if stem in ("index", "faq"):
        return
    found = [h for h, _ in sections(body)]
    positions = []
    for heading in GUIDE_HEADINGS:
        if heading not in found:
            rep.error(rel, f"guide missing section {heading!r}")
        else:
            positions.append(found.index(heading))
    if positions != sorted(positions):
        rep.error(rel, f"guide sections out of order, expected {GUIDE_HEADINGS}")
    if not re.search(r"^1\. ", dict(sections(body)).get("Steps", ""), re.M):
        rep.error(rel, "Steps section must contain numbered steps")
    if stem in VENDOR_GUIDES:
        if not re.search(r"Verified on \d{4}-\d{2}-\d{2} against vendor documentation", body):
            rep.error(rel, 'vendor guide needs "Verified on YYYY-MM-DD against vendor documentation"')
        if not re.search(r"https://", body):
            rep.error(rel, "vendor guide must list the URLs checked")
        if "Plain-chat fallback" not in found:
            rep.error(rel, "vendor guide needs a section named Plain-chat fallback")


def check_context_file(rep, rel, body):
    if not re.search(r"^\*\*Purpose:\*\*", body, re.M):
        rep.error(rel, "context pack file needs a line starting **Purpose:**")
    if "Do not fill with guesses – leave blank and the skills will ask" not in body:
        rep.error(rel, "context pack file needs the do-not-guess note")


def check_links(rep, rel, path, body, liquid_ok):
    masked = strip_code(body)
    for target in LINK_RE.findall(masked):
        if re.match(r"^(https?:|mailto:|#)", target) or "{{" in target:
            continue
        clean = target.split("#", 1)[0]
        if not clean:
            continue
        dest = (ROOT / clean.lstrip("/")) if clean.startswith("/") else (path.parent / clean)
        if not dest.exists():
            rep.error(rel, f"broken link: {target}")
    for name in CTX_RE.findall(body):
        if name not in CONTEXT_FILES:
            rep.error(rel, f"unknown context pack reference: [[context-pack:{name}]]")
        elif not (ROOT / "context-pack" / "templates" / f"{name}.md").exists():
            rep.error(rel, f"[[context-pack:{name}]] has no template file yet")
    if not liquid_ok and re.search(r"\{\{|\{%", body):
        rep.error(rel, "Liquid syntax found; it would be executed by Jekyll")


def iter_markdown():
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                path = Path(dirpath) / name
                rel = path.relative_to(ROOT).as_posix()
                if rel not in SKIP_FILES:
                    yield path, rel


def scan_text(rep, rel, text):
    for number, line in enumerate(text.splitlines(), 1):
        if "—" in line:
            rep.error(rel, f"line {number}: em dash")
        for match in BANNED_RE.finditer(line):
            rep.error(rel, f"line {number}: banned word {match.group(0)!r}")
        if rel not in PROJECT_INFRA_ALLOW:
            for match in REAL_NAMES_RE.finditer(line):
                rep.error(rel, f"line {number}: real company or product name {match.group(0)!r}")
        if rel != "ASSUMPTIONS.md":
            for match in RETIRED_RE.finditer(line):
                rep.error(rel, f"line {number}: retired example name {match.group(0)!r}")
            for match in DOMAIN_RE.finditer(line):
                rep.error(rel, f"line {number}: left over from the earlier example company: {match.group(0)!r}")
        if rel not in GOOGLE_ALLOWED:
            for match in GOOGLE_RE.finditer(line):
                rep.error(rel, f"line {number}: {match.group(0)!r} allowed only in the Google guide and its links")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--only", nargs="*", default=[], help="limit per-file errors to these path prefixes")
    args = parser.parse_args()
    rep = Report(args.only)

    version_file = ROOT / "VERSION"
    version = version_file.read_text().strip() if version_file.exists() else None

    if not args.only:
        for rel in ROOT_FILES:
            if not (ROOT / rel).exists():
                rep.error(rel, "required file missing")
        for agent in AGENTS:
            if not (ROOT / "agents" / f"{agent}.md").exists():
                rep.error(f"agents/{agent}.md", "required agent charter missing")
        for name in CONTEXT_FILES:
            if not (ROOT / "context-pack" / "templates" / f"{name}.md").exists():
                rep.error(f"context-pack/templates/{name}.md", "required template missing")
        examples = [p for p in (ROOT / "context-pack").glob("example-*") if p.is_dir()]
        if len(examples) != 1:
            rep.error("context-pack/example-<company>", f"expected one example folder, found {len(examples)}")
        for example in examples:
            for name in CONTEXT_FILES:
                if not (example / f"{name}.md").exists():
                    rep.error(f"{example.relative_to(ROOT)}/{name}.md", "required example file missing")
        for stem in PLAYBOOK_FILES:
            if not (ROOT / "playbooks" / f"{stem}.md").exists():
                rep.error(f"playbooks/{stem}.md", "required playbook missing")
        for stem in GUIDE_FILES:
            if not (ROOT / "guides" / f"{stem}.md").exists():
                rep.error(f"guides/{stem}.md", "required guide missing")
        for stem in OFFICE_FILES:
            if not (ROOT / "office" / f"{stem}.md").exists():
                rep.error(f"office/{stem}.md", "required office document missing")

    skills, agents_seen = [], {}
    for path, rel in sorted(iter_markdown()):
        text = path.read_text(encoding="utf-8")
        scan_text(rep, rel, text)
        fm, body = parse_frontmatter(text)
        top = rel.split("/", 1)[0]
        in_content = top in CONTENT_DIRS
        liquid_ok = bool(fm and fm.get("type") == "index")
        check_links(rep, rel, path, body, liquid_ok)
        if not in_content:
            continue
        if fm is None:
            rep.error(rel, "missing frontmatter")
            continue
        check_common_frontmatter(rep, rel, fm, version)
        if fm.get("diagram") and not (ROOT / "_includes" / "diagrams" / f"{fm['diagram']}.svg").exists():
            rep.error(rel, f"diagram {fm['diagram']} not found in _includes/diagrams/")
        kind = fm.get("type")
        if re.search(r"^# ", strip_code(body), re.M):
            rep.error(rel, "no H1 in the body; the layout prints the title")
        expected_kind = {"skills": "skill", "agents": "agent", "playbooks": "playbook", "guides": "guide", "office": "office"}.get(top)
        if kind == "index":
            continue
        if expected_kind and kind != expected_kind:
            rep.error(rel, f"type should be {expected_kind}, found {kind}")
        if kind == "skill":
            check_skill(rep, rel, fm, body)
            skills.append((rel, fm))
        elif kind == "agent":
            check_agent(rep, rel, fm, body)
            agents_seen[path.stem] = (rel, body)
            if path.stem not in AGENTS:
                rep.error(rel, "file name is not one of the 14 agent roles")
        elif kind == "guide":
            check_guide(rep, rel, fm, body)
        elif kind in ("context-template", "context-example"):
            if Path(rel).stem not in CONTEXT_FILES:
                rep.error(rel, "context pack file name is not one of the 10")
            check_context_file(rep, rel, body)
            wanted = "context-template" if "/templates/" in rel else "context-example"
            if kind != wanted:
                rep.error(rel, f"type should be {wanted}")

    by_function, by_owner = defaultdict(list), defaultdict(list)
    for rel, fm in skills:
        by_function[fm.get("function")].append(rel)
        by_owner[fm.get("owner")].append(rel)
    titles = Counter(fm.get("title") for _, fm in skills)
    for title, count in titles.items():
        if count > 1:
            rep.error(None, f"skill title used {count} times: {title}")

    for agent, (rel, body) in agents_seen.items():
        owns = dict(sections(body)).get("Owns", "")
        listed = set(re.findall(r"skills/[a-z0-9-]+/[a-z0-9-]+\.md", owns))
        expected = set(by_owner.get(agent, []))
        for missing in sorted(expected - listed):
            rep.error(rel, f"Owns section does not list {missing}")
        for extra in sorted(listed - expected):
            rep.error(rel, f"Owns section lists {extra}, whose owner field is different or missing")

    if not args.only:
        for function in FUNCTIONS:
            if len(by_function[function]) < 2:
                rep.error(f"skills/{function}", f"has {len(by_function[function])} skills, needs at least 2")
        for agent in AGENTS:
            if len(by_owner[agent]) < 2:
                rep.error(f"agents/{agent}.md", f"owns {len(by_owner[agent])} skills, needs at least 2")
        if not 40 <= len(skills) <= 60:
            rep.error(None, f"skills library has {len(skills)} skills, target is 40-60")
    for rel, fm in skills:
        if fm.get("owner") == REVIEWER and not re.search(r"(^|/)(review|evaluate)-", rel):
            rep.error(rel, "marketing reviewer owns review and evaluation skills only")

    for line in rep.warnings:
        print(f"WARN  {line}")
    for line in rep.errors:
        print(f"ERROR {line}")
    print(
        f"Summary: {len(rep.errors)} errors, {len(rep.warnings)} warnings. "
        f"Skills {len(skills)}, agents {len(agents_seen)}, functions covered "
        f"{sum(1 for f in FUNCTIONS if by_function[f])}/16."
    )
    return 1 if rep.errors else 0


if __name__ == "__main__":
    sys.exit(main())
