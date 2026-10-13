# {{instantie_meervoud}}

Eén map per {{instantie_enkelvoud}}, allemaal met dezelfde opbouw. Die opbouw staat klaar in `_template-{{i_nieuwe}}-{{instantie_slug}}/`.{{#if overlay}}

Hier staat enkel wat Claude over {{i_die}} {{instantie_enkelvoud}} moet weten. De bestanden zelf blijven in {{#if instanties_pad}}`{{instantie_map_bestaand}}`{{else}}je bestaande mappen{{/if}}, en daar verandert niets aan. Niet elke {{instantie_enkelvoud}} hoeft hier een map te krijgen: enkel {{instantie_lidwoord}} {{instantie_meervoud_lower}} waarvoor je met Claude werkt.{{/if}}

---

## {{i_Nieuwe}} {{instantie_enkelvoud}} erbij

1. Kopieer `_template-{{i_nieuwe}}-{{instantie_slug}}/` naar `[naam]/` in deze map.{{#if overlay}} Gebruik dezelfde naam als in je eigen map, dan vindt Claude de twee bij elkaar.{{/if}}
2. Doorloop `_kennis/templates/intake-vragenlijst-{{instantie_slug}}.md`, of plak de antwoorden die je al hebt.
3. Vraag Claude om `_context.md`{{#if volledig}}, `_voice.md` (via `_kennis/templates/voice-analyse-protocol.md`){{/if}} en `_strategie.md` te vullen.
{{#if volledig}}4. Voorbeelden per kanaal in `_voorbeelden/`.
5. Pas dan start het echte werk.
{{else}}4. Pas dan start het echte werk.
{{/if}}
## Naamgeving

{{#if overlay}}Dezelfde naam als de map in {{#if instanties_pad}}`{{instantie_map_bestaand}}`{{else}}je bestaande mappen{{/if}}. Staat daar een nummer of een datum voor, neem dat gerust over.{{else}}Korte, herkenbare naam. Kleine letters, koppeltekens bij meerdere woorden. Bijvoorbeeld `acme/`, `de-bakker/`, `studio-nova/`.{{/if}}

## Afsluiten

{{#if overlay}}Stopt de samenwerking of sluit het dossier: zet bovenaan `_context.md` "Afgesloten op [datum]". De map blijft staan, historische context blijft nuttig. Wat er met de bestanden in je eigen map gebeurt, beslis je zelf.{{else}}Stopt de samenwerking of sluit het dossier: verplaats de hele map naar `_archief/[YYYY-naam]/`. Niet verwijderen. Historische context blijft nuttig.{{/if}}
