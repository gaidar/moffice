---
title: Set weekly priorities
type: skill
function: budget-and-planning
owner: head-of-marketing
reads: [goals-and-kpis, channels-and-tools, company]
you_bring: Last week's numbers, what is due in the next two weeks, what slipped, and the days you have this week.
also_for: [what should i do this week, too much to do, weekly plan, what to drop, overloaded, pipeline behind, monday planning, to do list]
version: 0.1.0
updated: 2026-11-01
summary: Top three priorities and a do-not-do list from last week's numbers and plan.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this skill at the start of each week to pick up to three priorities and a do-not-do list, from last week's numbers and the plan. Do not use it to set the quarter's direction; use [Write a quarterly plan](write-quarterly-plan.md) instead. For the month's numbers and commentary, use [Write the monthly report](../analytics-and-campaign-evaluation/write-monthly-report.md).

## Inputs

- [[context-pack:goals-and-kpis]]: marketing goals, KPI baselines, which KPIs are reviewed weekly, and other priorities.
- [[context-pack:channels-and-tools]]: limits, hard rules, approvers and approval times.
- [[context-pack:company]]: the size of the team.

The marketer pastes into the chat:

- Last week's numbers and the total to date for each weekly KPI.
- The quarterly plan, or the items due in the next two weeks.
- What slipped last week, and any new requests.
- Days available this week.

## Procedure

1. Check the inputs. If no numbers were pasted, write [number needed] in each row, base the priorities on dates alone and ask in the last section.
2. Work out the pace for each KPI that has a goal: goal minus total to date, divided by weeks left. For a KPI with no goal, use its baseline divided by the weeks in the baseline period. Show the math and label each result as an estimate.
3. Rate each KPI by last week's number against its pace. "Ahead" is 100% or more, "Close" is 80% to 99%, "Behind" is under 80%. These cutoffs and the 14-day window in step 5 are starting rules the marketer can change, not benchmarks.
4. Do not call a trend from one week. A KPI that is Behind for one week gets a check, such as "find out why". Behind for two weeks or more gets a fix.
5. List candidates: plan items due within 14 days, items whose approval lead time means they must start this week, the fix or check for each Behind KPI, slipped items and new requests.
6. Rank the candidates. Hard deadlines within 14 days come first, counting approval time from channels-and-tools.md. Next come fixes for a Behind KPI tied to a marketing goal. Next come items slipped twice, which must either be done this week or dropped. New requests that serve no goal do not qualify.
7. Pick up to three priorities. For each one, write what done looks like by Friday, the owner and the goal served. Use only the marketer or people named in the context pack as owners.
8. Run the capacity check. Estimate days for each priority and add days for routine work the marketer names. If the total exceeds days available, drop the third priority, then the second. Never add a fourth.
9. Write the do-not-do list: 3 to 5 specific things the marketer might be tempted to do, each with the reason and when to look at it again. Include candidates that lost out in step 6. Add anything barred by limits or hard rules only if someone actually asked for it or the plan implies it.
10. Write up to 2 decisions for the marketer, each with your recommendation.
11. Check the draft against the context pack: goals and definitions match goals-and-kpis.md, approval times are respected, no hard rule is broken.
12. List everything you assumed or estimated in the last section, including each pace calculation.

## Output format

```
Status: Draft
Week of: <date>

## Priorities
| # | Priority | Done by Friday means | Owner | Goal served | Days |
<1 to 3 rows; priority up to 12 words; done means up to 20 words>

## Do not do this week
- <item, reason, when to revisit, up to 25 words each, 3 to 5 items>

## Numbers against pace
| KPI | Last week | To date | Pace needed | Rating |
<one row per weekly KPI; rating is Ahead, Close or Behind>

## Capacity
Days needed: <number> | Days available: <number> | Result: <fits, or what was dropped, up to 20 words>

## Decisions for the marketer
- <decision and recommendation, up to 30 words each, up to 2 items, or "None">

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Are there three priorities or fewer, each with a test for done by Friday?
- [ ] Does each priority serve a goal in the context pack?
- [ ] Do approval lead times still allow each deadline?
- [ ] Do the priorities fit the days available?
- [ ] Is each item on the do-not-do list something you would really be tempted to do?
- [ ] Is every pace calculation shown and labeled as an estimate?
- [ ] Is every trend backed by two or more weeks of numbers?

## Example (fictional company)

**Status:** Draft

**Week of:** January 25, 2027

**Priorities**

| # | Priority | Done by Friday means | Owner | Goal served | Days |
|---|---|---|---|---|---|
| 1 | Finish professional services campaign page and emails | Drafts ready for the February 15 launch | The marketer | Campaign by February 15 | 2.5 |
| 2 | Find out why pipeline is behind, with [Diagnose a pipeline gap](../analytics-and-campaign-evaluation/diagnose-pipeline-gap.md) | Search ads export reviewed, likely cause named | The marketer | $1.2 million pipeline | 1 |
| 3 | Send conference budget for approval | Request with Marta Ilves, CEO, who needs 3 days | The marketer | Pipeline, SQLs | 0.5 |

**Do not do this week**

- Outbound to software companies: inbound only. Revisit next quarter.
- A third blog post this month: the campaign comes first. Revisit in February.
- Manager view in campaign copy: internal only. Revisit once cleared for public mention.

**Numbers against pace**

| KPI | Last week | To date | Pace needed | Rating |
|---|---|---|---|---|
| New qualified pipeline | $70,000 | $270,000 | $93,000 | Behind |
| MQLs | 24 | 72 | 20 | Ahead |
| Website demo requests | 4 | 16 | About 4.5 | Close |

**Capacity**

Days needed: 4 | Days available: 4 | Result: fits

**Decisions for the marketer:** None.

**Assumptions and open questions**

- Assumption: this week's numbers, days and 10 weeks left are invented for this example, and the conference spend is over the $5,000 approval line.
- Estimate: pipeline pace is ($1.2 million minus $270,000) divided by 10 weeks. MQL pace is 260 divided by 13 weeks. Demo pace is 58 divided by 13 weeks.

## How to run it

```
Use the skill "Set weekly priorities". Read the context pack.
Task: <the week's start date and the days you have>.
<paste last week's numbers, what is due, what slipped and new requests here>
```
