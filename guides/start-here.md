---
title: Start here
type: guide
version: 0.1.0
updated: 2026-11-02
summary: Start from the job you need to finish. Give the office the facts that job needs, set up your AI tool and get a first draft, in about one to two hours.
diagram: office
diagram_caption: "What you are setting up. The steps below get you to your first draft."
---

## Who it is for

A marketer running a sales-led B2B company's marketing alone, with the AI subscription they already pay for. You need no code, no API keys and no servers. It covers getting and converting new business, with sales support. Retention, expansion, pricing and product-led growth are outside the current library.

Pick the row that fits. It decides which facts you need now.

| Where you are | First useful outcome | Your route | Leave for later |
|---|---|---|---|
| I need something today | One sales asset, campaign brief or leadership update | In step 1, use the [quick start](fill-the-context-pack.md#quick-start-in-15-minutes), and expect many placeholders. In step 2, use your guide's plain-chat fallback if you have no time for a project | The full library setup and context fields this job does not need |
| I am starting marketing, or a founder still sells | Buyer evidence, minimum sales material and one channel test | In step 1, use [No documents yet](fill-the-context-pack.md#no-documents-yet). In step 4, run [Starting from zero](../playbooks/from-zero.md) | Mature reporting, a broad content cadence and most specialist roles |
| I already run marketing | Priorities from your current work and results | In step 1, use [the first-pass prompt](fill-the-context-pack.md#fast-first-pass) on what you already have. In step 3, run [Monday in one chat](../playbooks/weekly.md#run-monday-in-one-chat) | Recreating goals, definitions and assets that already exist |
| I am only looking | A sample output with nothing to set up | [Try it in 10 minutes](../try.md), then stop | Everything else |

## What you need

- Any AI chat that takes file uploads, for step 1.
- A paid personal subscription to Claude, ChatGPT, Grok or Google Gemini, from step 2. On a team or company plan, ask whoever runs it whether projects and uploads are allowed. These steps were not checked there, and the plain-chat fallback still applies.
- Your company's basic facts: notes, old decks or the founders' time. Blanks are fine.
- One to two hours for steps 1 to 3, depending on your route. All times here are estimates from the steps, not measurements.

## Steps

1. **Name the job, and give the office the facts it needs. 15 minutes to an hour.** Use the [quick start](fill-the-context-pack.md#quick-start-in-15-minutes) or the [fast first pass](fill-the-context-pack.md#fast-first-pass), in plain chat. You end with one file, `my-context-pack.md`. Every skill reads it, so this step matters the most. If you want to see a result first, [try a sample company](../try.md), which takes 10 minutes and is optional.
2. **Set up your AI tool. About 30 minutes.** Follow one guide, and only one:
   - [Set up on Claude](setup-claude.md)
   - [Set up on ChatGPT and Codex](setup-chatgpt-codex.md)
   - [Set up on Grok](setup-grok.md)
   - [Set up on Google Gemini](setup-google.md)
3. **Ask for the job you named. About 15 minutes.** In your project, ask in plain words, for your own company. For example:

   ```
   Write a sales one-pager for our most important segment, aimed at the person who signs, for one-to-one use by sales.
   ```

   Answer the questions under "Assumptions and open questions" and ask for a new draft. [Use a skill](use-a-skill.md) covers the details.
4. **Start the routine.** Run [First week](../playbooks/first-week.md), or [Starting from zero](../playbooks/from-zero.md) if a founder still sells. Then [Weekly](../playbooks/weekly.md) takes over, at about two hours a week to start. When you are not sure what is next, ask: "What should I do next?" To keep track of jobs across chats, use [the workboard](../office/my-workboard.md), or your own task tool. [Run my week](../run-my-week.md) is the page to come back to.

Reference when you need it: [Setup guides](../setup.md), [Context pack](../context-pack.md), [Agent roles](../agent-roles.md).

## Worked example: what a fuller pack buys

The same request for one page for professional services firms, aimed at the VP of people, on three files of the sample company's pack (company, product, messaging), then on all ten.

Only the fields that differ are shown, shortened. Worked by following the skill, so a model's wording will vary. CogniATion is fictional. See [the full page](../try.md).

| Field | Three files | Full pack |
|---|---|---|
| The problem | `[buyer's daily problem needed]` `[segment's reason to buy needed]` | Your partners worry that junior staff accept the AI assistant's answers unchecked. That work reaches clients. |
| People keep practicing | More than 2.3 million practice sessions completed as of September 30, 2026 | 72% of assigned learners completed at least one session each week in Q3 2026 |
| You can see reasoning improve | `[progress proof needed]` | Brightmere Advisory's analysts raised their score on client memo reasoning by 22% |
| Customer quote | `[customer quote needed]` | Lena Marsh's approved quote, Brightmere Advisory |
| Common questions | `[buyer's objections needed]`: `[answer needed from sales]` | Legal review and feeling watched, answered from product.md |
| Approvals | `[approver needed]` | Tom Ferrant, head of sales, 2 days |

The three-file version does not borrow the 72% or the 22% from messaging.md, because only proof-points.md can clear them. It asks instead, and each bracket tells you which section to fill next.

## What success looks like

You have a one-page draft for your own company, using your real messaging and proof points, in the format the skill promises. It ends with a short list of assumptions and questions, not with made-up facts.

### What done looks like

That first draft is the start. Your CEO will ask what "set up" means when it is finished, and this is the answer:

- A project in your AI tool holding the office manual, your context pack and the skills.
- Company facts in one file, with customer items marked for permission.
- Goals for the quarter agreed with your CEO, and a plan with a budget.
- Agreed lead rules with sales and tracking in place.
- One output through draft, review and approval, and a weekly routine.

To check a draft's judgment and not only its rules, see [Judge an output](judge-an-output.md). For any word you do not know, see [the glossary](../office/glossary.md).

## Troubleshooting

- **The output sounds generic.** The context pack is thin, or the tool cannot see it. Ask: "List the context pack sections you can see, and say which have blanks." Then fill in what is missing in `my-context-pack.md` and upload it again.
- **The model made up a customer or a number.** Point to the rule: "The office manual says never to invent facts. Remove anything not in the context pack, and ask me for what is missing." If this keeps happening, check that the office manual is loaded.
- **It picked the wrong skill.** Say which one you want: `Use the skill "Write a battlecard"`. Titles are on [Find a task](../skills.md).
- **The tool cannot find a skill.** Upload or paste the skill's own file into the chat. Your setup guide's Plain-chat fallback section covers working this way.
- **You have only an hour today.** Use the quick start and your guide's plain-chat fallback. The project can wait, because your file is saved and blanks are fine.
- **You want only a few files.** Open any page on this site and use Copy full text or Download file at the top of the page.
