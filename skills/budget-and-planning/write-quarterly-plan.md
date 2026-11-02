---
title: Write a quarterly plan
type: skill
function: budget-and-planning
owner: head-of-marketing
reads: [goals-and-kpis, company, icp-and-segments, channels-and-tools, product]
you_bring: Last quarter's results, the days you can spend on this plan, and any hard dates not in the context pack.
also_for: [quarterly plan, marketing plan, 90-day plan, stop doing, what to stop, next quarter, what to focus on, plan for the ceo, goals for the quarter, hit the pipeline goal, one person team]
version: 0.1.0
updated: 2026-11-02
summary: Goals, bets, calendar, owners and a capacity check for one quarter.
judge: ["If you could only finish one bet this quarter which would it be and is it ranked first?", "Which bet would you cut if the CEO added a project next month?", "Did you reason the expected effect from your numbers or is it what you hope for?", "Would these bets close the gap even if they all went well?"]
show_to: your CEO, before you start, and ask which bet they would cut first
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this skill once a quarter to turn goals into a small set of bets, with dates, owners and a check that one marketer can actually do them. Do not use it to split money across channels; use [Allocate the budget](allocate-budget.md) instead. For the week ahead, use [Set weekly priorities](set-weekly-priorities.md). With no goals yet, run [Propose quarterly goals](propose-quarterly-goals.md) first.

## Inputs

- [[context-pack:goals-and-kpis]]: quarter, goals, budget, definitions, baselines, priorities.
- [[context-pack:company]]: the size of the marketing team and who can be named.
- [[context-pack:icp-and-segments]]: segment priority order.
- [[context-pack:channels-and-tools]]: channels, limits, approvers and approval times.
- [[context-pack:product]]: limits, and what may be said about the roadmap.

The marketer pastes into the chat:

- Last quarter's results against goals, if available.
- Days the marketer can spend on this plan in the quarter, after time off and fixed work.
- Hard dates and commitments not in the context pack.
- Everything now running.

## Procedure

1. Copy the quarter, company goal and marketing goals word for word from goals-and-kpis.md. If the marketing goals are blank, stop and point to [Propose quarterly goals](propose-quarterly-goals.md). Do not write goals for the marketer.
2. Work out each gap. Show goal, baseline and difference. Where goals chain, work backward and show the math, such as SQL goal divided by MQL to SQL rate. Label each result as an estimate. If a baseline is blank, write [baseline needed] and mark the gap unknown.
3. Write 3 to 5 bets. A bet is one coordinated effort with one goal, one segment and one window. Any goal with a date in goals-and-kpis.md becomes a bet automatically. Every goal needs at least one bet, and any idea or running work that serves no goal goes to "Not doing".
4. Rank the bets. Dated goals come first, then bets for the top segment in the priority order, then the rest. State each bet's expected effect as an estimate, with its reasoning in a few words, worked from your baselines. Write unknown only if no baseline helps. Do not use outside benchmarks.
5. Build the calendar. Place hard dates first, then count back from each one, using the approval times in channels-and-tools.md. Add the first draft date for each item needing approval.
6. Assign one owner to each bet and each calendar item. Use only people named in the context pack, or "the marketer". Mark anyone outside marketing "needs to agree".
7. Run the capacity check. Estimate days per bet from its pieces, add a row for running existing channels, and compare the total with the marketer's available days. Include freelance time. If demand exceeds supply, shrink or cut the lowest ranked bet until it fits, and record the cut under "Not doing".
8. Check the money. If the estimated cost of the bets exceeds the budget, say by how much and cut the lowest ranked bet.
9. Write up to 3 risks, each with its signal and response.
10. Check the draft against the context pack: goals word for word, limits and hard rules respected, nothing planned that the product cannot do, internal-only items marked.
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
<3 to 5 rows; bet up to 12 words; effect is an estimate with its reasoning>

## Calendar
| Date | Item | Bet | Owner | Approver and lead time |
<sorted by date, up to 15 rows>

## Capacity check
| Work | Marketer days and reasoning | Freelance days |
<one row per bet, existing channels, total, available>
Result: <fits, or what was cut, up to 30 words>

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
- [ ] Does each item have one owner named in the context pack, or the marketer?
- [ ] Does the capacity check fit, after cuts, with existing channel work counted?
- [ ] Are all derived numbers labeled as estimates, with the math shown?
- [ ] Are internal-only items marked?

## Example (fictional company)

**Status:** Draft

**Quarter:** Q1 2027

**Company goal:** Reach $7 million in annual recurring revenue by the end of 2027

**Goals and gaps**

| Goal | Baseline | Gap | Math |
|---|---|---|---|
| Create $1.2 million in new qualified pipeline by March 31, 2027 | $900,000 | $300,000 | Q3 2026 baseline |
| Produce 90 sales-qualified leads by March 31, 2027 | About 68 | About 22 | Estimate: 260 MQLs x 26% |
| Publish the campaign for professional services firms by February 15, 2027 | None | None | Dated |

**Bets**

| Rank | Bet | Goal served | Segment | Window | Owner | Expected effect |
|---|---|---|---|---|---|---|
| 1 | Professional services campaign | Campaign | Professional services | February 15 | Marketer | Estimate: 40 of the campaign's 116 MQLs are new, a third above 20 a week, 6 weeks |
| 2 | Regional conference | SQLs | Professional services | March 9–11 | Marketer | Estimate: 30 MQLs, 10 demo requests a day, 3 days |
| 3 | Manager view release (internal only) | Pipeline | All | February | Marketer | Estimate: 15 MQLs, helps calls more than leads |

**Calendar:** January 29 first drafts, February 15 live, March 9–11 conference.

**Capacity check (estimates):** Campaign 20 days (5 assets x 4). Conference 10 (3 on site). Release 15. Channels 20 (1.5 days a week). Total 65, 60 available (13 weeks, 5 off). Result: bet 3 shrinks by 5.

**Not doing:** outbound for software companies.

**Risks:** Campaign slips. Signal: no draft by January 29. Response: drop bet 3.

**Assumptions and open questions**

- Estimate: 90 SQLs / 26% = 346 MQLs, 86 above 260. The bets total 85, no margin.- Assumption: effects and day counts are illustrative.

## How to run it

```
Use the skill "Write a quarterly plan". Read the context pack.
Task: <the quarter, the days you have, and any hard dates>.
<paste last quarter's results here>
```
