"""Reproduce reported-input arithmetic; preserve failed checks and assumptions."""
from pathlib import Path
import collections,hashlib,json,statistics
d=json.loads(Path('data/willapa-tidalflat-inputs.json').read_text())
assert hashlib.sha256(Path(d['original_path']).read_bytes()).hexdigest()==d['sha256']
rows=[]
for row in d['table4_rows']:
    a,l,r=row['age_ka'],row['length_m'],row['reported_rate_m_per_ka']
    lo=(l-.05)/(a+.05);hi=(l+.05)/(a-.05)
    rows.append({**row,'computed_rate_m_per_ka':l/a,'rounded_input_rate_range':[lo,hi],'compatible_allowing_half_last_digit_rounding':lo<=r+.05 and hi>=r-.05})
rates=[r['computed_rate_m_per_ka'] for r in rows];printed=[r['reported_rate_m_per_ka'] for r in rows]
labgroups=collections.defaultdict(list)
for r in d['table3_sample_age_rows']:
    if r['beta_number']:labgroups[r['beta_number']].append(r['table_row'])
b=d['table5_inputs'];area=b['intertidal_area_m2'];sand=b['sand_fraction'];volume=area*b['depth_m']*sand
initial=area*b['post_subsidence_unit_thickness_m']*sand
out={'source_id':'S274','input_sha256':hashlib.sha256(Path('data/willapa-tidalflat-inputs.json').read_bytes()).hexdigest(),'table4_audit':rows,'summary':{'computed_mean_of_ratios':statistics.mean(rates),'computed_sample_sd_of_ratios':statistics.stdev(rates),'mean_printed_rates':statistics.mean(printed),'sample_sd_printed_rates':statistics.stdev(printed),'ratio_of_mean_length_to_mean_age':statistics.mean(r['length_m'] for r in rows)/statistics.mean(r['age_ka'] for r in rows)},'duplicate_beta_numbers':{k:v for k,v in labgroups.items() if len(v)>1},'table5_arithmetic':{'bulk_3m_volume_m3':area*b['depth_m'],'sand_3m_volume_m3':volume,'annual_sand_at_1m_per_ka_m3':area*sand*b['net_sedimentation_m_per_ka']/1000,'annual_bulk_accommodation_m3':area*b['net_sedimentation_m_per_ka']/1000,'initial_sand_volume_m3':initial,'initial_100yr_mean_sand_flux_m3_per_yr':initial/b['assumed_post_subsidence_duration_yr'],'bedload_only_volume_m3_per_yr':b['tributary_suspended_mass_t_per_yr']*b['bedload_fraction_relative_to_suspended']*b['assumed_mass_to_deposit_volume_factor'],'suspended_plus_bedload_volume_m3_per_yr':b['tributary_suspended_mass_t_per_yr']*(1+b['bedload_fraction_relative_to_suspended'])*b['assumed_mass_to_deposit_volume_factor']},'limits':'No conservation/hydrodynamic validation. Uniform area/fraction/thickness/duration assumed. Input-rounding bounds are diagnostic, not measured uncertainty. Mean ratios and ratio means differ. Bedload-only versus total are arithmetic scenarios; no grain-size/source discharge reconciliation.'}
out['conditional_duration_scenarios']=[{'years':t,'required_mean_sand_flux_m3_per_yr':initial/t,'multiple_of_reported_bedload_only_supply':initial/t/out['table5_arithmetic']['bedload_only_volume_m3_per_yr']} for t in (1,10,100)]
Path('data/willapa-tidalflat-budget.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({'summary':out['summary'],'failed_row_rounding_checks':[r['site'] for r in rows if not r['compatible_allowing_half_last_digit_rounding']],'duplicate_beta':out['duplicate_beta_numbers'],'budget':out['table5_arithmetic']},indent=2))
