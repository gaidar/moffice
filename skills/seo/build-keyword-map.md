---
title: Build a keyword map
type: skill
function: seo
owner: seo-specialist
reads: [product, icp-and-segments, personas, messaging, competitors, channels-and-tools]
you_bring: A keyword export with volume, its source and date, and a list of your existing pages.
also_for: [keyword research, seo plan, seo topics, which keywords, website content plan, organic traffic, what pages do we need, content gaps]
version: 0.1.0
updated: 2026-11-01
summary: Clusters keywords from a pasted export, sets intent and priority, and maps each cluster to one page.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when you have a keyword export and need to decide which page targets which cluster. Do not use it for one page you have already chosen; use [Write an SEO page brief](write-seo-page-brief.md) instead. To fix pages from performance data, use [Audit SEO from exports](audit-seo-from-exports.md).

## Inputs

- [[context-pack:product]]: what the product does and is not.
- [[context-pack:icp-and-segments]]: segments, priority order and disqualifiers.
- [[context-pack:personas]]: who has which problem, and their words.
- [[context-pack:messaging]]: pillars and words to avoid.
- [[context-pack:competitors]]: competitor names and dated facts, for comparison pages.
- [[context-pack:channels-and-tools]]: how often the marketer publishes.

The marketer pastes a keyword export (keyword, monthly volume, difficulty if available, plus the export's source and date) and a list of existing pages (URL and title).

## Procedure

1. Stop and ask if no keyword list is pasted. Never supply volumes, difficulty or rankings yourself. If the list has no volume column, write "unknown" in the Volume field and continue. If the page list is missing, write [page check needed] in the Action field and ask in the last section.
2. Clean the list. Merge duplicates and close variants under the highest-volume variant. Count rows in and rows kept.
3. Exclude. Move a keyword to the excluded table, with its reason, if it names something product.md says the product is not, matches a disqualifier, targets a region outside the ICP, or is about jobs, salaries or free downloads with no link to buying. High volume does not save it.
4. Set one intent per keyword:
   - Buy: software, pricing, vendor, demo, "best" plus the category.
   - Compare: "vs", "alternative", a competitor's name.
   - Solve: how to, checklist, template, exercise.
   - Learn: what is, meaning, definition.
   If the wording fits two, take the one closer to buying.
5. Cluster. Two keywords go together only if they share an intent and one page could fully answer both. Name the cluster after its highest-volume keyword.
6. Assign a segment and a persona. Use the segment whose name or buying reason matches the keyword. If two match, take the one higher in the priority order. If none matches, write "All". Use the persona whose job or daily problem matches, or the first listed on a tie (a starting rule). If segments or the priority order are blank, write [segment priority needed] and ask in the last section.
7. Assign one page and one action per cluster:
   - Update: an existing page has the same topic and intent.
   - Consolidate: two or more existing pages cover the cluster. Name the one to keep.
   - New: no page exists. Page type follows intent: Buy gets a product or solution page, Compare a comparison page, Solve a guide or blog post, Learn a blog post.
   - Hold: a Compare cluster names a competitor and competitors.md has no dated fact about it.
8. Set the tier. Tier 1: Buy or Compare in the first or second priority segment, or All. Tier 2: Solve in those segments, or Buy or Compare in any other segment. Tier 3: everything else. Within a tier, sort by volume, high to low, with unknown last. Break ties by lower difficulty.
9. Pick the next three briefs: the first three rows that are not Hold. Say how long they take at the publishing rate in channels-and-tools.md, labeled as an inference.
10. Check the draft against the context pack: each kept cluster needs a page that product.md and messaging.md can support, with no roadmap item and no word to avoid in its name or slug. Exclude any that fail.
11. List every assumption, estimate, inference and unknown in the last section. Say that volumes come from the marketer's export and were not verified.

## Output format

```
Status: Draft

## Keyword map: <product>, <export date>

Source: <export source and date the marketer named>
Rows in: <n>. Rows kept: <n>. Clusters: <n>.

## Clusters
Limit: 30 rows.
| # | Cluster | Intent | Volume | Segment | Persona | Action | Page | Tier |
|---|---|---|---|---|---|---|---|---|
| 1 | <primary keyword> | <intent> | <n or unknown> | <segment or All> | <persona> | <action> | <URL, or page type and slug> | <tier> |

## Keywords by cluster
- <primary keyword>: <the other keywords, comma separated, 9 at most>

## Excluded keywords
| Keyword | Volume | Reason, with file name |

## Next three briefs
1. <cluster>: <why it comes first, 25 words at most>

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does every volume come from the pasted export, or say "unknown"?
- [ ] Does each cluster map to exactly one page, and each page to one cluster?
- [ ] Did keywords for what the product is not go to the excluded table, even at high volume?
- [ ] Does every tier follow the rule and the priority order in icp-and-segments.md?
- [ ] Does every Compare cluster that names a competitor have a dated fact in competitors.md, or sit on Hold?

## Example (fictional company)

**Status:** Draft

**Keyword map: CogniATion Coach, assumed export**

Source: assumed export.
Rows in: 8. Rows kept: 5. Clusters: 3.

**Clusters**

| # | Cluster | Intent | Volume | Segment | Persona | Action | Page | Tier |
|---|---|---|---|---|---|---|---|---|
| 1 | critical thinking software for consultants | Buy | 390 | Professional services | Head of learning | New | Solution page, /consulting-firms | 1 |
| 2 | train analysts to check ai | Solve | 720 | Financial services | Head of learning | New | Guide, /check-ai-answers | 2 |
| 3 | new manager decision exercises | Solve | 260 | Software companies | Analyst or new manager | New | Blog post, /new-manager-decisions | 3 |

**Keywords by cluster**

- critical thinking software for consultants: critical thinking training for consultants
- train analysts to check ai: teach analysts to question ai

**Excluded keywords**

| Keyword | Volume | Reason, with file name |
|---|---|---|
| pre-employment critical thinking test | 1,300 | Not for hiring, product.md |
| ai memo writer | 880 | Will not write the memo, product.md |
| learning and development jobs | 2,400 | No link to buying |

**Next three briefs**

1. critical thinking software for consultants: first-priority segment, closest to buying.
2. train analysts to check ai: second-priority segment, and AI assistant rollouts trigger buying.
3. new manager decision exercises: this segment is served through inbound only.

**Assumptions and open questions**

- Assumption: all keywords, volumes and slugs are invented.
- Assumption: no existing page covers these clusters.
- Inference: three pages take about six weeks at about two blog posts a month, from channels-and-tools.md.
- Unknown: can solution pages ship alongside the blog schedule?

## How to run it

```
Use the skill "Build a keyword map". Read the context pack.
Task: <the export's source and date>.
<paste the keyword export and page list here>
```
