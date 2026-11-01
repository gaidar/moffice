---
title: Guides
type: index
version: 0.1.0
updated: 2026-11-01
summary: All guides for setting up and running the office.
---

Begin with [Start here](guides/start-here.md).

{% assign guides = site.pages | where: "type", "guide" | sort: "title" -%}
| Guide | What it covers |
|---|---|
{% for guide in guides -%}
| [{{ guide.title }}]({{ guide.url | relative_url }}) | {{ guide.summary }} |
{% endfor %}
