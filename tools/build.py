#!/usr/bin/env python3
"""Assemble the combined manuscript from front matter, chapters, and bibliography.

Output: book/manuscript.md
  - Chapters are concatenated in numeric order.
  - Footnote links to ../bibliography.md#key become in-document links (#key).
  - "Cited in" chapter links become in-document chapter anchors.
Run check_refs.py first; build aborts if references do not match.
"""
from __future__ import annotations

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

BOOK = Path(__file__).resolve().parent.parent
CHAPTERS = sorted((BOOK / "chapters").glob("[0-9][0-9]-*.md"))
FRONT = BOOK / "front-matter.md"
BIB = BOOK / "bibliography.md"
OUT = BOOK / "manuscript.md"

TITLE = "AI Risk, Security, Governance & Compliance"
SUBTITLE = "The Enterprise Guardrails Handbook"


def chapter_anchor(n: int) -> str:
    return f"chapter-{n}"


def main() -> int:
    check = subprocess.run([sys.executable, str(BOOK / "tools" / "check_refs.py")])
    if check.returncode != 0:
        print("Reference check failed; fix errors before building.")
        return 1

    parts: list[str] = [
        f"# {TITLE}\n\n## {SUBTITLE}\n\n*Manuscript build: {date.today().isoformat()}*\n",
    ]
    if FRONT.exists():
        parts.append(FRONT.read_text(encoding="utf-8"))

    toc = ["## Contents\n"]
    for ch in CHAPTERS:
        first = ch.read_text(encoding="utf-8").splitlines()[0].lstrip("# ").strip()
        toc.append(f"- [{first}](#{chapter_anchor(int(ch.name[:2]))})")
    toc.append("- [Annotated Bibliography](#bibliography)\n")
    parts.append("\n".join(toc))

    for ch in CHAPTERS:
        text = ch.read_text(encoding="utf-8")
        text = text.replace("../bibliography.md#", "#")
        text = text.replace("](../references/", "](references/")
        parts.append(f'<a id="{chapter_anchor(int(ch.name[:2]))}"></a>\n\n{text}')

    bib = BIB.read_text(encoding="utf-8")
    bib = re.sub(r"\]\(chapters/(\d\d)-[^)]+\)", lambda m: f"](#{chapter_anchor(int(m.group(1)))})", bib)
    parts.append(f'<a id="bibliography"></a>\n\n{bib}')

    OUT.write_text("\n\n---\n\n".join(parts) + "\n", encoding="utf-8")
    words = len(re.findall(r"\b\w+\b", OUT.read_text(encoding="utf-8")))
    print(f"Wrote {OUT.relative_to(BOOK.parent)} ({len(CHAPTERS)} chapter(s), ~{words:,} words)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
