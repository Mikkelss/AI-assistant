# Welkom in je Cowork-omgeving, {{naam}}

Dit document legt uit wat hier staat en hoe het werkt. Voor jou, de mens. De AI heeft zijn eigen instructies in `CLAUDE.md`.

---

## Begin hier

Open Cowork en typ:

> **SETUP**

Claude leest dan het setup-document en begint je vragen te stellen om deze omgeving aan jouw manier van werken{{#if multi_instance}} en je {{instantie_meervoud_lower}}{{/if}} aan te passen. Je hoeft zelf geen files te openen of in te vullen. Claude voert het gesprek en schrijft de antwoorden weg.

De setup is gefaseerd. Je hoeft niet alles in één keer te doen. Een eerste sessie van 15 tot 30 minuten volstaat om Claude bruikbaar te krijgen. Wanneer je later terugkomt en opnieuw `SETUP` typt, weet Claude waar je gebleven was. Dat houdt hij bij in `SETUP-STATUS.md`. Je mag die file altijd zelf openen om te zien hoever je staat.

Een aantal files zijn al deels voorgevuld op basis van {{bron_je}}. Die stukken staan gemarkeerd als voorstel. Tijdens de setup bevestig je ze, pas je ze aan of gooi je ze weg.

---

## Wat is dit?

Een werkfolder die als één samenhangend systeem werkt met Claude via Cowork. Het idee: je hoeft niet meer telkens uit te leggen wie je bent, {{#if multi_instance}}wie je {{instantie_enkelvoud}} is, {{/if}}hoe je schrijft of welk proces je volgt. Die context staat in de juiste files, en Claude laadt ze automatisch in op het juiste moment.

Concreet: je begint een nieuwe sessie en zegt "schrijf {{test_kanaal_enkelvoud}} {{#if multi_instance}}voor {{instantie_enkelvoud}} X {{/if}}over onderwerp Y". Claude leest stil de juiste context, stem en voorbeelden. De output zit al dicht bij wat je wil.

---

## De grote ideeën in vijf zinnen

1. `_kern/` is altijd geladen. Wat hier staat geldt voor élk werk. Klein en algemeen houden.
2. `{{eigen_map}}/` is je eigen {{werkdomein_lower}}{{#if volledig}}, behandeld als één van je {{instantie_meervoud_lower}}: die ene waarvoor je gratis werkt{{/if}}.
{{#if multi_instance}}3. `{{instantie_map}}/` bevat één map per {{instantie_enkelvoud}}, allemaal met dezelfde opbouw (kopie van `_template-{{i_nieuwe}}-{{instantie_slug}}/`).
4. {{#if volledig}}Je eigen stem en die van {{i_elke}} {{instantie_enkelvoud}} staan op hun eigen plek. Claude laadt de juiste stem op basis van waar je werkt. Geen vermenging.{{else}}De stem is altijd de jouwe en staat in `{{eigen_map}}/_voice.md`. Per {{instantie_enkelvoud}} staan enkel de feiten en het lopende werk.{{/if}}
5. `_voorbeelden/[kanaal]/` bevat per kanaal echte voorbeelden. Claude laadt enkel het kanaal van de huidige taak.
{{else}}3. `_voorbeelden/[kanaal]/` bevat per kanaal echte voorbeelden. Claude laadt enkel het kanaal van de huidige taak.
4. `projecten/` is voor afgebakend werk met begin en einde. Terugkerend werk staat in zijn eigen mappen.
5. `0. Inbox/` is de dropzone. Alles wat je niet meteen kan plaatsen, gooi je daar. Claude helpt sorteren.
{{/if}}
{{#if multi_instance}}---

## Hoe je een {{i_nieuwe}} {{instantie_enkelvoud}} erbij doet

1. Kopieer `{{instantie_map}}/_template-{{i_nieuwe}}-{{instantie_slug}}/` naar `{{instantie_map}}/[naam]/`.
2. Doorloop de intake-vragenlijst uit `_kennis/templates/` met {{persoon_lidwoord}} {{persoon}}, of plak de antwoorden die je al hebt.
3. Vraag Claude: "verwerk dit en vul de map van [naam] aan." Hij vult `_context.md`{{#if volledig}}, `_voice.md`{{/if}} en `_strategie.md`{{#if volledig}} en sorteert de voorbeelden per kanaal{{/if}}.
4. Klaar. Vanaf nu laadt Claude automatisch de juiste context wanneer je voor {{i_die}} {{instantie_enkelvoud}} werkt.

{{/if}}---

## Wat staat waar

- `CLAUDE.md`: routing-instructies voor de AI. Niet aanraken tenzij je weet wat je doet.
- `SETUP-START-HIER.md` en `SETUP-STATUS.md`: de setup-guide en waar je staat.
- `_kern/`: altijd-geladen meta-laag. Wie jij bent als {{rol_label}}, je werkregels, anti-AI-patronen{{#if vertrouwelijkheid}}, wat vertrouwelijk is{{/if}}. Geen stem hier.
- `_kennis/`: referenties op afroep. Frameworks, templates voor intake en voice-analyse.
- `0. Inbox/`: dropzone.
- `{{eigen_map}}/`: alles voor je eigen {{werkdomein_lower}}.
{{#if multi_instance}}- `{{instantie_map}}/`: één map per {{instantie_enkelvoud}}, plus de template.
{{/if}}- `9. Projecten/`: projecten die over meerdere werkdomeinen heen gaan.
- `_archief/`: afgesloten werk.

---

## Versioning en backup

**Versioning.** Telkens Claude een belangrijke file aanpast (je stem, je context, je strategie, een kern-file), bewaart hij eerst de oude versie in een `_versies/`-submap met datum en uur in de bestandsnaam. Je kan altijd terugkijken, en je mag oude versies zelf wegsmijten wanneer je zeker bent. Claude raakt die mappen niet aan tenzij je het vraagt.

**Backup en waar de map staat.** {{#if cloud_sync}}Je gaf aan dat je met {{cloud_sync}} werkt. {{/if}}Waar deze map precies komt te staan en hoe ze geback-upt wordt, beslis je samen met {{coach_voornaam}} in de eerste sessie. Zet ze tot dan niet rechtstreeks in een cloud-map: Cowork kan bestanden afknotten wanneer een synchronisatiedienst ze tegelijk vastneemt. De gebruikelijke oplossing is: map lokaal, met een geplande kopie naar de cloud. De `_versies/`-mappen zijn een tweede vangnet, geen vervanging voor een backup.

---

*Opgezet op {{aangemaakt_op}} door {{coach}}. Aanpassen mag, dit is jouw werkomgeving.*
