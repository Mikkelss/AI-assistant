{{#if overlay}}# Projecten en output

Alles wat Claude voor je maakt, komt hier. Eén map per project of taak: `YYYY-MM-projectnaam/`. Ook een losse brief of een verslag krijgt een map, dan blijft de historiek bij elkaar.

Je eigen mappen blijven de plek van het afgewerkte werk. {{#if bestaande_schrijven}}Claude zet iets daar enkel na je akkoord, en overschrijft nooit iets.{{else}}Jij zet het daar zelf, wanneer het af is. Claude schrijft niet in je eigen mappen.{{/if}}

Afgerond en overgezet? Verplaats de projectmap naar `_afgerond/` hier. Zo blijft deze map overzichtelijk.

---

## Nieuw project starten

1. Kopieer `_template/project.md` naar `YYYY-MM-projectnaam/project.md`.
2. Vul in.
3. Werk verder in die map.
{{else}}# Projecten (cross-cutting)

Projecten die breder gaan dan {{#if multi_instance}}één {{instantie_enkelvoud}} of {{/if}}{{wd_lidwoord}} eigen {{werkdomein_lower}}. Bijvoorbeeld: een nieuw proces ontwerpen, een tool bouwen, een opleiding volgen, de eigen werkwijze herdenken.

{{#if projecten_per_instantie}}Projecten die bij één {{instantie_enkelvoud}} horen: `{{instantie_map}}/[naam]/projecten/`.
{{/if}}Projecten die bij {{wd_lidwoord}} eigen {{werkdomein_lower}} horen: `{{eigen_map}}/projecten/`.

Bij twijfel: lokaal. Promoveren naar hier kan altijd later.

---

## Nieuw project starten

1. Kopieer `_template/project.md` naar `YYYY-MM-projectnaam/project.md`.
2. Vul in.
3. Werk verder in die map.
{{/if}}
