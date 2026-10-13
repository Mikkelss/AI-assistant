# Beslisboom: van kickoff-antwoorden naar config

Dit document vertaalt de antwoorden op de kickoff-vragenlijst naar de parameters in `config.json`, het bestand dat `scripts/build_skeleton.py` leest. Doorloop de blokken in volgorde. Waar een antwoord ontbreekt of vaag is, neem je de default en noteer je dat in het ontwerpvoorstel, zodat Michiel het kan bijsturen voor het skelet gebouwd wordt.

De volledige structuur van `config.json` staat onderaan, met een ingevuld voorbeeld in `assets/config.example.json`.

**Heeft de klant al een werkbare mappenstructuur?** Dan vertrek je niet van de kickoff-vragenlijst. Volg `references/bestaande-map.md`: scan van de mappen, `"overlay": true`, en de beslisboom hieronder enkel voor wat de scan niet beantwoordt.

---

## Blok 1 → identiteit en eigen werkdomein

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 1, 2 | `rol_label` | Het woord dat de klant zelf gebruikt voor zijn beroep, enkelvoud, kleine letters: "marketeer", "advocaat", "coach", "consultant", "copywriter", "boekhouder", "architect". Gebruik het woord van de klant, ook als jij een ander zou kiezen. |
| 2 | `sector` | Eén woord of korte term voor de sector: "marketing", "advocatuur", "coaching", "consultancy", "copywriting", "boekhouding", "architectuur". Wordt gebruikt om `references/sector-varianten.md` te raadplegen. |
| 3 | `naam`, `bedrijfsnaam` | Voornaam van de klant en naam van het bedrijf, de praktijk of het kantoor. |
| 2, 3 | `werkdomein_eigen` | De naam van map `1.`: "Eigen bedrijf" voor ondernemers en bureaus, "Eigen praktijk" voor advocaten, therapeuten, artsen, coaches met een praktijk, "Eigen kantoor" voor boekhouders, notarissen, architecten, "Eigen werking" wanneer niets anders past. Kies wat de klant zelf zou zeggen. |
| 4 | `team`, `multi_user` | `team` is vrije tekst voor `_context.md`. `multi_user` wordt `true` zodra iemand anders dan de klant zelf in de omgeving gaat werken (vraag 41 bevestigt dit). |
| 5, 6, 7 | `prefill.diensten`, `prefill.doelgroep`, `prefill.usps` | Letterlijk overnemen uit de antwoorden, licht opgeschoond. Dit zijn feiten, dus voorvullen mag. |

---

## Blok 2 → multi-instance-laag

Dit blok bepaalt de zwaarste structuurkeuze. Drie uitkomsten zijn mogelijk.

**Uitkomst A: geen multi-instance-laag.** Twee gevallen. Eén: vraag 8 is nee, of de klant heeft maar één of twee vaste opdrachtgevers waarvoor het werk nauwelijks verschilt. Twee: de klant heeft veel kortlopende, eenmalige opdrachten (vraag 10: weken, niet maanden) waarbij het enige wat verschilt in één file past (naam, locatie, aantal, datum, prijs). Doorvraag voor dat tweede geval: "als ik van elke opdracht één fiche zou bijhouden, staat daar dan alles op wat je moet weten?" Ja → uitkomst A, met één file per opdracht in een recurring-map. Dan `multi_instance: false`, geen map `2.`, en de instantie-velden in de config mogen leeg blijven. Fotografen, videomakers en illustratoren zitten meestal hier.

**Uitkomst B: multi-instance met volledig werkdomein per instantie.** Vraag 8 is ja én vraag 11 is ja (het werk verschilt fundamenteel: andere stem, andere strategie, andere context per klant). Dan `multi_instance: true` en `instantie_template: "volledig"`. Elke instantie krijgt `_context.md`, `_voice.md`, `_strategie.md`, `_voorbeelden/` en de recurring-mappen. Dit is het Kiara-patroon.

**Uitkomst C: multi-instance met lichte map per instantie.** Vraag 8 is ja maar vraag 11 is nee (telkens hetzelfde soort werk, dezelfde stem, enkel andere feiten). Dan `multi_instance: true` en `instantie_template: "licht"`. Elke instantie krijgt `_context.md` (met "Gevoeligheden eerst" en een partijentabel), `_strategie.md` (doel, spoor, mijlpalen) en de recurring-mappen; `projecten/` enkel als `projecten_per_instantie` true is. Voice en voorbeelden komen uit het eigen werkdomein, en het verschil in register per documenttype staat daar in `_voice.md` onder "Register per kanaal". Typisch voor een advocaat, een coach, een boekhouder, een architect, een consultant met één vaste methode. Na de eerste testronde blijkt dit vaker de juiste keuze dan verwacht: enkel wie voor merken schrijft (marketing, copywriting, ghostwriting) heeft echt een stem per instantie nodig.

Doorvraag bij twijfel over vraag 11: "Als ik een tekst van jou voor klant A naast een tekst voor klant B leg, zie ik dan het verschil zonder de naam te lezen?" Ja → volledig. Nee → licht.

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 8 | `multi_instance` | Zie uitkomsten hierboven. |
| 9 | `instantie_meervoud`, `instantie_enkelvoud`, `persoon_achter_instantie` | Letterlijk het woord van de klant. "Klanten"/"klant", "Dossiers"/"dossier", "Cliënten"/"cliënt", "Patiënten"/"patiënt", "Opdrachten"/"opdracht", "Projecten"/"project". Meervoud met hoofdletter voor de mapnaam, enkelvoud kleine letters voor in zinnen. Als de klant "projecten" zegt, gebruik dan "Opdrachten" voor map `2.` om verwarring met `9. Projecten/` te vermijden, en leg dat uit in het ontwerpvoorstel. `persoon_achter_instantie` is de mens met wie de klant praat wanneer de instantie geen mens is: bij "dossier" is dat "cliënt", bij "opdracht" "opdrachtgever". Het script leidt het af voor de courante woorden; vul het enkel in bij een ongewoon woord. |
| 11 | `instantie_template` | "volledig" of "licht", zie hierboven. |
| 12 | `projecten_per_instantie` | `true` wanneer de klant per instantie afgebakende projecten heeft. Default `true` bij "volledig", `false` bij "licht" tenzij expliciet anders. |
| 13 | `stakeholders_per_instantie` | `true` wanneer er meerdere contactpersonen per instantie zijn. Zet dan in het ontwerpvoorstel een opmerking dat een `relaties/`-submap per instantie later kan, zonder hem nu aan te maken. |

---

## Blok 3 → kanalen

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 14, 15 | `kanalen`, `kanalen_eigen_extra`, `test_kanaal` | `kanalen` is de lijst die élk werkdomein krijgt. `kanalen_eigen_extra` zijn kanalen die enkel de ondernemer zelf gebruikt (bij een marketeer: `rapport`, `offerte`); die komen enkel in het eigen werkdomein, zodat de instantie-template lean blijft. `test_kanaal` is optioneel: het kanaal waarop de klant in Fase B de eerste test doet. Leeg laten mag; het script kiest dan het eerste kanaal dat vrij testbaar is (een post of mail, geen verslag of offerte). Lijst van korte identifiers, kleine letters, geen spaties. Neem enkel output-types op die de klant minstens maandelijks maakt of waarvoor voorbeelden nuttig zijn. Bekende identifiers met een ingebouwde tip staan in `assets/kanalen.json`. Onbekende identifiers mag je toevoegen; het script geeft ze een generieke tip. |
| 16 | (geen parameter) | Gebruik dit antwoord in de customisatie-pass om in het voice-protocol van `CLAUDE.md` te benadrukken welke kanalen een sterk afwijkend register hebben. |
| 17 | `prefill.templates_bestaand` | Vrije tekst. Komt in het ontwerpvoorstel als "bestaande templates om over te nemen in `_kennis/templates/`". |

Richtlijn voor het aantal kanalen: 4 tot 8. Minder dan 4 en de laag voegt weinig toe. Meer dan 8 en de klant krijgt te veel lege mappen. Bundel waar zinnig: "facebook" en "instagram" blijven apart (ander register), maar "brief" en "aangetekende brief" worden één.

Bekende identifiers: `linkedin`, `instagram`, `facebook`, `tiktok`, `youtube`, `nieuwsbrief`, `blog`, `website`, `mail`, `ads`, `offerte`, `rapport`, `advies`, `contract`, `procedurestuk`, `pleitnota`, `brief`, `verslag`, `presentatie`, `script`, `casestudy`, `whitepaper`, `intake`, `evaluatie`.

---

## Blok 4 → recurring-mappen en projecten

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 18, 20 | `recurring_mappen` | Lijst van 2 tot 4 mapnamen voor terugkerend werk, kleine letters, meervoud. Bekende namen met een ingebouwde beschrijving staan in `assets/recurring.json`. Gebruik de woorden van de klant. Voorbeelden per sector staan in `references/sector-varianten.md`. |
| 19 | `projecten_per_instantie` | Bevestigt of corrigeert de keuze uit blok 2. |
| 21 | (geen parameter) | Gebruik dit in de customisatie-pass om de recurring-mappen van het eigen werkdomein te controleren. Vaak wil de klant voor zichzelf iets anders dan voor klanten (bijvoorbeeld `administratie/` erbij). Als dat zo is, zet dan `recurring_mappen_eigen` apart. |

Afgeleid: `content_kalender` wordt `true` zodra `kanalen` minstens één van `linkedin`, `instagram`, `facebook`, `tiktok`, `youtube`, `nieuwsbrief`, `blog` bevat. Dan komt er een `content-kalender.md` per werkdomein en een template in `_kennis/templates/`. Anders niet.

---

## Blok 5 → voice-laag

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 22 | `voice_gewicht` | Cijfer 8 tot 10 → "hoog". Cijfer 5 tot 7 → "midden". Cijfer 1 tot 4 → "laag". Bij "hoog" wordt Fase B in de setup-guide de zwaarste fase en krijgt de voice-analyse een aparte sessie in het trajectplan. Bij "laag" blijft `_voice.md` bestaan maar wordt hij korter en gaat de nadruk naar proces en context. |
| 23, 24 | `materiaal.voorbeelden_eigen`, `materiaal.voorbeelden_instantie` | `true`/`false`. Bepaalt of Fase B en C in de setup-guide meteen met materiaal kunnen starten. |
| 25 | `prefill.anti_ai` | Lijst van ergernissen, letterlijk overgenomen. Komen bovenaan in `_kern/anti-ai-stijl.md` als eerste eigen regels, vóór de defaults. |
| 26 | `talen` | Lijst van taalcodes, bijvoorbeeld `["nl"]` of `["nl", "fr"]`. Bij meer dan één taal én `voice_gewicht` "hoog": zet in het ontwerpvoorstel dat er per taal een `_voice-[taal].md` kan komen, zonder die nu aan te maken. Bij één taal: niets bijzonders. |

---

## Blok 6 → vertrouwelijkheid

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 27, 28 | `vertrouwelijkheid` | `true` zodra één van beide ja is: persoonsgegevens van derden (medisch, juridisch, financieel, HR) of een formele geheimhoudingsplicht (beroepsgeheim, deontologie, NDA). Bij twijfel `true`; het kost weinig en het ontbreken ervan is pijnlijker dan het overbodig zijn. |
| 29, 30 | `vertrouwelijkheid_regels` | Lijst van concrete regels in de woorden van de klant. Bij `vertrouwelijkheid` true komen ze in `_kern/vertrouwelijkheid.md`; bij false (het vaakst: geen NDA, wel één regel over discretie) zet het script ze onder "Veiligheid" in `_kern/werkregels.md`. Vul ze dus altijd in als er iets gezegd is. Bijvoorbeeld: "Nooit namen van cliënten in output die naar buiten gaat", "Medische details enkel in de dossiermap zelf, nooit in `_kern/` of `_kennis/`". |

Wanneer `vertrouwelijkheid` `true` is, verstrengt het script ook het inbox-protocol in `CLAUDE.md`: bij twijfel over de gevoeligheid van een bestand vraagt Claude eerst, in plaats van het te lezen en te classificeren.

---

## Blok 7 → sparring en frameworks

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 31 | `sparring` | `true` wanneer de klant AI (ook) als sparringpartner wil. Dan komt er een sparring-protocol in de setup-guide en een sessie in het trajectplan. `false` wanneer het enkel om uitvoerend werk gaat. |
| 32 | `frameworks_start` | Lijst van framework-namen die de klant al gebruikt. Per naam maakt de customisatie-pass een stub aan in `_kennis/frameworks/` met de vaste structuur, zodat de klant enkel nog moet invullen. |
| 33 | `sparring_beslissingen` | Lijst van de beslissingen die de klant met AI wil voorbereiden, in zijn woorden. Komen letterlijk in het sparring-blok van `SETUP-START-HIER.md`. |

---

## Blok 8 → nadruk van de fasen

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 34 | `prefill.huidige_tools` | Vrije tekst voor het ontwerpvoorstel en de ontwerpnotitie. |
| 35 | (geen parameter) | Gebruik dit in de customisatie-pass: wat eerder stilviel is een risico voor dit traject. Benoem het in de ontwerpnotitie en zet een tegenmaatregel in het trajectplan. |
| 36, 37 | `pijnpunten`, `fase_nadruk` | `pijnpunten` is de lijst van 3 tijdsvreters plus de "laat verdwijnen"-taak. `fase_nadruk` leid je af uit de aard van de pijn: vooral schrijfwerk en stem → "voice"; vooral nadenken, analyseren, beslissen → "strategie"; vooral herhaling, administratie, opvolging → "proces". Bij gemengd: kies de zwaarste en noteer de tweede. |

`fase_nadruk` verandert de volgorde van de setup-guide niet, wel de diepte per fase en de volgorde van de sessies in het trajectplan. Bij "strategie" komt de sparring-sessie vóór de skills-sessie. Bij "proces" komt de skills-sessie vroeger en wordt Fase B lichter.

---

## Blok 9 → traject en praktisch

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 38 | `tijd_per_week` | Vrije tekst, bijvoorbeeld "2 tot 3 uur, vooral in het weekend". Bepaalt de spreiding van sessies in het trajectplan: 2 uur per week of minder → sessies om de 2 weken (anders blijft er geen tijd voor huiswerk); meer → wekelijks kan. |
| 39 | `blokkades` | Lijst van periodes met datum. Het trajectplan plant rond deze periodes en zorgt dat er vóór een lange pauze iets werkends staat. |
| 40 | `cloud_sync` | Naam van de dienst of "geen". Bij "geen" komt in de ontwerpnotitie een actiepunt om dit vóór de eerste sessie te regelen. |
| 41 | `multi_user` | `true` zodra iemand anders meewerkt. Verandert het skelet niet in V1, maar zet in het ontwerpvoorstel een waarschuwing dat conflicten mogelijk zijn en dat dit in een latere fase een eigen aanpak vraagt. |
| 42 | `platform` | "windows" of "mac". Bepaalt de padnotatie in `LEESMIJ.md` en of de klant Claude Desktop nog moet installeren (actiepunt in de ontwerpnotitie). |

---

## Blok 10 → materiaal

| Vraag | Parameter | Hoe afleiden |
|---|---|---|
| 43 | `materiaal.website` | URL of leeg. Bij een URL: lees de site in de customisatie-pass en vul `prefill.bedrijf_in_een_zin`, `prefill.diensten`, `prefill.doelgroep` aan waar de kickoff-antwoorden dun zijn. Markeer wat van de website komt in de bronvermelding. |
| 44 | `materiaal.linkedin` | URL of leeg. Zelfde gebruik als website, voor `prefill.achtergrond`. |
| 45 | `materiaal.brand_book` | `true`/`false`. Bij `true`: actiepunt in de ontwerpnotitie om het document in `0. Inbox/` te droppen voor Fase B. |
| 46 | `materiaal.templates_bestaand` | `true`/`false` plus vrije tekst. Bij `true`: actiepunt om ze over te nemen in `_kennis/templates/`. |
| 47 | `materiaal.voorbeelden_eigen`, `materiaal.voorbeelden_instantie` | Bevestigt blok 5. |

---

## Voorvullen: wat wel en wat niet

De config heeft een `prefill`-blok. Alles wat daarin staat, komt in de gegenereerde files met de marker "[VOORSTEL op basis van je kickoff-antwoorden. Bevestig of pas aan tijdens SETUP Fase A.]" erboven. De klant ziet meteen dat het een voorstel is en neemt het tijdens Fase A over, past het aan of gooit het weg.

Wat je voorvult:
- Feiten over het bedrijf: `bedrijf_in_een_zin`, `diensten`, `doelgroep`, `usps`, `positionering`, `team`, `geschiedenis`.
- Feiten over de persoon: `achtergrond`, `sterktes`, `huidige_tools`.
- Wat de klant letterlijk zei over werkwijze: `proces`, `samenwerking`, `nee_tegen`.
- Anti-AI-ergernissen: `anti_ai`.

Wat je niet voorvult, ook al staat er iets bruikbaars in de antwoorden:
- `in_een_zin` (wie ben ik als [rol]) en `principes`. Dit zijn de identiteitsvragen. Laat ze als lege placeholder staan met de instructie dat de klant ze zelf formuleert tijdens Fase A. Je mag in de ontwerpnotitie wel noteren wat de klant erover zei, als geheugensteun voor Michiel tijdens de sessie.

De reden: een voorgevuld principe voelt niet als een keuze van de klant, en dan verdedigt hij het ook niet wanneer de output ervan afwijkt. Feiten zijn feiten; principes moeten doorleefd zijn.

---

## De volledige config

```json
{
  "naam": "Voornaam",
  "bedrijfsnaam": "Naam van bedrijf, praktijk of kantoor",
  "sector": "marketing",
  "rol_label": "marketeer",
  "werkdomein_eigen": "Eigen bedrijf",
  "werkdomein_lidwoord": "",
  "platform": "windows",
  "aangemaakt_op": "2026-09-28",
  "coach": "Michiel (AI Basecamp)",
  "coach_voornaam": "Michiel",

  "multi_instance": true,
  "instantie_meervoud": "Klanten",
  "instantie_enkelvoud": "klant",
  "instantie_lidwoord": "",
  "persoon_achter_instantie": "",
  "instantie_template": "volledig",
  "projecten_per_instantie": true,
  "stakeholders_per_instantie": false,

  "kanalen": ["linkedin", "instagram", "facebook", "nieuwsbrief", "mail", "website", "ads"],
  "kanalen_eigen_extra": [],
  "test_kanaal": "",
  "recurring_mappen": ["posts", "ads", "analyses"],
  "recurring_mappen_eigen": [],

  "voice_gewicht": "hoog",
  "talen": ["nl"],

  "vertrouwelijkheid": false,
  "vertrouwelijkheid_regels": [],

  "sparring": true,
  "sparring_beslissingen": [],
  "frameworks_start": [],

  "pijnpunten": [],
  "fase_nadruk": "voice",
  "tijd_per_week": "",
  "blokkades": [],
  "cloud_sync": "",
  "multi_user": false,
  "team": "",

  "materiaal": {
    "website": "",
    "linkedin": "",
    "brand_book": false,
    "templates_bestaand": false,
    "voorbeelden_eigen": false,
    "voorbeelden_instantie": false
  },

  "prefill": {
    "bedrijf_in_een_zin": "",
    "diensten": [],
    "doelgroep": "",
    "usps": [],
    "positionering": "",
    "team": "",
    "geschiedenis": "",
    "achtergrond": "",
    "sterktes": [],
    "proces": [],
    "nee_tegen": [],
    "samenwerking": "",
    "huidige_tools": "",
    "anti_ai": [],
    "templates_bestaand": ""
  }
}
```

Lege strings en lege lijsten zijn toegestaan. Het script behandelt ze als "niet voorgevuld" en zet dan de gewone placeholder. `recurring_mappen_eigen` leeg betekent: zelfde als `recurring_mappen`.

`werkdomein_lidwoord` werkt hetzelfde voor het eigen werkdomein: "het bedrijf", "het kantoor", maar "de praktijk", "de studio". Leeg laten mag; het script kent de courante de-woorden.

**Modus bestaande map.** Vijf extra velden, allemaal optioneel in de gewone modus: `"overlay": true`, `"bestaande_root"` (pad bij de klant, enkel ter info), `"bestaande_mappen"` (lijst van `{"pad", "rol", "wat"}`, optioneel `"actie"`), `"bestaande_schrijven": false` en `"instanties_start"` (0 tot 2 klantnamen, exact zoals de map bij de klant heet). Uitleg en bronnen in `references/bestaande-map.md`. Bij overlay negeert het script `recurring_mappen`, `recurring_mappen_eigen` en `projecten_per_instantie`: het werk staat in de mappen van de klant.

`instantie_lidwoord` ("de" of "het") stuurt de verbuiging in alle teksten: "deze klant" tegenover "dit dossier", "een nieuwe klant" tegenover "een nieuw dossier". Leeg laten mag: het script kent de courante het-woorden (dossier, project, bedrijf, traject, contract, …) en kiest zelf. Vul het enkel in bij een ongewoon woord.
