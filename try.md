---
title: Try it in 10 minutes
type: index
version: 0.1.0
updated: 2026-11-02
summary: See a real draft before you commit any time. Use a sample company, with any AI chat. No project, no setup and no facts of your own.
---

## Two steps

1. Get the sample file. It holds the office manual, one skill and the context pack for CogniATion, a fictional company.

   <div class="toolbar">
     <button type="button" class="btn primary office-copy" data-raw-url="https://raw.githubusercontent.com/gaidar/moffice/main/bundles/try-it.md">Copy the sample file</button>
     <a class="btn" href="https://raw.githubusercontent.com/gaidar/moffice/main/bundles/try-it.md">Open it as text</a>
     <span class="toolbar-status" role="status" aria-live="polite"></span>
   </div>

2. Start a new chat in your AI tool. Paste the file and the message below together, in one message. If the file is too long to paste, save it as a text file, upload it and send the message with it:

   ```
   Follow the office manual in the file I gave you. Use the skill "Write a sales one-pager". Read the context pack.
   Task: one page for professional services firms, aimed at the VP of people, for one-to-one use by sales.
   ```

## What you should get back

A one-pager in this format. Yours will differ in wording, because models vary. This one came from following the skill with the sample context pack, with the last section shortened.

<div class="output" markdown="1">
{% capture sample %}{% include sample-one-pager.md %}{% endcapture %}{{ sample }}
</div>

## What to look for

- **It used the facts it was given.** The 22% result comes from proof-points.md, marked Public. Corvane Software's result is left out, because the same segment has public proof.
- **It marked what it does not know.** `[Sales contact needed]` is a placeholder, not a made-up name.
- **It told you what it assumed.** The last section is your review list. Answer it and ask for a second draft.
- **Now judge it as a buyer.** The checks above only show it followed the rules. Would a VP of people care about the first line? Would your sales lead hand this over? That part is yours, and [Judge an output]({{ '/guides/judge-an-output.html' | relative_url }}) shows how.

If yours invents a customer or a number, tell it: "The office manual says never to invent facts. Remove anything not in the context pack."

## Try one more

Ask for something else from the same file, even though its skill is not loaded. The office manual tells the model how to handle a request with no skill:

```
Follow the office manual in the file I gave you. Write a short email inviting the same VP of people to a pilot call.
```

It should say that no skill covers this, name the closest one, write the email anyway and label it "No skill, ad hoc output".

Then see [more worked examples]({{ '/examples.html' | relative_url }}), or use it for your own company. Next come a first pass of the context pack, setup, your first skill and the cadence, and [Start here]({{ '/guides/start-here.html' | relative_url }}) walks you through them.
