# Vertrouwelijkheid

Wat in deze omgeving nooit gedeeld, gelezen zonder toestemming, of geproduceerd mag worden. Altijd geladen. Deze regels gaan voor op alle andere werkregels.

{{naam}} werkt als {{rol_label}} met informatie van derden{{#if multi_instance}} ({{instantie_meervoud_lower}}){{/if}}. Wat hieronder staat is de minimale set. Tijdens Fase A van de setup loop je ze samen door en vul je aan wat in jouw vak vanzelfsprekend is.

---

## Regels van {{naam}}

{{#if vertrouwelijkheid_regels}}{{bron_Uit}}:

{{#each vertrouwelijkheid_regels}}- {{this}}
{{/each}}{{else}}[Vul aan tijdens Fase A: de regels die voor jouw vak gelden.]{{/if}}

---

## Defaults

**Nooit naar buiten zonder expliciete vraag**
- Namen, contactgegevens of herkenbare details van {{#if multi_instance}}{{instantie_meervoud_lower}}{{else}}derden{{/if}} in output die bestemd is voor iemand anders dan {{naam}} zelf.
- Inhoud uit één {{#if multi_instance}}{{instantie_enkelvoud}}map{{else}}dossier{{/if}} in output voor {{#if multi_instance}}een {{i_andere}} {{instantie_enkelvoud}}{{else}}een ander dossier{{/if}}.

**Nooit in de altijd-geladen laag**
- Geen persoonsgegevens, dossierinhoud of {{#if multi_instance}}{{instantie_enkelvoud}}details{{else}}details van derden{{/if}} in `_kern/` of `_kennis/`. Die horen in het werkdomein zelf, waar ze enkel geladen worden wanneer daar gewerkt wordt.

**Inbox**
- Bij een bestand waarvan bestandsnaam of type doet vermoeden dat het gevoelige inhoud bevat: eerst vragen wat het is en waar het hoort, dan pas lezen.

**Voorbeelden**
- Voorbeelden in `_voorbeelden/` worden geanonimiseerd bewaard wanneer ze informatie van derden bevatten. Namen vervangen door rollen ("de cliënt", "de tegenpartij"), cijfers afronden of weglaten.

**Wanneer {{naam}} iets vraagt dat hiermee botst**
- Benoem de botsing en vraag bevestiging voor je verder gaat.

---

*Bijwerken telkens er een nieuwe regel of een nieuw type gevoelige informatie opduikt.*
