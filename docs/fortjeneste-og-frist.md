# Hva tjener inkassoselskapene, og hva koster en frys?

*Versjon 1, oktober 2026. Underlag for fristen på 60 dager i [forslaget](forslag.md). Bygger på [analysen](analyse.md). English version below.*

Spørsmålet: Hvis selskapene tjener godt på folk som ikke klarer å svare, hvor lenge skal vi la gebyrene løpe før stilleflagget slår inn? Og vil selskapene fortsatt tjene penger hvis gebyrene fryses etter to måneder?

Alle tall er hentet fra offentlige kilder 28. oktober 2026, og tallene fra Finanstilsynet og Finans Norge ble kontrollert på nytt 2. november 2026 (se Kilder). Regnestykkene i del 4 og 5 er **anslag** bygget på forutsetninger vi har valgt selv. De er merket, og koden ligger i [prototype/fryseregnestykke.py](../prototype/fryseregnestykke.py), så alle kan kjøre dem med andre tall.

## Kort oppsummert

- **Skyldnerne betaler milliarder.** I 2024 betalte skyldnere i Norge 3,28 mrd kr i forsinkelsesrenter, 2,93 mrd kr i inkassokostnader og 0,72 mrd kr i rettslige kostnader, til sammen ca. 6,9 mrd kr i tillegg til selve gjelden.
- **Renten er den store posten.** Ved utgangen av 2025 var 40 mrd kr av forbrukernes inkassogjeld påløpte renter, mot 67 mrd kr i opprinnelig gjeld.
- **De norske inkassoselskapene selv har tynne marginer.** Bransjen hadde 5,09 mrd kr i inntekter og 4,89 mrd kr i kostnader i 2024. De ni selskapene vi så på hadde til sammen 14,4 mrd kr i inntekter over fem år, men bare 0,18 mrd kr i samlet overskudd. Fortjenesten samler seg hos dem som **eier** gjelden (for eksempel Axactor Capital AS, med ca. 49 % overskuddsgrad) og i konsernene i utlandet.
- **En frys koster lite.** For en stille person med 5 000 kr i gjeld halverer stilleflagget det som legges på før velferdssjekken (762 kr mot 1 513 kr ved dag 150). For hele bransjen er tapet høyst 0,1 til 0,4 mrd kr i året, selv om opptil hver femte krone kom fra stille skyldnere. For inkassoselskapenes egne inntekter er virkningen under 1 %.
- **Fristen avgjøres av menneskene, ikke av pengene.** Om flagget kommer etter 30, 45, 60 eller 90 dager utgjør bare noen hundrelapper per sak. Det viktige er at flagget kommer **før** salæret dobles (tidligst rundt dag 57), slik forslaget allerede krever.

## 1. Hva skyldnerne betaler: hele bransjen

Tall fra Finanstilsynets inkassostatistikk. Mrd kr.

| År | Foretakenes inntekter i alt | Herav inkassoinntekter | Foretak med underskudd | Nye inkassosaker | Innbetalt av skyldnere | Herav renter | Herav utenrettslige kostnader | Herav rettslige kostnader |
|---|---|---|---|---|---|---|---|---|
| 2021 | ikke oppgitt | 3,5 | 18 | ikke oppgitt | ikke oppgitt for helår | | | |
| 2022 | ikke oppgitt | 3,3 | 21 | 10,66 mill. | 46,47 | 2,79 | 2,72 | 0,72 |
| 2023 | ikke oppgitt | 3,3 | 28 (41 %) | 10,47 mill. | 46,51 | 2,85 | 2,83 | 0,73 |
| 2024 | 5,09 | 3,82 | 20 (31 %) | 11,70 mill. | 51,17 | 3,28 | 2,93 | 0,72 |
| 2025 | 5,01 | 3,87 | 17 (27 %) | 11,74 mill. | ikke oppgitt ennå | | | |

- I 2024 var kostnadene 4,89 mrd kr. Inntekter minus kostnader blir da ca. 0,2 mrd kr (vår utregning).
- Ca. 78 % av de nye sakene gjelder forbrukere.
- Forbrukernes inkassogjeld ved utgangen av 2025: 67,1 mrd kr i hovedstol og 40,0 mrd kr i påløpte renter, av 117,7 mrd kr totalt.
- De ti største foretakene hadde 85 til 86 % av all gjeld til inndriving i 2020 til 2022 (Finanstilsynet har ikke oppgitt dette senere).
- Oppkjøpte krav (gjeld selskapene har kjøpt og eier selv): 407 164 saker med 18,8 mrd kr i opprinnelig hovedstol ved utgangen av 2024.
- Første halvår 2026: 6,32 millioner nye saker (+6,3 %) og 2,74 mrd kr i inntekter (+7,2 %).

## 2. De største selskapene i Norge

Tall fra årsregnskapene i Brønnøysundregistrene, slik Proff viser dem. Mill. kr, summert over årene som er oppgitt. Dette er de norske selskapene alene, ikke konsernene.

| Selskap (org.nr) | År | Driftsinntekter | Driftsresultat | Årsresultat | Overskuddsgrad |
|---|---|---|---|---|---|
| Intrum AS (835 302 202) | 2021–2025 | 4 398 | 123 | 146 | 3 % |
| Kredinor AS (927 901 048) | 2022–2025 | 2 979 | −530 | −638 | −21 % |
| Lowell Norge AS (848 579 122) | 2020–2024 | 1 494 | 10 | 96 | 6 % |
| PRA Group Europe AS (960 545 397) | 2021–2025 | 1 296 | −97 | −325 | −25 % |
| Axactor Capital AS (917 983 747) | 2021–2025 | 1 220 | 972 | 600 | 49 % |
| Riverty Services Norway AS (957 294 227) | 2021–2025 | 1 055 | 385 | 331 | 31 % |
| Lowell AS (979 683 529) | 2021–2025 | 850 | 74 | −148 | −17 % |
| Axactor Norway AS (911 831 392) | 2021–2025 | 696 | 49 | 62 | 9 % |
| Sergel Norge AS (984 272 170) | 2021–2025 | 434 | 60 | 55 | 13 % |
| **Sum** | | **14 423** | | **180** | **1 %** |

År for år:

| Selskap | 2021 | 2022 | 2023 | 2024 | 2025 |
|---|---|---|---|---|---|
| Intrum AS, årsresultat | 47 | −16 | −43 | 11 | 146 |
| Kredinor AS, årsresultat | | −45* | −545 | −380 | 331 |
| Lowell Norge AS, årsresultat | 37 | 28 | −1 | −23 | ikke publ. |
| Axactor Capital AS, årsresultat | 154 | 198 | 219 | −88 | 118 |
| Riverty Services Norway AS, årsresultat | 70 | 77 | 58 | 68 | 59 |
| PRA Group Europe AS, årsresultat | −182 | −111 | −48 | 34 | −17 |

\* Kredinors første regnskapsår gikk fra 22.09.2021 til 31.12.2022. Lowell Norge AS hadde 54 mill. kr i årsresultat i 2020.

Hva tabellen viser:

- **Inkasso som tjeneste gir lite overskudd i Norge.** Flere av de store har gått med underskudd flere år på rad. Vi har ikke undersøkt hvorfor (for eksempel nedskrivninger eller betalinger til konsernet), og regnskapene alene viser ikke hvor pengene ender i et konsern. Kredinor oppga for eksempel en nedskrivning på 85 mill. kr i tredje kvartal 2024.
- **Å eie gjelden er lønnsomt.** Axactor Capital AS, som eier gjelden Axactor har kjøpt i Norge, hadde et driftsresultat på 150–227 mill. kr i året, mens lønnskostnadene var bare 1,9–3,3 mill. kr i året. Når selskapet eier kravet, går også renten til selskapet.
- **Konsernene er store.** Axactor ASA hadde 258 mill. euro i inntekter og 125 mill. euro i driftsresultat i 2025 (2024: underskudd på 79 mill. euro). Intrum AB hadde 17,0 mrd svenske kroner i inntekter og 5,3 mrd i justert driftsresultat i 2025. Intrums tall for 2020 til 2024 kunne vi ikke hente.

Påstanden om at selskapene «tjener mange milliarder» stemmer for konsernene og for summen skyldnerne betaler. Den stemmer ikke for de norske inkassoselskapenes egne overskudd, og prosjektets tekster skiller derfor mellom hva skyldnerne betaler og hvem som sitter igjen med fortjenesten. Argumentet for stilleflagget blir likevel sterkere, ikke svakere: pengene kommer fra skyldnerne, og en frys tar bare en liten bit av dem.

## 3. Hvordan gebyrene vokser for en som ikke svarer

Gjeldende regler i 2026 (inkassosats 750 kr, kreditor med fradrag for merverdiavgift). Dagene telles fra inkassovarselet.

| Dag | Hva skjer | Hva legges på (krav på 5 000 kr) |
|---|---|---|
| −14 | Regningen forfaller (vår forutsetning) | forsinkelsesrente 12,25 % i året begynner å løpe, ca. 1,70 kr per dag |
| 0 | Inkassovarsel | 38 kr |
| 14 | Betalingsoppfordring med betalingsfrist på minst 14 dager | lett salær 600 kr |
| 57 | Fristen er oversittet med mer enn 28 dager | salæret kan dobles («tungt salær»): +600 kr |
| ca. 180 | Første rettslige skritt (vår forutsetning) | rettsgebyr 1 345 kr til staten, pluss salær vi ikke har tatt med |

Salær etter kravets størrelse (lett / tungt): til 1 000 kr: 262,50 / 525; til 10 000 kr: 600 / 1 200; til 50 000 kr: 1 200 / 2 400. Uten fradragsrett for kreditor er satsene 25 % høyere.

Finanstilsynet skriver: «Dersom skyldneren oversitter betalingsfristen i en betalingsoppfordring med mer enn 28 dager, kan inkassoforetaket doble dette salæret» ([oversikt over inndrivingskostnader](https://finanstilsynet.no/forbrukerinformasjon/inkassovirksomhet/oversikt-over-utenrettslige-inndrivingskostnader)). Med betalingsoppfordring på dag 14 og 14 dagers frist blir det tidligst dag 57.

## 4. Regnestykke: én stille skyldner

**Anslag.** Personen svarer aldri. Flagget fryser nye gebyrer, renter og rettslige skritt i opptil 6 måneder, slik forslaget sier. Ved dag 150 er det gått 90 dager etter et flagg på dag 60, altså tidspunktet for velferdssjekken.

Påløpt ved dag 150, krav på 5 000 kr (ingen rettsgebyr ennå, fordi første rettslige skritt er satt til dag 180):

| Flagg settes | Salær | Varsel | Rente | Sum lagt på |
|---|---|---|---|---|
| Aldri (dagens regler) | 1 200 | 38 | 275 | **1 513** |
| Dag 30 | 600 | 38 | 74 | 712 |
| Dag 45 | 600 | 38 | 99 | 737 |
| Dag 60 | 600 | 38 | 124 | **762** |
| Dag 90 | 600 | 38 | 175 | 813 |
| Dag 60, uten regelen om flagg før tungt salær | 1 200 | 38 | 124 | 1 362 |

Samme regnestykke for 20 000 kr: 3 539 kr uten flagg, 1 735 kr med flagg på dag 60. For 1 000 kr: 618 kr mot 325 kr.

Etter 12 måneder, hvis personen fortsatt er stille og fryseperioden er over, er forskjellen mindre: 3 219 kr uten flagg mot 2 914 kr med flagg (5 000 kr). Begge tallene inkluderer rettsgebyret på 1 345 kr, som går til staten. Gebyrene er da bare **utsatt**. Det eneste som faller helt bort er renten i de seks månedene frysen varer, pluss alt som ville påløpt etter en dødsdato.

Det viktigste regnestykket viser: **forskjellen mellom å flagge på dag 30 og dag 90 er bare ca. 100 kr for et krav på 5 000 kr** (ca. 400 kr for 20 000 kr), og alt er rente. Den store forskjellen er om det tunge salæret og de rettslige skrittene kommer før noen har sjekket om personen har det bra.

## 5. Regnestykke: hele bransjen

**Anslag.** Ingen vet hvor stor del av pengene som kommer fra folk som har vært helt stille i 60 dager. Vi regner derfor på tre nivåer: 5 %, 10 % og 20 %. Vi antar at stille skyldnere betaler like mye som andre. Det gjør de trolig ikke: i 38 552 av 106 424 utleggsbegjæringer for forbruksgjeld i 2024 (38,9 %) ble resultatet «intet til utlegg» ([Finanstilsynet, inkassostatistikk for 2024](https://www.finanstilsynet.no/496310/contentassets/5d628a2a2b774b01ab14f3a71286adb7/inkassostatistikk-for-2024.pdf), del 9). Tallene er derfor en **øvre grense**. Grunnlaget er 2024, siste år med fordeling av innbetalingene.

| Andel fra stille skyldnere | Tapt rente i fryseperioden | Kostnad ved at gebyrer kommer 6 mnd senere | Sum per år | Utsettelsen som andel av inkassoforetakenes inntekter |
|---|---|---|---|---|
| 5 % | 0,08 mrd kr | 0,01 mrd kr | 0,09 mrd kr | 0,2 % |
| 10 % | 0,16 mrd kr | 0,02 mrd kr | 0,19 mrd kr | 0,4 % |
| 20 % | 0,33 mrd kr | 0,04 mrd kr | 0,37 mrd kr | 0,9 % |

- Renten går til kreditoren, altså banken, eller inkassoselskapet når det eier kravet. Det tapet bæres altså mest av dem som eier gjelden, og de har de beste marginene (del 2).
- Inkassoselskapenes egne inntekter er salær. Det blir utsatt, ikke slettet, så virkningen for dem er under 1 % av inntektene.
- Med en frys etter to måneder vil skyldnerne fortsatt betale over 6,5 mrd kr i året i renter og kostnader, og selskapene vil fortsatt tjene penger.

## 6. Hva betyr dette for fristen?

Pengene avgjør ikke fristen. Selskapene taper nesten like lite om flagget kommer etter 30 dager som etter 90. Fristen bør derfor velges ut fra **menneskene**: hvor lenge kan noen være stille før det er grunn til bekymring, og hvor kort kan fristen være uten at folk som bare er trege eller på reise blir flagget?

Det tallene sier om valget:

1. **Flagget må komme før salæret dobles.** Dagens regler tillater tungt salær fra rundt dag 57. Forslaget krever allerede at flagget settes før tungt salær. Den regelen er viktigere enn selve fristen: uten den legger en sak på 5 000 kr på seg 600 kr mer.
2. **60 dager henger sammen med reglene.** Det er like etter tidligste dobling, så flagget-før-tungt-regelen gjør at ingen stille person får doblet salær før noen har sett etter. 45 dager ville gitt samme vern uten å trenge regelen, men flere flagg på folk som bare er sene.
3. **Balansen: ansvar skal fortsatt gjelde.** Frysen sletter ikke gjelden, lett salær står, og renten løper igjen etter seks måneder hvis personen er frisk og fortsatt ikke svarer. Den som tar kontakt får en vanlig betalingsplan.
4. **Mot misbruk** kan forslaget gjøre frysen til «fryst, ikke slettet»: Hvis det viser seg at personen var frisk og kunne svart, men lot være, kan frosne gebyrer og renter kreves etterpå. Hvis personen var syk, innlagt eller død, eller et pauseflagg var satt av lege, NAV eller verge, faller de bort. Da lønner det seg ikke å late som man er stille, og de som virkelig ikke klarte å svare blir ikke straffet. Dette er et forslag til diskusjon.

## Forutsetninger og usikkerhet

- Hvor stor andel av inntektene som kommer fra stille skyldnere er ukjent. Det er det viktigste tallet vi mangler, og det kan bare inkassobransjen eller Finanstilsynet svare på.
- Dagene for forfall (−14) og første rettslige skritt (180) er våre forutsetninger. Rettslig salær er ikke tatt med, så kostnaden uten flagg er heller for lav enn for høy.
- Renten er regnet som enkel rente på hovedstolen med 12,25 %.
- Selskapstallene er morselskapenes regnskap slik Proff viser dem. Vi har ikke sjekket dem mot hvert originale årsregnskap, og de viser ikke konsernenes samlede fortjeneste. Proff viste ikke 2020 for de fleste selskapene.
- Ny inkassolov ble sanksjonert 22. mai 2026, og myndighetene har signalisert ikrafttredelse 1. januar 2027. En ny inkassoforskrift skal fastsette nye satser. Gebyrene i del 3 og 4 kan derfor endre seg, og regnestykket bør kjøres på nytt da.
- Ingen opplysninger om enkeltpersoner er brukt.

## Kilder

Alle hentet 28. oktober 2026. Finanstilsynets statistikk og satser og Finans Norges notat ble kontrollert på nytt 2. november 2026.

- Finanstilsynet, [Inkassostatistikk for 2025](https://www.finanstilsynet.no/analyser-og-statistikk/statistikk-for-inkasso/2025/html/inkassostatistikk-for-2025) (13.04.2026)
- Finanstilsynet, [Inkassostatistikk for 2024](https://www.finanstilsynet.no/496310/contentassets/5d628a2a2b774b01ab14f3a71286adb7/inkassostatistikk-for-2024.pdf) (04.04.2025)
- Finanstilsynet, [Inkassostatistikk for 2. halvår 2023](https://www.finanstilsynet.no/contentassets/cdf73191c72f4cc3b8f11a6c6a3c6160/inkassostatistikk-for-2.-halvar-2023.pdf) og [Innrapporterte inkassotall for 2022](https://www.finanstilsynet.no/contentassets/cdf73191c72f4cc3b8f11a6c6a3c6160/innrapporterte-inkassotall-for-2022.pdf)
- Finanstilsynet, årsrapporter om inkassovirksomhet [2020](https://finanstilsynet.no/publikasjoner-og-analyser/arsrapport/arsrapport-2020/rapporter-tilsynsomradene-2020/inkassovirksomhet), [2021](https://www.finanstilsynet.no/publikasjoner-og-analyser/arsrapport/arsrapport-2021/rapporter-fra-tilsynsomradene-for-2021/inkassovirksomhet), [2022](https://finanstilsynet.no/publikasjoner-og-analyser/arsrapport/arsrapport-2022/rapporter-fra-tilsynsomradene-for-2022/inkassovirksomhet), [2024](https://finanstilsynet.no/publikasjoner-og-analyser/arsrapport/arsrapport-2024/rapporter-fra-tilsynsomradene-for-2024/inkassovirksomhet)
- Finanstilsynet, [Inkassostatistikk for første halvår 2026](https://www.finanstilsynet.no/analyser-og-statistikk/statistikk-for-inkasso/2026/html/inkassostatistikk-for-forste-halvar-2026/) (13.10.2026)
- Finanstilsynet, [Oversikt over utenrettslige inndrivingskostnader](https://finanstilsynet.no/forbrukerinformasjon/inkassovirksomhet/oversikt-over-utenrettslige-inndrivingskostnader) (oppdatert 25.02.2026), [Inkassosatsen i 2026 blir 750 kroner](https://www.finanstilsynet.no/nyhetsarkiv/nyheter/2026/inkassosatsen-i-2026-blir-750-kroner/) (06.01.2026), [Forsinkelsesrente fra 1. juli 2026](https://www.finanstilsynet.no/nyhetsarkiv/nyheter/2026/forsinkelsesrente-og-standardkompensasjon-for-inndrivelseskostnader-fra-1.-juli-2026) (29.06.2026)
- Proff, regnskap: [Intrum AS](https://www.proff.no/regnskap/intrum-as/lysaker/inkasso/IDTBFAY07ZR), [Kredinor AS](https://www.proff.no/regnskap/kredinor-as/oslo/inkasso/IFCG51407ZR), [Lowell Norge AS](https://www.proff.no/regnskap/lowell-norge-as/oslo/inkasso/IG2YI2407ZR), [Lowell AS](https://www.proff.no/regnskap/lowell-as/oslo/inkasso/IG7A0ND07ZR), [Axactor Norway AS](https://www.proff.no/regnskap/axactor-norway-as/drammen/inkasso/IF2VPLS07ZR), [Axactor Capital AS](https://www.proff.no/regnskap/axactor-capital-as/oslo/finans/IF6JKSJ0RSY), [Sergel Norge AS](https://www.proff.no/regnskap/sergel-norge-as-hovedkontor/sandefjord/inkasso/IGA0D9M07ZR), [PRA Group Europe AS](https://www.proff.no/regnskap/pra-group-europe-as/oslo/inkasso/IFVVTKL07ZR), [Riverty Services Norway AS](https://www.proff.no/regnskap/riverty-services-norway-as/oslo/inkasso/IFTY4YB07ZR)
- Axactor Capital AS, årsregnskap [2023](https://www.axactor.com/uploads/Norway-assets/Legal-documents-Axactor-Captial-AS/%C3%85rsregnskap-2023-Axactor-Capital-AS.pdf) og [2025](https://www.axactor.com/uploads/Norway-assets/Legal-documents-Axactor-Captial-AS/%C3%85rsregnskap-Axactor-Capital-AS-2025.pdf)
- Axactor ASA, kvartalsrapporter [Q4 2025](https://www.axactor.com/hubfs/axactor-assets/GROUP-Investor-Relations-assets/Reports-and-presentations/2025/Quarterly-Report-Q4-2025b.pdf), [Q4 2023](https://www.axactor.com/hubfs/axactor-assets/GROUP-Investor-Relations-assets/Reports-and-presentations/2023/Quarterly-Report-Q4-2023.pdf)
- Intrum AB, [Financial information](https://www.intrum.com/investors/financial-information/) (nøkkeltall 2025)
- Kredinor, [Foreløpige kvartalstall Q3 2024](https://www.kredinor.no/app/uploads/2024/10/2024-09-Borsmelding-forelopige-kvartalstall-Q3.pdf)
- Finans Norge, [Hva betyr ny inkassolov?](https://www.finansnorge.no/contentassets/416d893bcb3b440f80f937fd8e8d8d45/hva-betyr-ny-inkassolov.pdf)

---

# English version: What do collectors earn, and what does a freeze cost?

*Version 1, October 2026. Background for the 60-day deadline in the [proposal](forslag.md). Builds on the [analysis](analyse.md).*

The question: if companies earn well from people who cannot respond, how long should fees run before the silence flag kicks in? And would companies still make money if fees were frozen after two months?

All figures come from public sources, read on 28 October 2026; the Finanstilsynet and Finans Norge figures were checked again on 2 November 2026 (see Sources above). The calculations in parts 4 and 5 are **estimates** built on assumptions we chose. They are marked, and the code is in [prototype/fryseregnestykke.py](../prototype/fryseregnestykke.py) so anyone can rerun them with other numbers.

## Summary

- **Debtors pay billions.** In 2024, debtors in Norway paid NOK 3.28 bn in late-payment interest, NOK 2.93 bn in collection costs and NOK 0.72 bn in legal costs: about NOK 6.9 bn on top of the debts themselves.
- **Interest is the largest item.** At the end of 2025, NOK 40 bn of consumers' debt in collection was accrued interest, against NOK 67 bn of original debt.
- **Norwegian collection companies themselves have thin margins.** The industry had NOK 5.09 bn in income and NOK 4.89 bn in costs in 2024. The nine companies we looked at had NOK 14.4 bn in revenue over five years but only NOK 0.18 bn in combined net profit. Profit gathers with those who **own** the debt (e.g. Axactor Capital AS, about 49% net margin) and in the groups abroad.
- **A freeze costs little.** For a silent person owing NOK 5,000, the flag halves what is added before the welfare check (NOK 762 vs NOK 1,513 at day 150). For the whole industry the loss is at most NOK 0.1–0.4 bn a year, even if up to one krone in five came from silent debtors. For collection companies' own income the effect is below 1%.
- **The deadline is about people, not money.** Whether the flag comes after 30, 45, 60 or 90 days makes only a few hundred kroner of difference per case. What matters is that the flag comes **before** the fee doubles (from about day 57), as the proposal already requires.

## 1. What debtors pay: the whole industry

Finanstilsynet's collection statistics, NOK bn: firms' total income 5.09 (2024) and 5.01 (2025); collection income 3.5 (2021), 3.3 (2022), 3.3 (2023), 3.82 (2024), 3.87 (2025). Firms with a loss: 18 (2021), 21 (2022), 28 (2023), 20 (2024), 17 (2025). New cases: 10.66 m (2022) to 11.74 m (2025), about 78% from consumers. Collected from debtors: 46.47 bn (2022), 46.51 bn (2023), 51.17 bn (2024), of which interest 2.79 / 2.85 / 3.28 bn, out-of-court costs 2.72 / 2.83 / 2.93 bn and legal costs 0.72 / 0.73 / 0.72 bn. The ten largest firms held 85–86% of all claims in 2020–2022. Purchased claims: 407,164 cases with NOK 18.8 bn original principal at end 2024.

## 2. The largest companies in Norway

Official annual accounts as shown by Proff, Norwegian entities only, NOK m summed over the years available (table in the Norwegian section). Combined: NOK 14,423 m revenue and NOK 180 m net profit, about 1%. Kredinor (−638), PRA Group Europe (−325) and Lowell AS (−148) made losses over the period; Riverty (31% margin) and above all Axactor Capital AS, the entity that owns Axactor's purchased Norwegian debt (operating profit NOK 150–227 m a year, against wage costs of only NOK 1.9–3.3 m a year), made the money. At group level, Axactor ASA had EUR 258 m revenue and EUR 125 m operating profit in 2025 (2024: net loss of EUR 79 m); Intrum AB had SEK 17.0 bn income and SEK 5.3 bn adjusted operating profit in 2025.

The claim that the companies "earn many billions" holds for the groups and for what debtors pay in total. It does not hold for Norwegian collection companies' own profits, so the project's texts now separate what debtors pay from who keeps the profit. That makes the case for the flag stronger: the money comes from debtors, and a freeze takes only a small slice of it.

## 3. How fees grow when someone does not answer

2026 rules (collection rate NOK 750, creditor with VAT deduction), days counted from the collection notice: day −14 the bill falls due (our assumption) and 12.25% interest starts; day 0 notice, NOK 38; day 14 payment demand with light fee, NOK 600 on a NOK 5,000 claim; day 57 deadline overrun by more than 28 days, the fee may double (+NOK 600; Finanstilsynet: "if the debtor exceeds the payment deadline in a payment demand by more than 28 days, the collector may double this fee"); around day 180 the first legal step (our assumption), court fee NOK 1,345 plus legal fees not included here.

## 4. Estimate: one silent debtor

The person never answers. The flag freezes new fees, interest and legal steps for up to 6 months. Day 150 is the welfare check for a flag set on day 60. Added by day 150 on a NOK 5,000 claim (no court fee yet, since the first legal step is set at day 180): never flagged NOK 1,513; flag on day 30: 712; day 45: 737; day 60: 762; day 90: 813; day 60 without the "flag before heavy fee" rule: 1,362. For NOK 20,000: 3,539 vs 1,735. For NOK 1,000: 618 vs 325.

After 12 months, if the person is still silent and the freeze has ended, fees are only **delayed**: NOK 3,219 vs 2,914, both including the NOK 1,345 court fee, which goes to the state. What disappears for good is the interest during the freeze, plus anything after a date of death.

The difference between flagging on day 30 and day 90 is only about NOK 100 on a NOK 5,000 claim (about NOK 400 on NOK 20,000), all of it interest.

## 5. Estimate: the whole industry

Nobody knows what share of payments comes from people who have been silent for 60 days, so we use 5%, 10% and 20%, and assume silent debtors pay as much as others (they likely pay less: in 38,552 of 106,424 enforcement requests for consumer debt in 2024, 38.9%, the enforcement officer found nothing to seize, per Finanstilsynet's 2024 statistics, part 9). The results are therefore **upper bounds**, based on 2024: lost interest NOK 0.08 / 0.16 / 0.33 bn a year; cost of fees arriving 6 months later NOK 0.01 / 0.02 / 0.04 bn; for collection firms' own income (fees) the delay equals 0.2% / 0.4% / 0.9%. The lost interest falls mostly on whoever owns the debt, who also have the best margins. With a freeze after two months, debtors would still pay over NOK 6.5 bn a year in interest and costs, and the companies would still make money.

## 6. What this means for the deadline

Money does not decide the deadline; people do. How long can someone be silent before there is reason to worry, and how short can the deadline be without flagging people who are only slow or travelling?

1. **The flag must come before the fee doubles.** The rule that a flag is needed before a heavy fee matters more than the deadline itself; without it a NOK 5,000 case gains NOK 600 more.
2. **60 days fits the rules.** It is just after the earliest doubling, and with the flag-before-heavy-fee rule no silent person gets a doubled fee before someone has checked. 45 days would give the same protection without needing the rule, but more flags on people who are merely late.
3. **The balance: responsibility still applies.** The freeze does not delete the debt, the light fee stands, and interest runs again after six months if the person is well and still silent. Anyone who gets in touch gets a normal payment plan.
4. **Against misuse**, the freeze could become "frozen, not deleted": if the person turns out to have been well and able to answer, frozen fees and interest can be claimed afterwards; if they were ill, hospitalised or dead, or a pause flag was set by a doctor, NAV or a guardian, they are dropped. Faking silence then does not pay, and those who truly could not answer are not punished. This is a suggestion for discussion.

## Assumptions and uncertainty

The share of income from silent debtors is unknown and is the key missing number; only the industry or Finanstilsynet can answer it. Due date (day −14) and first legal step (day 180) are our assumptions, and legal fees are left out, so the no-flag cost is if anything too low. Interest is simple interest on the principal at 12.25%. Company figures are parent-company accounts as shown by Proff, not checked against each original filing, and they do not show group-wide profit; Proff did not show 2020 for most companies. A new Debt Collection Act was sanctioned on 22 May 2026, with 1 January 2027 signalled as the in-force date; new regulations will set new rates, so the calculation should be rerun then. No data about individuals has been used.
