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

**Last checked against documentation:** 2026-11-01. **Last tested in a live account:** not yet. If a screen differs, trust the help page.

## What you need

- A decision on your data settings. On consumer plans, whether your chats help improve Claude is a privacy setting you control. Check it before you upload company facts: [who can view your chats](https://support.claude.com/en/articles/8325621-i-would-like-to-input-sensitive-data-into-my-chats-with-claude-who-can-view-my-conversations). Never upload what the context pack guide tells you to strip.
- A Claude Pro or Max subscription, signed in at claude.ai in a browser
- The two office files. Step 1 links them.
- `my-context-pack.md`, from the [fast first pass](fill-the-context-pack.md#fast-first-pass). Blanks in it are fine.
- About 30 minutes, an estimate, not counting the context pack

## Steps

1. Download the two office files. Click each one, and it saves as a text file: [all-skills.md](https://raw.githubusercontent.com/gaidar/moffice/v0.1.0/bundles/all-skills.md) and [roles-and-playbooks.md](https://raw.githubusercontent.com/gaidar/moffice/v0.1.0/bundles/roles-and-playbooks.md). If a link opens the text instead, save that page under the same name. Keep them with `my-context-pack.md`.

2. Go to claude.ai/projects, click **+ New Project** in the upper right corner and name it `Marketing Office`. See [Anthropic's project steps](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

3. Open [the office manual](../office/office-manual.md) and click **Copy full text** at the top of the page. In the project, click **Set project instructions**, paste and click **Save instructions**. If it does not fit, see Notes.

4. In the project knowledge area on the right, click the **+** button and upload `my-context-pack.md`. If it is rejected, change the file's ending from .md to .txt and upload it again.

5. Upload `all-skills.md` and `roles-and-playbooks.md` the same way. Unverified – check the vendor help page: [upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude).

6. Start a new chat inside the project and paste this check:

   ```
   List the context pack sections you can see, and say which have blanks. Then name the skill you would use to write a sales one-pager, and show its Output format section word for word. Do not invent anything.
   ```

   Expected: it lists the 10 sections of your context pack, says which have blanks, and names "Write a sales one-pager". Compare its Output format with [the skill's page](../skills/product-marketing-and-sales-enablement/write-sales-one-pager.md). If it does not match, upload that skill's own file, using **Download file** on the same page.

7. Ask for your first draft, in plain words, in a new chat in the project. It tells you which skill it used. [Use a skill](use-a-skill.md) covers the rest.

   ```
   Write a sales one-pager for our most important segment, aimed at the person who signs, for one-to-one use by sales.
   ```

   If it picks the wrong skill or ignores your facts, use the exact form:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

### Notes

- **If the instructions do not fit**, paste this pointer instead, and upload `office-manual.md` with the other files. The manual is about 8,800 characters, and Anthropic states no limit for project instructions. Unverified – check the vendor help page: [create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).

  ```
  You are the Marketing Office. Before every response, read the file office-manual.md in this project's files and follow it exactly. It sets how skills and agent roles are used, the rule on facts, the assumption labels and the output conventions. Never invent facts about the company. If you cannot find office-manual.md, say so and ask the marketer to upload it.
  ```

- **Which Projects.** Use claude.ai/projects, not the "Projects" item at claude.ai/code, which is a separate beta for running Claude Code threads. Claude cannot read the project's name or description, so these can say anything.
- **File types.** Anthropic's list names TXT and does not name Markdown, which is why step 4 has the .txt route. Unverified – check the vendor help page: [upload files to Claude](https://support.claude.com/en/articles/8241126-upload-files-to-claude).
- **Capacity.** Anthropic sets no fixed file count for a project: each file can be up to 30MB, and all content must fit Claude's context window. On paid plans, Claude switches on [retrieval mode](https://support.claude.com/en/articles/11473015-retrieval-augmented-generation-rag-for-projects) automatically as the project nears that limit, which Anthropic says expands capacity by up to 10x.

## What success looks like

The project named Marketing Office shows the office manual in its instructions and your 3 files in project knowledge. A new chat inside it answers the check with the 10 context pack sections, says which have blanks, names "Write a sales one-pager" and returns its Output format as it appears on this site.

## Plain-chat fallback

This works with chat and file upload only. It costs a few minutes at the start of each chat, because nothing carries over for you.

1. Start a new chat at claude.ai, outside any project.
2. Copy [the office manual](../office/office-manual.md) with **Copy full text**, paste it as your first message, and send it.
3. Upload `my-context-pack.md` and the skill file, which you get with **Download file** on the skill's page. Click the "+" button in the lower-left corner of the chat box, then "Add files or photos", or drag the files into the chat window. The limit is 20 files per chat and 500MB per file. If a .md file is rejected, change its ending to .txt, or paste its text into the chat.
4. Paste the run prompt, with your skill title and task filled in:

   ```
   Use the skill "<title>". Read the context pack. Task: <what they want>.
   ```

   For an agent role, upload its charter instead of the skill file and use:

   ```
   Act as the <role> from the Marketing Office. Follow your charter. Read the context pack. Today's task: <task>.
   ```

5. Save each output yourself by copying it into your own file. Keep `my-context-pack.md` in the same folder.
6. When the chat gets long, close the session and save what comes back in [your workboard](../office/my-workboard.md). Anthropic says that on paid plans with code execution on, Claude summarizes earlier messages automatically, and that longer chats use more of your usage limit. It suggests a new chat when you near that limit or hit a length limit.

   ```
   Close my session
   ```

7. To begin the next chat, repeat steps 1 to 3, paste your workboard, then write `Start my session`.

### Optional extras

- **Individual files.** In place of the two combined files, get [the repository](https://github.com/gaidar/moffice) with GitHub's **Code** and **Download ZIP** buttons, and upload every file in each `skills/[function]/` folder and every file in `agents/`. Inference from how retrieval mode works: separate files make it easier for Claude to find one skill, so try this if Claude keeps missing skills.
- **Claude's own Skills feature.** The project path is the supported one, because that feature needs each skill repackaged as a ZIP with a skill.md file and required name and description fields.

## Troubleshooting

- **Claude picks the wrong skill or cannot find one.** Check that `all-skills.md` is in the project, and use the exact title. If the model cannot find a skill in the combined file, upload or paste that skill's own file. In plain chat, upload the skill file.
- **The check lists fewer than 10 sections.** Inference: in retrieval mode, Claude pulls only what seems relevant, so it may not list everything. Check that `my-context-pack.md` is in the project's file list and holds all 10 sections, then ask for the missing section by name.
- **Claude ignores the office manual.** Project instructions apply only to chats in that project. Check that the chat was started inside Marketing Office and that the instructions were saved.
- **Claude invents a fact.** Ask for its source in the context pack. If there is none, add the fact to the right section of `my-context-pack.md` or tell it to leave a visible placeholder such as `[customer quote needed]`. Check the office manual is loaded, because it holds the rule on facts.
- **File upload rejected.** Change the ending from .md to .txt. Anthropic's list names TXT, not Markdown. In a project, also check the file is under 30MB.
- **Instructions too long.** Use the pointer in Notes and upload `office-manual.md` as a file.
- **You updated your context pack.** Upload the new `my-context-pack.md`. If the old one still shows, remove it, so that two versions do not mix. How to remove it: Unverified – check the vendor help page: [create and manage projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects).
- **Forgot files in a new chat.** In plain chat, upload them now and ask Claude to read them again before it continues. In a project, files stay available across chats, so this should not happen.
- **You are near your usage limit in a long chat.** Save your outputs and start a new chat. Anthropic says longer chats use more of the limit.

## Verification

Verified on 2026-11-01 against vendor documentation. Not yet tested in a live account. The data settings note was checked on 2026-11-02 from search excerpts of the linked page.

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

- Notes: the character limit for project instructions. No page fetched states one for projects at claude.ai/projects.
- Notes: whether .md files upload. No page fetched lists Markdown as supported or rejected.
- Step 5: selecting several files at once.
- Troubleshooting, "You updated your context pack": how to remove a file from a project.
