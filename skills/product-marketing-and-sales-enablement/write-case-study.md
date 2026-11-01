---
title: Write a case study
type: skill
function: product-marketing-and-sales-enablement
owner: product-marketing-manager
reads: [product, messaging, proof-points, brand-voice, channels-and-tools]
version: 0.1.0
updated: 2026-11-01
summary: Turns interview notes into a case study, starting with a permission check on the customer, each number and each quote.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you, the marketer, decide what to use.

## When to use

Use this when you have notes or a transcript from a customer interview and want a case study. Do not use it to find patterns across many customers; use [Synthesize customer research](../segmentation-icp-and-personas/synthesize-customer-research.md) instead. For a short item without a customer story, use [Write a sales one-pager](write-sales-one-pager.md).

## Inputs

- [[context-pack:product]]: what the product does and is not, to check the customer's words against it.
- [[context-pack:messaging]]: pillars and words to avoid.
- [[context-pack:proof-points]]: permission status for the customer, each result and each quote.
- [[context-pack:brand-voice]]: voice and rules for public copy.
- [[context-pack:channels-and-tools]]: who approves a customer story, and how long it takes.

The marketer supplies: the customer's name, the interview notes or transcript, the date of the interview, and where the case study will appear. Web, email or social means public. One-to-one means sales hands it to a named buyer. If not stated, treat it as public.

## Procedure

1. Run the permission check before writing anything. Look up the customer in proof-points.md and compare its status with the intended use:
   - Public: continue.
   - Sales only: continue only for one-to-one use. If the use is public, stop and offer to draft a one-to-one version instead. Keep limits such as no logo.
   - Pending, None, Internal only or not listed: stop. Return the permission check and the request list. Write the story only if the marketer says the copy is for the customer's own approval. In that case, mark the status "Customer approval copy, not for circulation".
2. Check each result and each quote separately. A customer's name permission does not cover a new number or quote. For each item in the notes:
   - Listed in proof-points.md with a fitting status: use as written there.
   - Not listed: keep it in the permission check as "Needs customer approval", and use it in the draft inside a marked placeholder such as [needs approval: quote from notes]. Never present it as cleared.
3. Sort the notes into situation, why they chose, rollout and result. Use only what the notes or proof-points.md say. If a section has nothing behind it, write a placeholder such as [before-state detail needed] and ask the marketer for it.
4. Do not tidy quotes beyond removing filler words. Never write a quote the customer did not say. If the wording changes meaning, ask.
5. Check every product statement in the customer's words against product.md. If the customer describes something the product does not do, leave it out and flag it under Unknown.
6. Write the headline: what happened, in at most 12 words, naming the result or the job. Do not write how we feel about it.
7. Write the sections, keeping the customer as the subject: at most 80 words each for situation, why they chose, rollout and result. Give each number's period and sample where the notes have them.
8. Check the draft against the context pack: permission status, brand voice, words to avoid, what the product is not.
9. List the approval route from channels-and-tools.md for this customer and any pricing mention. A case study goes through this route even if the customer's name is already public, because the story is new. Items already approved in proof-points.md need no new customer approval.
10. List every assumption, inference and gap in the last section. Leave any blank field as a placeholder in square brackets, and never invent a detail to complete a story.

## Output format

```
Status: Draft
Customer: <name>
Intended use: <Public or one-to-one>

## Permission check
| Item | proof-points.md status | Fits this use? | Action |

## Case study (400 words maximum; this total governs if the field limits add up to more)
Headline: <max 12 words>
At a glance: <industry, size, result, max 25 words>
The situation: <max 80 words>
Why they chose: <max 80 words>
The rollout: <max 80 words>
The result: <max 80 words, with period and sample>
Quote: <exact words, name, title, company>
Next step: <max 15 words>

## Approval route
| Step | Approver | Typical time |

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Was the permission check done first, and does it cover the customer, each number and each quote?
- [ ] Does each item's status fit the intended use?
- [ ] Are quotes the customer's own words?
- [ ] Is every detail in the story found in the notes or proof-points.md?
- [ ] Are items without approval shown as marked placeholders?
- [ ] Is every number shown with its period and sample where known?
- [ ] Is the customer's approval route listed, then the internal approver?
- [ ] Is it free of hype and of words on the avoid list?

## Example (fictional company)

**Status:** Draft

**Customer:** Brightmere Advisory

**Intended use:** Public

**Permission check**

| Item | Status | Fits? | Action |
|---|---|---|---|
| Name and logo | Public, June 2026 | Yes | Use |
| Lena Marsh quote | Public, June 2026 | Yes | Use as written |
| 22% client memo reasoning result | Public, June 2026 | Yes | Use as written |
| Details from interview notes | Not listed | Not yet | Needs customer approval |

**Case study**

**Headline:** Brightmere Advisory's analysts raised client memo reasoning scores 22% in one quarter

**At a glance:** Professional services, 400 learners. Analysts raised their average score on client memo reasoning by 22% in one quarter of 2026.

**The situation:** [Before-state detail needed from interview notes]

**Why they chose:** [Reason needed from interview notes]

**The rollout:** [Detail needed from interview notes]

**The result:** Brightmere Advisory's analysts raised their average score on client memo reasoning by 22% in one quarter of 2026, as measured by Brightmere's partners.

**Quote:** "My analysts stopped asking the bot for the answer and started defending their own." Lena Marsh, head of learning, Brightmere Advisory

**Next step:** Start an 8-week paid pilot for up to 40 learners.

**Approval route**

| Step | Approver | Typical time |
|---|---|---|
| 1 | Brightmere Advisory, new story and details | 2 weeks for both steps |
| 2 | Marta Ilves, CEO | Included above |

**Assumptions and open questions**

- Assumption: no interview notes were supplied for this example, so sections wait on them. Any learner's conversation or score in the notes stays out, per the hard rule.
- Unknown: Can you paste the interview notes, how many analysts does the 22% cover, and who at Brightmere signs off on the new details?

## How to run it

```
Use the skill "Write a case study". Read the context pack.
Task: <the customer, where it will appear; interview notes pasted below>.
```
