---
title: Write a go-to-market plan
type: skill
function: go-to-market-and-launches
owner: product-marketing-manager
reads: [company, product, icp-and-segments, personas, messaging, competitors, proof-points, goals-and-kpis, channels-and-tools]
you_bring: What the plan is for, the start date, the budget, and any research on the target.
also_for: [go to market, gtm strategy, new segment, new market, new product, enter a market, sell to a new audience, market entry]
version: 0.1.0
updated: 2026-11-02
summary: Produces a go-to-market plan for one new product, new segment or new market, with a fit decision, route to market, phases, targets and a capacity check.
judge: ["Why would a buyer in this market choose you over doing nothing?", "Who is the first customer you could name and how would you reach them this month?", "Does sales have the time and a reason to sell this next to what they already sell?", "What result would make you stop and is anyone willing to actually stop?"]
show_to: your sales lead and your product lead, and ask what would make them pull out of this plan
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this for a new product, a new segment or a new market. Do not use it for one release of an existing product; use [Plan a product launch](plan-product-launch.md) instead. For one campaign inside an existing plan, use [Write a campaign brief](../campaign-design/write-campaign-brief.md).

## Inputs

- [[context-pack:company]]: team and publishable numbers.
- [[context-pack:product]]: what it is and is not, price, weak spots.
- [[context-pack:icp-and-segments]]: ICP, disqualifiers, segment priority, sales cycle, triggers.
- [[context-pack:personas]]: roles, objections, where they get information.
- [[context-pack:messaging]]: positioning, pillars, words to avoid.
- [[context-pack:competitors]]: sourced facts and what buyers do today.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:goals-and-kpis]]: goals, budget, baselines.
- [[context-pack:channels-and-tools]]: channels, limits, approvers, hard rules.

The marketer supplies: what the plan is for, the start date, the budget, and any research on the target, such as notes or market data with its source.

## Procedure

1. Classify the plan as new product, new segment or new market. If it fits more than one, plan for the one that changes most and list the others under Unknown.
2. Run the fit check: compare the target with the ICP, the disqualifiers and "what it is not" in product.md, plus language, region and integration limits for a new market. If the target meets a disqualifier or needs something the product does not do, write "Recommend against as written" on the decision line, name what would have to change, and still complete the plan.
3. If a blank changes the target or the decision, ask all such questions together before drafting. If it affects a detail, leave a placeholder in square brackets and ask in the last section. Never invent a market size, competitor move, customer or price.
4. Write the target: segment, personas, trigger. Use only the context pack and the marketer's research.
5. Restate the positioning for this target in at most 40 words. Keep the existing pillars. If the research contradicts one, keep it and ask in the last section.
6. Map proof to each pillar, using only items whose permission status fits the use. Mark any pillar with no public proof from this target as a gap, and make closing it a task in phase 1.
7. Pick one primary route: sales-led, inbound or partner. Choose inbound if icp-and-segments.md says the segment is served through inbound only, or if the marketer says sales has no capacity for it. Choose partner only if the marketer names a partner. Otherwise choose sales-led. Name at most three channels for phase 1, taken from channels-and-tools.md and from where the personas get information.
8. Write three phases: prepare, first test, expand. Each has dates, tasks, an owner and one exit test. The first test runs at the smallest size that can pass or fail its exit test. A phase starts only when the last one's exit test is met.
9. Set targets from goals-and-kpis.md, using its definitions and baselines. Label any split or backward calculation as an estimate and show the math. With no baseline, leave a placeholder.
10. Run the capacity check: count the team in company.md against the tasks, cut tasks until they fit, and list the cuts. List each approval and its typical time from channels-and-tools.md.
11. Check the draft against the context pack: product limits, words to avoid, permission status, hard rules. Fix anything that contradicts it.
12. List everything assumed, estimated, inferred or unknown in the last section.

## Output format

```
Status: Draft
Decision: <Proceed, Proceed with conditions, or Recommend against as written, plus one sentence why>
Plan type: <New product, new segment or new market>

## Target
- Segment: <one line>
- Personas: <champion, approver, signer, one line each>
- Trigger: <one line>
- Fit check: <max 40 words, including disqualifiers checked>

## Positioning for this target
<Max 40 words>

## Proof by pillar
| Pillar | Proof | Permission | Gap |

## Route to market
- Primary route: <sales-led, inbound or partner, with one-sentence reason>
- Phase 1 channels: <max 3>
- Competitor to expect: <one line per competitor, sourced, max 3>

## Phases
| Phase | Dates | Tasks (max 5) | Owner | Exit test |

## Targets
| Metric | Baseline | Target | Date | Basis |

## Budget and capacity
- Budget: <amount or placeholder>
- Capacity: <who, how much, what was cut>
- Approvals: <item, approver, typical time>

## Risks
<Max 3, each with the response>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the decision line appear first, and does it follow from the fit check?
- [ ] Does each pillar show proof with a permission status, or a named gap?
- [ ] Does each phase have an owner and an exit test that can fail?
- [ ] Is every split or calculated target labeled as an estimate with the math shown?
- [ ] Does the work fit the team, with cuts and approvers listed?

## Example (fictional company)

**Status:** Draft

**Decision:** Proceed with conditions. Financial services fits the ICP, but has no approved customer proof yet.

**Plan type:** New segment, moving financial services to active outreach.

**Target:** Banks, insurers and asset managers. Champion: head of learning. Approver: VP of people. Trigger: company-wide AI assistant rollout. Fit check: no disqualifier met.

**Positioning for this target:** For heads of learning at financial services firms whose analysts now lean on AI assistants, CogniATion Coach makes analysts practice reasoning on real work problems, because the chatbot declines to give the answer.

**Proof by pillar:** It asks: Lena Marsh quote, public, professional services, so a gap. Practice: 72% weekly completion, all customers, public. Reasoning improves: Brightmere Advisory result, same gap.

**Route to market:** Sales-led. Phase 1 channels: email list, webinar, learning and development conference. Expect Elenchly (completion data and quiz scores, per three prospects, 2026).

**Phases:** Prepare, by January 15, 2027: close the proof gap, draft security review answers; exit test is one approved customer. First test: through March 31. Expand: [date needed].

**Targets:** Pipeline $240,000 by March 31, 2027.

**Budget and capacity:** [Budget needed from the $70,000 quarter]. One marketer, designer four days a month. Budget over $5,000 per item: Marta Ilves, three days.

**Risks:** No proof by January 15: delay the first test. Long security reviews: read pipeline, not wins.

**Assumptions and open questions**

- Assumption: this segment is not yet in active outreach, and phase dates are a first pass.
- Estimate: $240,000 is the 20% customer share (internal) times the $1.2 million goal, not a forecast.
- Unknown: How much budget and sales time does this segment get?

## How to run it

```
Use the skill "Write a go-to-market plan". Read the context pack.
Task: <the new product, segment or market, the start date and the budget>.
<paste any research here, with its source>
```
