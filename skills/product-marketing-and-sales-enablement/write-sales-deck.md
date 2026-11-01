---
title: Write a sales deck
type: skill
function: product-marketing-and-sales-enablement
owner: product-marketing-manager
reads: [company, product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, channels-and-tools]
you_bring: The segment and buyer role for the first call, and whether the deck stays one-to-one or may be posted.
also_for: [pitch deck, first call slides, talk track, sales presentation, slides for sales, intro deck, what to say on a first call]
version: 0.1.0
updated: 2026-11-02
summary: Writes a first-call deck outline, slide by slide, with a talk track and proof chosen by where the deck will be used, and no design work.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when sales needs slides and a talk track for a first call with one kind of buyer in one segment. Do not use it for a page to hand over; use [Write a sales one-pager](write-sales-one-pager.md) instead. For a named competitor, use [Write a battlecard](write-battlecard.md). For how the slides look, use [Write a design brief](../brand-and-design-briefs/write-design-brief.md).

## Inputs

- [[context-pack:company]]: publishable numbers.
- [[context-pack:product]]: what it does and is not, price, pilot, roadmap rules.
- [[context-pack:icp-and-segments]]: reasons to buy, and triggers.
- [[context-pack:personas]]: daily problem and objections.
- [[context-pack:messaging]]: pillars, persona messages, words to avoid.
- [[context-pack:competitors]]: only what buyers do today, and why they stay.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:brand-voice]]: voice and rules.
- [[context-pack:channels-and-tools]]: approvers and hard rules.

The marketer supplies the segment, the persona, the call length, and the use. One-to-one means sales presents it or sends it to a named buyer. Open means posted online or sent to a list. If not stated, treat it as open use.

## Procedure

1. Choose one segment and one persona. If none is named, ask before drafting. If several are named, ask which comes first. Do not blend them.
2. Set the proof allowed. Open use takes Public items only. One-to-one use takes Public and Sales only items, keeping any limit in the entry, such as no logo. Internal only, Pending and None never appear. Prefer proof from the same segment, then the same persona (a starting rule). The talk track follows the same rule as the slides.
3. Use these 8 slides in order, for a 30-minute call that leaves half the time for the buyer (a starting rule; for a shorter call, cut slide 6 first):
   - 1 Why we are talking: the segment's trigger.
   - 2 The problem: the persona's daily problem, in their words.
   - 3 What you do today: from competitors.md, with no competitor names.
   - 4 What it does: from product.md only.
   - 5, 6 and 7: one pillar each, in the order in messaging.md.
   - 8 Next step: the pilot or trial in product.md, or [next step needed].
4. Write each slide: a headline of at most 10 words, at most 3 lines of at most 12 words each, and a line naming what it shows, such as a report, with [screenshot needed] where one is missing. Give no layout, color or type direction.
5. Write a talk track for each slide in at most 60 words, as a person would say it. It adds to the slide and does not read it out.
6. Add one question about the buyer's situation on slides 1, 2, 3 and 7.
7. Attach proof to slides 5 to 7. If a pillar has no allowed proof, use a product fact and say so, or write a placeholder such as [progress proof needed]. Leave out any number not in proof-points.md or marked publishable in company.md.
8. Write the backup, shown only if asked: up to 3 objections from personas.md in file order, each answered from the context pack, or [answer needed from sales]. Include price only if product.md allows it and the marketer asked, copied as written. Do not promise a feature or mention a roadmap item.
9. Check the draft against the context pack: what the product is not, words to avoid, brand voice, permission status, hard rules, including anything shown in a screenshot.
10. List the approvals from channels-and-tools.md: sales material, any pricing mention, any customer item not yet approved. List everything assumed or unknown in the last section.

## Output format

```
Status: Draft
Segment: <one>
Persona: <one>
Use: <One-to-one or open>
Call length: <minutes>

## Slides
Slide <number>: <slide name>
Headline: <max 10 words>
On the slide: <up to 3 lines, max 12 words each>
Shows: <content only, max 10 words>
Talk track: <max 60 words>
Question: <one, on slides 1, 2, 3 and 7 only>
<repeat for all 8 slides>

## Backup (only if asked)
- <Objection>: <answer, max 25 words>
Price: <as written in product.md, or omit this line>

## Draft notes (not on the slides)
- Proof used: <item, permission status, slide, any limit>
- Left out: <item, and why>
- Approvals needed: <item, approver, typical time>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does it speak to one segment and one persona, in 8 slides?
- [ ] Does every proof item, on a slide or in the talk track, fit the stated use and keep its limits?
- [ ] Is every product statement backed by product.md, with no roadmap items?
- [ ] Are competitor names absent from the slides and the talk track?
- [ ] Is the deck free of layout, color and type direction?
- [ ] Are approvers listed for sales material and any price?

## Example (fictional company)

**Status:** Draft

**Segment:** Professional services firms

**Persona:** Head of learning and development

**Use:** One-to-one

**Call length:** 30 minutes

**Slides** (three of 8 shown)

**Slide 3: What you do today**

Headline: The workshop ends, and nobody knows what changed

On the slide: An annual workshop. Telling staff to check the AI assistant.

Shows: Text only

Talk track: Firms like yours often run a workshop once a year, then ask staff to check what the AI assistant says. It seems free, and earlier training tools went unused.

Question: What happened after your last workshop, and how would you know?

**Slide 7: You can see reasoning improve**

Headline: Show that reasoning improved, team by team

On the slide: Brightmere Advisory: up 22% on client memo reasoning in one quarter. Corvane Software: 2.6 to 3.4 out of 5 in 12 weeks.

Shows: Team-level report, [screenshot needed]

Talk track: Brightmere's partners did the measuring, in 2026. Corvane is a software company, so treat it as a second reference. You see progress by team, never one person's conversation.

Question: What would your partners need to see?

**Slide 8: Next step**

Headline: An 8-week paid pilot for up to 40 learners

**Draft notes**

- Proof used: Brightmere, Public, slide 7. Corvane, Sales only, no logo, slide 7.
- Left out: price, not asked for. Roadmap, not cleared.
- Approvals needed: deck, Tom Ferrant, 2 days.

**Assumptions and open questions**

- Assumption: sales presents this live or sends it to a named buyer.
- Unknown: which team report can sales show?

## How to run it

```
Use the skill "Write a sales deck". Read the context pack.
Task: <the segment, the persona, the call length, and whether use is one-to-one or open>.
```
