---
title: Contributing
type: contributing
version: 0.1.0
updated: 2026-11-01
summary: How to report a problem, suggest a change or add a skill.
---

## Report a problem

Open [an issue](https://github.com/gaidar/moffice/issues/new). The most useful reports are these:

- A vendor setup step that no longer matches what you see. Include the guide, the step number and the date.
- A skill whose output misses its own template.
- A fact stated as true that is not verified.

## Suggest a change

Every page is a plain markdown file. Click Open on GitHub in the page toolbar, then use the edit button to propose a change. GitHub creates the pull request for you, and you need no local setup.

## Rules for all content

The validator enforces most of these, and it runs on every push.

- Sentence-case headings. En dashes or commas, never long dashes. US English.
- One term per concept. See [the glossary](office/glossary.md).
- No word from the banned list in `scripts/validate.py`.
- No real company names in examples. Use CogniATion, the fictional company in [the example pack](context-pack/example-cogniation/company.md). Vendor names are allowed where a guide needs them.
- No invented facts, sources, quotes, dates or numbers. Label anything unverified as an assumption, estimate, inference or unknown.
- No testimonials and no claims about results.
- Every skill and agent role says that it drafts and the marketer decides.

## Adding or changing a skill

1. Follow the format in [Write your own skill](guides/write-your-own-skill.md). The section headings and their order are fixed.
2. Keep the skill to 500–1,200 words, with an example of 150–300 words.
3. Set `owner` to one agent role. List the skill in that role's charter, under Owns.
4. List the context pack files in `reads`, and reference each one in Inputs like this: `[[context-pack:messaging]]`.
5. The marketing reviewer owns review skills only.
6. Do not add near-duplicates. Extend an existing skill if you can.

## Changing a vendor guide

Vendor-specific steps live only in the setup guides. State a vendor fact only if you read it on the vendor's own page, and update the guide's Verification section with the URL and date. Anything you could not check is marked "Unverified – check the vendor help page".

## Checking your work

These steps are optional and need a terminal. A maintainer can run them for you.

```
python3 scripts/validate.py                     # content rules, standard library only
bundle install && bundle exec jekyll build      # site, needs Ruby 3.3
python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements-pdf.txt
scripts/build-pdf.sh                            # PDFs
scripts/build-bundles.sh                        # bundles, commit the result
```

## License

By contributing, you agree that your contribution is licensed under the [Apache License 2.0](https://github.com/gaidar/moffice/blob/main/LICENSE).
