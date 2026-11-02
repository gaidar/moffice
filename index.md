---
layout: home
title: Home
heading: Run a tech company's marketing alone
type: index
version: 0.1.0
updated: 2026-11-02
summary: With the AI subscription you already pay for. Give it your company's facts once, then ask for a one-pager, a campaign brief or this week's priorities. Each comes back as a draft in a set format, built to use only your facts, with every gap listed as a question. You decide what to use.
scope_note: Written for sales-led B2B companies. A spreadsheet counts as a CRM, and if a founder still sells, with few or no customers, there is a route for that. Product-led motions are not covered.
---

## What you get

You ask in plain words:

```
Write a sales one-pager for professional services firms, aimed at the VP of people, for one-to-one use by sales.
```

The office finds the skill, tells you which one it used and reads your facts. You get this back, shown here for a fictional company called CogniATion:

<div class="output" markdown="1">
{% capture sample %}{% include sample-one-pager.md %}{% endcapture %}{{ sample }}
</div>

Three things to notice. The numbers come from your context pack, with their permission status checked. `[Sales contact needed]` shows a gap instead of inventing a name. The last section lists what it assumed, so you know what to check. [Try it yourself]({{ '/try.html' | relative_url }}), or see [more examples]({{ '/examples.html' | relative_url }}).

## How to begin

1. **Try it.** Use a sample company in any AI chat. [10 minutes]({{ '/try.html' | relative_url }}).
2. **Give it your facts.** [One file]({{ '/guides/fill-the-context-pack.html' | relative_url }}), from your documents or from a conversation with the founders. Blanks are fine.
3. **Set up your AI tool**, then ask for your first draft: [Claude]({{ '/guides/setup-claude.html' | relative_url }}), [ChatGPT and Codex]({{ '/guides/setup-chatgpt-codex.html' | relative_url }}), [Grok]({{ '/guides/setup-grok.html' | relative_url }}) or [Google Gemini]({{ '/guides/setup-google.html' | relative_url }}).

[Start here]({{ '/guides/start-here.html' | relative_url }}) walks you through it. After that, it depends on where the company is:

| Where you are | What to run |
|---|---|
| A sales team exists, and you are new here | [First week]({{ '/playbooks/first-week.html' | relative_url }}) |
| A founder still sells, with few or no customers | [Starting from zero]({{ '/playbooks/from-zero.html' | relative_url }}), the first 90 days, with what to skip |
| The office is running | [Weekly]({{ '/playbooks/weekly.html' | relative_url }}) |

## How the office works

<figure><div class="scroll">{% include diagrams/office.svg %}</div><figcaption>Every output is a draft with its assumptions listed. Nothing goes out until you decide.</figcaption></figure>

## Why not just ask your AI tool?

You can. But each request then starts from nothing, so facts drift and the model fills gaps with plausible guesses. Here the facts sit in one place, each job has written steps and a fixed format, and the rule is to ask rather than guess. Models can still make errors, so read what comes back.

## The operating routine

<figure><div class="scroll">{% include diagrams/cadence.svg %}</div><figcaption>A sample 13-week quarter, with one launch or one major campaign at a time. <a href="{{ '/playbooks.html' | relative_url }}">The playbooks</a> list the steps.</figcaption></figure>

## What it covers

| Function | Skills | Owning agent role |
|---|---|---|
{% for fn in site.data.functions -%}
{%- assign count = site.pages | where: "type", "skill" | where: "function", fn.slug | size -%}
| [{{ fn.label }}]({{ '/skills.html' | relative_url }}#{{ fn.slug }}) | {{ count }} | [{{ fn.owner_label }}]({{ '/agents/' | append: fn.owner | append: '.html' | relative_url }}) |
{% endfor %}

## Everything is plain text

Copy it, download it or get it from [GitHub](https://github.com/{{ site.repository }}). Playbooks and guides, the procedures you read yourself, also come as PDFs.
