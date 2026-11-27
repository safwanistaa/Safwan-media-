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
LESSON = "LESSON 03"; TOPIC = "OFFERS"

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


# 2 what is it — the 4 parts of an offer
def part(n, en, sub, a):
    return f'''<div style="display:flex;gap:26px;align-items:center;background:{PAPER};border:2px solid {RULE};border-radius:22px;padding:22px 30px">{num(n)}
<div style="flex:1;display:flex;flex-direction:column;gap:4px"><span style="font-size:35px;font-weight:800">{en}</span><span style="font-size:27px;color:{MUTED};line-height:1.35">{sub}</span></div><span lang="ar" dir="rtl" style="{AR}font-size:30px;font-weight:600;color:{MAROON}">{a}</span></div>'''
s2 = f'''
{h("An offer is not your product. <i style='color:" + MAROON + "'>It's the whole deal.</i>", 64)}
<div style="font-size:31px;line-height:1.4;color:{INK}">A good offer answers 4 questions in the customer's head:</div>
<div style="display:flex;flex-direction:column;gap:14px">
{part(1, "What do I get?", "The result, not just the item", "بستفيد شنو؟")}
{part(2, "What's extra?", "A bonus that makes it feel generous", "في زيادة؟")}
{part(3, "What if I don't like it?", "A promise that removes the risk", "لو ما عجبني؟")}
{part(4, "Why now?", "A real reason not to wait", "ليه هسي؟")}
</div>
{ar("العرض ما هو المنتج بس. هو الصفقة كلها.", 34, 700, MAROON)}
'''
page(2, "WHAT IT IS", s2)

# 3 REAL-LIFE EXAMPLE — café menu board
def mrow(item, price, dim=False):
    c = "#B9AFA2" if dim else "#EFE4D2"
    return f'<div style="display:flex;justify-content:space-between;font-size:25px;font-weight:600;color:{c};padding:8px 0;border-bottom:1px dashed #4A423B"><span>{item}</span><span>{price}</span></div>'
board = f"""<div style="width:400px;flex:none;background:#2B2622;border:10px solid #8A6A45;border-radius:18px;padding:26px 26px 30px;box-sizing:border-box;box-shadow:12px 12px 0 {RULE};display:flex;flex-direction:column;gap:6px">
<div style="text-align:center;font-size:22px;font-weight:800;letter-spacing:0.2em;color:#D9B26A;margin-bottom:8px">MENU</div>
{mrow("Coffee", "15")}
{mrow("Croissant", "10")}
{mrow("Juice", "14")}
<div style="margin-top:18px;background:#D9B26A;color:#2B2622;border-radius:12px;padding:16px 18px;display:flex;flex-direction:column;gap:4px">
<span style="font-size:19px;font-weight:800;letter-spacing:0.16em">MORNING DEAL</span>
<span style="font-size:27px;font-weight:800;line-height:1.2">Coffee + croissant</span>
<span style="font-size:22px;font-weight:600">Only 18 · before 10 AM</span>
</div>
<div style="text-align:right;font-size:18px;color:#B9AFA2;margin-top:6px">prices in AED</div>
</div>"""
def step(day, en, a):
    return f'<div style="display:flex;flex-direction:column;gap:4px"><span style="font-weight:800;font-size:22px;letter-spacing:0.16em;color:{GOLD}">{day}</span><span style="font-size:29px;font-weight:600;line-height:1.3">{en}</span>{ar(a, 27, 600, MUTED)}</div>'
s3 = f"""
{h("You've said yes to an offer <i style='color:" + MAROON + "'>you didn't plan.</i>", 62)}
<div style="display:flex;gap:40px;align-items:center">
{board}
<div style="flex:1;display:flex;flex-direction:column;gap:24px">
{step("9:40 AM, CAFÉ", "You walk in for just a coffee. 15 dirhams.", "مشيت عشان قهوة بس")}
{step("THEN THIS", "You see “coffee + croissant, 18, before 10”. Only 3 more, and the deal ends soon. You take it.", "قلت: بس 3 دراهم زيادة؟ خلاص")}
</div>
</div>
<div style="background:{MAROON};color:{CREAM};border-radius:22px;padding:24px 32px;font-size:28px;font-weight:600;line-height:1.4"><b>The business side:</b> a salon posts “Haircut, 60 AED” and gets 6 bookings a week. Then: “Haircut + beard trim + hot towel, 75 AED. Not happy? Next one is free. 15 slots this week.” All 15 slots get booked. Same chair, better offer. <span style="opacity:0.75">(example numbers)</span></div>
"""
page(3, "REAL-LIFE EXAMPLE", s3)

# 4 the 4 parts, each with an everyday example
def pt(n, title, ex, a):
    return f'''<div style="display:flex;gap:24px;align-items:flex-start;background:{PAPER};border:2px solid {RULE};border-radius:20px;padding:20px 28px">{num(n)}
<div style="flex:1;display:flex;flex-direction:column;gap:2px"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:16px"><span style="font-size:33px;font-weight:800">{title}</span><span lang="ar" dir="rtl" style="{AR}font-size:27px;font-weight:600;color:{MAROON}">{a}</span></div><span style="font-size:28px;color:{MUTED};line-height:1.35;font-style:italic">{ex}</span></div></div>'''
s4 = f'''
{h("Build it from 4 parts", 76)}
<div style="display:flex;flex-direction:column;gap:14px">
{pt(1, "The result", "Not “50 ml perfume”. Say “Smell fresh from morning to night.”", "النتيجة")}
{pt(2, "The bonus", "“Free travel-size bottle with every perfume.”", "الهدية")}
{pt(3, "The promise", "“Not happy with your cut? The next one is free.”", "الضمان")}
{pt(4, "The reason to act now", "“Only 20 abayas in this colour.” “Ends Thursday.”", "ليه هسي")}
</div>
<div style="font-size:29px;color:{MUTED};line-height:1.4">Each part removes one reason to say “maybe later”.</div>
'''
page(4, "STEP 1 · THE PARTS", s4)

# 5 fill-in formula
def blank(t):
    return f'<span style="background:#EADFC9;color:{MAROON};font-weight:800;border-radius:8px;padding:2px 10px">{t}</span>'
s5 = f'''
{h("Fill in the blanks", 80)}
<div style="background:{PAPER};border:2px solid {RULE};border-radius:24px;padding:34px 38px;font-size:36px;font-weight:600;line-height:1.75">
Get {blank("result")} with {blank("product")}, plus {blank("bonus")}. {blank("Promise")}. Only {blank("limit")}.
</div>
<div style="font-weight:800;font-size:24px;letter-spacing:0.16em;color:{GOLD}">FILLED IN · ABAYA STORE</div>
<div style="border-left:6px solid {MAROON};padding:6px 0 6px 30px;font-size:33px;font-weight:600;line-height:1.45">“Look elegant at every wedding and gathering with our linen abaya, plus a free matching sheyla. Free size exchange within 7 days. Only 30 pieces.”</div>
{ar("عبّي الفراغات دي، وعرضك جاهز.", 36, 700, MAROON)}
'''
page(5, "STEP 2 · THE FORMULA", s5)

# 6 before / after rewrites
rows = [("“Burger meal, 35 AED.”", "“Burger meal + free dessert, 35 AED. Weekdays only.”"),
        ("“Gym membership available.”", "“Train for 30 days. If you don't feel stronger, your money back.”"),
        ("“Perfume sale, 10% off.”", "“Buy any perfume, get a free travel size. This week only.”"),
        ("“English lessons, DM us.”", "“Speak with confidence in 8 weeks. First class free.”")]
tbl = ""
for a_, b_ in rows:
    tbl += f'<div style="display:grid;grid-template-columns:1fr 1.3fr;gap:28px;border-top:2px solid {RULE};padding:22px 0"><div style="font-size:28px;font-weight:500;line-height:1.35;color:{MUTED};text-decoration:line-through;text-decoration-color:{MAROON}">{a_}</div><div style="font-size:29px;font-weight:800;line-height:1.3;color:{INK}">{b_}</div></div>'
s6 = f'''
{h("Same product. <i style='color:" + MAROON + "'>Better offer.</i>", 76)}
<div style="display:grid;grid-template-columns:1fr 1.3fr;gap:28px;font-size:24px;font-weight:800;letter-spacing:0.16em;color:{GOLD}"><span>WEAK</span><span>IRRESISTIBLE</span></div>
<div style="display:flex;flex-direction:column;border-bottom:2px solid {RULE}">{tbl}</div>
{ar("نفس المنتج، نفس السعر تقريباً… بس العرض أقوى.", 34, 700, MAROON)}
'''
page(6, "STEP 3 · REWRITE", s6)

# 7 mistakes
def mis(t, fix):
    x = f'<svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="{MAROON}" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
    return f'<div style="display:flex;gap:22px;align-items:flex-start;padding:22px 0;border-bottom:2px solid {RULE}">{x}<div style="flex:1;display:flex;flex-direction:column;gap:6px"><span style="font-size:35px;font-weight:800;line-height:1.2">{t}</span><span style="font-size:29px;color:{MUTED};line-height:1.35"><b style="color:{GOLD}">Fix:</b> {fix}</span></div></div>'
s7 = f'''
{h("4 mistakes that kill offers", 76)}
<div style="display:flex;flex-direction:column">
{mis("Only cutting the price", "add value (a bonus, a promise) before you discount")}
{mis("Fake urgency: “ends today”, every day", "use real limits, and keep them")}
{mis("Five deals at once", "one clear offer per post")}
{mis("Talking about features", "talk about the result the customer gets")}
</div>
{ar("التخفيض ما هو الحل الوحيد. زيد القيمة، ما تنقّص القروش.", 34, 700, MAROON)}
'''
page(7, "AVOID THIS", s7)

# 8 checklist
def ck(t):
    b = f'<span style="width:46px;height:46px;border:3px solid {MAROON};border-radius:10px;flex:none;box-sizing:border-box;display:flex;align-items:center;justify-content:center"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{MAROON}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"/></svg></span>'
    return f'<div style="display:flex;gap:24px;align-items:center;font-size:36px;font-weight:600;line-height:1.3">{b}<span>{t}</span></div>'
s8 = f'''
{h("Before you post an offer:", 78)}
<div style="background:{PAPER};border:2px solid {RULE};border-radius:26px;padding:44px 44px;display:flex;flex-direction:column;gap:30px">
{ck("It leads with the result")}
{ck("There's a bonus that feels generous")}
{ck("A promise removes the risk")}
{ck("A real reason to buy now")}
{ck("One offer, said in one sentence")}
{ck("You can afford it if it sells out")}
</div>
{ar("اكتب عرضك هسي بالأربعة حاجات دي.", 40, 700, MAROON)}
'''
page(8, "SCREENSHOT THIS", s8)

# 9 CTA
s9 = f'''
{h('Learned something?<br><span style="font-style:italic;font-weight:700;color:' + MAROON + '">Pass it on.</span>', 104)}
<div style="display:flex;flex-direction:column;gap:22px;font-size:40px;font-weight:600">
<span>1. <b>Save</b> it for your next promo</span>
<span>2. <b>Send</b> it to someone who runs a business</span>
<span>3. <b>Follow</b> for Lesson 04 tomorrow</span>
</div>
<div style="background:{MAROON};color:{CREAM};border-radius:24px;padding:34px 40px;display:flex;flex-direction:column;gap:8px">
<span style="font-size:36px;font-weight:700">What should Lesson 04 be? Tell me in the comments.</span>
<span lang="ar" dir="rtl" style="{AR}font-size:34px;font-weight:600;text-align:right">الدرس الجاي يكون عن شنو؟ كلمني في الكومنتات</span>
</div>
'''
page(9, "NEW LESSON EVERY DAY", s9, last=True)

print("ok")

# ---- UNIFIED SERIES COVER (same layout every lesson; only the fields below change)
COVER = dict(num="03", topic="The Irresistible Offer", tag="COPYWRITING · SALES", hook="Don't drop your price. Make your offer stronger.",
             ar_topic="عرض ما بتقدر ترفضو", ar_hook="ما تنزّل السعر. خلّي العرض أقوى.")
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
