"""Inventory published RWL labels; no crossdating or new calendar assignment."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ledger = json.loads((ROOT / 'data/cascadia-raw-acquisition.json').read_text())
results = []
for item in ledger['files']:
    raw = (ROOT / item['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item['sha256']
    series = {}
    for line_no, line in enumerate(raw.decode('utf-8-sig').splitlines()[3:], 4):
        if not line.strip():
            continue
        tokens = line.split()
        name, start = tokens[0], int(tokens[1])
        row = [int(v) for v in tokens[2:]]
        s = series.setdefault(name, {'years': [], 'values': [], 'markers': []})
        for offset, value in enumerate(row):
            if value in (-9999, 999):
                assert offset == len(row)-1, (name, line_no, 'nonterminal marker')
                s['markers'].append({'line': line_no, 'value': value})
                continue
            assert value >= 0, (name, line_no, value)
            year = start + offset
            assert year not in s['years'], (name, year)
            s['years'].append(year)
            s['values'].append(value)
    summary=[]
    for name,s in series.items():
        assert len(s['markers']) == 1, (name, s['markers'])
        assert s['years'] == list(range(min(s['years']),max(s['years'])+1)), name
        summary.append(dict(id=name,start=min(s['years']),end=max(s['years']),
                            count=len(s['years']),terminator=s['markers'][0],
                            millimetres_per_integer=0.01 if s['markers'][0]['value']==999 else 0.001))
    results.append(dict(file=item['file'],series_count=len(summary),
                        first_assigned_year=min(s['start'] for s in summary),
                        last_assigned_year=max(s['end'] for s in summary),series=summary))
out=dict(status='FILE_STRUCTURE_AND_ASSIGNED_LABEL_AUDIT_NOT_CROSSDATING',
         units='Scale inferred per series from NOAA treeinfo.txt terminal codes; no width conversion performed.',
         limits='Series are not independent trees. Terminal trunk years are not death dates. Sentinels excluded; no dates independently established.',files=results)
(ROOT/'data/cascadia-raw-audit.json').write_text(json.dumps(out,indent=2)+'\n')
for r in results:
    print(r['file'],r['series_count'],r['first_assigned_year'],r['last_assigned_year'])
