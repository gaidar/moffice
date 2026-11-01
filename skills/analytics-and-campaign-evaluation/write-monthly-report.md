---
title: Write the monthly report
type: skill
function: analytics-and-campaign-evaluation
owner: marketing-analyst
reads: [goals-and-kpis, channels-and-tools, company]
you_bring: The month's actual for each KPI, quarter-to-date totals, spend by channel, and who will read the report.
also_for: [monthly report, board update, ceo update, report to leadership, month end numbers, are we on track, pipeline vs goal, marketing performance]
version: 0.1.0
updated: 2026-11-02
summary: Reports one closed month against goals-and-kpis.md, with short commentary and the decisions it calls for.
judge: ["If the CEO reads only the headline will they know what to do differently?", "Is one month enough to call this a trend or is it noise?", "Which number here are you hoping nobody asks about?", "What decision would change if this report were never written?"]
show_to: your CEO or manager, and ask which decision it helps them make
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this once a month, after the month has closed and you can pull its numbers. Do not use it to judge one campaign, which belongs to [Evaluate a campaign](evaluate-campaign.md), or to set the coming week's work, which belongs to [Set weekly priorities](../budget-and-planning/set-weekly-priorities.md).

## Inputs

- [[context-pack:goals-and-kpis]]: quarterly goals, definitions, KPI baselines and review cadence.
- [[context-pack:channels-and-tools]]: planned paid spend by channel.
- [[context-pack:company]]: which numbers are publishable, internal only or never to be mentioned.

The marketer pastes into the chat:

- The month being reported, and who will read the report.
- The month's actual for each KPI, plus quarter-to-date totals for each goal.
- Actual spend by channel, and planned spend if it differs from the context pack.
- Events that moved the numbers, such as a tracking gap, a launch or a staffing change.

## Procedure

1. Write one KPI row for every KPI in goals-and-kpis.md. Report KPIs reviewed weekly or monthly as the month's figure. Report a KPI reviewed quarterly only in the last month of a quarter, and otherwise write "next quarterly review". If an actual is missing, write [actual needed]. Never estimate an actual.
2. Convert baselines to a monthly figure. Divide a count or dollar baseline from a full quarter by 3 and label it an estimate. Compare rates directly, without dividing.
3. Write one goal row for every quarterly goal. Pace to date is the goal multiplied by months elapsed, divided by 3. For a dated goal that is not a number, such as a campaign publish date, use the marketer's status or write [status needed].
4. Set each numeric goal's status from actual divided by pace. "On pace" is 100% or more, "at risk" is 80% to 99%, and "off pace" is below 80%. These cutoffs and the 10% in step 7 are starting rules the marketer can change, not benchmarks.
5. Fill the spend table. Difference is actual minus planned.
6. Write the headline last, and put it first in the output. It names the goal furthest behind pace and the number that shows it. If every goal is on pace, it names the goal with the smallest margin.
7. Write commentary only for goals at risk or off pace, and for KPIs that differ from their monthly baseline by more than 10%. Explain a change only from what the marketer supplied. Label any explanation you worked out yourself as an inference, and otherwise write [reason not supplied].
8. Write up to 3 decisions the numbers call for. Each names the choice, your recommendation and the date it must be made by. Write "None this month" if no goal is at risk or off pace and no spend line is over plan.
9. Check the draft against the context pack: definitions match goals-and-kpis.md, and no number marked "never mention" in company.md appears. Mark the report "Internal" at the top if it holds any internal-only number. If it will go outside the company, use only publishable numbers. If a needed field is blank, leave a visible placeholder and ask in the last section. Never invent.
10. List every assumption, estimate, inference and unknown in the last section, including each baseline you divided and the date the numbers were pulled.

## Output format

```
Status: Draft

## Headline
<Audience marking, month, the goal furthest behind pace and its number. Max 50 words.>

## Goals
| Goal | Target | To date | Pace to date | Status |
<One row per quarterly goal. Status is on pace, at risk or off pace.>

## KPIs
| KPI | Month actual | Monthly baseline | Difference |
<One row per KPI in goals-and-kpis.md.>

## Spend
| Channel | Planned | Actual | Difference |
<One row per paid channel, then a total.>

## Commentary
<Up to 4 bullets, max 30 words each.>

## Decisions needed
| Decision | Recommendation | Decide by |
<Up to 3 rows, or "None this month".>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every KPI and quarterly goal in goals-and-kpis.md have a row?
- [ ] Does the headline name the goal furthest behind pace, with its number?
- [ ] Is every status set by the pace rule rather than by feel?
- [ ] Is every divided baseline labeled an estimate?
- [ ] Is every explanation either supplied by the marketer or labeled an inference?
- [ ] Is every number's audience correct under company.md?
- [ ] Does each decision have a recommendation and a date?

## Example (fictional company)

Status: Draft

Assumption: all of CogniATion's January 2027 actuals are illustrative, as if pasted by the marketer. Marked Internal because company.md does not list pipeline or SQLs as publishable.

**Headline**

Internal. January 2027: pipeline is the goal furthest behind, at $352,000 against a pace of $400,000.

**Goals**

| Goal | Target | To date | Pace to date | Status |
|---|---|---|---|---|
| Pipeline | $1.2 million | $352,000 | $400,000 | At risk (88%) |
| SQLs | 90 | 27 | 30 | At risk (90%) |
| Professional services campaign | February 15, 2027 | [status needed] | n/a | [status needed] |

**KPIs**

| KPI | Month actual | Monthly baseline | Difference |
|---|---|---|---|
| MQLs | 97 | 87 | +10 |
| MQL to SQL rate | 28% | 26% | +2 points |
| Website demo requests | 21 | 19 | +2 |

**Spend**

| Channel | Planned | Actual | Difference |
|---|---|---|---|
| Search ads | $5,000 | $5,200 | +$200 |
| Social network ads | $4,000 | $4,000 | $0 |
| Total | $9,000 | $9,200 | +$200 |

**Commentary**

- MQLs beat the baseline by 10, yet 90 SQLs still needs about 107 MQLs a month at this rate.

**Decisions needed**

| Decision | Recommendation | Decide by |
|---|---|---|
| Add a late March webinar for heads of learning? | Yes, MQL volume is the gap | February 5, 2027 |

**Assumptions and open questions**

- Assumption: other KPIs are left out here, condensed for length.
- Estimate: monthly baselines are Q3 2026 figures divided by 3. Pace is the goal divided by 3. MQL need is 90 / 0.28 / 3.
- Unknown: Why did search ads run $200 over plan?

## How to run it

```
Use the skill "Write the monthly report". Read the context pack.
Task: <the month, who will read it, and what moved the numbers>.
<paste the KPI actuals and spend here>
```
