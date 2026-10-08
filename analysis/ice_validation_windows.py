"""Audit denominators only; does not reproduce event matches or significance."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def window(row, margin):
    years=[1-y if row['era']=='BCE' else y for y in row['years_as_printed']]
    return set(range(min(years)-margin,max(years)+margin+1))

def main():
    data=json.loads((ROOT/'data/ice-historical-validation.json').read_text(encoding='utf-8'))
    output=[]
    for item in data['reported_statistics']:
        rows=[x for x in data['rows'] if item['subset']=='all' or x['rank']=='Probable']
        windows=[window(x,item['margin']) for x in rows]
        output.append({**item,'row_count':len(rows),'computed_sum_years':sum(map(len,windows)),
                       'computed_unique_years':len(set().union(*windows)),
                       'matches_sum':item['n_years']==sum(map(len,windows))})
    result={'convention':'Inclusive expanded date ranges; astronomical year numbering (1 BCE = 0). Sum counts overlaps repeatedly; union counts each year once.','rows':output,'limits':'No ice-event series supplied; matches, means and p-values not reproduced. Counting diagnostics alone cannot invalidate chronology.'}
    (ROOT/'analysis/ice-validation-windows-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(output,indent=2))

if __name__=='__main__':main()
