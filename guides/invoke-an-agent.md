---
title: Invoke an agent role
type: guide
version: 0.1.0
updated: 2026-11-02
summary: How to give a whole job to an agent role instead of running one skill.
---

A role is an instruction for one chat. It runs nothing by itself. Start with the head of marketing. Most people need the head of marketing and skills, and the rest of the roles are optional.

## Who it is for

A marketer who has run a skill or two and wants to hand over a bigger job. A role sends the decisions listed in its charter back to you.

## What you need

- Your tool, set up per your guide.
- A task, or a problem you want sorted out. You do not need to know the role's name yet.

Use a skill when you know exactly which output you want. Use an agent role when you know the problem but not the output, or when the job needs several skills in sequence.

## Steps

1. If you are unsure which role to use, ask the head of marketing:

   ```
   Act as the head of marketing from the Marketing Office. Follow your charter. Read the context pack. Which agent role should handle this? [describe the job]
   ```

   If you already know, pick the role from [the agent roster](../office/agent-roster.md). Open its charter and read the Owns section and the Decides versus escalates section.
2. Start a new chat in your project. If you use the plain-chat fallback, paste the office manual and upload the charter, the skills it will need and `my-context-pack.md`.
3. Click **Copy prompt** at the top of the charter page, paste it and write your task:

   ```
   Act as the demand generation manager from the Marketing Office. Follow your charter. Read the context pack. Today's task: we need 30 more sales-qualified leads from professional services firms this quarter. Propose a campaign.
   ```

4. Read which skills it names. It starts straight away, so if it plans something you do not want, stop it and say so.
5. Answer the questions that come back to you. Each one should come with a recommendation, or say what the role needs from you before it can make one.
6. When a job crosses roles, stay in this chat. The role says who owns the next part, runs it under that charter and comes back. To steer it yourself:

   ```
   Act as the content lead from the Marketing Office. Follow your charter. Read the context pack. Today's task: write the assets listed in the campaign brief above.
   ```

   Start a new chat only when this one gets long. Say `Close my session`, save what comes back in [your workboard](../office/my-workboard.md), then start the new chat with your workboard and `Start my session`.
7. Before anything goes public, get a review in the same chat. A review is not approval, and the draft stays a draft until you decide:

   ```
   Act as the marketing reviewer from the Marketing Office. Follow your charter. Read the context pack. Today's task: review the draft above against the skill it came from, "Write a campaign brief". Then correct what you find and show the corrected draft. Mark nothing approved.
   ```

   For a colder read of something that matters, paste the draft into a new chat. That chat has not seen how the draft was made.

8. To start your week with no specific task in mind:

   ```
   Act as the head of marketing from the Marketing Office. Follow your charter. Read the context pack. Today's task: tell me what to do this week. [paste last week's numbers]
   ```

## Worked example: a role plans a campaign

The facts come from [the CogniATion sample pack](../context-pack/example-cogniation/company.md). The prompt in step 3 returns this reply, shortened. The offer and the amount are illustrative, because the pack holds neither.

**Skills it plans.** [Write a campaign brief](../skills/campaign-design/write-campaign-brief.md), then [Design a nurture sequence](../skills/campaign-design/design-nurture-sequence.md) for leads not ready for sales. The paid plan goes to the paid media manager and the assets to the content lead.

**What it decides alone.** The offer: a guide to checking the reasoning in client memos, then a demo. The channels: professional social network ads, search ads and the email list.

**The arithmetic.** Estimate: 30 SQLs at the 26% MQL to SQL rate needs about 116 MQLs.

**What comes back to you.** All spending does, so the brief's budget line reads `[budget needed]` until you answer:

```
Question: how much of the $70,000 quarter budget goes to this campaign?
Mechanical share: 30 of the 90 SQL goal is a third, and a third of $70,000 is about $23,000. This is arithmetic, not a recommendation. It knows nothing about what these channels cost.
Recommendation: tell me what the channels actually cost per SQL last quarter. Then I can recommend an amount.
Any line over $5,000 needs Marta Ilves, CEO, 3 days, so ask her by February 12 to keep the February 15 start.

Question: are the 30 part of the 90 SQL goal, or on top of it?
Recommendation: part of it. A higher target is yours to set.

Unknown: is the $9,000 a month already running on search and social ads inside this amount?
```

A skill would have returned a brief. The role chose the skills, named the handoffs and brought the money back to you. It spends nothing. Do not forward the $23,000 as advice: it is the same share as 30 of 90, and nothing more. [Judge an output](judge-an-output.md) shows what to ask of a number like this.

## What success looks like

The role stays in its lane, names the skills it uses, returns outputs in each skill's format, or a short working view when a job runs several skills, and brings decisions back to you with a recommendation, or with the question it must answer first. When part of a task belongs to another role, it says which one and runs that part in the same chat.

## Troubleshooting

- **The role does another role's work without saying so.** Say: "Which charter are you running this part under?"
- **It makes a decision you wanted to make.** Point to the charter's Decides versus escalates section, and tell it to bring the decision back as a question.
- **It forgets the role in a long chat.** Paste the invoke prompt again, or say `Close my session` and resume in a new chat with `Start my session`.
- **It says it has no charter.** Upload the charter file from the `agents/` folder, or paste its text from [GitHub](https://github.com/gaidar/moffice/tree/main/agents).
