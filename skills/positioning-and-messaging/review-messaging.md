---
title: Review messaging
type: skill
function: positioning-and-messaging
owner: marketing-reviewer
reads: [company, product, icp-and-segments, personas, messaging, competitors, proof-points, channels-and-tools]
you_bring: The text to review, unless it is messaging.md, and whether its use is public, sales only or internal.
also_for: [does our message hold up, is our messaging clear, claims check, can we say this, messaging sounds like everyone, sales ignores the messaging, differentiation check, website sounds generic]
version: 0.1.0
updated: 2026-11-02
summary: Critiques messaging or positioning claim by claim for accuracy, proof and differentiation, and gives a verdict.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this on a positioning statement, a messaging framework or a set of claims before anyone builds on them. Do not use it on finished copy such as a page, an email or an ad; use [Review any output](../marketing-ops/review-any-output.md) instead. This skill critiques and does not rewrite; to produce new messaging, use [Build a messaging framework](build-messaging-framework.md).

## Inputs

From the context pack:

- [[context-pack:messaging]] – the text under review if none is pasted, and words to avoid
- [[context-pack:product]] – features, what it is not, known weak spots, roadmap rule
- [[context-pack:proof-points]] – evidence and permission status
- [[context-pack:competitors]] – dated facts, where each wins and loses
- [[context-pack:personas]] – what each persona is measured on
- [[context-pack:icp-and-segments]] – the target and its disqualifiers
- [[context-pack:company]] – which company numbers may be published
- [[context-pack:channels-and-tools]] – hard rules and approvers

The marketer supplies in the prompt: the text to review, if it is not messaging.md, and the intended use: public, sales only or internal.

## Procedure

1. Take the pasted text, or messaging.md if nothing is pasted. If both are blank, ask for the text.
2. Set the intended use from the prompt. If it is missing, treat the text as public, the strictest case, and record that as an assumption.
3. Split the text into numbered claims. A claim is any statement a buyer could check or dispute. Quote each one exactly, at most 20 words.
4. Run the accuracy test on each claim: does product.md support it, and does it stay clear of "What it is not", "Known weak spots" and roadmap items? A claim stronger than the fact fails. A claim with no fact in product.md is marked unknown, not false.
5. Run the proof test: is there an item in proof-points.md, or a publishable number in company.md, that backs this exact claim, with a permission status that allows the intended use? Proof that measures something else fails. An item with no entry in proof-points.md fails for public use and is listed as unknown. A plain capability that product.md supports needs no proof item.
6. Run the differentiation test: put each named competitor's name in the claim. If competitors.md suggests the sentence would still be true of all of them, mark "true of all". If of some, mark "true of some" and name them. If competitors.md is silent, write "cannot tell" and list it as unknown, without guessing.
7. Run the rules test: words from "words to avoid", competitor claims with no source and date, competitor names in text meant for ads, a target that conflicts with the disqualifiers, and a message that misses what its persona is measured on.
8. Rate each failure. Blocker: false, contradicts the context pack, or uses proof not permitted for the intended use. Major: a claim stronger than the fact, no proof, proof that measures something else, or "true of all" on a pillar. Minor: wording, or any other differentiation result short of "cannot tell".
9. Set the verdict. Any blocker: "Do not use". No blocker and at least one major: "Fix first". Otherwise: "Facts and proof checked". End every verdict with "Strategy not judged."
10. Name the single weakest idea in the text, the one a senior marketer would push on first. Ask it as a question for the marketer, and say why. It does not change the verdict.
11. For each finding, name the evidence by file and field, and give a fix direction in 20 words at most. Do not rewrite the claim unless the marketer asks.
12. List the claims that passed all tests, so the marketer knows what to keep.
13. Check the review against the context pack: every finding cites a real field, and competitor statements stay within competitors.md.
14. List everything you assumed, inferred or could not verify in the last section, each with its label.

## Output format

```
Status: Draft

## Verdict
<Do not use, Fix first or Facts and proof checked>, for <intended use>. Strategy not judged. <Reason, 40 words at most>
Weakest idea: <the single weakest idea, and why, as a question for the marketer, 30 words at most>

## Findings
| # | Claim | Test failed | Severity | Evidence | Fix direction |
(most severe first, 12 rows at most)

## Claims that passed
- <claim; 6 items at most>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Was every claim tested, not only the weak-looking ones?
- [ ] Does each finding cite a file and field?
- [ ] Does the verdict follow the severity rule?
- [ ] Was proof checked for what it actually measures, not only whether it exists?
- [ ] Was permission checked against the stated use?
- [ ] Are competitor statements limited to what the competitors file holds?
- [ ] Did the review stay a critique, with no rewriting unasked?

## Example (fictional company)

Status: Draft

**Verdict**

Do not use, for public. Strategy not judged. One claim promises a view of individuals that the product rules out, and two say more than the proof shows.

Weakest idea: why lead with "a chatbot built for practice", when Arguvia can say it too and your buyer's worry is showing that training worked?

**Findings**

| # | Claim | Test failed | Severity | Evidence | Fix direction |
|---|---|---|---|---|---|
| 1 | "Leaders can see how each person reasons" | Accuracy | Blocker | product.md: progress by team, never an individual's conversation | Claim team-level progress only |
| 2 | "Better reasoning in your first two weeks" | Proof | Major | proof-points.md: median of 9 days measures first live session, not reasoning | Claim only what 9 days shows |
| 3 | "Every learner practices every week" | Proof | Major | proof-points.md, Result 2: 72% of assigned learners, Q3 2026 | Use the actual figure |
| 4 | "A chatbot built for practice" | Differentiation | Minor | True of some: competitors.md lists Arguvia as a debate practice chatbot | Say which alternative this beats |

**Claims that passed**

- "It asks, it does not answer"
- "Brightmere's analysts raised client memo reasoning scores 22% in one quarter of 2026, as measured by Brightmere's partners"

**Assumptions and open questions**

- Assumption: public use, because none was stated.
- Assumption: the failed claims come from an illustrative draft pasted for this example, not from messaging.md.
- Inference: Finding 4 rests on Arguvia's category alone.
- Unknown: Does Arguvia also decline to give answers? competitors.md is silent, so "It asks" is marked cannot tell.

## How to run it

```
Use the skill "Review messaging". Read the context pack.
Task: <public, sales only or internal use>.
<paste the text here, unless it is messaging.md>
```
