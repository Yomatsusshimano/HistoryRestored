# Cascadia source formats: rounding loss and unresolved depth order

2026-10-09. C004 / S244. Read-only comparison of four workbooks with their CSV counterparts in the USGS2022 release. The formats share observations and are not independent evidence.

## Acquisition and comparison

The original1992 Copalis paper remains unrecovered: the publisher PDF request returned an access challenge, and bounded publisher/title/USGS searches did not yield an inspected full copy. The indexed supporting-file name is a future retrieval lead, not a downloaded supplement. No access control was bypassed, contact made or purchase requested.

The already acquired, hash-recorded `supplement.zip` contains formatted DOCX/XLSX counterparts to the plain archive. Four original XLSX members are now preserved unchanged: [soil stratigraphy](../sources/originals/cascadia/field-release-2022/03_Soil_stratigraphy.xlsx), [sampled dead redcedar](../sources/originals/cascadia/field-release-2022/11_Redcedar_dead_sampled.xlsx), [live/reference redcedar](../sources/originals/cascadia/field-release-2022/13_Redcedar_live.xlsx), and [Copalis vented sand](../sources/originals/cascadia/field-release-2022/18_Copalis_vented_sand.xlsx). Extracted bytes match their archive members exactly. S244's CC0 attribution applies; no workbook was rewritten or recalculated.

The [script](../analysis/cascadia_format_comparison.py) aligns original rows and named headers, compares stored/cached numeric cells with CSV numeric text, and retains cell addresses, formats, formulas, hashes and source rows in [results](../data/cascadia-format-comparison.json). Blank footer rows are excluded from nonblank counts. Date/text formatting and all annotations were not exhaustively compared. The reader reported an unparsed-header/footer warning; header/footer presentation is therefore not verified. Workbook XML was separately checked for the consequential depth cells and one formula cache.

| Table | Nonblank source rows | Numeric differences | Difference fields |
| --- | ---: | ---: | --- |
| 3 stratigraphy |245 |78 |22 coordinate values,9 depths,47 surveyed extents |
| 11 sampled trees |86 |106 |Coordinates |
| 13 live/reference trees |43 |96 |84 coordinate values,12 diameters |
| 18 vented sand |68 |136 |Coordinates |

Counts are differing cells, not errors, independent observations or validation scores. Formatted numeric exports explain many of these differences. Additional stored decimal places do not establish corresponding field accuracy.

## Physical inputs that lose information in CSV

Table3's `Depth` cells use format `0.0`. Stored examples include:

| Source sheet/cell | Field and soil | Stored metres | CSV metres |
| --- | --- | ---: | ---: |
| 03_Soil_stratigraphy!K2 |750, Y |0.85 |0.9 |
| 03_Soil_stratigraphy!K4 |T13, Ws |0.55 |0.6 |
| 03_Soil_stratigraphy!K5 |T13, local soil3 |0.95 |1.0 |
| 03_Soil_stratigraphy!K6 |T17, Y |0.25 |0.3 |

Surveyed extent cells often use whole-number format `0`. Eighteen positive stored extent cells become literal zero in CSV. At **SL86-66**, soil3 has stored `DistCont=0.02m` and `DistTotal=0.02m` (L32/M32), whereas both CSV fields are0. Those CSV zeros cannot be treated as proof of no observed extent.

One Table3 formula at **L228**, locality K29/P13/P21–P24, is `=18*0.02`, with cached value0.36 and CSV value0. An independent multiplication gives0.36. This verifies this simple arithmetic only; a cached value is not evidence of current native-engine recalculation or original measurement accuracy. No source formula was changed.

For Table18, thicknesses, zero/unknown distinction and vent flags remain as previously audited; all136 numeric differences are coordinate values. The CSV-based [GeoJSON](../data/copalis-vented-sand.geojson) remains a faithful export of that source format, not a full-precision survey. Future distance/elevation work should declare which coordinate version it uses and retain positional uncertainty.

## Exceptions that survive this comparison

The three [Copalis depth-order exceptions](COPALIS-VENTED-SAND.md) are present in the stored workbook values, not introduced by CSV rounding:

- **T6:** K17–K20 store0.4,0.9,0.4,0.9m for successive Y,Ws,U,S rows.
- **T1:** K21–K23 store1.3,1.8,0.3m for Ws,U,S.
- **A31:** K26–K29 store0.9,0.5,0.8,0.9m for Y,Ws,U,S.

The earlier coordinate discrepancies likewise remain. Table3 A31 is−124.1627/47.1197; Table18 stores−124.16091666666667/47.120416666666664. Table3 A40 is−124.1626/47.1198; Table18 stores−124.162470379/47.12028611. Rounding these Table18 values reproduces its CSV coordinates, but does not make them identical to Table3. No preferred point or repaired section is selected.

Table11 still has86 nonblank named rows in both formats, despite the guide's87. Table18 still has68 in both, despite the guide's67 overview. Table13 still gives tree702 endpoint1369/count379 and tree767 count882; the earlier measurement-range qualifications persist. The tree766 comments still name outer line1755O. These are not resolved by changing formats.

## Consequences for reconstruction

Use stored values, explicit units, source measurement precision and cell locators when building physical inputs. Preserve original CSV-based results as versioned diagnostics; do not silently replace their inputs or advertise decimal recovery as new field measurements. The release enables better input preparation but does not authenticate the cause, age, source pressure, sediment volume or global extent of venting.

Next: obtain original drawings/notes to resolve the surviving depth and location exceptions; inspect original1992 figures through a working authorized source; audit the Table6 calibration and sample associations separately. No original-note, native-engine, field or independent-review validation is claimed.
