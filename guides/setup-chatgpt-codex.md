---
title: Set up on ChatGPT and Codex
type: guide
version: 0.1.0
updated: 2026-11-01
summary: Set up the Marketing Office in a ChatGPT project on Plus or Pro, with an optional note on Codex and a plain-chat fallback.
diagram: setup
diagram_caption: "The steps below cover the top path. The plain-chat fallback covers the bottom one."
---

## Who it is for

A marketer with a personal ChatGPT Plus or Pro subscription. Both plans include projects: Plus allows 25 files per project, Pro allows 40.

## What you need

- A ChatGPT Plus or Pro subscription and a browser.
- The Marketing Office files, from [the Marketing Office repository](https://github.com/gaidar/moffice) on GitHub. Step 1 shows how to get them.
- Time: about 15 minutes (estimate), not counting filling in the context pack.

## Steps

1. Get the files from GitHub. Open [the Marketing Office repository](https://github.com/gaidar/moffice), click **Code** above the list of files, then click **Download ZIP**, which is [GitHub's own download](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives). Double-click the downloaded file to open it. You now have a folder of plain-text files.

2. In ChatGPT, select **New project** in the sidebar. Name it `Marketing Office`, then pick an icon and color. If you are offered project-only memory, choose it, because it keeps memories saved from your other work out of this project. You can change this later under **Project settings**, in **Memory**. See [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt).

3. Open `office/office-manual.md` in a text editor and copy all of it. In the project, open the more options menu (•••), select **Project settings**, paste the text as the project instructions, and save. Then reopen the settings and check that the last line, which starts "When the marketer asks", is still there.

   The manual is about 7,800 characters. The limit for project instructions: Unverified – check the vendor help page, [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt). Do not use your account-wide custom instructions for this, because [they stop at 5,000 characters](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions) on Plus and Pro.

4. If the manual does not fit or gets cut off, replace it with this short pointer, and upload `office/office-manual.md` as a file in step 5.

   ```
   You are the Marketing Office. Before answering any request, read the project file office-manual.md and follow it exactly. It sets the rule on facts, the assumption labels, the output format, and how to run skills and agent roles. The context pack files are your only source of facts about the company. Find skills in all-skills.md and agent role charters in all-agent-roles.md. If you cannot read office-manual.md, say so and stop. Do not improvise a version of it.
   ```

5. Upload these 12 files to the project's sources:
   - the 10 files in `context-pack/templates/`
   - `bundles/all-skills.md`
   - `bundles/all-agent-roles.md`

   Use the bundles on both plans. The 74 individual files do not fit under the limit of 25 on Plus or 40 on Pro, and 12 files do, or 13 with the manual. OpenAI's project page says only 10 files can be uploaded at the same time, so upload in two batches.

   Whether project uploads accept `.md` files: Unverified – check the vendor help page, [Uploading files and audio to ChatGPT](https://help.openai.com/en/articles/8555545-file-uploads-faq). If they are rejected, see Troubleshooting.

6. Start a new chat inside the project and paste this check prompt.

   ```
   List the context pack files you can see, and say which ones look blank. Then tell me which skill you would use to write a sales one-pager. Do not invent anything.
   ```

   Expected answer: it lists the 10 context pack files and names the skill "Write a sales one-pager".

7. If you have not filled the context pack yet, follow [Fill the context pack](fill-the-context-pack.md). Then, in the project's sources list, delete each blank file and upload the filled version.

8. Go to [Use a skill](use-a-skill.md). All your work runs from these two prompts, typed as plain messages in a chat inside the project.

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

   ```
   Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
   ```

### Optional: what Codex offers

Most marketers can skip Codex. OpenAI describes it as the option for software development and technical work, though [its guide](https://learn.chatgpt.com/docs/use-chatgpt) adds that it can be used for research, documents, presentations and other knowledge work if you prefer it. It is included with Plus and Pro.

What it adds is folder access. Codex is a separate view in the [ChatGPT desktop app](https://learn.chatgpt.com/docs/quickstart), with its own chat history, and it is not selectable on the web or mobile. You choose **Codex** from the ChatGPT dropdown and open a folder. If that folder is your Marketing Office folder, all 74 files should be readable without the bundles. Inference: the pages describe folder access but do not mention this use, and it was not tested. Unverified – check the vendor help page, [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex).

The cost is that it can read and change files in that folder, so keep a clean copy, or get the files from GitHub again. Your ChatGPT project does not carry over automatically (assumption, because the histories are separate), so begin with this message.

```
Read office/office-manual.md in this folder and follow it for this whole chat. The context pack is in context-pack/templates/. Skills are in skills/ and agent role charters are in agents/.
```

If you want a finished file such as a deck or a report, try ChatGPT Work before Codex. OpenAI points to it for [reviewable results](https://learn.chatgpt.com/docs/use-chatgpt), and you can start it from inside your project so it uses the project's context. Work and Codex [share the same usage limits](https://learn.chatgpt.com/docs/pricing), so check your usage before a large task.

### Optional: ChatGPT's own Skills feature

The project path is the supported one: OpenAI's help article lists [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt) for Business, Enterprise, Healthcare and Edu users, not Plus or Pro, and [each skill must be a folder](https://learn.chatgpt.com/docs/build-skills) with its own `SKILL.md` file, so the Marketing Office files would need repackaging.

## What success looks like

The sidebar shows a project called Marketing Office, with the office manual or the pointer in its instructions and at least 12 files in its sources. A new chat in that project answers the check prompt by listing brand-voice, channels-and-tools, company, competitors, goals-and-kpis, icp-and-segments, messaging, personas, product and proof-points, says which look blank, and names the skill "Write a sales one-pager". It adds no company facts of its own.

## Plain-chat fallback

Use this if you do not want a project, or a project gives you trouble. It needs only chat and file upload, and it costs a few minutes at the start of each chat. Get the files from GitHub first, as in step 1 above.

1. Start a new chat in ChatGPT, outside any project.

2. Open `office/office-manual.md` in a text editor, copy all of it, and paste it as your first message. If the message is too long to send, upload the file instead and write this.

   ```
   Read this file and follow it for this whole chat.
   ```

3. Upload the context pack files you need and the skill file from `skills/[function]/`. The skill's Inputs section names the context pack files it reads. For an agent role, upload its charter from `agents/`.

4. Paste the run prompt, filling in the details.

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

   ```
   Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
   ```

5. Save every output yourself, in your own files. Do not rely on finding it in the chat later.

6. When the chat gets long, or the answers start to ignore the manual or the output format, stop and paste this, then save the reply.

   ```
   Write a handoff note for a new chat: decisions made, facts I confirmed, open questions, and the current state of each draft. Do not invent anything.
   ```

7. To begin the next chat, repeat steps 1 to 3, paste the handoff note, and continue.

## Troubleshooting

- **The model says it cannot find a skill.** Check that `all-skills.md` is in the project's sources and that the chat is inside the project. Use the skill's exact title. If it still fails, upload the single file from `skills/[function]/` to the chat.
- **The model talks about ChatGPT's own Skills feature or asks you to install something.** Tell it that the skill is a section of the project file `all-skills.md`. You do not need an @ mention.
- **The model invents a fact.** Ask which context pack file states it. If none does, add the real fact to that file and upload it again, or tell the model to use a visible placeholder.
- **A file upload is rejected.** If it is the file type, rename the file so it ends in `.txt` instead of `.md`, since OpenAI's upload article lists TXT. If you are over the file limit, delete files until you are at 25 on Plus or 40 on Pro. OpenAI also lists a rate limit of 80 files every 3 hours, so wait and retry if you hit it.
- **The instructions are too long or get cut off.** Use the pointer in step 4 and upload the manual as a file.
- **The check prompt lists fewer than 10 files.** Upload the missing files again. Project files stay across the project's chats, so also check that you are not in a chat outside the project.
- **You forgot files in a new chat.** In a project, start the chat inside the project and the files come with it. In the plain-chat fallback, upload them again.
- **Answers still treat the context pack as blank after you filled it.** The blank versions are probably still there. Delete them from the sources list, upload the filled files, and start a new chat.
- **You do not see the project-only memory option.** Skip it. OpenAI says availability depends on your plan.

## Verification

Verified on 2026-11-01 against vendor documentation.

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

- [Projects in ChatGPT](https://help.openai.com/en/articles/10169521-projects-in-chatgpt): plan availability, 25 and 40 file limits, 10 uploads at a time, **New project**, **Project settings**, **Memory**, deleting from the sources list.
- [Uploading files and audio to ChatGPT](https://help.openai.com/en/articles/8555545-file-uploads-faq): per-project limits, TXT listed, 80 files every 3 hours.
- [ChatGPT custom instructions](https://help.openai.com/en/articles/8096356-chatgpt-custom-instructions): 5,000 characters on Plus and Pro, for account-wide instructions only.
- [Data analysis with ChatGPT](https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt): `.md` named for data analysis.
- [Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt): eligible plans.
- [ChatGPT Work and Codex](https://help.openai.com/en/articles/20001275-chatgpt-work-and-codex): Codex is separate, for technical work, desktop only, included with Plus and Pro, Work from a project.

What could not be verified:

- Step 3: the character limit for project instructions. No page found states one.
- Step 5: whether project uploads accept `.md` files, and the name of the upload button.
- Optional Codex note: reading all 74 files from the folder is an inference and was not tested. OpenAI's pages also conflict on where Codex runs: the help article says it is not selectable on the web or mobile, while the pricing page lists Codex on the web and iOS for Plus.
- Steps 2, 3, 5 and 7: every help.openai.com detail comes from search excerpts, not a full page read. One older version of the upload FAQ gives Plus 20 files per project. The 13 files in this guide fit either way.
