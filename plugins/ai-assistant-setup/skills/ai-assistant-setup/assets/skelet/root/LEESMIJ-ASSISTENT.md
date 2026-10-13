# Je AI-assistent, {{naam}}

Dit document legt uit wat er in je map bijgekomen is en hoe het werkt. Voor jou, de mens. Claude heeft zijn eigen instructies in `CLAUDE.md`.

---

## Wat er veranderd is aan je mappen

Niets.

Je bestaande mappen en bestanden staan waar ze stonden, met dezelfde namen en dezelfde inhoud. Er zijn enkel een paar mappen en files bijgekomen, allemaal met een naam die begint met een liggend streepje of in hoofdletters. Zo zie je meteen wat van de assistent is en wat van jou.

Claude mag in je mappen lezen. {{#if bestaande_schrijven}}Een nieuwe file in een van je mappen zetten doet hij enkel na je akkoord. Iets overschrijven, hernoemen, verplaatsen of verwijderen doet hij nooit.{{else}}Schrijven, hernoemen, verplaatsen of verwijderen doet hij daar niet. Wat hij voor je maakt, komt in `{{projecten_map}}/`. Jij beslist waar het daarna naartoe gaat.{{/if}}{{#if buiten_bereik_obj}} Buiten bereik, ook om te lezen: {{#each buiten_bereik_obj}}`{{pad}}`{{sep}}{{/each}}.{{/if}}

---

## Begin hier

Open Cowork op deze map en typ:

> **SETUP**

Claude leest dan het setup-document en neemt de leiding. De eerste stap (Fase 0) doe je samen met {{coach_voornaam}}. Claude heeft je mappen en een selectie van je documenten al gelezen en legt je voor wat hij daarin vond. Daarna vraagt hij wat enkel jij weet. Welk document het goede voorbeeld is voor een taak, welke regels je volgt zonder dat ze ergens staan, welke mappen hij beter niet opent.

Je hoeft niet alles in één keer te doen. Typ je later opnieuw `SETUP`, dan weet Claude waar je gebleven was. Dat houdt hij bij in `SETUP-STATUS.md`.

---

## Wat is er bijgekomen

- `CLAUDE.md`: de instructies voor Claude. Hierin staat ook de tabel met je bestaande mappen en wat Claude ermee mag. Die tabel vul je samen aan in Fase 0.
- `SETUP-START-HIER.md` en `SETUP-STATUS.md`: de setup-guide en waar je staat.
- `_kern/`: wat altijd geldt. Wie jij bent als {{rol_label}}, je werkregels, de schrijffouten die je niet meer wil zien{{#if vertrouwelijkheid}}, wat vertrouwelijk is{{/if}}.
- `_kennis/`: referenties op afroep. Welk document het voorbeeld is voor welke taak, frameworks, templates.
- `_context/`: wat Claude moet weten over {{wd_lidwoord}} eigen {{werkdomein_lower}}{{#if multi_instance}} en over je {{instantie_meervoud_lower}}{{/if}}. Je stem, je strategie, afspraken die nergens anders staan.
- `{{inbox_map}}/`: dropzone voor files die je aan Claude wil geven.
- `{{projecten_map}}/`: wat Claude voor je maakt en werk in uitvoering.
- `_ai-setup/`: de werkbestanden van de setup zelf. Claude gebruikt ze niet tijdens het gewone werk.

---

## Hoe het werkt, in vier zinnen

1. `_kern/` wordt altijd geladen. Daar staat enkel wat voor elke taak geldt.
2. {{#if multi_instance}}Werk je voor een {{instantie_enkelvoud}}, dan leest Claude de bestanden in je eigen map van {{i_die}} {{instantie_enkelvoud}} en de afspraken in `{{instantie_map}}/[naam]/`.{{else}}Voor elke taak leest Claude de bestanden in je eigen mappen die erbij horen, plus de context in `{{eigen_map}}/`.{{/if}}
3. Voor een taak met een vast voorbeeld (een verslag, een template, een brief) kijkt Claude eerst in `_kennis/referentiedocumenten.md`.
4. Wat Claude maakt, landt in `{{projecten_map}}/`{{#if bestaande_schrijven}} of, na je akkoord, in je eigen map{{/if}}.

---

## Versioning en backup

**Versioning.** Past Claude een belangrijke file van de assistent aan (je stem, je context, je werkregels), dan bewaart hij eerst de oude versie in een `_versies/`-submap. Aan je eigen bestanden komt hij niet.

**Backup.** Je map krijgt geen nieuwe backup-regeling door deze assistent. Wat je vandaag doet, blijft gelden. Bespreek met {{coach_voornaam}} of de nieuwe mappen mee in je backup zitten.

---

## De assistent weghalen

Wil je stoppen, dan verwijder je `CLAUDE.md`, `LEESMIJ-ASSISTENT.md`, de twee setup-files en de mappen `_kern`, `_kennis`, `_context`, `{{inbox_map}}`, `{{projecten_map}}` en `_ai-setup`. Kijk eerst in `{{projecten_map}}/` of er nog iets in zit dat je wil houden. Je eigen mappen staan er dan nog precies zoals vandaag.

---

*Toegevoegd op {{aangemaakt_op}} door {{coach}}.*
