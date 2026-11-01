---
title: Read attribution
type: skill
function: analytics-and-campaign-evaluation
owner: marketing-analyst
reads: [goals-and-kpis, icp-and-segments, personas, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Reads first and last touch data side by side and says what can and cannot be concluded from it.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this when you have pipeline or revenue by channel and need to know how far the credit can be trusted. Do not use it to judge one campaign against its targets, which belongs to [Evaluate a campaign](evaluate-campaign.md), or to split next period's money, which belongs to [Allocate the budget](../budget-and-planning/allocate-budget.md).

## Inputs

- [[context-pack:goals-and-kpis]]: the attribution model and the definition of pipeline.
- [[context-pack:icp-and-segments]]: the typical sales cycle, for judging how mature the data is.
- [[context-pack:personas]]: where buyers get information, for naming what tracking cannot see.
- [[context-pack:channels-and-tools]]: the channels in use and the tools that record touches.

The marketer pastes into the chat:

- A CRM export or summary with, for each channel, first touch pipeline and opportunities and last touch pipeline and opportunities.
- The period covered and the date the export was pulled.
- Any tracking change in the period, and when each campaign in the data started.

## Procedure

1. Confirm the model in goals-and-kpis.md. If it is blank, ask. If the export holds only one of the two touches, say the comparison cannot be made, write "not supplied" in the missing column and limit conclusions to the touch supplied.
2. Fill the credit table with one row per channel, plus a row for direct or unknown and a total row. Show dollars and opportunities for each touch.
3. Compare the two totals. If they differ, report the gap and ask why, because the columns do not then cover the same deals. Never add first and last touch together, since a deal with both touches would count twice.
4. Label each channel. Calculate its share of first touch dollars and its share of last touch dollars. "Starter" means first touch share is at least 1.5 times last touch share. "Closer" means the reverse. "Both" means anything in between. "Too few" means fewer than 5 opportunities on both touches, and it overrides the other labels. These cutoffs and the 25% in step 5 are starting rules the marketer can change, not benchmarks.
5. Apply two data warnings. If direct or unknown is above 25% of either total, label that row "warning" and say channel conclusions are weak. If a campaign started fewer days before the pull date than the short end of the sales cycle, mark it "still maturing" and draw no conclusion from it.
6. Write what can be concluded. Use only statements the data shows, in the form "[channel] was first touch on [number] opportunities worth [amount]". Label anything further as an inference and name its inputs.
7. Write what cannot be concluded. Always include these points: the data does not show that a channel caused pipeline, or whether a deal would have happened anyway, and it says nothing about touches between the first and the last. Add return on spend unless spend was supplied.
8. Name the blind spots. List each information source from personas.md that tracking cannot record, such as peers or professional associations, and say that credit for those conversations lands on a later touch.
9. Write up to 3 actions, each framed as a test with the number to watch and when to read it. Never recommend cutting a channel from a single touch, or from a channel labeled too few or still maturing.
10. Check the draft against the context pack: pipeline and model wording match goals-and-kpis.md, and channel names match channels-and-tools.md. If a needed field is blank, leave a visible placeholder such as [pull date needed] and ask in the last section. Never invent.
11. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
Status: Draft

## Bottom line
<What the data supports and how far to trust it. Max 40 words.>

## Credit by channel
| Channel | First touch | Last touch | Label |
<Dollars and opportunities in each touch column. Include direct or unknown and a total row. Label is starter, closer, both, too few, still maturing or warning.>

## What can be concluded
<Up to 4 bullets, max 25 words each.>

## What cannot be concluded
<Up to 4 bullets, max 25 words each.>

## Blind spots
<Up to 3 bullets, max 20 words each.>

## Tests to run
| Test | Number to watch | Read on |
<Up to 3 rows.>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Are first and last touch shown side by side and never summed?
- [ ] Do the two totals match, or is the gap reported?
- [ ] Does every channel label follow the share rule?
- [ ] Is direct or unknown shown as its own row, with the warning applied?
- [ ] Is causation left out of the conclusions?
- [ ] Are the blind spots taken from personas.md?
- [ ] Is every action framed as a test, with no cut based on one touch?

## Example (fictional company)

Status: Draft

Assumption: the $900,000 total is CogniATion's Q3 2026 pipeline baseline. The split by channel is illustrative, as if pasted by the marketer.

**Bottom line**

Webinars and email close deals that other channels start, but unknown touches are above 25% of first touch, so treat channel conclusions as weak.

**Credit by channel**

| Channel | First touch | Last touch | Label |
|---|---|---|---|
| Search ads | $252,000 (19) | $180,000 (14) | Both |
| Organic search | $198,000 (15) | $126,000 (9) | Starter |
| Social network ads | $108,000 (8) | $54,000 (4) | Starter |
| Webinars | $72,000 (5) | $216,000 (16) | Closer |
| Email | $27,000 (2) | $135,000 (10) | Closer |
| Direct or unknown | $243,000 (19) | $189,000 (15) | Warning |
| Total | $900,000 (68) | $900,000 (68) | |

**What can be concluded**

- Webinars were last touch on 16 opportunities worth $216,000.

**What cannot be concluded**

- Whether webinars caused those deals, or whether they would have happened anyway.

**Blind spots**

- Peers in other companies and learning and development associations leave no tracked touch.

**Tests to run**

| Test | Number to watch | Read on |
|---|---|---|
| Invite search ad leads to a webinar for heads of learning | MQL to SQL rate, baseline 26% | End of Q1 2027 |

**Assumptions and open questions**

- Estimate: 68 opportunities is 260 MQLs times the 26% rate, both Q3 2026 baselines.
- Unknown: How much of direct or unknown comes from untagged links or the video channel?

## How to run it

```
Use the skill "Read attribution". Read the context pack.
Task: <read which period's attribution, with the export pasted below>.
```
