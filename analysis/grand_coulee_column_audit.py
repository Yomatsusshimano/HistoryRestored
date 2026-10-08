"""Read-only numeric audit of pinned GC_dimensions.xls; requires xlrd 2.0.2."""
import argparse
import hashlib
import json
from pathlib import Path
import statistics
import xlrd

ROOT=Path(__file__).resolve().parents[1]

def audit(path):
    manifest=json.loads((ROOT/'data/grand-coulee-nested-inventory.json').read_text(encoding='utf-8'))
    expected=next(e['sha256'] for a in manifest['nested_archives'] for e in a['entries'] if e['path']=='column_counts/GC_dimensions.xls')
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=expected:
        raise ValueError('Workbook does not match acquired source')
    book=xlrd.open_workbook(file_contents=raw)
    sheet=book.sheet_by_name('Columns_loc3')
    if sheet.row_values(0)[:2]!=['Width (cm)','Height (cm)']:
        raise ValueError('Unexpected measurement headers')
    rows=[]
    for row in range(1,sheet.nrows):
        values=sheet.row_values(row)[:2]
        if any(sheet.cell_type(row,c)!=xlrd.XL_CELL_NUMBER for c in (0,1)):
            raise ValueError(f'Non-numeric measurement at row {row+1}; no imputation allowed')
        rows.append(values)
    summaries={}
    for c,label in enumerate(['width','height']):
        values=[v[c] for v in rows]
        summaries[label]={'count':len(values),'minimum_raw':min(values),'maximum_raw':max(values),'median_raw':statistics.median(values),'cached_summary_value':sheet.cell_value(1,c+3),'cached_summary_header':sheet.cell_value(0,c+3),'source_range':f'{"AB"[c]}2:{"AB"[c]}{sheet.nrows}'}
    return {'source_id':'S126','workbook_sha256':expected,'reader_version':xlrd.__version__,'sheet_names':book.sheet_names(),'sheet':'Columns_loc3','raw_headers':sheet.row_values(0)[:2],'summaries':summaries,'accepted_measurement_unit':None,'unit_resolution':'Unresolved: raw headers say cm; cached median headers say m. No conversion applied.','summit_sheet_present': 'Columns_loc1_2' in book.sheet_names(),'limits':'Cached summaries read, not formula recalculation. No measurement precision, representativeness, cohesion or erosion threshold validated.'}

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('workbook',type=Path)
    result=audit(parser.parse_args().workbook)
    (ROOT/'analysis/grand-coulee-column-audit-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
