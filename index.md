---
layout: home
title: Home
heading: Run a tech company's marketing alone
type: index
version: 0.1.0
updated: 2026-11-02
summary: With the AI subscription you already pay for. Give it your company's facts once, then ask for a one-pager, a campaign brief or this week's priorities. Each comes back as a draft in a set format, built to use only your facts, with every gap listed as a question. You decide what to use.
scope_note: Written for sales-led B2B companies with a CRM, MQLs and SQLs. Product-led motions are not covered.
---

## What you get

You paste a two-line prompt:

```
Use the skill "Write a sales one-pager". Read the context pack.
Task: one page for professional services firms, aimed at the VP of people, for one-to-one use by sales.
```

You get this back, for a fictional company called CogniATion:

<div class="output" markdown="1">
{% capture sample %}{% include sample-one-pager.md %}{% endcapture %}{{ sample }}
</div>

Three things to notice. The numbers come from your context pack, with their permission status checked. `[Sales contact needed]` shows a gap instead of inventing a name. The last section lists what it assumed, so you know what to check. [Try it yourself]({{ '/try.html' | relative_url }}), or see [more examples]({{ '/examples.html' | relative_url }}).

## How to begin

1. **Try it.** Use a sample company in any AI chat. [10 minutes]({{ '/try.html' | relative_url }}).
2. **Make a first pass of the context pack.** Give the office your company's facts in [one file]({{ '/guides/fill-the-context-pack.html' | relative_url }}). About an hour. Blanks are fine.
3. **Set up your AI tool.** About 30 minutes. Pick one:
   - [Claude]({{ '/guides/setup-claude.html' | relative_url }})
   - [ChatGPT and Codex]({{ '/guides/setup-chatgpt-codex.html' | relative_url }})
   - [Grok]({{ '/guides/setup-grok.html' | relative_url }})
   - [Google Gemini]({{ '/guides/setup-google.html' | relative_url }})
4. **Run your first skill.** Use your own facts, following [Use a skill]({{ '/guides/use-a-skill.html' | relative_url }}). About 15 minutes.
5. **Start the cadence.** Run [the first week playbook]({{ '/playbooks/first-week.html' | relative_url }}), then [the weekly playbook]({{ '/playbooks/weekly.html' | relative_url }}).

[Start here]({{ '/guides/start-here.html' | relative_url }}) walks you through all five. These times are estimates.

## What "set up" looks like when you are done

You can tell your CEO that all of this exists:

- A project in your AI tool, holding the office manual, your context pack and the skills.
- Company facts in one file, with every customer item marked for permission.
- Goals for the quarter, agreed with your CEO, and a plan with a budget.
- Agreed lead rules with sales, and tracking in place.
- One output through draft, review and approval, and a weekly routine you run.

## How the office works

<figure><div class="scroll">{% include diagrams/office.svg %}</div><figcaption>Every output is a draft with its assumptions listed. Nothing goes out until you decide.</figcaption></figure>

## Why not just ask your AI tool?

You can. Without this, each request starts from nothing. Facts drift, formats change, and the model fills gaps with plausible guesses. Here the facts sit in one place, each job has written steps and a fixed format, and the rule is to ask rather than guess. Models can still make errors, so read what comes back.

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

Copy it, or get it from [GitHub](https://github.com/{{ site.repository }}). Every page has buttons to copy the text, open the file on GitHub or see the raw file. Playbooks and guides, the procedures you read yourself, also come as PDFs.
