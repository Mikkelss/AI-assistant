---
name: ai-assistant-setup
description: "Start met INIT de AI-assistent van een klant van AI Basecamp, in haar Cowork, samen met Michiel. Heeft de klant al mappen, dan scant Claude de gekoppelde kopie, legt er een AI-laag naast zonder iets aan haar mappen te veranderen, en laat documentlezers parallel een selectie documenten lezen; de bevindingen komen klaar voor de setup-gids. Zonder mappen bouwt hij een nieuwe omgeving vanuit de kickoff-vragenlijst. Gebruik ALTIJD bij \"INIT\", \"init\", \"initialiseer de assistent\", \"zet de AI-assistent op\", \"ze heeft al mappen\", \"maak de Cowork-omgeving voor\", \"hier zijn de kickoff-antwoorden van X\", \"doe wat we voor Kiara deden\", ai-assistant-setup. NIET gebruiken bij \"SETUP\" of \"setup\": dat is de setup-gids in de map van de klant, die werkt zonder deze skill. Werk niet ad hoc - structuur, voice-protocol en flow moeten exact kloppen."
metadata:
  version: '1.5.0'
  updated: 2026-10-12 18:00
---

# AI-assistent setup voor een klant

Deze skill zet voor een klant van AI Basecamp een werkende Cowork-omgeving neer. Niet een generieke template, wel een omgeving die past bij hoe die ene ondernemer werkt: zijn sector, zijn klanten of dossiers, zijn kanalen, zijn gevoeligheden.

**De skill draait altijd bij de klant.** In haar Cowork, op haar computer, met haar account, met de map die ze zelf gekoppeld heeft. Michiel zit erbij en stuurt mee. Haar mappen en documenten komen nooit op de computer van Michiel, en de skill verwijst nergens naar zijn werkmap.

Het eindresultaat is een basis die klopt: de kamers op de juiste plek, de bordjes op de deuren, wat al in haar documenten stond netjes klaargezet, en een gids (`SETUP`) die de klant door de rest loodst. Wat over haar als persoon gaat, vult de klant zelf in.

**Twee woorden, twee taken.**

- **INIT** start deze skill, één keer per klant: de map in kaart brengen, de AI-laag en de setup-gids neerzetten, en de documenten laten lezen.
- **SETUP** is de setup-gids in de map van de klant. Die werkt volledig zonder deze skill: de klant kan hem later altijd zelf starten, ook als de plugin er niet meer is. Wordt deze skill toch geladen bij "setup", doe dan niets en volg de "Setup-trigger" in de `CLAUDE.md` van de klant.

## Eerst: waar staan we?

Draai bij elke INIT eerst:

```
python3 <skill-map>/scripts/waar_staan_we.py "<gekoppelde map>"
```

- **GEEN-MAP**: er is geen map gekoppeld. Vraag om de map te koppelen en stop.
- **NIEUW**: er staat nog geen AI-laag. Ga verder met de vraag hieronder en bouw.
- **CONFLICT**: er staat een `CLAUDE.md` of setup-file die niet van deze skill komt. Bouw niets, overschrijf niets. Toon wat er staat en leg het aan Michiel voor.
- **LAAG-AANWEZIG**: INIT is al gebeurd. Bouw niets opnieuw en draai het bouwscript niet.
  - Zegt de uitvoer "documenten nog niet gelezen" of "analyse: nog niet gedaan" en is het een bestaande map, maak dan enkel stap F van `references/bestaande-map.md` af (leesplan en lezen).
  - Anders is INIT klaar. Zeg dat, en dat de klant verder gaat met `SETUP` in een nieuw gesprek op deze map. Doe verder niets.

## Nieuwe omgeving of AI-laag op bestaande mappen?

Stel deze vraag vóór alles: **heeft de klant al een werkbare mappenstructuur?** Werk dat geordend staat per klant, dossier, werf of type, en waarin de klant zelf vlot haar weg vindt.

- **Nee**: de gewone modus. Kickoff-vragenlijst, nieuwe omgeving, de zes stappen hieronder.
- **Ja**: de modus bestaande map. Lees eerst `references/bestaande-map.md` volledig en volg die stap voor stap: scan van de gekoppelde kopie, voorstel samen bekijken, de AI-laag bouwen in de hoofdmap, en documentlezers een selectie documenten laten lezen. De bevindingen bevestigt de klant daarna in `SETUP`, Fase 0. Geen kickoff-vragenlijst.
- **Twijfel**: draai de scan (stap B in `references/bestaande-map.md`) en beslis samen met Michiel.

**Harde regel in de modus bestaande map:** aan de bestaande mappen verandert niets. Niets verwijderen, verplaatsen, hernoemen, overschrijven of erbij zetten. Het script bouwt enkel de AI-laag naast haar mappen, stopt bij elk naamconflict, kent daar geen `--force`, en controleert achteraf dat geen enkel bestaand bestand veranderd is. De documentlezers lezen enkel. In de `CLAUDE.md` van de klant staan haar mappen op alleen-lezen. Dat gaat pas open als de klant en Michiel het uitdrukkelijk beslissen.

**Vóór je start:** controleer dat er een map gekoppeld is in Cowork, en bij bestaande mappen dat het de kopie is en niet de originelen. Is er geen map gekoppeld, vraag dan om de map te koppelen en stop.

Hieronder staat per stap wat er in die modus anders is, telkens onder "Bij bestaande map".

## Wat je in handen krijgt

Drie soorten input, in aflopende volgorde van belang:

1. **De ingevulde kickoff-vragenlijst** (docx, md of geplakte tekst, in de gekoppelde map of in de chat). Dit is de bron voor bijna alles. De vragenlijst zelf staat in `references/kickoff-vragenlijst.md`.
2. **Materiaal**: website-URL, LinkedIn, brand book, voorbeelden van output. Gebruik dit om feiten aan te vullen waar de kickoff dun is. Nooit om identiteitsvragen in te vullen.
3. **Aanwijzingen van Michiel in de chat**: "doe het zoals bij Kiara", "hou het licht", "vertrouwelijkheid zeker aan". Die gaan voor op de beslisboom.

**Bij bestaande map:** de gekoppelde kopie zelf is de eerste bron: eerst de namen (scan), daarna een selectie documenten (documentlezers). Daarnaast wat Michiel en de klant in de sessie vertellen.

Geen kickoff-antwoorden in de gewone modus? Dan zijn er twee wegen. Michiel wil de vragenlijst zelf afnemen: geef hem `references/kickoff-vragenlijst.md`, en stop. Michiel wil het in de chat doen: doorloop de tien blokken van de vragenlijst met hem, blok per blok, en ga daarna verder alsof je de antwoorden als document kreeg. Vraag niet alle 47 vragen letterlijk; per blok volstaan de 2 of 3 die de beslissing bepalen (zie `references/beslisboom.md`).

## Het proces in zes stappen

### Stap 1: lezen en config afleiden

Lees de kickoff-antwoorden volledig. Lees dan `references/beslisboom.md` en doorloop de blokken in volgorde om `config.json` op te bouwen. Raadpleeg `references/sector-varianten.md` voor de sector van de klant; die geeft de typische keuzes als startpunt, de antwoorden van de klant gaan altijd voor.

Waar de antwoorden ontbreken of vaag zijn: neem de default uit de beslisboom en noteer dat als open punt voor het ontwerpvoorstel. Gok niet stil.

Vul het `prefill`-blok volgens de regels onderaan de beslisboom: feiten wel, identiteit niet. De klant moet "wie ben ik als [rol]" en "mijn principes" zelf formuleren tijdens Fase A. Dat is geen beperking van de skill, het is de reden waarom de setup later standhoudt.

Bij een website-URL of LinkedIn: lees die en vul `prefill` aan waar de kickoff dun is. Noteer per veld waar het vandaan komt; dat komt in de ontwerpnotitie.

**Bij bestaande map:** draai eerst `scripts/scan_structuur.py` rechtstreeks op de gekoppelde map (stap B in `references/bestaande-map.md`). Rapport, JSON en config gaan naar een werkmap buiten de map van de klant; na het bouwen komen ze in `_ai-setup/`. Bouw de config met `"overlay": true` en de extra velden uit stap C. De beslisboom gebruik je enkel voor wat de scan niet beantwoordt.

### Stap 2: ontwerpvoorstel tonen en wachten

Dit is het eerste pauzemoment. Toon Michiel en de klant, in de chat, in deze volgorde:

- **De mappenboom** die gebouwd zal worden (gebruik `--dry-run` van het script, zie stap 3, en plak de boom).
- **De sleutelkeuzes** als korte tabel: werkdomein-naam, instantie-naam en -template, kanalen, recurring-mappen, vertrouwelijkheid aan of uit, sparring aan of uit, voice-gewicht, fase-nadruk. Per keuze één regel reden, gekoppeld aan het kickoff-antwoord of aan een principe uit `references/principes.md`.
- **Afwijkingen van het Kiara-patroon** apart benoemd, want dat is het referentiekader dat Michiel kent.
- **Open punten** waar je een default nam.
- **Wat voorgevuld wordt** en wat bewust leeg blijft.

**Bij bestaande map:** hou het kort en in gewone taal, want de klant leest mee: de mappenkaart, de tabel bestaande mappen met rollen, wat de AI-laag toevoegt, het resultaat van de conflictcheck en de keuze voor alleen-lezen (stap D in `references/bestaande-map.md`). De sleutelkeuzes en het Kiara-patroon laat je weg tenzij Michiel ernaar vraagt.

Vraag dan expliciet om akkoord of bijsturing. Bouw niets voor Michiel bevestigt. Past hij iets aan, werk de config bij en toon enkel wat veranderde.

### Stap 3: skelet bouwen met het script

Het script staat in de map van deze skill: `scripts/build_skeleton.py`, naast `references/` en `assets/`. De skill-map is de map waarin deze SKILL.md staat; in Cowork bereik je ze via bash op het mount-pad van de skills of plugins (het pad staat bovenaan wanneer de skill geladen wordt). Draai de scripts met Python 3, geen extra packages nodig.

Ontbreekt een file die hier genoemd wordt (bijvoorbeeld `scripts/kies_documenten.py` of `references/documentlezer.md`), dan is de installatie onvolledig. Stop en zeg tegen Michiel dat de plugin opnieuw geïnstalleerd moet worden. Werk nooit met een mengeling van versies.

```
python3 <skill-map>/scripts/build_skeleton.py --config <pad>/config.json --dry-run
python3 <skill-map>/scripts/build_skeleton.py --config <pad>/config.json --out "<doelmap>"
python3 <skill-map>/scripts/build_skeleton.py --check "<doelmap>"
```

**Doelmap:** de map die de klant in Cowork gekoppeld heeft. In de gewone modus is dat een nieuwe, lege map.

**Config bewaren:** schrijf `config.json` eerst naar een werkmap buiten de doelmap (de scratch- of outputmap van Cowork, of `/tmp/ai-setup`). Het script bewaart de config na het bouwen zelf in `_ai-setup/config.json`. Zo kan de omgeving later opnieuw gegenereerd of aangepast worden.

**Bij bestaande map:** de doelmap is de hoofdmap van de gekoppelde kopie. Je geeft de scan mee voor de conflictcheck en laat de werkbestanden bewaren:

```
python3 <skill-map>/scripts/build_skeleton.py --config <werk>/config.json --out "<hoofdmap>" --bestaande <werk>/scan.json --bewaar <werk>/mappenkaart.md <werk>/scan.json
```

Meldt het script een conflict of een gewijzigd bestand, stop dan en leg het aan Michiel voor.

Het script weigert een bestaande, niet-lege doelmap tenzij `--force`. Gebruik `--force` enkel na expliciete bevestiging van Michiel, want het overschrijft wat er staat.

Na het bouwen draait het script zelf een controle op placeholder-resten en lege mappen. Staat er een probleem, los het op voor je verder gaat.

### Stap 4: customisatie-pass

Het script levert een correct maar generiek skelet. Nu maak je het van deze klant. Volg `references/customisatie-checklist.md` stap voor stap. De kern: routing-tabel en setup-guide in de taal van de sector, ergernissen van de klant bovenaan in de anti-AI-stijl, intake-vragenlijst en planningsinstrument passend bij het instantie-type, framework-stubs aangevuld, vertrouwelijkheidsregels concreet (sectorblokken in `references/vertrouwelijkheid-per-sector.md`).

**Bij bestaande map:** eerst de documenten (stap F in `references/bestaande-map.md`): leesplan maken, de documentlezers parallel laten lezen, samenleggen in `_ai-setup/analyse.md`. Schrijf zelf niets van de bevindingen in `_kern/` of `_kennis/`: dat gebeurt in `SETUP`, Fase 0, na het akkoord van de klant. Daarna de punten uit stap G. De customisatie (tabel bestaande mappen, vertrouwelijkheid) steunt dan op wat in haar documenten staat, niet op wat je uit de namen raadt.

Alles wat de klant leest, schrijf je in Michiel's stem: Vlaams-informeel, jij-vorm, geen em-dashes, geen "niet X maar Y", korte alinea's, cijfers als cijfers, "na je akkoord" en nooit "na jouw ja". Lees vóór je begint `assets/skelet/_kern/schrijfregels-basis.md` in deze skill: dat zijn de basisregels van AI Basecamp, en ze komen ook in de `_kern/` van de klant. De klant moet het gevoel hebben dat Michiel dit voor haar schreef.

### Stap 5: trajectplan en ontwerpnotitie

Twee documenten in `_ai-setup/` van de doelmap:

- `[datum]-trajectplan-[voornaam].md`: sessie per sessie volgens `references/trajectplan-skelet.md`, aangepast aan tijd, blokkades en fase-nadruk, met sessiedata als voorstel. Bij `multi_instance` false vervalt de fase "eerste klant" en gaat die tijd naar verdieping en vroegere skills.
- `[datum]-ontwerpnotitie-[voornaam].md`: wat gekozen is en waarom, wat voorgevuld is, wat bewust leeg bleef (met wat de klant erover zei als geheugensteun), aandachtspunten en actiepunten vóór de eerste sessie, en wat Michiel nog moet nakijken. Structuur staat in stap 8 van de customisatie-checklist.

Loopt de sessie uit, schrijf dan eerst de ontwerpnotitie kort (wat gekozen is, wat open staat) en werk ze later af. Een afgewerkte `analyse.md` gaat voor.

**Aandachtspunt dat in elke ontwerpnotitie hoort:** waar de Cowork-map fysiek staat. Michiel's eigen regel is: werkmap lokaal, met een geplande kopie naar de cloud, omdat Cowork bestanden stil afknot wanneer de map rechtstreeks in een OneDrive-map staat. Of dat ook geldt voor Dropbox of Google Drive, en voor Mac, is niet bevestigd. Zet het als beslispunt voor sessie 1 in de ontwerpnotitie en in het trajectplan, en schrijf in de `LEESMIJ.md` van de klant niet "zet de map in OneDrive" alsof dat vanzelfsprekend is.

### Stap 6: overzicht en tweede pauze

Toon Michiel en de klant wat er staat: de nieuwe files, wat al ingevuld en bevestigd is, wat nog open staat, en de lijst "nog na te kijken" uit de ontwerpnotitie.

Bij bestaande map: geef in een paar regels weer wat de lezers vonden (hoeveel voorbeelden, werkregels, feiten en vragen), zonder ze al te laten bevestigen.

Sluit INIT dan af met de volgende stap, letterlijk: **open een nieuw gesprek in Cowork op deze map en typ `SETUP`.** Een nieuw gesprek is nodig, want Claude leest de nieuwe `CLAUDE.md` pas bij de start van een gesprek. Vanaf dan leidt de setup-gids, en deze skill is niet meer nodig.

## Als Michiel er niet is

De twee pauzemomenten bestaan om Michiel te laten bijsturen. Zegt hij vooraf dat hij weg is ("beslis zelf, ik lees het achteraf"), dan neem je bij elk pauzemoment de beslissing die hij het meest waarschijnlijk zou nemen, schrijf je die op met de reden (in `ontwerpvoorstel.md` en `eindoverzicht.md` in de klantmap), en ga je door. Bevindingen uit de documenten schrijf je in die modus niet weg: ze blijven open in `_ai-setup/analyse.md` tot de klant ze bevestigt. Wat je nooit zelf beslist, ook niet in die modus: `--force` op een bestaande map, iets wijzigen buiten de AI-laag, `bestaande_schrijven` op `true` zetten, of een keuze die tegen een expliciete aanwijzing van Michiel ingaat.

Die notities komen in `_ai-setup/`. Vaste opbouw van `eindoverzicht.md` in die modus, zodat runs vergelijkbaar blijven: wat er staat (tabel met files), wat de customisatie-pass veranderde tegenover het script, de beslissingen die je zelf nam met reden, wat Michiel nog nakijkt, hoe de klant start, en onderaan verbeterpunten voor de skill zelf.

## Wat de skill bewust niet doet

- **De setup invullen zonder de klant.** Feiten en werkregels uit haar documenten zet je klaar als voorstel, en ze komen pas in de files na haar akkoord. Identiteit, stem en strategie zijn werk voor de klant zelf, tijdens de coaching.
- **Skills bouwen voor de klant.** Dat komt pas na sessie 3 of 4, wanneer de terugkerende taken duidelijk zijn. Een skill bevriest een patroon dat nog moet uitkristalliseren.
- **Meer lagen dan nodig.** Geen `relaties/`, geen `_memory.md` per werkdomein, geen multi-user-aanpak bij de start. Die komen op trigger, later. Het skelet is bewust lean; wat de klant niet nodig heeft, hoort er niet in.
- **De bestaande mappen van de klant aanpassen.** In de modus bestaande map blijft haar structuur exact zoals ze was. Opkuisen, hernoemen of context in haar mappen zetten kan later, op uitdrukkelijke vraag, als apart voorstel.
- **Overschrijven zonder vraag.** Nooit `--force` zonder bevestiging, nooit iets aanpassen buiten de AI-laag.

## Wanneer iets niet past

Past de klant in geen enkele sector-variant? Beantwoord de drie vragen onderaan `references/sector-varianten.md` (verschilt de stem per instantie, is er geheimhouding, waar zit de pijn) en bouw daarop. Leg in het ontwerpvoorstel uit dat het een nieuwe variant is. Werkt het, noteer de variant dan in het eindoverzicht onder "verbeterpunten voor de skill", zodat Michiel ze in de bron kan toevoegen.

Heeft de klant een wens die het voice-protocol breekt (bijvoorbeeld: "zet mijn stem in `_kern/` zodat ze altijd geladen is")? Doe het niet stil. Leg uit waarom niet (principe 2 in `references/principes.md`) en stel het alternatief voor: de stem in het eigen werkdomein, en het protocol zorgt dat ze geladen wordt wanneer het hoort.

## Bestanden in deze skill

- `references/kickoff-vragenlijst.md`: de 47 vragen in 10 blokken, met per blok welke beslissing eraan hangt.
- `references/beslisboom.md`: van antwoord naar config-parameter, plus de volledige config-structuur.
- `references/sector-varianten.md`: typische keuzes per sector en de drie vragen voor het onbekende geval.
- `references/principes.md`: de zeven principes, voor wanneer je een keuze moet verdedigen.
- `references/customisatie-checklist.md`: de tien stappen na het script.
- `references/vertrouwelijkheid-per-sector.md`: vaste blokken per sector voor `_kern/vertrouwelijkheid.md`.
- `references/trajectplan-skelet.md`: de vorm van het trajectplan en hoe de nadruk de volgorde verandert.
- `references/bestaande-map.md`: de modus bestaande map, van scan tot het lezen van de documenten. Wat daarna komt, staat in de setup-gids zelf.
- `references/documentlezer.md`: de instructie voor de documentlezers. De plugin levert ze ook mee als agent `documentlezer`.
- `assets/skelet/`: alle templates met placeholders. Aanpassen mag, maar test daarna met de drie voorbeeldconfigs.
- `assets/kanalen.json` en `assets/recurring.json`: bekende kanalen en recurring-mappen met hun tips. Nieuwe toevoegen mag.
- `assets/config.example.json`: de Kiara-config als voorbeeld.
- `scripts/waar_staan_we.py`: zegt of er al een AI-laag staat en waar de setup gebleven is. Altijd eerst draaien.
- `scripts/build_skeleton.py`: bouwt, controleert, toont de boom. Met `"overlay": true` enkel de AI-laag, met conflictcheck en controle op bestaande bestanden.
- `scripts/scan_structuur.py`: brengt een bestaande mappenstructuur in kaart. Opent geen enkel bestand.
- `scripts/kies_documenten.py`: maakt het leesplan: welke documenten de lezers lezen, in pakketten van hoogstens 6.
- `scripts/tekst_uit_document.py`: haalt tekst uit Word, PDF, PowerPoint, mail en tekstbestanden, zonder extra packages.
- `assets/skelet/_kern/schrijfregels-basis.md`: de basisregels van AI Basecamp tegen AI-stijl. Komt letterlijk in de `_kern/` van elke klant en wordt bij elke build gelijkgezet met Michiel's eigen versie.

---

## Changelog

- **1.5.0** (2026-10-12): INIT en SETUP gescheiden. INIT start deze skill één keer per klant: scan, AI-laag met setup-gids, documenten lezen, bevindingen in `_ai-setup/analyse.md` (vaste secties, `| status: open`). SETUP is enkel de setup-gids in de map van de klant en werkt zonder skill; de skill doet niets bij "setup". Fase 0 van de gids begint met "Wat Claude in je documenten vond": per onderwerp voorleggen, wegschrijven na akkoord met bron, status bijwerken. INIT eindigt met "open een nieuw gesprek en typ SETUP", omdat `CLAUDE.md` pas bij een nieuw gesprek geladen wordt. `waar_staan_we.py` blijft: een tweede INIT bouwt niets opnieuw.
- **1.4.1** (2026-10-12): één setup, één woord. Nieuw `scripts/waar_staan_we.py` (NIEUW, LAAG-AANWEZIG, CONFLICT, GEEN-MAP, plus openstaande punten en eerste open fase). Zegt de klant later opnieuw "setup", dan bouwt de skill niets opnieuw en gaat hij verder met de analyse of de setup-gids. Na het bouwen en lezen gaat de skill in hetzelfde gesprek meteen over naar de gids, zonder dat de klant `SETUP` moet typen. Vast formaat `| status: open` in `analyse.md`. `CLAUDE.md` van de klant zegt dat de plugin en de gids dezelfde setup zijn.
- **1.4.0** (2026-10-12): de skill draait altijd bij de klant, in haar Cowork, samen met Michiel. Modus bestaande map: geen export meer, de scan loopt rechtstreeks op de gekoppelde kopie, de laag wordt gebouwd in de hoofdmap (zelfde veiligheid: geen overschrijven, controle achteraf). Nieuw: stap "documenten lezen" met `kies_documenten.py` (leesplan, max 20 documenten, archief en buiten bereik nooit), `tekst_uit_document.py` (Word, PDF, PowerPoint, mail, zonder packages) en documentlezers die parallel lezen (agent `documentlezer` in de plugin, instructie in `references/documentlezer.md`). Bevindingen gaan naar `_ai-setup/analyse.md` en worden per onderwerp bevestigd voor ze in `_kern/` of `_kennis/` komen; `SETUP` slaat bevestigde punten over. Nieuwe map `_ai-setup/` voor config, scan, leesplan, analyse, ontwerpnotitie en trajectplan; `build_skeleton.py --bewaar`. `_kern/schrijfregels-basis.md` met de volledige anti-AI-schrijfstijl van Michiel in elke omgeving, `_kern/anti-ai-stijl.md` voor de eigen aanvullingen. Geen verwijzingen meer naar Michiel's werkmap. "Na jouw ja" vervangen door "na je akkoord".
- **1.3.0** (2026-09-29): modus bestaande map, na de opstart met An (Anders Office). Beslisvraag vooraf: heeft de klant al een werkbare mappenstructuur? Zo ja, geen kickoff-vragenlijst. Nieuw script `scan_structuur.py` (leest enkel namen, groottes en datums uit een map, PowerShell-CSV of padenlijst; herkent de klantenlaag, gedeelde opbouw, gevoelige namen, referentiemappen, versienamen en naamconflicten; stelt `bestaande_mappen` voor). `build_skeleton.py` met `"overlay": true`: enkel de AI-laag (`CLAUDE.md`, `LEESMIJ-ASSISTENT.md`, setup-files, `_kern`, `_kennis`, `_context`, `_inbox`, `_projecten`), nooit over een bestaand pad, geen `--force`, conflictcheck met `--bestaande`, controle achteraf dat geen bestaand bestand veranderde, `--check` enkel op de laag. Templates: hardregel en tabel "Bestaande mappen" in `CLAUDE.md`, alleen-lezen als default, Fase 0 "je mappen leren kennen" in setup-guide en status, `_kennis/referentiedocumenten.md`, beslisregels in werkregels, bronsystemen in `_context.md`, werkmap per klant, `LEESMIJ-ASSISTENT.md` met "wat er veranderd is: niets" en hoe je de laag weghaalt. Nieuwe reference `bestaande-map.md` (export, scan, config, ontwerpvoorstel, bouwen, customisatie, overzetten). Gewone modus levert byte voor byte dezelfde output als 1.2.0.
- **1.2.0** (2026-09-28): na testronde 2 (4 sectoren, met en zonder skill, 100% tegenover 58% op de checks). Templates: cloud-sync als beslispunt in plaats van vanzelfsprekendheid, "namens" tegenover "aan" een instantie in het voice-protocol bij volledig, discretieregels ook zonder vertrouwelijkheidsvlag, prijsregel zodra `offerte` een kanaal is (CLAUDE.md, werkregels, tarieflijst in `_context.md`), proces-nadruk splitst Fase B, `_voorbeelden/LEESMIJ.md` juist bij licht, `9. Projecten/LEESMIJ.md` juist zonder projecten per instantie, register-tabel met aanspreekvorm, laatste contrastzinnen weg. Script: enkelvoud en vrij-testbaar per kanaal met een slim gekozen test-kanaal, `kanalen_eigen_extra` voor kanalen die enkel de ondernemer gebruikt, persoon achter de instantie (cliënt bij dossier), ASCII-slug in map- en bestandsnamen, URL-detectie voor website en LinkedIn, waarschuwing bij kanalen of mappen die niet in de json staan. Data: 8 recurring-mappen erbij, enkelvoud voor alle kanalen. References: sector-variant creatieve solo, beslisboom-uitkomst A verbreed naar eenmalige opdrachten, intake-voorbeeldlijsten per instantie-type, planningsinstrument los van de content-kalender, sessiedata als voorstel met schoolvakantiecheck, twee nieuwe references (vertrouwelijkheid per sector, trajectplan-skelet), vaste opbouw voor het eindoverzicht.
- **1.1.0** (2026-09-28): na testronde 1 (3 sectoren, met en zonder skill). Templates: em-dashes en contrastzinnen weg, sparring-blok in setup-guide en CLAUDE.md, "Register per kanaal" in `_voice.md`, lichte instantie-template met eigen `_context.md` ("Gevoeligheden eerst", partijentabel) en `_strategie.md` (doel, spoor, mijlpalen), content-kalender enkel bij eigen of volledig, verwijzing naar `projecten/` enkel als die map bestaat. Script: lidwoord van het werkdomein (de praktijk, het kantoor), template-mapnaam verbogen (`_template-nieuw-dossier`), meervoud per kanaal. Data: 2 kanalen en 8 recurring-mappen erbij. References: advocaat-variant naar licht met register per documenttype, `sparring_beslissingen` uit vraag 33, planningsinstrument als vaste checklist-stap, verwijder-toestemming benoemd. SKILL.md: "als Michiel er niet is" en het cloud-sync-beslispunt.
- **1.0.0** (2026-09-28): eerste versie, gedestilleerd uit de opbouw met Kiara. Kickoff-vragenlijst, beslisboom, sector-varianten, skelet-templates met lidwoord-verbuiging, build-script met controle, customisatie-checklist, trajectplan en ontwerpnotitie als vaste deliverables.
