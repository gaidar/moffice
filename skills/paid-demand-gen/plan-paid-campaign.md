---
title: Plan a paid campaign
type: skill
function: paid-demand-gen
owner: paid-media-manager
reads: [icp-and-segments, personas, messaging, goals-and-kpis, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Sets the channel, audience, budget split, tests and stop rules for one paid campaign.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this before spending on a paid campaign, when you know the goal and the budget. Do not use it to plan a campaign across all channels, which belongs in [Write a campaign brief](../campaign-design/write-campaign-brief.md). Use [Allocate the budget](../budget-and-planning/allocate-budget.md) instead when the question is how much paid should get at all.

## Inputs

- [[context-pack:icp-and-segments]]: segment, region, company size, disqualifiers, triggers.
- [[context-pack:personas]]: who to target and the job titles to use.
- [[context-pack:messaging]]: pillars to test as angles.
- [[context-pack:goals-and-kpis]]: goals, budget, conversion rates, metric definitions.
- [[context-pack:channels-and-tools]]: current paid channels and spend, limits, approval thresholds.

The marketer supplies in the prompt: the goal, dates, budget, and the campaign brief if there is one. Paste past results and any keyword or audience-size figures. Without them, those fields stay unknown.

## Procedure

1. Check the gates first. List each limit in channels-and-tools.md as met, not met or unknown. If any is not met or unknown, say in the Gates section that no spend should start until it is met.
2. Set the target cost per MQL. Use the marketer's number if given. Otherwise work it out as an estimate: quarter budget divided by the SQL goal, multiplied by the MQL to SQL rate. Show the arithmetic. If any input is blank, write [target cost needed] and ask.
3. Choose channels. Use only the current paid channels in channels-and-tools.md, unless the marketer adds one. Exclude any type of ad that file forbids.
4. Define the audience per channel. For search ads: buying problems and terms from the persona's language, with disqualifier terms as exclusions. Treat volume as unknown unless pasted. For audience-targeted ads: job title from personas.md, industry, company size and region from icp-and-segments.md. Skip segments the priority order limits to other routes.
5. Split the budget. If channels-and-tools.md shows current spend, keep that ratio, so results can be compared with history. If not, give 70% to the channel that reaches people searching for a solution and 30% to the targeted channel. Hold back 10% of each line for tests.
6. Divide each line's budget by the target cost. That is the number of MQLs the line needs, an estimate and not a forecast. If a line needs fewer than 3, drop it and move its money to the other line.
7. Plan up to 2 tests. Each changes one thing and names the winner rule: the lower cost per MQL, once each option has at least 5 MQLs. If the budget cannot reach that, run one test only and say so.
8. Set the stop rules. Line: pause when spend reaches 3 times the target cost with no MQL. Campaign: review when cost per MQL stays above 2 times the target for two weeks in a row. These multiples, and the 70/30 split, 10%, 3-MQL and 5-MQL figures above, are starting rules the marketer can change, not benchmarks. They feed [Adjust paid campaigns](adjust-paid-campaigns.md).
9. List what must exist before launch: ad sets from [Write ad variations](write-ad-variations.md), landing page, tracking links, and any approval over the limits in channels-and-tools.md with its typical time.
10. Check the draft against the context pack: channel limits, disqualifiers, budget total, approval thresholds, definitions. Fix what contradicts it.
11. List everything assumed, estimated, inferred or unknown in the last section, using those labels.

## Output format

```
Status: Draft

## Gates
| Limit | Met, not met or unknown | What to do |

## Campaign summary
Goal: <one goal, with number and date>
Dates: <start to end>
Target cost per MQL: <number and arithmetic>

## Channels and audience
| Channel | Audience, up to 25 words | Exclusions |

## Budget split
| Line | Total | Per month | Test money | MQLs needed |

## Tests
| Test | What changes | Winner rule |

## Stop rules
<Up to 3 rules, each with a number>

## Needed before launch
| Item | Skill or owner | Approver and typical time |

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does the plan say clearly whether spend can start today?
- [ ] Does the budget split add up to the budget the marketer gave?
- [ ] Is the target cost the marketer's number, or an estimate with its arithmetic?
- [ ] Is every channel in channels-and-tools.md, with forbidden ad types excluded?
- [ ] Does each test change one thing and have a winner rule?
- [ ] Does each stop rule have a number?
- [ ] Are search volume and audience size marked unknown unless the marketer pasted them?
- [ ] Are approvals over the limit listed with time to get them?

## Example (fictional company)

Status: Draft

**Gates.** No ad spend without tracking in place: unknown, so confirm before February 15. No display retargeting: met.

**Campaign summary.** Goal: 67 MQLs from professional services firms by March 31, 2027. Dates: February 15 to March 31, 2027. Target cost per MQL: $202.

**Channels and audience**

| Channel | Audience | Exclusions |
|---|---|---|
| Search ads | Terms on critical thinking training and checking AI work | Course library, performance review terms |
| Professional social network ads | Heads of learning and VPs of people, consulting, accounting and law, 300 to 5,000 employees, United States, Canada, United Kingdom | Software companies |

**Budget split**

| Line | Total | Per month | Test money | MQLs needed |
|---|---|---|---|---|
| Search ads | $7,500 | $5,000 | $750 | 37 |
| Social ads | $6,000 | $4,000 | $600 | 30 |

**Tests.** One test only, given the budget: client memo angle against keep-practicing angle. Winner: lower cost per MQL at 5 MQLs each.

**Stop rules.** Line: pause at $606 with no MQL. Campaign: review after two weeks above $404 per MQL.

**Needed before launch.** Ad sets, landing page, tracking links. Search at $7,500 and social at $6,000 in total: Marta Ilves, 3 days.

**Assumptions and open questions**

- Assumption: all current paid spend moves to this campaign for 1.5 months.
- Assumption: a line's campaign total counts as one item for the $5,000 limit.
- Estimate: $202 is $70,000 divided by 90 SQLs, times the 26% MQL to SQL rate. 67 is $13,500 divided by $202, part of the 116 in the campaign brief.
- Unknown: search volume for these terms. Can you paste an export?

## How to run it

```
Use the skill "Plan a paid campaign". Read the context pack.
Task: <what they want>.
```
