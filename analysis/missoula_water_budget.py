"""Constant-discharge consistency check, not a flood simulation."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def calculate(data):
    volume_m3 = data['printed_volume_km3'] * 10**9
    discharge = data['printed_discharge_m3_s']
    stated_seconds = data['printed_duration_days'] * 86400
    assert volume_m3 > 0 and discharge > 0 and stated_seconds > 0
    return {
        'input_sha256_canonical_json': hashlib.sha256(json.dumps(data, sort_keys=True, separators=(',', ':')).encode()).hexdigest(),
        'constant_discharge_duration_days': volume_m3 / discharge / 86400,
        'mean_discharge_required_for_printed_duration_m3_s': volume_m3 / stated_seconds,
        'volume_at_printed_discharge_and_duration_km3': discharge * stated_seconds / 10**9,
        'calculated_over_printed_duration': volume_m3 / discharge / stated_seconds,
        'sensitivity_10_times_printed_discharge_duration_days': volume_m3 / (10*discharge) / 86400,
        'assumptions': 'Whole stated volume passes the same section at constant discharge; no additional storage, inflow or losses. Sensitivity is not a source correction.',
        'hydraulic_simulation': False,
        'scientific_validation': False,
    }


if __name__ == '__main__':
    data = json.loads((ROOT/'data/missoula-pulse-budget.json').read_text(encoding='utf-8'))
    result = calculate(data)
    (ROOT/'analysis/missoula-water-budget-result.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(f'Constant-discharge duration: {result["constant_discharge_duration_days"]:.6f} days; not a modeled hydrograph.')
