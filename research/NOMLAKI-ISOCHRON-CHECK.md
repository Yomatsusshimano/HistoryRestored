# Nomlaki inverse-isochron fit: close numerical agreement, explicit limits

2026-10-09. C005/S327; declared analytical diagnostic, without independent scientific review.

The [original methods audit](NOMLAKI-DIRECT-DATING.md) retained all nine ROSER-2a heating steps and the author's five marked plateau steps. The new [script](../analysis/nomlaki2021_isochron.py) fits those five steps using the original reduced inverse-isotope ratios, percentage uncertainties and within-point error correlations. [Inputs and results](../data/nomlaki2021-isochron.json) preserve the source comparisons and two sensitivity variants.

## Model and calculation

Let x=39Ar/40Ar and y=36Ar/40Ar. Fit y=a+b*x with a latent true x for each observation. Minimize the summed squared Mahalanobis residuals using each point's fixed2x2covariance, including its reported correlation coefficient. This is a declared Gaussian measurement-error model, not a claim to have recovered the original author's software. Different heating steps are treated as independent points conditional on those covariances; unreported shared reduction errors are not reconstructed.

Three initial slopes converge to the same objective. A second implementation profiles out the intercept and latent positions, using variance sy²+b²sx²-2b*rho*sx*sy, and agrees with the fit. These are checks of the same numerical model, not independent measurements or scientific reviews. Parameter covariance uses the local linearized residual Jacobian, without reducing errors when MSWD is below one.

The trapped ratio is1/a; the radiogenic40Ar*/39Ar ratio is−b/a. Age is ln(1+J*ratio)/lambda. J=0.0002608 comes from the workbook; lambda=5.463e-10/year is declared explicitly, consistent with the Min convention named in S327 and the numerical constant documented in existing S210. The exact S327decay/reduction implementation remains unverified. All ages below are conditional on those inputs.

| Quantity | Five marked steps, this diagnostic | AppS1Figure4e report |
| --- | ---: | ---: |
| Trapped40Ar/36Ar |286.070565 ±5.846766 |286.1 ±5.8 |
| MSWD |0.125933 |0.13 |
| Chi-square upper-tail probability,3degrees of freedom |0.944789 |0.94 |
| Age |3.340204Ma |3.339Ma |
| Analytical standard error |0.015009Ma |0.015Ma |
| Analytical error plus sharedJ contribution |0.015700Ma | Main Table4text reports0.016Ma |

The intercept, scatter and analytical error reproduce the reported rounded values closely. The age differs by0.001204Ma, about1,204years. This is small relative to the quoted analytical error but remains a discrepancy. Adding the declared sharedJ error yields a value rounding to0.016Ma, which is compatible with the main table's larger error. It does not prove how that table was calculated. Monitor and decay-constant systematic errors are not fully propagated here.

At the fixed declared lambda, the nine published step ages imply almost the same J, about0.0002607192, when inverted through the age equation. That differs from the stored0.0002608. This is a consistency diagnostic derived from already calculated ages, **not a measured replacement J**. It is not used to adjust the fit. Original reduction settings and unrounded calibration records are needed to determine the cause; a changed constant, calibration or transcription cannot be selected by guesswork.

## Selection and error sensitivity

| Variant | Conditional age,Ma | Trapped ratio | MSWD | Chi-square upper-tail probability |
| --- | ---: | ---: | ---: | ---: |
| Five marked steps with reported correlations |3.340204 |286.070565 |0.125933 |0.944789 |
| Same five steps, correlations set to zero |3.339657 |286.196384 |0.138448 |0.937055 |
| All nine steps with reported correlations |3.333983 |296.093650 |3.946409 |0.000257 |

All nine measurements remain visible. Their combined fit has substantially more scatter than the declared error model expects. Therefore the full-set line is a sensitivity result, not an accepted replacement chronology. The local covariance errors stored for that variant are unscaled analytical diagnostics, not a complete uncertainty estimate for a poorly fitting model. The five-step agreement also does not justify deleting the other steps or establish a unique geological explanation for their disagreement. No historical age emerges in these variants.

## What this establishes for the wider investigation

The reported ancient age now has a substantially reproduced inverse-ratio fit behind it, with a small unresolved age-conversion discrepancy. It is stronger evidence than a regional age citation alone, and remains conditional on the reduced data, selected steps, model and calibration. Its probability describes scatter under that model; it is not the probability that the historical hypothesis is false.

This does not independently authenticate the crystals, primary ash emplacement, the Mohave tephra match or the southern Bouse target-bed correlation. It does not date a later deposit merely containing old crystals. Next recover the original calibration/reduction settings to close the numerical discrepancy, and compare the original chemical and emplacement evidence connecting Dry Creek to named regional ash samples. Preserve the [Willow Wash layer-identity problem](WILLOW-WASH-NOMLAKI.md) as a separate unresolved issue.
