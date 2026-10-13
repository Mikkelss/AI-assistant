#!/usr/bin/env python3
"""
waar_staan_we.py: bepaalt waar de setup in de gekoppelde map staat. Leest enkel, schrijft niets.

Gebruik:
    python3 waar_staan_we.py "<gekoppelde map>"

Mogelijke uitkomsten (eerste regel):
    GEEN-MAP        de map bestaat niet
    NIEUW           er staat nog geen AI-laag: de skill mag bouwen
    CONFLICT        er staat een CLAUDE.md of setup-file die niet van deze skill komt: stop
    LAAG-AANWEZIG   de AI-laag staat er al: niets bouwen, verder met de analyse of de setup-gids
Daaronder, bij LAAG-AANWEZIG: openstaande punten in _ai-setup/analyse.md en de eerste open fase.
"""

import re
import sys
from pathlib import Path


def fasen(status_md):
    tekst = status_md.read_text(encoding="utf-8", errors="ignore")
    uit = []
    for m in re.finditer(r"^### (Fase [^\n]+)\n(?:.*\n)*?\*\*Status:\*\*\s*([^\n]+)", tekst, re.M):
        uit.append((m.group(1).strip(), m.group(2).strip()))
    return uit


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    root = Path(sys.argv[1])
    if not root.is_dir():
        print("GEEN-MAP")
        return
    claude, status = root / "CLAUDE.md", root / "SETUP-STATUS.md"
    van_ons = claude.is_file() and "## Setup-trigger" in claude.read_text(encoding="utf-8", errors="ignore") \
        and status.is_file()
    if van_ons:
        print("LAAG-AANWEZIG")
        analyse = root / "_ai-setup" / "analyse.md"
        if analyse.is_file():
            open_ = len(re.findall(r"\|\s*status:\s*open\b", analyse.read_text(encoding="utf-8", errors="ignore"), re.I))
            print(f"analyse: {open_} punt(en) open")
        else:
            leesplan = (root / "_ai-setup" / "leesplan.json").is_file()
            print("analyse: leesplan klaar, documenten nog niet gelezen" if leesplan else "analyse: nog niet gedaan")
        fs = fasen(status)
        eerste = next(((f, s) for f, s in fs if not s.lower().startswith("voltooid")), None)
        print(f"eerste open fase: {eerste[0]} ({eerste[1]})" if eerste else "alle fasen voltooid")
        return
    gevonden = [n for n in ("CLAUDE.md", "SETUP-START-HIER.md", "SETUP-STATUS.md", "LEESMIJ-ASSISTENT.md") if (root / n).exists()]
    if gevonden:
        print("CONFLICT")
        print("bestaat al, niet van deze skill: " + ", ".join(gevonden))
        return
    print("NIEUW")


if __name__ == "__main__":
    main()
