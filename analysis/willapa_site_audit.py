"""S274 Table1 transcription and environment-conditioned Table2 diagnostics."""
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean
from pypdf import PdfReader

ROOT=Path(__file__).resolve().parents[1]

def main():
    grain=json.loads((ROOT/'data/willapa-grain-inputs.json').read_text(encoding='utf-8'))
    original=ROOT/grain['original_path']
    assert hashlib.sha256(original.read_bytes()).hexdigest()==grain['sha256']
    pdf=PdfReader(original)
    sites=[]
    pattern=r'(?m)^\s*(W\d+|KI11|T\d+|G1)\s+(\d{7})\s+(\d{6})\s+(ITF|IAB|TIS|STC|ITM)\s+(-?\d+(?:\.\d+)?)\s+(\d+(?:\.\d+)?)(?:[ \t]+(na|\d+))?[ \t]*$'
    for index in [8,9]:
        for match in re.finditer(pattern,pdf.pages[index].extract_text()):
            site,n,e,setting,top,length,short=match.groups()
            sites.append(dict(site=site,utm_northing_m=int(n),utm_easting_m=int(e),
                modern_setting=setting,core_top_m_MTL=float(top),reported_core_length_m=float(length),
                shortening_percent=None if short in [None,'na'] else int(short),
                shortening_raw=short,locator=f'PDF{index+1}/Table1',raw=match.group().strip()))
    assert len(sites)==40 and len({s['site'] for s in sites})==40
    assert {s['site'] for s in sites}=={f'W{i}' for i in range(1,31)}|{'KI11','G1'}|{f'T{i}' for i in range(1,9)}
    inp=dict(source_id='S274',source_sha256=grain['sha256'],original_path=grain['original_path'],
        inspected='PDF9-10/Table1 all40rows and Figure6 visually inspected; extraction preserves literal classifications',
        coordinate_system=dict(source_label='UTM Sector10T',units='metres',horizontal_datum=None,epsg=None,
            limitation='Datum not declared in Table1. No geographic transformation or cross-dataset overlay performed.'),
        elevation_reference='Mean tidal level, not NAVD88; no vertical conversion performed',
        sites=sites)
    (ROOT/'data/willapa-sites.json').write_text(json.dumps(inp,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lookup={s['site']:s for s in sites}
    by_setting=defaultdict(list)
    for c in grain['cells']:
        if c['sand_weight_percent'] is not None: by_setting[lookup[c['site']]['modern_setting']].append(c)
    groups={}
    for label,cells in by_setting.items():
        by_core=defaultdict(list)
        for c in cells: by_core[c['site']].append(c['sand_weight_percent'])
        shallow=[c for c in cells if c['depth_end_m']<=3]
        groups[label]=dict(site_ids=sorted(by_core),core_n=len(by_core),composition_n=len(cells),
            mean_sand_weight_percent=mean(c['sand_weight_percent'] for c in cells),
            equal_core_mean_sand_weight_percent=mean(mean(v) for v in by_core.values()),
            shallow_composition_n=len(shallow),shallow_mean_sand_weight_percent=mean(c['sand_weight_percent'] for c in shallow))
    vib=[s for s in sites if s['site'].startswith('W')]
    shortening=[s['shortening_percent'] for s in vib if s['shortening_percent'] is not None]
    shortening_all=[s['shortening_percent'] for s in sites if (s['site'].startswith('W') or s['site']=='KI11') and s['shortening_percent'] is not None]
    measured=[c for c in grain['cells'] if c['sand_weight_percent'] is not None]
    selections={
        'all_table_and_note': measured,
        'exclude_modern_STC': [c for c in measured if lookup[c['site']]['modern_setting']!='STC'],
        'modern_ITF_only': [c for c in measured if lookup[c['site']]['modern_setting']=='ITF'],
        'dated_Table4_sites': [c for c in measured if c['site'] in ['W6','W8','W12','W13','W16','W18','W22','W24','W27','W30']],
    }
    selection_stats={k:dict(n=len(v),mean_sand_weight_percent=mean(c['sand_weight_percent'] for c in v),
        plus20_assumed_zero_mean_percent=sum(c['sand_weight_percent'] for c in v)/(len(v)+20),
        limitations='Declared diagnostic selection; not an authenticated author selection or baywide weighting.') for k,v in selections.items()}
    beyond=[]
    for c in grain['cells']:
        if c['sand_weight_percent'] is None: continue
        length=lookup[c['site']]['reported_core_length_m']
        # Strictly beyond length allowing half0.1m printed precision; not a correction.
        if c['depth_start_m']>length+.05:
            beyond.append(dict(site=c['site'],depth_start_m=c['depth_start_m'],depth_end_m=c['depth_end_m'],
                reported_core_length_m=length,raw=c['raw'],note_only=c['note_only']))
    out=dict(source_id='S274',table1_site_n=len(sites),
        W_only_modern_setting_counts=dict(Counter(s['modern_setting'] for s in vib)),
        W_and_KI11_modern_setting_counts=dict(Counter(s['modern_setting'] for s in sites if s['site'].startswith('W') or s['site']=='KI11')),
        prose_W_only_counts=dict(ITF=18,IAB=7,STC=2,TIS=2,ITM=1),
        W_only_shortening=dict(n=len(shortening),mean_percent=mean(shortening),min_percent=min(shortening),max_percent=max(shortening)),
        W_and_KI11_shortening=dict(n=len(shortening_all),mean_percent=mean(shortening_all),min_percent=min(shortening_all),max_percent=max(shortening_all)),
        environment_groups=groups,selection_sensitivities=selection_stats,composition_bins_starting_beyond_reported_length=beyond,
        limitations=['Modern classifications are not the historical facies of every core sample.',
            'Reported bin starts/lengths may use different depth conventions; no sample is discarded or relocated.',
            'Class means are descriptive sample summaries, not class areas or measured baywide volume weights.',
            'No common event horizon or held-out prediction established.'])
    (ROOT/'data/willapa-site-audit.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out,indent=2))

    # Native reported UTM coordinates only; no inferred datum, map registration or age axis.
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    colors=dict(ITF='#277da8',IAB='#bc6c25',STC='#7557a1',TIS='#42954a',ITM='#c13f66')
    fig,(ax,bx)=plt.subplots(1,2,figsize=(12,7),gridspec_kw={'width_ratios':[1.05,1]})
    for setting,color in colors.items():
        subset=[s for s in sites if s['modern_setting']==setting and (s['site'].startswith('W') or s['site']=='KI11')]
        ax.scatter([s['utm_easting_m']/1000 for s in subset],[s['utm_northing_m']/1000 for s in subset],color=color,label=setting,s=28)
    offsets={'W2':(-12,18),'W3':(12,-12),'W4':(12,9),'W8':(8,9),'W9':(-26,-12),
        'W14':(-32,14),'W15':(-10,-8),'W16':(4,-25),'W17':(8,3),'W21':(-25,-12)}
    for s in sites:
        if s['site'].startswith('W') or s['site']=='KI11':
            ax.annotate(s['site'],(s['utm_easting_m']/1000,s['utm_northing_m']/1000),xytext=offsets.get(s['site'],(4,2)),textcoords='offset points',fontsize=7,
                arrowprops=dict(arrowstyle='-',color='#888888',lw=.5) if s['site'] in offsets else None)
    ax.set(xlabel='Reported UTM easting (km)',ylabel='Reported UTM northing (km)',title='Core sites: Table1 modern setting')
    ax.legend(fontsize=8,loc='lower left');ax.grid(alpha=.2)
    labels=list(groups); vals=[groups[k]['mean_sand_weight_percent'] for k in labels]
    bx.barh(labels,vals,color=[colors[k] for k in labels]);bx.set_xlim(0,100)
    for i,k in enumerate(labels):bx.text(2,i,f'{vals[i]:.1f}%  (n={groups[k]["composition_n"]})',va='center',fontsize=9,color='white')
    bx.set(xlabel='Mean sample sand fraction by weight (%)',title='All printed compositions, grouped by modern site')
    bx.grid(axis='x',alpha=.2);bx.invert_yaxis()
    fig.suptitle('Willapa sampling context — descriptive, not an event reconstruction',fontsize=13)
    fig.text(.05,.035,'S274 Table1–2. Horizontal datum unreported; no geographic transformation.\nITF flat; IAB bank; STC subtidal bank; TIS inlet shoal; ITM marsh. Sample counts are not area weights.',fontsize=9)
    fig.tight_layout(rect=[0,.10,1,.95])
    fig.savefig(ROOT/'research/figures/willapa-site-context.png',dpi=150)
    plt.close(fig)

if __name__=='__main__': main()
