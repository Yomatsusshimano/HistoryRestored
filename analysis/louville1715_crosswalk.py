"""Compare separately printed times; do not infer the editorial mechanism."""
from pathlib import Path
import json, hashlib
ROOT = Path(__file__).resolve().parents[1]
p = ROOT/'data/louville1715-inputs.json'
x = json.loads(p.read_text(encoding='utf-8'))
def sec(s):
    h,m,s = map(int,s.split(':'))
    return h*3600+m*60+s
rows = [dict(**v, french_minus_english_s=sec(v['french'])-sec(v['english']))
        for v in x['paired_louville_times']]
counts = {}
for v in rows:
    k = str(v['french_minus_english_s'])
    counts[k] = counts.get(k,0)+1
out = dict(input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(), pairs=rows,
           offset_counts=counts,
           french_totality_s=sec(x['french_contacts']['total_end'])-sec(x['french_contacts']['total_begin']),
           limits='Arithmetic differences only. A clock-correction mechanism is consistent '
                  'with the pattern but not authenticated by original notes. '
                  'Shared venue/calibration/event prevents independent astronomical anchoring.')
(ROOT/'data/louville1715-results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k!='pairs'},indent=2))
