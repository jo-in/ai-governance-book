#!/usr/bin/env python3
"""Validate that chapter footnotes and the annotated bibliography match.

Checks:
  1. Every footnote reference [^x] in a chapter has a definition, and vice versa.
  2. Every footnote definition links to at least one bibliography entry.
  3. Every bibliography key linked from a chapter exists in bibliography.md.
  4. Every bibliography entry is cited by at least one chapter.
  5. Each entry's "Cited in" list matches the chapters that actually cite it.
  6. First citation of a source in each chapter carries an **Annotation:**.

Exit code 0 = all good; 1 = errors found.
Usage: python3 tools/check_refs.py   (run from the book/ directory or anywhere)
"""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
CHAPTERS = sorted((BOOK / "chapters").glob("[0-9][0-9]-*.md"))
BIB = BOOK / "bibliography.md"

FN_REF = re.compile(r"\[\^([A-Za-z0-9_-]+)\](?!:)")
FN_DEF = re.compile(r"^\[\^([A-Za-z0-9_-]+)\]:\s*(.*)$", re.M)
BIB_LINK = re.compile(r"bibliography\.md#([a-z0-9-]+)")
ANCHOR = re.compile(r'<a id="([a-z0-9-]+)"></a>')
CITED_IN = re.compile(r"\[(?:Ch\. \d+|Front Matter)\]\(chapters/(\d\d)-[^)]+\)")


def chapter_number(path: Path) -> int:
    return int(path.name[:2])


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []
    cited_by: dict[str, set[int]] = defaultdict(set)

    for ch in CHAPTERS:
        text = ch.read_text(encoding="utf-8")
        n = chapter_number(ch)
        defs = {m.group(1): m.group(2) for m in FN_DEF.finditer(text)}
        body = FN_DEF.sub("", text)
        refs = set(FN_REF.findall(body))

        for missing in sorted(refs - defs.keys()):
            errors.append(f"{ch.name}: footnote [^{missing}] referenced but not defined")
        for unused in sorted(defs.keys() - refs):
            errors.append(f"{ch.name}: footnote [^{unused}] defined but never referenced")

        seen_in_chapter: set[str] = set()
        for label in sorted(defs, key=lambda s: body.find(f"[^{s}]")):
            content = defs[label]
            keys = BIB_LINK.findall(content)
            if not keys:
                errors.append(f"{ch.name}: footnote [^{label}] has no bibliography link")
            for key in keys:
                cited_by[key].add(n)
                if key not in seen_in_chapter and "**Annotation:**" not in content:
                    warnings.append(
                        f"{ch.name}: first citation of '{key}' ([^{label}]) lacks an **Annotation:**"
                    )
                seen_in_chapter.add(key)

    bib_text = BIB.read_text(encoding="utf-8")
    anchors = ANCHOR.findall(bib_text)
    dupes = {a for a in anchors if anchors.count(a) > 1}
    for d in sorted(dupes):
        errors.append(f"bibliography.md: duplicate anchor '{d}'")
    anchor_set = set(anchors)

    for key in sorted(cited_by.keys() - anchor_set):
        errors.append(f"cited key '{key}' (Ch. {sorted(cited_by[key])}) missing from bibliography.md")
    for key in sorted(anchor_set - cited_by.keys()):
        errors.append(f"bibliography entry '{key}' is never cited in any chapter")

    # Verify "Cited in" lists
    entries = re.split(r'(?=<a id=")', bib_text)
    for entry in entries:
        m = ANCHOR.search(entry)
        if not m:
            continue
        key = m.group(1)
        listed = {int(x) for x in CITED_IN.findall(entry)}
        actual = cited_by.get(key, set())
        if listed != actual:
            errors.append(
                f"bibliography.md: '{key}' Cited-in lists {sorted(listed)} but actual is {sorted(actual)}"
            )

    total_notes = sum(len(FN_DEF.findall(c.read_text(encoding="utf-8"))) for c in CHAPTERS)
    print(f"Chapters checked: {len(CHAPTERS)} | footnotes: {total_notes} | "
          f"bibliography entries: {len(anchor_set)} | sources cited: {len(cited_by)}")
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    if errors:
        print(f"\n{len(errors)} error(s).")
        return 1
    print("\nAll references and bibliography entries match. ✅")
    return 0


if __name__ == "__main__":
    sys.exit(main())
