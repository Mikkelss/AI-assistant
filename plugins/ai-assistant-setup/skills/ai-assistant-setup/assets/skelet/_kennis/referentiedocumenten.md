# Referentiedocumenten

Per taak het document dat toont hoe het moet. Claude kijkt hier eerst, voor hij zelf een voorbeeld zoekt in de mappen. Het origineel blijft waar het staat, Claude leest het enkel.

| Taak | Referentiedocument (pad) | Wat eraan goed is | Laatst bevestigd |
|---|---|---|---|
{{#if pijnpunten}}{{#each pijnpunten}}| {{this}} | [vul aan tijdens Fase 0] | | |
{{/each}}{{else}}| [taak] | [pad] | [wat Claude moet overnemen] | |
{{/if}}{{#if referentie_obj}}
Mappen met templates en referentiedocumenten, volgens de mappenkaart: {{#each referentie_obj}}`{{pad}}/`{{sep}}{{/each}}.
{{/if}}
---

## Regels

- Eén referentie per taak. Zijn er twee, dan kiest {{naam}} welke geldt, of beschrijft wanneer welke.
- Staat een document met "v2", "final" of "kopie" in de naam, vraag dan welke versie de referentie is.
- Verandert {{naam}} de manier van werken, pas dan deze tabel aan. Een oud voorbeeld dat blijft staan, trekt de output terug naar hoe het vroeger was.

---

*Aangemaakt op {{aangemaakt_op}}. Aanvullen in Fase 0 van de setup, en telkens er een betere referentie opduikt.*
