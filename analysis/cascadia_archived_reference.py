"""Declared first-difference snag tests against archived processed reference versions."""
from pathlib import Path
import hashlib
import json
import numpy as np

ROOT = Path(__file__).resolve().parents[1]

def widths(item):
    raw = (ROOT/item['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item['sha256']
    result = {}
    for line in raw.decode('utf-8-sig').splitlines()[3:]:
        row = line.split()
        if not row:
            continue
        name, first = row[0], int(row[1])
        record = result.setdefault(name, {})
        for i, value in enumerate(map(int, row[2:])):
            if value in (999, -9999):
                continue
            assert value > 0 and first+i not in record
            record[first+i] = value
    return result

def difference(record, mode):
    years = sorted(record)
    assert years == list(range(years[0], years[-1]+1))
    values = np.array([record[y] for y in years], float)
    assert np.all(values > 0)
    if mode == 'log_difference':
        values = np.log(values)
    return years[1:], np.diff(values)

def scan(target_years, target_values, master_years, master_values):
    lo = master_years[0]-target_years[0]
    hi = master_years[-1]-target_years[-1]
    x = target_values-target_values.mean()
    correlations = []
    for shift in range(lo, hi+1):
        offset = target_years[0]+shift-master_years[0]
        y = master_values[offset:offset+len(x)]
        y = y-y.mean()
        correlations.append(float(np.dot(x,y)/np.sqrt(np.dot(x,x)*np.dot(y,y))))
    return lo, correlations

# Known nonperiodic signal tests both shift sign and full-window alignment.
rng = np.random.default_rng(1143)
z = rng.normal(size=500)
lo, values = scan(list(range(1500,1700)),z[100:300],list(range(1000,1500)),z)
assert lo+int(np.argmax(values)) == -400

chron_ledger = json.loads((ROOT/'data/cascadia-chronology-acquisition.json').read_text())
masters = {}
for item in chron_ledger['files']:
    name = Path(item['file']).name
    if not name.endswith('-crn-noaa.txt'):
        continue
    raw = (ROOT/item['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item['sha256']
    record, depth = {}, {}
    for line in raw.decode().splitlines():
        if not line or line.startswith('#') or line.startswith('age_CE'):
            continue
        y, v, n = line.split()
        record[int(y)], depth[int(y)] = float(v), int(n)
    kind = {'wa129-crn-noaa.txt':'standard', 'wa129a-crn-noaa.txt':'ARSTAN',
            'wa129r-crn-noaa.txt':'residual'}[name]
    masters[kind] = (record, depth, item['sha256'])
raw_ledger = json.loads((ROOT/'data/cascadia-raw-acquisition.json').read_text())
targets = {}
for item in raw_ledger['files'][1:]:
    for name, record in widths(item).items():
        assert name not in targets
        targets[name] = (record, item['sha256'])
assert len(targets) == 27
results = []
for kind, (master, depth, sha) in masters.items():
    for mode in ('log_difference','width_difference'):
        my, mv = difference(master,mode)
        rows = []
        for name, (record,target_sha) in targets.items():
            ty,tv = difference(record,mode)
            lo, correlations = scan(ty,tv,my,mv)
            actual = correlations[-lo]
            offset = ty[0]-my[0]
            assert np.isclose(actual,np.corrcoef(tv,mv[offset:offset+len(tv)])[0,1],atol=1e-12)
            if name == 'CPGF2NW':
                _, scaled = difference({y:10*v for y,v in record.items()},mode)
                _, check = scan(ty,scaled,my,mv)
                assert np.allclose(correlations,check,atol=1e-12)
            def candidate(shift):
                counts = [min(depth[y+shift],depth[y+shift-1]) for y in ty]
                return dict(shift=shift,assigned_end=ty[-1]+shift,r=correlations[shift-lo],
                            reference_count_min=min(counts),reference_count_median=float(np.median(counts)))
            scopes = {}
            for bound in (1720,1986):
                eligible = [s for s in range(lo,lo+len(correlations)) if ty[-1]+s <= bound]
                ranked = sorted(eligible,key=lambda s:-correlations[s-lo])
                scopes[str(bound)] = dict(tested=len(ranked),published_rank=ranked.index(0)+1,
                                         best=candidate(ranked[0]),top_five=[candidate(s) for s in ranked[:5]])
            rows.append(dict(id=name,raw_sha256=target_sha,n_differences=len(tv),
                             published_end=max(record),published_r=actual,
                             published_reference_count=candidate(0),
                             first_candidate_shift=lo,all_candidate_r=correlations,scopes=scopes))
        results.append(dict(reference_version=kind,reference_template_sha256=sha,transform=mode,rows=rows))
out = dict(status='ARCHIVED_REFERENCE_DIAGNOSTIC_NOT_ORIGINAL_METHOD_REPRODUCTION',
           source_ids=['S229','S233'],numpy_version=np.__version__,
           choices='Both target widths and archived indices differenced (log or linear). Full target overlap, all integer shifts, endpoints bounded separately by1720 and1986. No reference-depth or minimum-length exclusion; no significance probabilities. Reference count diagnostic is the minimum reported count of the two years contributing to each difference.',
           limits='Archived references already processed; additional differencing is a declared diagnostic, not original spline/AR method. Twenty-seven dependent series, not trees. Calendar inherited; original file identity and target processing unknown. Bound1720 inherits radiocarbon dating. No root endpoints or revised dates.',results=results)
(ROOT/'data/cascadia-archived-reference.json').write_text(json.dumps(out,indent=2)+'\n')
for result in results:
    counts={b:sum(r['scopes'][b]['published_rank']==1 for r in result['rows']) for b in ('1720','1986')}
    print(result['reference_version'],result['transform'],counts,'of27')
    for row in result['rows']:
        if row['scopes']['1720']['published_rank'] != 1 or row['id'] == 'CP790':
            print(row['id'],'rank',row['scopes']['1720']['published_rank'],
                  'r',round(row['published_r'],5),'best',row['scopes']['1720']['best'])
