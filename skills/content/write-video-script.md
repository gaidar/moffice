---
title: Write a video script
type: skill
function: content
owner: content-lead
reads: [company, product, personas, messaging, proof-points, brand-voice, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Produces a script for one short video, up to 120 seconds, with time, shot, spoken line and on-screen text in columns.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this for one short video of up to 120 seconds: a how-to clip, a product explainer, a customer clip or an event promo. Do not use it for a live session; use [Plan a webinar](../events-and-webinars/plan-webinar.md) instead.

## Inputs

- [[context-pack:personas]]: the viewer's daily problem and objections.
- [[context-pack:product]]: what can be shown, what it is not, roadmap limits.
- [[context-pack:messaging]]: messages by persona, words to avoid.
- [[context-pack:proof-points]]: customers, numbers and quotes with permission status.
- [[context-pack:company]]: leaders who can be named or quoted, publishable numbers.
- [[context-pack:brand-voice]]: voice, rules and visual basics.
- [[context-pack:channels-and-tools]]: the video channel, approvers and hard rules.

The marketer supplies the topic, video type, length, available footage and who will speak.

## Procedure

1. Fix the video type, one viewer from personas.md, one goal and the length from the request. If the type or goal is missing, ask. If no length is given, use 30 seconds for a how-to clip or promo and 60 seconds for an explainer or customer clip. Past 120 seconds, ask the marketer to split it or cut it. These lengths are starting rules the marketer can change.
2. Set the spoken word budget: length in seconds times 2 to 2.5 words a second (typical range, estimate). Show the arithmetic.
3. Choose one point. If the source holds more, keep the one closest to the viewer's daily problem or objection, or the first on a tie (a starting rule), and list the rest as cut.
4. Write three to eight rows, in time order. The first row runs up to 5 seconds and states the problem or the job. The middle rows show it being done. The last row gives the one action.
5. Write each shot as something the marketer can film or record: a named scenario, a task, a screen recording of a named feature. Follow the visual basics in brand-voice.md. If the scenario is not known, write [scenario needed]. List footage that does not exist yet under Footage needed.
6. No row's spoken line may run above the word rate in step 2.
7. Write on-screen text so the point still lands with the sound off, with no claim the spoken line does not support.
8. Name speakers only if company.md lists them as people who can be named or quoted, or proof-points.md has a public quote from them. Write a named person's line as [approved line needed] unless it is an approved quote. Otherwise use "narrator".
9. Use a customer name, number or quote only if proof-points.md marks it public, and a company number only if company.md marks it publishable. If a claim in messaging.md has no entry in proof-points.md, leave it out and ask. Do not name competitors. Filming at a customer's site needs that customer's permission, so list it under Approvals needed.
10. Show only features that exist today in product.md. Check the script against the context pack: facts, permissions, words to avoid, voice rules. Count the spoken words and enter the count.
11. List everything assumed under "Assumptions and open questions". If a needed context pack field is blank, including the approver for video, leave a placeholder in square brackets and ask in the last section. Never invent.

The marketer films and edits from the script. This skill produces and publishes nothing.

## Output format

```
Status: Draft
Title: <up to 60 characters, sentence case>
Video type: <how-to, explainer, customer clip or promo>
Channel: <from channels-and-tools.md>
Viewer: <one persona, up to 8 words>
Goal: <one sentence, up to 15 words>
Length: <seconds, up to 120>
Word budget: <Estimate: seconds times 2 to 2.5 words a second>
Spoken word count: <actual count>

## Script
| Time | Shot | Spoken line | On-screen text |
|---|---|---|---|
<3 to 8 rows; shot up to 15 words; on-screen text up to 7 words>

## Production notes
Speakers: <narrator or named person, with basis>
Footage needed: <each item, or "None">
End card: <text, up to 10 words, and logo rule from brand-voice.md>
Proof used: <each item and its permission status, or "None">
Cut from this script: <other points left out, or "None">

## Approvals needed
<approver and typical time from channels-and-tools.md, or [approver needed]>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the video make one point to one viewer, with one action?
- [ ] Is the spoken word count within the word budget, with the arithmetic shown?
- [ ] Does the first row state the problem or job within 5 seconds?
- [ ] Can every shot be filmed or recorded, or is it listed under Footage needed?
- [ ] Are all speakers, customers, numbers and quotes cleared in the context pack?
- [ ] Do the visuals follow brand-voice.md, with no stock images it rules out?
- [ ] Does every feature shown exist today?

## Example (fictional company)

**Status:** Draft

**Title:** Answer "why?" before your manager asks

**Video type:** How-to. **Channel:** Video channel. **Viewer:** Analyst or new manager.

**Goal:** Show how to practice answering "why?" in a session

**Length:** 30 seconds. **Word budget:** 60 to 75. **Spoken word count:** 61.

**Script**

| Time | Shot | Spoken line | On-screen text |
|---|---|---|---|
| 0–5 | Printed draft with "why?" in the margin | Your draft came back with "why?" on it. Now what? | "Why?" on your draft |
| 5–11 | Scripted demo: [scenario needed] opens | Open a work scenario and state your recommendation, in your own words. | Start from a work scenario |
| 11–18 | Scripted demo: CogniATion Coach asks for an assumption | CogniATion Coach won't write it for you. It asks for your assumptions and evidence. | It asks, it does not answer |
| 18–24 | Scripted demo: the Coach asks for an alternative | Then it asks what else you considered, and why that lost. | What else did you consider? |
| 24–30 | Logo on plain background | The Coach takes about 15 minutes a session. Share this with your learning team. | CogniATion Coach |

**Production notes**

Speakers: narrator. Footage needed: printed draft, scripted demo recording. End card: cogniation.example, logo on plain background. Proof used: None. Cut from this script: team reports.

**Approvals needed:** The marketer, same day.

**Assumptions and open questions**

- Assumption: the demo is illustrative, with no real learner's conversation or score.
- Estimate: word budget is 30 seconds times 2 to 2.5 words a second.
- Inference: analysts do not research training software, so the clip asks them to share it (personas.md).
- Unknown: which scenario should the clip show?

## How to run it

```
Use the skill "Write a video script". Read the context pack.
Task: <the topic, video type, length, and the footage and speakers you have>.
```
