"""Audit transcribed figures without correcting their source."""
from datetime import date
import json
from pathlib import Path

record = json.loads((Path(__file__).resolve().parents[1] / "data/denny-progress.json").read_text(encoding="utf-8"))
r = record["engineer_letter"]
total = sum(r["credited_components_cubic_yards"].values())
assert total == r["reported_total_cubic_yards"]
target = r["possible_working_days"] * r["hours_per_working_day"] * r["capacity_cubic_yards_per_hour"]
elapsed = (date.fromisoformat(r["letter_date"]) - date.fromisoformat(r["stated_start_date"])).days
print(f"Credited component sum: {total:,} cubic yards")
print(f"Capacity product: {target:,}; printed {r['reported_capacity_total_cubic_yards']:,}")
print(f"Calendar elapsed: {elapsed}; printed {r['reported_elapsed_days']}")
print(f"Credited daily average: {total/r['possible_working_days']:.6f}")
print(f"Credited hourly average: {total/r['possible_working_days']/r['hours_per_working_day']:.6f}")
print("Dates, measurement basis and transcription remain unverified against originals.")
