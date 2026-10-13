# Context: {{wd_naam}}

{{#if is_eigen}}Deze file beschrijft wie {{wd_lidwoord}} {{werkdomein_lower}} van {{naam}} is. Wordt alleen geladen wanneer er {{#if overlay}}voor {{wd_lidwoord}} eigen {{werkdomein_lower}}{{else}}in `{{wd_pad}}/`{{/if}} gewerkt wordt{{#if multi_instance}}, niet wanneer er voor een {{i_specifieke}} {{instantie_enkelvoud}} geschreven wordt{{/if}}.

Velden met "[VOORSTEL …]" komen uit {{bron_de}}. Tijdens Fase A bevestig je ze, pas je ze aan of gooi je ze weg.{{else}}Deze file beschrijft {{i_deze}} {{instantie_enkelvoud}}: wie, wat er speelt, wat je moet weten voor je iets schrijft of voorbereidt. Wordt alleen geladen wanneer er voor {{i_deze}} {{instantie_enkelvoud}} gewerkt wordt.{{#if overlay}}

**Werkmap:** {{#if werkmap}}`{{werkmap}}/`{{else}}[pad naar de bestaande map van {{i_deze}} {{instantie_enkelvoud}}]{{/if}}. Daar staan de bestanden zelf. {{#if bestaande_schrijven}}Lezen mag, een nieuwe file erin enkel na bevestiging{{else}}Alleen lezen{{/if}}, zie de hardregel in `CLAUDE.md`. Deze file bevat enkel wat Claude moet weten en wat nergens in die map staat.{{/if}}

Vul aan op basis van `_kennis/templates/intake-vragenlijst-{{instantie_slug}}.md`.{{/if}}

---

{{#if is_eigen}}## In één zin

{{#if prefill.bedrijf_in_een_zin}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{prefill.bedrijf_in_een_zin}}{{else}}[Vul aan: één zin die zegt wat je {{werkdomein_lower}} doet en voor wie.]{{/if}}

---

## Diensten of producten

{{#if prefill.diensten}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{#each prefill.diensten}}- {{this}}
{{/each}}{{else}}[Vul aan: welke diensten of producten lever je? Kort per stuk.]{{/if}}

---

## Doelgroep

{{#if prefill.doelgroep}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{prefill.doelgroep}}{{else}}[Vul aan: voor wie ben je er? Wie, situatie, probleem, wat maakt dat ze jou bellen.]{{/if}}

---

## Wat mij onderscheidt

{{#if prefill.usps}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{#each prefill.usps}}- {{this}}
{{/each}}{{else}}[Vul aan: minstens 3 concrete dingen. Geen "kwaliteit" of "persoonlijke aanpak".]{{/if}}

---

## Positionering

{{#if prefill.positionering}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{prefill.positionering}}{{else}}[Vul aan: premium of toegankelijk? Specialist of generalist? Partner op lange termijn of per opdracht?]{{/if}}

---

## Prijsstelling (intern, niet voor publicatie)

{{#if heeft_offerte}}Dit is de enige prijsbron voor Claude. Wat hier niet staat, vraagt hij.

| Dienst of pakket | Prijs | Inbegrepen | Opmerking |
|---|---|---|---|
| | | | |
{{else}}[Vul aan: tariefkaders, pakketten, projectprijzen. Helpt Claude bij mails over geld.]{{/if}}

---

## Geschiedenis kort

{{#if prefill.geschiedenis}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{prefill.geschiedenis}}{{else}}[Vul aan: sinds wanneer, hoe ontstaan, belangrijkste mijlpalen. 3 tot 5 zinnen.]{{/if}}

---

## Wie doet wat

{{#if prefill.team}}[VOORSTEL op basis van {{bron_je}}. Bevestig of pas aan tijdens SETUP Fase A.]
{{prefill.team}}{{else}}[Vul aan: alleen? Met freelancers of een team? Wie doet wat?]{{/if}}
{{#if overlay}}
---

## Bronsystemen

Welk systeem de bron is voor welke gegevens. Claude neemt cijfers en gegevens uit deze bron, nooit uit een oudere kopie in een map.

| Gegeven | Bronsysteem | Opmerking |
|---|---|---|
| [bv. facturen, planning, contactgegevens] | [pakket of map] | [vul aan tijdens Fase 0] |
{{/if}}{{else}}{{#if volledig}}## In één zin

[wie zijn ze en wat doen ze]

---

## Wat ze doen

- [dienst, product of activiteit 1]
- [2]
- [3]

---

## Voor wie zij werken

[wie is hun publiek of klant]

---

## Wat hen onderscheidt

- [concreet punt 1]
- [2]
- [3]

---

## Positionering

[waar staan ze in hun markt]

---

## Wat nooit mag

- [wat ze niet geassocieerd willen zien met hun naam]

---

## Contact en samenwerking

- Wie: [naam, rol]
- Kanalen: [waar en hoe vaak]
- Beslist: [wie tekent af, hoeveel iteraties]
- Rapportering: [vorm en frequentie]

---

## Geschiedenis

[sinds wanneer werken we samen, wat is al gedaan, belangrijkste momenten]
{{else}}## Gevoeligheden eerst

- [wat hier extra voorzichtigheid vraagt, of "geen"]

---

## In één zin

[wie is {{i_deze}} {{instantie_enkelvoud}} en waarvoor komen ze bij mij]

---

## Wie

| Rol | Naam | Wat je moet weten |
|---|---|---|
| [hoofdcontact of betrokkene] | | |
| [andere betrokkene] | | |

---

## Situatie en aanleiding

[wat speelt er, hoe is het zo gekomen, waarom nu]

---

## Wat ze willen bereiken

- [doel op korte termijn]
- [doel op langere termijn]

---

## Feiten en context die ik niet mag vergeten

- [feit, datum, afspraak]

---

## Wat nooit mag

- [wat niet gezegd, gedeeld of gedaan mag worden in dit geval]

---

## Samenwerking

- Kanalen: [waar en hoe vaak]
- Beslist: [wie]
- Volgende stap: [wat en wanneer]

---

## Geschiedenis

[sinds wanneer, wat is al gebeurd, belangrijkste momenten]
{{/if}}{{/if}}
---

*Bijwerken telkens er iets fundamenteels verandert.*
