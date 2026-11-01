---
title: Diagnose a pipeline gap
type: skill
function: analytics-and-campaign-evaluation
owner: marketing-analyst
reads: [goals-and-kpis, icp-and-segments, company, channels-and-tools]
you_bring: Your pipeline target, or last quarter's numbers if you have none, plus MQLs, SQLs and pipeline value so far from your CRM.
also_for: [pipeline is behind, pipeline is down, ceo asks why pipeline is down, no pipeline target, why is pipeline low, missing our pipeline target, pipeline shortfall, not enough leads, leads not converting, deal size dropped]
version: 0.1.0
updated: 2026-11-02
summary: Splits a gap against a pipeline target, or last quarter, into volume, conversion and deal size, using numbers you paste, and names the skill to run next.
judge: ["Does the driver match what sales says is happening and if not which one is wrong?", "Is this a one-quarter dip or has the trend been there for months?", "Would the split look different if you read it again in two weeks?", "What is the cheapest thing you could check this week to test the likely cause?"]
show_to: your sales lead, before the CEO, and ask whether the driver matches what they see in deals
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when pipeline is behind target, or down on last quarter, and you need to know where the gap sits. It shows where the gap is, not why. Do not use it to judge one finished campaign; use [Evaluate a campaign](evaluate-campaign.md) instead.

## Inputs

- [[context-pack:goals-and-kpis]]: target, SQL goal, definitions, baselines.
- [[context-pack:icp-and-segments]]: segment priority.
- [[context-pack:company]]: which numbers are internal only.
- [[context-pack:channels-and-tools]]: which tool holds any missing number.

The marketer pastes the read date, then MQLs, SQLs and pipeline value for the period so far, as goals-and-kpis.md defines them. With no target, also last quarter's three numbers. Optional: numbers by segment, MQLs older than 14 days, rejection reasons.

## Procedure

1. Stop and ask if MQLs, SQLs or pipeline value are missing. Do not fill them from baselines.
2. Set the target line. With no target, use last quarter as the line and say so: its MQLs, conversion, deal size and pipeline become the targets. Otherwise, target deal size is the pipeline target divided by the SQL goal, or the average in the pipeline definition, or [deal size needed]. Target conversion is the marketer's rate, or else the baseline MQL to SQL rate. Target MQLs is the pipeline target divided by target conversion and target deal size.
3. For a read before the period ends, scale target MQLs by days elapsed over days in the period (a starting rule). Use the marketer's phasing if given, and name any planned campaign this ignores.
4. Work out the actuals. Conversion is SQLs divided by MQLs. Deal size is pipeline value divided by SQLs, at the value pipeline is counted, not contract value.
5. Split the gap in this order, so the parts add up, and show the arithmetic:
   - Volume: (actual MQLs minus target MQLs) x target conversion x target deal size.
   - Conversion: actual MQLs x (actual conversion minus target conversion) x target deal size.
   - Deal size: actual MQLs x actual conversion x (actual deal size minus target deal size).
6. Mark each part Gap or Ahead, then test it. Recompute conversion on MQLs older than 14 days (a starting rule), since recent ones may have had no first call. If that meets target, mark conversion Lag. If the older count is missing, ask, and call the read provisional. Under 30 MQLs or 10 SQLs (a starting rule), mark the part Too few to call.
7. Name the main driver: the largest part still marked Gap. If it is under 60% of the sum of the negative effects (a starting rule), name the top two and call it Mixed. If nothing is marked Gap, recommend no action.
8. If segment numbers are pasted, name the segment holding most of the driver.
9. Name who to ask why, and one skill to run first:
   - Volume: ask sales which sources dried up. Run [Read attribution](read-attribution.md), then [Write a campaign brief](../campaign-design/write-campaign-brief.md), or [Allocate the budget](../budget-and-planning/allocate-budget.md) if money is the limit.
   - Conversion: ask the head of sales for the last 30 rejected MQLs with reasons. Run [Define the lead handoff](../marketing-ops/define-lead-handoff.md), or [Define the ICP](../segmentation-icp-and-personas/define-icp.md) if they are the wrong companies, or [Write a lead follow-up](../campaign-design/write-lead-follow-up.md) if they wait for first contact.
   - Deal size: ask account executives what changed in recent deals. Run [Analyze wins and losses](../competitive-intelligence/analyze-win-loss.md), or [Build a market segmentation](../segmentation-icp-and-personas/build-market-segmentation.md) if the segment mix moved.
   - Numbers in doubt: [Set tracking conventions](../marketing-ops/set-tracking-conventions.md).
10. Say that the split shows where the gap is, not why. Any cause is an Inference or an Unknown until the person in step 9 answers. See [Three hard situations](../../guides/hard-situations.md#the-ceo-asks-why-pipeline-is-down).
11. Write what to tell the CEO, in two or three plain sentences: the gap, where it is, and what you are checking by when. Offer no unchecked cause.
12. Check the draft against the context pack: definitions, baselines and internal-only numbers.
13. List everything assumed or unknown in the last section.

## Output format

```
Status: Draft
Read date: <date, and day of the period>
Target: <amount and date, or "No target set. Line used: last quarter, <amount>">
Answer: <gap, main driver and the skill to run first, up to 30 words>
What to tell the CEO: <two or three plain sentences>

## The numbers
| Measure | Target to date | Actual | Difference |
<rows: MQLs, conversion, SQLs, deal size, pipeline>

## The split
| Part | Effect | Share of shortfall | Arithmetic | Read |
<rows: volume, conversion, deal size, total; Read is Gap, Ahead, Lag or Too few to call>
Lag check: <conversion on older MQLs against target, or "Not pasted">

By segment: <where the driver sits, or "Not pasted">

## Find out why, then run next
This split shows where the gap is, not why.
Ask: <who, and what to ask>
First: <skill title>, because <reason, up to 20 words>

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Do the three effects add up exactly to the pipeline difference?
- [ ] Is every actual a number the marketer pasted, used as goals-and-kpis.md defines it?
- [ ] Are lag and small samples marked before a driver is named?
- [ ] Is every cause written as an Inference or an Unknown?
- [ ] Does the output name one skill to run first, and why?

## Example (fictional company)

**Status:** Draft

**Read date:** February 14, 2027, day 45 of 90

**Target:** $1.2 million by March 31, 2027

**Answer:** $180,000 behind to date, mainly conversion. Define the lead handoff first.

**What to tell the CEO:** We are $180,000 behind at the halfway point, mostly because fewer MQLs are becoming SQLs. That shows where, not why. I am asking Tom Ferrant for the rejected MQLs and will report back this week.

**The numbers:** MQLs 150 against 173. Conversion 20% against 26%. SQLs 30 against 45. Deal size $14,000 against $13,333. Pipeline $420,000 against $600,000.

**The split**

| Part | Effect | Share | Arithmetic | Read |
|---|---|---|---|---|
| Volume | -$80,000 | 40% | (150 - 173.08) x 26% x $13,333 | Gap |
| Conversion | -$120,000 | 60% | 150 x (20% - 26%) x $13,333 | Gap |
| Deal size | +$20,000 | None | 30 x ($14,000 - $13,333) | Ahead |

Lag check: 30 SQLs from 130 older MQLs is 23%, still under 26%.

**Find out why, then run next**

Ask: Tom Ferrant, head of sales, for the rejected MQLs and reasons.

First: [Define the lead handoff](../marketing-ops/define-lead-handoff.md), because conversion misses target after the lag check.

**Assumptions and open questions**

- Assumption: all actuals are invented. Target conversion is the 26% baseline, on a straight line that ignores the February 15 campaign.
- Estimate: $13,333 is $1.2 million divided by 90 SQLs.

## How to run it

```
Use the skill "Diagnose a pipeline gap". Read the context pack.
Task: split the gap against <target and date> into volume, conversion and deal size, using the numbers pasted below.
```
