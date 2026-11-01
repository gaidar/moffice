---
title: Specify a dashboard
type: skill
function: analytics-and-campaign-evaluation
owner: marketing-analyst
reads: [goals-and-kpis, channels-and-tools, company]
you_bring: Who will look at the dashboard, the decision each person makes from it, and the tool you will build it in.
also_for: [marketing dashboard, kpi dashboard, reporting setup, numbers do not match, what to track, ceo wants a dashboard, pipeline report, metric definitions]
version: 0.1.0
updated: 2026-11-01
summary: Writes a dashboard spec with metrics, definitions, sources and views, which the marketer builds in their own tool.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this before building or rebuilding a marketing dashboard, so the definitions are settled first. Do not use it to read the numbers themselves, which belongs to [Write the monthly report](write-monthly-report.md), or to fix link tagging, which belongs to [Set tracking conventions](../marketing-ops/set-tracking-conventions.md).

## Inputs

- [[context-pack:goals-and-kpis]]: KPIs, definitions, baselines, targets and review cadence.
- [[context-pack:channels-and-tools]]: which tool does which job, and who has access.
- [[context-pack:company]]: which numbers are internal only and which must never appear.

The marketer pastes into the chat:

- Who will look at the dashboard, and the decision each person makes from it.
- The tool it will be built in.
- Field names or export column headers from each source tool, if available.

## Procedure

1. Write the purpose: one audience and the decisions it supports. If the audiences need different numbers, give each its own view rather than a separate metric list.
2. List metrics. Start with every KPI in goals-and-kpis.md. Add another metric only if the marketer names a decision it changes. Cap the list at 12, and record what you cut.
3. Give each metric a definition, copied from goals-and-kpis.md where one exists. If none exists, write a proposed definition and label it an assumption. Never change a definition silently.
4. Give each metric a source, using the tool by job from channels-and-tools.md: pipeline and SQLs from the CRM, visits from the web analytics tool, and so on. If the marketer supplied field names, name the field. Otherwise write [field to confirm]. If a metric needs data from two tools, mark it "manual join" and name the shared field.
5. Set the refresh from the KPI's review cadence. A KPI reviewed weekly refreshes weekly, and so on.
6. Set the target from goals-and-kpis.md. If a KPI has only a baseline, show the baseline and write "no target set". Do not make one up.
7. Lay out the views. Make one view per review cadence that has KPIs, in order: weekly, monthly, quarterly. Choose the display by this rule: a goal shows as one number against target and pace, a trend shows as a line over time, and a comparison across channels shows as a table or bars.
8. Set access. A number marked internal only in company.md goes only in views for people inside the company. A number marked never to be mentioned stays off the dashboard. Flag any metric whose source tool the viewer cannot open, as listed in channels-and-tools.md.
9. Write the build check: recalculate each KPI for the last closed period and compare it with its baseline in goals-and-kpis.md. A mismatch means the definition or the source is wrong, so fix that before anyone reads the dashboard.
10. Check the draft against the context pack: every KPI is present, definitions are unchanged and tool jobs match. If a needed field is blank, leave a visible placeholder such as [target needed] and ask in the last section. Never invent.
11. List every assumption, estimate, inference and unknown in the last section, including each unconfirmed field.

## Output format

The marketer builds the dashboard from it.

```
Status: Draft

## Purpose
<Audience and the decisions it supports. Max 40 words.>

## Metrics
| Metric | Definition | Source | Refresh | Target or baseline |
<Up to 12 rows. Definition max 20 words.>

## Views
<One bullet per view: name, cadence, metrics in order, display for each. Max 40 words each.>

## Access
<Up to 4 bullets, max 25 words each.>

## Build check
<Up to 5 numbered steps, max 25 words each.>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Is every KPI in goals-and-kpis.md on the list?
- [ ] Are the definitions copied without silent changes?
- [ ] Does every metric have a source, with unconfirmed fields marked?
- [ ] Does each added metric have a named decision behind it?
- [ ] Does each view match a review cadence?
- [ ] Are internal-only numbers limited and never-mention numbers absent?
- [ ] Does the build check reproduce a known baseline?

## Example (fictional company)

Status: Draft

Assumption: CogniATion's marketer asked for one dashboard for the marketer and the head of sales, with no field names supplied.

**Purpose**

Marketer and Tom Ferrant, head of sales: decide each week whether pipeline is on pace and where to shift effort.

**Metrics**

| Metric | Definition | Source | Refresh | Target or baseline |
|---|---|---|---|---|
| New qualified pipeline | Value of opportunities accepted by sales, created this quarter, with marketing as first or last touch | CRM, [field to confirm] | Weekly | $1.2 million by March 31, 2027 |
| MQLs | Fits the ICP and has requested a demo, attended a webinar or downloaded two resources | CRM, [field to confirm] | Weekly | Baseline 260 |
| Website demo requests | No definition in goals-and-kpis.md, assumed completed demo forms | Web analytics tool, [field to confirm] | Weekly | Baseline 58 |
| MQL to SQL rate | SQLs divided by MQLs | CRM, [field to confirm] | Monthly | Baseline 26% |

**Views**

- Weekly: pipeline against pace, then MQLs and demo requests as lines.
- Monthly: MQL to SQL rate as a line.

**Access**

- The web analytics tool is marketer only, so the head of sales sees demo requests through the shared view.
- No view shows an individual learner's conversation or score.
- Runway and investor terms stay off the dashboard.

**Build check**

1. Recalculate Q3 2026 MQLs. The result should be 260.

**Assumptions and open questions**

- Assumption: the demo request and rate definitions above. Sources are mapped from tool jobs. Other KPIs are left out here, condensed for length.
- Unknown: Does the dashboard tool read the web analytics tool directly, or do you paste exports?

## How to run it

```
Use the skill "Specify a dashboard". Read the context pack.
Task: <specify a dashboard for whom, to support which decisions>.
```
