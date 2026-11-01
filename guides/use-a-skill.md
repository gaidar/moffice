---
title: Use a skill
type: guide
version: 0.1.0
updated: 2026-11-02
summary: How to run any skill, check the output and get a better second draft.
diagram: skill
diagram_caption: "Every skill page has these sections in this order."
---

## Who it is for

A marketer who has set up a tool and has a first pass of the context pack, even with blanks.

## What you need

- Your tool, set up per your guide.
- The title of the skill you want. Browse [the skills library](../skills.md).
- Whatever the "You bring" line at the top of the skill page names, such as a topic, an export or notes.
- About 10 minutes for most skills. This is an estimate.

## Steps

1. Open the skill page and read the When to use section. It tells you if another skill fits better.
2. Read the "You bring" line at the top of the page, and have those things ready.
3. In your tool, start a new chat in your project. If you use the plain-chat fallback, paste the office manual and upload `my-context-pack.md` plus the skill file.
4. Click **Copy prompt** at the top of the skill page. It copies the prompt from the page's How to run it section. Paste it into the chat and write your task after "Task:". Be specific about the goal, audience and any deadline:

   ```
   Use the skill "Write a marketing email". Read the context pack.
   Task: invitation to our March webinar on checking AI answers, for heads of learning at professional services firms.
   ```

5. Attach any exports or notes the skill asked for.
6. Read the "Assumptions and open questions" section first. It tells you what the draft is resting on.
7. Answer the open questions, in order, and correct any wrong assumptions:

   ```
   Answers: 1) contacts tagged professional services, 2) the webinar is on March 4. Produce the output again in the same format.
   ```

8. Run the skill's Quality checklist yourself. Any "no" means fix it, or ask for a fix.
9. For anything public, or anything that uses a customer name or number, run a review in a new chat. Say where it will appear and which skill it came from:

   ```
   Use the skill "Review any output". Read the context pack.
   Task: review this draft for public use. It came from the skill "Write a marketing email". [paste the draft]
   ```

10. Save what you keep. Name it the way [the output conventions](../office/output-conventions.md) describe.

## Worked example: draft, answers, review

The facts come from [the CogniATion sample pack](../context-pack/example-cogniation/company.md). The webinar, dates, link, list tag and colleague's edit are invented. Outputs are shortened.

**First draft.** The prompt in step 4 returns a complete email, with brackets for what the pack lacks. It ends:

```
- Unknown: Which part of the 5,400-contact list receives this?
- Unknown: What are the webinar date, send date and registration link?
- Unknown: Does this meet the rules that apply to your list?
```

**Your reply.**

```
Answers: 1) contacts tagged professional services, 2) webinar March 4, 2027, send February 16, link https://cogniation.example/webinar, 3) yes, I checked. Produce the output again in the same format.
```

**The lines that changed.** Tracking and footer fields stay in brackets, because you did not supply them.

| Line | First draft | Second draft |
|---|---|---|
| Audience | `[part of list needed]` | Contacts tagged professional services |
| Body | Join us in March. `[webinar date needed]` | Join us on March 4. |
| Link | `[link needed]` | https://cogniation.example/webinar |

**The review.** Suppose a colleague adds a line the skill would never write: "Haldane Ridge Capital is with us, and we reached $5.2 million in annual recurring revenue." You run Review any output for public use, saying the dates and link are yours. Verdict: Do not use yet. 2 blockers, 1 fix (no test send yet). Strategy not judged.

| Where | Problem | Source | What to change |
|---|---|---|---|
| "Haldane Ridge Capital" | Permission pending | proof-points.md | Remove the name |
| "$5.2 million in annual recurring revenue" | Internal-only number | company.md | Remove the number |

## What success looks like

The output follows the template on the skill's page, section by section. Facts match your context pack. Open questions are short and real.

## Troubleshooting

- **The output ignores the template.** Say: "Follow the Output format section of the skill exactly." If it repeats, upload the skill file to the chat.
- **The model says it has no such skill.** Check the title spelling against the page. If the model cannot find the skill in the combined file, upload or paste that skill's own file.
- **The output is too long.** Say: "Keep to the length limits in the Output format section."
- **It asks too many questions.** Say: "Draft now and leave placeholders in square brackets for anything you are missing."
- **It used a customer you cannot name.** Fix the permission status in `my-context-pack.md` and upload it again.
- **No skill fits.** Describe the job anyway. The office manual tells the model how to handle it and how to label the result. If you do the job often, see [Write your own skill](write-your-own-skill.md).
