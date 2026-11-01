---
title: Draft a holding statement
type: skill
function: pr-and-comms
owner: pr-and-communications-manager
reads: [company, product, messaging, brand-voice, channels-and-tools]
you_bring: What is confirmed and by whom, when it started, who is affected, what is being done, who is asking, and the next update time.
also_for: [outage statement, data breach, crisis communication, bad press, angry customer post, journalist calling, public complaint, incident response]
version: 0.1.0
updated: 2026-11-01
summary: Produces the first statement for an incident, with Q&A, an escalation check and a time for the next update.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this in the first hours of an incident, when people are asking and the facts are incomplete: an outage, a data problem, a safety event, a public complaint. Do not use it once the facts are known and you are announcing a fix or a change; use [Write a press release](write-press-release.md) instead. It does not replace a lawyer when step 2 says to call one.

## Inputs

- [[context-pack:company]]: public name, who may speak, press contact.
- [[context-pack:product]]: what the product does and is not.
- [[context-pack:messaging]]: words to avoid and promises the incident contradicts.
- [[context-pack:brand-voice]]: tone and things never to say.
- [[context-pack:channels-and-tools]]: approvers and owned channels.

The marketer supplies: what happened as far as confirmed, who confirmed it, when it started, who is affected, what is being done, who is asking, and the next update time.

## Procedure

1. Sort every fact from the prompt into two lists: confirmed (with who confirmed it) and not yet known. Anything without a named source goes in not yet known. If the prompt does not say what is confirmed, ask before drafting.
2. Run the escalation check. If the incident involves injury or death, personal or customer data, a regulator, police, a legal threat, or a claim about product safety, write "Stop: get a lawyer and the CEO before anything goes out" at the top, and still draft for their review.
3. Set the mode. Choose "reactive, send only when asked" when few customers are affected and no one outside has noticed. Choose "proactive" when customers are affected or a public report exists. In proactive mode, affected customers hear before anyone else.
4. Write the statement in four parts, in this order: what we know, who is affected as far as we know, what we are doing, when we will next update. Use only the confirmed list.
5. Do not state a cause, a fix time, an amount of data or a number of customers unless it is on the confirmed list. Do not say "no customer data was affected" unless a named person has checked. Do not blame a person, a supplier or a customer.
6. Write without marketing: no proof points, no customer names, no product benefits and no claims about reliability. A product feature that might limit the effect, such as a backup or offline mode, goes in only if someone has confirmed it worked during this incident.
7. Set the next update time from the prompt. If there is none, leave [next update time needed]. Never promise one the marketer did not give.
8. Write the customer note: the same facts, plus what the customer should do now. If nothing, say so.
9. Write 5 to 7 Q&A items, covering the hardest questions first: what happened, who is affected, is data safe, whose fault is it, when will it be fixed. Where the honest answer is unknown, answer "We do not know yet" and say when that will change.
10. Fill the escalation table from company.md and channels-and-tools.md. If a needed field is blank, or no approver is listed for incidents, or the usual approval time is too slow, leave a visible placeholder in square brackets and ask in the last section. Never invent.
11. Check the draft against the context pack: every word against words to avoid and brand-voice.md, and every statement against the confirmed list. Remove anything that fails.
12. List everything you assumed, and everything not yet known, in the last section.

## Output format

```
Status: Draft, not for release until approved
Escalation check: <"Stop: get a lawyer and the CEO" and the reason, or "No trigger found">
Mode: <Reactive or proactive, and one line why>

## Holding statement
<80 words maximum, the four parts from step 4>

## Customer note
<60 words maximum. Same facts, plus what to do now>

## Q&A
Q: <question>
A: <answer, 30 words maximum>
<5 to 7 pairs, hardest first>

## Do not say
- <Up to 5 tempting lines to avoid, each with the reason>

## Escalation
| Job | Person | When |
|---|---|---|
| Approves the statement | <name or placeholder> | <before release> |
| Speaks to press | <name or placeholder> | <when> |
| Handles press inquiries | <contact> | <when> |
| Tells customers | <name or placeholder> | <before public release> |
Update this statement when: <what would change it>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Is every statement backed by a fact with a named source?
- [ ] Did you run the escalation check, and act on any trigger?
- [ ] Is the statement free of cause, fix time and scope unless confirmed?
- [ ] Is it free of blame, jokes, marketing claims and customer names?
- [ ] Is there a time for the next update, from a real person?
- [ ] Do affected customers hear before the public?
- [ ] Does each Q&A answer say "We do not know yet" where that is the truth?

## Example (fictional company)

Status: Draft, not for release until approved

Escalation check: No trigger found, on the facts given

Mode: Proactive, because customers are affected

**Holding statement**

Some learners cannot start practice sessions in CogniATion Coach. We do not yet know the cause or which customers are affected. We are working to restore access. We will update you by [next update time needed].

**Customer note**

Some of your learners cannot start CogniATion Coach sessions. We are working on it. Please ask them to try again after our next update. Next update by [next update time needed].

**Q&A**

Q: Is learner data safe?

A: We do not know yet. [Named person to confirm before this changes]

Q: Whose fault is it?

A: We do not know the cause yet, and we will say when we do.

**Do not say**

- "No learner's conversation or score was affected." No named person has checked.

**Escalation**

| Job | Person | When |
|---|---|---|
| Approves the statement | Marta Ilves, CEO | Before release, same day |
| Speaks to press | Marta Ilves, CEO (assumption) | When asked |
| Handles press inquiries | press@cogniation.example | Now |
| Tells customers | [name needed] | Before public release |

Update this statement when: the cause or scope is confirmed.

**Assumptions and open questions**

- Assumption: the incident itself is invented for this example.
- Assumption: the CEO speaks to press, because company.md names no one for incidents.
- Unknown: who tells customers, and who can confirm whether learner data is affected?

## How to run it

```
Use the skill "Draft a holding statement". Read the context pack.
Task: <what is confirmed and by whom, when it started, who is affected, what is being done, who is asking, next update time>.
```
