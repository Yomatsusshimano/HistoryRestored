"""Conditional arithmetic reconstruction; does not validate instruments or circuits."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/upton-lamp-records.json').read_text(encoding='utf-8'))
output = []
for row, auxiliary_v in zip(data['calculations'], [1.5, 1.4]):
    v = row['voltage_reported']
    factor = 6.26
    derived_r = v * factor / auxiliary_v
    watts = v * auxiliary_v / factor
    assert abs(watts - v*v/derived_r) < 1e-12
    output.append({
        'page': row['page'],
        'auxiliary_voltage_reported': auxiliary_v,
        'factor_reported': factor,
        'factor_physical_identity': None,
        'hypothesized_relation': 'R = lamp_voltage * 6.26 / auxiliary_voltage',
        'resistance_reconstructed': derived_r,
        'power_from_reconstructed_resistance': watts,
        'lamps_per_hp_from_reconstructed_resistance': 33000/(44.3*watts),
        'lamps_per_hp_holding_written_resistance_fixed': row['lamps_per_hp_recalculated'],
        'interpretation': 'Arithmetic correspondence, not a verified circuit or independent resistance measurement.'
    })
result = {'source_id':'S180', 'assumption':'Reconstruct the apparent preceding voltage-ratio calculation; retain prior fixed-resistance calculation as a different conditional check.', 'rows':output}
(ROOT / 'analysis/upton-calculation-dependence.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
