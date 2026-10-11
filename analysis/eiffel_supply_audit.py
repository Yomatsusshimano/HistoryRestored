"""Selected source-account arithmetic; no physical production validation."""
from decimal import Decimal
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
d = json.loads((ROOT / 'data/eiffel-supply-weights.json').read_text())
net = d['workshop_gross'] - d['otis_deduction_excluding_rivets']
direct = sum(d['direct_site_items'])
combined = net + direct
superstructure = combined + sum(d['other_supplier_groups'])
infra = sum(d['infrastructure_items'])
cost = sum(map(Decimal, d['money_items']))
result = {
    'scope': 'Selected printed-account arithmetic only',
    'workshop_net_kg': net,
    'direct_site_kg': direct,
    'combined_kg': combined,
    'superstructure_kg': superstructure,
    'infrastructure_kg': infra,
    'tower_metal_kg': superstructure + infra,
    'weight_checks': {
        'workshop_net': net == d['printed_workshop_net'],
        'direct_site': direct == d['printed_direct_site_total'],
        'combined': combined == d['printed_workshop_and_direct_total'],
        'superstructure': superstructure == d['printed_superstructure_total'],
        'infrastructure': infra == d['printed_infrastructure_total'],
        'tower': superstructure + infra == d['printed_tower_metal_total'],
    },
    'computed_workshop_cost_francs': str(Decimal(combined) / 100 * Decimal(d['workshop_rate_per_100kg'])),
    'computed_money_total_francs': str(cost),
    'money_minus_table_francs': str(cost - Decimal(d['printed_money_total_table'])),
    'money_minus_prose_francs': str(cost - Decimal(d['printed_money_total_prose'])),
    'limits': d['limits'],
}
(ROOT / 'analysis/eiffel-supply-audit-result.json').write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps(result, indent=2))
