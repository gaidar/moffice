---
title: Write a campaign brief
type: skill
function: campaign-design
owner: demand-generation-manager
reads: [icp-and-segments, personas, messaging, proof-points, goals-and-kpis, channels-and-tools]
you_bring: The campaign goal, the time window and the budget.
also_for: [plan a campaign, need more leads, demand campaign, generate demand, campaign idea, pipeline campaign, campaign plan, more demo requests]
version: 0.1.0
updated: 2026-11-02
summary: Produces a single-goal campaign brief with audience, offer, channels, assets, timeline and targets.
judge: ["Why would this audience stop what they are doing for this offer?", "Is the offer something they want or something you want them to download?", "If this works what would a salesperson notice the following month?", "Could you run this same campaign for another segment by changing the name?"]
show_to: a salesperson who talks to this segment, and ask whether they would send this offer to a prospect
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this before any multi-channel campaign with one goal, one audience and one time window. Do not use it to promote a product release, which belongs in [Plan a product launch](../go-to-market-and-launches/plan-product-launch.md). For the paid part in detail, use the brief as input to [Plan a paid campaign](../paid-demand-gen/plan-paid-campaign.md) instead of expanding it here.

## Inputs

- [[context-pack:icp-and-segments]]: segments, priority order, disqualifiers, triggers, sales cycle.
- [[context-pack:personas]]: who the campaign speaks to, their objections, where they get information.
- [[context-pack:messaging]]: pillars, messages by persona, words to avoid.
- [[context-pack:proof-points]]: proof available and its permission status.
- [[context-pack:goals-and-kpis]]: goals, budget, baselines, metric definitions.
- [[context-pack:channels-and-tools]]: owned and paid channels, limits, approvers, typical approval times.

The marketer supplies in the prompt: the campaign goal, time window and budget. Optional: an offer idea, days available, and the result and lesson of the last similar campaign.

## Procedure

1. Fix one goal. If the marketer gives two, ask which wins. If they want a draft anyway, use the one named in goals-and-kpis.md and list the other as an open question.
2. Pick one segment and one primary persona. Use the marketer's choice. If none is given, take the top segment in the priority order and the persona that starts the purchase. Name one secondary persona at most.
3. Choose the offer by readiness: a useful resource for people who have not felt the problem yet, a demo or pilot for people who have hit a trigger from icp-and-segments.md. If the offer does not exist yet, add it to the assets table and label it as an assumption.
4. Choose one pillar from messaging.md as the lead message: the first with Public proof that fits the segment's reason to buy (a starting rule). Attach proof from proof-points.md with its status. Use only Public proof in anything the public sees. If a proof item appears in messaging.md but not in proof-points.md, do not treat it as cleared, and ask about it in the last section.
5. Choose channels from channels-and-tools.md only, unless the marketer adds one. Rank them by where the persona gets information. Give each one job: reach, conversion or follow-up. Drop any channel that breaks a limit in that file, and say why.
6. List the assets each channel needs and the skill that produces each one, or [skill title needed] if it is not in your files. If capacity was given and the list exceeds it, cut the lowest-ranked channel first.
7. Set targets using the metric definitions in goals-and-kpis.md. Work each one back from the quarter's goal and show the arithmetic as an estimate. With no share given, use the segment's share of customers (a starting rule). If no baseline exists, write [baseline needed]. Give each target a read date: the date promised, or the window's end plus that stage's timing in goals-and-kpis.md.
8. Build the timeline backward from the start date. Subtract each approver's typical time from channels-and-tools.md, then the production time. If production time is unknown, write [production time needed].
9. If the budget is blank, write [budget needed]. Flag any line that crosses an approval limit in channels-and-tools.md.
10. Write the decision check from the office manual. State which lesson this brief applies.
11. Check the draft against the context pack: segment, words to avoid, proof status, internal-only numbers, channel limits, approvers. Fix what contradicts it.
12. List everything assumed, estimated, inferred or unknown in the last section.

## Output format

```
Status: Draft

## Campaign summary
Name: <short name>
Goal: <one goal, with number and date>
Window: <start date to end date>
Lesson applied: <from which campaign, or "None yet">

## Audience
Segment: <one>
Primary persona: <role, and the trigger to reach them at>
Secondary persona: <role or "None">
Excluded: <disqualifiers>

## Offer
<What they get and what they do, up to 40 words>

## Message
Lead pillar: <one>
Line for the primary persona: <up to 20 words>
Proof: <item, permission status>

## Channels
| Channel | Job | Why this one (up to 15 words) |

## Assets
| Asset | Skill that produces it | Owner | Due |

## Timeline
| Date | Milestone | Approver, if any |

## Targets
| Metric | Baseline | Target | Read on | How worked out |

## Budget
<Total, by line, and any approval needed>

## Decision check
<five lines, as the office manual sets out>

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does the campaign have exactly one goal, one segment and one time window?
- [ ] Is every target defined the way goals-and-kpis.md defines it, with the arithmetic shown?
- [ ] Does each proof item used in public carry Public status in proof-points.md?
- [ ] Does each channel appear in channels-and-tools.md and respect its limits?
- [ ] Does each asset name a skill or a placeholder, an owner and a due date?
- [ ] Do the dates leave room for each approver's typical time?

## Example (fictional company)

Status: Draft

**Campaign summary.** Name: Defend the memo. Goal: 30 SQLs by March 31, 2027. Window: February 15 to March 31, 2027. Lesson applied: None yet.

**Audience.** Segment: professional services firms. Primary persona: head of learning and development, after a company-wide AI assistant rollout or a client complaint about poor reasoning. Secondary persona: managing partner. Excluded: fewer than 100 learners, wants a course library.

**Offer.** A guide to checking the reasoning in client memos, then a demo of CogniATion Coach.

**Message.** Lead pillar: you can see reasoning improve. Line: show that training changed how people reason. Proof: Brightmere Advisory's 22% result on client memo reasoning, Public.

| Channel | Job | Why this one |
|---|---|---|
| Professional social network ads | Reach | Finds heads of learning by job title |
| Search ads | Conversion | Reaches firms already looking |
| Email list | Follow-up | 5,400 contacts to start from |

**Assets.** Guide, then landing page: [Write a web page](../content/write-web-page.md), marketer, February 8.

**Timeline.** February 15: campaign live, the date in goals-and-kpis.md.

**Targets.** SQLs: baseline [needed]. Target 30, a third of the 90 goal, read March 31. MQLs: baseline 260 for all campaigns. Target 116, read March 31.

**Budget.** [budget needed]. Any line over $5,000 goes to Marta Ilves, 3 days.

**Decision check.** Constraint: too few relevant buyers. Why this: no campaign reaches this segment yet. Evidence: [needed]; under 58 MQLs at mid-window would disprove it. Test: page and email first. Displaces: a third blog post.

**Assumptions and open questions**

- Assumption: the marketer gave this campaign a third of the SQL goal.
- Estimate: 116 MQLs is 30 SQLs divided by the 26% MQL to SQL rate, rounded up.
- Unknown: how much of the $70,000 quarter budget goes to this campaign?

## How to run it

```
Use the skill "Write a campaign brief". Read the context pack.
Task: <the goal, the time window, the budget, and any offer idea>.
```
