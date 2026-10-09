"""Audit the printed synopsis; no geolocation or regional model fitting."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
inputs = ROOT / 'data/halley1715-regional-inputs.json'
ledger = json.loads(inputs.read_text(encoding='utf-8'))

def seconds(token):
    parts = list(map(int, token.split(':')))
    return sum(v * 60**i for i, v in enumerate(reversed(parts)))

rows = []
for row in ledger['rows']:
    duration = seconds(row['duration_token']) if row['duration_token'] else None
    endpoints = (seconds(row['emersion']) - seconds(row['immersion'])
                 if row['emersion'] and row['immersion'] else None)
    rows.append(dict(row=row['row'], place_token=row['place_token'],
                     duration_s=duration, endpoint_duration_s=endpoints,
                     endpoint_minus_printed_s=endpoints-duration
                     if endpoints is not None and duration is not None else None,
                     above_author_inferred_maximum=duration > 237
                     if duration is not None else None))
assert len(rows) == 26
out = dict(source_id='S282', input_sha256=hashlib.sha256(inputs.read_bytes()).hexdigest(),
           rows=rows, total_rows=len(rows),
           printed_duration_rows=sum(r['duration_s'] is not None for r in rows),
           paired_endpoint_rows=sum(r['endpoint_duration_s'] is not None for r in rows),
           author_inferred_maximum_s=237,
           above_maximum_rows=[r['row'] for r in rows if r['above_author_inferred_maximum']],
           limits='Arithmetic audit only. The237s maximum is Halley inferred geometry, '
                  'not a modern fitted regional maximum or observation. '
                  'Shared compilation and uncertain clocks/sites limit independence.')
(ROOT/'data/halley1715-regional-results.json').write_text(
    json.dumps(out, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k != 'rows'}, indent=2))
