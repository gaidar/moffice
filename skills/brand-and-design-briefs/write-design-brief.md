---
title: Write a design brief
type: skill
function: brand-and-design-briefs
owner: brand-and-creative-director
reads: [company, product, personas, messaging, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Produces a brief with final copy, specifications and dates that a designer can execute without a meeting.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this when you need a designer to make something specific: a booth panel, an ad set, a set of social images. Do not use it when the words are still undecided; write them first with the matching skill, such as [Write a web page](../content/write-web-page.md). If the campaign itself is not defined, use [Write a campaign brief](../campaign-design/write-campaign-brief.md) instead.

## Inputs

- [[context-pack:brand-voice]]: visual basics, voice and style details.
- [[context-pack:messaging]]: the main message and words to avoid.
- [[context-pack:proof-points]]: which customer names, logos, numbers and quotes may appear in public.
- [[context-pack:product]]: what the product does and is not, for the images.
- [[context-pack:personas]]: who will see the piece.
- [[context-pack:company]]: the designer's available time and the company's public name.
- [[context-pack:goals-and-kpis]]: campaign and event dates this quarter.
- [[context-pack:channels-and-tools]]: the approver and typical time.

The marketer supplies in the prompt: what is needed, where it will appear, the exact sizes and file formats, the due date, the copy if it already exists, and any files on hand.

## Procedure

1. State the job in one sentence: what the piece must get one named audience to notice or do. If the prompt asks for several unrelated jobs, write one brief for the first and list the others as open questions.
2. List each piece with its size, file format, quantity and where it will appear. Take sizes and formats only from the prompt. Otherwise leave [size needed] or [format needed].
3. Write the copy word for word, with its order on the piece. Mark each line "final" or "[copy needed]". The designer must never have to write or edit a line.
4. Choose the one thing the reader should see first, then rank everything else behind it, with no more than three levels. Cut anything that will not fit the piece, and say what you cut.
5. Add proof only from proof-points.md marked public, with its date or sample, and copy any quote word for word. Permission for a name or a logo does not cover photos of that customer's staff or offices. Ask for that separately, and leave [photo permission needed].
6. Copy the visual rules from brand-voice.md as written. If they are blank, leave [visual rules needed] and ask in the last section. Do not suggest named typefaces or color codes that the file does not give.
7. Write the "do not show" list: everything brand-voice.md rules out, anything the product does not do according to product.md, and any competitor name.
8. List the files the designer will receive and what is still missing, with who owes it and by when.
9. Set dates working back from the due date: first version, marketer's comments, final files. Allow for the approver's time from channels-and-tools.md. Allow two rounds of changes, a starting rule the marketer can change. If the dates do not fit, say which piece to cut.
10. Compare the work with the designer's time in company.md. Use the designer's own estimate if the marketer supplies it, otherwise leave [designer's estimate needed].
11. If any other needed context pack field is blank, leave a visible placeholder in square brackets and ask in the last section. Never invent.
12. Check the draft against the context pack: every name, number, quote and image rule against its source, and all the copy against words to avoid.
13. List everything you assumed, and everything a designer would still have to ask, in the last section.

## Output format

```
Status: Draft
Job: <one sentence, 25 words maximum>
Audience: <who sees it, where, in what setting, one line>
Sees first: <the one thing, one line>

## Pieces
| Piece | Size | File format | Quantity | Where it appears |
<One row per piece, or placeholders>

## Copy, word for word
<Piece name>
1. <Line, marked final or [copy needed]>
<Lines in reading order, three levels of importance at most>

## Visual rules
- <Copied from brand-voice.md>

## Do not show
- <Up to 6 items>

## Files provided and files missing
- <File, who has it, or who owes it and by when>

## Dates
| Step | Date | Who |
| First version | <date> | Designer |
| Comments | <date> | Marketer |
| Final files | <date> | Designer |
| Approval | <date, allowing for typical time> | <approver> |
Rounds of changes: <number>
Designer's time: <estimate or [designer's estimate needed], against available time>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Could the designer start without asking a single question?
- [ ] Is every line of copy word for word, or a visible placeholder?
- [ ] Does each piece have a size, file format and quantity, or a visible placeholder?
- [ ] Is it clear what the reader should see first?
- [ ] Is every customer name, number and quote public in proof-points.md, with its date or sample?
- [ ] Do the visual rules match brand-voice.md exactly?
- [ ] Do the dates allow for the approver's time and the designer's available days?

## Example (fictional company)

Status: Draft

Job: get heads of learning to stop and talk about showing that training worked.

Audience: learning leaders at the regional learning and development conference, March 9 to 11, 2027.

Sees first: the headline.

**Pieces**

| Piece | Size | File format | Quantity | Where it appears |
|---|---|---|---|---|
| Booth back panel | [size needed] | [format needed] | 1 | Booth |

**Copy, word for word**

Booth back panel

1. Your analysts have answers. Can they defend them? Final.
2. CogniATion Coach is an AI chatbot that won't give you the answer, so you learn to find it. Final.
3. "My analysts stopped asking the bot for the answer and started defending their own." Lena Marsh, head of learning, Brightmere Advisory. Final.

**Visual rules**

- Primary deep blue, secondary warm gray, one sans-serif typeface.
- Logo on plain backgrounds only, never on photos.
- No images of glowing brains or robots.

**Do not show**

- Any learner's conversation or score, even mocked up.
- The Coach writing a memo or giving the answer.
- Any competitor name.

**Files provided and files missing**

- Photos of Brightmere staff: [photo permission needed].

**Dates**

| Step | Date | Who |
|---|---|---|
| First version | [date needed] | Designer |
| Final files | [organizer's deadline needed] | Designer |
| Approval | [date needed] | The marketer, same day |

Designer's time: [designer's estimate needed], against about four days a month.

**Assumptions and open questions**

- Assumption: CogniATion has a booth, because goals-and-kpis.md lists only the dates.
- Unknown: what is the organizer's file deadline?

## How to run it

```
Use the skill "Write a design brief". Read the context pack.
Task: <what they want>.
```
