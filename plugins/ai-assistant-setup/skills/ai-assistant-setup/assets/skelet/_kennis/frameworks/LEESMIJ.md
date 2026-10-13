# Frameworks

Hier komen de methodieken en modellen die {{naam}} hergebruikt{{#if multi_instance}} over {{instantie_meervoud_lower}} heen{{/if}}. Eén file per framework, met deze structuur:

```
# [Naam framework]

## Wat is het
[korte beschrijving]

## Wanneer gebruik ik het
[concrete situaties]

## De stappen
[stap voor stap]

## Voorbeelden
[1 of 2 toepassingen uit de praktijk]

## Bronnen
[link, boek, auteur]
```

{{#if frameworks_start}}{{bron_Uit}} kwamen deze frameworks naar voren. Per framework staat er al een stub klaar:
{{#each frameworks_start}}- `{{slug}}.md`: {{titel}}
{{/each}}{{/if}}
Deze map wordt niet automatisch geladen. Claude raadpleegt enkel wat relevant is voor de vraag van dat moment.
