---
title: Audit the tool stack
type: skill
function: marketing-ops
owner: marketing-operations-manager
reads: [channels-and-tools, goals-and-kpis, company]
you_bring: Each tool's annual cost, renewal date, seats paid for and used, and when it was last used.
also_for: [too many tools, tool costs, software renewals, martech audit, cut software spend, what tools do we need, unused seats, crm renewal]
version: 0.1.0
updated: 2026-11-01
summary: Gives each marketing tool a keep, fix or cut decision, using costs and usage the marketer supplies.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this before a renewal, during budget planning, or when you suspect you are paying for tools nobody opens. Do not use it to split program money across channels, which belongs to [Allocate the budget](../budget-and-planning/allocate-budget.md), or to fix tagging and naming, which belongs to [Set tracking conventions](set-tracking-conventions.md).

## Inputs

- [[context-pack:channels-and-tools]]: tools by job, who has access, hard rules and approval limits.
- [[context-pack:goals-and-kpis]]: KPI list and definitions that depend on a tool, plus the budget.
- [[context-pack:company]]: team size, for judging seat counts.

The marketer pastes into the chat, for each tool:

- Annual cost, renewal date and notice period.
- Seats paid for and seats used, or the plan tier and actual usage.
- When it was last used, and any known problem.
- Whether its cost comes from the marketing budget.

## Procedure

1. List every tool from channels-and-tools.md and every tool the marketer adds. If the two lists differ, include both and flag the difference. If a tool's cost is missing, write [cost needed] and leave it out of the money totals.
2. For each tool, write what depends on it: any KPI it reports, any definition that needs its data and any hard rule that needs it. Write "nothing" if nothing does.
3. Give each tool one decision by applying these rules in order, and stop at the first that fits. Something depends on it and the marketer reports a problem: Fix. Something depends on it and no problem is reported: Keep. Nothing depends on it, and another listed tool does the same job or it has gone unused for 90 days: Cut. Nothing depends on it and it is in use: Keep, and review at renewal.
4. Change a Keep to Fix when paid seats or the plan tier exceed actual usage. The fix is to drop seats or tier at renewal.
5. If usage or last-used information is missing for a tool, do not decide. Write "no decision" and ask for it in the last section. The 90-day cutoff is a starting rule the marketer can change, not a benchmark.
6. For each Cut and Fix, write the steps: what to do, what breaks or moves, who else must agree and the last date to act, which is the renewal date minus the notice period. Anyone with access to the tool in channels-and-tools.md must be told. Do not name replacement products or describe a vendor's features.
7. Calculate the money: total annual cost, savings from cuts and savings from fixes. Savings start at renewal, so show first-year savings only for the months left after that date. Compare with the budget only if the marketer confirmed the cost comes from it, and show the division.
8. List gaps: any KPI with no tool to report it, and any job with no tool. State the gap only. Do not recommend a purchase.
9. Check the draft against the context pack: no Cut removes a tool that a KPI, definition or hard rule needs, and anything above the budget approval limit in channels-and-tools.md names that approver. If a needed field is blank, leave a visible placeholder and ask in the last section. Never invent.
10. List every assumption, estimate, inference and unknown in the last section, including each cost you did not receive.

## Output format

```
Status: Draft

## Bottom line
<Number of tools to keep, fix and cut, and annual savings. Max 30 words.>

## Decisions
| Tool | Annual cost | Depends on it | Decision | Reason |
<One row per tool. Decision is keep, fix, cut or no decision. Reason max 15 words.>

## Steps for cuts and fixes
| Tool | Step | Who must agree | Last date to act |
<One row per cut or fix.>

## Money
<Total annual cost, annual savings, first-year savings. Max 40 words.>

## Gaps
<Up to 3 bullets, max 20 words each, or "None".>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every tool in channels-and-tools.md have a row?
- [ ] Do the decisions follow the rules in order?
- [ ] Does each cut leave every KPI, definition and hard rule still served?
- [ ] Is every cost supplied by the marketer or left as a placeholder?
- [ ] Does each cut or fix show a last date to act and who must agree?
- [ ] Do first-year savings start at the renewal date?
- [ ] Is the output free of named replacement products?

## Example (fictional company)

Status: Draft

Assumption: all of CogniATion's costs, dates and usage are illustrative, as if pasted by the marketer on November 1, 2026. The survey tool is an illustrative addition.

**Bottom line**

Keep 4, fix 1, cut 1, no decision on 1. Annual savings of $4,200.

**Decisions**

| Tool | Annual cost | Depends on it | Decision | Reason |
|---|---|---|---|---|
| CRM | $14,000 | Pipeline, SQLs | Keep | Works |
| Marketing automation and email | $9,600 | MQLs | Fix | Plan is 10,000 contacts, list is 5,400 |
| Web analytics | $0 | Organic visits, ad tracking limit | Keep | Works |
| Webinar | $2,400 | MQL definition | Keep | Works |
| CMS | $3,000 | Website | Keep | Works |
| Design | [cost needed] | Nothing | No decision | Freelancer's own tools |
| Survey tool | $1,800 | Nothing | Cut | Unused for six months |

**Steps for cuts and fixes**

| Tool | Step | Who must agree | Last date to act |
|---|---|---|---|
| Marketing automation and email | Drop contact tier | Marketer | February 1, 2027 |
| Survey tool | Export results, cancel | Marketer | December 1, 2026 |

**Money**

Total $30,800 before the fix. Annual savings $4,200: $2,400 from the tier, $1,800 from the cut. First-year savings $3,100.

**Gaps**

- Video channel has 25 scenario walkthroughs, but channels-and-tools.md lists no hosting tool.

**Assumptions and open questions**

- Estimate: first-year savings cover 12 months from November 1, 2026: 8 months of the tier ($1,600, March 1 renewal), 10 of the cut ($1,500, January 1 renewal). Notice is one month.
- Unknown: Does the CRM cost come from the marketing or the sales budget?

## How to run it

```
Use the skill "Audit the tool stack". Read the context pack.
Task: <which tools, and the renewal or budget date behind this>.
<paste each tool's costs, renewal dates and usage here>
```
