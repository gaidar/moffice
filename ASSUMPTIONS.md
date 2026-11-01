# Assumptions

Every assumption made during the v0.1.0 build, one line each. Nobody was available to answer questions, so each was decided and logged here for the owner to review.

## Owner corrections received during the build

These five corrections override the requirements document where they conflict.

- No zip is provided. Guides send the marketer to GitHub, using GitHub's own Code and Download ZIP buttons to get many files at once. `scripts/build-zip.sh` is gone.
- `bundles/all-skills.md` and `bundles/all-agent-roles.md` are now committed files, because ChatGPT's project limit needs them and the zip no longer carries them. `scripts/build-bundles.sh` generates them, and the workflow fails if they are stale.
- PDFs exist only for playbooks and guides, except the FAQ. "Standard operating procedures for people to read" was read as those 16 documents. Skills, charters, the context pack and office documents have no PDF, and link to their text files on GitHub.
- "Avoid duplication with PDFs" was read as: PDFs drop from 105 to 16, and all are generated from the same markdown as the web page, so nothing is maintained twice. HTML pages for skills and charters stay, because they cost no upkeep and the original spec asks for them. Removing them is a small change if the owner prefers GitHub only.
- The site design follows marketingoffice.net: its palette, Archivo, Source Serif 4 and IBM Plex Mono fonts, a top bar, full-length pages and SVG diagrams. just-the-docs is removed, which also removes its site search. The Skills page has a filter instead.
- Diagrams live in `_includes/diagrams/` and are named in a page's frontmatter, so they do not appear in the raw markdown or the PDFs.
- Fonts load from Google Fonts, as on the reference site, with system fallbacks. This replaces the spec's system or Aptos font stack.
- The sample company is CogniATion, as the owner named it. The rest of the example was built to fit.

## Spec gaps and conflicts

- Definition of done lists four vendor guides (Claude, ChatGPT/Codex, Grok, Google), while the repo layout, the home page spec and the press release list three. Built four, added `guides/setup-google.md`, and linked all four from the home page.
- Google and Gemini are treated as allowed real names, because that guide requires them, and only in files that refer to the guide. The validator enforces this.
- The Definition of done skips item 10, and Phase 7 calls the walkthrough "item 9" while it is item 8. Treated the numbering as a typo and did the walkthrough.
- The press release says a fictional customer quote must not appear, but the text supplied contains no quote. Nothing to remove. Grep for the press release text is in the final report.
- "[CONFIRM: Jekyll + just-the-docs]" and "[CONFIRM: 14]" were not answered. Proceeded with Jekyll, just-the-docs and 14 agent roles, with no merged roles.
- "CNAME (if confirmed)": no domain was confirmed, so there is no `CNAME` file.
- Skills target: "around 50" in one place and "40–50" in another. Built 50, and the validator enforces 40–50.
- `updated: 2026-11-XX` in the frontmatter spec was set to the build date, 2026-11-01.
- "How to run it" is called a two-line prompt, but the sample is one line. Skills use two lines, and the validator accepts either.

## Structure

- Jekyll collections need folders named with a leading underscore, which conflicts with the required `skills/`, `agents/` paths and with the toolbar and PDF paths. Used plain Jekyll pages with path-based defaults. Each markdown file is still both the source and the page.
- Section index pages sit at the repo root (`skills.md`, `agents.md`, `playbooks.md`, `guides.md`, `office.md`, `context-pack.md`, `setup.md`).
- Added frontmatter types beyond the spec's list: `context-example` for the filled pack, `index` for section pages, `contributing` for `CONTRIBUTING.md`.
- `ASSUMPTIONS.md` is at the repo root, as the Operating rules and Deliver sections ask, though the layout does not list it.
- `CONTRIBUTING.md` has frontmatter so that it renders on the site. GitHub shows that frontmatter as a small table at the top of the file.
- Added `_data/functions.yml`, `_data/context_pack.yml` and `_data/nav.yml` to drive the coverage table, context pack links and top bar.
- Added `scripts/requirements-pdf.txt`, beyond the three scripts listed, to pin the PDF tools.
- Context pack references in skills render on the site as links to the blank templates.
- Internal markdown links use relative `.md` paths so they work on GitHub. The layout rewrites them to `.html` on the site.
- `bundles/` combines all skills and all charters into one file each. The spec did not ask for this. ChatGPT's verified project file limits (25 on Plus, 40 on Pro) cannot hold 74 separate files.
- `dev/` holds the owner's development documents, including the requirements. It is gitignored, and the validator and Jekyll skip it.

## Tooling

- PDF engine: Typst, driven through pandoc, both from pinned PyPI packages (`pypandoc_binary`, `typst`). The workflow uses the same packages as local builds.
- Ruby 3.3 was built with `ruby-build` into the gitignored `.tools/` folder for the local build. The workflow uses `ruby/setup-ruby`.
- GitHub Actions are pinned to commit SHAs, and only the deploy job gets Pages write permissions, following an automated security review.
- Homebrew was used only for packages the spec allows: `ruby-build` and `libyaml`. Two stopped `ruby@3.3` and `pandoc`/`typst` installs also pulled in build dependencies under `~/homebrew`, and these are listed in `dev/build-report.md`.

## Fictional company

- Company: CogniATion, named by the owner, 38 employees, Austin, Texas. Product: CogniATion Coach, a specialized AI chatbot that questions employees about work problems and scores their reasoning. It is sold to learning and development teams. Segments: professional services firms, software companies, financial services firms.
- Competitors: Arguvia and Deliberon. Customers: Brightmere Advisory, Corvane Software, Haldane Ridge Capital.
- Web searches on 2026-11-01 found no exact match for CogniATion, Arguvia, Deliberon, Brightmere Advisory, Corvane Software or Haldane Ridge Capital. Similar real names exist (Cognition AI, ArguAI, Cogni), none of them exact. CogniATion is close to Cognition AI, a real company. The owner chose the name, so it was kept. Searches cannot prove a name is unused.
- Austin, Texas is a real place, used only as the fictional company's location.
- People at CogniATion and its customers are invented names.
- The first example company, Ostrel Systems, was replaced in full. The validator rejects its names.

## Content decisions

- The marketing reviewer judges drafts before use and owns only review skills. The marketing analyst owns evaluation of results, including "Evaluate a campaign". The spec's "reviewer owns review and evaluation skills only" was read as limiting the reviewer, not as moving results evaluation away from the analyst, who is explicitly assigned campaign evaluation.
- "Review any output" sits in the marketing ops function because the quality gate is a process that spans all functions.
- Each function has one owning agent role in the coverage table. Review skills inside a function belong to the marketing reviewer.
- The real-name rule was read strictly: no social networks, ad platforms, CRMs or search engines by name, even in tool descriptions. Skills say "professional social network" or "search ads".
- Time estimates in guides and playbooks are the author's estimates from the number of steps, labeled as estimates. They have not been measured with real marketers.
- The under-one-day setup target has not been tested with a real marketer or in live vendor accounts. The walkthrough is a trace of the documents.
- The first skill in Start here is "Write a sales one-pager", because it shows the effect of the context pack quickly.

## Deployment

- The repository is private until the release, by the owner's decision. History starts from this commit. GitHub Pages is not enabled, so the site is offline until then.
- Published URL assumed to be the default for the repository, `https://gaidar.github.io/moffice/`.
