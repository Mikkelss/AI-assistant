# Voice: {{wd_naam}}

{{#if is_eigen}}De schrijfstem van {{naam}}. Wordt geladen bij werk voor {{wd_lidwoord}} eigen {{werkdomein_lower}}{{#if multi_instance}}{{#if volledig}} en bij alles wat {{naam}} zelf naar een {{instantie_enkelvoud}} stuurt (rapporten, mails, offertes). Wat een {{instantie_enkelvoud}} publiceert, volgt de `_voice.md` van {{i_die}} {{instantie_enkelvoud}}{{else}} én bij werk voor {{instantie_meervoud_lower}}: de stem is altijd die van {{naam}}{{/if}}{{/if}}.{{else}}De schrijfstem van {{i_deze}} {{instantie_enkelvoud}}. Wordt enkel geladen bij werk voor {{i_deze}} {{instantie_enkelvoud}}.{{/if}}

Bouw deze file op met `_kennis/templates/voice-analyse-protocol.md`, op basis van minstens 10 voorbeelden.

---

## In één zin

[zin die de stem beschrijft]

## Vorm en ritme

- [regel 1, bijvoorbeeld: openingszin is altijd een concreet feit]
- [regel 2, bijvoorbeeld: drie korte zinnen, dan één lange]
- [regel 3]

## Woordkeuze

**Wel:**
- [woorden die typerend zijn]

**Niet:**
- [woorden die nooit mogen]

## Aanspreekvorm

[jij / je / u / wij. Standaard één; waar het per kanaal verschilt, staat het in de register-tabel hieronder.]

## Register per kanaal

Dezelfde stem klinkt anders per kanaal. Per kanaal: voor wie, hoe lang, hoe opgebouwd, wat nooit.

| Kanaal | Lezer | Aanspreekvorm | Lengte en opbouw | Wat nooit |
|---|---|---|---|---|
{{#each kanalen_obj}}| {{label}} | | | | |
{{/each}}
## Verboden

- [openingen die nooit mogen]
- [zinsbouwen die vreemd voelen]
- [clichés]

## Signature-moves

- [patroon 1: iets wat alleen deze schrijver doet]
- [patroon 2]

## Voorbeelden: wel

[3 korte voorbeelden die de stem perfect vangen]

## Voorbeelden: niet

[1 of 2 anti-voorbeelden met korte uitleg waarom]

---

*Geen statisch document. Elke output die niet klopt is een aanleiding voor een extra regel, verbod of voorbeeld.*
