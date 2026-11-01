---
title: Write a lead follow-up
type: skill
function: campaign-design
owner: demand-generation-manager
reads: [icp-and-segments, personas, messaging, product, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
you_bring: The leads from your form, download or demo request, or the source you want rules for, and how sales routes them.
also_for: [demo request follow up, follow up on leads, inbound leads, contact form leads, download leads, leads going cold, how fast to call leads, what to send new leads]
version: 0.1.0
updated: 2026-11-02
summary: Sorts leads from a form, a download or a demo request into tiers and writes the timing, the messages and the handoff to sales.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when leads arrive from a form, a download or a demo request, not from an event. Do not use it for an event or webinar list; use [Follow up after an event](../events-and-webinars/follow-up-after-event.md) instead. It stops after three messages, so for a longer series use [Design a nurture sequence](design-nurture-sequence.md). For the permanent rules with sales, use [Define the lead handoff](../marketing-ops/define-lead-handoff.md).

## Inputs

- [[context-pack:icp-and-segments]]: fit, disqualifiers, triggers, segment priority.
- [[context-pack:personas]]: who is writing in.
- [[context-pack:messaging]]: messages by persona, words to avoid.
- [[context-pack:product]]: what can be promised, and any pilot.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:brand-voice]]: rules for all messages.
- [[context-pack:goals-and-kpis]]: MQL and SQL definitions.
- [[context-pack:channels-and-tools]]: approvers and hard rules.

The marketer supplies the source (which form, resource or demo page) and how leads reach sellers. To sort actual leads, paste a list with only: name, company, title, email, ICP fields, what the person did and when, and consent status.

## Procedure

1. If no source is named, ask. With a list, count rows, merge duplicates and list missing fields. With no list, write the rules and messages, with [n] and [lead] as placeholders. Mark fit you cannot confirm as Fit unknown.
2. Remove, and say why: existing customers (send to their account owner), competitors, vendors, students, anyone outside the ICP region, anyone matching a disqualifier. A lead whose consent is no or missing gets no marketing email, and the marketer decides.
3. Assign one tier to each remaining lead. A Tier B or C lead who replies with an ask moves to Tier A.
   - Tier A: asked for a demo, pricing or a call. Personal messages from sales, on business days 1, 3 and 7.
   - Tier B: fits the ICP, filled in a form or downloaded, with no ask. Marketing emails on business days 2 and 7.
   - Tier C: Fit unknown or partial fit, with no ask. One resource email on business day 5. No sales contact.
   These windows and message counts are starting rules the marketer can change.
4. Set the stop rules. A reply or an opt-out stops all messages. After the last message, a lead that fits the ICP goes to [Design a nurture sequence](design-nurture-sequence.md), and any other lead closes.
5. Mark MQL status separately from tier, using the exact definition in goals-and-kpis.md. Never mark anyone SQL, since sales decides that. If the definition is blank, write [MQL definition needed].
6. Draft each message: subject of 50 characters or fewer, body of 90 words or fewer, one ask. Refer only to what the person did, using [resource name] or [personal detail] for the rest. Take product statements from product.md. Use Public proof only, except that a Tier A message from one seller to one person may use Sales only proof. Never use internal numbers.
7. Write the sales handoff for Tier A, one row per lead, with [seller needed] if routing is missing. Rank by segment priority, then a named trigger, then date. If Tier A may exceed what sales can take that week, ask the marketer.
8. Set a check with sales 14 days after the first handoff (a starting rule). If more than a third of leads are rejected (a starting rule), recommend [Define the lead handoff](../marketing-ops/define-lead-handoff.md).
9. Check the draft against the context pack: every claim, permission, word to avoid, internal number, roadmap item and hard rule. Add approval time from channels-and-tools.md before the first send.
10. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
Status: Draft
Source: <form, download or demo request, by name>
Rows in: <n>. Duplicates: <n>. Removed: <n, with reasons>.

## Lead tiers
| Tier | Count | MQLs | Sender | After the last message |

## Timing
| Tier | Message | Business day | Date | Approver |

## Messages
Tier A, message 1
Subject: <50 characters at most>
Body: <90 words at most, one ask>
<same fields for each message in the timing table>

## Sales handoff
| Rank | Lead, title and company | Action and date | Fit and trigger | MQL | Seller | Due |

## Check with sales
Date: <date, or "14 days after first handoff">
Read: <accepted, rejected with reason, not contacted>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Do tier counts add up to rows in, minus duplicates and removals?
- [ ] Is MQL status marked by your definition, with nobody marked SQL?
- [ ] Does each message refer only to what the person did, with one ask?
- [ ] Do leads without consent stay off marketing email?
- [ ] Does every message use only proof with the right permission and no internal number?

## Example (fictional company)

**Status:** Draft

**Source:** Website demo page and guide downloads, week of January 11, 2027

Rows in: 14. Duplicates: 1. Removed: 2 (one customer, one under 100 learners).

**Lead tiers**

| Tier | Count | MQLs | Sender | After the last message |
|---|---|---|---|---|
| A | 5 | 4 | [seller needed] | Nurture if fit |
| B | 4 | 1 | Marketer | Nurture |
| C | 2 | 0 | Marketer | Closes |

**Timing** (Tier A shown): message 1 by January 12, message 2 by January 14, message 3 by January 20. Approver: Tom Ferrant.

**Messages** (Tier A, message 1 shown)

Subject: Your demo request for CogniATion Coach

Body: [First name], you asked for a demo of CogniATion Coach. It questions employees about a work problem instead of answering it, then scores their reasoning. Which work problem would you want to try it on? [Seller name] can show you on a call this week.

**Sales handoff**

| Rank | Lead, title and company | Action and date | Fit and trigger | MQL | Seller | Due |
|---|---|---|---|---|---|---|
| 1 | [lead name], head of learning, [accounting firm] | Demo request, Jan 11 | 150 people to train, AI assistant rollout | Yes | [seller needed] | Jan 12 |

**Assumptions and open questions**

- Assumption: all counts, dates and the sample lead are invented.
- Assumption: Tier A text counts as sales material, approved in advance.
- Inference: one Tier A lead is Fit unknown, so it is not yet an MQL.
- Unknown: how are leads routed across the three account executives?

## How to run it

```
Use the skill "Write a lead follow-up". Read the context pack.
Task: sort the leads pasted below from <form, download or demo request> and write the tiers, timing, messages and sales handoff.
```
