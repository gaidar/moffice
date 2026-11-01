---
title: Write a positioning statement
type: skill
function: positioning-and-messaging
owner: product-marketing-manager
reads: [product, icp-and-segments, personas, messaging, competitors, proof-points]
version: 0.1.0
updated: 2026-11-01
summary: Produces a positioning statement for one target, the reasoning behind it and what would break it.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this when you have no positioning statement, enter a new segment, or reach the quarterly positioning review. Do not use it to write pillars and persona messages; use [Build a messaging framework](build-messaging-framework.md) instead. To critique a statement you already have, use [Review messaging](review-messaging.md).

## Inputs

From the context pack:

- [[context-pack:product]] – category, features, limits, weak spots
- [[context-pack:icp-and-segments]] – priority order, situation, triggers
- [[context-pack:personas]] – the champion and their measures
- [[context-pack:messaging]] – the current statement and words to avoid
- [[context-pack:competitors]] – alternatives, the status quo, dated facts
- [[context-pack:proof-points]] – evidence and permission status

The marketer supplies in the prompt: the target segment, if it is not the first priority, and any new evidence, pasted with source and date.

## Procedure

1. Read the Inputs files. If the category, the ICP or the competitors are blank, ask all the questions together before drafting. If the marketer wants a draft anyway, leave a visible placeholder such as [category needed]. Never invent.
2. Pick one target. Use the segment the marketer names, otherwise the first in the priority order in icp-and-segments.md. If there is no priority order, ask. Use the persona marked as the champion in personas.md, or ask if none is marked.
3. List the alternatives: every competitor in competitors.md plus the status quo. A pasted competitor claim with no source and date stays out and is listed as unknown.
4. For each alternative, write what the product does that the alternative does not. Keep a difference only if product.md lists the capability, competitors.md backs the gap with "Where they lose" or a dated fact, and the difference does not touch "What it is not" or "Known weak spots".
5. Turn each difference into one value tied to what the target persona is measured on. Drop differences that reach no measure and keep at most 4 values.
6. Score each value out of 3, one point each: it has proof with status Public in proof-points.md, it answers a situation or trigger in icp-and-segments.md, and competitors.md records no alternative that can also claim it. Pending and None items count as no proof. So does proof found only in messaging.md, which also goes under unknowns.
7. Choose the lead value: the highest score. Break a tie with the value closest to the first item the persona is measured on. If the top score is 1, say under "What would break it" that the position is weak.
8. Take the category from product.md. Propose another only if the marketer asks.
9. Write the statement in the exact form shown in the template. The reason to believe must be a fact from product.md. Use at most two "Unlike" sentences, choosing the alternatives whose differences rest on dated facts first.
10. Write the one-sentence description with no competitor names. Reuse the current one if it still fits the lead value.
11. Fill in the reasoning table and name the segments and buyer types the statement gives up.
12. Name up to 3 things that would make the statement false or weak: a missing permission, a competitor change, a known weak spot.
13. Compare with the current statement. Same target and lead value: write "Keep the current statement" and list wording edits only. Otherwise say what changed and why. If there is none, write "No current statement".
14. Check the draft against the context pack: no claim crosses "What it is not", no word comes from "words to avoid", every competitor claim has a source and date, and only Public proof appears as public. Fix what fails.
15. List everything you assumed, inferred or could not find in the last section, each with its label.

## Output format

```
Status: Draft

## Positioning statement
For <target persona at target company type> who <situation>, <product> is <category> that <lead value>, because <reason to believe>. Unlike <alternative>, it <difference>. Unlike <alternative>, it <difference>.
(80 words at most)

## One-sentence description
<15 words at most>

## Reasoning
| Value | Beats | Proof and permission | Score |
(4 rows at most, cells 15 words at most)
Why this value leads: <30 words at most>
Who this gives up: <30 words at most>

## What would break it
- <3 items at most, 20 words each>

## Change from the current statement
<40 words at most>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the statement name one target, not several?
- [ ] Is the reason to believe a fact from the product file, not a hope?
- [ ] Could a named alternative not honestly say the same thing?
- [ ] Does every proof item show its permission status, with nothing pending or unapproved counted as proof?
- [ ] Does the statement stay clear of "What it is not" and "Known weak spots"?
- [ ] Does it say who the statement gives up?

## Example (fictional company)

Status: Draft

**Positioning statement**

For heads of learning at professional services firms who worry that junior staff accept AI answers without checking them, CogniATion Coach is critical thinking training software that shows whether people's reasoning improves, because it scores reasoning against a five-point rubric and reports progress by team. Unlike Deliberon, it is practice, not a course. Unlike Arguvia, it uses the customer's own scenarios and reports to the learning leader.

**One-sentence description**

CogniATion Coach makes people practice reasoning and shows learning leaders what improved.

**Reasoning**

| Value | Beats | Proof and permission | Score |
|---|---|---|---|
| See reasoning improve | Deliberon, Arguvia | Brightmere 22% result: Public | 3 |
| Asks, does not answer | Status quo | Lena Marsh quote: Public | 2 |
| People keep practicing | Status quo | 72% practice weekly: Public | 1 |

Why this value leads: the champion is measured on proof that training changed behavior, and this scores highest.

Who this gives up: software and financial services as lead targets, and buyers wanting one course library.

**What would break it**

- Deliberon adds reports on reasoning, removing the difference.
- Brightmere withdraws approval, leaving no Public reasoning result.
- Managers' requests for reports below team level start to block deals.

**Change from the current statement**

Narrowed to professional services. Leads with visible progress, not practice.

**Assumptions and open questions**

- Assumption: professional services is the target, as first in the priority order.
- Inference: visible progress leads, from the champion's measures and the scores above.
- Inference: Arguvia's debate practice could also claim questioning and practice, costing those values a point.
- Unknown: Do Deliberon's reports show more than completion data and quiz scores?

## How to run it

```
Use the skill "Write a positioning statement". Read the context pack.
Task: <what they want>.
```
