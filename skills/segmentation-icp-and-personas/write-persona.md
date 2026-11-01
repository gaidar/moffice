---
title: Write a persona
type: skill
function: segmentation-icp-and-personas
owner: insights-analyst
reads: [personas, icp-and-segments, messaging, proof-points, product]
version: 0.1.0
updated: 2026-11-01
summary: One buying persona with job, objections and language.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this skill to write or update one buying persona: a person in the buying decision, described by role, job, objections and language. Do not use it for raw research notes; use [Synthesize customer research](synthesize-customer-research.md) first and bring the findings here. To define which companies to target, use [Define the ICP](define-icp.md) instead.

## Inputs

- [[context-pack:personas]]: the existing entry for this role, its measures, daily problem, objections and information sources.
- [[context-pack:icp-and-segments]]: segments, triggers and the buying process.
- [[context-pack:messaging]]: the message for this persona, words to use and words to avoid.
- [[context-pack:proof-points]]: proof that answers objections, with permission status.
- [[context-pack:product]]: features and limits, so that answers to objections stay true.

The marketer states in the prompt:

- The role, and the segment if the persona differs by segment.
- Any evidence to add: interview quotes, call notes, research findings or sales comments.

## Procedure

1. Pick one role. If the marketer names several, write the first and list the rest under open questions. If the role is missing from personas.md and no evidence was pasted, ask for evidence. If the marketer wants a draft anyway, mark every field "Hypothesis".
2. Tag each field by source: "Pack" for the context pack, "Pasted" for the marketer's evidence, "Hypothesis" for anything else. When pasted evidence contradicts the context pack, show both and flag the conflict rather than choosing one.
3. Set the buying role, using exactly one of these: champion (pushes the purchase), approver (says yes for the department or team), signer (controls the money), daily user (works in the product), blocker (can stop it, such as IT or legal).
4. Write the job from what the person is measured on. Use the measures in personas.md. If that field is blank, write [measures needed] and ask in the last section. Leave out age, hobbies, family, invented names and any trait that does not change what you would say to this person.
5. List the triggers that bring this person into the decision, using only icp-and-segments.md or pasted evidence.
6. List up to 4 objections, in the person's own words where a source has them. Do not write new quotes. A paraphrase must be labeled as a paraphrase.
7. Answer each objection with one true statement from product.md, then one proof point from proof-points.md. A persona is an internal output, but its answers get reused, so use public proof only by default. If no public proof fits, write [proof needed], and name any sales-only item that could fit in one-to-one material without quoting it. Never use pending or none items. Where the product has a real limit, say so.
8. Build the language section: words this person uses, taken from quotes and sources only, and words to avoid, taken from messaging.md, plus any the evidence shows they dislike.
9. Write one message for this persona. Use the line from messaging.md if there is one. Write a new one only if the evidence supports a change, and label it "Proposed".
10. Check the draft against the context pack: test each answer against "What it is not" and known weak spots in product.md, and each proof point against its permission status.
11. List everything you assumed, inferred or could not find in the last section, including each field tagged Hypothesis.

## Output format

```
Status: Draft

## Persona
Role and title: <up to 12 words> | Source: <Pack, Pasted or Hypothesis>
Buying role: <champion, approver, signer, daily user or blocker>
Segment: <segment name or "All">

## Job
Measured on: <up to 25 words> | Source
Daily problem: <one quote or paraphrase, up to 30 words> | Source

## Triggers
- <trigger, up to 15 words, 1 to 4 items> | Source

## Objections and answers
| Objection | Answer | Proof and permission |
<1 to 4 rows; answer up to 30 words>

## Language
Words they use: <up to 10, from sources only>
Words to avoid: <from messaging.md and evidence>

## Message
<one sentence, up to 25 words, marked "Proposed" if new>

## Where they get information
- <source, up to 10 words, 1 to 4 items> | Source

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the persona cover one role only?
- [ ] Is every field tagged with its source?
- [ ] Is every quote traceable to a source, with no written-up quotes?
- [ ] Does every proof point carry a permission status that allows this use?
- [ ] Do the answers to objections stay within what the product does?
- [ ] Are demographics and invented personal details left out?
- [ ] Are all words from the "words to avoid" list kept out of the message?

## Example (fictional company)

**Status:** Draft

**Persona**

Role and title: head of learning and development, reports to the VP of people | Source: Pack

Buying role: champion

Segment: Professional services firms

**Job**

Measured on: participation in programs, manager feedback, proof that training changed behavior | Source: Pack

Daily problem: "Everyone finishes the course, and nobody can show me it changed how they work." | Source: Pack

**Triggers:** company-wide AI assistant rollout, client complaint about poor reasoning | Source: Pack

**Objections and answers**

| Objection | Answer | Proof and permission |
|---|---|---|
| "People won't make time for another training tool." | Sessions take about 15 minutes and use work problems. | 72% of assigned learners completed at least one session each week, Q3 2026, public |
| "How would I show the leadership team that it worked?" | Reports show progress on six thinking skills by team, and stop at team level. | Brightmere Advisory's analysts raised their average score on client memo reasoning by 22% in one quarter of 2026, as measured by Brightmere's partners, public |

**Language**

Words they use: finishes, course, changed how they work, leadership team

Words to avoid: revolutionary, world-class, brain training, unlock your potential, smarter, superintelligent, IQ

**Message:** Show that training changed how people reason, not only that they finished it.

**Where they get information:** peers in other companies, learning and development associations, conferences | Source: Pack

**Assumptions and open questions**

- Assumption: the triggers above are the two most relevant to this role, picked from the list in icp-and-segments.md.
- Unknown: does this persona change in financial services, where the security review runs longest?

## How to run it

```
Use the skill "Write a persona". Read the context pack.
Task: write the persona for <role>, in the <segment> segment, using the notes pasted below.
```
