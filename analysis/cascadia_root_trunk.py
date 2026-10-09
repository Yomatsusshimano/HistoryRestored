"""Candidate GF2 root/trunk relative alignments; not absolute crossdating."""
import hashlib,json
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
root_path=ROOT/'data/cascadia-width-extract.json'
roots_data=json.loads(root_path.read_text())
roots={s['id']:{s['start_year']+i:v for i,v in enumerate(s['widths'])}
       for s in roots_data['series'] if s['id'] in ('GF2RTC','GF2RTB')}
ledger=json.loads((ROOT/'data/cascadia-raw-acquisition.json').read_text())
item=next(i for i in ledger['files'] if i['file'].endswith('wa130.rwl'))
raw=(ROOT/item['file']).read_bytes();assert hashlib.sha256(raw).hexdigest()==item['sha256']
trunks={}
for line in raw.decode().splitlines()[3:]:
    row=line.split()
    if not row or not row[0].startswith('CPGF2'):continue
    name,start=row[0],int(row[1]);s=trunks.setdefault(name,{})
    for i,v in enumerate(map(int,row[2:])):
        if v in (999,-9999):continue
        assert v>0 and start+i not in s
        s[start+i]=v

def transform(s,kind):
    years=sorted(s);assert years==list(range(years[0],years[-1]+1))
    x=np.array([s[y] for y in years],float)
    if kind=='log_difference':x=np.log(x)
    if kind!='raw_width':x=np.diff(x);years=years[1:]
    return dict(zip(years,x))

results=[]
for mode in ('raw_width','log_difference','width_difference'):
    for rn,rs in roots.items():
        r=transform(rs,mode)
        for tn,ts in trunks.items():
            t=transform(ts,mode);ty=sorted(t);ry=sorted(r)
            x=np.array([t[y] for y in ty]);candidates=[]
            for delta in range(ry[0]-ty[0],ry[-1]-ty[-1]+1):
                y=np.array([r[v+delta] for v in ty])
                correlation=float(np.corrcoef(x,y)[0,1])
                candidates.append(dict(shift=delta,end=ty[-1]+delta,r=correlation))
            ranked=sorted(candidates,key=lambda c:-c['r'])
            actual=next(c for c in ranked if c['shift']==0)
            y=np.array([r[v] for v in ty]);xc=x-x.mean();yc=y-y.mean()
            assert np.isclose(actual['r'],np.dot(xc,yc)/np.sqrt(np.dot(xc,xc)*np.dot(yc,yc)),atol=1e-12)
            results.append(dict(transform=mode,root=rn,trunk=tn,n=len(ty),tested=len(ranked),
                                published_rank=next(i+1 for i,c in enumerate(ranked) if c['shift']==0),
                                published_r=actual['r'],best=ranked[0],candidates=ranked))
out=dict(status='CANDIDATE_SPECIMEN_LINK_RELATIVE_PATTERN_DIAGNOSTIC',
         source_ids=['S61','S229'],root_transcription_sha256=hashlib.sha256(root_path.read_bytes()).hexdigest(),
         trunk_file_sha256=item['sha256'],numpy_version=np.__version__,
         specimen_link='GF2 versus CPGF2 is a candidate based on site/tree labels and published context, not a verified physical specimen crosswalk.',
         method='Individual root versus trunk series; Pearson across every integer shift with full trunk overlap. Raw width and two adjacent-difference transformations. No spline or AR processing.',
         limits='Related radii, inherited years, short local shift domain, manual root transcription; no p-values, absolute year, physical chain of custody or final-ring anatomy independently verified.',results=results)
(ROOT/'data/cascadia-root-trunk.json').write_text(json.dumps(out,indent=2)+'\n')
for r in results:print(r['transform'],r['root'],r['trunk'],r['n'],r['tested'],r['published_rank'],round(r['published_r'],4),r['best'])
