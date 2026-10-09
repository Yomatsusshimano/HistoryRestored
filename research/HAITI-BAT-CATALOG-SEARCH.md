# Search by accession as well as taxon

2026-10-09. C011; S321 pinned museum export and S324 original2017study. Sourced draft without independent review.

The [earlier museum search](UFVP-SPECIMEN-PROVENANCE.md) selected bats by a Jérémie locality-name token. The [numbered-cave conflict](HAITI-BAT-LOCALITY-CROSSWALK.md) makes a broader search worthwhile: a bone's catalog locality might not contain that spelling. This follow-up reuses the same pinned export rather than adding an independent source.

The [script](../analysis/haiti_bat_catalog_search.py) checks the original archive hash and scans all554765occurrence rows. It selects Macrotus by the genus field or first scientific-name token, then filters the country field for Haiti. A separate Chiroptera census and exact catalog-number selection retain records missed by the genus filter. [Results and raw selected records](../data/haiti-bat-catalog-search.json) permit inspection of those boundaries.

## What the export actually contains

There are397Macrotus records across the export, one with countryHaiti: **UF282171** at Trou Jean Paul. The Haiti/Chiroptera selector finds2769records under four locality labels:2643JeanPaul,113CaverneSt.Ney,12TrouNicholas andoneJérémie5. These are catalog-record counts, not specimen-element or animal counts. No complete collection census is inferred from a downloadable export.

Both S324Macrotus accessions match uniquely:

| Accession | Catalog scientific name | Catalog locality/code | Collection date |
| --- | --- | --- | --- |
| UF282171 | Macrotus waterhousii | TROU JEAN PAUL / XH013H |1984-02-16 |
| UF307265 | Chiroptera | TROU JEAN PAUL / XH013H |1984-02-16 |

The2017specimen list assigns both to Macrotus waterhousii. The second export record retains only an order-level identification. Its blank genus explains why genus selection alone misses it. This does not establish that either identification is wrong or show a sequence of reclassification. Exact accession selection and source-specific identification must remain separate.

Both catalog records use18.28N,−72.28W, with blank datum and uncertainty. S324's Jean Paul locality row uses18.3375N,−72.280556W. The different precision and unknown datum do not authenticate either location or establish movement. Their matching locality code is an institutional catalog link, not an independent survey.

## The dated bone remains unresolved

Neither Jean Paul accession is assigned to Beta345518. The only Jérémie5bat entry, UF293830, is unidentified Chiroptera and likewise remains unassigned. S321has no dedicated radiocarbon laboratory-identifier field. A separate search across all occurrence-cell values finds no Beta345518token after removing whitespace/hyphens and ignoring case. This is bounded to the pinned export; it does not establish absence from labels, notebooks, laboratory records or museum holdings.

The next useful evidence is the original laboratory submission or loan/field-label record connecting the dated humerus to a UF accession and a numbered cave. More repeated searches within the same incomplete fields would not supply that connection. This branch can continue through original records while other geographic, construction and chronology tests proceed. No shared deposition, extinction date or global event follows from these catalog agreements.
