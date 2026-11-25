# -*- coding: utf-8 -*-
"""50 种前端风格的 demo 主题库：每种风格一套 token + 少量定制 CSS。"""

SANS = "'PingFang SC','Hiragino Sans GB','Noto Sans SC',system-ui,-apple-system,sans-serif"
SERIF = "Georgia,'Songti SC','Noto Serif SC','Times New Roman',serif"
MONO = "ui-monospace,'SF Mono',Menlo,'Courier New',monospace"
SYS = "'MS Sans Serif',Tahoma,Verdana,sans-serif"

BASE = dict(
    bg="#ffffff", bgimg="", surface="#ffffff", ink="#15150f", muted="#6d6d63",
    line="#e2e1d9", accent="#1d4ed8", on_accent="#ffffff",
    radius="14px", cardpad="26px", cardborder="1px solid var(--line)",
    shadow="0 1px 2px rgba(0,0,0,.04)",
    btnradius="10px", btnshadow="none", btnborder="none",
    ghostborder="1px solid var(--line)",
    fonth=SANS, fontb=SANS, fontk=MONO,
    lsh="-.02em", lhh="1.12", h1w="800", h1size="clamp(34px,5.6vw,64px)",
    ttk="none", lsk=".08em", cardgap="16px",
    navborder="1px solid var(--line)", leadfs="16.5px",
    layout="left", deco="", raw="", brandi="",
)

SLUGS = {
    1: "01-neo-brutalism", 2: "02-swiss-style", 3: "03-japanese-editorial",
    4: "04-terminal-cli", 5: "05-glassmorphism-retro", 6: "06-voxel",
    7: "07-neumorphism", 8: "08-retro-win95", 9: "09-biophilic",
    10: "10-3d-hyperrealism", 11: "11-vibrant-block", 12: "12-dark-oled",
    13: "13-accessible-ethical", 14: "14-claymorphism", 15: "15-aurora-ui",
    16: "16-retro-futurism", 17: "17-flat-design", 18: "18-liquid-glass",
    19: "19-motion-driven", 20: "20-micro-interactions", 21: "21-inclusive-design",
    22: "22-zero-interface", 23: "23-soft-ui", 24: "24-neubrutalism",
    25: "25-bento-grid", 26: "26-y2k", 27: "27-cyberpunk",
    28: "28-ai-native", 29: "29-memphis", 30: "30-vaporwave",
    31: "31-dimensional-layering", 32: "32-exaggerated-minimalism",
    33: "33-kinetic-typography", 34: "34-parallax-storytelling",
    35: "35-swiss-modernism-2", 36: "36-hud-sci-fi", 37: "37-bento-2",
    38: "38-spatial-ui", 39: "39-e-ink-paper", 40: "40-genz-chaos",
    41: "41-biomimetic", 42: "42-anti-polish-raw", 43: "43-tactile-digital",
    44: "44-nature-distilled", 45: "45-interactive-cursor",
    46: "46-voice-first", 47: "47-3d-product", 48: "48-gradient-mesh",
    49: "49-chromatic-aberration", 50: "50-vintage-film",
}

def T(**kw):
    d = dict(BASE)
    d.update(kw)
    return d

T1_ART = '<div class="art"><div class="obj"></div></div>'

THEMES = {
1: T(bg="#f2f0e6", surface="#fffdf5", ink="#111111", muted="#454540", line="#111111",
     accent="#f6d743", on_accent="#111111", radius="0", cardpad="24px",
     cardborder="3px solid #111", shadow="6px 6px 0 #111", btnradius="0",
     btnshadow="5px 5px 0 #111", btnborder="2px solid #111", ghostborder="2px solid #111",
     ttk="uppercase", lsk=".18em", navborder="3px solid #111",
     bgimg="background-image:radial-gradient(rgba(17,17,17,.16) 1px,transparent 1.2px);background-size:16px 16px;",
     raw=""".kicker{border:2px solid #111;background:#fff;padding:3px 9px;width:max-content;font-weight:600}
.card h3{text-transform:uppercase;letter-spacing:.04em}
.btn.ghost{background:#fff;color:#111;box-shadow:4px 4px 0 #111}
.card:nth-child(2){background:#fff}
h1{font-size:clamp(38px,6.4vw,76px);text-transform:none}"""),

2: T(bg="#fcfcfc", ink="#0a0a0a", muted="#6b6b6b", line="#e6e6e6", accent="#e4002b",
     radius="0", cardborder="none", cardpad="0 20px", shadow="none", btnradius="0",
     btnborder="0", ghostborder="1px solid #0a0a0a", lsh="-.045em", lhh="0.94",
     h1size="clamp(44px,7.2vw,88px)", lsk=".2em", ttk="uppercase",
     navborder="2px solid #0a0a0a",
     raw="""h1{font-weight:800}
.kicker{color:#e4002b}
.cards{border-top:1px solid #0a0a0a;padding-top:26px;gap:0}
.card{border-left:1px solid #e6e6e6;padding:4px 22px 0}
.card:first-child{border-left:0;padding-left:0}
.card .ico{border-radius:0;background:#e4002b}
.lead{max-width:44ch}
.btn.ghost{border:1px solid #0a0a0a}"""),

3: T(bg="#f3f1ea", surface="#fdfbf5", ink="#22211d", muted="#6b6759", line="#d4d3cc",
     accent="#dfff00", on_accent="#22211d", radius="6px",
     shadow="0 1px 0 rgba(0,0,0,.03)", h1w="600", lhh="1.35",
     lsk=".1em", ttk="uppercase", leadfs="15px",
     raw="""h1{font-weight:600;font-size:clamp(30px,4.4vw,50px);line-height:1.4}
h1 em{background:linear-gradient(transparent 66%,#dfff00 66%)}
.kicker{letter-spacing:.2em}
.card{background:#fdfbf5;border-color:#d4d3cc}
.card h3{font-weight:600;letter-spacing:0}
.btn{border-radius:4px;font-weight:500}
.cards{gap:14px}"""),

4: T(bg="#0d0f0e", surface="#111514", ink="#c5d0c0", muted="#7f8b7d", line="#242b22",
     accent="#dfff00", on_accent="#0d0f0e", radius="6px", cardborder="1px solid #242b22",
     shadow="none", fonth=MONO, fontb=MONO, lsh="-.01em", ttk="uppercase",
     lsk=".14em", navborder="1px solid #242b22",
     deco='<div class="term"><i></i>Node online<span>· build 2041 passed · 128ms</span></div>',
     raw=""".term{display:flex;gap:8px;align-items:center;font:12px/1 ui-monospace,monospace;color:#7f8b7d;margin-top:6px}
.term i{width:6px;height:6px;border-radius:50%;background:#b6ff3a;box-shadow:0 0 8px #b6ff3a;animation:pulse 1.6s infinite}
@keyframes pulse{50%{opacity:.3}}
.kicker:before{content:'$ ';color:#dfff00}
h1{font-weight:700;letter-spacing:-.02em;font-size:clamp(30px,4.6vw,52px);line-height:1.16}
.btn,.navbtn{font-weight:600;letter-spacing:.02em}
.card h3{text-transform:uppercase;letter-spacing:.08em;font-size:12px}
.card{padding:22px}"""),

5: T(bg="#071018", ink="#eef2ec", muted="#9fb0ad", line="rgba(255,255,255,.14)",
     accent="#dfff00", on_accent="#071018", surface="rgba(255,255,255,.07)", radius="18px",
     cardborder="1px solid rgba(255,255,255,.16)", shadow="0 24px 60px rgba(0,0,0,.45)",
     btnradius="999px",
     bgimg="background-image:radial-gradient(60% 50% at 18% 8%,rgba(36,84,255,.5),transparent),radial-gradient(50% 45% at 86% 16%,rgba(223,255,0,.16),transparent),radial-gradient(70% 60% at 60% 105%,rgba(0,180,160,.3),transparent);background-attachment:fixed;",
     raw="""body{background-color:#071018}
.card,.navbtn,.btn{backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px)}
body:after{content:'';position:fixed;inset:0;pointer-events:none;z-index:0;
  background:repeating-linear-gradient(to bottom,rgba(255,255,255,.055) 0 1px,transparent 1px 4px);mix-blend-mode:overlay}
h1{text-shadow:0 0 40px rgba(223,255,0,.18)}
.kicker{color:#dfff00}"""),

6: T(bg="#1b2417", surface="#2c3a24", ink="#e8e4d4", muted="#9aa88f", line="#0e140b",
     accent="#7B8F3A", on_accent="#0e140b", radius="0", cardborder="3px solid #0e140b",
     shadow="inset 0 -6px 0 rgba(0,0,0,.35),inset 0 4px 0 rgba(255,255,255,.07)",
     btnradius="0", btnshadow="inset 0 -5px 0 rgba(0,0,0,.4),inset 0 3px 0 rgba(255,255,255,.18)",
     btnborder="2px solid #0e140b", fonth=MONO, fontk=MONO, ttk="uppercase",
     lsk=".16em", lsh="0",
     bgimg="background-image:linear-gradient(rgba(255,255,255,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(255,255,255,.05) 1px,transparent 1px);background-size:16px 16px;",
     deco='<div class="hud"><span>HP</span><b>████████░░</b><em>18/20</em></div>',
     raw="""h1{letter-spacing:0;text-shadow:3px 3px 0 #0e140b;font-size:clamp(32px,5vw,56px);line-height:1.06}
.card{padding:20px}
.card:nth-child(2){background:#8B6B3D}
.card:nth-child(3){background:#3a3a3a}
.hud{display:flex;gap:8px;align-items:center;font:12px ui-monospace,monospace;color:#c7d3a8;margin-top:10px}
.hud span{color:#7B8F3A}
.hud b{letter-spacing:1px;color:#7B8F3A}
.hud em{font-style:normal;color:#9aa88f}"""),

7: T(bg="#e0e5ec", surface="#e0e5ec", ink="#3b4a5a", muted="#78879a", line="#d2d9e3",
     accent="#5b7cfa", radius="20px", cardborder="none", cardpad="32px",
     shadow="8px 8px 16px #c2c9d4,-8px -8px 16px #ffffff", btnradius="14px",
     btnshadow="6px 6px 12px #c2c9d4,-6px -6px 12px #ffffff", ghostborder="none",
     layout="center",
     raw=""".btn:active{box-shadow:inset 4px 4px 8px #c2c9d4,inset -4px -4px 8px #fff}
.btn.ghost{background:#e0e5ec;color:#3b4a5a}
.card .ico{border-radius:50%;box-shadow:inset 3px 3px 6px #c2c9d4,inset -3px -3px 6px #fff;background:#e0e5ec}
h1{color:#3b4a5a}
.nav{border-bottom:0}
.kicker{color:#78879a}"""),

8: T(bg="#008080", surface="#c0c0c0", ink="#000000", muted="#202020", line="#808080",
     accent="#000080", on_accent="#ffffff", radius="0", cardborder="2px solid",
     shadow="none", btnradius="0", btnshadow="none", btnborder="2px solid",
     ghostborder="2px solid", fonth=SYS, fontb=SYS, navborder="none", lsh="0",
     lhh="1.1", h1size="clamp(28px,4.2vw,48px)",
     raw="""body{background-color:#008080}
.nav{border:2px solid;border-color:#fff #808080 #808080 #fff;background:#c0c0c0;padding:8px 10px;margin-top:16px;color:#000}
.nav .brand,.nav nav{color:#000}
.card{border-color:#fff #808080 #808080 #fff;background:#c0c0c0;padding:36px 16px 16px;position:relative}
.card:before{content:'⬜ 属性';position:absolute;left:0;top:0;right:0;height:22px;background:#000080;color:#fff;
  font:11px Tahoma;line-height:22px;padding-left:6px}
.card:after{content:'';position:absolute;right:5px;top:4px;width:15px;height:15px;background:#c0c0c0;
  border:2px solid;border-color:#fff #808080 #808080 #fff}
.card h3{font-size:13px;font-weight:700}
.card .ico{border-radius:0;background:#000080}
.card p{font-size:12.5px;color:#202020}
.btn,.navbtn{border:2px solid;border-color:#fff #808080 #808080 #fff;background:#c0c0c0;color:#000;
  box-shadow:none;border-radius:0;font-size:13px}
.btn:active,.navbtn:active{border-color:#808080 #fff #fff #808080}
.btn.ghost{background:#c0c0c0;color:#000}
h1{font-family:'MS Sans Serif',Tahoma,sans-serif;font-weight:700;letter-spacing:0}
.lead{font-size:15px;color:#202020}
.kicker{color:#000;background:#c0c0c0;border:2px solid;border-color:#808080 #fff #fff #808080;padding:3px 8px;width:max-content;font-size:11px}"""),

9: T(bg="#f3f0e8", surface="#fdfbf5", ink="#2c332a", muted="#6b7565", line="#dedacd",
     accent="#6b8a5e", radius="16px", shadow="0 10px 30px rgba(90,110,80,.10)",
     navborder="3px solid #6b8a5e", cardpad="28px",
     bgimg="background-image:radial-gradient(40% 30% at 82% 0%,rgba(150,180,120,.35),transparent),radial-gradient(35% 30% at 8% 22%,rgba(205,193,150,.4),transparent);",
     raw=""".card .ico{border-radius:50%;background:#6b8a5e}
.kicker{color:#6b8a5e}
.nav{border-bottom:3px solid #6b8a5e;padding-bottom:14px}
.btn{border-radius:999px}
.btn.ghost{border-radius:999px;border-color:#c9c3ae}"""),

10: T(bg="#f4f5f8", surface="linear-gradient(160deg,#ffffff,#eef0f6)", ink="#14161a",
      muted="#6a6f7a", line="rgba(20,30,60,.08)", accent="#2b6cff", radius="22px",
      cardborder="1px solid rgba(255,255,255,.9)",
      shadow="0 24px 60px rgba(20,30,60,.14),0 2px 6px rgba(20,30,60,.06)",
      btnradius="14px", btnshadow="0 10px 24px rgba(43,108,255,.35)",
      ghostborder="1px solid rgba(20,30,60,.14)", layout="split",
      deco=T1_ART,
      raw=""".art{perspective:1000px;display:grid;place-items:center;min-height:340px}
.obj{width:250px;height:320px;border-radius:22px;background:linear-gradient(150deg,#fff,#dfe6f7 55%,#b9c8ea);
  box-shadow:0 45px 70px rgba(30,50,100,.3),0 6px 12px rgba(30,50,100,.12),inset 0 1px 0 #fff;
  transform:rotateY(-18deg) rotateX(6deg);transition:transform .5s cubic-bezier(.25,.46,.45,.94)}
.obj:hover{transform:translateY(-16px) translateZ(50px) rotateY(-8deg) rotateX(3deg)}
.card:hover{transform:translateY(-4px)}
.card{transition:transform .4s cubic-bezier(.25,.46,.45,.94)}
h1{font-weight:700;letter-spacing:-.035em}"""),

11: T(bg="#ffffff", surface="#ffffff", ink="#111111", line="#111111", accent="#ff6b6b",
      on_accent="#111111", radius="0", cardborder="3px solid #111", shadow="4px 8px 0 #111",
      btnradius="0", btnshadow="4px 6px 0 #111", btnborder="3px solid #111",
      ghostborder="3px solid #111", h1size="clamp(42px,6.8vw,82px)", lsh="-.04em",
      raw=""".card:nth-child(2){background:#ffd93d}
.card:nth-child(3){background:#4ecdc4}
.btn.ghost{background:#fff;color:#111}
h1{font-weight:900}
.nav{border-bottom:3px solid #111}
.kicker{color:#111;font-weight:700}"""),

12: T(bg="#000000", surface="#0a0a0a", ink="#ffffff", muted="#9a9a9a", line="#1a1a1a",
      accent="#ffffff", on_accent="#000000", radius="14px",
      cardborder="1px solid #1a1a1a", shadow="none", ghostborder="1px solid #2a2a2a",
      lsh="-.03em",
      raw="""h1{font-weight:700}
.card .ico{background:#fff;border-radius:50%}
.kicker{color:#7a7a7a}
.btn{font-weight:600}
.nav{border-bottom:1px solid #141414}"""),

13: T(bg="#ffffff", ink="#000000", muted="#3a3a3a", line="#000000", accent="#0033cc",
      radius="6px", cardborder="2px solid #000", shadow="none", btnborder="2px solid #000",
      btnradius="6px", ghostborder="2px solid #000",
      fonth="'Atkinson Hyperlegible',Arial,'PingFang SC',sans-serif", leadfs="18px",
      raw=""":focus-visible{outline:3px solid #000;outline-offset:3px}
.btn,.navbtn{min-height:44px;display:inline-flex;align-items:center;justify-content:center;padding:10px 22px;font-weight:700}
.card .ico{border-radius:2px}
.card{padding:28px}
.lead{line-height:1.7}
.kicker{font-size:12.5px;letter-spacing:.1em;color:#000}
.kicker:after{content:' · WCAG AA';color:#0033cc}
.btn.ghost{background:#fff;color:#000}"""),

14: T(bg="#f5d3ae", surface="linear-gradient(145deg,#ffdcb8,#eec296)", ink="#4a3324",
      muted="#8a6a52", line="rgba(74,51,36,.12)", accent="#d2691e", radius="24px",
      cardborder="none", cardpad="30px",
      shadow="10px 10px 20px #d9b48f,-10px -10px 20px #ffe6c9", btnradius="18px",
      btnshadow="8px 8px 16px #d9b48f,-8px -8px 16px #ffe6c9", ghostborder="none",
      layout="center",
      raw=""".btn:active{box-shadow:inset 6px 6px 12px #c99f78,inset -6px -6px 12px #ffe0bd}
.btn.ghost{background:transparent;box-shadow:none;border:0;color:#4a3324}
.card .ico{border-radius:50%;background:#ffd9b0;box-shadow:inset 4px 4px 8px #e0b892,inset -4px -4px 8px #fff1dd}
h1{color:#4a3324}
.nav{border-bottom:0}"""),

15: T(bg="#06070a", ink="#f2f6f4", muted="#96a3a2", line="rgba(255,255,255,.08)",
      accent="#0d9488", on_accent="#eafffb", surface="rgba(255,255,255,.05)", radius="18px",
      cardborder="1px solid rgba(255,255,255,.09)", shadow="0 24px 60px rgba(0,0,0,.5)",
      btnradius="999px",
      bgimg="background-image:radial-gradient(45% 40% at 14% 12%,rgba(56,189,248,.35),transparent),radial-gradient(40% 40% at 82% 8%,rgba(52,211,153,.3),transparent),radial-gradient(50% 45% at 70% 78%,rgba(168,85,247,.32),transparent);background-attachment:fixed;",
      raw=""".card,.btn{backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px)}
.card .ico{border-radius:50%;background:linear-gradient(140deg,#34d399,#0d9488)}
h1{font-weight:700;letter-spacing:-.03em}
.kicker{color:#34d399}"""),

16: T(bg="#1a0a2e", surface="rgba(40,20,60,.8)", ink="#ffe9f4", muted="#b58fc2",
      line="rgba(255,107,157,.28)", accent="#ff6b9d", on_accent="#1a0a2e", radius="16px",
      cardborder="1px solid rgba(255,107,157,.35)", shadow="0 0 30px rgba(255,107,157,.22)",
      btnradius="10px", btnshadow="0 0 18px rgba(255,107,157,.5)",
      bgimg="background-image:linear-gradient(180deg,#1a0a2e,#2b0d47 60%,#1a0a2e);",
      raw="""h1{text-shadow:0 0 26px rgba(255,107,157,.55);letter-spacing:.01em;font-weight:700}
.kicker{color:#ff6b9d;letter-spacing:.24em}
.card .ico{background:#ff6b9d;clip-path:polygon(50% 0,100% 100%,0 100%)}"""),

17: T(bg="#f7f8fa", ink="#1b2733", muted="#6b7b8c", line="#e6eaee", accent="#3490dc",
      radius="4px", shadow="none", btnradius="4px", cardborder="1px solid #e6eaee",
      raw=""".card .ico{background:#3490dc;border-radius:4px}
h1{font-weight:700}
.nav{border-bottom:1px solid #e6eaee}"""),

18: T(bg="#0b1020", ink="#eaf0ff", muted="#9fb0d0", line="rgba(255,255,255,.12)",
      accent="#a5b4fc", on_accent="#0b1020", surface="rgba(255,255,255,.035)", radius="18px",
      cardborder="1px solid rgba(255,255,255,.14)", shadow="0 24px 60px rgba(0,0,0,.5)",
      btnradius="999px",
      bgimg="background-image:radial-gradient(50% 50% at 18% 0%,rgba(80,120,255,.35),transparent),radial-gradient(45% 45% at 86% 26%,rgba(200,90,255,.28),transparent);background-attachment:fixed;",
      raw=""".card,.navbtn,.btn{backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.card{position:relative;overflow:hidden}
.card:before{content:'';position:absolute;inset:0;border-radius:inherit;pointer-events:none;
  background:linear-gradient(120deg,rgba(255,255,255,.2),transparent 42%)}
h1{font-weight:600;letter-spacing:-.025em}
.kicker{color:#a5b4fc}"""),

19: T(bg="#000000", surface="#0d0d0d", ink="#ffffff", muted="#9c9c9c", line="#222222", accent="#ff3b30",
      radius="16px", cardborder="1px solid #222", shadow="none", btnradius="12px",
      raw=""".card{transition:transform .45s cubic-bezier(.34,1.56,.64,1),border-color .3s}
.card:hover{transform:scale(1.05) rotate(1deg);border-color:#ff3b30}
.btn{transition:transform .3s cubic-bezier(.34,1.56,.64,1)}
.btn:hover{transform:scale(1.06)}
h1{transition:letter-spacing .6s;font-weight:800}
h1:hover{letter-spacing:.02em}
@media (prefers-reduced-motion:reduce){*{transition:none!important;animation:none!important}}"""),

20: T(bg="#fbfbfc", ink="#16181d", muted="#6a7080", line="#eeeeee", accent="#3b5bdb",
      radius="10px", cardborder="1px solid #eee", shadow="0 2px 4px rgba(0,0,0,.04)",
      btnradius="8px", btnshadow="0 2px 4px rgba(59,91,219,.18)",
      raw=""".card{transition:transform .2s ease,box-shadow .2s ease}
.card:hover{transform:translateY(-2px);box-shadow:0 8px 20px rgba(0,0,0,.09)}
.btn{transition:transform .15s ease,box-shadow .2s ease}
.btn:active{transform:scale(.95)}
.navbtn{transition:transform .15s ease}
.navbtn:active{transform:scale(.95)}"""),

21: T(bg="#ffffff", ink="#111111", muted="#4a4a4a", line="#111111", accent="#0055d4",
      radius="8px", cardborder="2px solid #111", shadow="none", btnborder="2px solid #111",
      btnradius="8px", ghostborder="2px solid #111", leadfs="17px",
      raw=""".btn,.navbtn{min-height:44px;display:inline-flex;align-items:center;justify-content:center;padding:10px 22px;font-weight:700}
:focus-visible{outline:3px solid #0055d4;outline-offset:2px}
.card .ico{border-radius:50%}
.kicker:after{content:' · 对比度 7:1';color:#0055d4}
.btn.ghost{background:#fff;color:#111}"""),

22: T(bg="#ffffff", surface="transparent", ink="#111111", muted="#8a8a8a", line="#eeeeee",
      accent="#111111", radius="0", cardborder="none", shadow="none", btnradius="999px",
      btnborder="1px solid #cccccc", ghostborder="1px solid #cccccc", layout="center",
      lsh="-.03em", h1w="600", leadfs="17px",
      raw=""".card{border-top:1px solid #eee;border-radius:0;padding:20px 0 0}
.card h3{font-weight:600}
.btn{background:transparent;color:#111}
.btn.ghost{background:#111;color:#fff;border-color:#111}
.nav{border-bottom:1px solid #f2f2f2}
.card .ico{display:none}
h1{font-weight:600}
.cards{display:none}
.askBox{display:flex;align-items:center;gap:10px;width:min(520px,100%);margin:6px auto 0;
  border:1px solid #e6e6e6;border-radius:999px;padding:12px 18px;background:#fff;
  box-shadow:0 8px 30px rgba(0,0,0,.06);color:#8a8a8a;font-size:13.5px}
.askDot{width:7px;height:7px;border-radius:50%;background:#111}
.askPh{flex:1;text-align:left}
.askKey{font-family:var(--font-k);font-size:11px;border:1px solid #eee;border-radius:5px;padding:2px 6px}
.secHead{border-top:1px solid #f2f2f2}"""),

23: T(bg="#eef0f4", surface="#ffffff", ink="#2a2f3a", muted="#6f7787", line="#e4e7ee",
      accent="#6382dc", radius="14px", cardborder="1px solid #e4e7ee",
      shadow="0 2px 12px rgba(40,50,80,.08)", btnradius="12px",
      btnshadow="0 2px 8px rgba(99,130,220,.25)",
      raw=""".card{padding:26px}
.btn{font-weight:600}
.nav{border-bottom:1px solid #e4e7ee}"""),

24: T(bg="#fffaee", surface="#ffffff", ink="#111111", line="#111111", accent="#ff6b6b",
      on_accent="#111111", radius="0", cardborder="3px solid #000", shadow="4px 4px 0 #000",
      btnradius="0", btnshadow="4px 4px 0 #000", btnborder="3px solid #000",
      ghostborder="3px solid #000", lsh="-.03em",
      raw=""".card:nth-child(2){background:#ffd93d}
.card .ico{border-radius:50%}
.btn.ghost{background:#ffd93d;color:#111}
.brand{text-transform:uppercase;letter-spacing:.04em}
h1{font-weight:900}"""),

25: T(bg="#f5f5f7", surface="#ffffff", ink="#1d1d1f", muted="#6e6e73", line="#e8e8ed",
      accent="#0071e3", radius="18px", cardborder="none", shadow="0 1px 3px rgba(0,0,0,.06)",
      btnradius="999px", lsh="-.035em", lhh="1.06",
      raw=""".cards{grid-template-columns:1.6fr 1fr 1fr}
.card{padding:30px}
.card:first-child{background:linear-gradient(140deg,#fff,#eef3ff)}
.card .ico{border-radius:12px}
h1{font-weight:700}
.btn{font-weight:600}"""),

26: T(bg="#d1f7ff", ink="#2b1b3a", muted="#5f5470", line="rgba(255,255,255,.7)",
      accent="#ff69b4", on_accent="#ffffff", surface="rgba(255,255,255,.55)", radius="18px",
      cardborder="1px solid rgba(255,255,255,.85)",
      shadow="0 12px 30px rgba(255,105,180,.28)", btnradius="999px",
      bgimg="background-image:linear-gradient(120deg,#d1f7ff,#e6dcff 45%,#ffccde);",
      raw=""".card,.btn,.navbtn{backdrop-filter:blur(5px);-webkit-backdrop-filter:blur(5px)}
.card{position:relative;overflow:hidden}
.card:before{content:'';position:absolute;inset:0;border-radius:inherit;pointer-events:none;
  background:linear-gradient(140deg,rgba(255,255,255,.65),transparent 45%)}
h1{color:#2b1b3a;text-shadow:0 0 18px rgba(255,255,255,.9);font-weight:800}
.kicker{color:#ff69b4}"""),

27: T(bg="#0a0a0a", surface="#0f0f12", ink="#e9ffe9", muted="#8a9a8a", line="#ff00ff",
      accent="#ff00ff", on_accent="#0a0a0a", radius="0", cardborder="1px solid #ff00ff",
      shadow="0 0 12px rgba(255,0,255,.35)", btnradius="0",
      btnshadow="0 0 14px rgba(255,0,255,.55)", ghostborder="1px solid #00ff88",
      ttk="uppercase", lsk=".2em",
      bgimg="background-image:linear-gradient(rgba(255,0,255,.06) 1px,transparent 1px),linear-gradient(90deg,rgba(0,255,136,.06) 1px,transparent 1px);background-size:40px 40px;",
      raw="""h1{text-shadow:0 0 18px rgba(255,0,255,.65);letter-spacing:.02em;font-weight:700}
.kicker{color:#00ff88;text-shadow:0 0 10px rgba(0,255,136,.7)}
.btn.ghost{color:#00ff88}
.card .ico{background:#00ff88;clip-path:polygon(0 0,100% 0,100% 70%,70% 100%,0 100%)}"""),

28: T(bg="#fafbff", surface="#ffffff", ink="#141826", muted="#666e85", line="#e7e9f7",
      accent="#667eea", radius="12px", cardborder="1px solid #e7e9f7",
      shadow="0 6px 20px rgba(102,126,234,.10)", btnradius="10px",
      btnshadow="0 6px 18px rgba(102,126,234,.28)",
      raw=""".btn,.navbtn{background-image:linear-gradient(135deg,#667eea,#764ba2);border:0}
.card{transition:box-shadow .2s}
.card:hover{box-shadow:0 12px 30px rgba(102,126,234,.2)}
h1{font-weight:800;letter-spacing:-.03em}
.card .ico{border-radius:10px;background:linear-gradient(135deg,#667eea,#764ba2)}
.kicker{color:#667eea}"""),

29: T(bg="#fdf6ec", surface="#ffffff", ink="#111111", muted="#555550", line="#111111",
      accent="#ff6b6b", on_accent="#111111", radius="16px", cardborder="2px solid #111",
      shadow="6px 6px 0 #4ecdc4", btnradius="999px", btnshadow="4px 4px 0 #111",
      btnborder="2px solid #111", ghostborder="2px solid #111",
      bgimg="background-image:radial-gradient(#ffe66d 3px,transparent 3px);background-size:46px 46px;",
      raw=""".card:nth-child(2){background:#ffe66d;box-shadow:6px 6px 0 #111}
.card:nth-child(3){background:#4ecdc4;box-shadow:6px 6px 0 #ff6b6b}
.btn.ghost{background:#ffe66d;color:#111}
h1{font-weight:900}
.card .ico{border-radius:50%;background:#111}"""),

30: T(bg="#1a0033", surface="rgba(60,20,90,.55)", ink="#ffe6ff", muted="#c09ad0",
      line="rgba(232,160,255,.35)", accent="#e8a0ff", on_accent="#1a0033", radius="10px",
      cardborder="1px solid rgba(232,160,255,.4)",
      shadow="0 0 24px rgba(232,160,255,.25)", btnradius="999px",
      bgimg="background-image:linear-gradient(#1a0033,#3d0a5c 55%,#1a0033);",
      raw=""".card,.btn{backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
h1{color:#e8a0ff;text-shadow:2px 0 #00ffff,-2px 0 #ff006e,0 0 30px rgba(232,160,255,.5);font-weight:700}
.kicker{color:#00ffff;letter-spacing:.28em}
.card .ico{background:#00ffff;border-radius:0}"""),

31: T(bg="#f0f0f5", surface="#ffffff", ink="#1a1d24", muted="#5f6675", line="#ececf2",
      accent="#4f5bd5", radius="14px", cardborder="1px solid #ececf2",
      shadow="0 1px 2px rgba(20,25,50,.06),0 4px 10px rgba(20,25,50,.06),0 12px 28px rgba(20,25,50,.08)",
      btnradius="10px", btnshadow="0 4px 12px rgba(79,91,213,.28)",
      raw=""".card{transition:transform .2s,box-shadow .25s}
.card:hover{transform:translateY(-3px);box-shadow:0 2px 4px rgba(20,25,50,.06),0 10px 20px rgba(20,25,50,.08),0 24px 48px rgba(20,25,50,.12)}
.card .ico{border-radius:10px}
.nav{border-bottom:1px solid #e6e6ee}"""),

32: T(bg="#ffffff", surface="#ffffff", ink="#0a0a0a", muted="#8a8a8a", line="#eeeeee",
      accent="#0a0a0a", on_accent="#ffffff", radius="0", cardborder="none", shadow="none",
      h1size="clamp(54px,11vw,164px)", lsh="-.055em", lhh="0.86", h1w="900",
      btnradius="0", btnborder="1px solid #0a0a0a", ghostborder="0",
      raw=""".card{border-top:1px solid #eee;padding:22px 0 0;border-radius:0}
.card h3{font-size:16px}
.card .ico{display:none}
.lead{font-size:15px;max-width:40ch}
.nav{border-bottom:1px solid #eee}
.btn{background:#0a0a0a;font-weight:600}
.btn.ghost{background:transparent;color:#0a0a0a;border:0;padding-left:0}
.kicker{letter-spacing:.22em}
.lead{font-size:16px;max-width:44ch}
.ess blockquote{font-size:26px;line-height:1.45;border-left:0;padding-left:0;margin:30px 0 18px}
.ess p{font-size:15px}
.cards{gap:0}
.card{border-top:1px solid #e8e8e8;padding:20px 26px 0 0}"""),

33: T(bg="#0b0b0b", surface="transparent", ink="#ffffff", muted="#a0a0a0", line="#262626", accent="#ff2d2d",
      on_accent="#ffffff", radius="0", cardborder="0", shadow="none",
      h1size="clamp(50px,9vw,118px)", lhh="0.86", lsh="-.045em", h1w="900", btnradius="0",
      bgimg="", navborder="1px solid #262626",
      raw="""h1{text-transform:uppercase}
.kicker{color:#ff2d2d;letter-spacing:.3em}
.card{border:0;border-left:2px solid #ff2d2d;padding:6px 0 6px 18px}
.card .ico{display:none}
.card h3{font-size:15px;text-transform:uppercase;letter-spacing:.06em}
.btn{border-radius:0;background:#ff2d2d}
.btn.ghost{border:1px solid #333;color:#fff}"""),

34: T(bg="#f6efe3", ink="#3a2f1f", muted="#7a6a52", line="#e0d5c0", accent="#8b6914",
      on_accent="#ffffff", surface="rgba(255,255,255,.72)", radius="14px",
      cardborder="1px solid rgba(255,255,255,.9)",
      shadow="0 12px 30px rgba(120,90,40,.12)", btnradius="8px",
      bgimg="background-image:linear-gradient(180deg,#f6efe3,#e8dcc6 45%,#f6efe3);",
      raw=""".nav{background:#3a2a10;color:#f3e6cf;border-bottom:0;padding:14px 18px;border-radius:10px;margin-top:10px}
.nav nav{color:#e3d3b5}
.nav .brand{color:#f7edda}
.nav .brand i{color:#d9b26a}
.navbtn{background:#8b6914;border-radius:6px}
.card{backdrop-filter:blur(6px);-webkit-backdrop-filter:blur(6px)}
h1{font-weight:600;letter-spacing:-.015em}
.card .ico{border-radius:50%;background:#8b6914}"""),

35: T(bg="#fcfcfc", ink="#0a0a0a", muted="#666660", line="#e6e6e6", accent="#0a0a0a",
      on_accent="#ffffff", radius="0", cardborder="0", shadow="none",
      h1size="clamp(30px,4.2vw,52px)", lhh="1.02", lsh="-.03em", h1w="900",
      btnradius="0", btnborder="2px solid #0a0a0a", ghostborder="2px solid #dddddd",
      raw=""".card{border:0;border-top:2px solid #0a0a0a;padding:18px 0 0;border-radius:0}
.card .ico{display:none}
.card h3{font-size:15px}
.nav{border-bottom:1px solid #0a0a0a}
.btn{background:#0a0a0a;font-weight:700}
.btn.ghost{color:#0a0a0a}
.kicker{letter-spacing:.34em;color:#000}
.lead{max-width:60ch;font-size:14.5px;line-height:1.75}
.cards{grid-template-columns:repeat(3,1fr);gap:0}
.card{border:0;border-top:2px solid #0a0a0a;border-radius:0;padding:14px 22px 0 0}
.card h3{font-size:13px;letter-spacing:.04em;text-transform:uppercase}
.card p{font-size:12px}
.idxRow span{font-size:17px}"""),

36: T(bg="#001020", surface="rgba(0,40,80,.35)", ink="#d6f2ff", muted="#6f9bb5",
      line="rgba(0,170,255,.45)", accent="#00aaff", on_accent="#001020", radius="2px",
      cardborder="1px solid rgba(0,170,255,.45)",
      shadow="0 0 20px rgba(0,170,255,.18),inset 0 0 30px rgba(0,170,255,.06)",
      btnradius="2px", btnshadow="0 0 14px rgba(0,170,255,.45)",
      fonth=MONO, fontb=MONO, ttk="uppercase", lsk=".2em",
      bgimg="background-image:linear-gradient(rgba(0,170,255,.08) 1px,transparent 1px),linear-gradient(90deg,rgba(0,170,255,.08) 1px,transparent 1px);background-size:32px 32px;",
      raw=""".card{position:relative;padding:24px}
.card:before,.card:after{content:'';position:absolute;width:10px;height:10px;border:1px solid #00aaff}
.card:before{left:-1px;top:-1px;border-right:0;border-bottom:0}
.card:after{right:-1px;bottom:-1px;border-left:0;border-top:0}
h1{text-shadow:0 0 20px rgba(0,170,255,.5);font-weight:400;letter-spacing:.02em;font-size:clamp(28px,4.4vw,50px)}
.kicker{color:#00aaff}
.kicker:after{content:' // SYSTEM ONLINE'}
.card h3{font-size:12px;letter-spacing:.16em;text-transform:uppercase}
.card .ico{width:9px;height:9px;border-radius:0;background:#00aaff;box-shadow:0 0 10px #00aaff;margin-bottom:18px}"""),

37: T(bg="#f2f2f7", surface="#ffffff", ink="#111111", muted="#6e6e73", line="#e5e5ea",
      accent="#ff3b30", radius="20px", cardborder="none", shadow="none", btnradius="999px",
      lsh="-.03em",
      raw=""".cards{grid-template-columns:1.5fr 1fr 1fr}
.card{padding:26px}
.card h3{font-size:15px}
.card .ico{border-radius:14px;background:#ff3b30}
h1{font-weight:800}
.btn{font-weight:600}"""),

38: T(bg="#05070f", ink="#eaf0ff", muted="#93a2c4", line="rgba(255,255,255,.12)",
      accent="#7c9cff", on_accent="#05070f", surface="rgba(255,255,255,.06)", radius="22px",
      cardborder="1px solid rgba(255,255,255,.12)", shadow="0 30px 80px rgba(0,0,0,.6)",
      btnradius="999px",
      bgimg="background-image:radial-gradient(60% 50% at 28% 0%,rgba(70,100,255,.3),transparent),radial-gradient(50% 50% at 82% 60%,rgba(160,80,255,.22),transparent);background-attachment:fixed;",
      raw=""".card,.navbtn,.btn{backdrop-filter:blur(20px);-webkit-backdrop-filter:blur(20px)}
.card{box-shadow:0 30px 80px rgba(0,0,0,.5),inset 0 1px 0 rgba(255,255,255,.16)}
h1{font-weight:600;letter-spacing:-.03em}
.kicker{color:#7c9cff;letter-spacing:.26em}"""),

39: T(bg="#faf8f0", surface="#fffdf7", ink="#2a2a26", muted="#6b6b60", line="#ddd8c8",
      accent="#2a2a26", on_accent="#faf8f0", radius="2px", cardborder="0", shadow="none",
      fonth=SERIF, fontb=SERIF, lhh="1.8", lsh="0", h1w="400", btnradius="2px",
      btnborder="1px solid #2a2a26", ghostborder="1px solid #c8c2b0", navborder="1px solid #ddd8c8",
      raw="""h1{font-size:clamp(28px,4vw,44px);line-height:1.4}
.lead{font-size:16px;line-height:1.9}
.card{padding:20px 0;border:0;border-bottom:1px solid #ddd8c8;border-radius:0}
.card .ico{display:none}
.card h3{font-size:16px;font-weight:400}
.cards{border-top:1px solid #ddd8c8;padding-top:8px}
.btn{background:#2a2a26;font-weight:400}
.btn.ghost{color:#2a2a26;background:transparent}
.kicker{letter-spacing:.16em}"""),

40: T(bg="#0f0f0f", surface="#ff5a1f", ink="#111111", muted="#3a3a3a", line="#000000",
      accent="#ffe600", on_accent="#0f0f0f", radius="18px", cardborder="2px solid #000",
      shadow="4px 4px 0 #000", btnradius="999px", btnshadow="4px 4px 0 #000",
      btnborder="2px solid #000", ghostborder="2px solid #ffffff",
      lsh="-.03em", ttk="uppercase", lsk=".2em",
      raw="""h1{color:#ffe600;font-weight:900}
.brand{color:#fff}
.nav nav a{color:#fff}
.card:nth-child(2){background:#ffe600}
.card:nth-child(3){background:#ffffff}
.card h3{color:#111;font-weight:800}
.card p{color:#222}
.btn.ghost{color:#fff}
.card .ico{background:#111;border-radius:6px}
.nav{border-bottom:2px solid #fff;padding-bottom:12px}"""),

41: T(bg="#c9d6c0", surface="rgba(255,255,255,.5)", ink="#1e2a1e", muted="#4d5c4a",
      line="rgba(30,42,30,.12)", accent="#2a4a2a", on_accent="#ffffff", radius="20px",
      cardborder="1px solid rgba(255,255,255,.6)",
      shadow="0 14px 40px rgba(30,50,30,.12)", btnradius="14px",
      bgimg="background-image:linear-gradient(180deg,#dfe8da,#93a58c);",
      raw=""".card{backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.nav{background:#2a4a2a;color:#e9f0e4;border-bottom:0;border-radius:14px;padding:14px 18px;margin-top:10px}
.nav nav{color:#cdddc6}
.nav .brand{color:#f0f6ec}
.nav .brand i{color:#b7d4a8}
.navbtn{background:#b7d4a8;color:#1e2a1e}
h1{font-weight:600;letter-spacing:-.02em}
.card .ico{border-radius:50%;background:#6f8f62}"""),

42: T(bg="#ffffff", ink="#111111", muted="#666660", line="#999999", accent="#111111",
      on_accent="#ffffff", radius="0", cardborder="1px dashed #999999", shadow="none",
      btnradius="0", btnborder="1px solid #111111", ghostborder="1px dashed #999999",
      fontb=MONO, fonth=MONO, lsh="0", lhh="1.15", h1w="700",
      h1size="clamp(30px,4.8vw,56px)",
      raw=""".nav{border-bottom:1px dashed #ccc}
.card{padding:20px}
.btn.ghost{background:#fff;color:#111}
.lead{font-size:14px;line-height:1.75}
.kicker{color:#666;letter-spacing:.1em}
.card .ico{display:none}
.card h3{font-size:13px;text-transform:uppercase;letter-spacing:.06em}"""),

43: T(bg="#f8f5f0", surface="#fffdf9", ink="#3a322a", muted="#7a6f62", line="#e6dfd2",
      accent="#6b4a2f", on_accent="#ffffff", radius="12px", cardborder="1px solid #e6dfd2",
      shadow="0 1px 0 rgba(0,0,0,.04),0 3px 0 #e8e2d8", btnradius="10px",
      btnshadow="0 3px 0 #d9cbb8",
      raw=""".btn{transition:transform .12s}
.btn:active{transform:scale(.98);box-shadow:0 1px 0 #d9cbb8}
.card{transition:transform .15s,box-shadow .15s}
.card:hover{transform:translateY(-1px);box-shadow:0 1px 0 rgba(0,0,0,.04),0 5px 0 #e8e2d8}
.card .ico{border-radius:8px}
h1{font-weight:700;letter-spacing:-.02em}"""),

44: T(bg="#f5f2eb", surface="#fffdf8", ink="#2d332a", muted="#6f7566", line="#e7e2d6",
      accent="#5a6a4a", on_accent="#ffffff", radius="10px", cardborder="1px solid #ece7db",
      shadow="0 1px 2px rgba(60,70,50,.04)", btnradius="8px", navborder="none",
      raw=""".nav{background:#5a6a4a;color:#f2f0e8;padding:14px 18px;border-radius:8px;margin-top:10px}
.nav nav{color:#e2e5d8}
.nav .brand{color:#f7f6f0}
.nav .brand i{color:#c8d3b8}
.navbtn{background:#c8d3b8;color:#2d332a}
.card{padding:24px}
.card .ico{border-radius:6px}
h1{font-weight:600;letter-spacing:-.015em}"""),

45: T(bg="#1a1a2e", ink="#e6e6ff", muted="#9a9ac0", line="rgba(255,255,255,.14)",
      accent="#7b61ff", on_accent="#ffffff", surface="rgba(255,255,255,.05)", radius="14px",
      cardborder="1px solid rgba(255,255,255,.12)",
      shadow="0 0 24px rgba(123,97,255,.22)", btnradius="10px",
      btnshadow="0 0 18px rgba(123,97,255,.45)",
      raw=""".card{transition:.3s}
.card:hover{border-color:#7b61ff;box-shadow:0 0 30px rgba(123,97,255,.4)}
.card .ico{border-radius:50%;background:#7b61ff}
a{cursor:crosshair}
.kicker{color:#7b61ff;letter-spacing:.24em}
h1{font-weight:700;letter-spacing:-.02em}"""),

46: T(bg="#0a0a1a", surface="rgba(255,255,255,.045)", ink="#ccd0ee", muted="#7a80a8",
      line="rgba(140,150,255,.18)", accent="#6d7cff", on_accent="#ffffff", radius="16px",
      cardborder="1px solid rgba(140,150,255,.16)",
      shadow="0 0 40px rgba(109,124,255,.18)", btnradius="999px", layout="center",
      deco='<div class="orb"></div>',
      raw=""".orb{width:110px;height:110px;border-radius:50%;margin:14px auto 0;
  background:radial-gradient(circle at 38% 32%,#aab4ff,#3a45b0);
  box-shadow:0 0 60px rgba(109,124,255,.55);animation:breath 3.4s ease-in-out infinite}
@keyframes breath{50%{transform:scale(1.08);box-shadow:0 0 90px rgba(109,124,255,.8)}}
.kicker{color:#8b95ff;letter-spacing:.26em}
h1{font-weight:500;letter-spacing:-.02em}
.card{text-align:left}
.card .ico{display:none}"""),

47: T(bg="#fafafa", ink="#111111", muted="#6b6b6b", line="#ececec", accent="#111111",
      on_accent="#ffffff", radius="14px", cardborder="none", shadow="none",
      btnradius="999px", btnborder="1px solid #111111", ghostborder="1px solid #e0e0e0",
      layout="split", lsh="-.04em", h1w="800",
      deco='<div class="art"><img class="prodShot" src="../assets/img2.jpg" alt="产品图"></div>',
      raw=""".art{display:grid;place-items:center;min-height:360px}
.prodShot{width:100%;max-width:420px;aspect-ratio:4/3;object-fit:cover;border-radius:18px;
  box-shadow:0 30px 70px rgba(0,0,0,.18),0 2px 8px rgba(0,0,0,.06);filter:none}
.art{display:grid;place-items:center}
.card .ico{display:none}
.card{border-top:1px solid #eee;padding:22px 0 0;border-radius:0}
.cards{gap:36px}
.btn{font-weight:600}
.kicker{letter-spacing:.22em}
.lead{font-size:16px;max-width:44ch}
.ess blockquote{font-size:26px;line-height:1.45;border-left:0;padding-left:0;margin:30px 0 18px}
.ess p{font-size:15px}
.cards{gap:0}
.card{border-top:1px solid #e8e8e8;padding:20px 26px 0 0}"""),

48: T(bg="#0a0616", ink="#f6efff", muted="#a99cc4", line="rgba(255,255,255,.12)",
      accent="#ff7ab6", on_accent="#0a0616", surface="rgba(255,255,255,.04)", radius="16px",
      cardborder="1px solid rgba(255,255,255,.10)", shadow="0 24px 60px rgba(0,0,0,.5)",
      btnradius="999px",
      bgimg="background-image:radial-gradient(45% 45% at 10% 10%,rgba(255,122,182,.45),transparent),radial-gradient(40% 40% at 90% 16%,rgba(90,200,255,.35),transparent),radial-gradient(50% 50% at 62% 92%,rgba(140,90,255,.4),transparent);background-attachment:fixed;",
      raw=""".card,.btn{backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
.card{border-color:rgba(255,255,255,.16)}
.card .ico{border-radius:50%;background:linear-gradient(140deg,#ff7ab6,#8c5aff)}
h1{font-weight:700;letter-spacing:-.03em}
.kicker{color:#ff7ab6}"""),

49: T(bg="#000000", surface="#0c0c0c", ink="#f2f2f2", muted="#8a8a8a", line="#333333", accent="#ff0044",
      on_accent="#ffffff", radius="0", cardborder="1px solid #333333",
      shadow="2px 0 0 rgba(255,0,68,.7),-2px 0 0 rgba(0,229,255,.7)",
      fontb=MONO, fonth=MONO, btnradius="0", ghostborder="1px solid #444444",
      bgimg="", navborder="1px solid #222",
      raw="""h1{text-shadow:2px 0 #ff0044,-2px 0 #00e5ff;font-weight:700;letter-spacing:-.01em}
.kicker{color:#00e5ff;letter-spacing:.22em}
.btn{box-shadow:2px 0 0 #00e5ff,-2px 0 0 #ff0044;transition:box-shadow .15s}
.btn:hover{box-shadow:4px 0 0 #00e5ff,-4px 0 0 #ff0044}
.card .ico{display:none}
.card h3{font-size:13px;text-transform:uppercase;letter-spacing:.1em}"""),

50: T(bg="#f5e8d0", surface="#faf0dd", ink="#3a2a10", muted="#8a7550", line="#e3d2b0",
      accent="#8b6914", on_accent="#f7efd9", radius="4px", cardborder="1px solid #e8d8b4",
      shadow="0 1px 3px rgba(80,60,20,.10)", btnradius="4px",
      fonth=SERIF, fontb=SERIF,
      raw="""body:after{content:'';position:fixed;inset:0;pointer-events:none;opacity:.55;
  background-image:radial-gradient(rgba(90,70,30,.18) .5px,transparent .5px);background-size:3px 3px;mix-blend-mode:multiply}
.nav{background:#3a2a10;color:#f0e2c4;padding:14px 18px;border-radius:4px;margin-top:10px;border-bottom:0}
.nav nav{color:#e0cda6}
.nav .brand{color:#f7edda}
.nav .brand i{color:#c9a24a}
.navbtn{background:#8b6914;border-radius:3px}
h1{font-weight:400;letter-spacing:-.01em;line-height:1.24}
.lead{line-height:1.8;font-size:16px}
.card .ico{display:none}
.card h3{font-weight:400;font-size:17px}
.card{padding:22px}"""),
}
