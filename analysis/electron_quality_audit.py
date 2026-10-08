"""Reconcile archived QC counts and calculate tree-label replication; no redating."""
import hashlib
import json
from pathlib import Path
import re
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
URL='https://www.ncei.noaa.gov/pub/data/paleo/treering/measurements/correlation-stats/wa171.txt'
SHA='889f5da95217aadf02ccdc4a25a21d53af3c0dc9f675c4b71aef528998765498'
p=ROOT/'tmp/research/wa171-quality.txt'
if not p.exists():
    p.parent.mkdir(parents=True,exist_ok=True)
    with urllib.request.urlopen(URL,timeout=30) as r:p.write_bytes(r.read())
raw=p.read_bytes()
assert hashlib.sha256(raw).hexdigest()==SHA
text=raw.decode('ascii')
part5,part7=text.split('PART 5:',1)[1].split('PART 7:',1)
flagged=[]
for line in part5.splitlines():
    match=re.match(r'\s*\d+\s+((?:ELE|KAP)\w+)\s+(\d+)\s+(\d+)\s+(.*)',line)
    if not match:continue
    flags=re.findall(r'\.\d+[AB]',match[4])
    if flags:flagged.append(dict(series=match[1],flagged_coefficients=flags))
stats=[]
for line in part7.splitlines():
    row=line.split()
    if len(row)>8 and row[0].isdigit() and re.fullmatch(r'(ELE|KAP)\w+',row[1]):
        stats.append(dict(series=row[1],first=int(row[2]),last=int(row[3]),
            years=int(row[4]),segments=int(row[5]),flags=int(row[6]),
            reported_correlation_with_master=float(row[7])))
coverage=json.loads((ROOT/'analysis/electron-measurement-coverage.json').read_text())
series={s['series'].removesuffix('_raw'):s for t in coverage['trees'] for s in t['series']}
assert set(series)=={s['series'] for s in stats}
assert all((s['first'],s['last'],s['years'])==(series[s['series']]['first'],series[s['series']]['last'],series[s['series']]['observations']) for s in stats)
assert sum(len(s['flagged_coefficients']) for s in flagged)==sum(s['flags'] for s in stats)
data=(ROOT/'tmp/research/wa171-rwl-noaa.txt').read_bytes()
assert hashlib.sha256(data).hexdigest()==coverage['input_sha256']
rows=[l.split('\t') for l in data.decode().splitlines() if l and not l.startswith('#')]
header=rows[0]
annual=[]
for row in rows[1:]:
    labels={header[i][:6] for i,v in enumerate(row[1:],1) if v!='NA'}
    annual.append(dict(year=int(row[0]),tree_ids=sorted(labels),count=len(labels)))
low=[]
for row in annual:
    if row['count']>2:continue
    if low and low[-1]['last']+1==row['year'] and low[-1]['tree_ids']==row['tree_ids']:
        low[-1]['last']=row['year']
    else:low.append(dict(first=row['year'],last=row['year'],tree_ids=row['tree_ids']))
out=dict(source_ids=['S74','S75'],quality_url=URL,quality_sha256=SHA,
    report_date='2025-11-18',series=len(stats),observed_widths=sum(s['years'] for s in stats),
    segments=sum(s['segments'] for s in stats),flags=sum(s['flags'] for s in stats),
    flagged_series=flagged,flag_meanings=dict(A='Below .3281 but highest at assigned position',B='Higher correlation at another position'),
    all_quality_spans_match_raw=True,ele045_statistics=[s for s in stats if s['series'].startswith('ELE045')],
    intervals_with_at_most_two_tree_ids=low,
    calendar_span_without_ELE045=[min(s['first'] for k,s in series.items() if not k.startswith('ELE045')),max(s['last'] for k,s in series.items() if not k.startswith('ELE045'))],
    limitations='Archived diagnostics, not a fresh COFECHA run. Segment windows overlap and radii from a tree are related. Tree-label counts are not specimen authentication. Omitting ELE045 preserves coverage bounds only; no correlation, peak-year or age-model sensitivity was computed.')
(ROOT/'analysis/electron-quality-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
