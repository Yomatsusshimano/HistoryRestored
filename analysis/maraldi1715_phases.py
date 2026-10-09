"""Unfitted clock/diameter diagnostic; original derived rows stay dependent."""
from pathlib import Path
import hashlib,importlib.metadata,inspect,json,math
import astronomy as a
import astronomy.astronomy as impl
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'data/maraldi1715-inputs.json';x=json.loads(p.read_text(encoding='utf-8'))
o=a.Observer(x['observer']['latitude'],x['observer']['longitude'],0)
day=a.Time.Parse('1715-05-03T00:00:00Z')
def seconds(s):
    v=list(map(int,s.split(':')));return v[0]*3600+v[1]*60+(v[2] if len(v)==3 else 0)
def apparent(t):
    return ((a.SiderealTime(t)+o.longitude/15-a.Equator(a.Body.Sun,t,o,True,True).ra+12)%24)*3600
def at_clock(token):
    target=seconds(token);t=day.AddDays(target/86400-o.longitude/360)
    for _ in range(5):t=t.AddDays((target-apparent(t))/86400)
    assert abs(apparent(t)-target)<.001
    return t
def magnitude(t):
    s=a.Equator(a.Body.Sun,t,o,True,True);m=a.Equator(a.Body.Moon,t,o,True,True)
    sr=math.asin(impl._SUN_RADIUS_AU/s.dist)
    mr=math.asin(impl._MOON_POLAR_RADIUS_AU/m.dist)
    sep=math.radians(a.AngleBetween(s.vec,m.vec))
    return max(0,(sr+mr-sep)/(2*sr))
e=a.SearchLocalSolarEclipse(day.AddDays(-1),o)
tables={}
for name in ['measured_rows','derived_rows']:
    rows=[]
    for v in x[name]:
        measured=(v['digits']+v['digit_minutes']/60)/12
        model=magnitude(at_clock(v['time_token']))
        rows.append(dict(**v,interpreted_diameter_fraction=measured,model_diameter_fraction=model,
                         model_minus_reported=model-measured,
                         clock_role='Reported seconds' if v['seconds_explicit'] else 'Nominal minute label; actual seconds unknown'))
    tables[name]=rows
out=dict(source_ids=['S289','S283'],input_sha256=hashlib.sha256(p.read_bytes()).hexdigest(),
         astronomy_engine_version=importlib.metadata.version('astronomy-engine'),
         module_sha256=hashlib.sha256(Path(inspect.getfile(a.Time)).read_bytes()).hexdigest(),
         observer=x['observer'],kind=e.kind.name,
         model_peak_apparent_seconds=apparent(e.peak.time),model_peak_diameter_fraction=magnitude(e.peak.time),
         model_partial_begin_apparent_seconds=apparent(e.partial_begin.time),
         model_partial_end_apparent_seconds=apparent(e.partial_end.time),
         partial_begin_model_minus_reported_s=apparent(e.partial_begin.time)-seconds(x['partial_begin']),
         partial_end_model_minus_reported_s=apparent(e.partial_end.time)-seconds(x['partial_end']),
         **tables, limits='Approximate fixed site, assumed local apparent clocks, conditional digit convention. '
          'Apparent angular-disc model using library polar lunar radius1736km; no limb/instrument/clock fit. '
          'Nominal missing seconds set to zero only as model evaluation labels, not recovered observations. '
          'Derived table is dependent; anomalous source tokens retained. No error distribution or confidence claim.')
(ROOT/'data/maraldi1715-results.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,ax=plt.subplots(figsize=(10,5.5))
curve_times=list(range(8*3600+10*60,10*3600+31*60,30))
def token(s):return f'{s//3600:02}:{s%3600//60:02}:{s%60:02}'
ax.plot([s/3600 for s in curve_times],[magnitude(at_clock(token(s))) for s in curve_times],
        color='#263e63',label='Fixed approximate-site angular-disc model')
for name,label,marker,color in [('measured_rows','Printed measured phases','o','#167d86'),
                               ('derived_rows','Source-derived phases (dependent)','x','#bc7332')]:
    ax.scatter([seconds(v['time_token'])/3600 for v in tables[name]],
               [v['interpreted_diameter_fraction'] for v in tables[name]],
               marker=marker,s=28,color=color,label=label,zorder=3)
v=next(v for v in tables['measured_rows'] if v['time_token']=='10:06')
ax.annotate('Printed late token 6 retained;\ntime interpretation unresolved',
            xy=(10.1,v['interpreted_diameter_fraction']),xytext=(9.35,.08),
            fontsize=9,arrowprops=dict(arrowstyle='->',color='#555'))
ticks=[8.25,8.5,8.75,9,9.25,9.5,9.75,10,10.25,10.5]
ax.set_xticks(ticks,[f'{int(t):02}:{round((t-int(t))*60):02}' for t in ticks])
ax.set(xlabel='Interpreted local apparent solar time (unknown seconds use nominal labels)',
       ylabel='Diameter fraction: conditional digit conversion',ylim=(0,1.03),
       title='Maraldi 1715 phases: source values retained, no fitted clock/site correction')
ax.grid(alpha=.2);ax.legend(loc='upper left',fontsize=9)
fig.text(.5,.015,'Not disc-area obscuration; no recovered clock, site or instrument confidence bounds.',ha='center',fontsize=9)
fig.tight_layout(rect=[0,.04,1,1])
fig.savefig(ROOT/'research/figures/maraldi1715-phases.png',dpi=160)
plt.close(fig)
print(json.dumps({k:v for k,v in out.items() if k not in tables},indent=2))
