# Assumptions

Every assumption made during the v0.1.0 build, one line each. Nobody was available to answer questions, so each was decided and logged here for the owner to review.

## Owner corrections received during the build

These corrections override the requirements document where they conflict.

- No zip is provided. Setup guides link the files directly, and each link saves the file from GitHub. GitHub's own Code and Download ZIP buttons appear only in the optional route for individual files. `scripts/build-zip.sh` is gone.
- `bundles/all-skills.md` and `bundles/roles-and-playbooks.md` are now committed files, because ChatGPT's project limit needs them and the zip no longer carries them. `scripts/build-bundles.sh` generates them, and the workflow fails if they are stale.
- PDFs exist only for playbooks and guides, except the FAQ. "Standard operating procedures for people to read" was read as those documents, now 19. Skills, charters, the context pack and office documents have no PDF, and link to their text files on GitHub.
- "Avoid duplication with PDFs" was read as: PDFs drop from 105 to 19, and all are generated from the same markdown as the web page, so nothing is maintained twice. HTML pages for skills and charters stay, because they cost no upkeep and the original spec asks for them. Removing them is a small change if the owner prefers GitHub only.
- The site design follows marketingoffice.net: its palette, Archivo, Source Serif 4 and IBM Plex Mono fonts, a top bar, full-length pages and SVG diagrams. just-the-docs is removed, which also removes its site search. The Skills page has a filter instead.
- Diagrams live in `_includes/diagrams/` and are named in a page's frontmatter, so they do not appear in the raw markdown or the PDFs.
- Fonts load from Google Fonts, as on the reference site, with system fallbacks. This replaces the spec's system or Aptos font stack.
- The sample company is CogniATion, as the owner named it. The rest of the example was built to fit.

## Reviews during the build

A CMO review, a new marketer review and two rounds of a from-zero CMO review were run and acted on. The reviews themselves are in `dev/reviews/`, which is not committed.

- Skills went from 50 to 56, above the 40–50 in the original layout, because the reviews found jobs nothing covered: pipeline diagnosis, interview guides, customer proof requests, sales decks, lead follow-up and goal setting. The validator now allows 40–60. The owner accepted 56 on 2026-11-02, then approved a 57th, Update the context pack, the same day.
- The default setup is 3 files rather than 74. One combined context pack replaces 10 separate files, and the office manual accepts this. The 10 templates remain as the source.
- The function table stays on the home page, because the website spec names it, though the CMO wanted it cut.
- On 2026-11-02 the owner cut the top bar to five items with no dropdowns, then approved Start here, Try it, Find a task, Run my week and FAQ the same day. Playbooks, Setup, Context pack and Agents are in the footer. Find a task is the existing Skills page at the same address, and Run my week links to the playbooks. The Definition of done only requires two clicks or fewer.
- "Unverified" labels stay in the vendor guides, though the CMO wanted them moved. Nothing was tested on paid accounts, and the spec requires them.
- PDFs now cover 19 documents, because the two new guides and the new playbook are procedures people read.
- Worked examples were produced by following the skills by hand with the sample context pack, and are labeled where figures are illustrative. They were not run in a live vendor account.
- A new skill's goal options use a 15% growth starting rule when there is no history. It is labeled a starting rule, not a benchmark. The owner accepted it on 2026-11-02.
- The worked examples use two illustrative webinars: February 24, 2027 in Plan a webinar and March 4, 2027 in Use a skill. The owner chose to keep both on 2026-11-02.
- "How to judge this" questions are the reviewers' and writers' judgment, not sourced from research.
- `playbooks/from-zero.md` was added as a seventh playbook, not as new skills, so the skill count stays at 56. Its order, time splits, the skip list and its thresholds are the reviewer's judgment, labeled as starting rules, and have not been run at a real company.
- Plain requests were added to the office manual. The exact prompt form stays in every skill and charter, as the spec requires.
- The agent role charters and the playbooks now share one bundle, `bundles/roles-and-playbooks.md`, because the manual sends the model to the playbooks and no uploaded file held them.
- Owner role columns were removed from playbook tables, because the person running them is one person. Each skill page still names its owner.
- Skill pages fold Inputs, Procedure and Output format in the browser, using script. The markdown, the section order and Copy full text do not change, and with no script nothing is folded.
- Examples left the top bar and stays in the footer, linked from Home and Try it.
- On 2026-11-02 the owner approved a readability pass. Top bar and button labels moved from uppercase monospace to Archivo in sentence case, which departs from marketingoffice.net on purpose, because those labels measured about 11px. The palette and all three fonts stay, and monospace stays for prompts, code and the label above page titles. Aptos, a right-hand contents rail, breadcrumbs and a hidden file-actions menu were declined. Contents sit collapsed at the top of the page, so the site still has no side menu. On phones, text-heavy tables stack as labeled fields and diagrams fold behind Show diagram.
- One review recommended collapsing the 14 roles into 3 modes, 4 macro-skills, a QA checkmark block in every skill, and an MCP track. The owner approved not doing these on 2026-11-02: the spec requires 14 roles and rules out MCP servers, and a model ticking its own work looks like proof it is not. One-chat runs give the benefit the first two were after.
- Two more reviews were worked through on 2026-11-02, and the owner approved these decisions the same day. The short working view applies only to jobs that run several skills, so single-skill templates and the validator are unchanged. Capacity stays in days, with one day as 8 hours. The interruption block stays at 2 hours as a starting rule, and the marketer's own four-week average replaces it. Downloads stay on GitHub, pinned to the release tag, with no copies on the site. The home headline became "Run B2B marketing alone with the AI you already pay for".
- Deferred until the pilot: smaller workflow bundles, an action panel on all 57 skill pages, one recovery page, a downloadable worked campaign and editable slide and page templates. The reviews' targets, such as a 70% draft-to-live ratio, were not adopted, because they have no baseline.
- To keep skills under the spec's 1,200 words and the manual under 1,500, some text was cut: the four-label block in skill templates became one line, as the labels are defined in the manual, and the manual's cadence list and its opening line about where to load it went, as the playbooks and setup guides hold them. Diagnose a pipeline gap no longer reads channels-and-tools.md, and no longer points to Set tracking conventions or Build a market segmentation. Evaluate a campaign lost two checklist items that its procedure already covers. The stage timing in the sample pack and the decision check lines in examples are illustrative.
- One-chat runs, the workboard and the 15-minute quick start have been traced with a fresh reader on the setup files. They have not been run in live vendor accounts or with real marketers. A pilot with about five solo marketers is planned after release.

## Spec gaps and conflicts

- Definition of done lists four vendor guides (Claude, ChatGPT/Codex, Grok, Google), while the repo layout, the home page spec and the press release list three. Built four, added `guides/setup-google.md`, and linked all four from the home page.
- Google and Gemini are treated as allowed real names, because that guide requires them, and only in files that refer to the guide. The validator enforces this.
- The Definition of done skips item 10, and Phase 7 calls the walkthrough "item 9" while it is item 8. Treated the numbering as a typo and did the walkthrough.
- The press release says a fictional customer quote must not appear, but the text supplied contains no quote. Nothing to remove. Grep for the press release text is in the final report.
- "[CONFIRM: Jekyll + just-the-docs]" and "[CONFIRM: 14]" were not answered. Proceeded with Jekyll, just-the-docs and 14 agent roles, with no merged roles.
- "CNAME (if confirmed)": no domain was confirmed, so there is no `CNAME` file.
- Skills target: "around 50" in one place and "40–50" in another. Built 50 first. The reviews took it to 56, and the validator now allows 40–60.
- `updated: 2026-11-XX` in the frontmatter spec was set to the build date, 2026-11-01.
- "How to run it" is called a two-line prompt, but the sample is one line. Skills use two lines, and the validator accepts either.

## Structure

- Jekyll collections need folders named with a leading underscore, which conflicts with the required `skills/`, `agents/` paths and with the toolbar and PDF paths. Used plain Jekyll pages with path-based defaults. Each markdown file is still both the source and the page.
- Section index pages sit at the repo root (`skills.md`, `agent-roles.md`, `playbooks.md`, `guides.md`, `office.md`, `context-pack.md`, `setup.md`). The agents index is not named `agents.md`, because on a case-insensitive disk coding tools load that file as `AGENTS.md`. Its URL stays `/agents.html`.
- Added frontmatter types beyond the spec's list: `context-example` for the filled pack, `index` for section pages, `contributing` for `CONTRIBUTING.md`.
- `ASSUMPTIONS.md` is at the repo root, as the Operating rules and Deliver sections ask, though the layout does not list it.
- `CONTRIBUTING.md` has frontmatter so that it renders on the site. GitHub shows that frontmatter as a small table at the top of the file.
- Added `_data/functions.yml`, `_data/context_pack.yml` and `_data/nav.yml` to drive the coverage table, context pack links and top bar.
- Added `scripts/requirements-pdf.txt`, beyond the three scripts listed, to pin the PDF tools.
- Context pack references in skills render on the site as links to the blank templates.
- Internal markdown links use relative `.md` paths so they work on GitHub. The layout rewrites them to `.html` on the site.
- `bundles/` combines all skills, all charters and all templates into one file each, and holds the trial file. The spec did not ask for this. ChatGPT's verified project file limits (25 on Plus, 40 on Pro) cannot hold the separate files.
- `dev/` holds the owner's development documents, including the requirements. It is gitignored, and the validator and Jekyll skip it.

## Tooling

- PDF engine: Typst, driven through pandoc, both from pinned PyPI packages (`pypandoc_binary`, `typst`). The workflow uses the same packages as local builds.
- Ruby 3.3 was built with `ruby-build` into the gitignored `.tools/` folder for the local build. The workflow uses `ruby/setup-ruby`.
- GitHub Actions are pinned to commit SHAs, and only the deploy job gets Pages write permissions, following an automated security review.
- Homebrew was used only for packages the spec allows: `ruby-build` and `libyaml`. Two stopped `ruby@3.3` and `pandoc`/`typst` installs also pulled in build dependencies under `~/homebrew`, and these are listed in `dev/build-report.md`.

## Fictional company

- Company: CogniATion, named by the owner, 38 employees, Austin, Texas. Product: CogniATion Coach, a specialized AI chatbot that questions employees about work problems and scores their reasoning. It is sold to learning and development teams. Segments: professional services firms, software companies, financial services firms.
- Competitors: Arguvia and Elenchly. Customers: Brightmere Advisory, Corvane Software, Haldane Ridge Capital.
- Web searches on 2026-11-01 found no exact match for CogniATion, Arguvia, Brightmere Advisory, Corvane Software or Haldane Ridge Capital. A review on 2026-11-02 found that the first competitor name, Deliberon, belongs to a real Windows AI app, so it became Elenchly, which had no exact match in a search that day. Similar real names exist (Cognition AI, ArguAI, Cogni), none of them exact. CogniATion is close to Cognition AI, a real company. The owner chose the name, so it was kept. Searches cannot prove a name is unused.
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
