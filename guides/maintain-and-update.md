---
title: Maintain and update
type: guide
version: 0.1.0
updated: 2026-11-02
summary: Keep your context pack current, take new versions of the office, and recheck your setup when your AI tool changes.
---

## Who it is for

A marketer running the office for more than a month. Outdated facts in the context pack cause bad output, and the office cannot notice them for you.

## What you need

- Your `my-context-pack.md` file.
- Your project in your AI tool.
- About 30 minutes a month. This is an estimate.

## Steps

### Monthly: the context pack

1. Run this in a new chat:

   ```
   Read the context pack. List anything that looks out of date: dates more than 90 days old, goals for a past quarter, proof points without a recent approval, competitor facts without a recent check date. Do not change anything, only report.
   ```

2. Fix what matters in `my-context-pack.md`. Put a date on each fact you change.
3. Upload the changed file to your project, then delete the old copy. Two versions of the same file produce mixed answers.

### Quarterly: the goals

4. Update the goals-and-kpis section as part of [the quarterly playbook](../playbooks/quarterly.md).
5. Review the messaging and icp-and-segments sections against what sales is hearing. Use [Review messaging](../skills/positioning-and-messaging/review-messaging.md).

### When the Marketing Office has a new version

6. Check [the changelog](https://github.com/gaidar/moffice/blob/main/CHANGELOG.md).
7. Get the new files from [GitHub](https://github.com/gaidar/moffice). Replace `all-skills.md`, `all-agent-roles.md` and the office manual in your project, or the individual files if you use those. Do not replace `my-context-pack.md`.
8. If you edited a skill, compare it with the new one before you replace it, or keep yours under a different title.

### When your AI tool changes something

Tool-specific steps appear only in the setup guides. Skills, charters and the context pack do not change when an AI tool does.

9. If a step in your setup guide no longer matches what you see, check the help pages listed in that guide's Verification section.
10. If the feature has moved or gone, use the guide's Plain-chat fallback section, which needs only chat and file upload.
11. Report it through [the issue tracker](https://github.com/gaidar/moffice/issues/new), so the guide can be fixed for others.

### Moving to another AI tool

12. Follow the setup guide for the new tool, and upload the same 3 files. The skills, charters and context pack are identical on Claude, ChatGPT, Grok and Google Gemini. Your saved outputs are plain text and move with you.

## What success looks like

The monthly check finds little. Outputs quote current numbers. Nobody at your company finds an old price or an old customer in something you drafted.

## Troubleshooting

- **Answers mix old and new facts.** You probably have two versions of a file in your project. Delete the old one.
- **A skill behaves differently after an update.** Read the changelog entry. Ask for the output again in a new chat.
- **A proof point has expired.** Mark it "pending" until the customer approves it again, so that skills stop using it.
- **Your AI tool has renamed a feature.** The steps may still work under the new name. Check the help page, then report the change.
