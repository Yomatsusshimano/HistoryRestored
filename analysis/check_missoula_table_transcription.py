"""Check literal table numbers against the pinned original PDF.

Usage: python analysis/check_missoula_table_transcription.py ORIGINAL.pdf
Requires pypdf. This complements scan inspection; it cannot verify gray shading,
survey correctness, interpretation, uncertainty or field-to-model registration.
"""
import argparse
import hashlib
import json
import re
from pathlib import Path
from pypdf import PdfReader

ROOT = Path(__file__).resolve().parents[1]


def check(pdf):
    data=json.loads((ROOT/'data/missoula-table1.json').read_text(encoding='utf-8'))
    assert hashlib.sha256(pdf.read_bytes()).hexdigest()==data['source_pdf_sha256'], 'PDF hash differs from registered original'
    reader=PdfReader(pdf)
    texts={5:reader.pages[5].extract_text(),6:reader.pages[6].extract_text()}
    for r in data['controls']:
        p=5 if r['table_row']<=24 else 6
        text=texts[p]
        coord=re.escape(r['printed_latitude_token'])+r'\s+'+re.escape(r['printed_longitude_w_token'])+r'\b'
        hit=re.search(coord,text)
        assert hit, r['id']
        following=[s for s in data['controls'] if s['table_row']==r['table_row']+1 and (s['table_row']<=24)==(r['table_row']<=24)]
        stop=len(text)
        if following:
            n=following[0]
            next_hit=re.search(re.escape(n['printed_latitude_token'])+r'\s+'+re.escape(n['printed_longitude_w_token'])+r'\b',text[hit.end():])
            assert next_hit, r['id']
            stop=hit.end()+next_hit.start()
        segment=text[hit.end():stop]
        nums=re.findall(r'(?<![\w.])\d+(?:\.\d+)?(?![\w.])',segment)
        ft=r['field_elevation_ft']; m=r['field_elevation_m']
        if ft is not None:
            assert re.search(r'\b'+str(ft)+r'\s+'+str(m)+r'\b',segment),r['id']
        else:
            assert str(m) in nums, r['id']
        for k in ('x_albers_m','y_albers_m','terrain_elevation_m','map_contour_interval_ft','map_contour_interval_m'):
            v=r[k]
            if v is not None: assert str(v) in nums,(r['id'],k)
        if r['x_albers_m'] is not None:
            assert re.search(r'\b'+str(r['x_albers_m'])+r'\s+'+str(r['y_albers_m'])+r'\s+'+str(r['terrain_elevation_m'])+r'\b',segment),r['id']
    print('47 rows agree with pinned PDF extraction for coordinates, ft/m pairs, contour values and projected/terrain triples. Shading and field validity are not machine-verified.')


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('pdf',type=Path)
    check(parser.parse_args().pdf)
