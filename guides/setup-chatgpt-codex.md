---
title: Set up on ChatGPT and Codex
type: guide
version: 0.1.0
updated: 2026-11-02
summary: Set up the Marketing Office in a ChatGPT project on Plus or Pro, with an optional note on Codex and a plain-chat fallback.
diagram: setup
diagram_caption: "The steps below cover the top path. The plain-chat fallback covers the bottom one."
---

## Who it is for

A marketer with a personal ChatGPT Plus or Pro subscription. Both plans include projects: Plus allows 25 files per project, Pro allows 40.

**Last checked against documentation:** 2026-11-01. **Last tested in a live account:** not yet. If a screen differs, trust the help page.

## What you need

- A decision on your data settings. OpenAI says data sharing is on by default in personal Free, Plus and Pro workspaces. To turn it off, go to Settings, then Data controls: [Data controls in ChatGPT](https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt). Do this before you upload company facts, and never upload what the context pack guide tells you to strip.
- A ChatGPT Plus or Pro subscription and a browser.
- The two office files. Step 1 links them.
- `my-context-pack.md`, from the [fast first pass](fill-the-context-pack.md#fast-first-pass). Blanks in it are fine.
- Time: about 30 minutes, an estimate, not counting the context pack.

## Steps

1. Download the two office files. Click each one, and it saves as a text file: [all-skills.md](https://raw.githubusercontent.com/gaidar/moffice/v0.1.0/bundles/all-skills.md) and [roles-and-playbooks.md](https://raw.githubusercontent.com/gaidar/moffice/v0.1.0/bundles/roles-and-playbooks.md). If a link opens the text instead, save that page under the same name. Keep them with `my-context-pack.md`.

2. In ChatGPT, select **New project** in the sidebar and name it `Marketing Office`. If you are offered project-only memory, choose it, because it keeps memories from your other work out of this project. See [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

3. Open [the office manual](../office/office-manual.md) and click **Copy full text** at the top of the page. In the project, open the more options menu (•••), select **Project settings**, paste the text as the project instructions and save. Reopen the settings and check that the last line, which starts "When the marketer asks", is still there. If it was cut off, see Notes.

4. Upload these 3 files to the project's sources: `my-context-pack.md`, `all-skills.md` and `roles-and-playbooks.md`. If a file is rejected, rename it to end in `.txt`. Unverified – check the vendor help page: [Uploading files and audio to ChatGPT](https://help.openai.com/en/articles/8555545-file-uploads-faq).

5. Start a new chat inside the project and paste this check:

   ```
   List the context pack sections you can see, and say which have blanks. Then name the skill you would use to write a sales one-pager, and show its Output format section word for word. Do not invent anything.
   ```

   Expected: it lists the 10 sections of your context pack, says which have blanks, and names "Write a sales one-pager". Compare its Output format with [the skill's page](../skills/product-marketing-and-sales-enablement/write-sales-one-pager.md). If it does not match, upload that skill's own file, using **Download file** on the same page.

6. Ask for your first draft, in plain words, in a new chat in the project. It tells you which skill it used. [Use a skill](use-a-skill.md) covers the rest.

   ```
   Write a sales one-pager for our most important segment, aimed at the person who signs, for one-to-one use by sales.
   ```

   If it picks the wrong skill or ignores your facts, use the exact form:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

### Notes

- **If the instructions are cut off**, paste this pointer instead, and upload `office-manual.md` as a file. The manual is about 8,800 characters. The limit for project instructions: Unverified – check the vendor help page: [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt). Do not use your account-wide custom instructions for this, because [they stop at 5,000 characters](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions) on Plus and Pro.

  ```
  You are the Marketing Office. Before answering any request, read the project file office-manual.md and follow it exactly. It sets the rule on facts, the assumption labels, the output format, and how to run skills and agent roles. The file my-context-pack.md is your only source of facts about the company. Find skills in all-skills.md, and agent role charters and playbooks in roles-and-playbooks.md. If you cannot read office-manual.md, say so and stop. Do not improvise a version of it.
  ```

- **Why combined files.** The individual files do not fit under the limit of 25 on Plus or 40 on Pro, and 3 files do, or 4 with the manual. OpenAI's project page says only 10 files can be uploaded at the same time, so one batch is enough.
- **Memory.** You can change the memory choice later under **Project settings**, in **Memory**.

## What success looks like

The sidebar shows a project called Marketing Office, with the office manual or the pointer in its instructions and your 3 files in its sources. A new chat in that project answers the check by listing brand-voice, channels-and-tools, company, competitors, goals-and-kpis, icp-and-segments, messaging, personas, product and proof-points, says which have blanks, and names the skill "Write a sales one-pager", with its Output format as it appears on this site. It adds no company facts of its own.

## Plain-chat fallback

Use this if you do not want a project, or a project gives you trouble. It needs only chat and file upload, and it costs a few minutes at the start of each chat.

1. Start a new chat in ChatGPT, outside any project.

2. Copy [the office manual](../office/office-manual.md) with **Copy full text**, and paste it as your first message. If the message is too long to send, upload the file instead and write this.

   ```
   Read this file and follow it for this whole chat.
   ```

3. Upload `my-context-pack.md` and the skill file, which you get with **Download file** on the skill's page. For an agent role, do the same from its charter page.

4. Paste the run prompt, filling in the details.

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

   ```
   Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
   ```

5. Save every output yourself, in your own files. Do not rely on finding it in the chat later.

6. When the chat gets long, or the answers start to ignore the manual or the output format, stop and paste this. Save the reply in [your workboard](../office/my-workboard.md).

   ```
   Close my session
   ```

7. To begin the next chat, repeat steps 1 to 3, paste your workboard, then write `Start my session`.

### Optional extras

- **Codex.** Most marketers can skip Codex: OpenAI describes it as the option for [software development and technical work](https://learn.chatgpt.com/docs/use-chatgpt), and it is a separate view in the [ChatGPT desktop app](https://learn.chatgpt.com/docs/quickstart), included with Plus and Pro.
- **ChatGPT Work.** If you want a finished file such as a deck or a report, OpenAI points to ChatGPT Work for [reviewable results](https://learn.chatgpt.com/docs/use-chatgpt). OpenAI's [Projects page](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) says Work is not available in a project that uses project-only memory. To use Work, make a second project with default memory, give it the same instructions and files, and start Work from inside it. Default memory can draw on your other work, so check facts against your context pack. Work and Codex [share the same usage limits](https://learn.chatgpt.com/docs/pricing), so check your usage before a large task.
- **ChatGPT's own Skills feature.** The project path is the supported one: OpenAI's help article lists [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) for Business, Enterprise, Healthcare and Edu users, not Plus or Pro, and [each skill must be a folder](https://learn.chatgpt.com/docs/build-skills) with its own `SKILL.md` file, so the Marketing Office files would need repackaging.

## Troubleshooting

- **The model picks the wrong skill or cannot find one.** Check that `all-skills.md` is in the project's sources and that the chat is inside the project. Use the skill's exact title. If the model cannot find a skill in the combined file, upload or paste that skill's own file from `skills/[function]/`.
- **The model talks about ChatGPT's own Skills feature or asks you to install something.** Tell it that the skill is a section of the project file `all-skills.md`. You do not need an @ mention.
- **The model invents a fact.** Ask which context pack section states it. If none does, add the real fact to that section of `my-context-pack.md` and upload it again, or tell the model to use a visible placeholder.
- **A file upload is rejected.** If it is the file type, rename the file so it ends in `.txt` instead of `.md`, since OpenAI's upload article lists TXT. If you are over the file limit, delete files until you are at 25 on Plus or 40 on Pro. OpenAI also lists a rate limit of 80 files every 3 hours, so wait and retry if you hit it.
- **The instructions are too long or get cut off.** Use the pointer in Notes and upload the manual as a file.
- **The check lists fewer than 10 sections.** Check that `my-context-pack.md` holds all 10 and upload it again. Project files stay across the project's chats, so also check that you are not in a chat outside the project.
- **You forgot files in a new chat.** In a project, start the chat inside the project and the files come with it. In the plain-chat fallback, upload them again.
- **You updated your context pack.** In the project's sources list, delete the old `my-context-pack.md`, upload the new one, and start a new chat.
- **You do not see the project-only memory option.** Skip it. OpenAI says availability depends on your plan.

## Verification

Verified on 2026-11-01 against vendor documentation. Not yet tested in a live account. The data settings note was checked on 2026-11-02 from search excerpts of the linked page.

- [Downloading source code archives](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives): GitHub's Code and Download ZIP steps
Fetched directly. The developers.openai.com pages for these topics redirect to learn.chatgpt.com.

- [Quickstart](https://learn.chatgpt.com/docs/quickstart): desktop and web setup, no terminal, the ChatGPT dropdown and Codex choice, folders.
- [ChatGPT desktop app](https://learn.chatgpt.com/docs/app): starting a chat, project or folder.
- [Projects and chats](https://learn.chatgpt.com/docs/projects): project instructions apply across chats, Sources, folder access can read and change files.
- [Use ChatGPT](https://learn.chatgpt.com/docs/use-chatgpt): what Chat, Work and Codex are for, and Codex for knowledge work.
- [Get started with Work](https://learn.chatgpt.com/docs/get-started-with-work): Work and finished files.
- [Work with files](https://learn.chatgpt.com/docs/artifacts-viewer): file previews in the desktop app.
- [Skills and plugins](https://learn.chatgpt.com/docs/skills-and-plugins): what a skill is, @ mentions.
- [Build skills](https://learn.chatgpt.com/docs/build-skills): folder layout, required `SKILL.md` name and description.
- [Pricing](https://learn.chatgpt.com/docs/pricing): Work and Codex on Plus and Pro, shared usage limits.
- [Documentation index](https://learn.chatgpt.com/docs): where the topic pages are.

Read only as excerpts in search results, because direct fetches of help.openai.com and openai.com returned an access error.

- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt): plan availability, 25 and 40 file limits, 10 uploads at a time, **New project**, **Project settings**, **Memory**, deleting from the sources list, Work unavailable with project-only memory (checked 2026-11-02).
- [Uploading files and audio to ChatGPT](https://help.openai.com/en/articles/8555545-file-uploads-faq): per-project limits, TXT listed, 80 files every 3 hours.
- [ChatGPT custom instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions): 5,000 characters on Plus and Pro, for account-wide instructions only.
- [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt): `.md` named for data analysis.
- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt): eligible plans.
- [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex): Codex is separate, for technical work, included with Plus and Pro, Work from a project.
- [Using Codex Cloud](https://help.openai.com/en/articles/20001545-using-codex-cloud): the Codex view is in the desktop app, and cloud tasks can run from the web and mobile (checked 2026-11-02).

What could not be verified:

- Notes: the character limit for project instructions. No page found states one.
- Step 4: whether project uploads accept `.md` files, and the name of the upload button.
- Steps 2, 3 and 4, and Troubleshooting, "You updated your context pack": every help.openai.com detail comes from search excerpts, not a full page read. One older version of the upload FAQ gives Plus 20 files per project. The 4 files in this guide fit either way.
