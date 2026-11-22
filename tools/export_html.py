#!/usr/bin/env python3
"""Export the book's Markdown chapters and Annotated Bibliography as linked multi-page HTML.

Pipeline:
  1. Validate footnotes and bibliography links using book/tools/check_refs.py (unless --skip-check).
  2. Render each selected chapter Markdown file to its own standalone HTML page, rewriting
     cross-file bibliography/chapter links, numbering multi-citation footnotes with bidirectional
     jumps, converting GitHub callouts, and preparing Mermaid diagrams.
  3. Render book/bibliography.md to bibliography.html with working back-links to included chapters.
  4. Generate index.html (Cover + Part-grouped Table of Contents), shared CSS/JS assets, and a
     file://-compatible client-side full-text search index (assets/search-index.js).
  5. Optionally open the output in a browser or serve it over localhost (--serve).

Usage examples:
  python3 book/tools/export_html.py
  python3 book/tools/export_html.py --clean --serve --open
  python3 book/tools/export_html.py --chapters 00 1-5 31 --no-bibliography -o book/build/sample-html
"""
from __future__ import annotations

import argparse
import functools
import html
import http.server
import json
import re
import socketserver
import subprocess
import sys
import unicodedata
import webbrowser
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Callable

from markdown_it import MarkdownIt

BOOK = Path(__file__).resolve().parent.parent
CHAPTERS_DIR = BOOK / "chapters"
BIB_PATH = BOOK / "bibliography.md"
DEFAULT_OUTPUT_DIR = BOOK / "build" / "html"

DEFAULT_TITLE = "Building Guardrails for Enterprise AI"
DEFAULT_SUBTITLE = "Hardening Enterprise AI Against Hallucinations, Hacks, and Liability"

MERMAID_CDN_URL = "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"

_FENCE_OPEN_RE = re.compile(r"^[ \t]{0,3}(`{3,}|~{3,})(.*)$")
_INLINE_CODE_RE = re.compile(r"(`+)([^`]|.*?[^`])\1|`+")
_FN_DEF_START_RE = re.compile(r"^\[\^([A-Za-z0-9_-]+)\]:[ \t]*(.*)$")
_FN_REF_RE = re.compile(r"(`?)\[\^([A-Za-z0-9_-]+)\]\1")
_NOTES_TAIL_RE = re.compile(
    r"(?:^---\s*\r?\n+)?^##[ \t]+(?:Notes|References)[ \t]*(?:\r?\n|$)",
    re.MULTILINE,
)
_ALERT_HEAD_RE = re.compile(
    r"^>[ \t]*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\][ \t]*(.*)$",
    re.IGNORECASE,
)
_CAPTION_COMMENT_RE = re.compile(r"^\s*%%\s*caption:\s*(.+?)\s*$", re.MULTILINE)
_HTML_TOKEN_RE = re.compile(r"(<!--.*?-->|<[^>]+>)", re.DOTALL)
_BARE_URL_RE = re.compile(r"https?://[^\s<>\"'`]+")
_HEADING_RE = re.compile(r"<h([23])([^>]*)>(.*?)</h\1>", re.DOTALL | re.IGNORECASE)
_ID_ATTR_RE = re.compile(r'\bid\s*=\s*(?:"([^"]+)"|\'([^\']+)\')', re.IGNORECASE)
_TABLE_BLOCK_RE = re.compile(r"(<table(?:\s[^>]*)?>.*?</table>)", re.DOTALL | re.IGNORECASE)
_CHAPTER_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((?:(?:\.\./)?chapters/)?(\d{2}-[A-Za-z0-9-]+)\.md(#[-A-Za-z0-9_]+)?\)"
)
_BIB_CHAPTER_LINK_RE = re.compile(
    r"\[([^\]]+)\]\((?:\.\./)?chapters/(\d{2}-[A-Za-z0-9-]+)\.md(#[-A-Za-z0-9_]+)?\)"
)
_REF_LINK_RE = re.compile(r"\[([^\]]+)\]\((?:\.\./)?references/[^)]+\)")

_ALERT_TITLES = {
    "note": "Note",
    "tip": "Tip",
    "important": "Important",
    "warning": "Warning",
    "caution": "Caution",
}


@dataclass(frozen=True)
class ChapterMeta:
    """Metadata describing a chapter file in the book."""

    num: int
    path: Path
    slug: str
    filename: str
    title: str
    part: str
    words: int


@dataclass(frozen=True)
class TocItem:
    """Single heading entry for a page's right-hand outline."""

    level: int
    slug: str
    text: str


@dataclass(frozen=True)
class NavPage:
    """Navigation descriptor for linear next/previous and sidebar links."""

    filename: str
    title: str
    short_label: str
    group: str


def chapter_number(path: Path) -> int:
    """Return the integer chapter prefix parsed from a chapter filename."""
    return int(path.name[:2])


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


def extract_chapter_meta(path: Path) -> ChapterMeta:
    """Read title, part grouping, and word count from a chapter Markdown file."""
    raw = path.read_text(encoding="utf-8")
    lines = raw.splitlines()
    num = chapter_number(path)

    title = path.stem
    for line in lines:
        if line.startswith("# "):
            title = line[2:].strip()
            break

    part = "Book"
    if num == 0:
        part = "Front Matter"
    elif num == 31:
        part = "Appendices"
    else:
        for line in lines[:10]:
            m = re.match(r"^\*(Part [IVX]+:\s*.+?)\*\s*$", line.strip())
            if m:
                part = m.group(1)
                break

    words = len(re.findall(r"\b\w+\b", raw))
    return ChapterMeta(
        num=num,
        path=path,
        slug=path.stem,
        filename=f"{path.stem}.html",
        title=title,
        part=part,
        words=words,
    )


def run_ref_check() -> bool:
    """Run book/tools/check_refs.py and return True when validation passes."""
    result = subprocess.run([sys.executable, str(BOOK / "tools" / "check_refs.py")])
    return result.returncode == 0


def split_code_fences(text: str) -> list[tuple[bool, str]]:
    """Split Markdown text into (is_fence, chunk) segments preserving exact line endings."""
    segments: list[tuple[bool, str]] = []
    buf: list[str] = []
    in_fence = False
    fence_char = ""
    fence_len = 0

    for line in text.splitlines(keepends=True):
        if not in_fence:
            m = _FENCE_OPEN_RE.match(line)
            if m:
                if buf:
                    segments.append((False, "".join(buf)))
                    buf.clear()
                in_fence = True
                fence_token = m.group(1)
                fence_char = fence_token[0]
                fence_len = len(fence_token)
                buf.append(line)
            else:
                buf.append(line)
        else:
            buf.append(line)
            stripped = line.lstrip(" ").rstrip("\r\n")
            if (
                len(line) - len(line.lstrip(" ")) <= 3
                and len(stripped) >= fence_len
                and set(stripped) == {fence_char}
            ):
                segments.append((True, "".join(buf)))
                buf.clear()
                in_fence = False
                fence_char = ""
                fence_len = 0

    if buf:
        segments.append((in_fence, "".join(buf)))
    return segments


def replace_outside_inline_code(text: str, fn: Callable[[str], str]) -> str:
    """Apply `fn` only to portions of `text` outside inline backtick spans."""
    out: list[str] = []
    pos = 0
    for match in _INLINE_CODE_RE.finditer(text):
        if match.start() > pos:
            out.append(fn(text[pos : match.start()]))
        out.append(match.group(0))
        pos = match.end()
    if pos < len(text):
        out.append(fn(text[pos:]))
    return "".join(out)


def transform_markdown_prose(text: str, fn: Callable[[str], str], *, skip_inline_code: bool = True) -> str:
    """Apply `fn` to prose outside fenced code blocks (and optionally inline code spans)."""
    parts: list[str] = []
    for is_fence, chunk in split_code_fences(text):
        if is_fence:
            parts.append(chunk)
        elif skip_inline_code:
            parts.append(replace_outside_inline_code(chunk, fn))
        else:
            parts.append(fn(chunk))
    return "".join(parts)


def create_markdown_renderer() -> MarkdownIt:
    """Create configured GFM-like markdown-it renderer with HTML-escaped Mermaid fences."""
    md = MarkdownIt("gfm-like", {"html": True, "linkify": False, "typographer": False})
    orig_fence = md.renderer.rules.get("fence")

    def _render_fence(tokens, idx, options, env):
        token = tokens[idx]
        info = (token.info or "").strip().lower()
        if info == "mermaid" or info.startswith("mermaid "):
            if isinstance(env, dict):
                env["mermaid_count"] = env.get("mermaid_count", 0) + 1
            raw_code = token.content.rstrip()
            cap_match = _CAPTION_COMMENT_RE.search(raw_code)
            caption_html = f"<figcaption>{html.escape(cap_match.group(1))}</figcaption>" if cap_match else ""
            # Escape HTML so tags like <br/> inside labels survive browser parsing intact for Mermaid.js.
            return (
                '<figure class="mermaid-wrap">'
                f'<pre class="mermaid">{html.escape(raw_code)}</pre>'
                f"{caption_html}</figure>\n"
            )
        if orig_fence:
            return orig_fence(tokens, idx, options, env)
        return f"<pre><code>{html.escape(token.content)}</code></pre>\n"

    md.renderer.rules["fence"] = _render_fence
    return md


def _format_ref_label(match: re.Match[str]) -> str:
    label = match.group(1)
    if label.startswith("`") and label.endswith("`"):
        return label
    return f"`{label}`"


def rewrite_chapter_links(
    text: str,
    *,
    include_bibliography: bool,
    included_chapters_by_num: dict[int, ChapterMeta],
) -> str:
    """Rewrite bibliography, chapter, and references links inside chapter prose/notes."""

    def _rewrite(chunk: str) -> str:
        if include_bibliography:
            chunk = re.sub(r"\((?:\.\./)?bibliography\.md#([A-Za-z0-9_-]+)\)", r"(bibliography.html#\1)", chunk)
            chunk = re.sub(r"\((?:\.\./)?bibliography\.md\)", r"(bibliography.html)", chunk)
        else:
            chunk = re.sub(
                r"\[↗\s*Bibliography\]\((?:\.\./)?bibliography\.md#([A-Za-z0-9_-]+)\)",
                r"Bibliography: \1",
                chunk,
            )
            chunk = re.sub(
                r"\[([^\]]+)\]\((?:\.\./)?bibliography\.md(?:#[A-Za-z0-9_-]+)?\)",
                r"\1",
                chunk,
            )

        chunk = _REF_LINK_RE.sub(_format_ref_label, chunk)

        def _replace_chap(m: re.Match[str]) -> str:
            label, stem, frag = m.group(1), m.group(2), m.group(3) or ""
            num = int(stem[:2])
            target = included_chapters_by_num.get(num)
            if target is not None:
                return f"[{label}]({target.filename}{frag})"
            return label

        return _CHAPTER_LINK_RE.sub(_replace_chap, chunk)

    return transform_markdown_prose(text, _rewrite, skip_inline_code=True)


def rewrite_bibliography_links(
    text: str,
    *,
    included_chapters_by_num: dict[int, ChapterMeta],
) -> str:
    """Rewrite chapter and repository reference links inside bibliography.md."""

    def _rewrite(chunk: str) -> str:
        def _replace_chap(m: re.Match[str]) -> str:
            label, stem, frag = m.group(1), m.group(2), m.group(3) or ""
            num = int(stem[:2])
            target = included_chapters_by_num.get(num)
            if target is not None:
                return f"[{label}]({target.filename}{frag})"
            return label

        chunk = _BIB_CHAPTER_LINK_RE.sub(_replace_chap, chunk)
        return _REF_LINK_RE.sub(_format_ref_label, chunk)

    return transform_markdown_prose(text, _rewrite, skip_inline_code=True)


def _extract_footnote_defs_from_chunk(chunk: str) -> tuple[str, dict[str, str]]:
    """Extract `[^id]: ...` definitions from a non-fence Markdown chunk."""
    defs: dict[str, str] = {}
    kept: list[str] = []
    lines = chunk.splitlines(keepends=True)
    i = 0

    while i < len(lines):
        m = _FN_DEF_START_RE.match(lines[i].rstrip("\r\n"))
        if not m:
            kept.append(lines[i])
            i += 1
            continue

        fn_id = m.group(1)
        body_parts = [m.group(2).strip()]
        i += 1

        while i < len(lines):
            raw_line = lines[i]
            stripped_nl = raw_line.rstrip("\r\n")
            if re.match(r"^(?: {2,}|\t)\S", stripped_nl):
                cont = re.sub(r"^(?: {1,4}|\t)", "", stripped_nl)
                body_parts.append(cont.strip())
                i += 1
            elif not stripped_nl.strip():
                # Keep blank line as part of this footnote only if an indented continuation follows.
                if i + 1 < len(lines) and re.match(r"^(?: {2,}|\t)\S", lines[i + 1]):
                    body_parts.append("")
                    i += 1
                else:
                    i += 1
                    break
            else:
                break

        defs[fn_id] = " ".join(part for part in body_parts if part)

    return "".join(kept), defs


def _strip_trailing_empty_notes_heading(text: str) -> str:
    """Remove trailing `## References` (and preceding divider) when only whitespace remains after it."""
    matches = list(_NOTES_TAIL_RE.finditer(text))
    if not matches:
        return text
    last = matches[-1]
    if not text[last.end() :].strip():
        return text[: last.start()].rstrip() + "\n"
    return text


def extract_and_rewrite_footnotes(
    text: str,
    md: MarkdownIt,
    *,
    include_bibliography: bool,
    included_chapters_by_num: dict[int, ChapterMeta],
) -> tuple[str, str, int, int]:
    """Process multi-reference footnotes into HTML citations + Notes section.

    Returns (updated_markdown, footnotes_html, unique_def_count, citation_ref_count).
    """
    defs: dict[str, str] = {}
    rebuilt_parts: list[str] = []
    for is_fence, chunk in split_code_fences(text):
        if is_fence:
            rebuilt_parts.append(chunk)
        else:
            cleaned, found = _extract_footnote_defs_from_chunk(chunk)
            defs.update(found)
            rebuilt_parts.append(cleaned)

    if not defs:
        return text, "", 0, 0

    body_md = _strip_trailing_empty_notes_heading("".join(rebuilt_parts))

    order: list[str] = []
    num_by_id: dict[str, int] = {}
    refs_by_id: dict[str, list[str]] = {}
    total_refs = 0

    def _replace_refs(prose_chunk: str) -> str:
        nonlocal total_refs

        def _sub(match: re.Match[str]) -> str:
            nonlocal total_refs
            fn_id = match.group(2)
            if fn_id not in defs:
                return match.group(0)

            total_refs += 1
            if fn_id not in num_by_id:
                num_by_id[fn_id] = len(order) + 1
                order.append(fn_id)
                refs_by_id[fn_id] = []

            k = len(refs_by_id[fn_id]) + 1
            ref_dom_id = f"fnref-{fn_id}" if k == 1 else f"fnref-{fn_id}-{k}"
            refs_by_id[fn_id].append(ref_dom_id)
            num = num_by_id[fn_id]
            return (
                f'<sup class="fn-ref">'
                f'<a href="#fn-{fn_id}" id="{ref_dom_id}" title="Jump to note {num}">[{num}]</a>'
                f"</sup>"
            )

        return _FN_REF_RE.sub(_sub, prose_chunk)

    body_md = transform_markdown_prose(body_md, _replace_refs, skip_inline_code=False)

    # Preserve unreferenced footnote definitions at the bottom if any exist.
    final_ids = list(order)
    for fn_id in defs:
        if fn_id not in num_by_id:
            final_ids.append(fn_id)

    items_html: list[str] = []
    for fn_id in final_ids:
        note_md = rewrite_chapter_links(
            defs[fn_id],
            include_bibliography=include_bibliography,
            included_chapters_by_num=included_chapters_by_num,
        )
        note_inline_html = md.renderInline(note_md)
        refs = refs_by_id.get(fn_id, [])
        if len(refs) == 1:
            backrefs = f' <a href="#{refs[0]}" class="fn-backref" title="Back to text">&#8617;&#xfe0e;</a>'
        elif len(refs) > 1:
            links = " ".join(
                f'<a href="#{r}" class="fn-backref" title="Back to citation {i}">&#8617;&#xfe0e;<sup>{i}</sup></a>'
                for i, r in enumerate(refs, 1)
            )
            backrefs = f" {links}"
        else:
            backrefs = ""

        items_html.append(
            f'<li id="fn-{fn_id}">'
            f'<span class="fn-body">{note_inline_html}</span>'
            f'<span class="fn-backrefs">{backrefs}</span>'
            f"</li>"
        )

    footnotes_html = (
        '<section class="footnotes" id="notes" aria-label="Notes">\n'
        "<h2>References</h2>\n"
        '<ol class="footnote-list">\n'
        + "\n".join(items_html)
        + "\n</ol>\n</section>"
    )
    return body_md, footnotes_html, len(defs), total_refs


def convert_github_alerts(text: str, md: MarkdownIt) -> tuple[str, dict[str, str]]:
    """Replace GitHub alert blockquotes (`> [!NOTE]`) with placeholder tokens & rendered HTML."""
    placeholders: dict[str, str] = {}
    out_segments: list[str] = []

    for is_fence, chunk in split_code_fences(text):
        if is_fence:
            out_segments.append(chunk)
            continue

        lines = chunk.splitlines(keepends=True)
        rebuilt: list[str] = []
        i = 0
        while i < len(lines):
            raw_line = lines[i].rstrip("\r\n")
            m = _ALERT_HEAD_RE.match(raw_line)
            if not m:
                rebuilt.append(lines[i])
                i += 1
                continue

            kind = m.group(1).lower()
            first_rest = m.group(2).strip()
            inner_lines: list[str] = []
            if first_rest:
                inner_lines.append(first_rest)
            i += 1

            while i < len(lines):
                cand = lines[i].rstrip("\r\n")
                if cand.startswith(">"):
                    inner_lines.append(re.sub(r"^>[ \t]?", "", cand))
                    i += 1
                else:
                    break

            inner_md = "\n".join(inner_lines).strip()
            inner_html = md.render(inner_md) if inner_md else ""
            title = _ALERT_TITLES.get(kind, kind.title())
            token = f"<!--CALLOUT_PLACEHOLDER_{len(placeholders)}-->"
            placeholders[token] = (
                f'<div class="callout callout-{kind}" role="note">'
                f'<div class="callout-title">{title}</div>'
                f'<div class="callout-body">{inner_html}</div>'
                f"</div>\n"
            )
            rebuilt.append(f"\n{token}\n\n")

        out_segments.append("".join(rebuilt))

    return "".join(out_segments), placeholders


def restore_callout_placeholders(html_str: str, placeholders: dict[str, str]) -> str:
    """Restore rendered GitHub callout divs from Markdown-safe comment placeholders."""
    for token, replacement in placeholders.items():
        html_str = html_str.replace(f"<p>{token}</p>", replacement)
        html_str = html_str.replace(token, replacement)
    return html_str


def _trim_url_suffix(raw_url: str) -> tuple[str, str]:
    """Detach trailing punctuation, unbalanced brackets, and escaped entities from a bare URL."""
    url = raw_url
    suffix = ""

    while True:
        changed = False
        for ent in ("&quot;", "&lt;", "&gt;", "&apos;"):
            if url.endswith(ent):
                url = url[: -len(ent)]
                suffix = ent + suffix
                changed = True
                break
        if changed:
            continue

        if url and url[-1] in ".,;:!?":
            # Avoid clipping valid HTML entity semicolons unless trailing standalone semicolon.
            suffix = url[-1] + suffix
            url = url[:-1]
            continue

        if url.endswith(")") and url.count(")") > url.count("("):
            suffix = ")" + suffix
            url = url[:-1]
            continue

        if url.endswith("]") and url.count("]") > url.count("["):
            suffix = "]" + suffix
            url = url[:-1]
            continue

        break

    return url, suffix


def autolink_html(html_str: str) -> str:
    """Convert bare https?:// URLs in HTML text nodes outside links/code/pre into <a> tags."""
    tokens = _HTML_TOKEN_RE.split(html_str)
    depths = {"a": 0, "code": 0, "pre": 0, "script": 0, "style": 0}
    out: list[str] = []

    for tok in tokens:
        if not tok:
            continue
        if tok.startswith("<"):
            tag_m = re.match(r"^<\s*(/?)\s*([a-zA-Z0-9]+)\b([^>]*)>", tok)
            if tag_m:
                is_close = bool(tag_m.group(1))
                tag_name = tag_m.group(2).lower()
                self_closing = tag_m.group(3).rstrip().endswith("/")
                if tag_name in depths and not self_closing:
                    if is_close:
                        depths[tag_name] = max(0, depths[tag_name] - 1)
                    else:
                        depths[tag_name] += 1
            out.append(tok)
            continue

        if any(depths.values()):
            out.append(tok)
            continue

        def _replace_url(m: re.Match[str]) -> str:
            clean, suffix = _trim_url_suffix(m.group(0))
            if not clean or clean in ("http://", "https://"):
                return m.group(0)
            decoded = html.unescape(clean)
            safe_href = html.escape(decoded, quote=True)
            safe_label = html.escape(decoded, quote=False)
            return f'<a href="{safe_href}" target="_blank" rel="noopener noreferrer">{safe_label}</a>{suffix}'

        out.append(_BARE_URL_RE.sub(_replace_url, tok))

    return "".join(out)


def slugify(text: str) -> str:
    """Create a GitHub-style URL slug from plain heading text."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_ish = normalized.encode("ascii", "ignore").decode("ascii").lower()
    cleaned = re.sub(r"[^\w\s-]", "", ascii_ish)
    slug = re.sub(r"[-\s]+", "-", cleaned).strip("-")
    return slug or "section"


def _strip_tags_plain(fragment: str) -> str:
    without_fn = re.sub(r'<sup class="fn-ref">.*?</sup>', "", fragment, flags=re.DOTALL)
    plain = re.sub(r"<[^>]+>", "", without_fn)
    return html.unescape(re.sub(r"\s+", " ", plain)).strip()


def postprocess_body_html(
    body_html: str,
    footnotes_html: str,
) -> tuple[str, list[TocItem]]:
    """Add unique slug IDs/anchors to h2/h3, wrap tables, and extract on-page TOC."""
    used_ids: set[str] = set()
    for m in _ID_ATTR_RE.finditer(body_html + footnotes_html):
        val = m.group(1) or m.group(2)
        if val:
            used_ids.add(val)

    toc: list[TocItem] = []

    def _add_heading_id(match: re.Match[str]) -> str:
        level = int(match.group(1))
        attrs = match.group(2)
        inner = match.group(3)
        plain = _strip_tags_plain(inner)

        existing_m = _ID_ATTR_RE.search(attrs)
        if existing_m:
            slug = existing_m.group(1) or existing_m.group(2) or slugify(plain)
            used_ids.add(slug)
            new_attrs = attrs
        else:
            base = slugify(plain)
            slug = base
            counter = 2
            while slug in used_ids:
                slug = f"{base}-{counter}"
                counter += 1
            used_ids.add(slug)
            new_attrs = f'{attrs} id="{slug}"'

        toc.append(TocItem(level=level, slug=slug, text=plain))
        if 'class="heading-anchor"' in inner:
            return f"<h{level}{new_attrs}>{inner}</h{level}>"
        anchor = f'<a class="heading-anchor" href="#{slug}" aria-label="Link to section">#</a>'
        return f"<h{level}{new_attrs}>{inner} {anchor}</h{level}>"

    updated = _HEADING_RE.sub(_add_heading_id, body_html)
    updated = _TABLE_BLOCK_RE.sub(r'<div class="table-wrap">\1</div>', updated)

    if footnotes_html:
        updated = f"{updated}\n{footnotes_html}"
        toc.append(TocItem(level=2, slug="notes", text="Notes"))

    return updated, toc


def _collapse_plain_text(html_fragment: str) -> str:
    without_anchors = re.sub(r'<a class="heading-anchor"[^>]*>#</a>', "", html_fragment)
    without_styles = re.sub(r"<(script|style)[^>]*>.*?</\1>", " ", without_anchors, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", without_styles)
    return html.unescape(re.sub(r"\s+", " ", text)).strip()


def extract_search_records(page_href: str, page_title: str, content_html: str) -> list[dict[str, str]]:
    """Split a rendered page by <h2> headings into section-anchored client-side search records."""
    h2_pattern = re.compile(r'<h2\b[^>]*\bid="([^"]+)"[^>]*>(.*?)</h2>', re.DOTALL | re.IGNORECASE)
    matches = list(h2_pattern.finditer(content_html))
    records: list[dict[str, str]] = []

    if not matches:
        body_text = _collapse_plain_text(content_html)
        if body_text:
            records.append(
                {"p": page_href, "t": page_title, "s": page_title, "id": "", "b": body_text}
            )
        return records

    intro_text = _collapse_plain_text(content_html[: matches[0].start()])
    if intro_text:
        records.append({"p": page_href, "t": page_title, "s": "Overview", "id": "", "b": intro_text})

    for idx, m in enumerate(matches):
        sec_id = m.group(1)
        sec_title = _strip_tags_plain(m.group(2).replace("#</a>", "</a>"))
        start = m.end()
        end = matches[idx + 1].start() if idx + 1 < len(matches) else len(content_html)
        sec_text = _collapse_plain_text(content_html[start:end])
        if sec_text or sec_title:
            records.append(
                {
                    "p": page_href,
                    "t": page_title,
                    "s": sec_title,
                    "id": sec_id,
                    "b": sec_text,
                }
            )

    return records


def build_sidebar_groups(
    chapters: list[ChapterMeta],
    *,
    include_bibliography: bool,
) -> list[tuple[str, list[NavPage]]]:
    """Group pages by Front Matter, Parts I-VIII, Appendices, and Bibliography."""
    groups: list[tuple[str, list[NavPage]]] = []
    index_by_group: dict[str, int] = {}

    for ch in chapters:
        nav_item = NavPage(
            filename=ch.filename,
            title=ch.title,
            short_label=ch.title,
            group=ch.part,
        )
        if ch.part not in index_by_group:
            index_by_group[ch.part] = len(groups)
            groups.append((ch.part, []))
        groups[index_by_group[ch.part]][1].append(nav_item)

    if include_bibliography:
        groups.append(
            (
                "Reference",
                [
                    NavPage(
                        filename="bibliography.html",
                        title="Annotated Bibliography",
                        short_label="Annotated Bibliography",
                        group="Reference",
                    )
                ],
            )
        )
    return groups


def render_sidebar_html(
    groups: list[tuple[str, list[NavPage]]],
    current_filename: str,
    book_title: str,
) -> str:
    """Render the left-hand navigation sidebar HTML."""
    parts: list[str] = [
        '<aside class="sidebar" id="sidebar" aria-label="Book navigation">',
        '  <div class="sidebar-search">',
        '    <label class="sr-only" for="search-input">Search handbook</label>',
        '    <input id="search-input" class="search-input" type="search" placeholder="Search handbook… (/)" autocomplete="off" />',
        '    <div id="search-results" class="search-results" hidden></div>',
        "  </div>",
        '  <nav class="sidebar-nav">',
        f'    <a class="nav-home{" is-active" if current_filename == "index.html" else ""}" href="index.html">Contents &amp; Overview</a>',
    ]

    for group_name, items in groups:
        parts.append('    <div class="nav-group">')
        parts.append(f'      <div class="nav-group-title">{html.escape(group_name)}</div>')
        parts.append('      <ul class="nav-list">')
        for item in items:
            active_cls = ' class="is-active" aria-current="page"' if item.filename == current_filename else ""
            parts.append(
                f'        <li><a href="{html.escape(item.filename)}"{active_cls}>{html.escape(item.short_label)}</a></li>'
            )
        parts.append("      </ul>")
        parts.append("    </div>")

    parts.append("  </nav>")
    parts.append("</aside>")
    return "\n".join(parts)


def render_right_toc_html(toc: list[TocItem]) -> str:
    """Render the sticky On-This-Page section outline."""
    if not toc:
        return '<aside class="page-toc" aria-label="On this page"></aside>'
    items = [
        f'<li class="toc-l{item.level}"><a href="#{html.escape(item.slug)}">{html.escape(item.text)}</a></li>'
        for item in toc
    ]
    return (
        '<aside class="page-toc" aria-label="On this page">\n'
        '  <div class="page-toc-inner">\n'
        '    <div class="page-toc-title">On this page</div>\n'
        f'    <ul>{"".join(items)}</ul>\n'
        "  </div>\n"
        "</aside>"
    )


def render_pager_html(prev_page: NavPage | None, next_page: NavPage | None) -> str:
    """Render Previous / Next navigation cards at the bottom of a page."""
    if prev_page is None and next_page is None:
        return ""
    left = (
        f'<a class="pager-card pager-prev" href="{html.escape(prev_page.filename)}">'
        f'<span class="pager-dir">&larr; Previous</span>'
        f'<span class="pager-title">{html.escape(prev_page.title)}</span></a>'
        if prev_page
        else '<span class="pager-spacer"></span>'
    )
    right = (
        f'<a class="pager-card pager-next" href="{html.escape(next_page.filename)}">'
        f'<span class="pager-dir">Next &rarr;</span>'
        f'<span class="pager-title">{html.escape(next_page.title)}</span></a>'
        if next_page
        else '<span class="pager-spacer"></span>'
    )
    return f'<nav class="pager" aria-label="Chapter navigation">{left}{right}</nav>'


def render_page_shell(
    *,
    page_title: str,
    book_title: str,
    book_subtitle: str,
    author: str | None,
    doc_date: str,
    current_filename: str,
    eyebrow: str,
    reading_meta: str,
    body_html: str,
    sidebar_groups: list[tuple[str, list[NavPage]]],
    toc: list[TocItem],
    prev_page: NavPage | None,
    next_page: NavPage | None,
    include_mermaid_cdn: bool,
) -> str:
    """Wrap rendered article HTML inside the responsive 3-column HTML reader shell."""
    full_title = book_title if current_filename == "index.html" else f"{page_title} — {book_title}"
    sidebar_html = render_sidebar_html(sidebar_groups, current_filename, book_title)
    right_toc_html = render_right_toc_html(toc)
    pager_html = render_pager_html(prev_page, next_page)
    mermaid_tag = (
        f'  <script src="{MERMAID_CDN_URL}" defer></script>\n'
        if include_mermaid_cdn
        else ""
    )

    author_line = f"{html.escape(author)} &middot; " if author else ""
    eyebrow_block = (
        f'<div class="doc-meta-bar">'
        f'<span class="doc-eyebrow">{html.escape(eyebrow)}</span>'
        f'<span class="doc-reading-meta">{html.escape(reading_meta)}</span>'
        f"</div>"
        if eyebrow or reading_meta
        else ""
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{html.escape(full_title)}</title>
  <meta name="description" content="{html.escape(book_subtitle)}" />
  <script>
    (function () {{
      var param = null;
      var saved = null;
      var winTheme = null;
      try {{
        param = new URLSearchParams(window.location.search).get("theme");
      }} catch (e) {{}}
      try {{
        saved = localStorage.getItem("book-theme");
      }} catch (e) {{}}
      try {{
        var wm = (window.name || "").match(/^book-theme:(dark|light)$/);
        if (wm) winTheme = wm[1];
      }} catch (e) {{}}
      var explicit = (param === "dark" || param === "light")
        ? param
        : ((saved === "dark" || saved === "light")
            ? saved
            : ((winTheme === "dark" || winTheme === "light") ? winTheme : null));
      if (explicit) {{
        try {{ localStorage.setItem("book-theme", explicit); }} catch (e) {{}}
        try {{ window.name = "book-theme:" + explicit; }} catch (e) {{}}
        document.documentElement.setAttribute("data-theme-explicit", "1");
      }}
      var theme = explicit || (window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light");
      document.documentElement.setAttribute("data-theme", theme);
    }})();
  </script>
  <link rel="stylesheet" href="assets/style.css" />
{mermaid_tag}  <script src="assets/search-index.js" defer></script>
  <script src="assets/app.js" defer></script>
</head>
<body>
  <header class="topbar">
    <div class="topbar-left">
      <button class="menu-toggle" id="menu-toggle" type="button" aria-label="Toggle navigation" aria-expanded="false">
        <span aria-hidden="true">&#9776;</span>
      </button>
      <a class="brand" href="index.html">
        <span class="brand-title">{html.escape(book_title)}</span>
      </a>
    </div>
    <div class="topbar-actions">
      <button class="icon-btn" id="search-focus-btn" type="button" title="Search (/ or Cmd+K)">Search <kbd>/</kbd></button>
      <button class="icon-btn" id="theme-toggle" type="button" title="Toggle color theme" aria-label="Toggle color theme">&#9680;</button>
    </div>
  </header>

  <div class="sidebar-backdrop" id="sidebar-backdrop"></div>

  <div class="layout">
{sidebar_html}
    <main class="main" id="main">
      <article class="content">
        {eyebrow_block}
        {body_html}
        {pager_html}
      </article>
      <footer class="doc-footer">
        {author_line}{html.escape(book_title)} &middot; Built {html.escape(doc_date)}
      </footer>
    </main>
{right_toc_html}
  </div>
</body>
</html>
"""


def build_index_body(
    *,
    title: str,
    subtitle: str,
    author: str | None,
    doc_date: str,
    chapters: list[ChapterMeta],
    include_bibliography: bool,
    bib_entries_count: int,
    total_footnotes: int,
    total_mermaid: int,
) -> str:
    """Build HTML body for index.html cover card and Part-grouped Table of Contents."""
    total_words = sum(ch.words for ch in chapters)
    first_href = chapters[0].filename if chapters else "bibliography.html"
    author_html = f'<p class="hero-author">By {html.escape(author)}</p>' if author else ""
    subtitle_html = f'<p class="hero-subtitle">{html.escape(subtitle)}</p>' if subtitle else ""

    stats_chips = [
        f"<span><strong>{len(chapters)}</strong> sections</span>",
        f"<span><strong>~{total_words:,}</strong> words</span>",
        f"<span><strong>{total_footnotes:,}</strong> footnotes</span>",
        f"<span><strong>{total_mermaid}</strong> diagrams</span>",
    ]
    if include_bibliography:
        stats_chips.append(f"<span><strong>{bib_entries_count}</strong> bibliography sources</span>")

    groups_html: list[str] = []
    seen_parts: list[str] = []
    by_part: dict[str, list[ChapterMeta]] = {}
    for ch in chapters:
        if ch.part not in by_part:
            seen_parts.append(ch.part)
            by_part[ch.part] = []
        by_part[ch.part].append(ch)

    for part in seen_parts:
        rows = []
        for ch in by_part[part]:
            read_min = max(1, round(ch.words / 240))
            rows.append(
                f'<li><a href="{html.escape(ch.filename)}">'
                f'<span class="toc-chap-title">{html.escape(ch.title)}</span>'
                f'<span class="toc-chap-meta">{ch.words:,} words &middot; ~{read_min} min</span>'
                f"</a></li>"
            )
        groups_html.append(
            f'<section class="index-group">'
            f"<h2>{html.escape(part)}</h2>"
            f'<ul class="index-list">{"".join(rows)}</ul>'
            f"</section>"
        )

    if include_bibliography:
        groups_html.append(
            '<section class="index-group">'
            "<h2>Reference</h2>"
            '<ul class="index-list">'
            '<li><a href="bibliography.html">'
            '<span class="toc-chap-title">Annotated Bibliography</span>'
            f'<span class="toc-chap-meta">{bib_entries_count} sources</span>'
            "</a></li></ul></section>"
        )

    return (
        '<div class="hero">\n'
        f"  <h1>{html.escape(title)}</h1>\n"
        f"  {subtitle_html}\n"
        f"  {author_html}\n"
        f'  <div class="hero-stats">{"".join(stats_chips)}</div>\n'
        f'  <div class="hero-actions"><a class="btn-primary" href="{html.escape(first_href)}">Start Reading &rarr;</a>'
        f'  <span class="hero-date">Edition date: {html.escape(doc_date)}</span></div>\n'
        "</div>\n"
        '<div class="index-toc">\n'
        + "\n".join(groups_html)
        + "\n</div>"
    )


def render_chapter_page(
    ch: ChapterMeta,
    md: MarkdownIt,
    *,
    include_bibliography: bool,
    included_chapters_by_num: dict[int, ChapterMeta],
) -> tuple[str, list[TocItem], dict[str, int]]:
    """Render one chapter Markdown file into article HTML, TOC items, and stats."""
    raw = ch.path.read_text(encoding="utf-8")
    body_md, fn_html, fn_defs, fn_refs = extract_and_rewrite_footnotes(
        raw,
        md,
        include_bibliography=include_bibliography,
        included_chapters_by_num=included_chapters_by_num,
    )
    body_md = rewrite_chapter_links(
        body_md,
        include_bibliography=include_bibliography,
        included_chapters_by_num=included_chapters_by_num,
    )
    body_md, callout_placeholders = convert_github_alerts(body_md, md)

    env: dict[str, int] = {"mermaid_count": 0}
    rendered_html = md.render(body_md, env)
    rendered_html = restore_callout_placeholders(rendered_html, callout_placeholders)
    final_html, toc = postprocess_body_html(rendered_html, fn_html)
    final_html = autolink_html(final_html)

    stats = {
        "footnotes": fn_defs,
        "footnote_refs": fn_refs,
        "mermaid": env.get("mermaid_count", 0),
    }
    return final_html, toc, stats


def render_bibliography_page(
    bib_path: Path,
    md: MarkdownIt,
    *,
    included_chapters_by_num: dict[int, ChapterMeta],
) -> tuple[str, list[TocItem], int]:
    """Render bibliography.md into HTML, TOC items, and entry anchor count."""
    raw = bib_path.read_text(encoding="utf-8")
    entry_count = len(re.findall(r'<a id="[a-z0-9-]+"></a>', raw))
    rewritten = rewrite_bibliography_links(raw, included_chapters_by_num=included_chapters_by_num)
    rewritten, callout_placeholders = convert_github_alerts(rewritten, md)
    rendered_html = md.render(rewritten)
    rendered_html = restore_callout_placeholders(rendered_html, callout_placeholders)
    final_html, toc = postprocess_body_html(rendered_html, "")
    final_html = autolink_html(final_html)
    return final_html, toc, entry_count


STYLESHEET_CSS = """/* Generated by book/tools/export_html.py */
:root {
  --bg: #ffffff;
  --bg-alt: #f8fafc;
  --bg-card: #f1f5f9;
  --text: #1e293b;
  --text-muted: #475569;
  --heading: #0f172a;
  --border: #e2e8f0;
  --accent: #1d4ed8;
  --accent-soft: #eff6ff;
  --code-bg: #f1f5f9;
  --pre-bg: #0f172a;
  --pre-text: #f8fafc;
  --target-bg: #fef9c3;
  --shadow: 0 4px 16px rgba(15, 23, 42, 0.08);
  --topbar-h: 56px;
  --sidebar-w: 280px;
  --toc-w: 230px;
  --font-sans: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  --font-mono: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
}

[data-theme="dark"] {
  --bg: #0b1120;
  --bg-alt: #111827;
  --bg-card: #1e293b;
  --text: #e2e8f0;
  --text-muted: #94a3b8;
  --heading: #f8fafc;
  --border: #1e293b;
  --accent: #60a5fa;
  --accent-soft: rgba(59, 130, 246, 0.14);
  --code-bg: #1e293b;
  --pre-bg: #020617;
  --pre-text: #e2e8f0;
  --target-bg: rgba(234, 179, 8, 0.22);
  --shadow: 0 6px 20px rgba(0, 0, 0, 0.45);
}

*, *::before, *::after { box-sizing: border-box; }

html {
  scroll-behavior: smooth;
  font-size: 16px;
}

body {
  margin: 0;
  background: var(--bg);
  color: var(--text);
  font-family: var(--font-sans);
  line-height: 1.68;
  -webkit-font-smoothing: antialiased;
}

.sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

.topbar {
  position: sticky;
  top: 0;
  z-index: 40;
  height: var(--topbar-h);
  background: var(--bg);
  border-bottom: 1px solid var(--border);
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 0 1rem;
  backdrop-filter: blur(8px);
}

.topbar-left {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  min-width: 0;
}

.menu-toggle {
  display: none;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--text);
  border-radius: 6px;
  width: 36px;
  height: 36px;
  font-size: 1.1rem;
  cursor: pointer;
}

.brand {
  color: var(--heading);
  text-decoration: none;
  font-weight: 700;
  font-size: 0.98rem;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.topbar-actions {
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.icon-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  background: var(--bg-alt);
  color: var(--text);
  border: 1px solid var(--border);
  border-radius: 6px;
  padding: 0.35rem 0.65rem;
  font-size: 0.85rem;
  cursor: pointer;
}

.icon-btn:hover { border-color: var(--accent); color: var(--accent); }

.icon-btn kbd {
  font-family: var(--font-mono);
  font-size: 0.75rem;
  padding: 0.05rem 0.35rem;
  border: 1px solid var(--border);
  border-radius: 4px;
  background: var(--bg);
}

.layout {
  display: grid;
  grid-template-columns: var(--sidebar-w) minmax(0, 1fr) var(--toc-w);
  max-width: 1480px;
  margin: 0 auto;
  min-height: calc(100vh - var(--topbar-h));
}

.sidebar {
  position: sticky;
  top: var(--topbar-h);
  height: calc(100vh - var(--topbar-h));
  overflow-y: auto;
  border-right: 1px solid var(--border);
  background: var(--bg-alt);
  padding: 1rem 0.85rem 2rem;
}

.sidebar-search {
  position: relative;
  margin-bottom: 1rem;
}

.search-input {
  width: 100%;
  padding: 0.5rem 0.7rem;
  border: 1px solid var(--border);
  border-radius: 7px;
  background: var(--bg);
  color: var(--text);
  font-size: 0.88rem;
}

.search-input:focus {
  outline: 2px solid var(--accent);
  outline-offset: -1px;
}

.search-results {
  position: absolute;
  top: calc(100% + 6px);
  left: 0;
  right: -20px;
  z-index: 60;
  max-height: 68vh;
  overflow-y: auto;
  background: var(--bg);
  border: 1px solid var(--border);
  border-radius: 8px;
  box-shadow: var(--shadow);
}

.search-empty {
  padding: 0.75rem 0.9rem;
  color: var(--text-muted);
  font-size: 0.86rem;
}

.search-item {
  display: block;
  padding: 0.65rem 0.85rem;
  text-decoration: none;
  color: var(--text);
  border-bottom: 1px solid var(--border);
}

.search-item:last-child { border-bottom: none; }
.search-item:hover, .search-item.is-focused { background: var(--accent-soft); }

.search-item-title {
  font-weight: 600;
  font-size: 0.84rem;
  color: var(--accent);
}

.search-item-sec {
  font-size: 0.82rem;
  font-weight: 600;
  color: var(--heading);
  margin-top: 0.1rem;
}

.search-item-snippet {
  font-size: 0.78rem;
  color: var(--text-muted);
  margin-top: 0.2rem;
  line-height: 1.4;
}

.search-item-snippet mark {
  background: var(--target-bg);
  color: inherit;
  border-radius: 2px;
  padding: 0 2px;
}

.nav-home {
  display: block;
  padding: 0.45rem 0.6rem;
  margin-bottom: 0.75rem;
  border-radius: 6px;
  font-size: 0.88rem;
  font-weight: 600;
  color: var(--heading);
  text-decoration: none;
}

.nav-home:hover, .nav-home.is-active {
  background: var(--accent-soft);
  color: var(--accent);
}

.nav-group { margin-bottom: 1rem; }

.nav-group-title {
  font-size: 0.72rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  padding: 0.25rem 0.6rem;
}

.nav-list {
  list-style: none;
  margin: 0.15rem 0 0;
  padding: 0;
}

.nav-list a {
  display: block;
  padding: 0.34rem 0.6rem;
  border-radius: 6px;
  font-size: 0.84rem;
  line-height: 1.35;
  color: var(--text);
  text-decoration: none;
}

.nav-list a:hover { background: var(--bg-card); color: var(--heading); }
.nav-list a.is-active {
  background: var(--accent-soft);
  color: var(--accent);
  font-weight: 600;
}

.main {
  min-width: 0;
  padding: 2rem 2.5rem 3rem;
}

.content {
  max-width: 78ch;
  margin: 0 auto;
}

.doc-meta-bar {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.75rem;
  font-size: 0.82rem;
  color: var(--text-muted);
}

.doc-eyebrow {
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--accent);
}

h1, h2, h3, h4 {
  color: var(--heading);
  line-height: 1.28;
  scroll-margin-top: calc(var(--topbar-h) + 1.25rem);
}

h1 {
  font-size: clamp(1.75rem, 2.5vw, 2.25rem);
  margin: 0 0 0.75rem;
  letter-spacing: -0.02em;
}

h2 {
  font-size: 1.45rem;
  margin: 2.3rem 0 0.85rem;
  padding-bottom: 0.35rem;
  border-bottom: 1px solid var(--border);
}

h3 {
  font-size: 1.15rem;
  margin: 1.65rem 0 0.6rem;
}

.heading-anchor {
  opacity: 0;
  margin-left: 0.35rem;
  font-weight: 400;
  text-decoration: none;
  color: var(--text-muted);
  transition: opacity 0.12s ease;
}

h2:hover .heading-anchor,
h3:hover .heading-anchor,
.heading-anchor:focus {
  opacity: 0.85;
}

a {
  color: var(--accent);
  text-underline-offset: 2px;
}

a[id] {
  scroll-margin-top: calc(var(--topbar-h) + 1.5rem);
}

p:has(> a[id]:target),
li:target,
:target {
  scroll-margin-top: calc(var(--topbar-h) + 1.5rem);
}

p:has(> a[id]:target),
.footnote-list li:target {
  background: var(--target-bg);
  border-radius: 6px;
  padding: 0.2rem 0.45rem;
  margin-left: -0.45rem;
  transition: background 0.3s ease;
}

blockquote {
  margin: 1.25rem 0;
  padding: 0.75rem 1.1rem;
  border-left: 4px solid var(--accent);
  background: var(--bg-alt);
  border-radius: 0 8px 8px 0;
}

blockquote > :first-child { margin-top: 0; }
blockquote > :last-child { margin-bottom: 0; }

.callout {
  margin: 1.35rem 0;
  padding: 0.9rem 1.1rem;
  border-left: 4px solid var(--accent);
  background: var(--bg-alt);
  border-radius: 0 8px 8px 0;
}

.callout-title {
  font-weight: 700;
  font-size: 0.88rem;
  text-transform: uppercase;
  letter-spacing: 0.04em;
  margin-bottom: 0.4rem;
}

.callout-tip { border-left-color: #10b981; }
.callout-important { border-left-color: #8b5cf6; }
.callout-warning { border-left-color: #f59e0b; }
.callout-caution { border-left-color: #ef4444; }
.callout-body > :first-child { margin-top: 0; }
.callout-body > :last-child { margin-bottom: 0; }

code {
  font-family: var(--font-mono);
  font-size: 0.88em;
  background: var(--code-bg);
  padding: 0.12em 0.36em;
  border-radius: 4px;
}

pre {
  background: var(--pre-bg);
  color: var(--pre-text);
  padding: 1rem 1.15rem;
  border-radius: 8px;
  overflow-x: auto;
  line-height: 1.5;
  font-size: 0.86rem;
}

pre code {
  background: transparent;
  padding: 0;
  font-size: inherit;
  color: inherit;
}

.mermaid-wrap {
  margin: 1.5rem 0;
  padding: 1rem;
  border: 1px solid var(--border);
  border-radius: 10px;
  background: var(--bg-alt);
  overflow-x: auto;
  text-align: center;
}

.mermaid-wrap pre.mermaid {
  margin: 0;
  background: transparent;
  color: var(--text);
  text-align: left;
}

.mermaid-wrap figcaption {
  margin-top: 0.6rem;
  font-size: 0.84rem;
  color: var(--text-muted);
}

.table-wrap {
  width: 100%;
  overflow-x: auto;
  margin: 1.35rem 0;
  border: 1px solid var(--border);
  border-radius: 8px;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.92rem;
}

th, td {
  padding: 0.6rem 0.8rem;
  border-bottom: 1px solid var(--border);
  text-align: left;
  vertical-align: top;
}

th {
  background: var(--bg-alt);
  color: var(--heading);
  font-weight: 600;
}

tr:last-child td { border-bottom: none; }
tbody tr:nth-child(even) td { background: rgba(148, 163, 184, 0.06); }

hr {
  border: 0;
  border-top: 1px solid var(--border);
  margin: 2rem 0;
}

.fn-ref a {
  text-decoration: none;
  font-weight: 600;
  padding: 0 1px;
}

.footnotes {
  margin-top: 3rem;
  padding-top: 1rem;
  border-top: 1px solid var(--border);
  font-size: 0.9rem;
}

.footnotes h2 {
  margin-top: 0;
  border-bottom: none;
  font-size: 1.2rem;
}

.footnote-list {
  padding-left: 1.4rem;
}

.footnote-list li {
  margin-bottom: 0.75rem;
  overflow-wrap: anywhere;
}

.fn-backref {
  text-decoration: none;
  margin-left: 0.25rem;
  font-size: 0.88em;
}

.pager {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  margin-top: 3rem;
  padding-top: 1.5rem;
  border-top: 1px solid var(--border);
}

.pager-card {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
  padding: 0.9rem 1rem;
  border: 1px solid var(--border);
  border-radius: 10px;
  text-decoration: none;
  background: var(--bg-alt);
}

.pager-card:hover { border-color: var(--accent); background: var(--accent-soft); }
.pager-next { text-align: right; }
.pager-dir { font-size: 0.78rem; color: var(--text-muted); font-weight: 600; }
.pager-title { font-size: 0.95rem; font-weight: 600; color: var(--heading); }

.doc-footer {
  max-width: 78ch;
  margin: 2rem auto 0;
  font-size: 0.8rem;
  color: var(--text-muted);
  text-align: center;
}

.page-toc {
  position: sticky;
  top: var(--topbar-h);
  height: calc(100vh - var(--topbar-h));
  overflow-y: auto;
  padding: 1.5rem 1rem;
}

.page-toc-title {
  font-size: 0.74rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  color: var(--text-muted);
  margin-bottom: 0.6rem;
}

.page-toc ul {
  list-style: none;
  margin: 0;
  padding: 0;
  border-left: 1px solid var(--border);
}

.page-toc li a {
  display: block;
  padding: 0.24rem 0 0.24rem 0.75rem;
  font-size: 0.8rem;
  line-height: 1.35;
  color: var(--text-muted);
  text-decoration: none;
  border-left: 2px solid transparent;
  margin-left: -1px;
}

.page-toc li.toc-l3 a { padding-left: 1.35rem; font-size: 0.77rem; }

.page-toc li a:hover,
.page-toc li a.is-active {
  color: var(--accent);
  border-left-color: var(--accent);
}

/* Index / Cover Page */
.hero {
  padding: 1.75rem;
  border: 1px solid var(--border);
  border-radius: 12px;
  background: var(--bg-alt);
  margin-bottom: 2rem;
}

.hero-subtitle { font-size: 1.15rem; color: var(--text-muted); margin: 0.25rem 0 0.75rem; }
.hero-author { font-weight: 600; margin: 0 0 1rem; }

.hero-stats {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin: 1rem 0 1.25rem;
}

.hero-stats span {
  background: var(--bg);
  border: 1px solid var(--border);
  padding: 0.3rem 0.65rem;
  border-radius: 999px;
  font-size: 0.83rem;
}

.hero-actions {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 1rem;
}

.btn-primary {
  display: inline-block;
  background: var(--accent);
  color: #ffffff;
  text-decoration: none;
  font-weight: 600;
  padding: 0.55rem 1.1rem;
  border-radius: 8px;
}

.hero-date { font-size: 0.84rem; color: var(--text-muted); }

.index-group { margin-bottom: 1.65rem; }
.index-list { list-style: none; padding: 0; margin: 0.6rem 0 0; }
.index-list li { margin-bottom: 0.35rem; }

.index-list a {
  display: flex;
  justify-content: space-between;
  align-items: baseline;
  gap: 1rem;
  padding: 0.5rem 0.75rem;
  border: 1px solid var(--border);
  border-radius: 8px;
  text-decoration: none;
  color: var(--heading);
  background: var(--bg);
}

.index-list a:hover { border-color: var(--accent); background: var(--accent-soft); }
.toc-chap-title { font-weight: 500; }
.toc-chap-meta { font-size: 0.8rem; color: var(--text-muted); white-space: nowrap; }

.sidebar-backdrop { display: none; }

@media (max-width: 1200px) {
  .layout { grid-template-columns: var(--sidebar-w) minmax(0, 1fr); }
  .page-toc { display: none; }
}

@media (max-width: 880px) {
  .menu-toggle { display: inline-flex; align-items: center; justify-content: center; }
  .layout { grid-template-columns: minmax(0, 1fr); }
  .main { padding: 1.25rem 1rem 2.5rem; }
  .sidebar {
    position: fixed;
    top: var(--topbar-h);
    left: 0;
    width: min(86vw, 310px);
    z-index: 50;
    transform: translateX(-105%);
    transition: transform 0.2s ease;
    box-shadow: var(--shadow);
  }
  body.sidebar-open .sidebar { transform: translateX(0); }
  body.sidebar-open .sidebar-backdrop {
    display: block;
    position: fixed;
    inset: var(--topbar-h) 0 0 0;
    background: rgba(15, 23, 42, 0.45);
    z-index: 45;
  }
  .search-results { right: 0; }
  .pager { grid-template-columns: 1fr; }
}

@media print {
  .topbar, .sidebar, .page-toc, .pager, .sidebar-backdrop { display: none !important; }
  .layout { display: block; }
  .main { padding: 0; }
  .content { max-width: none; }
  a { color: inherit; }
}
"""

APP_JS = r"""/* Generated by book/tools/export_html.py */
(function () {
  var htmlEl = document.documentElement;
  var themeBtn = document.getElementById("theme-toggle");
  var menuBtn = document.getElementById("menu-toggle");
  var backdrop = document.getElementById("sidebar-backdrop");
  var searchInput = document.getElementById("search-input");
  var searchResults = document.getElementById("search-results");
  var searchFocusBtn = document.getElementById("search-focus-btn");

  // Preserve original Mermaid definitions so theme switches re-render cleanly.
  var mermaidNodes = Array.prototype.slice.call(document.querySelectorAll("pre.mermaid"));
  mermaidNodes.forEach(function (node) {
    node.setAttribute("data-mermaid-src", node.textContent || "");
  });

  function renderMermaid() {
    if (!window.mermaid || !mermaidNodes.length) return;
    var isDark = htmlEl.getAttribute("data-theme") === "dark";
    mermaidNodes.forEach(function (node) {
      node.removeAttribute("data-processed");
      node.innerHTML = "";
      node.textContent = node.getAttribute("data-mermaid-src") || "";
    });
    window.mermaid.initialize({
      startOnLoad: false,
      theme: isDark ? "dark" : "neutral",
      securityLevel: "loose"
    });
    window.mermaid.run({ nodes: mermaidNodes });
  }

  function isValidTheme(val) {
    return val === "dark" || val === "light";
  }

  function readExplicitTheme() {
    var param = null;
    try {
      param = new URLSearchParams(window.location.search).get("theme");
    } catch (e) {}
    if (isValidTheme(param)) return param;

    var saved = null;
    try {
      saved = localStorage.getItem("book-theme");
    } catch (e) {}
    if (isValidTheme(saved)) return saved;

    try {
      var wm = (window.name || "").match(/^book-theme:(dark|light)$/);
      if (wm && isValidTheme(wm[1])) return wm[1];
    } catch (e) {}
    return null;
  }

  function storageWorks() {
    try {
      var probeKey = "__book_theme_probe__";
      localStorage.setItem(probeKey, "1");
      var ok = localStorage.getItem(probeKey) === "1";
      localStorage.removeItem(probeKey);
      return ok;
    } catch (e) {
      return false;
    }
  }

  function needsUrlThemeSync() {
    // file:// origins are isolated per-path in Safari/Firefox, so propagate ?theme= on file:// too.
    return window.location.protocol === "file:" || !storageWorks();
  }

  function persistTheme(theme) {
    try { localStorage.setItem("book-theme", theme); } catch (e) {}
    try { window.name = "book-theme:" + theme; } catch (e) {}
  }

  function applyThemeToHref(rawHref, theme) {
    if (!rawHref || rawHref.charAt(0) === "#") return rawHref;
    if (/^(?:[a-z][a-z0-9+.-]*:|\/\/)/i.test(rawHref)) return rawHref;

    var hashIdx = rawHref.indexOf("#");
    var beforeHash = hashIdx === -1 ? rawHref : rawHref.slice(0, hashIdx);
    var hashPart = hashIdx === -1 ? "" : rawHref.slice(hashIdx);
    var qIdx = beforeHash.indexOf("?");
    var pathPart = qIdx === -1 ? beforeHash : beforeHash.slice(0, qIdx);
    var queryPart = qIdx === -1 ? "" : beforeHash.slice(qIdx + 1);

    if (!/\.html?$/i.test(pathPart)) return rawHref;

    var params = new URLSearchParams(queryPart);
    params.set("theme", theme);
    var qs = params.toString();
    return pathPart + (qs ? "?" + qs : "") + hashPart;
  }

  function syncInternalLinks(theme) {
    var links = document.querySelectorAll("a[href]");
    for (var i = 0; i < links.length; i++) {
      var raw = links[i].getAttribute("href");
      var updated = applyThemeToHref(raw, theme);
      if (updated !== raw) {
        links[i].setAttribute("href", updated);
      }
    }
  }

  function syncCurrentUrl(theme) {
    try {
      var params = new URLSearchParams(window.location.search);
      params.set("theme", theme);
      var qs = params.toString();
      var nextUrl = window.location.pathname + (qs ? "?" + qs : "") + (window.location.hash || "");
      window.history.replaceState(null, "", nextUrl);
    } catch (e) {}
  }

  function updateToggleButton(theme) {
    if (!themeBtn) return;
    var isDark = theme === "dark";
    themeBtn.setAttribute("aria-pressed", String(isDark));
    themeBtn.setAttribute("title", isDark ? "Switch to light mode" : "Switch to dark mode");
  }

  var explicitTheme = readExplicitTheme();
  var initialTheme = htmlEl.getAttribute("data-theme") || "light";
  updateToggleButton(initialTheme);
  if (explicitTheme) {
    persistTheme(explicitTheme);
    if (needsUrlThemeSync()) {
      syncInternalLinks(explicitTheme);
    }
  }

  if (themeBtn) {
    themeBtn.addEventListener("click", function () {
      var next = htmlEl.getAttribute("data-theme") === "dark" ? "light" : "dark";
      explicitTheme = next;
      htmlEl.setAttribute("data-theme", next);
      htmlEl.setAttribute("data-theme-explicit", "1");
      updateToggleButton(next);
      persistTheme(next);
      if (needsUrlThemeSync()) {
        syncCurrentUrl(next);
        syncInternalLinks(next);
      }
      renderMermaid();
    });
  }

  window.addEventListener("pageshow", function () {
    var synced = readExplicitTheme();
    if (!synced) return;
    explicitTheme = synced;
    var current = htmlEl.getAttribute("data-theme");
    if (current !== synced) {
      htmlEl.setAttribute("data-theme", synced);
      htmlEl.setAttribute("data-theme-explicit", "1");
      updateToggleButton(synced);
      renderMermaid();
    }
    if (needsUrlThemeSync()) {
      syncInternalLinks(synced);
    }
  });

  function closeSidebar() {
    document.body.classList.remove("sidebar-open");
    if (menuBtn) menuBtn.setAttribute("aria-expanded", "false");
  }

  if (menuBtn) {
    menuBtn.addEventListener("click", function () {
      var isOpen = document.body.classList.toggle("sidebar-open");
      menuBtn.setAttribute("aria-expanded", String(isOpen));
    });
  }

  if (backdrop) backdrop.addEventListener("click", closeSidebar);

  // Scroll active sidebar entry gently into view.
  var activeLink = document.querySelector(".sidebar-nav a.is-active");
  if (activeLink && activeLink.scrollIntoView) {
    activeLink.scrollIntoView({ block: "center" });
  }

  // Right-hand TOC scroll-spy.
  var tocLinks = Array.prototype.slice.call(document.querySelectorAll(".page-toc a"));
  if (tocLinks.length && "IntersectionObserver" in window) {
    var linkById = {};
    var targets = [];
    tocLinks.forEach(function (a) {
      var id = decodeURIComponent((a.getAttribute("href") || "").replace(/^#/, ""));
      var el = id ? document.getElementById(id) : null;
      if (el) {
        linkById[id] = a;
        targets.push(el);
      }
    });

    function setActiveToc(id) {
      tocLinks.forEach(function (a) { a.classList.remove("is-active"); });
      if (id && linkById[id]) linkById[id].classList.add("is-active");
    }

    var observer = new IntersectionObserver(
      function (entries) {
        for (var i = 0; i < entries.length; i++) {
          if (entries[i].isIntersecting) {
            setActiveToc(entries[i].target.id);
            break;
          }
        }
      },
      { rootMargin: "-72px 0px -70% 0px", threshold: 0.01 }
    );
    targets.forEach(function (t) { observer.observe(t); });
  }

  // Client-side search across window.BOOK_SEARCH_INDEX.
  function escapeHtml(s) {
    return s.replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function highlightMatch(snippet, terms) {
    var safe = escapeHtml(snippet);
    terms.forEach(function (term) {
      if (!term) return;
      var esc = term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
      safe = safe.replace(new RegExp("(" + esc + ")", "gi"), "<mark>$1</mark>");
    });
    return safe;
  }

  function runSearch(rawQuery) {
    if (!searchResults) return;
    var q = (rawQuery || "").trim().toLowerCase();
    if (q.length < 2) {
      searchResults.hidden = true;
      searchResults.innerHTML = "";
      return;
    }

    var index = window.BOOK_SEARCH_INDEX || [];
    var terms = q.split(/\s+/).filter(Boolean);
    var hits = [];

    for (var i = 0; i < index.length; i++) {
      var rec = index[i];
      var tLow = rec.t.toLowerCase();
      var sLow = rec.s.toLowerCase();
      var bLow = rec.b.toLowerCase();
      var hay = tLow + " " + sLow + " " + bLow;
      var ok = true;
      for (var j = 0; j < terms.length; j++) {
        if (hay.indexOf(terms[j]) === -1) { ok = false; break; }
      }
      if (!ok) continue;

      var score = 0;
      terms.forEach(function (term) {
        if (tLow.indexOf(term) !== -1) score += 10;
        if (sLow.indexOf(term) !== -1) score += 6;
        if (bLow.indexOf(term) !== -1) score += 1;
      });
      hits.push({ rec: rec, score: score });
    }

    hits.sort(function (a, b) { return b.score - a.score; });
    hits = hits.slice(0, 15);

    if (!hits.length) {
      searchResults.innerHTML = '<div class="search-empty">No matching passages found.</div>';
      searchResults.hidden = false;
      return;
    }

    searchResults.innerHTML = hits.map(function (h) {
      var rec = h.rec;
      var href = rec.p + (rec.id ? "#" + rec.id : "");
      if (explicitTheme && needsUrlThemeSync()) {
        href = applyThemeToHref(href, explicitTheme);
      }
      var pos = rec.b.toLowerCase().indexOf(terms[0]);
      var start = Math.max(0, pos - 55);
      var end = Math.min(rec.b.length, (pos === -1 ? 120 : pos + 115));
      var snip = (start > 0 ? "…" : "") + rec.b.slice(start, end) + (end < rec.b.length ? "…" : "");
      return (
        '<a class="search-item" href="' + escapeHtml(href) + '">' +
        '<div class="search-item-title">' + escapeHtml(rec.t) + "</div>" +
        '<div class="search-item-sec">' + escapeHtml(rec.s) + "</div>" +
        '<div class="search-item-snippet">' + highlightMatch(snip, terms) + "</div>" +
        "</a>"
      );
    }).join("");
    searchResults.hidden = false;
  }

  var searchTimer = null;
  if (searchInput) {
    searchInput.addEventListener("input", function () {
      clearTimeout(searchTimer);
      searchTimer = setTimeout(function () { runSearch(searchInput.value); }, 110);
    });
    searchInput.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        searchResults.hidden = true;
        searchInput.blur();
      } else if (e.key === "Enter" && !searchResults.hidden) {
        var first = searchResults.querySelector("a.search-item");
        if (first) {
          e.preventDefault();
          window.location.href = first.getAttribute("href");
          searchResults.hidden = true;
          closeSidebar();
        }
      }
    });
  }

  function focusSearch() {
    if (!searchInput) return;
    if (window.innerWidth <= 880) {
      document.body.classList.add("sidebar-open");
      if (menuBtn) menuBtn.setAttribute("aria-expanded", "true");
    }
    searchInput.focus();
    searchInput.select();
  }

  if (searchFocusBtn) searchFocusBtn.addEventListener("click", focusSearch);

  document.addEventListener("keydown", function (e) {
    var tag = (e.target && e.target.tagName) ? e.target.tagName.toLowerCase() : "";
    if ((e.key === "/" && tag !== "input" && tag !== "textarea") || ((e.metaKey || e.ctrlKey) && e.key.toLowerCase() === "k")) {
      e.preventDefault();
      focusSearch();
    }
  });

  document.addEventListener("click", function (e) {
    if (searchResults && !searchResults.hidden) {
      if (!searchResults.contains(e.target) && e.target !== searchInput && e.target !== searchFocusBtn) {
        searchResults.hidden = true;
      }
    }
  });

  window.addEventListener("load", renderMermaid);
  if (document.readyState === "complete") renderMermaid();
})();
"""


def serve_directory(output_dir: Path, host: str, port: int, open_browser: bool) -> int:
    """Serve `output_dir` over HTTP until interrupted."""
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(output_dir))

    class ReusableThreadingTCPServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
        allow_reuse_address = True
        daemon_threads = True

    url = f"http://{host}:{port}/index.html"
    try:
        with ReusableThreadingTCPServer((host, port), handler) as httpd:
            print(f"Serving HTML book at {url} (Ctrl+C to stop)")
            if open_browser:
                webbrowser.open(url)
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped.")
    return 0


def build_arg_parser() -> argparse.ArgumentParser:
    """Construct the CLI argument parser."""
    parser = argparse.ArgumentParser(
        description="Export the book's Markdown chapters and Annotated Bibliography as linked multi-page HTML."
    )
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help=f"Output HTML directory (default: {DEFAULT_OUTPUT_DIR.relative_to(BOOK.parent)}).",
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
        help="Exclude book/bibliography.md from the HTML build.",
    )
    parser.add_argument("--title", default=DEFAULT_TITLE, help="Book title metadata.")
    parser.add_argument(
        "--subtitle",
        default=DEFAULT_SUBTITLE,
        help="Book subtitle metadata (pass empty string to omit).",
    )
    parser.add_argument("--author", default=None, help="Optional author line.")
    parser.add_argument(
        "--date",
        dest="doc_date",
        default=date.today().isoformat(),
        help="Edition date string (default: today ISO date).",
    )
    parser.add_argument(
        "--skip-check",
        action="store_true",
        help="Skip running book/tools/check_refs.py before generating HTML.",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove existing .html files in the output directory before writing.",
    )
    parser.add_argument(
        "--serve",
        action="store_true",
        help="Start a local HTTP preview server after building.",
    )
    parser.add_argument("--host", default="127.0.0.1", help="HTTP server host (default: 127.0.0.1).")
    parser.add_argument("--port", type=int, default=8000, help="HTTP server port (default: 8000).")
    parser.add_argument(
        "--open",
        action="store_true",
        help="Open index.html in the default web browser after building.",
    )
    parser.add_argument(
        "--no-mermaid-cdn",
        action="store_true",
        help="Omit Mermaid.js CDN script tag (renders Mermaid diagrams as code blocks offline).",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """CLI entrypoint for building the multi-page linked HTML edition."""
    parser = build_arg_parser()
    args = parser.parse_args(argv)

    all_chapter_paths = sorted(CHAPTERS_DIR.glob("[0-9][0-9]-*.md"))
    if not all_chapter_paths:
        print(f"ERROR: No chapter files found in {CHAPTERS_DIR}.", file=sys.stderr)
        return 1

    try:
        selected_paths = parse_chapter_selection(args.chapters, all_chapter_paths)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    if not args.skip_check and not run_ref_check():
        print("Reference check failed; fix errors or pass --skip-check.", file=sys.stderr)
        return 1

    output_dir: Path = args.output_dir
    assets_dir = output_dir / "assets"
    if args.clean and output_dir.exists():
        for stale in output_dir.glob("*.html"):
            stale.unlink()
    assets_dir.mkdir(parents=True, exist_ok=True)

    chapters = [extract_chapter_meta(p) for p in selected_paths]
    included_by_num = {ch.num: ch for ch in chapters}
    use_bib = (not args.no_bibliography) and BIB_PATH.exists()

    sidebar_groups = build_sidebar_groups(chapters, include_bibliography=use_bib)
    md = create_markdown_renderer()
    include_mermaid_cdn = not args.no_mermaid_cdn

    # Render chapter HTMLs first to gather full counts, TOCs, and search records.
    rendered_chapters: list[tuple[ChapterMeta, str, list[TocItem]]] = []
    total_footnotes = 0
    total_refs = 0
    total_mermaid = 0
    search_records: list[dict[str, str]] = []

    for ch in chapters:
        body_html, toc, ch_stats = render_chapter_page(
            ch,
            md,
            include_bibliography=use_bib,
            included_chapters_by_num=included_by_num,
        )
        rendered_chapters.append((ch, body_html, toc))
        total_footnotes += ch_stats["footnotes"]
        total_refs += ch_stats["footnote_refs"]
        total_mermaid += ch_stats["mermaid"]
        search_records.extend(extract_search_records(ch.filename, ch.title, body_html))

    bib_body_html = ""
    bib_toc: list[TocItem] = []
    bib_entries_count = 0
    if use_bib:
        bib_body_html, bib_toc, bib_entries_count = render_bibliography_page(
            BIB_PATH,
            md,
            included_chapters_by_num=included_by_num,
        )
        search_records.extend(
            extract_search_records("bibliography.html", "Annotated Bibliography", bib_body_html)
        )

    linear_pages: list[NavPage] = [
        NavPage("index.html", f"{args.title} — Contents", "Contents", "Contents")
    ]
    for ch in chapters:
        linear_pages.append(NavPage(ch.filename, ch.title, ch.title, ch.part))
    if use_bib:
        linear_pages.append(
            NavPage("bibliography.html", "Annotated Bibliography", "Annotated Bibliography", "Reference")
        )

    # Write index.html
    index_body = build_index_body(
        title=args.title,
        subtitle=args.subtitle,
        author=args.author,
        doc_date=args.doc_date,
        chapters=chapters,
        include_bibliography=use_bib,
        bib_entries_count=bib_entries_count,
        total_footnotes=total_footnotes,
        total_mermaid=total_mermaid,
    )
    index_html = render_page_shell(
        page_title="Contents",
        book_title=args.title,
        book_subtitle=args.subtitle,
        author=args.author,
        doc_date=args.doc_date,
        current_filename="index.html",
        eyebrow="",
        reading_meta="",
        body_html=index_body,
        sidebar_groups=sidebar_groups,
        toc=[],
        prev_page=None,
        next_page=linear_pages[1] if len(linear_pages) > 1 else None,
        include_mermaid_cdn=False,
    )
    (output_dir / "index.html").write_text(index_html, encoding="utf-8")

    # Write chapter pages
    for idx, (ch, body_html, toc) in enumerate(rendered_chapters):
        pos_in_linear = idx + 1
        prev_page = linear_pages[pos_in_linear - 1]
        next_page = linear_pages[pos_in_linear + 1] if pos_in_linear + 1 < len(linear_pages) else None
        read_min = max(1, round(ch.words / 240))
        page_html = render_page_shell(
            page_title=ch.title,
            book_title=args.title,
            book_subtitle=args.subtitle,
            author=args.author,
            doc_date=args.doc_date,
            current_filename=ch.filename,
            eyebrow=ch.part,
            reading_meta=f"{ch.words:,} words · ~{read_min} min read",
            body_html=body_html,
            sidebar_groups=sidebar_groups,
            toc=toc,
            prev_page=prev_page,
            next_page=next_page,
            include_mermaid_cdn=include_mermaid_cdn,
        )
        (output_dir / ch.filename).write_text(page_html, encoding="utf-8")

    # Write bibliography.html
    if use_bib:
        bib_html = render_page_shell(
            page_title="Annotated Bibliography",
            book_title=args.title,
            book_subtitle=args.subtitle,
            author=args.author,
            doc_date=args.doc_date,
            current_filename="bibliography.html",
            eyebrow="Reference",
            reading_meta=f"{bib_entries_count} sources",
            body_html=bib_body_html,
            sidebar_groups=sidebar_groups,
            toc=bib_toc,
            prev_page=linear_pages[-2] if len(linear_pages) > 1 else None,
            next_page=None,
            include_mermaid_cdn=False,
        )
        (output_dir / "bibliography.html").write_text(bib_html, encoding="utf-8")

    # Write static assets
    (assets_dir / "style.css").write_text(STYLESHEET_CSS, encoding="utf-8")
    (assets_dir / "app.js").write_text(APP_JS, encoding="utf-8")
    search_payload = f"window.BOOK_SEARCH_INDEX = {json.dumps(search_records, ensure_ascii=False)};\n"
    (assets_dir / "search-index.js").write_text(search_payload, encoding="utf-8")

    page_count = 1 + len(chapters) + (1 if use_bib else 0)
    print(
        f"Wrote {output_dir} | pages: {page_count} (chapters={len(chapters)}, "
        f"bibliography={'yes' if use_bib else 'no'}) | footnotes: {total_footnotes} "
        f"(refs={total_refs}) | mermaid: {total_mermaid} | search_sections: {len(search_records)}"
    )

    if args.serve:
        return serve_directory(output_dir, args.host, args.port, open_browser=args.open)

    if args.open:
        webbrowser.open((output_dir / "index.html").resolve().as_uri())

    return 0


if __name__ == "__main__":
    sys.exit(main())
