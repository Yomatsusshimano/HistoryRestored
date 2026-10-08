"""Map audited coordinates without geocoding missing fossil localities."""
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
CASE_IDS=['C003','C009','C011','C012','C013','C014','C015','C016','C022']
REPORTS=['ARCTIC-CHRONOLOGY','ARCTIC-CHRONOLOGY','SLOTH-CHRONOLOGY','MUSKOX-METHODS','ARCTIC-HYENA','CAMP-CENTURY','COYOTE-CANYON','THISTLE-CREEK','CAMPO-LABORDE']
BASE='https://github.com/Yomatsusshimano/HistoryRestored/blob/main/'
def load(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def save(p,d): (ROOT/p).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')

def main():
    cases={c['id']:c for c in load('data/cases.json')['cases']}
    sources={s['id']:s for s in load('data/sources.json')['sources']}
    features=[]; coverage=[]
    def point(cid,ident,lat,lon,role,sid,locator,datum,report,color):
        assert -90<=lat<=90 and -180<=lon<=180
        assert sid in sources
        features.append({'type':'Feature','geometry':{'type':'Point','coordinates':[lon,lat]},
            'properties':{'name':ident,'case_id':cid,'coordinate_role':role,
                'source_id':sid,'source_url':sources[sid]['url'],'source_locator':locator,
                'source_datum':datum,'positional_uncertainty_metres':None,
                'display_assumption':'Reported longitude/latitude plotted without datum transformation; orientation only, not survey precision.',
                'death_site_established':False,'event_correlation_established':False,
                'dating_and_context_audit':BASE+'research/'+report+'.md',
                'marker-color':color,'marker-size':'small'}})
    for cid,report in zip(CASE_IDS,REPORTS):
        c=cases[cid]; before=len(features); coord=c['coordinates']
        if coord is not None:
            sid=coord.get('source_id','S24' if cid=='C013' else None)
            point(cid,c['title'],coord['latitude'],coord['longitude'],coord.get('scope',coord.get('role')),sid,
                coord.get('locator','Locality paragraph, article p.3'),coord.get('datum'),report,
                '#b7791f' if cid=='C003' else '#805ad5' if cid=='C014' else '#276749')
        if cid=='C015':
            for row in load('data/coyote-osl.json')['samples']:
                point(cid,row['field_id']+' / '+row['lab_id'],row['latitude'],row['longitude'],
                    'Sediment sampling position ('+row['context']+'); not a fossil findspot',row['source_id'],
                    row['locator'],row['horizontal_datum'],report,'#2b6cb0')
        coverage.append({'case_id':cid,'title':c['title'],'reported_place':c['place'],
            'mapped_features':len(features)-before,'coordinate_status':'AUDITED_COORDINATE_AVAILABLE' if len(features)>before else 'NOT_RECOVERED_IN_AUDIT',
            'missing_coordinate_is_absence_evidence':False,'audit':BASE+'research/'+report+'.md'})
    assert len({f['properties']['name'] for f in features})==len(features)
    save('data/wildlife-localities.geojson',{'type':'FeatureCollection','features':features})
    save('data/wildlife-map-coverage.json',{'scope':'Nine selected audited cases; not species ranges or exhaustive geographic coverage',
        'coordinate_case_count':sum(r['mapped_features']>0 for r in coverage),
        'unmapped_case_count':sum(r['mapped_features']==0 for r in coverage),
        'point_count':len(features),'cases':coverage})
    print(f'{len(features)} features; {sum(r["mapped_features"]>0 for r in coverage)} mapped cases; {sum(r["mapped_features"]==0 for r in coverage)} unmapped cases')

if __name__=='__main__': main()
