# Context

Wat Claude moet weten en wat nergens in je eigen mappen staat. Je stem, je strategie, afspraken, gevoeligheden.

- `{{werkdomein_eigen}}/`: {{wd_lidwoord}} eigen {{werkdomein_lower}}. Stem (`_voice.md`), feiten (`_context.md`), strategie (`_strategie.md`) en voorbeelden per kanaal.
{{#if multi_instance}}- `{{instantie_meervoud}}/`: één map per {{instantie_enkelvoud}} die al in het systeem zit, plus de template. {{#if instanties_pad}}De bestanden van {{i_elke}} {{instantie_enkelvoud}} blijven in `{{instanties_pad}}/`. Hier staat enkel de context.{{/if}}
{{/if}}
Je eigen mappen bevatten het werk. Deze map bevat wat Claude nodig heeft om dat werk goed te lezen en te maken.

Niet elke {{#if multi_instance}}{{instantie_enkelvoud}}{{else}}opdracht{{/if}} hoeft hier meteen een map te krijgen. Begin met één, en voeg er een toe telkens je voor {{#if multi_instance}}{{i_die}} {{instantie_enkelvoud}}{{else}}iets nieuws{{/if}} met Claude aan de slag gaat.
