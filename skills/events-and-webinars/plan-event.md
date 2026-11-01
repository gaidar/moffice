---
title: Plan an event
type: skill
function: events-and-webinars
owner: events-and-webinar-manager
reads: [company, product, icp-and-segments, personas, messaging, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
you_bring: The event name, dates and location, the organizer's attendee information, the quotes, and who can staff it.
also_for: [trade show, conference booth, should we sponsor, event roi, sponsorship decision, booth planning, in-person event, leads from events]
version: 0.1.0
updated: 2026-11-01
summary: Produces a trade show or in-person event plan with a decision, targets, budget, booth or session, lead capture and timeline.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when you are deciding on or preparing for a trade show or other in-person event. Do not use it for an online session; use [Plan a webinar](plan-webinar.md) instead. Once the event is over, use [Follow up after an event](follow-up-after-event.md).

## Inputs

- [[context-pack:company]]: sales team, nameable people, internal numbers.
- [[context-pack:product]]: what can be shown in a demo.
- [[context-pack:icp-and-segments]]: fit criteria, disqualifiers, segment priority.
- [[context-pack:personas]]: who to talk to, their objections.
- [[context-pack:messaging]]: pillars, words to avoid.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:brand-voice]]: rules for booth copy.
- [[context-pack:goals-and-kpis]]: MQL and SQL definitions, conversion rates, quarter budget.
- [[context-pack:channels-and-tools]]: channels, approvers, spending limits.

The marketer supplies the event name, dates and location; the organizer's attendee information; quotes for the booth or session, travel and materials; and who can staff it.

## Procedure

1. Make the attendance decision from the organizer's attendee information, which is the organizer's claim. Go: attendees include ICP companies in the first or second priority segment. Go smaller: only a lower segment or part of the ICP. Do not attend: no match. No information: Unknown, and state what would make it Go.
2. Set one goal and work out the targets. Use: break-even SQLs = total cost ÷ (average contract value × SQL to won rate), and MQLs needed = SQLs ÷ MQL to SQL rate. Round up and show the math as an estimate. If a value is blank, write [contract value needed] or [rate needed].
3. If a booth conversation would not count under the MQL definition in goals-and-kpis.md, say so and name the step that makes it count, such as logging a demo request.
4. Build the budget. List fee, travel, materials, giveaways and lead capture. Each amount comes from a quote the marketer supplied, or reads [quote needed]. Show the total and its share of the quarter budget. Flag each line that passes the spending limit in channels-and-tools.md, with the approver and approval time.
5. Write the presence. Default to a booth, and add a session only if the organizer offers a slot and the topic works without a pitch. Write a headline that follows brand-voice.md, proof to show, one demo, and up to three qualifying questions drawn from the ICP situation and triggers. Anything visible to the public uses only proof marked public, and sales only proof stays one-to-one. Leave out roadmap items and anything marked internal.
6. Plan staffing. Each open hour needs two people, and one of them sells. Use names the marketer gave, or [person needed].
7. Set lead capture. Fields: name, company, title, email, ICP fields, current method, trigger, tier, next step, consent status. Tiers: A asked for a demo or named a trigger, and fits; B fits, with no ask; C everything else. Staff tier leads on the spot. Have legal confirm the consent wording.
8. Build the timeline by counting back from the first event day, with real dates: 8 weeks, approvals and booking; 6 weeks, design brief; 4 weeks, invitations; 2 weeks, personal outreach by sales; 1 week, staff briefing; next business day after the event, Tier A follow-up. If fewer than 8 weeks remain, compress and say what is at risk. Add approval time from channels-and-tools.md. Use only channels listed there. These times and the staffing rule are starting rules the marketer can change.
9. Check the draft against the context pack: fit rules, permissions, words to avoid, approvers, spending limits.
10. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
## Event plan: <event>, <dates>, <location>

Decision: <Go, Go smaller, Do not attend or Unknown>, <reason, 25 words at most>
Status: Draft, <internal only, if it holds internal numbers>

## Goal and targets
Goal: <one sentence>
| Measure | Target | How worked out |

## Budget
| Line | Amount or [quote needed] | Approver if over limit |
Total: <amount, share of quarter budget>

## Booth or session
Format: <booth, session or both>
Headline: <10 words at most>
Proof shown: <items, each marked public>
Demo: <25 words at most>
Qualifying questions: <up to 3>
Do not say: <up to 4 items>

## Staffing
<who covers what, 3 lines at most>

## Lead capture
Fields: <list>
Tiers: <A, B and C rules, one line each>
MQL rule: <how a booth lead counts, 25 words at most>

## Timeline
| Date | Step | Owner | Skill or approver |

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does the decision rest on attendee information you supplied, or say Unknown?
- [ ] Is every budget amount from a quote, or marked as [quote needed]?
- [ ] Does the plan say how a booth lead counts under your MQL definition?
- [ ] Is everything visible at the booth limited to proof marked public?
- [ ] Are the lead tiers the same ones your follow-up will use?

## Example (fictional company)

**Event plan: regional learning and development conference, March 9 to 11, 2027, [location needed]**

Decision: Unknown. Go if attendees include ICP firms in the top two segments.
Status: Draft, internal only.

**Goal and targets**

Goal: book demos with heads of learning.

| Measure | Target | How worked out |
|---|---|---|
| SQLs | 1 | $18,000 ÷ ($81,000 × 24%) = 0.9 |
| MQLs | 4 | 1 ÷ 26% = 3.8 |

**Budget**

Booth fee and travel [quote needed]. Total: $18,000 assumed, about 26% of $70,000. Lines over $5,000: Marta Ilves, 3 days.

**Booth or session**

Format: booth
Headline: Your analysts have answers. Can they defend them?
Proof shown: median of 9 days to first live session (public); Lena Marsh quote (public).
Demo: try a client memo scenario, see CogniATion Coach decline to answer, view a sample team report.
Qualifying questions: Have you rolled out a general AI assistant? How many people would you train?
Do not say: roadmap items, the February release, individual scores.

**Staffing**

Marketer and [account executive needed].

**Lead capture**

Fields: contact details, employees, people to train, current method, trigger, tier, next step, consent.
Tiers: A asked for a demo or named a trigger. B fits, no ask. C the rest.
MQL rule: log demo requests on the spot. A scan alone is not an MQL.

**Timeline**

| Date | Step | Owner | Skill or approver |
|---|---|---|---|
| Feb 1 | Book booth | Marketer | Over $5,000: Marta Ilves |
| Mar 12 | Tier A follow-up | Sales | Follow up after an event |

**Assumptions and open questions**

- Assumption: total cost of $18,000.
- Estimate: targets use internal contract value and Q3 2026 rates, rounded up.
- Unknown: what are the organizer's attendee list and booth price?

## How to run it

```
Use the skill "Plan an event". Read the context pack.
Task: <the event, dates, location and who can staff it>.
<paste attendee information and quotes here>
```
