# Verstädterung Philippinen & Metro Manila: Daten für das Poster (Stand: November 2026)

Legende: **[geprüft]** = Wert direkt aus der Primärdatei bzw. dem Primärdokument gelesen (Datei, Blatt, Zeile, Spalte angegeben). **[sekundär]** = nur über Sekundärquelle bzw. Suchmaschinen-Auszug einer PSA-Seite belegt (psa.gov.ph und alle rsso*.psa.gov.ph-Seiten waren gesperrt: Cloudflare 403 bzw. Proxy-Sperre). **[ungeprüft]** = nicht unabhängig bestätigt. **[abgeleitet]** = von mir berechnet, Formel angegeben.

Quelldateien (alle von population.un.org am 18.11.2026 heruntergeladen und mit Python/openpyxl/xlrd ausgelesen):
- WUP 2018 (Archiv-ZIP): https://population.un.org/wup/assets/Download/Archive/WUP2018-Excel-files.zip. Die alten Einzel-URLs `https://population.un.org/wup/Download/Files/WUP2018-F02-...xls` liefern inzwischen 404. Das ZIP enthält F02, F03, F05, F06, F09, F12, F15, F16 sowie DataSource-UrbanPopulation.xls. Blatt „Data“, Kopfzeile = Zeile 17, **Philippinen = Zeile 128** (Ländercode 608). Spalten E…Y = 1950, 1955 … 2050.
- WUP 2025, nationale Definitionen: `https://population.un.org/wup/assets/Download/Countries%20and%20Aggregates/WUP2025-F14-National-Definitions_Pop_by_category.xlsx`, `...F15-National-Definitions_percPop_by_category.xlsx`, `...F16-National-Definitions_Pop_rate_by_category.xlsx`, `...F17-National-Definitions_percPop_rate_by_category.xlsx`
- WUP 2025, Degree of Urbanisation (DEGURBA): `.../Countries%20and%20Aggregates/WUP2025-F02-Degree-of-Urbanization_percPop_by_category.xlsx`, `...F03-..._Pop_rate_by_category.xlsx`, `...F04-..._percPop_rate_by_category.xlsx`
- WUP 2025, Städte: `https://population.un.org/wup/assets/Download/Cities/WUP2025-F21-DEGURBA-Cities_Pop.xlsx`, `.../Cities/WUP2025-F18-DEGURBA-100_Largest_Cities.xlsx`
- WUP 2025, Metadaten der Datenquellen: `https://population.un.org/wup/assets/Download/WUP2025-M02-DataSources-National-Definitions-UrbanPercentage.xlsx`
- Aufbau der WUP-2025-Dateien: Kopfzeile in Zeile 1, **Philippinen = Zeile 161** in jedem Datenblatt (F02–F04, F14–F17). Jahresspalten: 1950 = K, 1960 = U, 1970 = AE, 1980 = AO, 1990 = AY, 2000 = BI, 2010 = BS, 2015 = BX, 2020 = CC, 2024 = CG, 2025 = CH, 2030 = CM, 2040 = CW, 2050 = DG.

---

## 1. Verstädterungsgrad (Anteil der städtischen Bevölkerung an der Gesamtbevölkerung) der Philippinen

### Takeaway
Nach nationaler Definition (PSA-Zensus 2020) lebten **54,0 %** der Filipinos in städtischen Barangays. UN WUP 2025 (nationale Definition, Jahresmitte) nennt **54,1 % (2020)**, **55,8 % (2025)** und **60,4 % (2050, Projektion)**. Die ältere WUP 2018 nennt für 2020 nur 47,4 %, weil ihr der Zensus 2020 noch nicht vorlag. Die UN-Kategorie „Degree of Urbanisation“ (Cities + Towns) ergibt wegen der anderen Definition einen viel höheren Wert: **85,2 % (2025)**. Für das Poster nur EINE Reihe verwenden, empfohlen: WUP 2025 nationale Definition + PSA 2020.

### Cited Findings

**Tabelle A: Verstädterungsgrad Philippinen in % (Jahresmitte)**

| Jahr | WUP 2025, nationale Definition (F15, Blatt „Urban“) [geprüft] | WUP 2018 (F02) [geprüft] | WUP 2025, DEGURBA „Cities and Towns“ (F02) [geprüft] | davon nur „Cities“ (DEGURBA) [geprüft] |
|---|---|---|---|---|
| 1950 | 25,24 | 27,14 | 47,50 | 19,68 |
| 1960 | 30,01 | 30,30 | 57,14 | 24,92 |
| 1970 | 31,86 | 32,98 | 64,34 | 29,95 |
| 1980 | 33,85 | 37,46 | 68,93 | 33,87 |
| 1990 | 36,00 | 46,99 | 74,48 | 36,05 |
| 2000 | 39,14 | 46,14 | 78,78 | 37,38 |
| 2010 | 45,52 | 45,33 | 82,00 | 39,23 |
| 2015 | 51,15 | 46,28 | 83,58 | 40,56 |
| 2020 | **54,11** | 47,41 | 84,81 | 41,47 |
| 2025 | **55,77** | 48,96 | **85,22** | 41,96 |
| 2030 (Proj.) | 57,26 | 50,92 | 85,59 | 42,28 |
| 2040 (Proj.) | 59,51 | 56,00 | 86,32 | 43,04 |
| 2050 (Proj.) | **60,41** | 61,78 | 86,77 | 43,87 |

- Exakte Werte WUP 2025 F15 „Urban“, Zeile 161: 1950 = 25.2406 (K), 1970 = 31.8647 (AE), 1990 = 36.0012 (AY), 2010 = 45.5208 (BS), 2020 = 54.1078 (CC), 2024 = 55.4521 (CG), 2025 = 55.7733 (CH), 2026 = 56.0874 (CI), 2050 = 60.4076 (DG). Titel der Datei: „File 15: Percentage of Population by national urban definition at Mid-Year … 1950-2050 (per cent)“. — [UN DESA WUP 2025 F15](https://population.un.org/wup/assets/Download/Countries%20and%20Aggregates/WUP2025-F15-National-Definitions_percPop_by_category.xlsx) [geprüft]
- Absolutwerte WUP 2025 F14, in Tausend, Zeile 161: städtische Bevölkerung 2020 = 60 644,67 / gesamt 112 081,26. 2025: 65 135,93 / 116 786,96. 2050: 81 171,79 / 134 373,44. — [UN DESA WUP 2025 F14](https://population.un.org/wup/assets/Download/Countries%20and%20Aggregates/WUP2025-F14-National-Definitions_Pop_by_category.xlsx) [geprüft]
- WUP 2018 F02, Blatt „Data“, Zeile 128, Spalten E (1950) bis Y (2050): 27.135, 28.702, 30.297, 31.604, 32.979, 35.56, 37.456, 42.235, 46.986, 46.56, 46.135, 45.71, 45.332, 46.284, 47.408, 48.958, 50.924, 53.285, 55.999, 58.912, 61.777. Die Werte gelten für 1950, 1955 … 2050. — [UN DESA WUP 2018 (ZIP), F02-Proportion_Urban.xls](https://population.un.org/wup/assets/Download/Archive/WUP2018-Excel-files.zip) [geprüft]
- WUP 2018 stützte sich nur auf die Zensen 1960, 1970, 1975, 1980, 1990, 2010 und 2015, also nicht auf 2020 (DataSource-UrbanPopulation.xls, Zeile 180). — [WUP 2018 ZIP](https://population.un.org/wup/assets/Download/Archive/WUP2018-Excel-files.zip) [geprüft]
- WUP 2025 DEGURBA F02, Zeile 161: „Cities and Towns“ 2025 = 85.222 (CH), „Cities“ 2025 = 41.963, „Towns“ (Towns and semi-dense areas) 2025 = 43.259, „Rural“ 2025 = 14.778. Definition laut Info-Blatt: Cities = mindestens 1 500 Einw./km² und mindestens 50 000 Einw.; Towns/semi-dense = mindestens 300 Einw./km² und mindestens 5 000 Einw.; Grundlage sind 1-km²-Rasterzellen. — [UN DESA WUP 2025 F02](https://population.un.org/wup/assets/Download/Countries%20and%20Aggregates/WUP2025-F02-Degree-of-Urbanization_percPop_by_category.xlsx) [geprüft]
- **PSA-Zensus 2020 (Stichtag 1. Mai 2020):** In der UN-Metadatendatei M02, Blatt „Urban_percentage“, Zeile 2600, ist für den „Philippines 2020 Census“ als Urban-Anteil DataValue = **54.0484008789062 %** eingetragen (Quelle: UNSD Demographic Yearbook 2022). 2015: 51.227 % (Zeile 2599), 2010: 45.330 % (Zeile 2598). — [UN DESA WUP 2025 M02](https://population.un.org/wup/assets/Download/WUP2025-M02-DataSources-National-Definitions-UrbanPercentage.xlsx) [geprüft, als UN-Wiedergabe der PSA-Zahl]
- PSA-Pressetext (laut Suchauszug und PNA): „58.93 million or 54.0 percent of the total 109.03 million population … lived in urban barangays“ (2020). 2015 waren es 51,73 Mio. bzw. 51,2 %. Ländliche Bevölkerung 2020: 50,10 Mio. bzw. 46,0 %. — [PSA: Urban population of the Philippines increases by 7.20 million](https://psa.gov.ph/statistics/population-and-housing/node/167692) [sekundär, Seite selbst gesperrt]; [PNA: More Filipinos prefer to live in urban communities](https://www.pna.gov.ph/articles/1178272) [sekundär]
- **Abweichung in PSA-Tabellen:** Eine PSA-Tabelle nennt 59 022 292 Stadtbewohner von 109 033 245. Eine andere Regionaltabelle nennt 58 930 729 (2020) bzw. 51 728 697 (2015, von 100 979 303). — [PSA Press Release PDF](https://psa.gov.ph/system/files/phcd/2022-12/1_PR_Urban%2520Population_RML_063022_ONS-signed.pdf) [sekundär, nur Suchauszug]. Entscheidung siehe Inferences.

### Inferences
- [abgeleitet] 58 930 729 / 109 033 245 × 100 = **54,0484 %**. Das stimmt auf 4 Nachkommastellen mit dem UN-M02-Wert überein. 59 022 292 / 109 033 245 ergäbe 54,13 %. Die Zahl **58 930 729 (54,0 %)** ist also die konsistente Zahl, 59 022 292 vermutlich ein Tabellenfehler.
- [abgeleitet] PSA 2015: 51 728 697 / 100 979 303 × 100 = 51,227 %. Das deckt sich mit M02 (51,227 %).
- Die Gesamtbevölkerung der Urban-Tabelle (109 033 245) liegt um 2 098 unter dem offiziellen Zensus-Total von 109 035 343 (Differenz [abgeleitet]). Die Ursache ist nicht geprüft.
- Definitionswechsel für die Poster-Fußnote: WUP 2018 und WUP 2025 F14–F17 verwenden die **nationale** Definition, auf den Philippinen das städtische Barangay nach PSA-Kriterien. WUP 2025 F01–F13 verwenden das international einheitliche **Degree of Urbanisation**, ein Rasterverfahren. Dadurch erscheinen die Philippinen zu rund 85 % „städtisch“ statt zu rund 56 %. Die beiden Reihen dürfen nicht in einem Diagramm gemischt werden.
- Die WUP-2018-Reihe zeigt zwischen 1990 und 2010 einen Rückgang (46,99 % → 45,33 %). Dahinter steckt vermutlich ein Definitionswechsel in den Zensen, keine echte Entstädterung. In WUP 2025 (national) steigt die Reihe dagegen stetig. Für das Poster daher WUP 2025 verwenden.

### Gaps
- Die PSA-Originaltabellen (psa.gov.ph) konnten nicht direkt geöffnet werden (Cloudflare 403, Regionalportale per Proxy gesperrt). PSA-Zahlen sind deshalb nur über die UN-Datei M02 [geprüft] und Suchauszüge bzw. PNA [sekundär] belegt.
- Weltbank-Werte wurden nicht abgerufen. Sie beruhen ohnehin auf WUP 2018.

---

## 2. Verstädterungsrate (jährliche Veränderungsrate der Stadtbevölkerung bzw. des Verstädterungsgrads)

### Takeaway
Die städtische Bevölkerung der Philippinen wuchs 2015–2020 laut PSA um rund **2,8 % pro Jahr** (+7,2 Mio.). Laut WUP 2025 (nationale Definition) wächst sie 2020–2025 nur noch um **≈ 1,43 % pro Jahr**, der Verstädterungsgrad selbst um ≈ 0,61 % pro Jahr. WUP 2018 nennt für 2015–2020 nur 1,99 % pro Jahr (veraltet, ohne Zensus 2020).

### Cited Findings

**Tabelle B: Raten (exponentiell, % pro Jahr)**

| Zeitraum | Größe | Wert | Status/Quelle |
|---|---|---|---|
| 2015–2020 | Wachstum Stadtbevölkerung (PSA, Zensus) | 2,8 % p. a.; +7,20 Mio. | [sekundär] PSA/PNA |
| 2015–2020 | Wachstum Stadtbevölkerung (WUP 2018 F06) | 1,992 % p. a. | [geprüft] |
| 2015–2020 | Veränderung des Verstädterungsgrads (WUP 2018 F09) | 0,480 % p. a. | [geprüft] |
| 2020–2025 | Wachstum Stadtbevölkerung (WUP 2018 F06) | 2,044 % p. a. | [geprüft] |
| 2020–2025 | Veränderung des Verstädterungsgrads (WUP 2018 F09) | 0,643 % p. a. | [geprüft] |
| 2015–2020 | Wachstum Stadtbevölkerung (WUP 2025 national, aus F14) | 2,37 % p. a. | [abgeleitet] |
| 2020–2025 | Wachstum Stadtbevölkerung (WUP 2025 national, aus F14) | **1,43 % p. a.** | [abgeleitet] |
| 2020–2025 | Veränderung des Verstädterungsgrads (WUP 2025 national, aus F15) | **0,61 % p. a.** | [abgeleitet] |
| 2025–2050 | Wachstum Stadtbevölkerung (WUP 2025 national) | 0,88 % p. a. | [abgeleitet] |
| 2025 | Jahreswert Wachstum Stadtbevölkerung (WUP 2025 F16, Spalte CH) | 1,3757 % | [geprüft] |
| 2025 | Jahreswert Veränderung des Verstädterungsgrads (WUP 2025 F17, Spalte CH) | 0,5697 % | [geprüft] |
| 2025 | Gesamtbevölkerung (WUP 2025 F16 „Total“, CH) | 0,8060 % | [geprüft] |

- WUP 2018 F06 („Average Annual Rate of Change of the Urban Population“), Zeile 128, 5-Jahres-Perioden: 1950–55: 4.66; 1980–85: 5.13; 1985–90: 4.76; 1990–95: 2.22; 2010–15: 2.05; 2015–20: 1.99198; 2020–25: 2.04438; 2045–50: 1.708. — [WUP 2018 ZIP, F06-Urban_Growth_Rate.xls](https://population.un.org/wup/assets/Download/Archive/WUP2018-Excel-files.zip) [geprüft]
- WUP 2018 F09 („Average Annual Rate of Change of the Percentage Urban“), Zeile 128: 2015–20: 0.47989; 2020–25: 0.64344; 1990–95 bis 2005–10 jeweils negativ (−0.18 bis −0.17). — [WUP 2018 ZIP, F09-Urbanization_Rate.xls](https://population.un.org/wup/assets/Download/Archive/WUP2018-Excel-files.zip) [geprüft]
- [abgeleitet] Kontrollrechnung WUP 2018: 100 × ln(52 008,603 / 47 078,199) / 5 = 1,992 %. Das bestätigt die F06-Formel r = 100 × ln(P₂/P₁)/n. Die Werte stammen aus F03, Zeile 128.
- WUP 2025 F16/F17 enthalten **Jahreswerte** (Spalte = Jahr), z. B. F16 „Urban“ 2020 = 1.7395, 2024 = 1.4013, 2025 = 1.3757. F17 „Urban“ 2020 = 0.6629, 2025 = 0.5697. — [WUP 2025 F16](https://population.un.org/wup/assets/Download/Countries%20and%20Aggregates/WUP2025-F16-National-Definitions_Pop_rate_by_category.xlsx), [WUP 2025 F17](https://population.un.org/wup/assets/Download/Countries%20and%20Aggregates/WUP2025-F17-National-Definitions_percPop_rate_by_category.xlsx) [geprüft]
- PSA: „The urban population … increased at an average of 2.8 percent annually during the period 2015 to 2020“, also +7,20 Mio. — [PSA node/167692](https://psa.gov.ph/statistics/population-and-housing/node/167692) [sekundär, Suchauszug]
- WUP 2025 DEGURBA F03 (Stadt- und Kleinstadtbevölkerung „Cities and Towns“), Jahreswert 2025 = 0.8969 % (CH). F04 (Anteil „Cities and Towns“) 2025 = 0.0908 %. — [WUP 2025 F03](https://population.un.org/wup/assets/Download/Countries%20and%20Aggregates/WUP2025-F03-Degree-of-Urbanization_Pop_rate_by_category.xlsx), [F04](https://population.un.org/wup/assets/Download/Countries%20and%20Aggregates/WUP2025-F04-Degree-of-Urbanization_percPop_rate_by_category.xlsx) [geprüft]

### Inferences
- [abgeleitet] Formel für die 5-Jahres-Raten aus WUP 2025: r = 100 × ln(Wert_Ende / Wert_Anfang) / Jahre.
  - Stadtbevölkerung 2020–2025: 100 × ln(65 135,932 / 60 644,675) / 5 = **1,429 % p. a.**
  - Verstädterungsgrad 2020–2025: 100 × ln(55,7733 / 54,1078) / 5 = **0,606 % p. a.**
  - Stadtbevölkerung 2015–2020: 100 × ln(60 644,675 / 53 872,761) / 5 = 2,368 % p. a.
  - Verstädterungsgrad 2015–2020: 100 × ln(54,1078 / 51,1549) / 5 = 1,122 % p. a.
  - Stadtbevölkerung 2025–2050: 100 × ln(81 171,786 / 65 135,932) / 25 = 0,880 % p. a.
- [abgeleitet] PSA-Rate nachgerechnet: Zensusstichtage 1.8.2015 und 1.5.2020, also 4,75 Jahre. 100 × ln(58 930 729 / 51 728 697) / 4,75 = 2,74 % p. a. Die PSA veröffentlicht 2,8 %; ihre genaue Formel ist nicht geprüft. Absoluter Zuwachs: 58 930 729 − 51 728 697 = 7 202 032.
- Die Jahreswerte in WUP 2025 F16 lassen sich nicht exakt aus den Jahreswerten in F14 nachrechnen (2020: Datei 1,7395 gegenüber ln-Differenz 2020→2021 = 1,537 bzw. 2019→2020 = 1,873). Die Berechnungskonvention der UN ist im Info-Blatt nicht dokumentiert. Für das Poster daher besser die oben abgeleiteten 5-Jahres-Raten **mit Formel** verwenden oder die F16/F17-Jahreswerte ausdrücklich als „Jahreswert 2025 laut UN“ kennzeichnen.
- Begriff „Verstädterungsrate“: Im Schulkontext meint der Begriff meist das Wachstum der Stadtbevölkerung (F06/F16). Die Veränderungsrate des Verstädterungsgrads (F09/F17) ist eine andere Größe. Auf dem Poster klar benennen, welche gemeint ist.

### Gaps
- Kein frei zugängliches PSA-Originaldokument mit der genauen Rechenformel für die 2,8 %.

---

## 3. NCR (Metro Manila): 100 % städtisch und Anteil an der Gesamtbevölkerung

### Takeaway
Die Aussage „NCR ist zu 100 % städtisch“ ist **bestätigt**: Nach PSA-Definition 2020 gelten alle Barangays der NCR automatisch als urban. Der Bevölkerungsanteil der NCR betrug 2024 **12,4 %** (14 001 751 von 112 729 484) und 2020 **12,4 %** (13 484 462 von 109 035 343).

### Cited Findings
- PSA-Urban-Definition 2020, wörtlich in UN M02, Blatt „Urban_definitions“, Zeile 2599: „A barangay is classified as urban if it meets any of the following: 1. It has a population size of 5,000 or more; or 2. It has at least one establishment with a minimum of 100 employees; or 3. It has five or more establishments with 10 to 99 employees and five or more facilities within a two-kilometer radius of the barangay hall. **Further, all barangays in the National Capital Region (NCR) are automatically classified as urban.**“ — [UN DESA WUP 2025 M02](https://population.un.org/wup/assets/Download/WUP2025-M02-DataSources-National-Definitions-UrbanPercentage.xlsx) [geprüft]
- PSA (Suchauszug): Die 1 710 Barangays der NCR wurden automatisch als urban eingestuft. Neben der NCR lagen 4 weitere Regionen über dem nationalen Wert von 54,0 %: Calabarzon, Central Luzon, Davao Region und Soccsksargen. — [PSA node/167692](https://psa.gov.ph/statistics/population-and-housing/node/167692) [sekundär]
- NCR-Bevölkerung laut Zensus 2024 (POPCEN, Stichtag 1. Juli 2024): 14 001 751. Zensus 2020: 13 484 462. 2015: 12 877 253. — [Wikipedia: Metro Manila](https://en.wikipedia.org/wiki/Metro_Manila), Zitat PSA [sekundär]
- Philippinen gesamt 2024: 112 729 484 (Stichtag 1. Juli 2024), amtlich festgestellt durch Proclamation No. 973 vom 11. Juli 2025. Zensus 2020: 109 035 343 (Stichtag 1. Mai 2020). Wachstum 2020–2024: 0,80 % p. a. — [Lawphil: Proclamation No. 973 (2025)](https://lawphil.net/executive/proc/proc2025/proc_973_2025.html); [Philstar](https://www.philstar.com/headlines/2025/07/18/2458844/philippines-population-reached-1127-million-2024-psa) [sekundär, Suchauszug; Lawphil nicht direkt geöffnet]
- Fläche der NCR: 636,00 km²; Dichte ≈ 22 000 Einw./km² (2024). — [Wikipedia: Metro Manila](https://en.wikipedia.org/wiki/Metro_Manila) [sekundär]

### Inferences
- [abgeleitet] NCR-Anteil 2024 = 14 001 751 / 112 729 484 × 100 = **12,42 %**
- [abgeleitet] NCR-Anteil 2020 = 13 484 462 / 109 035 343 × 100 = **12,37 %**
- [abgeleitet] Anteil der NCR an der Stadtbevölkerung 2020: Bei 100 % Verstädterung gilt 13 484 462 / 58 930 729 × 100 ≈ 22,9 %. Das ist als Ableitung zu kennzeichnen; die Urban-Tabelle verwendet eine leicht andere Gesamtbasis.
- Hinweis für das Poster: Die NCR (16 Städte + Pateros) ist eine Verwaltungsregion. Das tatsächliche zusammenhängende Siedlungsgebiet „Greater Manila“ reicht weit in Bulacan, Rizal, Cavite und Laguna hinein. Siehe Abschnitt 4: Laut UN-DEGURBA sind es rund 24,7 Mio. Einwohner.

### Gaps
- Die PSA-Regionaltabelle mit dem „level of urbanization“ je Region (NCR = 100,0) konnte nicht direkt eingesehen werden. Belegt ist der 100-%-Status über die Definition (geprüft) und den Suchauszug (sekundär).

---

## 4. Metropolisierung / Primacy (Manila gegenüber der zweitgrößten Stadt)

### Takeaway
Manila ist eine ausgeprägte **Primatstadt**. Nach WUP 2025 (Degree of Urbanisation, Stadt als zusammenhängendes Siedlungsgebiet) hat die Stadtregion Manila 2025 **24,7 Mio.** Einwohner, Cebu als zweitgrößte Stadt 3,0 Mio. Der Primacy-Index (Bevölkerung Stadt 1 / Stadt 2) liegt damit bei **≈ 8,1**. Rund **21 %** aller Filipinos leben in der Stadt Manila nach DEGURBA-Abgrenzung.

### Cited Findings

**Tabelle C: Größte Städte (Tausend Einwohner, Jahresmitte)**

| Quelle / Abgrenzung | Jahr | Manila | 2. Stadt | 3. Stadt |
|---|---|---|---|---|
| WUP 2025 F21 (DEGURBA „City“) [geprüft] | 2020 | 24 013,676 | Cebu City 2 889,534 | Davao City 1 470,399 |
| WUP 2025 F21 (DEGURBA „City“) [geprüft] | 2025 | **24 735,305** | Cebu City **3 044,564** | Davao City 1 546,026 |
| WUP 2025 F21 (DEGURBA „City“) [geprüft] | 2050 (Proj.) | 27 119,826 | Cebu City 3 651,959 | Davao City 1 912,096 |
| WUP 2018 F12 (Agglomeration, Manila = NCR) [geprüft] | 2020 | 13 923,452 | Davao City 1 825,45 | Cebu City 980,07 |
| WUP 2018 F12 [geprüft] | 2025 (Proj.) | 15 230,559 | Davao City 2 033,986 | Cebu City 1 061,623 |

- WUP 2025 F21 („Population Residing in Cities with 50,000 Inhabitants or More … (thousands)“), Blatt „Data“: Manila in Zeile 13357 (City_Code 2369), Cebu City in Zeile 13310, Davao City in Zeile 13319. Spalte BE = 2020, Spalte BJ = 2025. Insgesamt sind 162 philippinische Städte enthalten. — [UN DESA WUP 2025 F21](https://population.un.org/wup/assets/Download/Cities/WUP2025-F21-DEGURBA-Cities_Pop.xlsx) [geprüft]
- WUP 2025 F18 (100 größte Städte der Welt): Manila belegt 2020 Rang 7 (24 013,676 Tsd.; Landfläche 2 373 km²), 2025 Rang 8 (24 735,305 Tsd.; 2 438 km²; bebaute Fläche 483,0 km²) und 2050 Rang 9 (Proj.). Fundstellen: Blatt „Data“, Zeilen 908, 1009 und 1510. — [UN DESA WUP 2025 F18](https://population.un.org/wup/assets/Download/Cities/WUP2025-F18-DEGURBA-100_Largest_Cities.xlsx) [geprüft]
- WUP 2018 F12, Zeile 1365: Manila mit Fußnote (95), die lautet: „Refers to the National Capital Region.“ Werte 1950 = 1 543,666; 1975 = 4 999,303; 2000 = 9 957,962; 2020 = 13 923,452; 2035 = 18 649,422 (Tsd.). — [WUP 2018 ZIP, F12-Cities_Over_300K.xls](https://population.un.org/wup/assets/Download/Archive/WUP2018-Excel-files.zip) [geprüft]
- WUP 2018 F16 (Anteil der Agglomeration an der Gesamtbevölkerung, %), Zeile 1365: Manila 2020 = 12,692 %. F15 (Anteil an der Stadtbevölkerung): Manila 2020 = 26,771 %, 1975 = 34,045 % (Höchstwert der Reihe). — [WUP 2018 ZIP](https://population.un.org/wup/assets/Download/Archive/WUP2018-Excel-files.zip) [geprüft]

### Inferences
- [abgeleitet] Primacy-Index (2-Städte-Index = P₁/P₂):
  - WUP 2025 DEGURBA 2025: 24 735,305 / 3 044,564 = **8,12** (2020: 8,31; 2050: 7,43)
  - WUP 2018 (NCR-Abgrenzung) 2020: 13 923,452 / 1 825,45 (Davao) = **7,63** (2025: 7,49)
- [abgeleitet] Anteil von Manila (DEGURBA) an der Gesamtbevölkerung 2025: 24 735,305 / 116 786,962 (WUP 2025 F14 „Total“) × 100 = **21,2 %**. 2020: 21,4 %.
- Zweitgrößte Stadt je nach Quelle: In WUP 2018 ist es Davao (Stadtgrenze; Davao City umfasst eine sehr große Verwaltungsfläche). In WUP 2025 DEGURBA ist es Cebu (Metro-Cebu-Siedlungsgebiet). Auf dem Poster die Abgrenzung nennen.
- Der Index liegt in beiden Abgrenzungen deutlich über 2, dem Wert einer „ausgeglichenen“ Rangfolge nach der Rank-Size-Regel. Das ist ein klarer Beleg für **Metropolisierung bzw. Primacy**.

### Gaps
- Es wurde kein eigener, von PSA oder UN veröffentlichter Primacy-Index gefunden. Die Indizes oben sind eigene Ableitungen aus UN-Daten.
- PSA-Werte für Metro Cebu und Metro Davao (Zensus 2024) wurden nicht recherchiert, weil PSA nicht erreichbar war.
