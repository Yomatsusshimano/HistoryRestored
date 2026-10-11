# Shelbyville: modern parcel controls and nomination access

Research draft, 2026-10-11 (America/New_York). C030/R004; S391–S392. No independent review. [Structured query, records and retrieval ledger](../data/shelbyville-parcel-controls.json).

The county-linked public GIS connects **212 and 216 E Main Street to separate adjoining parcels in Original Town Block 4**. This materially narrows the address relationship suggested by the commercial listing. It does not yet connect an individual historical map footprint, the surviving vault or the original Reddit photograph to a certified parcel survey.

## County provenance and selected records

The county's [GIS instructions](https://www.shelbycounty-il.gov/documents/Zoning/Zoning%20Map.pdf), visually inspected as a complete one-page document, explicitly link [the public GIS portal](https://shelby-il.bhamaps.com/). Its HTML embeds an ArcGIS experience. The experience's public configuration advertises the [REACH_Parcels layer](https://services6.arcgis.com/nVxsrc8f8eCUeWXM/arcgis/rest/services/REACH_Parcels/FeatureServer/0). These are one delivery chain, not independent confirmations.

After inspecting the actual layer schema, an address-only query requested parcel identifiers, site addresses, selected legal fields and geometry. No owner-name fields were requested. The complete query parameters and response hashes are preserved in the ledger.

| Site address | Parcel identifier | Recorded legal description, selected portion | Recorded dimensions |
| --- | --- | --- | --- |
| 212 E Main | 2013-07-20-409-003 | Parts of lots 5 and 6, Block 4, Original Town | 28 feet × 100 feet |
| 216 E Main | 2013-07-20-409-004 | Parts of lots 5 and 6, Block 4, Original Town | 20 feet × 150 feet |

The returned polygons share a boundary, with 212 west of 216. Both reach the same northern frontage in the returned geometry; 216 extends farther south. These are readings of current tax-map geometry, not measurements from an original deed or certified survey. Returned coordinates use WKID 4326; no elevation or vertical datum was obtained. The service-wide edit timestamp is preserved only as retrieval metadata, not a record-specific date or historical event.

## What the match establishes

The [engineer's 2020 report](SHELBYVILLE-VAULT-ENGINEER-REPORT.md) identifies 212 E Main and estimates a vault plan approximately 28 feet east–west by 12 feet north–south. The county record's **28-foot parcel width agrees with that estimate**. It is a consistency check between address, parcel description and reported vault dimensions. It is not unique identification, a survey of the vault, proof of the commercial listing's ownership claims, or authentication of the Reddit photograph.

Block 4 also agrees with the [1886/1893/1933 map comparison](SHELBYVILLE-MAP-SEQUENCE.md). Exact registration still requires controls: earlier maps say W. Main and use different numbers, while the county records say E Main and current 200-series addresses. No dated renumbering/direction instrument, deed sequence or unchanged-fabric demonstration has been recovered. The 28-foot value is a horizontal dimension and cannot be treated as burial depth.

## National Register retrieval limit

The [NPS record for Shelbyville Historic District, NRIS 76000729](https://npgallery.nps.gov/AssetDetail/NRIS/76000729), advertises two downloadable assets. Both delivered one-page PDFs saying that the National Register PDF has not yet been digitized. The first was rendered and visually inspected; the second's extracted text was inspected. No nomination, numbered building inventory or construction chronology was obtained from these assets.

A separately encountered state PDF URL failed with a closed transport connection. These retrieval results do not establish that the nomination is absent, that no state digitization exists, or that its inventory contains no relevant building. The missing original record remains a concrete next target.

## Remaining test

Use original deeds, historical plans, a dated address crosswalk and controlled map registration to link specific footprints and surviving masonry. Obtain dated street-grade profiles or ordinances before adopting the engineer report's uncited historical grade-buildup account. Obtain the original Reddit photograph and remediation completion records. Any proposed natural mud layer needs an inspected section, sample identity and dating evidence. Current parcel records provide none of those measurements.
