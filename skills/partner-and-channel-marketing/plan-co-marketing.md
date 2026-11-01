---
title: Plan co-marketing with a partner
type: skill
function: partner-and-channel-marketing
owner: partner-marketing-manager
reads: [product, icp-and-segments, personas, messaging, proof-points, goals-and-kpis, channels-and-tools]
you_bring: The partner's name, its audience, what it can contribute, each side's budget, and the rules on sharing leads.
also_for: [joint webinar, joint campaign, co-branded content, partner campaign, share leads with a partner, partner event, pipeline through partners, cross promotion]
version: 0.1.0
updated: 2026-11-01
summary: Plans a joint campaign with one partner, including the split of work, lead handling and approvals.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when one named partner has agreed to discuss a joint campaign and you need a plan to take to them. Do not use it for an ongoing referral program, which belongs in [Build a partner kit](build-partner-kit.md). For a campaign you run alone, use [Write a campaign brief](../campaign-design/write-campaign-brief.md) instead.

## Inputs

- [[context-pack:product]]: what the product is not, and integrations that exist, so nothing joint is overstated.
- [[context-pack:icp-and-segments]]: segments and disqualifiers to test the partner's audience against.
- [[context-pack:personas]]: who the campaign speaks to, and where they get information.
- [[context-pack:messaging]]: pillars and words to avoid.
- [[context-pack:proof-points]]: proof and its permission status.
- [[context-pack:goals-and-kpis]]: goals, MQL definition, conversion rates.
- [[context-pack:channels-and-tools]]: channels, tools, approvers and typical times.

The marketer supplies in the prompt: the partner's name, what it sells, its audience, what it can contribute, any agreed terms, each side's budget, and the rules on sharing leads. If the context pack holds nothing about the partner, these facts come from the marketer or stay unknown.

## Procedure

1. Test the fit and give a verdict. Go: the partner's audience overlaps a priority segment, it does not sell what the product does, and it can bring one channel the company lacks. Fix first: one test is unknown. No-go: the partner competes with the product or its audience is mostly disqualified.
2. If no-go, stop and give the reason. If fix first, name the question that settles it and plan on the labeled assumption.
3. Write one joint goal using the MQL definition from goals-and-kpis.md, with a date. Record a different partner goal alongside it, without merging the two.
4. Choose one joint offer that neither side could make alone, such as a webinar, guide or event session. Do not imply an integration or joint product unless product.md lists it.
5. Write the split of work. Each task has one owner, one due date and one cost owner. If the marketer's capacity is unknown, write [capacity needed].
6. Write the lead rules: who collects the form, what consent wording appears, who may contact a lead and when, and how the other side learns the result. If no consent wording was given, write [consent wording needed, check with counsel]. Leads go to both sides only if the form says so.
7. Set the overlap rule for a lead already open in either side's CRM. Default: the existing owner keeps it, labeled as an assumption until both sides agree.
8. List approvals on both sides, using channels-and-tools.md and [partner approver needed]. Each side approves its own name, logo and claims. Use only Public proof in joint material.
9. Build the timeline backward from the start date, leaving room for the longest approval on each side.
10. Set targets with arithmetic shown, using rates from goals-and-kpis.md. If the partner's audience size is unknown, write [audience size needed] and give no registration target.
11. Check the draft against the context pack: what the product is not, disqualifiers, proof status, words to avoid, internal numbers. Fix what contradicts it.
12. List everything assumed, estimated, inferred or unknown in the last section, using those labels.

## Output format

The plan is written to be shared with the partner, so it holds no internal numbers.

```
Status: Draft

## Verdict
<Go, fix first or no-go, with the reason, up to 30 words>

## Joint campaign
Partner: <name, what it sells>
Goal: <one goal, with number and date>
Audience: <segment, persona>
Offer: <up to 25 words>

## Split of work
| Task | Owner | Due | Who pays |

## Lead rules
Collects: <side and form>
Consent wording: <text or placeholder>
Follow-up: <who, how soon>
Overlap: <rule>
Reporting back: <what, when>

## Approvals
| Item | Our approver and time | Partner approver and time |

## Timeline
| Date | Milestone |

## Targets
| Metric | Target | How worked out |

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the verdict rest on the partner's audience and product, not on enthusiasm?
- [ ] Does every task have one owner, one due date and one cost owner?
- [ ] Are lead collection, consent, follow-up and overlap all written down?
- [ ] Do both sides appear in the approvals table?
- [ ] Does the plan avoid implying an integration that product.md does not list?
- [ ] Is every fact about the partner from the marketer, or labeled?
- [ ] Does joint material use only Public proof and no internal numbers?

## Example (fictional company)

Status: Draft

**Verdict.** Fix first. Audience overlap with professional services firms is unconfirmed.

**Joint campaign.** Partner: [partner name needed], a learning and development association that sells memberships and events. Goal: [MQL target needed] by March 31, 2027. Audience: professional services firms, head of learning and development. Offer: joint webinar on showing that training changed how people reason.

**Split of work**

| Task | Owner | Due | Who pays |
|---|---|---|---|
| Webinar setup and registration | CogniATion | [date needed] | CogniATion |
| Invite to association members | Partner | [date needed] | Partner |
| Follow-up to registrants | CogniATion | [date needed] | CogniATion |

**Lead rules.** Collects: CogniATion, on its webinar tool. Consent wording: [consent wording needed, check with counsel]. Follow-up: CogniATion, [response time needed]. Overlap: existing owner keeps the lead. Reporting back: registrant and SQL counts after the webinar.

**Approvals**

| Item | Our approver and time | Partner approver and time |
|---|---|---|
| Lena Marsh quote | Already Public | Not needed |
| Partner name and logo | [approver needed] | [partner approver needed] |

**Timeline.** [dates needed, once the partner confirms].

**Targets.** Webinar attendees who fit the ICP count as MQLs per goals-and-kpis.md. Registration target: [audience size needed].

**Assumptions and open questions**

- Assumption: the partner is an association. No partner is named in the context pack.
- Inference: heads of learning would listen, because personas.md lists learning and development associations as an information source.
- Assumption: the existing lead owner keeps overlaps, until both sides agree.
- Unknown: how many of the association's members work at professional services firms?

## How to run it

```
Use the skill "Plan co-marketing with a partner". Read the context pack.
Task: <the partner, what it sells, its audience and contribution, each side's budget, and lead-sharing rules>.
```
