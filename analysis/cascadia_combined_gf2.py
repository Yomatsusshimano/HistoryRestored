"""Declared GF2 tree averages and radius omission sensitivity; no new dates."""
import hashlib
import json
from pathlib import Path
import numpy as np

ROOT=Path(__file__).resolve().parents[1]
inputs={}
def read_json(rel):
    b=(ROOT/rel).read_bytes(); inputs[rel]=hashlib.sha256(b).hexdigest()
    return json.loads(b)
old=read_json('data/cascadia-width-extract.json')
third=read_json('data/cascadia-third-root.json')
roots={s['id']:{s['start_year']+i:v for i,v in enumerate(s['widths'])}
       for s in old['series'] if s['id'] in ('GF2RTB','GF2RTC')}
roots['GF2RTA']={third['start_year']+i:v for i,v in enumerate(third['widths'])}
ledger=read_json('data/cascadia-raw-acquisition.json')
item=next(f for f in ledger['files'] if f['file'].endswith('wa130.rwl'))
raw=(ROOT/item['file']).read_bytes()
assert hashlib.sha256(raw).hexdigest()==item['sha256']
inputs[item['file']]=item['sha256']; trunks={}
for line in raw.decode().splitlines()[3:]:
    row=line.split()
    if not row or not row[0].startswith('CPGF2'): continue
    s=trunks.setdefault(row[0],{}); start=int(row[1])
    for i,v in enumerate(map(int,row[2:])):
        if v in (999,-9999): continue
        assert v>0 and start+i not in s
        s[start+i]=v
assert len(roots)==len(trunks)==3

def transform(s,mode):
    years=sorted(s); assert years==list(range(years[0],years[-1]+1))
    v=np.array([s[y] for y in years],float)
    if mode=='mean_divided_width':
        v=v/v.mean()
    else:
        if mode=='standardized_log_difference': v=np.log(v)
        v=np.diff(v); years=years[1:]
        v=(v-v.mean())/v.std(ddof=1)
    return dict(zip(years,v))

def average(series):
    years=sorted(set().union(*(set(s) for s in series.values())))
    assert years==list(range(years[0],years[-1]+1))
    result={y:float(np.mean([s[y] for s in series.values() if y in s])) for y in years}
    # Independently check sums and contributing-radius counts.
    for y in years:
        values=[s[y] for s in series.values() if y in s]
        assert np.isclose(result[y],sum(values)/len(values),atol=1e-12)
    return result,{y:sum(y in s for s in series.values()) for y in years}

def scan(target,master,ty):
    my=sorted(master); x=np.array([target[y] for y in ty]); rows=[]
    for shift in range(my[0]-ty[0],my[-1]-ty[-1]+1):
        y=np.array([master[t+shift] for t in ty]); r=float(np.corrcoef(x,y)[0,1])
        xc=x-x.mean(); yc=y-y.mean()
        check=float(np.dot(xc,yc)/np.sqrt(np.dot(xc,xc)*np.dot(yc,yc)))
        assert np.isclose(r,check,atol=1e-12)
        rows.append(dict(shift=shift,assigned_end=ty[-1]+shift,r=r))
    return sorted(rows,key=lambda v:-v['r'])

rng=np.random.default_rng(4719); known=rng.normal(size=100)
assert scan(dict(zip(range(1500,1530),known[20:50])),dict(zip(range(1400,1500),known)),list(range(1500,1530)))[0]['shift']==-80

results=[]; averages=[]
for mode in ('mean_divided_width','standardized_log_difference','standardized_width_difference'):
    rr={k:transform(s,mode) for k,s in roots.items()}
    tt={k:transform(s,mode) for k,s in trunks.items()}
    # Unit rescaling each radius independently must not change these transforms.
    for k,s in {**roots,**trunks}.items():
        a=transform(s,mode); b=transform({y:10*v for y,v in s.items()},mode)
        assert np.allclose(list(a.values()),list(b.values()),atol=1e-12)
    for omitted in (None,'GF2RTA','GF2RTB','GF2RTC'):
        selected={k:s for k,s in rr.items() if k!=omitted}
        root,rd=average(selected)
        # Fix the reference calendar span across all omission choices.
        first=1400 if mode=='mean_divided_width' else 1401
        root={y:root[y] for y in range(first,1700)}
        for basis in ('all_three_trunk_radii','NW_only'):
            chosen=tt if basis=='all_three_trunk_radii' else {'CPGF2NW':tt['CPGF2NW']}
            trunk,td=average(chosen)
            if omitted is None:
                averages.append(dict(transform=mode,basis=basis,
                    root_values=[dict(year=y,value=root[y],radii=rd[y]) for y in root],
                    trunk_values=[dict(year=y,value=trunk[y],radii=td[y]) for y in trunk]))
            for scope in ('full_trunk','last_255_observations'):
                ty=sorted(trunk)
                if scope=='last_255_observations': ty=ty[-255:]
                ranked=scan(trunk,root,ty); actual=next(v for v in ranked if v['shift']==0)
                results.append(dict(transform=mode,omitted_root=omitted,basis=basis,scope=scope,
                    first_target_year=ty[0],last_target_year=ty[-1],n=len(ty),tested=len(ranked),
                    published_r=actual['r'],published_rank=ranked.index(actual)+1,
                    best=ranked[0],candidates=ranked))
assert len(results)==48
out=dict(status='DECLARED_COMBINED_RADIUS_DIAGNOSTIC_NOT_ORIGINAL_PROCESSING',
    source_ids=['S61','S229','S231'],input_sha256=inputs,numpy_version=np.__version__,
    method='Normalize each radius before averaging available values annually. Three transformations; all roots or omit one; all trunks or NW alone; full trunk span or final255 observations. Fixed root reference1400/1401–1699; all integer complete-overlap shifts retained. No gap filling.',
    limits='No decay curves, splines or AR model reproduced.255-observation subset deliberately matches reported count only, not inferred original processing. Roots and trunks are related; common inherited calendar, retrospective choice and restricted shift domain. Manual transcription unreviewed; no p-values, new dates, specimen authentication or absolute chronology test.',
    averages=averages,results=results)
(ROOT/'data/cascadia-combined-gf2.json').write_text(json.dumps(out,indent=2)+'\n')
for mode in ('mean_divided_width','standardized_log_difference','standardized_width_difference'):
    rows=[r for r in results if r['transform']==mode]
    print(mode,'rank1',sum(r['published_rank']==1 for r in rows),'of',len(rows),
          'r range',round(min(r['published_r'] for r in rows),4),round(max(r['published_r'] for r in rows),4))
    for r in rows:
        if r['omitted_root'] is None or r['published_rank']!=1:
            print(r['omitted_root'],r['basis'],r['scope'],r['n'],r['published_rank'],round(r['published_r'],5),r['best'])
