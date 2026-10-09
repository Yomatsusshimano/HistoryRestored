# Cascadia field-table release: specimen association and reference-tree limits

2026-10-09. C004 / S244, compared with S61 and S229. A later USGS compilation supplies substantially more field context than the previously inspected article paragraphs. It does not independently authenticate specimens or calendar dates.

## Acquisition and inspection

The [USGS release](https://doi.org/10.5066/P9GEWF58), published September 16, 2022, was compiled by Brian F. Atwater in 2019–2020 from work mainly performed in 1986–1998. The landing page marks it CC0. ScienceBase JSON and all three listed downloads were recovered with ordinary certificate verification after web-tool access failed. The [acquisition ledger](../data/cascadia-field-acquisition.json) records URLs, sizes and SHA256 hashes. The unchanged [plain ZIP](../sources/originals/cascadia/field-release-2022/plain.zip) is preserved publicly.

The plain ZIP contains the guide and 18 numbered tables. Inspection here concentrates on guide sections on overlap, georeferencing and western redcedar, and CSV Tables 10–13. Other tables are acquired, not fully audited; formatted DOCX/XLSX versions and XML are likewise not claimed inspected. The guide is UTF-16; CSV parsing uses CP1252, retaining original bytes in the ZIP. Blank footer rows are excluded only from explicitly stated nonblank counts.

## GF2: newly recovered source-level links

Tables 10, 11 and 12 each identify GF2 at longitude −124.1632, latitude 47.1316. The guide specifies WGS84 and says these locations supersede earlier NAD27 coordinates. Table 12 rates GF2 coordinate confidence A, based on a conspicuous leaning tree on georeferenced airphotos. This is a source-derived location, not a new survey or precise footprint of the sampled root.

Table 12 reports:

| Field/context | Recorded information | Limit |
| --- | --- | --- |
| Root collection | May 31, 1994; bark-bearing root sawed as **UC-DC-3**, one slice 12 cm thick | Identifier and dimensions reported in compilation; original label, slice and accession record not inspected |
| Trunk collection | May 25, 1995; GF-2 sampled in three cores to match the sawed root | Supports reported one-tree association; no independent custody authentication |
| Tag identity | Tag **60**, recorded June 27, 1997 as tag **50** | Explicit conflict retained; do not silently choose one |
| Reported growth years | Trunk outer ring 1675; root bark ring 1699; earliest sampled ring 1368 in GF2RTB | Inherited ring assignments, not dates independently established here |
| Count field | RingCount 255 | Does not reproduce original processed series; guide's fields mix trunk and earliest root information for GF2 |
| June 27, 1997 exposure | Sandy gray mud without an organic horizon, containing sawed root in growth position; bark on lower third | Compilation of observations, not a newly inspected exposure or demonstrated worldwide layer |
| Depth below modern marsh | Root described at 0.9–1.3 m; buried-soil top 1.0 m below cleaned-bank marsh surface | Source wording retained despite describing no organic horizon; depth is not automatically subsidence or event-deposit thickness |
| Estimated tidal datum | Root 0.8–1.2 m below local MHHW | Approximate local tidal reference, not an independently reconstructed 1700 level |

The MHHW estimate used leveling to a high but ebbing tide on September 11, 1996, adjusted using an Aberdeen prediction. GF2 was connected by leveling on June 27, 1997 to a benchmark beside tree 789, with a reported 7 cm closure error. The tree-789 notes describe a December 29, 1997 cross-check differing by 0.1 m. These are distinct error/context statements; they are not a complete uncertainty budget and are not automatically additive corrections to GF2.

The compilation says the leaning trunk subsequently fell into the river; Table 10 places this between 1997 and 2000. Present physical accessibility or survival of sampled material is unknown. A linked historical oblique photograph is a retrieval lead, not an image inspected in this audit.

This advances the earlier [physical-linkage audit](CASCADIA-ROOT-LINKAGE.md): publications do supply specific specimen and survey details. The remaining gap is original-note/label/accession verification, not a total absence of reported root/trunk association. These tables, earlier articles and their measurements share researchers and fieldwork; they are not independent witnesses.

## Nineteen reference trees versus twenty-one measurement series

Table 13 has 43 records: 23 new redcedar, one survivor and 19 Long Island witnesses. Explicit label mapping accounts for all 21 S229 wa129 series. Two trees have inner/outer measurement series. [Reproducible audit](../analysis/cascadia_field_release.py) and [all-row crosswalk](../data/cascadia-field-audit.json) retain each source row and archived range.

Seventeen tree rows agree with the archived first year, last year and count of distinct measured years. Two need qualification:

- **702:** Table 13 gives 991–1369 and 379 rings. The archived LI702O measurements cover 991–1368, 378 values; the 999 unit/end marker occupies the next year position. Inclusion of that marker could explain the one-year difference, but the original compilation calculation has not been recovered. No ring is invented for 1369.
- **767:** Table 13 gives 1036–1917 and 882 rings. That is the inclusive span. Its explicitly reported inner/outer series cover 1036–1535 and 1544–1917: 874 distinct measured years with an eight-year gap. An inclusive span must not be treated as 882 measurements.

The 766 comments name an outer line `1755O` for 1515–1986. No such label occurs in the recovered wa129 file; **LI766O** has that range. The comments' label discrepancy is retained rather than silently corrected. Its 637-year distinct union agrees with the table's count; the overlapping two lines contain more measurements than distinct years.

The guide warns that all 19 witness-tree coordinates have larger location uncertainty. Most trees were sampled as recently logged stumps; some were already dead. Table 13 includes two witnesses whose first retained rings are after 1700 (760 and 759). “Witness” is the source's tree category, not a guarantee that every retained radius supplies pre-1700 growth or a living endpoint. Do not equate 21 series with 21 independent trees or infer that all endpoints were observed in living trees.

## Counts and source-version cautions

The parsed plain files contain 337 Table-10 records, 86 nonblank FieldID rows in Table 11, and 23 in Table 12. The guide describes up to 338 georeferenced victims/candidates and 87 sampled trees, including GF2. Table 11 has three blank footer rows; Table 12 has four. Footer removal does not reconcile the guide's 87 with 86 actual named rows. Formatted spreadsheet/source-version comparison remains pending; no missing tree or deliberate omission is inferred.

The guide also distinguishes confirmed/probable dead trees from candidates inferred from unexplained nineteenth-century map symbols. Its headline census is not 338 newly authenticated earthquake victims. Missing buried-soil entries need not mean the soil was absent: excavation was often for chainsaw sampling rather than stratigraphic observation.

## Consequences and next tests

The release narrows field-context gaps and provides locators for original notes, observers and photographs. It supplies neither Ozette ring-width measurements nor the original per-radius decay/spline/autoregressive output in the inspected material. The [regional processing sensitivity](CASCADIA-COMBINED-REGIONAL.md) therefore remains unresolved. No replacement date, chronology break or global-event link follows from this field compilation.

Next: inspect original GF2 field notes and slice/tag/accession records using UC-DC-3, GF-2 and both tag numbers; compare Table-11 versions/counts; inspect the linked photograph without treating it as custody proof; recover original processing/Ozette inputs. The other acquired sediment, radiocarbon and survey tables offer a separate route to testing regional deposits and chronology, requiring their own audit rather than wholesale acceptance.
