---
title: Propose quarterly goals
type: skill
function: budget-and-planning
owner: head-of-marketing
reads: [goals-and-kpis, company, channels-and-tools]
you_bring: Whatever numbers you have from last quarter, such as pipeline, leads, deals and a revenue goal, or none at all.
also_for: [no goals, no quarterly goal, ceo wants goals, set a target, how much pipeline to commit to, goal setting, talk to the ceo about goals, no numbers yet, get marketing set up]
version: 0.1.0
updated: 2026-11-02
summary: Turns whatever numbers you have into hold, grow and stretch goal options and a script for the CEO conversation, or into a learning goal if you have no numbers.
judge: ["If the CEO picks grow what stops being done to make room for it?", "Which lever in these options can marketing move alone and which one depends on sales?", "Is the step from hold to grow something you can explain or just a round number?", "Does any option connect to a revenue number the CEO already cares about?"]
show_to: your sales lead, before the CEO sees it, and ask which option they would put their own name on
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use. Here the CEO decides which goal to commit to.

## When to use

Use this when goals-and-kpis.md has no marketing goals, whether you have all of last quarter's numbers or none. Do not use it to plan the work once goals exist; use [Write a quarterly plan](write-quarterly-plan.md) instead. For the conversation itself, see [Three hard situations](../../guides/hard-situations.md#you-have-no-goals-yet).

## Inputs

- [[context-pack:goals-and-kpis]]: any goals, definitions and baselines already filled in.
- [[context-pack:company]]: who the CEO is, the size of the marketing and sales teams, and which numbers are internal only.
- [[context-pack:channels-and-tools]]: current channels, spend and limits.

The marketer pastes into the chat whatever exists. Blanks are fine.

- Last quarter's pipeline, leads, MQLs, SQLs and deals won.
- Any revenue goal someone has stated, and who stated it.
- Budget and days available next quarter, if known.

## Procedure

1. Collect the numbers from goals-and-kpis.md and the paste. Never fill a blank with an outside rate, a benchmark or a guess. If marketing goals are already filled in, ask whether to replace them.
2. Choose the route. With any number for last quarter, take the options route, steps 3 to 7. With no numbers at all, go to step 8.
3. Build the chain from what exists: MQLs x MQL to SQL rate = SQLs, then SQLs x value per SQL = pipeline, then SQLs x SQL to won rate = deals. Work out each rate from the marketer's numbers and label it an estimate. Write [number needed] for a missing link, and build only on what holds.
4. Write three options. Hold repeats last quarter. Grow moves one lever. Stretch moves that lever and a second one. Size a move from the marketer's best past quarter, or else use 15% (a starting rule, to show the arithmetic, not a forecast).
5. For each option, show:
   - The arithmetic, line by line.
   - What it would take: extra volume per week, the channel it comes from, and the money and days, or [budget needed] and [days needed].
   - What would have to be true: up to 3 conditions a named person could confirm.
6. If there is a revenue goal, work backward using only the marketer's rates: revenue goal divided by deal value is deals, divided by SQL to won rate is SQLs, divided by MQL to SQL rate is MQLs. Say which option it matches, or how far above stretch it sits, which the CEO needs to hear first.
7. Write the CEO script: a two-sentence opening, 3 to 5 questions, and the decision to request: which option, by what date, and what gets dropped. Do not choose for the CEO. Once decided, the marketer copies the goal into goals-and-kpis.md and runs the quarterly plan.
8. With no numbers, write no targets. Instead write:
   - Up to 8 questions to get the numbers, each with who to ask and where the answer lives.
   - A first-quarter learning goal: by a date, know the baselines for leads, qualified opportunities and pipeline, using definitions sales agrees. It holds no target number.
   - A short CEO script asking for that goal and saying when real options will follow.
9. Check the draft against the context pack: numbers match, internal-only numbers are marked, and a blank definition reads [definition needed].
10. List everything assumed, estimated, inferred or unknown in the last section.

## Output format

```
Status: Draft
Decision owner: <the CEO's name>. These are options, not goals, until the CEO picks one.
Route: <Options, or Learning goal>

## Numbers used
<each number and its source, or [number needed]>

## Options
| Option | Goal as worded | Arithmetic | What it would take | What would have to be true |
<Hold, Grow and Stretch, or "Not enough numbers yet">
Revenue goal check: <what it requires and which option it matches, or "None stated">

## If you have no numbers
| Question | Who to ask | Where it lives |
<up to 8 rows, or "Not needed">
Learning goal: <what you will know by when, with no target number, or "Not needed">

## CEO conversation
Opening: <two sentences>
Questions:
- <3 to 5 questions>
Decision to request: <one sentence, with a date>
Next step: <once the CEO decides>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every number trace to goals-and-kpis.md or the paste, with nothing from outside?
- [ ] Do the three options differ by named levers, with each move labeled?
- [ ] Is the script asking the CEO to decide, with no option chosen for them?
- [ ] With no numbers, is the output free of any target number?
- [ ] Are derived numbers labeled estimates, and internal-only numbers marked?

## Example (fictional company)

**Status:** Draft

**Decision owner:** Marta Ilves, CEO. These are options, not goals, until she picks one.

**Route:** Options

Assumption: this example treats goals-and-kpis.md as blank, with only the Q3 2026 baselines known.

**Numbers used:** 260 MQLs, 26% MQL to SQL, 24% SQL to won, $900,000 pipeline, all Q3 2026. Estimate: 260 x 26% = about 68 SQLs, and $900,000 / 68 = about $13,200 per SQL.

**Options**

| Option | Goal | Arithmetic | What it would take | What would have to be true |
|---|---|---|---|---|
| Hold | $900,000 pipeline | 68 x $13,200 | Same channels and spend | Q3 was not a one-off |
| Grow | About $1.03 million | 300 x 26% = 78 SQLs x $13,200 | 3 more MQLs a week, from a named channel | One sales development representative can work 23 MQLs a week |
| Stretch | About $1.19 million | 300 x 30% = 90 SQLs x $13,200 | Grow, plus fewer rejected leads | Tom Ferrant agrees the rejections can be fixed this quarter |

**CEO conversation**

Opening: "Here are three options from our Q3 numbers. They are arithmetic, not forecasts, and I need you to choose one."

Questions:

- What revenue does the company need next year, and how much of it should marketing source?
- Would you rather beat hold or miss stretch?
- What would you drop to make room for grow?

Decision to request: which option we commit to, by the end of this week.

Next step: copy the choice into goals-and-kpis.md, then plan.

**Assumptions and open questions**

- Assumption: 300 MQLs and 30% are Q3 plus the 15% starting rule, rounded, and are illustrative.
- Estimate: at 24%, about 16, 19 and 22 deals.
- Unknown: what would grow cost?

## How to run it

```
Use the skill "Propose quarterly goals". Read the context pack.
Task: <next quarter, and who decides>.
<paste whatever numbers you have, or say you have none>
```
