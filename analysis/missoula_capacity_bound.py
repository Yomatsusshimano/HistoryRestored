"""Conditional conservation bound; not a hydraulic simulation."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def capacity_bound(volume_km3, discharge_cap_m3_s, duration_days):
    if min(volume_km3, discharge_cap_m3_s, duration_days) <= 0:
        raise ValueError('Inputs must be positive')
    capacity = discharge_cap_m3_s * duration_days * 86400 / 1e9
    fraction = min(1.0, capacity / volume_km3)
    return {
        'maximum_volume_through_section_km3': capacity,
        'minimum_duration_for_whole_volume_days': volume_km3 * 1e9 / discharge_cap_m3_s / 86400,
        'maximum_fraction_through_section': fraction,
        'minimum_fraction_not_through_section_during_window': 1-fraction,
        'minimum_volume_not_through_section_during_window_km3': max(0.0, volume_km3-capacity),
    }

def main():
    source = ROOT/'data/missoula-pulse-budget.json'
    data = json.loads(source.read_text(encoding='utf-8'))
    result = {
        'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'source_id': data['source_id'],
        'assumption': 'Printed discharge is treated conditionally as an upper bound on nonnegative discharge through one section throughout the stated interval. Source does not establish this cap.',
        'derivation': 'Integral Q(t) dt <= Q_cap * T when 0 <= Q(t) <= Q_cap; pulses below the same cap cannot increase capacity.',
        'result': capacity_bound(data['printed_volume_km3'],data['printed_discharge_m3_s'],data['printed_duration_days']),
        'interpretation_limit': 'Nonpassed volume could be retained, routed elsewhere, or not released. No such partition is measured here. If discharge exceeds the assumed cap, this conditional bound does not apply.',
        'hydraulic_simulation': False,
        'scientific_validation': False,
    }
    (ROOT/'analysis/missoula-capacity-bound-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result['result'],indent=2))

if __name__ == '__main__': main()
