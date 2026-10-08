"""Audit published series coverage against S1; does not reproduce crossdating."""
import csv
import hashlib
import io
import json
from pathlib import Path
import re
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://www.ncei.noaa.gov/pub/data/paleo/treering/measurements/northamerica/usa/wa171-rwl-noaa.txt'
SHA = 'cb02dbf945b0b022e199b33f9e7c3470d9dff7302c8013f34e87b1200c57bd01'
path = ROOT / 'tmp/research/wa171-rwl-noaa.txt'
if not path.exists():
    path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(URL, timeout=30) as response:
        path.write_bytes(response.read())
raw = path.read_bytes()
assert hashlib.sha256(raw).hexdigest() == SHA, 'Source changed; inspect before use'
rows = [line.split('\t') for line in raw.decode('utf-8').splitlines()
        if line and not line.startswith('#')]
header, records = rows[0], rows[1:]
assert header[0] == 'age_CE' and len(set(header)) == len(header)
assert all(len(row) == len(header) for row in records)
years = [int(row[0]) for row in records]
assert years == list(range(min(years), max(years) + 1))
groups = {}
for col, name in enumerate(header[1:], 1):
    match = re.fullmatch(r'((?:ELE|KAP)\d{3})[A-Z]\d+_raw', name)
    assert match, name
    present = [int(row[0]) for row in records if row[col] != 'NA']
    assert present, name
    assert all(float(row[col]) >= 0 for row in records if row[col] != 'NA')
    groups.setdefault(match[1], []).append(dict(series=name, first=min(present),
        last=max(present), observations=len(present),
        internal_missing=max(present)-min(present)+1-len(present)))
table = list(csv.reader(io.StringIO((ROOT/'sources/originals/electron/C14_data_S1.csv').read_bytes().decode('cp1252'))))
expected = {r[0]: dict(transects=int(r[2]), first=int(r[3]), last=int(r[4]))
            for r in table if r and re.fullmatch(r'(ELE|KAP)\d{3}', r[0])}
assert set(expected) == set(groups), 'Tree identifiers differ'
trees = []
for tree, series in groups.items():
    observed = dict(transects=len(series), first=min(s['first'] for s in series),
                    last=max(s['last'] for s in series))
    trees.append(dict(tree=tree, observed=observed, table_S1=expected[tree],
                      agrees=observed == expected[tree], series=series))
out = dict(source_ids=['S72', 'S74'], input_url=URL, input_sha256=SHA,
    series_count=len(header)-1, tree_id_count=len(groups),
    first_assigned_year=min(years), last_assigned_year=max(years),
    calendar_rows=len(years), observed_widths=sum(s['observations'] for t in trees for s in t['series']),
    all_tree_summaries_agree=all(t['agrees'] for t in trees), trees=trees,
    crossdating_reproduced=False,
    limitations='Counts and ranges in the published assignment only. Tree-ID grouping follows archive labels; it is not independent specimen authentication. Neither absolute years, bark preservation, chronology standardization nor external matching are validated here.')
(ROOT/'analysis/electron-measurement-coverage.json').write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
print(json.dumps({k:v for k,v in out.items() if k != 'trees'}, indent=2))
print('Disagreements:', json.dumps([t for t in trees if not t['agrees']]))
