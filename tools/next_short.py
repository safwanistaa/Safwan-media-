"""Print the next Short to post on a track, and save 4 preview frames of it.

usage: python3 -I tools/next_short.py --track public   -> next Short for the normal (public) Reel
       python3 -I tools/next_short.py --track trial    -> next Short for the Trial Reel
       python3 -I tools/next_short.py --yt             -> oldest Short that is a public Reel but not yet on YouTube

MIXING RULE (Safwan, 27 Nov 2026):
  Phase 1: public Reels take the ODD-numbered videos (v01, v03, v05 ...), Trial Reels take the
           EVEN-numbered videos (v02, v04 ...). Each track goes through its videos in order,
           all parts of one video (p1..p6) before the next video.
  Phase 2: once a track has used up its phase-1 videos, it switches: public takes the EVEN videos
           (whatever was trialled), trial takes the ODD videos (whatever was public).
  A Short that already has the id for a track (ig_reel_id for public, ig_trial_id for trial) is
  never posted on that track again. Rows noted skipped-bad are skipped on both tracks.
Reads shorts/QUEUE.csv (order,file,video,part,seconds,title) and shorts/LOG.csv.
"""
import csv, json, os, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
q = list(csv.DictReader(open(os.path.join(ROOT, "shorts/QUEUE.csv"), encoding="utf-8")))
log_path = os.path.join(ROOT, "shorts/LOG.csv")
log = list(csv.DictReader(open(log_path, encoding="utf-8"))) if os.path.exists(log_path) else []
by_file = {r["file"]: r for r in log}


def has(r, key):
    row = by_file.get(r["file"])
    return bool(row and (row.get(key) or "skipped-bad" in (row.get("note") or "")))


def odd(r):
    return int(r["video"]) % 2 == 1


if "--yt" in sys.argv:
    track, phase = "yt", None
    todo = [r for r in q if by_file.get(r["file"], {}).get("ig_reel_id") and not by_file[r["file"]].get("yt_id")]
else:
    track = sys.argv[sys.argv.index("--track") + 1] if "--track" in sys.argv else ""
    if track not in ("public", "trial"):
        sys.exit("usage: next_short.py --track public|trial   (or --yt)")
    key = "ig_reel_id" if track == "public" else "ig_trial_id"
    phase1 = [r for r in q if odd(r) == (track == "public")]
    phase2 = [r for r in q if odd(r) != (track == "public")]
    todo = [r for r in phase1 if not has(r, key)]
    phase = 1
    if not todo:
        todo = [r for r in phase2 if not has(r, key)]
        phase = 2

if not todo:
    print(json.dumps({"done": True, "track": track}))
    sys.exit(0)

pick = dict(todo[0])
src = os.path.join(ROOT, pick["file"])
fr = os.path.join("/tmp", "frames_" + os.path.basename(src).replace(".mp4", ""))
os.makedirs(fr, exist_ok=True)
dur = float(pick["seconds"])
for i, t in enumerate([dur * 0.1, dur * 0.35, dur * 0.6, dur * 0.85]):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{t:.1f}", "-i", src, "-frames:v", "1",
                    "-vf", "scale=360:-1", f"{fr}/f{i + 1}.jpg"])
pick["track"] = track
pick["phase"] = phase
pick["url"] = "https://raw.githubusercontent.com/safwanistaa/Safwan-media-/main/" + pick["file"]
pick["frames"] = fr
pick["remaining_on_track"] = len(todo) - 1
pick["log"] = by_file.get(pick["file"])
print(json.dumps(pick, ensure_ascii=False, indent=1))
