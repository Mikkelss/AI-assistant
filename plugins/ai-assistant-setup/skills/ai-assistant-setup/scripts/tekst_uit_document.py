#!/usr/bin/env python3
"""
tekst_uit_document.py: haalt de leesbare tekst uit een document, zonder extra packages.

Bedoeld voor de documentlezers in de live-modus: zo kan een lezer een Word-,
PDF- of mailbestand lezen zonder dat er iets geïnstalleerd moet worden.
Het script opent het bestand enkel om te lezen en schrijft nooit iets weg.

Gebruik:
    python3 tekst_uit_document.py "pad/naar/bestand.docx"
    python3 tekst_uit_document.py --max 8000 "a.docx" "b.pdf"

Ondersteund: .docx .docm .dotx .odt .pptx .pdf .txt .md .csv .eml .html .htm .rtf
PDF gaat via pdftotext of pypdf als die er zijn, en anders meldt het script dat
de lezer de PDF met de Read-tool moet openen.
"""

import argparse
import email
import html
import re
import shutil
import subprocess
import sys
import zipfile
from email import policy
from pathlib import Path

MAX_DEFAULT = 12000
PDF_PAGINAS = 5


def _xml_tekst(xml, para_tag, tekst_tag):
    xml = re.sub(rf"</{para_tag}>", "\n", xml)
    xml = re.sub(r"<w:tab/>|<w:tab [^>]*/>", "\t", xml)
    xml = re.sub(r"<w:br/>|<w:br [^>]*/>|<text:line-break/>", "\n", xml)
    delen = re.findall(rf"<{tekst_tag}(?: [^>]*)?>([^<]*)</{tekst_tag}>|(\n|\t)", xml)
    return html.unescape("".join(a or b for a, b in delen))


def docx(pad):
    with zipfile.ZipFile(pad) as z:
        namen = ["word/document.xml"] + sorted(n for n in z.namelist() if re.match(r"word/(header|footer)\d*\.xml", n))
        stukken = [_xml_tekst(z.read(n).decode("utf-8", "ignore"), "w:p", "w:t") for n in namen if n in z.namelist()]
    return "\n".join(stukken)


def odt(pad):
    with zipfile.ZipFile(pad) as z:
        xml = z.read("content.xml").decode("utf-8", "ignore")
    xml = re.sub(r"</text:(p|h)>", "\n", xml)
    return html.unescape(re.sub(r"<[^>]+>", "", xml))


def pptx(pad):
    with zipfile.ZipFile(pad) as z:
        slides = sorted((n for n in z.namelist() if re.match(r"ppt/slides/slide\d+\.xml", n)),
                        key=lambda n: int(re.findall(r"\d+", n)[-1]))
        uit = []
        for i, n in enumerate(slides, 1):
            uit.append(f"--- slide {i} ---\n" + _xml_tekst(z.read(n).decode("utf-8", "ignore"), "a:p", "a:t"))
    return "\n".join(uit)


def pdf(pad):
    if shutil.which("pdftotext"):
        r = subprocess.run(["pdftotext", "-l", str(PDF_PAGINAS), "-layout", str(pad), "-"],
                           capture_output=True, text=True, timeout=60)
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
    try:
        from pypdf import PdfReader  # noqa
        lezer = PdfReader(str(pad))
        return "\n".join((p.extract_text() or "") for p in lezer.pages[:PDF_PAGINAS])
    except Exception:
        pass
    return (f"[Geen tekst uit deze PDF gehaald. Open ze met de Read-tool, enkel de eerste {PDF_PAGINAS} pagina's. "
            "Is het een scan zonder tekstlaag, sla ze dan over en meld dat.]")


def tekstbestand(pad):
    data = pad.read_bytes()
    for enc in ("utf-8", "cp1252", "latin-1"):
        try:
            return data.decode(enc)
        except UnicodeDecodeError:
            continue
    return data.decode("utf-8", "ignore")


def eml(pad):
    bericht = email.message_from_bytes(pad.read_bytes(), policy=policy.default)
    kop = f"Van: {bericht.get('From', '')}\nAan: {bericht.get('To', '')}\nOnderwerp: {bericht.get('Subject', '')}\n\n"
    deel = bericht.get_body(preferencelist=("plain", "html"))
    inhoud = deel.get_content() if deel else ""
    if deel is not None and deel.get_content_type() == "text/html":
        inhoud = html_naar_tekst(inhoud)
    return kop + inhoud


def html_naar_tekst(t):
    t = re.sub(r"(?is)<(script|style).*?</\1>", "", t)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</div>|</li>|</h\d>", "\n", t)
    return html.unescape(re.sub(r"<[^>]+>", "", t))


def rtf(pad):
    t = tekstbestand(pad)
    t = re.sub(r"\\par[d]?", "\n", t)
    t = re.sub(r"\\'([0-9a-f]{2})", lambda m: bytes.fromhex(m.group(1)).decode("cp1252", "ignore"), t)
    t = re.sub(r"\\[a-z]+-?\d* ?|[{}]", "", t)
    return t


LEZERS = {
    ".docx": docx, ".docm": docx, ".dotx": docx, ".odt": odt, ".pptx": pptx, ".pdf": pdf,
    ".txt": tekstbestand, ".md": tekstbestand, ".csv": tekstbestand,
    ".eml": eml, ".html": lambda p: html_naar_tekst(tekstbestand(p)), ".htm": lambda p: html_naar_tekst(tekstbestand(p)),
    ".rtf": rtf,
}


def lees(pad, maximum):
    pad = Path(pad)
    lezer = LEZERS.get(pad.suffix.lower())
    if not lezer:
        return f"[Formaat {pad.suffix or '(geen extensie)'} wordt niet gelezen. Sla dit bestand over.]"
    try:
        tekst = lezer(pad)
    except Exception as e:  # beschadigd of beveiligd bestand
        return f"[Kon dit bestand niet lezen ({type(e).__name__}). Sla het over en meld het.]"
    tekst = re.sub(r"[ \t]+\n", "\n", tekst)
    tekst = re.sub(r"\n{3,}", "\n\n", tekst).strip()
    if len(tekst) > maximum:
        tekst = tekst[:maximum] + f"\n\n[... ingekort: {len(tekst) - maximum} tekens niet getoond]"
    return tekst or "[Leeg document]"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("bestanden", nargs="+")
    ap.add_argument("--max", type=int, default=MAX_DEFAULT, help=f"maximum aantal tekens per bestand (default {MAX_DEFAULT})")
    a = ap.parse_args()
    for i, b in enumerate(a.bestanden):
        if len(a.bestanden) > 1:
            print(("\n" if i else "") + f"===== {b} =====")
        print(lees(b, a.max))


if __name__ == "__main__":
    sys.exit(main())
