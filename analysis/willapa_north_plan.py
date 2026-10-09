"""Recheck the inspected plan's reported retreat arithmetic, not survey accuracy."""
import hashlib
import json
from pathlib import Path
from pypdf import PdfReader

source = Path('tmp/research/willapa-master-plan.bin')
ledger = json.loads(Path('data/willapa-north-plan.json').read_text(encoding='utf-8'))
assert hashlib.sha256(source.read_bytes()).hexdigest() == ledger['sha256']
assert source.stat().st_size == ledger['bytes']
assert len(PdfReader(source).pages) == ledger['pdf_pages']
row = ledger['reported_retreat']
duration = row['end_year'] - row['start_year']
average = row['feet'] / duration
assert duration == row['elapsed_years']
assert abs(average - row['derived_mean_feet_per_year']) < 1e-10
print('Source identity and reported-total arithmetic checked; no field/model validation.')
