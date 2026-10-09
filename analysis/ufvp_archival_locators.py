"""Extract original finding-aid table cells; no rendered page or notebook claims."""
import json,zipfile,hashlib,xml.etree.ElementTree as ET
from pathlib import Path
p=Path('tmp/research/ufvp-archives-2026.docx'); z=zipfile.ZipFile(p)
ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
r=ET.fromstring(z.read('word/document.xml'))
def txt(e): return ''.join(t.text or '' for t in e.findall('.//w:t',ns))
paragraphs=[txt(a) for a in r.findall('.//w:p',ns)]
tables=r.findall('.//w:tbl',ns); rows=tables[2].findall('./w:tr',ns)
def cells(row): return [' | '.join(txt(a) for a in c.findall('./w:p',ns)) for c in row.findall('./w:tc',ns)]
assert cells(rows[0])==['Box','Book','Creator','Title','Year(s)','Keywords and Notes']
selected=[]
for ordinal in range(20,28):
    vals=cells(rows[ordinal-1]); assert len(vals)==6
    selected.append({'table_ordinal':3,'row_ordinal':ordinal,'series':'Series2:Field Notebooks','box_as_printed':vals[0],'book_as_printed':vals[1],'creator_as_printed':vals[2],'title_as_printed':vals[3],'years_as_printed':vals[4],'keywords_as_printed':vals[5],'raw_cells':vals,'notebook_contents_inspected':False})
assert selected[5]['title_as_printed']=='Jeremie #5, Stratigraphy'
assert selected[5]['box_as_printed']=='3' and selected[5]['book_as_printed']=='2'
tokens=['MKL 998','MKL 1006','MKL 992','XH007','170046','170308','170311','293844','Beta-345518']
out={'date':'2026-10-09','source_id':'S322','source_url':'https://www.floridamuseum.ufl.edu/vertpaleo/professionals/archives/','download_url':'https://www.floridamuseum.ufl.edu/wp-content/uploads/sites/41/2024/10/FLMNH-VP-Archives-Complete-4.7.2026.accessible-1.docx','docx_bytes':p.stat().st_size,'docx_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'inspection':'OOXML body extraction, all11059paragraphs searched. Selected Table3rows20–27transcribed from actual six-cell rows. No original notebook, physical shelf or rendered DOCX pages inspected.','table_count':len(tables),'body_paragraph_count':len(paragraphs),'application_page_count_metadata':121,'rendered_page_count':None,'file_metadata_modified_UTC':'2026-04-07T19:16:00Z','file_metadata_created_UTC':'2026-04-07T16:39:00Z','selected_entries':selected,'exact_token_search':{t:[i+1 for i,v in enumerate(paragraphs) if t in v] for t in tokens},'rights':'Public finding aid linked; no redistribution license established for original DOCX or underlying notebooks.','limits':['Finding-aid description only; title does not demonstrate preserved strata, specimen association or a catastrophe.','n.d. retained as unknown notebook date; cannot assign1984from neighboring rows.','Modern document metadata dates do not date notebooks or fossils.','Exact-token absence in body does not exclude alternate spelling or uncataloged specimen references.','Box/book locator not physical custody or independent authentication.'],'next_test':'Inspect Series2Box3Book2(Jeremie#5Stratigraphy), Box3Book4(Cordier-WoodsHaiti1983/1984), and relevant notebooks; seek explicit XH007/MKL998/1006/992 and accession/bag/depth joins.'}
Path('data/ufvp-archival-locators.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'selected':[(x['box_as_printed'],x['book_as_printed'],x['title_as_printed']) for x in selected],'exact_tokens':out['exact_token_search']},ensure_ascii=False,indent=2))
