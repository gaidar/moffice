---
title: Set up on Grok
type: guide
version: 0.1.0
updated: 2026-11-01
summary: Set up the Marketing Office as one Grok project on grok.com, with a plain-chat fallback that needs only chat and file upload.
diagram: setup
diagram_caption: "The steps below cover the top path. The plain-chat fallback covers the bottom one."
---

## Who it is for

A marketer with a personal SuperGrok plan, or Premium on The X Subscription, which xAI says includes the benefits of SuperGrok.

No xAI page states which plans include Projects. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq).

## What you need

- A paid Grok plan, as above.
- A computer with a standard Chrome or Chromium browser. xAI recommends this for grok.com.
- The Marketing Office files, from [the Marketing Office repository](https://github.com/gaidar/moffice) on GitHub. Step 1 shows how to get them.
- About 20 minutes (estimate), not counting filling in the context pack.

## Steps

xAI publishes no help page for Projects. Steps 3 to 5 rest on its [release notes](https://grok.com/release-notes), which confirm the features but rarely name the buttons.

1. Get the files from GitHub. Open [the Marketing Office repository](https://github.com/gaidar/moffice), click **Code** above the list of files, then click **Download ZIP**, which is [GitHub's own download](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives). Double-click the downloaded file to open it. You now have a folder of plain-text files.

2. Open grok.com in Chrome or Chromium and sign in. xAI warns that Projects can be missing on other web addresses. Use the computer rather than the phone for this setup, because xAI gives a limit of about 100 files at once on the web and 20 on Android.

3. Go to [grok.com/project](https://grok.com/project) and create a project named `Marketing Office`. xAI's release notes confirm you can create a project from multiple local files and folders at once, so you can select the folders from step 5 here if the screen offers it. The name of the create button is not given. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq).

4. Open the project's config tab, which xAI's notes describe as holding instructions and automations on the project canvas. Open `office/office-manual.md` in a text editor, copy all of it, paste it into the instructions and save.

   The manual is about 7,800 characters. xAI states no limit for project instructions. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq). The grok.com page data sets a custom instructions maximum of 12,000 characters. Inference: this may cover only the account-level setting.

   If the save is rejected or the text gets cut off, paste this short pointer instead, and upload `office/office-manual.md` with the files in step 5:

   ```
   You are the Marketing Office. Before any task, read the file office-manual.md in this project and follow it exactly. The marketer runs work with a skill request or an agent role request, as the manual describes. Use only the project files for facts about the company. Never invent facts. If a file you need is missing, say so and ask for it.
   ```

5. Upload these 74 files to the project, as folders if the screen allows:

   - `context-pack/templates/`: 10 files
   - `skills/`: 50 files, in one subfolder per function
   - `agents/`: 14 files

   xAI's FAQ allows about 100 files at once on the web, accepts Markdown and allows 150 MB per file, so 74 fits. It does not say whether that figure applies to projects, and no page gives a project file limit or names the upload control. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq).

   If Grok rejects 74 files, remove the `skills/` and `agents/` uploads and use 12 files instead: the 10 context pack files, `bundles/all-skills.md` and `bundles/all-agent-roles.md`. Do not upload both sets. Individual files are the first choice because xAI says very long files may be summarized or handled in sections. Inference: the bundles carry more risk of a skill being missed.

   Check that the files appear in the project's file tree. xAI fixed a bug in August 2026 where files uploaded during project creation landed outside the project.

6. Start a new chat inside the project and paste this check prompt:

   ```
   List the context pack files you can see, and say which ones look blank. Then tell me which skill you would use to write a sales one-pager. Do not invent anything.
   ```

   xAI's pages do not describe how project chats read project files, so this check is the real test. Unverified – check the vendor help page: [Grok FAQ](https://docs.x.ai/grok/faq).

7. Confirm the answer lists the 10 context pack files and names the skill "Write a sales one-pager". If it does not, go to Troubleshooting.

8. If the context pack is still blank, follow [Fill the context pack](fill-the-context-pack.md), then upload the filled files to the project. xAI's notes say Grok warns before uploads replace existing files, and replacing the blank files is what you want here.

9. Start work with [Use a skill](use-a-skill.md). Run each task in a new chat inside the project with one of these:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

   ```
   Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
   ```

Optional note on Grok's own Skills feature: xAI says you can create one by uploading a file and that skills work inside Projects, but it does not state the format grok.com accepts, so the project path is the supported one. Unverified – check the vendor help page: [Skills announcement](https://x.ai/news/grok-skills).

## What success looks like

In a chat inside the Marketing Office project, Grok's answer to the check prompt lists company, product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, goals-and-kpis and channels-and-tools. It says which look blank, which is all 10 until you fill them, and it names "Write a sales one-pager".

The project's config tab still shows the office manual or the short pointer, and the file tree shows your uploads.

## Plain-chat fallback

This works with only chat and file upload. It costs a few minutes at the start of each chat (estimate), because Grok gets the office manual and files again each time. Get the files from GitHub first, as in step 1 above.

1. Start a new chat at grok.com, outside any project.

2. Open `office/office-manual.md` in a text editor, copy all of it and paste it into the message box. Do not send yet.

3. Click the + icon next to the message input, or drag and drop on the web, and attach the skill file from `skills/[function]/` and the context pack files listed in its Inputs section. For an agent role, attach its charter from `agents/` and all 10 context pack files. xAI's limits are about 100 files at once on the web and 20 on Android.

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

## Troubleshooting

- **Grok says it cannot find a skill.** Check that the file is in the project's file tree and that the title in your prompt matches exactly. If you uploaded the bundles, upload that skill's own file too, or attach it in the chat.
- **Grok invents a fact.** Check that the office manual or pointer is still saved in the project, and that the context pack file is filled in. Then send: `Where did that fact come from? Name the context pack file. If it is not there, remove it and leave a visible placeholder, as the office manual says.`
- **Projects is missing.** xAI says this happens to some people on grok.x.ai or other web addresses. Use grok.com in a standard Chrome or Chromium browser.
- **File upload rejected: too many files.** Use the 12-file set from step 5. On Android, xAI's limit is 20 files, so switch to the web.
- **File upload rejected: "File type not supported".** xAI's fix is to convert to a supported format such as PDF or TXT, or try a different platform. The Marketing Office files are Markdown, which xAI lists as supported, so first check that you selected the right file.
- **Upload fails or shows "Tap to retry".** xAI's fix is to check the file size and try a smaller version or a different format. xAI also rejects empty files, so check that the file has content.
- **Files landed outside the project.** Upload them again from inside the project and check the file tree.
- **Instructions too long.** Use the short pointer from step 4 and upload `office/office-manual.md` as a file.
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
- Step 4: the character limit for project instructions.
- Step 5: the project file limit and the upload control.
- Step 6: how project chats read project files. These steps were written from documentation and were not run in a live Grok account.
- Optional note after step 9: the file format Grok's Skills feature accepts on grok.com.

These xAI pages refused the fetch with a 403 error, so nothing here relies on them: x.ai/grok, x.ai/pricing, x.ai/grok/use-cases and help.x.com/en/using-x/about-grok.
