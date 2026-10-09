"""Alternative-processing local-reference diagnostic; no new dates."""
import hashlib,json
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
ledger=json.loads((ROOT/'data/cascadia-raw-acquisition.json').read_text())
item=next(i for i in ledger['files'] if i['file'].endswith('wa130.rwl'))
raw=(ROOT/item['file']).read_bytes()
assert hashlib.sha256(raw).hexdigest()==item['sha256']
series={}
for line in raw.decode().splitlines()[3:]:
    if not line.strip():continue
    row=line.split();name=row[0];start=int(row[1]);s=series.setdefault(name,{})
    for i,v in enumerate(map(int,row[2:])):
        if v in (999,-9999):continue
        assert v>0 and start+i not in s
        s[start+i]=v
reference_ids=('CP791','CP793','CP794')
assert all(n in series for n in reference_ids)
results=[]
for mode in ('log_difference','width_difference'):
    ts={}
    for name,s in series.items():
        years=sorted(s);assert years==list(range(years[0],years[-1]+1))
        x=np.array([s[y] for y in years],float)
        if mode=='log_difference':x=np.log(x)
        x=np.diff(x);x=(x-x.mean())/x.std(ddof=1)
        ts[name]=dict(zip(years[1:],x))
    rows=[]
    for name,target in ts.items():
        refs=[n for n in reference_ids if n!=name]
        assert name not in refs
        # A target that is a reference tree is omitted from its own master.
        years=sorted(set().union(*(set(ts[n]) for n in refs)))
        assert years==list(range(years[0],years[-1]+1))
        depth={y:sum(y in ts[n] for n in refs) for y in years}
        master={y:np.mean([ts[n][y] for n in refs if y in ts[n]]) for y in years}
        for scope in ('full_target','trim_to_published_reference_overlap'):
            ty=sorted(target) if scope=='full_target' else sorted(set(target)&set(master))
            assert len(ty)>1
            x=np.array([target[y] for y in ty]);out=[]
            for delta in range(years[0]-ty[0],years[-1]-ty[-1]+1):
                if ty[-1]+delta>1720:continue
                y=np.array([master[t+delta] for t in ty])
                r=float(np.corrcoef(x,y)[0,1])
                out.append(dict(shift=delta,end=ty[-1]+delta,r=r,min_depth=min(depth[t+delta] for t in ty)))
            out.sort(key=lambda c:-c['r'])
            actual=next((c for c in out if c['shift']==0),None)
            if actual:
                y=np.array([master[t] for t in ty]);xc=x-x.mean();yc=y-y.mean()
                independent=float(np.dot(xc,yc)/np.sqrt(np.dot(xc,xc)*np.dot(yc,yc)))
                assert np.isclose(actual['r'],independent,atol=1e-12)
            rows.append(dict(id=name,scope=scope,reference_ids=refs,n_differences=len(ty),tested=len(out),
                         published_r=actual['r'] if actual else None,
                         published_rank=next((i+1 for i,c in enumerate(out) if c['shift']==0),None),
                         best=out[0] if out else None,candidates=out,
                         unresolved_reason=None if actual else 'Published span lacks complete local-reference overlap.'))
    results.append(dict(transform=mode,rows=rows))
    assert len(rows)==16
out=dict(status='RETROSPECTIVE_LOCAL_REFERENCE_SENSITIVITY_NOT_ORIGINAL_REPRODUCTION',
         source_ids=['S229','S231'],reference_choice='CP791/CP793/CP794 follows S231 local-master footnote; omit target if itself a reference.',
         processing='Adjacent log or width differences; normalize each series over its full span; average available reference values annually. Two target scopes: full record, or a fixed subset shared at published placement. Each scope tests all complete-overlap integer shifts up to1720. No gap filling; candidate scores within a scope have identical target observations.',
         limits='Reference dates fixed as published. This checks relative pattern agreement within Copalis, not absolute calendar placement. Local candidate domain is narrower than Long Island. Same-region climate and dating dependencies remain. No splines, AR models, anatomical matches or p-values reproduced.',
         numpy_version=np.__version__,results=results)
(ROOT/'data/cascadia-local-reference.json').write_text(json.dumps(out,indent=2)+'\n')
for v in results:
    print(v['transform'])
    for r in v['rows']:
        print(r['id'],r['scope'],r['n_differences'],r['tested'],r['published_rank'],r['published_r'],r['best'])
