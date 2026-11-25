#!/usr/bin/env python3
"""Export the book's Markdown chapters and Annotated Bibliography to Word (.docx) via Pandoc.

Pipeline:
  1. Validate footnotes and bibliography links using book/tools/check_refs.py.
  2. Assemble a Pandoc-ready Markdown manuscript in book/build/manuscript_pandoc.md:
     - Convert HTML <a id="key"></a> anchors to native Pandoc bookmarks []{#key}.
     - Attach {#chapter-N} / {#bibliography} IDs to top-level headings.
     - Rewrite cross-file links into in-document bookmarks.
     - Strip redundant trailing "## References" headings (Pandoc turns [^fn]: into native Word footnotes).
     - Insert OpenXML page breaks before each chapter and before the bibliography.
     - Optionally pre-render ```mermaid blocks to cached high-DPI PNGs via mermaid-cli (mmdc).
  3. Invoke `pandoc` to produce a styled .docx with a clickable TOC and Word footnotes.

Usage examples:
  python3 book/tools/export_docx.py
  python3 book/tools/export_docx.py --chapters 00 01 06 -o book/build/sample.docx
  python3 book/tools/export_docx.py --init-template
  python3 book/tools/export_docx.py --markdown-only --skip-mermaid
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shlex
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = BOOK / "chapters"
BIB_PATH = BOOK / "bibliography.md"
BUILD_DIR = BOOK / "build"
DIAGRAM_DIR = BUILD_DIR / "diagrams"
DEFAULT_OUTPUT = BUILD_DIR / "enterprise-ai-guardrails.docx"
DEFAULT_PANDOC_MD = BUILD_DIR / "manuscript_pandoc.md"
DEFAULT_REFERENCE_DOC = BOOK / "tools" / "reference.docx"

DEFAULT_TITLE = "Building Guardrails for Enterprise AI"
DEFAULT_SUBTITLE = "Hardening Enterprise AI Against Hallucinations, Hacks, and Liability"

PANDOC_READER_FORMAT = (
    "markdown+footnotes+pipe_tables+strikeout+raw_attribute+bracketed_spans"
    "+fenced_divs+yaml_metadata_block+header_attributes+autolink_bare_uris-tex_math_dollars"
)
PAGE_BREAK_OPENXML = '```{=openxml}\n<w:p><w:r><w:br w:type="page"/></w:r></w:p>\n```'

_MERMAID_BLOCK_RE = re.compile(r"```mermaid[ \t]*\r?\n(.*?)```", re.DOTALL)
_CAPTION_COMMENT_RE = re.compile(r"^\s*%%\s*caption:\s*(.+?)\s*$", re.MULTILINE)
_ALERT_RE = re.compile(
    r"^(>[ \t]*)\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\][ \t]*(\r?\n>[ \t]*)?",
    re.MULTILINE,
)
_NOTES_HEADING_RE = re.compile(
    r"(?:^---\s*\r?\n+)?^##[ \t]+(?:Notes|References)[ \t]*(?:\r?\n|$)",
    re.MULTILINE,
)
_FN_TAIL_LINE_RE = re.compile(r"^(?:\[\^[A-Za-z0-9_-]+\]:|(?: {2,}|\t))")


def chapter_number(path: Path) -> int:
    """Return the integer chapter prefix parsed from a chapter filename."""
    return int(path.name[:2])


def chapter_anchor(n: int) -> str:
    """Return the Pandoc bookmark identifier for chapter number `n`."""
    return f"chapter-{n}"


def parse_chapter_selection(specs: list[str] | None, all_chapters: list[Path]) -> list[Path]:
    """Resolve user chapter specs (single numbers or inclusive N-M ranges) into sorted paths."""
    if not specs:
        return list(all_chapters)

    by_num = {chapter_number(path): path for path in all_chapters}
    available = ", ".join(str(n) for n in sorted(by_num))
    selected_nums: set[int] = set()

    for raw in specs:
        for token in raw.split(","):
            part = token.strip()
            if not part:
                continue
            range_match = re.fullmatch(r"(\d+)-(\d+)", part)
            if range_match:
                start, end = int(range_match.group(1)), int(range_match.group(2))
                if start > end:
                    raise ValueError(f"Invalid descending chapter range '{part}'.")
                for n in range(start, end + 1):
                    if n not in by_num:
                        raise ValueError(
                            f"Chapter {n} (from range '{part}') not found. Available: {available}."
                        )
                    selected_nums.add(n)
            elif re.fullmatch(r"\d+", part):
                n = int(part)
                if n not in by_num:
                    raise ValueError(f"Chapter {n} not found. Available: {available}.")
                selected_nums.add(n)
            else:
                raise ValueError(
                    f"Invalid chapter specifier '{part}'. Use integers (e.g. 0, 06) or ranges (e.g. 1-5)."
                )

    if not selected_nums:
        raise ValueError("No chapters selected.")

    return [by_num[n] for n in sorted(selected_nums)]


def run_ref_check() -> bool:
    """Run book/tools/check_refs.py and return True when validation passes."""
    result = subprocess.run([sys.executable, str(BOOK / "tools" / "check_refs.py")])
    return result.returncode == 0


def convert_github_alerts(text: str) -> str:
    """Convert GitHub-style alert blockquotes into plain Markdown bold callouts for Word."""

    def _replace(match: re.Match[str]) -> str:
        prefix = match.group(1)
        label = match.group(2).title()
        continuation = match.group(3)
        if continuation is not None:
            return f"{prefix}**{label}:** "
        return f"{prefix}**{label}:**"

    return _ALERT_RE.sub(_replace, text)


def strip_empty_notes_heading(text: str) -> str:
    """Remove a trailing `## References` heading when only footnote definitions follow it."""
    matches = list(_NOTES_HEADING_RE.finditer(text))
    if not matches:
        return text

    last_match = matches[-1]
    tail = text[last_match.end():]
    tail_lines = tail.splitlines()
    if all(not line.strip() or _FN_TAIL_LINE_RE.match(line) for line in tail_lines):
        head = text[:last_match.start()].rstrip()
        cleaned_tail = tail.lstrip("\r\n")
        if head and cleaned_tail:
            return f"{head}\n\n{cleaned_tail}"
        return head or cleaned_tail
    return text


def attach_heading_id(text: str, anchor_id: str) -> str:
    """Attach Pandoc header ID `{#anchor_id}` to the first level-1 ATX heading."""

    def _replace(match: re.Match[str]) -> str:
        heading = match.group(1).rstrip()
        if re.search(r"\{#[A-Za-z0-9_-]+\}\s*$", heading):
            return heading
        return f"{heading} {{#{anchor_id}}}"

    return re.sub(r"^(#[ \t]+.+?)[ \t]*$", _replace, text, count=1, flags=re.MULTILINE)


def _format_ref_label(match: re.Match[str]) -> str:
    label = match.group(1)
    if label.startswith("`") and label.endswith("`"):
        return label
    return f"`{label}`"


def rewrite_chapter_links(text: str, include_bibliography: bool) -> str:
    """Rewrite bibliography and local repo links inside chapter text for standalone DOCX export."""
    if include_bibliography:
        text = re.sub(r"\((?:\.\./)?bibliography\.md#([a-z0-9-]+)\)", r"(#\1)", text)
    else:
        text = re.sub(
            r"\[↗\s*Bibliography\]\((?:\.\./)?bibliography\.md#([a-z0-9-]+)\)",
            r"Bibliography: \1",
            text,
        )
        text = re.sub(
            r"\[([^\]]+)\]\((?:\.\./)?bibliography\.md#[a-z0-9-]+\)",
            r"\1",
            text,
        )

    text = re.sub(r"\[([^\]]+)\]\((?:\.\./)?references/[^)]+\)", _format_ref_label, text)
    return text


def rewrite_bibliography(text: str, included_chapter_nums: set[int]) -> str:
    """Convert bibliography HTML anchors and Cited-in links into Pandoc in-document links."""
    text = attach_heading_id(text, "bibliography")

    # Place native Pandoc bookmark span inline at the start of the citation paragraph.
    text = re.sub(r'<a id="([a-z0-9-]+)"></a>[ \t]*\r?\n(?=\S)', r"[]{#\1}", text)
    text = re.sub(r'<a id="([a-z0-9-]+)"></a>', r"[]{#\1}", text)

    def _replace_chap_link(match: re.Match[str]) -> str:
        label = match.group(1)
        num = int(match.group(2))
        if num in included_chapter_nums:
            return f"[{label}](#{chapter_anchor(num)})"
        return label

    text = re.sub(r"\[([^\]]+)\]\(chapters/(\d\d)-[^)]+\)", _replace_chap_link, text)
    text = re.sub(r"\[([^\]]+)\]\((?:\.\./)?references/[^)]+\)", _format_ref_label, text)
    return text


def resolve_mermaid_cmd(override: str | None) -> list[str] | None:
    """Locate the Mermaid CLI command from an explicit override, PATH, or npx."""
    if override:
        parts = shlex.split(override)
        return parts if parts else None
    mmdc_path = shutil.which("mmdc")
    if mmdc_path:
        return [mmdc_path]
    npx_path = shutil.which("npx")
    if npx_path:
        return [npx_path, "-y", "-p", "@mermaid-js/mermaid-cli", "mmdc"]
    return None


def render_mermaid_blocks(
    text: str,
    diagram_dir: Path,
    mermaid_cmd: list[str] | None,
    *,
    skip: bool,
    strict: bool,
    scale: int,
    width: int,
    theme: str,
) -> tuple[str, dict[str, int]]:
    """Pre-render fenced ```mermaid blocks to cached PNGs and replace them with image links."""
    stats = {"found": 0, "rendered": 0, "cached": 0, "skipped": 0, "failed": 0}
    warned_missing_cmd = False

    def _replace(match: re.Match[str]) -> str:
        nonlocal warned_missing_cmd
        stats["found"] += 1
        code = match.group(1).strip()

        if skip:
            stats["skipped"] += 1
            return match.group(0)

        caption_match = _CAPTION_COMMENT_RE.search(code)
        caption = caption_match.group(1) if caption_match else ""

        digest = hashlib.sha256(
            f"{theme}:{scale}:{width}:{code}".encode("utf-8")
        ).hexdigest()[:12]
        png_path = diagram_dir / f"mermaid-{digest}.png"
        image_ref = f"![{caption}]({diagram_dir.name}/{png_path.name}){{width=95%}}"

        if png_path.exists() and png_path.stat().st_size > 0:
            stats["cached"] += 1
            return image_ref

        if not mermaid_cmd:
            stats["failed"] += 1
            msg = (
                "Mermaid CLI ('mmdc' or 'npx') not found; keeping fenced Mermaid block(s). "
                "Install with: npm install -g @mermaid-js/mermaid-cli (or pass --skip-mermaid)."
            )
            if strict:
                raise RuntimeError(msg)
            if not warned_missing_cmd:
                print(f"WARN: {msg}", file=sys.stderr)
                warned_missing_cmd = True
            return match.group(0)

        diagram_dir.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".mmd", encoding="utf-8", delete=False
        ) as tmp:
            tmp.write(code + "\n")
            tmp_path = Path(tmp.name)

        cmd = [
            *mermaid_cmd,
            "-i",
            str(tmp_path),
            "-o",
            str(png_path),
            "-b",
            "white",
            "-t",
            theme,
            "-s",
            str(scale),
            "-w",
            str(width),
        ]
        try:
            proc = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=120,
            )
        except (OSError, subprocess.SubprocessError) as exc:
            tmp_path.unlink(missing_ok=True)
            stats["failed"] += 1
            err_msg = f"Mermaid render failed for {png_path.name}: {exc}"
            if strict:
                raise RuntimeError(err_msg) from exc
            print(f"WARN: {err_msg}; keeping fenced Mermaid block.", file=sys.stderr)
            return match.group(0)

        tmp_path.unlink(missing_ok=True)
        if proc.returncode != 0 or not png_path.exists() or png_path.stat().st_size == 0:
            png_path.unlink(missing_ok=True)
            stats["failed"] += 1
            stderr_tail = (proc.stderr or proc.stdout or "").strip().splitlines()[-3:]
            detail = " | ".join(stderr_tail) if stderr_tail else f"exit code {proc.returncode}"
            err_msg = (
                f"Mermaid render failed for {png_path.name} ({detail}). "
                "Install/verify @mermaid-js/mermaid-cli or pass --skip-mermaid."
            )
            if strict:
                raise RuntimeError(err_msg)
            print(f"WARN: {err_msg}", file=sys.stderr)
            return match.group(0)

        stats["rendered"] += 1
        return image_ref

    updated = _MERMAID_BLOCK_RE.sub(_replace, text)
    return updated, stats


def build_yaml_frontmatter(
    title: str,
    subtitle: str | None,
    author: str | None,
    doc_date: str,
) -> str:
    """Build a YAML metadata header for Pandoc title page and Word document properties."""
    lines = ["---", f"title: {json.dumps(title)}"]
    if subtitle:
        lines.append(f"subtitle: {json.dumps(subtitle)}")
    if author:
        lines.append(f"author: {json.dumps(author)}")
    lines.append(f"date: {json.dumps(doc_date)}")
    lines.append("---")
    return "\n".join(lines)


def assemble_pandoc_markdown(
    chapters: list[Path],
    bib_path: Path | None,
    *,
    title: str,
    subtitle: str | None,
    author: str | None,
    doc_date: str,
    include_bibliography: bool,
    page_breaks: bool,
    diagram_dir: Path,
    mermaid_cmd: list[str] | None,
    skip_mermaid: bool,
    strict_mermaid: bool,
    mermaid_scale: int,
    mermaid_width: int,
    mermaid_theme: str,
) -> tuple[str, dict[str, int]]:
    """Assemble selected chapters and bibliography into a single Pandoc-ready Markdown string."""
    sections: list[str] = [build_yaml_frontmatter(title, subtitle, author, doc_date)]
    included_nums = {chapter_number(path) for path in chapters}
    use_bib = include_bibliography and bib_path is not None and bib_path.exists()

    mermaid_totals = {"found": 0, "rendered": 0, "cached": 0, "skipped": 0, "failed": 0}
    footnote_defs = 0

    for ch in chapters:
        num = chapter_number(ch)
        raw = ch.read_text(encoding="utf-8")
        text = convert_github_alerts(raw)
        text = strip_empty_notes_heading(text)
        text = attach_heading_id(text, chapter_anchor(num))
        text = rewrite_chapter_links(text, include_bibliography=use_bib)
        text, m_stats = render_mermaid_blocks(
            text,
            diagram_dir,
            mermaid_cmd,
            skip=skip_mermaid,
            strict=strict_mermaid,
            scale=mermaid_scale,
            width=mermaid_width,
            theme=mermaid_theme,
        )
        for key, value in m_stats.items():
            mermaid_totals[key] += value
        footnote_defs += len(re.findall(r"^\[\^[A-Za-z0-9_-]+\]:", text, re.MULTILINE))

        chunk = f"{PAGE_BREAK_OPENXML}\n\n{text.strip()}" if page_breaks else text.strip()
        sections.append(chunk)

    if use_bib and bib_path is not None:
        bib_raw = bib_path.read_text(encoding="utf-8")
        bib_text = convert_github_alerts(bib_raw)
        bib_text = rewrite_bibliography(bib_text, included_nums)
        bib_chunk = (
            f"{PAGE_BREAK_OPENXML}\n\n{bib_text.strip()}"
            if page_breaks
            else bib_text.strip()
        )
        sections.append(bib_chunk)

    assembled = "\n\n".join(sections) + "\n"
    stats = {
        "chapters": len(chapters),
        "footnotes": footnote_defs,
        "bibliography": 1 if use_bib else 0,
        **mermaid_totals,
    }
    return assembled, stats


def init_reference_template(dest: Path, force: bool) -> int:
    """Export Pandoc's default Word reference template so typography and layout can be styled."""
    pandoc_bin = shutil.which("pandoc")
    if not pandoc_bin:
        print(
            "ERROR: 'pandoc' is not installed on PATH.\n"
            "Install it first with:\n"
            "  brew install pandoc\n"
            f"Then re-run: python3 {Path(__file__).name} --init-template",
            file=sys.stderr,
        )
        return 1

    if dest.exists() and not force:
        print(
            f"Refusing to overwrite existing template: {dest}\n"
            "Pass --force to overwrite it.",
            file=sys.stderr,
        )
        return 1

    dest.parent.mkdir(parents=True, exist_ok=True)
    proc = subprocess.run(
        [pandoc_bin, "-o", str(dest), "--print-default-data-file", "reference.docx"],
        capture_output=True,
        text=True,
    )
    if proc.returncode != 0:
        print(
            f"ERROR: Pandoc failed to generate reference template: {proc.stderr.strip()}",
            file=sys.stderr,
        )
        return proc.returncode or 1

    print(f"Created Word style template: {dest}")
    print(
        "Customize these Word styles in LibreOffice Writer or Microsoft Word, then save:\n"
        "  - Normal / Body Text (body font, size, line spacing)\n"
        "  - Heading 1, Heading 2, Heading 3 (chapter and section typography)\n"
        "  - Block Text (callout quotes & bibliography annotations)\n"
        "  - Footnote Text (citation note size & spacing)\n"
        "  - Table (header shading, cell padding, borders)\n"
        "  - Page margins, running headers, and page-number footers"
    )
    return 0


def run_pandoc(
    md_path: Path,
    docx_path: Path,
    reference_doc: Path | None,
    *,
    toc: bool,
    toc_depth: int,
    resource_paths: list[Path],
) -> int:
    """Run Pandoc to convert the assembled Markdown manuscript to DOCX."""
    pandoc_bin = shutil.which("pandoc")
    if not pandoc_bin:
        print(
            f"\nPreprocessed Pandoc Markdown is saved at: {md_path}\n"
            "ERROR: 'pandoc' was not found on PATH, so the .docx file could not be generated.\n"
            "Install Pandoc on macOS with Homebrew:\n"
            "  brew install pandoc\n"
            "Then re-run:\n"
            f"  python3 {Path(__file__).resolve()}",
            file=sys.stderr,
        )
        return 1

    docx_path.parent.mkdir(parents=True, exist_ok=True)

    unique_paths: list[str] = []
    seen_paths: set[str] = set()
    for p in resource_paths:
        resolved = str(p.resolve())
        if resolved not in seen_paths:
            seen_paths.add(resolved)
            unique_paths.append(resolved)

    cmd = [
        pandoc_bin,
        str(md_path),
        f"--from={PANDOC_READER_FORMAT}",
        "--to=docx",
        "--standalone",
        f"--resource-path={os.pathsep.join(unique_paths)}",
        "-o",
        str(docx_path),
    ]
    if toc:
        cmd.extend(["--toc", f"--toc-depth={toc_depth}"])
    if reference_doc is not None:
        cmd.append(f"--reference-doc={reference_doc}")

    proc = subprocess.run(cmd)
    if proc.returncode != 0:
        print(f"ERROR: Pandoc exited with status {proc.returncode}.", file=sys.stderr)
        return proc.returncode

    size_kb = docx_path.stat().st_size / 1024
    print(f"Wrote Word document: {docx_path} ({size_kb:,.1f} KB)")
    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    """Construct the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Convert book Markdown chapters and Annotated Bibliography to Word (.docx) via Pandoc."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output .docx path (default: {DEFAULT_OUTPUT.relative_to(BOOK.parent)}).",
    )
    parser.add_argument(
        "--markdown-out",
        type=Path,
        default=DEFAULT_PANDOC_MD,
        help=f"Intermediate Pandoc Markdown path (default: {DEFAULT_PANDOC_MD.relative_to(BOOK.parent)}).",
    )
    parser.add_argument(
        "--chapters",
        nargs="+",
        metavar="SPEC",
        help="Subset of chapters to export, e.g. '00 01 06' or '1-5' (default: all chapters).",
    )
    parser.add_argument(
        "--no-bibliography",
        action="store_true",
        help="Exclude book/bibliography.md from the exported document.",
    )
    parser.add_argument(
        "--reference-doc",
        type=Path,
        default=None,
        help=(
            "Custom Word reference .docx template "
            f"(auto-uses {DEFAULT_REFERENCE_DOC.relative_to(BOOK.parent)} if present)."
        ),
    )
    parser.add_argument(
        "--init-template",
        action="store_true",
        help="Generate a starter Word style template via Pandoc and exit.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing template when used with --init-template.",
    )
    parser.add_argument("--title", default=DEFAULT_TITLE, help="Document title metadata.")
    parser.add_argument(
        "--subtitle",
        default=DEFAULT_SUBTITLE,
        help="Document subtitle metadata (pass empty string to omit).",
    )
    parser.add_argument("--author", default=None, help="Optional document author metadata.")
    parser.add_argument(
        "--date",
        dest="doc_date",
        default=date.today().isoformat(),
        help="Document date metadata (default: today ISO date).",
    )
    parser.add_argument("--no-toc", action="store_true", help="Omit Word Table of Contents.")
    parser.add_argument(
        "--toc-depth",
        type=int,
        default=2,
        help="Heading depth included in the Word TOC (default: 2).",
    )
    parser.add_argument(
        "--no-page-breaks",
        action="store_true",
        help="Do not insert page breaks before each chapter and bibliography.",
    )
    parser.add_argument(
        "--skip-check",
        action="store_true",
        help="Skip running book/tools/check_refs.py before assembling the manuscript.",
    )
    parser.add_argument(
        "--skip-mermaid",
        action="store_true",
        help="Keep fenced ```mermaid code blocks untouched instead of rendering PNG diagrams.",
    )
    parser.add_argument(
        "--strict-mermaid",
        action="store_true",
        help="Abort export if a Mermaid diagram fails to render.",
    )
    parser.add_argument(
        "--mermaid-cmd",
        default=None,
        help="Explicit Mermaid CLI command override (e.g. '/opt/homebrew/bin/mmdc').",
    )
    parser.add_argument(
        "--mermaid-scale",
        type=int,
        default=3,
        help="Mermaid PNG scale factor for crisp print/Retina output (default: 3).",
    )
    parser.add_argument(
        "--mermaid-width",
        type=int,
        default=1400,
        help="Mermaid diagram render width in pixels (default: 1400).",
    )
    parser.add_argument(
        "--mermaid-theme",
        default="neutral",
        help="Mermaid theme name: neutral, default, forest, dark (default: neutral).",
    )
    parser.add_argument(
        "--markdown-only",
        action="store_true",
        help="Write the preprocessed Pandoc Markdown manuscript and skip calling Pandoc.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint for exporting the book to DOCX via Pandoc."""
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    if args.init_template:
        template_dest = args.reference_doc or DEFAULT_REFERENCE_DOC
        return init_reference_template(template_dest, force=args.force)

    all_chapters = sorted(CHAPTERS_DIR.glob("[0-9][0-9]-*.md"))
    if not all_chapters:
        print(f"ERROR: No chapter files found in {CHAPTERS_DIR}.", file=sys.stderr)
        return 1

    try:
        selected_chapters = parse_chapter_selection(args.chapters, all_chapters)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    ref_doc: Path | None = None
    if args.reference_doc is not None:
        if not args.reference_doc.exists():
            print(f"ERROR: Reference document not found: {args.reference_doc}", file=sys.stderr)
            return 1
        ref_doc = args.reference_doc
    elif DEFAULT_REFERENCE_DOC.exists():
        ref_doc = DEFAULT_REFERENCE_DOC

    if not args.skip_check:
        if not run_ref_check():
            print("Reference check failed; fix errors or pass --skip-check.", file=sys.stderr)
            return 1

    mermaid_cmd = None if args.skip_mermaid else resolve_mermaid_cmd(args.mermaid_cmd)
    try:
        assembled, stats = assemble_pandoc_markdown(
            selected_chapters,
            BIB_PATH,
            title=args.title,
            subtitle=args.subtitle or None,
            author=args.author,
            doc_date=args.doc_date,
            include_bibliography=not args.no_bibliography,
            page_breaks=not args.no_page_breaks,
            diagram_dir=DIAGRAM_DIR,
            mermaid_cmd=mermaid_cmd,
            skip_mermaid=args.skip_mermaid,
            strict_mermaid=args.strict_mermaid,
            mermaid_scale=args.mermaid_scale,
            mermaid_width=args.mermaid_width,
            mermaid_theme=args.mermaid_theme,
        )
    except RuntimeError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    md_out: Path = args.markdown_out
    md_out.parent.mkdir(parents=True, exist_ok=True)
    md_out.write_text(assembled, encoding="utf-8")

    words = len(re.findall(r"\b\w+\b", assembled))
    print(
        f"Assembled {md_out} | chapters: {stats['chapters']} | "
        f"bibliography: {'yes' if stats['bibliography'] else 'no'} | "
        f"footnotes: {stats['footnotes']} | words: ~{words:,} | "
        f"mermaid (found={stats['found']}, rendered={stats['rendered']}, "
        f"cached={stats['cached']}, skipped={stats['skipped']}, failed={stats['failed']})"
    )

    if args.markdown_only:
        return 0

    return run_pandoc(
        md_out,
        args.output,
        ref_doc,
        toc=not args.no_toc,
        toc_depth=args.toc_depth,
        resource_paths=[md_out.parent, DIAGRAM_DIR.parent, BOOK],
    )


if __name__ == "__main__":
    sys.exit(main())
