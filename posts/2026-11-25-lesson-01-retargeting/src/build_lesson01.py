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
LESSON = "LESSON 01"; TOPIC = "RETARGETING"

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

# 2 what is it — loop diagram
steps = [("Sees your ad", "شاف إعلانك"), ("Visits / watches", "زار أو اتفرج"), ("Leaves", "مشى"), ("Sees a reminder ad", "شاف إعلان تذكير"), ("Comes back &amp; buys", "رجع واشترى")]
flow = ""
for k, (e, a) in enumerate(steps):
    hi = k >= 3
    bg = MAROON if hi else PAPER; fg = CREAM if hi else INK
    flow += f'<div style="display:flex;align-items:center;gap:24px;background:{bg};color:{fg};border:2px solid {MAROON if hi else RULE};border-radius:20px;padding:20px 28px"><span style="{SERIF}font-weight:800;font-size:36px;width:40px">{k+1}</span><span style="flex:1;font-size:34px;font-weight:700">{e}</span><span lang="ar" dir="rtl" style="{AR}font-size:30px;font-weight:600;opacity:0.85">{a}</span></div>'
    if k < 4:
        flow += f'<div style="height:14px;margin-left:46px;border-left:3px dashed {GOLD}"></div>'
s2 = f'''
{h("Retargeting = showing ads to people who already know you.", 64)}
<div style="display:flex;flex-direction:column">{flow}</div>
<div style="font-size:30px;color:{MUTED};line-height:1.4">Steps 4–5 are retargeting. These people already showed interest, so they're cheaper to convert than strangers.</div>
'''
page(2, "WHAT IT IS", s2)

# 3 REAL-LIFE EXAMPLE (series rule: every concept gets a relatable real-life example)
phone = f"""<div style="width:400px;flex:none;background:#fff;border:3px solid {INK};border-radius:44px;padding:22px 18px 26px;box-sizing:border-box;box-shadow:12px 12px 0 {RULE}">
<div style="display:flex;align-items:center;gap:12px;padding:4px 6px 14px"><span style="width:46px;height:46px;border-radius:50%;background:{GOLD}"></span><div style="display:flex;flex-direction:column"><span style="font-size:22px;font-weight:800">sneaker.store</span><span style="font-size:18px;color:{MUTED}">Sponsored</span></div></div>
<div style="height:250px;border-radius:18px;background:#EFE6D6;display:flex;align-items:center;justify-content:center"><svg width="230" height="120" viewBox="0 0 230 120" fill="none"><path d="M14 92c0-22 8-40 22-52 10 14 30 22 52 22 26 0 46-8 60-4 22 6 44 18 64 30 8 5 6 18-4 18H24c-6 0-10-6-10-14z" fill="{MAROON}"/><path d="M14 98h204v8c0 6-4 10-10 10H24c-6 0-10-4-10-10z" fill="{INK}"/><path d="M60 64l14 10M80 60l14 12M100 58l14 12" stroke="{CREAM}" stroke-width="5" stroke-linecap="round"/></svg></div>
<div style="padding:16px 6px 0;font-size:24px;font-weight:700;line-height:1.3">Still thinking about these? Free delivery today only.</div>
<div style="margin:16px 6px 0;background:{MAROON};color:{CREAM};text-align:center;border-radius:12px;padding:14px;font-size:22px;font-weight:800">Complete your order</div>
</div>"""
def step(day, en, a):
    return f'<div style="display:flex;flex-direction:column;gap:4px"><span style="font-weight:800;font-size:22px;letter-spacing:0.16em;color:{GOLD}">{day}</span><span style="font-size:31px;font-weight:600;line-height:1.3">{en}</span>{ar(a, 27, 600, MUTED)}</div>'
s3x = f"""
{h("You've already been retargeted. <i style='color:" + MAROON + "'>Many times.</i>", 64)}
<div style="display:flex;gap:40px;align-items:center">
{phone}
<div style="flex:1;display:flex;flex-direction:column;gap:26px">
{step("MONDAY, 1 AM", "You check out sneakers on a store's website, add them to cart… then close the tab.", "شفت جزمة في موقع، ضفتها للسلة وقفلت")}
{step("TUESDAY", "You open Instagram and there they are. Same sneakers. “Still thinking about these?”", "فتحت إنستقرام… لقيتها قدامك تاني")}
</div>
</div>
<div style="background:{MAROON};color:{CREAM};border-radius:22px;padding:26px 32px;font-size:30px;font-weight:600;line-height:1.4"><b>The business side:</b> an online perfume shop gets 1,000 visitors this week and only 20 buy. Retargeting reminds the other 980, who already know the shop.</div>
"""
page(3, "REAL-LIFE EXAMPLE", s3x)

# 3 audiences
def aud(n, title, sub, a):
    return f'''<div style="display:flex;gap:26px;align-items:flex-start;background:{PAPER};border:2px solid {RULE};border-radius:22px;padding:26px 30px">{num(n)}
<div style="flex:1;display:flex;flex-direction:column;gap:4px"><span style="font-size:36px;font-weight:800">{title}</span><span style="font-size:27px;color:{MUTED};line-height:1.35">{sub}</span>{ar(a, 28, 600, MAROON)}</div></div>'''
s3 = f'''
{h("Build these 4 audiences in Ads Manager", 66)}
<div style="display:flex;flex-direction:column;gap:16px">
{aud(1, "Website visitors", "Needs the Meta Pixel (+ Conversions API) on your site", "الناس الزارت موقعك")}
{aud(2, "Video viewers", "People who watched 50%+ of your videos or Reels", "الاتفرجوا على نص الفيديو أو أكتر")}
{aud(3, "Instagram &amp; Facebook engagers", "Liked, saved, commented, DM'd or visited your profile", "الاتفاعلوا مع حسابك")}
{aud(4, "Added to cart, didn't buy", "Your hottest audience. Don't ignore them", "ضافوا للسلة وما اشتروا")}
</div>
'''
page(4, "STEP 1 · AUDIENCES", s3)

# 4 recency
def heat(label, days, msg, a, w, col):
    return f'''<div style="display:flex;flex-direction:column;gap:10px">
<div style="display:flex;justify-content:space-between;align-items:baseline"><span style="{SERIF}font-weight:800;font-size:46px;color:{col}">{label}</span><span style="font-size:30px;font-weight:700;color:{MUTED}">{days}</span></div>
<div style="height:22px;background:{RULE};border-radius:11px;overflow:hidden"><div style="width:{w}%;height:100%;background:{col};border-radius:11px"></div></div>
<div style="display:flex;justify-content:space-between;gap:20px;align-items:baseline"><span style="font-size:32px;font-weight:600">{msg}</span><span lang="ar" dir="rtl" style="{AR}font-size:28px;font-weight:600;color:{MUTED}">{a}</span></div></div>'''
s4 = f'''
{h("Split them by how <i style='color:" + MAROON + "'>recent</i> they are", 70)}
<div style="display:flex;flex-direction:column;gap:40px">
{heat("Hot", "last 1–7 days", "Direct offer: “finish your order”", "عرض مباشر", 100, MAROON)}
{heat("Warm", "8–30 days", "Proof: reviews, results, testimonials", "إثبات وتجارب عملاء", 65, GOLD)}
{heat("Cool", "31–90 days", "Reminder: why you, what's new", "تذكير بقيمتك", 35, "#A89B88")}
</div>
{ar("ما تعرض نفس الإعلان لزول زارك أمس وزول زارك قبل شهرين.", 36, 700, MAROON)}
'''
page(5, "STEP 2 · RECENCY", s4)

# 5 message map
rows = [("Watched your video", "Show the next video or a case study"), ("Viewed a product", "Show that exact product + a review"), ("Added to cart", "Reminder + a real reason to finish (free delivery, bonus)"), ("Already bought", "Exclude them, or upsell later")]
tbl = ""
for k, (a_, b_) in enumerate(rows):
    tbl += f'<div style="display:grid;grid-template-columns:330px 1fr;border-top:2px solid {RULE}"><div style="padding:26px 24px 26px 0;font-size:32px;font-weight:800;color:{MAROON}">{a_}</div><div style="padding:26px 0;font-size:32px;font-weight:500;line-height:1.35">{b_}</div></div>'
s5 = f'''
{h("Match the ad to what they did", 74)}
<div style="display:grid;grid-template-columns:330px 1fr;font-size:24px;font-weight:800;letter-spacing:0.16em;color:{GOLD}"><span>THEY…</span><span>YOU SHOW…</span></div>
<div style="display:flex;flex-direction:column;border-bottom:2px solid {RULE}">{tbl}</div>
{ar("الإعلان لازم يكمل القصة من المكان الوقف فيهو العميل.", 36, 700, MAROON)}
'''
page(6, "STEP 3 · MESSAGE", s5)

# 6 mistakes
def mis(t, fix):
    x = f'<svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="{MAROON}" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
    return f'<div style="display:flex;gap:22px;align-items:flex-start;padding:22px 0;border-bottom:2px solid {RULE}">{x}<div style="flex:1;display:flex;flex-direction:column;gap:6px"><span style="font-size:36px;font-weight:800;line-height:1.2">{t}</span><span style="font-size:29px;color:{MUTED};line-height:1.35"><b style="color:{GOLD}">Fix:</b> {fix}</span></div></div>'
s6 = f'''
{h("4 mistakes that waste your budget", 74)}
<div style="display:flex;flex-direction:column">
{mis("Showing ads to people who already bought", "exclude recent purchasers")}
{mis("Same ad running for weeks", "watch frequency, refresh the creative")}
{mis("Audience too small to deliver", "widen the time window or combine sources")}
{mis("Creepy copy: “we saw you looking…”", "remind, don't stalk")}
</div>
{ar("أكبر غلطة: تصرف قروش على زول اشترى خلاص.", 36, 700, MAROON)}
'''
page(7, "AVOID THIS", s6)

# 7 checklist
def ck(t):
    b = f'<span style="width:46px;height:46px;border:3px solid {MAROON};border-radius:10px;flex:none;box-sizing:border-box;display:flex;align-items:center;justify-content:center"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{MAROON}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"/></svg></span>'
    return f'<div style="display:flex;gap:24px;align-items:center;font-size:36px;font-weight:600;line-height:1.3">{b}<span>{t}</span></div>'
s7 = f'''
{h("Your setup checklist", 80)}
<div style="background:{PAPER};border:2px solid {RULE};border-radius:26px;padding:44px 44px;display:flex;flex-direction:column;gap:30px">
{ck("Install Pixel + Conversions API")}
{ck("Create the 4 custom audiences")}
{ck("Split by Hot / Warm / Cool")}
{ck("One message per stage")}
{ck("Exclude buyers")}
{ck("Check frequency every week")}
</div>
{ar("اعمل سكرينشوت وابدأ الليلة.", 40, 700, MAROON)}
'''
page(8, "SCREENSHOT THIS", s7)

# 8 CTA
s8 = f'''
{h('Learned something?<br><span style="font-style:italic;font-weight:700;color:' + MAROON + '">Pass it on.</span>', 104)}
<div style="display:flex;flex-direction:column;gap:22px;font-size:40px;font-weight:600">
<span>1. <b>Save</b> it for your next campaign</span>
<span>2. <b>Send</b> it to someone running ads</span>
<span>3. <b>Follow</b> for Lesson 02 tomorrow</span>
</div>
<div style="background:{MAROON};color:{CREAM};border-radius:24px;padding:34px 40px;display:flex;flex-direction:column;gap:8px">
<span style="font-size:36px;font-weight:700">What should Lesson 02 be? Tell me in the comments.</span>
<span lang="ar" dir="rtl" style="{AR}font-size:34px;font-weight:600;text-align:right">الدرس الجاي يكون عن شنو؟ كلمني في الكومنتات</span>
</div>
'''
page(9, "NEW LESSON EVERY DAY", s8, last=True)
print("ok")

# ---- UNIFIED SERIES COVER (same layout every lesson; only the fields below change)
COVER = dict(num="01", topic="Retargeting", tag="META ADS", hook="They visited. They left. Here's how to bring them back.",
             ar_topic="الريتارجتنق", ar_hook="زارك ومشى؟ كدة بترجعو.")
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
