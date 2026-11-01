---
title: Fill the context pack
type: guide
version: 0.1.0
updated: 2026-11-01
summary: Turn your notes and old documents into the 10 files every skill reads, using your AI tool as the interviewer.
diagram: context
diagram_caption: "The steps below follow this order."
---

## Who it is for

A marketer who has finished one setup guide and now needs to give the office its facts. The office knows nothing about your company until you do this, and it decides nothing for you. It drafts, and you, the marketer, decide.

## What you need

- The 10 blank templates, in the folder `context-pack/templates/` on [GitHub](https://github.com/gaidar/moffice/tree/main/context-pack/templates).
- Whatever you already have: pitch deck, website copy, price list, customer stories, list of quotes, goals for the quarter, a list of who approves what.
- Your AI tool, set up per your guide.
- About 3 to 5 hours. This is an estimate. It depends on how much is already written down.

To see what a filled pack looks like, read [the fictional example](../context-pack/example-cogniation/company.md).

## Steps

Work through the files in this order, because later files draw on earlier ones:

| Order | File | Who usually knows it |
|---|---|---|
| 1 | [company.md](../context-pack/templates/company.md) | You, the CEO |
| 2 | [product.md](../context-pack/templates/product.md) | You, product lead |
| 3 | [icp-and-segments.md](../context-pack/templates/icp-and-segments.md) | You, sales |
| 4 | [personas.md](../context-pack/templates/personas.md) | You, sales |
| 5 | [proof-points.md](../context-pack/templates/proof-points.md) | You, customer success |
| 6 | [competitors.md](../context-pack/templates/competitors.md) | You, sales |
| 7 | [messaging.md](../context-pack/templates/messaging.md) | You |
| 8 | [brand-voice.md](../context-pack/templates/brand-voice.md) | You |
| 9 | [goals-and-kpis.md](../context-pack/templates/goals-and-kpis.md) | You, CEO, sales |
| 10 | [channels-and-tools.md](../context-pack/templates/channels-and-tools.md) | You |

For each file:

1. Start a new chat in your tool. Upload the blank template and any source documents you have for that topic.
2. Paste this prompt, changing the file name:

   ```
   We are filling in the context pack file company.md for the Marketing Office, using the template I uploaded.
   Rules: use only facts from my documents and my answers. Never guess. If you do not know a field, ask me.
   Step 1: fill in every field you can from my documents, and name the document each answer came from.
   Step 2: ask me about the remaining fields, a few at a time.
   Step 3: when I say "done", give me the whole file as plain markdown in one block. Keep the frontmatter and every heading. Under each field, keep only the answer. Leave a field blank if I did not answer it.
   ```

3. Answer the questions. When you do not know something, say "leave it blank". The skills will ask later.
4. Say `done`. Copy the finished block.
5. Open the template file in the plain text editor that comes with your computer, set to plain text mode, select everything, paste, and save it under the same file name. Save it in a folder called `my-context-pack`, so that you keep the blank templates.
6. Check the file yourself. Pay special attention to anything marked publishable and to each proof point's permission status. If a customer has not agreed in writing, mark it "pending".
7. Upload the finished file to your tool, in the way your setup guide describes, replacing the blank one if you uploaded it earlier.

When all 10 are in place, run this check in a new chat:

```
Read the context pack. List each of the 10 files, and for each one give the blank fields that would block a skill from running. Then list any contradictions between files. Do not fix anything, only report.
```

Fix what it finds, and upload the fixed files again.

## What success looks like

The check prompt returns all 10 files, a short list of acceptable blanks and no contradictions. A stranger reading your pack could brief a campaign.

Skills that rely on your blanks will ask for the missing facts, and that is the office working correctly.

## Troubleshooting

- **The model fills in fields you never gave it.** Say: "Remove every answer that did not come from my documents or my answers." Then check the file yourself before saving it.
- **You do not know the permission status of a customer.** Mark it "none" until someone checks. Skills will not use it in public copy.
- **You have no positioning yet.** Leave messaging.md blank for now, and run the skill [Write a positioning statement](../skills/positioning-and-messaging/write-positioning-statement.md) once the first six files are filled in. Then run [Build a messaging framework](../skills/positioning-and-messaging/build-messaging-framework.md) and paste the result into messaging.md.
- **Your brand voice is not written down.** Run [Codify the brand voice](../skills/brand-and-design-briefs/codify-brand-voice.md) with a few samples of writing you like.
- **Your tool will not take a .md file.** Save the file as .txt and upload that. Or paste the text into the chat.
- **Facts changed.** Edit the file, upload it again, and delete the old copy. The guide [Maintain and update](maintain-and-update.md) sets a monthly routine.
