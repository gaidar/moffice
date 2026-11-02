---
title: Plan a product launch
type: skill
function: go-to-market-and-launches
owner: product-marketing-manager
reads: [company, product, personas, messaging, proof-points, goals-and-kpis, channels-and-tools]
you_bring: What the release does in plain words, who confirmed it, and the planned date.
also_for: [release in eight weeks, product launch, new feature, launch plan, launch timeline, announce a release, tell sales about the release, launch dates]
version: 0.1.0
updated: 2026-11-02
summary: Sets the launch tier, timeline, owners and assets for one release, worked back from the launch date and the approval times.
judge: ["Would a customer notice this release if you told them nothing?", "Does the tier reflect what buyers will care about or what the team is proud of?", "What will sales do differently the week after launch?", "What is the one thing you want a buyer to do because of this launch?"]
show_to: your product lead, and ask which promise in it the release could fail to keep
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this for one release with a known scope and a planned date. Do not use it to enter a new segment or market or to bring a new product to market for the first time; use [Write a go-to-market plan](write-gtm-plan.md) instead.

## Inputs

- [[context-pack:company]]: team size and capacity.
- [[context-pack:product]]: current features, known weak spots, what it is not, roadmap rules.
- [[context-pack:personas]]: who the release changes things for.
- [[context-pack:messaging]]: pillars, messages by persona, words to avoid.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:goals-and-kpis]]: goals, baselines, other dated priorities.
- [[context-pack:channels-and-tools]]: channels, approvers and typical times, hard rules.

The marketer supplies: what the release does in plain words, who confirmed it, the planned date, and any early customer feedback or sales requests. No release facts come from anywhere else.

## Procedure

1. Write down what ships, in at most 40 words, from the marketer's description only. If the scope is blank, ask before drafting. If the date or another field is blank, use a placeholder such as [launch date needed], count days back from launch day and ask in the last section.
2. Set the launch tier with these rules, and stop at the first that fits:
   - Tier 1: the release changes who can buy, changes the price, adds a new product, or makes a new claim under a messaging pillar.
   - Tier 2: the release gives current customers or one persona a new capability, or fixes a known weak spot in product.md.
   - Tier 3: a fix or minor improvement.
3. State the one fact that would move the release to another tier.
4. Pick one primary persona, the one the release changes most, or the first in personas.md on a tie (a starting rule), and at most two others. Write one message for each, tied to a pillar and using only what the release does.
5. Build the asset list from the tier, in the order below, which runs from most to least needed. Each asset names the skill that produces it, an owner and a due date.
   - Tier 1: [web page](../content/write-web-page.md), [sales one-pager](../product-marketing-and-sales-enablement/write-sales-one-pager.md), [battlecard update](../product-marketing-and-sales-enablement/write-battlecard.md), [launch email](../content/write-marketing-email.md), [press release](../pr-and-comms/write-press-release.md), [media pitch](../pr-and-comms/write-media-pitch.md), [social posts](../content/write-social-posts.md), [video](../content/write-video-script.md) or [webinar](../events-and-webinars/plan-webinar.md).
   - Tier 2: sales one-pager or update, web page update, launch email, social posts.
   - Tier 3: a mention in the next newsletter, and a release note as a "No skill, ad hoc output".
6. Map proof to each message, using only items whose permission fits the channel. If no proof exists for this release, write a placeholder such as [customer quote needed]. Do not stretch older proof to cover it.
7. Build the timeline backward from launch day, counting L minus working days: launch and after-launch tasks, sales briefed and sales material delivered before anything public, approvals using the typical times in channels-and-tools.md, then production and scope freeze. Plan no public mention before launch day unless product.md clears that roadmap item.
8. Run the capacity check, as the office manual counts it, against company.md and the other dated priorities in goals-and-kpis.md. If effort or days are unknown, write Not assessed. If it does not fit, cut or move assets from the end of the tier's list. Never shorten an approver's typical time. List every cut.
9. Set one or two launch measures from goals-and-kpis.md, with baselines and a date to read them. Leave targets without a basis as placeholders.
10. Write what happens if the release slips: which assets hold, and who tells sales.
11. Write the decision check from the office manual.
12. Check the draft against the context pack: product limits, words to avoid, permission status, hard rules, roadmap rules. Fix anything that contradicts it.
13. List everything assumed, estimated, inferred or unknown in the last section. Schedule [Review launch readiness](review-launch-readiness.md) on the timeline before the first public date.

## Output format

```
Status: Draft
Release: <max 40 words>
Launch date: <date or placeholder>
Launch tier: <1, 2 or 3, plus one-sentence reason>
What would change the tier: <one sentence>

## Audience and messages
| Persona | Message (max 20 words) | Pillar | Proof and permission |

## Assets
| Asset | Skill | Owner | Due | Approver |

## Timeline
| Date or L minus | Task | Owner |

## Capacity
<Who, how much time, what was cut or moved, max 50 words>

## Launch measures
| Measure | Baseline | Target | Read on |

## If the release slips
<Max 40 words>

## Decision check
<five lines, as the office manual sets out>

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does the tier follow from the written rules, with a reason?
- [ ] Is every message free of anything product.md says the product is not?
- [ ] Does every asset have an owner, a due date and the right approver?
- [ ] Do the timeline dates allow each approver's typical time?
- [ ] Is sales briefed before anything goes public?
- [ ] Does the plan fit the team's capacity, with cuts listed?

## Example (fictional company)

**Status:** Draft, internal only.

**Release:** CogniATion Coach manager view. [Release scope needed from Anika Sole.]

**Launch date:** February 2027 [date needed].

**Launch tier:** 2. It gives managers a new capability and changes neither price nor buyer.

**What would change the tier:** If it changes who can buy, it moves to 1.

**Audience and messages**

| Persona | Message | Pillar | Proof and permission |
|---|---|---|---|
| Head of learning | Give managers a team view of reasoning, no individual's conversation shown. | You can see reasoning improve | [Customer quote needed] |

**Assets**

| Asset | Skill | Owner | Due | Approver |
|---|---|---|---|---|
| Web page update | Write a web page | Marketer | L-7 | Anika Sole, 2 days |
| Launch email | Write a marketing email | Marketer | L-5 | Anika Sole, 2 days |
| Sales one-pager | Write a sales one-pager | Marketer | L-7 | Tom Ferrant, 2 days |

**Timeline:** L-10 scope freeze. L-5 sales briefed. L-3 readiness review. L launch, nothing public before.

**Capacity:** One marketer, designer four days a month. Professional services campaign due February 15, so social posts move after launch.

**Launch measures:** Website demo requests, baseline 58 in Q3 2026. Target: [needed]. Read on L+30.

**If the release slips:** Hold public assets. Marketer tells Tom Ferrant.

**Decision check:** Constraint: too little proof. Why this: managers can see progress. Evidence: [needed]. Test: tier 2, not tier 1. Displaces: social posts, after launch.

**Assumptions and open questions**

- Assumption: no price change, view stays at team level, L-minus dates are provisional.
- Unknown: Which February date, is it confirmed, and does the view go below team level?

## How to run it

```
Use the skill "Plan a product launch". Read the context pack.
Task: <what ships, the planned date and who confirmed it>.
```
