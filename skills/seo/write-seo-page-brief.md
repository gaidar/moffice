---
title: Write an SEO page brief
type: skill
function: seo
owner: seo-specialist
reads: [product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Produces a brief for one page targeting one topic, ready to hand to the content lead.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this when you have chosen one topic and one page and need a brief the content lead can write from. Do not use it to choose topics; use [Build a keyword map](build-keyword-map.md) instead. To write the page itself, use [Write a web page](../content/write-web-page.md) or [Write a blog post](../content/write-blog-post.md).

## Inputs

- [[context-pack:product]]: features and limits.
- [[context-pack:icp-and-segments]]: the segment, its buying reason and its triggers.
- [[context-pack:personas]]: the reader's daily problem and objections.
- [[context-pack:messaging]]: pillars, words to use and avoid.
- [[context-pack:competitors]]: dated facts, if the page compares.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:brand-voice]]: rules for title and description.
- [[context-pack:goals-and-kpis]]: the conversion that counts, current campaigns.
- [[context-pack:channels-and-tools]]: who approves what.

The marketer supplies the topic and primary keyword. The skill works only from what is pasted, so the marketer also pastes the titles and headings of the top results, the volume, and any URLs available for internal links. Without them, those fields say unknown.

## Procedure

1. Confirm the scope is one topic and one page. If the request holds two intents, brief the one closer to buying and name the other under the last section.
2. Set the intent: Buy, Compare, Solve or Learn. If search results are pasted, use the intent most of them serve. If not, infer it from the keyword's wording and label it as an inference.
3. Set the page type by intent: Buy gets a product or solution page, Compare a comparison page, Solve a guide or blog post, Learn a blog post.
4. Choose one reader: the persona whose daily problem the keyword addresses. If two fit, take the one closer to the buying decision for that segment. If personas.md is blank, ask before drafting.
5. Write the angle in one sentence: what this page says that the pasted results do not, tied to one pillar. With no results pasted, base it on the pillar and mark the gap as unknown.
6. Write the title tag (60 characters at most), meta description (155 at most), H1 and slug. The primary keyword goes in the title, H1 and slug. Follow brand-voice.md.
7. Write the outline: 4 to 8 H2 headings. The first answers the search query directly. For each, state the question it must answer, the keyword it carries if any, and the proof it uses.
8. Choose proof from proof-points.md. A public page uses only items marked public. Leave out sales only, internal only, pending and none, and do not name those customers in the brief. Use a claim from messaging.md that names a customer only if proof-points.md shows permission for that claim. If a section has no usable proof, write [proof needed].
9. Write the do-not-say list: limits from product.md, the words to avoid, and any roadmap item. A Compare page names a competitor only with a dated fact from competitors.md. Any pricing mention goes to the approver in channels-and-tools.md.
10. Choose the page's one action. Buy and Compare pages ask for a demo or the pilot in product.md. Solve and Learn pages offer the next page to read, plus a smaller demo link. Add 3 to 5 internal links from the pasted URLs only, or write [internal link needed: topic].
11. Set the length from the median of the pasted results, or write [length needed]. Name the handoff: the content lead, the skill to run and the approver.
12. Check the draft against the context pack: every feature, number, name and word. Fix anything that contradicts it.
13. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
Status: Draft

## SEO page brief: <topic>

Primary keyword: <keyword>, volume <n and source, or unknown>
Secondary keywords: <up to 6>
Intent: <Buy, Compare, Solve or Learn>
Page type: <type>. Action: <New or Update, with URL>
Reader: <persona, segment>
Angle: <one sentence, 30 words at most>
Pillar: <one pillar from messaging.md>
Page action: <one action>

## Search details
Title tag: <60 characters at most>
Meta description: <155 characters at most>
H1: <70 characters at most>
Slug: <proposed>
Length: <range and basis, or [length needed]>

## Outline
| H2 | Must answer | Keyword | Proof, with permission status |
<4 to 8 rows>

## Do not say
- <up to 6 items>

## Internal links
- <URL or [internal link needed: topic]>

## Competing pages
- <what the pasted results cover and miss, up to 5 lines, or unknown>

## Handoff
To: content lead. Skill: <skill title>. Approver: <from channels-and-tools.md>

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does the brief cover one topic, one reader and one page action?
- [ ] Are the title tag and meta description inside their limits?
- [ ] Is every proof item marked public in proof-points.md for a public page?
- [ ] Does the page promise only what product.md says the product does?
- [ ] Could the content lead write the page from this brief without asking you anything?

## Example (fictional company)

**Status:** Draft

**SEO page brief: measuring critical thinking training**

Primary keyword: measure critical thinking training, volume unknown
Intent: Solve. Page type: guide. Action: New
Reader: head of learning and development, professional services
Angle: Completion data shows who finished, while rubric scores on real work scenarios show whether reasoning changed.
Pillar: You can see reasoning improve
Page action: Read the next page, plus a demo link

**Search details**

Title tag: How to measure critical thinking training | CogniATion
Meta description: Course completions show who finished. Learn how to score reasoning on real work scenarios and show your leadership team what changed.
H1: How to measure critical thinking training
Slug: /measure-critical-thinking-training
Length: [length needed]

**Outline**

| H2 | Must answer | Keyword | Proof, with permission status |
|---|---|---|---|
| Measure reasoning, not completions | How do I measure this training? | measure critical thinking training | Five-point rubric on six thinking skills, product.md |
| What a measured result looks like | Has anyone shown a change? | None | Brightmere Advisory analysts, 22% on client memo reasoning, 2026, public |
| How to report without watching individuals | Will people feel watched? | None | Team-level reports, product.md |
| How to keep people practicing | Will people make time? | None | 72% of assigned learners, a session each week, Q3 2026, public |

**Do not say**

Roadmap items, reports below team level, claims about intelligence or hiring, any word to avoid.

**Handoff**

To: content lead. Skill: Write a blog post. Approver: the marketer.

**Assumptions and open questions**

- Assumption: the guide format and topic.
- Inference: the intent is Solve, from the keyword's wording.
- Unknown: no search results pasted. What do the top results cover?

## How to run it

```
Use the skill "Write an SEO page brief". Read the context pack.
Task: write a brief for one page on <topic>, using the keyword and search results pasted below.
```
