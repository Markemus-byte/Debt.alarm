# Pensjon og arv: hvem får pensjonen når noen dør?

*Versjon 1, november 2026. En egen studie ved siden av inkassosporet: den handler om arv som forsvinner, men ikke om inkasso. English version below.*

Spørsmålet: Et menneske jobber i kanskje 50 år og tjener opp pensjon. Dør personen, går pengene ikke til arvingene slik andre verdier gjør. Hvorfor, hvem får dem, og hva ville det koste å endre det?

Alle fakta er hentet fra kildene nederst og kontrollert 2. november 2026. Lovdata og flere sider på nav.no og regjeringen.no lot seg ikke åpne, så enkelte regler er bekreftet av banker og forsikringsselskaper i stedet for lovteksten; det står ved hver av dem. Regnestykkene i del 5 og 9 er **anslag** bygget på SSBs dødelighetstabell og forutsetninger vi har valgt selv. Koden ligger i [prototype/pensjonsregnestykke.py](../prototype/pensjonsregnestykke.py), og testene låser de utregnede tallene som står her. Tall og påstander er kontrollert av en egen AI-gjennomgang (Claude) mot kildene og koden, ikke av en aktuar eller pensjonsjurist.

## Kort oppsummert

- **Mye av pensjonen arves ikke, men det meste av folketrygdpensjonen tilfaller heller ikke staten.** Alderspensjonen fra folketrygden, AFP, offentlig tjenestepensjon og fripoliser uten etterlattedekning stopper ved død. Innskuddspensjon, egen pensjonskonto og IPS går derimot til barn, ektefelle, samboer eller dødsboet.
- **Folketrygden har ingen pott per person.** Avgiftene du betalte, gikk til datidens pensjonister. Beholdningen din er et løfte om framtidig pensjon, ikke penger på en konto.
- **Det de døde ikke fikk, går i hovedsak til de andre i samme årskull.** Beholdningen til dem som dør før 62 år, deles ut til de gjenlevende gjennom delingstallet (Stortinget kaller det «arvegevinst»). Etter uttak finansierer de som dør tidlig, dem som lever lenge. I vår modell får et årskull som helhet ut minst like mye som alle medlemmene tjente opp (103–112 %).
- **Men fordelingen går fra kortlevde til langlevde.** Etter dagens dødelighet dør 8,4 % av 22-åringene før 67. Av dem som lever ved 67, dør 32–38 % før de har fått ut like mye som beholdningen. De som dør tidlig, har oftere lav inntekt og dårlig helse.
- **Etterlatte får mindre enn før.** Gjenlevendepensjonen fases ut og er erstattet av en omstillingsstønad i inntil 3 år (5 år ved utdanning).
- **Det finnes rimelige forslag.** En garanti om at familien får resten av de 5 første pensjonsårene, koster ca. 0,5–0,7 % av alderspensjonen. Full arv av alt som ikke er brukt opp, koster 9–12 % ekstra, eller 12–18 % lavere pensjon for alle.

## 1. Folketrygden: hvorfor alderspensjonen ikke arves

Alderspensjonen fra Nav arves ikke. Smarte Penger: «Verken pensjon under utbetaling eller pensjonsbeholdning arves». Pensjonen utbetales til og med dødsmåneden (Nav: «Pensjon og uføretrygd fra folketrygden blir utbetalt til og med dødsmåneden»).

**Slik er den bygget.** For alle født 1963 eller senere blir 18,1 % av inntekten opp til 7,1 G lagt inn i en *pensjonsbeholdning* hvert år (SNL). Ved uttak deles beholdningen på et *delingstall*. Delingstallet bygger på forventet levetid, men er lavere enn den, fordi pensjonen reguleres svakere enn lønningene, fordi det inneholder arvegevinst (se under), og av andre grunner vi ikke har klart å forklare (del 5). For 1963-kullet er delingstallet 16,11 ved uttak ved 67 år (Smarte Penger; Navs egen tabell lot seg ikke åpne). Med en beholdning på 4,9 mill. kr gir det ca. 303 000 kr i året.

**Beholdningen er et regnestykke, ikke en konto.** Folketrygden betales løpende over statsbudsjettet, og avgiftene gikk til dem som var pensjonister da. Statens pensjonsfond gir ingen personlige rettigheter; det finnes ingen konto per person der heller. Når noen dør, er det derfor ingen pott som «tilfaller staten»; statens framtidige utgift blir mindre.

**De døde gir til de gjenlevende i kullet.** Da Stortinget behandlet den nye alderspensjonen, ble det lagt til grunn at «effekten av endringer i dødelighet før 62 år inkluderes i delingstallene», og at arvegevinsten skal gå «inn i delingstallet fremfor å definere arvegevinsten som et årlig tilskudd til pensjonsbeholdningen» (Innst. O. nr. 67 (2008–2009)). SSB beskrev samme forslag som å ta hensyn til «arvegevinster forårsaket av at noen dør før 62 år» (SSB Rapport 2008/23). Beholdningen til dem som dør før 62, gir altså et lavere delingstall og høyere pensjon for resten av kullet, samme prinsipp som i Sverige. Vi har ikke funnet ut hvordan dødsfall mellom 62 år og uttak behandles.

**Det de etterlatte får fra Nav:**

- *Omstillingsstønad* i inntil 3 år fra måneden etter dødsfallet, med forlengelse i inntil 2 år ved nødvendig utdanning eller tiltak. Den reduseres med 45 % av inntekt over 0,5 G (Nav). Det finnes overgangsregler for eldre årskull.
- *Gjenlevendepensjon* fases ut: «ingen nye personer får gjenlevendepensjon», og mange som har den, får den i tre år fra 1. januar 2024 (Nav). Den gamle ordningen gikk fram til 67 år, og for eldre årskull kan en gjenlevende ektefelle få et tillegg i sin egen alderspensjon (gjenlevenderett). Slik vi forstår reglene, gjelder dette ikke dem som er født 1963 eller senere; det bør sjekkes med Nav.
- *Barnepensjon* til og med måneden barnet fyller 20 år (Nav).

## 2. Tjenestepensjon, AFP og privat sparing: hva arves?

Svaret avhenger av om pensjonen er *innskuddsbasert* (penger på en konto i ditt navn) eller *ytelsesbasert* (et løfte om en årlig sum så lenge du lever). Innskudd går til de etterlatte; ytelsesløfter stopper ved død.

| Pensjon | Arves den? | Hva skjer ved død | Kilde |
|---|---|---|---|
| Alderspensjon fra folketrygden | Nei | Utbetales til og med dødsmåneden. Etterlatte kan få omstillingsstønad og barnepensjon | Smarte Penger, Nav |
| Innskuddspensjon, egen pensjonskonto, pensjonskapitalbevis | Ja, i fast rekkefølge | Ifølge bankene: først barnepensjon til barn under 21 år (inntil 1 G i året), så til ektefelle, partner eller samboer, utbetalt over minst 10 år. Er ingen av dem der, betales resten som engangsbeløp til dødsboet (bekreftet av Skatteetaten, innskuddspensjonsloven § 7-7 fjerde ledd) | DNB, Nordea, Skatteetaten |
| IPS (individuell pensjonssparing) | Ja, samme rekkefølge | Barn under 21, så ektefelle, partner eller samboer, utbetalt over 10 år, ellers dødsboet | Nordnet |
| Fripolise og privat ytelsespensjon | Nei, bare eventuell etterlattedekning | DNB: «Gjenstående alderspensjon vil ikke bli utbetalt til etterlatte ved dødsfall»; kapitalen fordeles på de andre fripolisekundene | DNB |
| Offentlig tjenestepensjon (KLP, SPK) | Nei | Ektefellepensjon og barnepensjon til barn under 20 år. KLP: «Samboere har ikke rett på etterlattepensjon». Reglene kan variere mellom ordninger | KLP |
| AFP i privat sektor | Nei | «Livsvarig ytelse som utbetales til og med den måneden du dør» (Nav). Nordea: «ingen rett til arv» for AFP i privat og offentlig sektor | Nav, Nordea |

DNB og Nordea beskriver barnepensjonen i innskuddsordninger ulikt (inntil 1 G *samlet* mot *per barn*), og vi har ikke fått lest loven selv. Dette må sjekkes på Lovdata.

**Fripolisene er den mest konkrete gråsonen.** Mange som har byttet jobb, har fripoliser fra gamle ytelsesordninger. Uten etterlattedekning får familien ingenting, selv etter mange år i bedriften. Kapitalen går til selskapets andre fripolisekunder (dødelighetsarv), samme utjevning som i folketrygden, og den har gitt alle kundene litt høyere pensjon. Men her står det oppspart kapital i personens navn, og den forlater familien.

I offentlig tjenestepensjon er det annerledes: der betyr pensjon som ikke utbetales, direkte lavere kostnad for arbeidsgiveren eller staten.

## 3. Opptjent, men aldri utbetalt

1. **Død før uttak.** Folketrygdbeholdningen faller bort for familien. Dør personen før 62, går den til resten av kullet (del 1). Det samme gjelder AFP, offentlig tjenestepensjon (utover ektefelle- og barnepensjon) og fripoliser uten etterlattedekning. Innskuddspensjon og IPS går videre.
2. **Død kort tid etter uttak.** Folketrygden utbetales til og med dødsmåneden, selv om personen bare har fått noen få år av det beholdningen var regnet for.
3. **Utsatt uttak.** Den som venter med å ta ut pensjon for å få mer per år (uttak mellom 62 og 75 år, SNL), og så dør, har «spart» penger som ikke kommer familien til gode.

Dette treffer gruppen Debt.alarm handler om: syke og utslitte mennesker som dør tidligere enn snittet. På norskpensjon.no kan hver enkelt se alle pensjonsavtalene sine og sjekke hvilke som har etterlattedekning.

## 4. Hvem taper på utjevningen?

De som dør tidlig, er ikke tilfeldig valgt. Ifølge FHI lever de 25 % med høyest inntekt 6–8 år lenger enn de 25 % med lavest, og de med lengst utdanning lever 5–6 år lenger enn de med kortest. Blant 40-åringer er forskjellen mellom den rikeste og fattigste prosenten 13,8 år for menn og 8,4 år for kvinner (FHI 2019). Ved 65 år er utdanningsforskjellen mindre, ca. 3–4 år (FHI). Utjevningen i en livsvarig pensjon går dermed delvis fra dem med lav inntekt til dem med høy. Samtidig fordeler folketrygden andre veien på andre måter, for eksempel med garantipensjon og taket på 7,1 G.

## 5. Regneeksempel: hvor mye blir aldri utbetalt?

For en vanlig lønnstaker som lever ved 67 og tar ut pensjon da, blir i snitt 11–14 % av folketrygdbeholdningen aldri utbetalt fordi personen dør først, ca. 0,5–0,7 mill. kr. Samtidig får 67-åringene i snitt ut mer enn sin egen beholdning, delvis fordi de har arvet fra dem i kullet som døde før 62.

| Eksempel: født 1963, 600 000 kr i lønn i 45 år, uttak ved 67 | Tall |
|---|---|
| Pensjonsbeholdning ved 67 (18,1 % × 600 000 × 45 år) | ca. 4,9 mill. kr |
| Årlig alderspensjon (beholdning delt på 16,11) | ca. 303 000 kr |
| Andel som dør mellom 22 og 67 år, etter dødeligheten i 2025 | 8,4 % (menn 10,2 %, kvinner 6,6 %) |
| Forventet utbetaling til en 67-åring, i % av egen beholdning | 110–118 % |
| Hele kullet fra 22 år: utbetalt i % av alt kullet tjente opp | 103–112 % |
| Alder når utbetalingene har nådd beholdningen | ca. 84 år |
| Andel av 67-åringene som dør før det | 32–38 % |
| Snitt som aldri blir utbetalt, per 67-åring | 11–14 % av beholdningen, ca. 0,5–0,7 mill. kr |
| Snitt som aldri blir utbetalt, for dem som dør før 84 | ca. 35–36 % av beholdningen, ca. 1,7–1,8 mill. kr |

**Slik er tallene regnet.** Beholdningen er i dagens lønnsnivå og ser bort fra reell lønnsvekst. Dødeligheten er SSBs dødelighetstabell for 2025, og modellen gjenskaper SSBs forventede gjenstående levetid ved 67 år (19,15 mot SSBs 19,17). Hvert spenn har ett ytterpunkt fra tabellen slik den er, og ett med 20 % lavere dødelighet, fordi de som går av i 2030-årene, trolig lever lenger enn dagens tabell viser. Pensjon under utbetaling reguleres med snittet av lønns- og prisveksten (Innst. 233 S (2023–2024)), som vi har satt til lønnsvekst minus 0,75 % i året; det stemmer hvis reallønnsveksten er 1,5 %. «Utbetalt» er regnet i dagens lønnsnivå, så en krone utbetalt ved 80 teller litt mindre enn en ved 67. Uten den justeringen ville utbetalingene nådd beholdningen ved ca. 83 år.

**En kontroll av delingstallet.** SSB-tabellen alene gir et «delingstall» på 17,67 ved 67. Deler vi ut beholdningen som de som dør før 62 har tjent opp (vektet etter hvor mye de rakk å tjene), blir det ca. 17,1. Det offisielle 16,11 er ca. 6 % lavere enn det igjen. Vi kan ikke forklare resten; Nav bruker ti års observert dødelighet, fastsatt når kullet fyller 61 år, og kan bruke en annen formel enn vår.

## 6. Argumenter for og mot arvelig pensjon

En livsvarig pensjon er en forsikring mot å leve lenge. Arv og livsvarig garanti trekker i hver sin retning.

**For å la mer gå til familien**

- *Det føles som egne penger.* Beholdningen står på navnet ditt i Nav, og innskuddspensjon arves. To pensjoner tjent opp i samme jobb behandles helt ulikt.
- *Kortlevde subsidierer langlevde.* De som dør tidlig, har oftere lav inntekt og dårlig helse (del 4).
- *Etterlatte får mindre enn før.* Gjenlevendepensjonen er erstattet av en stønad i inntil 3 år.
- *Andre land gir valg.* I Sverige kan man beskytte partneren, og i Australia går hele pensjonssparingen videre.

**Mot**

- *Det finnes ingen pengepott per person.* Det som ikke utbetales i folketrygden, er ikke penger staten «tar»; det finansierer de langlevde i samme kull. Arv må betales av noen andre.
- *Forsikringen blir dyrere.* Uten at de som dør tidlig «betaler» for dem som lever lenge, må pensjonen ned for alle eller avgiftene opp.
- *De som lever lenge, trenger pengene mest.* En 95-åring uten annen inntekt er mer sårbar enn arvingene til en som døde ved 70.
- *Arv øker forskjeller mellom familier.* Arvingene er ofte voksne barn i 50- og 60-årene.
- *Man kan allerede velge.* IPS, egen sparing og livsforsikring går til de etterlatte.

## 7. Debatt og reformer i Norge

I kildene vi har gått gjennom, har arv av pensjon ikke vært et tema i de store pensjonsdebattene.

- **Pensjonsutvalget (NOU 2022:7)** foreslo at aldersgrensene følger levealderen fra 1964-kullet, at minstenivåene reguleres med lønnsveksten, og bedre vilkår for uføre. Arv og etterlatte nevnes ikke i regjeringens oppsummering.
- **Pensjonsforliket 29. februar 2024** (Meld. St. 6 (2023–2024), Innst. 233 S) viderefører levealdersjusteringen, som er blitt sterkere enn ventet: pensjonen ved 67 for 1963-kullet er «8,1 pst. lavere enn det Pensjonskommisjonen la til grunn» (Innst. 233 S). Etterlattepensjon nevnes bare som et stikkord i den delen vi fikk lest.
- **Etterlattereformen 2024** erstattet gjenlevendepensjonen med en tidsbegrenset omstillingsstønad.
- **Tallene i dag:** folketrygden betalte vel 334 mrd. kr i alderspensjon i 2025 til om lag 1 085 000 personer (Pensjonspolitisk arbeidsgruppe, mai 2026).
- **Stortinget:** vi fant ingen representantforslag om arv av pensjon i sesjonen 2026–2027. Eldre sesjoner og avisdebatter er ikke gjennomgått.

Vi har ikke funnet at noen har regnet offisielt på arvelig pensjon i Norge, så et forslag fra Debt.alarm kan være nytt i debatten.

## 8. Andre land

Ingen av landene vi så på, lar den offentlige grunnpensjonen gå i arv. Forskjellene ligger i den oppsparte delen og i hvilke valg folk får.

| Land | Hva skjer ved død | Kilde |
|---|---|---|
| Sverige, inkomstpension | Ingen etterlattebeskyttelse. Arvsvinster fra avdøde fordeles årlig til gjenværende pensjonister og pensjonssparere | Pensionsmyndigheten |
| Sverige, premiepension | Kontoen fordeles hver måned som arvsvinst. Man kan velge *efterlevandeskydd* ved første uttak: partneren får pensjonen resten av livet, men egen pensjon blir lavere, 7–46 % etter alderen på begge i Pensionsmyndighetens eksempeltabell (66 år med partner på 60: 775 kr per 1 000 kr, 22,5 % lavere). Kan ikke angres | Pensionsmyndigheten |
| Sverige, tjenestepensjon | Valgfritt *återbetalningsskydd*: familien får pengene, ved livsvarig utbetaling i inntil 20 år. Uten det kan pensjonen bli 5–15 % høyere | Swedbank |
| Danmark, folkepensjon og ATP | Folkepensjonen stopper dagen etter dødsfallet. ATP gir ektefelle eller samboer (meldt til ATP) et engangsbeløp, for innbetalinger etter 2002: fullt beløp, 75 000 DKK, ved død før folkepensjonsalderen; deretter synker det med 15 000 DKK i året fra året etter og er borte 5 år etter folkepensjonsalderen. 40 % går i avgift til staten | borger.dk |
| Danmark, arbeidsmarkedspensjoner | Inneholder ofte forsikringer til etterlatte ved død før pensjon. Supplerende arbeidsmarkedspensjon går til boet, med 40 % avgift | borger.dk |
| Australia, superannuation | Saldoen betales ut som «death benefit» til ektefelle, barn (uansett alder) eller boet, etter bindende nominasjon eller forvalterens skjønn. Den som ikke er «dependant» etter pensjonsloven, må ta den som engangsbeløp | ATO |

Sverige viser at arvelig pensjon har en pris som betales av personen selv. Australia viser at full arv fungerer når pensjonen er en ren sparekonto, men da er det ingen garanti for at pengene varer livet ut.

## 9. Mulige forslag og hva de koster

En garantert utbetalingstid på 5–10 år til familien er det mest realistiske forslaget. Full arv av alt som ikke er brukt opp, er mulig, men dyrt.

| Forslag | Hva familien får | Kostnad i % av alderspensjonen | Størrelsesorden, mrd. kr per år |
|---|---|---|---|
| 1. Valgfri partnerbeskyttelse (som Sverige) | Partneren får pensjonen livet ut, hvis man selv velger det | Betales av den som velger det, med lavere pensjon (i Sverige 7–46 %) | ca. 0 |
| 2. Garantert utbetaling i 5 år fra uttak | Resten av de 5 årene til ektefelle, samboer, barn eller boet | 0,5–0,7 % | ca. 2 |
| 3. Garantert utbetaling i 10 år fra uttak | Som over, men 10 år | 2,5–3,3 % | 8–11 |
| 4. Beholdningen ved død før 67 går til familien | Hele beholdningen, f.eks. i samme rekkefølge som innskuddspensjon | 4,7–6,3 % (lavere hvis bare ektefelle og barn) | 16–21 |
| 5. Full arv av ubrukt beholdning etter 67 | Beholdning minus det som er utbetalt, til boet | 9,4–12,4 % ekstra, eller 12–18 % lavere pensjon for alle | 32–41 |

**Slik er det regnet.** Prosentene er ekstra utgift delt på forventede pensjonsutbetalinger, fra modellen i del 5. Det er grunnen til at forslag 5 (9,4–12,4 %) ser lavere ut enn det som aldri blir utbetalt (11–14 % av *beholdningen*): utbetalingene er 110–118 % av beholdningen. Kronebeløpene er prosenten ganget med alderspensjonsutgiftene i 2025 (334 mrd. kr). De viser størrelsesorden ved dagens utgiftsnivå og kan bli både høyere og lavere når den nye ordningen er fullt innfaset. Forslag 2–4 kan betales med nye penger eller ved at pensjonen blir omtrent like mange prosent lavere for alle; forslag 4 betyr i praksis at arvegevinsten fra del 1 tas bort, men den dekker bare en del av kostnaden (ca. 3,5 % av utbetalingene i modellen). Forslag 5 krever at pensjonen blir 12–18 % lavere for alle, mer enn kostnaden, fordi lavere pensjon etterlater mer ubrukt beholdning som også skal betales ut.

Forslag 1 er ikke helt gratis: de som har en syk partner, vil oftere velge beskyttelsen, og det kan koste noe.

**Et engangsbeløp, som Danmarks ATP,** er enklest å forklare. Ett grunnbeløp (136 549 kr fra 1. mai 2026) til ektefelle, samboer eller barn koster 137 mill. kr per 1 000 dødsfall som omfattes. SSB publiserer dødsfall etter alder, men vi har ikke hentet de tallene ennå.

**Et forslag som passer Debt.alarm** kan være forslag 2 eller 3 kombinert med forslag 1, pluss en plikt for Nav og pensjonsselskapene til å varsle arvingene aktivt om innskuddspensjon, IPS og fripoliser med etterlattedekning når noen dør. Om slike penger i dag blir liggende uten at arvingene vet om dem, har vi ikke undersøkt; det må sjekkes før det brukes som argument.

## Forutsetninger og usikkerhet

- Lovteksten (innskuddspensjonsloven, folketrygdloven kapittel 20) lot seg ikke åpne. Reglene for innskuddspensjon bygger på bankenes og Skatteetatens beskrivelser.
- Delingstallet 16,11 er fra Smarte Penger; Navs egen tabell og formelen bak lot seg ikke åpne. Vi kan ikke forklare hele forskjellen mellom delingstallet og SSB-tabellen (del 5).
- Hvordan dødsfall mellom 62 år og uttak påvirker delingstallet, er ikke avklart. Det samme gjelder gjenlevenderetten for eldre årskull.
- Regnestykkene bruker én dødelighetstabell for begge kjønn, én lønn og én uttaksalder. De viser størrelsesorden, ikke Navs egne beregninger.
- Ingen opplysninger om enkeltpersoner er brukt.

## Kilder

Alle sidene er lest 2. november 2026.

**Norge**

- [Nav: Mistet noen (utbetaling til og med dødsmåneden)](https://www.nav.no/mistet-noen)
- [Nav: Omstillingsstønad](https://www.nav.no/omstillingsstonad)
- [Nav: Gjenlevendepensjon](https://www.nav.no/gjenlevendepensjon)
- [Nav: Barnepensjon](https://www.nav.no/barnepensjon)
- [Nav: AFP i privat sektor](https://www.nav.no/afp-i-privat-sektor)
- [Stortinget: Innst. O. nr. 67 (2008–2009), kap. 5 (arvegevinst)](https://stortinget.no/no/Saker-og-publikasjoner/Publikasjoner/Innstillinger/Odelstinget/2008-2009/inno-200809-067/5/)
- [Stortinget: Innst. O. nr. 67 (2008–2009), kap. 2](https://stortinget.no/no/Saker-og-publikasjoner/Publikasjoner/Innstillinger/Odelstinget/2008-2009/inno-200809-067/2/)
- [SSB: Rapport 2008/23](https://www.ssb.no/emner/12/90/rapp_200823/rapp_200823.pdf)
- [Stortinget: Innst. 233 S (2023–2024)](https://stortinget.no/no/Saker-og-publikasjoner/Publikasjoner/Innstillinger/Stortinget/2023-2024/inns-202324-233s/?m=0)
- [Stortinget: Regulering av pensjoner i 2026 (G = 136 549 kr)](https://www.stortinget.no/no/Saker-og-publikasjoner/Saker/Sak/?p=200335&target=case-status)
- [Stortinget: Representantforslag](https://www.stortinget.no/no/Saker-og-publikasjoner/Publikasjoner/Representantforslag/)
- [Regjeringen: Pensjonsutvalget foreslår endringer (NOU 2022:7)](https://www.regjeringen.no/no/aktuelt/foreslar-endringer-i-pensjonssystemet/id2919326/)
- [Pensjonspolitisk arbeidsgruppe, rapport mai 2026](https://www.regjeringen.no/contentassets/f1e0b8720fd7438bafa0775ee92246e0/rapport-fra-pensjonspolitisk-arbeidsgruppe-mai-2026.pdf)
- [Skatteetaten: Engangsutbetaling innskuddspensjon](https://www.skatteetaten.no/bedrift-og-organisasjon/arbeidsgiver/a-meldingen/veiledning/lonn-og-ytelser/oversikt-over-lonn-og-andre-ytelser/engangsutbetaling-innskuddspensjon)
- [SSB: Døde, dødelighetstabell 2025 (Tabell 6)](https://www.ssb.no/befolkning/fodte-og-dode/statistikk/dode)
- [FHI: Rike lever mykje lenger enn fattige (2019)](https://www.fhi.no/nyheter/2019/rike-lever-mykje-lenger-enn-fattige/)
- [FHI: Sosiale helseforskjeller i Norge](https://www.fhi.no/he/folkehelserapporten/samfunn/sosiale-helseforskjeller/)
- [SNL: Ny alderspensjon](https://snl.no/ny_alderspensjon)
- [Smarte Penger: Delingstall](https://www.smartepenger.no/pensjon/1322-delingstall)
- [Smarte Penger: Dette skjer med pensjonen din når du dør](https://www.smartepenger.no/pensjon/2587-dette-skjer-med-pensjonen-din-nar-du-dor)
- [Nordea: Hva skjer med pensjonen når du dør](https://www.nordea.no/private-banking/nye-perspektiver/hva-skjer-med-pensjonen-nar-du-dor.html)
- [DNB: Etterlattepensjon](https://www.dnb.no/pensjon/etterlattepensjon)
- [DNB: Fripoliser](https://www.dnb.no/pensjon/fripoliser)
- [KLP: Vilkår for etterlattepensjon](https://www.klp.no/pensjon/etterlattepensjon/vilkaar)
- [Nordnet: Hva skjer med IPS når jeg dør](https://www.nordnet.no/faq/pensjon/individuell-pensjonssparing-ips/hva-skjer-med-ips-nar-jeg-dor)

**Andre land**

- [Pensionsmyndigheten: Vad händer med pensionen när någon dör](https://www.pensionsmyndigheten.se/forsta-din-pension/sa-fungerar-pensionen/vad-hander-pension-dor)
- [Pensionsmyndigheten: Efterlevandeskydd inom premiepensionen](https://www.pensionsmyndigheten.se/forsta-din-pension/ekonomiskt-stod/efterlevandeskydd-inom-premiepensionen)
- [Swedbank: Vem ärver din pension](https://www.swedbank.se/privat/livet/arbetsliv/vem-arver-din-pension)
- [Swedbank: Återbetalningsskydd](https://www.swedbank.se/privat/pension/nar-du-narmar-dig-pension/aterbetalningsskydd.html)
- [borger.dk: Pension, når du dør](https://www.borger.dk/pension-og-efterloen/dit-liv-aendrer-sig---tjek-pensionen/pension-ved-sygdom-ulykke-og-doed/pension-naar-du-doer)
- [borger.dk: ATP engangsbeløb til ægtefælle](https://www.borger.dk/pension-og-efterloen/ATP-Livslang-pension-oversigt/ATP-udbetaling-ved-doed/ATP-engangsbelob-aegtefaelle)
- [ATO: Superannuation death benefits](https://www.ato.gov.au/individuals-and-families/super-for-individuals-and-families/super/withdrawing-and-using-your-super/superannuation-death-benefits)

---

# English version: Who gets the pension when someone dies?

*Version 1, November 2026. A separate study alongside the debt-collection track: it is about inheritance that disappears, not about debt collection.*

The question: someone works for perhaps 50 years and earns a pension. When they die, the money does not go to their heirs the way other assets do. Why, who gets it, and what would it cost to change that?

All facts come from the sources listed above and were checked on 2 November 2026. Lovdata and several pages on nav.no and regjeringen.no could not be opened, so some rules are confirmed by banks and insurers rather than the statute; this is noted for each. The figures in parts 5 and 9 are **estimates** built on Statistics Norway's life table and assumptions of our own. The code is in [prototype/pensjonsregnestykke.py](../prototype/pensjonsregnestykke.py), and its tests pin the computed figures quoted here. Figures and claims were checked against the sources and the code by a separate AI review (Claude), not by an actuary or pension lawyer.

## Summary

- **Much of the pension is not inherited, but most of the state pension does not go to the state either.** The folketrygd old-age pension, AFP, public-sector occupational pension and paid-up policies (fripoliser) without survivor cover stop at death. Defined-contribution pensions, the personal pension account and IPS go to children, spouse, cohabitant or the estate.
- **Folketrygden has no pot per person.** Contributions paid for the pensioners of the time. Your pension balance is a promise of future pension, not money in an account.
- **What the dead did not receive mainly goes to the rest of their cohort.** The balances of people who die before 62 are shared out to survivors through the divisor (Parliament calls this "arvegevinst", inheritance gain). After retirement, those who die early finance those who live long. In our model, a cohort as a whole receives at least as much as all its members earned (103–112 %).
- **But the pooling runs from the short-lived to the long-lived.** At today's mortality, 8.4 % of 22-year-olds die before 67. Of those alive at 67, 32–38 % die before receiving as much as their balance. People who die early more often have low incomes and poor health.
- **Survivors get less than before.** The survivor's pension is being phased out and replaced by a transition benefit for up to 3 years (5 with education).
- **Affordable options exist.** Guaranteeing the family the rest of the first 5 pension years costs about 0.5–0.7 % of old-age pension spending. Full inheritance of everything unused costs 9–12 % extra, or a 12–18 % lower pension for everyone.

## 1. Folketrygden: why the state pension is not inherited

The Nav old-age pension is not inherited: "Neither pension in payment nor the pension balance is inherited" (Smarte Penger). It is paid up to and including the month of death (Nav).

**How it is built.** For everyone born 1963 or later, 18.1 % of income up to 7.1 G is added to a *pension balance* each year (SNL). At withdrawal the balance is divided by a *divisor* (delingstall). The divisor is based on life expectancy but is lower than it, because pensions are indexed below wages, because it includes the inheritance gain (below), and for other reasons we could not explain (part 5). For the 1963 cohort retiring at 67 it is 16.11 (Smarte Penger; Nav's own table could not be opened). With a balance of NOK 4.9 million that gives about NOK 303,000 a year.

**The balance is a calculation, not an account.** Folketrygden is paid as it goes from the state budget, and contributions went to the pensioners of the time. The Government Pension Fund gives no personal rights; there is no individual account there either. When someone dies there is no pot that "goes to the state"; the state's future spending falls.

**The dead give to the survivors of their cohort.** When Parliament dealt with the new old-age pension, it was assumed that "the effect of changes in mortality before age 62 is included in the divisors", and that the inheritance gain goes "into the divisor rather than being defined as a yearly addition to the pension balance" (Innst. O. nr. 67 (2008–2009)). Statistics Norway described the same proposal as taking account of "inheritance gains caused by some dying before 62" (SSB Rapport 2008/23). The balances of those who die before 62 therefore give a lower divisor and a higher pension to the rest of the cohort: the same principle as Sweden. We have not established how deaths between 62 and withdrawal are treated.

**What survivors get from Nav:**

- A *transition benefit* (omstillingsstønad) for up to 3 years from the month after the death, extendable by up to 2 years for necessary education or measures, reduced by 45 % of income above 0.5 G (Nav). Older cohorts have transitional rules.
- The *survivor's pension* is being phased out: "no new people get survivor's pension", and many current recipients get it for three years from 1 January 2024 (Nav). The old scheme ran until 67, and for older cohorts a surviving spouse can get a supplement in their own old-age pension (gjenlevenderett). As we understand the rules, this does not apply to people born 1963 or later; this should be checked with Nav.
- A *child pension* up to and including the month the child turns 20 (Nav).

## 2. Occupational pensions, AFP and private savings: what is inherited?

It depends on whether the pension is *defined contribution* (money in an account in your name) or *defined benefit* (a promise of a yearly sum for life). Contributions go to survivors; benefit promises stop at death.

| Pension | Inherited? | What happens at death | Source |
|---|---|---|---|
| Folketrygd old-age pension | No | Paid through the month of death. Survivors may get the transition benefit and child pension | Smarte Penger, Nav |
| Defined contribution, personal pension account, pension capital certificates | Yes, in a fixed order | According to the banks: first a child pension to children under 21 (up to 1 G a year), then to a spouse, partner or cohabitant, paid out over at least 10 years. If none, the rest goes as a lump sum to the estate (confirmed by the Tax Administration, Defined Contribution Pensions Act § 7-7(4)) | DNB, Nordea, Skatteetaten |
| IPS | Yes, same order | Children under 21, then spouse, partner or cohabitant, paid out over 10 years, otherwise the estate | Nordnet |
| Paid-up policy and private defined benefit | No, only any survivor cover | DNB: the remaining old-age pension is not paid to survivors; the capital is shared among other paid-up policy customers | DNB |
| Public occupational pension (KLP, SPK) | No | Spouse pension and child pension for children under 20. KLP: cohabitants have no right to survivor pension. Rules may differ between schemes | KLP |
| Private-sector AFP | No | A lifelong benefit paid through the month of death (Nav). Nordea: no right of inheritance for private or public AFP | Nav, Nordea |

DNB and Nordea describe the child pension in contribution schemes differently (up to 1 G *in total* vs *per child*), and we could not read the act itself. This must be checked on Lovdata.

**Paid-up policies are the most concrete grey area.** Many who changed jobs hold paid-up policies from old benefit schemes. Without survivor cover the family gets nothing, even after many years in the company. The capital goes to the insurer's other paid-up policy customers (mortality pooling), the same pooling as in folketrygden, and it has given every customer a slightly higher pension. But here there is saved capital in the person's name, and it leaves the family.

Public occupational pension is different: there, pension that is not paid out directly lowers the cost for the employer or the state.

## 3. Earned but never paid

1. **Death before withdrawal.** The folketrygd balance is lost to the family. If the person dies before 62 it goes to the rest of the cohort (part 1). The same goes for AFP, public occupational pension (beyond spouse and child pensions) and paid-up policies without survivor cover. Defined contribution and IPS go on.
2. **Death shortly after withdrawal.** Folketrygden is paid through the month of death, even if the person received only a few years of what the balance was calculated for.
3. **Delayed withdrawal.** Someone who waits to get more per year (withdrawal from 62 to 75, SNL) and then dies has "saved" money that does not reach the family.

This hits the group Debt.alarm is about: ill and worn-out people who die earlier than average. On norskpensjon.no anyone can see all their pension agreements and check which have survivor cover.

## 4. Who loses from the pooling?

Those who die early are not random. According to the Norwegian Institute of Public Health (FHI), the top income quarter lives 6–8 years longer than the bottom quarter, and those with the most education live 5–6 years longer than those with the least. Among 40-year-olds the gap between the richest and poorest percent is 13.8 years for men and 8.4 for women (FHI 2019). At 65 the education gap is smaller, about 3–4 years (FHI). The pooling in a lifelong pension therefore partly runs from lower to higher incomes. At the same time, folketrygden redistributes the other way in other ways, for example through the guaranteed minimum pension and the 7.1 G ceiling.

## 5. Worked example: how much is never paid out?

For an ordinary earner who is alive at 67 and retires then, on average 11–14 % of the folketrygd balance is never paid out because the person dies first, about NOK 0.5–0.7 million. At the same time, 67-year-olds on average receive more than their own balance, partly because they inherited from cohort members who died before 62.

| Example: born 1963, NOK 600,000 salary for 45 years, withdrawal at 67 | Figure |
|---|---|
| Pension balance at 67 (18.1 % × 600,000 × 45 years) | about NOK 4.9 million |
| Annual pension (balance divided by 16.11) | about NOK 303,000 |
| Share dying between 22 and 67, at 2025 mortality | 8.4 % (men 10.2 %, women 6.6 %) |
| Expected payments to a 67-year-old, as % of own balance | 110–118 % |
| Whole cohort from age 22: paid out as % of all it earned | 103–112 % |
| Age when payments reach the balance | about 84 |
| Share of 67-year-olds dying before then | 32–38 % |
| Average never paid, per 67-year-old | 11–14 % of the balance, about NOK 0.5–0.7 million |
| Average never paid, for those dying before 84 | about 35–36 % of the balance, about NOK 1.7–1.8 million |

**Method.** The balance is in today's wage level and ignores real wage growth. Mortality is Statistics Norway's 2025 life table, and the model reproduces SSB's remaining life expectancy at 67 (19.15 vs SSB's 19.17). Each range has one end from the table as published and one with 20 % lower death rates, since people retiring in the 2030s will likely live longer than today's table shows. Pensions in payment are indexed with the average of wage and price growth (Innst. 233 S (2023–2024)), modelled as wage growth minus 0.75 % a year, which holds if real wage growth is 1.5 %. "Paid out" is measured in today's wage level, so a krone paid at 80 counts for slightly less than one paid at 67; without that adjustment payments would reach the balance at about 83.

**A check on the divisor.** The SSB table alone gives a "divisor" of 17.67 at 67. Sharing out the balance earned by those who die before 62 (weighted by how much they had earned) brings it to about 17.1. The official 16.11 is about 6 % lower again. We cannot explain the rest; Nav uses ten years of observed mortality, fixed when the cohort turns 61, and may use a different formula from ours.

## 6. Arguments for and against inheritable pension

A lifelong pension is insurance against living long. Inheritance and a lifelong guarantee pull in opposite directions.

**For letting more go to the family**

- *It feels like your own money.* The balance is in your name at Nav, and defined contribution is inherited. Two pensions earned in the same job are treated completely differently.
- *The short-lived subsidise the long-lived.* People who die early more often have low incomes and poor health (part 4).
- *Survivors get less than before.* The survivor's pension has been replaced by a benefit for up to 3 years.
- *Other countries offer choices.* Sweden lets people protect a partner, and Australia passes on the whole savings balance.

**Against**

- *There is no pot per person.* What folketrygden does not pay out is not money the state "takes"; it finances the long-lived of the same cohort. Inheritance must be paid by someone else.
- *The insurance gets dearer.* Without early deaths "paying" for long lives, pensions must fall for everyone or contributions rise.
- *Those who live long need the money most.* A 95-year-old with no other income is more vulnerable than the heirs of someone who died at 70.
- *Inheritance widens gaps between families.* Heirs are often adult children in their 50s and 60s.
- *People can already choose.* IPS, private savings and life insurance go to survivors.

## 7. Debate and reforms in Norway

In the sources we reviewed, inheritance of pension has not featured in the major pension debates.

- **The Pension Committee (NOU 2022:7)** proposed age limits that follow life expectancy from the 1964 cohort, minimum levels indexed to wages and better terms for disabled people. Inheritance and survivors are not mentioned in the government's summary.
- **The pension settlement of 29 February 2024** (Meld. St. 6 (2023–2024), Innst. 233 S) keeps the life-expectancy adjustment, which has become stronger than expected: the 1963 cohort's pension at 67 is "8.1 per cent lower than the Pension Commission assumed" (Innst. 233 S). Survivor pensions appear only as a heading in the part we could read.
- **The 2024 survivor reform** replaced the survivor's pension with a time-limited transition benefit.
- **Today's figures:** folketrygden paid just over NOK 334 bn in old-age pension in 2025 to about 1,085,000 people (Pension Policy Working Group, May 2026).
- **Parliament:** we found no private member's bill on pension inheritance in the 2026–2027 session. Older sessions and press debate were not reviewed.

We found no official costing of inheritable pension in Norway, so a Debt.alarm proposal may be new to the debate.

## 8. Other countries

No country we looked at lets the public basic pension be inherited. The differences lie in the saved part and in the choices people get.

| Country | What happens at death | Source |
|---|---|---|
| Sweden, income pension | No survivor protection. Inheritance gains from the deceased are distributed yearly to remaining pensioners and savers | Pensionsmyndigheten |
| Sweden, premium pension | The account is distributed monthly as inheritance gains. Optional survivor protection at first withdrawal: the partner gets the pension for life, but your own pension is lower, by 7–46 % depending on both ages in Pensionsmyndigheten's example table (age 66 with a partner of 60: SEK 775 per 1,000, 22.5 % lower). Irreversible | Pensionsmyndigheten |
| Sweden, occupational pension | Optional refund cover: the family gets the money, for lifelong payouts for up to 20 years. Without it the pension can be 5–15 % higher | Swedbank |
| Denmark, state pension and ATP | State pension stops the day after death. ATP pays a spouse or cohabitant (registered with ATP) a lump sum, for contributions after 2002: the full DKK 75,000 on death before state pension age; after that it falls by DKK 15,000 a year from the following year and is gone 5 years after state pension age. 40 % goes to the state as a levy | borger.dk |
| Denmark, labour-market pensions | Often include insurance for survivors on death before retirement. The supplementary labour-market pension goes to the estate with a 40 % levy | borger.dk |
| Australia, superannuation | The balance is paid as a death benefit to a spouse, children (any age) or the estate, by binding nomination or trustee discretion. A non-dependant under super law must take a lump sum | ATO |

Sweden shows that inheritable pension has a price paid by the person. Australia shows that full inheritance works when the pension is a plain savings account, but then nothing guarantees the money lasts a lifetime.

## 9. Possible proposals and their cost

A guaranteed payout period of 5–10 years to the family is the most realistic proposal. Full inheritance of everything unused is possible but expensive.

| Proposal | What the family gets | Cost, % of old-age pension | Order of magnitude, NOK bn per year |
|---|---|---|---|
| 1. Optional partner protection (as in Sweden) | Partner gets the pension for life, if the person chooses it | Paid by the chooser through a lower pension (7–46 % in Sweden) | about 0 |
| 2. Guaranteed payout for 5 years from withdrawal | The rest of the 5 years to spouse, cohabitant, children or estate | 0.5–0.7 % | about 2 |
| 3. Guaranteed payout for 10 years | As above, 10 years | 2.5–3.3 % | 8–11 |
| 4. Balance on death before 67 goes to the family | The whole balance, e.g. in the same order as defined contribution | 4.7–6.3 % (less if only spouse and children) | 16–21 |
| 5. Full inheritance of the unused balance after 67 | Balance minus what was paid, to the estate | 9.4–12.4 % extra, or a 12–18 % lower pension for everyone | 32–41 |

**Method.** Percentages are the extra cost divided by expected pension payments, from the model in part 5. That is why proposal 5 (9.4–12.4 %) looks lower than what is never paid out (11–14 % of the *balance*): payments are 110–118 % of the balance. NOK figures are the percentage times 2025 old-age pension spending (NOK 334 bn). They show the order of magnitude at today's spending level and may be higher or lower once the new scheme is fully phased in. Proposals 2–4 can be paid with new money or by lowering everyone's pension by roughly the same percentage; proposal 4 in effect removes the inheritance gain from part 1, but that covers only part of its cost (about 3.5 % of payments in the model). Proposal 5 needs a 12–18 % lower pension for everyone, more than its cost, because a lower pension leaves more unused balance that must also be paid out.

Proposal 1 is not quite free: people with an ill partner will be more likely to choose the protection, and that may cost something.

**A lump sum, like Denmark's ATP,** is simplest to explain. One G (NOK 136,549 from 1 May 2026) to a spouse, cohabitant or children costs NOK 137 million per 1,000 deaths covered. Statistics Norway publishes deaths by age, but we have not fetched those figures yet.

**A proposal that fits Debt.alarm** could combine proposal 2 or 3 with proposal 1, plus a duty for Nav and pension companies to actively tell heirs about defined-contribution, IPS and paid-up policies with survivor cover when someone dies. Whether such money currently goes unclaimed has not been investigated and must be checked before it is used as an argument.

## Assumptions and uncertainty

- The statutes (Defined Contribution Pensions Act, National Insurance Act chapter 20) could not be opened; the contribution rules rest on the banks' and the Tax Administration's descriptions.
- The divisor 16.11 comes from Smarte Penger; Nav's own table and formula could not be opened. We cannot explain the whole gap between the divisor and the SSB table (part 5).
- How deaths between 62 and withdrawal affect the divisor is unresolved, as is the survivor right for older cohorts.
- The estimates use one life table for both sexes, one salary and one retirement age. They show orders of magnitude, not Nav's own calculations.
- No data about individuals has been used.
