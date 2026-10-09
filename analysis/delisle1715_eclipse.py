"""Paris diagnostic with unknown printed seconds preserved as unknown."""
import hashlib, importlib.metadata, inspect, json
from pathlib import Path
import astronomy as a
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'data/delisle1715-inputs.json'
x=json.loads(p.read_text(encoding='utf-8'))
o=a.Observer(x['observer']['latitude'],x['observer']['longitude'],x['observer']['height_m'])
day=a.Time.Parse('1715-05-03T00:00:00Z')
def apparent_seconds(t,o):
    ra=a.Equator(a.Body.Sun,t,o,True,True).ra
    return ((a.SiderealTime(t)+o.longitude/15-ra+12)%24)*3600
def clock(s):
    h=int(s//3600); m=int((s-3600*h)//60)
    return f'{h:02}:{m:02}:{s-3600*h-60*m:06.3f}'
def parse(s):
    h,m,s=map(int,s.split(':'));return h*3600+m*60+s
def diagnostic(observer):
    e=a.SearchLocalSolarEclipse(day.AddDays(-1),observer)
    contacts={}
    for k in ['partial_begin','peak','partial_end']:
        v=getattr(e,k);s=apparent_seconds(v.time,observer)
        contacts[k]=dict(UT_label=str(v.time),apparent_local_time=clock(s),apparent_seconds=s,sun_altitude_deg=v.altitude)
    return dict(kind=e.kind.name,obscuration_area_fraction=e.obscuration,contacts=contacts,
                delta_t_s=a.DeltaT_EspenakMeeus(e.peak.time.ut))
baseline=diagnostic(o)
baseline['partial_begin_model_minus_reported_s']=[baseline['contacts']['partial_begin']['apparent_seconds']-parse(t) for t in x['contacts']['partial_begin']['tokens']]
baseline['peak_model_minus_nominal_minute_label_s']=baseline['contacts']['peak']['apparent_seconds']-parse('09:18:00')
baseline['partial_end_model_minus_nominal_reference_s']=baseline['contacts']['partial_end']['apparent_seconds']-parse('10:29:00')
variants=[]
for lat in [48.8362,48.8462,48.8562]:
    for lon in [2.3172,2.3372,2.3572]:
        for h in [0,50]:
            v=diagnostic(a.Observer(lat,lon,h))
            variants.append(dict(latitude=lat,longitude=lon,height_m=h,**v))
out=dict(source_ids=['S288','S283'],input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
         astronomy_engine_version=importlib.metadata.version('astronomy-engine'),
         module_sha256=hashlib.sha256(Path(inspect.getfile(a.Time)).read_bytes()).hexdigest(),
         observer=x['observer'],baseline=baseline,observer_variants=variants,
         limits='Retrospective conditional local-apparent-time interpretation, fixed unfitted approximate site. '
                'Source peak/end seconds unknown; nominal-label differences are not measured residuals. '
                'Digits are not area obscuration. No confidence bounds or wholly independent orbital/rotation validation.')
(ROOT/'data/delisle1715-results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps(baseline,indent=2))
