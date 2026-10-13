# Wie ik ben (als {{rol_label}})

Deze file beschrijft wie {{naam}} is als {{rol_label}}. Niet {{wd_lidwoord}} {{werkdomein_lower}} zelf (dat staat in `{{eigen_map}}/_context.md`), wel de aanpak, de principes en het proces. Deze info is altijd geladen, dus ze moet algemeen genoeg zijn om voor élk werk te gelden.

Velden met "[VOORSTEL …]" zijn voorgevuld uit {{bron_de}}. Tijdens Fase A van de setup bevestig je ze, pas je ze aan of gooi je ze weg. De velden "In één zin" en "Hoe ik mijn vak zie" zijn bewust leeg gelaten: die formuleer je zelf.

---

## In één zin

[Vul aan: één zin die zegt wie je bent als {{rol_label}} en wat je onderscheidt. Dit is een identiteitsvraag. Formuleer ze zelf, ook als er iets bruikbaars op je website staat.]

---

## Mijn achtergrond

{{#if prefill.achtergrond}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{prefill.achtergrond}}{{else}}[Vul aan: 3 tot 5 zinnen. Hoe ben je hierin terechtgekomen, wat heb je gedaan, wat is je expertise?]{{/if}}

---

## Hoe ik mijn vak zie

[Vul aan: 3 tot 5 principes waar je in gelooft. Concreet: "ik geloof in X want Y." Geen platitudes. Dit is een identiteitsvraag, dus zelf formuleren.]

---

## Mijn werkproces bij {{#if multi_instance}}een {{i_nieuwe}} {{instantie_enkelvoud}}{{else}}een nieuwe opdracht{{/if}}

{{#if prefill.proces}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{#each prefill.proces}}{{index1}}. {{this}}
{{/each}}{{else}}[Vul aan: stap voor stap. Bijvoorbeeld: intake, analyse van wat er al is, voorstel van aanpak, uitvoering, opvolging.]{{/if}}

---

## Waar ik goed in ben

{{#if prefill.sterktes}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{#each prefill.sterktes}}- {{this}}
{{/each}}{{else}}[Vul aan: 3 tot 5 dingen waar je sterk in bent.]{{/if}}

---

## Waar ik bewust nee tegen zeg

{{#if prefill.nee_tegen}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{#each prefill.nee_tegen}}- {{this}}
{{/each}}{{else}}[Vul aan: 3 tot 5 dingen die je niet doet, ook niet op vraag.]{{/if}}

---

## Hoe ik samenwerk met {{#if multi_instance}}{{personen}}{{else}}opdrachtgevers{{/if}}

{{#if prefill.samenwerking}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{prefill.samenwerking}}{{else}}[Vul aan: hoe vaak contact, via welke kanalen, welke vorm van rapportering, wat je van hen verwacht.]{{/if}}

---

*Deze file is altijd geladen. Houd ze onder 1 à 2 pagina's.*
