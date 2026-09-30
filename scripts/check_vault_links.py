#!/usr/bin/env python3
"""Fails if any [[wikilink]] under Docs/Palfrey Docs/ has no matching note.

Resolves links the way Obsidian resolves unambiguous wikilinks: by note
basename, ignoring folder and extension. Does not follow heading (#) or
block (^) anchors, only the note target itself.
"""
import re
import sys
from pathlib import Path

VAULT = Path("Docs/Palfrey Docs")
LINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")


def main() -> int:
    notes = {p.stem: p for p in VAULT.rglob("*.md") if ".obsidian" not in p.parts}
    broken = []
    for path in sorted(notes.values()):
        text = path.read_text(encoding="utf-8")
        for match in LINK_RE.finditer(text):
            # inside a markdown table cell, Obsidian's "|" alias separator
            # must be written "\|" so the table parser doesn't split the
            # cell early; strip that trailing backslash from the target.
            target = match.group(1).strip().rstrip("\\")
            if target and target not in notes:
                broken.append((path, target))
    if broken:
        print(f"Trovati {len(broken)} link rotti:")
        for path, target in broken:
            print(f"  {path}: [[{target}]]")
        return 1
    print(f"OK — {len(notes)} note, nessun link rotto.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
