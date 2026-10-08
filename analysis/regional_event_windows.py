"""Retrospective interval feasibility; not a dating model or confidence test."""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def minimum_span(intervals):
    if not intervals or any(len(x) != 2 or x[0] > x[1] for x in intervals):
        raise ValueError("Require ordered, nonempty closed intervals")
    return max(0, max(x[0] for x in intervals) - min(x[1] for x in intervals))


def main():
    paths = ["data/bonneville-dates.json", "data/electron-model-selection.json"]
    b, e = [json.loads((ROOT / p).read_text(encoding="utf-8")) for p in paths]
    bm = b["reported_model"]
    em = e["intervals_CE"]
    comparisons = []
    for level, bkey in [("95.4", "calendar_CE_2sigma"), ("99.7", "calendar_CE_3sigma")]:
        variants = [(name, em[name][level]) for name in
                    ("figure_A_five_samples", "figure_B_seven_samples")]
        if level == "99.7":
            variants.append(("release_abstract_99_7", em["release_abstract_99_7"]))
        for name, interval in variants:
            gap = minimum_span([bm[bkey], interval])
            comparisons.append({
                "reported_marginal_percent": level,
                "bonneville_CE": bm[bkey], "electron_variant": name,
                "electron_CE": interval, "minimum_touching_window_years": gap,
                "duration_feasibility": {str(d): d >= gap for d in [0, 1, 10, 25, 50, 100]}
            })
    result = {
        "status": "RETROSPECTIVE_CONDITIONAL_COMPARISON",
        "case_ids": ["C019", "C020"],
        "source_ids": ["S68", "S72", "S73"],
        "inputs_sha256": {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths},
        "definition": "Smallest closed window intersecting both reported calendar intervals; no joint confidence assigned.",
        "comparisons": comparisons,
        "limits": [
            "Intervals and event associations are accepted conditionally, not recalibrated or independently validated.",
            "Published variants are dependent alternatives, not independent replications.",
            "A feasible duration is not evidence of a common mechanism or continuous episode.",
            "A common additive calendar shift preserves all separations."
        ]
    }
    target = ROOT / "analysis/regional-event-windows-result.json"
    target.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(comparisons, indent=2))


if __name__ == "__main__":
    main()
