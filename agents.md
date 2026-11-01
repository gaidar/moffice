---
title: Agents
type: index
version: 0.1.0
updated: 2026-11-01
summary: The 14 agent roles. An agent role is a job description with a charter. It drafts and recommends, and you decide.
diagram: agents
diagram_caption: "Each role owns skills and can hand work to the others. You give the instructions, and you decide."
---

See [Invoke an agent role](guides/invoke-an-agent.md) for how to run one.

{% assign agents = site.pages | where: "type", "agent" | sort: "title" -%}
| Agent role | Mission | Skills owned | Text file |
|---|---|---|---|
{% for agent in agents -%}
{%- assign slug = agent.path | split: "/" | last | replace: ".md", "" -%}
{%- assign owned = site.pages | where: "type", "skill" | where: "owner", slug | size -%}
| [{{ agent.title }}]({{ agent.url | relative_url }}) | {{ agent.summary }} | {{ owned }} | [GitHub](https://github.com/{{ site.repository }}/blob/main/{{ agent.path }}) |
{% endfor %}
