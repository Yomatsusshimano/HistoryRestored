"""Retrospective Julian-calendar and local apparent-time eclipse diagnostic."""
import hashlib,importlib.metadata,inspect,json
from pathlib import Path
import astronomy as a
import astronomy.astronomy as implementation
ROOT=Path(__file__).resolve().parents[1]
pdf=ROOT/'sources/originals/astronomy/halley1715/halley1715.pdf'
assert hashlib.sha256(pdf.read_bytes()).hexdigest()=='a344be5d98d0206566d6a752fe5fefaed2ab88647ae5c2243bcd0b3c2a6a52bd'
def julian_jdn(year,month,day):
    q=(14-month)//12;y=year+4800-q;m=month+12*q-3
    return day+(153*m+2)//5+365*y+y//4-32083
def julian_time(year,month,day):
    return a.Time(julian_jdn(year,month,day)-0.5-2451545.0)
def apparent_seconds(time,observer):
    ra=a.Equator(a.Body.Sun,time,observer,True,True).ra
    return ((a.SiderealTime(time)+observer.longitude/15-ra+12)%24)*3600
def clock(seconds):
    h=int(seconds//3600);m=int((seconds-h*3600)//60);s=seconds-h*3600-m*60
    return f'{h:02}:{m:02}:{s:06.3f}'
observer=a.Observer(51.515,-0.110,0)
day=julian_time(1715,4,22);assert str(day)=='1715-05-03T00:00:00.000Z'
e=a.SearchLocalSolarEclipse(day.AddDays(-1),observer)
obsfile=ROOT/'data/halley1715-observations.json'
obs=json.loads(obsfile.read_text(encoding='utf-8'))
def parse_clock(text):
    h,m,s=map(int,text.split(':'));return h*3600+m*60+s
observed={key:parse_clock(row.get('reported_correct_time',row.get('correct_time'))) for key,row in obs['contacts'].items()}
contacts=[]
for key in ['partial_begin','total_begin','peak','total_end','partial_end']:
    event=getattr(e,key);s=apparent_seconds(event.time,observer)
    contacts.append(dict(contact=key,model_UT_label=str(event.time),sun_altitude_deg=event.altitude,
        model_apparent_local_time=clock(s),model_apparent_local_seconds=s,
        source_apparent_local_seconds=observed.get(key),model_minus_source_seconds=s-observed[key] if key in observed else None))
variants=[]
for lat in [51.505,51.515,51.525]:
    for lon in [-.130,-.110,-.090]:
        for height in [0,50]:
            o=a.Observer(lat,lon,height);v=a.SearchLocalSolarEclipse(day.AddDays(-1),o)
            variants.append(dict(latitude=lat,longitude=lon,height_m=height,kind=v.kind.name,
                total_duration_s=(v.total_end.time.ut-v.total_begin.time.ut)*86400 if v.total_begin else None,
                total_begin_apparent_seconds=apparent_seconds(v.total_begin.time,o) if v.total_begin else None))
# Integer year offsets preserve the source Julian month/day, with normal calendar conversion.
shifts=[]
for shift in range(-200,201):
    t=julian_time(1715+shift,4,22);v=a.SearchLocalSolarEclipse(t.AddDays(-1),observer)
    ondate=t.ut<=v.peak.time.ut<t.ut+1
    shifts.append(dict(year_offset=shift,source_Julian_year=1715+shift,converted_day=str(t),
        next_model_local_eclipse_peak=str(v.peak.time),eclipse_on_converted_day=ondate,
        kind_on_day=v.kind.name if ondate else None,sun_altitude_at_peak_deg=v.peak.altitude if ondate else None,
        total_duration_s=(v.total_end.time.ut-v.total_begin.time.ut)*86400 if ondate and v.total_begin else None))
rotation=[]
original_delta_t=implementation._DeltaT
try:
    for offset in [-60,-30,0,30,60]:
        # Explicit diagnostic override in this process only; original restored below.
        implementation._DeltaT=lambda ut,delta=offset:original_delta_t(ut)+delta
        v=a.SearchLocalSolarEclipse(julian_time(1715,4,22).AddDays(-1),observer)
        rotation.append(dict(delta_t_offset_s=offset,kind=v.kind.name,peak_UT_label=str(v.peak.time),
            total_duration_s=(v.total_end.time.ut-v.total_begin.time.ut)*86400 if v.total_begin else None,
            model_minus_source_begin_s=apparent_seconds(v.total_begin.time,observer)-observed['total_begin'] if v.total_begin else None,
            model_minus_source_end_s=apparent_seconds(v.total_end.time,observer)-observed['total_end'] if v.total_end else None))
finally:
    implementation._DeltaT=original_delta_t
out=dict(source_ids=['S282','S283','S284','S285','S286'],pdf_sha256=hashlib.sha256(pdf.read_bytes()).hexdigest(),observation_ledger_sha256=hashlib.sha256(obsfile.read_bytes()).hexdigest(),
    astronomy_engine_version=importlib.metadata.version('astronomy-engine'),module_sha256=hashlib.sha256(Path(inspect.getfile(a.Time)).read_bytes()).hexdigest(),
    source_date_Julian='1715-04-22',converted_date_Gregorian=str(day),observer=dict(latitude=51.515,longitude=-.110,height_m=0,role='Approximate Crane Court area; selected diagnostic coordinate, not measured historical site'),
    delta_t_seconds=a.DeltaT_EspenakMeeus(e.peak.time.ut),delta_t_model='Default Espenak-Meeus; historical rotation uncertainty not independently validated',
    model_kind=e.kind.name,model_obscuration=e.obscuration,contacts=contacts,
    source_total_duration_s=obs['reported_total_duration_s'],model_total_duration_s=(e.total_end.time.ut-e.total_begin.time.ut)*86400,
    observer_variants=variants,delta_t_stress_variants=rotation,integer_year_shift_range=[-200,200],integer_year_shifts=shifts,
    matching_day_offsets=[r['year_offset'] for r in shifts if r['eclipse_on_converted_day']],
    matching_day_total_offsets=[r['year_offset'] for r in shifts if r['kind_on_day']=='Total' and r['sun_altitude_at_peak_deg']>0],
    limits='Retrospective conditional diagnostic, not preregistration, independent review or proof of document authenticity. Fixed Julian month/day and integer year offsets only; flexible calendar/day/site changes excluded. Modern orbital model and historical DeltaT assumptions retained. Approximate coordinate and smooth-disk model; no fitting to source times.')
(ROOT/'data/halley1715-eclipse.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:out[k] for k in ['converted_date_Gregorian','delta_t_seconds','model_total_duration_s','contacts','matching_day_offsets','matching_day_total_offsets']},indent=2))
