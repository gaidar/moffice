# Test walkthrough

Traced on 2026-11-01. It covers the path a new marketer follows from the home page to a first output, using only Start here, one vendor setup guide and the "Fill the context pack" guide.

## What this test is, and is not

- **Done:** reading every step in order as a marketer would, checking that each link resolves, and checking that no step needs a terminal, an API key or a server. A fresh model session also ran the first skill from only the files a marketer would load, with the example pack as context.
- **Not done:** running these steps in a live vendor account or with a real marketer. Vendor screens were not seen. Vendor steps rest on fetched help pages, and each guide marks what it could not verify.

## The path

| Step | Page or action | What the marketer does | Terminal, API key or server? |
|---|---|---|---|
| 1 | Home page, `index.md` | Reads one paragraph and three steps, then clicks Start here | No |
| 2 | `guides/start-here.md`, step 1 | Opens the repository on GitHub. No account is needed | No |
| 3 | Start here, step 2 | Picks one of four setup guides | No |
| 4 | `guides/setup-claude.md`, steps 1 to 3 | Gets the files with GitHub's Code and Download ZIP buttons, creates a project and pastes the office manual | No |
| 5 | Setup guide, steps 4 to 6 | Uploads 10 context pack templates, then skills and charters, or the two bundle files | No |
| 6 | Setup guide, step 7 | Pastes the check prompt and confirms the answer | No |
| 7 | `guides/fill-the-context-pack.md` | For each of 10 files, uses the interview prompt, saves the answer in a text editor and uploads it | No |
| 8 | Fill the context pack, check prompt | Confirms that there are no contradictions | No |
| 9 | `guides/start-here.md`, step 4, and `guides/use-a-skill.md` | Pastes the "Write a sales one-pager" prompt | No |
| 10 | Start here, step 5 | Reads the output, answers the open questions, runs the Quality checklist | No |

The other three setup guides follow the same path:

| Guide | Persistent feature | Uploads | Notes |
|---|---|---|---|
| `setup-chatgpt-codex.md` | ChatGPT project | 12 files, because the verified limits are 25 on Plus and 40 on Pro | Codex note is optional, and no step in it uses a terminal |
| `setup-grok.md` | Grok project | 74 files, or 12 if rejected | xAI has no Projects help page, so several details are marked Unverified |
| `setup-google.md` | Gemini notebook | 74 files, or 12 | Gems were avoided because Google is making them read-only on November 17, 2026 |

Each guide also has a plain-chat fallback that works with no vendor feature beyond chat and file upload.

## Cold run of the first skill

A fresh model session received only the office manual, the 10 example pack files and the skill file. It ran first on the earlier example company, then again on CogniATion after the examples were rewritten. The prompt on CogniATion:

```
Use the skill "Write a sales one-pager". Read the context pack.
Task: one page for professional services firms, aimed at the VP of people, for one-to-one use by sales.
```

Result: a full one-pager in the template format, within every length limit, passing all seven checklist items, ending with "Assumptions and open questions", with no invented customer or number. It left a placeholder for the one question the pack could not answer. That gap was then filled.

A second skill, "Write a campaign brief", also ran cold. It passed six of seven checks. It could not name the skills for each asset, because only two skills were loaded, which is what a plain-chat session looks like. The skill now allows a placeholder there. It also needed a rule for the campaign's share of the goal, now added as a starting rule.

The runs were on one vendor's model. They say nothing about how the other vendors' models would do. Neither run was repeated after these last fixes.

## Problems found and fixed

| Problem | Fix |
|---|---|
| The blank templates hold fictional example lines, which a model could take as facts about the marketer's company | The office manual now says only text after "Answer:" counts |
| The manual said to ask before drafting, while skills told the model to write placeholders | The manual now says to ask first only if a blank changes the whole output, and otherwise to use a placeholder and ask at the end |
| The limit of one statistic per output, read literally, banned the company's own proof numbers | The limit now covers outside-world figures only |
| The approval table made every use of an approved customer quote look like a two-week job | The example pack now separates new customer items from those already approved |
| The condensed example in a skill differed from its template | The manual now says the template wins |
| The one-pager template had no line for the company name | Added |
| The manual pointed to a document not loaded in the tool | Reference removed |
| The pack had no answer to a buyer's legal and data questions | Added a Data and security field to the product template and example |
| The internal manager view release left its effect on team-level reports unclear | The example now states its scope |

## Site checks

Run on the final build. PDF checks apply to playbooks and guides only.

| Check | Result |
|---|---|
| Home, Start here, Setup, Context pack, Agents, Skills, Playbooks and FAQ are in the top bar on every page, Contributing in the footer | Pass, browser check |
| Every skill, agent, playbook and guide page has a toolbar | Pass, 81 of 81 pages, script over the built site |
| Download PDF appears only on 16 playbook and guide pages | Pass, script over the built site |
| Internal links, and GitHub links keeping their `.md` ending | Pass, script over the built site |
| Mobile width, 390 pixels, no horizontal page scroll | Pass, browser check |
| Skills filter narrows the list and hides empty groups | Pass, browser check |

A browser check found that the `.md` to `.html` link rewrite was also breaking GitHub links. The layout now protects external links.

## Checks on the live site

Run on 2026-11-01 against <https://gaidar.github.io/moffice/>.

| Check | Result |
|---|---|
| Home, Start here, Setup, Context pack, Agents, Skills, Playbooks, Guides, FAQ and Contributing return 200 | Pass |
| Download PDF returns a PDF for a playbook and a guide | Pass |
| Old zip, skill PDF and old example URLs return 404 | Pass |
| Bundle files are on GitHub as raw text | Pass |
| Agent role page shows three controls, guide page shows four | Pass, browser test |
| Copy text fetches the raw markdown and writes it to the clipboard | Pass, browser test |
| Copy text falls back to opening the raw file when the fetch fails | Pass, browser test with the fetch forced to fail |
| Site fonts load, no sidebar, diagrams shown | Pass, browser test |
| Dark mode | Pass, browser test |
