"""Single-assay diagnostic, not CALIB/OxCal reproduction or an arrival model."""
import argparse
import hashlib
import json
import math
from pathlib import Path
from bonneville_calibration_check import interpolate

ROOT=Path(__file__).resolve().parents[1]

def run(curve, step):
    raw=curve.read_bytes()
    curve_rows=sorted(tuple(map(float,line.split(',')[:3])) for line in raw.decode().splitlines()
                      if line and not line.startswith('#'))
    xs,means,sigmas=map(list,zip(*curve_rows))
    source=ROOT/'data/haiti-rodent-dates.json'
    sample=next(s for s in json.loads(source.read_text(encoding='utf-8'))['rows']
                if s['lab_id']=='UCIAMS 191028')
    years=[1000+i*step for i in range(round(950/step)+1)]
    logs=[]
    for year in years:
        mean=interpolate(xs,means,1950-year)
        sigma=interpolate(xs,sigmas,1950-year)
        variance=sample['radiocarbon_1sigma']**2+sigma**2
        logs.append(-.5*((sample['radiocarbon_BP']-mean)**2/variance+math.log(variance)))
    peak=max(logs)
    weights=[math.exp(x-peak) for x in logs]
    total=sum(weights)
    weights=[w/total for w in weights]
    def quantile(q):
        acc=0
        for year,w in zip(years,weights):
            acc+=w
            if acc>=q:return year
        return years[-1]
    selected=set(); mass=0
    for index in sorted(range(len(years)),key=lambda i:weights[i],reverse=True):
        selected.add(index);mass+=weights[index]
        if mass>=.954:break
    ranges=[]
    for i in sorted(selected):
        if not ranges or i!=ranges[-1][1]+1:ranges.append([i,i])
        else:ranges[-1][1]=i
    return {'source_ids':['S36','S128'],'lab_id':sample['lab_id'],'museum_id':sample['museum_id'],
            'radiocarbon_BP':sample['radiocarbon_BP'],'error_1sigma':sample['radiocarbon_1sigma'],
            'input_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
            'curve_sha256':hashlib.sha256(raw).hexdigest(),'curve_rows':len(curve_rows),
            'method':'Gaussian assay likelihood; linearly interpolated IntCal20 mean/sigma; sum of assay and curve variances; discrete uniform prior1000–1950CE; no reservoir offset.',
            'grid_step_years':step,'mode_CE':years[logs.index(max(logs))],
            'equal_tail_95_4_CE':[quantile(.023),quantile(.977)],
            'highest_density_95_4_segments_CE':[[years[a],years[b]] for a,b in ranges],
            'highest_density_actual_grid_mass':mass,
            'conditional_grid_mass_CE_at_or_after1492':sum(w for y,w in zip(years,weights) if y>=1492),
            'conditional_mass_CE_1463_to1470':sum(w for y,w in zip(years,weights) if 1463<=y<=1470),
            'first_last10year_mass':sum(w for y,w in zip(years,weights) if y<=1010 or y>=1940),
            'limitations':['Not CALIB8.2 or OxCal4.4 reproduction; curve smoothing/interval algorithms differ.',
                          'Uniform calendar prior and no-offset model are assumptions, not verified specimen history.',
                          'Conditional mass is not probability of rat arrival or historical fabrication.',
                          'No taxonomic, reservoir, contamination, raw-assay or deposition validation.',
                          'Reported published intervals retained; diagnostic does not replace them.'],
            'scientific_validation':False}

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('curve',type=Path)
    parser.add_argument('--step',type=float,default=.25)
    args=parser.parse_args()
    if args.step<=0 or 950/args.step!=round(950/args.step):raise ValueError('Step must divide950years')
    result=run(args.curve,args.step)
    (ROOT/'analysis/haiti-rat-calibration-check-result.json').write_text(
        json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({k:result[k] for k in ['mode_CE','equal_tail_95_4_CE','highest_density_95_4_segments_CE','conditional_grid_mass_CE_at_or_after1492']},indent=2))
