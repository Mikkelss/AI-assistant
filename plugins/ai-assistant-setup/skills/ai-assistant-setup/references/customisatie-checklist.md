# Customisatie-checklist: na het script, vóór de oplevering

Het script `build_skeleton.py` levert een correct en compleet skelet, maar generiek waar het niet anders kan. Deze checklist is het slimme deel dat jij daarna doet. Werk ze in volgorde af. Elke stap zegt welke file, wat je controleert of aanpast, en waarom het ertoe doet.

Schrijf alle tekst die de klant leest in de stijl van Michiel: Vlaams-informeel, jij-vorm, geen em-dashes, geen "niet X maar Y"-constructies, korte alinea's. De klant leest dit als een tekst van Michiel, niet van een tool.

**Modus bestaande map** (`overlay: true`): doe deze checklist, plus de zes extra punten in stap F van `references/bestaande-map.md`. Waar een stap hieronder over recurring-mappen of projecten per klant gaat, sla je hem over.

---

## 1. `CLAUDE.md`: routing-tabel in de taal van de sector

Open de routing-tabel. Het script vulde de rijen met de config-waarden, maar de voorbeelden in de linkerkolom zijn generiek ("content of analyse voor een klant"). Herschrijf ze naar wat deze klant écht doet. Voor een advocaat: "conclusie of dagvaarding voor een dossier", "brief aan een cliënt", "advies voor een nieuwe zaak". Voor een coach: "sessieverslag voor een cliënt", "opvolgmail na een sessie". Twee of drie rijen aanpassen volstaat; de structuur klopt al.

Controleer daarna het voice-protocol. Als blok 3 vraag 16 aangaf dat bepaalde kanalen een sterk afwijkend register hebben, voeg dan één zin toe die dat benoemt ("een pleitnota volgt een ander register dan een mail aan de cliënt: laad bij een pleitnota ook `_kennis/templates/register-pleitnota.md` als dat bestaat").

## 2. `SETUP-START-HIER.md`: vragen in de woorden van de klant

De vragen in Fase A, B en C zijn geparametriseerd met de rol en de instantie-naam, maar de voorbeelden tussen haakjes zijn generiek. Loop elke fase door en vervang generieke voorbeelden door sectorvoorbeelden. Waar staat "bijvoorbeeld: expertise tonen, achter de schermen" moet voor een advocaat staan "bijvoorbeeld: rechtspraak duiden, praktische tips voor ondernemers". Gebruik de kickoff-antwoorden als bron voor de voorbeelden waar dat kan.

Controleer ook de "handig materiaal"-lijstjes per fase tegen blok 10. Staat er "brand book" terwijl de klant er geen heeft, haal het weg. Heeft de klant een website, zet die URL er letterlijk in.

Bij `voice_gewicht` "laag": kort Fase B in. De voice-analyse blijft, maar met de nadruk op register en verslagstijl, niet op merkstem. Bij "hoog": laat Fase B zoals ze is en overweeg in het trajectplan een aparte sessie voor de voice-analyse.

## 3. `_kern/anti-ai-stijl.md`: de ergernissen van de klant bovenaan

Het script zette `prefill.anti_ai` bovenaan onder "Eigen ergernissen". Controleer dat ze er staan en dat de formulering concreet is. "Te formeel" is geen bruikbare regel; "geen 'geachte' in mails aan bestaande klanten" wel. Herformuleren mag, zonder VOORSTEL-markering: het zijn de woorden van de klant, jij maakt ze enkel scherper. Voeg per ergernis een alternatief toe waar dat kan ("in plaats van X: Y").

## 4. `_kennis/templates/`: intake en planningsinstrument aangepast aan het instantie-type

De intake-vragenlijst voor nieuwe instanties is geschreven voor "klant" als default. Bij een ander instantie-type herschrijf je de vragen die niet passen, in deze volgorde en met ongeveer dit aantal:

- **Dossier (advocaat, notaris):** gevoeligheden eerst (minderjarigen, geweld, medisch), partijen en hun rol, feiten en wat betwist wordt, rechtsvraag, gewenste uitkomst en spoor (bemiddeling of procedure), termijnen, wat de cliënt al weet en wil, afspraken over communicatie. Zo'n 15 tot 20 vragen.
- **Cliënt (coach, therapeut):** aanleiding en wie stuurde, doelen op korte en lange termijn, context (werk, team, thuis voor zover relevant), eerdere trajecten, wat werkt en wat niet bij deze persoon, afspraken met de opdrachtgever als die er is, praktisch. 12 tot 15 vragen.
- **Opdracht (consultant, architect):** opdrachtgever en stakeholders, vraag en scope, wat buiten scope valt, beslissers, deadlines en mijlpalen, beschikbare documenten, gevoeligheden (NDA, interne politiek). 12 tot 15 vragen.
- **Klant als merk (marketing, copy):** de bestaande vragenlijst volstaat.

Het planningsinstrument hangt aan het instantie-type, los van of er een content-kalender is. Een coach heeft een content-kalender (LinkedIn) én een trajectplanning per cliënt nodig. Maak dus per type: termijnenoverzicht (dossier), trajectplanning en sessieverslag-structuur (cliënt), mijlpalenplan (opdracht), shoot- of opdrachtfiche (eenmalige opdrachten). Als `_kennis/templates/[naam]-template.md`, in dezelfde stijl als de andere templates, met een verwijzing in `_strategie.md` van de instantie-template. Bij een termijnenoverzicht hoort ook een regel in `CLAUDE.md`: Claude berekent geen termijnen en zet geen datum in een tekst die niet in die tabel staat.

## 5. `_kennis/frameworks/`: stubs aanvullen

Het script maakte voor elke naam in `frameworks_start` al een stub `[slug].md` met de vaste structuur (wat is het, wanneer gebruik ik het, de stappen, voorbeelden, bronnen), allemaal met "[Vul aan]". Vul de secties in die je met zekerheid kent uit de kickoff-antwoorden of uit algemene kennis over het framework (GROW, SWOT, StoryBrand en dergelijke zijn bekend genoeg). De rest laat je staan. Zo moet de klant tijdens Fase B enkel aanvullen, niet vanaf nul beginnen.

## 6. `_kern/vertrouwelijkheid.md`: regels concreet maken

Alleen bij `vertrouwelijkheid` `true`. Het script zette de regels uit `vertrouwelijkheid_regels` erin plus een set defaults. Controleer dat de defaults passen bij de sector (een advocaat heeft andere defaults dan een coach) en dat de regels van de klant bovenaan staan. Voeg toe wat de sector vereist en wat de klant vergat: beroepsgeheim, bewaartermijnen, wat er gebeurt bij een datalek. Houd het op één pagina.

## 7. Trajectplan schrijven

In `_ai-setup/` van de doelmap: `[datum]-trajectplan-[voornaam].md`. Gebruik het patroon uit Kiara's trajectplan als vorm: per sessie doel, wat we tijdens de sessie doen, huiswerk, wat de klant meeneemt. Pas aan op:

- `fase_nadruk`: bij "strategie" de sparring-sessie vóór skills, bij "proces" skills vroeger en Fase B gesplitst (eerst het documenttype dat pijn doet, dan de stem), bij "voice" een aparte voice-sessie.
- Sessiedata: stel concrete data voor op de weekdag uit blok 9, gemarkeerd als voorstel, vertrekkend van vandaag, en controleer ze tegen `blokkades` en de Vlaamse schoolvakanties (herfst: week van 1 november; kerst: 2 weken rond nieuwjaar; krokus: eind februari; paas: 2 weken in april; zomer: juli en augustus). Gebruik `references/trajectplan-skelet.md` als vorm.
- `tijd_per_week`: minder dan 2 uur → sessies om de 2 weken en kleiner huiswerk.
- `blokkades`: plan zo dat er vóór een lange pauze iets werkends staat.
- `multi_instance` `false`: schrap Fase C uit het traject; de tijd gaat naar diepere uitwerking van het eigen werkdomein en vroegere skills.
- Blok 8 vraag 35 (wat eerder stilviel): benoem het risico en zet een tegenmaatregel in het plan.

## 8. Ontwerpnotitie schrijven

Naast het trajectplan, in `_ai-setup/`: `[datum]-ontwerpnotitie-[voornaam].md`. Dit is het document waarin Michiel en de klant later terugvinden wat er gekozen is. Structuur:

```
# Ontwerpnotitie: Cowork-setup voor [naam]

## Samenvatting van de keuzes
Tabel: parameter, gekozen waarde, reden (verwijs naar het principe of het kickoff-antwoord).

## Afwijkingen van de standaard
Wat anders is dan het Kiara-patroon en waarom.

## Wat voorgevuld is
Lijst van files met voorgevulde inhoud. Alles staat gemarkeerd als voorstel.

## Wat bewust leeg gelaten is
De identiteitsvragen, met wat de klant erover zei als geheugensteun voor de sessie.

## Aandachtspunten voor de eerste sessie
Risico's uit blok 8, multi-user-waarschuwing, meertaligheid, stakeholders per instantie, waar de map fysiek komt (lokaal met kopie, niet rechtstreeks in een cloud-map). Bij `vertrouwelijkheid` true altijd: wat gebeurt er met de data (voorwaarden van het Claude-plan, training op data, verwerkersovereenkomst, sectorregels). Een advocaat, boekhouder of therapeut gaat dat vragen; Michiel moet het antwoord klaar hebben.
Als de website of LinkedIn niet gelezen kon worden: zeg dat hier expliciet, zodat Michiel weet dat de prefill enkel op de kickoff steunt.

## Actiepunten vóór de eerste sessie
Cloud-sync regelen, Claude Desktop installeren, materiaal klaarzetten, brand book droppen.

## Wat Michiel nog moet nakijken
Concrete files waar je twijfelde bij de customisatie.
```

## 9. Wat bij de klant blijft

De skill draait bij de klant. Alles wat hij maakt, blijft in haar map: de AI-laag en de werkbestanden in `_ai-setup/`. Schrijf niets naar een andere plek en verwijs nergens naar de werkmap van Michiel. Wil Michiel iets meenemen (de ontwerpnotitie, het trajectplan), dan vraagt hij het zelf aan de klant.

## 10. Eindcontrole

Eerst een praktische noot: een gegenereerd bestand verwijderen vraagt in Cowork een aparte toestemming. Liever een bestand overschrijven of leegmaken dan verwijderen, tenzij het echt weg moet. Wil je toch verwijderen, zeg dan aan Michiel wat en waarom, en wacht op zijn akkoord.


- Draai `python scripts/build_skeleton.py --check <pad>`: zoekt naar overgebleven `{{` of `}}` in alle files en meldt lege mappen zonder LEESMIJ.
- Open `CLAUDE.md`, `LEESMIJ.md` en `SETUP-START-HIER.md` één keer volledig en lees ze als de klant. Klinkt het als iets dat Michiel zou schrijven? Staan er nog generieke voorbeelden die niet bij deze sector passen?
- Controleer dat `SETUP-STATUS.md` de juiste fasen toont (Fase C ontbreekt bij `multi_instance` `false`).
- Tel de kanaal-submappen in `_voorbeelden/` en vergelijk met `kanalen` in de config.

Pas daarna toon je Michiel het overzicht en vraag je zijn akkoord voor oplevering.
