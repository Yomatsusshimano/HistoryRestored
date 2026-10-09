"""Search pinned museum metadata by taxon and accession; never infer assay identity."""
import collections
import csv
import hashlib
import io
import json
import re
from pathlib import Path
import zipfile

ROOT = Path(__file__).resolve().parents[1]
archive = ROOT / 'tmp/research/ufvp-1.181.zip'
reference = json.loads((ROOT / 'data/ufvp-dated-specimen-links.json').read_text(encoding='utf-8'))
digest = hashlib.sha256(archive.read_bytes()).hexdigest()
assert digest == reference['archive_sha256'], 'Pinned archive changed'
targets = {'282171', '307265'}  # S324 S2Table page1, visually inspected
targets_found = []
macrotus_worldwide = []
haitian_bats = []
total = 0
assay_token_hits = []
with zipfile.ZipFile(archive) as z:
    with z.open('occurrence.txt') as f:
        reader = csv.DictReader(io.TextIOWrapper(f, encoding='utf-8'),
                                delimiter='\t', quoting=csv.QUOTE_NONE)
        for record in reader:
            total += 1
            if 'beta345518' in re.sub(r'[-\s]', '', '\t'.join(record.values())).casefold():
                assay_token_hits.append(record)
            number = record['catalogNumber'].lstrip('0')
            if number in targets:
                targets_found.append(record)
            scientific_genus = record['scientificName'].split(' ', 1)[0].casefold()
            if record['genus'].casefold() == 'macrotus' or scientific_genus == 'macrotus':
                macrotus_worldwide.append(record)
            if record['country'].casefold() == 'haiti' and record['order'].casefold() == 'chiroptera':
                haitian_bats.append(record)
assert total == reference['occurrence_records_scanned']
assert all(sum(r['catalogNumber'].lstrip('0') == n for r in targets_found) == 1 for n in targets)
haitian_macrotus = [r for r in macrotus_worldwide if r['country'].casefold() == 'haiti']
jeremie = [r for r in haitian_bats if 'jerem' in r['locality'].casefold() or 'jérém' in r['locality'].casefold()]
out = {
    'date': '2026-10-09', 'source_ids': ['S321', 'S324'],
    'archive_sha256': digest, 'dataset_version': reference['version'],
    'occurrence_records_scanned': total,
    'selection': {
        'taxon': 'genus equals Macrotus OR first scientificName token equals Macrotus, case-insensitive',
        'country': 'country equals Haiti, case-insensitive',
        'bat_census': 'country equals Haiti AND order equals Chiroptera, case-insensitive',
        'target_accessions': sorted(targets),
        'accession_role': 'Reported Jean Paul specimens in S324, not dated Beta345518'
    },
    'macrotus_worldwide_record_count': len(macrotus_worldwide),
    'macrotus_country_counts': dict(collections.Counter(r['country'] for r in macrotus_worldwide)),
    'haitian_macrotus_records': haitian_macrotus,
    'haitian_chiroptera_record_count': len(haitian_bats),
    'haitian_chiroptera_locality_counts': dict(collections.Counter(r['locality'] for r in haitian_bats)),
    'exact_target_records': targets_found,
    'jeremie_name_bat_records': jeremie,
    'assay_token_search': {
        'method': 'All occurrence-cell values searched for Beta345518 after removing whitespace and hyphens, case-insensitive',
        'hits': assay_token_hits,
        'scope': 'This pinned occurrence export only; not notebooks, labels, lab submissions or museum holdings'
    },
    'assay_accession_resolved': False,
    'limits': [
        'Catalog metadata, not original labels, physical authentication or a complete census of specimens held.',
        'Incomplete taxonomic and geographic fields can exclude records from selectors.',
        '307265 is Chiroptera in this export and Macrotus waterhousii in S324; no taxonomic correction or change sequence inferred.',
        'No dedicated radiocarbon lab-identifier field exists; a bounded free-cell token search does not prove absence from original records.',
        'Record counts are not numbers of individual animals, fossil elements or independently dated specimens.',
        'Collection dates, catalog modification dates and identification dates are distinct; none dates a bone or sediment.',
        'Reported locality/coordinate differences are preserved without interpreting movement or assigning an unknown datum.'
    ]
}
path = ROOT / 'data/haiti-bat-catalog-search.json'
path.write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('All occurrence rows:', total, 'Haitian Chiroptera:', len(haitian_bats),
      'Haitian Macrotus:', len(haitian_macrotus), 'Exact Jean Paul matches:', len(targets_found))
print('Beta345518 token hits:', len(assay_token_hits))
