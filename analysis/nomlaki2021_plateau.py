"""Extract the original ROSER-2a rows and check its marked plateau."""
import hashlib, json, math, sys
from pathlib import Path
from openpyxl import load_workbook

root=Path(__file__).resolve().parents[1]
path=Path(sys.argv[1])
assert hashlib.md5(path.read_bytes()).hexdigest()=='fbab392f4a92dd81ca2adc06dfe22821'
sheet=load_workbook(path,read_only=True,data_only=False)['Table S1']
assert sheet['A86'].value=='ROSER-2a'
rows=[]
for n in range(87,96):
 cells=list(sheet[n])
 assert len(cells)==31 and str(cells[0].value).startswith('20947-01')
 rows.append({'row':n,'raw_cells':[c.value for c in cells],
              'lab_id_bold':bool(cells[0].font.bold)})
selected=[r for r in rows if r['lab_id_bold']]
assert [r['row'] for r in selected]==list(range(90,95))
weights=[1/r['raw_cells'][24]**2 for r in selected] # Y: step age1sigma, excludingJ
age=sum(w*r['raw_cells'][23] for w,r in zip(weights,selected))/sum(weights)
q=sum(w*(r['raw_cells'][23]-age)**2 for w,r in zip(weights,selected))
mswd=q/(len(selected)-1)
sem=(1/sum(weights))**.5*max(1,mswd**.5)
release=sum(r['raw_cells'][16] for r in selected)
# First-order sharedJ contribution; not an independent error per heating step.
j=selected[0]['raw_cells'][3]; jerr=selected[0]['raw_cells'][4]
assert all(r['raw_cells'][3:5]==selected[0]['raw_cells'][3:5] for r in selected)
shared_j_ma=age*jerr/j
with_j=math.hypot(sem,shared_j_ma)
out={'source_id':'S327','sample':'ROSER-2a','workbook_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
 'workbook_sheet':'Table S1','header_rows':[[c.value for c in sheet[n]] for n in [3,4]],
 'rows':rows,'selected_rows':[r['row'] for r in selected],
 'selection_basis':'OriginalA-column bold font and row99note; no inferred replacement selection',
 'diagnostic':{'plateau_age_ma':age,'internal_modified_sem_ma':sem,'mswd':mswd,
 'selected_ar39_percent':release,'shared_j_first_order_error_ma':shared_j_ma,
 'combined_first_order_sem_ma':with_j,'reported_figure3_age_ma':3.314,'reported_figure3_error_ma':0.011},
 'limitations':'Reuses published derived step ages/errors and author-selected plateau. SharedJ propagation is first-order. No raw gas reduction, plateau-selection search or preferred inverse-isochron reproduction.'}
(root/'data/nomlaki2021-plateau.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(out['diagnostic'],indent=2))
