---
title: Plan a content calendar
type: skill
function: content
owner: content-lead
reads: [company, product, icp-and-segments, messaging, proof-points, goals-and-kpis, channels-and-tools]
you_bring: The period, any campaign briefs, items already scheduled, dates to avoid, hours per item and the hours you have for content.
also_for: [content plan, editorial calendar, what to publish, blog schedule, social schedule, posting schedule, content ideas, content for demand]
version: 0.1.0
updated: 2026-11-19
summary: Produces a dated content calendar for a set period, with every item tied to a goal or campaign and checked against capacity and approval times.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this to turn goals and campaigns into a dated list of what gets published, where and by whom, for a month or a quarter. Do not use it to choose the quarter's goals and bets; use [Write a quarterly plan](../budget-and-planning/write-quarterly-plan.md) instead. For the audience, offer and channels of one campaign, use [Write a campaign brief](../campaign-design/write-campaign-brief.md).

## Inputs

- [[context-pack:goals-and-kpis]]: marketing goals, deadlines and other priorities with dates.
- [[context-pack:channels-and-tools]]: channels, publishing cadence, approvers and their typical times.
- [[context-pack:company]]: size of the marketing team and any freelance time.
- [[context-pack:icp-and-segments]]: segment priority order.
- [[context-pack:messaging]]: pillars and words to avoid, for working titles.
- [[context-pack:proof-points]]: which customers and numbers may appear in public.
- [[context-pack:product]]: what may and may not be said about the roadmap.

The marketer supplies the period, any campaign briefs, items already scheduled, dates to avoid and, if known, effort per item and days available, as the office manual counts capacity.

## Procedure

1. Set the period from the request. If none is given, ask. Treat Monday to Friday as working days unless told otherwise.
2. List the fixed dates: deadlines from goals-and-kpis.md, dated priorities, and anything the marketer supplied. Give each goal in the period a one-letter tag (A, B).
3. Count the slots. For each channel in channels-and-tools.md, multiply its stated cadence by the length of the period, rounding up. That count is a ceiling, not a quota. Do not add slots beyond the cadence unless the marketer asks. If a channel has no stated cadence, write [cadence needed], leave that channel out of the calendar, except for fixed-date items, and ask in the last section.
4. Fill the slots in this order. First, items tied to a fixed date, published at least two working days before a hard deadline. Second, items supporting a campaign in the four weeks before its date. Third, remaining slots that can serve a goal, rotated through the segments in priority order, with the top segment getting the most. Leave the rest empty. The two-day and four-week windows are starting rules the marketer can change.
5. Give every item a goal tag. An item that serves no goal goes under "Cut or held", not on the calendar.
6. Name the skill that produces each item. If no skill fits, write "no skill".
7. Set the draft due date: publish date, minus the approver's typical time, minus one working day. A same-day approver counts as zero. Item types with no listed approver get [approver needed], and the draft due date is worked out as if the approver were same-day.
8. Move to "Cut or held" any item that depends on a roadmap item not cleared in product.md, an internal-only fact, or a proof point with status pending, sales only, internal only or none. Give held items no public date.
9. Run the capacity check. Count items per week and items needing design work. Count an item already in a campaign or launch plan once. If the marketer gave effort per item and days available, show both in days, as Estimates. If not, write [effort per item needed] or [days available needed], give the verdict "Not assessed" and do not guess. If the load exceeds them, remove items from the bottom of the order in step 4 and list them under "Cut or held".
10. Check the draft against the context pack: every date, cadence, approver and title. Remove words to avoid, and fix anything that contradicts a file.
11. List everything assumed, including publishing days you chose, under "Assumptions and open questions". If a needed context pack field is blank, leave a placeholder in square brackets and ask in the last section. Never invent.

The marketer copies the calendar into their own planning tool. This skill schedules and publishes nothing.

## Output format

```
Status: Draft
Period: <start date to end date>
Goals: <1 to 4 goals, each with a tag, copied from goals-and-kpis.md>
Fixed dates: <dated items, up to 8, or "None">

## Calendar
| Date | Channel | Working title | Goal | Segment | Skill | Approver, draft due |
|---|---|---|---|---|---|---|
<one row per item, in date order; working title up to 10 words>

## Capacity check
Items per week: <count by week>
Marketer: <days needed and days available with method, or the placeholder>
Design: <items needing design against available days>
Verdict: <fits, tight, over or Not assessed, in one sentence>

## Cut or held
<each item with its reason in up to 15 words, or "None">

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does every item have a date, a channel, a goal tag and a skill?
- [ ] Does each channel stay within the cadence in channels-and-tools.md?
- [ ] Are hard deadlines met at least two working days early?
- [ ] Is every draft due date worked out from the approver's typical time?
- [ ] Are roadmap items and unapproved proof points off the calendar?
- [ ] Is the verdict Not assessed whenever hours are unknown, with none made up?

## Example (fictional company)

**Status:** Draft

**Period:** February 8 to 15, 2027 (one week shown, condensed)

**Goals:** A: publish the campaign for professional services firms by February 15, 2027

**Fixed dates:** February 15, campaign deadline

**Calendar**

| Date | Channel | Working title | Goal | Segment | Skill | Approver, draft due |
|---|---|---|---|---|---|---|
| Feb 8 | Social | Did your last course change how anyone works? | A | Professional services | write-social-posts | Marketer, Feb 5 |
| Feb 9 | Blog | Three questions that show whether training changed the work | A | Professional services | write-blog-post | Marketer, Feb 8 |
| Feb 10 | Social | What to ask about one client memo | A | Professional services | write-social-posts | Marketer, Feb 9 |
| Feb 11 | Web | Professional services landing page update | A | Professional services | write-web-page | Marketer, Feb 8 |
| Feb 12 | Email | February newsletter: defending the reasoning in client memos | A | Professional services | write-marketing-email | Marketer, Feb 11 |
| Feb 12 | Social | The professional services page is live | A | Professional services | write-social-posts | Marketer, Feb 11 |

**Capacity check**

Items per week: six. Marketer: [effort per item needed]. Design: one page against about four designer days a month. Verdict: Not assessed until the hours are known.

**Cut or held**

CogniATion Coach manager view release: internal only, no public date.

**Assumptions and open questions**

- Assumption: social posts go out Monday, Wednesday and Friday.
- Assumption: the landing page is a fixed-date item, on top of the blog cadence.
- Unknown: how many hours does each item take?

## How to run it

```
Use the skill "Plan a content calendar". Read the context pack.
Task: <the period, the goals or campaigns to cover, and anything already scheduled>.
```
