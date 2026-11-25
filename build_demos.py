# -*- coding: utf-8 -*-
"""为每种风格各生成一个「完整」demo 页（7 段结构 + 风格专属模块）+ 一个 50 宫格视觉预览页。

v2：不再是「品牌栏 + Hero + 3 卡」的一屏骨架，而是
    导航 → Hero → 组件区（按钮/输入/开关/徽章/进度）→ 标志性模块 → 内容模块 → 页脚
"""
import json, os, html as H
from string import Template
from themes import THEMES, SLUGS
import build_components as BC
from build_bundle import ANTI as ANTI_TXT

OUT = os.path.dirname(os.path.abspath(__file__))
DEMOS = os.path.join(OUT, "demos")
os.makedirs(DEMOS, exist_ok=True)

STYLES = json.load(open(os.path.join(OUT, "styles.json"), encoding="utf-8"))
BY_ID = {s["id"]: s for s in STYLES}

# ============================================================
# 模块 HTML
# ============================================================
def _head(title, sub):
    return (f'<div class="secHead"><h2>{title}</h2><p>{sub}</p></div>')


def m_marquee():
    txt = "GRID / TYPE / SHADOW / MOTION / "
    return f'''<section class="sec secFull">
<div class="mq">
  <div class="mqRow"><span>{txt*3}</span><span>{txt*3}</span></div>
  <div class="mqRow rev"><span>{txt*2}2026 / {txt}</span><span>{txt*2}2026 / {txt}</span></div>
</div>
</section>'''


def m_index():
    rows = [("01", "品牌系统", "Identity", "2026"), ("02", "组件库", "Design System", "2026"),
            ("03", "官网改版", "Web", "2025"), ("04", "数据看板", "Analytics", "2025"),
            ("05", "移动端", "App", "2024")]
    body = "".join(
        f'<a class="idxRow" href="#"><b>{n}</b><span>{t}<i>{e}</i></span><em>{y}</em></a>'
        for n, t, e, y in rows)
    return f'''<section class="sec">
{_head("项目索引", "INDEX / 2026.11")}
<div class="idx">{body}</div>
</section>'''


def m_codewin():
    return f'''<section class="sec">
{_head("构建日志", "BUILD / 实时")}
<div class="cw">
  <div class="cwBar"><i></i><i></i><i></i><em>build.log — arc-studio</em></div>
<pre><span class="p">$</span> pnpm build --mode=prod
<span class="ok">✓</span> 2041 modules transformed
<span class="ok">✓</span> tokens generated · 50 themes
<span class="w">!</span> warning: 2 unused vars
<span class="ok">✓</span> built in <b>1.28s</b> · ready
<span class="p">$</span> <span class="cur">▍</span></pre>
</div>
</section>'''


def m_inventory():
    slots = "".join(f'<span class="slot s{i}"></span>' for i in range(1, 10))
    return f'''<section class="sec">
{_head("物品栏", "INVENTORY / 9 SLOTS")}
<div class="inv">
  <div class="invGrid">{slots}</div>
  <div class="invSide">
    <div class="hp"><span>HP</span><div class="hpBar"><i style="width:70%"></i></div><em>14/20</em></div>
    <div class="hp"><span>XP</span><div class="hpBar xp"><i style="width:42%"></i></div><em>420/1000</em></div>
    <div class="invLog"><span>▸ 已装备：橡木剑</span><span>▸ 获得：草方块 ×12</span><span>▸ 合成：石镐（3 木 / 2 石）</span></div>
  </div>
</div>
</section>'''


def m_win95():
    return f'''<section class="sec">
{_head("窗口与任务栏", "WINDOW / TASKBAR")}
<div class="w95">
  <div class="w95Win">
    <div class="w95Title"><span>ARC — 项目属性</span><span class="w95Btns"><i>_</i><i>□</i><i>×</i></span></div>
    <div class="w95Menu"><span>文件</span><span>编辑</span><span>查看</span><span>帮助</span></div>
    <div class="w95Body">
      <p class="w95Lab">项目名称：</p>
      <div class="w95Field"><input value="arc-studio" readonly></div>
      <p class="w95Lab">选项：</p>
      <label class="w95Chk"><span class="w95Box">✓</span>启用网格对齐</label>
      <label class="w95Chk"><span class="w95Box">✓</span>显示隐藏文件</label>
      <label class="w95Chk"><span class="w95Box"></span>兼容模式（Windows 95）</label>
      <div class="w95Actions"><button class="w95Btn">确定</button><button class="w95Btn">取消</button></div>
    </div>
  </div>
  <div class="w95Task">
    <button class="w95Start">⊞ 开始</button>
    <div class="w95Tasks"><span>ARC 工作室</span><span>build.log</span></div>
    <span class="w95Clock">18:07</span>
  </div>
</div>
</section>'''


def m_radar():
    blips = "".join(
        f'<i class="blip" style="left:{x}%;top:{y}%;animation-delay:{d}s"></i>'
        for x, y, d in [(28, 32, 0), (62, 22, .4), (48, 66, .8), (74, 58, 1.2)])
    return f'''<section class="sec">
{_head("监测面板", "RADAR / 实时信号")}
<div class="radarWrap">
  <div class="radar"><span class="r1"></span><span class="r2"></span><span class="r3"></span>
    <span class="sweep"></span>{blips}</div>
  <ul class="dataList">
    <li><b>SYS</b><span>运行正常</span><em>99.98%</em></li>
    <li><b>LAT</b><span>平均延迟</span><em>28ms</em></li>
    <li><b>REQ</b><span>今日请求</span><em>1.24M</em></li>
    <li><b>ERR</b><span>错误率</span><em>0.02%</em></li>
  </ul>
</div>
</section>'''


def m_sticker():
    return f'''<section class="sec">
{_head("装饰与贴纸", "SHAPES / STICKERS")}
<div class="stk">
  <span class="sh ball"></span><span class="sh star">★</span><span class="sh ring"></span>
  <span class="sh zig">~~~~</span><span class="sh dots"></span><span class="sh pill">NEW</span>
</div>
</section>'''


def m_glassstack():
    return f'''<section class="sec">
{_head("层次与玻璃", "LAYERS / BLUR")}
<div class="gls">
  <div class="glsCard c3"><span class="lab">BACKGROUND</span><p>背景层：渐变光斑 + 模糊 20px</p></div>
  <div class="glsCard c2"><span class="lab">MIDDLE</span><p>中间层：半透明卡片，1px 高光描边</p></div>
  <div class="glsCard c1"><span class="lab">FOREGROUND</span><p>前景层：内容与操作</p>
    <div class="row"><span class="badge">Glass</span><span class="badge soft">blur 16px</span></div>
  </div>
</div>
</section>'''


def m_gallery(bento=False):
    cls = "gal galB" if bento else "gal"
    caps = ["Brand", "Editorial", "Product", "Interface", "Motion", "Print"]
    items = "".join(
        f'<figure class="galItem"><span class="ph" style="background-image:url(../assets/img{i}.jpg)"></span>'
        f'<figcaption>{c}</figcaption></figure>'
        for i, c in enumerate(caps, start=1))
    return f'''<section class="sec">
{_head("作品网格", "GALLERY / 6")}
<div class="{cls}">{items}</div>
</section>'''


def m_table():
    rows = [("官网改版", "李", 82, "进行中"), ("组件库", "王", 100, "已完成"),
            ("数据看板", "陈", 46, "进行中"), ("移动端", "赵", 12, "待开始"),
            ("品牌手册", "周", 68, "进行中")]
    body = "".join(
        f'<tr><td>{n}</td><td>{o}</td><td class="r">{p}%</td>'
        f'<td><span class="badge {"soft" if s!="已完成" else ""}">{s}</span></td></tr>'
        for n, o, p, s in rows)
    return f'''<section class="sec">
{_head("数据表格", "TABLE / 5 ROWS")}
<div class="panel">
<table class="tbl">
  <thead><tr><th>项目</th><th>负责人</th><th class="r">进度</th><th>状态</th></tr></thead>
  <tbody>{body}</tbody>
</table>
</div>
</section>'''


def m_chart():
    hs = [42, 68, 55, 88, 61, 74, 96, 58]
    bars = "".join(f'<i style="height:{h}%"></i>' for h in hs)
    return f'''<section class="sec">
{_head("数据可视化", "CHART / 纯 CSS")}
<div class="panel chPanel">
  <div class="chTop"><div><b>12,480</b><span>本月构建次数</span></div>
    <div class="chLeg"><i></i>构建 <i class="g2"></i>失败</div></div>
  <div class="ch"><div class="chBars">{bars}</div>
    <div class="chAxis"><span>周一</span><span>周二</span><span>周三</span><span>周四</span>
      <span>周五</span><span>周六</span><span>周日</span><span>合计</span></div>
  </div>
</div>
</section>'''


def m_essay():
    return f'''<section class="sec">
{_head("正文排版", "EDITORIAL / READING")}
<div class="ess">
  <p class="dcap">好的界面不该让人意识到界面的存在。它把注意力让给内容，把节奏交给留白，把重量交给字重与字号——剩下的，全都交给读者自己。</p>
  <p>这套设计语言只做了三件事：定下一条基线，选好两组字，留够呼吸空间。没有多余的阴影，没有讨好的渐变，也没有为了显得高级而堆叠的装饰。</p>
  <blockquote>「少不是空，是把话说完整。」</blockquote>
  <p>当字号、行高、字距被认真对待时，一张页面不需要任何特效就已经足够耐看。</p>
</div>
</section>'''


def m_form():
    return f'''<section class="sec">
{_head("表单控件", "FORM / A11Y")}
<div class="panel frm">
  <label class="fl" for="f1">项目名称</label>
  <input class="inp" id="f1" placeholder="例如：arc-studio">
  <label class="fl" for="f2">团队邮箱</label>
  <input class="inp" id="f2" value="team@arc.studio">
  <p class="help">我们会用它发送构建通知，不会用于营销。</p>
  <div class="row"><span class="badge">已校验</span><span class="badge soft">必填 2 项</span></div>
  <a class="btn" href="#">保存设置</a>
</div>
</section>'''


def m_stats():
    data = [("128", "组件"), ("50", "套主题"), ("1.28s", "构建耗时"), ("99.98", "可用性")]
    cells = "".join(f'<div class="sttCell"><b>{n}</b><span>{l}</span></div>' for n, l in data)
    return f'''<section class="sec">
{_head("关键指标", "STATS / 4")}
<div class="stt">{cells}</div>
</section>'''


def m_strip(sid):
    idx = [(sid + i) % 12 + 1 for i in range(4)]
    items = "".join(
        f'<figure><span class="ph" style="background-image:url(../assets/img{n}.jpg)"></span></figure>'
        for n in idx)
    return f'''<section class="sec">
{_head("影像", "SELECTED WORK / 4")}
<div class="strip">{items}</div>
</section>'''


MODS = dict(marquee=m_marquee, index=m_index, codewin=m_codewin, inventory=m_inventory,
            win95=m_win95, radar=m_radar, sticker=m_sticker, glassstack=m_glassstack,
            gallery=m_gallery, table=m_table, chart=m_chart, essay=m_essay,
            form=m_form, stats=m_stats)

# 每种风格：标志性模块 + 内容模块
SIG = {
    1: "marquee", 2: "index", 3: "essay", 4: "codewin", 5: "glassstack", 6: "inventory",
    7: "form", 8: "win95", 9: "gallery", 10: "stats", 11: "marquee", 12: "table",
    13: "form", 14: "stats", 15: "glassstack", 16: "stats", 17: "gallery", 18: "glassstack",
    19: "marquee", 20: "form", 21: "form", 22: "essay", 23: "table", 24: "marquee",
    25: "gallery", 26: "sticker", 27: "codewin", 28: "chart", 29: "sticker", 30: "sticker",
    31: "table", 32: "index", 33: "marquee", 34: "gallery", 35: "index", 36: "radar",
    37: "gallery", 38: "glassstack", 39: "essay", 40: "sticker", 41: "gallery",
    42: "essay", 43: "form", 44: "gallery", 45: "radar", 46: "radar", 47: "gallery",
    48: "glassstack", 49: "codewin", 50: "gallery",
}
CON = {
    1: "table", 2: "essay", 3: "gallery", 4: "table", 5: "gallery", 6: "stats",
    7: "stats", 8: "table", 9: "essay", 10: "chart", 11: "stats", 12: "chart",
    13: "essay", 14: "gallery", 15: "chart", 16: "gallery", 17: "stats", 18: "chart",
    19: "gallery", 20: "stats", 21: "essay", 22: "stats", 23: "chart", 24: "stats",
    25: "stats", 26: "stats", 27: "chart", 28: "table", 29: "gallery", 30: "marquee",
    31: "chart", 32: "essay", 33: "essay", 34: "essay", 35: "table", 36: "codewin",
    37: "stats", 38: "chart", 39: "index", 40: "marquee", 41: "essay", 42: "index",
    43: "gallery", 44: "stats", 45: "gallery", 46: "essay", 47: "stats", 48: "chart",
    49: "chart", 50: "essay",
}

# 个别风格的组件微调
XRAW = {
    1: """.inp,.panel{border-width:3px}
.inp{box-shadow:4px 4px 0 #111}
.tbl th{border-bottom:2px solid #111}
.sttCell{border:3px solid #111;box-shadow:4px 4px 0 #111;background:#fff}""",
    6: """.inp{border-radius:0}
.sttCell{border:3px solid #0e140b}""",
    8: """.inp{border:2px solid;border-color:#808080 #fff #fff #808080;background:#fff;border-radius:0}
.panel{background:#c0c0c0;border:2px solid;border-color:#fff #808080 #808080 #fff}
.tbl th,.tbl td{border-bottom:1px solid #808080}
.badge{border:2px solid;border-color:#fff #808080 #808080 #fff;background:#c0c0c0;color:#000;border-radius:0}
.foot,.foot a,.foot p,.foot li,.footBottom{color:#eaf6f6}
.foot h4{color:#bfe3e3}
.lead,.kicker,.secHead p{color:#073b3b}""",
    12: """.inp{background:#0a0a0a}""",
    22: """.inp{border:1px solid #eaeaea;background:#fff;border-radius:999px;padding:11px 18px}
.panel{border:0;border-top:1px solid #eee;border-radius:0;padding:20px 0}""",
    32: """.panel{border:0;border-top:1px solid #eee;border-radius:0;padding:22px 0}
.sttCell{border-top:1px solid #eee;border-radius:0}""",
    39: """.panel{border:0;border-top:1px solid #ddd8c8;border-radius:0}
.sttCell{border-left:1px solid #ddd8c8}""",
    42: """.panel{border-style:dashed}
.inp{border:1px dashed #999;border-radius:0}""",
}

# ============================================================
# 模板
# ============================================================
MODCSS = """
/* ---------- 段落 ---------- */
.sec{padding:0 0 64px}
.secFull{padding:0 0 56px}
.secHead{display:flex;align-items:baseline;gap:14px;flex-wrap:wrap;margin:0 0 18px;
  border-top:var(--nav-border);padding-top:18px}
.secHead h2{margin:0;font-family:var(--font-h);font-size:19px;font-weight:var(--h1-w);letter-spacing:-.01em}
.secHead p{margin:0;font-size:12px;color:var(--muted);font-family:var(--font-k);letter-spacing:.06em}
.panel{background:var(--surface);border:var(--card-border);border-radius:var(--radius);
  padding:22px;box-shadow:var(--shadow)}
.lab{display:block;font-family:var(--font-k);font-size:10px;letter-spacing:.16em;
  text-transform:uppercase;color:var(--muted);margin-bottom:12px}
.row{display:flex;gap:10px;align-items:center;flex-wrap:wrap}
.tiny{font-size:11.5px}
/* ---------- 组件区 ---------- */
.compGrid{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--card-gap,16px)}
.inp{width:100%;padding:10px 14px;font-family:inherit;font-size:13.5px;color:var(--ink);
  background:var(--bg);border:1px solid var(--line);border-radius:var(--btn-radius);outline:none}
.inp::placeholder{color:var(--muted);opacity:.75}
.inp:focus{border-color:var(--accent)}
:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.btn.dis{opacity:.42;pointer-events:none}
.badge{display:inline-block;font-family:var(--font-k);font-size:10.5px;letter-spacing:.06em;
  padding:3px 9px;border-radius:999px;background:var(--accent);color:var(--on-accent)}
.badge.soft{background:transparent;color:var(--muted);border:1px solid var(--line)}
.sw{width:40px;height:22px;border-radius:999px;background:var(--line);position:relative;
  display:inline-block;flex:0 0 auto}
.sw i{position:absolute;top:3px;left:3px;width:16px;height:16px;border-radius:50%;background:var(--bg)}
.sw.on{background:var(--accent)}
.sw.on i{left:21px;background:var(--on-accent)}
.prog{height:8px;border-radius:999px;background:var(--line);overflow:hidden;margin-top:14px}
.prog i{display:block;height:100%;background:var(--accent)}
/* ---------- 表格 ---------- */
.tbl{width:100%;border-collapse:collapse;font-size:13px}
.tbl th{font-family:var(--font-k);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);font-weight:500}
.tbl td{padding:11px 10px;border-bottom:1px solid var(--line)}
.tbl tr:last-child td{border-bottom:0}
.tbl .r{text-align:right;font-family:var(--font-k);font-size:12.5px}
/* ---------- 图表 ---------- */
.chTop{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:22px;gap:16px}
.chTop b{display:block;font-family:var(--font-h);font-size:30px;line-height:1;letter-spacing:-.02em}
.chTop span{font-size:12px;color:var(--muted)}
.chLeg{display:flex;gap:12px;align-items:center;font-size:11.5px;color:var(--muted);font-family:var(--font-k)}
.chLeg i{width:9px;height:9px;border-radius:2px;background:var(--accent);display:inline-block;margin-right:5px}
.chLeg i.g2{background:var(--line)}
.ch{height:170px;display:flex;flex-direction:column;justify-content:flex-end}
.chBars{display:flex;align-items:flex-end;gap:8px;height:150px;
  border-bottom:1px solid var(--line);padding-bottom:0}
.chBars i{flex:1;background:var(--accent);border-radius:3px 3px 0 0;opacity:.9}
.chBars i:nth-child(2n){opacity:.55}
.chAxis{display:flex;justify-content:space-between;font-family:var(--font-k);font-size:10px;
  color:var(--muted);padding-top:8px}
/* ---------- 作品网格 ---------- */
.gal{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.galItem{margin:0}
.ph{display:block;position:relative;aspect-ratio:4/3;overflow:hidden;
  border-radius:calc(var(--radius) * .7);background-size:cover;background-position:center;
  background-color:var(--line);filter:var(--imgf,none);transition:transform .4s cubic-bezier(.2,.8,.3,1)}
.galItem:hover .ph,.strip figure:hover .ph{transform:scale(1.025)}
.ph:after{content:'';position:absolute;inset:0;background:var(--accent);
  mix-blend-mode:color;opacity:var(--duo,0)}
.galB{grid-template-columns:repeat(4,1fr);grid-auto-rows:168px;grid-auto-flow:dense}
.galB .galItem{display:grid;grid-template-rows:1fr auto}
.galB .ph{aspect-ratio:auto;height:100%}
.galB .galItem:nth-child(1){grid-column:span 2;grid-row:span 2}
.galB .galItem:nth-child(6){grid-column:span 4}
.galItem figcaption{margin-top:8px;font-family:var(--font-k);font-size:10.5px;
  letter-spacing:.12em;text-transform:uppercase;color:var(--muted)}
/* ---------- 影像带 ---------- */
.strip{display:grid;grid-template-columns:repeat(4,1fr);gap:10px}
.strip figure{margin:0;overflow:hidden;border-radius:calc(var(--radius) * .7)}
.strip .ph{aspect-ratio:1}
/* ---------- 指标 ---------- */
.stt{display:grid;grid-template-columns:repeat(4,1fr);gap:var(--card-gap,16px)}
.sttCell{background:var(--surface);border:var(--card-border);border-radius:var(--radius);
  padding:22px 20px;box-shadow:var(--shadow)}
.sttCell b{display:block;font-family:var(--font-h);font-size:clamp(28px,3.4vw,40px);
  line-height:1;letter-spacing:-.03em;font-weight:var(--h1-w)}
.sttCell span{display:block;margin-top:8px;font-size:12px;color:var(--muted)}
/* ---------- 正文 ---------- */
.ess{max-width:66ch}
.ess p{margin:0 0 16px;font-size:15.5px;line-height:1.85;color:var(--ink)}
.ess p.dcap{font-size:16.5px}
.ess p.dcap:first-letter{float:left;font-family:var(--font-h);font-size:3.1em;line-height:.88;
  padding:4px 10px 0 0;font-weight:var(--h1-w);color:var(--accent)}
.ess blockquote{margin:22px 0;padding:4px 0 4px 18px;border-left:3px solid var(--accent);
  font-family:var(--font-h);font-size:18px;line-height:1.6;color:var(--ink);font-style:normal}
/* ---------- 表单 ---------- */
.frm{display:grid;gap:8px;max-width:520px}
.fl{font-size:12.5px;color:var(--muted);font-family:var(--font-k);letter-spacing:.06em;margin-top:6px}
.help{margin:2px 0 8px;font-size:12px;color:var(--muted)}
/* ---------- 跑马灯 ---------- */
.secFull .mq{overflow:hidden;background:var(--ink);color:var(--bg);padding:14px 0 10px;
  margin:0 0 0;border-radius:var(--radius)}
.mqRow{display:flex;white-space:nowrap;animation:mv 26s linear infinite;will-change:transform}
.mqRow span{font-family:var(--font-h);font-size:clamp(22px,3vw,34px);font-weight:var(--h1-w);
  letter-spacing:.02em;padding-right:40px;line-height:1.15}
.mqRow.rev{font-size:.6em;opacity:.55;animation-direction:reverse;animation-duration:34s;
  border-top:1px solid currentColor;margin-top:8px;padding-top:8px}
@keyframes mv{to{transform:translateX(-50%)}}
/* ---------- 索引 ---------- */
.idx{border-top:1px solid var(--line)}
.idxRow{display:flex;align-items:baseline;gap:18px;padding:16px 4px;border-bottom:1px solid var(--line);
  color:inherit;text-decoration:none;transition:.18s}
.idxRow:hover{padding-left:12px}
.idxRow b{font-family:var(--font-k);font-size:12px;color:var(--muted);font-weight:500;min-width:26px}
.idxRow span{font-family:var(--font-h);font-size:20px;font-weight:600;letter-spacing:-.02em;flex:1}
.idxRow span i{font-style:normal;font-family:var(--font-k);font-size:10.5px;letter-spacing:.14em;
  text-transform:uppercase;color:var(--muted);margin-left:12px}
.idxRow em{font-style:normal;font-family:var(--font-k);font-size:11.5px;color:var(--muted)}
/* ---------- 代码窗 ---------- */
.cw{background:#0d0f0e;border:1px solid #242b22;border-radius:10px;overflow:hidden;
  box-shadow:0 24px 60px rgba(0,0,0,.35)}
.cwBar{display:flex;gap:6px;align-items:center;padding:10px 12px;background:#151a18;
  border-bottom:1px solid #242b22}
.cwBar i{width:9px;height:9px;border-radius:50%;background:#39463f}
.cwBar i:first-child{background:#ff5f57}.cwBar i:nth-child(2){background:#febc2e}
.cwBar i:nth-child(3){background:#28c840}
.cwBar em{font-style:normal;font-family:var(--font-k);font-size:11px;color:#7f8b7d;margin-left:8px}
.cw pre{margin:0;padding:18px 20px;font-family:var(--font-k);font-size:12.5px;line-height:2;
  color:#c5d0c0;overflow:auto}
.cw .p{color:var(--accent)}
.cw .ok{color:#8ee06a}.cw .w{color:#febc2e}
.cw b{color:#fff;font-weight:600}
.cw .cur{animation:blink 1.1s steps(2) infinite}
@keyframes blink{50%{opacity:0}}
/* ---------- 物品栏 ---------- */
.inv{display:grid;grid-template-columns:1fr 1fr;gap:24px;align-items:start}
.invGrid{display:grid;grid-template-columns:repeat(3,74px);gap:10px}
.slot{width:74px;height:74px;background:#2c3a24;border:3px solid #0e140b;
  box-shadow:inset 0 -6px 0 rgba(0,0,0,.35),inset 0 4px 0 rgba(255,255,255,.07)}
.slot:nth-child(1){background:#7B8F3A}.slot:nth-child(2){background:#8B6B3D}
.slot:nth-child(3){background:#6D6D6D}.slot:nth-child(4){background:#C4A87C}
.slot:nth-child(5){background:#4a5d3a}
.invSide{display:grid;gap:14px}
.hp{display:flex;align-items:center;gap:10px;font-family:var(--font-k);font-size:11.5px;color:#c7d3a8}
.hpBar{flex:1;height:12px;background:#0e140b;border:2px solid #0e140b;position:relative}
.hpBar i{display:block;height:100%;background:#7B8F3A}
.hpBar.xp i{background:#C4A87C}
.invLog{display:grid;gap:6px;font-size:12px;color:#9aa88f;font-family:var(--font-k)}
/* ---------- Win95 窗口 ---------- */
.w95{background:#008080;padding:18px;border-radius:2px}
.w95Win{max-width:560px;background:#c0c0c0;border:2px solid;border-color:#fff #808080 #808080 #fff;
  box-shadow:2px 2px 0 #000}
.w95Title{display:flex;justify-content:space-between;align-items:center;background:#000080;
  color:#fff;font:11px Tahoma,sans-serif;padding:3px 4px 3px 6px}
.w95Btns{display:flex;gap:2px}
.w95Btns i{font-style:normal;width:16px;height:14px;background:#c0c0c0;color:#000;
  border:2px solid;border-color:#fff #808080 #808080 #fff;font:9px/10px Tahoma;text-align:center}
.w95Menu{display:flex;gap:14px;padding:3px 8px;font:11px Tahoma;border-bottom:1px solid #808080;
  background:#c0c0c0}
.w95Body{padding:10px 12px 14px;font:11.5px Tahoma;color:#000}
.w95Lab{margin:6px 0 3px}
.w95Field input{width:100%;padding:3px 5px;border:2px solid;border-color:#808080 #fff #fff #808080;
  background:#fff;font:11.5px Tahoma}
.w95Chk{display:flex;align-items:center;gap:6px;margin:5px 0}
.w95Box{width:13px;height:13px;background:#fff;border:2px solid;border-color:#808080 #fff #fff #808080;
  font:9px/10px Tahoma;text-align:center;display:inline-block}
.w95Actions{display:flex;gap:6px;justify-content:flex-end;margin-top:12px}
.w95Btn{font:11px Tahoma;padding:3px 16px;background:#c0c0c0;border:2px solid;
  border-color:#fff #808080 #808080 #fff}
.w95Btn:active{border-color:#808080 #fff #fff #808080}
.w95Task{display:flex;align-items:center;gap:6px;margin-top:14px;background:#c0c0c0;
  border:2px solid;border-color:#fff #808080 #808080 #fff;padding:3px 4px}
.w95Start{font:11px Tahoma;padding:2px 8px;background:#c0c0c0;border:2px solid;
  border-color:#fff #808080 #808080 #fff;display:flex;align-items:center;gap:4px}
.w95Tasks{display:flex;gap:4px;flex:1;border-left:1px solid #808080;padding-left:6px}
.w95Tasks span{font:11px Tahoma;padding:2px 10px;background:#c0c0c0;border:2px solid;
  border-color:#808080 #fff #fff #808080}
.w95Clock{font:11px Tahoma;padding:2px 8px;border:2px solid;border-color:#808080 #fff #fff #808080}
/* ---------- 雷达 ---------- */
.radarWrap{display:grid;grid-template-columns:280px 1fr;gap:32px;align-items:center}
.radar{position:relative;width:260px;height:260px;border-radius:50%;border:1px solid var(--line);
  background:radial-gradient(circle,rgba(0,170,255,.10),transparent 70%)}
.radar>span{position:absolute;border:1px solid var(--line);border-radius:50%;opacity:.55}
.radar .r1{inset:10%}.radar .r2{inset:26%}.radar .r3{inset:42%}
.radar:before,.radar:after{content:'';position:absolute;background:var(--line);opacity:.5}
.radar:before{left:50%;top:0;bottom:0;width:1px}
.radar:after{top:50%;left:0;right:0;height:1px}
.sweep{position:absolute;inset:0;border-radius:50%;
  background:conic-gradient(from 0deg,color-mix(in srgb,var(--accent) 55%,transparent),transparent 28%);
  animation:spin 3.6s linear infinite}
@keyframes spin{to{transform:rotate(360deg)}}
.blip{position:absolute;width:7px;height:7px;border-radius:50%;background:var(--accent);
  box-shadow:0 0 12px var(--accent);animation:blink 1.9s infinite}
.dataList{list-style:none;margin:0;padding:0;display:grid;gap:0}
.dataList li{display:flex;align-items:baseline;gap:14px;padding:12px 2px;
  border-bottom:1px solid var(--line);font-family:var(--font-k);font-size:12px}
.dataList b{color:var(--accent);letter-spacing:.14em;font-weight:500;min-width:44px}
.dataList span{color:var(--muted);flex:1}
.dataList em{font-style:normal;color:var(--ink);font-size:14px}
/* ---------- 贴纸 ---------- */
.stk{position:relative;height:260px;border:1px dashed var(--line);border-radius:var(--radius);overflow:hidden}
.sh{position:absolute;display:grid;place-items:center;font-family:var(--font-k);font-weight:700}
.sh.ball{width:96px;height:96px;border-radius:50%;left:8%;top:16%;
  background:radial-gradient(circle at 34% 30%,#fff,var(--accent) 45%,#7a2ea0)}
.sh.star{width:88px;height:88px;left:38%;top:8%;font-size:44px;color:#ffd93d;
  text-shadow:3px 3px 0 #111}
.sh.ring{width:120px;height:120px;border-radius:50%;right:10%;top:30%;border:10px solid #4ecdc4}
.sh.zig{left:26%;bottom:14%;font-size:26px;letter-spacing:-4px;color:#ff6b6b}
.sh.dots{right:32%;bottom:8%;width:70px;height:70px;
  background-image:radial-gradient(#111 3px,transparent 3px);background-size:14px 14px}
.sh.pill{right:6%;bottom:16%;padding:6px 16px;border-radius:999px;background:#111;color:#ffe66d;
  font-size:12px;letter-spacing:.16em;transform:rotate(-8deg)}
/* ---------- 玻璃堆叠 ---------- */
.gls{position:relative;min-height:300px;display:grid;place-items:center}
.glsCard{position:absolute;width:min(420px,80%);border-radius:var(--radius);
  background:var(--surface);border:1px solid rgba(255,255,255,.18);padding:20px;
  -webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);
  box-shadow:0 24px 60px rgba(0,0,0,.32)}
.glsCard p{margin:0 0 12px;font-size:13.5px;line-height:1.7;color:var(--muted)}
.glsCard.c3{transform:translate(-46px,-46px) scale(.94);opacity:.55}
.glsCard.c2{transform:translate(-22px,-22px) scale(.97);opacity:.8}
.glsCard.c1{transform:translate(0,0);z-index:2}
"""

MODCSS += """
/* ---------- 面包屑 / 粘性导航 ---------- */
.nav{position:sticky;top:0;z-index:40;background:var(--bg)}
.nav.stuck{box-shadow:0 1px 0 var(--line)}
.nav{position:static}
.takeBar{position:sticky;top:0;z-index:45;display:flex;align-items:center;gap:8px;
  padding:10px 0;background:var(--bg);border-bottom:1px solid var(--line);flex-wrap:wrap}
#langSwitch select{font:inherit;font-size:11.5px;padding:5px 8px;border:1px solid var(--line);border-radius:6px;background:transparent;color:var(--ink)}
.tbName{font-family:var(--font-h);font-weight:700;font-size:13px;margin-right:auto}
.tbBtn{font:inherit;font-size:11.5px;font-weight:600;padding:6px 12px;border-radius:6px;
  border:1px solid var(--line);background:transparent;color:var(--ink);cursor:pointer;text-decoration:none}
.tbBtn:hover{border-color:var(--ink)}
.tbBtn.primary{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.howModal{position:fixed;inset:0;z-index:200;background:rgba(10,10,12,.55);display:grid;place-items:center;padding:24px}
.howModal[hidden]{display:none}
.howCard{background:#fff;color:#15150f;border-radius:14px;padding:26px 28px;max-width:520px;width:100%;
  position:relative;box-shadow:0 30px 80px rgba(0,0,0,.35);font-family:"PingFang SC",system-ui,sans-serif}
.howCard h3{margin:0 0 14px;font-size:18px;letter-spacing:-.02em}
.howClose{position:absolute;right:10px;top:8px;border:0;background:none;font-size:22px;cursor:pointer;color:#999}
.howList{margin:0;padding-left:20px;display:grid;gap:12px}
.howList b{display:block;font-size:13.5px;margin-bottom:2px}
.howList span{font-size:12.5px;color:#666;line-height:1.65}
.howAdv{margin-top:18px;padding-top:14px;border-top:1px solid #eee;display:flex;gap:10px;align-items:center;flex-wrap:wrap;font-size:12px;color:#666}
.howAdv .tbBtn{border-color:#ddd;color:#15150f}
.howHint{font-size:11.5px;color:#999}
.crumb{display:flex;gap:8px;align-items:center;font-family:var(--font-k);font-size:11px;
  color:var(--muted);padding:14px 0 0;letter-spacing:.04em}
.crumb a{color:inherit;text-decoration:none}
.crumb a:hover{color:var(--accent)}
.crumb b{color:var(--ink);font-weight:500}
/* ---------- 交互区 ---------- */
.iaBox{background:var(--surface);border:var(--card-border);border-radius:var(--radius);
  padding:20px 22px;box-shadow:var(--shadow);margin-bottom:var(--card-gap,16px)}
.iaTabs{display:flex;gap:2px;border-bottom:1px solid var(--line);margin-bottom:16px;flex-wrap:wrap}
.tab{font:inherit;font-size:13px;padding:9px 16px;background:none;border:0;border-bottom:2px solid transparent;
  color:var(--muted);cursor:pointer;margin-bottom:-1px}
.tab.on{color:var(--ink);border-bottom-color:var(--accent);font-weight:600}
.pane{display:none}
.pane.on{display:block}
.pTxt{margin:0 0 12px;font-size:13.5px;color:var(--muted);line-height:1.7}
.setRow{display:flex;justify-content:space-between;align-items:center;padding:10px 0;
  border-bottom:1px solid var(--line);font-size:13.5px}
.setRow:last-child{border-bottom:0}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:var(--card-gap,16px)}
.btn.sm{padding:8px 16px;font-size:12.5px}
.steps{list-style:none;display:flex;margin:0 0 16px;padding:0}
.steps li{flex:1;display:grid;gap:8px;position:relative;font-size:11.5px;color:var(--muted);
  font-family:var(--font-k);letter-spacing:.06em}
.steps li b{width:26px;height:26px;border-radius:50%;border:1px solid var(--line);display:grid;
  place-items:center;font-size:12px;background:var(--bg);font-weight:500;position:relative;z-index:1}
.steps li:after{content:'';position:absolute;left:26px;top:13px;right:6px;height:1px;background:var(--line)}
.steps li:last-child:after{display:none}
.steps li.on{color:var(--ink)}
.steps li.on b{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.steps li.done b{border-color:var(--accent);color:var(--accent)}
.drop{display:grid;gap:5px;place-items:center;padding:24px 16px;border:1px dashed var(--line);
  border-radius:var(--radius);cursor:pointer;text-align:center;transition:.15s}
.drop:hover,.drop.over{border-color:var(--accent);background:color-mix(in srgb,var(--accent) 7%,transparent)}
.drop b{font-size:13.5px;font-weight:600}
.drop span{font-size:11.5px;color:var(--muted)}
.upName{margin:10px 0 0;font-size:12px;color:var(--accent);font-family:var(--font-k);min-height:16px}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden;margin-bottom:14px}
.sg{font:inherit;font-size:11.5px;padding:5px 12px;border:0;background:none;color:var(--muted);cursor:pointer}
.sg.on{background:var(--accent);color:var(--on-accent)}
.stateBox{min-height:112px;display:grid;place-items:center;border:1px solid var(--line);
  border-radius:var(--radius);padding:16px}
.empty{display:grid;gap:5px;justify-items:center;color:var(--muted);font-size:12.5px;text-align:center}
.empty i{width:32px;height:32px;border:1px solid var(--line);border-radius:7px;display:block}
.empty small{font-size:11px;opacity:.75}
.skel{width:100%;display:grid;gap:9px;padding:4px 0}
.skel i{height:10px;border-radius:4px;background:linear-gradient(90deg,var(--line) 25%,
  color-mix(in srgb,var(--line) 45%,var(--bg)) 37%,var(--line) 63%);background-size:400% 100%;
  animation:shimmer 1.4s linear infinite}
@keyframes shimmer{to{background-position:-200% 0}}
.err{display:grid;gap:5px;justify-items:center;text-align:center;font-size:12.5px;color:#e5484d}
.err span{color:var(--muted)}
.toast{position:fixed;left:50%;bottom:76px;transform:translate(-50%,18px);background:var(--ink);
  color:var(--bg);padding:11px 22px;border-radius:999px;font-size:13px;opacity:0;pointer-events:none;
  transition:.25s cubic-bezier(.2,.8,.3,1);z-index:120;white-space:nowrap}
.toast.show{opacity:1;transform:translate(-50%,0)}
.modal{position:fixed;inset:0;background:rgba(8,8,12,.55);display:grid;place-items:center;padding:24px;
  opacity:0;pointer-events:none;transition:.2s;z-index:130}
.modal.open{opacity:1;pointer-events:auto}
.modalCard{background:var(--surface);color:var(--ink);border:var(--card-border);border-radius:var(--radius);
  padding:26px;max-width:400px;box-shadow:0 30px 80px rgba(0,0,0,.45);
  transform:translateY(10px) scale(.98);transition:.22s cubic-bezier(.2,.8,.3,1)}
.modal.open .modalCard{transform:none}
.modalCard h3{margin:0 0 8px;font-family:var(--font-h);font-size:18px}
.modalCard p{margin:0;font-size:13.5px;color:var(--muted);line-height:1.7}
[data-reveal]{transition:opacity .55s ease, transform .55s cubic-bezier(.2,.8,.3,1)}
[data-reveal].pre{opacity:0;transform:translateY(16px)}
@media (max-width:860px){.grid2{grid-template-columns:1fr}}
"""

MODCSS += """
/* RAIL-CSS-START ---------- 左侧缩略图导航 ---------- */
.rail{position:fixed;left:0;top:0;bottom:0;width:236px;z-index:60;display:flex;flex-direction:column;
  background:#f6f6f2;border-right:1px solid rgba(0,0,0,.13);
  box-shadow:2px 0 14px rgba(0,0,0,.07);color:#1b1b16;
  font-family:-apple-system,"PingFang SC",system-ui,sans-serif;
  overflow:hidden;transition:width .26s cubic-bezier(.2,.8,.3,1)}
.rail.closed{width:44px}
.rail.closed .railList,.rail.closed .railFoot,.rail.closed .railTop b{display:none}
.rail.closed .railTop{padding:7px 0;justify-content:center;border-bottom:0}
.rail.closed:after{content:'风格大全';writing-mode:vertical-rl;text-orientation:mixed;
  margin:16px auto 0;font:11px/1 ui-monospace,monospace;letter-spacing:.3em;color:#7c7c72;
  white-space:nowrap}
.railTop{display:flex;align-items:center;justify-content:space-between;gap:6px;padding:14px 14px;
  border-bottom:1px solid rgba(0,0,0,.1);font:12px/1 ui-monospace,monospace;
  letter-spacing:.12em;color:#71716a;text-transform:uppercase}
.railTop b{font-weight:600;color:#1b1b16}
.railTop button{width:26px;height:26px;border-radius:5px;border:1px solid rgba(0,0,0,.2);
  background:#fff;color:#3a3a33;cursor:pointer;font:13px/1 monospace;padding:0}
.railTop button:hover{background:#e9e9e2;color:#000}
.railList{overflow-y:auto;overflow-x:hidden;padding:10px;display:flex;flex-direction:column;
  gap:10px;flex:1;min-height:0;scrollbar-width:thin;overscroll-behavior:contain}
.railList::-webkit-scrollbar{width:6px}
.railList::-webkit-scrollbar-thumb{background:rgba(255,255,255,.18);border-radius:3px}
.railList .rItem{position:relative;flex:0 0 auto}
.railList .rThumb{display:block;border-radius:7px;overflow:hidden;text-decoration:none;
  border:1px solid rgba(0,0,0,.16);background:#fff;
  transition:border-color .15s,box-shadow .15s,transform .15s}
.railList .rThumb:hover{border-color:rgba(0,0,0,.45);box-shadow:0 3px 10px rgba(0,0,0,.1);transform:translateY(-1px)}
.railList .rThumb.on{border-color:#1d4ed8;box-shadow:0 0 0 2px rgba(29,78,216,.35)}
.railList .rDl{position:absolute;right:6px;top:6px;z-index:2;display:inline-flex;
  align-items:center;gap:3px;padding:3px 7px;border-radius:5px;line-height:1;
  font-family:-apple-system,"PingFang SC",system-ui,sans-serif;font-size:9.5px;font-weight:600;
  background:rgba(255,255,255,.94);color:#3f3f38;
  border:1px solid rgba(0,0,0,.13);box-shadow:0 1px 3px rgba(0,0,0,.12);text-decoration:none;
  white-space:nowrap;opacity:.92;
  transition:background .15s,color .15s,border-color .15s,opacity .15s}
.railList .rDl svg{width:10px;height:10px;flex:0 0 auto}
.railList .rDl:hover{background:#15803d;color:#fff;border-color:#15803d;opacity:1}
.railList img{display:block;width:100%;height:118px;object-fit:cover;object-position:top;
  background:#e8e8e2;border-bottom:1px solid rgba(0,0,0,.08)}
.railList .rThumb span{display:block;padding:8px 9px;font-size:12px;line-height:1.35;color:#4a4a41;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.railList .rThumb.on span{color:#0d0d0a;font-weight:600}
.railFoot{display:block;padding:13px 14px;border-top:1px solid rgba(0,0,0,.1);
  color:#1d4ed8;text-decoration:none;font:11.5px/1 ui-monospace,monospace;letter-spacing:.06em}
.railFoot:hover{color:#0b2ea8;background:rgba(0,0,0,.05)}
.railFoot.dl{color:#15803d;border-top:1px solid rgba(0,0,0,.07)}
a.railFoot[href$="-components.html"]{color:#7c3aed}
a.railFoot[href$="-components.html"]:hover{color:#fff;background:#7c3aed}
.railFoot.dl:hover{color:#fff;background:#15803d}
@media (min-width:1240px){body.has-rail{padding-left:236px}}
@media (min-width:1240px){body.has-rail.rail-closed{padding-left:44px}}
@media (max-width:1239px){
  body.has-rail.rail-closed{padding-left:44px}
  body.has-rail:not(.rail-closed) .rail{box-shadow:6px 0 30px rgba(0,0,0,.22)}
}
@media (max-width:700px){.rail{width:196px}.railList img{height:96px}
  body.has-rail.rail-closed{padding-left:44px}}
/* RAIL-CSS-END */
"""

TPL = Template("""<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>$no $cn $en — 风格 Demo</title>
<style>
:root{
--bg:$bg;--surface:$surface;--ink:$ink;--muted:$muted;--line:$line;
--accent:$accent;--on-accent:$on_accent;--radius:$radius;--card-pad:$cardpad;
--card-border:$cardborder;--shadow:$shadow;--btn-radius:$btnradius;
--btn-shadow:$btnshadow;--btn-border:$btnborder;--ghost-border:$ghostborder;
--font-h:$fonth;--font-b:$fontb;--font-k:$fontk;--ls-h:$lsh;--lh-h:$lhh;
--h1-w:$h1w;--h1-size:$h1size;--tt-k:$ttk;--ls-k:$lsk;--card-gap:$cardgap;
--nav-border:$navborder;--lead-fs:$leadfs;
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);$bgimg color:var(--ink);
  font-family:var(--font-b);-webkit-font-smoothing:antialiased;min-height:100vh;padding-bottom:64px}
.frame{max-width:1100px;margin:0 auto;padding:26px 44px 0;position:relative;z-index:1}
.nav{display:flex;align-items:center;gap:26px;padding:14px 0;border-bottom:var(--nav-border)}
.brand{font-family:var(--font-h);font-weight:800;font-size:17px;white-space:nowrap;
  display:flex;align-items:baseline;gap:9px}
.bn{font-family:var(--font-k);font-size:11px;letter-spacing:.1em;color:var(--muted);
  font-weight:500;flex:0 0 auto}
.bt{min-width:0;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.brand i{font-style:normal;color:var(--accent)}
.nav nav{display:flex;gap:22px;margin-left:auto;font-size:13px;color:var(--muted)}
.nav nav a{color:inherit;text-decoration:none}
.nav nav a:hover{color:var(--accent)}
.navbtn{font-size:12.5px;padding:7px 15px;border-radius:var(--btn-radius);background:var(--accent);
  color:var(--on-accent);border:var(--btn-border);box-shadow:var(--btn-shadow);text-decoration:none;
  font-weight:600;white-space:nowrap}
.hero{padding:72px 0 52px;display:grid;gap:18px;max-width:var(--hero-w,780px)}
.hero.center{max-width:820px;margin:0 auto;justify-items:center;text-align:center}
.hero.split{max-width:none;grid-template-columns:1.05fr .95fr;align-items:center;gap:44px}
.heroCopy{display:grid;gap:18px;justify-items:start;max-width:100%}
.hero.center .heroCopy{justify-items:center}
.kicker{font-family:var(--font-k);font-size:11px;letter-spacing:var(--ls-k);
  text-transform:var(--tt-k);color:var(--muted);margin:0;font-weight:500}
h1{font-family:var(--font-h);font-size:var(--h1-size);line-height:var(--lh-h);
  letter-spacing:var(--ls-h);margin:0;font-weight:var(--h1-w);color:var(--ink);
  margin-top:max(0px,calc((1 - var(--lh-h)) * 1em));
  margin-bottom:max(0px,calc((1 - var(--lh-h)) * 1em))}
h1 em{font-style:normal}
.lead{font-family:var(--font-b);font-size:var(--lead-fs);line-height:1.7;color:var(--muted);
  margin:0;max-width:56ch}
.cta{display:flex;gap:12px;flex-wrap:wrap;margin-top:2px}
.btn{padding:12px 24px;border-radius:var(--btn-radius);background:var(--accent);color:var(--on-accent);
  font-size:14px;font-weight:600;text-decoration:none;border:var(--btn-border);
  box-shadow:var(--btn-shadow);white-space:nowrap;display:inline-block}
.btn.ghost{background:transparent;color:var(--ink);border:var(--ghost-border);box-shadow:none}
.cards{display:grid;grid-template-columns:repeat(3,1fr);gap:var(--card-gap);padding:0}
.card{background:var(--surface);border:var(--card-border);border-radius:var(--radius);
  padding:var(--card-pad);box-shadow:var(--shadow);position:relative}
.card .ico{width:30px;height:30px;border-radius:8px;background:var(--accent);margin-bottom:16px;display:block}
.card h3{margin:0 0 8px;font-size:16px;font-family:var(--font-h);font-weight:700;letter-spacing:-.01em}
.card p{margin:0;font-size:13.5px;line-height:1.7;color:var(--muted)}
.foot{border-top:var(--nav-border);padding:32px 0 40px;display:grid;grid-template-columns:1.6fr 1fr 1fr 1fr;gap:28px}
.foot h4{margin:0 0 10px;font-size:11px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--muted);font-family:var(--font-k);font-weight:500}
.foot ul{list-style:none;margin:0;padding:0;display:grid;gap:7px;font-size:13px;color:var(--muted)}
.foot ul a{color:inherit;text-decoration:none}
.foot .fbrand{font-family:var(--font-h);font-weight:800;font-size:16px;
  display:flex;align-items:baseline;gap:8px}
.foot .fbrand+p{font-size:12.5px;color:var(--muted);margin:8px 0 0;max-width:26ch;line-height:1.7}
.footBottom{grid-column:1/-1;display:flex;justify-content:space-between;padding-top:18px;
  border-top:1px solid var(--line);font-family:var(--font-k);font-size:11.5px;color:var(--muted)}
.bar{position:fixed;left:50%;bottom:16px;transform:translateX(-50%);display:flex;gap:12px;
  align-items:center;background:rgba(12,12,12,.88);color:#e9e9e2;border:1px solid rgba(255,255,255,.16);
  -webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);padding:7px 15px;border-radius:999px;
  font:12px/1 ui-monospace,'SF Mono',Menlo,monospace;z-index:99;white-space:nowrap;
  max-width:calc(100vw - 24px);overflow:hidden}
.bar b{color:#8fb0ff;font-weight:600}
.bar span{color:#c9c9c2;overflow:hidden;text-overflow:ellipsis}
.bar a{color:#8fb0ff;text-decoration:none}
.bar a:hover{color:#fff}
$modcss
@media (max-width:860px){
  .frame{padding:18px 20px 0}
  .hero{padding:44px 0 32px;max-width:none}
  .hero.split{grid-template-columns:1fr;gap:28px}
  .cards,.compGrid,.stt,.gal,.inv{grid-template-columns:1fr}
  .nav nav{display:none}
  .navbtn{margin-left:auto}
  .brand{flex:1 1 auto;min-width:0;overflow:hidden}
  .brand .bn{display:none}
  .radarWrap{grid-template-columns:1fr;gap:20px}
  .foot{grid-template-columns:1fr 1fr}
  .invGrid{grid-template-columns:repeat(3,1fr)}
  .slot{width:100%;height:auto;aspect-ratio:1}
  .chAxis span:nth-child(n+5){display:none}
}
$raw
$raw2
</style></head>
<body>
<div class="rail" id="rail">
  <div class="railTop"><b>风格大全</b><button id="railCollapse" title="收起导航">‹</button></div>
  <div class="railList" id="railList"></div>
  <a class="railFoot" href="#components">◱ 组件总览（105）</a>
  <a class="railFoot" href="../50-frontend-styles.html">← 返回速查表</a>
  <a class="railFoot dl" href="../assets/zips/style-$slug.zip" download
     title="下载该风格的自包含 zip（spec + 提示词 + theme.css + demo）">⤓ 导出风格包</a>
</div>
<div class="frame">
  <header class="nav">
    <div class="brand"><span class="bn">$no</span><span class="bt">$cn</span></div>
    <nav><a href="#">产品</a><a href="#">方案</a><a href="#">客户</a><a href="#">文档</a></nav>
    <a class="navbtn" href="#">开始使用</a>
  </header>

  <div class="takeBar">
    <span class="tbName">$no $cn</span>
    <span id="langSwitch"></span>
    <a class="tbBtn primary" href="../assets/zips/style-$slug.zip" download>⤓ 下载风格包</a>
    <button class="tbBtn" id="copyPrompt">📋 复制给 AI 的话</button>
    <button class="tbBtn" id="howBtn">怎么用？</button>
  </div>
  <template id="tokTpl">$tokencss</template>
  <template id="promptTpl">$prompt</template>

  <div class="howModal" id="howModal" hidden>
    <div class="howCard">
      <button class="howClose" id="howClose">×</button>
      <h3>3 步拿走这套风格</h3>
      <ol class="howList">
        <li><b>下载风格包</b><span>点左上角「⤓ 下载风格包」，得到一个 zip。里面就是这个风格的全部代码 + 说明。</span></li>
        <li><b>解压，打开 demo.html</b><span>你会看到这套风格的完整页面（落地页 + 105 个组件），双击就能看。</span></li>
        <li><b>想做自己的页面</b><span>点「📋 复制给 AI 的话」，粘给任意 AI，把最后一行换成你的需求即可。</span></li>
      </ol>
      <div class="howAdv">
        <span>进阶：想自己改代码？</span>
        <button class="tbBtn" id="copyTok">复制 CSS 变量</button>
        <span class="howHint">zip 里还有 spec.md（规格卡）和 theme.css（现成样式表）</span>
      </div>
    </div>
  </div>

  <div class="crumb"><a href="#">首页</a><span>/</span><a href="#">设计系统</a><span>/</span><b>概览</b></div>
  <section class="hero$layoutcls">
    <div class="heroCopy">
      <p class="kicker">DESIGN SYSTEM 2026</p>
      <h1>把复杂的事<br><em>做得简单</em></h1>
      <p class="lead">更快的构建、更少的维护、更好的体验。一套设计语言，覆盖从落地页到后台的全部界面。</p>
      <div class="cta"><a class="btn" href="#">开始使用</a><a class="btn ghost" href="#">查看示例 →</a></div>
    </div>
    $deco
  </section>

  <section class="sec">
    <div class="secHead"><h2>组件与控件</h2><p>BUTTONS / INPUT / TOGGLE</p></div>
    <div class="compGrid">
      <div class="panel">
        <span class="lab">按钮</span>
        <div class="row"><a class="btn" href="#">主要操作</a><a class="btn ghost" href="#">次要</a>
          <a class="btn dis" href="#">禁用</a></div>
      </div>
      <div class="panel">
        <span class="lab">输入框</span>
        <input class="inp" placeholder="输入项目名称…">
        <div class="row" style="margin-top:12px"><span class="badge">进行中</span>
          <span class="badge soft">草稿</span></div>
      </div>
      <div class="panel">
        <span class="lab">开关与进度</span>
        <div class="row"><span class="sw on"><i></i></span><span class="sw"><i></i></span>
          <span class="tiny" style="color:var(--muted)">自动同步</span></div>
        <div class="prog"><i style="width:64%"></i></div>
      </div>
    </div>
  </section>

  <section class="sec">
    <div class="secHead"><h2>特性卡片</h2><p>CARDS / 3</p></div>
    <div class="cards">
      <article class="card"><span class="ico"></span><h3>构建快</h3><p>组件即拿即用，半天就能搭出一个完整页面。</p></article>
      <article class="card"><span class="ico"></span><h3>可维护</h3><p>一套 token 管住颜色、间距和圆角，改一处全站生效。</p></article>
      <article class="card"><span class="ico"></span><h3>好体验</h3><p>默认适配键盘操作、屏幕阅读器和暗色模式。</p></article>
    </div>
  </section>

$strip

$sig

$con

  <section class="sec" data-reveal>
    <div class="secHead"><h2>交互与状态</h2><p>TABS / STEPS / UPLOAD / STATES</p></div>
    <div class="iaBox">
      <div class="iaTabs" role="tablist">
        <button class="tab on" data-tab="0">概览</button>
        <button class="tab" data-tab="1">数据</button>
        <button class="tab" data-tab="2">设置</button>
      </div>
      <div class="pane on" data-pane="0">
        <p class="pTxt">切换 tab 相当于切换二级页面——同一个壳，不同的内容。</p>
        <div class="row"><span class="badge">进行中</span><span class="badge soft">v2.4</span>
          <span class="badge soft">5 个模块</span></div>
      </div>
      <div class="pane" data-pane="1">
        <table class="tbl"><thead><tr><th>指标</th><th class="r">本周</th><th class="r">环比</th></tr></thead>
          <tbody><tr><td>构建次数</td><td class="r">3,120</td><td class="r">+12%</td></tr>
          <tr><td>平均耗时</td><td class="r">1.28s</td><td class="r">-8%</td></tr></tbody></table>
      </div>
      <div class="pane" data-pane="2">
        <div class="setRow"><span>自动同步</span><span class="sw on"><i></i></span></div>
        <div class="setRow"><span>构建通知</span><span class="sw"><i></i></span></div>
      </div>
    </div>
    <div class="grid2">
      <div class="panel">
        <span class="lab">步骤条</span>
        <ol class="steps" id="steps"><li class="on"><b>1</b><span>需求</span></li>
          <li><b>2</b><span>设计</span></li><li><b>3</b><span>上线</span></li></ol>
        <div class="row"><button class="btn sm ghost" id="stepPrev">上一步</button>
          <button class="btn sm" id="stepNext">下一步</button></div>
      </div>
      <div class="panel">
        <span class="lab">上传（可拖拽）</span>
        <label class="drop" id="drop"><b>拖拽文件到这里</b>
          <span>或点击选择 · PNG / JPG · ≤ 5MB</span><input type="file" id="file" hidden></label>
        <p class="upName" id="upName"></p>
      </div>
      <div class="panel">
        <span class="lab">状态</span>
        <div class="seg" id="seg"><button class="sg on" data-state="empty">空</button>
          <button class="sg" data-state="load">载入</button><button class="sg" data-state="err">错误</button>
          <button class="sg" data-state="done">完成</button></div>
        <div class="stateBox" id="stateBox"></div>
      </div>
      <div class="panel">
        <span class="lab">反馈</span>
        <div class="row"><button class="btn sm" id="toastBtn">显示提示</button>
          <button class="btn sm ghost" id="modalBtn">打开弹窗</button></div>
        <p class="help" style="margin-top:12px">弹窗支持 Esc 关闭、点遮罩关闭。</p>
      </div>
    </div>
  </section>

  <section class="sec" id="components">
    <div class="secHead"><h2>组件总览</h2><p>105 COMPONENTS · 16 GROUPS</p></div>
    <div id="sheetHost" class="sheetHost"></div>
    <template id="sheetTpl"><style>$sheetcss</style><div class="wrap">$sheetbody</div></template>
  </section>

  <footer class="foot">
    <div><div class="fbrand"><span class="bn">$no</span>$cn</div>
      <p>前端设计风格大全 · 第 $no 个 · 同一套内容，只换设计语言。</p></div>
    <div><h4>产品</h4><ul><li><a href="#">设计系统</a></li><li><a href="#">组件库</a></li>
      <li><a href="#">主题商店</a></li></ul></div>
    <div><h4>资源</h4><ul><li><a href="#">文档</a></li><li><a href="#">更新日志</a></li>
      <li><a href="#">状态</a></li></ul></div>
    <div><h4>关于</h4><ul><li><a href="#">团队</a></li><li><a href="#">招聘</a></li>
      <li><a href="#">联系</a></li></ul></div>
    <div class="footBottom"><span>© 2026 $cn · 风格 Demo</span><span>Privacy · Terms · Cookies</span></div>
  </footer>
</div>
<div class="toast" id="toast">已保存到「我的项目」</div>
<div class="modal" id="modal">
  <div class="modalCard" role="dialog" aria-modal="true">
    <h3>删除这个项目？</h3>
    <p>删除后 30 天内可在「回收站」恢复，关联的构建记录会一并隐藏。</p>
    <div class="row" style="justify-content:flex-end;margin-top:18px">
      <button class="btn sm ghost" id="modalCancel">取消</button>
      <button class="btn sm" id="modalOk">删除</button>
    </div>
  </div>
</div>
<script>
(function(){
var rm=window.matchMedia('(prefers-reduced-motion: reduce)').matches;
var rv=[].slice.call(document.querySelectorAll('[data-reveal]'));
if(rv.length&&'IntersectionObserver' in window&&!rm){
  var io=new IntersectionObserver(function(es){es.forEach(function(en){
    if(en.isIntersecting){en.target.classList.remove('pre');io.unobserve(en.target);}})},
    {rootMargin:'0px 0px -6% 0px',threshold:.04});
  rv.forEach(function(e){
    if(e.getBoundingClientRect().top>window.innerHeight*.92){e.classList.add('pre');io.observe(e);}
  });
}else{rv.forEach(function(e){e.classList.remove('pre')})}
var nav=document.querySelector('.nav');
function onScroll(){
  if(nav)nav.classList.toggle('stuck',window.scrollY>6);
  if(!rm){[].forEach.call(document.querySelectorAll('.art'),function(a){
    a.style.transform='translateY('+Math.min(window.scrollY*.05,32)+'px)';});}
}
window.addEventListener('scroll',onScroll,{passive:true});onScroll();
[].forEach.call(document.querySelectorAll('.iaTabs .tab'),function(t){
  t.addEventListener('click',function(){
    [].forEach.call(document.querySelectorAll('.iaTabs .tab'),function(x){x.classList.remove('on')});
    t.classList.add('on');
    [].forEach.call(document.querySelectorAll('.pane'),function(p){
      p.classList.toggle('on',p.getAttribute('data-pane')===t.getAttribute('data-tab'));});
  });
});
var st=[].slice.call(document.querySelectorAll('#steps li')),cur=0;
function paint(){st.forEach(function(li,i){li.classList.toggle('on',i===cur);
  li.classList.toggle('done',i<cur);});}
var pv=document.getElementById('stepPrev'),nx=document.getElementById('stepNext');
if(pv)pv.onclick=function(){if(cur>0){cur--;paint();}};
if(nx)nx.onclick=function(){if(cur<st.length-1){cur++;paint();}};
var drop=document.getElementById('drop'),file=document.getElementById('file'),
    upName=document.getElementById('upName');
if(drop){
  ['dragenter','dragover'].forEach(function(ev){drop.addEventListener(ev,function(e){
    e.preventDefault();drop.classList.add('over');});});
  ['dragleave','drop'].forEach(function(ev){drop.addEventListener(ev,function(e){
    e.preventDefault();drop.classList.remove('over');});});
  drop.addEventListener('drop',function(e){
    var f=e.dataTransfer&&e.dataTransfer.files[0];if(f)upName.textContent='已选择：'+f.name;});
  file.addEventListener('change',function(){
    if(file.files[0])upName.textContent='已选择：'+file.files[0].name;});
}
var STATE={empty:'<div class="empty"><i></i><span>还没有数据</span><small>创建第一个项目后会显示在这里</small></div>',
  load:'<div class="skel"><i style="width:82%"></i><i style="width:100%"></i><i style="width:64%"></i></div>',
  err:'<div class="err"><b>加载失败</b><span>请求超时，请稍后重试</span></div>',
  done:'<div class="empty"><b style="color:var(--ink)">已完成</b><span>5 个项目 · 2.4 MB</span></div>'};
var box=document.getElementById('stateBox'),seg=document.getElementById('seg');
if(box&&seg){box.innerHTML=STATE.empty;
  [].forEach.call(seg.querySelectorAll('.sg'),function(b){b.onclick=function(){
    [].forEach.call(seg.querySelectorAll('.sg'),function(x){x.classList.remove('on')});
    b.classList.add('on');box.innerHTML=STATE[b.getAttribute('data-state')];};});}
var toast=document.getElementById('toast'),tt;
function showToast(){if(!toast)return;toast.classList.add('show');clearTimeout(tt);
  tt=setTimeout(function(){toast.classList.remove('show')},2200);}
var tb=document.getElementById('toastBtn');if(tb)tb.onclick=showToast;
var modal=document.getElementById('modal'),mb=document.getElementById('modalBtn');
function closeModal(){if(modal)modal.classList.remove('open');}
if(mb)mb.onclick=function(){modal.classList.add('open');};
var mc=document.getElementById('modalCancel'),mo=document.getElementById('modalOk');
if(mc)mc.onclick=closeModal;
if(mo)mo.onclick=function(){closeModal();showToast();};
if(modal)modal.addEventListener('click',function(e){if(e.target===modal)closeModal();});
document.addEventListener('keydown',function(e){if(e.key==='Escape')closeModal();});
})();
</script>
<script>
(function(){
var EMBED=location.search.indexOf('embed')>-1;
if(EMBED){
  var b=document.querySelector('.bar');b&&b.remove();
  var r=document.getElementById('rail');r&&r.remove();
  document.body.style.paddingBottom='0';
  return;
}
var DATA=$raildata, CUR="$slug";
var list=document.getElementById('railList'), rail=document.getElementById('rail');
if(!list||!rail) return;
var DL='<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
  +'stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/>'
  +'<path d="m7 11 5 5 5-5"/><path d="M5 21h14"/></svg>';
var active=null;
DATA.forEach(function(d){
  var wrap=document.createElement('div'); wrap.className='rItem';
  var a=document.createElement('a'); a.className='rThumb'; a.href=d[2]+'.html';
  a.title=d[0]+' '+d[1];
  if(d[2]===CUR){a.classList.add('on');active=wrap;}
  var img=document.createElement('img');
  img.loading='lazy'; img.alt=d[1];
  img.src='../assets/thumbs/'+d[0]+'.jpg';
  var sp=document.createElement('span');
  sp.textContent=d[0]+' '+d[1];
  a.appendChild(img); a.appendChild(sp);
  var dl=document.createElement('a'); dl.className='rDl';
  dl.href='../assets/zips/style-'+d[2]+'.zip'; dl.setAttribute('download','');
  dl.title='导出「'+d[1]+'」风格包（zip）';
  dl.innerHTML=DL+'<span>导出风格包</span>';
  wrap.appendChild(a); wrap.appendChild(dl);
  list.appendChild(wrap);
});
var KEY='arcRailScroll', saved=null;
try{saved=sessionStorage.getItem(KEY);}catch(e){}
if(saved!==null){list.scrollTop=parseInt(saved,10)||0;}
if(active){
  var st=list.scrollTop, h=list.clientHeight,
      top=active.offsetTop, bot=top+active.offsetHeight;
  if(top<st){list.scrollTop=Math.max(0,top-8);}
  else if(bot>st+h){list.scrollTop=bot-h+8;}
}
var saveTick=false;
list.addEventListener('scroll',function(){
  if(saveTick)return; saveTick=true;
  requestAnimationFrame(function(){
    saveTick=false;
    try{sessionStorage.setItem(KEY,String(list.scrollTop));}catch(e){}
  });
},{passive:true});
function setRail(open){
  rail.classList.toggle('closed',!open);
  document.body.classList.toggle('rail-closed',!open);
  document.body.classList.toggle('has-rail',true);
  var btn=document.getElementById('railCollapse');
  if(btn){btn.textContent=open?'‹':'›';btn.title=open?'收起导航':'展开导航';}
}
var col=document.getElementById('railCollapse');
if(col)col.onclick=function(){setRail(rail.classList.contains('closed'));};
setRail(window.innerWidth>=1240);
var wasNarrow=window.innerWidth<1240;
window.addEventListener('resize',function(){
  var narrow=window.innerWidth<1240;
  if(narrow!==wasNarrow){wasNarrow=narrow;if(narrow)setRail(false);}
});
})();
</script>
<script src="../assets/i18n.js" defer></script>
<script>
(function(){
  if(location.search.indexOf('embed')>-1) return;
  var host=document.getElementById('sheetHost'), tpl=document.getElementById('sheetTpl');
  if(!host||!tpl||!host.attachShadow) return;
  var root=host.attachShadow({mode:'open'});
  root.appendChild(tpl.content.cloneNode(true));
  function all(sel){ return [].slice.call(root.querySelectorAll(sel)); }
  var toast=root.getElementById('toast'), tt;
  all('[data-toast]').forEach(function(b){ b.onclick=function(){
    if(!toast)return; toast.classList.add('show'); clearTimeout(tt);
    tt=setTimeout(function(){ toast.classList.remove('show'); },2000); }; });
  var modal=root.getElementById('modal'), drawer=root.getElementById('drawer');
  all('[data-modal]').forEach(function(b){ b.onclick=function(){ modal.classList.add('open'); }; });
  all('[data-drawer]').forEach(function(b){ b.onclick=function(){ drawer.classList.add('open'); }; });
  all('[data-close]').forEach(function(b){ b.onclick=function(){
    modal.classList.remove('open'); drawer.classList.remove('open'); }; });
  if(modal) modal.addEventListener('click',function(e){ if(e.target===modal) modal.classList.remove('open'); });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'){
    if(modal) modal.classList.remove('open'); if(drawer) drawer.classList.remove('open'); }; });
  all('.sw').forEach(function(x){ x.onclick=function(){ x.classList.toggle('on'); }; });
  all('.btngroup .btn').forEach(function(b){ b.onclick=function(){
    [].slice.call(b.parentNode.querySelectorAll('.btn')).forEach(function(x){ x.classList.remove('on'); });
    b.classList.add('on'); }; });
  all('.seg .sg').forEach(function(b){ b.onclick=function(){
    [].slice.call(b.parentNode.querySelectorAll('.sg')).forEach(function(x){ x.classList.remove('on'); });
    b.classList.add('on'); }; });
  all('[data-tabs] .tab').forEach(function(b){ b.onclick=function(){
    [].slice.call(b.parentNode.querySelectorAll('.tab')).forEach(function(x){ x.classList.remove('on'); });
    b.classList.add('on'); }; });
  function tr(){ if(window.AtlasI18n&&window.AtlasI18n.dict&&window.AtlasI18n.translateRoot) window.AtlasI18n.translateRoot(root); }
  tr(); document.addEventListener('i18n:dict',tr); document.addEventListener('i18n:applied',tr);
  all('.side a').forEach(function(a){ a.onclick=function(){
    [].slice.call(a.parentNode.querySelectorAll('a')).forEach(function(x){ x.classList.remove('on'); });
    a.classList.add('on'); }; });
})();
</script>
<script>
(function(){
  function cp(txt,btn,label){
    var done=function(){ if(!btn)return; var o=btn.textContent; btn.textContent='已复制'; setTimeout(function(){btn.textContent=o;},1400); };
    if(navigator.clipboard&&navigator.clipboard.writeText){ navigator.clipboard.writeText(txt).then(done,function(){}); return; }
    var ta=document.createElement('textarea'); ta.value=txt; ta.style.position='fixed'; ta.style.opacity='0';
    document.body.appendChild(ta); ta.select(); try{document.execCommand('copy');done();}catch(e){} document.body.removeChild(ta);
  }
  var t=document.getElementById('tokTpl'), p=document.getElementById('promptTpl');
  var bt=document.getElementById('copyTok'), bp=document.getElementById('copyPrompt');
  if(bt&&t) bt.onclick=function(){ cp(t.content.textContent,bt); };
  if(bp&&p) bp.onclick=function(){ cp(p.content.textContent,bp,'已复制，粘给 AI 即可'); };
  var hm=document.getElementById('howModal'), hb=document.getElementById('howBtn'), hc=document.getElementById('howClose');
  if(hb&&hm) hb.onclick=function(){ hm.hidden=false; };
  if(hc&&hm) hc.onclick=function(){ hm.hidden=true; };
  if(hm) hm.addEventListener('click',function(e){ if(e.target===hm) hm.hidden=true; });
  document.addEventListener('keydown',function(e){ if(e.key==='Escape'&&hm) hm.hidden=true; });
})();
</script>
</body></html>""")



IMGFX = {
 1: ("grayscale(1) contrast(1.18)", 0.12),
 2: ("grayscale(1) contrast(1.06)", 0),
 3: ("saturate(.85) sepia(.14) brightness(1.03)", 0),
 4: ("grayscale(1) contrast(1.22) brightness(.82)", 0.20),
 5: ("saturate(1.1) brightness(.92)", 0),
 6: ("saturate(1.25) contrast(1.12)", 0),
 7: ("grayscale(.65) brightness(1.06)", 0),
 8: ("grayscale(1) contrast(1.3)", 0),
 9: ("saturate(1.18) brightness(1.02)", 0),
 10: ("saturate(1.05) contrast(1.05)", 0),
 11: ("saturate(1.45)", 0),
 12: ("brightness(.72) contrast(1.15) saturate(.9)", 0),
 13: ("none", 0),
 14: ("saturate(1.15) sepia(.1)", 0),
 15: ("saturate(1.2) brightness(.9)", 0),
 16: ("hue-rotate(-10deg) saturate(1.3) brightness(.9)", 0),
 17: ("saturate(1.2) contrast(1.05)", 0),
 18: ("saturate(1.15) brightness(.85)", 0),
 19: ("contrast(1.18) brightness(.85)", 0),
 20: ("none", 0),
 21: ("none", 0),
 22: ("grayscale(1) opacity(.9)", 0),
 23: ("saturate(.95) brightness(1.03)", 0),
 24: ("saturate(1.35) contrast(1.1)", 0),
 25: ("saturate(1.05)", 0),
 26: ("saturate(1.5) brightness(1.08) hue-rotate(-8deg)", 0),
 27: ("saturate(1.4) contrast(1.25) brightness(.8)", 0.42),
 28: ("saturate(1.05) brightness(1.02)", 0),
 29: ("saturate(1.5) contrast(1.15)", 0),
 30: ("hue-rotate(32deg) saturate(1.5) brightness(.9)", 0.25),
 31: ("none", 0),
 32: ("grayscale(1) contrast(1.12)", 0),
 33: ("grayscale(1) contrast(1.3) brightness(.78)", 0),
 34: ("sepia(.16) saturate(1.1)", 0),
 35: ("grayscale(1) contrast(1.15)", 0),
 36: ("grayscale(.55) brightness(.7) contrast(1.1)", 0.38),
 37: ("saturate(1.1)", 0),
 38: ("brightness(.78) saturate(1.1)", 0),
 39: ("grayscale(1) contrast(1.22) brightness(1.04)", 0),
 40: ("saturate(1.6) contrast(1.15)", 0),
 41: ("saturate(1.1) hue-rotate(-8deg)", 0),
 42: ("grayscale(1)", 0),
 43: ("sepia(.26) saturate(1.05)", 0),
 44: ("saturate(1.14) sepia(.08)", 0),
 45: ("brightness(.75) saturate(1.2)", 0.28),
 46: ("brightness(.58) saturate(.8)", 0.32),
 47: ("brightness(1.02)", 0),
 48: ("saturate(1.25) brightness(.85)", 0.26),
 49: ("contrast(1.2) brightness(.9)", 0.22),
 50: ("sepia(.35) saturate(.85) contrast(1.05)", 0),
}

def img_css(sid):
    f, d = IMGFX.get(sid, ("none", 0))
    return "\nbody{--imgf:%s;--duo:%s}\n" % (f, d)


RAILDATA = json.dumps([[f"{x['id']:02d}", x["cn"], SLUGS[x["id"]]] for x in STYLES],
                      ensure_ascii=False, separators=(",", ":"))


def build_module(key, sid):
    if key == "gallery":
        return m_gallery(bento=sid in (25, 37))
    return MODS[key]()


order = [s["id"] for s in STYLES]
for i, sid in enumerate(order):
    s = BY_ID[sid]
    th = THEMES[sid]
    slug = SLUGS[sid]
    nxt = SLUGS[order[(i + 1) % len(order)]] + ".html"
    layout = th["layout"]
    cls = "" if layout == "left" else (" center" if layout == "center" else " split")
    out = TPL.substitute(
        no=f"{sid:02d}", cn=s["cn"], en=s["en"], next=nxt, layoutcls=cls,
        deco=th["deco"], raw=th["raw"], raw2=XRAW.get(sid, "") + img_css(sid),
        modcss=MODCSS, brandi=th["brandi"],
        sig=build_module(SIG[sid], sid), con=build_module(CON[sid], sid),
        strip="" if "gallery" in (SIG[sid], CON[sid]) else m_strip(sid),
        sheetcss=BC.CSS + chr(10) + th["raw"] + chr(10) + XRAW.get(sid, "") + chr(10) + BC.PANEL_FX.get(sid, ""),
        sheetbody=BC.BODY,
        raildata=RAILDATA, slug=slug,
        tokencss=":root{ --bg:%s; --surface:%s; --ink:%s; --muted:%s; --line:%s; --accent:%s; --on-accent:%s; --radius:%s }" % (
            th["bg"], th["surface"], th["ink"], th["muted"], th["line"], th["accent"], th["on_accent"], th["radius"]),
        prompt=(
            "请用「%s」（%s）这套视觉风格，帮我做一个页面。\n\n"
            "它长什么样：%s\n"
            "要抓住这几点：%s\n\n"
            "配色（直接用这些值）：\n"
            "  背景 %s｜卡片 %s｜文字 %s｜强调色 %s\n"
            "形状：\n"
            "  圆角 %s｜卡片边 %s｜卡片阴影 %s\n\n"
            "不要出现：%s\n\n"
            "我的需求：<在这里写你要做的页面，比如「一个卖咖啡的落地页，要有首屏、三个卖点、价格表」>"
        ) % (s["cn"], s["en"], s["desc"], s["feat"], th["bg"], th["surface"],
             th["ink"], th["accent"], th["radius"], th["cardborder"], th["shadow"],
             ANTI_TXT.get(sid, "")),
        **{k: th[k] for k in (
            "bg", "bgimg", "surface", "ink", "muted", "line", "accent", "on_accent",
            "radius", "cardpad", "cardborder", "shadow", "btnradius", "btnshadow",
            "btnborder", "ghostborder", "fonth", "fontb", "fontk", "lsh", "lhh",
            "h1w", "h1size", "ttk", "lsk", "cardgap", "navborder", "leadfs")}
    )
    out = out.replace('<section class="sec">', '<section class="sec" data-reveal>')
    out = out.replace('<section class="sec secFull">', '<section class="sec secFull" data-reveal>')
    with open(os.path.join(DEMOS, slug + ".html"), "w", encoding="utf-8") as f:
        f.write(out)

# ---------------- gallery ----------------
GNAMES = {}
for s in STYLES:
    GNAMES[s["group"]] = s["groupName"]

items, chips = [], []
for gid, gname in GNAMES.items():
    n = sum(1 for s in STYLES if s["group"] == gid)
    chips.append(f'<button class="chip" data-g="{gid}">{H.escape(gname)} <em>{n}</em></button>')
for s in STYLES:
    slug = SLUGS[s["id"]]
    items.append(f'''<figure class="cell" data-g="{s["group"]}" data-k="{H.escape((s["cn"]+s["en"]+s["feat"]).lower())}">
  <a class="thumb" href="demos/{slug}.html">
    <iframe src="demos/{slug}.html?embed=1" loading="lazy" scrolling="no" tabindex="-1" title="{H.escape(s["cn"])}"></iframe>
  </a>
  <figcaption>
    <span class="num">{s["id"]:02d}</span>
    <span class="nm"><b>{H.escape(s["cn"])}</b><i>{H.escape(s["en"])}</i></span>
    <a class="open" href="demos/{slug}.html">打开 →</a>
  </figcaption>
</figure>''')

GAL = f'''<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>前端设计风格大全 · 视觉预览</title>
<style>
:root{{--paper:#fbfbf8;--ink:#15150f;--muted:#6d6d63;--line:#e2e1d9;--accent:#1d4ed8;--hl:#e9f0ff;
  --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);line-height:1.6;
  font-family:"PingFang SC","HarmonyOS Sans SC","Noto Sans SC",-apple-system,system-ui,sans-serif;
  -webkit-font-smoothing:antialiased}}
.wrap{{max-width:1320px;margin:0 auto;padding:56px 32px 90px}}
header{{border-bottom:2px solid var(--ink);padding-bottom:22px;margin-bottom:24px}}
.kicker{{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}}
h1{{font-size:clamp(28px,4vw,44px);line-height:1.12;letter-spacing:-.03em;margin:14px 0 10px;font-weight:800}}
h1 em{{font-style:normal;color:var(--accent)}}
.sub{{color:var(--muted);font-size:13.5px;max-width:820px}}
.sub a{{color:var(--accent);text-decoration:none;border-bottom:1px solid #c7d5f5}}
.toolbar{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:24px 0 12px}}
.chip{{font:inherit;font-size:12.5px;padding:6px 12px;border-radius:999px;cursor:pointer;
  border:1px solid var(--line);background:#fff;color:#3c3c34;transition:.15s}}
.chip em{{font-style:normal;font-family:var(--mono);font-size:11px;color:var(--muted);margin-left:4px}}
.chip:hover{{border-color:#b9b8ad}}
.chip.on{{background:var(--ink);color:#fff;border-color:var(--ink)}}
.chip.on em{{color:#bdbdb2}}
.count{{font-family:var(--mono);font-size:11.5px;color:var(--muted);margin:4px 0 20px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(330px,1fr));gap:26px 22px}}
.cell{{margin:0}}
.thumb{{display:block;position:relative;overflow:hidden;border-radius:10px;border:1px solid var(--line);
  aspect-ratio:1240/1020;background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.04);transition:.18s}}
.thumb:hover{{border-color:#b9b8ad;box-shadow:0 6px 18px rgba(0,0,0,.10)}}
.thumb iframe{{position:absolute;top:0;left:0;width:1240px;height:1020px;border:0;
  transform-origin:0 0;pointer-events:none;background:#fff}}
figcaption{{display:flex;align-items:baseline;gap:10px;padding:9px 2px 0}}
.num{{font-family:var(--mono);font-size:11px;color:#a3a399}}
.nm{{display:flex;flex-direction:column;min-width:0}}
.nm b{{font-size:13.5px;letter-spacing:-.01em}}
.nm i{{font-style:normal;font-family:var(--mono);font-size:10.5px;color:var(--muted);margin-top:1px;
  white-space:nowrap;overflow:hidden;text-overflow:ellipsis}}
.open{{margin-left:auto;font-size:12px;color:var(--accent);text-decoration:none;white-space:nowrap}}
.open:hover{{text-decoration:underline}}
.cell.hide{{display:none}}
footer{{margin-top:44px;padding-top:18px;border-top:1px solid var(--line);
  font-size:12px;color:var(--muted);font-family:var(--mono)}}
@media (max-width:640px){{.wrap{{padding:36px 16px 60px}}.grid{{grid-template-columns:1fr}}}}
</style></head><body><div class="wrap">
<header>
  <div class="kicker">Visual Preview · 50 Design Styles</div>
  <h1>前端设计风格大全，<em>先看长什么样</em></h1>
  <p class="sub">每格是同一段内容的真实渲染，共 <strong>8 段</strong>：导航（粘性＋面包屑）→ Hero → 组件区（按钮/输入/开关/进度/徽章）→ 特性卡片 → 风格专属模块（跑马灯、索引、代码窗、物品栏、Win95 窗口、雷达、贴纸、玻璃堆叠…）→ 内容模块（真实照片、表格、图表、正文）→ <strong>交互与状态</strong>（tab 切页、步骤条、拖拽上传、空/载入/错误/完成、Toast、弹窗）→ 页脚。缩略图只显示首屏，<strong>点格子看完整页面</strong>。</p>
</header>
<div class="toolbar"><button class="chip on" data-g="all">全部 <em>50</em></button>{''.join(chips)}</div>
<div class="count" id="count">显示 50 / 50</div>
<div class="grid" id="grid">
{''.join(items)}
</div>
<footer>50 demos · 同一套文案 / 同一批照片，50 套视觉语言 · 8 段结构 · 点击缩略图打开完整页面</footer>
</div>
<script>
const cells=[...document.querySelectorAll('.cell')],chips=[...document.querySelectorAll('.chip')],
      cnt=document.getElementById('count');let g='all';
function fit(){{
  document.querySelectorAll('.thumb').forEach(t=>{{
    const s=t.clientWidth/1240;const f=t.firstElementChild;
    if(f)f.style.transform='scale('+s+')';
  }});
}}
function render(){{
  let n=0;
  cells.forEach(c=>{{const ok=(g==='all'||c.dataset.g===g);
    c.classList.toggle('hide',!ok);if(ok)n++;}});
  cnt.textContent='显示 '+n+' / 50';fit();
}}
chips.forEach(c=>c.onclick=()=>{{chips.forEach(x=>x.classList.remove('on'));c.classList.add('on');g=c.dataset.g;render();}});
window.addEventListener('resize',fit);
window.addEventListener('load',fit);
requestAnimationFrame(fit);
</script></body></html>'''

with open(os.path.join(OUT, "previews.html"), "w", encoding="utf-8") as f:
    f.write(GAL)

print("demos:", len(os.listdir(DEMOS)), "| previews.html ok")
