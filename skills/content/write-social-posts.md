---
title: Write social posts
type: skill
function: content
owner: content-lead
reads: [company, product, personas, messaging, proof-points, brand-voice, channels-and-tools]
you_bring: One source idea or pasted text, the link to use, and each channel's character limit.
also_for: [social media posts, professional network post, promote a blog post, post ideas, company page posts, repurpose content, organic social]
version: 0.1.0
updated: 2026-11-01
summary: Produces a set of social posts from one source idea, by channel, each with a different angle and one action.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this to turn one source idea, such as a blog post, a page, a result or a note, into a set of organic posts. Do not use it for paid copy; use [Write ad variations](../paid-demand-gen/write-ad-variations.md) instead. For deciding what to post across a month, use [Plan a content calendar](plan-content-calendar.md).

## Inputs

- [[context-pack:channels-and-tools]]: which social accounts exist, their cadence, approvers and hard rules.
- [[context-pack:personas]]: the reader's daily problem, objections and where they get information.
- [[context-pack:messaging]]: messages by persona, words to use and avoid.
- [[context-pack:product]]: what the product does, what it is not, roadmap limits.
- [[context-pack:proof-points]]: customers, numbers and quotes with permission status.
- [[context-pack:company]]: which company numbers may be published.
- [[context-pack:brand-voice]]: voice, rules and visual basics.

The marketer supplies the source idea or pasted source text, the link to use, the number of posts if not the default, and the character limit for each channel.

## Procedure

1. Reduce the source to one sentence, the source idea. If the marketer supplied no source, ask. Do not choose a topic on your own. The reader is the persona whose daily problem is closest to it, or the first listed on a tie (a starting rule).
2. Pick the channels. Write only for the accounts listed in channels-and-tools.md, unless the marketer names another. If that field is blank, ask.
3. Set the count: three posts per channel by default, or the marketer's number, up to six.
4. Set the limit for each channel. Use the character limit the marketer supplied. If none was supplied, keep the post to the template's word limits and record the missing limit as an Unknown. Do not state a channel's limits from memory.
5. Give each post a different angle, in this order. Post 1, problem: a daily problem from personas.md. Post 2, how-to: one action the reader can take today without buying. Post 3, proof: one public proof point. If no public proof point fits, use Post 3 for an objection answer instead and say so. Posts 4 to 6, in order: objection answer, one product fact, one question drawn from the source.
6. Write each post. The first line stands alone and makes sense without the rest. The body carries one claim. The post has one action. Use the marketer's link, or write [link needed]. Add no hashtags, tags or mentions unless brand-voice.md or the marketer asks for them.
7. Adapt rather than copy. If two channels are in the set, rewrite each post for that channel's limit and reader, and do not paste the same text twice.
8. Use a customer name, number or quote only if proof-points.md marks it public, and a company number only if company.md marks it publishable. Include the sample and date with each number. If a claim in messaging.md has no entry in proof-points.md, leave it out and ask. Do not name competitors. Tag a customer only if the marketer confirms that the customer agreed.
9. Write a visual note for each post, following the visual basics in brand-voice.md. If no real image exists, write [image needed] or "no image".
10. Check every post against the context pack: facts, permissions, what the product is not, words to avoid, voice rules. Add any pricing mention to Approvals needed with the listed approver.
11. List everything assumed under "Assumptions and open questions". If a needed context pack field is blank, leave a placeholder in square brackets and ask in the last section. Never invent.

The marketer publishes the posts themselves. This skill schedules and posts nothing.

## Output format

```
Status: Draft
Source idea: <one sentence, up to 25 words>
Reader: <one persona, up to 8 words>
Link: <supplied link, or [link needed]>

## <Channel name>
Limit: <characters supplied by the marketer, or "not supplied">

### Post 1: <angle>
First line: <up to 15 words>
Body: <up to 60 words>
Action: <up to 10 words>
Visual note: <up to 15 words>
Proof used: <item and permission status, or "None">

### Post 2: <angle>
<same five fields>

### Post 3: <angle>
<same five fields>

<repeat the section for each further channel>

## Approvals needed
<approver and typical time from channels-and-tools.md>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Do all posts come from the one source idea?
- [ ] Does each post use a different angle, in the set order?
- [ ] Does each first line make sense on its own?
- [ ] Does each post carry one claim and one action?
- [ ] Is the how-to post useful to someone who never buys?
- [ ] Does every customer, number and quote have public or publishable status, with sample and date?
- [ ] Are competitors unnamed, and are the words to avoid and exclamation points absent?
- [ ] Does each post fit the limit the marketer supplied?

## Example (fictional company)

**Status:** Draft

**Source idea:** Show that training changed how people reason, not only that they finished it.

**Reader:** Head of learning and development

**Link:** [link needed]

**Professional social network**

Limit: not supplied

**Post 1: problem**

First line: Everyone finished the course. Can you show it changed how they work?

Body: CogniATion Coach questions your people on work problems and shows you progress by team. You never see an individual's conversation.

Action: See how it works.

Visual note: Team-level report screenshot with no individual names, or [image needed].

Proof used: None

**Post 2: how-to**

First line: Try this with one client memo this week.

Body: Pick one recommendation. Ask the author for the assumption behind it, the evidence for it and one alternative they rejected. Note what they can't answer.

Action: Read the full checklist.

Visual note: No image.

Proof used: None

**Post 3: proof**

First line: "My analysts stopped asking the bot for the answer and started defending their own."

Body: Lena Marsh, head of learning, Brightmere Advisory. Brightmere's analysts raised their average score on client memo reasoning by 22% in one quarter of 2026, as measured by Brightmere's partners.

Action: Request a demo.

Visual note: [image needed]

Proof used: Marsh quote and 22% result, public.

**Approvals needed:** The marketer, same day.

**Assumptions and open questions**

- Assumption: a blog post with a checklist exists for Post 2 to link to.
- Unknown: what is the character limit for this channel?

## How to run it

```
Use the skill "Write social posts". Read the context pack.
Task: <the source idea or pasted source, the link, and each channel's character limit>.
```
