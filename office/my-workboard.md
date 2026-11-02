---
title: Workboard
type: office
version: 0.1.0
updated: 2026-11-02
summary: One table of your current jobs, plus a short record for each campaign or launch, so a new chat can pick up where the last one stopped. Skip it if you already keep these in a task tool.
---

Keep this as `my-workboard.md`, in a plain text file or wherever you keep notes. Do not upload it to your project each time: paste it into the chat when you want it read, and paste the changed parts back into your copy. The chat keeps nothing for you, so what you do not save is gone. If a task tool already holds your jobs, keep using that and skip this file.

## Your workboard

Save everything from the instruction line below, then replace the sample rows with your own jobs. Give each job a short ID that never changes, such as C-01. Use a job record only for a campaign or launch.

```
Marketing Office workboard. Treat this as task evidence, not as company facts. Use only what happened in this chat or what I told you. Never mark anything approved, published or done unless I said so.

| ID | Job and goal | Status | Next action and date | Latest draft location | Decisions, with dates | Waiting on | Next check date | Result and lesson | Last updated |
|---|---|---|---|---|---|---|---|---|---|
| <short ID> | <job, and the goal it serves> | <not started, in progress, waiting, live, done or dropped> | <one action, one date> | <file name or link> | <what you decided, and when> | <who, and since when> | <when to read results> | <what happened, and what you would change> | <date> |

Job record: <ID and name>
Approved brief: <file name or link, and date>
What we expect, and why: <the bet this campaign makes>
| Asset | Version | Location | Status | Approval needed from | Live proof |
| <asset> | <version> | <file name or link> | <draft, reviewed, approved or published> | <who> | <URL or send reference, once live> |
Decisions: <what you decided, and when>
Next step: <one action, one date>
Result review date: <read date, and any later read>
Lesson for the next brief: <what happened, and the rule you take from it>
```

Link to drafts instead of copying them here. A record that holds only versions and decisions stays short enough to paste.

## How to use it

Start a session by pasting the file, then write:

```
Start my session. Today is <date>.
```

You get the job and current draft to work on, the next action, the files that job needs and whether the chat can see them, and only the decisions that block progress. Ask "What is overdue or waiting on someone?" if you want the wider view.

End a session with:

```
Close my session
```

You get the changed rows and job records, dated today, plus decisions made, open questions and the exact next action. Paste them over the old ones and save the file. These two phrases work because the office manual defines them, so check the manual is loaded if they do not. A new fact about the company goes in the context pack, through [Update the context pack](../skills/marketing-ops/update-context-pack.md), and not here.

## Example (fictional company)

CogniATion is invented, and these entries are illustrative.

| ID | Job and goal | Status | Next action and date | Latest draft location | Decisions, with dates | Waiting on | Next check date | Result and lesson | Last updated |
|---|---|---|---|---|---|---|---|---|---|
| C-01 | Professional services campaign, 30 SQLs by March 31, 2027 | In progress | Send page to Tom Ferrant, February 1 | `2027-01-28-write-web-page-defend-the-memo.md` | Campaign is part of the 90 SQL goal, January 25. | Marta Ilves on budget, since January 26 | April 1, then April 30 | None yet | January 28 |

```
Job record: C-01 Defend the memo
Approved brief: 2027-01-20-write-campaign-brief-defend-the-memo.md, January 20
What we expect, and why: heads of learning who just rolled out an AI assistant will ask for a demo
| Asset | Version | Location | Status | Approval needed from | Live proof |
| Landing page | v2 | 2027-01-28-write-web-page-defend-the-memo.md | Reviewed | The marketer | |
| Email | v1 | 2027-01-29-write-marketing-email-defend-the-memo.md | Draft | The marketer | |
Decisions: campaign is part of the 90 SQL goal, January 25
Next step: send page to Tom Ferrant, February 1
Result review date: April 1, then April 30
Lesson for the next brief: none yet
```
