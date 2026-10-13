# Setup-status

Deze file houdt bij hoe ver {{naam}} staat in de setup van de Cowork-omgeving. Claude leest ze wanneer {{naam}} `SETUP` typt en gebruikt ze om voor te stellen waar verder te gaan. Claude werkt ze ook bij. Handmatig aanpassen mag, maar hoeft niet.

---

## Overzicht

| Fase | Status | Gestart op | Voltooid op |
|---|---|---|---|
{{#if overlay}}| 0: je mappen leren kennen | Niet gestart | | |
{{/if}}| A: basis | Niet gestart | | |
| B: eigen {{werkdomein_lower}} verdiepen | Niet gestart | | |
{{#if multi_instance}}| C: eerste {{instantie_enkelvoud}} | Niet gestart | | |
{{/if}}
Status-waarden: `Niet gestart`, `In uitvoering`, `Voltooid`, `Op pauze`.

---

## Detail per fase

{{#if overlay}}### Fase 0: je mappen leren kennen

**Status:** Niet gestart

Gevuld na deze fase:
- [ ] Wat Claude in je documenten vond (`_ai-setup/analyse.md`): elk punt bevestigd, aangepast of geschrapt
- [ ] Tabel "Bestaande mappen" in `CLAUDE.md`: elke map in de hoofdmap staat erin, met bevestigde beschrijving en rol
- [ ] `_kennis/referentiedocumenten.md`: minstens 3 taken met hun referentiedocument
- [ ] `_kern/werkregels.md`: sectie "Beslisregels" ingevuld
- [ ] `{{eigen_map}}/_context.md`: sectie "Bronsystemen" ingevuld
- [ ] Mappen buiten bereik bevestigd

---

{{/if}}### Fase A: basis

**Status:** Niet gestart

Gevuld na deze fase:
- [ ] `_kern/wie-ik-ben.md`: geen `[Vul aan:` en geen `[VOORSTEL` meer
- [ ] `_kern/anti-ai-stijl.md`: minstens 3 eigen openingszinnen, 3 woorden en 2 zinsbouwen toegevoegd
- [ ] `{{eigen_map}}/_context.md`: basisvelden ingevuld en voorstellen bevestigd
{{#if vertrouwelijkheid}}- [ ] `_kern/vertrouwelijkheid.md`: doorgelopen en bevestigd
{{/if}}
---

### Fase B: eigen {{werkdomein_lower}} verdiepen

**Status:** Niet gestart

Gevuld na deze fase:
- [ ] `{{eigen_map}}/_strategie.md`: basisvelden ingevuld
- [ ] `{{eigen_map}}/_voice.md`: minstens 8 regels en 3 verboden, geen placeholders meer
- [ ] `{{eigen_map}}/_voorbeelden/`: minstens 3 voorbeelden in minstens 2 kanalen (te beginnen met `{{eerste_kanaal_id}}/` en `{{tweede_kanaal_id}}/`)
- [ ] Eerste test gedaan en geïtereerd

{{#if multi_instance}}---

### Fase C: eerste {{instantie_enkelvoud}}

**Status:** Niet gestart

Gevuld na deze fase:
{{#if overlay}}- Gekozen {{instantie_enkelvoud}}: {{#if instanties_start_obj}}{{#each instanties_start_obj}}{{naam}}{{sep}}{{/each}} (map in de AI-laag staat al klaar){{else}}[in te vullen in Fase 0]{{/if}}
{{/if}}- [ ] `{{instantie_map}}/[naam]/` aangemaakt als kopie van de template
- [ ] `_context.md` van {{i_die}} {{instantie_enkelvoud}}: alle basisvelden
{{#if volledig}}- [ ] `_voice.md` van {{i_die}} {{instantie_enkelvoud}}: gevuld op basis van stem-analyse
{{/if}}- [ ] `_strategie.md` van {{i_die}} {{instantie_enkelvoud}}: basisvelden
{{#if volledig}}- [ ] `_voorbeelden/[kanaal]/`: minstens 3 voorbeelden in de actieve kanalen
{{/if}}- [ ] Eerste test gedaan voor {{i_deze}} {{instantie_enkelvoud}}

{{/if}}---

## Logboek

(Elke sessie waarin Claude iets aan de setup veranderd heeft: datum plus één regel.)

- {{aangemaakt_op}}: {{#if overlay}}AI-laag toegevoegd door {{coach}} naast de bestaande mappen, op basis van de mappenstructuur en het kickoffgesprek. Aan de bestaande mappen is niets veranderd.{{else}}omgeving aangemaakt door {{coach}} op basis van {{bron_de}}.{{/if}}

---

*Wordt automatisch bijgewerkt door Claude na elke voltooide setup-stap.*
