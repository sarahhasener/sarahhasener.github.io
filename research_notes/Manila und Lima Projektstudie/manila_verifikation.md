# Manila / Metro Manila: verification of key figures against source pages

Checked 2026-11-16 (status as of November 2026). This file checks the figures in `manila_entwicklung.md` and `manila_herausforderungen.md`. Those two files were not changed.

## Method and access log (read first)

- Every page was downloaded directly with curl through the session proxy, then searched for the exact figure. WebFetch could not resolve any of the hosts ("ENOTFOUND"), so it was not used.
- **CONFIRMED** = the figure or wording was found on the opened page. **CORRECTED** = the opened page shows a different value. **NOT VERIFIABLE** = the page was blocked, or the figure is not on the page.
- **[sek.]** = secondary source (Wikipedia). It is only acceptable as a secondary source, and the PSA original behind it could not be opened.

| Host | Result in this session |
|---|---|
| psa.gov.ph, www.psa.gov.ph, rssoncr.psa.gov.ph (HTML **and** PDF/XLSX files) | **HTTP 403, Cloudflare "Just a moment… Enable JavaScript and cookies" bot challenge** (`cf-mitigated: challenge`). This block comes from the PSA website, not from the session allowlist. One plain retry a few minutes later gave the same 403. **No PSA figure could be opened directly.** |
| www.britannica.com | HTTP 403 (bot challenge), also on retry |
| link.springer.com | "Client Challenge – JavaScript is disabled" page (HTTP 200/303, no content) |
| earthobservatory.nasa.gov | Reachable, but answers **301 → https://science.nasa.gov/earth/earth-observatory/the-growth-of-manila-86780**. science.nasa.gov is blocked by the proxy (CONNECT 403). |
| population.un.org | **Works.** WUP 2025 Excel files were downloaded. |
| en.wikipedia.org, api.crossref.org, doi.org, unhabitat.org, www.worldbank.org, pids.gov.ph, human-settlement.emergency.copernicus.eu | Work |
| documents1.worldbank.org, projects.worldbank.org, search.worldbank.org, blogs.worldbank.org | Proxy CONNECT 403 (not on the allowlist) |
| pna.gov.ph, inquirer.net, rappler.com, gmanetwork.com, businessmirror.com.ph, dhsprogram.com, nhess.copernicus.org, officialgazette.gov.ph, pco.gov.ph, jscimedcentral.com, www.un.org, hudcc.gov.ph, rssocar.psa.gov.ph, tandfonline.com, europepmc.org, api.openalex.org, api.semanticscholar.org | Blocked (proxy 403 or no connection) |

**Practical consequence:** every PSA figure below is at most "CONFIRMED [sek.]": the same number appears in a Wikipedia table that names PSA as its source. Before printing, open the PSA pages yourself in a normal browser. They load fine there; the challenge only stops automated access.

---

## Verification table

### A. Population: PSA 2024 POPCEN and 2020 CPH

| # | Claim (from notes) | Status | URL opened | Reference unit / year as stated on the page | Short quote from the page |
|---|---|---|---|---|---|
| A1 | NCR 2024 = 14,001,751 | **NOT VERIFIABLE on PSA** (Cloudflare 403). **CONFIRMED [sek.]** | PSA (blocked): https://psa.gov.ph/content/highlights-national-capital-region-ncr-population-2024-census-population-2024-popcen · opened: https://en.wikipedia.org/wiki/Metro_Manila | NCR "Region", 2024 census | "the region has a population of 14,001,751 as of 2024" |
| A2 | NCR = 12.4 % of national population (112,729,484) | **NOT VERIFIABLE** (PSA blocked). The national total is **CONFIRMED [sek.]**. The share was not found as a stated figure on any opened page. | https://en.wikipedia.org/wiki/2024_Philippine_census | Philippines, 1 July 2024 | "Proclamation No. 973 stated that the population of the Philippines as of July 1, 2024 was 112,729,484" |
| A3 | NCR growth 0.91 %/yr 2020–24 | **NOT VERIFIABLE on PSA**. **CONFIRMED [sek.]** | https://en.wikipedia.org/wiki/Metro_Manila (census table, "Source: Philippine Statistics Authority") | NCR, 2020→2024, % p.a. | "2020 13,484,462 +0.97% 2024 14,001,751 +0.91%" |
| A4 | City of Manila 2024 = 1,902,590 | **NOT VERIFIABLE on PSA** (no PSA table could be opened). **CONFIRMED [sek.]** on two Wikipedia pages. | https://en.wikipedia.org/wiki/Manila ; https://en.wikipedia.org/wiki/2024_Philippine_census | City of Manila, 2024 census | "According to the 2024 census, it has a population of 1,902,590 people." / table: "Manila \| National Capital Region \| 1,902,590 \| 1,846,513 \| +3.04%" |
| A5 | Calabarzon 2024 = 16.93 million, most populous region | **CONFIRMED [sek.]** (exact value 16,933,234) | https://en.wikipedia.org/wiki/Calabarzon ; https://en.wikipedia.org/wiki/2024_Philippine_census | Region IV-A, 2024 census | "Population (2024 census) … Total 16,933,234 • Rank 1st" / "Most populous region Calabarzon (16,933,234)" |
| A6 | Central Luzon 2024 = 12.99 million | **CONFIRMED [sek.]** (exact value 12,989,074) | https://en.wikipedia.org/wiki/Central_Luzon | Region III, 2024 census | "Population (2024 census) … Total 12,989,074" |
| A7 | Growth 2020–24: Central Luzon 1.08 %, Calabarzon 1.07 % | **CONFLICT, not resolvable.** Both Wikipedia tables give **+1.08 %** (Calabarzon too). The notes' 1.07 % for Calabarzon could not be checked against PSA. | https://en.wikipedia.org/wiki/Calabarzon ; https://en.wikipedia.org/wiki/Central_Luzon | Region, 2020→2024, % p.a. | Calabarzon: "2020 16,195,042 +2.48% 2024 16,933,234 +1.08%"; Central Luzon: "2020 12,422,172 +2.17% 2024 12,989,074 +1.08%" |
| A8 | NCR 2020 = 13,484,462 | **NOT VERIFIABLE on PSA**. **CONFIRMED [sek.]** | https://en.wikipedia.org/wiki/Metro_Manila | NCR, 2020 census | "2020 13,484,462 +0.97%" (the Manila article's infobox prints "Urban 13,484,482", a typo on Wikipedia) |
| A9 | City of Manila 2020 = 1,846,513 | **NOT VERIFIABLE on PSA**. **CONFIRMED [sek.]** | https://en.wikipedia.org/wiki/Manila | City of Manila, 2020 census | "2020 1,846,513 +0.77%" |
| A10 | NCR land area 619.54 km² (PSA 2020) | **NOT VERIFIABLE** (PSA blocked). Wikipedia gives **636.00 km²**, a different area basis. | https://en.wikipedia.org/wiki/Metro_Manila | NCR region area | "It encompasses an area of 636.00 km²" |
| A11 | City of Manila land area 24.98 km² (PSA) | **NOT VERIFIABLE** (PSA blocked). Wikipedia uses **42.34 km²**. | https://en.wikipedia.org/wiki/Manila | City of Manila, area in infobox | area value "42.34" (km²) |
| A12 | Densities 2020: CoM 73,920/km², NCR 21,765/km² (PSA) | **NOT VERIFIABLE** (PSA blocked). Wikipedia shows **other values on other area bases**: CoM 44,936/km² (2024 ÷ 42.34 km²) and NCR 22,015.3/km² (2024 ÷ 636 km²). NCR "urban density 21,764.3/km²" in the Manila infobox is close to the PSA value. | https://en.wikipedia.org/wiki/Manila ; https://en.wikipedia.org/wiki/Metro_Manila | 2024 population per stated area | "Density 44,936/km²" ; "Urban density 21,764.3/km²" ; "Density 22,015.3/km²" |

### B. Historical census series

| # | Claim | Status | URL opened | Unit / year | Quote |
|---|---|---|---|---|---|
| B1 | NCR 1970 3,966,695; 1980 5,925,884; 1990 7,948,392; 2000 9,932,560; 2010 11,855,975; 2015 12,877,253 (PSA RSET NCR, 6th ed.) | **NOT VERIFIABLE on PSA** (the RSET PDF on rssoncr.psa.gov.ph returned a Cloudflare 403). **All six values CONFIRMED [sek.]** | https://en.wikipedia.org/wiki/Metro_Manila ("Population census of Metro Manila", source: PSA) | NCR (today's boundary), census years | "1970 3,966,695 +4.88% 1975 4,970,006 … 1980 5,925,884 +3.58% … 1990 7,948,392 +2.98% … 2000 9,932,560 +1.06% … 2010 11,855,975 +0.90% 2015 12,877,253 +1.59%" |
| B2 | Same table, earlier years | **Additional [sek.] data** | same | "Metro Manila" (back-calculated to today's area) | "1903 328,939 … 1918 461,166 … 1939 993,889 … 1948 1,569,128 … 1960 2,462,488" |
| B3 | "Metro" 1903 330,345 / 1948 1,569,148 / 1960 2,462,288 (from *Timeline of Manila*) | **CONFIRMED [sek.]** on Timeline of Manila, **but CONFLICTS** with the Metro Manila census table (328,939 / 1,569,128 / 2,462,488). Recommendation: use the Metro Manila table (B2), or leave out the pre-1970 metro values. | https://en.wikipedia.org/wiki/Timeline_of_Manila | "metro", historical | "Population: 219,928 city; 330,345 metro." / "983,906 city; 1,569,148 metro." / "1,138,611 city; 2,462,288 metro." |
| B4 | City of Manila 1903 219,928; 1918 285,306; 1939 623,492; 1948 983,906; 1960 1,138,611; 1970 1,330,788; 1980 1,630,485; 1990 1,601,234 | **CONFIRMED [sek.]** (all values) | https://en.wikipedia.org/wiki/Manila ; https://en.wikipedia.org/wiki/Census_in_the_Philippines | City of Manila, census years | "1903 219,928 — 1918 285,306 +1.75% 1939 623,492 +3.79% 1948 983,906 +5.20% 1960 1,138,611 +1.22% 1970 1,330,788 +1.57% 1975 1,479,116 +2.14% 1980 1,630,485 +1.97% 1990 1,601,234 −0.18%" |
| B5 | City of Manila 2000 1,581,082; 2010 1,652,171; 2015 1,780,148 | **CONFIRMED [sek.]** | https://en.wikipedia.org/wiki/Manila | City of Manila | "2000 1,581,082 −0.97% … 2010 1,652,171 −0.19% 2015 1,780,148 +1.43%" |

### C. UN World Urbanization Prospects 2025

| # | Claim | Status | URL opened | Unit / year | Quote / data |
|---|---|---|---|---|---|
| C1 | Manila agglomeration 2025 ≈ 24.7 million, rank 8 | **CONFIRMED** (primary UN data file) | https://population.un.org/wup/assets/Download/Cities/WUP2025-F18-DEGURBA-100_Largest_Cities.xlsx (linked from https://population.un.org/wup/) | "City" as defined by the **Degree of Urbanisation** (1 km² grid + satellite data). Population in **thousands**, mid-year. | Row: "2025, Rank_Order 8, Philippines, Manila, Population 24735.305, Land_area_km2 2438". File title: "File 18: The 100 Largest Cities Ranked by Population Size (thousands) at Each Point in Time, 1975-2050" |
| C2 | 1975 ≈ 8.3 million, rank 12 | **CONFIRMED** | same file | same | "1975, rank 12, Manila, 8329.012, land area 1015 km²" |
| C3 | 2050 projection ≈ 27.1 million, rank 9 | **CONFIRMED** (projection) | same file | same | "2050, rank 9, Manila, 27119.826, land area 2669 km²" |
| C4 | (extra) Time series from the same file | CONFIRMED | same file (identical in F19) | thousands | 1990: 13,905 (rank 8) · 2000: 17,799 (7) · 2010: 21,072 (6) · 2020: 24,014 (7) · 2025: 24,735 (8) |

Note: the UN unit has a land area of **2,438 km² in 2025**, about 4× the NCR (619.5–636 km²). This matches the notes' statement that the new definition is much wider than the NCR.

### D. Economy and demography

| # | Claim | Status | URL opened | Unit / year | Quote |
|---|---|---|---|---|---|
| D1 | NCR = 31.2 % of national GDP 2024, ₱6.94 trillion, growth 5.6 % | **NOT VERIFIABLE on PSA** (rssoncr.psa.gov.ph release returned 403). The 31.2 % share is **CONFIRMED [sek.]**, but Wikipedia only cites BusinessWorld (23 Apr 2025), not PSA. ₱6.94 trillion was not found. | PSA (blocked): https://rssoncr.psa.gov.ph/content/ncrs-economy-increases-56-percent-2024 · opened: https://en.wikipedia.org/wiki/Metro_Manila | NCR share of Philippine GDP, 2024 | "The National Capital Region accounts for 31.2% of the gross domestic product of the Philippines in 2024." (ref: BusinessWorld, "NCR economic output jumped by 5.6% in 2024 — PSA") |
| D2 | Services 82.9 % / industry 17.1 % of NCR economy | **NOT VERIFIABLE** (PSA blocked; not on any opened page) | — | — | — |
| D3 | Newer data | **Note:** Wikipedia already cites a PSA "2023 to 2025 Gross Regional Domestic Product" publication (https://psa.gov.ph/system/files/pad/3_2025%20GRDP%20Publication-signed.pdf, blocked here), with NCR GDP of **US$152.250 billion (2025)**. For a poster dated November 2026, the 2025 GRDP share may be the more current figure. It was **not checked**. | https://en.wikipedia.org/wiki/Metro_Manila | NCR, 2025 | "GDP total US$152.250 billion (2025)" |
| D4 | World Bank: Metro Manila contributes a large share of national output | **CONFIRMED** (different wording and value) | https://www.worldbank.org/en/country/philippines/brief/project-highlights-metro-manila-flood-management (dated September 29, 2017) | Metro Manila, approx. 2017 | "Metro Manila is home to around 15 million people and contributes about 35 percent to the Philippine economy." |
| D5 | NCR TFR = 1.2 (2022 NDHS) | **NOT VERIFIABLE** (dhsprogram.com blocked by the proxy; PSA blocked). The Wikipedia "Demographics of the Philippines" page has regional TFR only for 2013. | https://en.wikipedia.org/wiki/Demographics_of_the_Philippines (no 2022 regional value) | — | — |
| D6 | 2018 National Migration Survey (NCR 388,000 interregional in-migrants, etc.) | **NOT VERIFIABLE** (rssocar.psa.gov.ph blocked; PIDS DP 2023-20 not attempted) | — | — | — |

### E. Informal settler families (ISF)

| # | Claim | Status | URL opened | Unit / year | Quote |
|---|---|---|---|---|---|
| E1 | 596,308 ISF in NCR on 3,447.93 ha (DHSUD via PIDS) | **NOT VERIFIABLE.** The PIDS page is only a link record ("PIDS in the News") for a BusinessMirror article by Cai U. Ordinario, dated **Sep 08, 2024**. The figure is **not** on the PIDS page. The BusinessMirror article (businessmirror.com.ph) is blocked by the proxy. | https://pids.gov.ph/details/news/in-the-news/phl-has-largest-slum-area-in-the-world | — | "PHL has largest slum area in the world? BusinessMirror Cai U. Ordinario … Date Published Sep 08, 2024" |
| E2 | NHA 2011: 584,425 families; 104,219 ISF in danger zones (HUDCC 2014) | **NOT VERIFIABLE** (hudcc.gov.ph and events.development.asia blocked) | — | — | — |
| E3 | UN-Habitat 2023: 3.7 million ISF nationally, "half a million" in slums and high-risk areas in Metro Manila | **CONFIRMED** | https://unhabitat.org/sites/default/files/2023/06/5._un-habitat_philippines_country_report_2023_final_compressed.pdf (UN-Habitat Philippines Country Report, PDF created May 2023) | Families; Philippines / Metro Manila (NCR); no reference year given (report 2023) | "Informal settler families (ISFs) are estimated at 3.7 million, half a million of which are living in slums and high-risk areas in Metro Manila or National Capital Region." |
| E4 | (same report, extra) | CONFIRMED | same | Philippines | "Housing needs is projected to increase from 6.5 million housing backlog in 2022 to 22 million by 2040." |

Note on E3: the earlier note called the BusinessWorld version "seems high, check before using". The UN-Habitat original does say exactly 3.7 million ISF nationally, of which half a million are in Metro Manila slums or high-risk areas. So the figure can be cited directly from UN-Habitat. The report does not name the underlying data year or source.

### F. Historical dates

| # | Claim | Status | URL opened | Quote |
|---|---|---|---|---|
| F1 | 24 June 1571: Legazpi declares Manila capital | **CONFIRMED [sek.]** (Britannica blocked) | https://en.wikipedia.org/wiki/Intramuros | "Legazpi declared the area of Manila as the new capital of the Spanish colony on June 24, 1571" |
| F2 | Burnham Plan 1905; ~225,000 inhabitants; designed for 800,000 | **CONFIRMED [sek.]** | https://en.wikipedia.org/wiki/Burnham_Plan_of_Manila | "In 1905, Manila had a population of about 225,000. Burnham planned for a much-expanded city of 800,000." Report "Created June 28, 1905", "Commissioned by William Howard Taft" |
| F3 | Battle of Manila 3 Feb – 3 Mar 1945, ~100,000 civilian deaths | **CONFIRMED [sek.]** (Britannica blocked). The page says **"at least 100,000"**. | https://en.wikipedia.org/wiki/Battle_of_Manila_(1945) | "3 February – 3 March 1945" ; "resulted in the death of at least 100,000 civilians and the complete devastation of the city" ; infobox "Civilians: 100,000+ killed, 250,000 total casualties" ; "only the San Agustin Church seen standing" (Intramuros, May 1945); US forces "1,010 dead and 5,565 wounded"; "16,665 Japanese military dead" |
| F4 | PD 824 of 7 Nov 1975 creates Metro Manila | **CONFIRMED [sek.]** (Official Gazette blocked) | https://en.wikipedia.org/wiki/Metro_Manila | "On November 7, 1975, Metro Manila was formally established through Presidential Decree No. 824" |

### G. Subsidence literature (DOI checks)

| # | Claim | Status | URL opened | Result |
|---|---|---|---|---|
| G1 | Eco et al. 2020, *JSM Environmental Science & Ecology* 8(1):1068, DOI 10.47739/2333-7141/1068 | **NOT VERIFIABLE: the DOI does not resolve.** Crossref has no record (HTTP 404). The doi.org handle API returns "responseCode 100" (handle not found). doi.org itself returns 404. A Crossref bibliographic search (title + Eco/Rodolfo/Lagmay) found no matching record. The publisher site jscimedcentral.com is blocked. **Do not print this DOI.** Cite with the URL of the publisher PDF only, and note that the journal is not Crossref-registered. The subsidence rates (2.5 / 4.2 cm/yr) remain unverified. | https://api.crossref.org/works/10.47739/2333-7141/1068 ; https://doi.org/api/handles/10.47739/2333-7141/1068 | `{"responseCode":100,"handle":"10.47739/2333-7141/1068"}` |
| G2 | *Natural Hazards* DOI 10.1007/s11069-022-05509-2, authors/title "not verified" | **CONFIRMED metadata** (Crossref). **Rates (1–2 cm/yr in Manila/CAMANAVA, >4 cm/yr in neighbouring provinces, Raucoules 15 cm/yr): NOT VERIFIABLE.** Springer showed a JavaScript challenge, and Crossref has no abstract for this record. | https://api.crossref.org/works/10.1007/s11069-022-05509-2 | Title: "Sentinel-1 Interferometric Synthetic Aperture Radar (InSAR) reveals continued ground deformation in and around Metro Manila, Philippines, associated with groundwater exploitation". Authors: Karl Wyatt Espiritu, Christian James Reyes, Theresa Marie Benitez, Reina Clarise Tokita, Lear Joseph Galvez, Ryan Ramirez. *Natural Hazards* **114**(3): 3139–3161, published online 2022-08-06. This **is** the same paper as the ResearchGate entry listed separately in the notes (§3), so the "possibly identical" question is resolved: identical. |
| G3 | Rodolfo & Siringan 2006, *Disasters* 30:118–139 | **CONFIRMED** | https://api.crossref.org/works/10.1111/j.1467-9523.2006.00310.x | Title: "Global sea‐level rise is recognised, but flooding from anthropogenic land subsidence is ignored around northern Manila Bay, Philippines". Kelvin S. Rodolfo, Fernando P. Siringan. *Disasters* **30**(1): 118–139, March 2006. Abstract: "excessive groundwater extraction is lowering the land surface by several centimetres to more than a decimetre per year" ; global sea-level rise "of one to three millimetres per year"; "Even if groundwater use is greatly reduced … natural deltaic subsidence and global sea‐level rise will continue to aggravate flooding, although at substantially lower rates." |

### H. Flood management, storms, reclamation, imagery

| # | Claim | Status | URL opened | Unit / year | Quote |
|---|---|---|---|---|---|
| H1 | World Bank Metro Manila Flood Management Project: 36 pumping stations modernized + 20 new | **CONFIRMED** | https://www.worldbank.org/en/country/philippines/brief/project-highlights-metro-manila-flood-management (dated September 29, 2017) | Project, 2017 | "Under the Metro Manila Flood Management Project, 36 existing pumping stations will be modernized, 20 new ones will be constructed, and supporting infrastructure along critical waterways will be improved in the cities of Manila, Pasay, Taguig, Makati, Malabon, Mandaluyong, San Juan, Pasig, Valenzuela, Quezon City, and Caloocan." |
| H2 | Project supports ISF resettlement from waterways | **CONFIRMED** | same | — | "It will also support government's resettlement of informal settlers that have encroached on the waterways." |
| H3 | Total US$500 million (with AIIB), WB US$207.6 million, approved Sept 2017 | **NOT VERIFIABLE.** The amounts are **not** on the highlights page. That page links to the press release "Philippines: WB, AIIB Approve Funding for Flood Management in Metro Manila" (https://www.worldbank.org/en/news/press-release/2017/09/28/philippines-wb-aiib-approve-funding-for-flood-management-in-metro-manila), which returned **HTTP 404**. projects.worldbank.org and documents1.worldbank.org are blocked. Only the date (Sept 2017) and the AIIB involvement are confirmed, via the title of the linked press release. | — | Highlights page: "Slated to start this year, the project is scheduled to be completed in 2024." (original schedule) |
| H4 | Ondoy 2009 (Ketsana): Marikina River 21.5 m record | **CONFIRMED [sek.]** (Inquirer blocked) | https://en.wikipedia.org/wiki/Marikina_River | m water level | "… exceeded the limit of 20 meters compared to Typhoon Ketsana of 21.5 meters (70.5 ft) according to Marikina Disaster Risk Reduction and Management Office." |
| H5 | Ondoy rainfall 455 mm / 24 h | **CONFIRMED [sek.]** (Rappler blocked) | https://en.wikipedia.org/wiki/Tropical_Storm_Ketsana | 24 h, 26–27 Sept 2009 (PAGASA) | "PAGASA documented a record-high amount of rainfall in 24 hours at 455 millimetres … from 8 am … September 26 to 8 am … September 27" ; six-hour value "341.3 millimetres" |
| H6 | Ondoy deaths "more than 700" | **CORRECTED / unclear** (the Inquirer original is blocked). Wikipedia gives **464 deaths in Metro Manila** and **921 direct deaths overall** (all countries). Marikina: 78. | https://en.wikipedia.org/wiki/Tropical_Storm_Ketsana ; https://en.wikipedia.org/wiki/Marikina_River | Deaths | "At least 464 deaths" (Metro Manila) ; infobox "Fatalities 921 direct" ; "Marikina itself recorded 78 deaths" |
| H7 | Carina/Gaemi 24 July 2024: 3rd alarm at 18 m, peak 20.7 m | **CONFIRMED [sek.]**, with nuance: the 3rd alarm was raised when the river reached **18.4 m**. Peak 20.7 m per the Typhoon Gaemi article; the Marikina River article gives 20.6 m at 14:03 PHT. The notes' "20.7 m at 16:40 (Marikina PIO)" could not be checked (Inquirer blocked). | https://en.wikipedia.org/wiki/Typhoon_Gaemi ; https://en.wikipedia.org/wiki/Marikina_River | m, 24 July 2024 | "On July 24, the third and highest alarm was raised on the Marikina River after it rose to 18.4 m (60 ft) before peaking at 20.7 m (68 ft)" |
| H8 | Carina-enhanced monsoon 217 mm / 24 h | **NOT VERIFIABLE** (Rappler blocked; the figure is not in the Wikipedia articles) | — | — | — |
| H9 | Manila Bay reclamation suspension, Aug 2023 (Marcos/DENR) | **NOT VERIFIABLE** (Inquirer, GMA, PCO, Rappler and PNA blocked; Wikipedia "Manila Bay" and "Land reclamation in Metro Manila" have no text on the 2023 suspension) | https://en.wikipedia.org/wiki/Manila_Bay ; https://en.wikipedia.org/wiki/Land_reclamation_in_Metro_Manila | — | — |
| H10 | NASA Earth Observatory "The Growth of Manila" (1988/2014) URL | **URL CONFIRMED (redirect), content NOT VERIFIABLE.** The old EO URL redirects (HTTP 301) to the science.nasa.gov URL already cited in the notes. science.nasa.gov is blocked by the proxy, so the image dates, the 1,800→2,300 km² statement and the credits could not be checked. | https://earthobservatory.nasa.gov/images/86780/the-growth-of-manila → 301 → https://science.nasa.gov/earth/earth-observatory/the-growth-of-manila-86780 | — | — |
| H11 | GHSL / GHS-WUP 2025 page | **CONFIRMED** (page exists and describes the dataset) | https://human-settlement.emergency.copernicus.eu/ghs_wup2025.php | 1950–2100 | "Global projections of population by Degree of Urbanisation and for each city for the UN World Urbanization Prospects" ; "From 1975 to 2020, it is based on the Global Human Settlement Layer (GHSL)" |
| H12 | Greater Manila Area ≈ 26.7 million (2020) | **CONFIRMED [sek.]** | https://en.wikipedia.org/wiki/Greater_Manila_Area | NCR + Bulacan, Cavite, Laguna, Rizal; 2020 census | "As of the 2020 Census, the combined population of Metro Manila, Bulacan, Cavite, Laguna, and Rizal was approximately 26.7 million." |

---

## Short notes

1. **Safe to print with a primary source:**
   - UN WUP 2025: Manila 24,735,305 (2025, rank 8), 8,329,012 (1975, rank 12), 27,119,826 (2050, rank 9). Unit: Degree-of-Urbanisation "city", 2,438 km² in 2025.
   - UN-Habitat 2023: 3.7 million ISF nationally, half a million in Metro Manila.
   - World Bank: 36 modernized + 20 new pumping stations, ISF resettlement, "about 35 percent" of the economy.
   - Rodolfo & Siringan 2006 bibliographic data.
   - Bibliographic data of the *Natural Hazards* paper (Espiritu et al. 2022).
2. **PSA figures:** none could be opened, because PSA is behind a Cloudflare bot challenge, not the allowlist. All population counts in the notes (NCR 2024/2020, CoM 2024/2020, the NCR series 1970–2015, Calabarzon, Central Luzon, national total) match Wikipedia tables that cite PSA. They are very likely correct, but they count only as [sek.] until someone opens PSA in a browser.
   - These PSA-only values could not be confirmed anywhere: the 12.4 % share, the areas 619.54 / 24.98 km², the densities 73,920 / 21,765 per km², GRDP ₱6.94 trillion, and the services share of 82.9 %.
3. **Corrections and conflicts found:**
   - (a) The Eco et al. 2020 DOI 10.47739/2333-7141/1068 **does not resolve** (not registered with Crossref or the Handle system).
   - (b) Ondoy deaths: the notes say "> 700"; Wikipedia says 464 in Metro Manila and 921 overall.
   - (c) Carina third alarm: raised at 18.4 m. 18 m is the alarm threshold; 18.4 m is the level actually reached when the alarm was raised.
   - (d) Pre-1970 "metro" values differ between two Wikipedia pages (330,345 vs 328,939 for 1903, and so on).
   - (e) Calabarzon growth 2020–24: Wikipedia gives 1.08 %; the notes say 1.07 %.
   - (f) Area and density: Wikipedia uses 636.00 km² (NCR) and 42.34 km² (CoM), which give different densities from PSA's 619.54 / 24.98 km². Never mix these bases.
4. **Could not be checked (blocked hosts):** NCR TFR 1.2 (2022 NDHS); 2018 NMS migration figures; PIDS/DHSUD 596,308 ISF (the PIDS page only links to a BusinessMirror article from 8 Sep 2024); NHA 584,425 and 104,219; US$500M / US$207.6M project amounts; Carina rainfall 217 mm; Manila Bay reclamation suspension of Aug 2023; content of the NASA image page; subsidence rates in the *Natural Hazards* paper and in Eco et al.
5. **Possibly newer data:** Wikipedia already cites a PSA "2023 to 2025 GRDP" publication (NCR US$152.25 billion in 2025). For a poster dated November 2026, check whether the NCR share for 2025 differs from 31.2 % (2024).
