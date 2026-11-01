---
title: Synthesize customer research
type: skill
function: segmentation-icp-and-personas
owner: insights-analyst
reads: [personas, icp-and-segments, messaging, proof-points]
version: 0.1.0
updated: 2026-11-01
summary: Turns interview notes, survey exports and call notes into findings with evidence.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this skill to turn interview notes, survey exports or call notes into findings, each backed by evidence you can check. Do not use it for patterns across won and lost deals from a CRM export; use [Analyze wins and losses](../competitive-intelligence/analyze-win-loss.md) instead. To turn the findings into a buyer description, run [Write a persona](write-persona.md) next.

## Inputs

- [[context-pack:personas]]: current objections and daily problems, to test against the findings.
- [[context-pack:icp-and-segments]]: segments and triggers, to tag each source and compare.
- [[context-pack:messaging]]: pillars and words to use, to see which ones the research supports.
- [[context-pack:proof-points]]: permission statuses, to flag quotes that are not approved for use.

The marketer pastes into the chat:

- The research itself: interview notes, transcripts, survey results or call notes.
- For each source, if known: date, company type, role and how the person was chosen.
- The question the research was meant to answer, if there was one.

## Procedure

1. If no research text was pasted, ask for it and stop. Do not write findings from the context pack alone.
2. Number each source S1, S2 and so on, one per interview, call or survey. Record its type, date, role and segment. Write "unknown" for anything missing.
3. Pull excerpts word for word. Keep every quote exactly as written, and never tidy or combine quotes. Mark notes taken by an interviewer as "notes", not as the person's own words.
4. Tag each excerpt with one theme type: trigger, problem, objection, alternative considered, outcome or language.
5. Group excerpts into findings. Each finding is one plain claim about what buyers do, want or fear, in a full sentence. Do not write findings about what the company should do.
6. Count the sources behind each finding, not the mentions. Rate it Strong with 3 or more sources, Moderate with 2, Weak with 1. For surveys, give the question wording and the number of responses, and report counts rather than percentages under 30 responses. These counts are starting rules the marketer can change.
7. Report contradictions and silences: where sources disagree, show both sides, and note which segments or roles are missing from the sample. Say if the sample was chosen in a way that skews it, such as only current customers.
8. Rank findings by strength, then by how directly they answer the research question. Keep at most 7. Move the rest to the excerpt list.
9. Write one implication for each Strong or Moderate finding, naming the next skill to run. For a Weak finding, the only allowed implication is what to ask next.
10. Check the draft against the context pack: for each finding, say whether personas.md, icp-and-segments.md or messaging.md confirms it, contradicts it or is silent. Propose changes, but do not make them.
11. Mark quotes for use. A quote is internal only unless proof-points.md shows it with a permission status that allows the use. To use one publicly, the marketer must get approval first.
12. List everything you assumed, inferred or could not determine in the last section, including gaps in the sample.

## Output format

```
Status: Draft
Sources: <number and type of sources, date range, one line>
Sample gaps: <roles, segments or outcomes missing, up to 30 words>

## Findings
| ID | Finding | Strength | Sources | Context pack |
<up to 7 rows; finding up to 25 words; Sources lists IDs; Context pack is confirms, contradicts or silent, with the file name>

## Evidence
For each finding:
F<number>
- S<number>: "<quote, up to 30 words>" or notes: <paraphrase, up to 30 words>
<up to 3 excerpts per finding>

## Contradictions
- <what disagrees and which sources, up to 30 words each, or "None">

## Implications
- F<number>: <what follows and which skill to run next, up to 30 words>

## Proposed changes to the context pack
- <file, field, proposed text and the finding behind it, up to 40 words each, or "None">

## Quote permissions
- <quote reference and status from proof-points.md, or "internal only, no permission on file">

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every finding list the sources behind it, counted by source and not by mention?
- [ ] Is every quote word for word, with notes marked as notes?
- [ ] Are Weak findings limited to what to ask next?
- [ ] Are contradictions and sample gaps stated rather than smoothed over?
- [ ] Does each finding say what the context pack does with it?
- [ ] Is every quote marked with its permission status before anyone uses it?
- [ ] Are findings about buyers, with recommendations kept in the implications?

## Example (fictional company)

**Status:** Draft

**Sources:** 5 sources: four persona entries (S1 to S4) and one approved customer quote (S5), standing in for pasted notes.

**Sample gaps:** no lost deals or churned customers, and no software or financial services sources.

**Findings**

| ID | Finding | Strength | Sources | Context pack |
|---|---|---|---|---|
| F1 | Leaders doubt the reasoning behind confident junior work. | Strong | S2, S3, S4 | Confirms icp-and-segments.md, situation |
| F2 | Buyers doubt staff will use another tool, especially one withholding answers. | Moderate | S1, S4 | Confirms messaging.md, pillar 2 |
| F3 | People leaders fear staff will feel watched. | Weak | S2 | Confirms messaging.md, VP message |

**Evidence**

F1

- S2: "The partners keep telling me juniors can't think without the chatbot."
- S3: "I read work that sounds confident and hasn't been thought through."
- S4: "I get the draft back with 'why?' written on it, and I don't know how to answer."

F2

- S1: "People won't make time for another training tool."
- S4: "Why would I use a bot that won't give me the answer?"

**Contradictions:** S4 doubts a bot that withholds answers, while S5 says analysts "started defending their own."

**Implications**

- F1: lead the professional services campaign with pillar 3, using [Write a campaign brief](../campaign-design/write-campaign-brief.md).
- F2: test it in the head of learning entry, using [Write a persona](write-persona.md).
- F3: ask VPs of people what would make staff feel watched.

**Proposed changes to the context pack:** None.

**Quote permissions:** S1 to S4: internal only, no permission on file. S5: public, approved June 2026.

**Assumptions and open questions**

- Assumption: no research batch exists for CogniATion, so personas.md and proof-points.md stand in.
- Unknown: can you paste real interview notes?

## How to run it

```
Use the skill "Synthesize customer research". Read the context pack.
Task: turn the interview notes pasted below into findings with evidence.
```
