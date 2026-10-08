# Ice-core corrections and independent checks

2026-10-08. C023 / S107. Sourced draft without independent review.

[Sigl and colleagues (2015)](https://doi.org/10.1038/nature14565), pp.544–545, reports ice-core isotope features placed seven years earlier than corresponding tree-ring markers on older timescales. Selected text and Figures 1–2 were visually inspected in the [institutional PDF mirror](https://www.whoi.edu/cms/files/sigl15nat_240284.pdf). The [structured ledger](../data/ice-core-anchor-audit.json) preserves the reported comparisons and marker roles; it contains no digitized concentration measurements.

Figure 2 identifies Greenland fixed markers at 536, 626, 775, 939 and 1258 CE. The authors also describe evaluating revised chronologies with historical observations, tephra and the 994 isotope event. The follow-up methods inspection below clarifies their reported separation from fitting; the underlying records remain unverified.

For this investigation, the key result is methodological. A marker used to assign an ice-layer date cannot then count as an independent confirmation of that assigned date. Independent measurement of different isotopes does not automatically mean independent calendar placement. Conversely, this dependency alone does not invalidate synchronization: a genuinely unused marker can test a model once its identity, uncertainty and exclusion from fitting are established.

This provides a concrete candidate for examining chronology disagreement under objective 10, without assuming a break affecting every historical record. It also supplies a traceable public correction process relevant to objective 16. Neither a global seven-year conversion nor a deliberate rewriting mechanism follows. Do not apply this correction to Bonneville, Electron, Seattle or fossil dates.

The [MacBlo audit](MACBLO-ANCHORS.md) already involves a tree-ring isotope-marker comparison. Counting that route and this ice-core route as entirely independent calendar confirmations would require auditing their shared reference chain first.

Next, retrieve the raw isotope series and documentary supplement. Reproduce the published model and its stated unused-marker checks. Because those markers and the paper's results are already known to us, reproduction would be retrospective, not a new successful forecast. We have not audited later replacements for this historical chronology or independently validated its precision.

## Follow-up: constraints and unused checks

Methods PDF p.9 and Extended Data Tables 2–3 (PDF pp.17–18) were visually inspected. The [ledger](../data/ice-core-anchor-audit.json) now includes all six Greenland marker rows from Table 2's lower panel, with separate depths and initial calendar estimates for the two cores. These estimates precede the second round of constraints; they must not be mistaken for final NS1-2011 dates. The estimated NEEM depth for the 775 marker is flagged.

The methods explicitly say the Tianchi tephra, second isotope event and pre-536 historical checks were excluded from chronology development. For the second isotope event, the ice increase is assigned to **993 CE**, compared with production between the 993 and 994 Northern Hemisphere growing seasons. The earlier 987-versus-994 comparison therefore must not be read as an exact seven-year correction to every final ice-layer label.

The reported historical check comprises 32 observations, with 24 matching ice events within ±3 years and eight unmatched. The authors report a Monte Carlo significance result, but we have not reproduced their selection or null model. Preserve the misses; neither treat 24 matches as 32 successes nor dismiss all checks as fitted anchors. Distinct observations can provide a useful test even though source authentication and model reproduction remain outstanding.

Table 3 identifies the historical works underlying the 536, 626 and 939 constraints. These are citations and translations inside this paper, not original manuscripts inspected by this investigation. A documentary audit must trace their dating and transmission before using them to adjudicate historical fabrication.

## Supplement recovered: window-count audit

[S108, historical supplement](https://www.whoi.edu/fileserver.do?id=240285&p=244409&pt=2), pp.9–10 and 13, was visually inspected. The [date/rank ledger](../data/ice-historical-validation.json) contains 32 rows: 24 classified Probable and eight Possible by the authors. Individual matched-event assignments remain null; aggregate counts cannot identify which rows missed.

The [denominator calculation](../analysis/ice_validation_windows.py) expands each printed date range by the specified margin, inclusively. Its [results](../analysis/ice-validation-windows-result.json) distinguish summed window years from unique calendar years. For all 32 rows, sums of 229, 165 and 101 reproduce the reported ±3, ±2 and ±1 totals. For the probable subset, 124 and 76 reproduce the ±2 and ±1 totals. At ±3, the sum is **172**, while the supplement reports **155**; the unique-year union is 138, so merely deduplicating overlap does not recover 155 either.

This is an unresolved denominator discrepancy under the explicit counting rule, not a demonstrated correction to the published statistic. Different input selection, implementation or reporting could explain it. Neither the six means nor their significance tests have been reproduced. Repeatedly counted overlapping years are also not independent observations; the simulation must preserve or otherwise account for its sampling structure. Obtain the original ice-event vector and exact sampling code before judging the effect on the result.

## Original workbooks recovered

Publisher-linked Supplementary Data 3 (S109, Greenland) and Data 5 (S110, reconstruction) are now downloaded and hash-recorded in the [acquisition ledger](../data/ice-workbook-acquisition.json). Read-only cell inspection found layer-counting inputs and the annual combined sulfur series. The latter has 2,498 rows, endpoints 1998.5 and −499.5, and 15 combined-column cells containing −9.999. Around the era boundary the labels are 1.5, −0.5 and −1.5; 0.5 is absent. We preserve these labels and sentinel values pending convention verification. This is cell inspection, not a newly rendered workbook or reproduced age model.

The concentration series does not itself identify every year classified as volcanic for the historical test. The reconstruction workbook also concerns a combined forcing product, so its event list must not silently replace the NEEM-specific validation input. Thresholds, event duration, multi-core combination and calendar conversion need explicit reconciliation first. The historical ledger's individual match assignments therefore remain unknown.

The Greenland README further states that TUNU2013 dates come from volcanic synchronization rather than annual-layer counting. It can contribute a separate measured chemical signal, but its assigned dates are not an independently counted chronology. This is a concrete dependency to preserve when assessing apparent agreement among cores.

## Boundary encoding checked against Figure 2 source data

The publisher's Figure 2 workbook (S111) supplies an integer BCE/CE column alongside sulfur values. A [six-row crosswalk](../data/ice-calendar-crosswalk.json) compares its rows for 3 CE through 3 BCE with S109. All five paired numerical concentrations agree within 0.0005 ppb, consistent with the three-decimal rounding in the annual combined column. The remaining row, 2 CE, is blank in the figure source and −9.999 in the annual workbook, corroborating missingness for that row.

The pairs map 1.5 to 1 CE and −0.5 to 1 BCE. Thus the missing 0.5 label is not evidence of a missing historical year: these displayed labels omit year zero. Direct subtraction across the era boundary would introduce an extra year. Convert signed historical years to a continuous astronomical index explicitly before any duration calculation; do not regard that conversion as independent dating evidence.

This resolves the selected boundary correspondence, not every calendar convention or missing cell throughout the workbooks. Source-data sheet headers still describe concentrations and tree responses rather than the binary event classification used for historical validation. A supplementary-guide download timed out; the event-selection rule and simulation code remain outstanding. No threshold was chosen to force the reported match count.

## Detection method traced to the earlier study

The guide download succeeded on retry (S112). It indexes the released tables but does not supply the required binary validation series. [Sigl and colleagues (2013), S113](https://doi.org/10.1029/2012JD018603), section 2.4, p.1154, was then visually inspected. It estimates background with a 31-year running median and detects annual sulfur values exceeding that background by three median absolute deviations. Deposition is calculated separately against a reduced background after detected peaks are removed. The authors describe empirical parameter selection checked against historical eruptions.

The [method ledger](../data/ice-event-method.json) separates those reported choices from implementation questions not resolved on the inspected page: the MAD calculation domain and scaling, edge handling, missing years, and event grouping. Detection and deposition baselines must not be conflated. This earlier method is now a concrete lead for reproduction, but its precise application to the revised 2015 validation series is unverified. Choosing among implementations because one reproduces 24 matches would be fitting to the answer, not independent reproduction.

## Executed sensitivity analysis

The [script](../analysis/ice_detection_sensitivity.py) checks the S109 workbook hash and runs four explicitly chosen implementations. All use centered 31-calendar-year windows and require complete input in each window. None interpolates gaps. Local MAD uses deviations from that window's median; global-residual MAD uses deviations about the median of all available full-window residuals in the supplied record. Each is evaluated unscaled and with a 1.4826 normal-consistency factor. These are retrospective analyst choices, not recovered author settings.

| MAD version | Flagged years, 258 BCE–504 CE | Historical matches within ±3 years | Nonmatches | Unresolved entries |
| --- | --- | --- | --- | --- |
| Local, unscaled | 71 | 20 | 8 | 4 |
| Local, scaled | 38 | 12 | 16 | 4 |
| Global residual, unscaled | 67 | 20 | 8 | 4 |
| Global residual, scaled | 42 | 14 | 14 | 4 |

The period has 762 calendar years. Our complete-window rule leaves 139 years unclassified in each version; flagged counts therefore are not complete event totals. The four unresolved historical entries are 125–124 BCE, 121 BCE, 90 BCE and 14 CE. Unresolved does not mean no eruption. The two unscaled versions permit 20–24 matching entries depending on those unknowns, so 20 observed matches do not contradict the reported 24. Nor does possible agreement establish reproduction.

[Full results](../analysis/ice-detection-sensitivity-result.json) retain every variant's row-level states for ±1, ±2 and ±3 years. They do not replace the original ledger's unknown author-match assignments. Four tests check calendar conversion, synthetic peak detection, propagation of missing data and three-state matching. They validate that limited code behavior, not the chronology or volcanic interpretation. No event grouping, deposition flux, chance-match probability or Monte Carlo significance was computed. Exact processing choices and gap treatment remain the next necessary evidence.

## The 14 CE historical entry: text before event assignment

[Dio 56.29.2-5, S114](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/56%2A.html) narrates solar obscuration, a fiery sky, falling embers and red comets among omens preceding Augustus's death. The year is introduced by the consuls Sextus Apuleius and Sextus Pompeius. Section 30.5 dates the death to August 19; that is not an observation date for the solar phenomenon. No observing location, duration or named eyewitness is supplied in the selected passage. This is inspection of a translated transcription, not a manuscript or authenticated contemporary observation.

The passage alone cannot distinguish volcanic haze, an astronomical eclipse, literary portent or a combination of traditions. Its omen setting does not prove invention; its solar wording does not establish an eruption. S108 already ranks the entry Possible and discusses both an eclipse objection and allegorical interpretation. We have not independently checked the astronomical exclusion or the additional accounts cited through Stothers (2002).

[Cary's introduction, S115](https://penelope.uchicago.edu/Thayer/E/Roman/Texts/Cassius_Dio/Introduction%2A.html), places Dio's life long after Augustus and describes manuscripts covering Book 56. It lists Marcianus 395, with losses, and later derivative witnesses. Thus exclusive transmission through epitomes must not be assumed. We have not inspected the relevant folio, Greek variants or a modern manuscript catalog; this remains an editor-reported transmission outline.

The [text audit ledger](../data/ice-historical-text-audit.json) preserves these unknowns. Textual ambiguity is separate from missing sulfur inputs that left this row unresolved in our sensitivity analysis. Neither resolves the other, and neither identifies the authors' original ice match. Next steps are Greek/apparatus inspection, witness tracing and an explicit astronomical comparison. No calendar shift or deliberate fabrication follows from this entry.
