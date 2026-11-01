---
title: Skills
type: index
version: 0.1.0
updated: 2026-11-01
summary: All skills, grouped by function. A skill is a written procedure with a fixed output format. It produces a draft, and you decide what to use.
diagram: skill
diagram_caption: "Every skill has these sections in this order. The procedure and the template are what the model follows."
---

<input class="filter" type="search" placeholder="Filter skills" aria-label="Filter skills">

Text file links open the plain text on GitHub. See [Use a skill](guides/use-a-skill.md) for how to run one.

{% assign skills = site.pages | where: "type", "skill" -%}
{% for fn in site.data.functions %}
<div class="skill-group" markdown="1">

## {{ fn.label }} {#{{ fn.slug }}}

Owning agent role: [{{ fn.owner_label }}]({{ '/agents/' | append: fn.owner | append: '.html' | relative_url }})

{% assign group = skills | where: "function", fn.slug | sort: "title" -%}
<table>
<thead><tr><th>Skill</th><th>What it does</th><th>Text file</th></tr></thead>
<tbody>
{% for skill in group -%}
<tr data-skill><td><a href="{{ skill.url | relative_url }}">{{ skill.title }}</a></td><td>{{ skill.summary }}</td><td><a href="https://github.com/{{ site.repository }}/blob/main/{{ skill.path }}">GitHub</a></td></tr>
{% endfor -%}
</tbody>
</table>

</div>
{% endfor %}
