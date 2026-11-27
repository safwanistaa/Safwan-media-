"""Make ONE 1080x1920 Instagram story that recaps a day's grid posts.

Usage: python3 -I tools/make_recap_story.py <YYYY-MM-DD> posts/<folder1> [posts/<folder2> ...] [--variant N]
  <YYYY-MM-DD> = the day the posts went up (shown on the story).
  folders      = that day's grid-post folders (each with slide01.jpg), in posting order. 1-6 folders.
Writes posts/recaps/<YYYY-MM-DD>-story.jpg and prints the path.
The pill + EN + Sudanese-Arabic wording rotates by the number of recap stories already in
posts/STORIES.md (pass --variant N to force one).
Needs fonts: Inter, IBM Plex Sans Arabic (in ~/.fonts).
"""
import sys
import datetime as dt
from pathlib import Path
from playwright.sync_api import sync_playwright

VARIANTS = [  # (pill, English line, Sudanese Arabic line)
    ("YESTERDAY ON MY PAGE", "Missed one? They're all on my grid", "فاتك واحد؟ أمشي البروفايل وشوفهم كلهم"),
    ("IN CASE YOU MISSED IT", "Catch up on yesterday's posts", "بوستات أمبارح كلها في صفحتي"),
    ("DAILY RECAP", "Which one was your favourite?", "ياتو واحد عجبك أكتر؟"),
    ("CATCH UP", "Swipe through them on my page", "أدخل الصفحة وقلّب فيهم"),
    ("YESTERDAY'S DROPS", "Tell me which one is so you", "قول لي ياتو واحد دا إنت"),
]
LABELS = {"morning": "MORNING", "afternoon": "AFTERNOON", "evening": "EVENING",
          "night": "NIGHT", "lesson": "MARKETING CLASS", "manual": "BONUS"}

args = [a for a in sys.argv[1:]]
vi = None
if "--variant" in args:
    i = args.index("--variant"); vi = int(args[i + 1]); del args[i:i + 2]
day = dt.date.fromisoformat(args[0])
folders = [Path(f).resolve() for f in args[1:]]
assert 1 <= len(folders) <= 6, "give 1-6 post folders"
repo = Path(__file__).resolve().parent.parent
for f in folders:
    assert (f / "slide01.jpg").exists(), f"missing {f}/slide01.jpg"
if vi is None:
    log = repo / "posts" / "STORIES.md"
    vi = log.read_text(encoding="utf-8").count("| recap |") if log.exists() else 0
pill, en, ar = VARIANTS[vi % len(VARIANTS)]

n = len(folders)
cols = 1 if n == 1 else (2 if n <= 4 else 3)
w = {1: 720, 2: 450, 3: 400, 4: 400, 5: 300, 6: 300}[n]
h = int(w * 1350 / 1080)
date_label = day.strftime("%a %d %b").upper()
count_label = "1 NEW POST" if n == 1 else f"{n} NEW POSTS"

def label(f):
    parts = f.name.split("-")
    t = LABELS.get(parts[3] if len(parts) > 3 else "", "POST")
    return "LESSON" if (t == "MARKETING CLASS" and w < 400) else t

cards = "".join(
    f'<div class="card" style="width:{w}px;height:{h}px"><img src="{(f/"slide01.jpg").as_uri()}" alt="">'
    f'<div class="tag">{i+1:02d} · {label(f)}</div></div>'
    for i, f in enumerate(folders))
bg = (folders[0] / "slide01.jpg").as_uri()
grid_w = cols * w + (cols - 1) * 28

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#0E0E10}}
.bg{{position:absolute;inset:-60px;background:url('{bg}') center/cover;filter:blur(46px) brightness(0.38)}}
.wrap{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:38px;font-family:Inter,sans-serif;color:#fff}}
.pill{{font-weight:800;font-size:32px;letter-spacing:0.14em;padding:16px 34px;border-radius:999px;background:#fff;color:#111}}
.meta{{font-weight:700;font-size:28px;letter-spacing:0.18em;opacity:.8;margin-top:-14px}}
.grid{{width:{grid_w}px;display:flex;flex-wrap:wrap;justify-content:center;gap:28px}}
.card{{position:relative;border-radius:26px;overflow:hidden;box-shadow:0 24px 60px rgba(0,0,0,.55)}}
.card img{{width:100%;height:100%;object-fit:cover;display:block}}
.tag{{position:absolute;left:14px;top:14px;font-weight:800;font-size:{20 if w < 400 else 22}px;letter-spacing:0.08em;padding:8px 14px;border-radius:999px;background:rgba(14,14,16,.82);color:#fff}}
.en{{font-weight:700;font-size:44px;text-align:center;padding:0 60px}}
.ar{{font-family:'IBM Plex Sans Arabic',sans-serif;font-weight:700;font-size:42px;line-height:1.4;margin-top:-18px}}
.handle{{font-weight:600;font-size:30px;opacity:.85}}
</style></head><body><div class="bg"></div><div class="wrap">
<div class="pill">{pill}</div>
<div class="meta">{date_label} · {count_label}</div>
<div class="grid">{cards}</div>
<div class="en">{en}</div>
<div class="ar" lang="ar" dir="rtl">{ar}</div>
<div class="handle">@safwanistaa</div>
</div></body></html>"""

out_dir = repo / "posts" / "recaps"
out_dir.mkdir(parents=True, exist_ok=True)
out = out_dir / f"{day.isoformat()}-story.jpg"
tmp = out_dir / "_recap.html"
tmp.write_text(html, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(tmp.as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(500)
    pg.screenshot(path=str(out), type="jpeg", quality=92)
    b.close()
tmp.unlink()
print(out, f"(variant {vi % len(VARIANTS)}: {pill}; {n} posts)")
