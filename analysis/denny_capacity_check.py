"""Check a reported pump-capacity conversion, not achieved excavation."""
import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
record = json.loads((root / "data/denny-engineering.json").read_text(encoding="utf-8"))
pump = record["pump"]
daily = pump["guaranteed_gallons_per_minute"] * 60 * 24
assert daily == pump["calculated_gallons_per_24_hours"]
print(f"Continuous rated flow: {daily:,} gallons per 24 hours.")
print("Same gallon unit throughout; no US/Imperial conversion required.")
print("Actual operation, sediment throughput and excavation budget remain unverified.")
later = record["contemporary_press_comparison"]
later_daily = later["rated_gallons_per_minute"] * 60 * 24
assert later_daily == later["calculated_gallons_per_24_hours"]
print(f"S47 Lake Union continuous rated flow: {later_daily:,} gallons per 24 hours.")
print("Different reported installations and volume scopes; no actual-production comparison.")
