#!/usr/bin/env python3
"""
scan_structuur.py: brengt een bestaande mappenstructuur in kaart, zonder één bestand te openen.

Leest enkel namen, groottes en datums. Schrijft nooit iets in de gescande map.

Bronnen (één van drie):
    python scan_structuur.py --bron "/pad/naar/map"            # rechtstreeks een map aflopen
    python scan_structuur.py --bron structuur.csv              # export uit PowerShell (Windows)
    python scan_structuur.py --bron structuur.txt              # lijst van paden (Mac: find, Windows: dir /s /b)

Opties:
    --diepte 3                 hoe diep de boom in het rapport gaat (default 3)
    --rapport kaart.md         schrijf het rapport naar een file in plaats van naar het scherm
    --json scan.json           schrijf ook de ruwe analyse en het config-voorstel als JSON
    --root "C:\\Data\\An\\..."  root van de export, als het script ze niet zelf vindt

In de skill draait de scan rechtstreeks op de gekoppelde map (zie references/bestaande-map.md, stap B).
"""

import argparse
import csv
import io
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

# Namen die de AI-laag aan de root toevoegt. Bestaat er al iets met die naam, dan is er een conflict.
LAAG_NAMEN = ["CLAUDE.md", "SETUP-START-HIER.md", "SETUP-STATUS.md", "LEESMIJ-ASSISTENT.md",
              "_kern", "_kennis", "_context", "_inbox", "_projecten"]

NEGEER = {"desktop.ini", "thumbs.db", ".ds_store", "icon\r"}

HEURISTIEK = {
    "referentie": r"template|sjabloon|model(len)?\b|voorbeeld|standaard|huisstijl|logo|brand|checklist|procedure|handleiding|richtlijn",
    "archief": r"archief|archive|\boud\b|\bold\b|afgesloten|afgewerkt|historiek|backup|back-up",
    "gevoelig": r"personeel|\bhr\b|loon|lonen|salaris|payroll|medisch|ziekte|sollicit|contracten|fiscaal|belasting|bank|priv[eé]\b|paswoord|wachtwoord|password|gdpr|juridisch|geschil",
    "inbox": r"inbox|te sorteren|to sort|downloads|scans?\b|ontvangen|temp\b|tijdelijk",
    "instanties": r"klant|client|cli[eë]nt|dossier|werf|werven|project|opdracht|leerling|pati[eë]nt|deelnemer|kandida|leverancier",
}
VERSIE_RUIS = re.compile(r"(\bv\d+\b|final|definitief|kopie|copy|\(\d\)|_oud\b|nieuw\b)", re.I)
NUMMER_PREFIX = re.compile(r"^\s*(\d+[\.\-_ ]+|[a-z][\.\)]\s+)", re.I)
JAAR = re.compile(r"^(19|20)\d\d$")
DATUM = re.compile(r"^(19|20)\d\d[-_. ]?\d\d")


# ---------------------------------------------------------------- inlezen

def lees_tekst(pad):
    raw = Path(pad).read_bytes()
    if raw.startswith(b"\xff\xfe") or raw.startswith(b"\xfe\xff"):
        return raw.decode("utf-16")
    for enc in ("utf-8-sig", "cp1252", "latin-1"):
        try:
            return raw.decode(enc)
        except UnicodeDecodeError:
            continue
    return raw.decode("utf-8", errors="replace")


def delen(p):
    p = p.replace("\\", "/").strip()
    return [x for x in p.split("/") if x not in ("", ".")]


def parse_datum(s):
    s = (s or "").strip()
    if not s:
        return None
    for fmt in ("%d/%m/%Y %H:%M:%S", "%d-%m-%Y %H:%M:%S", "%m/%d/%Y %I:%M:%S %p", "%m/%d/%Y %H:%M:%S",
                "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S", "%d/%m/%Y %H:%M", "%d.%m.%Y %H:%M:%S"):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            pass
    m = re.search(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return datetime(int(m[1]), int(m[2]), int(m[3]))
    return None


def van_map(root):
    root = Path(root)
    items = []
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        rel = Path(dirpath).relative_to(root)
        rel_parts = [] if str(rel) == "." else list(rel.parts)
        for d in dirnames:
            try:
                st = os.stat(os.path.join(dirpath, d), follow_symlinks=False)
                mt = datetime.fromtimestamp(st.st_mtime)
            except OSError:
                mt = None
            items.append((tuple(rel_parts + [d]), True, None, mt))
        for f in filenames:
            try:
                st = os.stat(os.path.join(dirpath, f), follow_symlinks=False)
                size, mt = st.st_size, datetime.fromtimestamp(st.st_mtime)
            except OSError:
                size, mt = None, None
            items.append((tuple(rel_parts + [f]), False, size, mt))
    return root.name, items


def strip_root(rows, root_hint):
    """rows: lijst (delen, is_dir|None, size, mtime). Haalt het gemeenschappelijke voorvoegsel weg."""
    if root_hint:
        rp = delen(root_hint)
        low = [x.lower() for x in rp]
        out = []
        for parts, isd, size, mt in rows:
            if [x.lower() for x in parts[:len(rp)]] == low:
                rest = parts[len(rp):]
                if rest:
                    out.append((rest, isd, size, mt))
        return rp[-1] if rp else "root", out
    alle = [parts for parts, *_ in rows]
    if not alle:
        return "root", []
    prefix = list(alle[0])
    for parts in alle[1:]:
        n = 0
        while n < len(prefix) and n < len(parts) and prefix[n].lower() == parts[n].lower():
            n += 1
        prefix = prefix[:n]
        if not prefix:
            break
    # Het prefix mag geen volledig pad van een file zijn: laatste deel eraf als het zelf een entry is zonder kinderen.
    if prefix and any(len(p) == len(prefix) for p in alle) and sum(1 for p in alle if len(p) > len(prefix)) == 0:
        prefix = prefix[:-1]
    naam = prefix[-1] if prefix else "root"
    out = [(parts[len(prefix):], isd, size, mt) for parts, isd, size, mt in rows if len(parts) > len(prefix)]
    return naam, out


def van_csv(pad, root_hint):
    tekst = lees_tekst(pad)
    lijnen = [l for l in tekst.splitlines() if not l.startswith("#TYPE")]
    reader = csv.DictReader(io.StringIO("\n".join(lijnen)))
    rows = []
    for r in reader:
        r = {(k or "").strip().lower(): (v or "").strip() for k, v in r.items()}
        full = r.get("fullname") or r.get("path") or r.get("pad") or ""
        if not full:
            continue
        isd = None
        if "psiscontainer" in r:
            isd = r["psiscontainer"].lower() == "true"
        elif r.get("mode"):
            isd = r["mode"].lower().startswith("d")
        size = int(r["length"]) if r.get("length", "").isdigit() else None
        mt = parse_datum(r.get("lastwritetime") or r.get("lastwritetimeutc") or r.get("gewijzigd"))
        rows.append((delen(full), isd, size, mt))
    naam, rows = strip_root(rows, root_hint)
    return naam, afronden(rows)


def van_txt(pad, root_hint):
    rows = []
    for l in lees_tekst(pad).splitlines():
        if not l.strip():
            continue
        isd = True if l.rstrip().endswith(("/", "\\")) else None
        rows.append((delen(l), isd, None, None))
    naam, rows = strip_root(rows, root_hint)
    return naam, afronden(rows)


def afronden(rows):
    """Beslist voor elke entry zonder label of het een map is, en voegt ontbrekende tussenmappen toe."""
    paden = {tuple(p) for p, *_ in rows}
    ouders = set()
    for p in paden:
        for i in range(1, len(p)):
            ouders.add(tuple(p[:i]))
    items, gezien = [], set()
    for parts, isd, size, mt in rows:
        t = tuple(parts)
        if t in gezien:
            continue
        gezien.add(t)
        if isd is None:
            isd = t in ouders or "." not in t[-1]
        items.append((t, isd, size, mt))
    for o in ouders - gezien:
        items.append((o, True, None, None))
    return items


# ---------------------------------------------------------------- analyse

def kern_naam(naam):
    return NUMMER_PREFIX.sub("", naam).strip().lower()


def analyse(root_naam, items, diepte):
    items = [it for it in items if it[0] and it[0][-1].lower() not in NEGEER and not it[0][-1].startswith("~$")]
    dirs = {p for p, isd, *_ in items if isd}
    files = [(p, size, mt) for p, isd, size, mt in items if not isd]

    per_dir = defaultdict(lambda: {"files": 0, "direct": 0, "ext": Counter(), "laatst": None, "bytes": 0, "subdirs": set()})
    for p in dirs:
        if len(p) > 1:
            per_dir[p[:-1]]["subdirs"].add(p[-1])
        per_dir[p]  # zorgt dat lege mappen bestaan
    per_dir[()]
    for p in dirs:
        if len(p) == 1:
            per_dir[()]["subdirs"].add(p[0])
    for p, size, mt in files:
        ext = Path(p[-1]).suffix.lower() or "(geen)"
        per_dir[p[:-1]]["direct"] += 1
        for i in range(0, len(p)):
            d = per_dir[p[:i]]
            d["files"] += 1
            d["ext"][ext] += 1
            d["bytes"] += size or 0
            if mt and (d["laatst"] is None or mt > d["laatst"]):
                d["laatst"] = mt

    heeft_datums = any(mt for _, _, mt in files)
    nu = max((mt for _, _, mt in files if mt), default=None)

    # instantie-kandidaten: map met veel submappen die intern dezelfde opbouw delen
    kandidaten = []
    for p, info in per_dir.items():
        kids = sorted(info["subdirs"])
        if len(kids) < 4 or len(p) > 3:
            continue
        gedeeld = Counter()
        for k in kids:
            for gk in per_dir.get(p + (k,), {"subdirs": set()})["subdirs"]:
                gedeeld[kern_naam(gk)] += 1
        n = len(kids)
        top = sorted(((naam, c) for naam, c in gedeeld.items() if c / n >= 0.3), key=lambda x: (-x[1], x[0]))
        score = (top[0][1] / n) if top else 0
        naam_hint = bool(re.search(HEURISTIEK["instanties"], "/".join(p).lower()))
        # mappen per jaar of per datum zijn geen instanties
        jaren = sum(1 for k in kids if JAAR.match(kern_naam(k)) or DATUM.match(k.strip()))
        if jaren >= n * 0.6:
            continue
        if score >= 0.4 or (naam_hint and n >= 4) or (n >= 10 and info["direct"] <= 3):
            kandidaten.append({
                "pad": "/".join(p) if p else "(root)",
                "submappen": n,
                "gedeelde_opbouw": [{"naam": naam, "aandeel": round(c / n, 2)} for naam, c in top[:8]],
                "score": round(score + (0.2 if naam_hint else 0), 2),
                "voorbeelden": kids[:5],
            })
    kandidaten.sort(key=lambda k: (-k["score"], -k["submappen"]))
    # submappen van een sterke kandidaat zijn zelf geen kandidaat (een klantmap met 4 submappen is geen klantenlaag)
    sterk = [k["pad"] for k in kandidaten if k["score"] >= 0.4]
    kandidaten = [k for k in kandidaten
                  if not any(k["pad"] != s_ and (s_ == "(root)" or k["pad"].startswith(s_ + "/")) for s_ in sterk)]

    def rol_hint(pad_tuple):
        tekst = "/".join(pad_tuple).lower()
        hits = [rol for rol, rx in HEURISTIEK.items() if re.search(rx, tekst)]
        return hits

    signalen = defaultdict(list)
    for p in sorted(dirs):
        if len(p) > diepte:
            continue
        for rol in rol_hint(p[-1:]):
            signalen[rol].append("/".join(p))
    jaarmappen = sorted({"/".join(p[:-1]) or "(root)" for p in dirs if JAAR.match(kern_naam(p[-1]))})
    datummappen = []
    for p, info in per_dir.items():
        kids = info["subdirs"]
        if len(kids) >= 5 and sum(1 for k in kids if DATUM.match(k.strip())) >= len(kids) * 0.6:
            datummappen.append(("/".join(p) or "(root)", len(kids)))
    datummappen.sort()

    conflicten = []
    top_namen = {p[0].lower(): p[0] for p, *_ in items if len(p) == 1}
    for n in LAAG_NAMEN:
        if n.lower() in top_namen:
            conflicten.append(top_namen[n.lower()])

    losse_root = sorted(p[-1] for p, *_ in files if len(p) == 1)
    versie_ruis = [("/".join(p)) for p, *_ in files if VERSIE_RUIS.search(Path(p[-1]).stem)]

    # voorstel voor bestaande_mappen: per topmap één regel, instantie-kandidaten ingevoegd op hun eigen pad
    voorstel = []
    kand_paden = {k["pad"] for k in kandidaten if k["score"] >= 0.4}
    for top in sorted(per_dir[()]["subdirs"], key=str.lower):
        info = per_dir[(top,)]
        hints = rol_hint((top,))
        binnen = sorted(k for k in kand_paden if k == top or k.startswith(top + "/"))
        stats = beschrijf(info)
        oud = heeft_datums and nu and info["laatst"] and (nu - info["laatst"]).days > 730
        if binnen:
            for k in binnen[:2]:
                voorstel.append({"pad": k, "rol": "instanties", "wat": f"[vul aan] ({stats})"})
            if binnen[0] != top:
                voorstel.append({"pad": top, "rol": rol_uit(hints, oud), "wat": f"[vul aan] ({stats})"})
        else:
            voorstel.append({"pad": top, "rol": rol_uit(hints, oud), "wat": f"[vul aan] ({stats})"})

    return {
        "root_naam": root_naam,
        "gescand_op": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "totaal": {"mappen": len(dirs), "files": len(files), "bytes": per_dir[()]["bytes"],
                   "laatst_gewijzigd": nu.strftime("%Y-%m-%d") if nu else None,
                   "extensies": per_dir[()]["ext"].most_common(10)},
        "per_dir": per_dir,
        "dirs": dirs,
        "instantie_kandidaten": kandidaten[:6],
        "signalen": {k: v[:12] for k, v in signalen.items()},
        "jaarmappen": jaarmappen[:10],
        "datummappen": datummappen[:10],
        "conflicten": conflicten,
        "losse_root": losse_root,
        "versie_ruis": len(versie_ruis),
        "versie_ruis_voorbeelden": versie_ruis[:5],
        "heeft_datums": heeft_datums,
        "voorstel": voorstel,
    }


def rol_uit(hints, oud):
    if "gevoelig" in hints:
        return "buiten_bereik"
    if "archief" in hints or oud:
        return "archief"
    if "referentie" in hints:
        return "referentie"
    if "inbox" in hints:
        return "overig"
    return "werk"


def mb(b):
    if b >= 1024 ** 3:
        return f"{b / 1024 ** 3:.1f} GB"
    if b >= 1024 ** 2:
        return f"{b / 1024 ** 2:.0f} MB"
    return f"{b / 1024:.0f} KB"


def beschrijf(info):
    ext = ", ".join(e for e, _ in info["ext"].most_common(3)) or "leeg"
    s = f"{info['files']} file{'s' if info['files'] != 1 else ''}, vooral {ext}"
    if info["laatst"]:
        s += f", laatst gewijzigd {info['laatst'].strftime('%Y-%m')}"
    return s


# ---------------------------------------------------------------- rapport

def boom(a, diepte, max_kids=10):
    per_dir = a["per_dir"]
    kand = {k["pad"] for k in a["instantie_kandidaten"] if k["score"] >= 0.4}
    regels = []

    def walk(p, prefix):
        kids = sorted(per_dir[p]["subdirs"], key=str.lower)
        is_kand = ("/".join(p) or "(root)") in kand
        toon = kids if len(kids) <= max_kids else kids[:(4 if is_kand else max_kids - 2)]
        for i, k in enumerate(toon):
            last = i == len(toon) - 1 and len(toon) == len(kids)
            info = per_dir[p + (k,)]
            extra = f"  ({info['files']} file{'s' if info['files'] != 1 else ''}"
            if info["laatst"]:
                extra += f", {info['laatst'].strftime('%Y-%m')}"
            extra += ")"
            regels.append(prefix + ("└── " if last else "├── ") + k + "/" + extra)
            if len(p) + 1 < diepte and not is_kand:
                walk(p + (k,), prefix + ("    " if last else "│   "))
        if len(toon) < len(kids):
            regels.append(prefix + f"└── … en {len(kids) - len(toon)} andere submappen")
        if per_dir[p]["direct"] and kids:
            n = per_dir[p]["direct"]
            waar = p[-1] if p else "de hoofdmap"
            regels.append(prefix + f"    (+ {n} losse file{'s' if n != 1 else ''} in {waar})")

    regels.append(f"{a['root_naam']}/")
    walk((), "")
    return "\n".join(regels)


def rapport(a, diepte):
    t = a["totaal"]
    r = []
    r.append(f"# Mappenkaart: {a['root_naam']}\n")
    r.append(f"Gescand op {a['gescand_op']}. Enkel namen, groottes en datums gelezen, geen inhoud.\n")
    r.append("## In cijfers\n")
    r.append(f"- {t['mappen']} mappen, {t['files']} files" + (f", {mb(t['bytes'])}" if t["bytes"] else ""))
    if t["laatst_gewijzigd"]:
        r.append(f"- Laatste wijziging: {t['laatst_gewijzigd']}")
    if t["extensies"]:
        r.append("- Meest voorkomende types: " + ", ".join(f"{e} ({n})" for e, n in t["extensies"]))
    if not a["heeft_datums"]:
        r.append("- Geen datums in de bron. Actief of oud is dus niet af te leiden, vraag het in de sessie.")
    r.append("")
    r.append(f"## Boom (tot {diepte} niveaus)\n")
    r.append("Mappen met één submap per klant of dossier tonen enkel de eerste namen.\n")
    r.append("```\n" + boom(a, diepte) + "\n```\n")

    r.append("## Wat de structuur verraadt\n")
    if a["instantie_kandidaten"]:
        r.append("**Kandidaten voor de klantenlaag** (map met één submap per klant, dossier of werf):\n")
        for k in a["instantie_kandidaten"]:
            if k["score"] >= 0.4:
                opb = ", ".join(f"{g['naam']} ({int(g['aandeel'] * 100)}%)" for g in k["gedeelde_opbouw"]) or "geen gedeelde submappen"
                r.append(f"- `{k['pad']}`: {k['submappen']} submappen, sterk signaal. Gedeelde opbouw: {opb}.")
            else:
                r.append(f"- `{k['pad']}`: {k['submappen']} submappen, zwak signaal (geen gedeelde opbouw). Eén map per klant? Navragen.")
        r.append("\nGedeelde submappen met een hoog aandeel zijn kandidaten voor de werkregels (\"werfverslagen staan altijd in ...\").\n")
    else:
        r.append("- Geen duidelijke map met één submap per klant gevonden. Vraag in de sessie waar klantwerk staat.\n")
    for rol, uitleg in (("gevoelig", "Namen die op gevoelige inhoud wijzen (kandidaat buiten bereik of vertrouwelijkheid)"),
                        ("referentie", "Namen die op templates of referentiedocumenten wijzen"),
                        ("archief", "Namen die op archief wijzen"),
                        ("inbox", "Namen die op een dropzone of downloadmap wijzen")):
        if a["signalen"].get(rol):
            r.append(f"**{uitleg}:** " + ", ".join(f"`{x}`" for x in a["signalen"][rol]) + "\n")
    if a["datummappen"]:
        r.append("**Eén submap per datum** (verslagen, meetings, shoots): " + ", ".join(f"`{p}` ({n})" for p, n in a["datummappen"]) + "\n")
    if a["jaarmappen"]:
        r.append("**Per jaar ingedeeld:** " + ", ".join(f"`{x}`" for x in a["jaarmappen"]) + "\n")
    if a["losse_root"]:
        r.append(f"**Losse files in de hoofdmap:** {len(a['losse_root'])} (" + ", ".join(a["losse_root"][:6]) + ("…" if len(a["losse_root"]) > 6 else "") + ")\n")
    if a["versie_ruis"]:
        r.append(f"**Versienamen** (v2, final, kopie, (1)): {a['versie_ruis']} files. Signaal voor een werkregel over welke versie de referentie is.\n")

    r.append("## Naamconflicten met de AI-laag\n")
    if a["conflicten"]:
        r.append("Deze namen bestaan al in de hoofdmap. De AI-laag kan er zo niet bij zonder iets te overschrijven. Los dit op in het ontwerpvoorstel (andere naam voor de laag), niet door haar map te hernoemen:\n")
        for c in a["conflicten"]:
            r.append(f"- `{c}`")
        r.append("")
    else:
        r.append("Geen. De AI-laag kan in de hoofdmap zonder iets te raken.\n")

    r.append("## Voorstel voor `bestaande_mappen` in de config\n")
    r.append("Automatisch voorstel op basis van namen en datums. Rollen nakijken, `wat` invullen, en in de sessie met de klant bevestigen.\n")
    r.append("```json\n" + json.dumps(a["voorstel"], ensure_ascii=False, indent=2) + "\n```\n")
    r.append("Rollen: `instanties` (één submap per klant of dossier), `werk` (terugkerend werk), `referentie` (templates, voorbeelden, huisstijl), `archief` (enkel op vraag), `buiten_bereik` (nooit openen), `overig`.\n")
    r.append("---\n\n*Deze kaart bevat namen van mappen en files van de klant. Ze blijft in _ai-setup/ van haar map.*\n")
    return "\n".join(r)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--bron", required=True, help="map, .csv (PowerShell-export) of .txt (lijst van paden)")
    ap.add_argument("--root", help="root van de export (enkel bij csv of txt, als ze niet vanzelf gevonden wordt)")
    ap.add_argument("--diepte", type=int, default=3)
    ap.add_argument("--rapport", help="schrijf het rapport naar deze file")
    ap.add_argument("--json", help="schrijf de analyse ook als JSON")
    a = ap.parse_args()

    bron = Path(a.bron)
    if bron.is_dir():
        naam, items = van_map(bron)
    elif bron.suffix.lower() == ".csv":
        naam, items = van_csv(bron, a.root)
    elif bron.is_file():
        naam, items = van_txt(bron, a.root)
    else:
        print(f"Bron {bron} niet gevonden.", file=sys.stderr)
        sys.exit(2)
    if not items:
        print("Geen entries gevonden in de bron. Klopt het formaat? Zie references/bestaande-map.md.", file=sys.stderr)
        sys.exit(2)

    res = analyse(naam, items, a.diepte)
    tekst = rapport(res, a.diepte)
    if a.rapport:
        Path(a.rapport).write_text(tekst, encoding="utf-8")
        print(f"Rapport geschreven naar {a.rapport}")
    else:
        print(tekst)
    if a.json:
        uit = {k: v for k, v in res.items() if k not in ("per_dir", "dirs")}
        uit["topmappen"] = sorted(res["per_dir"][()]["subdirs"], key=str.lower)
        Path(a.json).write_text(json.dumps(uit, ensure_ascii=False, indent=2, default=str), encoding="utf-8")
        print(f"JSON geschreven naar {a.json}")


if __name__ == "__main__":
    main()
