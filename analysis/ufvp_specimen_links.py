"""Inspect pinned museum Darwin Core export; catalog association is not stratigraphy."""
import csv,io,json,zipfile,hashlib,collections,xml.etree.ElementTree as ET
from pathlib import Path
archive=Path('tmp/research/ufvp-1.181.zip')
sloths=json.loads(Path('data/dating-records.json').read_text(encoding='utf-8'))['samples']
sloths=[r for r in sloths if r.get('case_id')=='C011' and r.get('source_id')=='S22']
rodents=json.loads(Path('data/haiti-rodent-dates.json').read_text(encoding='utf-8'))['rows']
targets={r['museum_catalog_id'].split()[-1]:{'source_id':'S22','lab_id':r['field_id']} for r in sloths}
targets.update({r['museum_id'].split()[-1]:{'source_id':'S36','lab_id':r['lab_id']} for r in rodents})
targets['73946']={'source_id':None,'lab_id':None,'role':'Locality holotype comparator; not dated here'}
z=zipfile.ZipFile(archive)
meta=z.read('meta.xml'); eml=z.read('eml.xml')
hits=[]; total=0; loccounts=collections.Counter(); batcount=0; macros=[]; bat_rows=[]; fields=None
with z.open('occurrence.txt') as f:
    reader=csv.DictReader(io.TextIOWrapper(f,encoding='utf-8'),delimiter='\t',quoting=csv.QUOTE_NONE)
    fields=reader.fieldnames
    for r in reader:
        total+=1
        catalog=r['catalogNumber'].lstrip('0')
        if catalog in targets:
            hits.append({'target':targets[catalog],'catalog_number_normalized':catalog,'raw_fields':r})
        loc=r.get('locality','').lower()
        if 'jerem' in loc or 'jérém' in loc:
            loccounts[r['locality']]+=1
            if r['order']=='Chiroptera':
                batcount+=1
                bat_rows.append(r)
            if r['genus']=='Macrotus': macros.append(r)
assert total==554765
assert len(hits)==len(targets)==18
assert all(sum(h['catalog_number_normalized']==n for h in hits)==1 for n in targets)
ids={h['raw_fields']['id'] for h in hits}
media=[]; media_count=0
with z.open('multimedia.txt') as f:
    reader=csv.DictReader(io.TextIOWrapper(f,encoding='utf-8'),delimiter='\t',quoting=csv.QUOTE_NONE)
    media_fields=reader.fieldnames
    for r in reader:
        media_count+=1
        if r[media_fields[0]] in ids: media.append(r)
out={'date':'2026-10-09','source_id':'S321','dataset_uuid':'2fba9985-ac30-46cb-99bf-91ccde0d8d2f','version':'1.181','download_url':'https://ipt.floridamuseum.ufl.edu/ipt/archive.do?r=ufvp&v=1.181','archive_bytes':archive.stat().st_size,'archive_sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'metadata_sha256':hashlib.sha256(meta).hexdigest(),'eml_sha256':hashlib.sha256(eml).hexdigest(),'occurrence_records_scanned':total,'occurrence_columns':fields,'selection':'Exact normalized catalog numbers for all9S22sloths, all8S36rodents, andUF73946locality holotype comparator. All records scanned.','matches':hits,'jeremie_locality_counts':dict(loccounts),'jeremie_order_Chiroptera_count':batcount,'jeremie_Macrotus_candidates':macros,'multimedia_records_scanned':media_count,'target_multimedia_matches':media,'limits':['Published catalog records; physical specimen identity and field record chain not independently authenticated.','eventDate is catalog collection metadata, never biological age or sediment age.','fieldNumber is an uninterpreted code, not a depth; codes are retained literally.','Export has no excavation-depth/contact or bag/unit field; blank geodeticDatum/coordinateUncertainty not filled from precision.','No Macrotus candidate in selected locality-name search does not prove specimen absence from museum.','All coordinates are catalog labels, not animal findspots or independent site movement measurements.']}
out['jeremie_order_Chiroptera_rows']=bat_rows
out['license_as_published']='Florida Museum of Natural History, CC BY-NC4.0; original downloadable export linked; selected record transcription and analysis attributed.'
Path('data/ufvp-dated-specimen-links.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Scanned',total,'exact targets',len(hits),'media',media_count,'targetmedia',len(media),'JEREMIEBATS',batcount)
for h in hits:
 r=h['raw_fields']; print(r['catalogNumber'],r['scientificName'],r['fieldNumber'],r['eventDate'],r['locationID'],r['locality'])
print(eml.decode()[:2600])
