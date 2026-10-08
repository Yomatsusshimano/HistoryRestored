"""Recompute simple means from rounded published ages, preserving exclusions."""
import argparse,json,re,math,hashlib
from pathlib import Path
from pypdf import PdfReader
p=argparse.ArgumentParser();p.add_argument('pdf',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
t=PdfReader(a.pdf).pages[6].extract_text();groups={};group=None
for line in t.splitlines():
    if line.strip() in ('TAL 6071','TAL 6073'):
        group=line.strip();groups[group]=[]
    elif group and re.match(r'^\d+\.1 ',line):
        v=line.split();groups[group].append({'spot':v[0],'age_Ma':float(v[-2]),'one_sigma_Ma':float(v[-1])})
assert len(groups['TAL 6071'])==18 and len(groups['TAL 6073'])==17
exclusions={'TAL 6071':{'6.1':'older analysis excluded in source'},'TAL 6073':{'7.1':'much older grain','10.1':'much older grain','11.1':'older magmatic zircon interpretation','19.1':'older magmatic zircon interpretation','3.1':'younger analysis excluded in source'}}
def stats(rows):
    w=sum(1/x['one_sigma_Ma']**2 for x in rows);m=sum(x['age_Ma']/x['one_sigma_Ma']**2 for x in rows)/w
    return {'n':len(rows),'mean_Ma':m,'two_sigma_internal_Ma':2/math.sqrt(w),'MSWD':sum(((x['age_Ma']-m)/x['one_sigma_Ma'])**2 for x in rows)/(len(rows)-1)}
result={'source':'S214','locator':'Table1 printed777/PDF7; exclusion discussion printed780/782','source_sha256':hashlib.sha256(a.pdf.read_bytes()).hexdigest(),'scope':'Rounded published age arithmetic, not isotope refit, exact95percent interval reproduction or new dating.','groups':{}}
for g,rows in groups.items():
    for x in rows:x['exclusion_reason']=exclusions[g].get(x['spot'])
    selected=[x for x in rows if x['exclusion_reason'] is None]
    restored=selected+[x for x in rows if x['spot']==('6.1' if g=='TAL 6071' else '3.1')]
    result['groups'][g]={'sample_crosswalk': '02-440' if g=='TAL 6071' else '02-441','crosswalk_basis':'Table order, row counts and distinctive excluded ages agree with prose; not a recovered lab custody record.','rows':rows,'published_selection_calculated':stats(selected),'restore_single_marginal_exclusion':stats(restored),'reported_mean_Ma':2.65 if g=='TAL 6071' else 2.60,'reported_95percent_halfwidth_Ma':0.05 if g=='TAL 6071' else 0.06,'reported_MSWD':1.3 if g=='TAL 6071' else 0.97}
a.output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
for g,x in result['groups'].items():print(g,x['published_selection_calculated'],x['restore_single_marginal_exclusion'])
