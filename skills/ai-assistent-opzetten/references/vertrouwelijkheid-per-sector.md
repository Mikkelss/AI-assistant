# Vertrouwelijkheid per sector

Het skelet zet in `_kern/vertrouwelijkheid.md` een generieke set defaults. Per sector horen daar vaste blokken bij die anders elke keer opnieuw geschreven worden, met variatie in kwaliteit. Neem het blok van de sector over in de customisatie-pass (stap 6), zet de regels van de klant erboven, en houd het geheel op één pagina.

Alle blokken delen drie principes: gevoelige inhoud blijft in het werkdomein en komt nooit in `_kern/` of `_kennis/`; de inbox vraagt vóór het leest; wat Claude zelf aanbrengt en niet uit de bron komt, krijgt een markering.

---

## Advocaat, notaris, jurist

- Beroepsgeheim en deontologie van de Orde gaan voor op elke andere regel in deze omgeving.
- Namen van cliënten, tegenpartijen en kinderen enkel in de dossiermap zelf. Nooit in `_kern/`, `_kennis/`, voorbeelden of teksten die naar buiten gaan buiten de stukken.
- Dossiers met minderjarigen: extra terughoudend met details in samenvattingen. Dossiers met huiselijk geweld: het adres van de cliënt nergens, ook niet in samenvattingen van binnengekomen stukken; waar een stuk een adres vraagt, kantooradres met `[VRAAG]`.
- Rechtspraak, wetsartikelen en termijnen die niet uit het dossier of uit `_kennis/` komen, krijgen `[na te kijken]`. Claude berekent geen termijnen.
- Elk stuk dat Claude opstelt draagt bovenaan `ONTWERP, na te kijken door [naam]` tot de advocaat ze weghaalt.
- Bewaartermijnen en wat er gebeurt bij een datalek: `[na te kijken door de advocaat]`, want dat hangt af van kantoor en balie.

## Coach, therapeut, begeleider

- Wat in een sessie gezegd wordt, gaat niet naar de opdrachtgever (werkgever, HR) tenzij de cliënt het gezien en goedgekeurd heeft. Elke tekst voor een opdrachtgever krijgt `CONCEPT, nog niet gedeeld met de cliënt` tot dat gebeurd is.
- Cliënten die gestuurd zijn door hun werkgever: extra voorzichtig met wat naar die werkgever gaat. Bij twijfel: vragen.
- Geen herkenbare casussen in posts of nieuwsbrieven, ook niet geanonimiseerd als de situatie herkenbaar blijft. Claude voegt onder elke post die uit een echte situatie komt een herkenbaarheidscheck toe.
- Transcripten (Otter, Fireflies) zijn bronmateriaal: één keer lezen voor het verslag, daarna niet meer citeren. De ethische code van de beroepsvereniging (ICF, VVCEPC, …) gaat voor.
- Toestemming van cliënten voor AI-verwerking van sessiemateriaal: `[na te kijken door de coach]`.

## Boekhouder, accountant, fiscalist

- Financiële gegevens van een klant blijven in de klantmap. Geen cijfers van klant A in een tekst voor klant B, ook niet als voorbeeld of benchmark.
- Rijksregisternummers, rekeningnummers en loongegevens nooit in voorbeelden, samenvattingen of `_kennis/`.
- Fiscale bedragen, drempels en termijnen die niet uit de klantmap of uit `_kennis/` komen, krijgen `[na te kijken]`. Claude rekent niet zelf een aangifte uit.
- Adviezen krijgen `ONTWERP` tot de boekhouder ze nakeek.
- Beroepsgeheim en GDPR gaan voor. Wat bij een datalek moet gebeuren: `[na te kijken]`.

## Consultant, adviseur, interim-manager

- NDA's per opdracht gaan voor: wat onder NDA valt, blijft in de opdrachtmap en komt nooit in voorbeelden, frameworks of teksten voor een andere opdrachtgever.
- Interne cijfers, namen van medewerkers en organisatiegevoeligheden enkel in de opdrachtmap.
- Aanbevelingen die Claude formuleert zonder onderbouwing uit de opdrachtmap krijgen `[aanname]`.
- Rapporten en presentaties dragen `ONTWERP` tot de consultant ze nakeek.

## Marketeer, copywriter, creatieve solo (meestal géén vertrouwelijkheid.md)

Hier volstaat meestal een regel of twee onder "Veiligheid" in `_kern/werkregels.md`; het script zet ze daar automatisch wanneer `vertrouwelijkheid_regels` gevuld is en de vlag uit staat:

- Cijfers en interne informatie van klant A nooit bij klant B.
- Portretrecht: foto's en namen van klanten niet gebruiken als voorbeeld zonder akkoord.
- Tarieven van de ene klant niet tonen aan de andere.

Zet `vertrouwelijkheid` wél aan wanneer de klanten van de marketeer zelf in zorg, finance of HR zitten, want dan komt hun gevoelige materiaal in de omgeving terecht.

---

## Wat in elke ontwerpnotitie hoort bij `vertrouwelijkheid` true

Een vast punt onder "Aandachtspunten voor de eerste sessie": wat gebeurt er met de data. Concreet: onder welk Claude-plan werkt de klant, wordt er getraind op de gegevens, is er een verwerkersovereenkomst nodig, en wat zegt de beroepsvereniging over AI-tools. Michiel hoort het antwoord klaar te hebben vóór de eerste sessie, want de klant gaat het vragen.
