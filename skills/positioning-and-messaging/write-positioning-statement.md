---
title: Write a positioning statement
type: skill
function: positioning-and-messaging
owner: product-marketing-manager
reads: [product, icp-and-segments, personas, messaging, competitors, proof-points]
you_bring: The target segment if it is not your first priority, plus any new evidence and customer quotes with source and date.
also_for: [what category are we, we sound like everyone, how are we different, differentiation, explain what we do, why us, new segment positioning, ceo asks what we are]
version: 0.1.0
updated: 2026-11-02
summary: Produces a positioning statement for one target, the reasoning behind it and what would break it.
judge: ["Would a buyer who has never heard of you repeat this to a colleague?", "Could your top competitor say the same sentence?", "Is this why customers really chose you or why you wish they had?", "Which deals would you now walk away from because of this and would your CEO accept that?"]
show_to: your sales lead, and ask which line a buyer would argue with
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when you have no positioning statement, enter a new segment, or reach the quarterly positioning review. Do not use it to write pillars and persona messages; use [Build a messaging framework](build-messaging-framework.md) instead.

## Inputs

- [[context-pack:product]]: category, features, limits, weak spots
- [[context-pack:icp-and-segments]]: priority order, situation, triggers
- [[context-pack:personas]]: the champion and their measures
- [[context-pack:messaging]]: the current statement and words to avoid
- [[context-pack:competitors]]: alternatives, the status quo, dated facts
- [[context-pack:proof-points]]: evidence and permission status

The marketer supplies: the target segment, if not the first priority, and new evidence and customer quotes, with source and date.

## Procedure

1. If the category, the ICP or the competitors are blank, ask before drafting. If the marketer wants a draft anyway, leave a visible placeholder such as [category needed]. Never invent.
2. Pick one target. Use the segment the marketer names, otherwise the first in the priority order in icp-and-segments.md, or ask. Use the champion in personas.md, or ask.
3. List the alternatives: every competitor in competitors.md plus the status quo. A pasted competitor claim with no source and date stays out and is listed as unknown.
4. For each alternative, write what the product does that the alternative does not. Keep a difference only if product.md lists the capability, competitors.md backs the gap with "Where they lose" or a dated fact, and the difference does not touch "What it is not" or "Known weak spots".
5. Turn each difference into one value tied to what the target persona is measured on. Drop differences that reach no measure and keep at most 4 values.
6. Score each value out of 3, one point each: it has proof with status Public in proof-points.md, it answers a situation or trigger in icp-and-segments.md, and competitors.md records no alternative that can also claim it. Pending and None items count as no proof. So does proof found only in messaging.md.
7. Choose the lead value: the highest score. Break a tie with the value closest to the first item the persona is measured on. If the top score is 1, say under "What would break it" that the position is weak.
8. Compare two or three categories: product.md's plus others buyers use, from competitors.md or customer words. Say what buyers would compare each with and whether the lead value wins there. Keep product.md's unless another fits better, and say why.
9. Write the statement in the exact form shown in the template. The reason to believe must be a fact from product.md. Use at most two "Unlike" sentences, favoring differences that rest on dated facts.
10. Write the one-sentence description with no competitor names.
11. Fill in the reasoning table and name the segments and buyer types the statement gives up.
12. Name up to 3 things that would make it false or weak, such as a missing permission.
13. Mark the result Hypothesis if no customer quote, in proof-points.md or pasted notes, backs the lead value and the category.
14. Compare with the current statement. Same target and lead value: write "Keep the current statement" and list wording edits only. Otherwise say what changed and why. If there is none, write "No current statement".
15. Check the draft against the context pack: no claim crosses "What it is not", no word comes from "words to avoid", every competitor claim has a source and date, and only Public proof appears as public.
16. List everything you assumed, inferred or could not find in the last section, each with its label.

## Output format

```
Status: Draft
Evidence: <"Backed by" and the quotes, or "Hypothesis" and what is missing>

## Category comparison
| Category | Compared with | Lead value wins? |
(2 or 3 rows)

## Positioning statement
For <target persona at target company type> who <situation>, <product> is <category> that <lead value>, because <reason to believe>. Unlike <alternative>, it <difference>. Unlike <alternative>, it <difference>.
(max 80 words)

## One-sentence description
<max 15 words>

## Reasoning
| Value | Beats | Proof and permission | Score |
(max 4 rows, cells max 15 words)
Why this value leads: <max 30 words>
Who this gives up: <max 30 words>

## What would break it
- <max 3 items, 20 words each>

## Change from the current statement
<max 40 words>

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
- [ ] Does it say who the statement gives up?
- [ ] Were categories compared, and is the result marked Hypothesis if no customer quote backs it?

## Example (fictional company)

Status: Draft

Evidence: Hypothesis. The lead value rests on a measured result, and no customer quote names this category.

**Category comparison**

| Category | Compared with | Lead value wins? |
|---|---|---|
| Critical thinking training software | Elenchly | Yes |
| Course library | Elenchly | No, buyers expect courses |

**Positioning statement**

For heads of learning at professional services firms who worry that junior staff accept AI answers without checking them, CogniATion Coach is critical thinking training software that shows whether people's reasoning improves, because it scores reasoning against a five-point rubric and reports progress by team. Unlike Elenchly, it is practice, not a course. Unlike Arguvia, it uses the customer's own scenarios and reports to the learning leader.

**One-sentence description**

CogniATion Coach makes people practice reasoning and shows learning leaders what improved.

**Reasoning**

| Value | Beats | Proof and permission | Score |
|---|---|---|---|
| See reasoning improve | Elenchly, Arguvia | Brightmere 22% result: Public | 3 |
| Asks, does not answer | Status quo | Lena Marsh quote: Public | 2 |

Why this value leads: the champion is measured on proof that training changed behavior, and this scores highest.

Who this gives up: software and financial services, and buyers wanting one course library.

**What would break it**

- Elenchly adds reports on reasoning, removing the difference.
- Brightmere withdraws approval, leaving no Public reasoning result.

**Change from the current statement**

Narrowed to professional services. Leads with visible progress, not practice.

**Assumptions and open questions**

- Assumption: professional services is the target, as first in the priority order.
- Unknown: Do Elenchly's reports show more than completion data and quiz scores?

## How to run it

```
Use the skill "Write a positioning statement". Read the context pack.
Task: <the target segment, if not the first priority>.
<paste new evidence and customer quotes here>
```
