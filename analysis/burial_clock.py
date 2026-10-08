"""Illustrative closed-burial calculation with the 2013 paper's constants.

Not a full exposure/burial model or an independent validation of fossil age.
Run from any directory; reads the transcribed SF-08-C-015 ratio.
"""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def elapsed_ma(initial_ratio, observed_ratio, half_life_26_ma, half_life_10_ma):
    if not 0 < observed_ratio <= initial_ratio:
        raise ValueError('Expected positive decreasing ratio')
    if not 0 < half_life_26_ma < half_life_10_ma:
        raise ValueError('26Al must decay faster in this example')
    difference = math.log(2) / half_life_26_ma - math.log(2) / half_life_10_ma
    return math.log(initial_ratio / observed_ratio) / difference

def main():
    audit = json.loads((ROOT / 'data/dating-records.json').read_text(encoding='utf-8'))
    sample = next(s for s in audit['samples'] if s['field_id'] == 'SF-08-C-015')
    initial = 6.75
    half_26, half_10 = 0.72, 1.38
    observed = sample['ratio_26Al_10Be_S4']
    difference = math.log(2) / half_26 - math.log(2) / half_10
    result = {
        'status': 'ILLUSTRATIVE_CONDITIONAL_CALCULATION',
        'source_id': 'S13',
        'parameter_locator': 'Supplementary methods section 3.1, page 11',
        'sample_locator': 'Table S4, page 10',
        'field_id': sample['field_id'],
        'inputs': {'assumed_initial_ratio': initial, 'observed_ratio': observed,
                   'half_life_26Al_Ma_as_used_in_paper': half_26,
                   'half_life_10Be_Ma_as_used_in_paper': half_10},
        'equation': 't = ln(R0/R) / (ln(2)/half26 - ln(2)/half10)',
        'calculated_duration_Ma': elapsed_ma(initial, observed, half_26, half_10),
        'ratio_after_1000_years_if_initial_is_6_75': initial * math.exp(-difference * 0.001),
        'initial_ratio_needed_for_observed_ratio_after_1000_years': observed * math.exp(difference * 0.001),
        'uncertainty_propagated': False,
        'assumptions': ['Initial ratio is set equal to the published surface production ratio.',
                        'No post-burial production, mixing, or additional exposure.',
                        'Paper-era half-lives, not a statement of current recommended constants.'],
        'does_not_establish': ['Initial exposure history', 'Complete shielding history',
                               'Fossil-death date', 'Date of later redeposition',
                               'A common catastrophe or historical rewriting']
    }
    path = ROOT / 'analysis/burial-clock-result.json'
    path.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps(result, indent=2))

if __name__ == '__main__':
    main()
