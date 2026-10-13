# Werkregels

Regels die voor élk werk in deze omgeving gelden. Altijd geladen.

---

## Voice-protocol

Voor elke schrijftaak: bepaal eerst voor wie er geschreven wordt en op welk kanaal de tekst landt. Begin niet zonder beide.

**Voor wie:**
{{#if multi_instance}}- Werk voor een {{instantie_enkelvoud}}{{#if overlay}}{{#if instanties_pad}} (bestanden in `{{instanties_pad}}/[naam]/`){{/if}}, context{{/if}} uit `{{instantie_map}}/[naam]/` → laad {{#if volledig}}uitsluitend de `_voice.md` en `_context.md` van {{i_die}} {{instantie_enkelvoud}}. Negeer alle andere voices.{{else}}de `_context.md` van {{i_die}} {{instantie_enkelvoud}} voor de feiten en `{{eigen_map}}/_voice.md` voor de stem.{{/if}}
- Werk voor {{wd_lidwoord}} eigen {{werkdomein_lower}} → laad `{{eigen_map}}/_voice.md` en `_context.md`.
- Onduidelijk voor wie → vragen. Niets schrijven zonder antwoord.
{{else}}- Laad `{{eigen_map}}/_voice.md` en `_context.md`.
- Onduidelijk of het eigen werk is → vragen.
{{/if}}
**Op welk kanaal:**
- Bepaal het kanaal: {{kanalen_lijst}}.
- Laad uitsluitend `_voorbeelden/[kanaal]/` van dat werkdomein.
- Andere kanaal-submappen blijven dicht, zodat het ritme van het ene kanaal niet in het andere sijpelt.
- Onduidelijk welk kanaal → vragen.

De basisregels uit `_kern/schrijfregels-basis.md` en de anti-AI-stijl uit `_kern/anti-ai-stijl.md` gelden altijd, los van voice en kanaal.

---

{{#if overlay}}## Bestaande mappen

De mappen van {{naam}} bestonden al voor deze AI-laag. {{#if bestaande_schrijven}}Lezen mag. Een nieuwe file erin zetten mag na bevestiging. Bestaande files overschrijven, hernoemen, verplaatsen of verwijderen mag nooit.{{else}}Lezen mag. Schrijven, hernoemen, verplaatsen of verwijderen mag niet. Nieuwe output komt in `{{projecten_map}}/`.{{/if}} Welke map wat bevat en wat Claude ermee mag, staat in de tabel in `CLAUDE.md`.

{{#if buiten_bereik_obj}}Buiten bereik: {{#each buiten_bereik_obj}}`{{pad}}/`{{sep}}{{/each}}. Nooit openen.

{{/if}}---

## Beslisregels

Regels die {{naam}} toepast zonder dat ze ergens opgeschreven staan. Bijvoorbeeld: welke versie van een document geldt, wanneer iets naar een collega gaat, welk systeem de bron is voor welk gegeven.

- [Vul aan tijdens Fase 0]

---

{{/if}}## Projecten-regel

{{#if overlay}}- Werk in uitvoering en nieuwe output → `{{projecten_map}}/[YYYY-MM-projectnaam]/`, ook als het over één {{#if multi_instance}}{{instantie_enkelvoud}}{{else}}opdracht{{/if}} gaat.
- De bestaande mappen blijven de plek van het afgewerkte werk. {{naam}} zet het er zelf in{{#if bestaande_schrijven}}, of Claude na bevestiging{{/if}}.
{{else}}{{#if multi_instance}}- Project gebonden aan één {{instantie_enkelvoud}} of aan {{wd_lidwoord}} eigen {{werkdomein_lower}} → de lokale `projecten/`-map van dat werkdomein.
- Project dat over meerdere werkdomeinen heen gaat → `9. Projecten/`.
{{else}}- Project gebonden aan {{wd_lidwoord}} eigen {{werkdomein_lower}} → `{{eigen_map}}/projecten/`.
- Project dat breder gaat (een tool bouwen, een proces herdenken, een opleiding) → `9. Projecten/`.
{{/if}}- Bij twijfel: lokaal. Promoveren naar root kan altijd later.
{{/if}}

---

## Bestandsnamen

- Nieuwe files: `YYYY-MM-DD-beschrijvende-naam.ext`. Kleine letters, koppeltekens, geen spaties.{{#if overlay}} Enkel in de AI-laag. De namen in de bestaande mappen blijven zoals ze zijn.{{/if}}
- Projectmappen: `YYYY-MM-projectnaam/` (zonder dag, een project loopt langer).
- Korte, beschrijvende namen. Niet "document-1" of "versie-final-echt".
{{#if heeft_offerte}}
---

## Prijzen

De tarieflijst in `{{eigen_map}}/_context.md` is de enige prijsbron. Ontbreekt een prijs, dan vraagt Claude ze. Geen schattingen, geen afrondingen, geen "vanaf"-prijzen die {{naam}} niet zelf gaf.
{{/if}}
{{#if multi_instance}}---

## {{i_Nieuwe}} {{instantie_enkelvoud}} (proces)

1. Kopieer `{{instantie_map}}/_template-{{i_nieuwe}}-{{instantie_slug}}/` naar `{{instantie_map}}/[naam]/`.{{#if overlay}} Dat is de context in de AI-laag. De bestanden van {{i_die}} {{instantie_enkelvoud}} blijven in {{#if instanties_pad}}`{{instanties_pad}}/[naam]/`{{else}}de bestaande map{{/if}}.{{/if}}
2. Doorloop `_kennis/templates/intake-vragenlijst-{{instantie_slug}}.md`.
3. Vul `_context.md`{{#if volledig}}, `_voice.md` (volgens `_kennis/templates/voice-analyse-protocol.md`){{/if}} en `_strategie.md`.
{{#if volledig}}4. Sorteer voorbeelden per kanaal in `_voorbeelden/`.
5. Pas dan start het echte werk voor {{i_die}} {{instantie_enkelvoud}}.
{{else}}4. Pas dan start het echte werk voor {{i_die}} {{instantie_enkelvoud}}.
{{/if}}
{{/if}}---

## Veiligheid

- Niets overschrijven, hernoemen of verwijderen zonder eerst te tonen wat verandert en bevestiging te krijgen.
- Niets buiten deze werkfolder wijzigen tenzij {{naam}} het expliciet vraagt.
{{#if overlay}}- De bestaande mappen van {{naam}} volgen de regel hierboven. Die gaat voor op alles.
{{/if}}- Bij twijfel over de juiste plek: vragen, niet gokken.
- Versioning van kritieke files: bij batch-updates gaat de vorige versie naar `_versies/` naast de file, met datum-stamp. Zie `CLAUDE.md`.
{{#if vertrouwelijkheid}}- Vertrouwelijkheid: zie `_kern/vertrouwelijkheid.md`. Die regels gaan voor op alles hierboven.
{{else}}{{#if vertrouwelijkheid_regels}}- Discretie, in de woorden van {{naam}}:
{{#each vertrouwelijkheid_regels}}  - {{this}}
{{/each}}{{/if}}{{/if}}
---

## Backup en locatie van de map

Waar de map staat en hoe ze geback-upt wordt, is een beslissing voor de eerste sessie met {{coach_voornaam}}{{#if cloud_sync}} ({{naam}} werkt met {{cloud_sync}}){{/if}}. Tot dan staat de map lokaal, met een geplande kopie naar de cloud. De `_versies/`-mappen zijn een tweede vangnet, geen vervanging.

---

## Inbox

Files in `{{inbox_map}}/`: lezen, classificeren, plek voorstellen met reden, verplaatsen na bevestiging, hernoemen naar de conventie. Volledig protocol in `CLAUDE.md`.

---

## Memory (kort)

"Onthoud dit" → volg de allocatietabel in `CLAUDE.md`. Eén onderwerp, één thuis. Meest specifieke niveau wint.

---

*Vul aan wanneer een nieuwe regel opduikt die écht overal geldt. Domein-specifieke uitzonderingen horen in het werkdomein zelf, niet hier.*
