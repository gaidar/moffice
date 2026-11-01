---
title: Write a blog post
type: skill
function: content
owner: content-lead
reads: [company, product, personas, messaging, competitors, proof-points, brand-voice, channels-and-tools]
you_bring: An angle or SEO page brief, plus notes or sources for anything about practice, standards or regulation.
also_for: [blog article, thought leadership, website traffic, article idea, content for seo, write a post, organic traffic, blog draft]
version: 0.1.0
updated: 2026-11-01
summary: Produces one blog post from an angle or SEO page brief, built on material the marketer supplied and proof cleared for public use.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this for one post, from an angle you already have or a brief from [Write an SEO page brief](../seo/write-seo-page-brief.md). Do not use it for a page that asks the reader to act on an offer; use [Write a web page](write-web-page.md) instead. For a customer story, use [Write a case study](../product-marketing-and-sales-enablement/write-case-study.md).

## Inputs

- [[context-pack:personas]]: the reader's daily problem, objections and language.
- [[context-pack:messaging]]: pillars, messages by persona, words to use and avoid.
- [[context-pack:product]]: what the product does, what it is not, roadmap limits.
- [[context-pack:proof-points]]: customers, numbers and quotes with permission status.
- [[context-pack:company]]: which company numbers may be published.
- [[context-pack:competitors]]: why buyers stay with what they have today.
- [[context-pack:brand-voice]]: voice, point of view, rules.
- [[context-pack:channels-and-tools]]: who approves blog posts and pricing mentions.

The marketer supplies the angle or SEO page brief, plus notes or pasted sources for anything about practice, standards or regulation.

## Procedure

1. Find the source. If the marketer pasted an SEO page brief, take its topic, search intent, primary keyword and headings as given. If they gave an angle, use it. If they gave only a topic, write three one-sentence angles, choose the first that names a daily problem from personas.md (a starting rule), and record the choice as an assumption.
2. Fix one reader, the persona whose daily problem the angle names, or the first listed on a tie (a starting rule), and one takeaway: a single sentence saying what the reader can do after reading, even if they never buy.
3. Sort the material into three piles: facts from the context pack, what the marketer supplied, and what is missing. Claims about practice, standards or regulation come only from the marketer's notes or pasted sources. For each gap, write [source needed: what is missing] in the post and do not fill it from memory.
4. Write the outline: title, opening, three to five sections, closing action. Each section heading says what the reader finds out. Use time order for a sequence, otherwise put the most useful section first.
5. Draft to 600 to 1,000 words, unless the SEO page brief sets another length. Name the problem in the first two sentences, with no background first. End each section with something the reader can do or check.
6. Keep the product in its place: at most two mentions in the body, plus the closing action. Each mention describes something in product.md.
7. Add proof only where it backs a claim. Use a customer name, number or quote only if proof-points.md marks it public, and a company number only if company.md marks it publishable. State the sample and date. If a claim in messaging.md has no entry in proof-points.md, leave it out and ask.
8. Do not name competitors. Write about the alternative in general terms. For a named comparison, use [Write a web page](write-web-page.md) with the comparison page type.
9. If a primary keyword was supplied, put it in the title, the first 100 words and one section heading. State no search volumes unless supplied. With no keyword, write "none supplied".
10. Check the draft against the context pack, line by line: facts, permissions, what the product is not, words to avoid, voice rules. Add any pricing mention to Approvals needed, with the listed approver.
11. List everything assumed under "Assumptions and open questions", with each [source needed] item as an Unknown. If a needed context pack field is blank, leave a placeholder in square brackets and ask in the last section. Never invent.

The marketer places the post in their own CMS. This skill publishes nothing.

## Output format

```
Status: Draft
Reader: <one persona, up to 8 words>
Angle: <one sentence, up to 25 words>
Takeaway: <what the reader can do, up to 20 words>
Primary keyword: <from the brief, or "none supplied">
Title: <up to 65 characters, sentence case>
Meta description: <up to 155 characters>

## Post
<opening, up to 60 words>

### <section heading, up to 10 words>
<up to 200 words, ending in something to do or check>

<3 to 5 sections in total; the length in step 5 governs if the field limits add up to more>

### <closing heading, up to 10 words>
<up to 60 words, with one action and [link needed] unless a link was supplied>

## Proof and sources used
| Item | From | Permission status or date |
|---|---|---|
<one row per item, or "None">

## Approvals needed
<approver and typical time from channels-and-tools.md>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Could a reader act on the takeaway without buying the product?
- [ ] Does each section end in something to do or check?
- [ ] Is every claim about practice, standards or regulation sourced or shown as a placeholder?
- [ ] Is the product mentioned at most twice in the body, within its limits in product.md?
- [ ] Does every customer, number and quote have public or publishable status?
- [ ] Are competitors unnamed and the words to avoid absent?
- [ ] If a keyword was supplied, does it appear in the title, the first 100 words and one heading?

## Example (fictional company)

**Status:** Draft

**Reader:** Head of learning, professional services firm

**Angle:** Three questions show whether training changed how people reason, before the leadership team asks.

**Takeaway:** Ask the three questions about one client memo this week.

**Primary keyword:** none supplied

**Title:** Three questions that show whether training changed the work

**Meta description:** Test one client memo with three questions to see whether reasoning changed.

**Post (condensed)**

Everyone finished the course. Can you show that it changed how they work? Test one client memo this week.

**What does it assume?** Ask the author to name the assumptions behind the recommendation. Note any they can't name.

**What evidence backs it?** Ask where each key claim came from, and check one. [source needed: how firms review client memos]

**What else was considered?** Ask for one alternative and why it lost. CogniATion Coach asks for all three in practice sessions of about 15 minutes, and declines to give the answer.

**Where to start.** "My analysts stopped asking the bot for the answer and started defending their own." Lena Marsh, head of learning, Brightmere Advisory. Request a demo: [link needed]

**Proof and sources used:** Marsh quote, proof-points.md, public, approved June 2026.

**Approvals needed:** The marketer, same day.

**Assumptions and open questions**

- Assumption: the post targets professional services firms.
- Unknown: what do firms check in a client memo, and where is the source?

## How to run it

```
Use the skill "Write a blog post". Read the context pack.
Task: <the angle, if there is no SEO page brief>.
<paste the brief, notes and sources here>
```
