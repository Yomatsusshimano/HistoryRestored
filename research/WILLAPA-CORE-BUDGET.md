# Willapa core ages and a conditional sediment budget

2026-10-09. S274: Curt D. Peterson and Sandy Vanderburgh,2018, [Tidal Flat Depositional Response to Neotectonic Cyclic Uplift and Subsidence](https://doi.org/10.5539/jgg.v10n1p109). The [publisher PDF](../sources/originals/cascadia/willapa-tidalflat-2018.pdf) is preserved unchanged under its stated CC BY4.0license, with attribution to those authors. This release inspects selected methods, age and budget pages rather than certifying the complete study or reproducing its dating.

## Physical evidence, clocks and dependencies

PDF8/printed116describes sediment lost during core withdrawal, unexpanded shortening and preferential site selection. Reported compaction averages8percent in18cores; unknown top gaps prevent treating every recovered length as a complete original sequence. The [input ledger](../data/willapa-tidalflat-inputs.json) records selected inspection scope, hash, all23Table3rows and ten Table4rows. PDF19–20/printed127–128age-table scans were checked visually.

The age ledger preserves wood, peat, shell, introduced oyster and assigned subsidence-event markers separately. W18's AD1700contact is an assigned event age, not a radiocarbon determination. G1's starred300value is given for correspondence to that event, rather than an independently calculated median. Introduced oysters assume an approximately1900ADmarker. Calibrated wood/peat and shell rows use IntCal13 and MARINE13 respectively, with a392±35year marine reservoir correction transferred from Yaquina Bay, Oregon. Laboratory preparation, local reservoir suitability and sample-to-contact offsets remain unaudited. Neither event assignments nor related calibrated values are independent historical confirmation.

Beta158078is printed for both W3/pmwood at3.8m and W8/pfshell at1.2m, with different conventional ages. Both entries remain; the laboratory records are needed to resolve identity. W29's basal2.8msample has a table median126years BP, while adjacent prose calls its age approximately1.3ka. Table4W13age3.7kaalso differs from Table3's3973yearmedian at3.7m. W16Table4length3.2m differs from Table3's dated depth3.3m. None is silently repaired or attributed to fabrication.

## Numerical findings that support and challenge the source

The [audit script](../analysis/willapa_tidalflat_budget.py) calculates from printed inputs and retains [results](../data/willapa-tidalflat-budget.json). Table4W16gives3.2m/2.6ka, approximately1.231m/ka rather than printed1.1. W18gives0.9m/0.3ka,3.0rather than2.3. Both fail an interval-overlap check allowing half the final printed digit in numerator, denominator and reported rate. These are rounding diagnostics, not measured uncertainty.

Recalculating all ten ratios yields mean1.2283and sample SD0.6972m/ka, agreeing with the paper's rounded1.2±0.7. Thus the summary is supported by this calculation despite those row discrepancies. The printed rate column alone instead yields1.15±0.5017. The ratio of mean printed lengths to mean ages is0.9609m/ka; the prose's alternative0.9is not exactly reproduced from those displayed inputs. Unknown unrounded inputs remain relevant. Mean ratios and ratio means are different estimands; neither is an independent clock for a nominated mud layer.

## An executed supply constraint, not a validated flow model

Table5/PDF25assumes intertidal area1.9×10⁸m², sand fraction0.60and representative initial sandy-unit thickness0.5m. Their product is57millionm³of sand, compatible with the source's rounded60million. At1m/ka net accumulation, the same area/fraction yields114,000m³sand/year. Area, composition and thickness are extrapolated inputs, not a measured uniform baywide event horizon.

| Assumed duration for57millionm³ | Required average sand supply | Relative to17,685m³/year bedload-only scenario |
| --- | ---: | ---: |
|1year|57millionm³/year|3,223times |
|10years|5.7millionm³/year|322times |
|100years|570,000m³/year|32times |

These retrospective scenarios constrain what a rapid-deposition proposal would have to transport if those inputs apply. They do not establish impossibility: ocean/inlet supply, channel storage, erosion, porosity and recycling must also be measured and modeled. The source's100yearduration is an assumption; no event duration or candidate date is discovered by dividing volume by an assumed flux.

Reported tributary supply17,700m³/year is reproduced as131,000tonnes/year ×0.25 ×0.54 =17,685. Including the suspended load plus that bedload fraction instead yields88,425m³/year. Those scenarios distinguish sand/bedload from total sediment accounting; the original discharge grain-size partition and mass-volume factor need authentication before calling this an error or a closed conservation budget.

## Event deposit versus later accommodation filling

PDF20reports thin sandy laminae in eight protected marsh proxy sites, averaging0.5cm above17interpreted contacts; PDF25–26discusses sandy burial units averaging50cm above30contacts in13vibracores. These are different contexts and selections. Their thicknesses cannot be substituted for one another or generalized to every tsunami/debris setting. The source distinguishes possible initial inundation deposits from subsequent sediment infilling and explicitly leaves channel incision/source pathways unresolved. Its gravel lags have several possible causes.

The subsequent [grain-size audit](WILLAPA-GRAIN-AUDIT.md) recovers all printed Table2 entries. The roughly60% sample average is numerically plausible, while the reported composition census and grain-summary selection remain unreproduced. The table reports percent weight, so the volume products above additionally require explicit density, porosity and sediment-volume definitions; they remain conditional arithmetic.

Next recover laboratory identifiers, original core logs and exact dated-unit associations; reproduce calibration and quantify whether the inferred baywide volume survives spatial and conversion uncertainty. Then compare tidal/storm/post-subsidence and rapid-event transport models against the same observations. This selected audit advances physical inputs and rejection conditions. It establishes no worldwide event, new calendar transformation, independent review or complete catastrophe reconstruction.
