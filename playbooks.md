---
title: Playbooks
type: index
version: 0.1.0
updated: 2026-11-02
summary: What to run and when. A playbook is a sequence of skills for a period or a project. One person runs one launch or one major campaign at a time.
diagram: cadence
diagram_caption: "A sample 13-week quarter. Bars show when each playbook runs."
---

{% assign order = "from-zero,first-week,weekly,monthly,quarterly,campaign-lifecycle,launch" | split: "," -%}
{% assign playbooks = site.pages | where: "type", "playbook" -%}
| Playbook | What it covers |
|---|---|
{% for name in order -%}
{%- assign wanted = "playbooks/" | append: name | append: ".md" -%}
{%- for playbook in playbooks -%}
{%- if playbook.path == wanted -%}
| [{{ playbook.title }}]({{ playbook.url | relative_url }}) | {{ playbook.summary }} |
{% endif -%}
{%- endfor -%}
{%- endfor %}
