---
title: Build a messaging framework
type: skill
function: positioning-and-messaging
owner: product-marketing-manager
reads: [company, product, personas, messaging, competitors, proof-points, brand-voice, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Turns a positioning statement into pillars, proof per pillar, messages by persona and words to use and avoid.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this once the positioning statement is settled, or when pillars have drifted from what sales says. Do not use it without a statement; run [Write a positioning statement](write-positioning-statement.md) first. For finished page copy, use [Write a web page](../content/write-web-page.md) instead.

## Inputs

From the context pack:

- [[context-pack:messaging]] – statement, current pillars, words to use and avoid
- [[context-pack:product]] – features, what it is not, known weak spots
- [[context-pack:personas]] – roles, what each is measured on, objections
- [[context-pack:competitors]] – dated facts, where each wins and loses
- [[context-pack:proof-points]] – evidence and permission status
- [[context-pack:company]] – which company numbers may be published
- [[context-pack:brand-voice]] – voice traits and style rules
- [[context-pack:channels-and-tools]] – hard rules on competitor names

The marketer supplies in the prompt: a new positioning statement, if it differs from messaging.md, and any new proof with its permission status.

## Procedure

1. Read the positioning statement. If it is blank and none is pasted, stop and ask for it, or point to the skill "Write a positioning statement".
2. Split the statement into separate claims: the lead value, the reason to believe and each difference. Add the current pillars from messaging.md. Keep at most 6 candidates.
3. Keep a candidate only if all four are true: product.md supports it without crossing "What it is not" or "Known weak spots", it reaches what at least one persona is measured on, at least one alternative cannot say it as well, and it can be stated in 8 words or fewer.
4. Rank what is left by the number of personas it reaches, then by its best proof, in this order: Public, Sales only, Internal only, none. On a tie, keep messaging.md order (a starting rule). Take the top three as pillars. If only two survive, write two. Never pad.
5. For each pillar, write why it differs: the alternative it beats and the dated fact or field behind that. If it beats only the status quo, say so.
6. For each pillar, list proof from proof-points.md and publishable numbers from company.md, each with its permission status. Exclude Pending and None. Proof that appears only in messaging.md has no permission status, so replace it with a placeholder such as [proof permission needed] and add it to the unknowns.
7. Mark each pillar for public use. Ready means it has at least one Public proof item. Otherwise write "Not ready" and the reason.
8. For each persona in personas.md, in file order, write one message of 20 words at most that uses their words and speaks to what they are measured on. Reuse the current line if it still passes step 3.
9. For each persona, take the first objection and answer it in 25 words at most, using only product facts and permitted proof. If the context pack has no answer, write [answer needed].
10. Copy "Words to use" and "Words to avoid" unchanged. Propose up to 3 additions to each, with a reason: use words come from persona quotes, avoid words come from what the product is not.
11. Keep competitor names out of the one-sentence description, pillars and persona messages, because that copy may reach ads. Names belong only in "Why it differs".
12. Rewrite pillars and messages to match the voice traits and rules in brand-voice.md.
13. Check the draft against the context pack: no contradiction with product.md, no word from "words to avoid", no internal number, no roadmap item, every proof status correct. Fix what fails.
14. List everything you assumed, inferred or could not find in the last section, each with its label.

## Output format

```
Status: Draft

## Core
Positioning statement: <copied unchanged>
One-sentence description: <15 words at most, no competitor names>

## Pillars
Pillar 1: <8 words at most>
Why it differs: <25 words at most>
Proof: <item, source file, permission status; 3 items at most>
Public use: <Ready, or Not ready and why>
(Repeat for pillars 2 and 3. Three pillars at most.)

## Messages by persona
For each persona, in file order:
<Persona>: <message, 20 words at most>
Objection: <first objection from the persona file>
Answer: <25 words at most, or [answer needed]>

## Words to use
<Current list>. Proposed: <up to 3, with reason>

## Words to avoid
<Current list>. Proposed: <up to 3, with reason>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does each pillar trace back to the positioning statement?
- [ ] Does each pillar have proof with a permission status, or a visible gap?
- [ ] Is any pillar marked "Ready" without Public proof?
- [ ] Does every persona in the context pack have one message?
- [ ] Are the objection answers built from product facts, with gaps left as placeholders?
- [ ] Are competitor names limited to "Why it differs"?
- [ ] Is every message free of "words to avoid", internal numbers and roadmap items?

## Example (fictional company)

Status: Draft

**Core**

One-sentence description: CogniATion Coach won't give you the answer, so you learn to find it.

**Pillars**

Pillar 1: It asks, it does not answer. Why it differs: beats the status quo only, telling staff to check what the AI assistant says. Proof: Lena Marsh quote, proof-points.md, Public. Public use: Ready.

Pillar 2: People keep practicing. Why it differs: beats the status quo only, where earlier tools went unused. Proof: 72% of assigned learners practiced at least weekly, Q3 2026, proof-points.md, Public. Public use: Ready.

Pillar 3: You can see reasoning improve. Why it differs: three prospects described Deliberon's reports as completion data and quiz scores (calls, 2026). Proof: Brightmere Advisory's 22% rise in client memo reasoning scores, proof-points.md, Public. Public use: Ready.

**Messages by persona**

Head of learning: show that training changed how people reason, not only that they finished it. Objection: "People won't make time for another training tool." Answer: sessions run about 15 minutes, and 72% of assigned learners practiced at least weekly in Q3 2026.

VP of people: build judgment in junior staff, with no individual's conversation ever on display. Objection: "Is this another AI tool I have to defend to legal?" Answer: not a psychometric test, not for hiring or performance decisions. Leaders never see an individual's conversation.

**Words to use**

Reasoning, judgment, assumptions, practice, scenario. Proposed: none.

**Words to avoid**

Current list, unchanged. Proposed: none.

**Assumptions and open questions**

- Assumption: messaging.md is current. Condensed: positioning statement and two personas left out.
- Assumption: description trimmed from messaging.md to fit 15 words.
- Inference: Pillars 1 and 2 beat only the status quo, from competitors.md.
- Unknown: What can we tell legal about uploaded documents?

## How to run it

```
Use the skill "Build a messaging framework". Read the context pack.
Task: <what they want>.
```
