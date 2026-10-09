"""Audit archived USGS field-table labels, not dates or specimen custody."""
import csv
import hashlib
import io
import json
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
def digest(raw):
    return hashlib.sha256(raw).hexdigest()

acquisition = json.loads((ROOT / 'data/cascadia-field-acquisition.json').read_text())
item = next(f for f in acquisition['files'] if f['name'] == 'plain.zip')
raw = (ROOT / item['file']).read_bytes()
assert digest(raw) == item['sha256']
z = zipfile.ZipFile(io.BytesIO(raw))
assert len(z.namelist()) == 19
members = [{'name': n, 'bytes': len(z.read(n)), 'sha256': digest(z.read(n))}
           for n in z.namelist()]
def rows(name):
    # Source CSVs use a legacy single-byte encoding; preserve original ZIP bytes.
    return list(csv.DictReader(io.StringIO(z.read(name).decode('cp1252'))))
def meaningful(record):
    return any(str(v).strip() for v in record.values() if v is not None)

tables = {}
for n in ['10_Redcedar_dead_georeferenced.csv', '11_Redcedar_dead_sampled.csv',
          '12_Redcedar_dead_selected.csv', '13_Redcedar_live.csv']:
    parsed = rows(n)
    tables[n] = {'parsed_rows': len(parsed),
                 'nonblank_rows': sum(meaningful(r) for r in parsed)}
    if 'FieldID' in parsed[0]:
        tables[n]['rows_with_field_id'] = sum(bool(r['FieldID'].strip()) for r in parsed)

gf2 = {}
for n in list(tables)[:3]:
    matched = [r for r in rows(n) if r['FieldID'] == 'GF2']
    assert len(matched) == 1
    gf2[n] = {k: v for k, v in matched[0].items() if k and v.strip()}
assert all(r['Longitude'] == '-124.1632' and r['Latitude'] == '47.1316'
           for r in gf2.values())
assert gf2['12_Redcedar_dead_selected.csv']['RootBarkYr'] == '1699'

audit_path = ROOT / 'data/cascadia-raw-audit.json'
audit_raw = audit_path.read_bytes()
audit = json.loads(audit_raw)
reference = next(f for f in audit['files'] if f['file'].endswith('wa129.rwl'))
by_name = {s['id']: s for s in reference['series']}
mapping = {str(i): [f'LI{i}'] for i in range(745, 770)}
mapping.update({'701': ['LIDY701'], '702': ['LI702O'], '768': ['LIDY768'],
                '766': ['LI766I', 'LI766O'], '767': ['LI767I', 'LI767O']})
crosswalk = []
for r in rows('13_Redcedar_live.csv'):
    if r['Category'] != 'Witness':
        continue
    names = mapping[r['TreeID']]
    linked = [by_name[n] for n in names]
    years = set()
    for s in linked:
        years.update(range(s['start'], s['end'] + 1))
    first, last = min(years), max(years)
    crosswalk.append({'field_id': r['TreeID'], 'source_row': r,
                      'archived_series': linked, 'archived_union_first': first,
                      'archived_union_last': last, 'archived_unique_years': len(years),
                      'archived_span_years': last-first+1,
                      'source_first_matches': int(r['EarliestYr']) == first,
                      'source_last_matches': int(r['LatestYr']) == last,
                      'source_count_matches_union': int(r['RingCount']) == len(years)})
assert len(crosswalk) == 19
assert sum(len(r['archived_series']) for r in crosswalk) == 21
assert {s['id'] for r in crosswalk for s in r['archived_series']} == set(by_name)
exceptions = [r['field_id'] for r in crosswalk if not all(
    r[k] for k in ['source_first_matches', 'source_last_matches', 'source_count_matches_union'])]
assert exceptions == ['767', '702']

out = {'status': 'SOURCE_FIELD_TABLE_AND_LABEL_AUDIT_NOT_INDEPENDENT_AUTHENTICATION',
       'source_id': 'S244', 'input_zip_sha256': digest(raw),
       'raw_audit_sha256': digest(audit_raw), 'members': members,
       'table_counts': tables, 'gf2_source_rows': gf2,
       'reference_tree_crosswalk': crosswalk, 'reference_label_exceptions': exceptions,
       'limits': ['Coordinates and dates are source reports, not new measurements.',
                  'Matching related tables is not independent confirmation.',
                  'Nineteen trees account for twenty-one measurement series.',
                  'Processing outputs, original field scans and current custody remain unverified.']}
(ROOT / 'data/cascadia-field-audit.json').write_text(json.dumps(out, indent=2) + '\n')
print('GF2 source rows: 3; Long Island trees: 19; measurement series: 21')
print('Reference label exceptions:', exceptions)
print('Table row counts:', tables)
