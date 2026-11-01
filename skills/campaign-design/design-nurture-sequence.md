---
title: Design a nurture sequence
type: skill
function: campaign-design
owner: demand-generation-manager
reads: [icp-and-segments, personas, messaging, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
you_bring: Who enters and from which source, what counts as success, and which resources already exist.
also_for: [drip campaign, email sequence, leads not ready, cold leads, lead nurturing, warm up leads, automated emails, old demo requests]
version: 0.1.0
updated: 2026-11-01
summary: Designs a multi-email nurture with entry and exit rules, one purpose per email and a copy outline for each.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this for a series of emails to leads who are not ready to talk to sales. Do not use it for one standalone email or newsletter, which belongs in [Write a marketing email](../content/write-marketing-email.md). For the campaign that feeds the sequence, use [Write a campaign brief](write-campaign-brief.md) instead.

## Inputs

- [[context-pack:icp-and-segments]]: segment, disqualifiers, triggers, sales cycle length.
- [[context-pack:personas]]: who reads the emails, their objections.
- [[context-pack:messaging]]: pillars, messages by persona, words to avoid.
- [[context-pack:proof-points]]: proof per email and its permission status.
- [[context-pack:brand-voice]]: tone and rules for the copy.
- [[context-pack:goals-and-kpis]]: MQL and SQL definitions, which set the exit rules.
- [[context-pack:channels-and-tools]]: email list size, tools, approvers.

The marketer supplies in the prompt: who enters and from which source, what action counts as success, and which resources already exist.

## Procedure

1. Write the entry rule as a yes/no test on data the marketer's tools can see: source, segment, and action taken. If a lead already meets the MQL definition or has hit a trigger, keep them out and send them to sales.
2. Write the exit rules: met the MQL definition, requested a demo, accepted by sales, unsubscribed, matched a disqualifier, or finished the sequence. Name what happens next at each exit.
3. Set the length from the sales cycle in icp-and-segments.md: 3 emails if under 30 days, 5 if 30 to 90 days, 7 if longer. If the cycle is blank, use 5, label it an assumption and ask in the last section. These lengths and the spacing in step 4 are starting rules the marketer can change, not benchmarks.
4. Set the spacing: 3 days between the first two emails, then 7 days, unless the marketer's list rules differ. Count each send day from entry.
5. Choose one persona as the reader: the marketer's choice, or the first in personas.md (a starting rule). Skip any role personas.md says does not research software.
6. Give each email one job, in this order: name the trigger or problem, answer the top objection, show proof, answer the next objection, ask for the next step. If personas.md lists only one objection, use a pillar for the second. For 3 emails, keep the first, third and last jobs. For 7, add a use-case email and a how-it-works email before the last.
7. For each email, name one objection or pillar, one proof item with status, and one call to action. Use only Public proof, since email is not one-to-one sales material. If no proof fits, write [proof needed]. If a resource is not in the marketer's list, write [resource needed].
8. Write an outline for each email, not finished copy, following brand-voice.md.
9. Name the measures: share of leads reaching the success exit, unsubscribes per email, clicks per email. Leave targets as [target needed] unless the marketer gave them.
10. Check the draft against the context pack: disqualifiers, words to avoid, proof status, roadmap, voice rules. Fix what contradicts it.
11. List everything assumed, estimated, inferred or unknown in the last section, using those labels.

## Output format

Repeat the outline block for every email.

```
Status: Draft

## Sequence summary
Name: <short name>
Reader: <one persona>
Success: <one action>

## Entry and exit rules
Entry: <yes/no test, up to 30 words>
Keep out: <who never enters>
Exit: <event> – <what happens next>

## Sequence map
| Email | Send day | Job | Objection or pillar | Proof and status | Call to action |

## Copy outlines
Email <number>
Subject: <up to 60 characters>
Preview: <up to 90 characters>
Points: <up to 3, each up to 20 words>
Call to action: <up to 8 words>

## Measures
| Measure | Target | Where the marketer reads it |

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Can the entry rule be answered yes or no from data the marketer has?
- [ ] Does every exit say what happens to the lead next?
- [ ] Is a lead who meets the MQL definition removed and sent to sales?
- [ ] Does each email have exactly one job and one call to action?
- [ ] Is every proof item Public in proof-points.md?
- [ ] Do the subject lines follow brand-voice.md and avoid the listed words?

## Example (fictional company)

Status: Draft

**Sequence summary.** Name: Client memo nurture. Reader: head of learning and development. Success: demo request.

**Entry and exit rules.** Entry: professional services lead, fits the ICP, downloaded one resource, not yet an MQL. Keep out: fewer than 100 learners, wants a course library, wants scores on individuals for performance reviews. Exit: second download, webinar or demo request – goes to sales as an MQL. Unsubscribed – removed. Finished – back to the monthly newsletter.

**Sequence map**

| Email | Day | Job | Objection or pillar | Proof and status | Call to action |
|---|---|---|---|---|---|
| 1 | 0 | Problem | Finished, but no change shown | None | Read the guide |
| 2 | 3 | Objection | "People won't make time for another training tool." | 72% weekly session result, Public | Watch a scenario |
| 3 | 10 | Proof | It asks, it does not answer | Lena Marsh quote, Public | See how it works |
| 4 | 17 | Objection | "How would I show the leadership team that it worked?" | Brightmere Advisory 22% result, Public | See a team report |
| 5 | 24 | Next step | People keep practicing | 9-day median, Public | Request a demo |

**Copy outlines.** Email 2. Subject: Will your people make time for one more tool? Preview: What learners did in Q3 2026. Points: practice on real work problems; 72% of assigned learners completed at least one session each week in Q3 2026. Call to action: Watch a scenario.

**Measures.** Demo requests from the sequence: [target needed].

**Assumptions and open questions**

- Assumption: the guide and a team-level sample report exist.
- Unknown: what target do you want for demo requests from this sequence?

## How to run it

```
Use the skill "Design a nurture sequence". Read the context pack.
Task: <who enters and from which source, what counts as success, and which resources exist>.
```
