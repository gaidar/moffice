---
layout: home
title: Home
heading: Run B2B marketing alone with the AI you already pay for
type: index
version: 0.1.0
updated: 2026-11-02
summary: A free library of written marketing procedures and company-fact templates. Load them into your AI tool, start with the job you need to finish, and ask for a one-pager, a campaign brief or this week's priorities. You provide the facts, make the decisions and publish through your own tools.
scope_note: Built for sales-led B2B tech companies. It covers getting and converting new business, with sales support. Retention, expansion, pricing and product-led growth are outside the current library. A spreadsheet counts as a CRM, and if a founder still sells, with few or no customers, there is a route for that.
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

1. **Name the job you need to finish.** A sales asset, a campaign or this week's priorities.
2. **Give it the facts that job needs.** [One file]({{ '/guides/fill-the-context-pack.html' | relative_url }}), from your answers, your documents or a conversation with the founders. Blanks are fine.
3. **Set up your AI tool**, then ask for it: [Claude]({{ '/guides/setup-claude.html' | relative_url }}), [ChatGPT and Codex]({{ '/guides/setup-chatgpt-codex.html' | relative_url }}), [Grok]({{ '/guides/setup-grok.html' | relative_url }}) or [Google Gemini]({{ '/guides/setup-google.html' | relative_url }}).

<div class="statrow">
  <div class="stat"><div class="v t">15 minutes to 1 hour</div><div class="k">Give it the facts your job needs</div></div>
  <div class="stat"><div class="v t">About 30 minutes</div><div class="k">Set up your AI tool</div></div>
  <div class="stat"><div class="v t">About 15 minutes</div><div class="k">Get your first draft</div></div>
  <div class="stat"><div class="v t">Each week</div><div class="k">Run the routine</div></div>
</div>
<p class="note" style="margin:10px 0 18px">Times are estimates from the steps, not measurements.</p>

Want to see a result first? [Try a sample company]({{ '/try.html' | relative_url }}) in 10 minutes. [Start here]({{ '/guides/start-here.html' | relative_url }}) walks you through it. After that, it depends on where the company is:

| Where you are | What to run |
|---|---|
| A sales team exists, and you are new here | [First week]({{ '/playbooks/first-week.html' | relative_url }}) |
| A founder still sells, with few or no customers | [Starting from zero]({{ '/playbooks/from-zero.html' | relative_url }}), the first 90 days, with what to skip |
| The office is running | [Run my week]({{ '/run-my-week.html' | relative_url }}) |

## How the office works

Choose a job, provide the facts it needs, draft and review, publish in your own tools, then record the result and the next action.

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
