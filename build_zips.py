# -*- coding: utf-8 -*-
"""为每种风格打一个自包含 zip：spec + prompt + theme.css + demo + 图片 + 预览图。"""
import io, json, os, re, shutil, zipfile
from PIL import Image

from themes import THEMES, SLUGS
from build_bundle import (STYLES, IMGFX, ANTI, SPECIAL, comp,
                          font_kind, contrast, FONT_CN)

OUT = os.path.dirname(os.path.abspath(__file__))
ZIPS = os.path.join(OUT, "assets", "zips")
ZIMG = os.path.join(OUT, "assets", "zipimg")
os.makedirs(ZIPS, exist_ok=True)
os.makedirs(ZIMG, exist_ok=True)

# ---------- 图片压到适合投喂的尺寸 ----------
def prep_images():
    for i in range(1, 13):
        src = os.path.join(OUT, "assets", "img%d.jpg" % i)
        dst = os.path.join(ZIMG, "%02d.jpg" % i)
        if not (os.path.exists(src) and not os.path.exists(dst)):
            continue
        im = Image.open(src).convert("RGB").resize((480, 360), Image.LANCZOS)
        im.save(dst, "JPEG", quality=70, optimize=True)



HOWTO = """<!doctype html><html lang="zh-CN"><meta charset="utf-8"><title>怎么用这个风格包</title>
<style>body{{margin:0;background:#fbfbf8;color:#15150f;font:16px/1.7 "PingFang SC",system-ui,sans-serif}}
.wrap{{max-width:720px;margin:0 auto;padding:56px 24px 80px}}
h1{{font-size:30px;margin:0 0 8px}}p.sub{{color:#6d6d63;margin:0 0 28px}}
.step{{display:flex;gap:14px;margin:18px 0;padding:16px 18px;background:#fff;border:1px solid #e2e1d9;border-radius:12px}}
.n{{flex:0 0 auto;width:26px;height:26px;border-radius:50%;background:#15150f;color:#fff;display:grid;place-items:center;font-size:13px}}
b{{display:block;margin-bottom:2px}}small{{color:#6d6d63}}
table{{width:100%;border-collapse:collapse;margin-top:26px;font-size:14px}}
td,th{{text-align:left;padding:9px 10px;border-bottom:1px solid #e2e1d9}}th{{color:#6d6d63;font-size:12px}}
code{{background:#f0efe7;padding:1px 6px;border-radius:4px;font-size:13px}}</style>
<div class="wrap"><h1>怎么用这个风格包</h1>
<p class="sub">「{cn}」· 三步拿走。</p>
<div class="step"><span class="n">1</span><div><b>先看效果</b><small>双击 demo.html，这就是这套风格的完整页面（含 105 个组件）。</small></div></div>
<div class="step"><span class="n">2</span><div><b>做自己的页面</b><small>打开「给AI的话.txt」，整段复制给任意 AI，把最后一行换成你的需求。</small></div></div>
<div class="step"><span class="n">3</span><div><b>（可选）自己改代码</b><small>spec.md 是规格卡，theme.css 是现成的 CSS 变量与组件样式。</small></div></div>
<table><tr><th>文件</th><th>是什么</th></tr>
<tr><td><code>demo.html</code></td><td>完整样例页（落地页 + 组件总览）</td></tr>
<tr><td><code>给AI的话.txt</code></td><td>复制给 AI 的提示词，已填好风格参数</td></tr>
<tr><td><code>spec.md</code></td><td>规格卡：颜色、圆角、阴影、禁止项</td></tr>
<tr><td><code>theme.css</code></td><td>可直接引入的变量与基础组件样式</td></tr>
<tr><td><code>preview.jpg</code></td><td>首屏截图</td></tr></table>
</div></html>"""

ROOT_README = """# {cn} · {en}

一个可以「直接投喂给 AI」的风格包。包里没有废话，只有模型做对这一风格需要的东西。

## 里面有什么

| 文件 | 作用 |
|---|---|
| （组件已内嵌） | `demo.html` 里就包含 **105 个组件**，锚点 `#components` 直接跳 |
| `怎么用.html` | **先看这个**：三步拿走（双击用浏览器打开） |
| `给AI的话.txt` | 复制给 AI 的提示词，已填好参数 |
| `demo.html` | 该风格的完整样例页（8 段：导航/hero/组件/卡片/影像/专属模块/交互状态/页脚）。**这是"像"的基准** |
| `preview.jpg` | 首屏截图，用来快速锚定视觉 |
| `spec.md` | 规格卡：tokens / 必用手法 / 组件配方 / 禁止清单 / 无障碍 / 影像 |
| `spec.json` | 同上的机器读版本（写脚本或做 token 生成器时用） |
| `theme.css` | 由 tokens 生成的即用样式表，可直接 `@import` |
| `prompt.md` | 已经填好风格名的提示词，复制粘贴即可 |
| `assets/` | demo.html 用到的照片（已本地化，离线可看） |

## 三步用起来

1. **看**：双击 `demo.html`，确认这就是你要的感觉（`preview.jpg` 是首屏缩略）。
2. **喂**：把 `spec.md` + `prompt.md` 一起粘给 AI；想更稳就再加一句「参考 `demo.html` 的结构，但内容全部换掉」。
3. **改**：把你的需求填进 `prompt.md` 最后一行，让它出你真正要的页面。

## 注意

- `demo.html` 里的文案、品牌名、区块顺序都是**占位内容**，不是这个风格的一部分。要让 AI 换掉。
- 规格里没覆盖到的组件（日期选择器、分页器、树形菜单…），让 AI **先申报打算怎么做**，不要它自己发明。
- 改了 `assets/` 里没有的字体或图片时，记得把依赖一起带走。
"""

PROMPT_TMPL = """请用「{cn}」（{en}）这套视觉风格，帮我做一个页面。

它长什么样：{desc}
要抓住这几点：{feat}

配色（直接用这些值）：
  背景 {bg}｜卡片 {surface}｜文字 {ink}｜强调色 {accent}
形状：
  圆角 {radius}｜卡片边 {cardborder}｜卡片阴影 {shadow}

不要出现：{anti}

我的需求：<在这里写你要做的页面，比如「一个卖咖啡的落地页，要有首屏、三个卖点、价格表」>
"""

SPEC_TPL = """# {no} {cn} · {en}

> {desc}

- 分组：{group}
- 参考站点：{sites}
- 样例页：`demo.html`（截图 `preview.jpg`）

## 1. Tokens

| 角色 | 值 |
|---|---|
| 背景 `--bg` | `{bg}` |
| 表面 `--surface` | `{surface}` |
| 文字 `--ink` | `{ink}` |
| 次要文字 `--muted` | `{muted}` |
| 分割线 `--line` | `{line}` |
| 主色 `--accent` | `{accent}` |
| 主色上的字 `--on-accent` | `{on_accent}` |
| 圆角 `--radius` | `{radius}` |
| 卡片边 | `{cardborder}` |
| 卡片影 | `{shadow}` |
| 按钮边 | `{btnborder}` |
| 按钮影 | `{btnshadow}` |

字体：
- 标题：{fonth}，字重 {h1w}，行高 {lhh}，字距 {lsh}
- 元信息/小标签：{fontk}，{ttk} {lsk}

## 2. 必用手法

{moves}

## 3. 组件配方

{comp}

实现的 CSS 见同目录 `theme.css`（已经是可用的变量 + 组件基础样式）。

## 4. 关键实现

{special}

## 5. 禁止清单

{anti}

## 6. 无障碍

- 正文对比：**{cbg}:1**
- 主色底字：**{cacc}:1**
- focus：≥2px 实线 + offset 2px，禁止 `outline:none`
- 触摸目标：≥44px，间距 ≥8px
- 状态不能只靠颜色，必须带文字/图标

## 7. 影像处理

```css
.ph {{ filter: {imgf}; }}
```
{duotone}

## 8. 建议的验收

- [ ] 抽查 3 个元素，圆角/阴影/描边与 tokens 完全一致
- [ ] 主色没有溢出到正文
- [ ] 按钮有 hover / focus-visible / disabled 三态
- [ ] 表格 10 行以上不塌
- [ ] 空态、错误态、加载态都不是「暂无数据」四个字
- [ ] focus 环可见
"""


def css_vars(th):
    return f""":root{{
  --bg:{th['bg']};
  --surface:{th['surface']};
  --ink:{th['ink']};
  --muted:{th['muted']};
  --line:{th['line']};
  --accent:{th['accent']};
  --on-accent:{th['on_accent']};
  --radius:{th['radius']};
  --card-border:{th['cardborder']};
  --card-shadow:{th['shadow']};
  --btn-border:{th['btnborder']};
  --btn-shadow:{th['btnshadow']};
  --btn-radius:{th['btnradius']};
  --font-h:{th['fonth']};
  --font-k:{th['fontk']};
  --lh-h:{th['lhh']};
  --ls-h:{th['lsh']};
  --ls-k:{th['lsk']};
}}"""


THEME_CSS_TAIL = """
/* ---- 基础 ---- */
body{background:var(--bg);color:var(--ink);font-family:var(--font-h);-webkit-font-smoothing:antialiased}
h1,h2,h3{font-family:var(--font-h);font-weight:__HW__;line-height:var(--lh-h);letter-spacing:var(--ls-h);margin:0}
.kicker{font-family:var(--font-k);font-size:11px;letter-spacing:var(--ls-k);text-transform:__TT__;color:var(--muted)}

/* ---- 按钮 ---- */
.btn{background:var(--accent);color:var(--on-accent);border:var(--btn-border);border-radius:var(--btn-radius);
  box-shadow:var(--btn-shadow);padding:12px 24px;font-weight:600;cursor:pointer}
.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line);box-shadow:none}
.btn:disabled{opacity:.42;pointer-events:none}
.btn:focus-visible{outline:2px solid var(--accent);outline-offset:2px}

/* ---- 输入 ---- */
.inp{background:var(--bg);color:var(--ink);border:1px solid var(--line);border-radius:var(--btn-radius);padding:10px 14px}
.inp:focus{outline:2px solid var(--accent);outline-offset:2px}
.inp::placeholder{color:var(--muted);opacity:.75}

/* ---- 卡片 ---- */
.card{background:var(--surface);border:var(--card-border);border-radius:var(--radius);
  box-shadow:var(--card-shadow);padding:24px}

/* ---- 徽章 ---- */
.badge{display:inline-block;font-family:var(--font-k);font-size:10px;letter-spacing:.08em;
  background:var(--accent);color:var(--on-accent);border-radius:999px;padding:2px 9px}
.badge.soft{background:transparent;color:var(--muted);border:1px solid var(--line)}

/* ---- 表格 ---- */
.tbl{width:100%;border-collapse:collapse;font-size:13px}
.tbl th{font-family:var(--font-k);font-size:10px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);text-align:left;padding:8px 10px;border-bottom:1px solid var(--line)}
.tbl td{padding:11px 10px;border-bottom:1px solid var(--line)}
"""


def build_one(d):
    sid = d["id"]
    th = THEMES[sid]
    slug = SLUGS[sid]
    f, duo = IMGFX.get(sid, ("none", 0))
    cbg = contrast(th["ink"], th["bg"])
    cacc = contrast(th["on_accent"], th["accent"])

    spec = SPEC_TPL.format(
        no=f"{sid:02d}", cn=d["cn"], en=d["en"], desc=d["desc"], group=d["groupName"],
        sites="、".join(d["sites"]),
        bg=th["bg"], surface=th["surface"], ink=th["ink"], muted=th["muted"], line=th["line"],
        accent=th["accent"], on_accent=th["on_accent"], radius=th["radius"],
        cardborder=th["cardborder"], shadow=th["shadow"],
        btnborder=th["btnborder"], btnshadow=th["btnshadow"],
        fonth=th["fonth"], h1w=th["h1w"], lhh=th["lhh"], lsh=th["lsh"], fontk=th["fontk"],
        ttk=th["ttk"], lsk=th["lsk"],
        moves="\n".join("- " + x.strip() for x in d["feat"].split("/") if x.strip()),
        comp=comp(th, sid),
        special=SPECIAL.get(sid, "（无特殊要求，按 tokens 与组件配方执行）"),
        anti="\n".join("- ❌ " + x.strip() for x in ANTI.get(sid, "—").split("、") if x.strip()),
        cbg=f"{cbg:.1f}", cacc=f"{cacc:.1f}",
        imgf=f,
        duotone=(f"主色双色调叠加：`mix-blend-mode:color` + `opacity:{duo}`" if duo else "无额外染色。"),
    )

    prompt = PROMPT_TMPL.format(
        cn=d["cn"], en=d["en"], desc=d["desc"], feat=d["feat"],
        bg=th["bg"], surface=th["surface"], ink=th["ink"], accent=th["accent"],
        radius=th["radius"], cardborder=th["cardborder"], shadow=th["shadow"],
        anti=ANTI.get(sid, ""),
    )

    css = css_vars(th) + THEME_CSS_TAIL.replace("__HW__", th["h1w"]).replace(
        "__TT__", th["ttk"] if th["ttk"] != "none" else "none")

    # demo.html：去掉左侧导航外壳，图片路径改为包内路径
    html = io.open(os.path.join(OUT, "demos", slug + ".html"), encoding="utf-8").read()
    html = re.sub(r'<div class="rail" id="rail">.*?(?=<div class="frame">)', "", html, flags=re.S)
    html = re.sub(r'<script>\s*\(function\(\)\{\s*var EMBED.*?\}\)\(\);\s*</script>', "", html, flags=re.S)
    imgs = sorted(set(re.findall(r"assets/img(\d+)\.jpg", html)))
    html = html.replace("../assets/img", "assets/img")
    html = html.replace("../50-frontend-styles.html", "#")
    html = re.sub(r'\s*<a class="railFoot dl".*?</a>', "", html, flags=re.S)
    html = re.sub(r'/\* RAIL-CSS-START.*?/\* RAIL-CSS-END \*/', "", html, flags=re.S)
    # 包内是本地文件，运行时 i18n 走 fetch 会被 CORS 拦，去掉脚本与语言切换器
    html = re.sub(r'\s*<script src="\.\./assets/i18n\.js"[^>]*></script>', "", html)
    html = re.sub(r'\s*<span id="langSwitch"></span>', "", html)
    html = html.replace('"%s-components.html"' % slug, '"components.html"')

    def clean_comp(fname):
        h = io.open(os.path.join(OUT, "demos", fname), encoding="utf-8").read()
        h = h.replace("../assets/img", "assets/img")
        h = h.replace('"%s-components-biz.html"' % slug, '"components-biz.html"')
        h = h.replace('"%s-components.html"' % slug, '"components.html"')
        h = h.replace('"%s.html"' % slug, '"demo.html"')
        h = re.sub(r'\s*<a class="btn ghost sm" href="\.\./assets/zips/.*?</a>', "", h, flags=re.S)
        h = re.sub(r'<div class="rail" id="rail">.*?(?=<div class="topbar">)', "", h, flags=re.S)
        h = re.sub(r'/\* RAIL-CSS-START.*?/\* RAIL-CSS-END \*/', "", h, flags=re.S)
        h = re.sub(r'<script>\s*\(function\(\)\{\s*var EMBED.*?\}\)\(\);\s*</script>', "", h, flags=re.S)
        return h


    name = f"{sid:02d}-{slug.split('-', 1)[1]}"
    zpath = os.path.join(ZIPS, "style-%s.zip" % name)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        base = name + "/"
        z.writestr(base + "README.md", ROOT_README.format(cn=d["cn"], en=d["en"]))
        z.writestr(base + "怎么用.html", HOWTO.format(cn=d["cn"]))
        z.writestr(base + "给AI的话.txt", prompt)
        z.writestr(base + "prompt.md", prompt)
        z.writestr(base + "spec.md", spec)
        z.writestr(base + "spec.json", json.dumps({
            "id": f"{sid:02d}", "name": d["cn"], "nameEn": d["en"],
            "group": d["groupName"], "oneLiner": d["desc"],
            "tokens": {k: th[k] for k in ("bg", "surface", "ink", "muted", "line", "accent",
                                          "on_accent", "radius", "cardborder", "shadow",
                                          "btnborder", "btnshadow", "btnradius")},
            "moves": [x.strip() for x in d["feat"].split("/") if x.strip()],
            "antiPatterns": [x.strip() for x in ANTI.get(sid, "").split("、") if x.strip()],
            "implementation": SPECIAL.get(sid, ""),
            "a11y": {"contrastInkOnBg": round(cbg, 1), "contrastOnAccent": round(cacc, 1)},
            "imagery": {"filter": f, "duotone": duo},
            "references": d["sites"],
        }, ensure_ascii=False, indent=1))
        z.writestr(base + "theme.css", css)
        z.writestr(base + "demo.html", html)
        z.write(os.path.join(OUT, "assets", "thumbs", "%02d.jpg" % sid), base + "preview.jpg")
        for n in imgs:
            z.write(os.path.join(ZIMG, "%02d.jpg" % int(n)), base + "assets/img%s.jpg" % n)
    return zpath


def main():
    prep_images()
    total = 0
    for d in STYLES:
        p = build_one(d)
        total += os.path.getsize(p)
    print("zips:", len(STYLES), "| total %.1f MB" % (total / 1024 / 1024),
          "| avg %.0f KB" % (total / len(STYLES) / 1024))


if __name__ == "__main__":
    main()
