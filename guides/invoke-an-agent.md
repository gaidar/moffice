---
title: Invoke an agent role
type: guide
version: 0.1.0
updated: 2026-11-01
summary: How to give a whole job to an agent role instead of running one skill.
---

## Who it is for

A marketer who has run a skill or two and wants to hand over a bigger job. An agent role drafts and recommends. It sends the decisions listed in its charter back to you, and you, the marketer, decide.

## What you need

- Your tool, set up per your guide.
- The name of the role. See [the agent roster](../office/agent-roster.md).
- A task that fits what the role owns.

Use a skill when you know exactly which output you want. Use an agent role when you know the problem but not the output, or when the job needs several skills in sequence.

## Steps

1. Pick the role from [the agent roster](../office/agent-roster.md). Open its charter and read the Owns section and the Decides versus escalates section.
2. Start a new chat in your project. If you use the plain-chat fallback, paste the office manual and upload the charter, the skills it will need and the context pack files it reads.
3. Paste the prompt from the charter's How to invoke section and write your task:

   ```
   Act as the demand generation manager from the Marketing Office. Follow your charter. Read the context pack. Today's task: we need 40 more sales-qualified leads from professional services firms this quarter. Propose a campaign.
   ```

4. Read which skills it plans to run. If it plans something you do not want, say so before it starts.
5. Answer the questions it escalates to you. Each one should come with a recommendation.
6. To hand off to another role, start a new chat and paste the output in:

   ```
   Act as the content lead from the Marketing Office. Follow your charter. Read the context pack. Today's task: write the assets listed in this campaign brief. [paste the brief]
   ```

7. Before anything goes public, get a review:

   ```
   Act as the marketing reviewer from the Marketing Office. Follow your charter. Read the context pack. Today's task: review this draft against the skill it came from, "Write a campaign brief". [paste the draft]
   ```

8. To start your week with no specific task in mind:

   ```
   Act as the head of marketing from the Marketing Office. Follow your charter. Read the context pack. Today's task: tell me what to do this week. [paste last week's numbers]
   ```

## What success looks like

The role stays in its lane, names the skills it uses, returns outputs in each skill's format, and brings decisions back to you with a recommendation. When a task belongs to another role, it says which one.

## Troubleshooting

- **The role does work that belongs to another role.** Say: "Check your charter's Owns section. Which role owns this?"
- **It makes a decision you wanted to make.** Point to the charter's Decides versus escalates section, and tell it to bring the decision back as a question.
- **It forgets the role in a long chat.** Paste the invoke prompt again, or start a new chat and paste the latest output.
- **It says it has no charter.** Upload the charter file from the `agents/` folder, or paste its text from [GitHub](https://github.com/gaidar/moffice/tree/main/agents).
- **You are unsure which role to use.** Ask the head of marketing: "Which agent role should handle this?"
