"""Reported calendar-envelope geometry; not a mortality or deposition model."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]

def compare(intervals):
    if not intervals or any(len(i)!=2 or i[0]>i[1] for i in intervals):
        raise ValueError('Require ordered closed intervals')
    low=max(i[0] for i in intervals)
    high=min(i[1] for i in intervals)
    return {'intersection_CE':[low,high] if low<=high else None,
            'minimum_touching_window_years':max(0,low-high)}

def main():
    path=ROOT/'data/hispaniola2026-pooled-dates.json'
    data=json.loads(path.read_text(encoding='utf-8'))
    rows={r['lab_id']:r for r in data['rows']}
    results=[]
    for ids in [('RICH-24986','RICH-24977'),('RICH-24986','RICH-27406'),
                ('RICH-24986','RICH-24977','RICH-27406')]:
        intervals=[rows[i]['reported_2sigma_calendar_CE'] for i in ids]
        result=compare(intervals)
        results.append({'lab_ids':ids,'reported_calendar_envelopes_CE':intervals,**result,
                        'duration_feasibility':{str(d):d>=result['minimum_touching_window_years']
                                                for d in [0,1,10,100,200,250]}})
    out={'status':'RETROSPECTIVE_CONDITIONAL_ENVELOPE_COMPARISON',
         'input_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'comparisons':results,'regional_comparison':{
             'new_pool_CE':[1406,1453],
             'earlier_rat_S36_ledger_CE_arithmetic':[1435,1460],
             'earlier_rat_S316_citation_CE':[1435,1468],
             'intersection_each_version_CE':[1435,1453]},
         'limits':['Pool dates do not date each individual or deposition.',
                   'Marginal envelopes omit probability structure; no joint confidence assigned.',
                   'Regional overlap is not same-site coexistence or causal interaction.',
                   'S36 conversion is arithmetic only; no calibration rerun or transcription resolution.']}
    (ROOT/'analysis/hispaniola-pool-windows-result.json').write_text(
        json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
    print('Pool comparison: 227/207/227-year minimum touching windows; regional overlap1435–1453CE')

if __name__=='__main__':
    assert compare([[1,3],[2,4]])=={'intersection_CE':[2,3],'minimum_touching_window_years':0}
    assert compare([[1,3],[8,10]])=={'intersection_CE':None,'minimum_touching_window_years':5}
    main()
