"""Retrospective arithmetic and conditional mixing audit, not a redating."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def conventional_age(fm):
    if fm <= 0:
        raise ValueError('Fraction modern must be positive')
    return -8033 * math.log(fm)

def required_fraction(observed, original, contaminant):
    if contaminant == original:
        raise ValueError('Identical endmembers cannot identify a mixture')
    return (observed - original) / (contaminant - original)

def main():
    path = ROOT / 'data/campo-laborde-assays.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    parsed = {}
    rows = []
    for row in data['assays']:
        fm, sd = map(float, row['fraction_modern_as_printed'].split(' ± '))
        age, age_sd = map(float, row['radiocarbon_age_1SD_BP_as_printed'].replace(',', '').split(' ± '))
        parsed[row['lab_id']] = fm
        rows.append(dict(lab_id=row['lab_id'], fraction_modern=fm,
            fraction_modern_sd=sd, published_age_BP=age, published_sd_BP=age_sd,
            age_from_printed_fraction_BP=conventional_age(fm),
            first_order_sd_from_fraction_BP=8033*sd/fm,
            derived_minus_published_BP=conventional_age(fm)-age))
    original = parsed['CAMS-171852']
    observed = parsed['AA-71665']
    mixes = []
    for label, contaminant in [('Illustrative Fm=1 endmember', 1.0)] + [
        (i, parsed[i]) for i in ['CAMS-171873','CAMS-171875','CAMS-171874']]:
        fraction = required_fraction(observed, original, contaminant)
        mixes.append(dict(contaminant_scenario=label, contaminant_fraction_modern=contaminant,
            required_fraction_of_mixture_carbon=fraction,
            central_value_between_zero_and_one=0 <= fraction <= 1,
            reconstructed_fraction_modern=(1-fraction)*original+fraction*contaminant))
    result = dict(case_id='C022', source_ids=['S104','S133'],
        input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        formula='Conventional age = -8033 ln(Fm); first-order SD = 8033 SD(Fm)/Fm',
        arithmetic_limits='Assumes printed Fm is conventionally corrected. Derived age and published age are transformations of the same measurement, not independent observations. Differences are not statistical significance tests.',
        arithmetic=rows, mixing=mixes,
        mixing_assumptions='Fm_observed=(1-f)*Fm_original+f*Fm_contaminant. Assumes comparable normalization and linear carbon mixing. Original endmember is assumed equal to CAMS-171852; later extracted fractions are illustrative endmembers, not measured contamination of AA-71665.',
        mixing_limits='Central-value scenarios only; no uncertainty distribution, isotope-fractionation mixture correction, blank correction, extraction yield or contaminant mass in the original aliquot established. Dated carbon masses are not a complete fraction-yield balance. No calendar calibration or new specimen age.')
    out = ROOT/'analysis/campo-fraction-check-result.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__ == '__main__': main()
