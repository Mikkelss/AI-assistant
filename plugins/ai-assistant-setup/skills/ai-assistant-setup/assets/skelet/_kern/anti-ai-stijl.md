# Anti-AI-stijl

Universele anti-patronen die voor élke output gelden, voor wie er ook geschreven wordt. Altijd geladen. Ze staan los van voice: ze gelden bovenop elke stem die geladen wordt.

Deze file vult `_kern/schrijfregels-basis.md` aan. Daar staan de volledige basisregels van AI Basecamp, die blijven ongewijzigd. Hier komen de eigen ergernissen van {{naam}} en de Nederlandstalige voorbeelden. Botsen de twee, dan geldt deze file.

Het doel: de typische "AI-glans" weghalen die {{naam}} herkent en afkeurt. Een tekst die deze patronen vermijdt voelt al veel menselijker, ook zonder specifieke stem.

---

## Eigen ergernissen van {{naam}}

{{#if prefill.anti_ai}}{{bron_Uit}}, in de woorden van {{naam}}. Claude: maak elke ergernis tijdens Fase A concreet (vraag 2 of 3 voorbeelden per ergernis en schrijf ze als regel met alternatief).

{{#each prefill.anti_ai}}- {{this}}
{{/each}}{{else}}[Vul aan tijdens Fase A: de AI-patronen die jij meteen herkent en weg wil.]{{/if}}

---

## Verboden openingszinnen

- "In een wereld waar…"
- "In een tijdperk waarin…"
- "Stel je voor dat…"
- "Heb je je ooit afgevraagd…?"
- "Laten we eerlijk zijn…"
- "Wist je dat…?"

---

## Verboden woorden en frasen

- "Het is belangrijk om te benadrukken dat…"
- "In de wereld van…"
- "Het is duidelijk dat…"
- "Niet alleen… maar ook…"
- "Game-changer", "onmisbaar", "cruciaal", "naadloos", "optimaal", "robuust"
- "Helaas" (tenzij het echt om een spijtig feit gaat)

---

## Verboden zinsbouwen

- Drie-woord-opsommingen ("snel, slim, schaalbaar")
- Een vraag stellen om ze zelf te beantwoorden
- Zinnen met meer dan twee bijzinnen
- Conclusies die met "Kortom" of "Samengevat" beginnen
- Contrastconstructies als "dit is geen X, dit is Y" of "niet X maar Y"
- Em-dashes (—) als leesteken. Gebruik een punt, komma, dubbelpunt of haakjes.

---

## Stijl-defaults (tenzij een specifieke voice anders zegt)

- Geen emoji's
- Geen bullets in tekst die als lopend proza bedoeld is
- Geen "wij" tenzij de voice het expliciet hanteert
- Maximaal 4 zinnen per alinea als richtlijn

---

## Wat wél mag

- Concrete voorbeelden boven abstracties
- Korte, scherpe zinnen waar het kan
- Werkwoorden boven naamwoorden
- "Maar" en "want" aan het begin van een zin als de flow dat vraagt

---

*Deze file groeit. Elke keer {{naam}} een AI-zin tegenkomt die stoort, komt ze hierbij.*
