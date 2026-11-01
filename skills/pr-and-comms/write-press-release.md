---
title: Write a press release
type: skill
function: pr-and-comms
owner: pr-and-communications-manager
reads: [company, product, messaging, proof-points, brand-voice, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Produces a press release with approved quotes only and visible placeholders for anything not yet cleared.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this when something has actually changed and you want a formal announcement: a release, a funding round, a milestone, a leadership hire. Do not use it to reach one specific journalist; use [Write a media pitch](write-media-pitch.md) instead. If the news fails the test in step 1, use [Write a blog post](../content/write-blog-post.md) instead.

## Inputs

- [[context-pack:company]]: public name, headquarters, one-line description, who may be quoted on what, press contact, and which numbers are publishable, internal or forbidden.
- [[context-pack:product]]: what the product does, what it is not, and whether any roadmap item is cleared.
- [[context-pack:messaging]]: one-sentence description and words to avoid.
- [[context-pack:proof-points]]: customer names, results and quotes, with permission status.
- [[context-pack:brand-voice]]: style details and things never to say.
- [[context-pack:channels-and-tools]]: who approves a press release, and how long it takes.

The marketer supplies in the prompt: the news in one sentence, the release date or embargo, any quote text the speaker has approved, and any facts about the news that the context pack lacks.

## Procedure

1. Test the news. Write one sentence saying what changed, for whom, and as of when. If you cannot, or if nothing changed, say "Weak news" in the status line and recommend a blog post, then draft anyway only if the marketer asked for a release regardless.
2. Check clearance. If the news is a product or feature that product.md does not clear for public mention, mark the status line "Not cleared for public mention" and ask who can clear it. If the prompt contains a number company.md lists as internal or forbidden, leave it out and flag it.
3. Write the headline: under 12 words, sentence case, saying what happened. No exclamation points and no adjectives about the company.
4. Write the lead paragraph: who, what, when, where, in under 50 words, opening with the dateline from the headquarters in company.md.
5. Write the body in third person, even if brand-voice.md uses "we", because other people will reuse the text. Note this under assumptions. Keep every number with its date or sample as proof-points.md or company.md states it.
6. Add quotes. Use a customer quote only word for word and only with public permission in proof-points.md. For a company leader, use quote text only if the marketer supplied it as approved. Otherwise leave [quote from name, on topic, approval needed]. Never write a quote for anyone. Keep each leader to the topics company.md gives them.
7. Do not name competitors. Do not mention pricing unless it is the news, and then list the pricing approver from channels-and-tools.md.
8. Add the boilerplate from company.md, using only facts and publishable numbers from there, and the press contact.
9. Fill the approvals block from channels-and-tools.md. If a needed field in the context pack is blank, leave a visible placeholder in square brackets and ask in the last section. Never invent.
10. Check the draft against the context pack: every name, number and quote against its permission, every word against words to avoid, every product claim against what the product is not. Fix anything that fails.
11. List everything you assumed, every placeholder still open, and every approval still needed in the last section.

## Output format

```
Status: <Draft, plus "Weak news" or "Not cleared for public mention" if either applies>
Release: <date and time, or "Embargoed until <date>", or [release date needed]>

## <Headline, under 12 words>

<City, state, date> – <Lead paragraph, under 50 words>

<Body, 2 to 3 paragraphs, 150 words maximum in total>

"<Quote>" <Name, title, company>
<One or two quotes, each word for word or a placeholder>

## About <public company name>
<Boilerplate, 50 words maximum>

## Press contact
<Contact from company.md>

## Approvals needed
- <Approver, what they approve, typical time>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the headline say what happened, with no praise of the company?
- [ ] Can you point to what changed, and when?
- [ ] Is every quote word for word, approved for public use, or a visible placeholder?
- [ ] Does every number appear in company.md as publishable or in proof-points.md as public, with its date or sample?
- [ ] Is every leader quoted only on the topics company.md gives them?
- [ ] Is the release free of roadmap items, competitor names and words to avoid?
- [ ] Are the approver and the time they need listed, with the release date allowing for it?

## Example (fictional company)

Status: Draft

Release: [release date needed]

**CogniATion Coach reaches 28,000 learners at 64 companies**

Austin, Texas, [date] – CogniATion said today that 28,000 learners at 64 customer companies had active seats on CogniATion Coach, its critical thinking training software, as of September 30, 2026.

Learners have completed more than 2.3 million practice sessions as of the same date. The Coach is a chatbot that questions employees about a work problem instead of answering it, then scores their reasoning against a rubric. Learning leaders see progress by team, and never see an individual's conversation.

"My analysts stopped asking the bot for the answer and started defending their own." Lena Marsh, head of learning, Brightmere Advisory

[Quote from Marta Ilves, CEO, on company direction, approval needed]

**About CogniATion**

CogniATion makes a specialized AI chatbot that trains employees to think through problems instead of asking for answers. Founded in 2021, it is based in Austin, Texas.

**Press contact**

press@cogniation.example

**Approvals needed**

- Marta Ilves, CEO, this release, 2 days

**Assumptions and open questions**

- Assumption: third person is used despite "we" in brand-voice.md, because other people will reuse the text.
- Assumption: the 2.3 million sessions were completed by those 28,000 learners. company.md gives both numbers but does not link them. Confirm.
- Inference: the Lena Marsh quote needs no new customer approval, because proof-points.md marks it public, approved June 2026.
- Unknown: is a learner count news to the press, or would a blog post do? Step 1 is close to "Weak news".

## How to run it

```
Use the skill "Write a press release". Read the context pack.
Task: <what they want>.
```
