---
title: Write a sales one-pager
type: skill
function: product-marketing-and-sales-enablement
owner: product-marketing-manager
reads: [company, product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, channels-and-tools]
you_bring: The segment, the person it is for, and whether sales will hand it over or it goes online.
also_for: [sales sheet, leave behind, sales collateral, product sheet, flyer, handout for prospects, sales asked for something, demo follow up]
version: 0.1.0
updated: 2026-11-02
summary: Writes one page for one segment or persona that sales can hand to a buyer, with proof chosen by where the page will be used.
judge: ["Would a salesperson hand this over in a meeting or leave it in a folder?", "If the buyer forwarded this to their boss with no note would the boss see why it matters?", "Is the headline about the buyer's problem or about your product?"]
show_to: a salesperson, and ask which line they would cross out before sending it
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when sales needs one page to hand to one kind of buyer in one segment. Do not use it to handle a named competitor; use [Write a battlecard](write-battlecard.md) instead. For a page on the website, use [Write a web page](../content/write-web-page.md).

## Inputs

- [[context-pack:company]]: publishable numbers and public name.
- [[context-pack:product]]: features, what it is not, price, pilot, roadmap rules.
- [[context-pack:icp-and-segments]]: why this segment buys, and triggers.
- [[context-pack:personas]]: what the buyer is measured on, daily problem, objections.
- [[context-pack:messaging]]: pillars, proof, messages by persona, words to use and avoid.
- [[context-pack:competitors]]: only what buyers do today, and why they stay.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:brand-voice]]: voice, rules, style details.
- [[context-pack:channels-and-tools]]: approvers and hard rules.

The marketer supplies: the segment, the persona, and how the page will be used. Use one-to-one means sales hands or sends it to a named buyer. Open use means anywhere online or ungated. If not stated, treat it as open use.

## Procedure

1. Choose one segment and one persona. If none is named, ask before drafting. If the marketer names several, ask which one comes first. Do not blend them.
2. Set the proof allowed. Open use takes Public items only. One-to-one use takes Public and Sales only items, keeping any limit in the entry, such as no logo. Internal only, Pending and None never appear. Prefer proof from the same segment, then the same persona (a starting rule). If a number is not listed in proof-points.md or marked publishable in company.md, leave it out.
3. Write the headline: what happens for this buyer, in at most 10 words. Use the persona's message from messaging.md as the starting point.
4. Write the problem in the buyer's terms, from the persona's daily problem and the segment's reason to buy.
5. Write what the product does for this buyer in at most 40 words, from product.md only.
6. Write three benefit lines, one per pillar. Each has a claim, a proof line and the proof's permission status in the draft notes. If a pillar has no allowed proof, write a placeholder such as [progress proof needed], or use a product fact from product.md and say so.
7. Answer up to two of the persona's objections from personas.md, in file order. If the context pack has no answer to one, write [answer needed from sales]. Do not write an answer that promises a feature. Do not name competitors. Address what buyers do today instead.
8. Include price only if product.md says it may be published and the marketer asked for it. Copy the figures as written.
9. Write one next step, using the pilot or trial in product.md if there is one. Use a placeholder for the sales contact unless the marketer supplies it.
10. Leave a placeholder in square brackets for any blank context pack field this page needs, and ask about it in the last section.
11. Check the draft against the context pack: what the product is not, words to avoid, brand voice, permission status for the stated use. Check that the page body stays within 250 words.
12. List the approvals from channels-and-tools.md: sales material, any pricing mention, any customer item not yet approved in proof-points.md. List everything assumed or unknown in the last section.

## Output format

```
Status: Draft
Segment: <one>
Persona: <one>
Use: <One-to-one or open>

## Page (250 words maximum in total; this total governs if the field limits add up to more)
Company: <public name and one-line description from company.md>
Headline: <max 10 words>
The problem: <max 40 words>
What it does: <max 40 words>
Benefits:
- <Pillar claim, max 8 words>. <Proof, max 25 words>
- <Pillar claim, max 8 words>. <Proof, max 25 words>
- <Pillar claim, max 8 words>. <Proof, max 25 words>
Customer quote: <exact approved quote, name, title, company, or placeholder>
Common questions (up to two):
- <Objection>: <answer, max 25 words>
Price: <as written in product.md, or omit this line>
Next step: <max 20 words, with contact or placeholder>

## Draft notes (not on the page)
- Proof used: <item, permission status>
- Approvals needed: <item, approver, typical time>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does it speak to one segment and one persona, on one page?
- [ ] Does every proof item have a permission status that fits the stated use?
- [ ] Are quotes exact, with name and title as approved?
- [ ] Is every product statement backed by product.md, with no roadmap items?
- [ ] Is every word on the avoid list absent, and is the voice right?
- [ ] Are competitor names absent from the page?
- [ ] Are approvers listed for sales material and any price?

## Example (fictional company)

**Status:** Draft

**Segment:** Professional services firms

**Persona:** Head of learning and development

**Use:** Open

**Page**

**Company:** CogniATion makes a specialized AI chatbot that trains employees to think through problems instead of asking for answers.

**Headline:** Show that training changed how your analysts reason

**The problem:** Everyone finishes the course, and nobody can show it changed how they work. Partners worry that junior staff accept AI answers without checking them, in work that reaches clients.

**What it does:** CogniATion Coach questions employees about a work problem instead of answering it, then scores their reasoning against a rubric. You see progress by team, never an individual's conversation.

**Benefits:**

- It asks, it does not answer. The Coach asks for assumptions, evidence and alternatives, and declines to give the answer.
- People keep practicing. 72% of assigned learners completed at least one session each week in Q3 2026.
- You can see reasoning improve. Brightmere Advisory's analysts raised their average score on client memo reasoning by 22% in one quarter of 2026, as measured by Brightmere's partners.

**Customer quote:** "My analysts stopped asking the bot for the answer and started defending their own." Lena Marsh, head of learning, Brightmere Advisory

**Common questions:**

- "People won't make time for another training tool": Sessions take about 15 minutes, and 72% of assigned learners completed at least one each week in Q3 2026.
- "How would I show the leadership team that it worked?": Team-level reports show how scores move, with no individual's conversation shown.

**Next step:** Start an 8-week paid pilot for up to 40 learners. [Sales contact needed]

**Draft notes**

- Proof used: all Public; the first benefit is a product fact.
- Approvals needed: Tom Ferrant, 2 days.

**Assumptions and open questions**

- Unknown: Which sales contact goes on the page?

## How to run it

```
Use the skill "Write a sales one-pager". Read the context pack.
Task: <the segment, the person it is for, and whether use is one-to-one or open>.
```
