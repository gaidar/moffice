---
title: Read attribution
type: skill
function: analytics-and-campaign-evaluation
owner: marketing-analyst
reads: [goals-and-kpis, icp-and-segments, personas, channels-and-tools]
you_bring: A CRM export with first and last touch pipeline by channel, the date pulled, and answers to how did you hear about us if you collect them.
also_for: [which channel drives pipeline, what is working, where do deals come from, channel credit, first touch vs last touch, how did you hear about us, ceo asks which channel works]
version: 0.1.0
updated: 2026-11-02
summary: Reads first and last touch data side by side and says what can and cannot be concluded from it.
judge: ["Would the channel with the credit have worked without the one with none?", "Where do your best customers say they first heard of you and does that match this?", "Which channel has the most money riding on the least reliable credit?", "Is direct traffic hiding something you cannot track such as word of mouth?"]
show_to: a salesperson, and ask what recent buyers said made them first reach out
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when you have pipeline or revenue by channel and need to know how far the credit can be trusted. Do not use it to judge one campaign against its targets, which belongs to [Evaluate a campaign](evaluate-campaign.md).

## Inputs

- [[context-pack:goals-and-kpis]]: attribution model, pipeline definition.
- [[context-pack:icp-and-segments]]: typical sales cycle, for data maturity.
- [[context-pack:personas]]: where buyers get information.
- [[context-pack:channels-and-tools]]: channels in use, tools that record touches.

The marketer pastes:

- A CRM export or summary with first and last touch pipeline and opportunities for each channel.
- Answers to "how did you hear about us", counted by channel, if you collect them.
- The period and the date pulled.
- Tracking changes, and when each campaign started.

## Procedure

1. Confirm the model in goals-and-kpis.md. If it is blank, ask. If the export holds only one of the two touches, say the comparison cannot be made, write "not supplied" in the missing column and limit conclusions to the touch supplied.
2. Fill the credit table with one row per channel, plus a row for direct or unknown and a total row. Show dollars and opportunities for each touch, and the count of "how did you hear about us" answers, or "not collected".
3. Compare the two totals. If they differ, report the gap and ask why. Never add first and last touch together.
4. Label each channel from its share of first touch and last touch dollars. "More first touch" means first touch share is at least 1.5 times last touch share. "More last touch" means the reverse. "Both" means anything in between. "Too few" means fewer than 5 opportunities on both touches, and it overrides the other labels. These cutoffs and the 25% in step 5 are starting rules the marketer can change, not benchmarks.
5. Apply two data warnings. If direct or unknown is above 25% of either total, label that row "warning" and say channel conclusions are weak. If a campaign started fewer days before the pull date than the short end of the sales cycle, mark it "still maturing" and draw no conclusion from it.
6. Write what can be concluded. Use only statements the data shows, in the form "[channel] was first touch on [number] opportunities worth [amount]". Label anything further as an inference and name its inputs.
7. Write what cannot be concluded. Always include these points: the data does not show that a channel caused pipeline, or whether a deal would have happened anyway, and it says nothing about touches between the first and the last. Add return on spend unless spend was supplied.
8. Name the blind spots. List each information source from personas.md that tracking cannot record, and say that credit for those conversations lands on a later touch. Count answers naming those sources. Answers are self-reported, not credit.
9. Write up to 3 actions, each framed as a test with the number to watch and when to read it. Never recommend cutting a channel from a single touch, or from a channel labeled too few or still maturing.
10. Check the draft against the context pack: pipeline and model wording match goals-and-kpis.md, and channel names match channels-and-tools.md. If a needed field is blank, leave a visible placeholder such as [pull date needed] and ask in the last section. Never invent.
11. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
Status: Draft

## Bottom line
<What the data supports and how far to trust it. Max 40 words.>

## Credit by channel
| Channel | First touch | Last touch | How did you hear about us | Label |
<Dollars and opportunities in each touch column. Include direct or unknown and a total row. Answer counts or "not collected". Label is more first touch, more last touch, both, too few, still maturing or warning.>

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

Assumption: the $900,000 total is CogniATion's Q3 2026 pipeline baseline. The split by channel and the answers are illustrative.

**Bottom line**

Webinars and email appear more as last touch, organic search and social ads as first. Unknown touches top 25% of first touch, so channel conclusions are weak.

**Credit by channel**

| Channel | First touch | Last touch | How did you hear about us | Label |
|---|---|---|---|---|
| Search ads | $252,000 (19) | $180,000 (14) | 9 | Both |
| Organic search | $198,000 (15) | $126,000 (9) | 6 | More first touch |
| Social network ads | $108,000 (8) | $54,000 (4) | 4 | More first touch |
| Webinars | $72,000 (5) | $216,000 (16) | 6 | More last touch |
| Email | $27,000 (2) | $135,000 (10) | 1 | More last touch |
| Direct or unknown | $243,000 (19) | $189,000 (15) | 24 | Warning |
| Total | $900,000 (68) | $900,000 (68) | 50 | |

**What can be concluded**

- Webinars were last touch on 16 opportunities worth $216,000.

**What cannot be concluded**

- Whether webinars caused those deals, or whether they would have happened anyway.

**Blind spots**

- Peers and learning and development associations leave no tracked touch. 18 of the 24 unknown-row answers name them.

**Tests to run**

| Test | Number to watch | Read on |
|---|---|---|
| Invite search ad leads to a webinar for heads of learning | MQL to SQL rate, baseline 26% | End of Q1 2027 |

**Assumptions and open questions**

- Estimate: 68 opportunities is 260 MQLs times the 26% rate, both Q3 2026 baselines.
- Unknown: How much of direct or unknown comes from untagged links?

## How to run it

```
Use the skill "Read attribution". Read the context pack.
Task: <the period, the date pulled, and any tracking changes>.
<paste the CRM export here>
```
