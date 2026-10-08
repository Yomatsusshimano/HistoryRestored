"""Descriptive interval arithmetic; not a statistical extinction/event model.

Preserves disjoint published calendar sets. Never treats radiocarbon BP as cal BP.
Run with --plot to regenerate the optional matplotlib figure.
"""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def normalize(intervals):
    result = []
    for lo, hi in sorted(intervals):
        if lo > hi:
            raise ValueError('Reversed interval')
        if result and lo <= result[-1][1]:
            result[-1][1] = max(hi, result[-1][1])
        else:
            result.append([lo, hi])
    return result


def intersect(left, right):
    return normalize([[max(a, c), min(b, d)]
                      for a, b in left for c, d in right
                      if max(a, c) <= min(b, d)])


def common_set(sets):
    if not sets or any(not item for item in sets):
        raise ValueError('Every included sample needs a nonempty interval set')
    result = normalize(sets[0])
    for item in sets[1:]:
        result = intersect(result, item)
    return result


def minimum_cover(sets):
    """Shortest closed interval containing at least one point from each set.

    An optimum can begin at an input endpoint. For each such lower endpoint,
    take the earliest available point in each set at or above it. Retain all
    optimal endpoint witnesses; this is geometry of sets, not probability integration.
    """
    if not sets or any(not item for item in sets):
        raise ValueError('Missing interval set')
    sets = [normalize(item) for item in sets]
    candidates = sorted({v for item in sets for pair in item for v in pair})
    best, windows = None, []
    for lower in candidates:
        points = []
        for item in sets:
            eligible = [max(lower, a) for a, b in item if b >= lower]
            if not eligible:
                break
            points.append(min(eligible))
        if len(points) != len(sets):
            continue
        upper = max(points)
        width = upper - lower
        if best is None or width < best:
            best, windows = width, [[lower, upper]]
        elif width == best:
            windows.append([lower, upper])
    return {'minimum_span_calendar_years': best, 'optimal_endpoint_witness_windows_cal_BP_young_old': windows}


def analyze(rows):
    included = [r for r in rows if r['published_cal_BP_intervals_young_old']]
    sets = [r['published_cal_BP_intervals_young_old'] for r in included]
    comes = [r for r in included if r['taxon_as_published'] == 'Neocnus comes']
    return {
        'status': 'DESCRIPTIVE_PUBLISHED_INTERVAL_CHECK_NOT_STATISTICAL_REJECTION',
        'case_id': 'C011', 'source_id': 'S22',
        'included_field_ids': [r['field_id'] for r in included],
        'excluded': [{'field_id': r['field_id'], 'reason': 'No published calendar interval; radiocarbon value or bound not substituted'} for r in rows if r not in included],
        'common_cal_BP_intervals': common_set(sets),
        'all_included_cover': minimum_cover(sets),
        'same_taxon_sensitivity': {
            'taxon': 'Neocnus comes',
            'field_ids': [r['field_id'] for r in comes],
            'common_cal_BP_intervals': common_set([r['published_cal_BP_intervals_young_old'] for r in comes]),
            **minimum_cover([r['published_cal_BP_intervals_young_old'] for r in comes])},
        'limits': ['Published 95% calendar sets are not hard age bounds or a joint 95% confidence region.',
                   'No probability densities, recalibration, shared-error model or laboratory-quality assessment used.',
                   'Biological ages do not alone date deposition, extinction or geographic upheaval.',
                   'Retrospective descriptive analysis; not a preregistered or held-out test.']}


def plot(rows):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    included = [r for r in rows if r['published_cal_BP_intervals_young_old']]
    fig, ax = plt.subplots(figsize=(11, 5.8))
    for i, row in enumerate(included):
        for lo, hi in row['published_cal_BP_intervals_young_old']:
            ax.plot([lo, hi], [i, i], color='#185a75', lw=5, solid_capstyle='butt')
    ax.set_yticks(range(len(included)), [r['field_id']+' | '+r['taxon_as_published'] for r in included])
    ax.invert_yaxis()
    ax.set_xlabel('Published calendar years BP (older to the right)')
    ax.set_title('Haitian sloth bones: published 95% calendar-age sets', loc='left', pad=16)
    ax.grid(axis='x', alpha=.2)
    ax.spines[['top','right','left']].set_visible(False)
    fig.text(.03, .03, 'S22, Table 4 (2005). Disjoint segments retained. Two uncalibrated rows excluded.\nNo recalibration; no probability density shown; these are not depositional or extinction dates.', fontsize=9)
    fig.tight_layout(rect=[0,.11,1,1])
    fig.savefig(ROOT/'analysis/sloth-intervals.png', dpi=170)
    plt.close(fig)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--plot',action='store_true')
    args=parser.parse_args()
    data=json.loads((ROOT/'data/dating-records.json').read_text(encoding='utf-8'))
    rows=[r for r in data['samples'] if r['case_id']=='C011']
    result=analyze(rows)
    # Canonical JSON avoids Windows/Git newline differences in provenance hashes.
    result['input_rows_canonical_sha256']=hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':'),ensure_ascii=True).encode()).hexdigest()
    (ROOT/'analysis/sloth-intervals-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    if args.plot:
        plot(rows)
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
