# Geodaten: Verwaltungsgrenzen Metro Manila (NCR) für die Poster-Karte

## Welche frei lizenzierte Quelle liefert die Polygone der 17 NCR-LGUs, und unter welcher Lizenz?

### Takeaway
Die verwendeten Daten stammen aus **geoBoundaries gbOpen PHL ADM3** (Build vom 12.12.2023). geoBoundaries hat sie unverändert von den **OCHA-COD-AB-Grenzen der Philippinen auf HDX** übernommen (Quelle: NAMRIA/PSA). Lizenz: **CC BY 3.0 IGO**. Das erlaubt die Nutzung auf einem Schulposter, solange die Quelle genannt wird. GADM wurde nicht verwendet.

### Cited Findings
- Die geoBoundaries-API für PHL ADM3 (gbOpen) nennt: boundaryID `PHL-ADM3-30758251`, boundaryYearRepresented 2020, boundaryCanonical "Municipalities", boundarySource "National Mapping and Resource Information Authority (NAMRIA), Philippines Statistics Authority (PSA), OCHA Philippines", **boundaryLicense "Creative Commons Attribution 3.0 Intergovernmental Organisations (CC BY 3.0 IGO)"**, licenseSource/boundarySourceURL `data.humdata.org/dataset/philippines-administrative-levels-0-to-3`, sourceDataUpdateDate "Thu Jan 19 07:31:04 2023", buildDate "Dec 12, 2023", admUnitCount 1647 — [geoBoundaries API PHL ADM3](https://www.geoboundaries.org/api/current/gbOpen/PHL/ADM3/); dieselben Angaben stehen in der Metadaten-Datei des Releases — [geoBoundaries-PHL-ADM3-metaData.json (Commit 9469f09)](https://media.githubusercontent.com/media/wmgeolab/geoBoundaries/9469f09/releaseData/gbOpen/PHL/ADM3/geoBoundaries-PHL-ADM3-metaData.json)
- PHL ADM2 (Provinzen, für die Zuordnung verwendet): boundaryID `PHL-ADM2-2640588`, Lizenz ebenfalls CC BY 3.0 IGO, Quelle NAMRIA/PSA/OCHA, buildDate "Jul 05, 2023", 87 Einheiten — [geoBoundaries API PHL ADM2](https://www.geoboundaries.org/api/current/gbOpen/PHL/ADM2/)
- Laut geoBoundaries selbst ist das Projekt eine Ressource mit offener Lizenz ("CC BY 4.0 / ODbL"), und „the only requirement for use is acknowledgement“ — [geoBoundaries README](https://raw.githubusercontent.com/wmgeolab/geoBoundaries/main/README.md). Die Startseite schreibt: „Our license requires an acknowledgement in any products you produce which use this data“, und empfiehlt als Zitat Runfola, D. et al. (2020) *geoBoundaries: A global database of political administrative boundaries*. PLoS ONE 15(4): e0231866, https://doi.org/10.1371/journal.pone.0231866 — [geoboundaries.org](https://www.geoboundaries.org/). Für PHL gilt aber die Lizenz pro Datensatz in den Metadaten, also CC BY 3.0 IGO. Diese wird weiterverwendet, weil es die Lizenz der Ursprungsdaten ist.
- Der aktuelle HDX-Datensatz `cod-ab-phl` („Philippines - Subnational Administrative Boundaries“): license_id `cc-by-igo`, license_title „Creative Commons Attribution for Intergovernmental Organisations (CC BY-IGO)“, license_url http://creativecommons.org/licenses/by/3.0/igo/legalcode, dataset_source „National Mapping and Resource Information Authority (NAMRIA), Philippines Statistics Authority (PSA)“, Organisation OCHA Field Information Services Section (FISS), Hinweis „Prepared by OCHA“. Version 03 mit 1642 Admin-3-Einheiten. Daten: Grenzen von der Quelle erstellt am 09.02.2018, „valid for use by the humanitarian community“ seit 26.03.2018, auf Genauigkeit geprüft am 01.04.2024. Ressourcen zuletzt aktualisiert am 28.05.2026 — [HDX CKAN API cod-ab-phl](https://data.humdata.org/api/3/action/package_show?id=cod-ab-phl) / [HDX-Seite](https://data.humdata.org/dataset/cod-ab-phl)
- Die alte HDX-ID `philippines-administrative-levels-0-to-3`, auf die geoBoundaries verweist, liefert über die CKAN-API „Not found“. Der Datensatz läuft heute unter `cod-ab-phl` — [HDX CKAN API (alte ID)](https://data.humdata.org/api/3/action/package_show?id=philippines-administrative-levels-0-to-3)

### Inferences
- geoBoundaries verarbeitet HDX/COD-AB-Daten, deshalb sind die Geometrien praktisch dieselben wie bei OCHA. Den HDX-Datensatz selbst (Version 03, Shapefile/GeoJSON-Zip) habe ich nicht heruntergeladen. Ein Abgleich mit geoBoundaries war wegen derselben Herkunft nicht nötig.
- CC BY 3.0 IGO verlangt eine Quellenangabe. Ein Schulposter ist abgedeckt. Die Vereinfachung (Generalisierung) und das Zusammenfassen von Manilas Stadtbezirken sind Bearbeitungen und sollten als „bearbeitet/vereinfacht“ gekennzeichnet werden.

**Empfohlener Attributionstext für das Poster:**
> Grenzen: NAMRIA / PSA, bereitgestellt von OCHA (HDX COD-AB) über geoBoundaries (Runfola et al. 2020), Lizenz CC BY 3.0 IGO; vereinfacht und zusammengefasst.

Englische Kurzfassung: „Boundaries: NAMRIA/PSA via OCHA HDX & geoBoundaries (CC BY 3.0 IGO), simplified.“

### Gaps
- Die HTML-Startseite von www.geoboundaries.org ließ sich per curl laden, per WebFetch nicht (DNS). Die Lizenzangaben stammen aus der API, der Metadaten-JSON und der per curl geladenen Startseite.

## Was enthalten die erzeugten Dateien und wie wurden sie verarbeitet?

### Takeaway
`geodata/ncr_lgus.geojson` (190 KB) enthält genau die 17 NCR-LGUs mit sauberer Eigenschaft `name`. `geodata/context_provinces.geojson` (473 KB) enthält Bulacan, Rizal, Cavite und Laguna. Beide Dateien kommen aus derselben Topologie und haben deshalb deckungsgleiche gemeinsame Grenzen. Alle Geometrien sind gültig. Es wurde keine Geometrie erfunden.

### Cited Findings
- Quelldatei: `geoBoundaries-PHL-ADM3.topojson` in voller Auflösung (100.345.244 Bytes, SHA-256 `751065b1…7707`), heruntergeladen von [media.githubusercontent.com … 9469f09/…/PHL/ADM3/geoBoundaries-PHL-ADM3.topojson](https://media.githubusercontent.com/media/wmgeolab/geoBoundaries/9469f09/releaseData/gbOpen/PHL/ADM3/geoBoundaries-PHL-ADM3.topojson). Die Datei hat eine Layer-Ebene `PHLADM3gbOpen` mit 1.647 Polygonen und den Attributen shapeName, shapeISO (leer), shapeID, shapeGroup, shapeType. Einen Provinz- oder PSGC-Code gibt es nicht. github.com/…/raw/ war in der Session gesperrt, raw.githubusercontent.com liefert nur Git-LFS-Pointer, media.githubusercontent.com funktioniert.
- Hilfsdateien: die vereinfachten Dateien `geoBoundaries-PHL-ADM3_simplified.geojson` (7,07 MB) und `geoBoundaries-PHL-ADM2_simplified.geojson` (3,14 MB). Daraus wurde jeder ADM3-Einheit über einen Repräsentativpunkt eine Provinz zugeordnet, ohne Fehlzuordnung. Ergebnis: 30 Einheiten in den vier ADM2-Einheiten „NCR, City of Manila, First District“, „NCR, Second District“, „NCR, Third District“, „NCR, Fourth District“; dazu Bulacan 24, Cavite 23, Laguna 30, Rizal 14 — [geoBoundaries API ADM2](https://www.geoboundaries.org/api/current/gbOpen/PHL/ADM2/)
- Namensfeld `shapeName`. Die Quellnamen der NCR-Städte sind: „Caloocan City“, „City of Las Piñas“, „City of Makati“, „City of Malabon“, „City of Mandaluyong“, „City of Marikina“, „City of Muntinlupa“, „City of Navotas“, „City of Parañaque“, „Pasay City“, „City of Pasig“, „Pateros“, „Quezon City“, „City of San Juan“, „Taguig City“, „City of Valenzuela“. Die Schreibweisen sind korrekt mit ñ (UTF-8), nicht „Kalookan“. **Manila liegt in der Quelle nicht als eine Einheit vor, sondern als 14 Bezirke**: Binondo, Ermita, Intramuros, Malate, Paco, Pandacan, Port Area, Quiapo, Sampaloc, San Miguel, San Nicolas, Santa Ana, Santa Cruz, „Tondo I / II“. Ich habe sie zu „Manila“ zusammengefasst (dissolve). Namen wie San Juan, Quezon, San Miguel, Santa Cruz und Sampaloc kommen landesweit mehrfach vor. Deshalb wurde räumlich gefiltert (Zugehörigkeit zu einer NCR-ADM2-Einheit) und nicht nur nach Namen — [geoBoundaries PHL ADM3](https://www.geoboundaries.org/api/current/gbOpen/PHL/ADM3/)
- Verarbeitung mit mapshaper 0.6.102: Join der Provinzzuordnung, Filter auf NCR und die 4 Provinzen, Umbenennung, `-simplify 10% weighted keep-shapes` (18 Selbstüberschneidungen automatisch repariert), `-dissolve fields=name`, Ausgabe mit 5 Nachkommastellen (ca. 1 m).
- Ergebnisprüfung (shapely 2.2.0): 17 Features, Namensmenge stimmt genau, alle `is_valid = True`. Eigenschaften je Feature: `name`, `district` (First/Second/Third/Fourth District), `type` (`city`; Pateros = `municipality`). Ungefähre Flächen aus der Geometrie (lokal skaliert): Quezon City 162,3 km², Caloocan 53,2 (2 Teile, Nord und Süd), Valenzuela 46,5, Parañaque 44,8, Manila 41,9, Muntinlupa 39,1, Taguig 35,6, Las Piñas 32,7, Pasig 31,3, Makati 24,9, Marikina 22,9, Pasay 17,9, Malabon 15,8, Mandaluyong 11,3, Navotas 10,5, San Juan 5,8, Pateros 1,6. NCR gesamt ca. 598 km². Diese Flächen sind nur zur Plausibilitätsprüfung berechnet und keine amtlichen Werte.
- Kontext-Provinzen: Laguna (MultiPolygon, 4 Löcher), Bulacan (1 Loch), Cavite, Rizal (inklusive Talim Island). Jeweils `name` und `type: "province"`.

### Inferences
- Die NCR-Gesamtfläche der Geometrie (ca. 598 km²) ist plausibel, aber nicht amtlich. Für Flächenangaben auf dem Poster sollten amtliche PSA-Werte genommen werden, nicht die Geometrie.
- Die 10-%-Vereinfachung hat 126 bis 1.142 Stützpunkte pro LGU. Das reicht für einen großformatigen Druck. Eine stärker vereinfachte 3-%-Version (72 KB) wurde getestet und lag im Scratchpad, wurde aber nicht übernommen.

### Gaps
- PSGC-Codes fehlen, weil geoBoundaries sie nicht mitliefert. Bei Bedarf wären sie aus HDX `cod-ab-phl` (Attribut ADM3_PCODE) zu holen.

## Gewässer-Kontext: Manila Bay, Laguna de Bay, Pasig River

### Takeaway
Manila Bay und Laguna de Bay ergeben sich als **Lücken (Negativraum)** zwischen den Polygonen der NCR und der Kontext-Provinzen. Wenn man den Kartenhintergrund wasserblau färbt, erscheinen beide korrekt. Zusätzlich hat Natural Earth (public domain) ein gröberes Polygon „Laguna de Bay“. Für den **Pasig River** wurde keine freie, abrufbare Liniengeometrie gefunden.

### Cited Findings
- Punkttests: Laguna de Bay (121,25/14,38 und 121,12/14,40) und Manila Bay (120,85/14,55) liegen in keinem Polygon. Die Seen- und Buchtflächen sind also nicht Teil der ADM-Polygone. Sichtprüfung im Preview `geodata/preview_ncr_lgus.png` — abgeleitet aus [geoBoundaries PHL ADM3](https://www.geoboundaries.org/api/current/gbOpen/PHL/ADM3/)
- Natural Earth `ne_10m_lakes` enthält „Laguna de Bay“ (scalerank 8) und „Lake Taal“. `ne_10m_rivers_lake_centerlines` hat im Ausschnitt 120,7–121,6 °E / 14,0–15,0 °N **keinen** Fluss, also auch nicht den Pasig — [Natural Earth GeoJSON (nvkelso/natural-earth-vector)](https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_10m_lakes.geojson). Diese Dateien wurden nur geprüft und nicht ins Projekt übernommen.
- OpenStreetMap (ODbL) über die Overpass API wäre die naheliegende Quelle für den Pasig River. overpass-api.de wird vom Session-Proxy aber abgelehnt (403 connect_rejected).

### Inferences
- **Kartenausschnitt-Empfehlung:** In etwa 120,88–121,20 °E und 14,33–14,80 °N ist jede Fläche, die nicht von einem Polygon bedeckt ist, tatsächlich Wasser (Manila Bay im Westen, Laguna de Bay im Südosten). Außerhalb davon, z. B. östlich von Rizal (Provinz Quezon) oder nordwestlich von Bulacan (Pampanga), fehlen Nachbarprovinzen. Ein blauer Hintergrund würde dort fälschlich als Meer erscheinen.
- Der Pasig River verläuft teilweise entlang von LGU-Grenzen (Makati–Mandaluyong, Pasig–Taguig/Pateros) und durch Manila. Er kann aus den vorhandenen Daten nicht vollständig und sauber abgeleitet werden. Er sollte also nicht von Hand gezeichnet werden, oder nur als klar gekennzeichnete schematische Signatur.

### Gaps
- Keine freie Pasig-River-Geometrie im Projekt. Mögliche Lösung: OSM-Export (ODbL, Attribution „© OpenStreetMap contributors“), wenn overpass-api.de oder download.geofabrik.de in der Session freigegeben werden.

## Bekannte inhaltliche Einschränkung: Grenzstreit Makati–Taguig (Fort Bonifacio / EMBO)

### Takeaway
Die NAMRIA/PSA-Grenzen (Stand 2018) zeigen das umstrittene Gebiet Fort Bonifacio/BGC noch bei **Makati**. Der Oberste Gerichtshof (G.R. No. 235316) hat Fort Bonifacio einschließlich der EMBO-Barangays aber **Taguig** zugesprochen. Die Karte zeigt also den Stand vor dem Urteil und braucht einen Hinweis.

### Cited Findings
- Punkttest in `ncr_lgus.geojson`: ungefähre Koordinaten von BGC High Street (121,0509/14,5507), Pembo (121,0590/14,5470) und Comembo (121,0640/14,5510) liegen im Polygon **Makati**. Die Koordinaten habe ich selbst angenähert, sie sind nicht amtlich. Makati ist in der Geometrie ca. 24,9 km² groß, Taguig ca. 35,6 km².
- Philstar berichtete am 04.04.2023 unter dem Titel „It’s final: Taguig has jurisdiction over BGC“ — [Philstar](https://www.philstar.com/headlines/2023/04/04/2256709/its-final-taguig-has-jurisdiction-over-bgc); BusinessMirror am 31.05.2023 „Supreme Court rules Taguig City owns Fort Bonifacio“ — [BusinessMirror](https://businessmirror.com.ph/2023/05/31/supreme-court-rules-taguig-city-owns-fort-bonifacio/). Laut einer Fallzusammenfassung heißt das Verfahren Municipality of Makati v. Municipality of Taguig — [jur.ph](https://jur.ph/jurisprudence/digest/municipality-of-makati-v-municipality-of-taguig)

### Inferences
- Empfehlung für das Poster: eine Fußnote wie „Grenzen Stand NAMRIA/PSA 2018; das Gebiet Fort Bonifacio/BGC einschließlich der EMBO-Barangays gehört laut Urteil des Supreme Court (G.R. No. 235316, rechtskräftig 2023) zu Taguig.“ Die Geometrie selbst habe ich nicht verändert, weil keine freie Polygonquelle für die neue Grenze vorlag.

### Gaps
- Das genaue Datum der Rechtskraft war in den Suchergebnissen widersprüchlich (Angaben 2022 und 2023). Wikipedia und andere Seiten waren in der Session nicht erreichbar. Vor dem Druck sollte das Datum an einer primären Quelle (Supreme Court) geprüft werden.
- Ob die HDX-Version 03 (geprüft im April 2024) die neue Grenze enthält, ist ungeprüft. Die Grenzen selbst sind laut HDX auf den 09.02.2018 datiert, eine Übernahme ist also unwahrscheinlich.
