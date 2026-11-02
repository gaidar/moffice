# Test walkthrough

Traced on 2026-11-02. It covers the path a new marketer follows from the home page to a first output.

## What this test is, and is not

- **Done:** reading every step in order as a marketer would, checking that links and anchors resolve, and checking that no step needs a terminal, an API key or a server. Fresh model sessions followed the trial and two skills, using only the files a marketer would load. A senior marketing review and a junior marketer review went through the site.
- **Not done:** running these steps in a live vendor account or with a real marketer. Vendor screens were not seen. Vendor steps rest on fetched help pages, and each guide marks what it could not verify.

## The path

| Step | Page or action | What the marketer does | Terminal, API key or server? |
|---|---|---|---|
| 1 | Home page, `index.md` | Reads what you get, sees a sample output, clicks Try it | No |
| 2 | `try.md` | Copies the sample file, pastes it with one message into any AI chat, compares the result | No |
| 3 | `guides/start-here.md` | Decides to go on | No |
| 4 | `guides/fill-the-context-pack.md` | Uploads the combined templates and source documents to one chat, answers blocking questions, saves one file | No |
| 5 | One setup guide | Downloads two files, creates a project, pastes the office manual, uploads 3 files, runs one check | No |
| 6 | `guides/use-a-skill.md` | Asks in plain words, checks which skill it used, answers its questions, asks for a second draft | No |
| 7 | `playbooks/first-week.md` or `playbooks/from-zero.md`, then `playbooks/weekly.md` | Starts the routine | No |

Each setup guide also has a plain-chat fallback that works with no vendor feature beyond chat and file upload.

## Cold runs

Fresh model sessions received only the files a marketer would load.

| Run | Result |
|---|---|
| Write a sales one-pager, CogniATion | Template followed, all limits met, all seven checks passed, no invented customer or number |
| Write a campaign brief, CogniATion | Six of seven checks passed. It could not name skills with only two loaded. The skill now allows a placeholder there |
| Try it, following the page | One-pager matched the page, with the same facts and placeholder. Send order was unclear, since fixed |
| Plain requests, 8 messages with no skill named, CogniATion | 6 went to a suitable skill or sequence, 1 ambiguous message got a clarifying question, 1 with no skill was flagged as ad hoc. Line order and playbook naming were unclear, since fixed |
| "We are brand new, what first?", blank pack | Reached Starting from zero, and named what to skip |
| Founder interview prompt, no documents | Filled only what was said. Plain facts unmarked, the claim about buyers marked "(founder belief)". An earlier run kept stale template lines, since fixed |
| Write a home page, with an unsupported 70% claim marked founder belief | Kept the claim off the page and asked for its source |
| Define the ICP, with findings that contradict the founders' belief | Followed the findings, flagged the conflict and marked every criterion Hypothesis |

The runs were on one vendor's model, reading files directly and not through a vendor's project. They say nothing about how the other vendors' models or their file search would do. The first three skill rows were not repeated after the last fixes.

## Problems found and fixed

| Problem | Fix |
|---|---|
| About a day of effort before any useful draft | A 10-minute trial, then a one-hour first pass |
| 74 uploads, and 10 rounds of chat to fill the pack | One combined pack file, and 3 files to upload |
| Blank templates could be read as facts | The office manual says only text after "Answer:" counts. Blanks are no longer uploaded |
| Finding a skill needed the system's vocabulary | A table by situation, keywords behind the filter, and a message when nothing matches |
| Nothing helped set goals, and the plan stopped without them | Propose quarterly goals, with a CEO script |
| Review read as approval of the idea | The verdict now says strategy was not judged, and names the weakest idea |
| Confidential data warning was only in the FAQ | Moved to the upload step |
| First week and weekly routines assumed too much | A CEO conversation on day 1, conversations across the week, a starter routine |

## Site checks

Run on the local build on 2026-11-02. The live site is offline while the repository is private, so these need repeating at the release, along with Copy text and Raw file, which read from GitHub.

| Check | Result |
|---|---|
| Top bar on every page, Contributing, Guides, Office and Glossary in the footer | Pass, browser check |
| Toolbar on every skill, agent, playbook and guide page | Pass, 90 of 90 pages, script over the built site |
| Copy prompt on every skill and charter, and it copies the right text | Pass, 70 of 70 pages by script, one tested in the browser |
| Download PDF only on 19 playbook and guide pages | Pass, script over the built site |
| Internal links and 237 anchors | Pass, none missing, script over the built site |
| One Skills filter over situations and the full list, on phrases such as "new company", "90-day plan" and "leads are bad", with a message when nothing matches | Pass, browser check |
| Model instructions folded on skill pages, opened by a link to a section inside, with section numbers kept | Pass, one page in the browser |
| Download links in setup guides save each file under its own name | Save path passed against a simulated GitHub response. Failure path passed for real, by opening the raw file. Repeat at the release |
