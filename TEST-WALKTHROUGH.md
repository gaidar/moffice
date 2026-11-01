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
| 5 | One setup guide | Creates a project, pastes the office manual, uploads 3 files, runs two check prompts | No |
| 6 | `guides/use-a-skill.md` | Copies a skill's prompt, gets a draft, answers its questions, asks for a second draft | No |
| 7 | `playbooks/first-week.md`, `playbooks/weekly.md` | Starts the routine | No |

Each setup guide also has a plain-chat fallback that works with no vendor feature beyond chat and file upload.

## Cold runs

Fresh model sessions received only the files a marketer would load.

| Run | Result |
|---|---|
| Write a sales one-pager, CogniATion | Template followed, all limits met, all seven checks passed, no invented customer or number |
| Write a campaign brief, CogniATion | Six of seven checks passed. It could not name skills with only two loaded. The skill now allows a placeholder there |
| Try it, following the page | One-pager matched the page, with the same facts and placeholder. Send order was unclear, since fixed |

The runs were on one vendor's model. They say nothing about how the other vendors' models would do. They were not repeated after the last fixes.

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
| Toolbar on every skill, agent, playbook and guide page | Pass, 89 of 89 pages, script over the built site |
| Copy prompt on every skill and charter, and it copies the right text | Pass, 70 of 70 pages by script, one tested in the browser |
| Download PDF only on 18 playbook and guide pages | Pass, script over the built site |
| Internal links and 227 anchors | Pass, none missing, script over the built site |
| Skills filter on phrases such as "pipeline down" and "leads are bad", with a message when nothing matches | Pass, browser check |
