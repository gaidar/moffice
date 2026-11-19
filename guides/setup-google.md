---
title: Set up on Google Gemini
type: guide
version: 0.1.0
updated: 2026-11-19
summary: Set up the Marketing Office in one Gemini notebook, with the office manual as its instructions and 3 files as its sources.
diagram: setup
diagram_caption: "The steps below cover the top path. The plain-chat fallback covers the bottom one."
---

## Who it is for

A marketer with a personal Google Account on Google AI Plus, Google AI Pro or Google AI Ultra. Each plan has room in one notebook for the 3 files this guide uses, and for the individual files if you prefer them: up to 100, 300, and 500 or 600 sources respectively.

On a Workspace or Education account, notebooks depend on your admin, who must turn on both Gemini and Gemini Notebook. Google's post for these accounts says a notebook takes up to 10 sources, enough for the 3 files. On a personal account, Google's April 2026 announcement excludes anyone under 18. If either stops you, use the plain-chat fallback.

**Last checked against documentation:** 2026-11-19. **Last tested in a live account:** not yet. If a screen differs, trust the help page.

## What you need

- A decision on your data settings. Model training now has its own box, under Settings, then History. If you clear the box for chat content and click Turn off, Google says your future chats are not used to train generative AI models, unless you send feedback. It says it still reviews chats and uses them to respond, to improve its services in other ways and to protect its users, including with human reviewers. See the [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en) and [manage your history](https://support.google.com/gemini/answer/13278892?hl=en&co=GENIE.Platform%3DDesktop). Google also says files you add to a notebook are not used directly to train its foundational models, unless you send feedback, while notebook chats in Gemini follow the settings above ([notebooks in Gemini Apps](https://support.google.com/gemininotebook/answer/17003757)). Make this choice before you upload company facts, and never upload what the context pack guide tells you to strip.
- A computer with a browser, signed in at [gemini.google.com](https://gemini.google.com).
- The two office files. Step 1 links them.
- `my-context-pack.md`, from the [fast first pass](fill-the-context-pack.md#fast-first-pass). Blanks in it are fine.
- History turned on. Some Google pages still call it Keep Activity. Without it you can still chat with a notebook, but new chats are not saved to it and Gemini cannot use past chats. You can keep History on and still clear the training box. See [the notebooks help page](https://support.google.com/gemini/answer/16972047?hl=en&co=GENIE.Platform%3DDesktop).
- About 30 minutes, an estimate, not counting the context pack.

## Steps

1. Download the two office files. Click each one, and it saves as a text file: [all-skills.md](https://raw.githubusercontent.com/gaidar/moffice/v0.1.0/bundles/all-skills.md) and [roles-and-playbooks.md](https://raw.githubusercontent.com/gaidar/moffice/v0.1.0/bundles/roles-and-playbooks.md). If a link opens the text instead, save that page under the same name. Keep them with `my-context-pack.md`.

2. Go to [gemini.google.com](https://gemini.google.com). At the top, click Open sidebar. Under "Notebooks," click New notebook, and name it "Marketing Office". If notebooks do not appear, see Notes.

3. Enter this prompt to start the notebook:

   ```
   This notebook holds the Marketing Office. I am adding its files now. Wait for my next message.
   ```

4. Open [the office manual](../office/office-manual.md) and click **Copy full text** at the top of the page. In Gemini, click Open sidebar, then under "Notebooks," All notebooks, then Marketing Office. At the top, click More, then Notebook settings. Paste and click Save. If it does not fit, see Notes.

5. Click Add sources and add these 3 files: my-context-pack.md, all-skills.md and roles-and-playbooks.md. If you cannot select several at once, add them one at a time. Unverified – check the vendor help page ([add sources](https://support.google.com/gemininotebook/answer/16215270?hl=en&co=GENIE.Platform%3DDesktop)).

6. In the notebook, paste this check:

   ```
   List the context pack sections you can see, and say which have blanks. Then name the skill you would use to write a sales one-pager, and show its Output format section word for word. Do not invent anything.
   ```

   Expected: it lists the 10 sections of your context pack, says which have blanks, and names "Write a sales one-pager". Compare its Output format with [the skill's page](../skills/product-marketing-and-sales-enablement/write-sales-one-pager.md). If it does not match, upload that skill's own file, using **Download file** on the same page.

7. Ask for your first draft, in plain words, in a new chat in the notebook. It tells you which skill it used. [Use a skill](use-a-skill.md) covers the rest.

   ```
   Write a sales one-pager for our most important segment, aimed at the person who signs, for one-to-one use by sales.
   ```

   If it picks the wrong skill or ignores your facts, use the exact form:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

### Notes

- **If notebooks do not appear.** Google is rolling them out gradually, and in the European Economic Area you must connect Gemini Notebook first. To do that, add `@Gemini Notebook` to a prompt asking Gemini to create a notebook, then follow the on-screen instructions. If they still do not appear, use the plain-chat fallback.
- **If the instructions do not fit**, add office-manual.md as a source in step 5, and paste this in Notebook settings instead. The office manual is about 8,800 characters, and Google's pages state no character limit for notebook instructions. Unverified – check the vendor help page ([notebooks in Gemini](https://support.google.com/gemini/answer/16972047?hl=en&co=GENIE.Platform%3DDesktop)).

  ```
  You are the Marketing Office. Your rules are in the source named office-manual.md in this notebook. Read that source before every task and follow it exactly. Never invent facts about the company. If something is missing, ask the marketer.
  ```

- **Use this notebook, not Gems.** On personal accounts for users 18 and over, Gems became read-only on November 17, 2026, and will be removed on December 17, 2026.

## What success looks like

"Marketing Office" appears under "Notebooks" in the Gemini sidebar. The check returns these 10 sections: company, product, icp-and-segments, personas, messaging, competitors, proof-points, brand-voice, goals-and-kpis and channels-and-tools. It says which have blanks, names the skill "Write a sales one-pager" and returns its Output format as it appears on this site.

## Plain-chat fallback

This works with chat and file upload only. It costs a few minutes at the start of each chat, because Gemini does not keep the setup for you.

1. Go to [gemini.google.com](https://gemini.google.com) and start a new chat.

2. Copy [the office manual](../office/office-manual.md) with **Copy full text**, and paste it as your first message. Add this line at the end, then send:

   ```
   These are your rules for this chat. Reply only with "Ready".
   ```

3. In the text box, click Add files, then Upload Files. Add my-context-pack.md and the skill file, which you get with **Download file** on the skill's page. For an agent role, add its charter instead.

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

6. When the chat gets long, or Gemini starts to miss details or forget earlier decisions, send this and save the reply in [your workboard](../office/my-workboard.md):

   ```
   Close my session
   ```

7. To begin the next chat, repeat steps 1 to 3. Then paste your workboard and write `Start my session`.

### Optional extras

- **Individual files.** In place of the two combined files, get [the repository](https://github.com/gaidar/moffice) with GitHub's **Code** and **Download ZIP** buttons, and add the files in the function folders under skills/ and the files in agents/. They all fit within the source limit of every paid plan.
- **Gemini's own skills feature.** The notebook path is the supported one, because uploading to that feature needs each skill repackaged as a SKILL.md file whose skill name is lowercase and hyphenated.

## Troubleshooting

- **The model picks the wrong skill or cannot find one.** Check the title against the skill's file. Google says naming a source in your question helps narrow the search, so add all-skills.md to your prompt. If the model cannot find a skill in the combined file, upload or paste that skill's own file.
- **The model invents a fact.** Say: "Use only the context pack. Mark anything missing as Unknown." Then add the fact to the right section of my-context-pack.md and replace that source. Notebook chats in Gemini can use web search and other tools, so ask for a citation on any outside claim.
- **File upload is rejected.** Check that you chose a .md file. Notebook sources can be up to 500,000 words or 200 MB each, and markdown is a listed source type. If you hit the source limit, go back to the 3 files in step 5. Without a paid plan, the limit is 50 sources.
- **"You've reached your limit for chats with files."** This is a rolling limit in chat. Wait for it to reset, or use the notebook.
- **"Delete data to upload file."** Gemini's own storage is full. Click Settings, then History, and delete Gemini history you no longer need.
- **Instructions are too long.** Use the pointer and the office-manual.md source from Notes.
- **You forgot files in a new chat.** In a notebook, sources stay in place, so confirm you opened Marketing Office. In the plain-chat fallback, upload them again.
- **The notebook forgets past chats.** Turn on History. Without it, Gemini cannot use past chats in a notebook.
- **Notebooks do not appear in the sidebar.** The feature is rolling out gradually. Try the connection in Notes, then use the plain-chat fallback.
- **You deleted the notebook.** Its sources and added chats are deleted too. Create it again from step 2 and upload your 3 files.

## Verification

Verified on 2026-11-19 against vendor documentation. Not yet tested in a live account.

- [Downloading source code archives](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives): GitHub's Code and Download ZIP steps
- [Organize your projects with notebooks in Gemini Apps](https://support.google.com/gemini/answer/16972047?hl=en&co=GENIE.Platform%3DDesktop): notebook creation, instructions path, History, connection step, rollout, web search in chats
- [Gemini Apps Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en): History and model training settings, last updated November 17, 2026
- [Manage and delete your history](https://support.google.com/gemini/answer/13278892?hl=en&co=GENIE.Platform%3DDesktop): the training box under Settings, then History, needs History on
- [Add sources](https://support.google.com/gemininotebook/answer/16215270?hl=en&co=GENIE.Platform%3DDesktop): markdown as a source type, per-source limits, free source limit, naming sources in questions
- [Gemini Notebook plans](https://support.google.com/gemininotebook/answer/16213268?hl=en): sources per notebook on each plan
- [Notebooks in Gemini Apps, Gemini Notebook Help](https://support.google.com/gemininotebook/answer/17003757): syncing, one set of custom instructions across both apps, notebook files not used directly for training
- [Gemini Notebook FAQ](https://support.google.com/gemininotebook/answer/16269187?hl=en): per-source limit
- [Use chat in Gemini Notebook](https://support.google.com/gemininotebook/answer/16179559?hl=en): no instruction character limit stated
- [Create a notebook in Gemini Notebook](https://support.google.com/gemininotebook/answer/16206563?hl=en): no instruction character limit stated
- [Usage limits in Gemini Notebook](https://support.google.com/gemininotebook/answer/17670842?hl=en): compute-based usage limits
- [Attach and analyze files](https://support.google.com/gemini/answer/14903178?hl=en&co=GENIE.Platform%3DDesktop): Add files path, 10-file limit, error messages, Settings, then History
- [Gemini Apps limits](https://support.google.com/gemini/answer/16275805?hl=en): plan tiers and context windows
- [Create and manage skills](https://support.google.com/gemini/answer/17094296?hl=en&co=GENIE.Platform%3DDesktop): SKILL.md upload requirements, lowercase hyphenated skill name
- [Transition from Gems to skills](https://support.google.com/gemini/answer/18560919?hl=en): Gems dates for users 18 and over, and skills limits
- [Use Gems](https://support.google.com/gemini/answer/15146780?hl=en&co=GENIE.Platform%3DDesktop): notice that Gems are going away
- [How to use Gems](https://support.google.com/gemini/answer/15236405): what Gems are
- [Personal instructions](https://support.google.com/gemini/answer/16598625?hl=en&co=GENIE.Platform%3DDesktop): account-wide instructions, not used in this setup
- [Google AI plans](https://one.google.com/about/google-ai-plans/): plan names Plus, Pro and Ultra
- [Notebooks announcement](https://blog.google/innovation-and-ai/products/gemini-app/notebooks-gemini-notebooklm/): April 2026 age exclusion
- [Turn Gemini Notebook on or off for users](https://knowledge.workspace.google.com/admin/generative-ai/gemini-notebook): admin control on Workspace and Education accounts
- [Notebooks for schools and organizations](https://workspaceupdates.googleblog.com/2026/09/notebooks-in-gemini-dedicated-workspace-for-focused-organized-work-now-for-schools-and-organizations.html): Gemini and Gemini Notebook both set to On, up to 10 sources, gradual rollout
- [Flexible usage limits post](https://blog.google/innovation-and-ai/products/gemini-notebook/new-flexible-usage-limits/): limits changed from September 2026, no source count stated
- [Custom chat post](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-custom-personas-engine-upgrade/): no instruction character limit stated

What could not be verified:

- Notes: the character limit for notebook instructions.
- Steps, step 5: whether several local files can be selected at once.
- Plain-chat fallback, step 3: whether .md files upload in chat, and whether a second message gets around the 10-file limit.
