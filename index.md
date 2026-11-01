---
layout: home
title: Home
heading: A marketing department in plain text
type: index
version: 0.1.0
updated: 2026-11-01
summary: Marketing Office is a free, open source playbook of skills and agent roles that you load into Claude, ChatGPT/Codex, Grok or Google Gemini on a personal subscription, to run a tech company's marketing function alone. It needs no servers, no API keys and no code. It produces drafts, plans, analyses and reviews, and you decide what to use.
---

## How to begin

1. **Pick your vendor.** Follow one setup guide.
2. **Fill the context pack.** Give the office the facts about your company, in [10 files]({{ '/context-pack.html' | relative_url }}).
3. **Run your first skill.** Paste one prompt and check the output.

Begin with [Start here]({{ '/guides/start-here.html' | relative_url }}), or go straight to a setup guide:

- [Set up on Claude]({{ '/guides/setup-claude.html' | relative_url }})
- [Set up on ChatGPT and Codex]({{ '/guides/setup-chatgpt-codex.html' | relative_url }})
- [Set up on Grok]({{ '/guides/setup-grok.html' | relative_url }})
- [Set up on Google Gemini]({{ '/guides/setup-google.html' | relative_url }})

## How the office works

<figure><div class="scroll">{% include diagrams/office.svg %}</div><figcaption>Every output is a draft with its assumptions listed. Nothing goes out until you decide.</figcaption></figure>

## What it covers

| Function | Skills | Owning agent role |
|---|---|---|
{% for fn in site.data.functions -%}
{%- assign count = site.pages | where: "type", "skill" | where: "function", fn.slug | size -%}
| [{{ fn.label }}]({{ '/skills.html' | relative_url }}#{{ fn.slug }}) | {{ count }} | [{{ fn.owner_label }}]({{ '/agents/' | append: fn.owner | append: '.html' | relative_url }}) |
{% endfor %}

## The operating cadence

<figure><div class="scroll">{% include diagrams/cadence.svg %}</div><figcaption>A sample 13-week quarter. <a href="{{ '/playbooks.html' | relative_url }}">The playbooks</a> list the steps.</figcaption></figure>

## Everything is plain text

Copy it, or get it from [GitHub](https://github.com/{{ site.repository }}). Every page has buttons to copy the text, open the file on GitHub or see the raw file. Playbooks and guides, the procedures you read yourself, also come as PDFs.
