---
title: Update the context pack
type: skill
function: marketing-ops
owner: marketing-operations-manager
reads: [company, product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
you_bring: Your notes, such as a sales call, a customer email or a price change, with the date and who said it.
also_for: [update my context pack, a fact changed, new proof point, new objection, add this to the pack, record this, keep the pack current, customer said yes, price changed]
version: 0.1.0
updated: 2026-11-02
summary: Turns pasted notes into the exact changes to make in your context pack, showing only what changes and never marking anything approved on its own.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when a note, call or email changes a fact your skills rely on. Do not use it to fill a blank pack from scratch; use [Fill the context pack](../../guides/fill-the-context-pack.md) instead. To find what has gone stale without new notes, run the monthly check in [Maintain and update](../../guides/maintain-and-update.md).

## Inputs

- [[context-pack:company]]: company facts, and which numbers may be used where.
- [[context-pack:product]]: what it does and is not, prices, roadmap limits.
- [[context-pack:icp-and-segments]]: segments, fit and disqualifiers.
- [[context-pack:personas]]: buyers, their problems and objections.
- [[context-pack:messaging]]: claims, pillars and words to avoid.
- [[context-pack:competitors]]: competitor facts, with sources and dates.
- [[context-pack:proof-points]]: customers, numbers and quotes, with permission status.
- [[context-pack:brand-voice]]: voice rules.
- [[context-pack:goals-and-kpis]]: goals, baselines and definitions.
- [[context-pack:channels-and-tools]]: channels, tools, limits and approvers.

The marketer pastes into the chat:

- The notes, with the date and who said each thing.
- Any permission a customer or the CEO has given, in their words if possible.

## Procedure

1. Read the notes and list each separate fact they state. If a note has no date or no source, write [date needed] or [source needed] for it and ask in the last section.
2. Sort each fact. A company fact goes on in step 3. A task, deadline or decision goes under "Not added", with the workboard named as its place. An opinion from one person stays an opinion: record it with its source, or mark it "(founder belief)" if a founder said it about buyers, the market, competitors or results.
3. Find the section and field each fact belongs in, using the templates' field names. If no field fits, put it under "Not added" and say why.
4. Compare the fact with the current answer in that field. Mark it new, changed or the same. Drop anything that is the same.
5. A newer fact from the person who owns it, such as a price from whoever approves pricing, is a change. Name that person as the source. For any other contradiction, do not choose. Put both under "Conflicts to settle", with a question and your recommendation.
6. Set permission only from what the notes say. A customer's written yes, with its date, can move an item to the status they agreed to. A verbal yes is "pending" until it is in writing. No word on permission means "none". Being pleased, being quoted in sales notes, or appearing in an export is not permission.
7. Do not change a goal, target, MQL or SQL definition, or budget. Put each one under "Conflicts to settle" as a decision for the marketer, since these belong to the marketer and whoever approves them.
8. Write each change as it should read in the file: section, field name, and the full new "Answer:" line, with its source and date. Keep the rest of the answer word for word. Do not reword what you are not changing.
9. Do not return the whole context pack. A retyped pack can change facts without anyone noticing, so return only the changed fields.
10. Name which skills read each changed section, up to 3, so the marketer knows what to run again.
11. Check every change against the context pack once more: no new claim beyond the notes, no permission raised without a source, no field name altered.
12. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
Status: Draft
Notes from: <dates and sources, up to 20 words>

## Changes to make
| Section | Field | Now | Change to | Source and date | New or changed |
<one row per field. "Now" up to 15 words; write "Blank" if empty>

## Paste these lines
<For each change: the section name, the field name and the full new "Answer:" line, in a code block.>
Paste these into my-context-pack.md, save it, upload the new file and delete the old copy. This chat changes no file.

## Conflicts to settle
| Field | The pack says | The notes say | Question and recommendation |
<one row per conflict or reserved decision, or "None". Question and recommendation up to 25 words.>

## Not added
- <item, reason, and where it belongs instead, up to 20 words each, or "None">

## Skills to run again
- <changed section: up to 3 skill titles, or "None">

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every change name its source and date?
- [ ] Were only changed fields returned, with no retyped pack?
- [ ] Is every permission status backed by what the notes say?
- [ ] Are contradictions and reserved decisions left for the marketer?
- [ ] Is one person's opinion recorded as an opinion, not a fact?
- [ ] Do the field names match the templates exactly?

## Example (fictional company)

Status: Draft

Notes from: Tom Ferrant, January 29, 2027; Haldane Ridge Capital email, February 2, 2027.

Assumption: the notes below are invented for this example. Tom Ferrant said a managing partner asked about individual scores. He also thinks the price is too high. Haldane Ridge Capital's head of learning wrote that the firm's name may be used in sales material.

**Changes to make**

| Section | Field | Now | Change to | Source and date | New or changed |
|---|---|---|---|---|---|
| personas.md | Persona 3, objections | "Why not just tell people to check the AI's work?" | Add "Can I see how each associate scored?" | Tom Ferrant, January 29, 2027 | New |
| proof-points.md | Customer 3, permission | Pending, requested October 2026 | Sales only | Haldane Ridge Capital email, February 2, 2027 | Changed |

**Paste these lines**

```
personas.md, Persona 3, Objections
Answer: "Why not just tell people to check the AI's work?"; "Can I see how each associate scored?" (Tom Ferrant, first call, January 29, 2027)
```

**Conflicts to settle:** None.

**Not added**

- Price is too high: one opinion. Keep the note, and watch for it in win-loss.

**Skills to run again:** personas.md: Write a web page.

**Assumptions and open questions**

- Unknown: does Haldane Ridge Capital's yes cover a quote or a result as well as the name?

## How to run it

```
Use the skill "Update the context pack". Read the context pack.
Task: update it from these notes.
<paste your notes here, with the date and who said each thing>
```
