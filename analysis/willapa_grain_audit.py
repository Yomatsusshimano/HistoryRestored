"""Audit literal S274 Table2 and declared selection sensitivities; no inferred values."""
import hashlib
import json
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean

ROOT=Path(__file__).resolve().parents[1]

def summarize(cells):
    measured=[c for c in cells if c['sand_weight_percent'] is not None]
    pairs=[c for c in measured if c['sand_mean_um'] is not None]
    x=[c['sand_weight_percent'] for c in pairs]
    y=[c['sand_mean_um'] for c in pairs]
    mx,my=mean(x),mean(y)
    xx=sum((v-mx)**2 for v in x); yy=sum((v-my)**2 for v in y)
    xy=sum((a-mx)*(b-my) for a,b in zip(x,y))
    cores=defaultdict(list)
    for c in measured: cores[c['site']].append(c['sand_weight_percent'])
    sand_sum=sum(c['sand_weight_percent'] for c in measured)
    return dict(composition_n=len(measured),composition_sand_sum=sand_sum,
        sand_weight_mean_percent=sand_sum/len(measured),core_n=len(cores),
        equal_core_sand_weight_mean_percent=mean(mean(v) for v in cores.values()),
        grain_n=len(pairs),grain_mean_um=my,grain_min_um=min(y),grain_max_um=max(y),
        ols_with_intercept_r_squared=xy**2/(xx*yy),ols_slope_um_per_percent=xy/xx,
        plus20_assumed_zero_sections_n=len(measured)+20,
        plus20_assumed_zero_mean_percent=sand_sum/(len(measured)+20),
        conditional_equal_density_volume_m3=1.9e8*.5*sand_sum/(len(measured)+20)/100)

def main():
    inp=json.loads((ROOT/'data/willapa-grain-inputs.json').read_text(encoding='utf-8'))
    assert hashlib.sha256((ROOT/inp['original_path']).read_bytes()).hexdigest()==inp['sha256']
    cells=inp['cells']; assert len(cells)==218
    assert len({(c['site'],c['depth_start_m']) for c in cells})==len(cells)
    variants={
        'all_table_and_note': cells,
        'table_only': [c for c in cells if not c['note_only']],
        'all_except_KI11': [c for c in cells if c['site']!='KI11'],
        'depth_end_at_most_3m': [c for c in cells if c['depth_end_m']<=3],
        'all_except_W28_645um_cell': [c for c in cells if not(c['site']=='W28' and c['depth_start_m']==2)],
        'printed_composition_sums_100_only': [c for c in cells if c['sand_weight_percent'] is not None and sum(c[k] or 0 for k in ['sand_weight_percent','mud_weight_percent','gravel_weight_percent'])==100],
    }
    anomalies=[]
    for c in cells:
        if c['sand_weight_percent'] is None: continue
        total=sum(c[k] or 0 for k in ['sand_weight_percent','mud_weight_percent','gravel_weight_percent'])
        if total!=100: anomalies.append(dict(site=c['site'],depth_start_m=c['depth_start_m'],raw=c['raw'],printed_total=total))
    results={k:summarize(v) for k,v in variants.items()}
    target=inp['reported_targets']
    for result in results.values():
        result['composition_count_matches_report']=result['composition_n']==target['composition_n']
        result['grain_count_matches_report']=result['grain_n']==target['grain_n']
    out=dict(source_id='S274',source_sha256=inp['sha256'],
        status_counts=dict(Counter(c['status'] for c in cells)),reported_targets=target,
        variants=results,printed_composition_anomalies=anomalies,
        limitations=['Variants are declared sensitivities, not inferred author selections.',
            'Twenty zero sections are a reported assumption, not twenty recovered sieve measurements.',
            'Equal sample/core weights are not area weights; no spatial confidence interval computed.',
            'Mass fraction equals solid volume fraction only under equal constituent density; bulk volume additionally needs porosity definitions.',
            'SD of grains is not measurement error of composition or uncertainty of the budget.'])
    (ROOT/'data/willapa-grain-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))

if __name__=='__main__': main()
