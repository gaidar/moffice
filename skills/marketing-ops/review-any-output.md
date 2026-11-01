---
title: Review any output
type: skill
function: marketing-ops
owner: marketing-reviewer
reads: [company, product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Critiques any output against the context pack and its originating skill's checklist, without rewriting it.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this before anything public, or anything with a customer name or a number, is used. Do not use it for messaging and positioning, which get [Review messaging](../positioning-and-messaging/review-messaging.md), or for a launch plan, which gets [Review launch readiness](../go-to-market-and-launches/review-launch-readiness.md). To judge results after they happen, use [Evaluate a campaign](../analytics-and-campaign-evaluation/evaluate-campaign.md) instead.

## Inputs

- [[context-pack:company]]: which numbers are publishable, internal only or never to be mentioned.
- [[context-pack:product]]: what the product does, what it is not, prices and roadmap limits.
- [[context-pack:icp-and-segments]]: whether the audience fits.
- [[context-pack:personas]]: whether the output speaks to the right person.
- [[context-pack:messaging]]: claims, proof and words to avoid.
- [[context-pack:competitors]]: competitor facts, with sources and dates.
- [[context-pack:proof-points]]: permission status of each customer, number and quote.
- [[context-pack:brand-voice]]: voice rules for public copy.
- [[context-pack:goals-and-kpis]]: definitions and targets.
- [[context-pack:channels-and-tools]]: hard rules and who approves what.

The marketer pastes into the chat:

- The output to review, in full.
- The title of its originating skill, and that skill's quality checklist if it is not in the files available.
- Where it will appear: public, one-to-one sales or internal.

## Procedure

1. Set the audience from the marketer's statement. If none was given, review it as public, the strictest case, and record that as an assumption.
2. Find the originating skill's quality checklist. If it is not available, ask for it. If the marketer wants the review anyway, write "checklist not run" and do not improvise one from the skill's title.
3. Go through the output line by line and list each factual claim, name, number, quote, price, date and competitor statement.
4. Check each item against the context pack and mark it supported, contradicted or not found. Anything not found is a problem unless it is a visible placeholder. If a file needed for a check is blank, write "could not check" and ask. Never invent.
5. Apply the permission check for the audience. Every customer name, number and quote must have a status in proof-points.md that allows this use. Every company number must have a status in company.md that allows it.
6. Check the product limits in product.md, the competitor sources in competitors.md, and the hard rules in channels-and-tools.md.
7. For public copy, check the words to avoid in messaging.md and the rules in brand-voice.md.
8. Run the originating skill's checklist. Answer each question yes or no, with the line or fact that shows it.
9. Sort every problem. A blocker is a contradicted or unsupported fact, a permission breach, an unannounced roadmap item, a broken product limit, a breach of a hard rule or an invented placeholder fill. A fix is a word to avoid, a voice problem, a missing template field, a length breach or a failed checklist item that is not already a blocker.
10. Set the verdict. Any blocker means "Do not use yet". No blockers and at least one fix means "Fix first". Neither means "Ready for your decision". Never call the output approved, since only the marketer changes its status.
11. List the approvers from channels-and-tools.md that this output needs.
12. Say what to change in each problem row, in one line. Do not rewrite the output unless the marketer asks.
13. List every assumption, estimate, inference and unknown in the last section, including anything you could not check.

## Output format

```
Status: Draft

## Verdict
<Do not use yet, Fix first, or Ready for your decision, with the count of blockers and fixes. Max 30 words.>

## Blockers
| Where | Problem | Source | What to change |
<One row per blocker, or "None". What to change max 15 words.>

## Fixes
| Where | Problem | Source | What to change |
<One row per fix, or "None". What to change max 15 words.>

## Checklist results
| Question | Yes or no | Evidence |
<One row per question in the originating skill's checklist, or "checklist not run".>

## Approvals needed
<Up to 4 bullets: what needs approval, who approves and typical time.>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Was every claim, name, number and quote checked, not just the obvious ones?
- [ ] Was the permission check run for the stated audience?
- [ ] Does each problem name the context pack file behind it?
- [ ] Do the verdict and the problem sorting follow the rules?
- [ ] Was the originating skill's real checklist used, or marked as not run?
- [ ] Are the approvers named from channels-and-tools.md?
- [ ] Did the review stay a critique, with no rewrite unless asked?

## Example (fictional company)

Status: Draft

Assumption: the draft below is an illustrative CogniATion search ad, reviewed as public. It was deliberately written with errors, and is not usable copy.

Draft reviewed: "Unlike Arguvia, CogniATion Coach raises IQ and makes your analysts smarter. 64 customer companies live. The manager view arrives in February."

**Verdict**

Do not use yet. 3 blockers, 1 fix.

**Blockers**

| Where | Problem | Source | What to change |
|---|---|---|---|
| "Unlike Arguvia" | Competitor name in an ad | channels-and-tools.md, hard rules | Remove the name |
| "raises IQ" | Claim about intelligence | channels-and-tools.md, hard rules; product.md, what it is not | Describe practice on reasoning, with no intelligence claim |
| "arrives in February" | Roadmap, internal only | product.md, goals-and-kpis.md | Remove the line |

**Fixes**

| Where | Problem | Source | What to change |
|---|---|---|---|
| "smarter" | Word to avoid | messaging.md | Use "reasoning" or "judgment" language |

**Checklist results**

| Question | Yes or no | Evidence |
|---|---|---|
| Are competitors left out if channels-and-tools.md forbids naming them? | No | "Unlike Arguvia" |

**Approvals needed**

- Ads go to the marketer, same day.
- Product claims go to Anika Sole, VP product, if this runs as launch copy, 2 days.

**Assumptions and open questions**

- Assumption: the originating skill is [Write ad variations](../paid-demand-gen/write-ad-variations.md). One checklist question is shown, condensed for length.
- Inference: "64 customer companies" is publishable, from company.md, as of September 30, 2026.
- Unknown: What character limits apply?

## How to run it

```
Use the skill "Review any output". Read the context pack.
Task: <review which output, for which audience, with the output and its originating skill named below>.
```
