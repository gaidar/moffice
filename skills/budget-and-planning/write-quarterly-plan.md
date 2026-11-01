---
title: Write a quarterly plan
type: skill
function: budget-and-planning
owner: head-of-marketing
reads: [goals-and-kpis, company, icp-and-segments, channels-and-tools, product]
version: 0.1.0
updated: 2026-11-01
summary: Goals, bets, calendar, owners and a capacity check for one quarter.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this skill once a quarter to turn goals into a small set of bets, with dates, owners and a check that one marketer can actually do them. Do not use it to split money across channels; use [Allocate the budget](allocate-budget.md) instead. For the week ahead, use [Set weekly priorities](set-weekly-priorities.md).

## Inputs

- [[context-pack:goals-and-kpis]]: quarter, company goal, marketing goals, budget, definitions, baselines and other priorities.
- [[context-pack:company]]: the size of the marketing team and who can be named.
- [[context-pack:icp-and-segments]]: segment priority order.
- [[context-pack:channels-and-tools]]: channels, limits, approvers and approval times.
- [[context-pack:product]]: limits, and what may be said about the roadmap.

The marketer pastes into the chat:

- Last quarter's results against goals, if available.
- Days the marketer can spend on this plan in the quarter, after time off and fixed work.
- Hard dates and commitments not in the context pack, such as events, releases or sales requests.

## Procedure

1. Copy the quarter, company goal and marketing goals word for word from goals-and-kpis.md. If the marketing goals are blank, ask for them and stop. Do not write goals for the marketer.
2. Work out each gap. Show goal, baseline and difference. Where goals chain, work backward and show the math, such as SQL goal divided by MQL to SQL rate. Label each result as an estimate. If a baseline is blank, write [baseline needed] and mark the gap unknown.
3. Write 3 to 5 bets. A bet is one coordinated effort with one goal, one segment and one window. Any goal with a date in goals-and-kpis.md becomes a bet automatically. Every goal needs at least one bet, and any idea that serves no goal goes to "Not doing".
4. Rank the bets. Dated goals come first, then bets for the top segment in the priority order, then the rest. State each bet's expected effect as an estimate with its method, or as unknown. Do not use outside benchmarks.
5. Build the calendar. Place hard dates first, then count back from each one, using the approval times in channels-and-tools.md. Add the first draft date for each item needing approval.
6. Assign one owner to each bet and each calendar item. Use only people named in the context pack, or "the marketer". Anyone outside marketing is marked "needs to agree".
7. Run the capacity check. Estimate days per bet, add a separate row for running existing channels, and compare the total with the marketer's available days. Do the same for any freelance time in company.md. If demand exceeds supply, shrink or cut the lowest ranked bet until it fits, and record the cut under "Not doing".
8. Check the money. If the estimated cost of the bets exceeds the budget, say by how much and cut the lowest ranked bet. The detailed split belongs to [Allocate the budget](allocate-budget.md).
9. Write up to 3 risks, each with the signal that shows it is happening and the response.
10. Check the draft against the context pack: goals word for word, limits and hard rules respected, nothing planned that the product cannot do, and internal-only items marked internal.
11. List everything you assumed or estimated in the last section, including every day count.

## Output format

```
Status: Draft
Quarter: <quarter>
Company goal: <word for word, one line>

## Goals and gaps
| Goal | Baseline | Gap | Math |
<one row per marketing goal, plus any derived number labeled Estimate>

## Bets
| Rank | Bet | Goal served | Segment | Window | Owner | Expected effect |
<3 to 5 rows; bet up to 12 words; effect is an estimate with its method, or "unknown">

## Calendar
| Date | Item | Bet | Owner | Approver and lead time |
<sorted by date, up to 15 rows>

## Capacity check
| Work | Marketer days | Freelance days |
<one row per bet, one row for existing channels, one total row, one available row>
Result: <fits, or what was cut to make it fit, up to 30 words>

## Not doing
- <item and reason, up to 20 words each, 2 to 6 items>

## Risks
- <risk, signal, response, up to 30 words each, up to 3 items>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Are the goals copied word for word, with no new goals added?
- [ ] Does every goal have a bet, and does every bet serve a goal?
- [ ] Does each calendar date allow for the approval time of its approver?
- [ ] Does each item have one owner, who is named in the context pack or is the marketer?
- [ ] Does the capacity check fit, after cuts, with existing channel work counted?
- [ ] Are all derived numbers labeled as estimates, with the math shown?
- [ ] Are internal-only items marked, so the plan is not shared outside the company as is?

## Example (fictional company)

**Status:** Draft

**Quarter:** Q1 2027

**Company goal:** Reach $7 million in annual recurring revenue by the end of 2027

**Goals and gaps**

| Goal | Baseline | Gap | Math |
|---|---|---|---|
| Create $1.2 million in new qualified pipeline by March 31, 2027 | $900,000 | $300,000 | Goal minus Q3 2026 |
| Produce 90 sales-qualified leads by March 31, 2027 | About 68 | About 22 | Estimate: 260 MQLs x 26% |
| Publish the campaign for professional services firms by February 15, 2027 | Unknown | Unknown | Dated goal |

**Bets**

| Rank | Bet | Goal served | Segment | Window | Owner | Expected effect |
|---|---|---|---|---|---|---|
| 1 | Professional services campaign | Campaign | Professional services | February 15 | The marketer | Unknown |
| 2 | Regional learning and development conference | SQLs | Professional services | March 9 to 11 | The marketer | Unknown |
| 3 | Manager view release support (internal only) | Pipeline | All | February | The marketer | Unknown |

**Calendar:** January 29 first drafts, February 15 campaign live, March 9 to 11 conference.

**Capacity check:** 65 days needed, 60 available. Result: bet 3 shrinks by 5 days.

**Not doing:** outbound for software companies, inbound only. Display retargeting, barred by limits.

**Risks:** Campaign slips. Signal: no draft by January 29. Response: drop bet 3.

**Assumptions and open questions**

- Estimate: 90 SQLs at 26% needs about 346 MQLs, against 260.
- Assumption: 60 marketer days and all day counts are invented.
- Unknown: what is the conference cost?

## How to run it

```
Use the skill "Write a quarterly plan". Read the context pack.
Task: write the plan for <quarter>, using last quarter's results and the available days pasted below.
```
