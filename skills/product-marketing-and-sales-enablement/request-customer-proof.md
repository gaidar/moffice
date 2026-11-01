---
title: Request customer proof
type: skill
function: product-marketing-and-sales-enablement
owner: product-marketing-manager
reads: [proof-points, icp-and-segments, messaging, brand-voice, channels-and-tools]
you_bring: The claim or segment that needs proof, where it will appear, and who you know at the customer.
also_for: [customer quote, customer testimonial, logo permission, permission to use a customer name, reference customer, need proof for a claim, ask a customer for a number]
version: 0.1.0
updated: 2026-11-02
summary: Writes the ask to a customer for a quote, number or logo, with who to ask, the message, the permission wording and the entry for proof-points.md.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when a claim needs a customer quote, number or logo that you do not have permission to use. Do not use it to write the full story; use [Write a case study](write-case-study.md) once you have notes. To learn what customers think rather than clear what they said, use [Write an interview guide](../segmentation-icp-and-personas/write-interview-guide.md).

## Inputs

- [[context-pack:proof-points]]: what is on file, permission status, the format of an entry.
- [[context-pack:icp-and-segments]]: segment priority.
- [[context-pack:messaging]]: pillars and which claims lack cleared proof.
- [[context-pack:brand-voice]]: voice for the message.
- [[context-pack:channels-and-tools]]: who approves customer items, how long it takes, hard rules.

The marketer supplies the claim or segment, where the proof would appear, and the date it is needed. Optional: customers and contacts to consider, anything a customer said word for word, and any number with its period, sample and who measured it.

## Procedure

1. Name the gap: one claim, one segment, one intended use. If none is given, list the pillars in messaging.md with no Public proof for the top segment, and ask which comes first.
2. List what proof-points.md holds for the gap. If a Public item covers the use, say no request is needed and stop. If a request is Pending, write one reminder rather than a second ask, and keep the item out of all drafts.
3. Choose who to ask, up to 3 customers, ranked by same segment, then a result on file, then a known contact (a starting rule). Use only names from proof-points.md or the marketer. Ask whether any has an open dispute or renewal.
4. Name who can approve, since a company name, number or logo may need someone senior: [customer approver needed] if unknown. Name the sender, or [sender needed].
5. Choose the smallest ask that fills the gap, up to 3 items (a starting rule). Prefer widening an existing permission, then an exact quote, a number, a logo. Approval for one item does not cover the next.
6. Set the exact text, in the customer's own words or number. Never write a quote and offer it as theirs. With no words on file, ask one question they can answer themselves. Give each number's period, sample and who measured it, or [period needed].
7. Write the message in at most 120 words: the exact text, where it would appear, a reply date, and that saying no changes nothing. Offer no discount or favor unless the marketer supplies one. The marketer sends it.
8. Write the permission wording as a reply they can copy: item, credit, uses, logo and who is approving. Only a written reply counts. The wording is a starting point for any legal review on either side.
9. Write the proof-points.md entries in that file's format: now, if yes, if no. The current status holds until the written reply arrives. Use only the status values the file defines.
10. Set the dates: send, one reminder after 5 business days (a starting rule), and the approval route from channels-and-tools.md. If the needed date leaves less than the typical time, say so.
11. Check the draft against the context pack: permission status, internal-only numbers, words to avoid, brand voice, hard rules.
12. List everything assumed or unknown in the last section.

## Output format

```
Status: Draft
Gap: <claim, segment, intended use>

## On file
| Item | Status | Covers this use? |

## Who to ask
| Rank | Customer and person | Who approves | Why them | Sender |

## The ask
<Each item: exact text or number, credit, where it would appear>

## Message
Subject: <50 characters at most>
Body: <120 words at most>

## Permission wording
"<reply they can copy, up to 60 words>"

## Entry for proof-points.md
Now: <item, current status, then "pending, requested <month and year>">
If yes: <"Permission: <status>, approved <month and year> by <name, title>">
If no: <what stays, or "Permission: none">

## Route and dates
| Date | Step | Owner |

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Is every customer and person from proof-points.md or the marketer?
- [ ] Is every quote the customer's own words, and every number given with its period and sample?
- [ ] Does the message say that saying no changes nothing?
- [ ] Does the permission wording cover item, credit, uses, logo and approver?
- [ ] Does the entry keep the current status until a written reply arrives?
- [ ] Do the dates allow the typical approval time?

## Example (fictional company)

**Status:** Draft

**Gap:** Pillar 3, you can see reasoning improve, software companies, website.

**On file**

| Item | Status | Covers this use? |
|---|---|---|
| Corvane Software result and quote | Sales only, no logo | No, not online |

**Who to ask**

| Rank | Customer and person | Who approves | Why them | Sender |
|---|---|---|---|---|
| 1 | Corvane Software, Sam Oduya, VP engineering | [customer approver needed] | Same segment, proof on file | [sender needed] |

**The ask:** public use of Quote 2 and Result 3, credit as already approved. Logo, yes or no.

**Message**

Subject: Could we use your words on our website?

Body: Sam, our sales material carries this quote from you, approved in August: "Managers argue about the assumption now, not about who is senior." May we also use it on our website, with the result that 120 engineering managers went from 2.6 to 3.4 out of 5 in 12 weeks? If you say no, nothing changes. Could you reply by November 18?

**Permission wording:** "Yes, CogniATion may use this quote and result on its website and in ads, credited to me by name and title. Logo: yes or no. I can approve this for Corvane Software."

**Entry for proof-points.md**

Now: Quote 2 and Result 3. Permission: sales only, approved August 2026. Public use: pending, requested November 2026.

If yes: Permission: public, approved [month and year] by Sam Oduya, VP engineering.

If no: Stays sales only.

**Route and dates:** November 4, send. November 11, reminder. Then Marta Ilves, CEO. Allow 2 weeks.

**Assumptions and open questions**

- Assumption: all dates, and that the website is the use.
- Unknown: has Haldane Ridge Capital answered the October request? It stays out of all drafts until then.

## How to run it

```
Use the skill "Request customer proof". Read the context pack.
Task: draft the request for <the claim or segment that needs proof>, for use on <where it will appear>, needed by <date>.
```
