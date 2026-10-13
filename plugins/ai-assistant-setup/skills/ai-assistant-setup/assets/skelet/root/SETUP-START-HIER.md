# Setup-guide: start hier

Welkom in je Cowork-omgeving, {{naam}}. Dit document begeleidt je stap voor stap doorheen het instellen van je werkruimte. Aan het einde staat alles klaar om er écht mee te werken.

---

## Hoe je dit start

Dit document lees je niet zelf, Claude leest het. Wat jij doet:

> **Open Cowork en typ: `SETUP`**

Vanaf dat moment neemt Claude de leiding. Hij stelt je vragen één voor één, wacht op je antwoord, en vult ondertussen de juiste files aan. Jij hoeft alleen te antwoorden. Geen markdown, geen files openen, geen mappen zoeken.

Kom je later terug en typ je opnieuw `SETUP`, dan herkent Claude waar je gebleven was (via `SETUP-STATUS.md`) en stelt hij voor om vanaf daar verder te gaan.

{{#if overlay}}Deze omgeving staat naast je bestaande mappen. Die blijven zoals ze zijn: Claude leest erin, maar verandert er niets aan. Een deel van de files is al voorgevuld op basis van je mappenstructuur en ons gesprek. Die stukken staan gemarkeerd als voorstel. Je loopt ze samen met Claude door: bevestigen, aanpassen of weggooien.{{else}}Een deel van de files is al voorgevuld op basis van {{bron_je}}. Die stukken staan gemarkeerd als voorstel. Tijdens Fase A loop je ze samen met Claude door: bevestigen, aanpassen of weggooien.{{/if}}

---

## Materiaal aanleveren tijdens de setup

Naast je antwoorden kan je ook bestaand materiaal aanleveren: website, documenten, {{eerste_kanaal_meervoud_lower}}, {{#if materiaal.brand_book}}je brand book, {{/if}}screenshots. Claude leest die en doet voorstellen. Dat versnelt vooral het zware werk: stem-analyse, feiten destilleren, bestaande output per kanaal in kaart brengen.

**Hoe je materiaal aanlevert:** {{#if overlay}}staat het al in je mappen, wijs dan gewoon aan waar. Claude leest het daar en laat het origineel staan. Andere documenten{{else}}documenten{{/if}} in `{{inbox_map}}/` droppen, URLs gewoon in het gesprek plakken, screenshots in het gesprek of in de inbox.

**Wat Claude er wel en niet mee doet.** Er zijn drie soorten vragen:

1. **Identiteitsvragen** (wie ben je, welke principes, wat weiger je). Die formuleer jij zelf. Claude gebruikt het materiaal hooguit als geheugensteun, niet om het antwoord voor te stellen. Dit zijn keuzes, geen feiten, en als AI ze invult voelen ze niet als de jouwe.
2. **Feitenvragen** (wat doe je, voor wie, wat maakt je anders). Claude mag voorstellen doen uit materiaal. Jij bevestigt.
3. **Stem- en voorbeeldwerk.** Claude doet hier de analyse uit materiaal. Zonder materiaal werkt dit niet goed.

**Wat Claude altijd checkt:** is het materiaal nog actueel? Een rebrand die bezig is of een oude stem die je achter je liet, moet eruit voor we erop bouwen.

**Bronvermelding:** elke file die op basis van materiaal gevuld wordt, krijgt onderaan een regel: "Voorgesteld op [datum] op basis van [bron]. Bevestigd door {{naam}}."

**Handig om bij de hand te hebben:**
- Fase A: {{#if materiaal.website_url}}je website ({{materiaal.website_url}}){{else}}je website-URL{{/if}}{{#if materiaal.linkedin_url}}, je LinkedIn ({{materiaal.linkedin_url}}){{else}}, je LinkedIn-profiel{{/if}}.
- Fase B: 10 tot 15 voorbeelden van eigen output waar je trots op bent, per kanaal gesorteerd als dat lukt{{#if materiaal.brand_book}}, plus je brand book{{/if}}.
{{#if multi_instance}}- Fase C: van één {{instantie_enkelvoud}}: {{#if volledig}}website of profiel, 10 tot 15 goede voorbeelden van wat je voor hen maakte, en de context die je hebt{{else}}de context die je hebt en 2 of 3 voorbeelden van wat je voor hen maakte{{/if}}.
{{/if}}
---

## De fasen

| Fase | Inhoud | Tijd | Wanneer |
|---|---|---|---|
{{#if overlay}}| 0 | Je mappen leren kennen: wat staat waar, welk document is het voorbeeld, welke regels staan nergens | 30 tot 45 min | Eerst, samen met {{coach_voornaam}} |
{{/if}}| A | Basis: wie je bent, wat je {{werkdomein_lower}} doet, anti-AI-ergernissen | 15 tot 30 min | Eerst |
| B | Eigen {{werkdomein_lower}} verdiepen: stem, strategie, voorbeelden | 30 tot 60 min | Tweede sessie of dezelfde dag |
{{#if multi_instance}}| C | Eerste {{instantie_enkelvoud}} in het systeem | 60 tot 90 min | Wanneer je er klaar voor bent |
| D | Routine voor {{i_elke}} {{i_nieuwe}} {{instantie_enkelvoud}} (geen guide meer nodig) | 30 min per {{instantie_enkelvoud}} | Telkens |
{{/if}}
Je hoeft ze niet na elkaar te doen. Pauzeer wanneer je wil.

---

## Voor Claude: algemene gespreksinstructies

({{naam}}: deze sectie is voor Claude.)

Wanneer {{naam}} `SETUP` typt (of een variant):

1. **Detecteer waar {{naam}} staat** via `SETUP-STATUS.md`. Stel voor om bij {{#if overlay}}Fase 0{{else}}Fase A{{/if}} te starten of verder te gaan vanaf de eerste niet-afgewerkte fase. Bevestig vóór je begint.

2. **Neem de leiding.** Vragen één voor één. Vraag, wacht, bevestig kort, volgende vraag. Rustig tempo, dit is een coachingmoment.

3. **Bevestig per antwoord welke file je gaat bijwerken**, zodat {{naam}} weet wat er achter de schermen gebeurt. Schrijf niet na elk antwoord. Verzamel binnen een fase eerst alles.

4. **Voorgevulde velden:** toon ze één voor één en vraag: klopt dit, wil je het aanpassen, of weg ermee? Verwijder daarna de voorstel-markering. Een bevestigd voorstel wordt gewoon tekst.

5. **Aan het einde van elke fase:** schrijf alle betrokken files in één keer (met versioning volgens `CLAUDE.md` als de file al inhoud had), toon wat er nieuw of anders is, en vraag: doorgaan of pauzeren? Werk daarna `SETUP-STATUS.md` bij: checkboxes, status, datum, logregel.

6. **Bij onduidelijke antwoorden:** doorvragen. Niet zelf invullen. Een lege placeholder is beter dan iets verzonnen.

7. **Bij vermoeidheid of weerstand:** stel voor om te pauzeren. Beter een halve setup vandaag en de rest morgen dan een fase die nooit afkomt.

8. **Tijdens de setup geen andere taken aannemen.** Vraagt {{naam}} halverwege iets anders, bevestig dan dat je dat na de huidige stap doet, of vraag of de setup even op pauze mag.

9. **Materiaal per soort vraag:** identiteitsvragen → {{naam}} antwoordt zelf, geen voorstellen uit materiaal. Feitenvragen → voorstel mag ("op basis van [bron] denk ik X, klopt dat?"). Stem en voorbeelden → werk uit materiaal, {{naam}} stuurt bij.

10. **Actualiteitscheck bij elk stuk materiaal:** vraag één keer of het nog beschrijft waar {{naam}} nu staat.

11. **Bronvermelding** onderaan elke file die uit materiaal gevuld is:
    ```
    ---
    *Voorgesteld op [YYYY-MM-DD] op basis van [bron]. Bevestigd door {{naam}}.*
    ```

12. **Materiaal in `{{inbox_map}}/`** verwerk je volgens het inbox-protocol in `CLAUDE.md`. Tijdens de setup is de context meestal duidelijk uit de fase waarin je zit.
{{#if overlay}}
13. **De bestaande mappen blijven onaangeroerd,** ook tijdens de setup. Lees erin wanneer het helpt, en enkel wat de tabel "Bestaande mappen" in `CLAUDE.md` toelaat. Wat je eruit gebruikt (een voorbeeld, een feit), neem je over in de AI-laag. Het origineel blijft waar het staat.

14. **Bouw verder op de analyse.** Staat er een `_ai-setup/analyse.md`, dan las Claude bij de start (INIT) een selectie documenten. Punten met `status: open` overloop je in Fase 0. Wat als bevestigd of aangepast staat, is al weggeschreven: vraag het niet opnieuw.
{{/if}}
---

{{#if overlay}}# Fase 0: je mappen leren kennen (30 tot 45 min)

**Doel:** Claude weet wat er in je mappen staat, welk document voor welke taak het voorbeeld is, en welke regels je toepast zonder dat ze ergens opgeschreven staan. Je mappen zelf veranderen niet.

**Files:** `_ai-setup/analyse.md`, `CLAUDE.md` (tabel "Bestaande mappen"), `_kennis/referentiedocumenten.md`, `_kern/werkregels.md` (sectie "Beslisregels"), `_kern/wie-ik-ben.md` (enkel feiten), `{{eigen_map}}/_context.md`{{#if vertrouwelijkheid}}, `_kern/vertrouwelijkheid.md`{{/if}}.

## Eerst: wat Claude in je documenten vond

Bij de start (INIT) las Claude een selectie van je documenten. Wat hij vond, staat in `_ai-setup/analyse.md`. Niets daarvan staat al in je assistent: jij beslist wat erin komt.

**Instructie aan Claude:** bestaat `_ai-setup/analyse.md` niet, of staat er geen enkel punt meer op `status: open`, sla dit deel dan over. Anders: overloop de punten met `status: open`, per sectie en in deze volgorde:

1. **Beste voorbeeld per taak** → `_kennis/referentiedocumenten.md`, één rij per taak.
2. **Werkregels** → sectie "Beslisregels" in `_kern/werkregels.md`. Daar horen ook vaste opbouw en notaties bij (hoe een verslag is opgebouwd, hoe bedragen geschreven worden). Enkel een ergernis over AI-taal gaat naar `_kern/anti-ai-stijl.md` onder "Eigen ergernissen".
3. **Feiten over het bedrijf** → `{{eigen_map}}/_context.md`. Niet in `_kern/wie-ik-ben.md`: die file gaat over {{naam}} zelf, en die vult {{naam}} in Fase A in eigen woorden in.
4. **Vragen** → stel ze één voor één. Het antwoord gaat naar de file waar het onderwerp hoort, meestal "Beslisregels".

Toon een sectie als korte genummerde lijst, met de bron per punt, en vraag per punt: klopt dit, aanpassen, of weg ermee? Schrijf pas na het akkoord. Hier schrijf je per sectie, niet per fase (uitzondering op regel 3): zo staat wat {{naam}} bevestigde meteen vast, ook als ze halverwege stopt. Landen 2 secties in dezelfde file, schrijf die file dan één keer, na de laatste van de 2.

Zet bij elk weggeschreven punt de bron op dezelfde regel, zodat je per regel ziet waar ze vandaan komt: `(bron: [bestand], bevestigd [YYYY-MM-DD])`.

Zet daarna in `analyse.md` per punt de status: `bevestigd`, `aangepast` of `geschrapt`, en bij een vraag `beantwoord`, met het antwoord en de file waar het naartoe ging. Stopt {{naam}} halverwege, dan blijven de rest `open` en neem je ze de volgende keer eerst.

## Daarna: de mappen overlopen

**Instructie aan Claude:** de tabel "Bestaande mappen" in `CLAUDE.md` werd bij de start al samen bekeken. Toon ze kort en vraag enkel of er iets mist of niet klopt. Sla elke vraag hieronder over die al beantwoord is in de punten die {{naam}} net bevestigde. Was de tabel bij de start niet besproken, loop dan de tabel "Bestaande mappen" in `CLAUDE.md` samen met {{naam}} door, map per map. Toon de beschrijving en wat Claude ermee mag, en vraag: klopt dit? Om een beschrijving scherper te maken mag je de namen van submappen en files bekijken. De inhoud van een file open je pas als {{naam}} dat goedvindt. Mappen met rol `buiten_bereik` open je niet, ook niet om namen te bekijken. Staat er een map in de hoofdmap die niet in de tabel staat, vraag dan wat erin zit en welke rol ze krijgt.

## Vragen

1. Welke taken wil je als eerste door Claude laten doen? Noem er 3 tot 5.{{#if pijnpunten}} (Uit ons gesprek: {{#each pijnpunten}}{{this}}{{sep}}{{/each}}. Klopt dat nog?){{/if}}
2. Per taak: welk document is het beste voorbeeld van hoe het moet? Waar staat het, en wat maakt het goed?
3. Welke regels pas je toe die nergens opgeschreven staan? Denk aan: welke versie van een document geldt, wanneer iets naar een collega of klant gaat, wat je altijd nog controleert.
4. Welke correcties doe je telkens opnieuw op teksten van AI of van anderen?
5. Welk systeem is de bron voor welke gegevens? Denk aan je boekhoudpakket, planning, CRM of mailbox.
6. Welke mappen of {{#if multi_instance}}{{instantie_meervoud_lower}}{{else}}klanten{{/if}} blijven buiten bereik, ook om enkel te lezen?
{{#if multi_instance}}{{#if instanties_start_obj}}7. In Fase C starten we met {{#each instanties_start_obj}}{{naam}}{{sep}}{{/each}}. Klopt dat nog?{{else}}7. Met w{{i_elke}} {{instantie_enkelvoud}} starten we in Fase C? Tip: kies {{instantie_lidwoord}} {{instantie_enkelvoud}} met het meeste recente werk in de map.{{/if}}
{{/if}}
**Instructie aan Claude:** de overlopen tabel → `CLAUDE.md` (versioning volgens de regels daar, toon wat er verandert). Vraag 1 en 2 → `_kennis/referentiedocumenten.md`, één rij per taak. Vraag 3 → sectie "Beslisregels" in `_kern/werkregels.md`. Vraag 4 → correcties over schrijfstijl naar `_kern/anti-ai-stijl.md` onder "Eigen ergernissen", correcties over inhoud naar "Beslisregels". Vraag 5 → sectie "Bronsystemen" in `{{eigen_map}}/_context.md`. Vraag 6 → rol `buiten_bereik` in de tabel in `CLAUDE.md` en de lijst in `_kern/werkregels.md`.{{#if multi_instance}} Vraag 7 → noteer in `SETUP-STATUS.md` bij Fase C.{{/if}}

**Einde Fase 0:** toon de bijgewerkte tabel en `_kennis/referentiedocumenten.md`. Vraag bevestiging, stel Fase A voor of pauze.

---

{{/if}}# Fase A: basis (15 tot 30 min)

**Doel:** Claude kent jou als {{rol_label}}, weet wat je {{werkdomein_lower}} doet en welke AI-ergernissen hij moet vermijden. Na deze fase kan je Claude beginnen gebruiken. Het wordt beter met elke volgende fase.

**Files:** `_kern/wie-ik-ben.md`, `_kern/anti-ai-stijl.md` (aanvullen op de defaults), `{{eigen_map}}/_context.md` (basis){{#if vertrouwelijkheid}}, `_kern/vertrouwelijkheid.md` (controleren){{/if}}.

## Vragen

**Over jou als {{rol_label}}** (jij formuleert, geen voorstellen uit materiaal)

1. Hoe zou je jezelf beschrijven als {{rol_label}}, in één zin? Wat onderscheidt je van anderen die hetzelfde doen?
2. Hoe ben je hierin terechtgekomen? Kort, 3 tot 5 zinnen.
3. Welke 3 tot 5 principes hanteer je in je werk? Concreet: "ik geloof in X want Y."
4. Welke 3 tot 5 dingen weiger je, ook als iemand erom vraagt?
5. Welk proces doorloop je standaard bij {{#if multi_instance}}een {{i_nieuwe}} {{instantie_enkelvoud}}{{else}}een nieuwe opdracht{{/if}}? Stap voor stap.
6. Waar ben je écht goed in? 3 tot 5 dingen.

**Over je {{werkdomein_lower}}** (voorstellen uit materiaal en kickoff mogen)

7. Wat doet je {{werkdomein_lower}} in één zin?
8. Welke diensten of producten lever je? Top 3.
9. Wie is je ideale {{#if multi_instance}}{{persoon}}{{else}}klant{{/if}}? 5 zinnen: wie, situatie, probleem, wat maakt dat ze jou bellen.
10. Wat zijn je 3 belangrijkste sterktes tegenover anderen? Concreet, geen "kwaliteit".
11. Waar sta je in de markt: premium of toegankelijk, specialist of generalist?
12. Sinds wanneer bestaat het? Alleen of met anderen?

**Anti-AI-stijl** (jouw input)

13. Welke openingszinnen van AI wil je nooit meer zien? Minstens 3.
14. Welke woorden of frasen mag AI nooit meer gebruiken voor jou, naast wat er al in `_kern/anti-ai-stijl.md` staat?
15. Welke zinsbouwen herken je meteen als AI?

{{#if vertrouwelijkheid}}**Vertrouwelijkheid** (controleren)

16. Loop `_kern/vertrouwelijkheid.md` samen door. Klopt wat er staat? Ontbreekt er iets dat in jouw vak vanzelfsprekend is?

{{/if}}**Instructie aan Claude:** vragen 1 tot 6 → `_kern/wie-ik-ben.md`. Vragen 7 tot 12 → `{{eigen_map}}/_context.md`. Vragen 13 tot 15 → toevoegen aan `_kern/anti-ai-stijl.md` onder "Eigen ergernissen", de defaults blijven staan.{{#if vertrouwelijkheid}} Vraag 16 → `_kern/vertrouwelijkheid.md`.{{/if}}

**Einde Fase A:** toon de ingevulde files, vraag bevestiging, stel Fase B voor of pauze.

---

# Fase B: eigen {{werkdomein_lower}} verdiepen (30 tot 60 min)

**Doel:** je eigen {{werkdomein_lower}} heeft een werkende stem, een uitgesproken strategie en een eerste voorbeeldenpool per kanaal. Na deze fase kan je output voor jezelf laten maken die écht klinkt als jij.

**Files:** `{{eigen_map}}/_voice.md`, `{{eigen_map}}/_strategie.md`, `{{eigen_map}}/_voorbeelden/[kanaal]/` (voor 2 of 3 kanalen om te starten){{#if content_kalender}}, `{{eigen_map}}/content-kalender.md`{{/if}}.

{{#if fase_proces}}**Bij jou ligt de nadruk op proces.** Begin deze fase daarom met het documenttype dat je het meeste tijd kost{{#if pijnpunt_1}} ({{pijnpunt_1}}){{/if}}: register, structuur, voorbeelden en één echte test. De bredere stem komt daarna. Claude splitst Fase B dan in twee delen en werkt `SETUP-STATUS.md` per deel bij.

{{/if}}**Voorbereiding:** verzamel 10 tot 15 voorbeelden van eigen output waarvan je zegt "dit ben ik". En 2 of 3 anti-voorbeelden: typische AI-output die je afkeurt. {{#if overlay}}Staan ze in je mappen, dan wijs je gewoon aan waar. Claude neemt de tekst over in `_voorbeelden/`, het origineel blijft staan. Andere voorbeelden drop je in `{{inbox_map}}/`.{{else}}Drop ze in `{{inbox_map}}/` of houd ze bij de hand.{{/if}}

## Vragen

**Strategie** (voorstellen uit materiaal mogen)

1. Wat is je focus voor dit jaar? Welk hoofddoel?
2. Voor wie ga je dit jaar het hardst werken? Een niche, een sector, een type {{#if multi_instance}}{{persoon}}{{else}}klant{{/if}}?
3. Vul aan: "Voor [doelgroep] die [probleem] hebben, bied ik [oplossing] omdat [wat mij anders maakt]."
4. Welke 3 tot 5 thema's komen in al je communicatie terug?
5. Op welke kanalen ben je actief en hoe vaak?
6. Welke meetbare doelen wil je dit kwartaal halen?

**Stem** (Claude analyseert uit materiaal)

7. Geef me je 10 tot 15 voorbeelden, per kanaal gesorteerd als het lukt.
8. Geef me 2 of 3 anti-voorbeelden.

**Instructie aan Claude voor de stem-analyse:** volg `_kennis/templates/voice-analyse-protocol.md`. Identificeer ritme, woordkeuze, openingen, afsluitingen, signature-moves. Schrijf 8 tot 15 concrete regels (geen "informeel" of "menselijk"). Destilleer verboden uit de anti-voorbeelden. Vul `{{eigen_map}}/_voice.md`. Verdeel de voorbeelden per kanaal over `{{eigen_map}}/_voorbeelden/[kanaal]/`, één file per voorbeeld, naam `YYYY-MM-DD-beschrijving.md`, met datum en "waarom dit een goed voorbeeld is" bovenaan.{{#if voice_laag}} Bij deze setup ligt de nadruk op register en structuur eerder dan op persoonlijkheid: beschrijf hoe {{test_kanaal_enkelvoud}} van {{naam}} opgebouwd is en klinkt, niet een merkstem.{{/if}}

**Test**

9. Vraag Claude {{test_kanaal_enkelvoud}} voor je {{werkdomein_lower}} te schrijven over een onderwerp dat hij zelf kiest. Lees kritisch. Wat voelt nog "AI"?
10. Voeg op basis daarvan regels of verboden toe aan `_voice.md`, of een sterker voorbeeld aan `_voorbeelden/`. Test opnieuw. 3 tot 5 rondes.

**Einde Fase B:** je hebt een werkende stem voor je eigen {{werkdomein_lower}}, getest op minstens één kanaal. Vraag bevestiging, stel {{#if multi_instance}}Fase C{{else}}een eerste echte taak{{/if}} voor of pauze.

{{#if multi_instance}}---

# Fase C: eerste {{instantie_enkelvoud}} in het systeem (60 tot 90 min)

**Doel:** één {{instantie_enkelvoud}} volledig in het systeem, zodat je het herhaalproces hebt doorleefd voor je het op meer {{instantie_meervoud_lower}} loslaat.

**Files:** `{{instantie_map}}/[naam]/` als kopie van `_template-{{i_nieuwe}}-{{instantie_slug}}/`, met `_context.md`{{#if volledig}}, `_voice.md`{{/if}}, `_strategie.md`{{#if volledig}} en voorbeelden per kanaal{{/if}}.

## Vragen

1. W{{i_elke}} {{instantie_enkelvoud}} kies je als eerste? Tip: niet de moeilijkste. Kies degene die je het best kent en waarvan je het meeste materiaal hebt.

**Instructie aan Claude:**

1. Kopieer `{{instantie_map}}/_template-{{i_nieuwe}}-{{instantie_slug}}/` naar `{{instantie_map}}/[naam]/`. Bevestig de mapnaam met {{naam}} (kleine letters, koppeltekens).{{#if overlay}} Staat de map er al (klaargezet bij de opbouw), gebruik die.{{#if instanties_pad}} Bekijk daarna `{{instanties_pad}}/[naam]/`: eerst de namen van submappen en files, dan enkel de inhoud die {{naam}} aanwijst. Vul de regel "Werkmap" bovenaan `_context.md` in met dat pad. Aan die map zelf verandert niets.{{/if}}{{/if}}
2. Doorloop de intake-vragenlijst uit `_kennis/templates/intake-vragenlijst-{{instantie_slug}}.md` in segmenten, niet in één keer.
3. Vul `_context.md` en `_strategie.md` van de nieuwe map.
{{#if volledig}}4. Vraag voorbeelden per kanaal. Verdeel ze over `_voorbeelden/[kanaal]/` zoals in Fase B.
5. Doe een stem-analyse op die voorbeelden en vul `_voice.md` van de {{instantie_enkelvoud}}.
6. Test: schrijf één stuk output voor {{i_deze}} {{instantie_enkelvoud}} op één kanaal. Itereer tot het zit.
{{else}}4. Test: schrijf één stuk output voor {{i_deze}} {{instantie_enkelvoud}}. De stem komt uit `{{eigen_map}}/_voice.md`, de feiten uit de nieuwe `_context.md`. Itereer tot het zit.
{{/if}}
**Einde Fase C:** {{instantie_enkelvoud}} 1 staat klaar. Vraag {{naam}} om de eerstvolgende week al het werk voor {{i_deze}} {{instantie_enkelvoud}} via Cowork te doen, als test in de echte wereld.

---

# Fase D: {{i_nieuwe}} {{instantie_enkelvoud}} erbij (routine, 30 min)

Geen begeleiding meer nodig. Het patroon:

1. Kopieer `{{instantie_map}}/_template-{{i_nieuwe}}-{{instantie_slug}}/` naar `{{instantie_map}}/[naam]/`.{{#if overlay}}{{#if instanties_pad}} Vul bovenaan `_context.md` de werkmap in: `{{instanties_pad}}/[naam]/`.{{/if}}{{/if}}
2. Laat de intake-vragenlijst beantwoorden, in een gesprek of schriftelijk.
3. Plak de antwoorden in een gesprek met Claude: "doorloop dit en vul de map van [naam] aan."
4. Claude vult `_context.md`{{#if volledig}}, `_voice.md`{{/if}} en `_strategie.md`{{#if volledig}}, en sorteert voorbeelden per kanaal{{/if}}.
5. Test en itereer.

{{/if}}{{#if sparring}}---

# Sparren: strategie en moeilijke beslissingen

Je gaf aan dat je Claude ook wil gebruiken om te sparren. Daarvoor geldt een vast patroon, zodat het sparren iets oplevert en niet uitloopt op vage bevestiging van wat je al dacht.

**Hoe je start:** zeg "ik wil sparren over [onderwerp] voor [eigen werk{{#if multi_instance}} of {{instantie_enkelvoud}} X{{/if}}]". Claude laadt dan enkel de context van dat werkdomein en de frameworks uit `_kennis/frameworks/` die passen.

**Wat Claude dan doet:**
1. Eerst de feiten samenvatten uit de context, zodat je ziet waarop hij redeneert. Wat ontbreekt, benoemt hij als ontbrekend. Niets verzinnen.
2. Dan een standpunt innemen met redenering. Geen "aan de ene kant, aan de andere kant".
3. Dan het sterkste tegenargument geven, en zeggen in welk geval dat tegenargument wint.
4. Wanneer jij beslist: de beslissing loggen in `_strategie.md` van het werkdomein (of in `project.md` bij een project), met datum en reden.

**Waarvoor je dit vooral wil gebruiken (uit je kickoff):**
{{#if sparring_beslissingen}}{{#each sparring_beslissingen}}- {{this}}
{{/each}}{{else}}- [Vul aan tijdens Fase B: de beslissingen waarvoor je Claude als sparringpartner wil.]
{{/if}}
**Instructie aan Claude:** dit patroon geldt telkens {{naam}} "sparren", "denk even mee" of "wat zou jij doen" zegt. Stap 1 mag je niet overslaan, ook niet als het gesprek al bezig is.

{{/if}}---

## Wanneer je vastloopt

- **Weet je niet wat te antwoorden?** Sla over. Een lege placeholder is geen probleem.
- **Voelt de stem nog niet goed?** Meer voorbeelden in `_voorbeelden/[kanaal]/` werkt beter dan meer regels in `_voice.md`. AI leert beter van patronen dan van abstracties.
- **Wil je iets veranderen aan de structuur?** Vraag Claude. Niet zelf manueel beginnen verschuiven, dan loopt het systeem uit elkaar.
- **Wil je terug naar een vorige versie?** Kijk in de `_versies/`-map naast de file.

---

## Wat na de setup?

Vanaf dan is het simpel. Voor je eigen {{werkdomein_lower}}: "schrijf X voor mezelf". {{#if multi_instance}}Voor een {{instantie_enkelvoud}}: "schrijf X voor [naam] op kanaal Y". {{/if}}Claude laadt de juiste context, stem en voorbeelden. En je kan altijd zeggen: "de output voor X zit nog niet goed, wat passen we aan?" Claude denkt mee.

---

*Aangemaakt op {{aangemaakt_op}} door {{coach}}. Dit document blijft staan. Je kan altijd terugkomen om een fase opnieuw te doen.*
