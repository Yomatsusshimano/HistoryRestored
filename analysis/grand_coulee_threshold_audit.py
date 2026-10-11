"""Intersect published model-threshold envelopes; does not run a hydraulic model.

Standard library only. Source transcription and conditional semantics are in
data/grand-coulee-thresholds.json. Table and caption values stay separate.
"""
import hashlib
import json
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
path = ROOT / 'data/grand-coulee-thresholds.json'
data = json.loads(path.read_text(encoding='utf-8'))
results = []
for row in data['scenarios']:
    values = []
    for start, end, step in row['discharge_sequences']:
        start, end, step = map(lambda x: Decimal(str(x)), (start, end, step))
        assert step > 0 and end >= start and (end-start) % step == 0
        values.extend(start + i*step for i in range(int((end-start)/step)+1))
    assert len(values) == len(set(values)) == row['reported_runs'], row['id']
    lower = max(row['east_rim_lower'], row['hartline_lower'], row['lenore_lower'])
    for variant in ('table', 'caption'):
        upper = row['lenore_upper_'+variant]
        if upper is None:
            continue
        results.append(dict(
            scenario=row['id'], upper_value_source=variant,
            lower_envelope=lower, upper_envelope=upper,
            envelope_overlaps=lower <= upper,
            gap_if_disjoint=max(0, lower-upper),
            tested_discharge_count=len(values),
            simulated_points_inside_inclusive_envelope=[float(q) for q in values if Decimal(str(lower)) <= q <= Decimal(str(upper))]))
result = dict(input_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
              units=data['units'], results=results,
              caveat='Conditional envelope arithmetic on reported modeled thresholds. Boundary equality is unresolved; inclusive values are a permissive screen. No raw stage comparison, hydraulic run, coevality validation or confidence interval.')
(ROOT/'analysis/grand-coulee-threshold-audit-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
for row in results:
    print(row['scenario'], row['upper_value_source'], row['lower_envelope'], row['upper_envelope'], 'overlap', row['envelope_overlaps'])
