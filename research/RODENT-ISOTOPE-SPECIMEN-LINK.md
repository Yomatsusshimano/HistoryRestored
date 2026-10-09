# Enamel isotope data linked to the early rat specimen

2026-10-09. S317/S36/S316; sourced draft without independent review. The [early-rat calibration audit](HAITI-RAT-CALIBRATION.md) left specimen-specific dietary evidence open. A primary supplement now supplies an exact museum-ID link, while leaving the radiocarbon offset unmeasured.

## Source and access

Cooke and Crowley's2018 *Deciphering the isotopic niches of now-extinct Hispaniolan rodents* has a publisher-hosted [supplement](https://doi.org/10.6084/m9.figshare.7209677.v1), resource DOI10.1080/02724634.2018.1510414. The Figshare API supplied the47450-byte DOCX and explicit CC BY4.0license. Its MD5 matches publisher metadata. The [unaltered original](../sources/originals/wildlife/rodent2018/ujvp_a_1510414_sm2027.docx) and [serialized API metadata](../sources/originals/wildlife/rodent2018/figshare-metadata.json) are preserved with original-author attribution.

The [extractor](../analysis/extract_rodent2018_supplement.py) reads exact OOXML cells. The [ledger](../data/rodent2018-isotope-crosswalk.json) retains all five tables and their locators. Table1S occupies four separate table objects:74tissue rows representing40museum identifiers. Table2S contains19modern rat molar-comparison records; those are not isotope measurements of the fossil rats. Main article full methods and rendered document pages were not inspected. The packaged DOCX renderer and LibreOffice were unavailable, so access is FULL_TEXT_PORTION. The original file was not reformatted or edited.

## Exact specimen join

All eight museum identifiers in the2022radiocarbon ledger have matching isotope rows. Case and whitespace normalization is used only for identifier matching: an original `Uf` spelling is retained in raw cells. Taxon labels are not used to force matches. Each accession link still requires independent physical identification to authenticate that the measured tissues came from the same animal.

| Museum ID |2022assay |2018enamel part |Carbon value, per mil |Oxygen value, per mil |
| --- | --- | --- | --- | --- |
| UF293844 | UCIAMS191028 | Whole | −12.1 | −2.4 |
| UF293847 | UCIAMS191029 | Tip | −12.9 | −3.0 |
| UF293847 | UCIAMS191029 | Base | −13.1 | −2.7 |

The article's [institutional abstract](https://pure.johnshopkins.edu/en/publications/deciphering-the-isotopic-niches-of-now-extinct-hispaniolan-rodent) identifies the tissue as incisor enamel. Per-mil units are explicit in the supplement; the isotope reference scale has not been independently recovered from the full methods and remains null. The table gives Rattussp. for both fossil accessions. Modern Rattusrattus and Rattusnorvegicus comparison records do not automatically resolve these fossils' species identities.

## What this changes

There is now published carbon-isotope information under the exact accession of the early rat, rather than only measurements on other animals at the same site. The2026discussion's broad absence-of-isotope-values statement therefore needs qualification: **enamel measurements exist; a collagen isotope measurement has not been recovered in this audit**. This is a source-scope correction, not proof of deliberate omission or a corrected date.

Enamel carbon and collagen carbon must remain different observables. An enamel value cannot be copied into a collagen field, compared directly with the2026collagen measurements as if the tissue were identical, or turned into a numerical dietary reservoir fraction without an appropriate model and baseline evidence. The reference scale, pretreatment, fractionation and relevant formation periods also need checking. No marine or freshwater correction is inferred solely from these values.

Tip/base values are subsamples, not separately dated animals. Table averages do not add independent isotope observations. Matching eight accessions also does not create eight new biological dates or establish contemporaneous cave deposition. None of the earlier radiocarbon inputs or the sloth mortality calculation has changed.

## Next discriminator

Recover the full2018methods, tooth-to-mandible accession records and any collagen-specific carbon/nitrogen measurements for UF293844, together with original laboratory certificates and exact calibration outputs. Those could test dietary bias while preserving the early date as adverse evidence. Site coordinates in the supplement are rounded locality labels with unspecified datum; they must not become precise death locations or transport paths. A common catastrophe, extinction mechanism, recovered geography and all twenty original outcomes remain unestablished.
