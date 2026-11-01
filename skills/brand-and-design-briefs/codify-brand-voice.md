---
title: Codify the brand voice
type: skill
function: brand-and-design-briefs
owner: brand-and-creative-director
reads: [company, personas, messaging, proof-points, brand-voice]
version: 0.1.0
updated: 2026-11-01
summary: Builds or updates brand-voice.md from writing samples the marketer pastes, with evidence for every rule.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this when brand-voice.md is blank, or when the company's writing has changed and the file no longer describes it. Do not use it to check one piece of writing against the voice; use [Review any output](../marketing-ops/review-any-output.md) instead. Do not use it to change what the company claims; use [Build a messaging framework](../positioning-and-messaging/build-messaging-framework.md) instead.

## Inputs

- [[context-pack:brand-voice]]: the current file, if filled, to compare against the samples.
- [[context-pack:company]]: public name.
- [[context-pack:personas]]: who the writing is for, to set the reading level.
- [[context-pack:messaging]]: words to use and words to avoid, so that the voice does not contradict them.
- [[context-pack:proof-points]]: which quotes belong to customers, so that they are not counted as the company's voice.

The marketer supplies in the prompt: at least five writing samples the company has published or would publish, ideally from more than one channel, each marked with its channel and date. Add any lines the company would never publish, and any visual rules.

## Procedure

1. Sort the samples. Remove customer quotes, including any in proof-points.md, as well as legal text and anything written by another company. Mark each remaining sample with its channel. If fewer than five remain, ask for more. If the marketer wants a draft anyway, mark every trait "low evidence".
2. Find what repeats. For each sample, note sentence length, point of view, use of jargon, use of numbers, how headlines are written, and what the writing does with the reader. Keep only a pattern seen in at least three samples. Five samples and three repeats are starting rules the marketer can change.
3. Choose three traits. Each trait must be one adjective plus what it means in practice, must come from a pattern in step 2, and must rule something out. Reject any trait that nearly every company would claim, such as "professional" or "friendly".
4. Attach evidence. For each trait, quote one short line from a sample. If you cannot quote one, drop the trait.
5. Set the reading level from the personas.md reader the samples speak to most, as one line naming the reader and where they read.
6. Set the point of view from what the samples do. If they disagree, use the one in the majority and flag the rest.
7. Write three to five Do rules and three to five Do not rules. Each must be something a writer can check on a sentence. Refer to words to avoid in messaging.md, without repeating the list.
8. Write style details from the samples: spelling, capitalization, product name. Where the samples are inconsistent, pick the most frequent form and flag the choice.
9. Choose "sounds like us" from the samples, word for word. Choose "does not sound like us" from lines the marketer supplied. If there are none, write one and mark it "written by the model" under assumptions.
10. Fill visual basics only from the prompt or the current file. Writing samples say nothing about color or logos, so otherwise leave [visual rules needed]. If any other field is blank and the samples do not settle it, leave a visible placeholder in square brackets and ask in the last section. Never invent.
11. If brand-voice.md is already filled, list each change and the sample that supports it. Keep a rule the samples do not contradict. Remove a rule only if the marketer agrees.
12. Check the draft against the context pack: the voice must not contradict messaging.md, and no customer's words may be used as the company's.
13. List everything you assumed, and each low-evidence rule, in the last section.

This skill saves nothing. The marketer copies the file section into brand-voice.md after deciding what to keep.

## Output format

```
Status: Draft

## Brand voice file
Copy this into brand-voice.md.

### Voice
Voice in three traits:
- <Trait>: <what it means in practice, 15 words maximum>
Reading level: <one line>
Point of view: <one line>

### Rules
Do:
- <3 to 5 habits, one line each>
Do not:
- <3 to 5 habits, one line each>
Style details: <spelling, capitalization, product name>

### Examples
Sounds like us: <one or two sentences, word for word from a sample>
Does not sound like us: <one or two sentences>

### Visual basics
Colors, type and logo rules: <from the prompt or the current file, or [visual rules needed]>

## Evidence
| Trait or rule | Quoted line, 15 words maximum | Sample channel and date |
<One row for each trait, and for each rule resting on a sample>

## Changes from the current file
- <Change, and the sample behind it. Write "New file" if brand-voice.md was blank>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Could a writer check each Do and Do not rule on a single sentence?
- [ ] Does each trait rule something out, and have a quoted line behind it?
- [ ] Is every quoted line from the company's own writing, with no customer's words?
- [ ] Is the "sounds like us" line word for word from a sample?
- [ ] Are the visual rules from the marketer or the current file, not guessed?
- [ ] Does the file agree with words to avoid in messaging.md?

## Example (fictional company)

**Status:** Draft

**Brand voice file**

**Voice**

Voice in three traits:

- Plain: short words, no learning jargon.
- Curious: asks a real question where others would make a claim.
- Respectful: assumes the reader is capable, and never talks down about AI users.

Reading level: a busy head of learning reading between meetings.

Point of view: "we" for CogniATion, "you" for the reader.

**Rules**

Do: name the work (the memo, the decision, the client call). Use numbers only from proof-points.md or the publishable list in company.md.

Do not: no exclamation points. No warnings that AI is making people stupid.

Style details: CogniATion, never Cogniation or COGNIATION. The Coach on second mention.

**Examples**

Sounds like us: Your analysts have answers. Can they defend them?

Does not sound like us: Unlock your team's cognitive potential with next-generation AI.

**Visual basics**

Primary deep blue, secondary warm gray, one sans-serif typeface. Logo on plain backgrounds only, never on photos. No images of glowing brains or robots.

**Evidence**

| Trait | Quoted line | Sample |
|---|---|---|
| Plain | "It asks, it does not answer" | messaging.md, channel unknown |
| Curious | "Your analysts have answers. Can they defend them?" | brand-voice.md, channel unknown |

**Changes from the current file**

None.

**Assumptions and open questions**

- Assumption: lines from messaging.md and brand-voice.md stand in for pasted samples, so all traits are low evidence.
- Unknown: can you paste five published samples?

## How to run it

```
Use the skill "Codify the brand voice". Read the context pack.
Task: <what they want>.
```
