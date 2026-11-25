# -*- coding: utf-8 -*-
"""用 headless Chrome 给每个 demo 截一张缩略图（16:9），供表格与左侧导航使用。"""
import json, os, subprocess, sys, tempfile
from PIL import Image

OUT = os.path.dirname(os.path.abspath(__file__))
THUMBS = os.path.join(OUT, "assets", "thumbs")
os.makedirs(THUMBS, exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
STYLES = json.load(open(os.path.join(OUT, "styles.json"), encoding="utf-8"))
from themes import SLUGS

W, H = 1440, 810
TW, TH = 720, 405

tmp = tempfile.mkdtemp(prefix="thumbs-")
prof = os.path.join(tmp, "prof")

for s in STYLES:
    sid = s["id"]
    slug = SLUGS[sid]
    png = os.path.join(tmp, "shot.png")
    if os.path.exists(png):
        os.remove(png)
    url = "file://%s/demos/%s.html?embed=1" % (OUT, slug)
    cmd = [CHROME, "--headless=new", "--no-sandbox", "--disable-crash-reporter",
           "--disable-breakpad", "--disable-gpu", "--hide-scrollbars",
           "--user-data-dir=" + prof, "--window-size=%d,%d" % (W, H),
           "--virtual-time-budget=3000", "--screenshot=" + png, url]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    if not os.path.exists(png):
        print("FAIL", sid, slug, flush=True)
        continue
    im = Image.open(png).convert("RGB").crop((0, 0, W, H)).resize((TW, TH), Image.LANCZOS)
    im.save(os.path.join(THUMBS, "%02d.jpg" % sid), "JPEG", quality=86, optimize=True)
    print("ok", "%02d" % sid, slug, flush=True)

print("done", len(os.listdir(THUMBS)))
