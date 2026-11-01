---
title: Write a media pitch
type: skill
function: pr-and-comms
owner: pr-and-communications-manager
reads: [company, product, icp-and-segments, personas, messaging, proof-points, brand-voice, channels-and-tools]
you_bring: The type of journalist or outlet, what they have covered recently, and any news hook or date.
also_for: [press coverage, pitch a journalist, get media attention, trade press, earned media, story idea, pr outreach, reporter email]
version: 0.1.0
updated: 2026-11-01
summary: Produces one short pitch and angle for one type of journalist or outlet, using only public proof.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this to offer one story to one type of journalist or outlet, such as a trade editor covering corporate learning. Do not use it for a formal announcement to everyone; use [Write a press release](write-press-release.md) instead. Run it once per type of outlet, because an angle that fits two kinds of reader usually fits neither.

## Inputs

- [[context-pack:company]]: who may speak on what, press contact, publishable numbers.
- [[context-pack:product]]: what the product does and is not, and whether any roadmap item is cleared.
- [[context-pack:icp-and-segments]]: the segment this reader cares about and what triggers buying there.
- [[context-pack:personas]]: the problems and language of the people the outlet writes for.
- [[context-pack:messaging]]: pillars and words to avoid.
- [[context-pack:proof-points]]: customers, results and quotes, with permission status.
- [[context-pack:brand-voice]]: tone and things never to say.
- [[context-pack:channels-and-tools]]: who approves outside communication.

The marketer supplies in the prompt: the type of journalist or outlet, what that person has covered recently with links or titles if known, the journalist's name if known, and any news hook or date.

## Procedure

1. Name the reader of the outlet in one line: their job and what they worry about. Take this from personas.md if the outlet writes for one of the personas. If it does not, ask the marketer who reads it.
2. Write three candidate angles, one line each, stated as a story about the reader's problem, not about the company. Discard any angle that needs a fact not in the context pack or the prompt.
3. Pick one angle using this order: it has public proof, then it connects to a hook the marketer supplied, then it fits the highest-priority segment in icp-and-segments.md. State the pick and why in one line. List the rejected angles.
4. Write the subject line: under 10 words, naming the topic, with no "exclusive" unless the marketer says it is.
5. Write the opening: one sentence linking to the journalist's recent coverage, only if the marketer supplied it. Otherwise leave [recent coverage needed]. Never guess what a journalist wrote or cares about.
6. Write the pitch body: the story in two sentences, then one to three proof items, each public in proof-points.md or publishable in company.md, with its date or sample.
7. Write the offer: exactly what the journalist can have, such as an interview or data. Name a company leader only for the topics company.md gives them. If the best speaker is outside those topics, say so as an open question. A public quote does not mean a customer agreed to an interview, so label any customer interview "to be confirmed with the customer".
8. Close with one clear question the journalist can answer yes or no. No follow-up pressure.
9. Do not name competitors, mention roadmap items or attach pricing. If a needed context pack field is blank, leave a visible placeholder in square brackets and ask in the last section. Never invent.
10. Check the draft against the context pack: every name and number against its permission, every word against words to avoid, every claim against what the product is not. If the approvals table has no line for media pitches, say who you assumed approves it.
11. List everything you assumed, and every placeholder still open, in the last section.

This skill finds no journalists and sends nothing. The marketer chooses the recipient and sends the pitch.

## Output format

```
Status: Draft
Reader: <who reads this outlet, one line>
Angle: <one sentence>
Why this angle: <one line>
Rejected angles: <up to 2, one line each>

## Pitch
Subject: <under 10 words>

<Greeting, with the journalist's name or [name needed]>

<Opening, one sentence on their coverage, or [recent coverage needed]>

<Story, two sentences>

<Proof, 1 to 3 items, one line each, with date or sample>

<Offer, one or two sentences>

<One yes-or-no question>

<Marketer's name, press contact>

Total pitch length: 150 words maximum, not counting the subject.

## Approvals needed
- <Approver, what they approve>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Is the angle about the reader's problem, not about the company?
- [ ] Is the pitch 150 words or fewer?
- [ ] Is the reference to the journalist's work supplied by the marketer, or a visible placeholder?
- [ ] Is every proof item public or publishable, with its date or sample?
- [ ] Is it clear what the journalist can have, and is any customer interview marked as unconfirmed?
- [ ] Is the pitch free of competitor names, roadmap items and words to avoid?
- [ ] Could the journalist answer the closing question with one word?

## Example (fictional company)

Status: Draft

Reader: editors at a trade publication on corporate learning, writing for heads of learning and development.

Angle: how a head of learning can show that training changed how people reason, not only that they finished it.

Why this angle: it has public proof, and professional services, where Brightmere Advisory sits, is the top-priority segment.

Rejected angles: junior staff accepting AI answers unchecked, no public number behind it. Time to first live session, weaker for this reader.

**Pitch**

Subject: Showing that training changed how people reason

Hi [name needed],

[recent coverage needed]

The heads of learning we talk to can show who finished a course, but not whether it changed how people work. Many have rolled out AI assistants and worry that junior staff now accept answers without checking them.

Proof: analysts at Brightmere Advisory, a professional services firm using CogniATion Coach, raised their average score on client memo reasoning by 22% in one quarter of 2026, as measured by Brightmere's partners. 72% of assigned learners completed at least one session each week in Q3 2026, across all customers.

We can share a quote from Lena Marsh, Brightmere's head of learning, with an interview to be confirmed with the customer. Anika Sole, our VP product, can explain how the Coach questions employees instead of answering them.

Would a conversation about this be useful for your readers?

[Marketer's name], press@cogniation.example

**Approvals needed**

- Marta Ilves, CEO, this pitch

**Assumptions and open questions**

- Assumption: the outlet is invented for this example, and its readers match the head of learning in personas.md.
- Inference: Anika Sole fits, because company.md gives her how the Coach works.
- Unknown: who should speak on measuring reasoning? company.md gives leaders no such topic.

## How to run it

```
Use the skill "Write a media pitch". Read the context pack.
Task: <the type of journalist or outlet, recent coverage, name if known, and any news hook or date>.
```
