"""Fixed-equivalent-dose sensitivity, not revised ages or DRAC replication."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def calculate(data):
    results = []
    for row in data['rows']:
        a, b, c = [pair[0] for pair in row['dose_rates_Gy_per_kyr']]
        assert min(a, b, c) > 0
        results.append({
            'lab_fraction_label': row['lab_fraction_label'],
            'K_only_age_change_percent': 100 * (a / b - 1),
            'water_only_age_change_percent': 100 * (b / c - 1),
            'combined_age_change_percent': 100 * (a / c - 1),
        })
    return {'source_id': data['source_id'],
            'formula': 'At fixed equivalent dose, age_new / age_old = dose_rate_old / dose_rate_new.',
            'scope': 'Central-value component sensitivity only; no uncertainty propagation, revised age or correction-chain replication.',
            'results': results}

if __name__ == '__main__':
    data = json.loads((ROOT / 'data/camp-century-dose-scenarios.json').read_text(encoding='utf-8'))
    result = calculate(data)
    (ROOT / 'analysis/camp-dose-sensitivity-result.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))
