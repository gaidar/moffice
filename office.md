---
title: Office
type: index
version: 0.1.0
updated: 2026-11-01
summary: The core documents of the office.
---

{% assign docs = site.pages | where: "type", "office" | sort: "title" -%}
| Document | What it covers |
|---|---|
{% for doc in docs -%}
| [{{ doc.title }}]({{ doc.url | relative_url }}) | {{ doc.summary }} |
{% endfor %}
