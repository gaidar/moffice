# Marketing Office

A free, open source playbook of skills and agent roles that you load into Claude, ChatGPT/Codex, Grok or Google Gemini on a personal subscription, to run marketing alone at a sales-led B2B company. No servers, no API keys, no code.

The office produces drafts, plans, analyses and reviews. It does not know your market. You decide.

Website: <https://marketingoffice.net/>. See [DEPLOY.md](DEPLOY.md) for the deployment status and steps.

## Start

Open [Start here](guides/start-here.md), which starts from the job you need to finish and takes you through the facts it needs, one setup guide and your first draft. To see a result first, [try it in 10 minutes](try.md) with a sample company. If marketing does not exist yet at your company, also see [Starting from zero](playbooks/from-zero.md). The times are estimates from the steps, not measurements.

## What is in the repo

| Folder | What it holds |
|---|---|
| `office/` | Office manual, output conventions, glossary, agent roster, workboard |
| `context-pack/templates/` | 10 blank context pack files |
| `context-pack/example-cogniation/` | The same 10 files, filled in for a fictional company |
| `agents/` | 14 agent role charters |
| `skills/` | 57 skills, in a folder per function |
| `playbooks/` | Starting from zero, first week, weekly, monthly, quarterly, launch, campaign lifecycle |
| `guides/` | Start here, four vendor setup guides, and guides for running the office |
| `bundles/` | Generated. All skills, all charters and playbooks, and all context pack templates in one file each, plus the sample file for the trial |
| `scripts/` | Validator, site check, PDF build, bundle build |

Everything is plain markdown, here on GitHub. Playbooks and guides, except the FAQ, also come as PDFs on the website.

## What it does not do

It covers getting and converting new business, with sales support. Retention, expansion, pricing and product-led growth are outside the current library. It ships no connectors to external tools. You may have to write your own skills to publish landing pages in your CMS, pull data from your CRM or set up email lists. See [Write your own skill](guides/write-your-own-skill.md). There is no hosted service.

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

All companies in the examples are invented. A web search cannot prove that a name is unused. Vendor names belong to their owners. This project is not affiliated with or endorsed by any vendor.
