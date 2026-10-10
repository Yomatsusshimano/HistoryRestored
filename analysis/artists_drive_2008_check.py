"""Declared five-oxide ratio diagnostic; not geological correlation validation."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'data/artists-drive-2008-crosswalk.json'
data = json.loads(path.read_text(encoding='utf-8'))
reference = data['rows'][0]['oxides']
indices = [0, 1, 2, 5, 6]
results = []
for row in data['rows'][1:]:
    value = sum(min(reference[i], row['oxides'][i]) /
                max(reference[i], row['oxides'][i]) for i in indices) / len(indices)
    match = round(value, 4) == row['reported_SC']
    assert match, row['sample']
    results.append({'sample': row['sample'], 'declared_ratio_mean': value,
                    'reported_SC': row['reported_SC'], 'rounded_match': match})
later = json.loads((ROOT / 'data/nomlaki-chemical-crosswalk.json').read_text(encoding='utf-8'))
later_values = later['S327_tableS4']['sample_raw_cells'][4:13]
earlier = next(row for row in data['rows'] if row['sample'] == 'FLV-119-WW')['oxides']
assert earlier == later_values
data['diagnostic'] = {'oxide_indices': indices, 'reference_sample': 'JRK-DV-39',
    'rule': 'Mean min/max concentration ratios for Si/Al/Fe/Ca/Ti oxides',
    'results': results, 'S327_all_nine_printed_values_equal': True,
    'physical_aliquot_identity_verified': False,
    'original_method_implementation_verified': False,
    'geological_correlation_validated': False}
path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Four rounded coefficients reproduced; nine-value crosswalk matches. No geological validation.')
