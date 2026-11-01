---
title: Playbooks
type: index
version: 0.1.0
updated: 2026-11-01
summary: The operating cadence and project sequences. A playbook is a sequence of skills for a period or a project.
diagram: cadence
diagram_caption: "A sample 13-week quarter. Bars show when each playbook runs."
---

{% assign playbooks = site.pages | where: "type", "playbook" | sort: "title" -%}
| Playbook | What it covers |
|---|---|
{% for playbook in playbooks -%}
| [{{ playbook.title }}]({{ playbook.url | relative_url }}) | {{ playbook.summary }} |
{% endfor %}
