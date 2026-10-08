"""Invert S138 Figure 2's printed curve, not its unrecovered regression."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
a, b, c = -0.0641, -0.5114, 3.031

def roots_for_y(y):
    discriminant = b*b - 4*a*(c-y)
    if discriminant < 0:
        return []
    return sorted([(-b + math.sqrt(discriminant))/(2*a),
                   (-b - math.sqrt(discriminant))/(2*a)])

rows = []
for level, reported_age in [(15, 13.2), (20, 15.4)]:
    roots = roots_for_y(-level)
    positive = [r for r in roots if r >= 0]
    assert len(positive) == 1
    age = positive[0]
    assert abs(a*age**2+b*age+c+level) < 1e-10
    rows.append({
        'excavation_level': level,
        'reported_approximate_age_ka': reported_age,
        'assumed_equation_y': -level,
        'all_real_age_roots_ka': roots,
        'nonnegative_root_ka': age,
        'difference_from_reported_approximate_age_ka': age-reported_age,
        'literal_positive_level_real_roots': roots_for_y(level),
    })
result = {
    'source_id': 'S138',
    'locator': 'Figure 2, printed p.4 / repository PDF p.6',
    'printed_equation': 'y = -0.0641*x^2 - 0.5114*x + 3.031',
    'printed_R_squared': 0.961,
    'x_axis': 'OSL Data (ka ago)',
    'y_axis': 'Level (10 cm/level), increasing downward',
    'sign_interpretation': 'Use y=-level to match the downward plotted curve; this sign convention is inferred, not explicitly supplied by the caption.',
    'results': rows,
    'limits': [
        'Inversion of rounded printed coefficients only; no refit of original points.',
        'No laboratory ages, uncertainty propagation or 95% confidence intervals reproduced.',
        'No sample-to-level survey crosswalk or independent chronological validation.',
        'The negative-age roots are retained as algebraic solutions, not physical ages.',
    ],
}
(ROOT/'data/coyote-printed-curve-check.json').write_text(
    json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
