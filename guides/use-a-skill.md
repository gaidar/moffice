---
title: Use a skill
type: guide
version: 0.1.0
updated: 2026-11-01
summary: How to run any skill, check the output and get a better second draft.
diagram: skill
diagram_caption: "Every skill page has these sections in this order."
---

## Who it is for

A marketer who has set up a tool and filled in at least company.md, product.md and messaging.md. A skill produces a draft, and you, the marketer, decide what to use.

## What you need

- Your tool, set up per your guide.
- The title of the skill you want. Browse [the skills library](../skills.md).
- Anything the skill's Inputs section says you must supply, such as a topic, an export or notes.
- About 10 minutes for most skills. This is an estimate.

## Steps

1. Open the skill page and read the When to use section. It tells you if another skill fits better.
2. Check the Inputs section. Have ready whatever it says the marketer supplies.
3. In your tool, start a new chat in your project. If you use the plain-chat fallback, paste the office manual and upload the context pack files listed in Inputs, plus the skill file.
4. Paste the prompt from the How to run it section, and write your task after "Task:". Be specific about the goal, audience and any deadline:

   ```
   Use the skill "Write a marketing email". Read the context pack.
   Task: invitation to our March webinar on checking AI answers, for heads of learning at professional services firms.
   ```

5. Attach any exports or notes the skill asked for.
6. Read the "Assumptions and open questions" section first. It tells you what the draft is resting on.
7. Answer the open questions, and correct any wrong assumptions:

   ```
   Answers: 1) yes, 2) the webinar is on March 4, 3) leave out the pricing. Produce the output again in the same format.
   ```

8. Run the skill's Quality checklist yourself. Any "no" means fix it, or ask for a fix.
9. For anything public, or anything that uses a customer name or number, run a review in a new chat:

   ```
   Use the skill "Review any output". Read the context pack.
   Task: review this draft, which came from the skill "Write a marketing email". [paste the draft]
   ```

10. Save what you keep. Name it the way [the output conventions](../office/output-conventions.md) describe.

## What success looks like

The output follows the template on the skill's page, section by section. Facts match your context pack. Open questions are short and real.

## Troubleshooting

- **The output ignores the template.** Say: "Follow the Output format section of the skill exactly." If it repeats, upload the skill file to the chat.
- **The model says it has no such skill.** Check the title spelling against the page. Upload or paste the skill file.
- **The output is too long.** Say: "Keep to the length limits in the Output format section."
- **It asks too many questions.** Say: "Draft now and leave placeholders in square brackets for anything you are missing."
- **It used a customer you cannot name.** Fix the permission status in proof-points.md and upload it again.
- **No skill fits.** Describe the job anyway. The office manual tells the model how to handle it and how to label the result. If you do the job often, see [Write your own skill](write-your-own-skill.md).
