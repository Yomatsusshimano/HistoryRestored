# Camp Century plants and sediment chronology

Research draft, 2026-10-08 (America/New_York). C014, S25-S26. No independent review.

## Plants and their context

[Christ and colleagues (2021)](https://doi.org/10.1073/pnas.2021442118) describe upper sample 1059-4 and lower sample 1063-7 beneath Greenland's ice. Figure 3 shows twigs and moss remains, including *Polytrichum juniperinum*, *Tomentypnum nitens* and a possible *Empetrum* twig in the upper sample. The lower sample has less identifiable bryophyte remains. The fungus *Cenococcum geophilum* is kept separate from plants. These are recovered fragments, not a documented rooted forest.

The paper reports a twig radiocarbon result older than 50 radiocarbon ka, while its methods discuss small sample mass and possible modern-carbon contamination. The detailed radiocarbon table is uninspected here; this audit does not substitute that bound for an exact plant age. The upper sample's initial luminescence work was compromised by light exposure.

## Later sediment measurement

[Christ and colleagues (2023)](https://doi.org/10.1126/science.ade4248) dated potassium feldspar from the frozen core interior, cut under darkroom conditions. Figure 3 reports corrected ages of 434 ± 39 ka and 395 ± 36 ka; the pooled result is 416 ± 38 ka. The text calls the pooled uncertainty 1 sigma. It interprets the sediment as deposited by flowing water after sunlight exposure.

The coarse fraction is 150–355 micrometres in page 2 text and Figure 1, but 150–250 in Figure 3. This discrepancy remains unresolved. The 2023 core log refines the upper unit from the earlier diamicton description to bedded sand. Original aliquot data and supplements have not been audited.

## Measurement and inference boundaries

| Evidence | What is being measured or described | What it does not alone establish |
| --- | --- | --- |
| Plant micrographs and identifications | Biological fragments recovered from particular core samples | Growth in their exact recovered positions; one forest type; precise death dates |
| Feldspar luminescence | A mineral signal interpreted through exposure, dose and correction models | A direct date for each plant, worldwide flooding, or historical chronology fabrication |
| Sedimentary bedding and provenance | A proposed local depositional process and material source | A globally shared event or a quantified flood magnitude |
| Ice-sheet simulations | Consequences conditional on model parameters | A measured shoreline or unique reconstruction of the entire ice sheet |

The later interior sampling offers a stated reason why the newer luminescence analysis can be informative despite the earlier light-exposure problem. That procedural explanation still needs checking against handling records and raw data. It should neither be dismissed as an unexplained date change nor treated as proof that every possible contamination problem was solved.

The earlier and later studies share core material and some investigators/data. They are complementary analyses, not fully independent discoveries. Grain-size fractions from one subsample are not separate regional event dates. The pooled age and its two contributing fraction results must not be counted as three independent dates.

This is positive evidence worth investigating for vegetation and major local environmental change beneath present ice. It does not by itself support a recent global mud flood, sudden geographic upheaval, or a connection to the Arctic camel, hyena or historical urban cases. Connecting those cases requires compatible event horizons, not merely surprising modern locations.

## Access, reproducibility and next work

Figure 3 in each paper was visually checked from local PDF renders. Relevant main-text results and methods were read; the 2023 page-2 grain-size description was read as extracted text. Rendering warned about unavailable fonts in the 2021 PDF; the checked plant labels and the 2023 age/size labels remained legible. The PDFs are linked through S25-S26 with retrieval hashes, not republished here. PMC access failed, but institutional PDF copies were accessible.

[Structured dating records](../data/dating-records.json) retain separate fraction and pooled rows, shared-parent identifiers, uncertainty wording and both conflicting size labels. They are transcriptions, not a new calibration. No exact specimen coordinates, additional taxa, or unreported direct plant ages have been invented.

Next: retrieve radiocarbon and luminescence supplements, reconcile the size labels and uncertainty definitions, and reproduce fading/residual-dose corrections from aliquots. Check plant transport and sample handling against core photographs and logs. Assess later work before treating this two-paper audit as a current comprehensive synthesis.

## Catalog location and custody follow-up

S134, the [NSF Ice Core Facility catalog](https://icecores.org/inventory/camp-century), supplies a CC 63-66 drill-site coordinate and directs basal-material custody to the Niels Bohr Institute. This supersedes missing site coordinates, while individual plant growth positions remain unknown. See the [spatial audit](WILDLIFE-GEOGRAPHY.md) for the coordinate role and precision limits. No custody-chain inspection or sampling has occurred.

## Handling history: sample-specific limits

[Bierman et al. (2024)](https://tc.copernicus.org/articles/18/4029/2024/) (S135), section 4.1 and visually inspected Table 5 (p.4044), documents archive alterations. The [handling ledger](../data/camp-century-handling.json) preserves affected segment IDs: two missing, two previously thawed and six inverted according to the text. Table 5 omits the inversion flag for 1063-7, listing prior pilot sampling only; omission remains unknown rather than a denial. Section 3.3 describes correcting inverted magnetic vectors by a 180-degree rotation about the sample x-axis. Original orientation reconstruction remains unaudited.

For our interpretation, storage orientation, original depositional order and event age are distinct. A stored cylinder turned upside down does not by itself redetermine its age, prove geological overturning or invalidate other segments. Conversely, a reported correction cannot substitute for checking the photographs, sample axes and resulting measurements. The 1063-7 discrepancy should be reconciled before using its directional evidence.

This publication narrows the earlier custody gap but does not close the chain of handling. Next inspect the segment-level supplement and original photographs, and connect the dated interior aliquots to their precise parent segments. No missing segment is treated as an absent geological layer, and no archive alteration establishes intentional historical fabrication.

## Supplement follow-up: scope of the orientation issue

[S136, Tables S5 and S9](https://tc.copernicus.org/articles/18/4029/2024/tc-18-4029-2024-supplement.pdf), PDF pp.6 and 10, were visually inspected. S5 supplies no magnetic-direction values for 1063-7; S9 lacks an inversion statement and says its dimensions could not be measured after pilot cutting. Thus these tables do not resolve the main-text statement, but they prevent us from assigning this sample a magnetic result that is not reported.

S9 explicitly calls 1060-C4 inverted, whereas the main text and S5 footnote flag 1060-C3. S5 also lacks an inversion footnote on 1063-4, despite main-text/Table 5 reporting. The ledger keeps each source component separately. Missing flags are not assertions of upright orientation.

The next discriminating evidence is the original segment photographs, sample-axis records and uncorrected magnetic vectors. Until those are reconciled, do not silently swap sample identities, flip published values again, infer polarity boundaries, or convert these metadata differences into age corrections. These tables are from the same study and provide internal cross-checks, not independent validation.

## Cosmogenic model dependency and static code audit

The [author-linked script](https://github.com/drewchrist-geo/Camp_Century_complex_26Al10Be_modelling/blob/b00d69a476ff0bba2d236bc180e48f88dece5982/lumin_cosmo_burial_model_jun23.m) (S137) is pinned by commit and hash in the [model ledger](../data/camp-century-model-audit.json). Lines 64-65 prescribe a normal draw with mean 416,000 years and error 38,000 years. This is an input to the burial/exposure calculation, not an independently recovered luminescence age. Agreement of the conditioned output with that input cannot be counted as a second confirmation.

Static inspection found that line 240 constructs lower-sediment uncertainty `ratl_0unc` using upper-sediment ratio `rat_0`, rather than the corresponding lower ratio `ratl_0`. The result feeds an uncertainty summary and compiled array. Its effect on the paper's reported values and figures has not been quantified; the script's other covariance calculations must not automatically be declared affected. No source code or scientific result has been corrected here.

The script uses 100 simulations and contains no explicit random-seed assignment. Exact execution and sensitivity to simulation count, weighting and constants remain pending. The publisher returned HTTP 403 for the attempted luminescence supplement, leaving dose-rate, fading and residual-dose reproduction unresolved. This code audit narrows evidence dependence; it does not redetermine either sediment or plant ages.

## Quantified uncertainty-prefactor sensitivity

The pinned repository's `cc_nuclides.mat` was decoded into [eight numeric arrays](../data/camp-century-nuclide-inputs.json), with its hash preserved. These contain six upper and three lower concentration/error entries; laboratory identifiers are absent, so row positions are not invented assay identities.

The [component calculation](../analysis/camp_uncertainty_prefactor.py) uses the code's inverse-square-root-error weights on the central input values, without random perturbations. Weighted upper and lower Al/Be ratios are approximately 4.4079 and 1.7448. Applying the source's common burial correction gives 5.4159 and 2.1438. The ratio between the two, **2.5263**, is the multiplier introduced in this central-input calculation by the upper-ratio prefactor in the lower-ratio uncertainty expression. The common burial factor cancels in this comparison.

With normalized weighted within-array spreads, the expression gives approximately 0.9840 using the upper ratio and 0.3895 using the corresponding lower ratio. These are illustrative component spreads, **not replacement published uncertainties**. Monte Carlo perturbations, covariance, measurement calibration and other code paths have not been reproduced. Substituting only this uncertainty prefactor leaves the mean ratio unchanged. Neither value changes the imposed luminescence age or independently dates deposition.

Three analytic checks verify equal weights, the inverse-square-root weighting rule and zero spread for identical observations. They test the implementation, not the physical model. Full execution and comparison with the published outputs remain necessary before assigning a scientific effect to the source-code concern.

## Surface-exposure threshold reproduced as a component

The [threshold calculation](../analysis/camp_exposure_limit.py) solves the source model's production equation for the duration at which inherited inventory reaches zero, separately for Al-26 and Be-10. At the central weighted inputs and prescribed 416 ka burial, the crossings are **16,701.8 years for Al-26** and **22,460.5 years for Be-10**. Both inventories must remain nonnegative, so the Al-26 crossing controls. The last admissible point on a 1,000-year grid is therefore 16,000 years, consistent with the source code's approximate central criterion.

Using its alternative Al-26 production rate of 27.8 rather than 30.3 atoms/g/year gives a central crossing of 18,217.1 years, with other inputs fixed. These rates are source-code scenarios, not newly calibrated measurements. The article itself cautions that production below the surface permits longer exposure (S26, pp.2-3).

A seeded 100,000-draw component calculation propagates independent Gaussian measurement errors and the specified 416 +/- 38 ka input. Its threshold median is 16,698 years, with 2.5th and 97.5th percentiles of approximately 15,319 and 18,182 years. No draws were excluded; Al-26 controlled every sampled crossing. The [result file](../analysis/camp-exposure-limit-result.json) records assumptions and the input hash.

These are percentiles of a **conditional threshold distribution**, not a posterior for actual exposure or a confidence limit proving exposure ended by 16 ka. Production uncertainties, shielding, erosion and error correlations remain omitted. The two nuclides share the sampled burial age. Gaussian aggregation reproduces the linear weighted-mean sampling distribution under independence; it does not reproduce the finite MATLAB random stream, its plots or the full model. The previously flagged lower-sediment uncertainty expression is not used in this upper-sediment threshold calculation.

Three analytic tests check inversion of the production equation, its boundary cases and weighted-Gaussian variance. This supports a specific numerical interpretation of the exposure limit, while the luminescence input and the broader catastrophe claim remain independently unverified.

## Later dating lead and raw-data access audit

[Woznick's 2024 thesis record (S142)](https://digitalcommons.usu.edu/etd2023/281/) identifies a dedicated luminescence study, but its linked PDF returned HTTP 403. At that retrieval stage only repository metadata and abstract were inspected; the browser recovery below supersedes this access limitation.

[Collins et al. (2025), S143](https://cp.copernicus.org/articles/21/1359/2025/), sections 5.2-5.3, proposes glacial deposition, retreat, weathering, downslope flow, fluvial deposition and readvance. It leaves Unit 2's origin uncertain between interglacial snow/firn and remnant basal ice, and cites earlier dating for its time constraints. This is a process interpretation, not an independently established new clock.

The paper links [S144's sediment-characterization data package](https://doi.org/10.18739/A2QN5ZD22). Its public EML describes XRD, EDS, SEM and CT data. Our [access ledger](../data/camp-century-data-access.json) records downloaded metadata hashes and the public resource-map/index check: one indexed package member, the metadata itself. No measurement files were recovered through this package. System metadata marks it unarchived and supplies no successor identifier. This is a dated retrieval result, not proof that data are absent elsewhere; descriptive filenames are not downloaded data. It is also not a recovered substitute for the 2023 luminescence supplement.

Next obtain the thesis/full supplement or their authenticated public deposits, then link dated aliquots to core segments and reproduce dose, fading and residual corrections. Additional interpretations of the same core cannot substitute for those input checks or establish a global synchronous event.

## Recovered thesis: additional segments and resetting limits

The normal repository Download link subsequently delivered [Woznick (2024), S142](https://digitalcommons.usu.edu/etd2023/281/). Table 3.9 (printed p.65/PDF p.78), the results narrative (p.63/PDF p.76) and Table 3.2 (p.44/PDF p.57) were visually inspected. The [transcription](../data/camp-century-thesis-luminescence.json) records the PDF hash, measured fractions, aliquot counts, doses, fading rates and conflicting entries. Font warnings occurred during rendering, but the checked values and labels were legible.

| New upper segment | Sediment unit | Reported depth (cm) | Table age, ka (1 SE) | Narrative age, ka |
| --- | --- | --- | --- | --- |
| 1059-6 / USU-4162A | 5 | 29.5 | 417 +/- 37 | 417 +/- 37 |
| 1060-C1 / USU-4167A | 4 | 88.5 | 422 +/- 34 | 422 +/- 42 |
| 1060-C3 / USU-4169A | 3 | 108.5 | 414 +/- 34 | 414 +/- 38 |

These are additional spatial samples from the core, strengthening the evidence that the upper units have similar luminescence histories under the method's assumptions. They are not three independent laboratories: p.43 says the pilot and thesis samples used the same reader and conditions. The older 1059-4 and 1063-7 results are reproduced for comparison, not counted as new measurements.

The central ages' 414-422 ka spread is not an 8 kyr measured depositional duration. Errors span tens of thousands of years; shared systematic uncertainty and the narrative/table differences preclude an unqualified tighter pooled date. No new joint age or duration is calculated here.

For Unit 1, segment 1062-3 is reported saturated, with a >850 ka limit and a fading rate reused from USU-3505. Table 3.9 identifies it as USU-4183A; Table 3.2 assigns USU-4189A/B/C to that segment. Both are retained pending the laboratory crosswalk. Unit 2 sample 1061-D1 had no result at thesis completion; its date remains null. A saturated mineral signal is not an exact date for final sediment emplacement.

The discussion on p.72 explicitly allows incomplete bleaching and resulting age overestimates. It reports a 50 Gy residual correction for the pilot and a similar correction for thesis samples. This supports testing signal resetting rather than assuming that every transported grain began with zero stored dose. It does not demonstrate a recent burial date or quantify how much of the apparent age is inherited. A source's acknowledgement of an uncertainty is neither proof that it was fully corrected nor evidence of concealment.

Next reconstruct the sample-specific correction chain from dose-rate inputs, aliquot distributions and residual/fading calculations, resolving the lab identifiers first. The thesis narrows the former access gap and adds observations, but does not establish a common catastrophe across distant sites or a mechanism of historical fabrication.

## Dose-rate scenarios: a reproducible component sensitivity

Thesis Tables 3.4 and 3.8 (printed pp.47 and 62) were visually checked. The [scenario ledger](../data/camp-century-dose-scenarios.json) preserves four fine-fraction rows and their three alternatives: assumed internal potassium and water; measured potassium with assumed water; measured potassium and water. These alternatives must not be mistaken for four independent measurements or silently substituted into the final age table. A-only and A+B sample labels remain distinct.

At fixed equivalent dose, age is inversely proportional to dose rate. The [calculation](../analysis/camp_dose_sensitivity.py) and [results](../analysis/camp-dose-sensitivity-result.json) therefore isolate the consequence of changing each denominator, without claiming to rerun DRAC or correct an age:

| Table 3.8 label (53-150 micrometres) | Internal-K change alone | Water change alone | Both changes |
| --- | --- | --- | --- |
| USU-4162A+B | +1.68% | -5.06% | -3.46% |
| USU-4162A | +1.72% | -5.08% | -3.45% |
| USU-4167A | +0.59% | -3.53% | -2.96% |
| USU-4169A+B | +0.24% | +17.38% | +17.66% |

Percentages describe conditional age changes, not probabilities or corrected published dates. The water comparison holds measured internal potassium fixed. For 4169A+B, the source dose rates fall from 2.533 to 2.158 Gy/kyr; the corresponding fixed-dose age increases by 17.38%. The combined percentage is multiplicative, not the sum of the other two. Uncertainty and covariance have not been propagated. This establishes sensitivity to a documented input choice, not that the choice was wrong. Present/core water measurements also do not by themselves reconstruct moisture throughout burial.

Table 3.4 explicitly lists 20% water as used for 1059-6 and 1060-C1, and 42% for 1060-C3. Its role must be reconciled with Table 3.8's scenario columns and the final Table 3.9 rates. A nearest numerical match is insufficient evidence to choose a correction pipeline. The original DRAC inputs/outputs, aliquot dose-response and fading experiments, residual-dose estimates and their uncertainty propagation remain the next required records. No extra 50 Gy subtraction has been applied to values that may already contain that correction.

The same inspection narrows the lower-sample identity issue: Table 3.4 and Appendix I Table A.2 (p.96) both pair USU-4183A/B with 1062-3; the appendix pairs USU-4189A with 1063-5. This supports the age table's lab family within the thesis, but does not replace the original luminescence submission and aliquot records. The conflicting Table 3.2 entries remain visible.

## Original 2023 supplement recovered

The publisher's normal browser links delivered the [25-page methods PDF (S145)](https://www.science.org/doi/suppl/10.1126/science.ade4248/suppl_file/science.ade4248_sm.pdf) and [19 workbooks (S146)](https://www.science.org/doi/suppl/10.1126/science.ade4248/suppl_file/science.ade4248_data_s1_to_s19.zip). The [access ledger](../data/camp-century-data-access.json) records hashes for both downloads and every workbook. This supersedes earlier retrieval failures; full analysis remains pending.

Methods p.3, visually checked, explains that 95% of the isolated coarse fraction fell within 150-250 micrometres after initial 150-355 sieving. S1 footnote 7 and S10 footnote 5 agree. This explains the distinction between original and dominant grain sizes; it does not license changing all source labels. S1 reports 2.35 +/- 0.21 Gy/kyr for this fraction, versus 2.52 +/- 0.41 in the thesis pilot row. Keep the original-study and thesis values separate pending reconciliation.

The [residual-test transcription](../data/camp-century-residual-test.json) contains four S8 aliquots. Recomputing its actual mean and sampling-standard-error formulas yields **51.3623 +/- 5.0066 Gy**, matching workbook caches; the adopted correction is 50 Gy. See the [reproducible calculation](../analysis/camp_residual_check.py) and [result](../analysis/camp-residual-check-result.json). This is an experimental summary check, not replication of fading correction or final age uncertainty. The companion material's laboratory light exposure does not independently prove complete resetting during natural transport. Next trace S3-S5 and S11 through the final age calculation.

## Fading worksheet reproduction and dose-output crosswalk

The [S5 example inputs](../data/camp-century-fading-example.json) retain run, fraction, delays, doses and fading rates. A [Python implementation](../analysis/camp_fading_worksheet.py) reproduces all 30 cached correction factors across six temperature steps and five regenerative doses, within 1e-12. Its zero-fading boundary returns one. The [result](../analysis/camp-fading-worksheet-result.json) checks spreadsheet arithmetic, not physical calibration, dose-response fitting, every aliquot or final ages. The logarithm uses base 10 as in the workbook's Excel LOG expression.

The [S11 crosswalk](../data/camp-century-drac-crosswalk.json) exposes different stored values:

| Fraction, micrometres | Highlight rate +/- error, Gy/kyr | Detailed output rate +/- error, Gy/kyr |
| --- | --- | --- |
| 63-150 | 2.053 +/- 0.185 | 2.047 +/- 0.182 |
| 150-250 | 2.337 +/- 0.208 | 2.515 +/- 0.409 |
| 250-355 | 2.685 +/- 0.221 | Not populated |

S11 cells T17/U17 weight the two coarse highlight rows 95:5, yielding 2.3544 +/- 0.20865, consistent with S1's rounded 2.35 +/- 0.21. The error formula is a linear weighted sum; covariance has not been established. The detailed 150-250 output rounds to the thesis's 2.52 +/- 0.41. This numerical match narrows the provenance question but does not identify which processing version was intended. Full DRAC recalculation and the transition from corrected dose-response curves to pooled age/uncertainty remain necessary.

## Aliquot aggregation remains unresolved

The [250-degree aliquot transcription](../data/camp-century-aliquots-250.json) preserves all 44 S4 rows, including two fine-fraction values marked rejected. Rejection was decoded from cell styles matching the workbook's grey key, not inferred from numerical extremeness. It leaves 22 fine and 20 coarse accepted aliquots, consistent with S1. Summary cells contain stored numbers, not aggregation formulas.

An [exploratory calculation](../analysis/camp_aliquot_summary.py) compares two explicit rules against those stored summaries ([results](../analysis/camp-aliquot-summary-result.json)):

| Fraction, micrometres | Source weighted mean, Gy | Arithmetic mean, Gy | Inverse-variance mean, Gy |
| --- | --- | --- | --- |
| 63-150 | 940.4888 | 941.1402 | 912.7265 |
| 150-355 | 979.9092 | 981.2660 | 952.1009 |

The arithmetic means differ by less than 0.2% from the stored means, but do not reproduce them exactly. Inverse-variance weighting differs more and is not established as the source's rule. For the coarse fraction, the ordinary sampling SE (26.2351 Gy) reproduces the stored SE; for the fine fraction, it gives 23.5716 versus 24.9990 Gy. No replacement ages follow from this comparison. The actual weighting, accepted-input version, shared uncertainties and final pooling procedure must be identified before claiming complete reproduction or a scientific dating error.

## Central age chain and figure variant

Figure S1 (S145, PDF p.8) was visually inspected. It reports a fine-fraction corrected age of 435 +/- 39 ka, whereas S1 and the main text report 434 +/- 39 ka. The figure caption describes a radial plot but supplies no explicit aggregation rule.

Using the stored S4 dose summaries, the adopted 50 Gy residual and S11 rates, the [central-age calculation](../analysis/camp_age_chain.py) produces these [results](../analysis/camp-age-chain-result.json):

| Variant | Calculation, Gy divided by Gy/kyr | Result, ka | Rounded source value matched |
| --- | --- | --- | --- |
| Fine, highlight dose rate | (940.4888267 - 50) / 2.053 | 433.7500 | S1/main text: 434 |
| Fine, detailed dose rate | (940.4888267 - 50) / 2.047 | 435.0214 | Figure S1: 435 |
| Coarse, 95:5 mixture rate | (979.9092256 - 50) / 2.3544 | 394.9665 | S1/Figure S1: 395 |

This recovers the published fraction central values conditionally on stored intermediate results. It does not recover their uncertainty, the underlying weighted dose summaries or the pooled 416 +/- 38 ka result. The fine variants differ by about 1.27 ka, small compared with the reported 39 ka uncertainty; this discrepancy alone is not evidence of a materially different chronology. Matching rounded values is a reproducible explanation to investigate, not proof of the authors' processing history. Resolve the aggregation and uncertainty chain before promoting the component audit to full replication.

## Provenance: mineral formula mismatch

S146 Data S18 reports mineral abundance as percent area. Its row 5, labelled Amphi+Pyrox, contains formulas such as `SUM(B4,B35,B15)`. Those cells are labelled Albite, Pyrite and Calcite (low Mg), respectively. The same references occur in all six size/sample columns. The [dependency transcription](../data/camp-century-mineral-formulas.json) preserves formulas, labels and values; the [calculation](../analysis/camp_mineral_formula.py) reproduces all six cached sums.

As a diagnostic, summing the rows labelled Amphibole, CaFe-amphibole and Pyroxene gives different garnet-to-sum ratios ([results](../analysis/camp-mineral-formula-result.json)):

| Size, micrometres | Upper 1059-4: source formula / label-based ratio | Lower 1063-7: source formula / label-based ratio |
| --- | --- | --- |
| 0-63 | 0.161 / 1.808 | 0.064 / 0.654 |
| 63-125 | 0.137 / 0.977 | 0.038 / 0.272 |
| 125-250 | 0.103 / 0.999 | 0.035 / 0.270 |

The upper sample's ratio exceeds the lower sample's in every size class under both calculations. Thus this formula concern changes magnitudes but does not reverse that directional comparison. Original mineral classifications and the figure's aggregation must be checked before replacing published values or attributing an effect to the weathering interpretation. No cross-fraction pooling is justified without weights.

S16's five geochronology K-S p-values range from 0.100 to 0.918, and S19 reports mineralogy non-rejections. These are reported test outcomes, not proof of identical sources or a unique local origin. Similar source materials can occupy more than one location. The workbook concern does not establish distant transport, geographic upheaval or intentional misrepresentation. A transport reconstruction still needs source-terrain discrimination and mapped feasible paths, beyond comparisons between two core samples.
