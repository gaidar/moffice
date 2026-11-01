---
title: Set tracking conventions
type: skill
function: marketing-ops
owner: marketing-operations-manager
reads: [channels-and-tools, goals-and-kpis, icp-and-segments]
you_bring: Current UTM values or campaign names if any exist, each platform in use, and any limits on values.
also_for: [utm, messy utms, campaign naming, link tagging, tracking links, reports do not agree, cannot track leads, source is unknown]
version: 0.1.0
updated: 2026-11-01
summary: Sets UTM and campaign naming rules and a tracking sheet format, so the numbers can be read later.
---

**Draft only.** The model does not know your market. It produces a draft, plan, analysis or review, and you decide what to use.

## When to use

Use this once before running paid or email campaigns, and again when a channel is added or reports stop agreeing. Do not use it to read the resulting data, which belongs to [Read attribution](../analytics-and-campaign-evaluation/read-attribution.md), or to decide which metrics to display, which belongs to [Specify a dashboard](../analytics-and-campaign-evaluation/specify-dashboard.md).

## Inputs

- [[context-pack:channels-and-tools]]: owned and paid channels, tools and hard rules on tracking and names.
- [[context-pack:goals-and-kpis]]: the attribution model and the campaigns planned this quarter.
- [[context-pack:icp-and-segments]]: segment names, for the segment codes.

The marketer pastes into the chat:

- Current UTM values or campaign names, as an export from the web analytics tool, if any exist.
- The name of each ad and social platform in use, for source values.
- Any limits a tool puts on parameter values.

## Procedure

1. List every channel from channels-and-tools.md, plus any the marketer adds, with one row each in the allowed values table.
2. Copy these format rules into the output as written: lowercase only, hyphens between words, no spaces or special characters, no personal data, no customer names, no competitor names, 40 characters at most per value. Link parameters can be seen by anyone who clicks. The 40-character cap is a starting rule the marketer can change.
3. Set the parameters. Source, medium and campaign are required on every link from outside the website. Source is the site or sender. Medium comes from the allowed list only. Campaign follows the pattern in step 5. Content is required when a campaign has more than one variant. Term is used for search ads only, and holds the keyword theme.
4. Build the allowed values table. Each channel gets one medium and one source. Use the marketer's platform names for source. If none was supplied, write [platform name needed]. A new value goes into the table before it is used on any link.
5. Set the campaign pattern: year and quarter, segment code, then topic, such as [yyyy]q[n]-[segment]-[topic]. Give each segment in icp-and-segments.md a short code, and use "all" for campaigns across segments. The same name goes in the CRM, the marketing automation tool and the ad account, so one campaign has one name everywhere.
6. Write the exceptions. Never tag links between pages on the company's own website, since that restarts the visit and overwrites its source. Do not tag links in organic search results. For print and event material, use a short link or code that redirects to a tagged link, with the medium for events.
7. Write the attribution requirement. If goals-and-kpis.md reports first and last touch, the marketer must confirm that the CRM stores both on each lead. Record this as unknown until confirmed.
8. Write the tracking sheet format with these columns in this order: date, campaign, channel, source, medium, content, term, destination page, full link, owner, tested (yes or no). Add one row per link. Set the rule: no link goes live until it has been clicked and the visit appears in the web analytics tool.
9. Map old values to new ones when the marketer supplied existing values. Old data keeps its old names, and the map is used for reading across the change.
10. Check the draft against the context pack: every channel has values, every segment has a code, and hard rules on ad spend and names are reflected. If a needed field is blank, leave a visible placeholder and ask in the last section. Never invent.
11. List every assumption, estimate, inference and unknown in the last section.

## Output format

```
Status: Draft

## Format rules
<The rules from the procedure, as up to 8 bullets.>

## Allowed values
| Channel | Source | Medium |
<One row per channel.>

## Campaign names
<Pattern, segment codes and up to 3 real campaign names. Max 60 words.>

## Parameter rules
| Parameter | Required when | Value |
<One row each for source, medium, campaign, content and term.>

## Exceptions
<Up to 5 bullets, max 25 words each.>

## Tracking sheet format
| date | campaign | channel | source | medium | content | term | destination page | full link | owner | tested |
<One filled sample row, then the go-live rule in one sentence.>

## Assumptions and open questions
- Assumption: <what you took as true, and why>
- Estimate: <the number, and how you worked it out>
- Inference: <what you concluded, and from which inputs>
- Unknown: <what you need from the marketer, as a question>
```

## Quality checklist

- [ ] Does every channel in channels-and-tools.md have allowed values?
- [ ] Does every segment have a code?
- [ ] Are source, medium and campaign required on every outside link?
- [ ] Are links between the company's own pages left untagged?
- [ ] Are customer and competitor names kept out of all values?
- [ ] Is there a sample row with a complete, working link format?
- [ ] Is there a go-live rule that requires a tested link?

## Example (fictional company)

Status: Draft

Assumption: source values stand in for platform names, which CogniATion's context pack leaves out. The topic, page path, content and term values are illustrative.

**Format rules**

- Lowercase, hyphens between words, no spaces or special characters.
- No personal data, customer names or competitor names.
- 40 characters at most per value.

**Allowed values**

| Channel | Source | Medium |
|---|---|---|
| Search ads | search-engine | paid-search |
| Professional social network ads | pro-social | paid-social |
| Company social page | pro-social | organic-social |
| Newsletter | newsletter | email |
| Video channel | video-channel | organic-video |
| Regional conference | ld-conference | event |

**Campaign names**

Pattern: year and quarter, segment, topic. Codes: proserv, software, finserv. Examples: 2027q1-proserv-defend-the-memo, 2027q1-all-ld-conference.

**Parameter rules**

| Parameter | Required when | Value |
|---|---|---|
| Source, medium, campaign | Every outside link | As above |
| Content | More than one variant | Variant name |
| Term | Search ads only | Keyword theme |

**Exceptions**

- No tags on links between cogniation.example pages.
- Conference print material uses a short link that redirects to a tagged link, with medium event.

**Tracking sheet format**

Sample row: 2027-01-15, 2027q1-proserv-defend-the-memo, search ads, search-engine, paid-search, defend-answers-a, critical-thinking, /professional-services, cogniation.example/professional-services?utm_source=search-engine&utm_medium=paid-search&utm_campaign=2027q1-proserv-defend-the-memo&utm_content=defend-answers-a&utm_term=critical-thinking, marketer, no.

No ad spend until the link is tested, per the tracking limit in channels-and-tools.md.

**Assumptions and open questions**

- Unknown: Does the CRM store first and last touch on each lead?

## How to run it

```
Use the skill "Set tracking conventions". Read the context pack.
Task: <which channels, and any limits a tool puts on values>.
<paste current values and platform names here>
```
