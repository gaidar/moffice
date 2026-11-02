---
title: Evaluate a campaign
type: skill
function: analytics-and-campaign-evaluation
owner: marketing-analyst
reads: [goals-and-kpis, icp-and-segments, channels-and-tools]
you_bring: The campaign brief, its results by channel with the date pulled, and anything that disturbed the numbers.
also_for: [did the campaign work, campaign results, campaign roi, campaign post-mortem, was it worth the money, pipeline from a campaign, what to do after a campaign]
version: 0.1.0
updated: 2026-11-02
summary: Compares a finished campaign's results with its targets, says what worked and sets what to do next.
judge: ["Would these leads have come anyway without the campaign?", "Are you judging the campaign or the timing and the list it went to?", "Would you run it again if the money were your own?", "Did sales notice this campaign and did it change any conversation?"]
show_to: the salesperson who got the most leads from it, and ask whether those leads were worth the call
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this after a campaign's time window has closed and you have its numbers, and again on any later read date. Do not use it for weekly spend decisions on a live paid campaign, which belong to [Adjust paid campaigns](../paid-demand-gen/adjust-paid-campaigns.md), or for credit across all channels, which belongs to [Read attribution](read-attribution.md).

## Inputs

- [[context-pack:goals-and-kpis]]: MQL, SQL and pipeline definitions, stage timing, plus KPI baselines for comparison.
- [[context-pack:icp-and-segments]]: ICP criteria for judging lead quality, and the typical sales cycle.
- [[context-pack:channels-and-tools]]: channels used, paid limits and hard rules.

The marketer pastes into the chat:

- The campaign brief, or its goal, audience, time window, targets and budget.
- Results by channel: spend, leads, MQLs, SQLs and pipeline, with the date pulled.
- Anything that disturbed the results, such as a tracking gap.

## Procedure

1. If the targets or the results are missing, ask for them before drafting. If only part is missing, mark that row "no data". Never reconstruct a target from the results. Check the numbers: one period, stage definitions as in goals-and-kpis.md, no repeated lead ID, totals that add up. If not, say what to fix, and mark those rows "no data". Ask for a missing pull date.
2. Fill the results table with one row per target in the brief. Difference is actual minus target, as a number and a percentage.
3. Set each row's read date: the date the brief promised. If it promised none, use the end date for leads and MQLs, the end date plus the long end of the stage timing in goals-and-kpis.md for SQLs and pipeline, or the end date plus the long end of the sales cycle for won deals. If the timing is blank, write [stage timing needed] and ask.
4. Set each row's status. Before its read date, use "too early". On or after it, use "hit" at or above target and "missed" below it, with the number at that date. Use "no data" when the number was not supplied. Leads keep maturing after a deadline, so give a missed SQL, pipeline or won-deal row a later read: the end date plus that same time. Report the later result on its own line. It never changes the status.
5. Set the verdict from the status of the campaign's one goal metric, and name its read date if too early or its later read if missed.
6. Calculate cost per MQL for each channel with spend. Show the division. Compare a rate with a baseline only if both use the same definition.
7. Write what worked and what did not. Each bullet needs a number from the table. Under 20 leads in a channel (a starting rule), write "too few to read" and draw no conclusion. Say "coincided with" rather than "caused" unless the marketer supplied a control group.
8. Write next actions. Each one starts with keep, change or stop. Stop a channel only when it missed its target, its later read has passed and it has enough leads to read. Name an owner from the marketer's input, or write [owner needed].
9. Check the draft against the context pack: terms match goals-and-kpis.md, actions respect the limits in channels-and-tools.md, and lead quality uses the ICP criteria. If a needed field is blank, leave a visible placeholder and ask in the last section.
10. List every assumption, estimate, inference and unknown in the last section, including any row with no data and the date the numbers were pulled.

## Output format

```
Status: Draft

## Verdict
<Hit, missed or too early, then the goal metric's number. Name its read date if too early, its later read if missed. Max 40 words.>

## Results against targets
| Metric | Target | Read date | Actual | Difference | Status |
<One row per target. Status is hit, missed, too early or no data.>
Later read: <metric, date, and the matured result with its pull date once that date has passed, or "None">

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
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does the verdict rest on the campaign's one goal metric?
- [ ] Does every target in the brief have a row, with status set by the rule?
- [ ] Is each row read on its own date, with a missed deadline called missed and maturing leads given a later read?
- [ ] Do MQL, SQL and pipeline match the definitions in goals-and-kpis.md?
- [ ] Does every next action have an owner or a visible placeholder?

## Example (fictional company)

Status: Draft

Assumption: this CogniATion webinar and all its results are illustrative, as if pasted on November 1, 2026, against a brief promising its targets by October 31.

**Verdict**

Missed at October 31: pipeline $80,000 against $125,000. Later read November 14, for leads still qualifying.

**Results against targets**

| Metric | Target | Read date | Actual | Difference | Status |
|---|---|---|---|---|---|
| MQLs | 40 | Oct 31 | 46 | +6, +15% | Hit |
| SQLs | 10 | Oct 31 | 6 | -4, -40% | Missed |
| Pipeline | $125,000 | Oct 31 | $80,000 | -$45,000, -36% | Missed |

Later read: SQLs and pipeline, November 14.

**Cost by channel**

| Channel | Spend | Leads | MQLs | Cost per MQL |
|---|---|---|---|---|
| Analyst reasoning webinar | $4,500 | 88 | 46 | $98 |

**What worked**

- Webinar topic drew 46 MQLs against a target of 40.

**What did not work**

- 6 SQLs from 46 MQLs is 13% so far, against the 26% baseline, with 13 days of qualifying left.

**Next actions**

| Action | Keep, change or stop | Owner | By when |
|---|---|---|---|
| Keep the analyst reasoning topic for the next webinar | Keep | Marketer | January 2027 |
| Read SQLs and pipeline again | Keep | Marketer | November 14, 2026 |

**Assumptions and open questions**

- Assumption: the campaign ended October 15, 2026.
- Estimate: $4,500 / 46 = $98. Later read is the end date plus the 30-day MQL to SQL time.
- Unknown: How many of the 42 leads short of MQL missed the ICP?
- Unknown: How many of the 46 MQLs has sales called so far?

## How to run it

```
Use the skill "Evaluate a campaign". Read the context pack.
Task: <the campaign and its time window>.
<paste the brief and results by channel here>
```
