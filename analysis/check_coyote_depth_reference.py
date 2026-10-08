"""Compare published depth/elevation references; do not recalculate fossil ages."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
samples = json.loads((ROOT / 'data/coyote-osl.json').read_text(encoding='utf-8'))['samples']
samples = [s for s in samples if s['field_id'].startswith('CCMS-')]
assert len(samples) == 4
reference = 319.0  # S138 chronology subsection, not a surveyed correction.
rows = []
for s in samples:
    common_depth = reference - s['elevation_m']
    rows.append({
        'sample_id': s['field_id'],
        'source_id': 'S32',
        'locator': 'Table 2, PDF p.8',
        'reported_depth_m': s['depth_m'],
        'reported_elevation_NAVD88_m': s['elevation_m'],
        'implied_depth_zero_elevation_m': round(s['depth_m'] + s['elevation_m'], 6),
        'depth_below_319_m': round(common_depth, 6),
        'reported_minus_common_depth_m': round(s['depth_m'] - common_depth, 6),
    })

def bracket(pairs, target):
    pairs = sorted(pairs)
    if target < pairs[0][0] or target > pairs[-1][0]:
        return {'status': 'outside_sample_range', 'sample_ids': []}
    for (a, aid), (b, bid) in zip(pairs, pairs[1:]):
        if a <= target <= b:
            return {'status': 'bracketed', 'sample_ids': [aid, bid]}
    raise AssertionError('Unclassified position')

# Basic interval classification checks, independent of the source values.
assert bracket([(1, 'a'), (3, 'b')], 2)['sample_ids'] == ['a', 'b']
assert bracket([(1, 'a'), (3, 'b')], 0)['status'] == 'outside_sample_range'
fossils = []
for specimen, elevation in [('CCMS XU1 L15 FS021 1a', 317.4),
                            ('CCMS XU1 L20 FS038 1c', 316.9)]:
    depth = reference - elevation
    fossils.append({
        'specimen_id': specimen, 'source_id': 'S138',
        'locator': 'Results: Lizard maxillae temporal resolution',
        'reported_elevation_m': elevation,
        'computed_depth_below_319_m': round(depth, 6),
        'bracket_using_reported_elevations': bracket(
            [(s['elevation_m'], s['field_id']) for s in samples], elevation),
        'bracket_if_reported_sample_depths_are_used_as_below_319': bracket(
            [(s['depth_m'], s['field_id']) for s in samples], depth),
    })
result = {
    'status': 'DIAGNOSTIC_NOT_AGE_MODEL',
    'source_ids': ['S32', 'S138'],
    'comparison_reference_elevation_m': reference,
    'samples': rows, 'fossils': fossils,
    'limits': [
        'Source depth origins and survey precision remain unresolved.',
        'Same elevation does not establish the same bed across separate locations.',
        'The mixed-reference scenario is conditional, not a recovered implementation.',
        'No replacement ages, regression, uncertainty intervals or geological correction inferred.',
    ],
}
out = ROOT / 'data/coyote-depth-reference-check.json'
out.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps(result, indent=2))
