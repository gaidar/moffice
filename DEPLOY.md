# Deploy

The site is built and deployed by `.github/workflows/pages.yml` on every push to `main`. It builds PDFs for playbooks and guides in the workflow. PDFs are not committed. `bundles/` is committed, and the workflow fails if it does not match the skills and charters, so run `scripts/build-bundles.sh` and commit after you edit them.

## Current status

The repository is private until the release, and Pages is not enabled. The workflow still validates and builds on each push, then fails at the release tag check or the Pages step, and nothing deploys.

At the release, tag it as described under Release tag, make the repository public and apply the Pages setting below. Then re-run the workflow.

## One-time GitHub settings

1. **Pages source:** in the repository, go to Settings, then Pages. Under "Build and deployment", set Source to "GitHub Actions".
2. **Custom domain:** none is confirmed for this project, so there is no `CNAME` file. To add one, enter the domain under Settings, then Pages, add a `CNAME` file containing the domain, and change `url` and `baseurl` in `_config.yml`. `scripts/build-pdf.sh` also has the site address in it.

The repository must be public, or on a plan that allows Pages for private repositories. The toolbar's Copy full text and Download file buttons read from `raw.githubusercontent.com`, which works for anonymous visitors only on a public repository.

## Release tag

Copy full text, Download file and the download links in the guides read from the tag `v<VERSION>`, not from `main`, so a download matches the release its page belongs to. GitHub stays the only copy. The workflow stops if the tag is not on GitHub. Tag and push together:

```
git tag v0.1.0
git push --atomic origin main v0.1.0
```

A later edit reaches the site at once, and reaches the downloads only with the next version and tag. Open on GitHub still shows `main`.

## Published address

<https://gaidar.github.io/moffice/>

## Republishing after you edit

Edit the markdown, then commit and push to `main`. You can use the GitHub web editor. The workflow validates content first, and a validator error stops the deployment. See the Actions tab for the result and the exact error.

## Local build

```
python3 scripts/validate.py
bundle install
bundle exec jekyll build
python3 -m venv .venv && .venv/bin/pip install -r scripts/requirements-pdf.txt
scripts/build-pdf.sh
scripts/build-bundles.sh
```

Ruby 3.3 is what the workflow uses. The local output is in `_site/`.

## Versions

Bump `VERSION`, `office_version` in `_config.yml`, the `version` field in the content files and the tag in the download links together, and add a `CHANGELOG.md` entry. Then tag as above. The validator fails if content versions or download links do not match `VERSION`.
