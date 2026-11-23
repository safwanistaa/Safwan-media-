import re
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

src_dir = Path(sys.argv[1])
out_dir = Path(sys.argv[2])
names = sys.argv[3:]
out_dir.mkdir(parents=True, exist_ok=True)


def to_html(text):
    body = re.search(r"<x-dc>(.*)</x-dc>", text, re.S).group(1)
    styles = "".join(re.findall(r"<style>(.*?)</style>", body, re.S))
    body = re.sub(r"<helmet>.*?</helmet>", "", body, flags=re.S)
    return ("<!doctype html><html><head><meta charset='utf-8'><style>"
            "html,body{margin:0;width:1080px;height:1350px}" + styles +
            "</style></head><body>" + body + "</body></html>")


with sync_playwright() as p:
    browser = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox"])
    page = browser.new_page(viewport={"width": 1080, "height": 1350})
    for i, name in enumerate(names, 1):
        # Write next to the source so relative image paths (e.g. photo.jpg) resolve.
        tmp = src_dir / f"_render_{i:02d}.html"
        tmp.write_text(to_html((src_dir / name).read_text(encoding="utf-8")), encoding="utf-8")
        page.goto(tmp.resolve().as_uri())
        tmp.unlink()
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(300)
        page.screenshot(path=str(out_dir / f"slide{i:02d}.jpg"), type="jpeg", quality=92)
    browser.close()
print("ok")
