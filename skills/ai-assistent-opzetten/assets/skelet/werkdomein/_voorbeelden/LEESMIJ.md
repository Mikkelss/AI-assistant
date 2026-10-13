# Voorbeelden: {{wd_naam}}

Referentie-voorbeelden per kanaal. Claude gebruikt ze om te begrijpen hoe output voor {{#if is_eigen}}{{wd_lidwoord}} eigen {{werkdomein_lower}}{{else}}{{i_deze}} {{instantie_enkelvoud}}{{/if}} op dit specifieke kanaal moet voelen.

---

## Hoe het werkt

- Eén submap per kanaal: {{#each kanalen_obj}}`{{id}}/`{{sep}}{{/each}}.
- Eén voorbeeld per file. Naam: `YYYY-MM-DD-korte-beschrijving.md`.
- Bovenaan elk voorbeeld: datum en 1 of 2 zinnen waarom dit een goed voorbeeld is.

## Conditional loading

Claude laadt alleen de submap van het kanaal waar de huidige taak op landt. {{test_kanaal_enkelvoud_cap}}? Alleen `{{test_kanaal_id}}/` wordt gelezen. Andere kanalen{{#if multi_instance}} en andere werkdomeinen{{/if}} blijven dicht.

## Wat hier hoort

- Output die écht raak was en die je opnieuw zou willen kunnen maken.
- 3 tot 10 voorbeelden per actief kanaal. Kwaliteit boven aantal.
- Variatie binnen een kanaal (kort en lang, verschillende types).

## Wat hier niet hoort

- Anti-voorbeelden: die staan in `../_voice.md` onder "Voorbeelden: niet".
- Drafts of werk in uitvoering: die staan {{#if overlay}}in `{{projecten_map}}/`{{else}}in de recurring-mappen of in `projecten/`{{/if}}.
{{#if is_eigen}}{{#if volledig}}- Voorbeelden die een {{instantie_enkelvoud}} publiceert in zijn eigen stem: die horen in de map van {{i_die}} {{instantie_enkelvoud}}. Wat {{naam}} zelf naar {{instantie_meervoud_lower}} stuurt, hoort wél hier.{{else}}{{#if multi_instance}}- Let op: bij deze opzet komen de beste voorbeelden net uit het werk voor {{instantie_meervoud_lower}}. Die horen dus wél hier, geanonimiseerd (namen vervangen door rollen, cijfers weglaten).{{else}}- Voorbeelden van anderen.{{/if}}{{/if}}{{else}}- Voorbeelden van andere {{instantie_meervoud_lower}} of van {{wd_lidwoord}} eigen {{werkdomein_lower}}.{{/if}}
{{#if vertrouwelijkheid}}
## Vertrouwelijkheid

Voorbeelden met informatie van derden worden geanonimiseerd bewaard. Zie `_kern/vertrouwelijkheid.md`.
{{/if}}
