"""Arithmetic audit of printed r, overlap and t; not raw crossdating."""
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
# S68 Table 3, printed p. 78 / PDF p. 14; visually inspected.
groups = {
    'Powerhouse-Wyeth': [(127,.52,6.8),(88,.31,3.0),(64,.34,2.8),(114,.25,2.7),(112,.21,2.2)],
    'Powerhouse-Perham': [(116,.43,5.0),(53,.34,2.5),(141,.21,2.5),(55,.32,2.4),(113,.22,2.4)],
    'Wyeth-Perham': [(102,.52,6.1),(51,.51,4.1),(89,.31,3.0),(76,.30,2.7),(127,.21,2.4)],
}
def statistic(r,n):
    return r * math.sqrt((n-2)/(1-r*r))

rows=[]
for pair, values in groups.items():
    for rank,(n,r,t) in enumerate(values,1):
        low,high=statistic(r-.005,n),statistic(r+.005,n)
        rows.append(dict(pair=pair,rank=rank,overlap=n,printed_r=r,printed_t=t,
                         calculated_t=statistic(r,n),
                         t_range_from_r_rounding=[low,high],
                         compatible_with_printed_rounding=low<t+.05 and high>t-.05))
out=dict(source_id='S68',method='t = r sqrt((n-2)/(1-r^2)); r rounding +/-0.005 and t rounding +/-0.05',
         scope='Printed summary arithmetic only; no raw series, residual autocorrelation test, multiple-alignment correction, p-value audit or calendar calibration.',
         rows=rows,
         prose_example=dict(locator='printed p. 75 / PDF p. 11',n=50,r=.3281,printed_t=3.5,calculated_t=statistic(.3281,50)),
         raw_alignment_reproduced=False)
path=ROOT/'analysis/bonneville-correlation-audit.json'
path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'table_rows':len(rows),'rounding_compatible':sum(x['compatible_with_printed_rounding'] for x in rows),'prose_example':out['prose_example']},indent=2))
