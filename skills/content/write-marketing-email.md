---
title: Write a marketing email
type: skill
function: content
owner: content-lead
reads: [company, product, personas, messaging, proof-points, brand-voice, channels-and-tools]
you_bring: The purpose, who receives it, the send date, the action and the link.
also_for: [newsletter, email blast, webinar invite, announcement email, email to customers, email to the list, low open rates, demo invite]
version: 0.1.0
updated: 2026-11-01
summary: Produces one standalone marketing email or newsletter issue, with subject lines, body, one main action and send notes.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this for one email: an announcement, an invitation or a newsletter issue. Do not use it for a series of emails; use [Design a nurture sequence](../campaign-design/design-nurture-sequence.md) instead.

## Inputs

- [[context-pack:channels-and-tools]]: the email list, its cadence, approvers and hard rules.
- [[context-pack:personas]]: the reader's daily problem and objections.
- [[context-pack:messaging]]: messages by persona, words to use and avoid.
- [[context-pack:product]]: what the product does, prices, what it is not, roadmap limits.
- [[context-pack:proof-points]]: customers, numbers and quotes with permission status.
- [[context-pack:company]]: public name, publishable numbers.
- [[context-pack:brand-voice]]: voice, point of view, rules.

The marketer supplies the purpose, the list or part of the list receiving it, the send date, the action and link, and the items for a newsletter issue. Past results, if any, come as pasted numbers.

## Procedure

1. Set the email type: standalone or newsletter. If the request needs more than one email in a planned order, stop and point the marketer to [Design a nurture sequence](../campaign-design/design-nurture-sequence.md).
2. Fix the audience, one reader from personas.md and one main action. If the marketer does not say which part of the list receives it, ask. Do not assume the list can be split by segment or persona.
3. Write three subject lines of up to 50 characters, one of each kind: a question, a plain statement of fact, and a line naming the task, decision or document. Recommend the one closest to the reader's daily problem, or the question on a tie (a starting rule). Use no exclamation points and no all caps, and give no deadline or scarcity unless the marketer supplied it.
4. Write a preheader of up to 90 characters that adds something the subject line does not say.
5. Write the body. For a standalone email, up to 150 words: open on the reader's problem in the first sentence, give what you know that helps, then the action, in the point of view set in brand-voice.md. For a newsletter, up to 250 words: up to three items, each a heading and up to 60 words, with the first item carrying the main action and the others carrying a plain link.
6. Use a customer name, number or quote only if proof-points.md marks it public, and a company number only if company.md marks it publishable. State the sample and date. If a claim in messaging.md has no entry in proof-points.md, leave it out and ask. Do not name competitors.
7. Write links as the marketer's URL, or [link needed]. Add [tracking parameters needed] unless the marketer supplied them, following the skill [Set tracking conventions](../marketing-ops/set-tracking-conventions.md) once it has been run.
8. Write the footer fields as placeholders unless the marketer supplied them: [postal address needed], [unsubscribe link needed]. Do not give legal advice. Add an open question asking the marketer to confirm the email meets the rules that apply to their list.
9. Check the draft against the context pack: facts, permissions, what the product is not, words to avoid, voice rules. Add any pricing mention to Approvals needed with the listed approver.
10. List everything assumed under "Assumptions and open questions". If a needed context pack field is blank, leave a placeholder in square brackets and ask in the last section. Never invent.

The marketer loads the email into their own email tool and sends a test first. This skill sends nothing.

## Output format

```
Status: Draft
Email type: <standalone or newsletter>
Audience: <list or part of list, up to 15 words>
Reader: <one persona, up to 8 words>
Main action: <up to 8 words>
Send date: <supplied date, or [send date needed]>

## Subject lines
Question: <up to 50 characters>
Fact: <up to 50 characters>
Task, decision or document: <up to 50 characters>
Recommended: <which one, and why in up to 15 words>
Preheader: <up to 90 characters>
From name: <from the context pack or the marketer>

## Body
<standalone: up to 150 words. Newsletter: up to 250 words, up to 3 items>
Button or link text: <up to 5 words>
Link: <URL with tracking, or [link needed] [tracking parameters needed]>

## Footer
<[postal address needed] [unsubscribe link needed], or supplied values>

## Proof used
<each item and its permission status, or "None">

## Approvals needed
<approver and typical time from channels-and-tools.md>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Is this one email, with one main action?
- [ ] Are the subject lines within 50 characters, with no invented urgency?
- [ ] Does the body open on the reader's problem and stay inside its word limit?
- [ ] Does every customer, number and quote have public or publishable status, with sample and date?
- [ ] Are competitors unnamed, and are the words to avoid and exclamation points absent?
- [ ] Are the link, tracking and footer fields filled or shown as placeholders?
- [ ] Has the marketer sent a test to themselves before it goes out?

## Example (fictional company)

**Status:** Draft

**Email type:** Standalone. **Audience:** [part of list needed]. **Reader:** Head of learning. **Main action:** Request a demo. **Send date:** [send date needed]

**Subject lines**

Question: Did your last course change how anyone works?

Fact: Practice reasoning in about 15 minutes a session

Task, decision or document: Test the reasoning in one client memo

Recommended: Question, names the proof the reader is asked for.

Preheader: Completion data won't show it. Team-level progress on reasoning can.

From name: CogniATion

**Body**

When leadership asks whether your last course changed how people work, what do you show them?

CogniATion Coach is a chatbot that questions employees about a work problem instead of answering it. Sessions take about 15 minutes. The Coach scores reasoning against a rubric, and you see progress by team, never an individual's conversation.

People keep practicing. Across all customers in Q3 2026, 72% of assigned learners completed at least one session each week.

"My analysts stopped asking the bot for the answer and started defending their own." Lena Marsh, head of learning, Brightmere Advisory.

Button: Request a demo. Link: [link needed] [tracking parameters needed]

**Footer:** [postal address needed] [unsubscribe link needed]

**Proof used:** 72% figure and Marsh quote, public.

**Approvals needed:** The marketer, same day.

**Assumptions and open questions**

- Assumption: CogniATion is the from name.
- Unknown: which part of the 5,400-contact list receives this?
- Unknown: does this meet the rules that apply to your list?

## How to run it

```
Use the skill "Write a marketing email". Read the context pack.
Task: <the purpose, who receives it, the send date, the action and the link>.
```
