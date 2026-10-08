# A published pulse alternative and its water budget

2026-10-08. C008 / S30–S31. Sourced draft; neither alternative nor conventional account is independently validated here.

[Shaw et al. (1999), institutional PDF](https://faculty.washington.edu/tswanson/302add/ESS%20Readings/Bretz.pdf), *The Channeled Scabland: Back to Bretz?*, Geology 27, 605–608. Relevant text inspected; the conclusions and numeric exponents on p. 608 were visually checked. Rendering reported font substitutions, but these numerals were legible. This is a published regional alternative, not evidence of a recent worldwide catastrophe.

## What the alternative actually proposes

The authors explain selected downstream rhythmites as pulses during one flood, invoking additional northern water sources. They interpret Ninemile sediment as centuries of lake deposition, decoupled from downstream beds. Their argument disputes subaerial-exposure interpretations using sedimentary structures and proposes a large subglacial reservoir. They expressly allow multiple floods in the wider Scabland history (pp. 605–608).

Their interpretation must be evaluated at the named sections; it cannot legitimately be expanded into a claim that every varve, every regional landform or all geological history formed in one event. The [Sanpoil audit](MISSOULA-STRATIGRAPHY.md) supplies additional observations for that comparison. Opposed currents and reworked sediment can occur in complicated floods, so their existence alone does not determine duration. The discriminating evidence is the complete stratigraphic context and independently tested time intervals.

## Reproducible conservation check

Page 608 prints a reservoir volume of order 100,000 km³, discharge about 1,000,000 m³/s at Wallula Gap, and duration about 100 days. The [input record](../data/missoula-pulse-budget.json), [calculation](../analysis/missoula_water_budget.py), and [results](../analysis/missoula-water-budget-result.json) preserve those values.

For the stated volume passing one section at constant discharge:

`duration = (100000 × 10^9 m³) / (10^6 m³/s) / 86400 = 1157.407 days`

This is about 11.57 times the printed duration. At the stated discharge, 100 days passes 8,640 km³; passing the stated volume in 100 days requires a mean discharge of approximately 11.574 million m³/s. A tenfold-discharge sensitivity gives 115.74 days. **That sensitivity is not a correction attributed to the authors.** No erratum resolving the printed combination was inspected.

The quantities are approximate, but they do not reconcile as printed under this constant-flow calculation. A hydrograph, stored volume, multiple outlets or an amended exponent might change the comparison; each would need evidence. A peak discharge is not automatically a sustained mean. This check identifies an internal constraint to resolve; it neither measures the reservoir nor settles the sedimentary interpretation.

## Contemporary challenge: incomplete retrieval

The [retrieved comment fragment](https://www.droyer.wescreates.wesleyan.edu/reply.pdf), PDF p. 2 / printed p. 573, contains the beginning of Komatsu et al. (2000), alongside unrelated correspondence. It reports a model with a 2,184 km³ input, peak discharge 17 million m³/s and Manning coefficient 0.1, and downstream inundation deficiencies under its assumptions. The fragment ends mid-comment; the continuation and author reply are not reviewed. Its reported numerical results were not reproduced.

A model's conditional water deficit does not independently verify the much larger reservoir proposed in 1999. The [later model audit](MISSOULA-MODEL-AUDIT.md) demonstrates why terrain, blockage geometry and sediment treatment must also be checked. These studies are not a clean independent vote count: they share field observations and citations.

## Next discriminating work

Retrieve the complete 2000 comments/replies and the original section logs. Compare actual bed boundaries, dike origins, exposure indicators and current directions using the same standards on both accounts. Date material associated with alleged exposure surfaces where possible, and specify preservation/detection expectations before treating an absent soil as evidence of continuous inundation. Test the proposed reservoir's volume, confinement and release route against mapped evidence. The 1986 USGS report download returned HTTP 403 this turn; its annuality arguments remain uninspected directly.
