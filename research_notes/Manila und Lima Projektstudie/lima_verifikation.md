# Lima – Verification of key figures against the original pages

Verification date: 16 Nov 2026. This file checks the figures in `lima_entwicklung.md` and `lima_herausforderungen.md`; those two files were not modified.

**Method.** The WebFetch tool failed with a DNS error for every host. Pages were therefore opened with `curl` through the session proxy and converted to text (HTML) or read with `pdftotext` (PDF). Where several URLs exist for the same document, the URL actually opened is the one listed.

**Hosts that could not be opened (status NOT VERIFIABLE for figures that depend on them):**
- Refused by the session proxy, although some are on the extended allowlist: `limacomovamos.org`, `www.limacomovamos.org`, `earthobservatory.nasa.gov`, `censos2025.inei.gob.pe`, `sistemas.inei.gob.pe`, `m.inei.gob.pe`, `tc.gob.pe`, `portal.indeci.gob.pe`, `www.un.org`, `es.wikipedia.org`, `www.uv.mx`, `www.lincolninst.edu`, `www.sedapal.com.pe`, plus the news sites `infobae.com`, `larepublica.pe` and `elperuano.pe`.
- Reached, but the site itself answered HTTP 403: `www.britannica.com`, `www.r4v.info`, `doi.org`, `openknowledge.worldbank.org`.
- One retry was made for each blocked host, without success.

**Status key.**
- **CONFIRMED**: the number or wording was seen on the opened page.
- **CORRECTED**: the opened page shows a different value.
- **NOT VERIFIABLE**: the page was blocked, or the figure was not found on the opened page.

---

## 1. Table

### A. Population series and reference units

| # | Claim in notes | Status | URL opened | Reference unit / year as stated on page | Short quote |
|---|---|---|---|---|---|
| A1 | Lima Metropolitana (Lima + Callao) total population 1940–1993: 661,508 / 1,901,927 / 3,418,452 / 4,835,793 / 6,434,323. Censada: 645,172 / 1,845,910 / 3,302,523 / 4,608,010 / 6,345,856 | CONFIRMED | https://proyectos.inei.gob.pe/web/biblioineipub/bancopub/Est/LIb0002/cap0101.htm | "Lima Metropolitana" = the 49 districts of 1993, i.e. Lima + Callao. The presentation page (https://proyectos.inei.gob.pe/web/biblioineipub/bancopub/Est/LIb0002/presenta.htm) says "los 49 distritos". Censuses 1940–1993. | Cuadro 1.1: "1940 … 661508 … 645172 … 1993 … 6434323 … 6345856" |
| A2 | Lima Metropolitana share of Peru 1940 → 1993 | CONFIRMED (new detail) | same as A1 | Lima Metropolitana total population vs. Peru total | Cuadro 1.2: "9,4 / 18,3 / 24,2 / 27,2 / 28,4" (%, 1940, 1961, 1972, 1981, 1993) |
| A3 | Provincia de Lima 1940 = 577,437 | **CORRECTED** | https://www.inei.gob.pe/media/MenuRecursivo/publicaciones_digitales/Est/Lib1483/cap03/cap03.pdf (INEI, Compendio Estadístico Perú 2017, cuadro 3.3) | "Provincia de Lima 3/" with footnote "Comprende los 43 distritos de la provincia de Lima". Población censada. | "Provincia de Lima 3/ 562 885 · 1 632 370 · 2 981 292 · 4 164 597 · 5 706 127 · 7 605 742" (1940, 1961, 1972, 1981, 1993, 2007). The value 577,437 was not found on any opened page. |
| A4 | Provincia de Lima 1961 = 1,682,509 | **CORRECTED** | same as A3 | Provincia de Lima, censada | 1961 = **1,632,370** |
| A5 | Provincia de Lima 1972, 1981 and 1993 (listed as a gap in the notes) | CONFIRMED (new) | same as A3 | Provincia de Lima, censada | 2,981,292 / 4,164,597 / 5,706,127 |
| A6 | Callao 1940–2007 (listed as a gap in the notes) | CONFIRMED (new) | same as A3 | "Prov. Const. del Callao", censada | "82 287 · 213 540 · 321 231 · 443 413 · 639 729 · 876 877". Check: Provincia de Lima 1940 (562,885) + Callao (82,287) = 645,172, which matches the Lima Metropolitana figure in A1. |
| A7 | 2007 Lima Metropolitana (incl. Callao): gap in the notes | CONFIRMED (new) | https://www.inei.gob.pe/media/MenuRecursivo/publicaciones_digitales/Est/Lib1375/cap03/cap03.pdf (INEI, Compendio Estadístico Perú 2016, cap. 3) | "Lima Metropolitana 3/" with footnote "3/ Comprende la provincia de Lima y la Provincia Constitucional del Callao". Censada, 2007. | "Lima Metropolitana 3/ 645 172 1 845 910 3 302 523 4 608 010 6 345 856 8 482 619". Urban censada 2007: 8,472,935. |
| A8 | 2007 Provincia de Lima = 7,605,742 censada | CONFIRMED | https://www.inei.gob.pe/media/MenuRecursivo/publicaciones_digitales/Est/Lib1583/15ATOMO_01.pdf | Provincia de Lima, censada | Cuadro 2.1: "2007 7 605 742 7 595 925 9 817" |
| A9 | 2017 Provincia de Lima = 8,574,974 censada | CONFIRMED | same as A8; also https://www.inei.gob.pe/media/MenuRecursivo/noticias/nota-de-prensa-no-108-2018-inei.pdf | "provincia de Lima (43 distritos)", censada 2017 | "la provincia de Lima (43 distritos) tiene 8 millones 574 mil 974 habitantes" |
| A10 | 2017 Provincia de Lima incl. omission = 9,162,322 | NOT VERIFIABLE | Lib1583 PDF (A8), full text searched | – | Not found in the cited PDF. No other INEI page with this figure was opened. |
| A11 | 2017 Callao = 994,494, growth 1.3%/yr | CONFIRMED | nota de prensa 108-2018 (A9) | Provincia Constitucional del Callao, censada 2017; growth 2007–2017 | "la Provincia Constitucional del Callao con 994 mil 494 habitantes y una tasa de 1.3%" |
| A12 | 2017 Lima Metropolitana (Lima + Callao) = 9,569,468 | CONFIRMED as arithmetic only | A9 + A11 | Sum of the two INEI censada figures. Not printed as one number on any opened page. | 8,574,974 + 994,494 = 9,569,468 |
| A13 | 2017: 8,567,786 urban residents (99.9%) | CONFIRMED | Lib1583 (A8) | Provincia de Lima, censada | "8 millones 567 mil 786 habitantes, lo que representa el 99,9%" |
| A14 | 2017 largest districts: SJL 1,038,495; SMP 654,083; Ate 599,196; Comas 520,450 | CONFIRMED | Lib1583 (A8) | Provincia de Lima, censada 2017 | "San Juan de Lurigancho (1 millón 38 mil 495 personas), San Martín de Porres (654 mil 83 personas), Ate (599 mil 196) y Comas (520 mil 450)" |
| A15 | Provincia de Lima = 29.2% of Peru (2017, censada) | NOT VERIFIABLE | Lib1583 (A8) searched | – | The percentage does not appear in the opened PDF. |
| A16 | 2023 projection: 10,151,000 = 30.1% of Peru; density 3,879.1 inh/km²; Surquillo densest; Punta Negra 69.6 inh/km² | CONFIRMED, with unit clarified | https://www.inei.gob.pe/media/MenuRecursivo/noticias/nota-de-prensa-no-006-2023-inei.pdf (same file the notes cited on m.inei.gob.pe) | INEI projection to 30 Jun 2023. "Lima Metropolitana" = "Lima con sus 43 distritos", so Callao is **not** included. | "Lima con sus 43 distritos alberga 10 millones 151 mil habitantes, los cuales representan el 30,1% de la población total del país (33 millones 726 mil)"; "densidad poblacional alcanza 3 879,1"; "Surquillo … 29 863,3 hab/km2"; "Punta Negra con 69,6 hab/km2" |
| A17 | 2021 projection (extra) | CONFIRMED (new) | https://www.inei.gob.pe/media/MenuRecursivo/noticias/nota-de-prensa-no-006-2021-inei.pdf | Provincia de Lima, projection to 30 Jun 2021 | "la provincia de Lima alcanza 9 millones 847 mil habitantes" |
| A18 | 2025 pre-census projection 10,432,133 | NOT VERIFIABLE | – (Infobae and Andina not opened; infobae.com blocked) | – | – |
| A19 | 2025 census, first results: Lima Metropolitana 10,129,708 = 29.7% of Peru's 34,157,732 | CONFIRMED | https://www.gob.pe/institucion/inei/noticias/1399446-inei-poblacion-del-peru-totalizo-34-millones-157-mil-732-habitantes-al-2025 (29 May 2026) | "Lima Metropolitana", listed beside **departments** (Piura, La Libertad, Arequipa). Callao appears separately as its own ámbito ("Provincia Constitucional del Callao (218 mil)" net migration). The national figure is **total population incl. omission**. | "Lima Metropolitana concentra el 29,7% de la población nacional, con 10 millones 129 mil 708 habitantes" |
| A20 | 2025 national figures | CONFIRMED | same as A19 | Peru, Censos Nacionales 2025 | "34 millones 157 mil 732"; "32 millones 706 mil 28 personas fueron efectivamente censadas"; omitted "1 millón 451 mil 704 … 4,25%"; growth "1,11%" (2017–2025) |
| A21 | 2025 census, provincial results: Lima Metropolitana about 9.6 million, growth 1.1%/yr | CONFIRMED | https://www.gob.pe/institucion/inei/noticias/1417313-censos-nacionales-2025-lima-metropolitana-continua-siendo-la-provincia-mas-poblada (10 Jul 2026) | "Lima Metropolitana" as a **province** (= Provincia de Lima). Callao is listed separately: "…Arequipa, Trujillo y la Provincia Constitucional del Callao superan el millón de personas, cada una". | "siendo Lima Metropolitana la más poblada del país con 9,6 millones de habitantes"; "Lima Metropolitana mantuvo un crecimiento moderado (1,1%)" |
| A22 | 2025 Callao population | NOT VERIFIABLE (exact figure) | A21 | Provincia Constitucional del Callao | The page says only "superan el millón de personas". The exact number would be on censos2025.inei.gob.pe, which is blocked. |
| A23 | 2025 districts: SJL 1,125,000; SMP 724,000; Ate 669,000; Comas 553,000; Callao district 456,000; Carabayllo +2.9%/yr | CONFIRMED | A21 | Districts, 2025 census; growth 2017–2025 | "San Juan de Lurigancho … 1 millón 125 mil habitantes, seguido de San Martín de Porres (724 mil), Ate (669 mil), Comas (553 mil) y Callao (456 mil)"; "Carabayllo (2,9%) en Lima" |
| A24 | 2025: 65.5% of foreigners live in Lima Metropolitana | CONFIRMED | A21 | Foreign population counted in the 2025 census | "la población extranjera censada en el país totalizó 1 millón 53 mil personas … el 65,5% de los extranjeros vive en Lima Metropolitana" |
| A25 | 2025: about 900,000 Venezuelans counted | NOT VERIFIABLE | A21 | – | No Venezuelan figure appears on the INEI page. It came from Infobae, which is blocked. |

### B. Migration, fertility, Venezuelans

| # | Claim | Status | URL opened | Unit / year on page | Quote |
|---|---|---|---|---|---|
| B1 | 36.4% of Provincia de Lima are lifetime in-migrants (2017) | CONFIRMED | https://www.inei.gob.pe/media/MenuRecursivo/noticias/nota-de-prensa-no-006-2021-inei.pdf | Provincia de Lima, Censos 2017 | "el 36,4% de la población de la provincia de Lima es inmigrante" |
| B2 | Share **born in another department** (2017) | CONFIRMED (exact value) | same as B1 | Provincia de Lima, 2017 | "el 32,79% nació en otro departamento del Perú, el 2,33% en otra provincia del departamento de Lima; mientras que, 1,28% nació en el extranjero". Top origins: Junín 3.93%, Áncash 3.02%, Cajamarca 2.61%, Ayacucho 2.19%; 1.5% were born in Callao. |
| B3 | El Búho: 31.6% / 2,985,643 (Lima region + Callao) | NOT VERIFIABLE | – (elbuho.pe not tried; not an official source) | – | Use B2 instead. |
| B4 | TFR Lima Metropolitana 1.22 (ENDES 2024) | CONFIRMED | https://proyectos.inei.gob.pe/endes/2024/departamentales/Endes15/pdf/Lima_Metropolitana.pdf | "Lima Metropolitana" (ENDES; the page does not define the districts). Refers to the 3 years before the survey. | "La Tasa Global de Fecundidad (TGF) estimada para Lima Metropolitana fue 1,22 hijos por mujer" |
| B5 | Departamento de Lima 1.6; Peru 1.8 / 1.76 (BCRP) | NOT VERIFIABLE | not opened (bcrp.gob.pe not on the allowlist) | – | – |
| B6 | Venezuelans: about 1,000,000 in Lima; 1.66 million / 1.54 million / 1.7 million in Peru (R4V, UNHCR) | NOT VERIFIABLE | https://www.r4v.info/es/peru and https://www.r4v.info/en/peru returned HTTP 403 | – | For the poster, only the INEI census statement (A24) is verified. |
| B7 | BCRP: Lima Metropolitana receives 40% of interdepartmental migration | NOT VERIFIABLE | not opened | – | – |
| B8 | 2025 census: Lima has the largest net internal migration (extra) | CONFIRMED (new) | A19 page | "Lima" (ámbito; the wording does not say whether this means Lima Metropolitana or the department), census 2025 | "Lima registró el mayor saldo migratorio … con 2 millones 300 mil personas … la Provincia Constitucional del Callao (218 mil)" |

### C. History and urban structure

| # | Claim | Status | URL opened | Unit / year on page | Quote |
|---|---|---|---|---|---|
| C1 | Founded 18 Jan 1535 by Pizarro as "Ciudad de los Reyes" | CONFIRMED (Wikipedia only; Britannica returned 403) | https://en.wikipedia.org/wiki/Lima | – | Infobox: "Established 18 January 1535"; founder Francisco Pizarro. Caveat: the text also says "on 6 January 1535, Lima was founded" and "its foundation was decided on January 6". 6 Jan is the Epiphany, which gave the name; 18 Jan is the official founding date. |
| C2 | City walls 1684–1687 | CONFIRMED | https://en.wikipedia.org/wiki/Lima | – | "construction of the Walls of Lima between 1684 and 1687" |
| C3 | Villa El Salvador founded 1971 (11 May 1971); legal district by DL 23605 on 1 Jun 1983 | CONFIRMED (year and 1983 law); the 11 May date is NOT VERIFIABLE | https://en.wikipedia.org/wiki/Villa_El_Salvador_District | – | "Founded 1971"; "began in 1971 as a squatted pueblo joven"; "Since June 1, 1983 … (by law № 23605) established as a district". The exact day 11 May was not on the page (es.wikipedia is blocked). Caveat: https://en.wikipedia.org/wiki/Lima says "in 1973 the self-managed community of Villa El Salvador was created", which is a conflicting date inside Wikipedia. Use "1971". |
| C4 | COFOPRI created 1996 | CONFIRMED | https://cdn.www.gob.pe/uploads/document/file/1379677/072-2016-cofopri-de-pei-2016-2018.pdf (COFOPRI, PEI 2016–2018) | National | "COFOPRI fue creado en 1996 mediante el Decreto Legislativo N° 803, Ley de Promoción del Acceso a la Propiedad Formal" |
| C5 | COFOPRI issued "about two million" titles; time to title cut from 7 years to 45 days (Lincoln Institute) | NOT VERIFIABLE (lincolninst.edu blocked) | – | – | The official alternative from the same PEI as C4, at national level: baseline "Cantidad de predios formalizados … 2459803 … 1996-2015". These are formalised urban plots, **not** titles, and the figure covers all of Peru, not only Lima. |
| C6 | Matos Mar barriada shares: 1956 9.5%; 1959 14.3%; 1961 17%; about 2010 36.5% in more than 3,000 barriadas | NOT VERIFIABLE | https://www.uv.mx/… (blocked) | – | No allowed host holds the text. |
| C7 | Provincia de Lima = 43 districts | CONFIRMED | https://cdn.www.gob.pe/uploads/document/file/1903877/Lima%20Metropolitana_Informaci%C3%B3n%20Territorial%20Completo.pdf (PCM, Viceministerio de Gobernanza Territorial); also the footnote in A3 | Provincia de Lima | "La provincia de Lima, está conformada por 43 distritos" |
| C8 | Area of Provincia de Lima 2,672.28 km² | **Conflicting sources** (not CONFIRMED by an official source) | PCM PDF (C7); https://en.wikipedia.org/wiki/Lima | PCM: Provincia de Lima. Wikipedia: "Metropolitan Lima" = province. | PCM: "una extensión territorial aproximada de 2 638 kilómetros cuadrados". Wikipedia: "Metropolitan Lima covers 2,672.28 square kilometres". INEI area not found. |
| C9 | Lima + Callao 2,819 km² | CONFIRMED on Wikipedia only (CAF not opened) | https://en.wikipedia.org/wiki/Lima_metropolitan_area | Conurbation Lima + Callao | "The conurbation has an area of 2,819.26 km2"; the Lima infobox gives "Metro 2,819.3 km2" |
| C10 | 50 districts (43 + 7 Callao) | NOT VERIFIABLE on an opened official page | – | – | Only "43" was confirmed (C7). The 1996 INEI profile (A1) counts "49 distritos". That fits Callao having 6 districts before Mi Perú was created; Mi Perú's creation date was not checked. |
| C11 | Muro de la vergüenza: TC ruling 20 Dec 2022 (Exp. 01606-2018-PHC/TC), demolition within 180 days; demolition began Sept 2023 | NOT VERIFIABLE | tc.gob.pe blocked; news sites blocked | – | Only https://en.wikipedia.org/wiki/Wall_of_Shame_(Lima) could be opened. It redirects to "Squatting in Peru" and says the wall "by 2019 was ten kilometres (6.2 mi) long". Nothing about the ruling or the demolition. |

### D. Water (SUNASS)

| # | Claim | Status | URL opened | Unit / year on page | Quote |
|---|---|---|---|---|---|
| D1 | More than 635,000 people (6%) without SEDAPAL network water, "2023" | CONFIRMED, but **reference year CORRECTED** | https://www.gob.pe/institucion/sunass/noticias/689765-sunass-en-lima-metropolitana-hay-mas-de-635-mil-personas-sin-cobertura-de-agua-potable | Lima Metropolitana. The **data year is 2021 (ENAPRES)**; the press note is dated 18 Jan 2023. | "Más de 635 mil personas de Lima Metropolitana (es decir el 6 % de su población) no tienen acceso al agua potable desde la red pública de Sedapal … según la … (Enapres) del … INEI al año 2021." |
| D2 | Tanker water 16–18 S/ per m³ vs about 3 S/ per m³ from the network | CONFIRMED | same as D1 | Lima, statement of 18 Jan 2023 | "paga hasta 6 veces más por el metro cúbico (m3) del agua, entre 16 a 18 soles que debe comprar a camiones cisterna, cuando un usuario conectado a la red paga, en promedio, 3 soles por m3" |
| D3 | Per-capita use by district in 2022: San Isidro 280, Miraflores 238 … Lurigancho 32, Ancón 33, Santa Rosa 39, Pachacámac 39, Pucusana 41 | CONFIRMED | same as D1. This SUNASS page is the primary source, so Canal N and RPP are not needed. | Litres per inhabitant per day, average for 2022 | "San Isidro (280 litros), Miraflores (238), La Molina (210), Barranco (177) y San Borja (176) … Lurigancho (32), Ancón (33), Santa Rosa (39), Pachacamac (39) y Pucusana (41)" |
| D4 | Sewerage gap (extra) | CONFIRMED (new) | same as D1 | Lima Metropolitana, ENAPRES 2021 | "más de 904 mil personas … no tienen acceso a la red de alcantarillado … 8 %" |
| D5 | 2015/16 study: 15 S/ per m³; 72 S/ per month; 724 S/ per year saving | NOT VERIFIABLE | The old sunass.gob.pe URL redirects to a 404 page on gob.pe | – | – |
| D6 | ENDES 2024: 84.0% of dwellings get drinking water from the public network | CONFIRMED | ENDES PDF (B4) | Lima Metropolitana, ENDES 2024, drinking-water source | "En Lima Metropolitana, el 84,0% de las viviendas utilizaban el agua para beber por red pública" |
| D7 | Rímac supplies about 80% of Lima's water | NOT VERIFIABLE | No official page with this figure found; sedapal.com.pe blocked | – | Wikipedia (Lima) only says the Rímac is "a vital resource for the city, since it carries what will become drinking water". No percentage. |

### E. Hazards and climate

| # | Claim | Status | URL opened | Unit / year on page | Quote |
|---|---|---|---|---|---|
| E1 | INDECI scenario Mw 8.8 + tsunami: 110,313 dead, 2,096,824 injured, 353,497 dwellings destroyed, 623,882 uninhabitable | CONFIRMED | https://cdn.www.gob.pe/uploads/document/file/5183107/Estudio%20de%20vulnerabilidad%20y%20Riesgo%20S%C3%ADsmico%20en%20Lima%20%E2%80%93%20Callao.pdf (INDECI-DIPRE, "Escenario sísmico para Lima Metropolitana y Callao: Sismo 8.8Mw", 2017) | Lima Metropolitana **and** Callao; population base "más de 10'200,000 habitantes" (INEI projection 2017) | "se estima un total de 110,313 fallecidos, 2'096,824 heridos, 353,497 viviendas destruidas y 623,882 viviendas inhabitables (Tabla 19)" |
| E2 | Simulacro May 2026: 9,255 dead, 157,000 injured, 363,936 destroyed dwellings; MML 1,455,746 damnificados | NOT VERIFIABLE | Infobae blocked | – | – |
| E3 | INDECI: almost 1.5 million people in very high risk (2022) | NOT VERIFIABLE | La República blocked | – | – |
| E4 | El Niño Costero 2017, Lima region: about 16,000 damnificados, 41,000 afectados, 17 dead; national 162 dead, 141,000 damnificados, about 1 million afectados; 3,535 people in 25 shelters in Lurigancho | NOT VERIFIABLE | es.wikipedia, Infobae and mindef.gob.pe blocked; no INDECI compendium for 2017 found on an allowed host | – | https://en.wikipedia.org/wiki/2017_Peru_floods was opened. Its infobox gives "≥418 deaths, >824 injuries, 361 missing" for the whole event; that article also covers Ecuador and Colombia. It has no Lima figures, so it does not match the notes. |
| E5 | Annual rainfall 16 mm (Wikipedia, "Climate of Peru") | CONFIRMED as stated, but a **better value exists** | https://en.wikipedia.org/wiki/Climate_of_Peru | Lima, normals period not stated | "Lima's precipitation of 16 mm (0.63 in)" |
| E6 | Better rainfall value (SENAMHI normals, via Wikipedia) | CONFIRMED (Wikipedia table citing SENAMHI; senamhi.gob.pe itself not opened) | https://en.wikipedia.org/wiki/Lima | (a) Campo de Marte station, 123 m, 1991–2020. (b) Jorge Chávez airport station, 1991–2020. | (a) Annual precipitation "9.8 (0.39)" mm, "Source: … SENAMHI". (b) "6.4 (0.25)" mm (DWD/Meteo Climat). Also: "Coastal districts receive only 10 to 30 mm"; inland districts "10 and 60 mm". |
| E7 | "Desert city" ranking | Wikipedia wording found; no reliable source | https://en.wikipedia.org/wiki/Lima | – | "Lima is the world's third largest desert city, after Karachi, Pakistan, and Cairo, Egypt." The sentence carries no citation in the extracted text. Do not use it. |

### F. UN figure

| # | Claim | Status | URL opened | Unit / year on page | Quote |
|---|---|---|---|---|---|
| F1 | UN WUP 2025: Lima 10,580,000 (2025); 12,358,000 (2050); rank 32 | CONFIRMED | https://population.un.org/wup/assets/Download/Cities/WUP2025-F18-DEGURBA-100_Largest_Cities.xlsx and https://population.un.org/wup/assets/Download/Cities/WUP2025-F20-DEGURBA-Capital_Cities.xlsx. The data booklet on www.un.org was blocked. | "City" by Degree of Urbanisation (DEGURBA), mid-year, in thousands | 2025: "Rank_Order 32 … Lima … 10580.241"; 2050: "Rank 32 … 12358.372" |
| F2 | UN WUP series (extra, for a chart) | CONFIRMED (new) | F18 file (F1) | Same unit as F1. Land area and built-up area are in km². | Population in thousands: 1975 3,519.8 · 1980 4,207.1 · 1985 4,831.4 · 1990 5,487.0 · 1995 6,272.8 · 2000 6,991.7 · 2005 7,802.1 · 2010 8,532.4 · 2015 9,288.3 · 2020 10,036.6 · 2025 10,580.2 · 2030 11,145.0 · 2050 12,358.4. Land area of the city 607 km² (1975) → 1,026 km² (2025). |
| F3 | 33 megacities worldwide in 2025 | NOT VERIFIABLE | www.un.org blocked | – | – |

---

## 2. Notes

**1. The 2025 discrepancy (10,129,708 vs. about 9.6 million): what each figure refers to.**

What the two opened INEI pages show:
- **The 10,129,708 figure (29 May 2026, "primeros resultados").**
  - "Lima Metropolitana" is listed beside departments (Piura 2,115,587; La Libertad; Arequipa).
  - Callao is treated as a separate ámbito in the same note.
  - The 29.7% share is computed on the national **total population incl. omission** (34,157,732): 10,129,708 / 34,157,732 = 29.66%.
- **The "9,6 millones" figure (10 Jul 2026, provincial and district results).**
  - It refers to "Lima Metropolitana" as a **province**.
  - Callao is again separate ("la Provincia Constitucional del Callao superan el millón").
- **Conclusion.** Neither figure includes Callao. Both refer to the territory of the Provincia de Lima (43 districts). INEI has called the 43 districts "Lima Metropolitana" in its projections too (2023 note: "Lima con sus 43 distritos … 10 millones 151 mil").

Why the two numbers differ is **not stated** on either page. One possible explanation, which is my inference only:
- 10.13 million could be the total population incl. the estimated omission.
- 9.6 million could be the censada (counted) population.
- Support for this: in the July note, the rural share of 19.4% fits the censada base (6,334,000 / 32,706,028 = 19.4%), not the total (6,334,000 / 34,158,000 = 18.5%). So the July note at least partly uses censada figures.
- This was not confirmed on an INEI table, because censos2025.inei.gob.pe is blocked.

**Poster recommendation:** use 10,129,708 with the label "Lima Metropolitana (Provincia de Lima, 43 Distrikte), Zensus 2025, Gesamtbevölkerung inkl. Untererfassung (INEI, Mai 2026)". If "Lima + Callao" is wanted, the Callao 2025 figure (only "> 1 Mio.") still has to be checked on censos2025.inei.gob.pe.

**2. Reference units in the historical series.**
- Up to 2007, INEI uses "Lima Metropolitana" = **Lima + Callao** (footnote 3/ in Lib1375; "49 distritos" in LIb0002).
- In recent projections and the 2025 census, "Lima Metropolitana" = **Provincia de Lima only**.
- A consistent "Lima + Callao" censada series therefore reads:
  - 645,172 (1940)
  - 1,845,910 (1961)
  - 3,302,523 (1972)
  - 4,608,010 (1981)
  - 6,345,856 (1993)
  - 8,482,619 (2007)
  - 9,569,468 (2017; sum of 8,574,974 + 994,494)
- 2025 for Lima + Callao is not available yet; see note 1.

**3. Corrections to carry into the notes or poster.**
- Provincia de Lima 1940 = **562,885**, not 577,437. 1961 = **1,632,370**, not 1,682,509. Both are censada, INEI Compendio 2017.
- SUNASS "635,000 without network water" is **ENAPRES 2021** data, published 18 Jan 2023. It is not a 2023 measurement.
- The 2023 density of 3,879.1 inh/km² refers to the **43 districts**, not Lima + Callao.
- Rainfall: prefer **9.8 mm/yr (SENAMHI, Campo de Marte, 1991–2020)** over 16 mm. Coastal districts get 10–30 mm. The SENAMHI page itself was not opened; the figure comes from the Wikipedia table citing SENAMHI.
- Born in another department (Provincia de Lima, 2017) = **32.79%**. Total in-migrants incl. other provinces of the Lima department and abroad = 36.4%.

**4. Still open (NOT VERIFIABLE because of blocks).**
- Venezuelans in Lima (R4V, UNHCR)
- The Matos Mar barriada shares
- The COFOPRI "two million titles" and "45 days" claims
- The Muro de la vergüenza ruling and demolition: the TC PDF is at tc.gob.pe/jurisprudencia/2023/01606-2018-HC.pdf, which is blocked
- The El Niño Costero 2017 Lima figures
- The Rímac 80% share
- The simulacro 2026 figures
- The 2025 pre-census projection 10,432,133
- The exact 2025 census figure for Callao
- The 50-district count
- The 2017 shares 29.2% and 9,162,322

To check these, the session would need `censos2025.inei.gob.pe`, `tc.gob.pe`, `limacomovamos.org`, `es.wikipedia.org`, `www.uv.mx` and `www.lincolninst.edu`. It would also need `www.r4v.info` and `www.britannica.com` to stop answering HTTP 403.
