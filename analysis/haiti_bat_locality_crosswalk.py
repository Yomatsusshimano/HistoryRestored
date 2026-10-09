"""Read original locality cells and compare labels without assigning a specimen."""
from collections import Counter
from decimal import Decimal
import hashlib
import json
from pathlib import Path
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
source = ROOT / 'sources/originals/wildlife/bats2017/pone.0178066.s001.xlsx'
bat_file = ROOT / 'data/jeremie-bat2015-date.json'
book = openpyxl.load_workbook(source, read_only=True, data_only=False)
sheet = book['Sheet1']
header = [cell.value for cell in sheet[1]]
rows = []
formulas = []
for cells in sheet.iter_rows(min_row=2):
    if not any(c.value is not None for c in cells):
        continue
    rows.append({'excel_row': cells[0].row,
                 'raw_cells': {c.coordinate: c.value for c in cells},
                 'fields': dict(zip(header, [c.value for c in cells]))})
    formulas.extend(c.coordinate for c in cells if c.data_type == 'f')
bat = json.loads(bat_file.read_text(encoding='utf-8'))
point = bat['locality_label']
quantum = Decimal('0.00001')
def five(value):
    return Decimal(str(value)).quantize(quantum)

matches = [r for r in rows if
           five(r['fields']['Latitude']) == five(point['latitude_as_printed']) and
           five(r['fields']['Longitude']) == five(point['longitude_as_printed'])]
jeremie = [r for r in rows if 'jeremie' in str(r['fields']['Specific Locality']).lower()]
assert len(rows) == 36 and len(matches) == 1 and not formulas
result = {
    'date': '2026-10-09',
    'source_id': 'S324',
    'original_workbook_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
    'bat_record_sha256': hashlib.sha256(bat_file.read_bytes()).hexdigest(),
    'sheet': sheet.title,
    'range_read': sheet.calculate_dimension(),
    'rows': rows,
    'formula_cells': formulas,
    'basis_counts': dict(Counter(r['fields']['Basis of record'] for r in rows)),
    'jeremie_name_rows': jeremie,
    'comparison': {
        'method': 'Numeric latitude and longitude rounded separately to five decimal places; no spatial transformation or distance estimate',
        'bat2015_printed_point': point,
        'matching_rows': matches,
        'cave_identity_authenticated': False,
        'dated_bone_accession_authenticated': False,
        'same_deposit_established': False
    },
    'limits': [
        'Numeric agreement is documentary linkage, not measured spatial accuracy or specimen custody.',
        'S1 assigns Trou Jeremie #1, whereas S318 names the sloth context Jérémie #5; cause unresolved.',
        'New-locality elevations estimated with GoogleEarth according to supporting-information caption; not independent elevation measurements.',
        'Unknown datum, coordinate uncertainty and dated-bone accession stay unknown.',
        'S2 specimen list concerns Trouing Jean Paul, not the 2015 dated Jérémie humerus.'
    ]
}
out = ROOT / 'data/haiti-bat2017-locality-crosswalk.json'
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('Read', len(rows), 'localities:', result['basis_counts'])
print('Five-decimal match:', matches[0]['excel_row'], matches[0]['fields']['Specific Locality'])
