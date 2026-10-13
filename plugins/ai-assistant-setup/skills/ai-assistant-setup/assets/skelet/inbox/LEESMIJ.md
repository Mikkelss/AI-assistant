# Inbox

Dropzone voor alles wat nog gesorteerd moet worden. Sleep hier files in die je later wil verwerken. Claude leest, herkent voor wie het is{{#if multi_instance}} (eigen {{werkdomein_lower}} of een {{i_specifieke}} {{instantie_enkelvoud}}){{/if}}, en plaatst het op de juiste plek na jouw bevestiging.

{{#if vertrouwelijkheid}}Bij bestanden die gevoelige inhoud kunnen bevatten, vraagt Claude eerst wat het is voor hij ze leest. Zie `_kern/vertrouwelijkheid.md`.

{{/if}}---

## Werkwijze

1. Sleep een file hierin (of meerdere).
2. Vraag Claude om te verwerken, of zeg gewoon "verwerk de inbox".
3. Claude classificeert, stelt een plek voor met reden, verplaatst na bevestiging.

{{#if multi_instance}}Voor {{instantie_enkelvoud}}-materiaal: zet de naam in de bestandsnaam of zeg het in de chat ("dit is voor [naam]"). Dan routeert Claude rechtstreeks naar de juiste map.

{{/if}}---

## Wat hier mag

- Voorbeelden van output die je goed vond → komen in `_voorbeelden/[kanaal]/` van het juiste werkdomein.
- Contextdocumenten (positionering, brand book, achtergrondstukken) → Claude verwerkt ze in `_context.md` of `_strategie.md`.
{{#if overlay}}- Rapporten, analyses en materiaal voor lopend werk → `{{projecten_map}}/`. Hoort het in een van je eigen mappen, dan zet je het daar zelf.{{else}}- Rapporten en analyses → de analyse- of rapportmap van het werkdomein.
- Materiaal voor lopend werk → de juiste recurring-map of projectmap.{{/if}}
- Frameworks en methodieken → `_kennis/frameworks/`.
- Onduidelijk? Gewoon droppen. Claude vraagt door.

---

## Houd deze map leeg

Wat hier te lang ligt, raakt vergeten. Bij meer dan 5 à 10 files: "verwerk de inbox".
