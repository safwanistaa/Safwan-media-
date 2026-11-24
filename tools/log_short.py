"""Record a posted Short in shorts/LOG.csv (creates or updates the row for that file).

usage: python3 -I tools/log_short.py <file> key=value [key=value ...]
keys: date, slot, ig_reel_id, ig_trial_id, yt_id, caption, note
"""
import csv, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
path = os.path.join(ROOT, "shorts/LOG.csv")
cols = ["file", "date", "slot", "ig_reel_id", "ig_trial_id", "yt_id", "caption", "note"]
rows = list(csv.DictReader(open(path, encoding="utf-8"))) if os.path.exists(path) else []
f = sys.argv[1]
row = next((r for r in rows if r["file"] == f), None)
if row is None:
    row = {c: "" for c in cols}
    row["file"] = f
    rows.append(row)
for kv in sys.argv[2:]:
    k, v = kv.split("=", 1)
    row[k] = v
with open(path, "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, fieldnames=cols)
    w.writeheader()
    w.writerows(rows)
print("logged", f)
