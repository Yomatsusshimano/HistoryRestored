"""Declared combined-GF2 comparison with archived Long Island outputs."""
import hashlib
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
inputs={}
def read(rel):
    b=(ROOT/rel).read_bytes();inputs[rel]=hashlib.sha256(b).hexdigest()
    return json.loads(b)
combined=read('data/cascadia-combined-gf2.json')
ledger=read('data/cascadia-chronology-acquisition.json')
masters={}
for item in ledger['files']:
    name=Path(item['file']).name
    if not name.endswith('-crn-noaa.txt'):continue
    b=(ROOT/item['file']).read_bytes();assert hashlib.sha256(b).hexdigest()==item['sha256']
    inputs[item['file']]=item['sha256']; record={};depth={}
    for line in b.decode().splitlines():
        if not line or line.startswith('#') or line.startswith('age_CE'):continue
        y,v,n=line.split();record[int(y)]=float(v);depth[int(y)]=int(n)
    kind={'wa129-crn-noaa.txt':'standard','wa129a-crn-noaa.txt':'ARSTAN','wa129r-crn-noaa.txt':'residual'}[name]
    masters[kind]=(record,depth)

def transformed(record,mode):
    years=sorted(record);assert years==list(range(years[0],years[-1]+1))
    v=np.array([record[y] for y in years],float);assert np.all(v>0)
    if mode=='mean_divided_width':v=v/v.mean()
    else:
        if mode=='standardized_log_difference':v=np.log(v)
        v=np.diff(v);years=years[1:];v=(v-v.mean())/v.std(ddof=1)
    return dict(zip(years,v))

def correlate(x,y):
    xc=x-x.mean();yc=y-y.mean()
    return float(np.dot(xc,yc)/np.sqrt(np.dot(xc,xc)*np.dot(yc,yc)))

# Nonperiodic known signal verifies shift sign and target extraction.
rng=np.random.default_rng(1675);noise=rng.normal(size=400)
known=[correlate(noise[70:150],noise[i:i+80]) for i in range(321)]
assert int(np.argmax(known))==70

results=[]
for item in combined['averages']:
    mode,basis=item['transform'],item['basis']
    target={r['year']:r['value'] for r in item['trunk_values']}
    counts={r['year']:r['radii'] for r in item['trunk_values']}
    for kind,(record,depth) in masters.items():
        master=transformed(record,mode);my=sorted(master)
        for scope in ('full_trunk','last_255_observations'):
            ty=sorted(target)
            if scope=='last_255_observations':ty=ty[-255:]
            x=np.array([target[y] for y in ty]);lo=my[0]-ty[0];hi=my[-1]-ty[-1]
            values=[]
            for shift in range(lo,hi+1):
                y=np.array([master[t+shift] for t in ty]);values.append(correlate(x,y))
            actual=values[-lo];y=np.array([master[t] for t in ty])
            assert np.isclose(actual,np.corrcoef(x,y)[0,1],atol=1e-12)
            # Averaged targets are not reconstructed from their scaled constituents here.
            assert np.isclose(actual,correlate(x*10,y/10),atol=1e-12)
            def candidate(shift):
                n=[depth[t+shift] if mode=='mean_divided_width' else min(depth[t+shift],depth[t+shift-1]) for t in ty]
                return dict(shift=shift,assigned_end=ty[-1]+shift,r=values[shift-lo],
                            reference_count_min=min(n),reference_count_median=float(np.median(n)))
            bounds={}
            for bound in (1720,1986):
                eligible=[s for s in range(lo,hi+1) if ty[-1]+s<=bound]
                rank=sorted(eligible,key=lambda s:-values[s-lo])
                bounds[str(bound)]=dict(tested=len(rank),published_rank=rank.index(0)+1,
                    best=candidate(rank[0]),top_five=[candidate(s) for s in rank[:5]])
            results.append(dict(transform=mode,basis=basis,reference=kind,scope=scope,
                n=len(ty),first_target_year=ty[0],last_target_year=ty[-1],
                target_count_distribution={str(k):sum(counts[t]==k for t in ty) for k in sorted(set(counts[t] for t in ty))},
                published_r=actual,published_reference_counts=candidate(0),
                first_candidate_shift=lo,all_candidate_r=values,bounds=bounds))
assert len(results)==36
# Cross-check every candidate in the six comparable NW-only scans against the
# earlier separately implemented per-radius diagnostic, not just its best rank.
previous=read('data/cascadia-archived-reference.json')
modes={'standardized_log_difference':'log_difference',
       'standardized_width_difference':'width_difference'}
checked=0
for r in results:
    if r['basis']!='NW_only' or r['scope']!='full_trunk' or r['transform'] not in modes:continue
    v=next(v for v in previous['results'] if v['reference_version']==r['reference'] and v['transform']==modes[r['transform']])
    p=next(p for p in v['rows'] if p['id']=='CPGF2NW')
    assert r['first_candidate_shift']==p['first_candidate_shift']
    assert np.allclose(r['all_candidate_r'],p['all_candidate_r'],atol=1e-12)
    checked+=1
assert checked==6
out=dict(status='COMBINED_TARGET_ARCHIVED_REFERENCE_DIAGNOSTIC_NOT_ORIGINAL_REPRODUCTION',
    source_ids=['S229','S231','S233'],input_sha256=inputs,numpy_version=np.__version__,
    method='Reuse already-declared per-radius target transforms and annual averages; same transform applied to archived reference indices. Three reference versions, two trunk bases, full/final255 scopes; all complete-overlap integer shifts. Endpoint bounds1720 and1986 retained separately. No minimum reference depth or significance test.',
    limits='Hybrid transformed raw targets versus processed reference indices; original decay/spline/AR settings/version unknown.255 is count sensitivity, not original indices.1720 inherits radiocarbon. All tests retrospective/dependent; reference count not authenticated tree count. Regional alternative maxima are not replacement dates or tests of a common absolute calendar shift.',
    prior_scan_crosschecks=checked,results=results)
(ROOT/'data/cascadia-combined-regional.json').write_text(json.dumps(out,indent=2)+'\n')
for r in results:
    b=r['bounds']['1720']
    print(r['transform'],r['basis'],r['reference'],r['scope'],r['n'],
          'rank',b['published_rank'],'r',round(r['published_r'],5),
          'best',b['best'])
