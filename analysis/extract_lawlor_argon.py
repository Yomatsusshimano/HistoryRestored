"""Extract original stored Lawlor cells; requires xlrd 2.0.2. No age refit."""
import argparse, hashlib, json
from pathlib import Path
import xlrd
p=argparse.ArgumentParser();p.add_argument('workbook');a=p.parse_args()
b=Path(a.workbook).read_bytes()
assert hashlib.sha256(b).hexdigest()=='64d4ae344cc82962d5249513e96e23628437e931c9e915de8cf3c1f549f26299'
s=xlrd.open_workbook(file_contents=b).sheet_by_name('Table')
def vals(i):return [None if c.ctype in (xlrd.XL_CELL_EMPTY,xlrd.XL_CELL_BLANK) else c.value for c in s.row(i)]
headers=vals(0);rows=[]
for i in range(8,55):
 v=vals(i)
 if v[1] not in ('LAWL-1','LAWL-2'):continue
 rows.append(dict(sheet_row=i+1,source_omitted=i+1 in (19,20,21,22,23,55),values=dict(zip(headers,v))))
assert len(rows)==35 and sum(x['source_omitted'] for x in rows)==6
summaries=[]
for prefix in ['20975-01','20954-01','20955-02']:
 rr=[x for x in rows if x['values']['Run_ID'].startswith(prefix)]
 kept=[x for x in rr if not x['source_omitted']]
 omitted=[x for x in rr if x['source_omitted']]
 summaries.append(dict(run=prefix,rows=len(rr),kept=len(kept),omitted=len(omitted),kept_age_range_ma=[min(x['values']['Age'] for x in kept),max(x['values']['Age'] for x in kept)],stored_percent_sum=sum(x['values']['Ar39_CumPct'] for x in kept),omitted_fraction_from_stored_moles=sum(x['values']['Ar39_Moles'] for x in omitted)/sum(x['values']['Ar39_Moles'] for x in rr)))
out=dict(source_id='S198',doi='10.1130/GES00609.S1',sha256=hashlib.sha256(b).hexdigest(),sheet='Table',scope='Lawlor rows only. Stored values, not recalculated formulas or unscaled physical quantities. Blank cells null; numeric zeros retained without assuming physical meaning.',header_rows={str(i+1):vals(i) for i in range(6)},rows=rows,summary_rows={str(i):vals(i-1) for i in [17,36,53]},run_summaries=summaries)
Path('data/lawlor-argon-rows.json').write_text(json.dumps(out,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
print(json.dumps(summaries,indent=2))
