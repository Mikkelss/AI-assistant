#!/usr/bin/env python3
"""
build_skeleton.py: bouwt een Cowork-werkomgeving uit een config.json en de templates in assets/skelet/.

Gebruik:
    python build_skeleton.py --config config.json --out "/pad/naar/Naam Cowork"
    python build_skeleton.py --config config.json --out "/pad" --force      # overschrijft een bestaande, niet-lege map
    python build_skeleton.py --check "/pad/naar/Naam Cowork"                # zoekt overgebleven {{ }} en lege mappen
    python build_skeleton.py --dry-run --config config.json                 # toont enkel de boom, schrijft niets

Modus bestaande map (config "overlay": true): bouwt enkel de AI-laag (CLAUDE.md, setup-files, _kern, _kennis,
_context, _inbox, _projecten) naast de mappen die er al zijn. Schrijft nooit over een bestaand pad, kent geen --force,
en controleert achteraf dat geen enkel bestaand bestand veranderd is.
    python build_skeleton.py --config config.json --out "/pad/An AI-laag" --bestaande scan.json   # conflictcheck met de scan

De templates gebruiken een kleine eigen syntax:
    {{var}}  {{pad.naar.var}}
    {{#if var}} ... {{else}} ... {{/if}}
    {{#each lijst}} ... {{this}} {{index1}} {{sep}} {{/each}}     (dict-items: hun keys zijn direct beschikbaar)
"""

import argparse
import json
import os
import re
import shutil
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSETS = HERE.parent / "assets"
SKELET = ASSETS / "skelet"

TAG = re.compile(r"\{\{\s*(#if|#each|else|/if|/each)?\s*([^}]*?)\s*\}\}")


# ---------------------------------------------------------------- renderer

def _lookup(path, ctx):
    if path == "this":
        return ctx.get("this")
    cur = ctx
    for part in path.split("."):
        if isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
        if cur is None:
            return None
    return cur


def render(tpl, ctx):
    out = []
    i = 0
    while i < len(tpl):
        m = TAG.search(tpl, i)
        if not m:
            out.append(tpl[i:])
            break
        out.append(tpl[i:m.start()])
        kind, arg = m.group(1), m.group(2)
        if kind is None:
            val = _lookup(arg, ctx)
            out.append("" if val is None else str(val))
            i = m.end()
            continue
        if kind in ("else", "/if", "/each"):
            raise ValueError(f"Onverwachte tag {{{{{kind}}}}} op positie {m.start()}")
        close = "/if" if kind == "#if" else "/each"
        depth, j, else_span = 1, m.end(), None
        while depth:
            m2 = TAG.search(tpl, j)
            if not m2:
                raise ValueError(f"Niet-gesloten {{{{{kind} {arg}}}}}")
            k2 = m2.group(1)
            if k2 == kind:
                depth += 1
            elif k2 == close:
                depth -= 1
            elif k2 == "else" and depth == 1 and kind == "#if":
                else_span = (m2.start(), m2.end())
            j = m2.end()
        body_start, body_end = m.end(), m2.start()
        if kind == "#if":
            val = _lookup(arg, ctx)
            if else_span:
                true_body, false_body = tpl[body_start:else_span[0]], tpl[else_span[1]:body_end]
            else:
                true_body, false_body = tpl[body_start:body_end], ""
            out.append(render(true_body if val else false_body, ctx))
        else:
            items = _lookup(arg, ctx) or []
            body = tpl[body_start:body_end]
            n = len(items)
            for idx, it in enumerate(items):
                sub = dict(ctx)
                sub["this"] = it
                sub["index1"] = idx + 1
                sub["sep"] = ", " if idx < n - 1 else ""
                if isinstance(it, dict):
                    sub.update(it)
                out.append(render(body, sub))
        i = j
    return "".join(out)


def tidy(text):
    """Maximaal twee opeenvolgende lege regels, geen trailing spaties, één newline op het einde."""
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip("\n") + "\n"


# ---------------------------------------------------------------- config

DEFAULTS = {
    "naam": "Naam",
    "bedrijfsnaam": "",
    "sector": "",
    "rol_label": "ondernemer",
    "werkdomein_eigen": "Eigen bedrijf",
    "werkdomein_lidwoord": "",
    "platform": "windows",
    "aangemaakt_op": "",
    "coach": "Michiel (AI Basecamp)",
    "coach_voornaam": "Michiel",
    "multi_instance": True,
    "instantie_meervoud": "Klanten",
    "instantie_enkelvoud": "klant",
    "instantie_lidwoord": "",
    "instantie_template": "volledig",
    "projecten_per_instantie": True,
    "stakeholders_per_instantie": False,
    "kanalen": ["linkedin", "mail", "website"],
    "kanalen_eigen_extra": [],
    "persoon_achter_instantie": "",
    "test_kanaal": "",
    "recurring_mappen": ["content", "analyses"],
    "recurring_mappen_eigen": [],
    "voice_gewicht": "midden",
    "talen": ["nl"],
    "vertrouwelijkheid": False,
    "vertrouwelijkheid_regels": [],
    "sparring": False,
    "sparring_beslissingen": [],
    "frameworks_start": [],
    "pijnpunten": [],
    "fase_nadruk": "voice",
    "tijd_per_week": "",
    "blokkades": [],
    "cloud_sync": "",
    "multi_user": False,
    "team": "",
    "materiaal": {},
    "prefill": {},
    # modus bestaande map
    "overlay": False,
    "bestaande_root": "",
    "bestaande_mappen": [],
    "bestaande_schrijven": False,
    "instanties_start": [],
}

# Wat de AI-laag in de hoofdmap zet bij overlay. Enkel deze namen worden aangemaakt.
LAAG_NAMEN = ["CLAUDE.md", "SETUP-START-HIER.md", "SETUP-STATUS.md", "LEESMIJ-ASSISTENT.md",
              "_kern", "_kennis", "_context", "_inbox", "_projecten", "_ai-setup"]
ROLLEN = ("instanties", "werk", "referentie", "archief", "buiten_bereik", "overig")


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s).strip("-").lower()
    return s or "item"


def load_config(path):
    cfg = dict(DEFAULTS)
    user = json.loads(Path(path).read_text(encoding="utf-8"))
    cfg.update(user)
    cfg["materiaal"] = {**DEFAULTS["materiaal"], **(user.get("materiaal") or {})}
    cfg["prefill"] = {k: v for k, v in (user.get("prefill") or {}).items() if v not in ("", [], None)}
    if not cfg["aangemaakt_op"]:
        from datetime import date
        cfg["aangemaakt_op"] = date.today().isoformat()
    return cfg


def derive(cfg):
    kanalen_db = json.loads((ASSETS / "kanalen.json").read_text(encoding="utf-8"))
    recurring_db = json.loads((ASSETS / "recurring.json").read_text(encoding="utf-8"))

    ctx = dict(cfg)
    ctx["volledig"] = cfg["multi_instance"] and cfg["instantie_template"] == "volledig"
    ctx["voice_hoog"] = cfg["voice_gewicht"] == "hoog"
    ctx["voice_laag"] = cfg["voice_gewicht"] == "laag"
    ov = bool(cfg.get("overlay"))
    ctx["overlay"] = ov
    if ov:
        ctx["eigen_map"] = f"_context/{cfg['werkdomein_eigen']}"
        ctx["instantie_map"] = f"_context/{cfg['instantie_meervoud']}"
        ctx["projecten_per_instantie"] = False
    else:
        ctx["eigen_map"] = f"1. {cfg['werkdomein_eigen']}"
        ctx["instantie_map"] = f"2. {cfg['instantie_meervoud']}"
    ctx["inbox_map"] = "_inbox" if ov else "0. Inbox"
    ctx["projecten_map"] = "_projecten" if ov else "9. Projecten"
    ctx["archief_map"] = "_archief"
    ctx["leesmij_root"] = "LEESMIJ-ASSISTENT.md" if ov else "LEESMIJ.md"
    # waar de voorgevulde voorstellen vandaan komen
    ctx["bron_je"] = "ons kickoffgesprek en je bestaande mappen" if ov else "je kickoff-antwoorden"
    ctx["bron_de"] = "het kickoffgesprek en de bestaande mappen" if ov else "de kickoff-antwoorden"
    ctx["bron_Uit"] = "Uit het kickoffgesprek" if ov else "Uit de kickoff"
    ctx["instantie_meervoud_lower"] = cfg["instantie_meervoud"].lower()

    # Lidwoord van de instantie bepaalt de verbuiging van deze/die/elke/nieuwe/andere/specifieke.
    # "de klant" → deze klant, een nieuwe klant. "het dossier" → dit dossier, een nieuw dossier.
    HET_WOORDEN = {"dossier", "project", "bedrijf", "kind", "gezin", "traject", "programma", "team", "contract", "pand", "gebouw", "merk", "product"}
    enk = cfg["instantie_enkelvoud"].lower()
    lidwoord = (cfg.get("instantie_lidwoord") or ("het" if enk in HET_WOORDEN else "de")).lower()
    het = lidwoord == "het"
    ctx["instantie_lidwoord"] = lidwoord
    ctx["i_deze"] = "dit" if het else "deze"
    ctx["i_Deze"] = "Dit" if het else "Deze"
    ctx["i_die"] = "dat" if het else "die"
    ctx["i_elke"] = "elk" if het else "elke"
    ctx["i_nieuwe"] = "nieuw" if het else "nieuwe"
    ctx["i_Nieuwe"] = "Nieuw" if het else "Nieuwe"
    ctx["i_andere"] = "ander" if het else "andere"
    ctx["i_specifieke"] = "specifiek" if het else "specifieke"

    wd = cfg["werkdomein_eigen"]
    ctx["werkdomein_lower"] = re.sub(r"^eigen\s+", "", wd, flags=re.I).lower() or wd.lower()
    # Lidwoord van het werkdomein: "het bedrijf", "het kantoor", maar "de praktijk", "de studio", "de werking".
    WD_DE = {"praktijk", "studio", "werking", "zaak", "winkel", "onderneming", "organisatie", "school", "vereniging"}
    wd_lid = (cfg.get("werkdomein_lidwoord") or ("de" if ctx["werkdomein_lower"].split()[-1] in WD_DE else "het")).lower()
    ctx["wd_lidwoord"] = wd_lid
    ctx["wd_Lidwoord"] = wd_lid.capitalize()

    onbekend = []

    def kanaal_obj(kid):
        info = kanalen_db.get(kid)
        if info is None:
            onbekend.append(f"kanaal '{kid}'")
            info = {}
        return {
            "id": slugify(kid),
            "label": info.get("label", kid.capitalize()),
            "tip": info.get("tip", "Noteer per voorbeeld het type, de lezer en waarom het werkte."),
            "voorbeeld_prompt": info.get("prompt", f"schrijf een {kid} over X"),
            "content": info.get("content", False),
            "meervoud": info.get("meervoud", ""),
            "enkelvoud": info.get("enkelvoud", f"een {kid}"),
            "vrij_testbaar": info.get("vrij_testbaar", True),
        }

    kanalen_obj = [kanaal_obj(k) for k in cfg["kanalen"]]
    extra_obj = [kanaal_obj(k) for k in cfg.get("kanalen_eigen_extra") or [] if k not in cfg["kanalen"]]
    ctx["kanalen_obj"] = kanalen_obj                  # voor instanties
    ctx["kanalen_obj_eigen"] = kanalen_obj + extra_obj  # voor het eigen werkdomein
    alle = kanalen_obj + extra_obj
    ctx["kanalen_lijst"] = ", ".join(f"`{k['id']}`" for k in alle)
    ctx["content_kalender"] = any(k["content"] for k in alle)
    ctx["heeft_offerte"] = any(k["id"] == "offerte" for k in alle)
    first = alle[0] if alle else {"id": "mail", "label": "Mail", "enkelvoud": "een mail", "meervoud": "mails"}
    second = alle[1] if len(alle) > 1 else first
    ctx["eerste_kanaal_id"] = first["id"]
    ctx["eerste_kanaal_label"] = first["label"]
    ctx["eerste_kanaal_label_lower"] = first["label"].lower()
    ctx["eerste_kanaal_meervoud_lower"] = first.get("meervoud") or (first["label"].lower() + "s")
    ctx["tweede_kanaal_id"] = second["id"]
    ctx["tweede_kanaal_label"] = second["label"]
    ctx["tweede_kanaal_label_lower"] = second["label"].lower()
    # test-kanaal voor Fase B: expliciet uit config, anders het eerste vrij testbare kanaal met content, anders het eerste vrij testbare
    tk = None
    if cfg.get("test_kanaal"):
        tk = next((k for k in alle if k["id"] == slugify(cfg["test_kanaal"])), None)
    if tk is None:
        tk = next((k for k in alle if k["content"] and k["vrij_testbaar"]), None) or next((k for k in alle if k["vrij_testbaar"]), None) or first
    ctx["test_kanaal_id"] = tk["id"]
    ctx["test_kanaal_enkelvoud"] = tk.get("enkelvoud", f"een {tk['id']}")
    ctx["test_kanaal_enkelvoud_cap"] = ctx["test_kanaal_enkelvoud"][:1].upper() + ctx["test_kanaal_enkelvoud"][1:]
    ctx["fase_proces"] = cfg.get("fase_nadruk") == "proces"
    ctx["pijnpunt_1"] = (cfg.get("pijnpunten") or [""])[0]
    # persoon achter de instantie: bij "dossier" is de gesprekspartner een cliënt, bij "opdracht" een opdrachtgever
    PERSOON = {"dossier": "cliënt", "zaak": "cliënt", "opdracht": "opdrachtgever", "project": "opdrachtgever", "traject": "deelnemer", "programma": "deelnemer", "pand": "bouwheer", "gebouw": "bouwheer"}
    persoon = (cfg.get("persoon_achter_instantie") or PERSOON.get(enk, enk)).lower()
    ctx["persoon"] = persoon
    ctx["personen"] = cfg["instantie_meervoud"].lower() if persoon == enk else persoon + ("s" if persoon.endswith(("r", "n")) else "en")
    ctx["persoon_lidwoord"] = "de"
    ctx["instantie_slug"] = slugify(enk)
    # materiaal: enkel URLs als URL tonen
    mat = dict(cfg.get("materiaal") or {})
    for key in ("website", "linkedin"):
        v = str(mat.get(key) or "")
        mat[key + "_url"] = v if ("http" in v or "." in v.split()[0] if v else False) else ""
    ctx["materiaal"] = mat

    def recurring_objs(names):
        objs = []
        for r in names:
            info = recurring_db.get(r)
            if info is None:
                onbekend.append(f"recurring-map '{r}'")
                info = {}
            objs.append({
                "id": slugify(r),
                "label": info.get("label", r.capitalize()),
                "beschrijving": info.get("beschrijving", f"terugkerend werk van het type '{r}'"),
            })
        return objs

    ctx["recurring_obj"] = recurring_objs(cfg["recurring_mappen"])
    ctx["recurring_obj_eigen"] = recurring_objs(cfg["recurring_mappen_eigen"] or cfg["recurring_mappen"])
    ctx["frameworks_start"] = [{"titel": f, "slug": slugify(f)} for f in cfg["frameworks_start"]]

    # modus bestaande map: de mappen die er al zijn, met wat Claude ermee mag
    ACTIE = {
        "instanties": f"Eén submap per {enk}. Lees de map van {ctx['i_die']} {enk} wanneer je voor hen werkt."
                      + (f" Afspraken en context staan in `{ctx['instantie_map']}/[naam]/`." if cfg["multi_instance"] else ""),
        "werk": "Terugkerend werk. Recente files zijn het voorbeeld voor vorm en opbouw.",
        "referentie": "Templates en referentiedocumenten. Vertrekpunt voor nieuw werk, het origineel blijft onaangeroerd.",
        "archief": f"Oud werk. Enkel openen wanneer {cfg['naam']} erom vraagt.",
        "buiten_bereik": "Nooit openen, ook niet om iets te zoeken.",
        "overig": "Openen wanneer de taak erom vraagt.",
    }
    bm = []
    for m in cfg.get("bestaande_mappen") or []:
        rol = (m.get("rol") or "overig").strip()
        if rol not in ROLLEN:
            onbekend.append(f"rol '{rol}' bij bestaande map '{m.get('pad')}'")
            rol = "overig"
        pad = str(m.get("pad", "")).replace("\\", "/").strip("/")
        wat = re.sub(r"\s*\[vul aan\]\s*", " ", str(m.get("wat") or "")).strip()
        if not wat or re.fullmatch(r"\(.*\)", wat):
            wat = "[wat hier staat, bevestigen in Fase 0]"
        bm.append({"pad": pad, "rol": rol, "wat": wat, "actie": m.get("actie") or ACTIE[rol]})
    ctx["bestaande_mappen_obj"] = bm
    ctx["heeft_bestaande_mappen"] = bool(bm)
    ctx["buiten_bereik_obj"] = [m for m in bm if m["rol"] == "buiten_bereik"]
    ctx["referentie_obj"] = [m for m in bm if m["rol"] == "referentie"]
    inst = [m for m in bm if m["rol"] == "instanties"]
    ctx["instanties_pad"] = inst[0]["pad"] if inst else ""
    ctx["instantie_map_bestaand"] = f"{inst[0]['pad']}/" if inst else ""
    # bij overlay krijgt de contextmap dezelfde naam als de bestaande klantmap, zodat de twee bij elkaar te vinden zijn
    ctx["instanties_start_obj"] = [{"naam": n, "slug": re.sub(r'[<>:"/\\|?*]', "-", n).strip(" .")}
                                   for n in (cfg.get("instanties_start") or [])]
    if ov and cfg.get("instanties_start") and not cfg["multi_instance"]:
        onbekend.append("instanties_start zonder multi_instance (genegeerd)")
    ctx["_onbekend"] = sorted(set(onbekend))
    return ctx


# ---------------------------------------------------------------- builder

class Builder:
    def __init__(self, ctx, out, dry=False):
        self.ctx = ctx
        self.out = Path(out)
        self.dry = dry
        self.written = []

    def _tpl(self, rel):
        return (SKELET / rel).read_text(encoding="utf-8")

    def write(self, rel_out, tpl_rel, extra=None):
        ctx = dict(self.ctx)
        if extra:
            ctx.update(extra)
        text = tidy(render(self._tpl(tpl_rel), ctx))
        self._put(rel_out, text)

    def _put(self, rel_out, text):
        dest = self.out / rel_out
        self.written.append(rel_out)
        if self.dry:
            return
        if self.ctx.get("overlay") and dest.exists():
            raise FileExistsError(f"{rel_out} bestaat al. In de modus bestaande map wordt nooit iets overschreven.")
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(text, encoding="utf-8")

    def mkdir(self, rel):
        self.written.append(rel.rstrip("/") + "/")
        if not self.dry:
            (self.out / rel).mkdir(parents=True, exist_ok=True)

    # --- lagen

    def root(self):
        for f in ("CLAUDE.md", "SETUP-START-HIER.md", "SETUP-STATUS.md"):
            self.write(f, f"root/{f}")
        if self.ctx["overlay"]:
            self.write("LEESMIJ-ASSISTENT.md", "root/LEESMIJ-ASSISTENT.md")
        else:
            self.write("LEESMIJ.md", "root/LEESMIJ.md")

    def kern(self):
        for f in ("wie-ik-ben.md", "werkregels.md", "anti-ai-stijl.md"):
            self.write(f"_kern/{f}", f"_kern/{f}")
        # de basisregels tegen AI-stijl: letterlijk overgenomen, geen template
        self._put("_kern/schrijfregels-basis.md", self._tpl("_kern/schrijfregels-basis.md"))
        if self.ctx["vertrouwelijkheid"]:
            self.write("_kern/vertrouwelijkheid.md", "_kern/vertrouwelijkheid.md")

    def kennis(self):
        self.write("_kennis/frameworks/LEESMIJ.md", "_kennis/frameworks/LEESMIJ.md")
        for fw in self.ctx["frameworks_start"]:
            self._framework_stub(fw)
        self.write("_kennis/templates/voice-analyse-protocol.md", "_kennis/templates/voice-analyse-protocol.md")
        if self.ctx["multi_instance"]:
            self.write(f"_kennis/templates/intake-vragenlijst-{self.ctx['instantie_slug']}.md",
                       "_kennis/templates/intake-vragenlijst.md")
        if self.ctx["content_kalender"]:
            self.write("_kennis/templates/content-kalender-template.md", "_kennis/templates/content-kalender-template.md")
        if self.ctx["overlay"]:
            self.write("_kennis/referentiedocumenten.md", "_kennis/referentiedocumenten.md")

    def _framework_stub(self, fw):
        text = (f"# {fw['titel']}\n\n## Wat is het\n\n[Vul aan]\n\n## Wanneer gebruik ik het\n\n[Vul aan]\n\n"
                f"## De stappen\n\n1. [Vul aan]\n\n## Voorbeelden\n\n[Vul aan]\n\n## Bronnen\n\n[Vul aan]\n\n"
                f"---\n\n*Stub aangemaakt op {self.ctx['aangemaakt_op']} op basis van de kickoff. Vul aan tijdens Fase B.*\n")
        self._put(f"_kennis/frameworks/{fw['slug']}.md", text)

    def inbox(self):
        self.write(f"{self.ctx['inbox_map']}/LEESMIJ.md", "inbox/LEESMIJ.md")

    def werkdomein(self, base, wd_naam, is_eigen, werkmap=""):
        ov = self.ctx["overlay"]
        heeft_voice = is_eigen or self.ctx["volledig"]
        heeft_voorbeelden = is_eigen or self.ctx["volledig"]
        # bij overlay staan het terugkerende werk en de projecten in de bestaande mappen of in _projecten/
        heeft_projecten = (not ov) and (is_eigen or self.ctx["projecten_per_instantie"])
        recurring = [] if ov else (self.ctx["recurring_obj_eigen"] if is_eigen else self.ctx["recurring_obj"])
        kanalen = self.ctx["kanalen_obj_eigen"] if is_eigen else self.ctx["kanalen_obj"]
        extra = {"wd_naam": wd_naam, "wd_pad": base, "is_eigen": is_eigen, "recurring_obj": recurring,
                 "heeft_projecten": heeft_projecten, "heeft_voice": heeft_voice, "kanalen_obj": kanalen,
                 "werkmap": werkmap}

        self.write(f"{base}/_context.md", "werkdomein/_context.md", extra)
        if heeft_voice:
            self.write(f"{base}/_voice.md", "werkdomein/_voice.md", extra)
        self.write(f"{base}/_strategie.md", "werkdomein/_strategie.md", extra)
        if self.ctx["content_kalender"] and (is_eigen or self.ctx["volledig"]):
            self.write(f"{base}/content-kalender.md", "werkdomein/content-kalender.md", extra)
        if heeft_voorbeelden:
            self.write(f"{base}/_voorbeelden/LEESMIJ.md", "werkdomein/_voorbeelden/LEESMIJ.md", extra)
            for k in kanalen:
                self.write(f"{base}/_voorbeelden/{k['id']}/LEESMIJ.md", "werkdomein/_voorbeelden/_kanaal/LEESMIJ.md",
                           {**extra, **k})
        for r in recurring:
            self.write(f"{base}/{r['id']}/LEESMIJ.md", "werkdomein/_recurring/LEESMIJ.md", {**extra, **r})
        if heeft_projecten:
            self.write(f"{base}/projecten/LEESMIJ.md", "werkdomein/projecten/LEESMIJ.md", extra)

    def eigen(self):
        self.werkdomein(self.ctx["eigen_map"], self.ctx["werkdomein_eigen"], True)

    def instanties(self):
        if not self.ctx["multi_instance"]:
            return
        base = self.ctx["instantie_map"]
        self.write(f"{base}/LEESMIJ.md", "instanties/LEESMIJ.md")
        tpl = f"{base}/_template-{self.ctx['i_nieuwe']}-{self.ctx['instantie_slug']}"
        ip = self.ctx["instanties_pad"]
        self.werkdomein(tpl, f"[naam {self.ctx['instantie_enkelvoud']}]", False,
                        f"{ip}/[naam]" if ip else "")
        if self.ctx["overlay"]:
            for inst in self.ctx["instanties_start_obj"]:
                self.werkdomein(f"{base}/{inst['slug']}", inst["naam"], False,
                                f"{ip}/{inst['naam']}" if ip else "")

    def projecten(self):
        pm = self.ctx["projecten_map"]
        self.write(f"{pm}/LEESMIJ.md", "projecten/LEESMIJ.md")
        self.write(f"{pm}/_template/project.md", "projecten/_template/project.md")

    def archief(self):
        if self.ctx["overlay"]:
            return  # de klant heeft haar eigen archief; de AI-laag voegt er geen toe
        self.write("_archief/LEESMIJ.md", "archief/LEESMIJ.md")

    def context_leesmij(self):
        if self.ctx["overlay"]:
            self.write("_context/LEESMIJ.md", "context/LEESMIJ.md")

    def ai_setup(self):
        self.write("_ai-setup/LEESMIJ.md", "ai-setup/LEESMIJ.md")

    def build(self):
        self.root(); self.kern(); self.kennis(); self.inbox(); self.context_leesmij(); self.ai_setup()
        self.eigen(); self.instanties(); self.projecten(); self.archief()
        return self.written


# ---------------------------------------------------------------- check

def laag_paden(root):
    """Bij overlay: enkel de paden van de AI-laag, nooit de mappen van de klant."""
    return [root / n for n in LAAG_NAMEN if (root / n).exists()]


def check(path):
    root = Path(path)
    problems = []
    overlay = (root / "LEESMIJ-ASSISTENT.md").exists()
    if overlay:
        scope = laag_paden(root)
        md_files = [p for s_ in scope for p in ([s_] if s_.is_file() else s_.rglob("*.md")) if p.suffix == ".md"]
        dirs = [d for s_ in scope if s_.is_dir() for d in [s_, *s_.rglob("*")] if d.is_dir()]
        verplicht = ("CLAUDE.md", "LEESMIJ-ASSISTENT.md", "SETUP-START-HIER.md", "SETUP-STATUS.md")
    else:
        md_files = list(root.rglob("*.md"))
        dirs = [d for d in root.rglob("*") if d.is_dir()]
        verplicht = ("CLAUDE.md", "LEESMIJ.md", "SETUP-START-HIER.md", "SETUP-STATUS.md")
    for f in md_files:
        txt = f.read_text(encoding="utf-8", errors="ignore")
        if "{{" in txt or "}}" in txt:
            for n, line in enumerate(txt.splitlines(), 1):
                if "{{" in line or "}}" in line:
                    problems.append(f"placeholder-rest  {f.relative_to(root)}:{n}: {line.strip()[:80]}")
    for d in dirs:
        if not any(d.iterdir()):
            problems.append(f"lege map          {d.relative_to(root)}/")
    for name in verplicht:
        if not (root / name).exists():
            problems.append(f"ontbreekt         {name}")
    kern = root / "_kern"
    if (kern / "_voice.md").exists():
        problems.append("fout              _kern/_voice.md bestaat: voice hoort niet in _kern")
    return problems


def snapshot(root):
    """Grootte en wijzigingstijd van elk bestaand bestand, om achteraf te bewijzen dat niets veranderde."""
    snap = {}
    for dirpath, dirnames, filenames in os.walk(root, followlinks=False):
        for f in filenames:
            p = os.path.join(dirpath, f)
            try:
                st = os.stat(p, follow_symlinks=False)
                snap[os.path.relpath(p, root)] = (st.st_size, st.st_mtime_ns)
            except OSError:
                pass
    return snap


def conflicten(out, bestaande_json):
    namen = {n.lower(): n for n in LAAG_NAMEN}
    gevonden = []
    if out.exists():
        for e in out.iterdir():
            if e.name.lower() in namen:
                gevonden.append(f"{e.name} (staat al in de doelmap)")
    if bestaande_json:
        data = json.loads(Path(bestaande_json).read_text(encoding="utf-8"))
        top = list(data.get("topmappen") or []) + list(data.get("losse_root") or [])
        for n in top:
            if n.lower() in namen:
                gevonden.append(f"{n} (staat al in de hoofdmap van de klant, volgens de scan)")
    return gevonden


def print_tree(paths):
    tree = {}
    for p in sorted(paths):
        node = tree
        for part in p.rstrip("/").split("/"):
            node = node.setdefault(part, {})
    def walk(node, prefix=""):
        items = sorted(node.items(), key=lambda kv: (not kv[1], kv[0]))
        for i, (name, child) in enumerate(items):
            last = i == len(items) - 1
            print(prefix + ("└── " if last else "├── ") + name + ("/" if child else ""))
            if child:
                walk(child, prefix + ("    " if last else "│   "))
    walk(tree)


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--config", help="pad naar config.json")
    ap.add_argument("--out", help="doelmap, bv. '.../Kiara Cowork'")
    ap.add_argument("--force", action="store_true", help="bestaande niet-lege doelmap toch gebruiken")
    ap.add_argument("--dry-run", action="store_true", help="toon enkel wat er gebouwd zou worden")
    ap.add_argument("--check", metavar="PAD", help="controleer een gebouwde omgeving op placeholder-resten en lege mappen")
    ap.add_argument("--bestaande", metavar="SCAN_JSON", help="overlay: JSON van scan_structuur.py, voor de conflictcheck met de hoofdmap van de klant")
    ap.add_argument("--bewaar", nargs="*", default=[], metavar="FILE",
                    help="extra werkbestanden (mappenkaart, scan) die na het bouwen in _ai-setup/ komen")
    a = ap.parse_args()

    if a.check:
        probs = check(a.check)
        if probs:
            print(f"{len(probs)} probleem/problemen gevonden in {a.check}:")
            for p in probs:
                print("  " + p)
            sys.exit(1)
        print(f"OK: geen placeholder-resten, geen lege mappen, kernfiles aanwezig in {a.check}")
        return

    if not a.config:
        ap.error("--config is verplicht (behalve bij --check)")
    cfg = load_config(a.config)
    ctx = derive(cfg)

    if a.dry_run:
        b = Builder(ctx, a.out or f"<doelmap>/{cfg['naam']} {'AI-laag' if ctx['overlay'] else 'Cowork'}", dry=True)
        paths = b.build()
        print(f"Zou {len([p for p in paths if not p.endswith('/')])} files schrijven naar {b.out}:\n")
        print_tree(paths)
        if ctx["_onbekend"]:
            print("\nNiet in assets/*.json (krijgen een generieke tekst, nalezen in de customisatie-pass): " + ", ".join(ctx["_onbekend"]))
        return

    if not a.out:
        ap.error("--out is verplicht")
    out = Path(a.out)

    if ctx["overlay"]:
        bouw_overlay(ctx, out, a)
        return

    if out.exists() and any(out.iterdir()) and not a.force:
        print(f"Doelmap {out} bestaat en is niet leeg. Gebruik --force om toch te schrijven.", file=sys.stderr)
        sys.exit(2)
    out.mkdir(parents=True, exist_ok=True)

    b = Builder(ctx, out)
    paths = b.build()
    bewaar_setup(out, a)
    files = [p for p in paths if not p.endswith("/")]
    print(f"{len(files)} files geschreven naar {out}\n")
    print_tree(paths)

    if ctx["_onbekend"]:
        print("\nNiet in assets/*.json (generieke tekst, nalezen in de customisatie-pass): " + ", ".join(ctx["_onbekend"]))
    probs = check(out)
    if probs:
        print(f"\nLet op, {len(probs)} controlepunt(en):")
        for p in probs:
            print("  " + p)
        sys.exit(1)
    print("\nControle OK: geen placeholder-resten, geen lege mappen.")


def bewaar_setup(out, a):
    """Config en werkbestanden van de setup in _ai-setup/, zodat de laag later opnieuw te bouwen is."""
    doel = out / "_ai-setup"
    doel.mkdir(parents=True, exist_ok=True)
    for bron, naam in [(a.config, "config.json")] + [(f, Path(f).name) for f in (a.bewaar or [])]:
        src = Path(bron)
        if not src.is_file():
            print(f"Let op: {bron} niet gevonden, niet bewaard in _ai-setup/.")
            continue
        dst = doel / naam
        if dst.exists():
            print(f"Let op: _ai-setup/{naam} bestaat al, niet overschreven.")
            continue
        dst.write_bytes(src.read_bytes())


def bouw_overlay(ctx, out, a):
    if a.force:
        print("--force bestaat niet in de modus bestaande map. Er wordt nooit iets overschreven.", file=sys.stderr)
        sys.exit(2)
    conf = conflicten(out, a.bestaande)
    if conf:
        print("Gestopt: de AI-laag botst met namen die al bestaan. Niets geschreven.", file=sys.stderr)
        for c in conf:
            print("  " + c, file=sys.stderr)
        print("Kies samen met Michiel een oplossing. De mappen van de klant blijven zoals ze zijn.", file=sys.stderr)
        sys.exit(2)
    if ctx["multi_instance"] and not ctx["instanties_pad"]:
        print("Let op: multi_instance staat aan, maar geen enkele bestaande map heeft rol 'instanties'. "
              "De routing naar klantmappen blijft dan algemeen.")
    out.mkdir(parents=True, exist_ok=True)
    voor = snapshot(out)
    b = Builder(ctx, out)
    try:
        paths = b.build()
    except FileExistsError as e:
        print(f"Gestopt: {e}", file=sys.stderr)
        sys.exit(2)
    bewaar_setup(out, a)
    na = snapshot(out)
    gewijzigd = [p for p, v in voor.items() if na.get(p) != v]
    files = [p for p in paths if not p.endswith("/")]
    print(f"AI-laag: {len(files)} nieuwe files geschreven naar {out}\n")
    print_tree(paths)
    print(f"\nBestaande bestanden in de doelmap: {len(voor)} voor, {len(gewijzigd)} gewijzigd.")
    if gewijzigd:
        print("FOUT: deze bestaande bestanden zijn veranderd:")
        for p in gewijzigd:
            print("  " + p)
        sys.exit(3)
    if ctx["_onbekend"]:
        print("\nNakijken in de customisatie-pass: " + ", ".join(ctx["_onbekend"]))
    probs = check(out)
    if probs:
        print(f"\nLet op, {len(probs)} controlepunt(en):")
        for p in probs:
            print("  " + p)
        sys.exit(1)
    print("\nControle OK: geen placeholder-resten, geen lege mappen in de AI-laag.")


if __name__ == "__main__":
    main()
