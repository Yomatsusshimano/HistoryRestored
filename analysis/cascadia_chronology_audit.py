"""Audit archived Long Island chronology versions; not original dating reproduction."""
import hashlib
import json
from pathlib import Path
import statistics

ROOT = Path(__file__).resolve().parents[1]
ledger = json.loads((ROOT/'data/cascadia-chronology-acquisition.json').read_text())
files = {}
for item in ledger['files']:
    raw = (ROOT/item['file']).read_bytes()
    assert hashlib.sha256(raw).hexdigest() == item['sha256']
    files[Path(item['file']).name] = raw.decode('utf-8')
summaries = []
for suffix, kind in [('', 'standard'), ('a', 'ARSTAN'), ('r', 'residual')]:
    name = f'wa129{suffix}.crn'
    text = files[name]
    decadal, missing = {}, []
    for line in text.splitlines()[3:]:
        if not line.strip():
            continue
        # Partial opening decade retains ten slots, including 9990 placeholders.
        decade = (int(line[6:10])//10)*10
        for i in range(10):
            cell = line[10+7*i:17+7*i]
            if not cell.strip():
                continue
            value, n = int(cell[:4]), int(cell[4:])
            year = decade+i
            assert year not in decadal
            if value == 9990:
                assert n == 0
                missing.append(year)
            else:
                assert n > 0
                decadal[year] = (value, n)
    template = {}
    for line in files[f'wa129{suffix}-crn-noaa.txt'].splitlines():
        if not line or line.startswith('#') or line.startswith('age_CE'):
            continue
        year, value, n = line.split()
        year, scaled = int(year), float(value)*1000
        assert abs(scaled-round(scaled)) < 1e-8 and year not in template
        template[year] = (round(scaled), int(n))
    assert decadal == template, 'Decadal/template mismatch: '+name
    years = sorted(decadal)
    assert years == list(range(years[0], years[-1]+1))
    depth = [decadal[y][1] for y in years]
    summaries.append(dict(file=name,version=kind,header=text.splitlines()[:3],
                          first_valid_year=years[0],last_valid_year=years[-1],
                          valid_year_count=len(years),missing_slots=missing,
                          sample_count_min=min(depth),sample_count_max=max(depth),
                          sample_count_median=statistics.median(depth),
                          sample_count_1699=decadal[1699][1],
                          template_correspondence='All valid assigned years, index values and sample counts match exactly.',
                          values=[dict(year=y,index=decadal[y][0]/1000,sample_count=decadal[y][1]) for y in years]))
result=dict(source_ids=['S233','S230'],status='ARCHIVED_PROCESSED_OUTPUT_RECOVERED_NOT_1997_VERSION_AUTHENTICATED',
            method='Fixed-column Tucson decadal parser; 9990 missing code omitted; compare independently tabulated NOAA template rows exactly at integer index scale.',
            limits='Archived chronology labels and assigned years inherited. Template copies are dependent records. Sample counts are source fields, not independently verified tree identities. No per-radius settings or 1997 input version authenticated.',
            versions=summaries)
(ROOT/'data/cascadia-chronology-audit.json').write_text(json.dumps(result,indent=2)+'\n')
for s in summaries:
    print(s['version'],s['first_valid_year'],s['last_valid_year'],s['valid_year_count'],
          'sample count',s['sample_count_min'],s['sample_count_max'],s['sample_count_median'],
          '1699',s['sample_count_1699'],'missing',s['missing_slots'])
