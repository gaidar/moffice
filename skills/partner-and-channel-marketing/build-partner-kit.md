---
title: Build a partner kit
type: skill
function: partner-and-channel-marketing
owner: partner-marketing-manager
reads: [company, product, icp-and-segments, personas, messaging, proof-points, brand-voice, channels-and-tools]
you_bring: The partner's type and name, whether it refers or sells, who receives referrals, and any commercial terms to include.
also_for: [reseller materials, referral program, partner enablement, channel partner, partner leads, partners selling it wrong, reseller pitch, agency partner kit]
version: 0.1.0
updated: 2026-11-01
summary: Builds the messages and materials a partner needs to refer or sell the product accurately.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this when a partner will refer or sell your product and needs words they can use without calling you. Do not use it for a single joint campaign, which belongs in [Plan co-marketing with a partner](plan-co-marketing.md). For a page your own sales team hands to a buyer, use [Write a sales one-pager](../product-marketing-and-sales-enablement/write-sales-one-pager.md) instead.

## Inputs

- [[context-pack:company]]: the public name and the numbers that may be published.
- [[context-pack:product]]: what it does, what it is not, pricing, and roadmap limits.
- [[context-pack:icp-and-segments]]: who to send over, disqualifiers, triggers.
- [[context-pack:personas]]: messages and objections by role.
- [[context-pack:messaging]]: one-sentence description, pillars, words to avoid.
- [[context-pack:proof-points]]: proof the partner may repeat.
- [[context-pack:brand-voice]]: voice for the copy, logo rules.
- [[context-pack:channels-and-tools]]: approvers and hard rules.

The marketer supplies in the prompt: the partner's type and name, whether it refers or sells, who receives referrals, and any commercial terms to include. If the context pack holds nothing about partners, these facts come from the marketer or stay as placeholders.

## Procedure

1. Set the kit type from the partner's role. Refer: the partner makes an introduction and leaves the sale to you. Sell: the partner quotes and closes. If the role is not given, ask. A Sell kit adds pricing. A Refer kit leaves it out unless the marketer asks.
2. Write who to send over, as signs a partner can spot in conversation: company type, size, situation and triggers from icp-and-segments.md. Write who not to send over from the disqualifiers and what the product is not. Reword any term on the avoid list.
3. Write the short description: 30 words at most, built from the one-sentence description and one pillar.
4. Write three fit questions for the partner to ask, each based on a trigger or a daily problem from personas.md.
5. Copy the message from messaging.md for each role the partner will meet.
6. Write up to three objections and answers, from personas.md. Answers use only features in product.md and Public proof.
7. List proof the partner may repeat: Public items and publishable company numbers only. A partner passes material along outside any one-to-one sale, so leave out Sales only items. If nothing qualifies, write [public proof needed].
8. Write the do-not-say list: what the product is not, integrations it does not have, roadmap items, internal numbers, and any claim about competitors. Competitor questions go to you, not the partner.
9. Write the referral steps: what the partner sends, to whom, what happens next. If unknown, write [referral contact needed] or [response time needed].
10. Write the ready-to-send text in brand voice: one introduction email and one social post. Leave price out unless the marketer asks and the approver is listed.
11. List the naming and logo rules from brand-voice.md, and the approvals the kit needs from channels-and-tools.md.
12. Check the kit against the context pack: permission status, avoid list, roadmap, what the product is not, hard rules. Fix what contradicts it.
13. List everything assumed, estimated, inferred or unknown in the last section, using those labels.

## Output format

Everything above the last section goes to the partner. The last section stays with the marketer.

```
Status: Draft

## Kit type
<Refer or sell, and the partner>

## Short description
<Up to 30 words>

## Who to send over
Yes: <up to 4 signs>
No: <up to 4 signs>
Questions to ask: <3>

## Messages by role
| Role | Message, up to 20 words |

## Objections
| Objection | Answer, up to 30 words |

## Proof you may repeat
<Item, source date. Up to 5>

## Do not say
<Up to 6 items>

## How to refer
<Up to 4 numbered steps>

## Ready-to-send text
Introduction email: <up to 120 words>
Social post: <up to 60 words>

## Name and logo rules
<Up to 4 rules>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Could a partner decide who to send over without calling you?
- [ ] Is every proof item Public, with no Sales only or Internal only items?
- [ ] Are all numbers publishable in company.md or Public in proof-points.md?
- [ ] Does the do-not-say list cover what the product is not and the roadmap?
- [ ] Are competitor claims left out?
- [ ] Are the email and post within their word limits and in brand voice?
- [ ] Are the referral contact and response time filled in or visibly marked?

## Example (fictional company)

Status: Draft

**Kit type.** Refer. Partner: [partner name needed], an AI rollout consultancy.

**Short description.** CogniATion Coach is an AI chatbot that won't give you the answer, so you learn to find it. Learning leaders see progress by team.

**Who to send over.** Yes: knowledge-work companies, 300 to 5,000 employees, at least 100 people to train, after an AI assistant rollout or a client complaint about poor reasoning. No: fewer than 100 learners, wants a course library, wants scores on individuals for performance reviews. Questions to ask: Do junior staff check what the AI assistant says? Has a client complained about poor reasoning? Who owns learning and development?

**Messages by role.** Head of learning: show that training changed how people reason, not only that they finished it.

**Objections.** "Will people feel they are being watched?" Learning leaders see progress by team and never see an individual's conversation.

**Proof you may repeat.** 64 customer companies as of September 30, 2026. Median of 9 days from signed contract to first live session, 31 rollouts, January to September 2026. Lena Marsh quote, Brightmere Advisory.

**Do not say.** Not a general AI assistant, course library or learning management system. Not for hiring or performance decisions. No claim about raising intelligence. No future features. No competitor claims.

**How to refer.** Email [referral contact needed]. CogniATion replies in [response time needed].

**Ready-to-send text.** Email: Your junior staff have answers from the AI assistant. Can they defend them? CogniATion Coach makes people practice reasoning on real work problems. Want an introduction?

**Name and logo rules.** CogniATion, spelled exactly that way. The Coach on second mention. Logo on plain backgrounds only.

**Assumptions and open questions**

- Assumption: the partner refers and is a consultancy.
- Unknown: who at CogniATion receives referrals?

## How to run it

```
Use the skill "Build a partner kit". Read the context pack.
Task: <the partner's type and name, whether it refers or sells, who receives referrals, and any terms>.
```
