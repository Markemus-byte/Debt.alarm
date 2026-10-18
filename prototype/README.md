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

## Kjør testene / Run the tests

Krever bare Python 3.10 eller nyere. Needs only Python 3.10 or newer.

```
cd prototype
python3 -m unittest -v
```
