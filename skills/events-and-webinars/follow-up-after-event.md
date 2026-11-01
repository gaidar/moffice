---
title: Follow up after an event
type: skill
function: events-and-webinars
owner: events-and-webinar-manager
reads: [company, product, icp-and-segments, messaging, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Sorts event or webinar leads into tiers, drafts follow-up messages and writes the handoff to sales.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this right after a trade show, in-person event or webinar, once you have the lead list. Do not use it for a long series of emails; use [Design a nurture sequence](../campaign-design/design-nurture-sequence.md) instead. To set the permanent rules between marketing and sales, use [Define the lead handoff](../marketing-ops/define-lead-handoff.md).

## Inputs

- [[context-pack:company]]: the sales team.
- [[context-pack:product]]: what can be promised and what it is not.
- [[context-pack:icp-and-segments]]: fit criteria, disqualifiers, triggers, segment priority.
- [[context-pack:messaging]]: messages by persona, words to avoid.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:brand-voice]]: rules for all messages.
- [[context-pack:goals-and-kpis]]: MQL and SQL definitions, and how pipeline is credited.
- [[context-pack:channels-and-tools]]: approvers and hard rules.

The marketer pastes the lead list with only the fields this skill needs: name, company, title, email, ICP fields, what the person did (demo request, conversation, scan, attended, no-show), staff notes, tier if captured at the event, and consent status. Also the event name and dates, what was promised on site, and the routing of leads to sellers. Remove anything else before pasting.

## Procedure

1. Stop and ask if no lead list is pasted. Count rows, merge duplicates and list missing fields. Do not guess fit from the company name: mark it Fit unknown.
2. Remove from follow-up, and say why: existing customers (send to their account owner), competitors, vendors, students, anyone outside the ICP region, and anyone matching a disqualifier. A lead whose consent status is no or missing gets no marketing email. Flag those for the marketer to decide.
3. Assign one tier to each remaining lead, keeping any event tier that the data supports:
   - Tier A: fits the ICP, and asked for a demo, pricing or a call, or named a trigger from icp-and-segments.md. A personal message from sales, within 1 business day.
   - Tier B: fits the ICP, had a conversation or attended, with no ask. A marketing email within 2 business days, then nurture.
   - Tier C: Fit unknown, scan only, or no-show. A resource email within 5 business days, then nurture. No sales contact.
   These windows are starting rules the marketer can change.
4. Mark MQL status separately from tier, using the exact definition in goals-and-kpis.md. Never mark anyone SQL, since sales decides that. If the definition is blank, write [MQL definition needed].
5. Draft one message per tier, plus a no-show version for webinars: subject of 50 characters or fewer, body of 120 words or fewer, one ask. Refer only to conversations in the notes, and mark where the Tier A sender adds a detail with [personal detail from notes]. Use proof marked public, or one-to-one proof only in Tier A messages that one seller sends to one person.
6. Write the sales handoff for Tier A, one row per lead. Use [seller needed] if routing is missing. Rank by segment priority, then by whether a trigger was named. If Tier A may exceed what sales can take that week, ask the marketer, and say which leads to contact first.
7. Build the calendar with real dates: Tier A, Tier B, Tier C, then a check with sales 14 days after the event on accepted and rejected leads. Add approval time before sending from channels-and-tools.md, and route sales messages to the approver listed there.
8. Set the report: leads, tiers, MQLs, SQLs, pipeline credited under the attribution model in goals-and-kpis.md. Compare with event targets if the marketer pastes the plan. Leave anything not yet known as [figure needed], and pass results to [Evaluate a campaign](../analytics-and-campaign-evaluation/evaluate-campaign.md).
9. Check the draft against the context pack: every claim, permission, word to avoid, internal number and roadmap item.
10. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
Status: Draft

## Event follow-up: <event>, <dates>

Rows in: <n>. Duplicates: <n>. Removed: <n, with reasons>.

## Lead tiers
| Tier | Count | MQLs | Action | Sender | Due date |

## Messages
Tier A
Subject: <50 characters at most>
Body: <120 words at most, one ask>
Tier B
<same fields>
Tier C
<same fields>
No-show, webinars only
<same fields>

## Sales handoff
| Rank | Lead | Title and company | Fit evidence | Trigger | Next step | Seller | Due |

## Calendar
| Date | Step | Owner | Approver |

## Report
| Measure | Count | Target if supplied | Next read date |

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Do tier counts add up to the rows in, minus duplicates and removals?
- [ ] Is MQL status marked by your definition, with nobody marked SQL?
- [ ] Does each message refer only to what happened, with one ask and no invented talk?
- [ ] Do leads without consent stay off marketing email?
- [ ] Does every message use only proof with the right permission and no internal number?

## Example (fictional company)

**Status:** Draft

**Event follow-up: regional learning and development conference, March 9 to 11, 2027**

Rows in: 62. Duplicates: 2. Removed: 4 (two customers, two under 100 learners).

**Lead tiers**

| Tier | Count | MQLs | Action | Sender | Due date |
|---|---|---|---|---|---|
| A | 9 | 6 | Personal message | [seller needed] | Mar 12 |
| B | 19 | 0 | Marketing email | Marketer | Mar 15 |
| C | 28 | 0 | Resource email | Marketer | Mar 18 |

**Messages** (Tier A shown)

Tier A
Subject: Showing your training changed the work
Body: [First name], you asked how to show your leadership team that training changed how people reason. [personal detail from notes]. CogniATion Coach questions employees about a work problem and scores their reasoning against a rubric. You see progress by team, and never an individual's conversation. Can I show you on a call this week?

**Sales handoff**

| Rank | Lead | Title and company | Fit evidence | Trigger | Next step | Seller | Due |
|---|---|---|---|---|---|---|---|
| 1 | [lead name] | Head of learning, [accounting firm] | 150 people to train | AI assistant rollout | Demo | [seller needed] | Mar 12 |

**Calendar**

| Date | Step | Owner | Approver |
|---|---|---|---|
| Mar 5 | Approve Tier A text | Marketer | Tom Ferrant |

**Report:** 6 MQLs against a target of 4. Next read Mar 25.

**Assumptions and open questions**

- Assumption: all counts and the sample lead are invented.
- Assumption: Tier A text counts as sales material, Tom Ferrant, 2 days.
- Inference: 6 Tier A leads requested demos, so they meet the MQL definition.
- Unknown: how are leads routed across the three account executives?

## How to run it

```
Use the skill "Follow up after an event". Read the context pack.
Task: sort the leads pasted below from <event> and draft the follow-up and sales handoff.
```
