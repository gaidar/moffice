---
title: Fill the context pack
type: guide
version: 0.1.0
updated: 2026-11-02
summary: Turn your notes and old documents into one file, my-context-pack.md, that every skill reads, in about an hour of plain chat.
diagram: context
diagram_caption: "The order the sections follow. The fast first pass drafts them all at once."
---

## Who it is for

A marketer ready to give the office its facts. The office knows nothing about your company until you do this. You do not need a project yet, because this works in plain chat.

## What you need

- The 10 templates in one file. Open [context-pack-templates.md](https://raw.githubusercontent.com/gaidar/moffice/main/bundles/context-pack-templates.md) and save the page to your computer under that name, or copy all of it into a plain text file.
- Whatever you already have: pitch deck, website copy, price list, customer stories, list of quotes, goals for the quarter, a list of who approves what.
- Any AI chat that takes file uploads.
- A plain text editor. One comes with your computer.
- About an hour for the chat in the fast first pass. This is an estimate, and it depends on how much is already written down. True answers from your CEO, sales and customer success can take days. Blanks in the meantime are normal, and do not mean you failed.

To see what a filled pack looks like, read [the fictional example](../context-pack/example-cogniation/company.md).

## Steps

### Fast first pass

Do not invent anything to fill a field. Blanks are fine: skills ask about them later.

1. Start one new chat. **Before you upload anything, strip what should not leave the company.** You are probably on a personal subscription, so remove revenue, runway, customer contracts and personal data from your documents. Delete those slides or pages, or copy out only the parts you need. Blanks are fine, so nothing here is worth the risk. If you are unsure about a document, ask your CEO first. Check the data settings for your plan on your AI tool's help page.

   Then upload `context-pack-templates.md` and your stripped source documents. If your tool limits uploads, send the most useful documents first and the rest in your next message.
2. Paste this prompt:

   ```
   We are filling in the context pack for the Marketing Office. The file context-pack-templates.md holds all 10 templates. The other files I uploaded are my source documents.

   Rules:
   - Use only facts from my documents and my answers. Never guess, and never fill a field with something plausible.
   - "Guidance:" and "Example:" lines describe a fictional company. They are never facts.
   - After every answer, name its source in parentheses: the document and the page, or "my answer".
   - A blank field is fine. Leave it empty.
   - Do not mark a number as publishable, or a customer, number or quote as approved, unless a document or I say so.

   Step 1: draft every section from my documents.
   Step 2: ask me only the questions that block work, all together and numbered. These are: two sources that disagree, the permission status of any customer, number or quote you found, whether a number may be published, and the main segment and buyer if no document says. Ask nothing else.
   Step 3: when I have replied, return one combined file in one block, named my-context-pack.md. Give each of the 10 templates its own section, headed with its file name, such as "# company.md", in this order: company, product, icp-and-segments, personas, proof-points, competitors, messaging, brand-voice, goals-and-kpis, channels-and-tools. Keep every heading, every field name and every "Answer:" line. Delete the frontmatter and the "Guidance:" and "Example:" lines. Below the block, list the fields left blank.
   ```

3. Answer the questions. When you do not know something, say "leave it blank".
4. Save it. Copy the finished block. Open the plain text editor that comes with your computer, set it to plain text mode, paste, and save the file as `my-context-pack.md`. If your editor will only save it as .txt, that works too. This file is your master copy, so keep it somewhere you can find it.
5. Check the file yourself. Pay special attention to anything marked publishable and to each proof point's permission status. Use these rules:

   - **A logo already on your website:** treat it as public, for logo use only, and confirm with whoever put it there that it was approved. A logo on your website is not permission for a quote or a number.
   - **You have asked a customer and have no written yes:** mark it "pending".
   - **Everything else:** mark it "none" until you have asked. To ask, run [Request customer proof](../skills/product-marketing-and-sales-enablement/request-customer-proof.md), which writes the email for you.
6. Start a new chat, upload `my-context-pack.md`, and paste this check prompt:

   ```
   Read my-context-pack.md. Each section is one file of my context pack. List each of the 10 sections, and for each one give the blank fields that would block a skill from running. Then list any contradictions between sections. Then list every customer, number and quote with its permission status. Do not fix anything, only report. Do not invent anything.
   ```

7. Fix what it finds in your file and save it. Then go on to [Start here](start-here.md), step 3.

### What you will likely be missing

You will probably finish the chat with gaps, because the answers were never written down. This is normal. Go on with setup, and fill these over the following days and weeks:

| Likely gap | What fills it |
|---|---|
| A quarterly goal | [Propose quarterly goals](../skills/budget-and-planning/propose-quarterly-goals.md), then your CEO decides. See [You have no goals yet](hard-situations.md#you-have-no-goals-yet). |
| An MQL definition sales accepts | [Define the lead handoff](../skills/marketing-ops/define-lead-handoff.md), then your sales lead agrees to it |
| Positioning | [Write a positioning statement](../skills/positioning-and-messaging/write-positioning-statement.md) |
| Brand voice | [Codify the brand voice](../skills/brand-and-design-briefs/codify-brand-voice.md) |
| Dated competitor facts | [Write a competitor profile](../skills/competitive-intelligence/write-competitor-profile.md), with what sales has heard |
| An approvals list | Your CEO. Ask who must approve what, and how long it takes. |

### Go deeper on one file

This is optional, for later, when a skill keeps asking about the same section. Work through the sections in this order, because later ones draw on earlier ones:

| Order | Section | Who usually knows it |
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

1. Start a new chat. Upload `my-context-pack.md`, `context-pack-templates.md` and any source documents for that topic, stripped as in the fast first pass.
2. Paste this prompt, changing the section name:

   ```
   We are improving the company.md section of my-context-pack.md for the Marketing Office, using the matching template in context-pack-templates.md.
   Rules: use only facts from my documents and my answers. Never guess. If you do not know a field, ask me.
   Step 1: fill in every blank field you can from my documents, and name the source of each answer.
   Step 2: ask me about the remaining fields, a few at a time.
   Step 3: when I say "done", give me the whole section as plain markdown in one block, with its heading, every field name and every "Answer:" line. Leave a field blank if I did not answer it.
   ```

3. Answer the questions, then say `done`.
4. Paste the block over that section in `my-context-pack.md` and save it. Upload the new file to your project and delete the old copy.

If you prefer separate files, save each section under its own file name. Skills read them the same way.

## Worked example: filling it in

CogniATion is the sample company, and its facts come from [its example pack](../context-pack/example-cogniation/company.md). The deck, its slide numbers and this exchange are invented to show the steps.

The marketer uploads the templates and an investor deck, with the revenue and funding slides removed, then pastes the prompt. Under Employees, the draft reads:

```
Answer: 38 employees (source: investor deck, slide 2)
```

The number comes from the deck, with its source, and not from the template's "Example:" line, which happens to say the same thing.

Slide 9 shows Haldane Ridge Capital as a customer, and nothing says it agreed to that. So the model asks:

```
1. Slide 9 names Haldane Ridge Capital, with 250 learners. No document says it agreed to be named. What is its permission status?
```

The marketer replies:

```
1. We asked in October 2026 and have no answer yet. Mark it pending.
```

The entry is saved like this:

```
Customer 3
Answer: Haldane Ridge Capital, financial services, 250 learners. Permission: pending, requested October 2026. Do not use. (source: investor deck, slide 9; my answer)
```

From now on, skills leave Haldane Ridge out. Being in a deck is not permission.

## Worked example: a messy first pass

This is CogniATion at an earlier stage, before the approvals in [its example pack](../context-pack/example-cogniation/proof-points.md) had been found or asked for. The deck, its slide numbers, the deck's figures and the marketer's replies are invented to show how a first pass really goes.

The marketer uploads an old deck, website copy and a price list, with the revenue slide removed. The model comes back with this:

```
1. The deck (slide 3) says 41 customer companies. The website says 64. Which is right, and as of what date?
2. The deck (slide 5) calls the product a course. The website calls it critical thinking training software. Which is right?
3. The deck (slide 11) lists $150 per learner per year. The price list says $180. Which is right, and may it be published?
4. I found three customers, four results and two quotes. No document says any of them may be used. What is the status of each?
```

The marketer knows the answers to only some of these:

```
1. 64, as of September 30, 2026. The deck is old.
2. Training software. It is not a course.
3. I do not know. Leave it blank. I will ask Anika Sole, VP product.
4. Brightmere's logo is on our website. We asked Haldane Ridge Capital in October and have no answer. I do not know about the rest.
```

Most of the proof section is saved like this:

```
Customer 1
Answer: Brightmere Advisory, professional services. Permission: public, logo only, on our website. Approval to confirm with Marta Ilves. Not for quotes or numbers. (source: website; my answer)

Customer 2
Answer: Corvane Software, 120 learners. Permission: none. (source: old deck, slide 10)

Quote 1
Answer: "My analysts stopped asking the bot for the answer and started defending their own." Lena Marsh, Brightmere Advisory. Permission: none. (source: old deck, slide 12)
```

The other quote and all four results are saved as "none" too, and Haldane Ridge Capital as "pending". Goals, the MQL definition, brand voice and the approvals list stay blank. The first one-pager from this file has `[customer quote needed]`, `[progress proof needed]` and `[approver needed]` in it.

Those brackets are not a failure. The office did not put an unapproved quote in front of a buyer, and each bracket shows the next person to ask. Anika Sole answers on the price the next day. Lena Marsh's approval takes longer, and until it arrives the marketer works without that quote. The finished example pack is what this file becomes after those conversations, not after one hour in a chat.

## What success looks like

The check prompt returns all 10 sections, a list of blanks you can name a next step for, and no contradictions you have not resolved. After the first pass, that is enough to go on. A stranger reading your pack could brief a campaign only later, once the gaps above are filled.

Skills that rely on your blanks will ask for the missing facts, and that is the office working correctly.

## Troubleshooting

- **The model fills in fields you never gave it.** Say: "Remove every answer that did not come from my documents or my answers." Then check the file yourself before saving it.
- **The reply stops partway through the file.** Say: "Continue from where you stopped, in one block." Paste the rest below what you have.
- **You do not know the permission status of a customer.** Mark it "none" until someone checks, unless it is a logo on your website, as in step 5. Skills will not use a "none" item in public copy.
- **You have no positioning yet.** Leave the messaging section blank for now, and run the skill [Write a positioning statement](../skills/positioning-and-messaging/write-positioning-statement.md) once the first six sections are filled in. Then run [Build a messaging framework](../skills/positioning-and-messaging/build-messaging-framework.md) and paste the result into that section.
- **Your brand voice is not written down.** Run [Codify the brand voice](../skills/brand-and-design-briefs/codify-brand-voice.md) with a few samples of writing you like.
- **Your tool will not take a .md file.** Save the file as .txt and upload that. Or paste the text into the chat.
- **Facts changed.** Edit `my-context-pack.md`, upload it again, and delete the old copy. The guide [Maintain and update](maintain-and-update.md) sets a monthly routine.
