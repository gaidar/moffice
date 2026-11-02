---
title: Set up on Grok
type: guide
version: 0.1.0
updated: 2026-11-02
summary: Set up the Marketing Office as one Grok project on grok.com, with a plain-chat fallback that needs only chat and file upload.
diagram: setup
diagram_caption: "The steps below cover the top path. The plain-chat fallback covers the bottom one."
---

## Who it is for

A marketer with a personal SuperGrok plan, or Premium on The X Subscription, which xAI says includes the benefits of SuperGrok.

If you do not see Projects on your plan, use the plain-chat fallback. No xAI page states which plans include Projects. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq).

These steps were written from xAI's FAQ and release notes on the date below, and have not been run in a live account, so if a screen differs, trust xAI's pages.

## What you need

- A paid Grok plan, as above.
- A computer with a standard Chrome or Chromium browser. xAI recommends this for grok.com.
- The two office files. Step 1 links them.
- `my-context-pack.md`, from the [fast first pass](fill-the-context-pack.md#fast-first-pass). Blanks in it are fine.
- About 30 minutes, an estimate, not counting the context pack.

## Steps

xAI publishes no help page for Projects. Steps 3 to 5 rest on its [release notes](https://grok.com/release-notes), which confirm the features but rarely name the buttons.

1. Download the two office files. Click each one, and it saves as a text file: [all-skills.md](https://raw.githubusercontent.com/gaidar/moffice/main/bundles/all-skills.md) and [roles-and-playbooks.md](https://raw.githubusercontent.com/gaidar/moffice/main/bundles/roles-and-playbooks.md). If a link opens the text instead, save that page under the same name. Keep them with `my-context-pack.md`.

2. On a computer, open grok.com in Chrome or Chromium and sign in. Projects can be missing on other web addresses.

3. Go to [grok.com/project](https://grok.com/project) and create a project named `Marketing Office`. The name of the create button is not given, so look for the one that starts a project. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq).

4. Open [the office manual](../office/office-manual.md) and click **Copy text** at the top of the page. Open the project's config tab, which holds instructions and automations on the project canvas. Paste into the instructions and save. If the save is rejected or the text is cut off, see Notes.

5. Upload these 3 files to the project: `my-context-pack.md`, `all-skills.md` and `roles-and-playbooks.md`. Check that they appear in the project's file tree. If the upload is rejected, see Troubleshooting. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq).

6. Start a new chat inside the project and paste this check. xAI's pages do not describe how project chats read project files, so this is the real test. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq).

   ```
   List the context pack sections you can see, and say which have blanks. Then name the skill you would use to write a sales one-pager, and show its Output format section word for word. Do not invent anything.
   ```

   Expected: it lists the 10 sections of your context pack, says which have blanks, and names "Write a sales one-pager". Compare its Output format with [the skill's page](../skills/product-marketing-and-sales-enablement/write-sales-one-pager.md). If it does not match, upload that skill's own file, using **Raw file** on the same page. If it fails, go to Troubleshooting.

7. Ask for your first draft, in plain words, in a new chat in the project. It tells you which skill it used. [Use a skill](use-a-skill.md) covers the rest.

   ```
   Write a sales one-pager for our most important segment, aimed at the person who signs, for one-to-one use by sales.
   ```

   If it picks the wrong skill or ignores your facts, use the exact form, which always works:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

### Notes

- **If the instructions do not fit**, paste this pointer instead, and upload `office-manual.md` with the files in step 5. The manual is about 8,800 characters, and xAI states no limit for project instructions. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq). The grok.com page data sets a custom instructions maximum of 12,000 characters. Inference: this may cover only the account-level setting.

  ```
  You are the Marketing Office. Before any task, read the file office-manual.md in this project and follow it exactly. It says how to handle plain requests, skill requests and agent role requests. Use only the project files for facts about the company. Never invent facts. If a file you need is missing, say so and ask for it.
  ```

- **File limits.** xAI's FAQ allows about 100 files at once on the web and 20 on Android, accepts Markdown and allows 150 MB per file, so 3 fits. It does not say whether that figure applies to projects, and no page gives a project file limit or names the upload control.
- **Creating from files.** xAI's release notes confirm you can create a project from multiple local files at once, so you can select the files from step 5 in step 3 if the screen offers it.
- **File tree.** xAI fixed a bug in August 2026 where files uploaded during project creation landed outside the project.

## What success looks like

In a chat inside the Marketing Office project, Grok's answer to the check lists company, product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, goals-and-kpis and channels-and-tools. It says which have blanks, names "Write a sales one-pager" and returns its Output format as it appears on this site.

The project's config tab still shows the office manual or the short pointer, and the file tree shows your uploads.

## Plain-chat fallback

This works with only chat and file upload. It costs a few minutes at the start of each chat (estimate), because Grok gets the office manual and files again each time.

1. Start a new chat at grok.com, outside any project.

2. Copy [the office manual](../office/office-manual.md) with **Copy text** and paste it into the message box. Do not send yet.

3. Click the + icon next to the message input, or drag and drop on the web, and attach `my-context-pack.md` and the skill file, which you get with **Raw file** on the skill's page. For an agent role, attach its charter in place of the skill file. xAI's limits are about 100 files at once on the web and 20 on Android.

4. Below the office manual in the same message, paste one of these and send:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

   ```
   Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
   ```

5. Save every output you want to keep in your own files. Keep your own copy rather than relying on the chat.

6. When the chat gets long, or Grok starts dropping the template or forgetting rules, send this and save the reply:

   ```
   Summarize this chat for handoff to a new chat: what was decided, which outputs are finished, what is still open, and which files you used. Do not invent anything.
   ```

7. To begin the next chat, repeat steps 1 to 3, attach any saved outputs you still need, paste the saved summary below the office manual, and then paste the run prompt.

### Optional extras

- **Individual files.** xAI says very long files may be summarized or handled in sections. Inference: the combined files carry some risk of a skill being missed. If Grok cannot find a skill, upload that skill's own file. If this keeps happening, get [the repository](https://github.com/gaidar/moffice) with GitHub's **Code** and **Download ZIP** buttons, and upload `skills/` and `agents/` as folders, if the screen allows, in place of the two combined files. Do not upload both sets.
- **Grok's own Skills feature.** xAI says you can create one by uploading a file and that skills work inside Projects, but it does not state the format grok.com accepts, so the project path is the supported one. Unverified – check the vendor help page: [Skills announcement](https://x.ai/news/grok-skills).

## Troubleshooting

- **Grok picks the wrong skill or cannot find one.** Check that `all-skills.md` is in the project's file tree and that the title in your prompt matches exactly. If the model cannot find a skill in the combined file, upload or paste that skill's own file.
- **Grok invents a fact.** Check that the office manual or pointer is still saved in the project, and that the context pack section is filled in. Then send: `Where did that fact come from? Name the context pack section. If it is not there, remove it and leave a visible placeholder, as the office manual says.`
- **Projects is missing.** xAI says this happens to some people on grok.x.ai or other web addresses. Use grok.com in a standard Chrome or Chromium browser.
- **File upload rejected: too many files.** Use the 3 files from step 5. On Android, xAI's limit is 20 files, so switch to the web.
- **File upload rejected: "File type not supported".** xAI's fix is to convert to a supported format such as PDF or TXT, or try a different platform. The Marketing Office files are Markdown, which xAI lists as supported, so first check that you selected the right file.
- **Upload fails or shows "Tap to retry".** xAI's fix is to check the file size and try a smaller version or a different format. xAI also rejects empty files, so check that the file has content.
- **Files landed outside the project.** Upload them again from inside the project and check the file tree.
- **You updated your context pack.** Upload the new `my-context-pack.md` to the project. xAI's notes say Grok warns before uploads replace existing files, and replacing the old file is what you want here.
- **Instructions too long.** Use the pointer in Notes and upload `office-manual.md` as a file.
- **Forgot files in a new chat.** In the plain-chat fallback, attach them and send the run prompt again. In a project, check that you started the chat inside the project and not from the main chat screen.
- **Grok pauses paid features.** Your weekly usage limit has been met. xAI says the pool resets on the schedule shown in the Usage tab in Settings.

## Verification

Verified on 2026-11-01 against vendor documentation.

- [Downloading source code archives](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives): GitHub's Code and Download ZIP steps
- [docs.x.ai/grok/faq](https://docs.x.ai/grok/faq): file counts, 150 MB per file, Markdown support, the + icon, upload error fixes, grok.com for Projects, weekly usage limit
- [grok.com/release-notes](https://grok.com/release-notes): project config tab for instructions (Aug 1, 2026), creating a project from files and folders and the replace warning (Jul 25, 2026), skills inside Projects (May 16, 2026), empty files rejected (May 30, 2026)
- [grok.com/release-notes/aug-15-2026](https://grok.com/release-notes/aug-15-2026): fix for files landing outside a new project
- [grok.com/project](https://grok.com/project): page titled "Projects - Grok"
- [grok.com/plans](https://grok.com/plans): page data with a custom instructions maximum of 12,000 characters, 100 files and 150 MB per file; no plan comparison readable
- [x.ai/news/x-subscription](https://x.ai/news/x-subscription): Premium includes the benefits of SuperGrok, and existing SuperGrok subscribers keep their plan
- [x.ai/news/grok-skills](https://x.ai/news/grok-skills): Skills on grok.com and file upload as one way to create one; no format stated
- [docs.x.ai/grok/overview](https://docs.x.ai/grok/overview): paid SuperGrok plans raise limits; no Projects content
- [docs.x.ai/grok/user-guide](https://docs.x.ai/grok/user-guide): SuperGrok named as a Grok Business license; no Projects steps
- [docs.x.ai/grok/management](https://docs.x.ai/grok/management): projects and skills named in team sharing rules; no setup steps
- [x.ai/news/grok-business](https://x.ai/news/grok-business): Projects named for document search on team plans; no setup steps
- [x.ai/news/grok-automations](https://x.ai/news/grok-automations): no Projects content
- [docs.x.ai/llms.txt](https://docs.x.ai/llms.txt) and [docs.x.ai/sitemap.xml](https://docs.x.ai/sitemap.xml): no help page for Projects or instructions in the /grok/ section

What could not be verified, each one Unverified – check the vendor help page:

- Who it is for: which plans include Projects.
- Step 3: the name of the create button.
- Notes: the character limit for project instructions.
- Notes: the project file limit and the upload control.
- Step 6: how project chats read project files. These steps were written from documentation and were not run in a live Grok account.
- Optional extras: the file format Grok's Skills feature accepts on grok.com.

These xAI pages refused the fetch with a 403 error, so nothing here relies on them: x.ai/grok, x.ai/pricing, x.ai/grok/use-cases and help.x.com/en/using-x/about-grok.
