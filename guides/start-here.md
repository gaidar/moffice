---
title: Start here
type: guide
version: 0.1.0
updated: 2026-11-01
summary: The single entry point, from nothing to a first working output in under one working day.
diagram: office
diagram_caption: "What you are setting up. The steps below get you to your first draft."
---

## Who it is for

A marketer with one paid personal subscription to Claude, ChatGPT, Grok or Google Gemini, who wants to run a tech company's marketing function alone. You need no code, no API keys and no servers.

The Marketing Office does not know your market. It produces drafts, plans, analyses and reviews, and you decide what to use.

## What you need

- A paid personal subscription to one of the four tools above.
- A browser.
- Your company's basic facts: messaging, target customers, product facts, proof points. Rough notes and old decks are fine. Blanks are fine too.
- About one working day. This is an estimate: about 1 hour for setup, 3 to 5 hours for the context pack, and about 1 hour for your first outputs.

## Steps

1. Open [the Marketing Office on GitHub](https://github.com/gaidar/moffice). Everything is there as plain text. You do not need a GitHub account. Your setup guide shows how to get the files onto your computer.
2. Set up your tool. Follow one guide, and only one:
   - [Set up on Claude](setup-claude.md)
   - [Set up on ChatGPT and Codex](setup-chatgpt-codex.md)
   - [Set up on Grok](setup-grok.md)
   - [Set up on Google Gemini](setup-google.md)
3. Fill the context pack. Follow [Fill the context pack](fill-the-context-pack.md). This step takes the most time and matters the most, because every skill reads these files.
4. Run your first skill. Follow [Use a skill](use-a-skill.md), and paste this into your tool, changing the words after "Task:":

   ```
   Use the skill "Write a sales one-pager". Read the context pack.
   Task: one page for our most important segment, aimed at the person who signs.
   ```

5. Check the output against the Quality checklist at the end of [the skill](../skills/product-marketing-and-sales-enablement/write-sales-one-pager.md). Then answer any questions under "Assumptions and open questions" and ask for a new draft.
6. Try an agent role. Follow [Invoke an agent role](invoke-an-agent.md).
7. Start the cadence. Run [the first week playbook](../playbooks/first-week.md), then [the weekly playbook](../playbooks/weekly.md).

## What success looks like

You have a one-page draft for your own company, using your real messaging and proof points, in the format the skill promises. It ends with a short list of assumptions and questions, not with made-up facts.

## Troubleshooting

- **The output sounds generic.** The context pack is thin, or the tool cannot see it. Ask: "Which context pack files can you see?" Then fill in or upload what is missing.
- **The model made up a customer or a number.** Point to the rule: "The office manual says never to invent facts. Remove anything not in the context pack, and ask me for what is missing." If this keeps happening, check that the office manual is loaded.
- **The tool cannot find a skill.** Upload or paste the skill file into the chat. Your setup guide's Plain-chat fallback section covers working this way.
- **You have only an hour today.** Do steps 1 and 2 today, and fill in only company.md, product.md and messaging.md for now. Skills will ask about the rest.
- **You want only a few files.** Open any page on this site and use Copy text or Raw file at the top of the page.
