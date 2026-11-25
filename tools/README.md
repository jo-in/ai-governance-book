This script exports the AI Guardrails book from the workspace root (`/Users/work/Antigravity/retrieval-v2`) into a Pandoc-ready Markdown file and then converts that into a Microsoft Word `.docx` document. All citations, references, and diagrams are processed during export.

---

### 1. Prerequisites (Current Machine Check)

* **`python3`** — already installed (`/usr/local/bin/python3`).
* **`pandoc` (required for `.docx` output)** — **not currently installed** on `PATH`. Install it via Homebrew:
  ```bash
  brew install pandoc
  ```
* **Mermaid CLI (optional, recommended for diagrams)** — `mmdc` is not installed globally, though `npx` is available (`/opt/homebrew/bin/npx`). The script falls back to `npx -y -p @mermaid-js/mermaid-cli mmdc`, but because there are 31 Mermaid diagrams in the manuscript, installing `mmdc` globally first is noticeably faster and avoids repeated `npx` overhead:
  ```bash
  npm install -g @mermaid-js/mermaid-cli
  ```
  *(Rendered diagrams are cached by content hash in `book/build/diagrams/`, so subsequent runs skip re-rendering unchanged diagrams.)*

---

### 2. Run a Full Book Export

From `/Users/work/Antigravity/retrieval-v2`:

```bash
python3 book/tools/export_docx.py
```

By default, this runs a three-step pipeline:
1. Validates all footnotes and bibliography links via [check_refs.py](file:///Users/work/Antigravity/retrieval-v2/book/tools/check_refs.py).
2. Assembles a Pandoc-ready Markdown manuscript at [manuscript_pandoc.md](file:///Users/work/Antigravity/retrieval-v2/book/build/manuscript_pandoc.md) (converting footnotes, internal bookmarks, GitHub alerts, page breaks, and rendering Mermaid diagrams to `book/build/diagrams/`).
3. Runs `pandoc` to generate **`book/build/enterprise-ai-guardrails.docx`** with a clickable Table of Contents (depth 2) and native Word footnotes.

---

### 3. Common Usage Examples

**Add author metadata and choose a custom output file:**
```bash
python3 book/tools/export_docx.py --author "Your Name" -o book/build/draft-v1.docx
```

**Export only selected chapters (supports numbers, comma lists, and inclusive ranges):**
```bash
python3 book/tools/export_docx.py --chapters 00 1-5 31 -o book/build/sample.docx
```

**Export quickly without rendering Mermaid diagrams (leaves `mermaid` blocks as code):**
```bash
python3 book/tools/export_docx.py --skip-mermaid
```

**Abort if any Mermaid diagram fails to render (strict CI/release check):**
```bash
python3 book/tools/export_docx.py --strict-mermaid
```

**Assemble Markdown only (skip calling `pandoc`):**
```bash
python3 book/tools/export_docx.py --markdown-only --skip-mermaid
```

---

### 4. Customizing Word Styling (Optional)

No custom Word template exists at `book/tools/reference.docx` yet. To customize fonts, headings, tables, margins, headers, or footers:

1. Generate Pandoc's starter template (requires `pandoc`):
   ```bash
   python3 book/tools/export_docx.py --init-template
   ```
2. Open `book/tools/reference.docx` in Microsoft Word or LibreOffice Writer, edit the built-in styles (`Normal` / `Body Text`, `Heading 1–3`, `Block Text`, `Footnote Text`, `Table`, and page margins/headers/footers), and save.
3. Re-run `python3 book/tools/export_docx.py` — it automatically picks up `book/tools/reference.docx` whenever the file exists (or pass `--reference-doc path/to/template.docx`).

---

### 5. Useful CLI Flags

| Flag | Purpose |
| :--- | :--- |
| `-o`, `--output PATH` | Output `.docx` path (default: `book/build/enterprise-ai-guardrails.docx`) |
| `--chapters SPEC ...` | Subset of chapters, e.g. `00 01 06` or `1-5` (default: all) |
| `--no-bibliography` | Exclude [bibliography.md](file:///Users/work/Antigravity/retrieval-v2/book/bibliography.md) |
| `--title` / `--subtitle` / `--author` / `--date` | Override Word document metadata and title page fields |
| `--no-toc` / `--toc-depth N` | Omit the TOC or change heading depth (default: `2`) |
| `--no-page-breaks` | Do not insert page breaks before each chapter and bibliography |
| `--skip-check` | Skip running [check_refs.py](file:///Users/work/Antigravity/retrieval-v2/book/tools/check_refs.py) before export |
| `--skip-mermaid` / `--strict-mermaid` | Skip diagram rendering, or fail hard if a diagram errors |
| `--mermaid-scale N` / `--mermaid-width PX` / `--mermaid-theme NAME` | Tune diagram DPI/size/theme (defaults: `3`, `1400`, `neutral`) |
| `--mermaid-cmd CMD` | Override the Mermaid CLI binary path (e.g. `'/opt/homebrew/bin/mmdc'`) |
| `--init-template` (`--force`) | Generate (or overwrite) the starter `book/tools/reference.docx` template |
| `--markdown-only` | Write `book/build/manuscript_pandoc.md` only and exit |