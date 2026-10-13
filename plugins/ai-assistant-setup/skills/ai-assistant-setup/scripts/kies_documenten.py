#!/usr/bin/env python3
"""
kies_documenten.py: kiest welke documenten de documentlezers lezen, en verdeelt ze in pakketten.

Leest enkel namen, groottes en datums om te kiezen. Opent geen enkel bestand
en schrijft niets in de map van de klant, enkel naar --json en --md.

Gebruik:
    python3 kies_documenten.py --map "<hoofdmap>" --config "<config.json>" \
        --json leesplan.json --md leesplan.md

De rollen komen uit `bestaande_mappen` in de config:
    referentie  → pakket "templates en voorbeelden"
    werk        → pakket "recente output"
    overig      → pakket "recente output"
    instanties  → pakket "klantwerk" (de klantmappen met het meest recente werk)
    archief, buiten_bereik → nooit gelezen
Daarnaast zoekt het script over de hele map naar materiaal over het bedrijf
(masterprompt, AI-clone, voorstelling, website-tekst) en zet dat in het pakket
"over het bedrijf".
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

LEESBAAR = {".docx", ".docm", ".dotx", ".odt", ".pptx", ".pdf", ".txt", ".md", ".rtf", ".eml", ".html", ".htm"}
LAAG = {"claude.md", "setup-start-hier.md", "setup-status.md", "leesmij-assistent.md",
        "_kern", "_kennis", "_context", "_inbox", "_projecten", "_ai-setup"}
OVER_ONS = re.compile(r"master\s*-?prompt|ai[\s_-]*clone|over[\s_-]*ons|bedrijfs?voorstelling|voorstelling|"
                      r"brochure|website|about|profiel|bedrijfsprofiel|missie|visie|aanbod|diensten", re.I)
TIJDELIJK = re.compile(r"^(~\$|\.~|\.)|\.tmp$|^thumbs\.db$|^desktop\.ini$", re.I)

PAKKETTEN = {
    "over-het-bedrijf": ("Over het bedrijf",
                         "Feiten over het bedrijf en de ondernemer: wat ze doen, voor wie, aanbod, werkwijze. "
                         "Geen uitspraken over wie de ondernemer is als persoon."),
    "templates-en-voorbeelden": ("Templates en voorbeelden",
                                 "Vaste opbouw, vaste formuleringen, huisstijl en notaties. Welk document is per taak het goede voorbeeld?"),
    "recente-output": ("Recente output",
                       "Hoe de ondernemer vandaag echt schrijft en werkt: terugkerende opbouw, notaties, afspraken en regels die nergens staan."),
    "klantwerk": ("Klantwerk",
                  "Wat terugkomt in het werk voor klanten: vaste stappen, termijnen, wat altijd gecontroleerd wordt. "
                  "Geen namen of gegevens van klanten in de regels."),
}


def bestanden_onder(root, rel_dir):
    basis = root / rel_dir
    for dirpath, dirnames, filenames in os.walk(basis):
        dirnames[:] = [d for d in dirnames if not TIJDELIJK.search(d)]
        for f in filenames:
            if TIJDELIJK.search(f):
                continue
            p = Path(dirpath) / f
            if p.suffix.lower() not in LEESBAAR:
                continue
            try:
                st = p.stat()
            except OSError:
                continue
            yield {"pad": p.relative_to(root).as_posix(), "grootte": st.st_size, "mtime": st.st_mtime}


def kies(root, cfg, per_map, maximum, max_mb):
    mappen = cfg.get("bestaande_mappen") or []
    verboden = [m["pad"].rstrip("/") for m in mappen if m.get("rol") in ("archief", "buiten_bereik")]
    overgeslagen = {"te groot": 0, "archief of buiten bereik": 0}
    grens = max_mb * 1024 * 1024

    def toegelaten(rel):
        return not any(rel == v or rel.startswith(v + "/") for v in verboden)

    def filter_groot(lst):
        ok = []
        for d in lst:
            if d["grootte"] > grens:
                overgeslagen["te groot"] += 1
            else:
                ok.append(d)
        return ok

    pakket = {k: [] for k in PAKKETTEN}
    gekozen = set()

    def voeg_toe(sleutel, docs, bron):
        for d in docs:
            if d["pad"] in gekozen:
                continue
            gekozen.add(d["pad"])
            pakket[sleutel].append({**d, "map": bron})

    for m in mappen:
        rol, pad = m.get("rol"), m["pad"].rstrip("/")
        if rol in ("archief", "buiten_bereik"):
            overgeslagen["archief of buiten bereik"] += 1
            continue
        if not (root / pad).is_dir():
            continue
        if rol == "instanties":
            klanten = []
            for sub in sorted((root / pad).iterdir()):
                if not sub.is_dir() or TIJDELIJK.search(sub.name):
                    continue
                rel_sub = f"{pad}/{sub.name}"
                if not toegelaten(rel_sub):
                    continue
                docs = filter_groot(list(bestanden_onder(root, rel_sub)))
                if docs:
                    klanten.append((max(d["mtime"] for d in docs), rel_sub, docs))
            for _, rel_sub, docs in sorted(klanten, reverse=True)[:3]:
                voeg_toe("klantwerk", sorted(docs, key=lambda d: -d["mtime"])[:2], rel_sub)
        else:
            docs = [d for d in filter_groot(list(bestanden_onder(root, pad))) if toegelaten(d["pad"])]
            sleutel = "templates-en-voorbeelden" if rol == "referentie" else "recente-output"
            voeg_toe(sleutel, sorted(docs, key=lambda d: -d["mtime"])[:per_map], pad)

    # materiaal over het bedrijf, overal behalve archief en buiten bereik
    kandidaten = []
    for top in sorted(root.iterdir()):
        if top.name.lower() in LAAG - {"_inbox"} or TIJDELIJK.search(top.name):
            continue
        rel_top = top.name
        if top.is_file():
            if top.suffix.lower() in LEESBAAR and OVER_ONS.search(top.stem):
                st = top.stat()
                kandidaten.append({"pad": rel_top, "grootte": st.st_size, "mtime": st.st_mtime})
            continue
        if not toegelaten(rel_top):
            continue
        for d in bestanden_onder(root, rel_top):
            if Path(d["pad"]).name.lower() == "leesmij.md":
                continue
            if toegelaten(d["pad"]) and (OVER_ONS.search(Path(d["pad"]).stem) or rel_top.lower() == "_inbox"):
                kandidaten.append(d)
    voeg_toe("over-het-bedrijf", sorted(filter_groot(kandidaten), key=lambda d: -d["mtime"])[:4], "verspreid")

    # totaal begrenzen: om de beurt uit elk pakket houden, zodat elk pakket iets overhoudt
    if sum(len(v) for v in pakket.values()) > maximum:
        gehouden = {k: [] for k in pakket}
        rij = {k: list(v) for k, v in pakket.items()}
        n = 0
        while n < maximum and any(rij.values()):
            for k in PAKKETTEN:
                if rij[k] and n < maximum:
                    gehouden[k].append(rij[k].pop(0))
                    n += 1
        overgeslagen["boven het maximum"] = sum(len(v) for v in rij.values())
        pakket = gehouden

    uit = []
    for k, (titel, vraag) in PAKKETTEN.items():
        docs = pakket[k]
        if not docs:
            continue
        # grote pakketten splitsen, zodat geen lezer meer dan 6 documenten krijgt
        for i in range(0, len(docs), 6):
            deel = docs[i:i + 6]
            nr = f"-{i // 6 + 1}" if len(docs) > 6 else ""
            uit.append({
                "id": k + nr, "titel": titel + (f" ({i // 6 + 1})" if nr else ""), "vraag": vraag,
                "documenten": [{"pad": d["pad"], "map": d["map"], "kb": round(d["grootte"] / 1024),
                                "gewijzigd": datetime.fromtimestamp(d["mtime"]).strftime("%Y-%m-%d")} for d in deel],
            })
    return uit, {k: v for k, v in overgeslagen.items() if v}


def als_md(pakketten, overgeslagen, root):
    totaal = sum(len(p["documenten"]) for p in pakketten)
    r = [f"# Leesplan\n\n{totaal} documenten in {len(pakketten)} pakketten, uit `{root}`.\n"]
    for p in pakketten:
        r.append(f"## {p['titel']} (`{p['id']}`)\n\n{p['vraag']}\n")
        for d in p["documenten"]:
            r.append(f"- `{d['pad']}` ({d['kb']} kB, {d['gewijzigd']})")
        r.append("")
    if overgeslagen:
        r.append("## Niet gelezen\n")
        for k, v in overgeslagen.items():
            r.append(f"- {k}: {v}")
        r.append("")
    return "\n".join(r)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--map", required=True, help="hoofdmap van de klant (de gekoppelde kopie)")
    ap.add_argument("--config", required=True, help="config.json met bestaande_mappen")
    ap.add_argument("--per-map", type=int, default=3, help="aantal recentste documenten per map (default 3)")
    ap.add_argument("--max", type=int, default=20, help="maximum aantal documenten in totaal (default 20)")
    ap.add_argument("--max-mb", type=float, default=10, help="grotere bestanden worden overgeslagen (default 10 MB)")
    ap.add_argument("--json", help="schrijf het leesplan als JSON")
    ap.add_argument("--md", help="schrijf het leesplan als markdown")
    a = ap.parse_args()

    root = Path(a.map)
    if not root.is_dir():
        sys.exit(f"Map niet gevonden: {root}")
    cfg = json.loads(Path(a.config).read_text(encoding="utf-8"))
    pakketten, overgeslagen = kies(root, cfg, a.per_map, a.max, a.max_mb)
    if a.json:
        Path(a.json).write_text(json.dumps({"pakketten": pakketten, "overgeslagen": overgeslagen},
                                           ensure_ascii=False, indent=2), encoding="utf-8")
    md = als_md(pakketten, overgeslagen, root)
    if a.md:
        Path(a.md).write_text(md, encoding="utf-8")
    print(md)


if __name__ == "__main__":
    main()
