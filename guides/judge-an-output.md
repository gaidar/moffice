---
title: Judge an output
type: guide
version: 0.1.0
updated: 2026-11-02
summary: How to tell whether a draft is a good idea, not only whether it followed the rules, when you have never been the senior reviewer.
---

A draft can pass every check and still be wrong. This guide gives you the questions a senior reviewer would ask, so you can catch that without their years of experience.

## Who it is for

A marketer who is told to treat the office as a capable new hire, which makes you the senior reviewer, and who has not been one before. You do not need to know the answers. You need to know what to ask, and who to ask next.

## What you need

- A draft from a skill or an agent role, with its Assumptions and open questions section left in.
- Your own numbers from last quarter, if you have them.
- About 15 minutes for a draft that matters. This is an estimate.

## Steps

1. **Know what the rules checks prove.** A skill's Quality checklist and [Review any output](../skills/marketing-ops/review-any-output.md) check facts, permissions and format. They show that the draft matches your context pack and breaks no hard rule. They do not show that the idea is good, that a number is high enough, or that a buyer will care. A clean review means the draft is ready for you to judge. It does not mean someone senior has agreed with it.

2. **Read the brackets, then the assumptions.** A bracket such as `[customer quote needed]` means the model had no fact and did not invent one. That is the office working. Many brackets mean a thin context pack, not a broken tool. For each one, get the fact, cut the claim, or leave it for later.

   Then read Assumptions and open questions before the body. Each Assumption and Estimate there is something you are being asked to accept. A big decision often rests on one short line in that list.

3. **Ask five questions of any recommendation.**

   - **What would have to be true?** Write the conditions out as sentences, then check the weakest one first.
   - **What is it based on?** Your own numbers, one quarter, a small sample, an average across very different things, a starting rule, or only the model's reasoning?
   - **What is the cheapest test?** Look for something smaller than the full spend: a CRM export, a call with a rep, or a small amount for a few weeks.
   - **Who would disagree?** Name the person. Then ask them before the draft is final. Their objection is usually more useful than their approval.
   - **What will you do if it fails?** You want a date, a number and an action. If there is no answer, you have a hope and not a plan.

4. **Judge a number when you have no benchmark.** Is 20% MQL to SQL fine or a crisis? The office will not tell you, because an outside figure may not fit your definitions or your market. Compare it three ways:

   - **With your own last quarter.** Use the same definition. Ask how far it moved, and what changed.
   - **With a peer in another company.** Ask how they define the stage before you compare the number, and what they would worry about in your place. Keep your internal numbers out of it.
   - **With sales.** Ask: "Of the last 10 leads I sent you, how many were worth the call?"

   If the three disagree, call the number unknown and say so.

5. **Show it to the person who can see what you cannot.** Show it early, and ask one direct question.

   | The output | Show it to | Ask |
   |---|---|---|
   | Goals, budget, priorities | Your CEO | "Which would you choose, and what would you drop?" |
   | Lead rules, sales material | Your sales lead or a rep | "Which line would you cross out?" |
   | Product claims | Your product lead | "Is any of this untrue, or about to change?" |
   | Positioning, messaging | A rep, then a customer who has agreed to talk | "Does this sound like the problem you have?" |
   | A plan you are unsure of | A peer in another company, with internal numbers removed | "What would you ask me about this?" |

6. **Push back on the model.** Paste these into the same chat as the draft:

   ```
   Argue against this recommendation. Give the three strongest reasons it is wrong.
   ```

   ```
   Which of your claims rest only on my context pack and which on your assumptions? List them in two columns.
   ```

   ```
   What would have to be true for this to work? Mark each item known, assumed or unknown.
   ```

   ```
   What numbers would you need from me to be confident in this, and what would change your answer?
   ```

   Treat the replies as a list of things to check, not as a verdict. If the model changes its answer only because you pushed, ask what new fact made it change.

## Worked example: a plausible draft that is wrong

CogniATion is the sample company. Its $70,000 budget, its 26% MQL to SQL rate, its 90 SQL goal and its approver come from [its example pack](../context-pack/example-cogniation/goals-and-kpis.md). The MQL and SQL counts by channel are illustrative, and the channel spend assumes the pack's monthly amounts ran for the whole of last quarter.

The marketer asks the head of marketing role where the quarter's money should go, and pastes spend and MQLs by channel, because that is what the report shows. The draft, shortened:

```
Status: Draft
Recommendation: put $42,000 of the $70,000 budget into professional social network ads.
Why: the lowest cost per MQL last quarter, $120 against $375 for search ads.
Estimate: $42,000 / $120 = 350 MQLs. 350 x 26% = 91 SQLs, which meets the goal of 90.
Approval: over $5,000, so Marta Ilves, CEO, 3 days.
Assumption: the 26% rate applies to every channel.
```

Every fact traces to the pack or to what was pasted. The arithmetic is right, the approver is right, and no permission or hard rule is broken. A review of facts, permissions and format finds no blocker. It is still a bad idea, and the five questions show why.

**What would have to be true?** MQLs from these ads convert at 26%. The $120 holds when spend goes from $12,000 to $42,000. One sales development representative can call all of them.

**What is it based on?** The 26% is a company-wide average, which is the line in the assumptions. The marketer pulls last quarter from the CRM by channel, with SQLs added:

| Channel | Spend | MQLs | Cost per MQL | SQLs | MQL to SQL | Cost per SQL |
|---|---|---|---|---|---|---|
| Professional social network ads | $12,000 | 100 | $120 | 5 | 5% | $2,400 |
| Search ads | $15,000 | 40 | $375 | 16 | 40% | $938 |

At 5%, 350 MQLs is about 18 SQLs, not 91. The cheapest channel per MQL is the most expensive per SQL.

**What is the cheapest test?** The CRM export, which cost nothing and has already changed the answer. Next comes a small increase on search ads for a few weeks, because $938 per SQL may not hold at a higher spend either.

**Who would disagree?** Tom Ferrant, head of sales. An illustrative reply: "Those people downloaded two guides. Most of them are not asking for anything." The pack's MQL definition does count two downloads, so this is worth checking.

**What will you do if it fails?** The draft does not say. As written, $42,000 is spent by March 31 with no point at which to stop. The marketer adds a date to read SQLs by channel, and a rate below which the rest of the money moves.

What goes to Marta is not a better answer, but a better question: the table, the small test, and a decision on whether to fund it. [Allocate the budget](../skills/budget-and-planning/allocate-budget.md) would have helped too, since it ranks channels by pipeline per dollar and caps any line, but only with pipeline by channel pasted in.

## What success looks like

For any recommendation you pass on, you can say in your own words what it rests on, who disagrees and what you will do if it fails. You can separate "the facts check out" from "this is a good idea". When you do not know, you can say so, along with how you plan to find out.

## Troubleshooting

- **The draft is full of brackets.** That is normal for a thin pack. Each bracket names the section or the person to go to next. See [Fill the context pack](fill-the-context-pack.md#what-you-will-likely-be-missing).
- **You have no numbers from last quarter.** Then this quarter sets your baseline. Ask sales in the meantime, and label any recommendation as a bet to test.
- **You have no peer to ask.** Try a former colleague, or a rep who has worked at another company. Your CEO may know someone. Keep internal numbers out of the conversation.
- **The model agrees with every objection.** Start a new chat, paste only the draft, and paste the "Argue against" prompt. Then ask: "What evidence would change your mind?"
- **You found a problem and cannot tell how serious it is.** Ask how much it would cost to undo. If little, run the small test. If a lot, take it to your CEO, with the question you could not answer.
- **You are still not sure.** Say so when you show it: "I checked the facts. I am not sure about the judgment. It rests on these two things." A senior person will take that over false confidence.
- **The words are unfamiliar.** See [the glossary](../office/glossary.md).
