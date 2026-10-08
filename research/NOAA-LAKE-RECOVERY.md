# Recovered lake records do not yet reproduce the Touchet reference

Research draft, 2026-10-08. C008; S171. No independent review.

The NOAA archive provides numerical Fish Lake, Oregon and Mono Lake, California records, but **this recovered release cannot supply the overlapping reference described by Clague et al. (2003)**. Its Fish Lake series stops at 9,966 radiocarbon years BP. The paper describes averaging the two lakes over 12,300–13,100 radiocarbon years BP. An extended or different Fish Lake version, or an explanation of that discrepancy, is still required. This is a version/coverage problem, not proof that the paper's directions or flood chronology are false.

## What was recovered

[NOAA's paleomagnetic data page](https://www.ngdc.noaa.gov/geomag/paleo.shtml) identifies the IAGA version 3.5 distribution. The original FTP service remains accessible at `ftp://ftp.ngdc.noaa.gov/geomag/Paleomag/access/ver3.5/`. Its release note says SECVR was unchanged from version 3.4, May 1999. The ASCII exports and Access 2000 database were retrieved. No database macros or application code were run: the MDB was opened read-only through Microsoft's ACE OLEDB provider.

The [structured subset](../data/secvr-lake-subset.json) retains five tables, exact export tokens and line numbers, field names obtained from the MDB schema, source URLs and SHA256 hashes. LOCATION links Fish Lake to reference 12 (Verosub et al. 1986) and Mono Lake to reference 18 (Lund et al. 1988). These are archived derivatives of those studies, not newly recovered specimen measurements or laboratory reports.

| Site | Stacked rows | Smoothed rows | Archived age extent | Rows within 12,300–13,100 in each series |
| --- | ---: | ---: | --- | ---: |
| Fish Lake, Oregon | 268 | 253 | 147–9,966 | 0 |
| Mono Lake, California | 404 | 404 | 12,250–34,967 | 12 |

The smoothed table explicitly distinguishes `C14AGES` from `CALAGES`; all selected `CALAGES` entries are blank. LOCATION describes C14 age assignments. These ages are not supplied with a separate radiocarbon assay at each row. Metadata endpoint ranges also differ from the actual numerical endpoints; the table above uses the latter. Depth units are not inferred from a column name.

For each lake, `C14AGES.txt` contains just one placeholder row: the site name followed by six empty fields. The MDB confirms nulls. **Zero populated assay rows in this release does not mean the original studies had no assays.** Material, laboratory ID, preparation, age uncertainty and age–depth construction still need original documentation.

Mono Lake's smoothed and stacked values are identical after removing the empty calendar-age column. The two files are representations of the same series, not independent observations. Fish Lake's metadata describes a seven-point weighted filter; this is distinct from the additional three-point smoothing described in the 2003 comparison.

## A second archive issue: depth precision

A direct MDB-to-ASCII check found matching ages, directions, intensities, row identifiers and null fields, but 415 Fish Lake depth entries differ: 213 stacked and 202 smoothed. Every discrepancy equals truncation of the database value to two decimal places in the ASCII export. For example, stacked result 2 has ASCII depth `0.20` versus MDB `0.209`. The maximum difference is 0.009 in the archive's depth units. This is not ordinary nearest-value rounding.

All differing depth pairs are preserved in the JSON. The export has not silently replaced the more precise database depths, and this precision difference has not been converted into a dating correction. Exact-equality checks initially failed; inspecting those failures exposed the export behavior. Age coverage is unchanged between the two representations.

## Reproduction and next test

Run `python research/check_secvr_lakes.py`. To additionally verify complete row selection, original-file hashes and exact tokens, download the five ASCII files named in the manifest and run `python research/check_secvr_lakes.py --source-dir PATH`.

The schema provenance records the MDB hash and read-only `OpenSchema(4)` procedure. The MDB comparison used `SELECT *` from LAKESTACK, LAKESMOOTH and C14AGES filtered on the two site names; numerical rows were joined on SITENAME and RESNO. The script checks the published depth pairs and coverage; it does not independently rerun the MDB query or reproduce scientific age models.

Next locate the actual extended Fish Lake series used in 2003, together with its age controls and the exact reference-curve transformations. Until then, do not extrapolate this Holocene series to fill the gap, splice in Fish Lake Utah, or claim a reproduced 60-year flood interval. The [Touchet directional observations](TOUCHET-MAGNETIC-AUDIT.md) remain separate evidence; this recovery supplies no new duration bound or common-event chronology.
