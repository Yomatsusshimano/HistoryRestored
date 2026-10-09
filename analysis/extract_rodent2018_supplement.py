"""Extract original OOXML table cells and join exact museum IDs, without dating corrections."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZipFile
import xml.etree.ElementTree as E

ROOT=Path(__file__).resolve().parents[1]
NS={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

def key(text):return re.sub(r'\s+','',text).upper()

def main(source):
    raw=source.read_bytes()
    doc=E.fromstring(ZipFile(source).read('word/document.xml'))
    tables=[]
    for number,table in enumerate(doc.findall('.//w:tbl',NS),1):
        rows=[]
        for row in table.findall('w:tr',NS):
            rows.append([' '.join(n.text or '' for n in cell.findall('.//w:t',NS))
                         for cell in row.findall('w:tc',NS)])
        tables.append({'OOXML_table_number':number,'rows':rows})
    header=tables[0]['rows'][0]
    assert len(header)==21
    isotope_rows=[]
    for table in tables[:4]:
        for number,cells in enumerate(table['rows'],1):
            if not key(cells[0]).startswith('UF'):continue
            assert len(cells)==21
            isotope_rows.append({'OOXML_table_number':table['OOXML_table_number'],
                                 'row_number':number,'museum_id':cells[0],'cells':cells})
    dates=json.loads((ROOT/'data/haiti-rodent-dates.json').read_text(encoding='utf-8'))
    matches=[]
    for dated in dates['rows']:
        found=[r for r in isotope_rows if key(r['museum_id'])==key(dated['museum_id'])]
        matches.append({'museum_id':dated['museum_id'],'lab_id':dated['lab_id'],
                        'dated_taxon_as_published':dated['taxon_as_published'],
                        'isotope_rows':found,'match_basis':'Exact normalized museum ID only',
                        'isotope_tissue':'Incisor enamel per linked article abstract; not collagen',
                        'identity_limit':'Same accession label; physical object/sample identity not independently authenticated.'})
    assert len(matches)==8
    result={'date':'2026-10-09','source_id':'S317','access':'FULL_TEXT_PORTION',
            'file_sha256':hashlib.sha256(raw).hexdigest(),'file_md5':hashlib.md5(raw).hexdigest(),
            'coverage':'All five OOXML tables extracted; Table1S spans first four table objects, Table2S fifth. No rendered document pages inspected.',
            'raw_header_cells':header,'raw_tables':tables,
            'isotope_row_count':len(isotope_rows),
            'unique_isotope_museum_id_count':len({key(r['museum_id']) for r in isotope_rows}),
            'matched_dated_museum_ids':sum(bool(m['isotope_rows']) for m in matches),'joins':matches,
            'isotope_reference_scale':None,
            'unit':'Per mil as table header; reference scale not independently recovered from full methods.',
            'limits':['Tip/base/whole are tissue subsamples, not independently dated animals.',
                      'No collagen carbon/nitrogen isotope measurement assigned from enamel.',
                      'No reservoir fraction, dietary mixture or radiocarbon correction estimated.',
                      'Main article methods/figures and DOCX rendered layout uninspected.',
                      'Species names and raw numerical tokens retained, including discrepancies.'],
            'scientific_validation':False}
    (ROOT/'data/rodent2018-isotope-crosswalk.json').write_text(
        json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(f"Extracted {len(isotope_rows)} isotope rows; {result['unique_isotope_museum_id_count']} museum IDs; {result['matched_dated_museum_ids']}/8 dated IDs matched")

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('source',type=Path)
    main(parser.parse_args().source)
