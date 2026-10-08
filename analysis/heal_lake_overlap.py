"""Potential overlap links only; interval overlap is not ring-pattern agreement."""
import hashlib
import json
from pathlib import Path
import re
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'tmp/research/zhang-1996.pdf'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='89e223f6f0f548fc7c2ea1a5c0a112df3dede46f772c1b7aa16049a7c34b5ed8'
pdf=PdfReader(p);rows=[]
for page in [36,37,38]:
    for line in pdf.pages[page-1].extract_text().splitlines():
        m=re.match(r'^\s*(\d+)\s+(.+?)\s+(\d+)\s*--\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+([.\d]+)\s+([.\d]+)\s*$',line)
        if not m or not 1<=int(m[1])<=100:continue
        label=m[2].replace(' ','').replace('l','1')
        rows.append(dict(row=int(m[1]),sample=label,first=int(m[3]),last=int(m[4]),
            printed_span=int(m[5]),segments=int(m[6]),flags=int(m[7]),
            correlation_with_master=float(m[8]),pdf_page=page))
assert [r['row'] for r in rows]==list(range(1,101))
assert len({r['sample'] for r in rows})==100
# This subset includes every table row with last year >=700, not the full chronology.
assert min(r['last'] for r in rows)==705
def overlap(a,b):return max(0,min(a['last'],b['last'])-max(a['first'],b['first'])+1)
anchors={r['sample'] for r in rows if r['last']==1992}
# Widest-path capacity: maximum achievable minimum interval overlap along a path.
capacity={r['sample']:float('inf') if r['sample'] in anchors else 0 for r in rows}
parent={}
for _ in rows:
    changed=False
    for a in rows:
        for b in rows:
            if a is b:continue
            value=min(capacity[a['sample']],overlap(a,b))
            if value>capacity[b['sample']]:
                capacity[b['sample']]=value;parent[b['sample']]=a['sample'];changed=True
    if not changed:break
thresholds={}
for threshold in [30,50,100,150]:
    connected=[r for r in rows if capacity[r['sample']]>=threshold]
    thresholds[str(threshold)]=dict(connected_rows=len(connected),earliest_assigned_year=min(r['first'] for r in connected),
        disconnected=[r['sample'] for r in rows if capacity[r['sample']]<threshold])
low=[]
for y in range(700,1993):
    present=[r['sample'] for r in rows if r['first']<=y<=r['last']]
    if len(present)<=3:
        if low and low[-1]['last']+1==y and low[-1]['samples']==present:low[-1]['last']=y
        else:low.append(dict(first=y,last=y,samples=present))
out=dict(source_id='S82',case_id='C021',scope='Table 3.3 rows 1–100, all intervals ending at or after 700 CE; printed pp.28–30 visually inspected',
    rows=rows,endpoint_1992_labels=sorted(anchors),
    printed_span_disagreements=[r for r in rows if r['printed_span']!=r['last']-r['first']+1],
    potential_connectivity_by_minimum_pair_overlap=thresholds,low_depth_intervals=low,
    capacity_to_1992={k:None if v==float('inf') else v for k,v in capacity.items()},
    limitations='Overlap geometry on published assignments, not correlations or actual assembly order. Endpoint-1992 labels are provisional anchor candidates, not authenticated living samples. Omits pre-700-only rows. Thresholds are exploratory, not validated acceptance rules. Does not date an error, show independence, or justify a 132-year shift.')
(ROOT/'analysis/heal-lake-overlap.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['endpoint_1992_labels','printed_span_disagreements','potential_connectivity_by_minimum_pair_overlap','low_depth_intervals']},indent=2))
