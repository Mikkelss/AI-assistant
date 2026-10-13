# Voice-analyse-protocol

Stap voor stap een `_voice.md` opbouwen voor {{wd_lidwoord}} eigen {{werkdomein_lower}}{{#if volledig}} of voor een {{instantie_enkelvoud}}{{/if}}. Doel: een file die concreet genoeg is dat AI niet meer terugvalt op zijn generieke schrijfstijl.

{{#if voice_laag}}Bij {{naam}} ligt de nadruk op register en structuur eerder dan op persoonlijkheid. Beschrijf dus vooral hoe elk type output opgebouwd is en welk register het heeft, en minder "wie ben ik als schrijver".

{{/if}}---

## Wat je nodig hebt

- Minimum 10 voorbeelden waarvan {{#if volledig}}de eigenaar van de stem{{else}}{{naam}}{{/if}} zegt "dit ben ik écht": {{kanalen_lijst}}.
- 3 tot 5 anti-voorbeelden: "dit ben ik absoluut niet".
- 30 tot 60 minuten (de eerste keer langer).

## Stap 1: verzamel en groepeer

Sorteer per kanaal. Houd de anti-voorbeelden apart.

## Stap 2: markeer wat opvalt

Per voorbeeld: hoe begint het, welk ritme (kort, lang, gemengd), aanspreekvorm, terugkerende woorden, humor of ernst, beelden en vergelijkingen, hoe eindigt het.

## Stap 3: destilleer regels

Schrijf 8 tot 15 regels die de stem beschrijven. Het soort regel dat werkt:

- "Openingszin is altijd een concreet feit, nooit een vraag."
- "Drie korte zinnen, dan één lange. Dat ritme komt overal terug."
- "In mails altijd 'je', in formele stukken 'u'."
- "Beelden komen uit de praktijk van de lezer, niet uit sport of oorlog."

Vage regels als "informeel" of "menselijk" zijn nutteloos voor AI. Schrap ze.

## Stap 4: destilleer verboden

Uit de anti-voorbeelden: welke openingen nooit, welke woorden taboe, welke zinsbouwen vreemd. Concreet opschrijven als don'ts.

## Stap 5: signature-moves

Wat doet deze schrijver dat niemand anders doet? Eén of twee patronen waaraan je een tekst meteen herkent. Een vaste afsluiter, een typische wending, een woord dat niemand anders zo gebruikt.

## Stap 6: schrijf `_voice.md`

Vul de secties van de bestaande `_voice.md` in het werkdomein: in één zin, vorm en ritme, woordkeuze, verboden, signature-moves, voorbeelden wel, voorbeelden niet.

## Stap 7: verdeel de voorbeelden

Zet de wel-voorbeelden per kanaal in `_voorbeelden/[kanaal]/`, één file per voorbeeld, naam `YYYY-MM-DD-korte-beschrijving.md`, met bovenaan de datum en waarom dit een goed voorbeeld is. Streef naar 3 tot 10 per actief kanaal. Kanalen waarop niet gewerkt wordt blijven leeg.

## Stap 8: test

Laat Claude één stuk output schrijven voor één kanaal, met enkel `_voice.md`, `_context.md` en `_voorbeelden/[dat kanaal]/` geladen. Lees kritisch. Wat voelt nog "AI"? Voeg een regel of verbod toe, of een sterker voorbeeld. Test opnieuw. 3 tot 5 rondes per kanaal. Een stem die werkt voor {{eerste_kanaal_label}} werkt niet automatisch voor {{tweede_kanaal_label}}.

---

## Onderhoud

`_voice.md` is geen statisch document. Elke output die niet klopt is een aanleiding om te kijken welke regel ontbrak. Na 5 tot 10 rondes zit een stem meestal stabiel. Meer voorbeelden toevoegen werkt vaak beter dan meer regels.
