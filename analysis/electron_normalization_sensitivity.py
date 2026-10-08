"""Retrospective alternatives; no tuning to obtain the known 1507 result."""
import json
import math
import statistics
from electron_macblo_comparison import ROOT, INPUTS, load, transform, mean_curve, scan, summarize

# Known-formula fixtures check orientation, centered-window edges, and no imputation.
w={1:1.,2:2.,3:4.,4:8.,5:16.}
assert math.isclose(transform(w,'Hollstein')[3],math.log(2))
assert transform(w,'BailliePilcher')=={3:math.log(20/31)}
assert 3 not in transform({1:1.,3:4.},'Hollstein')
assert transform({1:0.,2:0.},'P2')=={}

out=dict(source_ids=['S74','S77','S78'],prospective_test=False,publication_replication=False,
    inputs={k:dict(name=v[0],sha256=v[2]) for k,v in INPUTS.items()},methods={})
for method in ['P2','Hollstein','BailliePilcher']:
    e=load('electron',method);m=load('macblo',method)
    a=mean_curve(e,'electron',True);b=mean_curve(m,'macblo',True)
    fits=scan(a,b)
    years=sorted(a.keys() & b.keys())
    r=statistics.correlation([a[y] for y in years],[b[y] for y in years])
    assert math.isclose(r,next(f for f in fits if f['end_year']==1507)['r'],abs_tol=1e-12)
    # Remove each reference label group as well as each Electron label group.
    omissions={}
    for kind,series in [('electron',e),('macblo',m)]:
        size=6 if kind=='electron' else 5
        results={}
        for group in sorted({s[:size] for s in series}):
            reduced=mean_curve(series,kind,True,group)
            fs=scan(reduced,b) if kind=='electron' else scan(a,reduced)
            results[group]=dict(best=fs[0],rank_1507=next(i+1 for i,f in enumerate(fs) if f['end_year']==1507))
        omissions[kind]=results
    out['methods'][method]=dict(full=summarize(fits),omissions=omissions,
        transformed_electron_values=sum(map(len,e.values())),transformed_macblo_values=sum(map(len,m.values())))
out['limitations']='Related retrospective runs using existing ring/calendar assignments. Five-character MacBlo and six-character Electron groups are label assumptions. No calibrated multiple-search probability, original-settings replication, or independent reference dating. Log transforms exclude zero current/previous widths; centered five-year transform requires complete windows. No imputation.'
(ROOT/'analysis/electron-normalization-sensitivity.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
for method,x in out['methods'].items():
    print(method,json.dumps(dict(best=x['full']['top5'][0],runner_up=x['full']['top5'][1],
        omissions={k:dict(count=len(v),best_years=sorted({r['best']['end_year'] for r in v.values()})) for k,v in x['omissions'].items()})))
