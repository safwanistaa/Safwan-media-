"""Make a 1080x1920 Instagram story image that promotes a grid post.

Usage: python3 -I tools/make_story.py posts/<post-folder> [variant-number]
Writes posts/<post-folder>/story.jpg using that folder's slide01.jpg.
The pill + EN + Sudanese-Arabic wording rotates through VARIANTS so stories
don't repeat: by default it picks the next one after the stories already
logged in posts/STORIES.md (pass a number to force one).
Needs fonts: Inter, IBM Plex Sans Arabic (in ~/.fonts).
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

VARIANTS = [  # (pill, English line, Sudanese Arabic line)
    ("NEW POST", "Swipe through it on my page", "في بوست جديد في صفحتي، أدخل شوفو"),
    ("JUST DROPPED", "Fresh on the grid. Go see", "البوست الجديد نزل، ما تفوّتو"),
    ("DID YOU SEE THIS?", "Or did you miss this one?", "شفت البوست دا ولا لسه؟"),
    ("NEW ON THE GRID", "Tap my profile, it's up", "أمشي البروفايل، البوست هناك"),
    ("SWIPE TILL THE END", "The last slide is the best one", "قلّب لحدي آخر سلايد، أحلى حاجة في الآخر"),
    ("YOUR TAKE?", "Drop your answer in the comments", "أكتب لي رأيك في الكومنتات"),
    ("SEND THIS", "Share it with someone who needs it", "رسّلو لزول محتاجو"),
    ("UP NOW", "Go check the post, then come back", "أدخل شوف البوست وتعال"),
    ("THIS ONE'S FOR YOU", "You'll relate to this one", "البوست دا حيشبهك"),
    ("FRESH POST", "Tell me if this is you", "قول لي لو دا إنت"),
]

folder = Path(sys.argv[1]).resolve()
if len(sys.argv) > 2:
    vi = int(sys.argv[2])
else:
    log = folder.parent / "STORIES.md"
    done = log.read_text(encoding="utf-8").count("| story ") if log.exists() else 0
    vi = done
pill, en, ar = VARIANTS[vi % len(VARIANTS)]
cover = folder / "slide01.jpg"
assert cover.exists(), f"missing {cover}"

html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
html,body{{margin:0;width:1080px;height:1920px;overflow:hidden;background:#0E0E10}}
.bg{{position:absolute;inset:-60px;background:url('{cover.as_uri()}') center/cover;filter:blur(40px) brightness(0.45)}}
.wrap{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:44px;font-family:Inter,sans-serif;color:#fff}}
.pill{{font-weight:800;font-size:34px;letter-spacing:0.14em;padding:16px 34px;border-radius:999px;background:#fff;color:#111}}
.card{{width:860px;height:1075px;border-radius:36px;overflow:hidden;box-shadow:0 30px 80px rgba(0,0,0,.55)}}
.card img{{width:100%;height:100%;object-fit:cover;display:block}}
.en{{font-weight:700;font-size:46px}}
.ar{{font-family:'IBM Plex Sans Arabic',sans-serif;font-weight:700;font-size:44px;line-height:1.4}}
.handle{{font-weight:600;font-size:30px;opacity:.85}}
</style></head><body><div class="bg"></div><div class="wrap">
<div class="pill">{pill}</div>
<div class="card"><img src="{cover.as_uri()}" alt=""></div>
<div class="en">{en}</div>
<div class="ar" lang="ar" dir="rtl">{ar}</div>
<div class="handle">@safwanistaa</div>
</div></body></html>"""

tmp = folder / "_story.html"
tmp.write_text(html, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto(tmp.as_uri())
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(400)
    pg.screenshot(path=str(folder / "story.jpg"), type="jpeg", quality=92)
    b.close()
tmp.unlink()
print(folder / "story.jpg", f"(variant {vi % len(VARIANTS)}: {pill})")
