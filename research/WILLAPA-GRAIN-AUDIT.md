# Willapa grain-size reproduction and budget limits

2026-10-09. Source S274, Peterson and Vanderburgh (2018), [original preserved article](../sources/originals/cascadia/willapa-tidalflat-2018.pdf). PDF16-18/printed124-126 were visually inspected. Table2 has 31 site rows; the additional W29 sample at 3.5-4m occurs in its notes. The [literal input ledger](../data/willapa-grain-inputs.json) retains all 217 grid cells plus that note sample, distinguishing missing `na`, unprinted cells and reported composition with no grain mean. All 157 composition/grain tokens agree with a separate PDF text-extraction comparison; depth placement was checked on scans.

The [executed audit](../analysis/willapa_grain_audit.py) verifies the original PDF hash and publishes [results](../data/willapa-grain-audit.json). It uses printed sand percentages without normalization. All declared selection variants are retained; none is treated as the authors' authenticated analysis selection.

## Counts and numerical reproduction

| Selection | Composition count | Mean sand by weight | Grain count | Mean grain size, µm | OLS R² with intercept |
| --- | ---: | ---: | ---: | ---: | ---: |
| Paper's reported summary | 159 | 70% | 144 | 185 | 0.7 |
| All table entries and W29 note | 157 | 68.439% | 144 | 187.799 | 0.142638 |
| Table only, excluding note | 156 | 68.462% | 143 | 187.748 | 0.142952 |
| All except KI11 | 151 | 69.404% | 144 | 187.799 | 0.142638 |
| Only bins ending at or above 3m depth | 149 | 69.148% | 138 | 188.594 | 0.130720 |
| All except W28 2-2.5m cell | 156 | 68.724% | 143 | 184.601 | 0.661350 |

All entries include 16 explicit missing cells and 45 unprinted cells; neither becomes zero. Thirteen reported compositions have no grain mean. Excluding KI11 changes composition counts but not grain counts because that core has no reported grain means.

W28's 2-2.5m entry is literally 24:36:40 sand:mud:gravel and 645±504µm. With it retained, the range is 86-645µm, rather than the prose's 86-249µm. Removing this cell reproduces the reported range, rounded 185µm mean and one-decimal R²0.7, but leaves 143 pairs rather than 144. This is a sensitivity result, not evidence that the authors actually excluded it. Original worksheets and selection rules are required to reconcile the summaries. Grain SD describes the grain distribution; it is not a confidence interval for the sand percentage or budget.

Five printed compositions do not sum to100: W4 3-3.5m=110, W6 1-1.5m=101, W11 1-1.5m=101, W16 0.5-1m=94, W24 2-2.5m=98. Possible rounding is relevant to small differences but does not reconcile every entry. Values remain literal. The separately reported strict-total100 sensitivity also fails the stated composition count. These discrepancies do not establish deliberate fabrication.

PDF16 also prints beach mean sizes0.19-0.27µm and inner-shelf0.13-0.23µm while comparing them with185µm. The units are preserved as printed; the cited earlier measurements must be inspected before proposing a correction.

## What the sand fraction supports

PDF24/printed132 estimates60% sand from159 vibracore sections plus20 gouge-core sections assigned apparent0% sand. Its stated0-3m depth scope is not identical to the complete Table2 selection, which includes deeper bins and the W29 note. The literal ledger instead supplies157 compositions; adding20 assumed zeros produces177 entries and **60.706% sand by weight**. The selection restricted to bins ending at3m gives149+20 entries and60.964%. These values are compatible with approximately60% at one significant figure, without reproducing the reported179-entry census.

Applying60.706% directly to the previous area1.9×10⁸m² and thickness0.5m produces **57.671millionm³** under the same conditional conversion as the [previous budget](WILLAPA-CORE-BUDGET.md). The roughly1.18% change from57million is a numerical sensitivity, not a confidence bound. The source's20 zeros are assumed apparent compositions, not20 recovered sieve measurements.

Equal weighting of the31 core composition means yields68.586%, compared with68.439% for equal weighting of all157 samples. Their closeness does not establish spatial representativeness. Neither scheme weights measured depositional areas; differing core lengths, selection of sites, missing intervals, compaction and environments remain consequential.

The table explicitly reports **percent weight**. For constituent masses M_s and M_i and densities rho_s and rho_i, the sand solid-volume fraction is `(M_s/rho_s) / sum(M_i/rho_i)`. It equals mass fraction if constituent densities are equal. Sand solid volume additionally depends on the solid fraction of the bulk deposit; an equivalent bulk sand volume needs its own packing/porosity definition. No measured density or porosity is supplied by this audit, so these are unresolved conversions rather than guessed corrections.

The approximately60% input is therefore numerically plausible as a coarse sample average. The specific census, grain-summary selection and baywide mass-to-volume extrapolation remain unreproduced. Next recover original measurement worksheets and spatial sampling weights; specify density/porosity and sediment-volume definitions before comparing conserved tidal, storm, post-subsidence and rapid-event transport models. No event date, worldwide layer, independently validated model or successful prospective prediction follows from this calculation.
