"""Inspect the published NOAA subset; optionally verify extraction against local originals.

Usage: python research/check_secvr_lakes.py [--source-dir tmp/research/secvr]
Original files and their FTP URLs/SHA256 hashes are listed in the JSON manifest.
Fields are original strings; blank fields are not zero or dated observations.
"""
import argparse
import csv
import hashlib
import json
from decimal import Decimal, ROUND_DOWN
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def inspect(data):
    result = {}
    for lake in ('Fish Lake', 'Mono Lake'):
        result[lake] = {}
        for name, age_field in [('LAKESTACK', 'AGE'), ('LAKESMOOTH', 'C14AGES')]:
            table = data['tables'][name]
            rows = [dict(zip(table['columns'], r['values'])) for r in table['rows']
                    if r['values'][0] == lake]
            ages = [int(r[age_field]) for r in rows]
            assert len({r['RESNO'] for r in rows}) == len(rows)
            assert all(r['CALAGES'] == '' for r in rows) if name == 'LAKESMOOTH' else True
            result[lake][name] = {'rows': len(rows), 'age_min': min(ages),
                                 'age_max': max(ages),
                                 'rows_in_12300_13100': sum(12300 <= a <= 13100 for a in ages)}
        t = data['tables']['C14AGES']
        assay_rows = [r['values'] for r in t['rows'] if r['values'][0] == lake]
        assert len(assay_rows) == 1 and all(v == '' for v in assay_rows[0][1:])
        result[lake]['populated_assay_rows'] = 0
    stack = data['tables']['LAKESTACK']['rows']
    smooth = data['tables']['LAKESMOOTH']['rows']
    a = [r['values'] for r in stack if r['values'][0] == 'Mono Lake']
    b = [r['values'][:3] + r['values'][4:] for r in smooth if r['values'][0] == 'Mono Lake']
    assert a == b
    result['mono_smooth_equals_stack_after_blank_CALAGES_removed'] = True
    for row in data['mdb_comparison']['depth_differences']:
        assert Decimal(row['mdb_depth']).quantize(Decimal('.01'), rounding=ROUND_DOWN) == Decimal(row['ascii_depth'])
        table = data['tables'][row['table']]
        original = next(r['values'] for r in table['rows']
                        if r['values'][:2] == [row['site'], row['resno']])
        assert original[table['columns'].index('DEPTH')] == row['ascii_depth']
    result['MDB_ASCII_depth_differences'] = len(data['mdb_comparison']['depth_differences'])
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--source-dir', type=Path)
    args = parser.parse_args()
    data = json.loads((ROOT / 'data/secvr-lake-subset.json').read_text(encoding='utf-8'))
    if args.source_dir:
        for name, table in data['tables'].items():
            raw = (args.source_dir / (name + '.txt')).read_bytes()
            assert hashlib.sha256(raw).hexdigest() == table['sha256'], name
            rows = list(csv.reader(raw.decode('cp1252').splitlines(), delimiter=';'))
            for row in table['rows']:
                assert rows[row['source_line'] - 1] == row['values'], (name, row['source_line'])
            selected = [(i+1, r) for i, r in enumerate(rows)
                        if (r[0] in ('12', '18') if name == 'REFSECVR'
                            else any(v in ('Fish Lake', 'Mono Lake') for v in r))]
            assert selected == [(r['source_line'], r['values']) for r in table['rows']], name
        print('Original file hashes, line values and complete target selection verified.')
    print(json.dumps(inspect(data), indent=2))


if __name__ == '__main__':
    main()
