"""Compare reported collection identity; do not decode excavation notation."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
lead_path = ROOT / 'data/jeremie-holotype-code.json'
catalog_path = ROOT / 'data/ufvp-dated-specimen-links.json'
lead = json.loads(lead_path.read_text(encoding='utf-8'))
catalog = json.loads(catalog_path.read_text(encoding='utf-8'))
matches = [row for row in catalog['matches']
           if row['catalog_number_normalized'] == lead['catalog_number']]
assert len(matches) == 1, 'Holotype catalog join must be unique'
record = matches[0]['raw_fields']
result = {
    'input_sha256': {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in (lead_path, catalog_path)},
    'source_ids': [lead['source_id'], catalog['source_id']],
    'accession': f"{record['institutionCode']}:{record['collectionCode']}:{record['catalogNumber']}",
    'unique_catalog_match': True,
    'taxon_agrees': record['scientificName'] == lead['taxon'],
    'collection_date_agrees': record['eventDate'] == lead['collection_date'],
    'catalog_type_status': record['typeStatus'],
    'catalog_location_id': record['locationID'],
    'catalog_field_number_raw': record['fieldNumber'],
    'survey_stratigraphic_code_raw': lead['stratigraphic_code_raw'],
    'dated_same_taxon_accessions': [r['catalog_number_normalized']
                                  for r in catalog['matches']
                                  if r['raw_fields']['scientificName'] == lead['taxon']
                                  and r['target'].get('lab_id')],
    'depth_resolved': False,
    'dated_specimen_to_unit_join_resolved': False,
    'interpretation': 'Collection identity agreement; no independent physical authentication or dating/depth transfer.'
}
assert result['taxon_agrees'] and result['collection_date_agrees']
out = ROOT / 'analysis/jeremie-holotype-code-check-result.json'
out.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(result['accession'], 'catalog/date/taxon agree; code key and dated-specimen layer remain unknown')
