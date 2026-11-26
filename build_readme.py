# -*- coding: utf-8 -*-
"""生成 README.md：读 styles.json，自动出 52 行表格，风格增减不用手改。

用法：python build_readme.py
发布到 GitHub 前，把下面的 OWNER / REPO 改成你的，再跑一次。
"""
import io, json, os

OWNER = "1981yangcq"     # ← 改成你的 GitHub 用户名
REPO = "frontend-style-pack"        # ← 仓库名
BASE = f"https://{OWNER}.github.io/{REPO}/"
REL = f"https://github.com/{OWNER}/{REPO}/releases/latest/download/"

OUT = os.path.dirname(os.path.abspath(__file__))
STYLES = json.load(open(os.path.join(OUT, "styles.json"), encoding="utf-8"))
SLUG = {s["id"]: s.get("slug") for s in STYLES}

# 从 themes.py 拿 slug（保持与 demo 文件名一致）
from themes import SLUGS

rows = []
for s in STYLES:
    slug = SLUGS[s["id"]]
    rows.append(
        f"| {s['id']:02d} | **{s['cn']}**<br><sub>{s['en']}</sub> | {s['desc']} | "
        f"[预览]({BASE}demos/{slug}.html) · [下载]({REL}style-{slug}.zip) |"
    )

N = len(STYLES)
README = f"""<div align="center">

# 前端设计风格大全 · Style Atlas

**按感觉挑一个，直接拿走。**

{N} 种前端设计风格：每张缩略图都是真实渲染的一屏，点进去就是完整页面（落地页 + 105 个组件），
下载一个 zip 就带走全部代码与规格。

[**🌐 在线预览**]({BASE}) · [**⬇ 下载风格包**]({REL.replace('latest/download/', '')}) · [**📖 怎么给 AI 用**](specs/README.md)

</div>

---

## 这是什么

做前端最常见的时间浪费，不是写代码，是**决定长什么样**：翻 Dribbble、扒 Awwwards、拼组件库、对齐颜色……
这里把「风格」整包做好：一套配色、一套圆角阴影、一套组件，**挑中就能用**。

三种用法：

| 你是谁 | 怎么用 |
|---|---|
| **只想快速要个页面** | 在线预览挑一个 → 下载 zip → 解压双击 `demo.html` 看效果 |
| **想让 AI 帮你做** | 点「复制给 AI 的话」，粘给任意 AI，最后一行换成你的需求 |
| **要自己改代码** | zip 里有 `spec.md`（规格卡）+ `theme.css`（现成变量与组件） |

> 不用先懂「新粗野主义」是什么。看图就行。

---

## 三步拿走

1. **看图挑一个** —— 首页支持按「明暗 / 软硬 / 繁简」筛，或者点 🎲 手气不错
2. **点「下载风格包」** —— 得到一个 zip，解压后双击 `怎么用.html` 或 `demo.html`
3. **想做自己的页面** —— 复制「给 AI 的话」，粘给 AI，改最后一行

---

## {N} 种风格

> 点「预览」看完整页面，点「下载」直接拿 zip。

| # | 风格 | 一句话 | 链接 |
|---|---|---|---|
{chr(10).join(rows)}

---

## 一个风格包里有什么

| 文件 | 说明 |
|---|---|
| `怎么用.html` | **先看这个**，三步说明（浏览器直接打开） |
| `demo.html` | 完整样例页：落地页 + 105 个组件，单文件自包含 |
| `给AI的话.txt` | 复制给 AI 的提示词，已填好该风格的配色与禁忌 |
| `spec.md` | 规格卡：tokens、必用手法、禁止清单、无障碍下限 |
| `spec.json` | 同上的机器读版本 |
| `theme.css` | 由 tokens 生成的现成样式表，可直接 `@import` |
| `preview.jpg` | 首屏截图 |
| `assets/` | demo 用到的照片（已本地化，离线可看） |

---

## 给 AI 用（免下载）

不想下 zip，也可以直接用全量包：

- [`styles-bundle.md`](styles-bundle.md) —— 全部风格的规格，一次粘给 AI
- [`styles-bundle.json`](styles-bundle.json) —— 机器读版本
- [`specs/README.md`](specs/README.md) —— 怎么投喂、三种档位、验收清单

最省事的用法：

```
下面是前端设计风格大全的规格库，请只使用我指定的那一种。
【指定风格】27 / 赛博朋克
【我的需求】做一个卖咖啡的落地页，要有首屏、三个卖点、价格表
```

---

## 本地跑起来

纯静态，无依赖，直接双击 `index.html` 就能看。

重新生成（改了风格之后）：

```bash
pip install pillow
python build_demos.py      # 生成 50 个风格页（含组件总览）
python build_thumbs.py     # 重截 50 张缩略图
python build_zips.py       # 打包 50 个风格包
python build.py            # 首页
```

---

## 贡献一个新风格

见 [CONTRIBUTING.md](CONTRIBUTING.md)。核心是 3 步：

1. 在 `styles.json` 加一行（名称 / 一句话 / 分组 / 参考站点）
2. 在 `themes.py` 加一套 tokens（颜色 / 圆角 / 阴影 / 字体）
3. 跑 `build_demos.py`，能生成页面就说明合格

提交后会自动出现在网站和 AI 投喂包里。

---

## 许可与致谢

- **代码**（生成器、CSS、HTML）：[MIT](LICENSE)
- **文案 / 规格卡 / 组件矩阵**：CC BY 4.0
- **风格清单**参考 B 站视频《50 种前端风格主义》及配套仓库（MIT）、[UI UX Pro Max Skill](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill)（MIT）
- **demo 实现 / 规格卡 / 组件总览 / 导出包**：本仓库原创
- **演示照片**来自 [picsum.photos](https://picsum.photos)（Unsplash），仅作占位，商用请自行替换

---

<sub>关键词：前端设计风格 · UI 风格 · 网页设计 · CSS · design system · design tokens · 前端模板 · AI 提示词 · brutalist · glassmorphism · neumorphism · 极简 · 复古 · 赛博朋克</sub>
"""


LANG_BLOCK = f"""## 10 种语言

站点所有文案（含 105 个组件、50 个风格描述）均已翻译，右上角切换：

| | | | |
|---|---|---|---|
| [简体中文]({BASE}) | [繁體中文]({BASE}?lang=zh-TW) | [English]({BASE}?lang=en) | [Español]({BASE}?lang=es) |
| [Português (BR)]({BASE}?lang=pt-BR) | [Français]({BASE}?lang=fr) | [Русский]({BASE}?lang=ru) | [Deutsch]({BASE}?lang=de) |
| [日本語]({BASE}?lang=ja) | [한국어]({BASE}?lang=ko) | | |

缩略图随语言切换：每种语言都有 50 张真实渲染截图。

---

"""
README = README.replace("## " + str(len(STYLES)) + " 种风格", LANG_BLOCK + "## " + str(len(STYLES)) + " 种风格", 1)

io.open(os.path.join(OUT, "README.md"), "w", encoding="utf-8").write(README)
print("README.md", len(README.encode("utf-8")) // 1024, "KB")
