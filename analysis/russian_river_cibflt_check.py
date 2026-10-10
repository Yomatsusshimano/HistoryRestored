"""Summarize a transcribed modern column; this is not a fossil depth classifier."""
import json
from pathlib import Path

root=Path(__file__).resolve().parents[1]
d=json.loads((root/'data/russian-river-faunal-controls.json').read_text(encoding='utf8'))
rows=d['S333']['L1_81_CIBFLT_complete_column']
assert len(rows)==21 and len({r['sample'] for r in rows})==21
assert all(0<=r['CIBFLT_percent']<=100 and r['depth_m_uncorrected']>0 for r in rows)
positives=[r for r in rows if r['CIBFLT_percent']>0]
print(json.dumps({'column_rows':len(rows),'reported_positive_rows':len(positives),
 'reported_positive_depths_m':sorted(r['depth_m_uncorrected'] for r in positives),
 'positive_rows_at_or_above_50m_depth':sum(r['depth_m_uncorrected']>=50 for r in positives),
 'full_assemblage_model':False,'fossil_depth_estimate':None},indent=2))
