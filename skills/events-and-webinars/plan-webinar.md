---
title: Plan a webinar
type: skill
function: events-and-webinars
owner: events-and-webinar-manager
reads: [company, product, icp-and-segments, personas, messaging, proof-points, brand-voice, goals-and-kpis, channels-and-tools]
you_bring: The date or window, available speakers, any topic idea, and past registration and attendance numbers if you have them.
also_for: [no webinar history, how many sign-ups, online event, virtual event, webinar topic, webinar promotion, run of show, low webinar attendance, webinar for leads, live demo session]
version: 0.1.0
updated: 2026-11-02
summary: Produces a webinar plan with goal, topic, promotion timeline, run of show, roles and a failure plan.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when you are planning one live online session. Do not use it for an in-person event; use [Plan an event](plan-event.md) instead. For the wider campaign around it, use [Write a campaign brief](../campaign-design/write-campaign-brief.md), and once the session is over, use [Follow up after an event](follow-up-after-event.md).

## Inputs

- [[context-pack:company]]: people who can be named.
- [[context-pack:product]]: what can be shown live.
- [[context-pack:icp-and-segments]]: segment priority and triggers.
- [[context-pack:personas]]: daily problems and objections.
- [[context-pack:messaging]]: pillars and words to avoid.
- [[context-pack:proof-points]]: evidence and permission status.
- [[context-pack:brand-voice]]: rules for all copy.
- [[context-pack:goals-and-kpis]]: MQL definition and current goals.
- [[context-pack:channels-and-tools]]: list size, channels, approvers, limits.

The marketer supplies the date or window, speakers, any topic idea, and any past registration and attendance numbers.

## Procedure

1. Set the goal. Name the KPI in goals-and-kpis.md the webinar serves. Read the MQL definition and say which attendees count under it. If fit data is needed to count them, add those fields to the registration form.
2. Set targets: sign-ups needed = attendee target ÷ past attendance rate, shown as an estimate. With no history, use 30% to 50% of sign-ups attending (typical range, estimate), show sign-ups as a range, and say to replace it with the marketer's own numbers after the first event. With no attendee target, use one week's MQLs from the baseline (a starting rule), or ask.
3. Write three topic candidates. Each one states the persona, the daily problem from personas.md, the pillar and whether public proof exists. Reject any candidate that needs a roadmap item, a feature product.md does not list, or proof that is not marked public. Choose by these tests in order, including any topic the marketer gave: higher-priority segment, public proof available, fit with a current campaign in goals-and-kpis.md.
4. Write the title, saying what the attendee will be able to do, the abstract and three takeaways. Follow brand-voice.md. The session teaches first, and the product appears only as the way to do what was taught.
5. Assign roles: host, presenter, producer, chat moderator. The presenter cannot also produce. One person can hold producer and moderator, or host and moderator. Use only names from company.md or the marketer. Anyone else is [speaker needed]. A customer guest needs public permission in proof-points.md and the customer's agreement, so allow for approval time.
6. Build the promotion timeline by counting back from the session, with real dates: 4 weeks, registration page live; 3 weeks, first invitation; 2 weeks, social posts; 1 week, second invitation and personal invitations from sales; 1 day and 1 hour, reminders. If fewer than 3 weeks remain, say so and name what gets cut. Use only channels in channels-and-tools.md. Add paid spend only if the marketer asks and tracking is in place. Name the skill for each piece of copy. These times and the 45-minute default are starting rules the marketer can change.
7. Write the run of show by the minute: start time, what happens, who, what is on screen. Default to 45 minutes: 3 opening, 27 teaching and demo, 12 questions, 3 next step. Put one next step at the close and prepare two starter questions.
8. Write the failure plan: a dry run two business days before, a recorded demo if the live one fails, a named backup if the presenter drops out, what to do if the webinar tool goes down, and the follow-up date.
9. Check the draft against the context pack: claims, permissions, words to avoid and limits. For any blank field, leave a placeholder in square brackets and ask in the last section.
10. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
Status: Draft

## Webinar plan: <title>

Date and length: <date, time, minutes>
Goal: <KPI served, 25 words at most>
Who counts: <how attendees become MQLs, 25 words at most>
Targets: <attendees, sign-ups, with math; with no history, a range marked "typical range, estimate", to replace after the first event>
Form fields: <up to 8>

## Topic
| Topic | Persona | Segment | Pillar | Public proof | Result |
<3 rows>

## Copy
Title: <70 characters at most>
Abstract: <80 words at most>
Takeaways: <3 lines>
Proof used: <items, each marked public>

## Roles
Host: <name>. Presenter: <name>. Producer: <name>. Moderator: <name>

## Promotion timeline
| Date | Channel | Message | Owner | Skill or approver |

## Run of show
| Minute | What happens | Who | On screen |

## Failure plan
<up to 5 lines>

## Assumptions and open questions
- <Assumption, Estimate, Inference or Unknown>: <one item, unknowns as questions>
```

## Quality checklist

- [ ] Does the plan say which attendees count as MQLs, and does the form capture what that takes?
- [ ] Does the topic pass the rejection rules, with no roadmap item or feature outside product.md?
- [ ] Is every proof item marked public?
- [ ] Does each role have a real name or a visible placeholder, with the presenter not producing?
- [ ] Is there a plan for a failed demo and a missing presenter?

## Example (fictional company)

**Status:** Draft

**Webinar plan: How to show that training changed reasoning**

Date and length: February 24, 2027, 45 minutes
Goal: MQLs for the professional services campaign.
Who counts: attendees who fit the ICP.
Targets: 20 attendees who fit the ICP, one week of MQLs (260 / 13, a starting rule). 40 to 67 sign-ups: 30% to 50% attend (typical range, estimate). Replace with your own numbers after this event.
Form fields: name, email, company, employees, people to train

**Topic**

| Topic | Persona | Segment | Pillar | Public proof | Result |
|---|---|---|---|---|---|
| Show that training changed reasoning | Head of learning | Professional services | You can see reasoning improve | Brightmere Advisory 22% result | Chosen |

**Copy**

Title: How to show that training changed reasoning
Abstract: What completion data cannot show, how to score reasoning with a rubric, and how to report by team.
Proof used: Brightmere Advisory 22% result, public.

**Roles**

Host: the marketer. Presenter: [speaker needed]. Producer and moderator: [second person needed].

**Promotion timeline**

| Date | Channel | Message | Owner | Skill or approver |
|---|---|---|---|---|
| Jan 27 | Website | Registration page | Marketer | Write a web page |
| Feb 3 | Email list | Invitation | Marketer | Write a marketing email |

**Run of show**

| Minute | What happens | Who | On screen |
|---|---|---|---|
| 0 | Scoring and demo | Presenter | Sample scenario, team report |
| 42 | Request a demo | Host | Link |

**Failure plan**

Dry run February 22. Recorded demo as backup.

**Assumptions and open questions**

- Assumption: the date, after the February 15 campaign.
- Unknown: who presents?

## How to run it

```
Use the skill "Plan a webinar". Read the context pack.
Task: <the date or window, speakers, and topic or ask for options>.
```
