---
title: Adjust paid campaigns
type: skill
function: paid-demand-gen
owner: paid-media-manager
reads: [messaging, goals-and-kpis, channels-and-tools]
you_bring: An ad export for the four weeks ending seven days ago and for the last seven days, paid's budget and expected SQLs, and the paid plan's stop rules.
also_for: [ads not working, cost per lead too high, should i pause this ad, paid search results, weekly ad review, wasting ad budget, cut ad spend, junk leads from ads]
version: 0.1.0
updated: 2026-11-02
summary: Turns a pasted performance export into weekly keep, cut or change decisions for each campaign line.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this once a week while paid campaigns are running, with a current export in hand. Do not use it to judge a finished campaign, which belongs in [Evaluate a campaign](../analytics-and-campaign-evaluation/evaluate-campaign.md). If no plan exists yet, use [Plan a paid campaign](plan-paid-campaign.md) instead.

## Inputs

- [[context-pack:messaging]]: words to avoid.
- [[context-pack:goals-and-kpis]]: MQL and SQL definitions, conversion rates.
- [[context-pack:channels-and-tools]]: monthly budget per channel, limits, approval thresholds.

The marketer supplies: a performance export with spend and conversions per line, split into the four weeks ending seven days ago and the last seven days; paid's budget and expected SQLs; and the paid plan's target cost and stop rules. Better still, add CRM MQLs and SQLs per line.

## Procedure

1. Check the export: both date ranges, spend, conversions, no repeated lines, and totals that match the lines. If something is missing or wrong, say what to export again. Judge lines on the rolling four weeks, leaving out the last seven days, or the MQL to SQL time in goals-and-kpis.md when judging on SQLs. Use the last seven days only for rule 1 and pace.
2. Get the target cost. Use the target from the paid plan. If there is none, estimate: paid's own budget divided by the SQLs expected from paid is the cost per SQL, and that times the MQL to SQL rate is the cost per MQL. Show the arithmetic. If expected SQLs are unknown, write [expected SQLs needed] and apply only rules 1 and 6.
3. Choose the conversion to judge. Use SQLs per line if pasted, against the cost per SQL. Otherwise use MQLs, as goals-and-kpis.md defines them. Ad-tool conversions are not MQLs: judge them only against a plan target for that event, or with evidence of how many become MQLs. Without either, write [target for this conversion needed], apply only rules 1 and 6, and report tracking and spend.
4. Compute for each line: spend, conversions and cost per conversion. Use only the marketer's numbers.
5. Decide for each line, using the first rule below that matches. If the paid plan has its own stop rules, its numbers replace these multiples. These numbers and windows are starting rules, not benchmarks.

   | Rule | Condition | Decision |
   |---|---|---|
   | 1 | Tracking looks broken: clicks but no conversion data, or a sudden drop to zero | Change: fix tracking, and pause if channels-and-tools.md forbids spend without it |
   | 2 | Spend below the target cost | Keep: too little data |
   | 3 | Spend at 3 times the target cost or more, no conversions | Cut |
   | 4 | Cost per conversion above 1.5 times the target, at least 5 conversions | Change one thing |
   | 5 | Cost per conversion at or below the target | Keep |
   | 6 | Anything else | Keep: watch next week |

6. For each change, name one thing: audience, search terms, ad copy, destination page, bid, or tracking under rule 1. Pick the likely cause from the export. If the export cannot show it, propose the cheapest to test, and label that an assumption. Do not change a line changed in the last two weeks unless rule 3 applies.
7. Move cut money to the Keep line with the lowest cost per conversion, up to its plan limit. Otherwise report it as unspent. Keep totals within the monthly budget in channels-and-tools.md, and flag anything needing approval.
8. Compare spend to date with the monthly budget per channel and say whether it is on pace, over or under.
9. Write the steps the marketer takes in the ad tool, in order. Say nothing as if it were already done.
10. Check the decisions against the context pack: limits, forbidden ad types, words to avoid, budget, approval thresholds.
11. List everything assumed, estimated, inferred or unknown in the last section, using those labels.

## Output format

```
Status: Draft
Window judged: <dates, and the gap left out> | Judged on: <SQLs, MQLs or ad-tool conversions>

## Decisions this week
| Line | Spend | Conversions | Cost per conversion | Decision | Rule | Reason, up to 15 words |

## Changes to make
| Line | One change | What to do in the ad tool | Check in two weeks |

## Budget
Moved: <from, to, amount>
Pace: <channel, spend to date, monthly budget, on pace or over or under>
Approval needed: <approver, or "None">

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does every line in the export have exactly one decision and the rule behind it?
- [ ] Were lines judged on the rolling four weeks, and on SQLs when pasted?
- [ ] Do all the numbers trace back to the pasted export or show their arithmetic?
- [ ] Is the target cost from the paid plan or a labeled estimate, for the same conversion judged?
- [ ] Is each change limited to one thing per line?
- [ ] Do lines with too little data stay at Keep instead of being judged?
- [ ] Do the totals stay inside the monthly budget, with approvals flagged?

## Example (fictional company)

Status: Draft

Window judged: December 21 to January 17, leaving out January 18 to 24. Judged on: MQLs.

**Decisions this week**

| Line | Spend | Conversions | Cost per conversion | Decision | Rule | Reason |
|---|---|---|---|---|---|---|
| Search, critical thinking terms | $3,780 | 21 | $180 | Keep | 5 | Below the $234 target |
| Search, general AI training terms | $820 | 0 | None | Cut | 3 | Over $702 with no MQLs |
| Social, heads of learning | $3,600 | 8 | $450 | Change | 4 | Above the $351 limit |

**Changes to make**

| Line | One change | What to do in the ad tool | Check in two weeks |
|---|---|---|---|
| Social, heads of learning | Audience | Limit to professional services firms | Cost per MQL under $351 |
| Search, general terms | Pause | Pause the line | No further spend |

**Budget.** Moved: about $205 a week from general terms to critical thinking terms. Pace, last seven days: search $1,150 of $5,000 a month, social $900 of $4,000, both on pace. Approval needed: None.

**Assumptions and open questions**

- Assumption: the export figures and the 30 SQLs expected from paid are invented. No SQLs were pasted, so conversions are MQLs.
- Estimate: $234 is paid's $27,000 for the quarter divided by 30 SQLs, times the 26% MQL to SQL rate. $702 is three times that, $351 is 1.5 times.

## How to run it

```
Use the skill "Adjust paid campaigns". Read the context pack.
Task: <paid's budget and expected SQLs, and the plan's target cost and stop rules>.
<paste the export here, with CRM MQLs and SQLs if you have them>
```
