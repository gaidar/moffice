---
title: FAQ
type: guide
version: 0.1.0
updated: 2026-11-02
summary: Short answers on cost, AI tools, limits, data and what the office does not do.
---

## What it is

**What is the Marketing Office?** A free, open source playbook: a set of skills and agent roles in plain text that you load into your AI tool, plus a company context pack that every skill reads and a weekly, monthly and quarterly cadence.

**Does it replace a marketing team?** It gives one marketer the structure of a department: defined roles, written procedures and fixed output formats. It produces drafts, plans, analyses and reviews, and the marketer decides. It does not know your market, your customers or what will work.

**Are there results or benchmarks I can expect?** None are claimed. The project has no customer data, and any time estimate in the guides is labeled as an estimate.

**Why not just ask my AI tool?** You can. Without this, each request starts from nothing, so facts drift, formats change and the model fills gaps with plausible guesses. The office keeps the facts in one place, gives each job written steps and a fixed format, and tells the model to ask rather than guess.

**Who is it for?** One marketer, or a small team, at a sales-led B2B tech company. Product-led motions are not covered.

**A founder still sells, and we have few or no customers. Is this for us?** Yes. [Starting from zero](../playbooks/from-zero.md) gives you the first 90 days, says what the skills' terms mean at your stage and lists what to skip. A spreadsheet counts as a CRM.

**I have run marketing before. What is the fast way in?** Ask in plain words, once your project is set up. You do not need the role names or the skill titles. You need [the first-pass prompt](fill-the-context-pack.md#fast-first-pass) and [your setup guide](../setup.md).

**What if I have no data yet?** Start anyway, with [Starting from zero](../playbooks/from-zero.md) if you have nothing at all. Leave blanks in the context pack, and skills will ask or leave a visible placeholder. Skills that need numbers, such as Allocate the budget, have a route for no history, and label the result a hypothesis.

## Cost and setup

**What does it cost?** The Marketing Office is free, under the Apache License 2.0, with no hosted service. You pay for your own subscription to your AI tool. Check the plan and price on its site.

**How long does setup take?** About two hours to a first draft with your own facts. These are estimates from the steps in the guides, not measured averages.

**Do I need to code or use a terminal?** No. No servers and no API keys either. Copying, pasting, uploading files and following numbered steps cover everything.

**Which AI tool should I choose?** The one you already pay for. Skills, agent roles and the context pack are identical across all of them. Only the setup guide differs.

**My AI tool's screen does not match the guide.** These tools change often. Each setup guide has a verification date and the help pages it was checked against. Check those pages, or use the guide's plain-chat fallback.

## What it does not do

**Does it connect to my CMS, CRM or email tool?** No. The office has no connectors to external tools. You paste exports in, and you copy outputs out. To fit your own tools, see [Write your own skill](write-your-own-skill.md).

**Will it publish or send anything?** No. It writes drafts. You publish and send.

**Does it browse the web for competitor news or search volumes?** Skills do not assume it can. You paste the data in, or the skill labels it unknown. If your tool can browse, you may ask it to, and you should check the sources it gives.

## Data and trust

**Where does my context pack live?** In your own files, and in your AI tool account once you upload it. The Marketing Office has no server and sees nothing. Read your AI tool's terms and your company's policy before you upload anything confidential. You can leave sensitive numbers out of the context pack, and the skills will ask when they need them.

**Can I trust the output?** Treat it as a draft from a capable new hire who has read your files. Skills check drafts against the context pack and list their assumptions, but models still make errors. Run the Quality checklist, and use the marketing reviewer for anything public.

**What stops it from making up customers or numbers?** Rules in the office manual and in each skill: use only the context pack, use proof points only with the right permission status, ask when something is blank. These rules lower the risk but do not remove it. Check names, numbers and quotes yourself.

**Are the example companies real?** No. CogniATion, CogniATion Coach, Arguvia, Elenchly and the customers in the examples are invented. Their names were searched on the web, and no exact match turned up, though a search cannot prove a name is unused.

## Using it

**What if no skill fits my job?** Ask anyway. The office manual tells the model to say no skill covers it, name the closest one, do the work under the same rules and label the result as ad hoc.

**Do I have to use the exact prompts?** No. In a project, say what you need, and the office picks the skill and tells you which. The exact form is there for when it picks wrong.

**I work with a freelancer or an agency. How do I share this?** Keep one master `my-context-pack.md`, with one person who edits it. Send a brief, plus only the sections of the pack the job needs: [Write a design brief](../skills/brand-and-design-briefs/write-design-brief.md) for designers, and [Write a campaign brief](../skills/campaign-design/write-campaign-brief.md) for everyone else. Check what they return with [Review any output](../skills/marketing-ops/review-any-output.md).

**Why are all the outputs in the same format?** So that you can compare them over time, hand them from one role to another and check them quickly.

**Can I edit the skills?** Yes. They are plain text, and the license allows it. Keep a copy of your changes for when you take a new version.

**Why do only some pages have a PDF?** PDFs are for procedures people read: playbooks and guides. Skills, charters and the context pack go into your AI tool, so they are text files on GitHub.

**How do I report a mistake?** Use the Report an issue link at the bottom of every page. See [Contributing](../CONTRIBUTING.md) for suggesting changes.
