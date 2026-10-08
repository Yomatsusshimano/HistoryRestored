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
