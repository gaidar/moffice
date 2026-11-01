---
title: Set up on Claude
type: guide
version: 0.1.0
updated: 2026-11-02
summary: Create one Claude project with the office manual in its instructions and 3 files in its knowledge, or run the office in plain chat.
diagram: setup
diagram_caption: "The steps below cover the top path. The plain-chat fallback covers the bottom one."
---

## Who it is for

Marketers with a personal Claude Pro or Max plan. Anthropic lists projects on Free too, with a limit of five, but says project instructions are for paid plans and limits automatic capacity expansion to paid plans.

These steps were written from Anthropic's help pages on the date below, and have not been run in a live account, so if a screen differs, trust the help page.

## What you need

- A Claude Pro or Max subscription, signed in at claude.ai in a browser
- The Marketing Office files, from [the Marketing Office repository](https://github.com/gaidar/moffice) on GitHub. Step 1 shows how to get them.
- `my-context-pack.md`, from the [fast first pass](fill-the-context-pack.md#fast-first-pass). Blanks in it are fine.
- A plain text editor, for opening and copying the office manual
- About 30 minutes, an estimate, not counting the context pack

## Steps

1. Get the files from GitHub. Open [the Marketing Office repository](https://github.com/gaidar/moffice), click **Code** above the list of files, then click **Download ZIP**, which is [GitHub's own download](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives). Double-click the downloaded file to open it. You now have a folder of plain-text files.

2. Go to claude.ai/projects, or hover over the left side of your account and click "Projects". Click "+ New Project" in the upper right corner and name the project `Marketing Office`. Claude cannot read the name or description, so the description can say anything. See [Anthropic's project steps](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

   Use claude.ai/projects, not the "Projects" item at claude.ai/code, which is a separate beta for running Claude Code threads.

3. Open `office/office-manual.md` in a plain text editor and copy all of it. In the project, click "Set project instructions", paste, and click "Save instructions". Anthropic's course calls this panel "Instructions".

   If the text does not fit, paste this short pointer instead, then upload `office-manual.md` with the other files:

   ```
   You are the Marketing Office. Before every response, read the file office-manual.md in this project's files and follow it exactly. It sets how skills and agent roles are used, the rule on facts, the assumption labels and the output conventions. Never invent facts about the company. If you cannot find office-manual.md, say so and ask the marketer to upload it.
   ```

   The office manual is about 7,800 characters, and Anthropic's help pages state no character limit for these instructions. Unverified – check the vendor help page: [create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

4. Upload your context pack first, as a test. In the project knowledge area on the right side of the project's main page, click the "+" button and upload `my-context-pack.md`. Anthropic's file help also calls this area "Files".

   If the file is rejected, change the file's ending from .md to .txt and upload it again, and do the same with the files in step 5. Anthropic's list names TXT and does not name Markdown. Unverified – check the vendor help page: [upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude).

5. Upload `bundles/all-skills.md` and `bundles/all-agent-roles.md` the same way. If your file picker takes only one file at a time, upload them one at a time. Unverified – check the vendor help page: [upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude).

   Anthropic sets no fixed file count for a project: each file can be up to 30MB, and all content must fit Claude's context window. On paid plans, Claude switches on [retrieval mode](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) automatically as the project nears that limit, which Anthropic says expands capacity by up to 10x.

6. Start a new chat inside the project and paste this check prompt:

   ```
   List the context pack sections you can see, and say which have blanks. Then tell me which skill you would use to write a sales one-pager. Do not invent anything.
   ```

   Expected: it lists the 10 sections of your context pack, says which have blanks, and names the skill "Write a sales one-pager".

   Then check that it can use a skill from the combined file, with this second check:

   ```
   Show me the Output format section of the skill "Write a sales one-pager", word for word.
   ```

   Compare the answer with [the skill's page on this site](../skills/product-marketing-and-sales-enablement/write-sales-one-pager.md). If it does not match, upload or paste that skill's own file, `skills/product-marketing-and-sales-enablement/write-sales-one-pager.md`.

7. Follow [Use a skill](use-a-skill.md) for your first output. Run work inside the project with these prompts:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

   ```
   Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
   ```

## What success looks like

The project named Marketing Office shows the office manual in its instructions and your 3 files in project knowledge. A new chat inside it answers the check prompt with the 10 context pack sections, says which have blanks, and names "Write a sales one-pager". The second check returns the skill's Output format as it appears on this site.

## Plain-chat fallback

This works with chat and file upload only. It costs a few minutes at the start of each chat, because nothing carries over for you. Get the files from GitHub first, as in step 1 above.

1. Start a new chat at claude.ai, outside any project.
2. Copy all of `office/office-manual.md` from a plain text editor, paste it as your first message, and send it.
3. Upload `my-context-pack.md` and the skill file. Click the "+" button in the lower-left corner of the chat box, then "Add files or photos", or drag the files into the chat window. The limit is 20 files per chat and 500MB per file. If a .md file is rejected, change its ending to .txt, or paste its text into the chat.
4. Paste the run prompt, with your skill title and task filled in:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

   For an agent role, upload its charter instead of the skill file and use:

   ```
   Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
   ```

5. Save each output yourself by copying it into your own file. Keep `my-context-pack.md` in the same folder.
6. When the chat gets long, ask for a handoff note and save it. Anthropic says that on paid plans with code execution on, Claude summarizes earlier messages automatically, and that longer chats use more of your usage limit. It suggests a new chat when you near that limit or hit a length limit.

   ```
   Write a handoff note for a new chat: decisions made, outputs finished, open questions and the next step. Do not invent anything.
   ```

7. To begin the next chat, repeat steps 1 to 3, paste the handoff note, then paste the run prompt.

### Optional extras

- **Individual files.** In place of the two bundles, upload every file in each `skills/[function]/` folder and every file in `agents/`. Inference from how retrieval mode works: separate files make it easier for Claude to find one skill, so try this if Claude keeps missing skills.
- **Claude's own Skills feature.** The project path is the supported one, because that feature needs each skill repackaged as a ZIP with a skill.md file and required name and description fields.

## Troubleshooting

- **Claude says it cannot find a skill.** Check that `all-skills.md` is in the project, and use the exact title. If the model cannot find a skill in the combined file, upload or paste that skill's own file. In plain chat, upload the skill file.
- **The check prompt lists fewer than 10 sections.** Inference: in retrieval mode, Claude pulls only what seems relevant, so it may not list everything. Check that `my-context-pack.md` is in the project's file list and holds all 10 sections, then ask for the missing section by name.
- **Claude ignores the office manual.** Project instructions apply only to chats in that project. Check that the chat was started inside Marketing Office and that the instructions were saved.
- **Claude invents a fact.** Ask for its source in the context pack. If there is none, add the fact to the right section of `my-context-pack.md` or tell it to leave a visible placeholder such as `[customer quote needed]`. Check the office manual is loaded, because it holds the rule on facts.
- **File upload rejected.** Change the ending from .md to .txt. Anthropic's list names TXT, not Markdown. In a project, also check the file is under 30MB.
- **Instructions too long.** Use the short pointer in step 3 and upload `office-manual.md` as a file.
- **You updated your context pack.** Upload the new `my-context-pack.md`. If the old one still shows, remove it, so that two versions do not mix. How to remove it: Unverified – check the vendor help page: [create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).
- **Forgot files in a new chat.** In plain chat, upload them now and ask Claude to read them again before it continues. In a project, files stay available across chats, so this should not happen.
- **You are near your usage limit in a long chat.** Save your outputs and start a new chat. Anthropic says longer chats use more of the limit.

## Verification

Verified on 2026-11-01 against vendor documentation.

- [Downloading source code archives](https://docs.github.com/en/repositories/working-with-files/using-files/downloading-source-code-archives): GitHub's Code and Download ZIP steps
- [What are projects?](https://support.claude.com/en/articles/9517075-what-are-projects): plans, five-project Free limit, paid retrieval mode
- [How can I create and manage projects?](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects): project, instructions and file upload steps, button names
- [Upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude): file types, chat and project limits, chat upload buttons
- [Retrieval augmented generation for projects](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects): automatic switch, up to 10x capacity, paid plans
- [Understanding Claude's personalization features](https://support.claude.com/en/articles/10185728-understanding-claude-s-personalization-features): project instructions for paid plans, apply only inside the project
- [What are skills?](https://support.claude.com/en/articles/12512176-what-are-skills): what skills are, plans, code execution requirement
- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude): ZIP upload path and common upload failures
- [How to create custom skills](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills): required skill.md, name, description and ZIP structure
- [How do usage and length limits work?](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work): long chats, summarizing, starting a new chat
- [How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans): context window, automatic summarizing on paid plans
- [Claude pricing](https://claude.com/pricing): Pro and Max include projects and skills
- [Projects in Claude Code docs](https://code.claude.com/docs/en/claude-projects): the separate beta at claude.ai/code
- [Introduction to projects, Claude Academy](https://academy.claude.com/courses/claude-101/introduction-to-projects): "Instructions" panel name, file types named

What could not be verified:

- Step 3: the character limit for project instructions. No page fetched states one for projects at claude.ai/projects.
- Step 4: whether .md files upload. No page fetched lists Markdown as supported or rejected.
- Step 5: selecting several files at once.
- Troubleshooting, "You updated your context pack": how to remove a file from a project.
