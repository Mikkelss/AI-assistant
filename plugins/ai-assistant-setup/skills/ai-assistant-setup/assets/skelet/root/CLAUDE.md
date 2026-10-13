# CLAUDE.md: {{naam}} Cowork

Dit is de routing-file van de werkomgeving. Bij elke sessiestart leest de AI deze file en volgt hij de regels en pointers die hier staan. Alleen wat hier expliciet "altijd inladen" zegt, wordt automatisch geladen. De rest komt erbij op aanvraag.
{{#if overlay}}
Deze omgeving is een laag bovenop mappen die er al waren. De AI-laag bestaat uit `CLAUDE.md`, de setup-files, `LEESMIJ-ASSISTENT.md`, `_kern/`, `_kennis/`, `_context/`, `_inbox/`, `_projecten/` en `_ai-setup/`. Al de rest is van {{naam}} en blijft zoals het is. Zie "Bestaande mappen: hardregel" hieronder.
{{/if}}
---

## Sessiestart: altijd inladen

Bij elke nieuwe sessie, stil, zonder bevestiging vragen:

1. `_kern/wie-ik-ben.md`: wie {{naam}} is als {{rol_label}} en hoe {{naam}} werkt
2. `_kern/werkregels.md`: werkwijze, bestandsnamen, voice-protocol, projecten-regel
3. `_kern/schrijfregels-basis.md`: de basisregels tegen AI-stijl, voor élke output en in elke taal (de file zelf is in het Engels)
4. `_kern/anti-ai-stijl.md`: de eigen ergernissen en aanvullingen van {{naam}}, bovenop de basisregels
{{#if vertrouwelijkheid}}5. `_kern/vertrouwelijkheid.md`: wat nooit gedeeld, gelezen of geproduceerd mag worden
{{/if}}
Niets anders is altijd geladen. `_ai-setup/` bevat enkel werkbestanden van de setup en wordt tijdens het gewone werk niet gelezen. Voice en context van {{#if multi_instance}}het eigen werkdomein of een {{i_specifieke}} {{instantie_enkelvoud}}{{else}}het werkdomein{{/if}} worden pas geladen wanneer er in die map gewerkt wordt (zie voice-protocol hieronder).

---

## Setup-trigger

`SETUP-START-HIER.md` wordt niet automatisch ingeladen bij sessiestart. Niet voorstellen, niet ernaar verwijzen op eigen initiatief.

**Trigger:** wanneer {{naam}} `SETUP` typt (in hoofdletters, of een variant als "setup", "start setup", "doe de setup", "laten we de setup doen"):

`SETUP` is enkel deze gids. De plugin `ai-assistant-setup` hoort bij `INIT` (het eenmalige opzetten) en wordt hier niet gebruikt.

1. Lees `SETUP-STATUS.md` om te zien welke fasen al voltooid zijn.
2. Lees `SETUP-START-HIER.md` integraal voor de gespreksinstructies en vragen.
3. Stel voor om te starten of verder te gaan op basis van `SETUP-STATUS.md`: alle fasen "Niet gestart" → {{#if overlay}}Fase 0{{else}}Fase A{{/if}}; een fase "In uitvoering" → die afwerken; een fase "Voltooid" en de volgende "Niet gestart" → die volgende.
4. Voer het gesprek actief: stel zelf de vragen één voor één, wacht op antwoord, bevestig kort, ga naar de volgende vraag. Jij neemt de leiding.
5. Verwerk per fase de antwoorden in de juiste files (zoals beschreven in `SETUP-START-HIER.md`) en toon het resultaat ter bevestiging.
6. Aan het begin van een fase: zet de status van die fase in `SETUP-STATUS.md` op `In uitvoering` met de startdatum.
7. Aan het einde van een voltooide fase: vink de checkboxes af, zet de status op `Voltooid` met datum, en vraag of {{naam}} door wil naar de volgende fase of wil stoppen. Bij stoppen: zet de volgende fase niet aan. In elke sessie waarin iets aan de setup veranderde, komt er één logregel onderaan `SETUP-STATUS.md`, ook als de fase nog niet af is.

---

## Voice-protocol: hardregel

Voor elke schrijftaak: bepaal eerst (1) voor wie er geschreven wordt en (2) op welk kanaal of in welk documenttype de tekst landt. Begin niet aan een tekst zonder beide.

**Stap 1: voor wie**
{{#if multi_instance}}- Werk voor een {{instantie_enkelvoud}}{{#if overlay}}{{#if instanties_pad}} (bestanden in `{{instanties_pad}}/[naam]/`){{/if}}, context{{/if}} uit `{{instantie_map}}/[naam]/` → laad {{#if volledig}}uitsluitend de `_voice.md`, `_context.md` en (indien relevant) `_strategie.md` van {{i_die}} {{instantie_enkelvoud}}. Negeer alle andere voices.{{else}}de `_context.md` van {{i_die}} {{instantie_enkelvoud}} voor de feiten, en `{{eigen_map}}/_voice.md` voor de stem (de stem is altijd die van {{naam}} zelf).{{/if}}
- Werk voor {{wd_lidwoord}} eigen {{werkdomein_lower}} → laad `{{eigen_map}}/_voice.md`, `_context.md` en (indien relevant) `_strategie.md`.
{{#if volledig}}- Let op het verschil tussen schrijven **namens** een {{instantie_enkelvoud}} en schrijven **aan** een {{instantie_enkelvoud}}. Wat {{instantie_lidwoord}} {{instantie_enkelvoud}} zelf publiceert (post, advertentie, nieuwsbrief): stem van {{instantie_lidwoord}} {{instantie_enkelvoud}}. Wat {{naam}} naar {{instantie_lidwoord}} {{instantie_enkelvoud}} stuurt (rapport, mail, offerte): stem van {{naam}} (`{{eigen_map}}/_voice.md`) met de `_context.md` van {{i_die}} {{instantie_enkelvoud}} als achtergrond. Twijfel? Vraag het.
{{/if}}- Geen {{instantie_enkelvoud}} of eigen werk in scope → vraag expliciet: "Voor wie schrijf je dit?" Schrijf niets zonder antwoord.
{{else}}- Laad `{{eigen_map}}/_voice.md`, `_context.md` en (indien relevant) `_strategie.md`.
- Twijfel of het om eigen werk gaat of om iets voor een derde → vraag het. Schrijf niets zonder antwoord.
{{/if}}
**Stap 2: op welk kanaal**
- Bepaal het kanaal: {{kanalen_lijst}}.
- Laad uitsluitend de inhoud van `_voorbeelden/[kanaal]/` van het werkdomein dat in stap 1 bepaald is.
- Negeer alle andere kanaal-submappen binnen `_voorbeelden/`. Zo vermijd je dat het ritme van het ene kanaal in het andere sijpelt.
- Bij twijfel over het kanaal: vraag "voor welk kanaal is dit?". Schrijf niets zonder antwoord.

Voorbeelden van kanaal-detectie:
{{#each kanalen_obj}}- "{{voorbeeld_prompt}}" → `_voorbeelden/{{id}}/`
{{/each}}
De basisregels uit `_kern/schrijfregels-basis.md` en de anti-AI-stijl uit `_kern/anti-ai-stijl.md` blijven altijd geldig. Die staat los van voice en kanaal en geldt voor élke output.

---

{{#if overlay}}## Bestaande mappen: hardregel

De mappen van {{naam}} {{#if bestaande_root}}in `{{bestaande_root}}` {{/if}}bestonden al voor deze AI-laag. Daar geldt:

{{#if bestaande_schrijven}}- Lezen mag, binnen wat de tabel hieronder toelaat.
- Een nieuwe file in een bestaande map mag enkel na bevestiging van {{naam}}. Toon eerst het volledige pad.
- Bestaande files en mappen nooit overschrijven, hernoemen, verplaatsen of verwijderen. Ook niet op vraag van een andere taak. Vraagt {{naam}} het zelf, toon dan eerst exact wat er verandert en wacht op een uitdrukkelijk ja.
{{else}}- Lezen mag, binnen wat de tabel hieronder toelaat.
- Schrijven in een bestaande map mag niet. Geen nieuwe files, geen aanpassingen, niets hernoemen, verplaatsen of verwijderen.
- Nieuwe output komt in `{{projecten_map}}/`. {{naam}} zet het zelf op de juiste plek in de eigen mappen.
- Vraagt {{naam}} toch om iets in een bestaande map te zetten: zeg dat deze regel dat nu tegenhoudt, en dat ze aangepast kan worden in overleg met {{coach_voornaam}}.
{{/if}}- Twijfel je of een map bij de AI-laag hoort of bij {{naam}}? Behandel ze als bestaande map.

| Map | Wat erin zit | Wat Claude ermee doet |
|---|---|---|
{{#each bestaande_mappen_obj}}| `{{pad}}/` | {{wat}} | {{actie}} |
{{/each}}{{#if heeft_bestaande_mappen}}| Alle andere bestaande mappen | Nog niet beschreven | Eerst aan {{naam}} vragen wat erin zit voor je ze opent |
{{else}}| [nog in te vullen tijdens Fase 0] | | |
{{/if}}
{{#if buiten_bereik_obj}}**Buiten bereik, zonder uitzondering:** {{#each buiten_bereik_obj}}`{{pad}}/`{{sep}}{{/each}}. Niet openen, niet doorzoeken, niet citeren. Ook niet als een zoekopdracht er vanzelf in zou belanden.

{{/if}}**Referentiedocumenten:** welk document voor welke taak het voorbeeld is, staat in `_kennis/referentiedocumenten.md`. Kijk daar eerst voor je zelf een voorbeeld zoekt in de mappen.

---

{{/if}}## Routing: wat hoort waar

| Type werk | Folder |
|---|---|
{{#if overlay}}| Bestanden van {{naam}}: dossiers, verslagen, templates, archief | De bestaande mappen, zie de tabel hierboven. Alleen lezen{{#if bestaande_schrijven}}, nieuwe files na bevestiging{{/if}}. |
| Stem, context en strategie van {{wd_lidwoord}} eigen {{werkdomein_lower}} | `{{eigen_map}}/` |
{{#if multi_instance}}| Context en afspraken over een {{instantie_enkelvoud}} | `{{instantie_map}}/[naam]/`{{#if instanties_pad}}. De bestanden zelf staan in `{{instanties_pad}}/[naam]/`{{/if}} |
| {{i_Nieuwe}} {{instantie_enkelvoud}} in de AI-laag | Kopieer `{{instantie_map}}/_template-{{i_nieuwe}}-{{instantie_slug}}/` naar `{{instantie_map}}/[naam]/` |
{{/if}}| Nieuwe output en werk in uitvoering | `{{projecten_map}}/[YYYY-MM-projectnaam]/` |
| Welk document het voorbeeld is voor welke taak | `_kennis/referentiedocumenten.md` |
{{else}}| Content, analyse of ander werk voor {{wd_lidwoord}} eigen {{werkdomein_lower}} | `{{eigen_map}}/` |
{{#if multi_instance}}| Werk voor een {{instantie_enkelvoud}} | `{{instantie_map}}/[naam]/` |
| {{i_Nieuwe}} {{instantie_enkelvoud}} aanmaken | Kopieer `{{instantie_map}}/_template-{{i_nieuwe}}-{{instantie_slug}}/` naar `{{instantie_map}}/[naam]/` |
{{#if projecten_per_instantie}}| Project gebonden aan één {{instantie_enkelvoud}} | `{{instantie_map}}/[naam]/projecten/[YYYY-MM-projectnaam]/` |
{{/if}}{{/if}}| Project gebonden aan {{wd_lidwoord}} eigen {{werkdomein_lower}} | `{{eigen_map}}/projecten/[YYYY-MM-projectnaam]/` |
| Project dat over meerdere werkdomeinen heen gaat | `{{projecten_map}}/[YYYY-MM-projectnaam]/` |
{{/if}}| Framework, methodiek, theorie | `_kennis/frameworks/` |
| Herbruikbare template (intake, voice-analyse, planning) | `_kennis/templates/` |
| Losse file binnengekomen, plek nog onduidelijk | `{{inbox_map}}/` |
{{#if overlay}}| Afgesloten project van de AI-laag | `{{projecten_map}}/_afgerond/` |
{{else}}| Afgesloten {{#if multi_instance}}{{instantie_enkelvoud}} of {{/if}}project | `_archief/` |
{{/if}}

---

## Memory-allocatie: waar regels en beslissingen heen gaan

Wanneer {{naam}} zegt "onthoud dit" of "remember this", volgt de AI deze tabel:

| Aard van de uitspraak | Locatie |
|---|---|
| Wie {{naam}} is als {{rol_label}}, principes, proces | `_kern/wie-ik-ben.md` |
| Werkregel die overal geldt (naming, flow, …) | `_kern/werkregels.md` |
| AI-anti-patroon dat voor élke output geldt | `_kern/anti-ai-stijl.md` (`_kern/schrijfregels-basis.md` blijft ongewijzigd) |
{{#if vertrouwelijkheid}}| Regel over wat nooit gedeeld of gelezen mag worden | `_kern/vertrouwelijkheid.md` |
{{/if}}| Feit of kennis (framework, theorie, procedure) | `_kennis/frameworks/` of `_kennis/templates/` |
| Stijl-, context- of strategie-regel voor {{wd_lidwoord}} eigen {{werkdomein_lower}} | `{{eigen_map}}/_voice.md`, `_context.md` of `_strategie.md` |
{{#if multi_instance}}| Context{{#if volledig}}-, stijl-{{/if}} of strategie-regel voor één {{instantie_enkelvoud}} | `{{instantie_map}}/[naam]/_context.md`{{#if volledig}}, `_voice.md`{{/if}} of `_strategie.md` |
{{/if}}| Status of planning van een lopend project | `project.md` binnen die projectmap |
{{#if overlay}}| Welk document de referentie is voor een taak | `_kennis/referentiedocumenten.md` |
| Wat een bestaande map bevat of wat Claude ermee mag | Tabel "Bestaande mappen" in deze file (na bevestiging van {{naam}}) |
{{/if}}
Regels:
1. Eén onderwerp, één thuis. Geen dubbele opslag tussen niveaus.
2. Het meest specifieke niveau wint bij conflict ({{#if multi_instance}}{{instantie_enkelvoud}} boven eigen werkdomein boven kern{{else}}werkdomein boven kern{{/if}}).
3. Bij twijfel: vragen aan {{naam}} waar het hoort, met een suggestie.

---

## Inbox-protocol

Wanneer iets in `{{inbox_map}}/` belandt: actief routeren, niet laten liggen.

{{#if vertrouwelijkheid}}**Eerst, vóór het lezen:** schat op basis van bestandsnaam en type in of het bestand gevoelige inhoud kan bevatten (persoonsgegevens, {{#if multi_instance}}{{instantie_enkelvoud}}informatie, {{/if}}financiële of medische data). Bij twijfel: vraag {{naam}} eerst wat het is en waar het hoort, en lees pas daarna. Zie `_kern/vertrouwelijkheid.md`.

{{/if}}**Stap 1: lezen en classificeren.** Bepaal het type (voorbeeld van output, contextdocument, asset, rapport, verslag, intake-antwoord, anders), voor wie het is (eigen {{werkdomein_lower}}{{#if multi_instance}}, een {{i_specifieke}} {{instantie_enkelvoud}}{{/if}}, of cross-cutting){{#if multi_instance}}, en indien voor een {{instantie_enkelvoud}}: welke. Hints: naam in de bestandsnaam, naam of URL in de inhoud, of {{naam}} die het in de chat zegt. Vergelijk met de submappen onder `{{instantie_map}}/`{{/if}}.

{{#if multi_instance}}**Stap 2: {{instantie_enkelvoud}}-context bepalen als die ontbreekt.** Geen match gevonden? Vraag: "Voor wie is dit: eigen {{werkdomein_lower}} of een {{i_specifieke}} {{instantie_enkelvoud}}?" Niet gokken. Bestaat {{i_die}} {{instantie_enkelvoud}} nog niet, vraag dan of er een nieuwe map moet komen (kopie van de template).

{{/if}}**Stap {{#if multi_instance}}3{{else}}2{{/if}}: subfolder bepalen.**

| Type | Voorgestelde plek |
|---|---|
| Voorbeeld van output die "écht hen" is | `_voorbeelden/[kanaal]/` van het werkdomein |
| Anti-voorbeeld | Sectie "Voorbeelden: niet" in `_voice.md`, of `_kern/anti-ai-stijl.md` indien algemeen |
| Contextdocument (positionering, huisstijlgids, stuk met achtergrond) | Update `_context.md` op basis van de inhoud en bewaar het brondocument in de root van het werkdomein |
| Strategie- of planningsdocument | Update `_strategie.md` en bewaar de bron |
{{#if overlay}}| Asset, rapport, analyse of verslag bij lopend werk | `{{projecten_map}}/[YYYY-MM-projectnaam]/`. Hoort het in een bestaande map, dan geldt de hardregel |{{else}}| Asset gekoppeld aan lopend werk | De passende recurring-map of `projecten/[naam]/` van het werkdomein |
| Rapport of analyse | De passende recurring-map van het werkdomein |
| Verslag of meeting-notes | `projecten/[naam]/` indien gekoppeld aan een project, anders nieuwe projectmap |{{/if}}
{{#if multi_instance}}| Intake-antwoorden van een {{i_nieuwe}} {{instantie_enkelvoud}} | Verwerken in `_context.md` en `_strategie.md` van die map |
{{/if}}| Framework of methodiek van algemene aard | `_kennis/frameworks/` |
| Onduidelijk type, duidelijk werkdomein | Root van dat werkdomein met de markering "te sorteren" |

Bij een voorbeeld: bepaal ook het kanaal. Onduidelijk? Vraag het.

**Stap {{#if multi_instance}}4{{else}}3{{/if}}: voorstellen en bevestigen.** Toon wat de file is, voor wie, welke plek je voorstelt (volledig pad) en welke bijkomende actie (bijvoorbeeld "ook `_voice.md` bijwerken met het patroon in deze tekst"). Wacht op bevestiging.

**Stap {{#if multi_instance}}5{{else}}4{{/if}}: verplaatsen, hernoemen, verwerken.** Verplaats, hernoem naar `YYYY-MM-DD-beschrijvende-naam.ext` als dat nog niet zo is, en doe een voorstel voor eventuele updates aan `_voice.md`, `_context.md` of `_strategie.md`. Tweede bevestiging vóór je die files aanpast.{{#if overlay}}{{#if bestaande_schrijven}} Hoort de file in een bestaande map, dan geldt de hardregel hierboven: nieuwe file na bevestiging, niets overschrijven.{{else}} Hoort de file in een bestaande map, dan zet {{naam}} ze daar zelf. Claude verplaatst enkel binnen de AI-laag.{{/if}}{{/if}}

Bij twijfel over de plek: maximum 2 opties voorleggen. Bulk-drops groeperen per type en in batch behandelen.

---

## Werkregels die overal gelden

- Bestandsnamen: `YYYY-MM-DD-beschrijvende-naam.ext`. Kleine letters, koppeltekens, geen spaties.{{#if overlay}} Dat geldt voor nieuwe files in de AI-laag. De namen in de bestaande mappen blijven zoals ze zijn.{{/if}}
- Niets overschrijven, hernoemen of verwijderen zonder eerst te tonen wat er verandert en bevestiging te krijgen.
- Niets buiten deze werkfolder wijzigen zonder expliciete vraag.
{{#if overlay}}- De bestaande mappen van {{naam}} volgen de hardregel bovenaan. Die gaat voor op elke andere regel.
- Werk-in-uitvoering en nieuwe output komen in `{{projecten_map}}/`.{{else}}- Werk-in-uitvoering komt in een `projecten/`-map, niet los tussen terugkerend werk.{{/if}}
{{#if heeft_offerte}}- Prijzen komen uitsluitend uit de tarieflijst in `{{eigen_map}}/_context.md`. Staat een prijs daar niet, vraag ze aan {{naam}}. Nooit een bedrag schatten of afronden in een offerte.
{{/if}}
---

## Versioning van kritieke files

**Krijgen versioning:** `_kern/*.md`, `CLAUDE.md`, `SETUP-STATUS.md`, en per werkdomein `_context.md`, `_voice.md`, `_strategie.md`.{{#if overlay}} Ook `_kennis/referentiedocumenten.md`.{{/if}}

**Krijgen geen versioning:** terugkerende content, LEESMIJ-files, project-files, files in `_voorbeelden/` (die zijn onveranderlijk eens toegevoegd), files in `{{inbox_map}}/`.

**Hoe:** vóór een kritieke file overschreven wordt bij een batch-update (meer dan 3 regels gewijzigd), bewaar de huidige versie als `[basename]-YYYY-MM-DD-HHMM.md` in een `_versies/`-submap naast de file{{#if overlay}} (voor files in de hoofdmap, zoals `CLAUDE.md` en `SETUP-STATUS.md`: in `_ai-setup/_versies/`, want in de hoofdmap komt niets bij){{/if}}. Maak die submap aan als ze nog niet bestaat. Meld in de bevestiging waar de vorige versie staat. Kleine inline-aanpassingen die {{naam}} live bevestigt, hoeven geen versie.

{{naam}} mag `_versies/`-mappen zelf opruimen. De AI raakt ze niet aan tenzij gevraagd.

---

{{#if sparring}}## Sparring-protocol

Wanneer {{naam}} wil sparren ("denk even mee", "wat zou jij doen", "ik wil sparren over"):

1. Laad enkel de context van het werkdomein waarover het gaat, plus passende frameworks uit `_kennis/frameworks/`.
2. Vat eerst de feiten uit die context samen. Benoem wat ontbreekt. Verzin niets.
3. Neem een standpunt in met redenering. Geef daarna het sterkste tegenargument en wanneer dat wint.
4. Na een beslissing van {{naam}}: log ze in `_strategie.md` van het werkdomein of in `project.md`, met datum en reden.

Volledige uitleg in `SETUP-START-HIER.md`, sectie "Sparren".

---

{{/if}}## Skills

Nog geen skills geconfigureerd. Komen later in het traject, wanneer de terugkerende taken duidelijk zijn.

---

*Aangemaakt op {{aangemaakt_op}} door {{coach}}.*
