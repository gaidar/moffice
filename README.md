# Marketing Office

A free, open source playbook of skills and agent roles that you load into Claude, ChatGPT/Codex, Grok or Google Gemini on a personal subscription, to run a tech company's marketing function alone. No servers, no API keys, no code.

The office produces drafts, plans, analyses and reviews. It does not know your market. You decide.

Website: <https://gaidar.github.io/moffice/>. See [DEPLOY.md](DEPLOY.md) for the deployment status and steps.

## Start

Open [Start here](guides/start-here.md). It takes you through one setup guide, the context pack and your first skill. The target is under one working day. That is an estimate from the steps, not a measured result.

## What is in the repo

| Folder | What it holds |
|---|---|
| `office/` | Office manual, output conventions, glossary, agent roster |
| `context-pack/templates/` | 10 blank context pack files |
| `context-pack/example-cogniation/` | The same 10 files, filled in for a fictional company |
| `agents/` | 14 agent role charters |
| `skills/` | 50 skills, in a folder per function |
| `playbooks/` | Weekly, monthly, quarterly, first week, launch, campaign lifecycle |
| `guides/` | Start here, four vendor setup guides, and guides for running the office |
| `bundles/` | All skills and all charters in one file each, generated, for vendors with a low file limit |
| `scripts/` | Validator, PDF build, bundle build |

Everything is plain markdown, here on GitHub. Playbooks and guides also come as PDFs on the website.

## What it does not do

It has limited connectors to external tools. You may have to write your own skills to publish landing pages in your CMS, pull data from your CRM or set up email lists. See [Write your own skill](guides/write-your-own-skill.md). There is no hosted service.

## Working on the repo

```
python3 scripts/validate.py
bundle exec jekyll build
scripts/build-pdf.sh
scripts/build-bundles.sh
```

Details are in [CONTRIBUTING.md](CONTRIBUTING.md). Assumptions behind this build are in [ASSUMPTIONS.md](ASSUMPTIONS.md).

## License and author

Apache License 2.0, see [LICENSE](LICENSE). Author and maintainer: Gaidar Magdanurov.

All company names in the examples are fictional. Vendor names belong to their owners. This project is not affiliated with or endorsed by any vendor.
