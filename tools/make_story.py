"""Make a 1080x1920 Instagram story image that promotes a grid post.

Usage: python3 -I tools/make_story.py posts/<post-folder>
Writes posts/<post-folder>/story.jpg using that folder's slide01.jpg.
Needs fonts: Inter, IBM Plex Sans Arabic (in ~/.fonts).
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

folder = Path(sys.argv[1]).resolve()
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
<div class="pill">NEW POST</div>
<div class="card"><img src="{cover.as_uri()}" alt=""></div>
<div class="en">Swipe through it on my page</div>
<div class="ar" lang="ar" dir="rtl">في بوست جديد في صفحتي، أدخل شوفو</div>
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
print(folder / "story.jpg")
