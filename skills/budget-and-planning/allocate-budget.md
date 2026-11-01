---
title: Allocate the budget
type: skill
function: budget-and-planning
owner: head-of-marketing
reads: [goals-and-kpis, channels-and-tools, icp-and-segments, personas]
you_bring: What the budget covers, your committed costs, and last period's results by channel if you have any.
also_for: [budget was cut, where to spend, marketing budget split, channel mix, no past results, how much for ads, new budget, pipeline per dollar]
version: 0.1.0
updated: 2026-11-02
summary: Splits program budget across channels with a stated rationale and cut order.
judge: ["Is the largest line there because it earned it or because it was largest last quarter?", "Is any line too small to produce a result you could even measure?", "What would you need to see in 60 days to move money between lines?", "Which line are you funding only because stopping it would be awkward?"]
show_to: whoever approves spend, often the CEO, and ask which line they would question first
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this to split a period's program budget across channels, with a reason for each line and a cut order. Do not use it to choose goals and bets; use [Write a quarterly plan](write-quarterly-plan.md) first. For the plan inside one paid channel, use [Plan a paid campaign](../paid-demand-gen/plan-paid-campaign.md) instead.

## Inputs

- [[context-pack:goals-and-kpis]]: budget, goals, dated commitments, other priorities.
- [[context-pack:channels-and-tools]]: paid spend, limits, hard rules, approval threshold.
- [[context-pack:icp-and-segments]]: segment priority order, which decides ties.
- [[context-pack:personas]]: where buyers get information.

The marketer pastes:

- What the budget covers, such as salaries, tools and freelancers.
- Committed costs: contracts, deposits and quotes.
- Last period's results by channel: spend, leads and pipeline, if available.
- The quarterly plan, if one exists.

## Procedure

1. Set the total. Take the budget from goals-and-kpis.md or the prompt. If it is blank, ask for it and stop. If the marketer has not said what the budget covers, assume program spend only, and record that.
2. Place committed lines first. A line is committed if a contract or deposit exists, or if it is existing paid spend carried at its current rate for the period. Mark committed spend that could still be stopped as "Stoppable".
3. Remove anything barred. Apply the limits and hard rules in channels-and-tools.md. Any ad line needing tracking that is not in place gets the note "no spend until tracking is live", and its money stays in the reserve.
4. Set aside a reserve of 10% of the total. This and the 10% and 40% caps in step 6 are starting rules the marketer can change, not benchmarks.
5. Rate the remaining candidate lines. "Dated" means a goal or event in goals-and-kpis.md depends on it. "Proven" means pasted results show pipeline from it. "Untested" means neither.
6. Fund in this order: Dated lines, then Proven lines from highest pipeline per dollar, then Untested lines, capped together at 10% of the total. Cap any line at 40% of the total. Flag a signed contract above that. Break ties toward the higher segment in the priority order. Do not use outside benchmarks to rank channels.

   No history: if no results were pasted and over half the total is still unfunded after Committed and Dated lines, drop the 10% cap. Fund channels reaching where personas.md says buyers get information, most-named first. Rate them Hypothesis: a bet to test, not evidence.

7. Price each line. Use a quote or supplied cost if any. If not, give a holding amount, label it an estimate and show how you reached it, or write [cost needed].
8. Check the arithmetic. Lines plus reserve must equal the total exactly, and shares must add up to 100%. If an amount is left, add it to the reserve. If you are over, cut in the cut order.
9. Write the cut order. Cut the reserve first, then Untested and Hypothesis lines, then Proven lines, then Stoppable lines, then Dated lines, then Committed lines. Within a group, cut the lowest pipeline per dollar first, or the smallest line if there are no results. Say what each cut gives up, and show what happens at 10% and 25% less budget.
10. Flag approvals: the approver and lead time for each line above the threshold in channels-and-tools.md.
11. Check the draft against the context pack: total matches the budget, hard rules respected, every dated commitment funded or flagged as unfunded.
12. List everything you assumed or estimated in the last section, including every holding amount.

## Output format

```
Status: Draft
Period: <period>
Total: <amount> | Covers: <what the budget includes, up to 20 words>

## Allocation
| Line | Amount | Share | Rating | Rationale | Cut rank |
<one row per line, up to 10 rows, reserve included, then a total row; rating is Committed, Stoppable, Dated, Proven, Untested, Hypothesis or Reserve; rationale up to 20 words; cut rank 1 is cut first>

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
- [ ] Does every line have a rating and a rationale tied to a goal, pasted results or, for Hypothesis, personas.md?
- [ ] Is every line at or under 40% of the total, or flagged?
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
| Search ads | $15,000 | 21% | Stoppable | $5,000 a month | 3 |
| Professional social network ads | $12,000 | 17% | Stoppable | $4,000 a month | 2 |
| Professional services campaign | $14,000 | 20% | Dated | Goal due February 15 | 4 |
| Regional conference, March 9 to 11 | $18,000 | 26% | Dated | Named priority | 5 |
| Freelance designer | $4,000 | 6% | Committed | Existing design support | 6 |
| Reserve | $7,000 | 10% | Reserve | Starting rule | 1 |
| Total | $70,000 | 100% | | | |

**Cut plan**

- At 10% less ($7,000): the reserve goes.
- At 25% less ($17,500): the reserve and $10,500 of the $12,000 in social ads.

**Approvals needed:** All lines over $5,000: Marta Ilves, CEO, 3 days.

**Not funded:** Display retargeting, barred by limits.

**Assumptions and open questions**

- Assumption: the budget excludes salaries and tools, includes the designer, and tracking is live on both ad channels.
- Estimate: campaign, conference and designer are holding amounts, splitting the $36,000 left after ads and reserve.
- Unknown: what is the conference quote, and the designer's rate?
- Unknown: can you paste pipeline by channel?

## How to run it

```
Use the skill "Allocate the budget". Read the context pack.
Task: <the period and what the budget covers>.
<paste committed costs and results by channel here>
```
