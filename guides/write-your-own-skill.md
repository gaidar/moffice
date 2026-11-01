---
title: Write your own skill
type: guide
version: 0.1.0
updated: 2026-11-02
summary: Turn a job you do repeatedly into a skill with a fixed procedure and output, including skills that prepare work for your CMS, CRM or email tool.
---

## Who it is for

A marketer who keeps repeating the same job in chat, or who needs output shaped for their own tools. The Marketing Office has limited connectors to external tools, so this is how you fit the office to your CMS, CRM or email setup.

## What you need

- A job you have done at least twice, and one example of a good result.
- A plain text editor.
- About 30 minutes. This is an estimate.

## Steps

1. Copy the template below into a new text file. Name the file with lowercase words and hyphens, starting with a verb, for example `write-release-notes-email.md`.
2. Start a new chat and paste this prompt, attaching your example of a good result:

   ```
   Using the Marketing Office skill format below, draft a skill for this repeating job: [describe the job].
   Attached is an example of a good result. The procedure must be numbered steps a model can follow without judgment calls I have not written down. The output format must be an exact template. Ask me about anything you cannot tell from the example. Do not invent facts about my company.
   [paste the template]
   ```

3. Check the draft with this test: could a model produce the output from this skill alone, plus a filled context pack? If not, rewrite the vague steps.
4. Fill in the fields at the top. `owner` is the file name of one agent role from [the agent roles](../agents.md). `reads` lists the context pack files the skill uses. `you_bring` says what the marketer must have ready, and shows at the top of the skill page. `also_for` lists the words someone might search for when they need this skill, and feeds the filter in the skills library.
5. Test it twice on real tasks. Change the procedure every time you have to correct the output for the same reason.
6. Run [Review any output](../skills/marketing-ops/review-any-output.md) on the skill's first real output.
7. Upload the file to your project next to `all-skills.md`, or paste it into the chat. `my-context-pack.md` stays as it is. If you want to share the skill, see [Contributing](../CONTRIBUTING.md).

### Skill template

```markdown
---
title: <sentence case, starts with a verb>
type: skill
function: <one of the 16 function folder names>
owner: <agent role file name>
reads: [<context pack file names>]
you_bring: <what the marketer must have ready, in one short sentence>
also_for: [<words someone might search for, such as pipeline or website>]
version: 0.1.0
updated: <YYYY-MM-DD>
summary: <one sentence>
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

<Two or three sentences. Include when not to use it and which skill to use instead.>

## Inputs

<Context pack files it reads, written like [[context-pack:messaging]]. What the marketer must supply in the prompt.>

## Procedure

1. <Numbered steps the model follows.>
2. <If a blank changes the whole output, ask before drafting. If it affects a detail, leave a placeholder in square brackets and ask in the last section. Never invent.>
3. <Check the draft against the context pack and fix any contradiction.>
4. <List what you assumed.>

## Output format

(The exact template in a fenced block, with field names, order and length limits. Its first line is "Status: Draft". Its last section is always "Assumptions and open questions".)

## Quality checklist

- [ ] <Five to ten yes/no checks the marketer runs before using the output.>

## Example (fictional company)

<150 to 300 words of sample output, using a fictional company.>

## How to run it

(The prompt in a fenced block, because the Copy prompt button copies the first block under this heading.)

Use the skill "<title>". Read the context pack.
Task: <the specific things the marketer must state, and any export or notes to attach>.
```

### Skills for your own tools

The office cannot publish, send or pull data by itself. A skill can still make that work fast by shaping the output for your tool. For example:

- **CMS:** a skill that outputs page copy in the exact fields your page builder has, field by field, so that you paste it in.
- **CRM:** a skill that takes a pasted export, checks the column names first, and refuses to proceed if a column is missing.
- **Email:** a skill that outputs subject, preview text, body and segment rules in the order your email tool asks for them.

Name the tool's fields in the Output format section. If your AI tool has its own connection to these systems, follow that tool's documentation. The office does not cover that.

## What success looks like

Two different runs of the skill return the same structure, and you edit content rather than format.

## Troubleshooting

- **The output changes shape between runs.** Put the template in a fenced code block, and add length limits for each field.
- **The model skips steps.** Make each step produce something visible in the output.
- **The skill gets long.** Split it in two. The library's skills run 500 to 1,200 words.
- **It invents facts.** Add a step that names the context pack file for each fact, and that says to ask when it is blank.
- **The model cannot find your new skill.** Upload the file to your project, or paste it into the chat.
