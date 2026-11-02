---
title: Write a competitor profile
type: skill
function: competitive-intelligence
owner: product-marketing-manager
reads: [competitors, product, icp-and-segments, proof-points, channels-and-tools]
you_bring: The competitor's name, today's date, and pasted source text with where it came from and the date checked.
also_for: [competitor research, competitor analysis, what does the rival do, rival pricing, new competitor, update competitor file, rival product changes]
version: 0.1.0
updated: 2026-11-01
summary: Creates or updates a sourced profile of one competitor from what the marketer pastes.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this to create a profile of one competitor, or to update one at the monthly refresh, from sources you paste. Do not use it for a sales sheet; use [Write a battlecard](../product-marketing-and-sales-enablement/write-battlecard.md) instead. For patterns across many deals, use [Analyze wins and losses](analyze-win-loss.md).

## Inputs

- [[context-pack:competitors]] – the current entry and its dated facts
- [[context-pack:product]] – features, what it is not, known weak spots
- [[context-pack:icp-and-segments]] – the target, to judge where the competitor matters
- [[context-pack:proof-points]] – proof for the answer, with permission status
- [[context-pack:channels-and-tools]] – hard rules on naming competitors

The marketer supplies: the competitor's name, today's date, and pasted source text such as pricing page copy, help center pages, product pages, review site excerpts or call notes. Each paste needs its source and the date it was checked. Work only from what is pasted.

## Procedure

1. Find the competitor in competitors.md. If it is there, the mode is Update. If not, the mode is New. If nothing is pasted and competitors.md has no entry, ask for sources and stop.
2. Give each pasted item an ID (E1, E2) and sort it by source type: Own for the competitor's published pages, Buyer for call notes and lost-deal notes, Third party for review sites, articles and anything else.
3. Use nothing from memory, even if you recognize the name. An item with no source or no date goes under "Unverified" and into the unknowns.
4. Write each fact in one sentence that shows where it came from: "lists", "per its help center", "three prospects reported". Write an absence as "not found in [source]", never as "does not have". Report a buyer's statement as a report, with the count of buyers.
5. Mark each fact in Update mode: New, Confirmed by a new source, Changed, Contradicted, or Unchanged if no new source touches it. Never overwrite silently. A newer Own source replaces an older Own source. A Buyer or Third party item does not replace an Own source: keep both, with dates, and mark them Contradicted.
6. Mark any fact checked more than 6 months before today's date as Stale. Six months is a starting rule the marketer can change. If the marketer gave no date, skip Stale marks and ask in the last section.
7. Write "Where they win" and "Where they lose", at most 3 lines each, with the IDs or the existing entry behind each line. A line with one source is an inference, and gets that label. Keep existing lines with no new evidence as they are.
8. Fill in the side-by-side table, 6 rows at most, using capabilities buyers in the ICP ask about. "Us" comes only from product.md, including "Known weak spots" and "What it is not". Set "Stronger" to Them, Us or Cannot tell. Use Cannot tell when the two sides measure different things. Show every row where they are stronger.
9. Write "Our answer": one sentence on when the competitor is a fair choice, one factual sentence on the difference, and one question the buyer can ask them. Use proof only if its status fits one-to-one sales use. No criticism beyond the known facts.
10. Write "Use limits": the profile is internal by default. Copy any hard rule on competitor names from channels-and-tools.md, and name the approver for sales material.
11. Check the draft against the context pack: every fact has a source and date, "Us" matches product.md, no Pending or None proof appears, and no roadmap item is used. Fix what fails.
12. List what to check next, by source, and list everything you assumed, inferred or could not find in the last section.

## Output format

Field names through "Our answer" match competitors.md, so the marketer can paste them in by hand.

```
Status: Draft
Mode: <New or Update>

## Name and category
<Name: how buyers see them, 12 words at most>

## Where they win
- <3 lines at most, 20 words each, with evidence IDs>

## Where they lose
- <3 lines at most, 20 words each, with evidence IDs>

## Known facts, with source and date
- <Fact> (<source>, checked <date>) <New, Confirmed, Changed, Contradicted, Unchanged or Stale>
(10 items at most)

## Our answer
<3 sentences at most>

## Unverified
- <Item, and what source would settle it; write None if empty>

## Side by side
| Capability | Them | Us | Stronger |
(6 rows at most, cells 12 words at most)

## Use limits
<30 words at most>

## Check next
- <Source to check, and why; 3 items at most>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every known fact have a source and a checked date?
- [ ] Is anything from memory, with no pasted source?
- [ ] Are absences written as "not found", not as facts?
- [ ] Are buyer reports labeled as reports, with a count?
- [ ] Does the table show where the competitor is stronger?
- [ ] Do "Us" cells match the product file, weak spots included?
- [ ] Were changes marked, with no fact silently overwritten?
- [ ] Is the use limit stated?

## Example (fictional company)

Status: Draft

Mode: Update

**Name and category**

Elenchly: established course library on critical thinking and decision making.

**Where they win**

- Large companies wanting one library through their learning management system (existing entry).

**Where they lose**

- Buyers who want to see behavior change, not course completions (existing entry).

**Known facts, with source and date**

- Three prospects described its reports as completion data and quiz scores (calls, 2026). Unchanged.
- More than 200 video courses listed on its product pages (checked October 2026). Unchanged.

**Our answer**

A fair choice if you want a library. CogniATion Coach is practice that reports progress by team. Ask how the last course changed the work.

**Unverified**

None.

**Side by side**

| Capability | Them | Us | Stronger |
|---|---|---|---|
| Course library | More than 200 video courses, per product pages | Not a course library | Them |
| Reports for learning leaders | Completion data and quiz scores, reported by three prospects | Team-level progress on six thinking skills | Cannot tell, different measures |

**Use limits**

Internal. No competitor names in ads. Tom Ferrant approves sales material.

**Check next**

- Its product pages, for changes to its reports.

**Assumptions and open questions**

- Assumption: no new source pasted, so all facts come from competitors.md.
- Unknown: Do Elenchly's reports show how people work after a course?

## How to run it

```
Use the skill "Write a competitor profile". Read the context pack.
Task: <the competitor's name and today's date>.
<paste each source here, with its origin and date checked>
```
