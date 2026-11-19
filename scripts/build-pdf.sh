#!/usr/bin/env bash
# Write pdf/**/*.pdf mirroring the markdown paths. Needs Python with the packages
# in scripts/requirements-pdf.txt, which provide pandoc and the Typst PDF engine.
# Set PYTHON to choose an interpreter. Defaults to .venv/bin/python if present.
set -euo pipefail
cd "$(dirname "$0")/.."

python_bin="${PYTHON:-}"
if [ -z "$python_bin" ]; then
  if [ -x .venv/bin/python ]; then python_bin=".venv/bin/python"; else python_bin="python3"; fi
fi

"$python_bin" - <<'PY'
import pathlib, re, shutil, subprocess, sys, tempfile
import pypandoc, typst

# The published address comes from _config.yml, so a domain change needs no edit here.
config = pathlib.Path("_config.yml").read_text(encoding="utf-8")
url = re.search(r'^url:\s*"?([^"\s]+)', config, re.M).group(1).rstrip("/")
baseurl = re.search(r'^baseurl:\s*"?([^"\s]*)', config, re.M)
site = url + (baseurl.group(1) if baseurl else "").rstrip("/") + "/"
pandoc = pypandoc.get_pandoc_path()
# PDFs only for the procedures people read. Everything else is a text file on GitHub.
sources = sorted(
    p for top in ["playbooks", "guides"]
    for p in pathlib.Path(top).glob("*.md") if p.name != "faq.md"
)
out_root = pathlib.Path("pdf")
if out_root.exists():
    shutil.rmtree(out_root)

failures = []
with tempfile.TemporaryDirectory() as tmp:
    tmp = pathlib.Path(tmp)
    # Relative .md links would be dead in a PDF, so point them at the published page.
    lua = tmp / "links.lua"
    # Paths are resolved here, so a PDF never links to ".../guides/../office/...".
    # agent-roles.md is the one page whose URL differs from its file name.
    lua.write_text(
        'local function normalize(path)\n'
        '  local parts = {}\n'
        '  for seg in path:gmatch("[^/]+") do\n'
        '    if seg == ".." then\n'
        '      if #parts > 0 then table.remove(parts) end\n'
        '    elseif seg ~= "." then\n'
        '      table.insert(parts, seg)\n'
        '    end\n'
        '  end\n'
        '  return table.concat(parts, "/")\n'
        'end\n'
        'function Link(el)\n'
        '  if not el.target:match("^%a+:") and not el.target:match("^#") then\n'
        '    local target = el.target:gsub("%.md", ".html")\n'
        '    target = normalize("PAGE_DIR/" .. target)\n'
        '    target = target:gsub("^agent%-roles%.html", "agents.html")\n'
        '    el.target = "SITE_ROOT" .. target\n'
        '  end\n'
        '  return el\n'
        'end\n'
    )
    # Left-aligned, unjustified text, and tables that can split across pages.
    style = tmp / "style.typ"
    style.write_text(
        "#set par(justify: false)\n"
        "#set text(hyphenate: false)\n"
        "#show figure: set block(breakable: true)\n"
        "#show table.cell: set align(left)\n"
        "#show table.cell: set text(size: 9pt)\n"
    )
    for src in sources:
        target = out_root / src.with_suffix(".pdf")
        target.parent.mkdir(parents=True, exist_ok=True)
        typ = tmp / (src.as_posix().replace("/", "__") + ".typ")
        lua_text = lua.read_text().replace("PAGE_DIR", src.parent.as_posix()).replace("SITE_ROOT", site)
        lua_file = tmp / "links-current.lua"
        lua_file.write_text(lua_text)
        # Pandoc reads "[[context-pack:x]]: text" as a link definition and drops the line.
        prepared = tmp / "current.md"
        prepared.write_text(re.sub(r"\[\[context-pack:([a-z-]+)\]\]", r"\1.md", src.read_text(encoding="utf-8")), encoding="utf-8")
        try:
            subprocess.run(
                [pandoc, str(prepared), "-f", "markdown-smart", "-t", "typst", "-s", "--wrap=none",
                 "--columns=2000", "--include-before-body", str(style),
                 "--lua-filter", str(lua_file), "-o", str(typ)],
                check=True, capture_output=True, text=True,
            )
            typst.compile(str(typ), output=str(target))
        except Exception as exc:  # keep going, report at the end
            detail = getattr(exc, "stderr", "") or str(exc)
            failures.append(f"{src}: {detail.strip()[:300]}")

built = len(list(out_root.rglob("*.pdf")))
print(f"build-pdf: wrote {built} of {len(sources)} PDFs to pdf/")
for line in failures:
    print(f"build-pdf: FAILED {line}")
sys.exit(1 if failures else 0)
PY
