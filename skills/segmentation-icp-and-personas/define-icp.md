---
title: Define the ICP
type: skill
function: segmentation-icp-and-personas
owner: insights-analyst
reads: [icp-and-segments, product, company, goals-and-kpis]
you_bring: A customer export with one row per customer, lost deals with reasons, and notes on why customers succeeded or left.
also_for: [ideal customer, who to target, wrong leads, junk leads, bad fit customers, who to disqualify, target accounts, customers who churn]
version: 0.1.0
updated: 2026-11-02
summary: Defines fit criteria and disqualifiers from customer data.
judge: ["Do your best customers really look like this or is it who you wish you sold to?", "Does this describe companies that stay and grow or only companies that were easy to close?", "If you had to pick ten accounts today would this make the choice easy?", "Are there enough companies like this to reach your goals?"]
show_to: whoever talks to customers after the sale, and ask which of these companies they would not sign again
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this skill to define which companies buy, succeed and stay, and which to turn away, from your customer data. Do not use it to rank groups of companies against each other; use [Build a market segmentation](build-market-segmentation.md) instead. The ICP describes companies, so for the people inside them use [Write a persona](write-persona.md).

## Inputs

- [[context-pack:icp-and-segments]]: the current company type, size, region, situation, disqualifiers and triggers.
- [[context-pack:product]]: "What it is not" and known weak spots, which become disqualifiers.
- [[context-pack:company]]: internal churn and contract value, as a comparison for the customer data.
- [[context-pack:goals-and-kpis]]: the MQL definition, which depends on the ICP.

The marketer pastes into the chat:

- A customer export with one row per customer: industry, employees, sites, team size, region, contract value, days to close, start date, and whether the customer is active or churned.
- A list of lost deals with the reason, if available.
- Any notes on why a customer succeeded or left.

## Procedure

1. Read the inputs and count the customer rows. With 20 or more rows, mark criteria as "Data". With fewer than 20 rows or no export, proceed from the context pack and mark every criterion "Hypothesis". Say which applies on the first line of the output.
2. Sort the customers into two groups. "Good outcome" means active for at least 12 months with no known dispute over value. "Poor outcome" means churned, or active under 12 months with a known problem. Leave out customers too new to judge, and report how many you left out.
3. Compare the groups on each attribute: industry, size, team size, region, what they used before and any other column. Keep an attribute as a fit criterion only if at least 60% of the good-outcome group shares the value, and the share in the poor-outcome group is at least 20 points lower. These cutoffs, and the 20 rows and 12 months above, are starting rules the marketer can change, not benchmarks.
4. State each criterion as a test someone can apply from public information or one sales call, such as "at least 100 people to train". Reject criteria that require judgment, such as "innovative culture".
5. Write the disqualifiers from three sources: any item under "What it is not" in product.md that a buyer needs, any known weak spot that caused a churn or a loss, and any attribute shared by most of the poor-outcome group. Give the reason for each.
6. List the buying triggers from icp-and-segments.md, plus any trigger appearing in at least 3 customer notes.
7. Write the scoring rule. Tier A meets every criterion and has a trigger. Tier B meets every criterion with no trigger. Tier C misses exactly one criterion. Out misses two or more, or has any disqualifier.
8. Check the draft against the context pack: compare each criterion with icp-and-segments.md, flag every change, and say whether the MQL definition in goals-and-kpis.md still works. Where a needed field is blank, write a placeholder such as [region needed] and ask in the last section.
9. List everything you assumed, estimated, inferred or could not find in the last section, including any customers you excluded and why.

## Output format

```
Status: Draft
Evidence basis: <"Data" with row count and number excluded, or "Hypothesis", one line>

## ICP in one sentence
<company type, size, region and situation, up to 40 words>

## Fit criteria
| Criterion | Test | Evidence | Basis |
<3 to 6 rows; Basis is Data or Hypothesis; Evidence is a count from the export or a named context pack file>

## Disqualifiers
- <disqualifier and reason, up to 25 words each, 2 to 6 items>

## Buying triggers
- <trigger and source, up to 20 words each, 2 to 6 items>

## Scoring rule
| Tier | Test | What sales and marketing do |
<4 rows: A, B, C, Out>

## Changes to the context pack
- <file, field, current text, proposed text, up to 40 words each, or "None">

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the ICP describe companies, with no people or job titles in the criteria?
- [ ] Can each criterion be tested from public information or one sales call?
- [ ] Is each criterion marked Data or Hypothesis, with Data backed by a count?
- [ ] Does each disqualifier give a reason tied to the product or to poor outcomes?
- [ ] Does the scoring rule put every company in exactly one tier?
- [ ] Are all proposed changes to the context pack listed, and none made silently?
- [ ] Would turning away the Out tier be acceptable to sales, if you asked them today?

## Example (fictional company)

**Status:** Draft

**Evidence basis:** Hypothesis. No customer export pasted, so this works from the context pack.

**ICP in one sentence:** Knowledge-work companies of 300 to 5,000 employees in the United States, Canada and the United Kingdom that have rolled out general AI assistants and have someone responsible for learning and development.

**Fit criteria**

| Criterion | Test | Evidence | Basis |
|---|---|---|---|
| Company type | Consulting, accounting, law, software or financial services | icp-and-segments.md | Hypothesis |
| Size | 300 to 5,000 employees | icp-and-segments.md | Hypothesis |
| People to train | At least 100 | icp-and-segments.md, product.md | Hypothesis |
| Region | United States, Canada or United Kingdom | icp-and-segments.md | Hypothesis |
| AI rollout | General AI assistants already rolled out to staff | icp-and-segments.md | Hypothesis |

**Disqualifiers**

- Fewer than 100 learners: below the product's minimum.
- Wants a course library: CogniATion Coach is not one.
- Wants scores on individuals for performance reviews: the Coach is not for performance decisions, and reports stop at team level.
- Proposed: wants to screen job candidates, because the Coach is not for hiring decisions.

**Buying triggers:** company-wide AI assistant rollout, client complaint about poor reasoning, new head of learning, annual training budget planning.

**Scoring rule:** A meets all criteria with a trigger. B meets all, no trigger. C misses one. Out misses two, or has a disqualifier.

**Changes to the context pack:** Add the hiring disqualifier to icp-and-segments.md.

**Assumptions and open questions**

- Inference: the proposed disqualifier comes from "What it is not" in product.md.
- Unknown: can you paste the customer export, so criteria can move from Hypothesis to Data?
- Unknown: should companies needing training in other languages be Out, given the English-only product?

## How to run it

```
Use the skill "Define the ICP". Read the context pack.
Task: <why customers succeeded or left, if known>.
<paste the customer export and lost deals here>
```
