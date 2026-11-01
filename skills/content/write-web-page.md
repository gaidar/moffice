---
title: Write a web page
type: skill
function: content
owner: content-lead
reads: [company, product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, channels-and-tools]
you_bring: The page type, the reader, the one action the page asks for, and any SEO page brief.
also_for: [website copy, landing page, homepage, website rewrite, pricing page, website not converting, demo request page, product page]
version: 0.1.0
updated: 2026-11-01
summary: Produces section-by-section copy for one web or landing page, with one reader, one action and every proof item checked for permission.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this for copy on one web or landing page. Do not use it for an article; use [Write a blog post](write-blog-post.md) instead. For a handout that sales sends or leaves behind, use [Write a sales one-pager](../product-marketing-and-sales-enablement/write-sales-one-pager.md).

## Inputs

- [[context-pack:messaging]]: positioning, pillars, messages by persona, words to avoid.
- [[context-pack:product]]: features, prices, what it is not, roadmap limits.
- [[context-pack:personas]]: the reader's daily problem and objections.
- [[context-pack:icp-and-segments]]: why each segment buys.
- [[context-pack:proof-points]]: customers, numbers and quotes with permission status.
- [[context-pack:company]]: publishable company numbers.
- [[context-pack:competitors]]: dated facts, for comparison pages only.
- [[context-pack:brand-voice]]: voice, rules and visual basics.
- [[context-pack:channels-and-tools]]: approvers and hard rules.

The marketer supplies the page type, the reader, the one action the page asks for, and any SEO page brief.

## Procedure

1. Fix the page type, one reader and one action from the request. If the reader or action is missing, ask. If the marketer wants a draft anyway, write [reader needed] or [action needed].
2. Pick the sections by page type and omit the rest of the template. Landing or segment page: Hero, Problem, How it works, Proof, Objections, Final action. Product page: the same plus Features. Pricing page: Hero, Price, Objections, Final action. Comparison page: Hero, Comparison, Proof, Final action. Any other type: ask which of these is closest.
3. If an SEO page brief was pasted, take its topic, search intent and headings, and put the primary keyword in the SEO title and hero. State no search volumes unless supplied.
4. Write the headline first, from the pillar that best answers the reader's daily problem. If two fit, take the first in messaging.md, a starting rule. It says what happens to the reader, not how the company feels.
5. Write each section to do one job. Problem uses the reader's situation and the segment's reason to buy. How it works has exactly three steps from product.md. Objections answers up to three objections from personas.md, each with a fact from the context pack.
6. Use a customer name, number or quote only if proof-points.md marks it public, and a company number only if company.md marks it publishable. State the sample and date of each number. If a claim in messaging.md has no entry in proof-points.md, leave it out and ask.
7. Claim nothing listed under what the product is not, and mention no roadmap items unless product.md clears them.
8. Include prices only on pricing pages or when asked, using the exact price points, and add the pricing approver to Approvals needed.
9. Name competitors only on comparison pages, using only facts in competitors.md with their source and date.
10. Write the hero's visual note from the visual basics in brand-voice.md. If no real image exists, write [image needed].
11. Check the draft against the context pack, line by line: facts, permissions, words to avoid, voice rules. Fix anything that contradicts a file.
12. List everything assumed under "Assumptions and open questions". If a needed context pack field is blank, leave a placeholder in square brackets and ask in the last section. Never invent.

The marketer places the copy in their own CMS. This skill publishes nothing.

## Output format

```
Status: Draft
Page type: <landing, segment, product, pricing or comparison>
Reader: <segment and persona, up to 12 words>
Action: <the one action, up to 8 words>
SEO title: <up to 60 characters>
Meta description: <up to 155 characters>

## Hero
Headline: <up to 10 words, sentence case>
Subhead: <up to 25 words>
Button: <up to 4 words>
Visual note: <up to 20 words>

## Problem
<up to 60 words>

## How it works
<exactly 3 steps, each up to 20 words>

## Features
<product pages only: 3 to 6 items, up to 15 words each>

## Price
<pricing pages only: price points, what is included, up to 60 words>

## Comparison
<comparison pages only: up to 6 rows, each fact with source and date>

## Proof
<1 to 3 quotes or numbers, attributed, with sample and date>

## Objections
<up to 3: objection in the reader's words, answer up to 30 words>

## Final action
<one line, up to 15 words, and the hero's button>

## Proof used
<each item and its permission status>

## Approvals needed
<approver and typical time from channels-and-tools.md, or "None">

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the page have one reader and one action, with the same button at top and bottom?
- [ ] Does every proof item show public or publishable status in Proof used?
- [ ] Does each number state its sample and date?
- [ ] Are competitors unnamed unless this is a comparison page?
- [ ] Is every claim inside the limits in product.md, with no roadmap items?
- [ ] Are the words to avoid absent and the brand voice rules followed?
- [ ] Is every pricing mention listed under Approvals needed?

## Example (fictional company)

**Status:** Draft

**Page type:** Landing. **Reader:** Professional services head of learning. **Action:** Request a demo.

**SEO title:** Critical thinking training for analysts | CogniATion

**Meta description:** CogniATion Coach questions your analysts on work problems and won't give the answer.

**Hero**

Headline: See reasoning improve, team by team

Subhead: CogniATion Coach is an AI chatbot that won't give your people the answer. They practice reasoning on work problems.

Button: Request a demo

Visual note: Team-level report screenshot, no individual names or scores.

**Problem**

Everyone finishes the course, and nobody can show it changed how they work. In your firm, their reasoning reaches clients.

**How it works**

1. Choose from 180 work scenarios, or build ones from your documents.
2. In about 15 minutes, the Coach asks for assumptions, evidence and alternatives, and won't give the answer.
3. The Coach scores reasoning against a rubric. You see progress by team, never an individual's conversation.

**Proof**

Brightmere Advisory's analysts raised their average score on client memo reasoning by 22% in one quarter of 2026, as measured by Brightmere's partners.

"My analysts stopped asking the bot for the answer and started defending their own." Lena Marsh, head of learning, Brightmere Advisory.

**Objections**

"People won't make time for another training tool." 72% of assigned learners completed at least one session each week (all customers, Q3 2026).

**Final action**

Show that training changed how people reason. Button: Request a demo

**Proof used:** Brightmere result, Marsh quote, 72% figure, public.

**Approvals needed:** The marketer, same day.

**Assumptions and open questions**

- Assumption: a demo request is the action.
- Unknown: which report screenshot can the hero use?

## How to run it

```
Use the skill "Write a web page". Read the context pack.
Task: <the page type, the reader, the one action, and any SEO page brief>.
```
