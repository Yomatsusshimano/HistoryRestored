"""Inspect reference coverage and published pulse measurements; no new dates."""
import hashlib
import json
from pathlib import Path
import re
import urllib.request
import zipfile
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/'tmp/research/sciadv.adh4973_sm.pdf'
if not pdf.exists():
    with urllib.request.urlopen('https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10530078/supplementaryFiles',timeout=30) as r:
        from io import BytesIO
        with zipfile.ZipFile(BytesIO(r.read())) as z:
            pdf.parent.mkdir(parents=True,exist_ok=True)
            pdf.write_bytes(z.read('sciadv.adh4973_sm.pdf'))
sha=hashlib.sha256(pdf.read_bytes()).hexdigest()
assert sha=='160329ac32f2ce9af0b739d54658e1afe63fc5054c72db28754492cf0693918a', 'Supplement changed; inspect before reuse'
text=PdfReader(pdf).pages[7].extract_text()
measurements=[]
for line in text.splitlines():
    m=re.match(r'^(Lake WA|Hamma|Price)\s+(OS-\d+)\s+(.*)',line)
    if not m:continue
    v=m[3].split();assert len(v)==8,(line,v)
    measurements.append(dict(site=m[1],lab_id=m[2],assigned_year=int(v[0]),
        fraction_modern=float(v[1]),fraction_modern_error=float(v[2]),age_BP=int(v[3]),age_error=int(v[4]),
        delta14C=float(v[5]),upper_bound=float(v[6]),lower_bound=float(v[7])))
assert len(measurements)==35
jumps={}
for site in ('Lake WA','Hamma','Price'):
    rows=sorted([r for r in measurements if r['site']==site],key=lambda r:r['assigned_year'])
    diffs=[]
    for a,b in zip(rows,rows[1:]):
        assert b['assigned_year']==a['assigned_year']+1
        diffs.append(dict(from_year=a['assigned_year'],to_year=b['assigned_year'],
            delta14C_increase=round(b['delta14C']-a['delta14C'],6),
            fraction_modern_increase=round(b['fraction_modern']-a['fraction_modern'],6)))
    jumps[site]=dict(maximum_delta14C_increase=max(diffs,key=lambda r:r['delta14C_increase']),all_changes=diffs)
raw=(ROOT/'tmp/research/can682-rwl-noaa.txt').read_bytes()
assert hashlib.sha256(raw).hexdigest()=='bf0993a3377e13796c6c45bc4b8c3cf587666816f40520a2137c4cad2202d0d4'
rows=[l.split('\t') for l in raw.decode().splitlines() if l and not l.startswith('#')]
spans=[]
for i,name in enumerate(rows[0][1:],1):
    years=[int(r[0]) for r in rows[1:] if r[i]!='NA']
    spans.append(dict(series=name,first=min(years),last=max(years),observations=len(years),internal_missing=max(years)-min(years)+1-len(years)))
out=dict(source_ids=['S77','S79','S80'],supplement_sha256=sha,locator='Supplement Table S2, PDF page 8, visually inspected',
    measurements=measurements,annual_changes=jumps,reference_spans=spans,
    reference_series_ending_1990=[s['series'] for s in spans if s['last']==1990],
    reference_series_spanning_1507_through_1990=[s['series'] for s in spans if s['first']<=1507 and s['last']==1990],
    independent_calendar_reproduction=False,
    limitations='Years are published crossdates, not inferred blindly here. Pulse measurements are from earthquake-killed wood, not MacBlo or Electron. Lab IDs identify assays, not separate trees. Adjacent changes share measurements; no independent-error significance inferred. Reference endpoints do not authenticate bark or collection dates.')
(ROOT/'data/macblo-anchor-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(dict(supplement_sha256=sha,rows=len(measurements),jumps={k:v['maximum_delta14C_increase'] for k,v in jumps.items()},reference_to_1990=out['reference_series_ending_1990']),indent=2))
