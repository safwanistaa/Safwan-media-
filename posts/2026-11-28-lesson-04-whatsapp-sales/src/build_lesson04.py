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
LESSON = "LESSON 04"; TOPIC = "WHATSAPP SALES"

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



# 2 what it is — the chat-to-sale path
def part(n, en, sub, a):
    return f'''<div style="display:flex;gap:26px;align-items:center;background:{PAPER};border:2px solid {RULE};border-radius:22px;padding:20px 30px">{num(n)}
<div style="flex:1;display:flex;flex-direction:column;gap:4px"><span style="font-size:34px;font-weight:800">{en}</span><span style="font-size:27px;color:{MUTED};line-height:1.35">{sub}</span></div><span lang="ar" dir="rtl" style="{AR}font-size:29px;font-weight:600;color:{MAROON}">{a}</span></div>'''
s2 = f'''
{h("Every chat is a customer <i style='color:" + MAROON + "'>halfway to buying.</i>", 64)}
<div style="font-size:31px;line-height:1.4;color:{INK}">WhatsApp marketing = walking that person from “hi” to “paid”, in 5 moves:</div>
<div style="display:flex;flex-direction:column;gap:12px">
{part(1, "Start the chat", "Make it one tap: link or QR code", "خلّيهو يبدأ")}
{part(2, "Reply fast", "First impressions happen in minutes", "رُد بسرعة")}
{part(3, "Show it", "Photo, price, catalog, in one message", "ورّيهو")}
{part(4, "Close it", "Give one clear next step", "اقفل البيعة")}
{part(5, "Follow up", "One polite reminder, not ten", "تابع معاهو")}
</div>
{ar("الزول الكلّمك في الواتساب، نُص الطريق للشراء جاهو براهو.", 32, 700, MAROON)}
'''
page(2, "WHAT IT IS", s2)

# 3 REAL-LIFE EXAMPLE — two shops, same question
def bub(t, me=False, time=""):
    bg = "#DCEFD6" if me else "#FFFFFF"
    al = "flex-end" if me else "flex-start"
    return f'<div style="align-self:{al};max-width:300px;background:{bg};border-radius:16px;padding:10px 14px;font-size:20px;font-weight:500;line-height:1.3;color:{INK};box-shadow:0 1px 0 #C9BFB0">{t}<div style="text-align:right;font-size:14px;color:{MUTED};margin-top:2px">{time}</div></div>'
def phone(name, inner, tag, tagc):
    return f'''<div style="flex:1;display:flex;flex-direction:column;gap:12px">
<div style="background:#EFE8DC;border:3px solid {INK};border-radius:30px;overflow:hidden;height:440px;box-sizing:border-box;display:flex;flex-direction:column">
<div style="background:{INK};color:{CREAM};padding:14px 18px;font-size:20px;font-weight:700;display:flex;align-items:center;gap:10px"><span style="width:30px;height:30px;border-radius:50%;background:#8A7F72;flex:none"></span>{name}</div>
<div style="flex:1;padding:14px;display:flex;flex-direction:column;gap:9px">{inner}</div></div>
<span style="align-self:center;font-weight:800;font-size:21px;letter-spacing:0.14em;color:{tagc}">{tag}</span></div>'''
p1 = phone("Perfume Shop A", bub("Salam, how much is the oud set?", True, "11:02 PM") + bub("hi", False, "next day 3:40 PM") + bub("…never mind, I bought it already", True, "3:41 PM"), "LOST THE SALE", MAROON)
p2 = phone("Perfume Shop B", bub("Salam, how much is the oud set?", True, "11:02 PM") + bub("Welcome! The oud set is 180 AED. For you or a gift? We deliver tomorrow.", False, "11:02 PM") + bub("Gift! Wrap it please", True, "11:05 PM"), "MADE THE SALE", GOLD)
s3 = f"""
{h("You've done this. <i style='color:" + MAROON + "'>Shop B got your money.</i>", 60)}
<div style="display:flex;gap:30px">{p1}{p2}</div>
{ar("سألت عن السعر بالليل. الرد السريع هو الجاب القروش.", 30, 600, MUTED)}
<div style="background:{MAROON};color:{CREAM};border-radius:22px;padding:22px 30px;font-size:27px;font-weight:600;line-height:1.4"><b>The business side:</b> an abaya store gets 40 chats a week and closes 5. It adds an instant greeting, saved replies and one follow-up the next day. Same 40 chats, now 12 orders. <span style="opacity:0.75">(example numbers)</span></div>
"""
page(3, "REAL-LIFE EXAMPLE", s3)

# 4 set up the business app tools, each with an everyday example
def pt(n, title, ex, a):
    return f'''<div style="display:flex;gap:24px;align-items:flex-start;background:{PAPER};border:2px solid {RULE};border-radius:20px;padding:18px 28px">{num(n)}
<div style="flex:1;display:flex;flex-direction:column;gap:2px"><div style="display:flex;justify-content:space-between;align-items:baseline;gap:16px"><span style="font-size:32px;font-weight:800">{title}</span><span lang="ar" dir="rtl" style="{AR}font-size:26px;font-weight:600;color:{MAROON}">{a}</span></div><span style="font-size:27px;color:{MUTED};line-height:1.35;font-style:italic">{ex}</span></div></div>'''
s4 = f'''
{h("Set up the free tools <i style='color:" + MAROON + "'>once.</i>", 72)}
<div style="display:flex;flex-direction:column;gap:12px">
{pt(1, "Business profile", "Hours, location, a one-line “what we sell”.", "البروفايل")}
{pt(2, "Greeting message", "“Welcome! Send a photo of what you like, we reply with price.”", "رسالة الترحيب")}
{pt(3, "Away message", "“We're closed now. We reply at 10 AM, first thing.”", "رسالة الغياب")}
{pt(4, "Quick replies", "Save answers you type every day: price list, location, delivery.", "ردود جاهزة")}
{pt(5, "Catalog", "Your best products with photo + price, so no one waits.", "الكتالوج")}
</div>
<div style="font-size:27px;color:{MUTED};line-height:1.4">Find them in the WhatsApp Business app: Settings, then Business tools.</div>
'''
page(4, "STEP 1 · SET IT UP", s4)

# 5 the reply that sells
def line(n, en, ex):
    return f'<div style="display:flex;gap:22px;align-items:flex-start">{num(n)}<div style="flex:1;display:flex;flex-direction:column;gap:4px"><span style="font-size:32px;font-weight:800;line-height:1.25">{en}</span><span style="font-size:28px;color:{MUTED};line-height:1.35;font-style:italic">{ex}</span></div></div>'
s5 = f'''
{h("“Price?” Answer like this:", 76)}
<div style="background:{PAPER};border:2px solid {RULE};border-radius:24px;padding:32px 36px;display:flex;flex-direction:column;gap:24px">
{line(1, "Answer the question first", "“The linen abaya is 220 AED.”")}
{line(2, "Ask one helpful question", "“Is it for daily wear or an occasion?”")}
{line(3, "Show, don't describe", "Send 2 photos or the catalog link.")}
{line(4, "Give one next step", "“Want it delivered tomorrow? Just send your area.”")}
</div>
<div style="font-weight:800;font-size:24px;letter-spacing:0.16em;color:{GOLD}">ALL IN ONE MESSAGE</div>
<div style="align-self:flex-start;max-width:760px;background:#FFFFFF;border:2px solid {RULE};border-radius:22px 22px 22px 6px;padding:20px 26px;font-size:29px;font-weight:500;line-height:1.4">The linen abaya is 220 AED. Daily wear or an occasion? Here are 2 colours [photos]. Want it tomorrow? Just send your area.</div>
{ar("ما ترسل السعر وتسكت. السعر، سؤال، صورة، والخطوة الجاية.", 32, 700, MAROON)}
'''
page(5, "STEP 2 · THE REPLY", s5)

# 6 labels + follow-up map
rows = [("NEW CHAT", "Reply within minutes, even at night (away message)."),
        ("ASKED PRICE", "Next day: “Still thinking? Your size is still in stock.”"),
        ("ORDERED", "Same day: confirm, delivery time, thank you."),
        ("DELIVERED", "3 days later: “Happy with it? A photo would make our day.”")]
tbl = ""
for a_, b_ in rows:
    tbl += f'<div style="display:grid;grid-template-columns:300px 1fr;gap:28px;align-items:center;border-top:2px solid {RULE};padding:22px 0"><span style="justify-self:start;background:#EADFC9;color:{MAROON};font-weight:800;font-size:23px;letter-spacing:0.1em;border-radius:10px;padding:8px 14px">{a_}</span><div style="font-size:29px;font-weight:600;line-height:1.35;color:{INK}">{b_}</div></div>'
s6 = f'''
{h("Label every chat. <i style='color:" + MAROON + "'>Then follow up.</i>", 62)}
<div style="font-size:29px;line-height:1.4;color:{MUTED}">Labels sort chats by where the customer is. Each label has its own next message:</div>
<div style="display:flex;flex-direction:column;border-bottom:2px solid {RULE}">{tbl}</div>
{ar("رسالة متابعة وحدة ممكن ترجّع ليك زبون كان ماشي.", 32, 700, MAROON)}
'''
page(6, "STEP 3 · FOLLOW UP", s6)

# 7 mistakes
def mis(t, fix):
    x = f'<svg aria-hidden="true" width="40" height="40" viewBox="0 0 24 24" fill="none" stroke="{MAROON}" stroke-width="2.6" stroke-linecap="round"><path d="M6 6l12 12M18 6L6 18"/></svg>'
    return f'<div style="display:flex;gap:22px;align-items:flex-start;padding:22px 0;border-bottom:2px solid {RULE}">{x}<div style="flex:1;display:flex;flex-direction:column;gap:6px"><span style="font-size:35px;font-weight:800;line-height:1.2">{t}</span><span style="font-size:29px;color:{MUTED};line-height:1.35"><b style="color:{GOLD}">Fix:</b> {fix}</span></div></div>'
s7 = f'''
{h("4 mistakes that lose WhatsApp sales", 70)}
<div style="display:flex;flex-direction:column">
{mis("Replying hours later", "greeting + away message, and check chats at set times")}
{mis("Sending only the price, then silence", "price + question + photo + next step")}
{mis("Messaging everyone, every day", "only message people who chatted or agreed")}
{mis("3-minute voice notes", "short text they can read in 5 seconds")}
</div>
{ar("الزبون ما بستنّى. لو ما رديت، زول تاني حيرُد.", 34, 700, MAROON)}
'''
page(7, "AVOID THIS", s7)

# 8 checklist
def ck(t):
    b = f'<span style="width:46px;height:46px;border:3px solid {MAROON};border-radius:10px;flex:none;box-sizing:border-box;display:flex;align-items:center;justify-content:center"><svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="{MAROON}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12l5 5 9-10"/></svg></span>'
    return f'<div style="display:flex;gap:24px;align-items:center;font-size:36px;font-weight:600;line-height:1.3">{b}<span>{t}</span></div>'
s8 = f'''
{h("Your WhatsApp sales setup:", 78)}
<div style="background:{PAPER};border:2px solid {RULE};border-radius:26px;padding:44px 44px;display:flex;flex-direction:column;gap:30px">
{ck("Chat link or QR code in your bio")}
{ck("Profile: hours, location, what you sell")}
{ck("Greeting + away message on")}
{ck("Quick replies for your top 5 questions")}
{ck("Best products in the catalog")}
{ck("Every chat labelled, one follow-up sent")}
</div>
{ar("سوّي الحاجات دي النهارده، وشوف الفرق الأسبوع الجاي.", 36, 700, MAROON)}
'''
page(8, "SCREENSHOT THIS", s8)

# 9 CTA
s9 = f'''
{h('Learned something?<br><span style="font-style:italic;font-weight:700;color:' + MAROON + '">Pass it on.</span>', 104)}
<div style="display:flex;flex-direction:column;gap:22px;font-size:40px;font-weight:600">
<span>1. <b>Save</b> it for when you set up your shop</span>
<span>2. <b>Send</b> it to someone who sells on WhatsApp</span>
<span>3. <b>Follow</b> for Lesson 05 tomorrow</span>
</div>
<div style="background:{MAROON};color:{CREAM};border-radius:24px;padding:34px 40px;display:flex;flex-direction:column;gap:8px">
<span style="font-size:36px;font-weight:700">What should Lesson 05 be? Tell me in the comments.</span>
<span lang="ar" dir="rtl" style="{AR}font-size:34px;font-weight:600;text-align:right">الدرس الجاي يكون عن شنو؟ كلمني في الكومنتات</span>
</div>
'''
page(9, "NEW LESSON EVERY DAY", s9, last=True)

print("ok")

# ---- UNIFIED SERIES COVER (same layout every lesson; only the fields below change)
COVER = dict(num="04", topic="WhatsApp That Sells", tag="WHATSAPP · SALES", hook="Turn \"how much?\" chats into paid orders.",
             ar_topic="واتساب بيبيع", ar_hook="حوّل سؤال «بكم؟» لطلب مدفوع.")
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
