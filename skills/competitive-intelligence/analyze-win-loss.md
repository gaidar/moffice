---
title: Analyze wins and losses
type: skill
function: competitive-intelligence
owner: product-marketing-manager
reads: [competitors, icp-and-segments, product, messaging, goals-and-kpis]
version: 0.1.0
updated: 2026-11-01
summary: Finds patterns across won and lost deals from a pasted CRM export and call notes, and tests the context pack against them.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this at the quarterly review, or after a run of unexpected losses, when you can paste a CRM export of closed deals. Do not use it for interviews or surveys with no deal outcomes; use [Synthesize customer research](../segmentation-icp-and-personas/synthesize-customer-research.md) instead. For one competitor's facts, use [Write a competitor profile](write-competitor-profile.md).

## Inputs

From the context pack:

- [[context-pack:competitors]] – where each wins and loses, the status quo
- [[context-pack:icp-and-segments]] – fit criteria, disqualifiers, segments
- [[context-pack:product]] – limits and weak spots, to sort product gaps
- [[context-pack:messaging]] – the pillars to test
- [[context-pack:goals-and-kpis]] – the SQL definition and the SQL to won baseline

The marketer supplies in the prompt: a CRM export pasted as text, with one row per deal, and call notes marked with the deal ID. The export needs deal ID, outcome and close date. Segment, competitor, stated reason and amount make the analysis better. Remove contact names first if your company's rules require it.

## Procedure

1. Check the export. If deal ID, outcome or close date is missing, ask for it and stop. List any other missing column as an unknown and skip the cuts that need it. Never fill in a value.
2. Clean the data: remove duplicates and open deals, and keep only deals that meet the SQL definition in goals-and-kpis.md. If the export cannot show that, keep all closed deals and record it as an assumption.
3. Sort every deal into Won, Lost to a named competitor, or No decision. A deal lost to the buyer's current approach counts as No decision, with the status quo noted.
4. Code each lost and no-decision deal with one reason: Product gap, Price, Implementation effort, Competitor strength, Timing, Status quo, Not ICP or Unknown. Code a blank or vague reason as Unknown.
5. Read the call notes. Where they contradict the CRM reason, use the reason in the notes and count the disagreement in the data summary.
6. Mark each deal as ICP fit or not, using the criteria and disqualifiers in icp-and-segments.md. If the data cannot show it, mark it Unknown.
7. Build the cuts, in this order, with what the data allows: by segment, by competitor, by reason, by ICP fit, by deal size. Report counts. Show a percentage only for a group of 20 or more closed deals.
8. Write patterns. A pattern has at least 3 deals, with a call note on at least one. Anything less is an observation. The 3-deal and 20-deal cutoffs are starting rules the marketer can change. State each as "N of M deals", and name the deal IDs. Say "because" only if a buyer said so. Otherwise label it an inference.
9. Test the context pack: for each pillar and each competitor's "Where they win" and "Where they lose", write Holds, Challenged or No data, with the pattern or deals behind it.
10. Recommend up to 5 actions, based on patterns only. Each names the change, the agent role that owns it and the skill to run. Observations get one action: what data to collect next.
11. Check the draft against the context pack: competitor statements match competitors.md or a cited call note, and definitions match goals-and-kpis.md. Compare with the SQL to won baseline only if the denominators match. Mark deal names and quotes internal.
12. List everything you assumed, inferred or could not find in the last section, each with its label.

## Output format

```
Status: Draft

## Bottom line
<60 words at most: what the deals say and the single most important action>

## Data summary
Period: <dates>. Closed deals: <n>. Won: <n>. Lost to a named competitor: <n>. No decision: <n>.
Reason unknown: <n>. CRM reason contradicted by notes: <n>. Not ICP: <n>.

## Cuts
| Cut | Won | Lost | No decision |
(one table, one row per group, percentages only for groups of 20 or more)

## Patterns
1. <Pattern, N of M deals, deal IDs, evidence. 40 words at most. 5 patterns at most>

## Observations
- <Fewer than 3 deals. 20 words at most each. 5 items at most, or None>

## Context pack test
| Item | Holds, Challenged or No data | Evidence |

## Recommended actions
1. <Change, owning agent role, skill to run. 25 words at most. 5 actions at most>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Do the deal counts add up to the closed total?
- [ ] Are open deals out, and no-decision deals apart from losses?
- [ ] Are blank reasons coded Unknown, not guessed?
- [ ] Does every pattern have at least 3 deals and named deal IDs?
- [ ] Are percentages limited to groups of 20 or more?
- [ ] Is each causal claim backed by a buyer's words, or labeled an inference?
- [ ] Does each action trace to a pattern and name a skill?
- [ ] Are deal names and quotes marked internal?

## Example (fictional company)

Status: Draft

**Bottom line**

In this invented deal set, most losses went to Arguvia on price at software companies, or to Deliberon from buyers wanting a course library. Screen for that disqualifier earlier.

**Data summary**

Assumption: all counts are invented, because the context pack holds no CRM export.

Period: Q3 2026. Closed deals: 24. Won: 9. Lost to a named competitor: 10. No decision: 5. Reason unknown: 3. CRM reason contradicted by notes: 2. Not ICP: 3.

**Cuts**

| Cut | Won | Lost | No decision |
|---|---|---|---|
| Professional services | 5 | 3 | 1 |
| Financial services | 3 | 2 | 1 |
| Software companies | 1 | 5 | 3 |

**Patterns**

1. 4 of 6 losses to Arguvia were software company deals citing price (D3, D7, D12, D19).
2. 3 of 4 losses to Deliberon wanted a course library, an ICP disqualifier (D5, D14, D21).

**Observations**

- 2 no-decision deals kept an annual workshop, saying earlier tools went unused.
- 1 financial services deal ended with no decision during its security review.

**Context pack test**

| Item | Result | Evidence |
|---|---|---|
| Deliberon "Where they win" | Holds | Pattern 2 |
| Pillar 3 | No data | No deal mentions team reports |

**Recommended actions**

1. Screen for the course library disqualifier before SQL, marketing operations manager, Define the lead handoff.

**Assumptions and open questions**

- Assumption: all deals, IDs and counts above are invented.
- Inference: both patterns rest on that set and competitors.md.
- Unknown: Do call notes exist for the won deals?

## How to run it

```
Use the skill "Analyze wins and losses". Read the context pack.
Task: <what they want>.
```
