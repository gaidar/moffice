---
title: Write ad variations
type: skill
function: paid-demand-gen
owner: paid-media-manager
reads: [personas, messaging, proof-points, brand-voice, channels-and-tools]
you_bring: The channel, the audience, the destination page, and the character limit for every ad field.
also_for: [ad copy, ad headlines, search ad text, ads to test, new ad creative, social ad copy, ad fatigue, demo ad]
version: 0.1.0
updated: 2026-11-01
summary: Writes ad copy sets by angle, within the character limits the marketer supplies.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when a paid plan names the channel, audience and angles and you need copy to test. Do not use it for organic posts, which belong in [Write social posts](../content/write-social-posts.md). If channel, audience and budget are still open, use [Plan a paid campaign](plan-paid-campaign.md) first instead.

## Inputs

- [[context-pack:personas]]: the audience's language, daily problem and objections.
- [[context-pack:messaging]]: pillars as angles, messages by persona, words to use and avoid.
- [[context-pack:proof-points]]: numbers and quotes, and whether they may appear in public.
- [[context-pack:brand-voice]]: voice, do and do-not rules, style details.
- [[context-pack:channels-and-tools]]: hard rules on ads, and who approves what.

The marketer supplies in the prompt: the channel, the audience, the destination page, and the character limit for every ad field on that channel. Optional: the number of angles, and past ads with their results.

## Procedure

1. Get the character limits. If the marketer did not give them, ask and stop. If they want a draft anyway, write to [limit needed] and mark every length as unchecked. Do not use limits from memory.
2. Choose angles. Use the angles from the marketer or the paid plan. Otherwise, take one angle from each pillar in messaging.md, plus one from the persona's daily problem, up to 4 in total. Drop a pillar that has no public proof and no plain benefit to state.
3. Write 2 variations per angle. The two must differ in one thing only, such as the opening claim or the call to action, so a result can be read. Fill every field the marketer listed.
4. Apply the claim rules. Numbers only from proof-points.md with Public status, worded as that file words them, without dropping what the number measures. Customer names only with Public status. Do not name a competitor if channels-and-tools.md forbids it, even if the positioning statement names one. No internal numbers, no roadmap, no words from the avoid list.
5. Mention price only if the marketer asks. If an ad mentions price, list the pricing approver from channels-and-tools.md in the Approvals section.
6. Count characters for each field, including spaces and punctuation, and write the count next to it. Rewrite anything over the limit. Never cut a word in a way that changes the claim. Tell the marketer to confirm the counts in their ad tool.
7. Match each ad to the destination page. If the page does not carry the claim in the ad, flag it. If the destination is unknown, write [destination page needed].
8. Check the draft against the context pack: proof status, competitor rule, words to avoid, voice rules, spelling of the product name. Fix what contradicts it.
9. List everything assumed, estimated, inferred or unknown in the last section, using those labels. Say which angle you would test first and why, labeled as an inference.

## Output format

Repeat the table for each angle.

```
Status: Draft

## Ad set summary
Channel: <one>
Audience: <up to 20 words>
Destination: <page>
Limits: <field and character limit, as supplied>

## Angle <number>: <angle name>
Source: <pillar or persona problem>
Proof: <item and permission status, or "None">
| Variation | Field | Copy | Characters |

## Approvals
<Approver and typical time, or "None beyond the marketer">

## Test order
<Angles in test order, one line each>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Are the character limits the ones the marketer supplied?
- [ ] Is every field within its limit, with the count shown?
- [ ] Does each pair of variations differ in only one thing?
- [ ] Is every number or customer name Public in proof-points.md and worded as written there?
- [ ] Are competitors left out if channels-and-tools.md forbids naming them?
- [ ] Is the copy free of the words to avoid and the do-not rules in brand-voice.md?
- [ ] Does the destination page back up each claim?

## Example (fictional company)

Status: Draft

**Ad set summary.** Channel: search ads. Audience: heads of learning at professional services firms. Destination: professional services landing page. Limits: headline 30, description 90.

**Angle 1: See reasoning improve.** Source: pillar 3. Proof: None.

| Variation | Field | Copy | Characters |
|---|---|---|---|
| A | Headline | Can your analysts defend it? | 28 |
| A | Description | CogniATion Coach reports progress to you, with no individual's conversation on display. | 87 |

**Angle 2: Finished is not changed.** Source: head of learning's daily problem. Proof: None.

| Variation | Field | Copy | Characters |
|---|---|---|---|
| A | Headline | Did the training change work? | 29 |
| A | Description | Show that training changed how people reason, not only that they finished it. | 77 |

**Angle 3: People keep practicing.** Source: pillar 2. Proof: 72% weekly session result, Public.

| Variation | Field | Copy | Characters |
|---|---|---|---|
| A | Headline | Practice people keep doing | 26 |
| A | Description | 72% of assigned learners completed at least one session each week in Q3 2026. | 77 |

**Approvals.** None beyond the marketer.

**Test order.** Angle 1 against 3, then 2.

**Assumptions and open questions**

- Assumption: variation B is cut here to save space.
- Assumption: the marketer supplied these limits.
- Inference: angle 1 first, because the destination page cites client memos and analysts.
- Inference: the 22% Brightmere Advisory result stays on the landing page, because 90 characters cannot hold what it measures.
- Unknown: is the landing page live?

## How to run it

```
Use the skill "Write ad variations". Read the context pack.
Task: <the channel, audience, destination page, and character limit for every ad field>.
```
