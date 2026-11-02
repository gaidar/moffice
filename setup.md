---
title: Setup
type: index
version: 0.1.0
updated: 2026-11-02
summary: Pick the guide for your AI tool, and follow only that one. Skills, agent roles and the context pack are the same on all of them.
diagram: setup
diagram_caption: "Every guide covers both paths. Use the project path if your plan has it."
---

{% assign guides = site.pages | where: "type", "guide" | sort: "title" -%}
| Setup guide | What it covers |
|---|---|
{% for guide in guides -%}
{%- if guide.path contains "guides/setup-" -%}
| [{{ guide.title }}]({{ guide.url | relative_url }}) | {{ guide.summary }} |
{% endif -%}
{%- endfor %}

Try the [10-minute version](try.md) first if you want to see a result before you set anything up. Each guide also lists the vendor help pages it was checked against, with the date, and marks anything it could not verify.
