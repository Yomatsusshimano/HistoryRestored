# Colorado River burial dating: an independent measurement route

SOURCED_DRAFT, 2026-10-08. No independent review or reproduced isochron fit.

[Seong et al., S216](https://doi.org/10.18814/epiiugs/2024/024015) uses cosmogenic10Be–26Al burial dating on22 cobbles. The13-page [publisher PDF](https://pdf.medrang.co.kr/IUGS/2025/048/IUGS048-01-51.pdf) was recovered (SHA256 `144a94d32e26d41796c07f97e1b8976fcba5c5dd4285eda7de81e02f7781142c`). Online publication was2024-07-01; the issue is Episodes48(1),2025. Table2/printed57 was visually inspected; selected methods/results were text-read.

## Preserve source differences before fitting

| Site | Table2 age±1σ, Ma | Nearby prose/abstract age±1σ, Ma | Retained/total |
|---|---|---|---|
|Topock|2.02±0.24|2.12±0.26|4/6|
|Bat Cave|2.08±0.31|2.05±0.31|4/5|
|Santa Fe Railway|4.25±0.68|4.37±0.71|6/6|
|Palo Verde|3.03±0.26|3.03±0.26|3/5|

Table2 excludesTPK001/004, BC009 andPVD020/021 because their reported ratios exceed6.75. Its aluminium concentration header reads27Al although its title and ratio concern26Al. All22 rows and both age versions are preserved in [structured records](../data/colorado-burial-rows.json). Numeric concentration quotients correspond to the listed ratios, but that is not authority to silently change the isotope header.

The method assumes source-basin steady-state erosion, rapid transport and common post-burial history among cobbles at equal depth. Those assumptions and post-burial production matter to the fitted ages.

## Relevance to the catastrophe test

This is a different measurement route from zircon or sanidine crystallization dating. It targets burial history through cosmogenic nuclide concentrations, so it can address a gap left by inherited mineral ages. It is not automatically an independent confirmation of every regional age: some authors overlap with the earlier studies, geological unit assignments share previous mapping, and the model has physical assumptions to test. Distinct measurements, shared interpretation and independent replication are different properties.

The published million-year burial results, if their sample contexts and model hold, challenge a recent single-burial interpretation for these sampled deposits. A hypothesis of recent movement of previously buried cobbles must instead specify whether that process could preserve the observed inter-cobble relationship, shielding history and sedimentary context. Merely observing that a cobble can be reworked does not reproduce those measurements; merely obtaining a linear fit would not prove a unique burial history either.

The three table/prose differences are reproducibility issues, not demonstrated fraud or evidence for a young chronology. Neither version will be silently selected as the correct one. The source's exclusions also require explicit sensitivity analysis, especially where only three points remain. They must not disappear from the public record.

Next trace Figure4 slopes, correction equations, concentration errors and covariance; reproduce both retained-sample fits and declared exclusion sensitivity; then evaluate each site's burial context. No regressions, original AMS validation, historical-age rejection probability or global-event model are claimed in this first audit.


## Figure and equation check

S216 printed56/PDF6 and Fig4 printed59/PDF9 were visually inspected. Figure4 agrees with the prose for Topock, Bat Cave and Santa Fe, but gives **Palo Verde3.04±0.34Ma**, versus3.03±0.26 in both table and prose. Thus all four sites now have a documented age-summary difference somewhere in the paper. The figure describes a Bayesian fit using100,000 simulations, retained points, propagated measurement/production uncertainty and an erosion-corrected initial ratio. Those implementation details have not been reproduced.

Equation5 prints `t = tau ln(Rm/Rinh)`, with tau positive at approximately2.07Ma. Every plotted slope is below the stated nominal initial ratio6.75, so literal substitution gives a negative age. From `Rm = Rinh exp(-t/tau)`, algebra instead gives `t = tau ln(Rinh/Rm)`. This identifies a sign/ratio-order inconsistency in the printed equation, not proof that the unpublished calculation used the wrong sign.

| Site | Figure slope | Literal printed equation, Ma | Decay-consistent nominal calculation, Ma |
|---|---:|---:|---:|
|Topock|2.39|−2.149|2.149|
|Bat Cave|2.47|−2.081|2.081|
|Santa Fe Railway|0.79|−4.441|4.441|
|Palo Verde|1.63|−2.941|2.941|

[The script](../analysis/check_burial_slope_ages.py) and [output](../data/burial-slope-age-check.json) preserve both calculations. These use rounded slopes, approximate tau and a fixed6.75 initial ratio; they intentionally do not pretend to reproduce the erosion correction or Bayesian fit. Their differences from reported ages must not be called failed reproductions of an algorithm that has not been recovered.

For diagnosis only, solving the decay-consistent relation backward from the figure ages yields implied initial ratios6.656,6.650,6.523 and7.079 respectively. Those numbers are algebraically fitted to the published answers. They are not independent estimates of source erosion or validation of any correction. In particular, the Palo Verde value merits checking against the actual correction parameters rather than silently selecting a different age version to make it fit.

The physically meaningful audit remains open: recover the MATLAB implementation, priors and post-burial/erosion corrections, reproduce Figure4 from the22 preserved measurements, then examine exclusion sensitivity and field histories. Documentation discrepancies narrow the reproducibility task; they do not by themselves establish a different burial time or historical catastrophe.


## Exclusion sensitivity: point cutoff versus uncertainty

The source excludes five points because their measured ratios exceed6.75. We tested that rule against the published errors without changing the source selection. For each point define `D = N26 - 6.75*N10`. With measurement covariance set to zero, `sigma_D = sqrt(sigma26² + 6.75²*sigma10²)`. This uses the aluminium column as26Al conditionally, preserving its printed-header warning.

| Excluded sample | D/sigma_D, fixed6.75 | Including a3% initial-ratio uncertainty term |
|---|---:|---:|
|TPK001|4.56|4.41|
|TPK004|2.88|2.62|
|BC009|4.84|4.69|
|PVD020|2.74|2.43|
|PVD021|0.49|0.47|

PVD021 is not well separated from the cutoff under these assumptions: the threshold lies within one propagated measurement standard deviation. That is a reason to examine the exclusion's effect, not proof that the grain shares the modeled history. The other four are farther above the cutoff. These scaled residuals are not calibrated rejection probabilities; covariance and full analytical error structure remain unknown. The3% production-ratio term is shared model uncertainty, not five independent additional measurements.

For a transparent sensitivity diagnostic, we fitted `N26 = intercept + slope*N10` using inverse aluminium-error variance weights. The Palo Verde source-retained three points yield slope1.63558. Restoring PVD021 gives1.42366; including all five gives2.29957. [Code](../analysis/check_burial_exclusions.py) and [results](../data/burial-exclusion-check.json) retain every membership choice.

These are deliberately limited weighted least-squares calculations: they treat10Be as exact and omit covariance, Bayesian priors, erosion correction and full post-burial modeling. The three-point slope's proximity to the published1.63 is a useful arithmetic comparison, not replication of the authors' method. No ages are inferred from these diagnostic slopes. The membership choices materially change the slope, so a robust age assessment must carry the selection alternatives through the complete model rather than report only the retained fit.

Next prioritize recovery of the original fitting implementation and the sample-specific reason for rejecting PVD021 beyond its central ratio. Keep physically different histories and analytical uncertainty as separate possible explanations until tested.


## Software lineage and two different exclusion rules

S216's acknowledgements credit Greg Balco and Lydia Staisch for MATLAB code; its methods cite Balco–Rovey2008 and Bender et al.2016. We inspected the latter's [publisher methods and availability statement, S217](https://doi.org/10.1002/2015JB012303) as web text. Bender describes100,000 candidate lines, Gaussian x/y measurement errors, slope bounds0–6.75, and using the posterior slope mode. Its exclusion rule is more than2σ departure from that fitted line. Scripts and inputs were offered on request; they were not recovered in this search. S216's exact combined implementation remains uninspected. No author was contacted.

A bound on fitted slope and a cutoff on each point's ratio are mathematically different. For a line `y = m*x + b`, the individual ratio is `y/x = m + b/x`. Thus a positive intercept permits an individual ratio above6.75 while the slope remains below6.75. For example, a deliberately synthetic point with x=30,000, m=2 and b=200,000 has y=260,000 and y/x=8.67. It lies exactly on the specified line. It is not a Colorado measurement, physical burial reconstruction or demonstrated explanation of any excluded sample.

This algebra matters because S216's method includes a common post-burial contribution rather than forcing the line through the origin. The nominal production ratio alone therefore does not prove that every higher measured ratio is incompatible with every common-history isochron. A physically constrained model of intercept, production and shielding might still reject particular points; that requires the model and data, not just a comparison of a central ratio with6.75.

The predecessor's rule must not be substituted silently for the later paper's stated procedure. Its priors, posterior summary and rejection threshold are useful lineage evidence, but citation does not prove that S216 inherited every setting. Our next reconstruction should explicitly compare the published ratio-screened membership against an all-point, errors-in-both-variables fit with declared priors and residual checks. Any replacement implementation must be labeled independently specified until checked against original code and inputs. Other publicly searchable burial packages are not established copies of the program used here.

## Independent fit with uncertainty in both isotopes

We now fit the preserved Table2 measurements with an explicitly specified **profile chi-square diagnostic**, keeping all source exclusions visible. [Python code](../analysis/fit_burial_eiv.py) uses only the standard library; [complete results](../data/burial-eiv-fit.json) include membership, intercepts and signed residuals. The aluminium header discrepancy remains: use as26Al is conditional.

Let x and y be the reported10Be and aluminium concentrations, with errors sx and sy. Assume independent Gaussian measurement errors, zero covariance and a straight relationship with no intrinsic scatter. Minimizing over each unknown true x coordinate gives

`Q(m,b) = sum[(y - m*x - b)^2 / (sy^2 + m^2*sx^2)]`.

At each slope, the intercept is the weighted mean of `y-m*x`. This profiles the latent coordinates; it does **not** integrate them out. Accordingly it is not the marginalized likelihood with a log-variance term, a Bayesian posterior, or a reproduction of the original MATLAB calculation. The declared slope range is0–6.75, motivated by the predecessor's reported range but not asserted to reproduce S216's settings. Intercepts are unconstrained. All fitted slopes are interior and all intercepts positive; this alone does not establish physically feasible shielding or post-burial production.

| Site / membership | n | Fitted slope | Intercept, atoms/g | Q/(n−2) |
|---|---:|---:|---:|---:|
| Topock, source retained |4|2.392369|118329|7.791|
| Topock, all measured |6|1.971779|171351|21.188|
| Bat Cave, source retained |4|2.472629|69973|2.812|
| Bat Cave, all measured |5|2.048330|104855|19.629|
| Santa Fe Railway, all six retained |6|0.797257|219080|9.413|
| Palo Verde, source retained |3|1.651889|256915|1.011|
| Palo Verde, restore PVD021 |4|1.424877|271869|1.038|
| Palo Verde, all measured |5|2.591745|206735|11.917|

The retained Topock and Bat Cave slopes round to the published2.39 and2.47. Santa Fe rounds to0.80 versus printed0.79, and Palo Verde to1.65 versus1.63. Approximate numerical agreement is informative but cannot identify an unrecovered algorithm or reproduce its uncertainty interval.

Restoring PVD021 changes the Palo Verde slope by about14% while Q/(n−2) remains near1. Its signed normalized residual in that four-point fit is about1.00. Adding PVD020 as well increases scatter substantially; its residual in the five-point fit is about5.55. Thus these two exclusions do not have equivalent effects in this diagnostic. No point is newly rejected here, and neither fit establishes which cobbles share a burial history.

The retained Topock and Santa Fe sets already scatter more than this measurement-only line model would suggest. For example, TPK006 has normalized residual−3.43 in the retained Topock fit, and CHM018 has+4.36 at Santa Fe. These are fitted residuals, not independently calibrated standard-normal test statistics. Q/(n−2) is descriptive here: we do not assign p-values, apply iterative clipping, or claim that any single residual disproves the complete source model. Unknown covariance, systematic errors, extra scatter, differing histories and transcription/analytical issues need separate investigation.

The optimizer checks both slope endpoints and refines every grid-local minimum found in4096 intervals. Doubling to8192 changes the fitted slopes by less than6.2e−8. A noisy equal-error synthetic dataset matches an independent closed-form Deming regression within1e−6, and an exact synthetic line is recovered. These checks support the numerical implementation, not the geological assumptions or a global chronology.

No diagnostic slope is converted into a new age. Source erosion, full post-burial production, shared errors, sample history and the original posterior calculation remain unresolved. Next inspect the original sampling sections and burial-depth histories, particularly whether the common-history assumption can explain the retained scatter and the selective effect of PVD021. This directly tests whether a date of prior burial can be transferred to the deposition episode relevant to the catastrophe hypothesis.

## Field context and the event actually dated

We inspected Table1 and Figures2–3 visually in the publisher PDF (printed55,54,58), and read the site descriptions, sampling methods and discussion at54–60. [Structured field-context records](../data/colorado-burial-context.json) preserve all22 sample IDs, lithologies and four reported locations. This is inspection of published evidence, not a field visit.

| Site | Reported depth below terrace tread | Elevation as printed | Published context |
|---|---:|---:|---|
|Topock|8.50m|159m asl|Natural exposure of paleochannel conglomerate|
|Bat Cave|7.23m|148m asl|Artificial cut in correlated boulder conglomerate|
|Santa Fe Railway|8.23m|187m asl|Middle of a unit with reported upward-fanning dips and underlying sandstone|
|Palo Verde|6.50m|151m asl|Possibly artificial cut; terrace/deposit relationship discussed as uncertain|

Table1 lists density2.0g/cm³ for every sample. Its density superscript lacks an explanation on the inspected table page, so measured versus assumed status remains unknown. The depth footnote mentions10cm for each subsample despite site depths of650–850cm; the relation of that statement to the actual calculation is unresolved. Longitude values are positive under an east header despite the southwestern US setting. We retain the printed values and flag the discrepancy; we do not map them as verified coordinates. The coordinate datum was not established.

Figure3 shows the exposures and marks sampled gravel intervals with boxes. It supports the authors' reported sampling in gravel rather than a directly sampled widespread mud layer. It does not resolve each cobble's position, historical overburden, cut age or lateral shielding. Equal current depth is useful sampling control but cannot by itself prove equal shielding through time.

**Palo Verde has an explicitly unresolved landscape history in the source itself.** The authors compare relatively weak carbonate-soil development with older fan soils and question how terrace forms relate to their burial age. Discussion at59–60 considers an old channel deposit subsequently reburied and recently exhumed, or terrace landforms younger than the deposit. They propose U-series dating of carbonate coatings on clast undersides as a test; no new coating dates are reported in the inspected passage. An age of coating growth would itself need attachment and stratigraphic context before it could bracket deposition or exposure.

Figure2 is a diagrammatic regional synthesis whose caption explicitly says the Palo Verde–Santa Fe Railway relationship is not observed. Its drawn arrangement must not be promoted into measured direct superposition. At Santa Fe, the cotton-rat fossils discussed as an alternative age correlation come from a nearby lower subunit; resemblance in tooth size is not an independent numerical date on these cobbles. The source uses its burial result to favor one correlation, so the resulting fossil-age assignment cannot then independently validate that same result.

Topock and Bat Cave were sampled to discriminate between competing field interpretations: younger conglomerate inset into Bullhead deposits versus membership in the Bullhead unit. Possible included Bullhead clasts are reported from earlier field work. The paper favors a younger unit and entertains a single flood for that conglomerate. That is a scoped regional flood interpretation; it does not correlate every sampled unit, wildlife assemblage or historical anomaly with the same event.

The source also offers analytical or inherited-history explanations for high ratios, including uncertainty in natural aluminium measurement and rapid elevation changes before transport. It does not provide a demonstrated sample-specific cause for PVD021. Reported low10Be blank-correction concerns include both excluded BC009 and retained BC010, another reason to seek original laboratory error records instead of treating membership as a clean quality division.

For the catastrophe test, distinguish initial burial, subsequent reburial, terrace formation and final exposure. The million-year interpretation challenges recent **first burial** under the stated model. It does not, by itself, rule out later movement or landscape modification. Conversely, the paper's acknowledgment of possible exhumation does not demonstrate a recent flood, worldwide upheaval or fabricated chronology. A proposed later event must independently predict mapped contacts, sediment provenance and transport, exposure history and an event-specific bracket.

Next recover the cited local mapping and any subsequent carbonate-coating dates; seek actual overburden/exposure histories before attempting physical intercept or reburial calculations. No shielding history is filled in from present depth alone.

## Mapping coverage and citation lineage

The cited [Castle Rock map, S218](https://doi.org/10.3133/sim3411) covers34°30′–34°37′30″N, from selected marginal text in the [author-uploaded map](https://www.researchgate.net/publication/329352022_Geologic_map_of_the_Castle_Rock_75%27_quadrangle_Arizona_and_California). All four S216 sample latitudes fall outside that interval. It provides regional context, not direct mapped contacts at those exposures. This latitude comparison requires no correction of S216's longitude header. Map graphics and the accompanying pamphlet remain uninspected after USGS access errors.

S216's bibliography has2018 and2019 Castle Rock entries with the same SIM3411 identifier and DOI. They are not two independent mapping confirmations. Also, a passage about incomplete Palo Verde mapping on the ResearchGate page belongs to a2019 citing article, not the map itself; it must not be attributed to the2018 document.

Bounded searches pairing Palo Verde alluvium with U-series, carbonate dating and coatings found no new date linked to PVD019–023. This is a search limit, not evidence that no such measurements exist. House2016 and mapping that actually covers the sampled exposure remain the next targets.

## Topock: a relative sequence to test

[S219, the original Topock map pamphlet](https://pubs.usgs.gov/sim/3236/sim3236_pamphlet.pdf), printed25, was recoverable here only as an indexed search excerpt. It reports sandstone/conglomerate (Trbs) blocks inside the inset Bat Cave boulder conglomerate (Trbb), and later incision associated with the Chemehuevi Formation. The authors interpret erosion, deposition, then erosion again. They also propose a single flood for Trbb from its thickness and lack of internal bedding. These are compatible statements about different scopes.

Incorporated older sediment blocks would support recycling and relative ordering if confirmed at the relevant contacts. They do not by themselves measure the intervals between events. A rapid-event alternative must explain the nested geometry and material transfer; the geometry alone cannot supply a million-year duration. Neither a global flood nor a recent age follows from the proposed single local flood.

Extracted map margins span34.625–34.75°N. Topock and Bat Cave sample latitudes fall within that range. Santa Fe's printed34.750047°N lies just north of the nominal boundary; coordinate uncertainty and neighboring coverage require checking before assigning a mapped polygon. Palo Verde is outside. Longitude interpretation remains conditional on resolving S216's header.

Map graphics, pamphlet photographs and exact sample-to-contact links remain uninspected after download and screenshot failures. Next obtain those observations before treating this relative sequence as independently verified field evidence.

## Full pamphlet recovered: contact and provenance limits

Follow-up recovered the original USGS pamphlet using a standard browser-style request. SHA256: `97a1b85d78a3765b11bf792ea0bf756a5c437f5154b6538ed19cf7147f75fcdf`. Figures15–16 (printed26–27/PDF30–31) were rendered and visually inspected; printed25–27,31 and selected unit descriptions41–42 were text-read. This supersedes the pamphlet access gap above, while map-sheet geometry and specimen-to-contact linkage remain open.

Figure16 shows a coarse conglomerate above a contrasting finer red substrate, with a marked contact and tool for scale. Its caption identifies **Trbb over Tcgn (Miocene gneiss-clast conglomerate)**,1.8km east-southeast of Topock. It is not a photograph of Trbb over Trbs sandstone, nor is it identified as the later isotope collection site. The separate Trbs-block observation has a more specific locator in the unit description: NW quarter of NW quarter of SE quarter, section1, T15N, R21W (printed41). That location is now a concrete target for matching field evidence, not a verified sample match.

Figure15 labels more tilted middle Santa Fe beds (Trbfm), a less-deformed upper conglomerate (Trbfu), and the overlying piedmont unit (QTa1). The photograph and caption support distinct attitudes and contacts. The authors interpret progressive deformation; neither this image nor its labels alone determine elapsed time. The descriptions report paleosols in Trbfm and a carbonate soil above Trbfu. Those are potentially useful tests of intervening exposure, but their origin, intactness and formation times require their own evidence.

Crucially, printed41 explicitly says the inferred younger position of Trbb relative to Santa Fe has **no observed direct stratigraphic relation**; its relation to QTa1 is also unobserved. Preserve those gaps when reconstructing the sequence. Reported regional ordering must not turn into an invented continuous measured section.

Printed26 describes a mixed provenance: many boulders have plausible nearby sources, while quartzite records much longer river transport. This concerns the deposit as a whole, not proof that the selected quartz-rich dated cobbles violate or satisfy a shared pre-burial model. Petrographic/source assignment must be tied to sample IDs before that assumption can be tested.

The paleontology discussion (printed31) adds a separate warning for wildlife correlation: a reported mammoth tooth came from in or near mapped artificial fill beside the railway bridge, leaving its original stratigraphic context unknown. It cannot independently date the conglomerate or demonstrate contemporaneous mortality. A reported equine rib in Trbb is a different occurrence, not an interchangeable age marker; no direct bone date is supplied in the inspected passage.

Next match the section1 sandstone-block locality and the dated sample coordinates, recover the original fossil collection records, and examine the reported paleosols before inferring either a single rapid sequence or long intervening exposure. Publication of photographs improves access to evidence; it does not replace these remaining tests.
