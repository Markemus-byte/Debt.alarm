# Prototype: Stilleflagget

En enkel modell av reglene i [forslaget](../docs/forslag.md) og [det tekniske konseptet](../docs/teknisk-konsept.md). Den er laget for diskusjon og testing av reglene, ikke for bruk i drift.

A simple model of the rules in the proposal and the technical concept. It is meant for discussing and testing the rules, not for production use.

## Hva den viser / What it shows

- Et stilleflagg kan bare settes etter 60 dager uten kontakt eller betaling, og gjelder personen på tvers av kreditorer.
- Gebyrer stoppes i maksimalt 6 måneder, og stoppet opphører når kontakt er oppnådd.
- Pauseflagg kan settes uten begrunnelse, og bare den som satte dem kan fjerne dem.
- Oppslag krever en aktiv sak, viser bare ja/nei og dato, og logges.
- Velferdssjekk utløses én gang etter 90 dager med åpent flagg.
- Kostnader etter dødsdatoen faller bort.
- Lukkede flagg slettes etter 12 måneder, og fødselsnummer lagres aldri, bare et pseudonym.

## Regnestykket for fristen / The freeze calculation

`fryseregnestykke.py` regner ut tallene i [fortjeneste og frist](../docs/fortjeneste-og-frist.md): hva som legges på kravet til en som aldri svarer, med og uten stilleflagg, og en øvre grense for hva en frys koster bransjen. Fristene hentes fra `stilleflagg.py`, så de to modellene alltid bruker de samme reglene. Testene låser tallene som står i dokumentet. Endres en sats eller en regel, feiler testene, og dokumentet må oppdateres.

`fryseregnestykke.py` computes the figures in the profits document: what is added to the claim of someone who never answers, with and without a silence flag, and an upper bound on what a freeze costs the industry. It takes the time limits from `stilleflagg.py`. The tests pin the figures quoted in the document, so a change in a rate or rule makes them fail until the document is updated.

```
cd prototype
python3 fryseregnestykke.py
```

## Kjør testene / Run the tests

Krever bare Python 3.10 eller nyere. Needs only Python 3.10 or newer.

```
cd prototype
python3 -m unittest -v
```
