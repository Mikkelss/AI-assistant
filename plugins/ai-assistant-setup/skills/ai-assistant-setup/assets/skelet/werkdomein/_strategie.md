# Strategie: {{wd_naam}}

{{#if is_eigen}}De strategie voor {{wd_lidwoord}} eigen {{werkdomein_lower}}: focus, positionering, kanalen, doelen. Wordt enkel geladen bij eigen werk.{{else}}{{#if volledig}}De strategie voor {{i_deze}} {{instantie_enkelvoud}}: focus, aanpak, doelen. Wordt enkel geladen bij werk voor {{i_deze}} {{instantie_enkelvoud}}.{{else}}De aanpak voor {{i_deze}} {{instantie_enkelvoud}}: doel, spoor, mijlpalen, lopend werk, beslissingen. Wordt enkel geladen bij werk voor {{i_deze}} {{instantie_enkelvoud}}.{{/if}}{{/if}}

---

{{#if is_eigen}}## Focus dit jaar

[hoofddoel, in één of twee zinnen]

## Positionering

[Voor [doelgroep] die [probleem] hebben, bied ik [oplossing] omdat [wat anders is].]

## Terugkerende thema's

- [thema 1]
- [thema 2]
- [thema 3]

## Kanalen en ritme

| Kanaal | Doel | Frequentie | Type |
|---|---|---|---|
{{#each kanalen_obj}}| {{label}} | | | |
{{/each}}
## Doelen

| Periode | Hoofddoel | Meetbaar |
|---|---|---|
| | | |

{{else}}{{#if volledig}}## Focus dit kwartaal

[hoofddoel, in één of twee zinnen]

## Positionering

[Voor [doelgroep] die [probleem] hebben, bieden zij [oplossing] omdat [wat anders is].]

## Terugkerende thema's

- [thema 1]
- [thema 2]
- [thema 3]

## Kanalen en ritme

| Kanaal | Doel | Frequentie | Type |
|---|---|---|---|
{{#each kanalen_obj}}| {{label}} | | | |
{{/each}}
## Doelen

| Periode | Hoofddoel | Meetbaar |
|---|---|---|
| | | |

{{else}}## Doel van de samenwerking

[wat moet er bereikt zijn als dit goed afloopt]

## Spoor en aanpak

[welke weg kies ik en waarom; wat zijn de alternatieven die ik bewust niet neem]

## Mijlpalen en termijnen

| Datum | Wat | Status |
|---|---|---|
| | | |

{{/if}}## Lopend werk{{#if heeft_projecten}} en projecten{{/if}}

- [wat ligt er nu op tafel]{{#if heeft_projecten}}
- [project of traject]: zie `projecten/[map]/`{{/if}}

{{/if}}## Beslissingen (logboek)

- [datum]: [beslissing], [reden]

---

*Bijwerken telkens de aanpak schuift. Beslissingen loggen zodat je later weet waarom iets veranderde.*
