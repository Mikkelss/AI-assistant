# Modus bestaande map

Voor een klant die al een werkbare mappenstructuur heeft. De skill bouwt dan geen nieuwe omgeving. Hij legt een AI-laag naast de mappen die er al zijn, leest een selectie van haar documenten en zet de basis van de assistent goed. De klant werkt verder in haar eigen structuur.

De skill draait altijd bij de klant: in haar Cowork, op haar computer, met haar account. Michiel zit erbij. Haar mappen komen nooit op de computer van Michiel.

Gedestilleerd uit de opstart met An (Anders Office, september en oktober 2026).

---

## Wanneer deze modus

Beslisvraag vóór stap 1 van de skill: **heeft de klant al een bruikbare mappenstructuur?**

- Ja: het werk staat geordend (per klant, dossier, werf of type) en de klant vindt er zelf vlot haar weg in. → Deze modus.
- Nee: weinig mappen, alles op één hoop, of de klant wil haar structuur zelf herdenken. → De gewone modus met kickoff-vragenlijst.
- Twijfel: draai eerst de scan (stap B) en beslis samen met Michiel.

---

## De harde regel

Aan de bestaande mappen verandert niets. Niet bij het bouwen, niet tijdens het lezen, niet tijdens de setup, en daarna ook niet tot de klant en Michiel uitdrukkelijk iets anders beslissen.

Wat dat concreet betekent:

- De scan en het leesplan lezen enkel namen, groottes en datums. De documentlezers openen bestanden enkel om te lezen.
- De AI-laag bestaat uit exact deze namen in de hoofdmap: `CLAUDE.md`, `LEESMIJ-ASSISTENT.md`, `SETUP-START-HIER.md`, `SETUP-STATUS.md`, `_kern/`, `_kennis/`, `_context/`, `_inbox/`, `_projecten/`, `_ai-setup/`. Er komt niets bij in een bestaande map.
- Het script stopt als één van die namen al bestaat. In deze modus bestaat `--force` niet.
- Na het bouwen vergelijkt het script elk bestaand bestand (grootte en wijzigingstijd) met de toestand ervoor. Eén verschil en het script meldt een fout.
- In de `CLAUDE.md` van de klant staan de bestaande mappen op alleen-lezen (`bestaande_schrijven: false`). Nieuwe output komt in `_projecten/`, de klant zet het zelf op zijn plek.
- Tijdelijke bestanden (scan, config vóór het bouwen) komen in een werkmap buiten de map van de klant, nooit in haar map. Na het bouwen bewaart het script ze in `_ai-setup/`.

---

## Stap A: vertrekpunt in de sessie

Samen met de klant, vóór de skill start:

1. Een **kopie** van haar mappen maken. De assistent werkt in de kopie, de originelen blijven onaangeroerd.
2. Gevoelige mappen uit de kopie halen: personeel, lonen, medische gegevens, wachtwoorden, en alles waarvan de klant zegt dat het niet bij Claude hoort.
3. De kopie koppelen als map in Cowork.

Daarna typt Michiel **INIT**. Dat start deze skill. Controleer eerst dat er een map gekoppeld is en dat het de kopie is. Twijfel je, vraag het.

**Werkmap voor tijdelijke bestanden.** Gebruik een map buiten de kopie, bijvoorbeeld de scratch- of outputmap van Cowork, of `/tmp/ai-setup`. Noem ze hieronder `<werk>`.

---

## Stap B: de scan

```
python3 <skill-map>/scripts/scan_structuur.py --bron "<hoofdmap>" --rapport <werk>/mappenkaart.md --json <werk>/scan.json
```

Het rapport toont:

- **Boom** tot 3 niveaus, met aantal files en laatste wijziging per map. Klantmappen worden ingekort.
- **Kandidaten voor de klantenlaag**: een map met veel submappen die intern dezelfde opbouw delen. De gedeelde submappen (bijvoorbeeld `werfverslagen` in 89% van de klantmappen) zijn kandidaten voor kanalen en werkregels.
- **Signalen uit namen**: gevoelig (personeel, loon, medisch), referentie (templates, sjablonen, huisstijl), archief, dropzone, mappen per jaar, versienamen (v2, final, kopie).
- **Naamconflicten** met de AI-laag.
- **Een voorstel voor `bestaande_mappen`** om in de config te zetten.

De scan raadt. Wat hij voorstelt, bevestigen de klant en Michiel in stap D.

---

## Stap C: de config

Zelfde config als in de gewone modus, met `"overlay": true` en deze extra velden. Schrijf ze naar `<werk>/config.json`.

| Veld | Wat | Waar het vandaan komt |
|---|---|---|
| `overlay` | `true` | Beslisvraag hierboven |
| `bestaande_root` | Naam of pad van de hoofdmap, enkel ter info in `CLAUDE.md` | De gekoppelde map |
| `bestaande_mappen` | Lijst van `{"pad", "rol", "wat"}`, optioneel `"actie"` om de standaardtekst te vervangen | Voorstel uit de scan, `wat` zelf aanvullen, rollen nakijken |
| `bestaande_schrijven` | `false` bij de start. Enkel `true` als de klant en Michiel dat uitdrukkelijk willen | Default |
| `instanties_start` | Namen van 0 tot 2 klantmappen die meteen een contextmap krijgen, met exact dezelfde naam als bij de klant | Klant met het meeste recente werk, of leeg laten en in Fase 0 kiezen |

Rollen: `instanties` (één submap per klant of dossier), `werk` (terugkerend werk), `referentie` (templates, voorbeelden, huisstijl), `archief` (enkel op vraag), `buiten_bereik` (nooit openen), `overig`.

De rest van de config leid je zo af:

| Config | Bron in deze modus |
|---|---|
| `multi_instance`, `instantie_meervoud`, `instantie_enkelvoud` | De kandidaat voor de klantenlaag. Neem het woord van de klant (`Klanten`, `Werven`, `Dossiers`) |
| `kanalen` | Gedeelde submappen en bestandstypes. `werfverslagen` wordt kanaal `werfverslag`. Nieuw kanaal? Voeg het toe aan `assets/kanalen.json` |
| `vertrouwelijkheid` | Gevoelige namen in de scan en de sector |
| `instantie_template` | Sectorvariant. Schrijft de klant altijd in eigen naam, dan `licht` |
| `pijnpunten`, `sector` | Wat Michiel vertelt en wat de klant in de sessie zegt |
| `prefill` | Leeg bij het bouwen. Feiten komen pas na het lezen (stap F) en na bevestiging |
| `coach_voornaam` | `Michiel` |
| `rol_label`, `werkdomein`, `sector` | Wat de klant en Michiel in de sessie zeggen, en wat de mappen tonen. Neem nooit waarden over uit `assets/config.example.json`: dat is de config van een andere klant |
| Al de rest | Default uit `beslisboom.md`, genoteerd als open punt |

**Geen kickoff-vragenlijst.** Wat in de documenten staat, halen de documentlezers eruit. Wat enkel de klant weet, komt in Fase 0 van de setup.

---

## Stap D: het voorstel, samen bekijken

Toon de klant en Michiel in de chat, kort en in gewone taal:

- **De mappenkaart**: de boom uit de scan, ingekort tot wat de keuzes uitlegt.
- **De tabel bestaande mappen**: map, wat erin zit, rol, wat Claude ermee mag. Gevoelige mappen apart benoemd.
- **Wat de AI-laag toevoegt**: de lijst namen hierboven, plus het resultaat van de conflictcheck.
- **Alleen-lezen**: waarom de mappen van de klant op alleen-lezen staan, en wat ze daardoor zelf doet (output uit `_projecten/` op zijn plek zetten).

Vraag akkoord of bijsturing. Pas de config aan tot ze klopt. Bouw niets voor het akkoord er is.

Is er een naamconflict (de klant heeft al een `_kern` of een `CLAUDE.md`), dan los je dat op in het voorstel. Haar map hernoemen is geen optie: stop en bespreek het met Michiel.

---

## Stap E: bouwen in de hoofdmap

```
python3 <skill-map>/scripts/build_skeleton.py --config <werk>/config.json --dry-run
python3 <skill-map>/scripts/build_skeleton.py --config <werk>/config.json --out "<hoofdmap>" --bestaande <werk>/scan.json --bewaar <werk>/mappenkaart.md <werk>/scan.json
```

De laag komt rechtstreeks in de hoofdmap van de kopie. Het script stopt bij elk conflict, schrijft nooit over een bestaand pad, en controleert achteraf dat geen enkel bestaand bestand veranderde. Meldt het een conflict of een gewijzigd bestand: stop, toon de melding en leg het aan Michiel voor.

Config, mappenkaart en scan staan daarna in `_ai-setup/`.

---

## Stap F: documenten lezen

Dit is wat de setup snel en concreet maakt: de basis komt uit wat de klant echt schrijft. Er is geen aparte toestemming nodig, want de klant koppelde de kopie zelf in Cowork. Meld wel kort welke documenten je gaat lezen.

**1. Leesplan maken.**

```
python3 <skill-map>/scripts/kies_documenten.py --map "<hoofdmap>" --config "<hoofdmap>/_ai-setup/config.json" --json "<hoofdmap>/_ai-setup/leesplan.json" --md "<hoofdmap>/_ai-setup/leesplan.md"
```

Het script kiest per map de 3 nieuwste tekstdocumenten, de klantmappen met het meest recente werk, en materiaal over het bedrijf (masterprompt, AI-clone, voorstelling). Archief en alles buiten bereik slaat het over, net als bestanden groter dan 10 MB. Maximaal 20 documenten, verdeeld over pakketten van hoogstens 6. Toon de klant het leesplan in een paar regels.

**2. De lezers starten, allemaal tegelijk.** Start per pakket één documentlezer, alle pakketten in hetzelfde bericht zodat ze parallel lopen. Geef elke lezer:

- de hoofdmap
- de id, titel en vraag van het pakket, en de paden uit `leesplan.json`
- het volledige pad naar `<skill-map>/scripts/tekst_uit_document.py`

Welke lezer:

- Is de agent `documentlezer` beschikbaar (de plugin levert hem mee, soms als `ai-assistant-setup:documentlezer`), gebruik die.
- Anders: start een gewone subagent en geef hem de volledige tekst van `references/documentlezer.md` mee als instructie, gevolgd door het pakket.
- Kunnen er geen subagents gestart worden: lees de pakketten zelf, één na één, volgens dezelfde instructie.

**3. Samenleggen.** Wanneer alle lezers klaar zijn:

- Voeg dezelfde regels en feiten samen. Een regel die in 2 pakketten terugkomt, krijgt "zeker: hoog".
- Leg tegenspraak tussen lezers bloot als vraag aan de klant. Kies nooit zelf.
- Schrap wat over de klant als persoon gaat (karakter, principes, waarom ze doet wat ze doet). Dat vult ze zelf in, in Fase A.
- Schrijf alles naar `_ai-setup/analyse.md`, in exact deze vorm:

```
# Wat Claude in je documenten vond

Gelezen op [YYYY-MM-DD]: [aantal] documenten, zie `_ai-setup/leesplan.md`.

## Beste voorbeeld per taak
- [taak]: `[pad]`, [waarom] | bron: [pad] | status: open

## Werkregels
- [regel] | bron: [pad], [pad] | zeker: hoog | status: open

## Feiten over het bedrijf
- [feit] | bron: [pad] | status: open

## Vragen
- [vraag] | bron: [pad], [pad] | status: open
```

Elke regel eindigt op `| status: open`. Na de bespreking in `SETUP` wordt dat `bevestigd`, `aangepast`, `geschrapt` of, bij een vraag, `beantwoord`. Zo ziet `waar_staan_we.py` hoeveel er nog open staat.

**4. Niet zelf wegschrijven.** In INIT komt niets van de bevindingen in `_kern/` of `_kennis/`. De setup-gids legt ze in Fase 0 voor aan de klant en schrijft ze weg na haar akkoord. Zo blijft `SETUP` volledig zonder deze skill te gebruiken.

**Tijd en verbruik.** Met 4 lezers tegelijk duurt het lezen enkele minuten. Elke lezer kost gebruik van het abonnement van de klant, daarom blijft het bij maximaal 20 documenten en de eerste pagina's van lange PDF's. Wil Michiel meer of minder, pas dan `--max` of `--per-map` aan.

---

## Stap G: customisatie en start van de setup

Naast `customisatie-checklist.md`:

1. **Tabel "Bestaande mappen" in `CLAUDE.md`.** Maak `wat` concreet met wat de lezers vonden. Pas `actie` aan waar de standaardtekst te vaag is ("de 3 nieuwste werfverslagen zijn het voorbeeld voor vorm en toon").
2. **Vertrouwelijkheid.** Mappen met rol `buiten_bereik` staan ook in `_kern/vertrouwelijkheid.md`, met de reden.
3. **Geen werkmappen in `_context/`.** Geen recurring-mappen, geen projecten per klant. Het werk staat in haar mappen, de output in `_projecten/`.
4. **Ontwerpnotitie en trajectplan** in `_ai-setup/`. Sessie 1 is deze opstart. Fase A en B schuiven een sessie op als de tijd op is.

Daarmee is INIT klaar. Geef kort weer wat de lezers vonden en sluit af met: **open een nieuw gesprek in Cowork op deze map en typ `SETUP`.** De gids begint in Fase 0 met de bevindingen uit `_ai-setup/analyse.md` en vraagt daarna wat enkel de klant weet. Vanaf dan is de skill niet meer nodig.

Controleer op het einde of de nieuwe mappen mee in haar backup zitten. De vraag over cloud-sync blijft een beslispunt (zie SKILL.md, stap 5).

---

## Weghalen

Wil de klant stoppen, dan verwijdert ze de namen uit de lijst bovenaan. Haar eigen mappen staan er dan nog zoals op dag 1. Dat staat ook in haar `LEESMIJ-ASSISTENT.md`.
