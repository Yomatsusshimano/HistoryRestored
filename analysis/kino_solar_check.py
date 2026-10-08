"""Retrospective date compatibility check; not historical authentication.

Run with --fetch to retrieve JPL output, otherwise verify the saved response.
"""
import argparse
import csv
import hashlib
import io
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import urlopen

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data/kino-horizons-response.json"
OUT = ROOT / "data/kino-solar-check.json"
PARAMS = {
    "format": "text", "COMMAND": "'10'", "OBJ_DATA": "'NO'",
    "MAKE_EPHEM": "'YES'", "EPHEM_TYPE": "'OBSERVER'",
    "CENTER": "'500@399'", "START_TIME": "'1702-03-03 00:00'",
    "STOP_TIME": "'1702-03-04 00:00'", "STEP_SIZE": "'1 h'",
    "TIME_TYPE": "'UT'", "CAL_TYPE": "'GREGORIAN'",
    "QUANTITIES": "'2'", "ANG_FORMAT": "'DEG'",
    "APPARENT": "'AIRLESS'", "CSV_FORMAT": "'YES'",
}
URL = "https://ssd.jpl.nasa.gov/api/horizons.api?" + urlencode(PARAMS)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fetch", action="store_true")
    args = parser.parse_args()
    if args.fetch:
        with urlopen(URL, timeout=60) as response:
            raw = response.read()
        # Check identity and successful table before saving.
        text = raw.decode("utf-8")
        assert "Sun (10)" in text and "Earth (399)" in text
        assert "$$SOE" in text and "$$EOE" in text
        RAW.write_text(json.dumps({"response": text}, indent=2) + "\n", encoding="utf-8")
    text = json.loads(RAW.read_text(encoding="utf-8"))["response"]
    raw = text.encode("utf-8")
    assert "Sun (10)" in text and "Earth (399)" in text
    assert "Calendar mode   : Gregorian" in text
    assert "Center-site name: GEOCENTRIC" in text
    assert "DEC_(a-app)" in text
    table = text.split("$$SOE", 1)[1].split("$$EOE", 1)[0].strip()
    rows = list(csv.reader(io.StringIO(table)))
    assert len(rows) == 25
    records = [{"date_UT": r[0].strip(), "declination_deg": float(r[4])}
               for r in rows]
    values = [r["declination_deg"] for r in records]
    result = {
        "case_id": "C005", "source_id": "S43", "status": "SOURCED_DRAFT",
        "reviewers": [], "request_url": URL, "parameters": PARAMS,
        "response_sha256": hashlib.sha256(raw).hexdigest(),
        "reported_declination_deg": -6.5,
        "calendar_assumption": "Gregorian; source calendar unverified",
        "sampling": "Hourly Earth-center values, March 3 00:00 through March 4 00:00 UT; no exact local noon assigned",
        "sampled_declination_min_deg": min(values),
        "sampled_declination_max_deg": max(values),
        "minimum_sampled_absolute_difference_deg": min(abs(x + 6.5) for x in values),
        "maximum_sampled_absolute_difference_deg": max(abs(x + 6.5) for x in values),
        "measurement_uncertainty_deg": None,
        "statistical_compatibility": None,
        "historical_date_authenticated": False,
        "records": records,
    }
    encoded = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    if args.fetch:
        OUT.write_text(encoded, encoding="utf-8")
    else:
        assert json.loads(OUT.read_text(encoding="utf-8")) == result
    print(json.dumps({k: v for k, v in result.items() if k not in
                      {"request_url", "parameters", "records"}}, indent=2))


if __name__ == "__main__":
    main()
