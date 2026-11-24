"""Print the next Short to post, and save 4 preview frames of it.

usage: python3 -I tools/next_short.py            -> next unposted Short (JSON)
       python3 -I tools/next_short.py --yt       -> oldest Short posted to Instagram but not yet to YouTube
Reads shorts/QUEUE.csv (order,file,video,part,seconds,title) and shorts/LOG.csv.
"""
import csv, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
q = list(csv.DictReader(open(os.path.join(ROOT, "shorts/QUEUE.csv"), encoding="utf-8")))
log_path = os.path.join(ROOT, "shorts/LOG.csv")
log = list(csv.DictReader(open(log_path, encoding="utf-8"))) if os.path.exists(log_path) else []
by_file = {r["file"]: r for r in log}

if "--yt" in sys.argv:
    pick = next((r for r in q if r["file"] in by_file and by_file[r["file"]].get("ig_reel_id")
                 and not by_file[r["file"]].get("yt_id")), None)
else:
    pick = next((r for r in q if r["file"] not in by_file), None)

if not pick:
    print(json.dumps({"done": True}))
    sys.exit(0)

src = os.path.join(ROOT, pick["file"])
fr = os.path.join("/tmp", "frames_" + os.path.basename(src).replace(".mp4", ""))
os.makedirs(fr, exist_ok=True)
dur = float(pick["seconds"])
for i, t in enumerate([dur * 0.1, dur * 0.35, dur * 0.6, dur * 0.85]):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.1f}", "-i", src, "-frames:v", "1",
                    "-vf", "scale=360:-1", f"{fr}/f{i + 1}.jpg"])
pick["url"] = "https://raw.githubusercontent.com/safwanistaa/Safwan-media-/main/" + pick["file"]
pick["frames"] = fr
pick["remaining"] = sum(1 for r in q if r["file"] not in by_file) - (0 if "--yt" in sys.argv else 1)
pick["log"] = by_file.get(pick["file"])
print(json.dumps(pick, ensure_ascii=False, indent=1))
