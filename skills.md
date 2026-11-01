---
title: Skills
type: index
version: 0.1.0
updated: 2026-11-02
summary: Start from what you need to do. Each skill is a written procedure with a fixed output format. It produces a draft, and you decide what to use.
---

## What do you need to do?

| What is happening | Start with | Then |
|---|---|---|
| Sales says the leads are bad | [Start with this situation](guides/hard-situations.md#sales-says-the-leads-are-bad) | [Define the lead handoff](skills/marketing-ops/define-lead-handoff.md) |
| Pipeline is down, or the CEO asks why | [Diagnose a pipeline gap](skills/analytics-and-campaign-evaluation/diagnose-pipeline-gap.md) | [What to do next](guides/hard-situations.md#the-ceo-asks-why-pipeline-is-down) |
| I do not know what to do this week | [Set weekly priorities](skills/budget-and-planning/set-weekly-priorities.md) |  |
| We have no goals, or the CEO has not set any | [Propose quarterly goals](skills/budget-and-planning/propose-quarterly-goals.md) | [Write a quarterly plan](skills/budget-and-planning/write-quarterly-plan.md) |
| I have to plan next quarter, and have never done it | [Quarterly playbook](playbooks/quarterly.md) | [Write a quarterly plan](skills/budget-and-planning/write-quarterly-plan.md) |
| The budget was cut, or I must split it | [Allocate the budget](skills/budget-and-planning/allocate-budget.md) |  |
| Sales needs something for a buyer this week | [Write a sales one-pager](skills/product-marketing-and-sales-enablement/write-sales-one-pager.md) | [Write a sales deck](skills/product-marketing-and-sales-enablement/write-sales-deck.md) |
| A rival keeps appearing in deals | [Write a battlecard](skills/product-marketing-and-sales-enablement/write-battlecard.md) | [Write a competitor profile](skills/competitive-intelligence/write-competitor-profile.md) |
| We keep losing deals and I do not know why | [Analyze wins and losses](skills/competitive-intelligence/analyze-win-loss.md) | [Write an interview guide](skills/segmentation-icp-and-personas/write-interview-guide.md) |
| I need to run a campaign | [Write a campaign brief](skills/campaign-design/write-campaign-brief.md) |  |
| Leads came in and nothing happened | [Write a lead follow-up](skills/campaign-design/write-lead-follow-up.md) | [Design a nurture sequence](skills/campaign-design/design-nurture-sequence.md) |
| The website or a landing page needs work | [Write a web page](skills/content/write-web-page.md) |  |
| I need content for next month | [Plan a content calendar](skills/content/plan-content-calendar.md) | [Write a blog post](skills/content/write-blog-post.md) |
| Search traffic is flat | [Audit SEO from exports](skills/seo/audit-seo-from-exports.md) | [Build a keyword map](skills/seo/build-keyword-map.md) |
| Ad spend is not producing results | [Adjust paid campaigns](skills/paid-demand-gen/adjust-paid-campaigns.md) | [Plan a paid campaign](skills/paid-demand-gen/plan-paid-campaign.md) |
| We have a webinar or an event coming up | [Plan a webinar](skills/events-and-webinars/plan-webinar.md) | [Plan an event](skills/events-and-webinars/plan-event.md) |
| We have news to announce | [Write a press release](skills/pr-and-comms/write-press-release.md) | [Write a media pitch](skills/pr-and-comms/write-media-pitch.md) |
| Something went wrong in public | [Draft a holding statement](skills/pr-and-comms/draft-holding-statement.md) |  |
| Our messaging sounds like everyone else's | [Review messaging](skills/positioning-and-messaging/review-messaging.md) | [Build a messaging framework](skills/positioning-and-messaging/build-messaging-framework.md) |
| I am not sure who we should sell to | [Define the ICP](skills/segmentation-icp-and-personas/define-icp.md) | [Write a persona](skills/segmentation-icp-and-personas/write-persona.md) |
| I need customer quotes or proof | [Request customer proof](skills/product-marketing-and-sales-enablement/request-customer-proof.md) | [Write a case study](skills/product-marketing-and-sales-enablement/write-case-study.md) |
| I need to talk to customers | [Write an interview guide](skills/segmentation-icp-and-personas/write-interview-guide.md) | [Synthesize customer research](skills/segmentation-icp-and-personas/synthesize-customer-research.md) |
| The CEO asks how marketing is doing | [Write the monthly report](skills/analytics-and-campaign-evaluation/write-monthly-report.md) | [Read attribution](skills/analytics-and-campaign-evaluation/read-attribution.md) |
| Did that campaign work? | [Evaluate a campaign](skills/analytics-and-campaign-evaluation/evaluate-campaign.md) |  |
| A partner wants to do something together | [Plan co-marketing with a partner](skills/partner-and-channel-marketing/plan-co-marketing.md) | [Build a partner kit](skills/partner-and-channel-marketing/build-partner-kit.md) |
| A release is coming | [Launch playbook](playbooks/launch.md) | |
| I cannot tell if an output is any good | [Judge an output](guides/judge-an-output.md) | |

Not sure? Ask the head of marketing:

```
Act as the head of marketing from the Marketing Office. Follow your charter. Read the context pack. Today's task: which skill or agent role should handle this? <describe it>
```

## All skills

<input class="filter" type="search" placeholder="Filter, for example pipeline, leads or website" aria-label="Filter skills">
<p class="filter-empty" hidden>Nothing matches. Try one word, such as leads or pipeline, or use the table above.</p>

Skill pages have a Copy prompt button. Text file links open the plain text on GitHub. See [Use a skill](guides/use-a-skill.md). Not sure of a word? See the [glossary](office/glossary.md).

{% assign skills = site.pages | where: "type", "skill" -%}
{% for fn in site.data.functions %}
<div class="skill-group" markdown="1">

### {{ fn.label }} {#{{ fn.slug }}}

{% assign group = skills | where: "function", fn.slug | sort: "title" -%}
<table>
<thead><tr><th>Skill</th><th>What it does</th><th>Text file</th></tr></thead>
<tbody>
{% for skill in group -%}
<tr data-skill data-keywords="{{ skill.also_for | join: ' ' }}"><td><a href="{{ skill.url | relative_url }}">{{ skill.title }}</a></td><td>{{ skill.summary }}</td><td><a href="https://github.com/{{ site.repository }}/blob/main/{{ skill.path }}">GitHub</a></td></tr>
{% endfor -%}
</tbody>
</table>

</div>
{% endfor %}

## How a skill is built

<figure><div class="scroll">{% include diagrams/skill.svg %}</div><figcaption>Every skill has these sections in this order. The procedure and the template are what the model follows.</figcaption></figure>
