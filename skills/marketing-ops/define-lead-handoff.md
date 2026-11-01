---
title: Define the lead handoff
type: skill
function: marketing-ops
owner: marketing-operations-manager
reads: [goals-and-kpis, icp-and-segments, personas, company, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Sets lifecycle stages, routing rules and response times between marketing and sales.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

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

## Procedure

1. Write the lifecycle stages in this order: Lead, MQL, SQL, Won or lost, plus two side stages, Recycled and Disqualified. Each gets an entry rule, an owner and an exit rule. Copy the MQL and SQL definitions from goals-and-kpis.md word for word. Propose rules for the other stages and label them assumptions.
2. Turn the disqualifiers in icp-and-segments.md into Disqualified rules. A disqualified lead does not go to sales.
3. Write the routing rules, one row per trigger, in priority order. A lead asking to talk to sales comes first, and every other MQL trigger follows. Every row names exactly one owning role. Apply territory or ownership rules only if the marketer supplied them. Otherwise write [territory rule needed].
4. Set a response time for each routing row, using the marketer's figure. If none was given, write [response time to agree with sales].
5. Set what happens when the time is missed: reassign if a second person holds that role, otherwise tell that person's manager, or write [escalation owner needed].
6. Write the rejection rule. Sales may reject an MQL only with one of these reasons: not ICP, wrong person, no contact after the agreed attempts, duplicate, not ready. "Not ICP" and "duplicate" move the lead to Disqualified. "Not ready" and "no contact" move it to Recycled. "Wrong person" goes back to marketing to find the right contact.
7. Run the capacity check. Weekly volume today is the MQL baseline divided by the weeks in that period. Weekly volume needed is the SQL goal divided by the MQL to SQL rate, then divided by the weeks in the quarter. Show the division and label both as estimates. Flag any shortfall against the marketer's capacity figure, or record capacity as unknown.
8. List the CRM fields the rules need: stage, stage date, owner, rejection reason and first response date. The marketer sets these up, since the office cannot reach the CRM.
9. Check the draft against the context pack: definitions are word for word, the sales roles exist in company.md, and the fit rules match icp-and-segments.md. If a needed field is blank, leave a visible placeholder and ask in the last section. Never invent.
10. List every assumption, estimate, inference and unknown in the last section, including anything sales has not yet agreed to.

## Output format

```
Status: Draft

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
- [ ] Does every stage have an entry rule, one owner and an exit rule?
- [ ] Are the disqualifiers applied before a lead reaches sales?
- [ ] Is every response time supplied by the marketer or left as a placeholder?
- [ ] Does each routing row say what happens when the time is missed?
- [ ] Does the capacity check show its math?
- [ ] Has someone in sales been named to agree to the rules?

## Example (fictional company)

Status: Draft

Assumption: the response times are illustrative, as if proposed by CogniATion's marketer. Lead and owner rules await agreement from Tom Ferrant, head of sales. Won or lost and Recycled are left out for length.

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
| Webinar or two downloads, ICP fit | Sales development representative | 2 business days | Head of sales told |

**Rejection rule**

Not ICP or duplicate: Disqualified. Not ready or no contact: Recycled. Wrong person: back to marketer.

**Capacity check**

About 20 MQLs a week today, 27 needed, one person. Capacity unknown.

**CRM fields to set up**

- Stage, stage date, owner, rejection reason, first response date.

**Assumptions and open questions**

- Estimate: 260 / 13 = 20. 90 / 0.26 / 13 = 27.
- Unknown: How many MQLs a week can that person take?
- Unknown: Who marks a lead wanting a course library or individual scores, often known only after a call?
- Unknown: Which account executive gets which SQL? [territory rule needed]

## How to run it

```
Use the skill "Define the lead handoff". Read the context pack.
Task: <define the handoff, with today's routing and any proposed response times pasted below>.
```
