# A specific archival route for the missing island photographs

2026-10-09 (America/New_York). Sourced draft, not independently reviewed.

The negative1950 digital-inventory search does not exhaust archival holdings. NARA's Special List25 contains a Washington entry written **Willpa Bay**, filed under RG23 Project Completion Reports. This is a more specific retrieval lead than the general analog-film transfer notice. It does not authenticate the missing50-O-1613 photograph or its annotated enlargement.

## Original finding-aid rows

S268 is the unchanged [federal workbook](../sources/originals/cascadia/Special-List-25-United-States.xlsx), downloaded through the link on NARA's [domestic aerial-photography guide](https://www.archives.gov/research/cartographic/aerial-photography/domestic-photography). The Washington header and all546rows were read. These four target-area entries are preserved in the [ledger](../data/willapa-nara-finding-aid.json); the [read-only script](../analysis/willapa_nara_finding_aid.py) reproduces the selection and checks the original file hash. No workbook was edited, recalculated or visually rendered. The rows contain literal values rather than formulas. Other-state holdings were not audited.

| Washington locator | Area as written | Symbol / year as written | RG | Filed under / other locator |
| --- | --- | --- | --- | --- |
| A340:J340 | Pacific | NONE / ****P |373 |46N/123 to124W; index typeLI; scaleVARIES |
| A341:J341 | Pacific | DGM /1949P |114 |Brooklyn Area; T153991055; PI-L;1:20,000 |
| A342:J342 | Pacific | DOQ /1951P |114 |T153991060; PI-L;1:20,000 |
| A530:J530 | Willpa Bay | blank / blank |23 |Project Completion Reports; remaining locator fields blank |

The spelling **Willpa** is retained. Reading it as Willapa is a retrieval hypothesis, not a silent correction. The county entries do not establish island coverage. The suffixP, asterisks and index codes remain uninterpreted here.1949/1951 entries are candidate alternate observations, not substitutes for the named1950frame.

## The series and report numbers can now be named

S269, NARA's [RG23 aerial-photography guide](https://www.archives.gov/research/cartographic/aerial-photography/rg-23-uscgs-aerial-photography-sl25), describes Project Completion Reports,1957–1964, and says the series' aerial prints are filed with reports104and106. Its linked [catalog record305404](https://catalog.archives.gov/id/305404) is therefore a series-level retrieval target. The guide also distinguishes Geodetic Survey Control Prints and Indexes,1940–1959, from other RG23 photography. A series date span is not an exposure date: its example includes a1950print.

The guide's [Report104 example](https://www.archives.gov/files/research/cartographic/aerial-photography/rg23-305404-report104-cape-1950-01.jpg) was downloaded and visually inspected. It shows two mounted aerial images labeled CAPE,1950, on page9. Neither frame1613 nor the island is authenticated in that example. The linked example inventory screenshot shows other areas and does not display the Washington target row. They are examples of archival arrangement, not new island observations. Their download hashes and inspection limits are recorded in the [retrieval ledger](../data/willapa-nara-route-acquisition.json).

The catalog URL returned a JavaScript application shell, not inspectable series/item metadata. In-app browser access was unavailable for this check. No catalog contents beyond the guide's identified title/link are claimed. The Tacoma1966item was retried through normal TLS and again failed certificate validation; its image and reverse remain uninspected. No certificate override was used.

## What to retrieve and what it would test

The next specific archive targets are RG23/series305404/reports104and106, using both Willpa and Willapa spellings. Determine which report, if either, contains the named roll50-O, exposure1613, July11,1950, northern Long Beach Peninsula image. Locate the annotated1:10000 enlargement and June1953field sheet separately. Report numbers alone do not establish a frame match, an accession for the2022film transfer, or independent corroboration of the1953narrative.

For alternate dated observations, obtain the actual Pacific County indexes linked by DGM/T153991055 and DOQ/T153991060, then establish coverage, acquisition time, tidal surface, camera geometry and control before comparing boundaries. Do not interpret empty date cells as1950, or nearby county coverage as target coverage.

No archive order, paid request, visit or third-party message was made. The available online lead changes the next retrieval action while leaving the physical photograph, transition timing, cause and global reconstruction unresolved. All twenty original outcomes remain active.

## Follow-up: the actual catalog description is recovered

The earlier application-shell limitation is now partly superseded. S270 uses NARA's [documented open export](https://www.archives.gov/developer/national-archives-catalog-dataset), accessed without an API key or account. All400objects under the RG23description prefix were downloaded and parsed:441,496,756bytes and11,823records. Their S3modification labels are September28,2026. These labels describe export objects, not historical records or photo dates; the export is not asserted to equal the latest live catalog.

The [acquisition manifest](../data/willapa-nara-catalog-acquisition.json) records every object URL key, hash, size and record count. The [audit script](../analysis/willapa_nara_catalog.py) checks those inputs and the [result ledger](../data/willapa-nara-catalog-audit.json). Two [unchanged record excerpts](../sources/originals/cascadia/nara-rg23-selected.jsonl) are preserved, not the complete400files. Initial16connection resets were resolved by a terminal-run retry at lower concurrency; final coverage has zero failed objects.

| Series305404field | Source value | Retrieval significance |
| --- | --- | --- |
| Local identifier |23-AERIALREPORTS |Specific series identity |
| Accession number |NN3-23-93-2 |Existing series accession; not proof of2022film transfer |
| Records-center transfer number |66A2582 |Cataloged series transfer locator |
| Arrangement |Final report numbers |Use report104/106, not an inferred frame-number filing order |
| Physical occurrence |Eight standard letter archival boxes;3ft6in |Reported extent, not a photographed/inspected box inventory |
| Finding aid |Report list filed among search paths |A list exists according to metadata; it was not retrieved here |
| General notes |Only104and106contain aerial photographs |Series-level selection rule, not authentication of frame1613 |

The exact source is rg_23-323.jsonl,line1. The description lists project instructions, diagrams, field-inspection reports, photographs, clippings and correspondence among its contents. None of those report contents was inspected in this step. The eight-box description and1957–1964span are archival metadata rather than measured shoreline observations.

The declared search used exact series/ancestor identifiers and title strings Willapa/Willpa. It found the series but **no descendant description for305404** in this export. This does not demonstrate that paper reports or photographs are absent, or that all relevant records would appear as descendants. Full OCR/text searches and other record groups are outside this test.

The second match is naId196068540, title **6185 - Willapa Bay, Washington**, rg_23-395.jsonl,line3, with reported scale1:40,000. Its preserved description supplies no authenticated exposure/survey date or digital image. It cannot yet be compared with the T9637chart-use log as a newly observed coastline.

Next obtain the report list and actual104/106contents using the concrete series/accession locators, or inspect alternate DGM/DOQcounty indexes if accessible online. Do not repeat absent-series-description as the current gap. The specific missing evidence remains the target photograph, annotated enlargement, field sheet and authenticated boundary/tide correspondence. No third-party request or API-key application was sent, and the full twenty outcomes remain incomplete.
