---
title: Allocate the budget
type: skill
function: budget-and-planning
owner: head-of-marketing
reads: [goals-and-kpis, channels-and-tools, icp-and-segments]
version: 0.1.0
updated: 2026-11-01
summary: Splits program budget across channels with a stated rationale and cut order.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this skill to split a period's program budget across channels and programs, with a reason for each line and an agreed order for cuts. Do not use it to choose goals and bets; use [Write a quarterly plan](write-quarterly-plan.md) first. For the audience, tests and stop rules inside one paid channel, use [Plan a paid campaign](../paid-demand-gen/plan-paid-campaign.md) instead.

## Inputs

- [[context-pack:goals-and-kpis]]: budget for the quarter, marketing goals, dated commitments and other priorities.
- [[context-pack:channels-and-tools]]: current paid spend, limits, hard rules and the approval threshold for budget.
- [[context-pack:icp-and-segments]]: segment priority order, which decides ties.

The marketer pastes into the chat:

- What the budget covers, such as whether it includes salaries, tools and freelancers.
- Committed costs: contracts, deposits and quotes.
- Last period's results by channel: spend, leads and pipeline, if available.
- The quarterly plan, if one exists.

## Procedure

1. Set the total. Copy the budget from goals-and-kpis.md or take it from the prompt. If it is blank, ask for it and stop. If the marketer has not said what the budget covers, assume it is program spend only, and record that.
2. Place committed lines first. A line is committed if a contract or deposit exists, or if it is existing paid spend carried at its current monthly rate times the number of months. Mark committed spend that could still be stopped as "Stoppable".
3. Remove anything barred. Apply the limits and hard rules in channels-and-tools.md. Any ad line needing tracking that is not in place gets the note "no spend until tracking is live", and its money stays in the reserve.
4. Set aside a reserve of 10% of the total. This, and the 10% cap in step 6, are starting rules the marketer can change, not benchmarks.
5. Rate the remaining candidate lines. "Dated" means a goal or event in goals-and-kpis.md depends on it. "Proven" means pasted results show pipeline from it. "Untested" means neither.
6. Fund in this order: Dated lines, then Proven lines from highest pipeline per dollar, then Untested lines, capped together at 10% of the total. When two lines tie, fund the one serving the higher segment in the priority order. Do not use outside benchmarks to rank channels.
7. Price each line. Use a quote or supplied cost if there is one. If not, give a holding amount, label it an estimate and show how you reached it, or write [cost needed]. Never present a holding amount as a quote.
8. Check the arithmetic. Lines plus reserve must equal the total exactly, and shares must add up to 100%. If an amount is left, add it to the reserve. If you are over, cut in the cut order.
9. Write the cut order. Cut the reserve first, then Untested lines, then Proven lines, then Stoppable lines, then Dated lines, then Committed lines. Within a group, cut the lowest pipeline per dollar first, or the smallest line if there are no results. Say what each cut gives up, and show what happens at 10% and 25% less budget.
10. Flag approvals. For each line above the budget threshold in channels-and-tools.md, name the approver and lead time.
11. Check the draft against the context pack: total matches the budget, hard rules respected, every dated commitment funded or flagged as unfunded.
12. List everything you assumed or estimated in the last section, including every holding amount.

## Output format

```
Status: Draft
Period: <period>
Total: <amount> | Covers: <what the budget includes, up to 20 words>

## Allocation
| Line | Amount | Share | Rating | Rationale | Cut rank |
<one row per line, up to 10 rows, reserve included, then a total row; rating is Committed, Stoppable, Dated, Proven, Untested or Reserve; rationale up to 20 words; cut rank 1 is cut first>

## Cut plan
- At 10% less (<amount>): <what is cut and what it gives up, up to 30 words>
- At 25% less (<amount>): <what is cut and what it gives up, up to 30 words>

## Approvals needed
| Line | Approver | Lead time |
<one row per line above the threshold, or "None">

## Not funded
- <item and reason, up to 20 words each, or "None">

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Do the lines and the reserve add up to the exact total?
- [ ] Does every line have a rating and a rationale tied to a goal or to pasted results?
- [ ] Are holding amounts labeled as estimates, with the method shown?
- [ ] Does every line respect the limits and hard rules in the context pack?
- [ ] Is every dated commitment funded, or flagged as unfunded?
- [ ] Does the cut plan add up at both 10% and 25% less?
- [ ] Is each line above the approval threshold flagged with its approver?

## Example (fictional company)

**Status:** Draft

**Period:** Q1 2027

**Total:** $70,000 | **Covers:** program spend, see assumptions

**Allocation**

| Line | Amount | Share | Rating | Rationale | Cut rank |
|---|---|---|---|---|---|
| Search ads | $15,000 | 21% | Stoppable | $5,000 a month, current rate | 3 |
| Professional social network ads | $12,000 | 17% | Stoppable | $4,000 a month, current rate | 2 |
| Professional services campaign | $14,000 | 20% | Dated | Goal due February 15 | 4 |
| Regional conference, March 9 to 11 | $18,000 | 26% | Dated | Named priority, learning and development event | 5 |
| Freelance designer | $4,000 | 6% | Committed | Existing design support | 6 |
| Reserve | $7,000 | 10% | Reserve | Starting rule | 1 |
| Total | $70,000 | 100% | | | |

**Cut plan**

- At 10% less ($7,000): the reserve goes, with no cover for overruns.
- At 25% less ($17,500): the reserve and $10,500 of the $12,000 in social ads.

**Approvals needed:** All lines over $5,000: Marta Ilves, CEO, 3 days.

**Not funded:** Display retargeting, barred by limits.

**Assumptions and open questions**

- Assumption: the budget excludes salaries and tools, includes the designer, and tracking is live on both ad channels.
- Estimate: campaign, conference and designer amounts split the $36,000 left after ads and reserve. They are holding amounts with no quotes behind them.
- Unknown: what is the conference quote, and the designer's rate?
- Unknown: can you paste pipeline by channel? Without it, no line rates as Proven.

## How to run it

```
Use the skill "Allocate the budget". Read the context pack.
Task: split the <period> budget across channels, using the costs and channel results pasted below.
```
