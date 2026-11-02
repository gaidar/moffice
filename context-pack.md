---
title: Context pack
type: index
version: 0.1.0
updated: 2026-11-01
summary: The facts about your company, in one file you keep up to date. Every skill reads it, so output stays consistent across channels and months.
diagram: context
diagram_caption: "The first pass drafts them all at once. Blanks are fine: skills ask for what is missing."
---

See [Fill the context pack](guides/fill-the-context-pack.md) for the one-hour first pass. It uses [all 10 templates in one file](https://github.com/gaidar/moffice/blob/main/bundles/context-pack-templates.md).

## Blank templates

{% assign templates = site.pages | where: "type", "context-template" | sort: "title" -%}
| Template | What it holds | Text file |
|---|---|---|
{% for item in templates -%}
| [{{ item.title }}]({{ item.url | relative_url }}) | {{ item.summary }} | [GitHub](https://github.com/{{ site.repository }}/blob/main/{{ item.path }}) |
{% endfor %}

## Filled example

A complete pack for a fictional company, CogniATion, which makes a specialized AI chatbot that trains people to think. Its product, customers, people, competitors, numbers and quotes are all invented.

{% assign examples = site.pages | where: "type", "context-example" | sort: "title" -%}
| Example file | Text file |
|---|---|
{% for item in examples -%}
| [{{ item.title }}]({{ item.url | relative_url }}) | [GitHub](https://github.com/{{ site.repository }}/blob/main/{{ item.path }}) |
{% endfor %}
