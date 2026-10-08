"""Exploratory P2 comparison, not replication of unspecified CDendro settings.

The published 1507 match was known before this analysis. No prospective claim.
Each series is transformed to width[y]/(width[y]+width[y-1]); only adjacent,
observed, positive-sum pairs enter. Annual means weight either series equally,
or label groups equally after averaging within groups. Labels are not custody
verification. Pearson r and t=r*sqrt((n-2)/(1-r*r)) rank all overlapping shifts.
No p-values: serial dependence and searching many shifts require further tests.
"""
import hashlib
import json
import math
from pathlib import Path
import urllib.request

ROOT=Path(__file__).resolve().parents[1]
INPUTS={
 'electron':('wa171-rwl-noaa.txt','usa','cb02dbf945b0b022e199b33f9e7c3470d9dff7302c8013f34e87b1200c57bd01'),
 'macblo':('can682-rwl-noaa.txt','canada','bf0993a3377e13796c6c45bc4b8c3cf587666816f40520a2137c4cad2202d0d4')}

def transform(widths, method='P2'):
    result={}
    for y,v in widths.items():
        if method=='P2' and y-1 in widths and v+widths[y-1]>0:
            result[y]=v/(v+widths[y-1])
        elif method=='Hollstein' and v>0 and widths.get(y-1,0)>0:
            result[y]=math.log(v/widths[y-1])
        elif method=='BailliePilcher' and v>0 and all(y+j in widths for j in range(-2,3)):
            result[y]=math.log(5*v/sum(widths[y+j] for j in range(-2,3)))
    if method not in ('P2','Hollstein','BailliePilcher'):
        raise ValueError(method)
    return result

def load(kind, method='P2'):
    name,country,sha=INPUTS[kind]
    path=ROOT/'tmp/research'/name
    url=f'https://www.ncei.noaa.gov/pub/data/paleo/treering/measurements/northamerica/{country}/{name}'
    if not path.exists():
        path.parent.mkdir(parents=True,exist_ok=True)
        with urllib.request.urlopen(url,timeout=30) as r:path.write_bytes(r.read())
    raw=path.read_bytes();assert hashlib.sha256(raw).hexdigest()==sha
    rows=[l.split('\t') for l in raw.decode().splitlines() if l and not l.startswith('#')]
    head=rows[0];assert head[0]=='age_CE'
    assert all(len(r)==len(head) for r in rows[1:])
    result={}
    for col,name in enumerate(head[1:],1):
        widths={int(r[0]):float(r[col]) for r in rows[1:] if r[col]!='NA'}
        assert all(v>=0 for v in widths.values())
        result[name]=transform(widths,method)
    return result

def mean_curve(series,kind,tree_weight=False,omit=None):
    groups={}
    for name,values in series.items():
        group=name[:6] if kind=='electron' else name[:5]
        if group==omit:continue
        for year,value in values.items():groups.setdefault(year,{}).setdefault(group,[]).append(value)
    result={}
    for year,trees in groups.items():
        values=[sum(v)/len(v) for v in trees.values()] if tree_weight else [x for v in trees.values() for x in v]
        result[year]=sum(values)/len(values)
    return result

def scan(a,b):
    fits=[]
    for shift in range(min(b)-max(a),max(b)-min(a)+1):
        pairs=[(v,b[y+shift]) for y,v in a.items() if y+shift in b]
        n=len(pairs)
        if n<30:continue
        mx=sum(x for x,y in pairs)/n;my=sum(y for x,y in pairs)/n
        xx=sum((x-mx)**2 for x,y in pairs);yy=sum((y-my)**2 for x,y in pairs)
        if not xx or not yy:continue
        r=sum((x-mx)*(y-my) for x,y in pairs)/math.sqrt(xx*yy)
        t=r*math.sqrt((n-2)/(1-r*r))
        fits.append(dict(end_year=1507+shift,overlap=n,r=r,t=t))
    return sorted(fits,key=lambda x:x['t'],reverse=True)

def summarize(fits):
    return dict(top5=fits[:5],known_1507=next(f for f in fits if f['end_year']==1507),
        known_1507_rank=next(i+1 for i,f in enumerate(fits) if f['end_year']==1507),
        tested_shifts=len(fits),best_at_least_100=next(f for f in fits if f['overlap']>=100),
        best_at_least_300=next(f for f in fits if f['overlap']>=300))

if __name__ == '__main__':
    e=load('electron');m=load('macblo')
    variants={}
    for label,weighted,omit in [('series_equal',False,None),('tree_labels_equal',True,None),('tree_labels_equal_without_ELE045',True,'ELE045')]:
        variants[label]=summarize(scan(mean_curve(e,'electron',weighted,omit),mean_curve(m,'macblo',weighted)))
    leaveout={}
    reference=mean_curve(m,'macblo',True)
    for tree in sorted({name[:6] for name in e}):
        f=scan(mean_curve(e,'electron',True,tree),reference)
        leaveout[tree]=dict(best=f[0],known_1507_rank=next(i+1 for i,v in enumerate(f) if v['end_year']==1507))
    out=dict(source_ids=['S74','S77','S78'],inputs={k:dict(name=v[0],sha256=v[2]) for k,v in INPUTS.items()},
        method='Unclipped P2 on each series, annual arithmetic means, positive Pearson t ranking; see script docstring.',
        publication_replication=False,prospective_test=False,macblo_series=len(m),electron_series=len(e),
        variants=variants,leave_one_electron_tree_label_out=leaveout,
        limitations='Published internal ring assignments and reference dating are accepted inputs. Grouping uses first six Electron or five MacBlo label characters, not authenticated specimen independence. P2 is a declared alternative, not the unknown article settings or P2YrsL. No multiple-search significance or independent calendar validation. Missing/zero-sum pairs excluded; no imputation.')
    (ROOT/'analysis/electron-macblo-comparison.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(variants=variants,leaveout_best_years={k:v['best']['end_year'] for k,v in leaveout.items()},macblo_series=len(m)),indent=2))
