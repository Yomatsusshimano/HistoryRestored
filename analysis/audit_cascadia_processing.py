"""Check archived processing-output identity and record counts, not dating."""
from pathlib import Path
import hashlib,json,urllib.request
ROOT=Path(__file__).resolve().parents[1]
ledger=json.loads((ROOT/'data/cascadia-stats-acquisition.json').read_text())
texts=[]
for item in ledger['files']:
    local=ROOT/item['file']
    raw=local.read_bytes() if local.exists() else urllib.request.urlopen(item['url'],timeout=30).read()
    assert hashlib.sha256(raw).hexdigest()==item['sha256']
    texts.append(raw.decode('cp1252'))
marker='Supplementary information for'
supp=[t[t.index(marker):t.index('\n COFECHA')].strip() for t in texts]
assert len(set(supp))==1, 'Supplement copies differ; inspect before merging evidence'
t=texts[0].split('PART 7:')[1]
rows=[]
for line in t.splitlines():
    tokens=line.split()
    if len(tokens)==17 and tokens[0].isdigit():
        rows.append(dict(id=tokens[1],start=int(tokens[2]),end=int(tokens[3]),
                         years=int(tokens[4]),segments=int(tokens[5]),flags=int(tokens[6]),
                         correlation_with_master=float(tokens[7]),ar_order=int(tokens[-1])))
raw_audit=json.loads((ROOT/'data/cascadia-raw-audit.json').read_text())['files'][0]
assert len(rows)==21
by_id={r['id']:r for r in rows}
for s in raw_audit['series']:
    r=by_id[s['id']]
    assert (s['start'],s['end'],s['count'])==(r['start'],r['end'],r['years'])
out=dict(source_id='S231',status='ARCHIVED_OUTPUT_ACCOUNTING_NOT_COFECHA_REPRODUCTION',
         supplement_body_identical_across_five_files=True,
         normalized_body_sha256=hashlib.sha256(supp[0].encode()).hexdigest(),
         qc_date='2006-05-25',qc_spline_years=32,qc_segment_years=50,qc_lag_years=25,
         years=sum(r['years'] for r in rows),segments=sum(r['segments'] for r in rows),
         flags=sum(r['flags'] for r in rows),rows=rows,
         limitations='Overlapping segments are not independent. Flags are diagnostics, not proven dating errors. 2006 QC processing is not the 1997 analysis.')
assert (out['years'],out['segments'],out['flags'])==(9067,359,123)
(ROOT/'data/cascadia-processing-audit.json').write_text(json.dumps(out,indent=2)+'\n')
print(out['years'],out['segments'],out['flags'],'all21 raw extents match; five supplement bodies identical')
