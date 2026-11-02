---
title: Start here
type: guide
version: 0.1.0
updated: 2026-11-02
summary: From nothing to a first draft with your own facts, in about two hours, starting with a 10-minute trial on a sample company.
diagram: office
diagram_caption: "What you are setting up. The steps below get you to your first draft."
---

## Who it is for

A marketer who wants to run a tech company's marketing function alone, with the AI subscription they already pay for. You need no code, no API keys and no servers.

| Where you are | What it changes |
|---|---|
| Looking, not committing | Do step 1 and stop |
| The company has a sales team | All five steps. In step 5, run First week |
| A founder still sells, with few or no customers | All five steps. In step 2, use [No documents yet](fill-the-context-pack.md#no-documents-yet). In step 5, run [Starting from zero](../playbooks/from-zero.md) |
| You have run marketing before | Same steps, faster. You need [the first-pass prompt](fill-the-context-pack.md#fast-first-pass) and [your setup guide](../setup.md) |

## What you need

- Any AI chat that takes file uploads, for steps 1 and 2.
- A paid personal subscription to Claude, ChatGPT, Grok or Google Gemini, from step 3. On a team or company plan, ask whoever runs it whether projects and uploads are allowed. These steps were not checked there, and the plain-chat fallback still applies.
- Your company's basic facts: notes, old decks or the founders' time. Blanks are fine.
- About two hours for steps 1 to 4. All times here are estimates from the steps, not measurements.

## Steps

1. **Try it with a sample company. 10 minutes.** Follow [Try it in 10 minutes](../try.md). You see a real draft with nothing to set up.
2. **Make a first pass of the context pack. About an hour.** Follow [Fast first pass](fill-the-context-pack.md#fast-first-pass) in plain chat. You end with one file, `my-context-pack.md`. Every skill reads it, so this step matters the most.
3. **Set up your AI tool. About 30 minutes.** Follow one guide, and only one:
   - [Set up on Claude](setup-claude.md)
   - [Set up on ChatGPT and Codex](setup-chatgpt-codex.md)
   - [Set up on Grok](setup-grok.md)
   - [Set up on Google Gemini](setup-google.md)
4. **Ask for your first draft. About 15 minutes.** In your project, ask in plain words, for your own company:

   ```
   Write a sales one-pager for our most important segment, aimed at the person who signs, for one-to-one use by sales.
   ```

   Answer the questions under "Assumptions and open questions" and ask for a new draft. [Use a skill](use-a-skill.md) covers the details.
5. **Start the routine.** Run [First week](../playbooks/first-week.md), or [Starting from zero](../playbooks/from-zero.md) if a founder still sells. Then [Weekly](../playbooks/weekly.md) takes over, at about two hours a week to start. When you are not sure what is next, ask: "What should I do next?"

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
- **It picked the wrong skill.** Say which one you want: `Use the skill "Write a battlecard"`. Titles are on the [Skills page](../skills.md).
- **The tool cannot find a skill.** Upload or paste the skill's own file into the chat. Your setup guide's Plain-chat fallback section covers working this way.
- **You have only an hour today.** Do steps 1 and 2. The setup can wait, because your file is saved and blanks are fine.
- **You want only a few files.** Open any page on this site and use Copy text or Raw file at the top of the page.
