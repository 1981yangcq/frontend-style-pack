# -*- coding: utf-8 -*-
"""给每个 demo 截缩略图（16:9）。支持按语言出图：python build_thumbs.py --lang=en"""
import json, os, subprocess, sys, tempfile, threading, functools, http.server, socketserver
from PIL import Image

OUT = os.path.dirname(os.path.abspath(__file__))
LANG = "zh-CN"
for a in sys.argv[1:]:
    if a.startswith("--lang="):
        LANG = a.split("=", 1)[1]
THUMBS = os.path.join(OUT, "assets", "thumbs") if LANG == "zh-CN" else os.path.join(OUT, "assets", "thumbs", LANG)
os.makedirs(THUMBS, exist_ok=True)

# 本地 http 服务：file:// 下 fetch 语言包会被拦
PORT = 8731
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=OUT)
class Q(socketserver.TCPServer):
    allow_reuse_address = True
httpd = Q(("127.0.0.1", PORT), Handler)
threading.Thread(target=httpd.serve_forever, daemon=True).start()

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
    url = "http://127.0.0.1:%d/demos/%s.html?embed=1&lang=%s" % (PORT, slug, LANG)
    cmd = [CHROME, "--headless=new", "--no-sandbox", "--disable-crash-reporter",
           "--disable-breakpad", "--disable-gpu", "--hide-scrollbars",
           "--user-data-dir=" + prof, "--window-size=%d,%d" % (W, H),
           "--virtual-time-budget=4500", "--screenshot=" + png, url]
    subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60)
    if not os.path.exists(png):
        print("FAIL", sid, slug, flush=True)
        continue
    im = Image.open(png).convert("RGB").crop((0, 0, W, H)).resize((TW, TH), Image.LANCZOS)
    im.save(os.path.join(THUMBS, "%02d.jpg" % sid), "JPEG", quality=86, optimize=True)
    print("ok", "%02d" % sid, slug, flush=True)

httpd.shutdown()
print("done", LANG, len(os.listdir(THUMBS)), "->", THUMBS)
