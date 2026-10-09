# Long Island processed reference chronologies recovered

2026-10-09. S233 adds three investigator chronology outputs from NOAA's [Washington chronology directory](https://www.ncei.noaa.gov/pub/data/paleo/treering/chronologies/northamerica/usa/), and three later NOAA tabular copies. This changes the access status: processed site outputs are available. Their exact relationship to the1997 study's input files and per-radius processing remains unverified.

## Versions and numerical coverage

| File | Type under NOAA's format convention | Valid assigned years | Valid annual values | Reported sample counts, min-max | Count at1699 |
| --- | --- | --- | ---: | --- | ---: |
| [wa129.crn](../sources/originals/cascadia/wa129.crn) | Standard | 991-1986 | 996 | 1-17 | 15 |
| [wa129a.crn](../sources/originals/cascadia/wa129a.crn) | ARSTAN | 992-1986 | 995 | 1-17 | 15 |
| [wa129r.crn](../sources/originals/cascadia/wa129r.crn) | Residual | 993-1986 | 994 | 1-17 | 15 |

S230's [NOAA format guide](https://www.ncei.noaa.gov/pub/data/paleo/treering/treeinfo.txt) distinguishes standard, residual autoregressive processing, and ARSTAN's reintroduced pooled persistence. The files themselves do not supply complete settings or per-radius indices. Type labels alone do not reproduce those operations.

The [audit script](../analysis/cascadia_chronology_audit.py) reads fixed-column index/count pairs, removes9990 missing slots, and compares every valid assigned year, index and sample count against the corresponding NOAA template file. All three comparisons are exact. Opening partial decades retain placeholders: the printed first-year fields are not instructions to shift the entire row to that year. Final slots1987-1989 are likewise missing, not measured growth.

The [acquisition ledger](../data/cascadia-chronology-acquisition.json) records all six URLs and byte hashes; preserved files remain unchanged. The [result ledger](../data/cascadia-chronology-audit.json) retains every annual index/count, version header and missing slot. Median reported sample count is10 in each version. These fields are not independent specimen identities, and the maximum17 should not be equated with the total19 trees mentioned in the paper: total trees and simultaneous annual contributions are different quantities, with the original membership/crosswalk still needed.

## Metadata and provenance limits

The templates identify study5382 and investigator D.K. Yamaguchi. They report contribution/file dates2005-09-14, chronology templates added2018-12-20, and raw templates added2019-02-08. Their publication fields are blank. These are archive metadata, not tree collection dates or proof of exact1997 file identity.

All templates share a generic First_Year991 and “standard chronology method” variable description, even though the residual data begin993 and its decadal header carries R. The residual valid span matches the1997 paper's993-1986 composite span; that is useful correspondence, not version authentication. The a/r suffixes and decadal type codes must remain explicit when using the records. Generic template resource descriptions also call them raw measurements; the values and CRN links identify processed chronologies.

These are alternative processed versions of one source collection. Their tabular copies are duplicates, not additional trees or independent dates. Earlier statements that processed outputs were wholly unrecovered are superseded; original settings, individual processed radii and exact study-version linkage remain unresolved.

## Next discriminating calculation

Compare the available residual chronology against separately declared processing of the snag widths, retaining standard/ARSTAN versions as sensitivities and all alternative placements. Call this an archived-reference diagnostic unless the original target processing and version identity are established. Do not label a hybrid raw/processed comparison as reproduction of the1997 published correlations or as an independent absolute-date test.
