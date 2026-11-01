---
title: Build a market segmentation
type: skill
function: segmentation-icp-and-personas
owner: insights-analyst
reads: [icp-and-segments, product, channels-and-tools, goals-and-kpis]
you_bring: A customer export with industry, size, contract value, days to close and status, plus won and lost deals if you have them.
also_for: [which market to target, market segments, who should we sell to, target market, rank segments, focus on one segment, too many markets, where is demand]
version: 0.1.0
updated: 2026-11-02
summary: Splits the market into segments and ranks them from data the marketer supplies.
judge: ["Would you actually market differently to these segments or are they only different labels?", "Can you reach the top segment through a channel you already have?", "Did the top segment win on buying evidence or because its data was easier to find?", "What will you stop doing for the segments at the bottom?"]
show_to: your sales lead, and ask whether the top segment matches the deals they would chase first
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this skill to split your market into segments and rank them, usually once a quarter or before a new go-to-market plan. Do not use it to set company-level fit rules; use [Define the ICP](define-icp.md) instead. To describe the people inside a segment, use [Write a persona](write-persona.md).

## Inputs

- [[context-pack:icp-and-segments]]: current segments, priority order, sales cycle and triggers.
- [[context-pack:product]]: "What it is not" and known weak spots, which can rule a segment out.
- [[context-pack:channels-and-tools]]: channels that already reach a segment.
- [[context-pack:goals-and-kpis]]: goals and events that already point at a segment.

The marketer pastes into the chat:

- A customer export with industry, size, contract value, days to close and whether the customer is still active.
- A deal export with won and lost deals, if available.
- Any market size figures, each with its source. Without them, market size stays unknown.

## Procedure

1. Read the inputs. If neither the marketer's data nor the segments in icp-and-segments.md exist, ask for one of them and stop. If only the context pack exists, proceed and mark every rank as provisional.
2. Group the companies by shared need and way of buying. Keep two groups separate only if they differ on what triggers the purchase, who signs or how long the deal takes. Merge them if they differ only by industry label. End with 3 to 6 segments.
3. Apply the product gate. If a segment's main need matches an item under "What it is not" in product.md, move it to "Not served" with the reason, and do not score it.
4. Score Need for each remaining segment. Give 3 if an outside party forces the purchase, such as a regulator or the buyer's own customer. Give 2 if the driver is a recurring cost the buyer feels. Give 1 if the purchase is optional.
5. Score Win ease by comparing segments on days to close and price pressure. Give 3 to the best segment, 1 to the worst and 2 to any in between.
6. Score Retention the same way, from active and churned customers. Give 3 to the best, 1 to the worst and 2 to any in between.
7. Score Reach. Give 3 if a channel in channels-and-tools.md or an event in goals-and-kpis.md already targets the segment. Give 2 if it is reachable through inbound or new spend alone. Give 1 if no route is known.
8. When data for a score is missing, give it 1, write "unknown" beside it and mark the segment's rank provisional. Do not infer a score from general knowledge of an industry.
9. Add the scores and rank the segments. Break ties by Retention, then Win ease. The scoring scale and the segment count are starting rules the marketer can change, not benchmarks. Market size is shown but not scored, because it is often unavailable and a large segment you cannot win is no use.
10. Write the recommendation: the top segment gets first call on effort, the second gets a defined smaller share of effort, and the rest get inbound only or nothing. Say which.
11. Check the draft against the context pack: compare the rank with the priority order in icp-and-segments.md and list every difference with the data behind it. Keep internal numbers marked internal.
12. List everything you assumed, estimated, inferred or could not find in the last section, including each unknown score and missing market size.

## Output format

```
Status: Draft
Data used: <sources and row counts, one line>

## Ranked segments
| Rank | Segment | Need | Win ease | Retention | Reach | Total | Share of customers | Market size |
<one row per segment, 3 to 6 rows; scores 1 to 3; "unknown" beside any defaulted score; market size with source, or "unknown">

## Segment definitions
- <segment name>: <shared need, way of buying and how to recognize a company in it, up to 50 words each>

## Not served
- <segment and reason from product.md, up to 25 words each, or "None">

## Recommendation
<where effort goes first, second and not at all, up to 80 words>

## Changes to icp-and-segments.md
- <field, current text, proposed text, data behind it, up to 40 words each, or "None">

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every score trace to pasted data or a named context pack file, or say "unknown"?
- [ ] Are segments split by need and way of buying, not by industry label alone?
- [ ] Is every scored segment's main need something the product can meet?
- [ ] Is market size either sourced or marked unknown?
- [ ] Is every difference from the current priority order listed with its data?
- [ ] Do the totals add up, and do ties follow the stated rule?
- [ ] Are internal numbers marked internal, so this output does not get reused in public copy?

## Example (fictional company)

**Status:** Draft

**Data used:** icp-and-segments.md, product.md and goals-and-kpis.md only, no export pasted. All ranks provisional.

**Ranked segments**

| Rank | Segment | Need | Win ease | Retention | Reach | Total | Share of customers (internal) | Market size |
|---|---|---|---|---|---|---|---|---|
| 1 | Professional services | 3 | 3 | 1 unknown | 3 | 10 | 45% | unknown |
| 2 | Financial services | 2 | 1 | 3 | 2 | 8 | 20% | unknown |
| 3 | Software companies | 1 | 2 | 1 unknown | 2 | 6 | 35% | unknown |

**Segment definitions**

- Professional services: consulting, accounting and law. Junior staff's reasoning reaches clients. Fastest sales cycle.
- Financial services: banks, insurers and asset managers. Analysts' judgment carries risk. Longest security review.
- Software companies: buy to build decision-making in new managers. Most price-sensitive.

**Not served:** Buyers wanting a course library, which CogniATion Coach is not.

**Recommendation:** Professional services first, with the February campaign. Financial services second, about a quarter of effort (assumption). Software companies inbound only.

**Changes to icp-and-segments.md:** None. The rank matches the current priority order.

**Assumptions and open questions**

- Inference: professional services Need 3 treats a client complaint, a trigger in icp-and-segments.md, as outside pressure.
- Inference: professional services Reach 3 comes from the campaign in goals-and-kpis.md. The conference names no segment, so earns no credit.
- Inference: Win ease and Retention come from notes in icp-and-segments.md, with security reviews ranked worse than price pressure.
- Unknown: what are days to close and retention by segment, and any sourced market size?

## How to run it

```
Use the skill "Build a market segmentation". Read the context pack.
Task: <any market size figures, with sources>.
<paste the customer and deal exports here>
```
