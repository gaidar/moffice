---
title: Adjust paid campaigns
type: skill
function: paid-demand-gen
owner: paid-media-manager
reads: [messaging, goals-and-kpis, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Turns a pasted performance export into weekly keep, cut or change decisions for each campaign line.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this once a week while paid campaigns are running, with last week's export in hand. Do not use it to judge a finished campaign, which belongs in [Evaluate a campaign](../analytics-and-campaign-evaluation/evaluate-campaign.md). If no plan exists yet, use [Plan a paid campaign](plan-paid-campaign.md) instead.

## Inputs

- [[context-pack:messaging]]: words to avoid when suggesting new copy or terms.
- [[context-pack:goals-and-kpis]]: MQL and SQL definitions, quarter budget, conversion rates.
- [[context-pack:channels-and-tools]]: monthly budget per channel, limits, approval thresholds.

The marketer supplies in the prompt: the week's performance export with spend and conversions per line, its date range, and the target cost per MQL and stop rules from the paid plan. Better still, add MQLs and SQLs per line from the CRM.

## Procedure

1. Check the export: date range present, spend and conversions present, totals that match the lines. If a column is missing, ask for it. Do not fill it in.
2. Get the target cost. Use the target from the paid plan. If there is none, work it out as an estimate: quarter budget divided by the SQL goal, multiplied by the MQL to SQL rate. Show the arithmetic and ask in the last section.
3. Choose the conversion to judge. Use MQLs per line if the marketer pasted them, as goals-and-kpis.md defines them. If only ad-tool conversions are available, use those and label the result as lower confidence.
4. Compute for each line: spend, conversions and cost per conversion. Round to whole dollars. Use only the marketer's numbers.
5. Decide for each line, using the first rule below that matches. If the paid plan has its own stop rules, its numbers replace these multiples. These multiples are starting rules the marketer can change, not benchmarks.

   | Rule | Condition | Decision |
   |---|---|---|
   | 1 | Tracking looks broken: clicks but no conversion data, or a sudden drop to zero | Change: fix tracking, and pause if channels-and-tools.md forbids spend without it |
   | 2 | Spend below the target cost | Keep: too little data |
   | 3 | Spend at 3 times the target cost or more, no conversions | Cut |
   | 4 | Cost per conversion above 1.5 times the target, at least 2 conversions | Change one thing |
   | 5 | Cost per conversion at or below the target | Keep |
   | 6 | Anything else | Keep: watch next week |

6. For each change, name one thing: audience, search terms, ad copy, destination page or bid. Pick the likely cause from the export. If the export cannot show it, pick ad copy and label that as an assumption. Do not change a line changed last week unless rule 3 applies, so results can be read.
7. Move cut money to the Keep line with the lowest cost per conversion, up to its plan limit. Otherwise report it as unspent. Keep totals within the monthly budget in channels-and-tools.md, and flag anything needing approval.
8. Compare spend to date with the monthly budget per channel and say whether it is on pace, over or under.
9. Write the steps the marketer takes in the ad tool, in order. Say nothing as if it were already done.
10. Check the decisions against the context pack: limits, forbidden ad types, words to avoid, budget, approval thresholds. Fix what contradicts it.
11. List everything assumed, estimated, inferred or unknown in the last section, using those labels.

## Output format

Each line in the export gets one row.

```
Status: Draft

## Decisions this week
| Line | Spend | Conversions | Cost per conversion | Decision | Rule | Reason, up to 15 words |

## Changes to make
| Line | One change | What to do in the ad tool | Check next week |

## Budget
Moved: <from, to, amount>
Pace: <channel, spend to date, monthly budget, on pace or over or under>
Approval needed: <approver, or "None">

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every line in the export have exactly one decision and the rule behind it?
- [ ] Do all the numbers trace back to the pasted export or show their arithmetic?
- [ ] Is the target cost from the paid plan, or labeled as an estimate?
- [ ] Is each change limited to one thing per line?
- [ ] Do lines with too little data stay at Keep instead of being judged?
- [ ] Do the totals stay inside the monthly budget, with approvals flagged?
- [ ] Are the actions written as steps for the marketer, not as things already done?

## Example (fictional company)

Status: Draft

**Decisions this week**

| Line | Spend | Conversions | Cost per conversion | Decision | Rule | Reason |
|---|---|---|---|---|---|---|
| Search, critical thinking terms | $540 | 3 | $180 | Keep | 5 | Below the $202 target |
| Search, general AI training terms | $610 | 0 | None | Cut | 3 | Over $606 with no MQLs |
| Social, heads of learning | $900 | 2 | $450 | Change | 4 | Above the $303 limit |

**Changes to make**

| Line | One change | What to do in the ad tool | Check next week |
|---|---|---|---|
| Social, heads of learning | Audience | Limit to professional services firms, as in the paid plan | Cost per MQL under $303 |
| Search, general terms | Pause | Pause the line | No further spend |

**Budget.** Moved: $610 a week from general terms to critical thinking terms. Pace: search at $1,150 this week against $5,000 a month, on pace. Social at $900 against $4,000 a month, on pace. Approval needed: None, since the search total does not change.

**Assumptions and open questions**

- Assumption: the export figures are made up for this example, as if the marketer pasted them. Conversions are MQLs.
- Estimate: $202 is $70,000 divided by 90 SQLs, times the 26% MQL to SQL rate. $606 is three times that, $303 is 1.5 times.
- Unknown: how many of these MQLs became SQLs? Can you paste the CRM figures?

## How to run it

```
Use the skill "Adjust paid campaigns". Read the context pack.
Task: <what they want>.
```
