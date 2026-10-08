"""Apply the Bonneville simplified likelihood assumptions to Electron assays."""
import argparse,csv,hashlib,json,math
from pathlib import Path
from bonneville_calibration_check import interpolate,summarize
ROOT=Path(__file__).resolve().parents[1]

def run(curve,step=.25):
    raw=curve.read_bytes()
    expected=next(s['downloaded_sha256'] for s in json.loads((ROOT/'data/sources.json').read_text(encoding='utf-8'))['sources'] if s['id']=='S128')
    if hashlib.sha256(raw).hexdigest()!=expected:raise ValueError('Curve hash mismatch')
    rows=sorted(tuple(map(float,l.split(',')[:3])) for l in raw.decode().splitlines() if l and not l.startswith('#'))
    xs,means,sigmas=map(list,zip(*rows))
    source=ROOT/'sources/originals/electron/C14_data_S2.csv'
    lines=list(csv.reader(source.read_text(encoding='utf-8',errors='replace').splitlines()))
    samples=[dict(tree=r[0],lab_id=r[3],age=float(r[5]),sigma=float(r[6]),offset=float(r[8])) for r in lines[3:] if r and r[0]]
    selected=[s for s in samples if s['tree']!='KAP14a']
    assert len(selected)==7 and len([s for s in selected if s['tree']=='ELE01'])==5
    model=json.loads((ROOT/'data/electron-model-selection.json').read_text(encoding='utf-8'))['illustrated_model']
    normalize=lambda lab:lab.replace('-','').replace(' ','')
    expected_offsets=dict(zip(model['lab_ids'],model['ring_offsets_years']))
    assert {normalize(s['lab_id']):s['offset'] for s in selected}==expected_offsets
    years=[1+i*step for i in range(round(1949/step)+1)]
    variants={}
    for label,group in [('five_ELE01',[s for s in selected if s['tree']=='ELE01']),('seven_samples',selected),('omit_ELE01',[s for s in selected if s['tree']!='ELE01'])]:
        logs=[]
        for death in years:
            log=0
            for s in group:
                calbp=1950-death+s['offset']; mean=interpolate(xs,means,calbp);sigma=interpolate(xs,sigmas,calbp)
                variance=s['sigma']**2+sigma**2
                log+=-.5*((s['age']-mean)**2/variance+math.log(variance))
            logs.append(log)
        variants[label]={'lab_ids':[s['lab_id'] for s in group],**summarize(years,logs)}
    return {'source_ids':['S72','S73','S128'],'assay_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'curve_sha256':expected,'step_years':step,'prior':'Uniform death year 1–1950 CE','selected_inputs':selected,'excluded':'KAP14a separately treated because unknown missing outer rings and unsuccessful crossdating, as recorded in model-selection audit.','method':'Same fixed-offset Gaussian product and interpolated curve mean/sigma as bonneville_calibration_check.py','limitations':['Not OxCal reproduction or independent chronology.','No offset uncertainty, within-sample averaging, calibration covariance, or assay dependence modeled.','Equal-tail intervals differ in definition from some published summaries.','ELE01 five determinations are one tree, not five independent event witnesses.','Source tree identities and relative offsets retained without revalidation.'],'variants':variants,'scientific_validation':False}

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('curve',type=Path);a=p.parse_args()
    result=run(a.curve)
    (ROOT/'analysis/electron-calibration-check-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result['variants'],indent=2))
