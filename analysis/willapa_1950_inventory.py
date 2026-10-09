"""Audit the preserved NOAA 1950 inventory; requires pyshp (shapefile).

Run from repository root: python analysis/willapa_1950_inventory.py
This checks inventory contents, not whether a physical photograph survives.
"""
from collections import Counter
from io import BytesIO
from pathlib import Path
import hashlib
import json
import zipfile
import shapefile

ARCHIVE = Path('sources/originals/cascadia/NOAA_NGS_IMAGERY_1950.ZIP')
EXPECTED_SHA256 = '0f5bcfae1bbca5efb0da2fed87e5dac9cc6c901d38df70446a58b669620f314c'
QUERY = [-124.3, 46.4, -123.9, 46.85]  # west,south,east,north; NAD83 degrees


def overlaps(a, b):
    return a[0] <= b[2] and a[2] >= b[0] and a[1] <= b[3] and a[3] >= b[1]


def audit():
    payload = ARCHIVE.read_bytes()
    digest = hashlib.sha256(payload).hexdigest()
    assert digest == EXPECTED_SHA256, 'Unexpected inventory version'
    with zipfile.ZipFile(BytesIO(payload)) as z:
        members = z.namelist()
        def member(suffix):
            matches = [n for n in members if n.lower().endswith(suffix)]
            assert len(matches) == 1, (suffix, matches)
            return z.read(matches[0])
        reader = shapefile.Reader(shp=BytesIO(member('.shp')),
                                  shx=BytesIO(member('.shx')),
                                  dbf=BytesIO(member('.dbf')))
        prj = member('.prj').decode('utf-8')
        assert 'GCS_North_American_1983' in prj and 'Degree' in prj
        rows = []
        for index, item in enumerate(reader.iterShapeRecords()):
            rows.append({'row_index': index, 'attributes': item.record.as_dict(),
                         'bbox': list(item.shape.bbox)})
    wa = [r for r in rows if r['attributes']['State'].strip() == 'WA']
    targets = [r for r in rows if r['attributes']['ExposeNum'].strip() in ('1613', '1614')]
    nearby = [r for r in rows if overlaps(r['bbox'], QUERY)]
    result = {
        'source_id': 'S267', 'accessed_date': '2026-10-09',
        'url': 'https://www.ngs.noaa.gov/web/APOS2/download/shp/NOAA_NGS_IMAGERY_1950.ZIP',
        'local_copy': ARCHIVE.as_posix(), 'bytes': len(payload), 'sha256': digest,
        'coordinate_reference_text': prj, 'query_bbox_west_south_east_north': QUERY,
        'selection_method': 'Inclusive footprint bounding-box intersection; no point-center substitution',
        'total_records': len(rows), 'washington_records': len(wa),
        'washington_roll_counts': dict(sorted(Counter(r['attributes']['RollNumber'].strip() for r in wa).items())),
        'washington_reported_center_extent': {
            'longitude': [min(r['attributes']['Longitude'] for r in wa), max(r['attributes']['Longitude'] for r in wa)],
            'latitude': [min(r['attributes']['Latitude'] for r in wa), max(r['attributes']['Latitude'] for r in wa)]},
        'exposure_1613_or_1614_matches': targets, 'query_bbox_matches': nearby,
        'limits': ['Inventory absence does not establish physical loss or absence of survey.',
                   'Exposure number is not a unique cross-year identifier; target also requires roll/date/place authentication.',
                   'No original image, annotated enlargement or field sheet recovered.']}
    assert len(rows) == 1479 and len(wa) == 48
    assert len(targets) == 0 and len(nearby) == 0
    return result


if __name__ == '__main__':
    result = audit()
    Path('data/willapa-1950-inventory.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(f"Inventory audited: {result['total_records']} records, {result['washington_records']} WA; zero target-number or query-bbox matches.")
