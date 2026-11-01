---
title: Write an interview guide
type: skill
function: segmentation-icp-and-personas
owner: insights-analyst
reads: [icp-and-segments, personas, messaging, product, proof-points, channels-and-tools]
you_bring: What you need to learn, and a list of customers or lost deals to choose from if you have one.
also_for: [customer interviews, lost deal interviews, talk to customers, interview questions, why we lost deals, voice of the customer, recruit customers for research]
version: 0.1.0
updated: 2026-11-02
summary: Writes the questions, recruiting list and invitation for customer or lost-deal conversations, plus a note-taking format that feeds Synthesize customer research.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this before you talk to customers or to buyers from lost deals, when you have a question and no notes yet. Do not use it once you have notes; use [Synthesize customer research](synthesize-customer-research.md) instead. For patterns in a CRM export of won and lost deals, use [Analyze wins and losses](../competitive-intelligence/analyze-win-loss.md).

## Inputs

- [[context-pack:icp-and-segments]]: segments, fit criteria and triggers.
- [[context-pack:personas]]: roles, objections and daily problems, to test.
- [[context-pack:messaging]]: pillars, to keep out of the questions.
- [[context-pack:product]]: limits and roadmap rules, so the interviewer promises nothing.
- [[context-pack:proof-points]]: permission status of customers and quotes.
- [[context-pack:channels-and-tools]]: hard rules.

The marketer supplies the research question, the kind of conversation (customer, lost deal or both) and minutes per conversation. Optional: a list with only name, title, company, segment, outcome, date and account owner.

## Procedure

1. Fix one research question and the decision it informs. If there are several, ask which comes first. If there is none, ask before drafting.
2. Set the sample: at least 5 conversations per group, a group being one kind of conversation in one segment (a starting rule). Synthesize customer research rates a finding Strong at 3 sources, and five leaves room for that.
3. Build the recruiting list from the pasted list and proof-points.md only. Never invent a name. With no list, write the selection criteria and rows of [name needed]. Rank by fit with the ICP, then a purchase or loss in the last 6 months (a starting rule), then a group the context pack says little about. Flag anyone with an open deal or dispute. Name who makes each introduction, or [account owner needed].
4. Write the invitation in at most 80 words: why you are asking, the length, no sales pitch, and that nothing is quoted or named without written approval. For lost deals, add that you are not reopening the deal. Mention an incentive only if the marketer approved one. Nothing is sent; outreach comes back to the marketer.
5. Write at most 10 open questions for 30 minutes, in proportion for other lengths (a starting rule). Ask about what happened, not what the person would do. Tag each with one theme type from Synthesize customer research, and cover all six: trigger, problem, objection, alternative considered, outcome, language. For lost deals, ask what they chose and what has happened since.
6. Check the draft against the context pack: each question tests an entry in personas.md, icp-and-segments.md or messaging.md without quoting it. No pillar wording, product name or competitor name appears until the person brings it up. Nothing breaks a hard rule.
7. Write the interviewer rules: no pitching, no promises about features or roadmap, ask "why?" and then wait. The person who sold the deal does not run the conversation (a starting rule).
8. Write the note-taking format, one block per conversation, in the fields Synthesize customer research uses. The person's own words go in quotation marks. Anything else is marked notes.
9. Set the next steps: paste all blocks into [Synthesize customer research](synthesize-customer-research.md). Every quote stays internal until cleared with [Request customer proof](../product-marketing-and-sales-enablement/request-customer-proof.md).
10. List everything assumed or unknown in the last section, including any group the sample leaves out.

## Output format

```
Status: Draft
Research question: <one, up to 25 words>
Decision it informs: <up to 20 words>
Conversations: <number, kind, minutes each>

## Recruiting list
| Rank | Person, title and company | Group | Why them | Who introduces |

## Invitation
Subject: <50 characters at most>
Body: <80 words at most>

## Interview guide
Opening: <what the interviewer says, up to 40 words>
| # | Question | Theme type | What it tests |
<up to 10 rows>

## Interviewer rules
- <up to 5 lines>

## Note-taking format
Source: S<number>
Type and date: <customer or lost deal, date>
Role and segment: <role, segment>
How chosen: <list rank or introduction>
Excerpts: <one per line>
- <theme type>: "<word for word>" or notes: <paraphrase>
Quote status: internal only, unless proof-points.md says otherwise

## Next steps
<When to paste the notes, and into which skill, up to 25 words>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Is there one research question, tied to one decision?
- [ ] Does every name on the list come from the marketer or the context pack?
- [ ] Do the questions ask about past events, with no pillar wording?
- [ ] Are all six theme types covered?
- [ ] Does the invitation say that nothing is quoted without written approval?
- [ ] Does the note format separate word-for-word quotes from notes?

## Example (fictional company)

**Status:** Draft

**Research question:** Why do professional services firms move past the annual workshop, or stay with it?

**Decision it informs:** Which pillar leads the February 15 campaign.

**Conversations:** 5 customers and 5 lost deals, 30 minutes each.

**Recruiting list**

| Rank | Person, title and company | Group | Why them | Who introduces |
|---|---|---|---|---|
| 1 | Lena Marsh, head of learning, Brightmere Advisory | Customer | Same segment | [account owner needed] |
| 2 | [name needed] | Lost deal | Lost in the last 6 months | [account owner needed] |

**Invitation**

Subject: 30 minutes on how you chose training

Body: [First name], we are trying to understand how firms decide on training for how people reason. Could I ask you about it for 30 minutes? I will not sell you anything, and nothing gets quoted or named without your written approval.

**Interview guide** (three of 10 questions)

| # | Question | Theme type | What it tests |
|---|---|---|---|
| 1 | What happened that made you look at this? | Trigger | Triggers in icp-and-segments.md |
| 2 | What did you do before, and what happened after? | Alternative considered | What buyers do today |
| 3 | Tell me about the last time you had to show training worked. | Problem | Head of learning objection |

**Next steps:** After the tenth conversation, paste all notes into Synthesize customer research.

**Assumptions and open questions**

- Assumption: Lena Marsh is willing to talk.
- Unknown: can you paste lost deals from the CRM?
- Unknown: the sample leaves out software and financial services. Is that acceptable?

## How to run it

```
Use the skill "Write an interview guide". Read the context pack.
Task: write the guide for <customer or lost-deal> conversations, to answer <research question>. Any list of names is pasted below.
```
