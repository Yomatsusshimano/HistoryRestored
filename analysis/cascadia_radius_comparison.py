"""Descriptive within-root comparison, not independent calendar crossdating."""
import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'data/cascadia-width-extract.json'
data = json.loads(source.read_text(encoding='utf-8'))

def values(name):
    row = next(s for s in data['series'] if s['id'] == name)
    return {row['start_year']+i: w for i,w in enumerate(row['widths'])}

def pearson(a, b):
    assert len(a) == len(b) and len(a) > 1
    ma, mb = sum(a)/len(a), sum(b)/len(b)
    da, db = [x-ma for x in a], [x-mb for x in b]
    return sum(x*y for x,y in zip(da,db))/math.sqrt(sum(x*x for x in da)*sum(y*y for y in db))

c, b = values('GF2RTC'), values('GF2RTB')
years = sorted(c.keys() & b.keys())
assert years == list(range(1400,1700))
x, y = [c[i] for i in years], [b[i] for i in years]
result = {
    'input_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'series': ['GF2RTC','GF2RTB'],
    'alignment': 'Published year labels; no search over calendar placements',
    'common_start': years[0], 'common_end': years[-1], 'paired_widths': len(years),
    'raw_pearson_r': pearson(x,y),
    'first_difference_pairs': len(years)-1,
    'first_difference_pearson_r': pearson([v-u for u,v in zip(x,x[1:])], [v-u for u,v in zip(y,y[1:])]),
    'significance_test': None,
    'limitations': ['Related radii from the same root, not independent trees',
                   'No external reference chronology or absolute date test',
                   'No serial-correlation correction or anatomical reassessment',
                   'Manual transcription has documented corrections; independent audit pending']
}
(ROOT/'analysis/cascadia-radius-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
