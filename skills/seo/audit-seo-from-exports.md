---
title: Audit SEO from exports
type: skill
function: seo
owner: seo-specialist
reads: [product, icp-and-segments, messaging, brand-voice, goals-and-kpis, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Turns pasted search console and crawl exports into a ranked list of fixes with evidence and owners.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this monthly, or after a site change, when you have search console or crawl exports and need to know what to fix first. Do not use it to plan new topics; use [Build a keyword map](build-keyword-map.md) instead. To rebuild one page after the audit, use [Write an SEO page brief](write-seo-page-brief.md).

## Inputs

- [[context-pack:product]]: what the product is and is not.
- [[context-pack:icp-and-segments]]: segments, to decide which pages matter most.
- [[context-pack:messaging]]: words to avoid.
- [[context-pack:brand-voice]]: rules for replacement titles and descriptions.
- [[context-pack:goals-and-kpis]]: the organic KPI and its baseline.
- [[context-pack:channels-and-tools]]: who can change what on the site.

The marketer pastes at least one export. The search console export needs page, query if available, clicks, impressions, CTR and average position, for two equal periods with dates. The crawl export needs URL, status code, indexability, canonical, title, meta description, inlinks and click depth. Also useful: dates of site changes and a list of the pages that matter most.

## Procedure

1. Inventory the data: file, date range, row count and columns. If a row count is a round limit, such as exactly 1,000, flag it as possibly truncated. If no export is pasted, stop and ask. Any check whose columns are missing goes under Not checked.
2. Tag each URL as ICP page or Other. It is an ICP page if the marketer listed it, or if its topic matches a segment or the product. Label topic matches as an inference. If icp-and-segments.md is blank, write [ICP needed] and ask in the last section.
3. Run these checks in order. Every finding names URLs and quotes numbers from the export. The cutoffs are starting rules the marketer can change, not benchmarks.
   - Blocked: status 4xx or 5xx, noindex, or a canonical pointing elsewhere.
   - Lost ground: clicks down 25% or more between periods, from at least 20 clicks.
   - Near win: average position 4 to 15, with impressions in the top quarter of the export.
   - Weak snippet: position 10 or better with CTR below this export's median for its band (1 to 3, or 4 to 10), or a title over 60 characters, or a meta description missing or over 155.
   - Competing pages: two or more URLs each holding at least 10% of a query's impressions.
   - Structure: an ICP page with 2 inlinks or fewer, or click depth over 3.
   - Off target: impressions driven by queries for something product.md says the product is not.
4. Rate impact. High: an ICP page with a Blocked, Lost ground or Near win finding. Medium: an ICP page with any other finding, or an Other page that is Blocked. Low: everything else.
5. Rate effort from who can make the change, using channels-and-tools.md. Low: one page, in the CMS, by the marketer. Medium: a page rewrite. High: engineering, or a change across the site.
6. Rank fixes in this order: High impact and Low effort, High and Medium, Medium and Low, High and High, Medium and Medium, then the rest. Keep the top 10. The rest go under Parked with a reason.
7. Write each fix: what to change, on which URL, who does it, and the number to check in next month's export. For a title or description problem, draft the replacement within the limits and the brand voice.
8. State causes only as far as the data shows. Label a cause as an inference and name the inputs, or write "cause unknown". Do not mention search engine updates or competitor moves unless the marketer supplied them.
9. Compare with the organic KPI only if the marketer pasted the same measure. Clicks in a search console export are not the same as visits in a web analytics tool. If the KPI is blank, write [organic KPI needed].
10. Check the draft against the context pack: replacement titles use no word to avoid, promise only what product.md supports, and owners match channels-and-tools.md.
11. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
Status: Draft

## SEO audit: <site>, <periods compared>

Bottom line: <biggest problem and first fix, 2 sentences at most>
Data used: <each export, dates, row count, 40 words at most>

## Prioritized fixes
Limit: 10 rows, ranked.
| # | Fix | URL | Check | Evidence from export | Impact | Effort | Who | Next-month test |

## Draft titles and descriptions
- <URL>: <title, 60 characters at most> / <description, 155 characters at most>

## KPI comparison
<one line: KPI, baseline, current figure and source, or [figure needed]>

## Parked
- <URL or issue>: <reason, 15 words at most>

## Not checked
- <check>: <missing column or export>

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does every finding quote a URL and a number from your exports?
- [ ] Do the rankings follow the impact and effort rules, with nothing moved by feel?
- [ ] Are checks with missing data listed under Not checked, not skipped silently?
- [ ] Is every cause labeled as an inference or marked unknown?
- [ ] Does each fix name an owner who has access, per channels-and-tools.md?

## Example (fictional company)

**Status:** Draft

**SEO audit: cogniation.example, September and October 2026**

Bottom line: The professional services page is blocked from search. Remove the noindex first.
Data used: search console by page (400 rows), crawl (210 URLs).

**Prioritized fixes**

| # | Fix | URL | Check | Evidence from export | Impact | Effort | Who | Next-month test |
|---|---|---|---|---|---|---|---|---|
| 1 | Remove noindex | /professional-services | Blocked | Noindex, 0 clicks | High | Low | Marketer | Impressions above 0 |
| 2 | Rewrite title | /critical-thinking-training | Near win | Position 7.2, 4,100 impressions, CTR 0.9%, band median 2.1% | High | Low | Marketer | CTR above band median |
| 3 | Add three inlinks | /scenario-library | Structure | 1 inlink, depth 4 | Medium | Low | Marketer | 4 inlinks |

**Draft titles and descriptions**

- /critical-thinking-training: Critical thinking training that asks instead of answers / CogniATion Coach questions employees about work problems, declines to give the answer and scores their reasoning. You see progress by team.

**KPI comparison**

Organic visits from ICP pages: baseline 9,400, Q3 2026. Current: [figure needed].

**Parked**

- /company-news: Other page, low impact.

**Not checked**

- Competing pages and Off target: no query by page export.

**Assumptions and open questions**

- Assumption: all URLs, exports and figures are invented for this example.
- Inference: /professional-services is an ICP page, because its topic matches the first-priority segment in icp-and-segments.md.
- Unknown: was the noindex deliberate?
- Unknown: what is the web analytics figure for organic visits?

## How to run it

```
Use the skill "Audit SEO from exports". Read the context pack.
Task: audit our site from the search console and crawl exports pasted below, for <periods>.
```
