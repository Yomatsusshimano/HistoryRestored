# Lost Cabin reversal: original result and source-version differences

SOURCED_DRAFT, 2026-10-08. No independent scientific review.

S211 is Jonathan Schwing's2019 thesis as released by the Arizona Geological Survey in May2021, Contributed Report CR-21-B. [Original PDF](https://data.azgs.arizona.edu/api/v1/collections/AGCR-1674164262353-833/cr-21-bschwing.pdf). The117-page file has SHA256 `e32ac9bcc798d388307a5420cd2bf56905c3c730f721900c04a40f6dbb97dd3b`. Printed17 and46-47 (PDF25,54-55) were visually checked; methods printed9 and results15-16 were text-read. This is selected inspection, not a full thesis review.

## What passed

Printed17 reports an inclination-corrected reversal test classified Rb: observed angle7.15°, critical angle7.18°. Normal input mean is declination10.8°, inclination56°, N59; reverse mean is declination178°, inclination−56°, N111. The reported result passes by0.03° at displayed precision. This margin is not a p-value and does not by itself establish instability or failure.

The preceding paragraph explains the correction: uncorrected mean inclinations57.2° and−43.1° are replaced by56° and−56° after elongation/inclination analysis. The combined corrected inclination has a reported95% interval49°–64°. Thus the claimed pass belongs to the corrected analysis; it must not be described as an uncorrected test reproduced by this archive. Methods printed9 reports110 reverse components, whereas results16-17 reports111; retain that count discrepancy until the input list is reconciled.

Printed16 describes170 usable components from39 sites. The archive has not reconstructed the exact membership of the reversal-test input or its covariance/selection. It is unsafe to assume the reported pooled result is an independent local test of the36 Highwall specimens in Crow2021. The [Highwall audit](HIGHWALL-WASH.md) still correctly records Crow's explicit failed local test and provisional correlation. A passing comparison study does not automatically repair that failure.

## The Highwall records changed between versions

The thesis High Wall Wash table on printed46-47 has39 specimen entries. Crow2021 Table6 has36. Both contain matching specimen names and many matching directions, so they are versions of substantially shared observations, not independent replications.

| Example | S211 thesis release | S210 supplement |
|---|---|---|
| HWW6-2 | Reverse, thermal, rankC | Not listed |
| HWW6-11 | Reverse, AF/LTD, rankC; direction/MAD blank | Not listed |
| HWW12-10 | Normal, thermal, rankC | Not listed |
| HWW7-1 quality | B | C |
| HWW11-1 MAD / quality | 4.6 / B | 15 / C |
| HWW12-8 MAD / quality | 3.4 / A | 5.2 / B |

These are selected documented differences, not an exhaustive change log. No explanation for the revisions was recovered in the inspected passages. Removal, reinterpretation, transcription and correction are possible explanations to test; none is established. Retain the source-specific values rather than merging them into a synthetic dataset. This observation alone supplies no evidence of intentional manipulation.

## A coordinate discrepancy is now explicit

The thesis table repeatedly places High Wall Wash at **35.381872,−114.574136**. The later Table6 footnote gives **32.381873,−114.574136**. Latitude differs by nearly3°, far beyond rounding; longitude is identical. The earlier coordinate is a specific candidate correction to investigate, not yet a verified field location. Neither coordinate has a stated datum in these inspected entries. The thesis also prints the earlier pair for the Golden Section table, so a mapped location check remains necessary before choosing a canonical point.

[Structured comparison](../data/schwing-source-comparison.json) preserves both coordinates, test parameters and selected sample differences. Missing directions remain null; later-source absence does not mean the specimen never existed.

## What this changes

The original comparison test is now accessible and its correction dependence is explicit. Its source shares investigators and specimen records with the later study; it cannot be counted as wholly independent corroboration. Neither the reported pass nor these version discrepancies determine a historical-era age or a global catastrophe.

Next reconstruct the reversal-test input and correction procedure, inspect original location maps, and trace the documented revision path between the39- and36-specimen tables. These checks bear directly on the strength and geographic placement of the proposed time marker. Bed-specific age transfer and the main paper's fault-duplication interpretation remain separate unresolved tests.

## Follow-up: map, selection and chronological dependence

Additional inspection: printed29-30,68 and73 (PDF37-38,76,81) visually checked; methods7-9 and discussion26 text-read. These findings narrow the unresolved questions above.

**Location:** Figure5 places High Wall Wash Ash Site and Golden Section at separate labeled points east of Lake Mohave; Golden Section is southeast of Highwall. Their duplicated table coordinate therefore cannot accurately represent both plotted sites at the precision printed. The map confirms distinct locations in the named study region, but has no coordinate graticule from which this audit can validate the six-decimal entries. No replacement point was digitized. The later32° latitude remains a discrepant source value, not an accepted location.

**Selection:** Printed29 expressly excludes HWW1-HWW4 from site statistics because of coarse volcanic clasts, and uses AF demagnetization to assign reverse polarity to HWW5-HWW8 and normal polarity to HWW9-HWW12. This explains why a count of all thermal and AF specimen labels is not the author's site interpretation. It also gives a specific earlier interpretation of group8 against which to compare the later prose. It does not resolve which specimens entered every pooled statistical calculation. Printed26 explains that thermal treatment and AF can isolate different carriers and interprets a high-temperature hematite component as secondary; the archive has not verified this mineralogical interpretation.

**Test scope:** Figure10's caption explicitly describes mean directions from all sample sites. Consequently the published corrected test should be labeled a pooled study result, not a separately reproduced Lost Cabin Wash-only result. Exact membership, exclusions and the110/111 discrepancy still require reconciliation.

**Geometry check:** Using the printed mean declinations and inclinations and flipping the reverse mean to its antipode gives a corrected angular separation of **7.14742741°**, reproducing reported7.15°. The uncorrected printed means give **16.25146121°**. The spherical dot-product equation is `cos(gamma)=sin(I1)sin(I2)+cos(I1)cos(I2)cos(D1-D2)`. [Calculation script](../analysis/check_schwing_angles.py) reads the preserved parameters and updates [structured results](../data/schwing-source-comparison.json). This verifies geometry only: it does not reproduce the critical angle, bootstrap correction or reversal significance. In particular, applying the corrected7.18° critical angle to the uncorrected means would not constitute a valid uncorrected test.

**Age assignment:** Printed30 explicitly combines three dated ashes and the correlated reversal in two washes to identify the5.235Ma C3r/C3n.4n transition using Ogg2012. This is an interpreted match to a calibrated polarity timescale, not a numerical age measured from the magnetic direction alone. The same page assigns Golden Section to C3n.3r using lithology, elevation and the downstream Buzzards Peak4.83Ma age, leading to an inferred4.799-4.997Ma arrival interval. Those numerical bounds are author interpretations with shared inputs, not extra independent clocks. Modern elevations likewise are not automatically coeval paleosurfaces.

The next substantive step is to reconstruct the selected directional dataset and evaluate the ash/stratigraphic constraints used to choose among possible polarity intervals. The verified map distinction should prevent merging the two field localities; a location survey or georeferenced original map is still needed for precise coordinates.

## Candidate directional dataset: reconstruction attempt

The [candidate extraction](../data/schwing-direction-candidates.json) preserves168 numerical normal/reverse specimen rows from Table2 (printed40-49 / PDF48-57), plus22 other specimen lines for review. Inclusion is declared before interpreting the output: N/R label, numeric declination/inclination/MAD, quality A/B/C, equal weight per specimen, and no further method, locality or outlier exclusions. The alternative method spelling `Thermal` is included alongside `TH`. This candidate is **not** asserted to be the author's selected input.

| Uncorrected quantity | Candidate extraction | Thesis printed16 |
|---|---:|---:|
| Normal N | 57 | 59 |
| Normal declination | 12.1901° | 10.8° |
| Normal inclination | 56.1628° | 57.2° |
| Reverse N | 111 | 111 |
| Reverse declination | 176.8726° | 178° |
| Reverse inclination | −42.1262° | −43.1° |

Means are directions of summed unit vectors, not arithmetic averages of angles. A matching reverse count does not establish matching specimens or values. These differences are a failed reproduction of the reported pooled summary under this **specified candidate selection**, not proof the source's calculation is wrong. Potential causes include source-table versions, transcription/extraction limitations and different selections or processing. The thesis explicitly excludes some coarse HWW samples from site statistics, so the all-eligible-row selection cannot simply be presumed authoritative.

HWW6-11 has a reverse label but no numerical direction and is retained among ineligible/unparsed lines; no missing angle was invented. Ambiguous and N/A records likewise are not turned into normal/reverse observations. Table2 spans different specimen groups and includes site means; site-mean summary lines are not counted again as individual specimens. All preserved rows carry original PDF-page and line provenance. HWW scans were already visually checked; the remaining table pages need full visual transcription review before promoting this into a verified input dataset.

Reproduce with [the extraction script](../analysis/extract_schwing_directions.py), requiring pypdf:

```text
python analysis/extract_schwing_directions.py path/to/schwing2021.pdf data/schwing-direction-candidates.json
```

The next check is a row-by-row visual comparison and explicit reconstruction of selection rules. Do not adjust or add rows merely to force N59/N111 or the reported mean. The E/I correction and reversal test must wait for a defensible input dataset; the earlier mean-angle check remains valid at its narrower scope.

## Scan check and limited site-mean checks

All Table2 page images (printed40-49 / PDF48-57) have now been inspected across this and earlier audit steps. The previously pending non-HWW pages were checked against the extracted table text. No two missing normal numerical rows were recovered by this scan pass. The scan confirms, rather than repairs, such source entries as LCW20-6C labeled R with positive inclination67.5°, and LCW14-2 labeled A/A with no direction. Their interpretation is unresolved; source values remain unchanged. This is self-review of a transcription, not independent scientific review or proof of the original software input.

Three displayed site blocks were also tested using equal-weight sums of all listed specimen unit vectors, without fitting exclusions or corrections:

| Block | Recomputed declination / inclination | Printed site mean |
|---|---:|---:|
| Wolverine Creek1, printed48 | 172.2086° / −51.4181° | 172.2° / −51.4° |
| Wolverine Creek2, printed48 | 157.0966° / −49.9629° | 174.7° / −47.1° |
| Lost Cabin28, printed44 | 22.8098° / 38.6908° | 9.4° / 39.1° |

The first reproduces at printed precision; the other two do not. Preserving the successful control alongside failures prevents treating every computation as suspect. These are three selected checks, not a failure rate for the thesis. They do not identify the original weighting, processing or possible table-version changes. [Inputs/results](../data/schwing-site-checks.json) and [script](../analysis/check_schwing_sites.py) make the conditional calculations repeatable.

At this point, further ad hoc changes to specimen membership would risk fitting the answer. The decisive unresolved evidence is the original directional input/export and documented selection/correction settings, or an additional accessible source that supplies them. The archive can continue evaluating the regional chronology using independently specified ash and stratigraphic constraints while retaining this local reproducibility limit.
