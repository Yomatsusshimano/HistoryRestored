"""Coverage of an unconfirmed reference candidate; no crossdating."""
import hashlib
import json
from pathlib import Path
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
URL = 'https://www.ncei.noaa.gov/pub/data/paleo/treering/measurements/northamerica/usa/wa027-rwl-noaa.txt'
EXPECTED = '24e989136dcc7deb2128a994678cbe25729b2d582ab7708145a13a389d657b08'
path = ROOT/'tmp/research/wa027-rwl-noaa.txt'
if not path.exists():
    path.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(URL, timeout=30) as response:
        path.write_bytes(response.read())
data = path.read_bytes()
assert hashlib.sha256(data).hexdigest() == EXPECTED, 'Source changed; review before use'
rows = [line.split('\t') for line in data.decode('utf-8').splitlines()
        if line and not line.startswith('#')]
header, records = rows[0], rows[1:]
assert header[0] == 'age_CE'
assert all(len(row) == len(header) for row in records)
years = [int(row[0]) for row in records]
assert years == list(range(1397,1977))
selected = [row for row in records if 1397 <= int(row[0]) <= 1446]
counts = [sum(value != 'NA' for value in row[1:]) for row in selected]
series = []
for column, name in enumerate(header[1:], 1):
    present = [int(row[0]) for row in selected if row[column] != 'NA']
    if present:
        series.append(dict(series=name,first_year=present[0],last_year=present[-1],observed_years=len(present)))
out = dict(source_id='S70',input_sha256=EXPECTED,candidate_identity='UNCONFIRMED',
           proposed_final_ring=1446,reference_start=1397,maximum_overlap_years=len(selected),
           observed_series=series,total_series_years=sum(counts),
           minimum_annual_series_count=min(counts),maximum_annual_series_count=max(counts),
           mean_annual_series_count=sum(counts)/len(counts),
           independent_tree_count=None,crossdating_reproduced=False,
           limitations='Coverage only. Does not establish specimen independence, reference identity, accuracy of assigned years, or statistical strength of any match.')
(ROOT/'analysis/bonneville-reference-coverage.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out,indent=2))
