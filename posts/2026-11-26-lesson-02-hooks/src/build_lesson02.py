"""Marketing Class lesson builder (Lesson 01 = reference example).
Usage: python3 -I build_lessonNN.py <slides_dir>   then copy assets/photos/02-arms-crossed.jpg to <slides_dir>/photo.jpg and render with tools/render_dc.py.
To make a new lesson: copy this file, change LESSON/TOPIC/N and the COVER dict, rewrite the inner slides (2..N-1).
Do NOT change page(), cover(), the palette, fonts or the last-slide CTA structure: the series look must stay identical.
"""
import sys
from pathlib import Path
OUT = Path(sys.argv[1]); OUT.mkdir(parents=True, exist_ok=True)
N = 9
CREAM = "#F6F1E7"; PAPER = "#FBF8F2"; MAROON = "#6B1E2E"; GOLD = "#8C6420"; INK = "#1E1A17"; MUTED = "#6A6158"; RULE = "#DDD2C0"
AR = "font-family:'IBM Plex Sans Arabic',sans-serif;"
SERIF = "font-family:'Playfair Display',serif;font-variant-numeric:lining-nums;"
LESSON = "LESSON 02"; TOPIC = "HOOKS"

def ar(t, size=36, w=600, c=INK, extra=""):
    return f'<div lang="ar" dir="rtl" style="{AR}font-weight:{w};font-size:{size}px;line-height:1.55;text-align:right;color:{c};{extra}">{t}</div>'

ARROW = f'<svg aria-hidden="true" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{MAROON}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>'
BOOKMARK = f'<svg aria-hidden="true" width="26" height="26" viewBox="0 0 24 24" fill="none" stroke="{GOLD}" stroke-width="2.2" stroke-linejoin="round"><path d="M6 3h12v18l-6-4-6 4z"/></svg>'

def page(i, kicker, body, last=False):
    right = (f'<span style="display:flex;align-items:center;gap:12px;font-size:24px;font-weight:700;color:{MAROON};letter-spacing:0.04em">Swipe {ARROW}</span>'
             if not last else f'<span style="display:flex;align-items:center;gap:10px;font-size:24px;font-weight:700;color:{GOLD}">{BOOKMARK} Save for later</span>')
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Marketing class {LESSON} slide {i}</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<style>
body{{margin:0}}
</style>
</helmet>
<div style="width:1080px;height:1350px;box-sizing:border-box;padding:0;background:{CREAM};display:flex;flex-direction:column;font-family:Inter,sans-serif;color:{INK}">
<div style="height:14px;background:{MAROON}"></div>
<div style="flex:1;display:flex;flex-direction:column;padding:56px 80px 56px">
<div style="display:flex;justify-content:space-between;align-items:center">
<span style="display:flex;align-items:center;gap:16px"><span style="background:{MAROON};color:{CREAM};font-weight:800;font-size:22px;letter-spacing:0.14em;padding:10px 18px;border-radius:8px">MARKETING CLASS</span><span style="font-weight:700;font-size:22px;letter-spacing:0.14em;color:{GOLD}">{LESSON} · {TOPIC}</span></span>
<span style="font-weight:700;font-size:24px;color:{MUTED};letter-spacing:0.08em">{i:02d} / {N:02d}</span>
</div>
<div style="margin-top:44px;font-weight:800;font-size:24px;letter-spacing:0.2em;color:{GOLD}">{kicker}</div>
<div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:30px;min-height:0">
{body}
</div>
<div style="display:flex;justify-content:space-between;align-items:center;padding-top:24px;border-top:2px solid {RULE}">
<span style="font-size:24px;font-weight:600;color:{MUTED}">@safwanistaa · Save &amp; share with a marketer</span>
{right}
</div>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
    (OUT / f"Slide{i:02d}.dc.html").write_text(html, encoding="utf-8")

def h(t, size=84):
    return f'<div style="{SERIF}font-weight:800;font-size:{size}px;line-height:1.05;letter-spacing:-0.01em">{t}</div>'

def num(n):
    return f'<span style="width:64px;height:64px;border-radius:50%;background:{MAROON};color:{CREAM};{SERIF}font-weight:800;font-size:34px;display:flex;align-items:center;justify-content:center;flex:none">{n}</span>'

# 2 what is it — the 3 layers of a hook
def layer(n, en, sub, a):
    return f'''<div style="display:flex;gap:26px;align-items:center;background:{PAPER};border:2px solid {RULE};border-radius:22px;padding:24px 30px">{num(n)}
<div style="flex:1;display:flex;flex-direction:column;gap:4px"><span style="font-size:36px;font-weight:800">{en}</span><span style="font-size:27px;color:{MUTED};line-height:1.35">{sub}</span></div><span lang="ar" dir="rtl" style="{AR}font-size:30px;font-weight:600;color:{MAROON}">{a}</span></div>'''
s2 = f'''
{h("A hook = the first 1–3 seconds that make someone <i style='color:" + MAROON + "'>stop scrolling.</i>", 62)}
<div style="font-size:31px;line-height:1.4;color:{INK}">It's made of three things people get at the same moment:</div>
<div style="display:flex;flex-direction:column;gap:16px">
{layer(1, "What they see", "The first frame: a face, movement, something unexpected", "البشوفو")}
{layer(2, "What they hear", "Your first sentence", "البسمعو")}
{layer(3, "What they read", "The short text on screen", "البقروهو")}
</div>
<div style="font-size:30px;color:{MUTED};line-height:1.4">If they don't stop, the rest of your video doesn't matter. Nobody sees it.</div>
{ar("لو الزول ما وقف في أول تلاتة ثواني، باقي الفيديو ما بفرق.", 34, 700, MAROON)}
'''
page(2, "WHAT IT IS", s2)

# 3 REAL-LIFE EXAMPLE
phone = f"""<div style="width:380px;height:560px;flex:none;background:{INK};border:3px solid {INK};border-radius:44px;padding:14px;box-sizing:border-box;box-shadow:12px 12px 0 {RULE}">
<div style="position:relative;width:100%;height:100%;border-radius:32px;overflow:hidden;background:linear-gradient(170deg,#7A3A46 0%,#3A1820 100%)">
<svg style="position:absolute;left:110px;top:250px" width="130" height="190" viewBox="0 0 130 190" fill="none"><rect x="45" y="0" width="40" height="34" rx="6" fill="#D9B26A"/><rect x="10" y="34" width="110" height="150" rx="26" fill="#EFE4D2" opacity="0.92"/><rect x="30" y="80" width="70" height="44" rx="8" fill="{MAROON}"/></svg>
<div style="position:absolute;left:22px;right:22px;top:70px;background:#fff;color:{INK};border-radius:12px;padding:14px 16px;font-size:27px;font-weight:800;line-height:1.25;text-align:center">Stop spraying perfume on your wrists.</div>
<div style="position:absolute;right:16px;bottom:120px;display:flex;flex-direction:column;gap:22px;align-items:center"><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2"><path d="M12 21s-7-4.4-9.3-9C1 8.6 3 5 6.5 5c2 0 3.6 1.2 4.3 2.6h2.4C13.9 6.2 15.5 5 17.5 5 21 5 23 8.6 21.3 12 19 16.6 12 21 12 21z"/></svg><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round"><path d="M22 3L2 11l8 3 3 8z"/></svg><svg width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2.2" stroke-linejoin="round"><path d="M6 3h12v18l-6-4-6 4z"/></svg></div>
<div style="position:absolute;left:22px;bottom:30px;display:flex;align-items:center;gap:10px;color:#fff;font-size:20px;font-weight:700"><span style="width:34px;height:34px;border-radius:50%;background:#D9B26A"></span>perfume.corner</div>
</div></div>"""
def step(day, en, a):
    return f'<div style="display:flex;flex-direction:column;gap:4px"><span style="font-weight:800;font-size:22px;letter-spacing:0.16em;color:{GOLD}">{day}</span><span style="font-size:30px;font-weight:600;line-height:1.3">{en}</span>{ar(a, 27, 600, MUTED)}</div>'
s3 = f"""
{h("You've stopped for a hook. <i style='color:" + MAROON + "'>Today, probably.</i>", 62)}
<div style="display:flex;gap:40px;align-items:center">
{phone}
<div style="flex:1;display:flex;flex-direction:column;gap:24px">
{step("11 PM, SCROLLING", "You're flicking past videos without thinking. Next. Next. Next.", "قاعد تسكرول ساي، فيديو ورا فيديو")}
{step("THEN THIS", "One video opens with: “Stop spraying perfume on your wrists.” You stop. You watch to the end. You send it to a friend.", "وقفت، اتفرجت لي آخرو، ورسلتو لصاحبك")}
</div>
</div>
<div style="background:{MAROON};color:{CREAM};border-radius:22px;padding:24px 32px;font-size:29px;font-weight:600;line-height:1.4"><b>The business side:</b> a perfume shop posts the same video twice. Version A opens with “Hi guys, welcome to our shop”: 400 views. Version B opens with “Your perfume is gone by noon. Here's why”: 4,000 views. Same product, new first line. <span style="opacity:0.75">(example numbers)</span></div>
"""
page(3, "REAL-LIFE EXAMPLE", s3)

# 4 five hook types, each with an everyday example
def ht(n, title, ex, a):
    return f'''<div style="display:flex;gap:24px;align-items:flex-start;background:{PAPER};border:2px solid {RULE};border-radius:20px;padding:20px 28px">{num(n)}
<div style="flex:1;display:flex;flex-direction:column;gap:2px"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:16px"><span style="font-size:33px;font-weight:800">{title}</span><span lang="ar" dir="rtl" style="{AR}font-size:27px;font-weight:600;color:{MAROON}">{a}</span></div><span style="font-size:28px;color:{MUTED};line-height:1.35;font-style:italic">{ex}</span></div></div>'''
s4 = f'''
{h("5 hooks that work for any business", 66)}
<div style="display:flex;flex-direction:column;gap:14px">
{ht(1, "The mistake", "“Stop washing your abaya in hot water.”", "قول الغلطة")}
{ht(2, "The question", "“Why does café coffee taste better than yours?”", "اسأل سؤال")}
{ht(3, "The result first", "“This salon went from 5 to 30 bookings a week.”", "ابدأ بالنتيجة")}
{ht(4, "The number", "“3 dishes first-timers always order here.”", "رقم أو قائمة")}
{ht(5, "The relatable moment", "“When you said ‘just one shawarma’…”", "موقف عاشوهو كلهم")}
</div>
'''
page(4, "STEP 1 · PICK A TYPE", s4)

# 5 stack the 3 layers
rows = [("Say it", "Start with the payoff. No “hi guys”, no long intro.", "قول"), ("Show it", "Something moves or surprises in the very first frame.", "ورّي"), ("Write it", "5–7 big words on screen. Many people watch on mute.", "اكتب")]
tbl = ""
for a_, b_, c_ in rows:
    tbl += f'<div style="display:grid;grid-template-columns:240px 1fr;border-top:2px solid {RULE}"><div style="padding:28px 20px 28px 0;display:flex;flex-direction:column;gap:2px"><span style="font-size:36px;font-weight:800;color:{MAROON}">{a_}</span><span lang="ar" dir="rtl" style="{AR}font-size:28px;font-weight:600;color:{MUTED};text-align:left">{c_}</span></div><div style="padding:28px 0;font-size:32px;font-weight:500;line-height:1.35">{b_}</div></div>'
s5 = f'''
{h("Stack all 3 layers in second one", 72)}
<div style="display:grid;grid-template-columns:240px 1fr;font-size:24px;font-weight:800;letter-spacing:0.16em;color:{GOLD}"><span>LAYER</span><span>DO THIS</span></div>
<div style="display:flex;flex-direction:column;border-bottom:2px solid {RULE}">{tbl}</div>
<div style="background:{PAPER};border:2px solid {RULE};border-radius:20px;padding:24px 30px;font-size:30px;line-height:1.4"><b style="color:{GOLD}">Example:</b> you <b>say</b> “Your perfume is gone by noon,” you <b>show</b> a spray in slow motion, you <b>write</b> “Perfume fading fast?”</div>
{ar("قول، ورّي، واكتب… التلاتة مع بعض في أول ثانية.", 34, 700, MAROON)}
'''
page(5, "STEP 2 · STACK IT", s5)

# 6 before / after rewrites
rows = [("“Welcome back to my page! Today…”", "“You're losing customers in 3 seconds.”"), ("“New collection now available!”", "“The abaya colour everyone asked for is back.”"), ("“We have the best coffee in town.”", "“Why home coffee never tastes like this.”"), ("“Some tips about our menu.”", "“Don't order this dish on your first visit.”")]
tbl = ""
for a_, b_ in rows:
    tbl += f'<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;border-top:2px solid {RULE};padding:24px 0"><div style="font-size:29px;font-weight:500;line-height:1.35;color:{MUTED};text-decoration:line-through;text-decoration-color:{MAROON}">{a_}</div><div style="font-size:30px;font-weight:800;line-height:1.3;color:{INK}">{b_}</div></div>'
s6 = f'''
{h("Same video. <i style='color:" + MAROON + "'>Better first line.</i>", 72)}
<div style="display:grid;grid-template-columns:1fr 1fr;gap:28px;font-size:24px;font-weight:800;letter-spacing:0.16em;color:{GOLD}"><span>BORING</span><span>HOOK</span></div>
<div style="display:flex;flex-direction:column;border-bottom:2px solid {RULE}">{tbl}</div>
{ar("ما تبدأ بالسلام والتعريف. ابدأ بالحاجة البتهمّو.", 34, 700, MAROON)}
'''
page(6, "STEP 3 · REWRITE", s6)

# 7 mistakes
def mis(t, fix):
    x = f'<svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="{MAROON}" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
    return f'<div style="display:flex;gap:22px;align-items:flex-start;padding:22px 0;border-bottom:2px solid {RULE}">{x}<div style="flex:1;display:flex;flex-direction:column;gap:6px"><span style="font-size:36px;font-weight:800;line-height:1.2">{t}</span><span style="font-size:29px;color:{MUTED};line-height:1.35"><b style="color:{GOLD}">Fix:</b> {fix}</span></div></div>'
s7 = f'''
{h("4 mistakes that kill your views", 74)}
<div style="display:flex;flex-direction:column">
{mis("Opening with your logo or a long intro", "start with the payoff, brand it later")}
{mis("Clickbait the video doesn't deliver", "the hook is a promise, keep it")}
{mis("A wall of text on screen", "one short line, big and readable")}
{mis("The good part shows up at second 10", "move it to second 1")}
</div>
{ar("الهوك وعد. لو ما وفّيت بيهو، الناس ما بترجعوا ليك تاني.", 34, 700, MAROON)}
'''
page(7, "AVOID THIS", s7)

# 8 checklist
def ck(t):
    b = f'<span style="width:46px;height:46px;border:3px solid {MAROON};border-radius:10px;flex:none;box-sizing:border-box;display:flex;align-items:center;justify-content:center"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{MAROON}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"/></svg></span>'
    return f'<div style="display:flex;gap:24px;align-items:center;font-size:36px;font-weight:600;line-height:1.3">{b}<span>{t}</span></div>'
s8 = f'''
{h("Before you post, check:", 80)}
<div style="background:{PAPER};border:2px solid {RULE};border-radius:26px;padding:44px 44px;display:flex;flex-direction:column;gap:30px">
{ck("First sentence = the payoff")}
{ck("Something moves in frame 1")}
{ck("5–7 words of text on screen")}
{ck("The video delivers the promise")}
{ck("Wrote 3 hooks, picked the best")}
{ck("Checked where viewers drop off")}
</div>
{ar("اكتب تلاتة هوكات هسي واختار أقواهم.", 40, 700, MAROON)}
'''
page(8, "SCREENSHOT THIS", s8)

# 9 CTA
s9 = f'''
{h('Learned something?<br><span style="font-style:italic;font-weight:700;color:' + MAROON + '">Pass it on.</span>', 104)}
<div style="display:flex;flex-direction:column;gap:22px;font-size:40px;font-weight:600">
<span>1. <b>Save</b> it for your next Reel</span>
<span>2. <b>Send</b> it to someone who posts content</span>
<span>3. <b>Follow</b> for Lesson 03 tomorrow</span>
</div>
<div style="background:{MAROON};color:{CREAM};border-radius:24px;padding:34px 40px;display:flex;flex-direction:column;gap:8px">
<span style="font-size:36px;font-weight:700">What should Lesson 03 be? Tell me in the comments.</span>
<span lang="ar" dir="rtl" style="{AR}font-size:34px;font-weight:600;text-align:right">الدرس الجاي يكون عن شنو؟ كلمني في الكومنتات</span>
</div>
'''
page(9, "NEW LESSON EVERY DAY", s9, last=True)
print("ok")

# ---- UNIFIED SERIES COVER (same layout every lesson; only the fields below change)
COVER = dict(num="02", topic="Scroll-Stopping Hooks", tag="REELS · TIKTOK", hook="You get 3 seconds. Here's how to use them.",
             ar_topic="الهوك: أول 3 ثواني", ar_hook="عندك 3 ثواني بس. استغلها صاح.")
def cover(c):
    lw = max(len(w) for w in c["topic"].split())
    fs = max(64, min(100, int(980 / lw)))
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Marketing class lesson {c["num"]} cover</title>
<script src="./support.js"></script>
</head>
<body>
<x-dc>
<helmet>
<style>
body{{margin:0}}
</style>
</helmet>
<div style="width:1080px;height:1350px;box-sizing:border-box;background:{MAROON};position:relative;overflow:hidden;font-family:Inter,sans-serif;color:{CREAM}">
<div style="position:absolute;right:-60px;bottom:0;width:560px;height:760px;border-radius:280px 280px 0 0;overflow:hidden;background:#2A0E14;border:6px solid {GOLD};border-bottom:none"><img src="photo.jpg" style="width:100%;height:100%;object-fit:cover;object-position:50% 15%"></div>
<div style="position:absolute;left:0;right:0;top:0;padding:60px 80px 0;display:flex;justify-content:space-between;align-items:center">
<span style="background:{CREAM};color:{MAROON};font-weight:800;font-size:30px;letter-spacing:0.16em;padding:14px 24px;border-radius:10px">MARKETING CLASS</span>
<span style="font-weight:700;font-size:24px;color:#E7D9C2;letter-spacing:0.08em">01 / {N:02d}</span>
</div>
<div style="position:absolute;left:80px;top:180px;width:560px;display:flex;flex-direction:column;gap:6px">
<span style="font-weight:800;font-size:28px;letter-spacing:0.24em;color:#D9B26A">LESSON</span>
<span style="{SERIF}font-weight:800;font-size:300px;line-height:0.85;color:#D9B26A;letter-spacing:-0.02em">{c["num"]}</span>
</div>
<div style="position:absolute;left:80px;top:560px;width:500px;display:flex;flex-direction:column;gap:22px">
<span style="align-self:flex-start;border:2px solid #D9B26A;color:#D9B26A;font-weight:800;font-size:24px;letter-spacing:0.18em;padding:8px 16px;border-radius:8px">{c["tag"]}</span>
<span style="{SERIF}font-weight:800;font-style:italic;font-size:{fs}px;line-height:1.02;width:500px">{c["topic"]}</span>
<span lang="ar" dir="rtl" style="{AR}font-weight:700;font-size:56px;line-height:1.3;text-align:right;width:500px">{c["ar_topic"]}</span>
<span style="font-size:36px;font-weight:600;line-height:1.35;color:#EFE4D2;width:500px">{c["hook"]}</span>
<span lang="ar" dir="rtl" style="{AR}font-weight:600;font-size:34px;line-height:1.5;color:#EFE4D2;text-align:right;width:500px">{c["ar_hook"]}</span>
</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:110px;background:{CREAM};color:{MAROON};display:flex;justify-content:space-between;align-items:center;padding:0 80px;box-sizing:border-box">
<span style="font-size:26px;font-weight:700">@safwanistaa · a new lesson every day</span>
<span style="display:flex;align-items:center;gap:12px;font-size:26px;font-weight:800">Swipe {ARROW}</span>
</div>
</div>
</x-dc>
<script type="text/x-dc" data-dc-script data-props='{{"$preview":{{"width":1080,"height":1350}}}}'>
class Component extends DCLogic {{
renderVals() {{
return {{}};
}}
}}
</script>
</body>
</html>
'''
    (OUT / "Slide01.dc.html").write_text(html, encoding="utf-8")
cover(COVER)
