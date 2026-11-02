---
title: Agents
permalink: /agents.html
type: index
version: 0.1.0
updated: 2026-11-02
summary: A role is an instruction for one chat. It runs nothing by itself. Use one when you know the problem but not the output. Start with the head of marketing.
diagram: agents
diagram_caption: "Each role owns skills and can hand work to the others. You give the instructions, and you decide."
---

See [Invoke an agent role](guides/invoke-an-agent.md) for how to run one, and [a worked example](guides/invoke-an-agent.md#worked-example-a-role-plans-a-campaign).

{% assign agents = site.pages | where: "type", "agent" | sort: "title" -%}
| Agent role | Bring it | Skills | Text file |
|---|---|---|---|
{% for agent in agents -%}
{%- if agent.path contains "head-of-marketing" -%}
{%- assign owned = site.pages | where: "type", "skill" | where: "owner", "head-of-marketing" | size -%}
| [{{ agent.title }}]({{ agent.url | relative_url }}) | {{ agent.bring_it }} | {{ owned }} | [GitHub](https://github.com/{{ site.repository }}/blob/main/{{ agent.path }}) |
{% endif -%}
{%- endfor -%}
{% for agent in agents -%}
{%- unless agent.path contains "head-of-marketing" -%}
{%- assign slug = agent.path | split: "/" | last | replace: ".md", "" -%}
{%- assign owned = site.pages | where: "type", "skill" | where: "owner", slug | size -%}
| [{{ agent.title }}]({{ agent.url | relative_url }}) | {{ agent.bring_it }} | {{ owned }} | [GitHub](https://github.com/{{ site.repository }}/blob/main/{{ agent.path }}) |
{% endunless -%}
{%- endfor %}
