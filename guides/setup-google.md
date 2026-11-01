---
title: Set up on Google Gemini
type: guide
version: 0.1.0
updated: 2026-11-02
summary: Set up the Marketing Office in one Gemini notebook, with the office manual as its instructions and 3 files as its sources.
diagram: setup
diagram_caption: "The steps below cover the top path. The plain-chat fallback covers the bottom one."
---

## Who it is for

A marketer with a personal Google Account on Google AI Plus, Google AI Pro or Google AI Ultra. Each plan has room in one notebook for the 3 files this guide uses, and for the individual files if you prefer them: up to 100, 300, and 500 or 600 sources respectively.

Google's April 2026 announcement says notebooks in Gemini are not available on Workspace or Education accounts, or to anyone under 18. If that is you, use the plain-chat fallback.

These steps were written from Google's help pages on the date below, and have not been run in a live account, so if a screen differs, trust the help page.

## What you need

- A computer with a browser, signed in at [gemini.google.com](https://gemini.google.com).
- The Marketing Office files, from [the Marketing Office repository](https://github.com/gaidar/moffice) on GitHub. Step 1 shows how to get them.
- `my-context-pack.md`, from the [fast first pass](fill-the-context-pack.md#fast-first-pass). Blanks in it are fine.
- Keep Activity turned on. Without it you can still chat with a notebook, but new chats are not saved to it and Gemini cannot use past chats. See [the notebooks help page](https://support.google.com/gemini/answer/16972047?hl=en&co=GENIE.Platform%3DDesktop).
- About 30 minutes, an estimate, not counting the context pack.

## Steps

1. Get the files from GitHub. Open [the Marketing Office repository](https://github.com/gaidar/moffice), click **Code** above the list of files, then click **Download ZIP**, which is [GitHub's own download](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives). Double-click the downloaded file to open it. You now have a folder of plain-text files.

2. Go to [gemini.google.com](https://gemini.google.com). At the top, click Open sidebar. Under "Notebooks," click New notebook.

   Google is rolling notebooks out gradually, and in the European Economic Area you must connect Gemini Notebook first. To do that, add `@Gemini Notebook` to a prompt asking Gemini to create a notebook, then follow the on-screen instructions. If notebooks still do not appear, use the plain-chat fallback.

3. Name the notebook "Marketing Office".

4. Enter this prompt to start the notebook:

   ```
   This notebook holds the Marketing Office. I am adding its files now. Wait for my next message.
   ```

5. Add the office manual as the notebook's instructions:

   1. Open office/office-manual.md in any text editor and copy all of it.
   2. In Gemini, click Open sidebar. Under "Notebooks," click All notebooks, then click Marketing Office.
   3. At the top, click More, then Notebook settings.
   4. Paste the text and click Save.

   If it does not fit, add office/office-manual.md as a source in step 6, and paste this in Notebook settings instead:

   ```
   You are the Marketing Office. Your rules are in the source named office-manual.md in this notebook. Read that source before every task and follow it exactly. Never invent facts about the company. If something is missing, ask the marketer.
   ```

   The office manual is about 7,800 characters, and Google's pages state no character limit for notebook instructions. Unverified – check the vendor help page ([notebooks in Gemini](https://support.google.com/gemini/answer/16972047?hl=en&co=GENIE.Platform%3DDesktop)).

6. Click Add sources and add these 3 files:

   - my-context-pack.md
   - bundles/all-skills.md
   - bundles/all-agent-roles.md

   If you cannot select several files from your computer at once, add them one at a time. Unverified – check the vendor help page ([add sources](https://support.google.com/gemininotebook/answer/16215270?hl=en&co=GENIE.Platform%3DDesktop)).

7. In the Marketing Office notebook, paste this check prompt:

   ```
   List the context pack sections you can see, and say which have blanks. Then tell me which skill you would use to write a sales one-pager. Do not invent anything.
   ```

   The expected answer lists the 10 sections of your context pack, says which have blanks, and names the skill "Write a sales one-pager".

   Then check that it can use a skill from the combined file, with this second check:

   ```
   Show me the Output format section of the skill "Write a sales one-pager", word for word.
   ```

   Compare the answer with [the skill's page on this site](../skills/product-marketing-and-sales-enablement/write-sales-one-pager.md). If it does not match, upload or paste that skill's own file, `skills/product-marketing-and-sales-enablement/write-sales-one-pager.md`.

8. Run your first skill with [Use a skill](use-a-skill.md).

Use this notebook, not Gems. On personal accounts, Gems become read-only on November 17, 2026, and are removed on December 17, 2026.

## What success looks like

"Marketing Office" appears under "Notebooks" in the Gemini sidebar. The check prompt returns these 10 sections: company, product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, goals-and-kpis and channels-and-tools. It says which have blanks, then names the skill "Write a sales one-pager". The second check returns the skill's Output format as it appears on this site.

To run work, open the notebook and paste one of these prompts:

```
Use the skill "<title>". Read the context pack. Task: <what they want>.
```

```
Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
```

## Plain-chat fallback

This works with chat and file upload only. It costs a few minutes at the start of each chat, because Gemini does not keep the setup for you.

1. Go to [gemini.google.com](https://gemini.google.com) and start a new chat.

2. Open office/office-manual.md, copy all of it, and paste it as your first message. Add this line at the end, then send:

   ```
   These are your rules for this chat. Reply only with "Ready".
   ```

3. In the text box, click Add files, then Upload Files. Add my-context-pack.md and the skill file. For an agent role, add its charter from agents/ instead of the skill file.

   Google allows up to 10 files in the same prompt, subject to availability. If you need more, send the rest in a second message. That second message is an inference from the per-prompt limit, not a documented method.

   Google's upload page says "most file types" and does not list markdown. If a file is rejected, open it and paste its text into the chat. Whether .md files upload in chat: Unverified – check the vendor help page ([upload files](https://support.google.com/gemini/answer/14903178?hl=en&co=GENIE.Platform%3DDesktop)).

4. Paste one of the run prompts with your task filled in, then send:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

   ```
   Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
   ```

5. Save every output you keep in your own files. Do not rely on finding it in the chat later.

6. When the chat gets long, or Gemini starts to miss details or forget earlier decisions, send this and save the reply:

   ```
   Write a handoff note for my next chat: the task, the decisions made, the facts I gave you, the open questions and the current draft. Do not invent anything.
   ```

7. To begin the next chat, repeat steps 1 to 3. Then paste your saved handoff note and continue with the run prompt.

### Optional extras

- **Individual files.** In place of the two bundles, add the files in the function folders under skills/ and the files in agents/. They all fit within the source limit of every paid plan.
- **Gemini's own skills feature.** The notebook path is the supported one, because uploading to that feature needs each skill repackaged around a file named SKILL.md in a folder with a lowercase, hyphenated name.

## Troubleshooting

- **The model says it cannot find a skill.** Check the title against the skill's file. Google says naming a source in your question helps narrow the search, so add all-skills.md to your prompt. If the model cannot find a skill in the combined file, upload or paste that skill's own file.
- **The model invents a fact.** Say: "Use only the context pack. Mark anything missing as Unknown." Then add the fact to the right section of my-context-pack.md and replace that source. Notebook chats in Gemini can use web search and other tools, so ask for a citation on any outside claim.
- **File upload is rejected.** Check that you chose a .md file. Notebook sources can be up to 500,000 words or 200 MB each, and markdown is a listed source type. If you hit the source limit, go back to the 3 files in step 6. Without a paid plan, the limit is 50 sources.
- **"You've reached your limit for chats with files."** This is a rolling limit in chat. Wait for it to reset, or use the notebook.
- **"Delete data to upload file."** Gemini's own storage is full. Click Settings & help, then Activity, and delete Gemini activity you no longer need.
- **Instructions are too long.** Use the short text and the office-manual.md source from step 5.
- **You forgot files in a new chat.** In a notebook, sources stay in place, so confirm you opened Marketing Office. In the plain-chat fallback, upload them again.
- **The notebook forgets past chats.** Turn on Keep Activity. Without it, Gemini cannot use past chats in a notebook.
- **Notebooks do not appear in the sidebar.** The feature is rolling out gradually. Try the connection in step 2, then use the plain-chat fallback.
- **You deleted the notebook.** Its sources and added chats are deleted too. Create it again from step 2 and upload your 3 files.

## Verification

Verified on 2026-11-01 against vendor documentation.

- [Downloading source code archives](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives): GitHub's Code and Download ZIP steps
- [Notebooks in Gemini Apps](https://support.google.com/gemini/answer/16972047?hl=en&co=GENIE.Platform%3DDesktop): notebook creation, instructions path, Keep Activity, connection step, rollout, web search in chats
- [Add sources](https://support.google.com/gemininotebook/answer/16215270?hl=en&co=GENIE.Platform%3DDesktop): markdown as a source type, per-source limits, free source limit, naming sources in questions
- [Gemini Notebook plans](https://support.google.com/gemininotebook/answer/16213268?hl=en): sources per notebook on each plan
- [Notebooks in Gemini Apps, Gemini Notebook Help](https://support.google.com/gemininotebook/answer/17003757): syncing and one set of custom instructions across both apps
- [Gemini Notebook FAQ](https://support.google.com/gemininotebook/answer/16269187?hl=en): per-source limit
- [Use chat in Gemini Notebook](https://support.google.com/gemininotebook/answer/16179559?hl=en): no instruction character limit stated
- [Create a notebook in Gemini Notebook](https://support.google.com/gemininotebook/answer/16206563?hl=en): no instruction character limit stated
- [Usage limits in Gemini Notebook](https://support.google.com/gemininotebook/answer/17670842?hl=en): compute-based usage limits
- [Upload and analyze files](https://support.google.com/gemini/answer/14903178?hl=en&co=GENIE.Platform%3DDesktop): Add files path, 10-file limit, error messages
- [Gemini Apps limits](https://support.google.com/gemini/answer/16275805?hl=en): plan tiers and context windows
- [Create and manage skills](https://support.google.com/gemini/answer/17094296?hl=en&co=GENIE.Platform%3DDesktop): SKILL.md upload requirements
- [Transition from Gems to skills](https://support.google.com/gemini/answer/18560919?hl=en): Gems dates and skills limits
- [Use Gems](https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop): notice that Gems are going away
- [How to use Gems](https://support.google.com/gemini/answer/15236405): what Gems are
- [Personal instructions](https://support.google.com/gemini/answer/16598625?hl=en&co=GENIE.Platform%3DDesktop): account-wide instructions, not used in this setup
- [Google AI plans](https://one.google.com/about/google-ai-plans/): plan names Plus, Pro and Ultra
- [Notebooks announcement](https://blog.google/innovation-and-ai/products/gemini-app/notebooks-gemini-notebooklm/): April 2026 account and age exclusions
- [Flexible usage limits post](https://blog.google/innovation-and-ai/products/gemini-notebook/new-flexible-usage-limits/): limits changed from September 2026, no source count stated
- [Custom chat post](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/): no instruction character limit stated

What could not be verified:

- Steps, step 5: the character limit for notebook instructions.
- Steps, step 6: whether several local files can be selected at once.
- Plain-chat fallback, step 3: whether .md files upload in chat, and whether a second message gets around the 10-file limit.
