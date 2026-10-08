# MacBlo reference anchors and their dependencies

2026-10-08. Supporting audit for C020; no independent scientific review.

[Black et al. 2023, S79](https://doi.org/10.1126/sciadv.adh4973) reports that Jacoby collected MacBlo cores from living and dead trees in 1991. King and Harley remeasured archived material in 2021; 15 trees were dated, nine retaining bark. The article describes both statistical and anatomical checks. Its text says CAN382 but links study 38202, whose NOAA code is CAN682; retain the identifier discrepancy. Original collection logs, specimen-level bark records and scan sequences have not been inspected here.

The [NOAA measurements, S77](https://doi.org/10.25921/g9vh-cy16) contain nine series extending through assigned year 1990; each also spans 1507. Thus the 1507 reference position does not depend solely on joining short, detached early fragments. This is a property of the published measurements, not authentication of their calendar labels or physical continuity.

The 2023 study also reports a radiocarbon-pulse check in linked earthquake-killed wood. [Supplement Table S2, S80](https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10530078/supplementaryFiles), PDF page 8, was visually inspected and all 35 rows extracted with lab accession identifiers. The [script](../analysis/macblo_anchor_audit.py) computes adjacent differences from the printed values:

| Site label | Assays | Largest increase at assigned years | Change in published Δ14C |
| --- | --- | --- | --- |
| Lake WA | 13 | 774 → 775 | 10.373 |
| Hamma | 11 | 774 → 775 | 10.142 |
| Price | 11 | 774 → 775 | 8.182 |

Fraction-modern measurements rise at the same transitions. [The ledger](../data/macblo-anchor-audit.json) retains values, uncertainties as printed, all annual differences, source hash and reference spans. Assay counts are not independent tree counts. Adjacent differences share measurements; no probability of a unique match is calculated here.

The evidence chain is: reported collection-year/bark anchoring → MacBlo ring placement → relative matching to earthquake-killed wood → a separately measured radiocarbon feature assigned to the established 774–775 excursion. Electron is linked through its separate ring-pattern comparison with MacBlo. The pulse assays were not taken from MacBlo or Electron. This supports a cross-checking route but does not constitute a new blind date determination in this archive. Original pulse-reference data, sample custody and a full independent model comparison remain needed.
