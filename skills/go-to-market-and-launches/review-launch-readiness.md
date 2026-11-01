---
title: Review launch readiness
type: skill
function: go-to-market-and-launches
owner: marketing-reviewer
reads: [company, product, messaging, competitors, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
you_bring: The launch plan, the full text of each asset, the launch date, and which approvals are in.
also_for: [are we ready to launch, go or no-go, launch checklist, launch next week, launch review, should we delay, launch risks, final check before launch]
version: 0.1.0
updated: 2026-11-01
summary: Returns a go, no-go or fix-first verdict on a launch plan and its assets, with blockers, fixes and approval status.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this once a launch plan and its assets exist, before the first public date. Do not use it to build the plan; use [Plan a product launch](plan-product-launch.md) instead. For one output outside a launch, use [Review any output](../marketing-ops/review-any-output.md).

## Inputs

- [[context-pack:company]]: which numbers may be published.
- [[context-pack:product]]: features, what it is not, roadmap rules, prices.
- [[context-pack:messaging]]: pillars and words to avoid.
- [[context-pack:competitors]]: sourced facts, to check every competitor claim.
- [[context-pack:proof-points]]: permission status for each customer, number and quote.
- [[context-pack:brand-voice]]: rules for public copy.
- [[context-pack:goals-and-kpis]]: definitions and baselines, to check launch measures.
- [[context-pack:channels-and-tools]]: approvers, typical times, channel limits, hard rules.

The marketer supplies: the launch plan, the full text of each asset, today's date, the launch date, who confirmed the release is on track, and which approvals are in.

## Procedure

1. List every asset in the plan and mark it Reviewed, Not supplied or Not finished. Review only what was pasted.
2. Check the release. If nobody named has confirmed that the release and the date are on track, record a blocker.
3. Check each claim in each asset against the context pack, in this order: product.md for what the product does and does not do, including roadmap rules; company.md for numbers; proof-points.md for customer names, numbers and quotes, against where the asset will appear; competitors.md for competitor claims, which need a source and a date; hard rules in channels-and-tools.md. Quote the words at fault and name the file.
4. Check public assets against brand-voice.md and the words to avoid in messaging.md.
5. Check approvals. For each asset, find its approver in channels-and-tools.md. Mark it Received, Requested or Not requested. Only the marketer's word counts as Received. Count the working days left and compare them with the typical time. If the time left is shorter, it cannot be fixed in time.
6. Check sales readiness: sales material is finished, sales is briefed before the first public date, and the plan says who answers buyer questions.
7. Check measurement and fallback: tracked links or tracking in place for anything paid, a launch measure with a baseline that matches goals-and-kpis.md, and a written plan if the release slips.
8. If a context pack file needed for a check is blank, mark that check Unknown and ask the marketer. Do not pass it, and do not fill the gap.
9. Rate each finding:
   - Blocker: a false claim, a claim the product cannot meet, proof without permission, a broken hard rule, a missing required approval, an unconfirmed release, or a planned asset that the launch cannot run without.
   - Fix: wrong voice, weak proof, a missing measure or fallback, or a late or unbriefed sales team.
   - Note: anything else worth a look.
10. Set the verdict with these rules, and stop at the first that fits:
    - No-go: a blocker cannot be fixed before the launch date, or the product cannot do what the main message claims.
    - Fix first: there is at least one blocker or an unknown, and all can be fixed before the launch date.
    - Go: no blockers and no unknowns. Fix items can remain, listed with owners.
11. For each blocker and fix, say what must change and who does it. Do not rewrite the asset unless asked.
12. List everything assumed or unknown in the last section. Say that the verdict is a recommendation and that the marketer decides.

## Output format

```
Verdict: <Go, No-go or Fix first>
Why: <max 30 words>
Latest date to fix: <date, from the launch date minus the longest approval still needed>
Status: Draft, recommendation only

## Blockers
| Asset | Words or issue | Breaks | What must change | Owner |

## Fixes
| Asset | Issue | What must change | Owner |

## Notes
<Max 3, one line each, or None>

## Asset status
| Asset | Reviewed, Not supplied or Not finished | Approver | Approval status | Time needed |

## Checks not run
<Each check not run, and why, or None>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the verdict come first, and does it follow from the written rules?
- [ ] Does each blocker quote the words at fault and name the file they break?
- [ ] Was each claim checked against the permission status for the place it will appear?
- [ ] Is each approval checked against the typical time and the days left?
- [ ] Are assets not supplied listed, instead of being passed?
- [ ] Does every blocker and fix have an owner?
- [ ] Is the review free of rewritten copy, unless the marketer asked for it?

## Example (fictional company)

**Verdict:** Fix first

**Why:** Two claims on the page are wrong and the date is unconfirmed, but all can be fixed and approved before launch.

**Latest date to fix:** L-2, two days for Anika Sole.

**Status:** Draft, recommendation only

**Blockers**

| Asset | Words or issue | Breaks | What must change | Owner |
|---|---|---|---|---|
| Launch page | "See each analyst's score" | Hard rule, channels-and-tools.md; product.md: no reports below team level | Remove the claim | Marketer |
| Launch page | "Makes new managers smarter" | Words to avoid, messaging.md; hard rule on intelligence claims | Remove the claim | Marketer |
| Launch page, launch email | No product claims approval | channels-and-tools.md | Send to Anika Sole, 2 days | Marketer |
| Release | No named person has confirmed the date | Unconfirmed release | Get a named confirmation | Marketer |

**Fixes**

| Asset | Issue | What must change | Owner |
|---|---|---|---|
| Launch email | Exclamation point in the subject line | Remove it, per brand-voice.md | Marketer |

**Notes:** None

**Asset status**

| Asset | Status | Approver | Approval status | Time needed |
|---|---|---|---|---|
| Launch page | Reviewed | Anika Sole | Not requested | 2 days |
| Launch email | Reviewed | Anika Sole | Not requested | 2 days |
| Sales one-pager | Not supplied | Tom Ferrant | Unknown | 2 days |

**Checks not run:** Sales one-pager, not supplied.

**Assumptions and open questions**

- Assumption: the reviewed plan and copy are illustrative, supplied by the marketer for the manager view release.
- Unknown: Who can confirm the release date, and can you paste the one-pager?

## How to run it

```
Use the skill "Review launch readiness". Read the context pack.
Task: <today's date, the launch date, who confirmed it, and which approvals are in>.
<paste the launch plan and each asset here>
```
