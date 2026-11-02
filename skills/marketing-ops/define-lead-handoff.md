---
title: Define the lead handoff
type: skill
function: marketing-ops
owner: marketing-operations-manager
reads: [goals-and-kpis, icp-and-segments, personas, company, channels-and-tools]
you_bring: How leads move today and where they stall, response times, sales capacity, who in sales will agree, and if sales says the leads are bad, the last 30 rejected MQLs with reasons.
also_for: [leads are bad, bad leads, junk leads, lead quality, sales complains, mql definition, sales ignores leads, leads not followed up, lead routing, demo requests go nowhere]
version: 0.1.0
updated: 2026-11-02
summary: Sets lifecycle stages, routing rules and response times between marketing and sales.
judge: ["Would your sales lead sign these rules today or only accept them in theory?", "If every lead followed these rules would sales have better conversations or only cleaner records?", "What happens when the rules say a lead is good and sales still refuses it?", "Who looks at rejected leads each month and what changes as a result?"]
show_to: the salesperson who works these leads first, and ask which rule they would ignore
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when leads stall between marketing and sales, or when sales disputes lead quality. Do not use it for handing off the leads from one event, which belongs to [Follow up after an event](../events-and-webinars/follow-up-after-event.md), or for what happens to leads not ready for sales, which belongs to [Design a nurture sequence](../campaign-design/design-nurture-sequence.md).

## Inputs

- [[context-pack:goals-and-kpis]]: MQL and SQL definitions, MQL volume, conversion rate and SQL goal.
- [[context-pack:icp-and-segments]]: fit criteria, disqualifiers, segment priority and sales cycle.
- [[context-pack:personas]]: which job titles count as buyers.
- [[context-pack:company]]: size and roles of the sales team.
- [[context-pack:channels-and-tools]]: who has access to the CRM and marketing automation tool.

The marketer pastes into the chat:

- How leads move today, and where they stall.
- Any territory or account ownership rules.
- Current or proposed response times, and how many leads a week each sales role can take.
- Who in sales will agree to the rules.
- If sales says the leads are bad, the last 30 rejected MQLs with reasons.

## Procedure

1. If sales says the leads are bad, start here, before defining anything. Get the last 30 rejected MQLs with reasons (a starting rule), or ask sales for one reason per lead. Sort and count by the reasons in step 7. Say what the largest group points to: not ICP, the fit rules; not ready, nurture; no contact, follow-up; wrong person, contact data. To raise it without a fight, see [Three hard situations](../../guides/hard-situations.md#sales-says-the-leads-are-bad).
2. Write the lifecycle stages in this order: Lead, MQL, SQL, Won or lost, plus two side stages, Recycled and Disqualified. Each gets an entry rule, an owner and an exit rule. Copy the MQL and SQL definitions from goals-and-kpis.md word for word. If blank, and for other stages, propose a rule and label it an assumption. With no sales team, the person who sells is sales.
3. Turn the disqualifiers in icp-and-segments.md into Disqualified rules.
4. Write the routing rules, one row per trigger, in priority order. A lead asking to talk to sales comes first, and every other MQL trigger follows. Every row names exactly one owning role. Apply territory or ownership rules only if the marketer supplied them. Otherwise write [territory rule needed].
5. Set a response time for each routing row, using the marketer's figure. If none was given, write [response time to agree with sales].
6. Set what happens when the time is missed: reassign if a second person holds that role, otherwise tell that person's manager, or write [escalation owner needed].
7. Write the rejection rule. Sales may reject an MQL only with one of these reasons: not ICP, wrong person, no contact after the agreed attempts, duplicate, not ready. "Not ICP" and "duplicate" move the lead to Disqualified. "Not ready" and "no contact" move it to Recycled. "Wrong person" goes back to marketing.
8. Run the capacity check. Weekly volume today is the MQL baseline divided by the weeks in that period. Weekly volume needed is the SQL goal divided by the MQL to SQL rate, then divided by the weeks in the quarter. Show the division and label both as estimates. Flag any shortfall against the marketer's capacity figure, or record capacity as unknown.
9. List the fields the rules need: stage, stage date, owner, rejection reason, first response date. A spreadsheet can hold them.
10. Check the draft against the context pack: definitions are word for word, the sales roles exist in company.md, and the fit rules match icp-and-segments.md. Leave a visible placeholder for any blank field and ask in the last section.
11. List every assumption, estimate, inference and unknown in the last section, including anything sales has not agreed to.

## Output format

```
Status: Draft

## Rejected leads, sorted
| Reason | Count | What it points to |
<Largest first, or "Not in dispute".>

## Lifecycle stages
| Stage | Entry rule | Owner | Exit rule |
<One row per stage. Each cell max 20 words.>

## Routing rules
| Trigger | Goes to | Response time | If missed |
<Up to 6 rows, in priority order.>

## Rejection rule
<The five reasons and where each sends the lead. Max 50 words.>

## Capacity check
<Volume today, volume needed, capacity, and the gap. Max 50 words.>

## CRM fields to set up
<Up to 8 bullets, one field each.>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Are the MQL and SQL definitions word for word from goals-and-kpis.md?
- [ ] Are the disqualifiers applied before a lead reaches sales?
- [ ] Is every response time supplied by the marketer or left as a placeholder?
- [ ] Does each routing row say what happens when the time is missed?
- [ ] Has someone in sales been named to agree to the rules?

## Example (fictional company)

Status: Draft

Assumption: the response times are illustrative, as if proposed by CogniATion's marketer. Lead and owner rules await agreement from Tom Ferrant, head of sales. Won or lost and Recycled are left out for length.

**Rejected leads, sorted** (invented for this example)

From 30 rejected MQLs: not ICP 14, not ready 9, no contact 5, wrong person 2. The largest group points to the fit rules, so disqualifiers come first.

**Lifecycle stages**

| Stage | Entry rule | Owner | Exit rule |
|---|---|---|---|
| Lead | Gave contact details | Marketer | Meets MQL definition, or disqualified |
| MQL | Fits the ICP and has requested a demo, attended a webinar or downloaded two resources | Sales development representative | First call held, or rejected |
| SQL | Accepted by an account executive after a first call | Account executive | Won or lost |
| Disqualified | Fewer than 100 learners, wants a course library, or wants scores on individuals for performance reviews | Marketer | None |

**Routing rules**

| Trigger | Goes to | Response time | If missed |
|---|---|---|---|
| Demo request, ICP fit | Sales development representative | 1 business day | Head of sales told |

**Rejection rule**

Not ICP or duplicate: Disqualified. Not ready or no contact: Recycled. Wrong person: back to marketer.

**Capacity check**

About 20 MQLs a week today, 27 needed, one person. Capacity unknown.

**CRM fields to set up**

- Stage, stage date, owner, rejection reason, first response date.

**Assumptions and open questions**

- Estimate: 260 / 13 = 20. 90 / 0.26 / 13 = 27.
- Unknown: How many MQLs a week can that person take?

## How to run it

```
Use the skill "Define the lead handoff". Read the context pack.
Task: <where leads stall and who in sales will agree>.
<paste today's routing, response times and sales capacity here>
```
