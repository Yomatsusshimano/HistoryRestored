"""Retrospective alternative-processing diagnostic, NOT original crossdating."""
from pathlib import Path
import hashlib,json
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def read_series(item):
    raw=(ROOT/item['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==item['sha256']
    series={}
    for line in raw.decode('utf-8-sig').splitlines()[3:]:
        if not line.strip(): continue
        parts=line.split(); name=parts[0]; start=int(parts[1])
        s=series.setdefault(name,{})
        for i,v in enumerate(map(int,parts[2:])):
            if v in (999,-9999): continue
            assert start+i not in s
            s[start+i]=v
    return series

def transformed(s,kind):
    years=sorted(s); assert years==list(range(years[0],years[-1]+1))
    x=np.array([s[y] for y in years],dtype=float)
    assert np.all(x>0), 'Zero/nonpositive width needs a declared handling rule'
    if kind=='log_difference': x=np.log(x)
    x=np.diff(x); x=(x-x.mean())/x.std(ddof=1)
    return dict(zip(years[1:],x))

def shifts(target,master):
    ty=sorted(target); my=sorted(master)
    assert ty==list(range(ty[0],ty[-1]+1))
    assert my==list(range(my[0],my[-1]+1))
    x=np.array([target[y] for y in ty]); x=x-x.mean()
    out=[]
    for delta in range(my[0]-ty[0],my[-1]-ty[-1]+1):
        y=np.array([master[t+delta] for t in ty]); y=y-y.mean()
        r=float(np.dot(x,y)/np.sqrt(np.dot(x,x)*np.dot(y,y)))
        out.append(dict(shift=delta,assigned_end=ty[-1]+delta,r=r))
    return out

# Verify shift sign and recovery with a constructed nonperiodic signal.
rng=np.random.default_rng(1143); z=rng.normal(size=500)
master_test=dict(enumerate(z,1000)); target_test=dict(enumerate(z[100:300],1500))
assert max(shifts(target_test,master_test),key=lambda r:r['r'])['shift']==-400
positive=dict(enumerate(np.exp(z[:100]),1000))
for kind in ('log_difference','width_difference'):
    original=list(transformed(positive,kind).values())
    rescaled=list(transformed({y:v*10 for y,v in positive.items()},kind).values())
    assert np.allclose(original,rescaled,rtol=1e-12,atol=1e-12)

ledger=json.loads((ROOT/'data/cascadia-raw-acquisition.json').read_text())
all_series=[read_series(i) for i in ledger['files']]
results=[]
for kind in ('log_difference','width_difference'):
    refs={name:transformed(s,kind) for name,s in all_series[0].items()}
    for weighting in ('equal_series','paired_ids_merged'):
        groups={}
        for name,s in refs.items():
            group=name
            if weighting=='paired_ids_merged' and name in ('LI766I','LI766O','LI767I','LI767O'):
                group=name[:-1]
            groups.setdefault(group,[]).append(s)
        gy={g:{y:float(np.mean([s[y] for s in ss if y in s]))
               for y in sorted(set().union(*(set(s) for s in ss)))} for g,ss in groups.items()}
        years=sorted(set().union(*(set(s) for s in gy.values())))
        depth={y:sum(y in s for s in gy.values()) for y in years}
        master={y:float(np.mean([s[y] for s in gy.values() if y in s])) for y in years}
        rows=[]
        for file,ss in zip(ledger['files'][1:],all_series[1:]):
            for name,s in ss.items():
                target=transformed(s,kind); candidates=shifts(target,master)
                actual=next(c for c in candidates if c['shift']==0)
                assert np.isclose(actual['r'],np.corrcoef(list(target.values()),[master[y] for y in target])[0,1],atol=1e-12)
                scopes={}
                for bound in (1720,1986):
                    eligible=[c for c in candidates if c['assigned_end']<=bound]
                    ranked=sorted(eligible,key=lambda c:-c['r'])
                    for candidate in ranked[:5]:
                        counts=[depth[y+candidate['shift']] for y in target]
                        candidate['reference_depth_min']=min(counts)
                        candidate['reference_depth_median']=float(np.median(counts))
                    scopes[str(bound)]=dict(tested=len(ranked),published_rank=next(i+1 for i,c in enumerate(ranked) if c['shift']==0),best=ranked[0],top_five=ranked[:5])
                rows.append(dict(id=name,file=file['file'],n_differences=len(target),published_end=max(s),
                                 published_r=actual['r'],minimum_reference_depth_at_published=min(depth[y] for y in target),scopes=scopes))
        results.append(dict(transform=kind,weighting=weighting,reference_groups=len(groups),rows=rows))
out=dict(status='RETROSPECTIVE_SENSITIVITY_NOT_ORIGINAL_REPRODUCTION',numpy_version=np.__version__,
         choices='All positive widths; adjacent differences (log or integer widths); each reference series z-scored over its full difference span; reference averaged per year. Optional paired766/767 identifier grouping is inferred, not a verified specimen crosswalk. Targets tested separately at every full-overlap integer shift; two endpoint upper bounds. No significance probabilities.',
         limitations='Published reference calendar retained. Varying reference depth includes single-series years. Radii and tests are dependent. No root death dates or new calendar assignments. No original spline/AR processing or anatomical matching.',results=results)
(ROOT/'data/cascadia-alignment-sensitivity.json').write_text(json.dumps(out,indent=2)+'\n')
for v in results:
    print(v['transform'],v['weighting'],{bound:sum(r['scopes'][bound]['published_rank']==1 for r in v['rows']) for bound in ('1720','1986')},'of',len(v['rows']))
    for name in ('CP790','CP791','CPGF2NW'):
        r=next(r for r in v['rows'] if r['id']==name)
        print(name,round(r['published_r'],4),r['scopes']['1720']['published_rank'],r['scopes']['1720']['best'])
    print('Exceptions:',[(r['id'],r['scopes']['1720']['published_rank']) for r in v['rows'] if r['scopes']['1720']['published_rank']!=1])
