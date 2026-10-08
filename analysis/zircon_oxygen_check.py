"""Descriptive, retrospective comparison; no source-assignment probability."""
import json
import statistics
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def describe(rows):
    measured=[r for r in rows if r['oxygen18_permil'] is not None]
    values=[r['oxygen18_permil'] for r in measured]
    return dict(rows=len(rows),measured=len(values),missing=len(rows)-len(values),
                mean=statistics.mean(values),median=statistics.median(values),
                minimum=min(values),maximum=max(values))

def main():
    original=json.loads((ROOT/'data/harvey-zircon-rows.json').read_text())['rows']
    pre=json.loads((ROOT/'data/harvey-prekilgore-rows.json').read_text())['rows']
    assert len(pre)==24 and len({r['row_key'] for r in pre})==24
    groups={'Bouse':[r for r in original if r['group']=='Bouse'],
            'Lawlor':[r for r in original if r['group']=='Lawlor'],
            'Pre-Kilgore':pre,
            'Pre-Kilgore unmarked':[r for r in pre if not r['prior_source_marker']],
            'Pre-Kilgore prior':[r for r in pre if r['prior_source_marker']]}
    stats={g:describe(rows) for g,rows in groups.items()}
    b=[r for r in groups['Bouse'] if r['oxygen18_permil'] is not None]
    p=[r for r in pre if r['oxygen18_permil'] is not None]
    nearest_b=min(b,key=lambda r:r['oxygen18_permil'])
    nearest_p=max(p,key=lambda r:r['oxygen18_permil'])
    overlap=[]
    for br in b:
        for pr in p:
            if max(br['oxygen18_permil']-2*br['oxygen18_sigma_permil'],pr['oxygen18_permil']-2*pr['oxygen18_sigma_permil']) <= min(br['oxygen18_permil']+2*br['oxygen18_sigma_permil'],pr['oxygen18_permil']+2*pr['oxygen18_sigma_permil']):
                overlap.append([br['id'],pr['row_key']])
    out=dict(source_id='S196',units='per mil; published oxygen values',groups=stats,
             minimum_point_gap=nearest_b['oxygen18_permil']-nearest_p['oxygen18_permil'],
             gap_ids=[nearest_b['id'],nearest_p['row_key']],two_sigma_interval_overlap_pairs=overlap,
             limitations='Unweighted descriptive summaries of selected analyses. Interval overlaps use printed one-sigma errors, not calibrated joint confidence or independent source-assignment tests. No unmeasured values filled; no grain-level independence assumed.')
    (ROOT/'data/zircon-oxygen-check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

if __name__=='__main__':main()
