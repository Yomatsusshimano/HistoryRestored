"""Recompute the published residual experiment's mean and sampling SE."""
import json
import math
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'data/camp-century-residual-test.json').read_text(encoding='utf-8'))
values = [r['residual_Gy'] for r in data['aliquots']]
result = {
    'n': len(values),
    'mean_Gy': statistics.mean(values),
    'standard_error_Gy': statistics.stdev(values) / math.sqrt(len(values)),
    'method': 'Arithmetic mean; sample standard deviation / sqrt(n), matching S8 formulas.',
    'scope': 'Workbook summary reproduction only; no fading, DRAC, geological resetting or final-age validation.',
}
assert math.isclose(result['mean_Gy'], data['workbook_mean_Gy'], abs_tol=1e-10)
assert math.isclose(result['standard_error_Gy'], data['workbook_standard_error_Gy'], abs_tol=1e-10)
(ROOT / 'analysis/camp-residual-check-result.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
print(json.dumps(result, indent=2))
