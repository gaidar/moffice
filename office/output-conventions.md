---
title: Output conventions
type: office
version: 0.1.0
updated: 2026-11-02
summary: The rules every skill output follows, so outputs look and read the same across roles and months.
---

Every output from a skill or an agent role follows these rules. The office manual has the short version.

## Structure

1. Start with the result. No introduction, no recap of the task, no closing remarks.
2. Use the template from the skill's Output format section. Keep its field names and section order. When one job runs several skills in a chat, show the working view the office manual describes, and the full record on request.
3. Stay inside the length limits in the template. Limits count a field's content, not its label. If the content does not fit, cut it and say what you cut under "Assumptions and open questions".
4. End with the section "Assumptions and open questions". Nothing comes after it.

## The last section

Use this title and these four labels. Skip a label that has no items. If no label has items, write "None".

```
## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Facts and sources

| Kind of statement | What to do |
|---|---|
| Fact about the company in the context pack | Use it as written |
| Fact about the company not in the context pack | Ask first if it changes the whole output. Otherwise, leave a placeholder in square brackets and ask in the last section |
| Task evidence: an export, note or answer the marketer supplied for this task | Use it for this task and name it as the source. It does not clear a customer, number or quote for public use. If it conflicts with the context pack, show both and ask |
| Customer name, quote or result | Use only if proof-points.md shows the right permission status for that use |
| Company number | Use anywhere only if company.md marks it publishable. Any other number stays in internal output. Never use a number company.md says never to mention |
| Competitor claim | Use only if competitors.md has it with a source and date. Otherwise label it unknown |
| Outside fact the marketer gave you | Use it and name the source they gave |
| Outside fact from your memory | Label it unverified, or leave it out |
| Benchmark or industry average | Use at most one per output, labeled "typical range, estimate" |

A placeholder is always visible and in square brackets: `[customer quote needed]`, `[Q3 pipeline number needed]`. Never replace a placeholder with a plausible guess.

## Writing

- Use sentence-case headings. Capitalize the first word and proper names only.
- Use en dashes (–) or commas. Never use long dashes.
- Write in US English.
- Keep paragraphs short, with one idea each.
- Use lists for real items or sequences. Use tables for comparisons or numbers. Use bold only for real emphasis.
- Avoid the words listed under "words to avoid" in messaging.md, and the words `scripts/validate.py` rejects in this repo.
- Write like an experienced operator advising a busy, skeptical peer. Direct and serious, with no hype.

For public copy, brand-voice.md takes priority over the tone rule above.

## Tracking and file names

Save each output you keep with this name, so that you can find it later: `YYYY-MM-DD-<skill-file-name>-<short-topic>.md`. For example, `2026-11-02-write-campaign-brief-spring-webinar.md`.

Campaign names and tracking parameters follow the conventions set by the skill "Set tracking conventions", once you have run it.

## Status labels

Every output is one of these. The model marks new outputs as draft. Only the marketer changes the status.

| Status | Meaning |
|---|---|
| Draft | Produced by the office, not reviewed by the marketer |
| Reviewed | Checked by the marketer, or by the marketing reviewer and then the marketer |
| Approved | The marketer decided to use it, and any approver listed in channels-and-tools.md has signed off |
| Published | Live, sent or handed to sales |
