"""Retrospective implementation sensitivity, NOT an exact-paper reproduction.

Requires the unmodified S109 workbook at the path supplied on the command line.
All four variants are reported; none is selected by matching published totals.
"""
import argparse
import hashlib
import json
import math
from pathlib import Path
from statistics import median
import openpyxl
from ice_validation_windows import window

ROOT=Path(__file__).resolve().parents[1]

def ordinal(midyear):
    signed=math.floor(midyear)
    if signed==0:
        raise ValueError('Unexpected zero historical year')
    return signed+1 if signed<0 else signed

def backgrounds(series, radius=15):
    out={}
    for year in series:
        vals=[series.get(y) for y in range(year-radius,year+radius+1)]
        out[year]=median(vals) if all(v is not None for v in vals) else None
    return out

def classify(series, bg, scope, scale):
    residuals=[series[y]-v for y,v in bg.items() if v is not None]
    center=median(residuals)
    global_mad=median(abs(v-center) for v in residuals)
    out={}
    for year,value in series.items():
        if bg[year] is None:
            out[year]=None
            continue
        mad=global_mad if scope=='global_residual' else median(
            abs(series[y]-bg[year]) for y in range(year-15,year+16))
        out[year]=value>bg[year]+3*scale*mad
    return out,global_mad

def match_state(flags, years):
    vals=[flags.get(y) for y in years]
    if any(v is True for v in vals):return 'MATCH'
    if any(v is None for v in vals):return 'UNRESOLVED'
    return 'NO_MATCH'

def main(path):
    sources=json.loads((ROOT/'data/sources.json').read_text(encoding='utf-8'))['sources']
    expected=next(x for x in sources if x['id']=='S109')['downloaded_workbook_sha256']
    actual=hashlib.sha256(path.read_bytes()).hexdigest()
    if actual!=expected:raise ValueError('S109 checksum mismatch')
    sheet=openpyxl.load_workbook(path,read_only=True,data_only=True)['6 - NEEM_annual_combined']
    series={}
    for row in sheet.iter_rows(min_row=2,values_only=True):
        y=ordinal(row[0])
        if y in series:raise ValueError('Duplicate year')
        series[y]=None if row[4] in (None,-9.999) else row[4]
    bg=backgrounds(series)
    historical=json.loads((ROOT/'data/ice-historical-validation.json').read_text(encoding='utf-8'))
    period=range(1-258,504+1)
    variants=[]
    for scope in ['local_window','global_residual']:
        for scale in [1.0,1.4826]:
            flags,gm=classify(series,bg,scope,scale)
            matches=[]
            for margin in [1,2,3]:
                states=[{'row':r['row'],'state':match_state(flags,window(r,margin))} for r in historical['rows']]
                matches.append({'margin':margin,'counts':{s:sum(x['state']==s for x in states) for s in ['MATCH','NO_MATCH','UNRESOLVED']},'rows':states})
            variants.append({'MAD_scope':scope,'MAD_scale':scale,'global_residual_MAD':gm if scope=='global_residual' else None,
                'period_counts':{'years':len(period),'flagged':sum(flags.get(y) is True for y in period),'unresolved':sum(flags.get(y) is None for y in period)},
                'historical_matches':matches})
    result={'status':'RETROSPECTIVE_SENSITIVITY_NOT_REPRODUCTION','source_id':'S109','sha256':actual,
      'choices':{'window':'31 consecutive calendar years centered on target; all values required','missing':'-9.999 and blank treated as unavailable; no interpolation','global_MAD_domain':'All full-window residuals in entire supplied series','scales':'Unscaled and normal-consistency factor 1.4826; neither claimed as author implementation','comparison_period':'258 BCE through 504 CE inclusive; no year zero'},
      'variants':variants,'limits':'No event grouping, deposition integration or Monte Carlo significance computed. Published matching totals are not calibration targets.'}
    (ROOT/'analysis/ice-detection-sensitivity-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps([{k:v for k,v in x.items() if k!='historical_matches'}|{'matches':[{'margin':m['margin'],**m['counts']} for m in x['historical_matches']]} for x in variants],indent=2))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('workbook',type=Path);main(p.parse_args().workbook)
