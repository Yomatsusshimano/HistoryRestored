"""Reproduce modern point-elevation diagnostics, without replacing flood controls."""
import hashlib,json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'sources/originals/missoula/lynch-terrain'


def audit():
    ledger=json.loads((FOLDER/'acquisition.json').read_text(encoding='utf-8'))
    table=json.loads((ROOT/'data/missoula-table1.json').read_text(encoding='utf-8'))
    controls={r['table_row']:r for r in table['controls']}
    groups={12:[],45:[]}
    for q in ledger['query_results']:
        raw=(FOLDER/q['response_file']).read_bytes()
        assert hashlib.sha256(raw).hexdigest()==q['sha256'],q['id']
        r=json.loads(raw); assert r==q['response']
        assert r['location']['spatialReference']['wkid']==4326
        assert abs(r['location']['x']-q['longitude'])<1e-10 and abs(r['location']['y']-q['latitude'])<1e-10
        groups[q['table_row']].append(dict(label=q['label'],elevation_m=float(r['value']),raster_id=r['rasterId'],resolution=r['resolution'],reported_acquisition_date=r['attributes']['AcquisitionDate']))
    meta_raw=(FOLDER/'raster-metadata.json').read_bytes()
    assert hashlib.sha256(meta_raw).hexdigest()==ledger['metadata_sha256']
    meta=json.loads(meta_raw)['features'][0]['attributes']
    result=[]
    for n,rows in groups.items():
        assert {r['label'] for r in rows}=={'nominal','SW','SE','NW','NE'}
        assert all(r['raster_id']==meta['OBJECTID'] and r['resolution']==1 for r in rows)
        nominal=next(r['elevation_m'] for r in rows if r['label']=='nominal')
        c=controls[n]
        result.append(dict(table_row=n,control_id=c['id'],published_field_elevation_m=c['field_elevation_m'],
            published_model_terrain_m=c['terrain_elevation_m'],modern_nominal_elevation_m=nominal,
            modern_minus_published_field_m=nominal-c['field_elevation_m'],
            modern_minus_published_model_terrain_m=None if c['terrain_elevation_m'] is None else nominal-c['terrain_elevation_m'],
            five_queried_values_min_m=min(r['elevation_m'] for r in rows),five_queried_values_max_m=max(r['elevation_m'] for r in rows),samples=rows))
    low,high=result
    return dict(source_id='S335',controls=result,
        published_upper_minus_lower_m=high['published_field_elevation_m']-low['published_field_elevation_m'],
        modern_upper_point_minus_lower_point_m=high['modern_nominal_elevation_m']-low['modern_nominal_elevation_m'],
        minimum_separation_between_queried_value_sets_m=high['five_queried_values_min_m']-low['five_queried_values_max_m'],
        raster_id=meta['OBJECTID'],dataset=meta['Name'],vertical_datum=meta['VerticalDatum'],
        catalog_acquisition_date_unix_ms=meta['AcquisitionDate'],catalog_start_date=meta['StartDate'],catalog_end_date=meta['EndDate'],catalog_publication_date=meta['pubdate'],
        limits='Modern USGS service elevations, not ancient stages, original field validation or S27 modified terrain. Five point values do not bound all interior positions or vertical uncertainty. EPQS date 5/3/2023 differs from catalog AcquisitionDate; source-date semantics unverified. No water surface or discharge computed.',
        hydraulic_simulation_executed=False,independent_scientific_validation=False)


if __name__=='__main__':
    result=audit()
    (ROOT/'analysis/lynch-terrain-audit-result.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('controls',)},indent=2))
