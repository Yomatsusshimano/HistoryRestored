"""Check published outer date bounds; not a calibration or statistical rejection."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
rows = json.loads((root / 'data/roopkund-dating-audit.json').read_text(encoding='utf-8'))['samples']
assert len(rows) == 37 and len({r['field_id'] for r in rows}) == 37

def check(selected):
    lo = max(selected, key=lambda r: r['calibrated_outer_low_CE'])
    hi = min(selected, key=lambda r: r['calibrated_outer_high_CE'])
    gap = max(0, lo['calibrated_outer_low_CE'] - hi['calibrated_outer_high_CE'])
    return {
        'samples': len(selected),
        'latest_lower_bound_CE': lo['calibrated_outer_low_CE'],
        'latest_lower_sample': lo['field_id'],
        'earliest_upper_bound_CE': hi['calibrated_outer_high_CE'],
        'earliest_upper_sample': hi['field_id'],
        'minimum_continuous_span_years': gap,
        'fits_duration_years': {str(d): gap <= d for d in [0, 1, 10, 100]},
    }

result = {'all_dated': check(rows)}
for label, groups in [('A', ['Roopkund_A']), ('B_C', ['Roopkund_B', 'Roopkund_C'])]:
    result[label] = check([r for r in rows if r['population_label'] in groups])
print(json.dumps(result, indent=2))
