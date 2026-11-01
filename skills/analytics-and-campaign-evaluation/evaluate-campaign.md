---
title: Evaluate a campaign
type: skill
function: analytics-and-campaign-evaluation
owner: marketing-analyst
reads: [goals-and-kpis, icp-and-segments, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Compares a finished campaign's results with its targets, says what worked and sets what to do next.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this after a campaign's time window has closed and you have its numbers. Do not use it for weekly spend decisions on a live paid campaign, which belong to [Adjust paid campaigns](../paid-demand-gen/adjust-paid-campaigns.md), or for credit across all channels, which belongs to [Read attribution](read-attribution.md).

## Inputs

- [[context-pack:goals-and-kpis]]: MQL, SQL and pipeline definitions, plus KPI baselines for comparison.
- [[context-pack:icp-and-segments]]: ICP criteria for judging lead quality, and the typical sales cycle.
- [[context-pack:channels-and-tools]]: channels used, paid limits and hard rules.

The marketer pastes into the chat:

- The campaign brief, or its goal, audience, time window, targets and budget.
- Results by channel: spend, leads, MQLs, SQLs and pipeline, with the date pulled.
- Anything that disturbed the results, such as a tracking gap or a changed offer.

## Procedure

1. If the targets or the results are missing, ask for them before drafting. If only part is missing, mark that row "no data". Never reconstruct a target from the results.
2. Fill the results table with one row per target in the brief. Difference is actual minus target, as a number and a percentage.
3. Set each row's status. Use "hit" at or above target and "missed" below it. Use "no data" when the number was not supplied. Use "too early" for SQL, pipeline or won deals when fewer days have passed since the campaign ended than the long end of the typical sales cycle and the number is still below target.
4. Set the verdict from the campaign's one goal metric. "Hit" means the goal metric was hit. "Missed" means it was missed. "Too early" means its status is too early, and the verdict then names the date to read it again: the end date plus the long end of the sales cycle.
5. Calculate cost per MQL for each channel with spend. Show the division. Compare a rate with a baseline only if both use the same definition.
6. Write what worked and what did not. Each bullet needs a number from the table. Under 20 leads in a channel, write "too few to read" and draw no conclusion. That cutoff is a starting rule the marketer can change, not a benchmark. Say "coincided with" rather than "caused" unless the marketer supplied a control group.
7. Write next actions. Each one starts with keep, change or stop. Stop a channel only when it missed its target, is not too early and has enough leads to read. Name an owner from the marketer's input, or write [owner needed].
8. Check the draft against the context pack: terms match the definitions in goals-and-kpis.md, the proposed actions respect the limits in channels-and-tools.md, and lead quality uses the ICP criteria. If a needed field is blank, leave a visible placeholder such as [MQL definition needed] and ask in the last section. Never invent.
9. List every assumption, estimate, inference and unknown in the last section, including any row with no data and the date the numbers were pulled.

## Output format

```
Status: Draft

## Verdict
<Hit, missed or too early, then the goal metric's number. If too early, the date to read it again. Max 40 words.>

## Results against targets
| Metric | Target | Actual | Difference | Status |
<One row per target. Status is hit, missed, too early or no data.>

## Cost by channel
| Channel | Spend | Leads | MQLs | Cost per MQL |
<One row per channel with spend. Write "not supplied" for gaps.>

## What worked
<Up to 3 bullets, max 25 words each, each with a number.>

## What did not work
<Up to 3 bullets, max 25 words each, each with a number.>

## Next actions
| Action | Keep, change or stop | Owner | By when |
<Up to 5 rows.>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the verdict rest on the campaign's one goal metric?
- [ ] Does every target in the brief have a row, with status set by the rule?
- [ ] Are recent SQL and pipeline numbers marked too early rather than missed?
- [ ] Does every worked or did-not-work bullet carry a number from the table?
- [ ] Do MQL, SQL and pipeline match the definitions in goals-and-kpis.md?
- [ ] Is causation claimed only where a control group exists?
- [ ] Does every next action have an owner or a visible placeholder?

## Example (fictional company)

Status: Draft

Assumption: this CogniATion webinar on analyst reasoning and all its results are illustrative, as if pasted by the marketer on November 1, 2026.

**Verdict**

Too early. Goal of $125,000 pipeline stands at $80,000. Read again January 13, 2027.

**Results against targets**

| Metric | Target | Actual | Difference | Status |
|---|---|---|---|---|
| MQLs | 40 | 46 | +6, +15% | Hit |
| SQLs | 10 | 6 | -4, -40% | Too early |
| Pipeline | $125,000 | $80,000 | -$45,000, -36% | Too early |

**Cost by channel**

| Channel | Spend | Leads | MQLs | Cost per MQL |
|---|---|---|---|---|
| Analyst reasoning webinar | $4,500 | 88 | 46 | $98 |

**What worked**

- Webinar topic drew 46 MQLs against a target of 40.

**What did not work**

- 6 SQLs from 46 MQLs is 13% so far, against the 26% baseline, with the sales cycle still open.

**Next actions**

| Action | Keep, change or stop | Owner | By when |
|---|---|---|---|
| Keep the analyst reasoning topic for the next webinar | Keep | Marketer | January 2027 |
| Read pipeline again | Keep | Marketer | January 13, 2027 |

**Assumptions and open questions**

- Assumption: the campaign ended October 15, 2026.
- Estimate: $4,500 / 46 = $98. Reread date is the end date plus 90 days.
- Inference: too early, from 17 days elapsed against the 45 to 90 day sales cycle.
- Unknown: How many of the 42 leads short of MQL missed the ICP, such as having fewer than 100 learners?
- Unknown: How many of the 46 MQLs has sales called so far?

## How to run it

```
Use the skill "Evaluate a campaign". Read the context pack.
Task: <evaluate which campaign, with its brief and results pasted below>.
```
