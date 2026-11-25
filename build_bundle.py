# -*- coding: utf-8 -*-
"""把 50 个风格压成一份可一次性投喂给 AI 的 bundle（md + json）。

数据来源：
  styles.json  -> 名称/分组/一句话/必用手法/参考站点
  themes.py    -> tokens（颜色/形状/字体）
  build_demos.py 里的 IMGFX -> 影像滤镜
"""
import ast, io, json, os, re

OUT = os.path.dirname(os.path.abspath(__file__))
from themes import THEMES, SLUGS

STYLES = json.load(open(os.path.join(OUT, "styles.json"), encoding="utf-8"))

# ---- 从 build_demos.py 里抠出 IMGFX（避免 import 触发整站生成）----
_src = io.open(os.path.join(OUT, "build_demos.py"), encoding="utf-8").read()
_m = re.search(r"IMGFX = (\{.*?\n\})", _src, re.S)
IMGFX = ast.literal_eval(_m.group(1)) if _m else {}

# ---- 每个风格手写的「禁止」清单（代码推不出来的部分）----
ANTI = {
1: "任何圆角、模糊阴影、渐变、浅灰文字、衬线字体",
2: "圆角、卡片阴影、装饰图形、居中对称的居中排版",
3: "高饱和撞色、粗黑边、重阴影、等宽标题",
4: "衬线字体、圆角、亮色块、摄影图当主视觉",
5: "不透明实心卡片、无模糊、暖色调、细边框",
6: "圆角、抗锯齿渐变、细字重、彩色渐变",
7: "硬阴影、深色底、高对比描边、高饱和色",
8: "圆角、扁平阴影、现代无衬线、渐变",
9: "纯黑、高饱和荧光、直角、重投影",
10: "扁平无层次、零阴影、纯二维色块",
11: "低饱和、细边框、留白过多、灰度照片",
12: "任何非黑背景、浅灰卡片、彩色强调色",
13: "低对比、细边框、隐藏 focus、仅靠颜色传信息",
14: "尖角、硬阴影、高饱和、1px 细边框",
15: "纯色背景、不透明卡片、暖色、硬边",
16: "冷灰、无发光、扁平无辉光、极简排版",
17: "任何阴影、渐变、拟物质感、长投影",
18: "不透明卡片、硬边、纯色底、重描边",
19: "静态无反馈、无过渡、纯色平涂",
20: "跳变式状态切换、无过渡、强装饰",
21: "低对比、隐藏 focus、小触摸目标、仅靠颜色",
22: "边框、阴影、装饰元素、多层级",
23: "硬阴影、纯黑、高饱和、直角",
24: "灰白底、冷色、细边框、保守排版",
25: "边框、浓阴影、非对齐、杂乱拼贴",
26: "暗色、低饱和、直角、无高光",
27: "白底、圆角、柔和阴影、低饱和",
28: "高饱和撞色、重描边、暗色底",
29: "克制配色、无装饰、直角、极简",
30: "亮色、锐利清晰、直角、无噪点",
31: "扁平无层次、零阴影、纯色块",
32: "阴影、圆角、装饰图形、彩色强调",
33: "小字号、多层信息、装饰插图、柔和配色",
34: "纯色平铺、无纵深、扁平",
35: "阴影、圆角、装饰图形、多色",
36: "圆角、柔和阴影、亮色、衬线字体",
37: "边框、重阴影、低饱和、直角",
38: "不透明面板、硬边、纯色底、重描边",
39: "阴影、彩色强调、动效、渐变",
40: "克制、统一、对称、极简",
41: "纯几何、硬边、高对比黑白",
42: "圆角、渐变、精修阴影、装饰",
43: "纯数字质感、无触感、扁平、高饱和",
44: "高饱和、强对比、装饰图形",
45: "默认光标、静态页面、无 hover 反馈",
46: "密集信息、多个并列按钮、无主焦点",
47: "杂乱背景、多彩、装饰元素",
48: "纯色背景、不透明卡片、硬边",
49: "柔和配色、圆角、低对比、无错位",
50: "纯白、高饱和、锐利边缘、无颗粒",
}

# ---- 代码推不出来的关键实现细节（没写就用通用规则）----
SPECIAL = {
1: "点阵底纹 16px；硬影偏移 5–6px，模糊恒为 0",
2: "零圆角 + 非对称 4+8 栅格 + 全站只有一个强调红",
6: "方块 inset 边框（亮/暗双色）+ 16px 网格对齐",
7: "同色背景 + 双向软阴影（暗右下/亮左上），按压用 inset",
8: "双色 inset 立体边框模拟凸起；标题栏 #000080；任务栏",
9: "radial-gradient 光斑模拟树影；页眉底部 3px 绿线",
10: "perspective 1000px + 多层光照阴影",
14: "双向软阴影 + 24px 超大圆角；按压 inset",
15: "多层 radial-gradient 光斑 + blur(10px) 毛玻璃",
16: "霓虹发光 box-shadow 0 0 Npx；太空紫底",
18: "blur(20px) + 1px 高光描边 + 极透卡片",
19: "弹簧缓动 cubic-bezier(.34,1.56,.64,1)；必须做 reduced-motion 兜底",
26: "冰蓝→樱花粉渐变 + 磨砂卡片 + 金属高光",
27: "发光边框 box-shadow 0 0 12px neon + 文字辉光",
29: "彩色硬影交替（青/黑）+ 点阵贴纸装饰",
30: "粉紫霓虹 + CRT 扫描线 + 文字双色分离",
36: "四角角标框 + 环形雷达 + 等宽数据字",
38: "blur(20px) + 22px 圆角 + 微光玻璃轮廓",
40: "粗黑边 + 彩色硬影 + 30px 胶囊按钮",
41: "绿灰纵向渐变 + 半透明卡片 + 不规则有机圆角",
49: "红/绿/蓝三色错位描边 + hover 错位幅度加大",
50: "胶片颗粒叠加层 + 深棕页眉 + 古铜按钮",
}

FONT_CN = {"serif": "衬线（Georgia/宋体）", "mono": "等宽", "sans": "无衬线（系统/PingFang）"}


def font_kind(stack: str) -> str:
    s = stack.lower()
    if "georgia" in s or "songti" in s or "serif" in s and "sans-serif" not in s:
        return "serif"
    if "mono" in s:
        return "mono"
    return "sans"


def rgb(hexs: str):
    h = hexs.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lum(hexs: str) -> float:
    def f(c):
        c = c / 255
        return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    r, g, b = rgb(hexs)
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def contrast(a: str, b: str) -> float:
    l1, l2 = sorted([lum(a), lum(b)], reverse=True)
    return (l1 + 0.05) / (l2 + 0.05)


def comp(th, style_id):
    """从 tokens 生成组件配方的一句话描述。"""
    btn_shadow = th["btnshadow"]
    if btn_shadow == "none":
        shadow_kind = "无阴影"
    elif re.search(r"^\s*0\s+0\s+\d+px\s+rgba", btn_shadow):
        shadow_kind = "发光（无偏移）"
    elif re.search(r"^\s*-?\d+px\s+-?\d+px\s+0\b", btn_shadow):
        shadow_kind = "硬影（模糊 0）"
    else:
        shadow_kind = "柔和阴影"

    def edge(v):
        return "无边框" if v in ("0", "none", "0 none") else v

    def shad(v):
        return "无阴影" if v in ("none", "0") else v

    def rad(v):
        return "零圆角" if v in ("0", "0px", "none") else f"圆角 {v}"

    return (
        f"按钮=底 {th['accent']} + 字 {th['on_accent']} + {edge(th['btnborder'])} + {shadow_kind}；"
        f"输入=底 {th['bg']} + 边 1px {th['line']} + {rad(th['btnradius'])}；"
        f"卡片=底 {th['surface']} + {edge(th['cardborder'])} + {rad(th['radius'])} + {shad(th['shadow'])}；"
        f"表格=表头/行底边 1px {th['line']}"
    )


def block(d):
    sid = d["id"]
    th = THEMES[sid]
    f, duo = IMGFX.get(sid, ("none", 0))
    c_ink_bg = contrast(th["ink"], th["bg"])
    c_ink_acc = contrast(th["on_accent"], th["accent"])
    fh = font_kind(th["fonth"])
    lines = []
    lines.append(f"### {sid:02d} {d['cn']} · {d['en']}")
    lines.append(f"- 分组：{d['groupName']}")
    lines.append(f"- 定位：{d['desc']}")
    lines.append("- tokens："
                 f"bg `{th['bg']}` · surface `{th['surface']}` · ink `{th['ink']}` · muted `{th['muted']}` · "
                 f"line `{th['line']}` · accent `{th['accent']}` · on-accent `{th['on_accent']}`")
    lines.append("- 形状："
                 f"圆角 `{th['radius']}` · 卡片边 `{th['cardborder']}` · 卡片影 `{th['shadow']}` · "
                 f"按钮边 `{th['btnborder']}` · 按钮影 `{th['btnshadow']}`")
    lines.append("- 字体："
                 f"标题 {FONT_CN[fh]} {th['h1w']} · 元信息等宽 · "
                 f"行高 {th['lhh']} · 标题字距 {th['lsh']} · 小标签 {'大写 ' if th['ttk']=='uppercase' else ''}{th['lsk']}")
    lines.append(f"- 必用手法：{d['feat']}")
    lines.append(f"- 组件：{comp(th, sid)}")
    if sid in SPECIAL:
        lines.append(f"- 关键实现：{SPECIAL[sid]}")
    lines.append(f"- 禁止：{ANTI.get(sid, '—')}")
    a11y = f"正文对比 {c_ink_bg:.1f}:1 / 主色底字 {c_ink_acc:.1f}:1"
    if c_ink_bg < 4.5 or c_ink_acc < 4.5:
        a11y += "（偏低，需加深文字或用描边补强）"
    lines.append(f"- 无障碍：{a11y}；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px")
    lines.append(f"- 影像：`filter:{f}`" + (f" + 主色双色调 opacity {duo}" if duo else ""))
    lines.append(f"- 参考：{'、'.join(d['sites'])}")
    lines.append(f"- 样例页：`demos/{SLUGS[sid]}.html`")
    return "\n".join(lines)


HEADER = """# 前端设计风格大全 · AI 投喂包（单文件全量）

> 一次投喂，覆盖全部风格。用法见文末「怎么用」。

每种风格给出：分组 / 定位 / tokens（色值·形状·字体）/ 必用手法 / 组件配方 / 关键实现 / 禁止清单 / 无障碍下限 / 影像滤镜 / 参考站点 / 样例页路径。

---

## 索引（按编号）

"""

FOOTER = """

---

## 怎么用（复制这一段当提示词开头）

```
下面是前端设计风格大全的规格库。请只使用我指定的那一种，不要混搭，也不要自创新颜色。

【指定风格】<填风格编号或名称，例如 27 / 赛博朋克>

【必须遵守】
1. 严格使用该风格的 tokens（色值、圆角、阴影、字体），不得新增颜色
2. 实现该风格的「必用手法」，至少 3 个
3. 一条都不能碰「禁止」清单
4. 满足「无障碍」下限；focus 必须可见
5. 我的页面里如果有规格没覆盖的组件（如日期选择器、分页器），
   先声明你打算怎么做，等我确认再写，不要自己发明

【输出流程】
1. 先复述你选中的 tokens 表
2. 再给页面骨架（只列区块，不带样式）
3. 最后逐区块实现

【任务】<你的真实需求，例如：做一个 SaaS 数据看板>
```

### 换风格只要改一行

把「指定风格」改成 `03 / 日系编辑美学`，其余不动。

### 想一次看多个

「请分别用 01、18、27 三种风格各出一版，共用同一套页面结构，只换 tokens 与组件规则」——单文件里都在，不用分开投。

### 想更稳

把对应的「样例页」也贴给它（`demos/NN-xxx.html`），加一句：
「参考这个页面的结构，但内容全部换掉，只保留 tokens 和组件规则。」
"""


def main():
    md = [HEADER]
    for d in STYLES:
        md.append(f"{d['id']:02d} {d['cn']} · {d['en']}（{d['groupName']}）")
    md.append("\n---\n")
    for d in STYLES:
        md.append(block(d))
        md.append("")
    md.append(FOOTER)
    text = "\n".join(md)
    with io.open(os.path.join(OUT, "styles-bundle.md"), "w", encoding="utf-8") as f:
        f.write(text)

    data = {"version": 1, "count": len(STYLES), "styles": []}
    for d in STYLES:
        sid = d["id"]
        th = THEMES[sid]
        f, duo = IMGFX.get(sid, ("none", 0))
        data["styles"].append({
            "id": f"{sid:02d}", "name": d["cn"], "nameEn": d["en"],
            "group": d["groupName"], "oneLiner": d["desc"],
            "tokens": {
                "bg": th["bg"], "surface": th["surface"], "ink": th["ink"],
                "muted": th["muted"], "line": th["line"],
                "accent": th["accent"], "onAccent": th["on_accent"],
                "radius": th["radius"], "cardBorder": th["cardborder"],
                "cardShadow": th["shadow"], "btnBorder": th["btnborder"],
                "btnShadow": th["btnshadow"],
                "fontHeading": th["fonth"], "fontMono": th["fontk"],
                "headingWeight": th["h1w"], "headingLineHeight": th["lhh"],
                "headingLetterSpacing": th["lsh"], "kickerLetterSpacing": th["lsk"],
            },
            "moves": [x.strip() for x in d["feat"].split("/") if x.strip()],
            "components": comp(th, sid),
            "implementation": SPECIAL.get(sid, ""),
            "antiPatterns": [x.strip() for x in ANTI.get(sid, "").split("、") if x.strip()],
            "a11y": {
                "contrastInkOnBg": round(contrast(th["ink"], th["bg"]), 1),
                "contrastOnAccent": round(contrast(th["on_accent"], th["accent"]), 1),
                "focus": "≥2px 实线 + offset 2px",
                "touchTarget": "≥44px",
            },
            "imagery": {"filter": f, "duotone": duo},
            "references": d["sites"],
            "assets": {"demo": f"demos/{SLUGS[sid]}.html", "thumb": f"assets/thumbs/{sid:02d}.jpg"},
        })
    with io.open(os.path.join(OUT, "styles-bundle.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    kb = len(text.encode("utf-8")) / 1024
    print(f"styles-bundle.md  {kb:.0f} KB  {len(text.splitlines())} lines")
    print(f"styles-bundle.json {os.path.getsize(os.path.join(OUT,'styles-bundle.json'))/1024:.0f} KB")


if __name__ == "__main__":
    main()
