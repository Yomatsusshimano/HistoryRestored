# Near-contemporary financial reporting: original printed conflicts

Research draft, 2026-10-11. S351; C006. No independent review.

Alfred Neymarck's *Ce que la France a gagné à l'exposition de 1889*, Journal de la société statistique de Paris 31 (1890), pp79-96, contains an Eiffel financial summary with several internal arithmetic conflicts. The [NUMDAM original PDF](https://www.numdam.org/item/JSFS_1890__31__79_0.pdf) was acquired through normal HTTPS. The digital wrapper and original printed pp79, 88 and 89 were rendered and visually inspected; the remainder was not visually audited. The tower identification and disputed digits are on the original page, not inferred from search text or OCR.

## What the original reports

Page89 attributes the cost breakdown to an administration-supplied document without identifying its date or archival reference. Eleven entries sum exactly to its printed **7,514,094.69 francs**. This does not establish the underlying document, cost scope or actual payments. The footnote mentions a de Foville lecture in a January issue of Journal des économistes, without stating the year; it does not identify an original financial ledger. Page79 reports a communication delivered on19November, with no year in that footnote. We retain the hosted1890 publication year without inventing a precise delivery date.

| Printed assertion on p89 | Calculation from printed operands | Difference: printed minus calculated |
| --- | ---: | ---: |
| Initial estimate7,233,384 plus increase280,716 equals cost7,514,094.69 | Actual increase280,710.69 | +5.31 francs in stated increase |
| Capital5,500,000;10,100shares at500 | 5,050,000 | +450,000 francs |
|20,200titles at approximately400, valued8,200,000 | 8,080,000 | +120,000 francs |
| Founder10,100titles at400, valued4,400,000 | 4,040,000 | +360,000 francs |

The approximately400-franc quotation limits interpretation of the combined market valuation. The founder paragraph explicitly multiplies by400. These mismatches do not identify whether errors arose in reporting, composition, rounding or upstream records. No corrected values are silently substituted into the source's claims.

## Comparison with other accounts

The capital/share figures conflict with S17's reproduced statutes and S350's yearbook allocation:10,200shares at500 gives5,100,000, including contributed operating rights. See the [capital audit](EIFFEL-COMPANY-CAPITAL.md). S351 does not preserve that rights-versus-cash distinction. A separate publication is not independent transaction evidence when the underlying administration/company disclosures remain unknown.

S351 reports6,459,584.20francs of gross receipts for15May–5November. S17's audited summary is6,523,847.40, a difference of64,263.20. S17 combines differently treated categories, including souvenir margin and ticket receipts after an exhibition share. The period and accounting boundaries have not been matched. The difference must not be labeled missing money or equated with the64,046-franc exhibition share.

The page asserts capital repayment and discusses market values. No repayment schedule, coupons, bank entries or original resolutions accompany this statement. It cannot close the outstanding repayment test.

## Evidence needed next

Locate the administration-supplied breakdown and the cited de Foville publication; compare category definitions, dates and capital figures against original company records. Preserve S351 as evidence of what a near-contemporary author published, with its arithmetic defects. It neither authenticates every financial claim nor proves inherited construction, fabrication or a catastrophe. All twenty objectives remain active.

The [transcription ledger](../data/eiffel-1890-statistical-report.json) preserves all eleven cost rows, source hash, inspected-page limits and calculated differences. Run `python analysis/eiffel_1890_report_audit.py` to reproduce the internal arithmetic. The PDF is linked rather than redistributed; its wrapper states reproduction conditions and reserved rights.
