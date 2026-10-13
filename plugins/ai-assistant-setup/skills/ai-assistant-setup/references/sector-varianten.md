# Sector-varianten: welke knoppen verschuiven

Per sectortype de typische config-keuzes. Gebruik dit als startpunt, niet als wet: de kickoff-antwoorden gaan altijd voor. Wanneer een klant in geen enkele variant past, combineer je de dichtstbijzijnde en leg je in het ontwerpvoorstel uit wat je gekozen hebt.

Elke variant geeft: werkdomein-naam, instantie-naam, template-type, kanalen, recurring-mappen, vertrouwelijkheid, sparring, en waar de nadruk typisch ligt.

---

## Marketing-bureau, social media manager, contentbureau

De referentie-case (Kiara). Het werk verschilt sterk per klant: andere stem, andere strategie, andere kanalen.

```
werkdomein_eigen:      Eigen bedrijf
instantie:             Klanten / klant
instantie_template:    volledig
kanalen:               linkedin, instagram, facebook, nieuwsbrief, mail, website, ads
recurring_mappen:      posts, ads, analyses
projecten_per_instantie: true
vertrouwelijkheid:     false (tenzij klanten in zorg, finance of HR)
sparring:              meestal true (strategie per klant)
voice_gewicht:         hoog
fase_nadruk:           voice
```

Aandachtspunt: voorbeelden per kanaal zijn hier de hefboom. Zonder 3 tot 10 voorbeelden per actief kanaal per klant blijft de output generiek.

---

## Copywriter, tekstschrijver, ghostwriter

Zeer dicht bij het marketingbureau, maar vaker één kanaal per klant en meer langere vormen.

```
werkdomein_eigen:      Eigen bedrijf
instantie:             Klanten / klant  (soms Opdrachten / opdracht bij kortlopend werk)
instantie_template:    volledig
kanalen:               linkedin, blog, website, nieuwsbrief, mail, casestudy, whitepaper
recurring_mappen:      teksten, briefings, feedback
projecten_per_instantie: true
vertrouwelijkheid:     false, tenzij ghostwriting onder NDA
sparring:              soms (positionering, tone-of-voice-advies)
voice_gewicht:         hoog
fase_nadruk:           voice
```

Aandachtspunt: bij ghostwriting is de "voice" die van een persoon, niet van een bedrijf. `_voice.md` per instantie beschrijft dan een mens, en `_voorbeelden/` bevat teksten die die persoon zelf schreef of goedkeurde.

---

## Advocaat, jurist, notaris (solo of klein kantoor)

De feiten verschillen volledig per dossier, de stem niet: die is van de advocaat. Wat wél sterk verschilt is het register per documenttype (een conclusie tegenover een mail aan de cliënt). Daarom: lichte dossier-template, en het register zit in de eigen `_voice.md` onder "Register per kanaal". Dit is bijgesteld na de eerste testronde; de eerste versie schreef "volledig" voor, en dat bleek 35 keer dezelfde `_voice.md` op te leveren.

```
werkdomein_eigen:      Eigen kantoor  (of Eigen praktijk; let op het lidwoord: het kantoor, de praktijk)
instantie:             Dossiers / dossier  (het-woord: dit dossier, een nieuw dossier)
instantie_template:    licht  (volledig enkel als de advocaat per dossier écht anders schrijft, zeldzaam)
kanalen:               procedurestuk, pleitnota, advies, brief, mail, overeenkomst
recurring_mappen:      stukken, briefwisseling, adviezen  (of: correspondentie, nota's)
projecten_per_instantie: true (elke procedurefase is een project)
vertrouwelijkheid:     true, altijd
sparring:              true (procedurestrategie, argumentatie)
voice_gewicht:         midden (register belangrijker dan persoonlijkheid)
fase_nadruk:           strategie of proces
```

Aandachtspunten:
- `_kern/vertrouwelijkheid.md` is hier geen optie maar een must: geen cliëntnamen in output buiten de dossiermap, geen dossierinhoud in `_kennis/` of `_kern/`, inbox-protocol vraagt eerst vóór het leest. Bij dossiers met minderjarigen of huiselijk geweld: extra regels (adres nergens vermelden).
- In de customisatie-pass: een termijnenoverzicht-template in `_kennis/templates/` als vervanger van de content-kalender, en in `_strategie.md` van het dossier een termijnentabel. Regel: Claude berekent geen termijnen en zet geen datum in een tekst die niet in die tabel staat.
- Elk stuk dat Claude opstelt krijgt bovenaan een markering zoals `ONTWERP, na te kijken door [naam]` tot de advocaat ze weghaalt. En alles wat Claude zelf aanbrengt (rechtspraak, wetsartikelen, feiten die niet in het dossier staan) krijgt `[na te kijken]`. Dat is de tegenmaatregel voor het bekende probleem dat AI rechtspraak verzint.
- De `_context.md` van de lichte template heeft "Gevoeligheden eerst" bovenaan. Voor een advocaat is dat de juiste volgorde.

---

## Coach, therapeut, begeleider

Het werk verschilt per cliënt in inhoud, maar minder in stem. De output is vooral verslagen, opvolgmails en materiaal voor de cliënt.

```
werkdomein_eigen:      Eigen praktijk
instantie:             Cliënten / cliënt
instantie_template:    licht (de stem is die van de coach; het verschil per cliënt zit in de inhoud)
                       volledig enkel als de coach per cliënt in een andere stem schrijft, wat zelden voorkomt
kanalen:               intake, verslag, mail, evaluatie, oefening, presentatie
recurring_mappen:      sessies, evaluaties, materiaal
projecten_per_instantie: false (het traject zelf is het project; enkel true bij duidelijke deelprojecten)
vertrouwelijkheid:     true bij therapeutisch of persoonlijk werk; bij zuiver business-coaching afwegen
sparring:              true (reflectie op de eigen aanpak, voorbereiding van sessies)
voice_gewicht:         laag tot midden
fase_nadruk:           proces
```

Aandachtspunt: de "voice" is hier vooral gespreksvoering en verslagstijl. `_voice.md` beschrijft hoe verslagen klinken (u of jij, directief of open, lengte), niet een merkstem. `_kennis/frameworks/` wordt vroeg belangrijk (GROW, systemisch werk, eigen modellen).

---

## Consultant, adviseur, interim-manager

Het werk verschilt per opdracht in inhoud, de methode is vaak dezelfde. Output is rapport-zwaar.

```
werkdomein_eigen:      Eigen bedrijf
instantie:             Klanten / klant  of  Opdrachten / opdracht (vraag het, bij langlopend "klant", bij projectmatig "opdracht")
instantie_template:    volledig bij lange trajecten met eigen stakeholders; licht bij korte, methodische opdrachten
kanalen:               rapport, presentatie, advies, mail, verslag, offerte
recurring_mappen:      deliverables, werksessies, analyses
projecten_per_instantie: true
vertrouwelijkheid:     vaak true (NDA's, interne cijfers)
sparring:              true, dit is de hoofd-use-case
voice_gewicht:         midden
fase_nadruk:           strategie
```

Aandachtspunt: `_kennis/frameworks/` is hier de kern van het systeem. De consultant leeft van zijn methode; die hoort als eerste gedocumenteerd. `stakeholders_per_instantie` is bijna altijd true; benoem in het ontwerpvoorstel dat een `relaties/`-submap per opdracht later kan.

---

## Boekhouder, accountant, fiscalist

Veel klanten, weinig variatie in stem, veel variatie in feiten. Lichte instantie-template.

```
werkdomein_eigen:      Eigen kantoor
instantie:             Klanten / klant  (soms Dossiers)
instantie_template:    licht
kanalen:               mail, brief, advies, rapport, checklist
recurring_mappen:      kwartaal, jaarafsluiting, correspondentie
projecten_per_instantie: false (tenzij overnames, herstructureringen)
vertrouwelijkheid:     true, altijd (financiële gegevens)
sparring:              soms (fiscale optimalisatie, adviesvoorbereiding)
voice_gewicht:         laag
fase_nadruk:           proces
```

Aandachtspunt: de waarde zit in de procesbeschrijvingen en checklists in `_kennis/`, niet in de voice. Overweeg `recurring_mappen` te koppelen aan de fiscale kalender.

---

## Architect, interieurontwerper, studio

Per project een eigen context, stem is die van de studio.

```
werkdomein_eigen:      Eigen studio  (of Eigen bureau)
instantie:             Projecten / project  → gebruik "Opdrachten" voor map 2. om verwarring met 9. Projecten te vermijden, en leg dat uit
instantie_template:    licht
kanalen:               nota, mail, presentatie, offerte, verslag, website
recurring_mappen:      correspondentie, verslagen, documenten
projecten_per_instantie: false (de opdracht is het project)
vertrouwelijkheid:     soms (bouwheren willen discretie)
sparring:              soms (conceptontwikkeling)
voice_gewicht:         midden
fase_nadruk:           proces
```

---

## Creatieve solo met eenmalige opdrachten (fotograaf, videomaker, illustrator, grafisch ontwerper)

Veel klanten per jaar, bijna allemaal eenmalig, en elke opdracht verloopt hetzelfde: aanvraag, offerte, briefing, uitvoering, levering. Het enige wat verschilt past in één file. Dan geen instantielaag; elke opdracht wordt één file in een recurring-map van het eigen werkdomein.

```
werkdomein_eigen:      Eigen studio  (de studio)
multi_instance:        false  (zie beslisboom, uitkomst A, tweede geval)
kanalen:               instagram, mail, offerte, website  (+ linkedin of nieuwsbrief als ze die echt gebruiken)
recurring_mappen:      shoots (of opdrachten), offertes, posts
vertrouwelijkheid:     false, met portretrecht en "tarieven niet doortonen" als werkregels
sparring:              meestal false
voice_gewicht:         midden (Instagram en mails moeten klinken als de maker, offertes vooral duidelijk)
fase_nadruk:           proces
```

Aandachtspunten:
- Zodra `offerte` een kanaal is, zet het script de prijsregel aan: prijzen enkel uit de tarieflijst in `_context.md`. Zorg dat die tarieflijst in Fase A gevuld wordt, want dat is de tegenmaatregel voor AI-offertes met verzonnen prijzen.
- Een `shoot-template.md` of `opdracht-template.md` in `_kennis/templates/` (aanvraag, briefing, datum, locatie, aantal, prijs, status, akkoord fotogebruik) is hier het planningsinstrument. Maak het in de customisatie-pass.
- Fase C en D vallen weg. Die tijd gaat naar de offerte-flow en een vroege skill (offerte in 5 minuten, leveringsmail).

---

## Wanneer geen variant past

Stel jezelf drie vragen, in deze volgorde:

1. **Verschilt de stem per instantie?** Ja → volledig template. Nee → licht.
2. **Is er een geheimhoudingsplicht of zijn er persoonsgegevens van derden?** Ja → vertrouwelijkheid aan.
3. **Waar zit de pijn: schrijven, denken of herhalen?** → fase_nadruk voice, strategie of proces.

Met die drie antwoorden en de woorden van de klant voor werkdomein, instantie en recurring-mappen heb je 80% van de config. De rest zijn details die tijdens de customisatie-pass en de eerste sessie vanzelf scherper worden.
