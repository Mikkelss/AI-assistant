# Intake-vragenlijst: {{i_nieuwe}} {{instantie_enkelvoud}}

Te doorlopen bij {{i_elke}} {{i_nieuwe}} {{instantie_enkelvoud}}. De antwoorden vormen de basis voor `_context.md`{{#if volledig}}, `_voice.md`{{/if}} en `_strategie.md` in de map van {{i_die}} {{instantie_enkelvoud}}.

Deze vragen zijn een startpunt. Pas ze aan aan wat jij in jouw vak écht moet weten voor je kan beginnen.

---

## 1. Wie

1. Wie is {{i_deze}} {{instantie_enkelvoud}}? Naam, wat ze doen, sinds wanneer, hoe groot.
2. Wie is mijn contactpersoon? Wie beslist? Wie moet ik nog kennen?
3. Hoe zijn ze bij mij terechtgekomen?

## 2. Wat en waarom

4. Wat is de vraag of het probleem waarvoor ze bij mij komen?
5. Wat willen ze bereikt hebben over 3 maanden? Over een jaar?
6. Wat hebben ze al geprobeerd? Wat werkte, wat niet?
7. Wat is het grootste risico of de grootste frustratie vandaag?

## 3. Context

8. Wat moet ik weten over hun situatie dat niet in de vraag zelf zit? (markt, geschiedenis, gevoeligheden, interne dynamiek)
9. Wat onderscheidt hen van vergelijkbare {{instantie_meervoud_lower}}? Concreet.
10. Zijn er dingen die absoluut niet mogen of niet gezegd mogen worden?

{{#if volledig}}## 4. Stem en stijl

11. Welke 3 tot 5 woorden beschrijven hun toon?
12. Welke woorden of uitdrukkingen gebruiken ze nooit?
13. Spreken ze hun publiek aan met "jij", "je" of "u"?
14. Lever per kanaal waar ze actief zijn 5 tot 10 voorbeelden van output die écht hen is: {{kanalen_lijst}}.
15. Lever 2 of 3 voorbeelden van wat ze absoluut niet zijn.
16. Op welke kanalen zijn ze actief en op welke niet?

## 5. Praktisch

17. Via welke kanalen werken we samen? Hoe vaak?
18. Welke tools of toegangen heb ik nodig?
19. Wie tekent af? Hoeveel iteraties zijn realistisch?
20. Hoe willen ze rapportering, en hoe vaak?
{{else}}## 4. Praktisch

11. Via welke kanalen werken we samen? Hoe vaak?
12. Welke documenten, toegangen of gegevens heb ik nodig om te starten?
13. Wie tekent af? Zijn er deadlines?
14. Hoe willen ze op de hoogte gehouden worden?
{{/if}}
---

*Eens beantwoord: gebruik dit om `_context.md`{{#if volledig}}, `_voice.md` (samen met `voice-analyse-protocol.md`){{/if}} en `_strategie.md` te vullen in `{{instantie_map}}/[naam]/`.*
