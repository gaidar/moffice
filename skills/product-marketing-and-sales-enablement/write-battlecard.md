---
title: Write a battlecard
type: skill
function: product-marketing-and-sales-enablement
owner: product-marketing-manager
reads: [competitors, product, icp-and-segments, personas, messaging, proof-points, channels-and-tools]
you_bring: The competitor's name, today's date, and any new sourced material or lost-deal notes with dates.
also_for: [rival keeps appearing in deals, competitor comes up on calls, sales needs help against a competitor, how to beat a rival, objection handling, competitive sheet, losing to a competitor, talk track]
version: 0.1.0
updated: 2026-11-02
summary: Produces a short internal sheet for sales against one named competitor, using only sourced and dated facts from competitors.md.
judge: ["Could a salesperson find the answer in the ten seconds they have on a call?", "Does it help win on what buyers care about or only list what the competitor lacks?", "Would someone who used to work at this competitor call it fair?", "What should a salesperson say when the buyer already prefers the competitor?"]
show_to: the salesperson who last lost to this competitor, and ask what the card gets wrong
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when sales needs a sheet for deals against one named competitor already in competitors.md. Do not use it to research or update what you know about the competitor; use [Write a competitor profile](../competitive-intelligence/write-competitor-profile.md) instead. For a page a buyer can read, use [Write a sales one-pager](write-sales-one-pager.md).

## Inputs

- [[context-pack:competitors]]: facts with source and date, where they win and lose, our answer.
- [[context-pack:product]]: features, what it is not, known weak spots, price, roadmap rules.
- [[context-pack:icp-and-segments]]: disqualifiers, to know when to walk away.
- [[context-pack:personas]]: objections and who to direct questions to.
- [[context-pack:messaging]]: pillars and words to avoid.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:channels-and-tools]]: approver and hard rules.

The marketer supplies: the competitor's name, today's date, and any new sourced material or lost-deal notes, each with its source and date checked. Work only from what is pasted.

## Procedure

1. Find the competitor in competitors.md. If it is not there and the marketer has pasted nothing, stop and ask for a competitor profile first. For what buyers do today, use the status quo entry and the same template.
2. Copy each known fact with its source and date. Write absences as "not found in [source]", never as "does not have". Give what buyers said as a report, with the count.
3. Mark any fact checked more than 6 months before today's date as Stale and tell sales to verify it before using it. Six months is a starting rule the marketer can change.
4. Use nothing about the competitor from memory, even if you recognize the name. Any claim sales wants but competitors.md does not support goes under Unknown.
5. Write "Where they win" honestly, from competitors.md. Add a "When to walk away" line from the ICP disqualifiers and the competitor's strengths.
6. Write "Where we win": at most 3 lines, each tied to a pillar and to a sourced fact about them. Nothing beyond product.md. List our own weak spots from product.md under "Where we are exposed", with what sales says when asked.
7. Write 3 to 5 questions for sales to ask the buyer, starting from "Our answer" in competitors.md. Each question must point at a gap in the sourced facts, not at a guess.
8. Write at most 3 things the buyer will say, and an answer of at most 30 words each. Use objections from personas.md and the marketer's notes. If there is no basis for an answer, write [answer needed from sales].
9. Choose proof. Use Public and Sales only items, keeping limits such as no logo. Mark each as usable in one-to-one conversations. Internal only, Pending and None never appear. Do not use internal numbers from company.md.
10. If you compare prices, use only prices in product.md and sourced competitor prices, label the math as an estimate, and flag the approver for any pricing mention.
11. If a context pack field is blank, leave a placeholder in square brackets and ask in the last section.
12. Check the draft against the context pack: every competitor line has a source and date, permission status, what the product is not, words to avoid. Add "Internal, sales use only, not for ads or buyers" at the top, because hard rules may ban competitor names in ads.
13. List everything assumed, estimated or unknown in the last section.

## Output format

```
Internal, sales use only, not for ads or buyers
Status: Draft
Competitor: <name and category>
Facts last checked: <latest and oldest date>

## Where they win
<Max 2 lines>

## When to walk away
<Max 2 lines>

## Where we win
<Max 3 lines, each tied to a pillar>

## Where we are exposed
<Max 2 lines, each with what sales says, max 25 words>

## Known facts
| Fact | Source | Date checked | Stale? |

## Questions to ask the buyer
<3 to 5 numbered questions>

## What the buyer will say
| They say | Answer (max 30 words) |

## Proof to use
| Item | Permission | Limit |

## Approval
<Approver and typical time>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every statement about the competitor have a source and a date from competitors.md or the marketer's paste?
- [ ] Are absences written as "not found", not as facts?
- [ ] Is it honest about where they win and where we are exposed?
- [ ] Does it say when to walk away?
- [ ] Is each proof item allowed for one-to-one use, with its limits shown?
- [ ] Is it free of internal numbers and roadmap items?
- [ ] Is it marked as not for ads or buyers, with the approver named?

## Example (fictional company)

Internal, sales use only, not for ads or buyers

**Status:** Draft

**Competitor:** Arguvia, low-cost debate practice chatbot for individuals

**Facts last checked:** October 2026

**Where they win:** Small teams and individuals wanting something today at a low price.

**When to walk away:** Fewer than 100 learners.

**Where we win:** You can see reasoning improve: team reports and custom scenarios, against generic topics and no team reports found.

**Where we are exposed:** Price. Say: "Fine for one person practicing. Ask how they would show leadership that it worked." No reports below team level. Say: "No individual's conversation is on display."

**Known facts**

| Fact | Source | Date checked | Stale? |
|---|---|---|---|
| Lists $9 per user per month | Pricing page | October 2026 | No |
| Generic debate topics only | Help center | October 2026 | No |
| Team reports not found | Help center | October 2026 | No |

**Questions to ask the buyer**

1. How would you show leadership that it worked?
2. Do you need your own scenarios, or will generic topics do?
3. Who needs to see team progress?

**What the buyer will say**

| They say | Answer |
|---|---|
| "It is cheaper." | Yes, $108 per user a year against our $180. Ask what leadership would see. |

**Proof to use**

| Item | Permission | Limit |
|---|---|---|
| "Managers argue about the assumption now, not about who is senior." Sam Oduya, VP engineering, Corvane Software | Sales only | One-to-one, no logo |

**Approval:** Tom Ferrant, 2 days. Anika Sole for the price, 1 day.

**Assumptions and open questions**

- Estimate: $108 is $9 times 12 months. Our $180 excludes the $5,000 setup.
- Unknown: Has Arguvia won where the buyer needed team reports?

## How to run it

```
Use the skill "Write a battlecard". Read the context pack.
Task: <the competitor's name and any new sourced notes, with dates>.
```
