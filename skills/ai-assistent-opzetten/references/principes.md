# De zeven principes achter de architectuur

Lees dit wanneer je een ontwerpkeuze moet verdedigen in het ontwerpvoorstel, of wanneer een klantsituatie niet in de beslisboom past en je zelf moet beslissen. De principes zijn de "waarom" achter elke regel in de templates. Volledige uitleg met voorbeelden staat in Michiel's blauwdruk: `_kennis/frameworks/2026-05-28-blauwdruk-cowork-setup-voor-ondernemers.md` in zijn werkfolder.

## 1. Werkdomein als eenheid van context

Een werkdomein is een afgebakende ruimte waarbinnen het werk inhoudelijk samenhangt: het eigen bedrijf, elke klant, elk dossier. Elk werkdomein heeft eigen context, eigen stijl, eigen lopend werk. Alles wat conditioneel geladen wordt, wordt geladen per werkdomein.

## 2. Meta in `_kern`, voice in werkdomein

`_kern/` is altijd geladen en bevat daarom enkel wat voor élk werk geldt: wie de ondernemer is als professional, werkregels, anti-patronen. Nooit de schrijfstem. Bij iemand die vooral voor anderen schrijft, lekt een stem in `_kern/` in al het klantwerk. Dat is de eerste fout die je wil vermijden, en de reden waarom `_voice.md` in het werkdomein zit en niet in `_kern/`.

## 3. Conditional loading als hardregel

Voice, context en voorbeelden worden pas geladen wanneer er in dat werkdomein gewerkt wordt, en voorbeelden enkel voor het kanaal van de huidige taak. Het voice-protocol in `CLAUDE.md` maakt dit hard: geen tekst zonder eerst te bepalen voor wie en op welk kanaal. Een LinkedIn-voorbeeld hoort niet in een mail te sijpelen.

## 4. Template-first voor schaalbaarheid

Elk patroon dat zich herhaalt (nieuwe klant, nieuw dossier) bestaat één keer als template en wordt gekopieerd. Zonder template wordt elke nieuwe instantie een ad-hoc structuur en breekt het systeem na drie klanten.

## 5. Identiteit, feiten en voice zijn drie verschillende dingen

Bij het vullen van de setup uit materiaal of kickoff-antwoorden: identiteitsvragen (wie ben ik, welke principes) formuleert de klant zelf. Feitenvragen (wat doe ik, USPs, doelgroep) mag AI voorstellen, klant bevestigt. Voice-werk doet AI uit materiaal, klant stuurt bij. Wie dit door elkaar haalt, krijgt een setup die niet doorleefd voelt of een invulproces dat eindeloos sleept.

## 6. Status-tracking en versioning voor werk over meerdere sessies

`SETUP-STATUS.md` houdt bij welke fase af is, zodat hervatten triviaal is. Kritieke files (`_kern/*`, `_context.md`, `_voice.md`, `_strategie.md`, `CLAUDE.md`) krijgen bij batch-updates een kopie in `_versies/` met datum-stamp. De klant kan zelf opruimen. Eén overschreven voice-file zonder backup en het vertrouwen is weg.

## 7. Trigger-driven onboarding

De setup start pas wanneer de klant `SETUP` typt. Niet automatisch bij elke sessie, niet als suggestie bij elke prompt. De klant mag eerst experimenteren zonder druk; de setup volgt wanneer ze eraan toe is.

---

## Wat hieruit volgt voor het ontwerpvoorstel

Wanneer je een afwijking van de standaard voorstelt, koppel ze aan een principe. "Vertrouwelijkheid aan omdat ze met medische dossiers werkt" is een gevolg van principe 2 en 3 (gevoelige context blijft in het werkdomein). "Lichte instantie-template omdat het werk per klant niet verschilt" is een gevolg van principe 1 (het werkdomein is dan het eigen bedrijf, niet de klant). Zo begrijpt Michiel niet alleen wát je voorstelt, maar ook waarom, en kan hij het uitleggen aan de klant.
