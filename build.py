# -*- coding: utf-8 -*-
"""生成《前端设计风格大全》：md / html / xlsx"""
import colorsys, json, os, html as H
from themes import SLUGS, THEMES
from build_bundle import ANTI

OUT = os.path.dirname(os.path.abspath(__file__))

G = {
    "G1": "排版与网格",
    "G2": "质感与视觉基调",
    "G3": "复古与怀旧",
    "G4": "科技与未来",
    "G5": "粗野与反设计",
    "G6": "自然·人文·无障碍",
    "G7": "动态与交互",
}

# (序号, 中文名, 英文名, 分组, 一句话说明, 关键特征, 标杆网站)
ROWS = [
(1,"新粗野主义","Neo-Brutalism","G5",
 "把网页当作未经打磨的原件，用粗黑边框和生硬投影表达诚实与反叛。",
 "3px 纯黑边框 / 零圆角块状卡片 / 6px 硬投影无模糊 / 点阵网格背景 / 等宽大写标签 / EXP.01 实验编号",
 ["gumroad.com","theverge.com","balenciaga.com"]),
(2,"瑞士·国际主义平面设计","Swiss Style","G1",
 "源自 1950s 苏黎世与巴塞尔，用网格和字号层级取代一切装饰。",
 "12 列网格 / 非对称 4+8 布局 / 900 字重无衬线标题 / 墨·灰·纸·线四色 / 目录式编号 / 全站 0 圆角",
 ["vitsœ.com","museum-gestaltung.ch","ibm.com/design/language"]),
(3,"日系编辑美学","Japanese Editorial","G1",
 "把杂志版式搬上网页：暖纸底、极细分割线、一处荧光色点睛。",
 "#f1f0ea 纸色底 / 低对比暖灰分割线 / 中日文混排+等宽数字 / 荧光黄标题下划线 / 超大留白 / 低饱和暖色谱",
 ["muji.com","tsutaya.tsite.jp","ndc.co.jp"]),
(4,"终端·开发者工具审美","Terminal CLI Aesthetic","G4",
 "把命令行搬进浏览器，用等宽字体和状态灯建立工程可信感。",
 "全站等宽字体 / $ 提示符与路径式文案 / 绿色脉冲状态点 / 墨黑+灰绿+酸黄冷工业色 / ASCII 装饰",
 ["vercel.com","charm.sh","railway.com"]),
(5,"玻璃拟态 + 复古未来","Glassmorphism + Retrofuturism","G2",
 "毛玻璃卡片浮在发光背景上，再叠一层 CRT 扫描线，介于高级与怀旧之间。",
 "backdrop-filter blur(16px) / 半透明卡片+1px 高光描边 / 扫描线 overlay / 酸黄×深蓝高对比",
 ["apple.com","microsoft.com","dribbble.com"]),
(6,"体素美学","Voxel Aesthetic","G3",
 "用 16×16 的方块世界语言做界面，像在网页里开了一局沙盒游戏。",
 "image-rendering: pixelated / 方块凸凹边框 / Press Start 2P 像素字 / 大地限色板 / steps() 帧动画",
 ["minecraft.net","roblox.com","sandbox.game"]),
(7,"新拟物化","Neumorphism","G2",
 "元素与背景同色，只靠一明一暗两道光「挤」出立体感。",
 "同色底 #e0e5ec / 双向软阴影 8px·16px / inset 按压凹陷 / 20px 大圆角 / 低对比灰蓝",
 ["neumorphism.io","figma.com","dribbble.com"]),
(8,"复古 Windows 95","Retro Win95","G3",
 "完整复刻 1995 年的桌面系统：窗口、任务栏、开始按钮一个不少。",
 "#008080 桌面 / outset·inset 3D 边框 / #c0c0c0 面板 / MS Sans Serif / 虚线 focus 框 / 像素图标",
 ["jdan.github.io/98.css","windows93.net","poolside.fm"]),
(9,"有机自然","Biophilic Design","G6",
 "把阳光、植物和手工纸的质感搬进屏幕，让界面会呼吸。",
 "奶油米+鼠尾草绿 / radial-gradient 树影光斑 / 纸感卡片 / 16px 大圆角 / 漫反射弱阴影",
 ["patagonia.com","ecosia.org","airbnb.com"]),
(10,"3D 超写实","3D & Hyperrealism","G4",
 "用透视、多层阴影和材质渐变，在平面上伪造真实的三维空间。",
 "perspective 1000px / hover 多轴位移+旋转 / 多层 rgba 光照阴影 / 玻璃金属渐变 / 平滑缓动",
 ["apple.com","tesla.com","spline.design"]),
(11,"鲜艳块状","Vibrant & Block-based","G5",
 "大色块 + 撞色 + 粗边框，把页面做成一块块高饱和积木。",
 "红黄高饱和撞色 / 4-8px 硬阴影 / 3px 黑边 / 零圆角 / 白底衬托色彩张力",
 ["spotify.com","duolingo.com","mailchimp.com"]),
(12,"OLED 暗黑","Dark Mode OLED","G2",
 "为纯黑屏幕优化的暗色方案：黑得彻底、亮得克制。",
 "#000 纯黑底 / #0a0a0a 卡片+1px #1a1a1a 描边 / 白字灰文 / 反色按钮作视觉锚点 / 省电",
 ["linear.app","vercel.com","apple.com"]),
(13,"无障碍伦理","Accessible & Ethical","G6",
 "把可读性和可达性当第一美学，宁可朴素也不牺牲可用。",
 "WCAG AA·AAA 4.5:1 / 2px 粗边框 / Atkinson Hyperlegible 字体 / 44×44 触摸目标 / 可见 focus 环",
 ["gov.uk","w3.org/WAI","apple.com/accessibility"]),
(14,"粘土风","Claymorphism","G2",
 "元素像被手指揉圆的粘土，柔软、有体积、没有一条硬边。",
 "双向软阴影+内阴影做体积 / 24px 超大圆角 / 暖杏→可可色 / 无边框只靠光影",
 ["claymorphism.io","dribbble.com","duolingo.com"]),
(15,"极光界面","Aurora UI","G2",
 "深色底上流动的极光色斑配毛玻璃，近年 SaaS 的「高级感模板」。",
 "多层 radial-gradient 光斑 / blur(10px) 毛玻璃 / 翡翠绿按钮 / 1px 微光描边",
 ["stripe.com","linear.app","raycast.com"]),
(16,"复古未来","Retro-Futurism","G3",
 "80 年代人们想象的未来：太空紫、霓虹粉、会发光的按钮。",
 "#1a0a2e 太空紫 / 霓虹粉发光辉影 / 半透明紫卡片 / 80s 科幻标题 / 比赛博朋克更暖",
 ["spacex.com","tesla.com","awwwards.com"]),
(17,"扁平设计","Flat Design","G2",
 "去掉一切阴影、渐变和纹理，只留颜色、形状和字。",
 "零阴影零渐变 / 纯色块 / 品牌蓝 #3490dc / 3-4px 小圆角 / 渲染极快",
 ["material.io","microsoft.com"]),
(18,"液态玻璃","Liquid Glass","G2",
 "Apple 2025 年的设计语言：界面像一层会折射背景的液态玻璃。",
 "blur(20px) 强模糊 / 极透卡片 / 16px 大圆角模拟表面张力 / 随内容变色的微光描边 / 高光流动",
 ["apple.com","apple.com/apple-vision-pro"]),
(19,"动效驱动","Motion-Driven","G7",
 "页面几乎靠动效讲故事，滚动、悬停、转场本身就是内容。",
 "弹簧缓动回弹 / hover 缩放旋转 / 滚动驱动动画 / 暗色舞台 / 尊重 prefers-reduced-motion",
 ["lusion.co","activetheory.net","awwwards.com"]),
(20,"微交互","Micro-interactions","G7",
 "不追求视觉冲击，而是在每个按钮、每个状态里塞进恰到好处的反馈。",
 "按压 scale(0.95) / 200-300ms 标准缓动 / 渐进阴影 / hover 抬升 2px / 1px 精确描边",
 ["stripe.com","linear.app","superhuman.com"]),
(21,"包容性设计","Inclusive Design","G6",
 "假设用户有视力、运动、认知等各种差异，让所有人用同一个界面。",
 "高对比粗边框 / 大触摸目标 / 可见焦点导航 / ≥16px 字号+1.6 行高 / 信息不只靠颜色",
 ["microsoft.com/design/inclusive","gov.uk","apple.com/accessibility"]),
(22,"零界面","Zero Interface","G4",
 "界面退到近乎不存在，只留文字和留白，交互靠对话而非点击。",
 "透明无边框卡片 / 无装饰性 hover / 留白即层级 / 单一输入框 / 适合 AI 与语音场景",
 ["chatgpt.com","claude.ai","perplexity.ai"]),
(23,"柔和 UI 进化","Soft UI Evolution","G2",
 "新拟物与扁平之间的企业级折中：有一点软，但绝不牺牲清晰。",
 "1px 边框+双层柔阴影 / 浅蓝灰底 #eef0f4 / 蓝紫按钮 #6382dc / 14px 圆角软垫感",
 ["notion.so","linear.app","slack.com"]),
(24,"新粗野 2.0","Neubrutalism","G5",
 "粗野主义的乐观版：奶油底、红黄撞色、粗黑边，年轻品牌的标准动作。",
 "#fffaee 奶油底 / 红黄撞色 / 3px 黑边 / 4px 无模糊硬阴影 / 零圆角",
 ["gumroad.com","clerk.com","cal.com"]),
(25,"便当盒网格","Bento Box Grid","G1",
 "像日式便当一样把不等大的圆角卡片拼在一起，一屏讲清所有卖点。",
 "grid-column·row span 拼贴 / Apple 灰 #f5f5f7 / 18px 圆角 / 无边框靠留白分区 / 胶囊按钮",
 ["apple.com","vercel.com","nothing.tech"]),
(26,"Y2K 美学","Y2K Aesthetic","G3",
 "千禧年对未来的想象：冰蓝粉渐变、金属高光、圆润到发亮的控件。",
 "冰蓝→樱花粉渐变 / 磨砂半透明 / 粉红 #ff69b4 主色+辉光 / 16px 胶囊圆角",
 ["poolsuite.net","mschf.com","apple.com"]),
(27,"赛博朋克","Cyberpunk UI","G4",
 "高对比霓虹 + 纯黑 + 故障感，把反乌托邦科技做成视觉语言。",
 "#0a0a0a 底+品红·亮绿霓虹 / 发光边框与文字辉光 / 等宽字体 / 零圆角 / glitch 抖动",
 ["cyberpunk.net","awwwards.com","mschf.com"]),
(28,"AI 原生界面","AI-Native UI","G4",
 "为 AI 产品长出来的视觉：蓝紫渐变、微光边框、对话优先的布局。",
 "#667eea→#764ba2 蓝紫渐变 / 卡片蓝紫描边+微光 / 亮白底 / 12px 流线圆角 / chat-first 布局",
 ["openai.com","anthropic.com","v0.dev"]),
(29,"孟菲斯设计","Memphis Design","G5",
 "1981 年米兰的反现代主义：几何、撞色、波点，故意「不协调」。",
 "粉·青·黄三色撞色 / 彩色硬阴影交替 / 波点锯齿装饰 / 错位拼贴 / 20px 胶囊按钮",
 ["memphis.it","dribbble.com","figma.com"]),
(30,"蒸汽波","Vaporwave","G3",
 "80 年代合成器音乐 + 消费主义残影，粉紫霓虹里带一点虚无。",
 "粉紫霓虹 / 日英混排 / 大理石·棕榈·Windows 元素 / CRT 扫描线与色差 / 慢速循环",
 ["poolsuite.net","mschf.com","awwwards.com"]),
(31,"维度层叠","Dimensional Layering","G2",
 "用递进阴影搭出清晰的 Z 轴，让信息有「离你多远」的层次。",
 "1·2·4·8px 递进阴影 / #f0f0f5 浅灰舞台 / 大卡片悬浮 / 1px #eee 极浅描边",
 ["linear.app","notion.so","stripe.com"]),
(32,"极度极简","Exaggerated Minimalism","G1",
 "把极简推到极端：字大到占满屏，其余什么都没有。",
 "5rem·900 字重·-0.05em 字距 / 纯白底 / 无阴影无装饰 / 1px 细线分割 / 无 hover",
 ["apple.com","muji.com","teenage.engineering"]),
(33,"动态排版","Kinetic Typography","G1",
 "让文字本身成为主角，靠大小、节奏和动画制造海报级冲击。",
 "6rem+ 超大标题 / line-height 0.9 / 黑白极端对比 / 滚动与逐字动画 / 影视海报感",
 ["grillitype.com","resn.co.nz","awwwards.com"]),
(34,"视差叙事","Parallax Storytelling","G7",
 "用滚动速度差讲故事，像翻一本有纵深的长卷。",
 "多层滚动视差 / 半透明卡片透出背景 / 纵向渐变章节 / 长滚动节奏 / 品牌故事页",
 ["nytimes.com","apple.com","airbnb.com"]),
(35,"瑞士现代 2.0","Swiss Modernism 2.0","G1",
 "瑞士风格的极端化版本：去掉一切，只剩字重、行高和一条细线。",
 "2px 顶部线分割 / 4rem·900 标题 / 0.85 行高 / 零阴影零圆角 / 纯白 #fcfcfc",
 ["vitsœ.com","ibm.com/design/language","muji.com"]),
(36,"科幻 HUD","HUD / Sci-Fi FUI","G4",
 "电影里飞船控制台的界面语言：发光细线、角标框、滚动数据。",
 "#001020 深空蓝 / 青色发光边框 / 等宽数据字体 / 环形与网格刻度 / 透明按钮",
 ["spacex.com","nasa.gov","cyberpunk.net"]),
(37,"便当网格 2.0","Bento Grids 2.0","G1",
 "便当网格的年轻化版本：暖灰底、iPhone 红点缀、更松快的圆角。",
 "#f2f2f7 暖灰底 / 20px 大圆角 / 无边框靠底色分区 / grid span 拼接 / 彩色点缀",
 ["apple.com","nothing.tech","arc.net"]),
(38,"空间计算","Spatial UI / VisionOS","G4",
 "为头显和空间屏设计：界面像悬在空气里的玻璃板，有厚度、有光照。",
 "blur(20px) 强模糊 / 22px 超大圆角 / 1px 微光玻璃轮廓 / 深空渐变 / 轻量景深",
 ["apple.com/apple-vision-pro","meta.com"]),
(39,"电子墨水","E-Ink & Paper","G6",
 "把屏幕做成纸：暖白底、衬线字、零阴影，为长时间阅读而生。",
 "#faf8f0 纸色 / Georgia 衬线 / 1.8 行高 / 零阴影 / 1px 细线分割 / 无动效",
 ["readwise.io/read","ia.net","amazon.com/kindle"]),
(40,"Z 世代混沌","Gen Z Chaos / Maximalism","G5",
 "精心设计的「乱七八糟」：高饱和、错位、贴纸感，反叛一切高级感。",
 "亮黄·橙红高饱和 / 黑底白字混排 / 错位拼贴 / 粗边框+彩色硬阴影 / 30px 胶囊按钮",
 ["mschf.com","gumroad.com","duolingo.com"]),
(41,"仿生有机 2.0","Biomimetic / Organic 2.0","G6",
 "不只借用自然的颜色，而是借用自然的生长逻辑与结构。",
 "绿灰纵向渐变 / 半透明卡片像细胞壁 / 有机不规则圆角 / 生长与流动动画",
 ["biomimicry.org","patagonia.com","airbnb.com"]),
(42,"反精致粗糙","Anti-Polish / Raw Aesthetic","G5",
 "刻意不做设计：虚线框、系统字体、零圆角，像线框图直接上线。",
 "dashed 虚线边框 / 等宽或系统字体 / 零圆角零阴影 / 无 hover / 纯文本排版",
 ["news.ycombinator.com","are.na","berkshirehathaway.com"]),
(43,"触觉数字","Tactile Digital / Deformable UI","G6",
 "让屏幕上的东西摸起来像纸、像布、像木头，靠厚度和形变传递温度。",
 "底部 2px 实心投影做厚度 / active scale(0.98) 形变 / 棉纸亚麻底色 / 深棕木质按钮",
 ["teenage.engineering","muji.com","braun.com"]),
(44,"自然精粹","Nature Distilled","G6",
 "不画叶子不画山，只把自然提炼成比例、色温和克制的绿。",
 "#f5f2eb 羊皮纸底 / 森林绿页眉 #5a6a4a / 0.03 极弱阴影 / 用色温而非阴影分区",
 ["aesop.com","kinfolk.com","patagonia.com"]),
(45,"光标交互","Interactive Cursor Design","G7",
 "把鼠标指针变成主角：准星、拖尾、磁吸，光标本身就是导航。",
 "自定义或十字准星光标 / 拖尾与磁吸 / 发光微辉卡片 / 深紫科技底 / 隐藏默认指针",
 ["cuberto.com","lusion.co","aristidebenoist.com"]),
(46,"语音优先","Voice-First Multimodal","G7",
 "为「说话」而设计的界面：一个入口、一圈声波，其余全部退场。",
 "#0a0a1a 极深底 / 柔和蓝紫文字 / 声波纹扩散动效 / 16px 大圆角 / 单一语音入口",
 ["pi.ai","chatgpt.com","alexa.amazon.com"]),
(47,"3D 产品展示","3D Product Preview","G4",
 "像摄影棚一样把产品放在无影墙前，让 3D 模型成为唯一内容。",
 "浅色无影棚背景 / 产品居中悬浮+大投影 / 可旋转与配置器 / AR 预览 / 单色系统",
 ["apple.com","nike.com","ikea.com"]),
(48,"渐变网格","Gradient Mesh / Aurora Evolved","G2",
 "极光 UI 的进化版：多层多色光斑交织，像一张会呼吸的渐变网格。",
 "多层 radial-gradient 网格叠加 / 0.04 极透玻璃卡片 / 描边随光斑变色 / 色彩反射按钮",
 ["stripe.com","framer.com","linear.app"]),
(49,"色差 RGB 分裂","Chromatic Aberration / RGB Split","G5",
 "把镜头色差这个「缺陷」变成设计语言，红绿蓝错位制造数字故障感。",
 "红·绿·蓝错位描边 / text-shadow 2px 0 红、-2px 0 蓝 / 黑底等宽字体 / hover 错位跳变",
 ["awwwards.com","cyberpunk.net","mschf.com"]),
(50,"复古胶片","Vintage Analog / Retro Film","G3",
 "旧照片和旧书的气质：暖黄氧化色、胶片颗粒、棕色调。",
 "#f5e8d0 暖黄纸色 / Georgia 衬线 / 胶片颗粒噪点 / #3a2a10 深棕页眉 / 古铜按钮",
 ["aesop.com","kinfolk.com","nytimes.com"]),
]

assert len(ROWS) == 50, len(ROWS)
for r in ROWS:
    assert r[3] in G, r

DATA = [{"id": r[0], "cn": r[1], "en": r[2], "group": r[3], "groupName": G[r[3]],
         "desc": r[4], "feat": r[5], "sites": r[6]} for r in ROWS]

with open(os.path.join(OUT, "styles.json"), "w", encoding="utf-8") as f:
    json.dump(DATA, f, ensure_ascii=False, indent=1)

# ---------- Markdown ----------
md = ["# 前端设计风格大全", "",
      "> 对应视频：https://www.bilibili.com/video/BV1pVKa6LEJF/ ｜ 原始代码仓库：https://github.com/rxw2023/Front-end-Design-Styles ｜ 风格体系参考：UI UX Pro Max Skill",
      "",
      "| # | 风格名称 | 风格说明与特点 | 风格标杆网站 | 分组 | Demo |",
      "|---|---|---|---|---|---|"]
for d in DATA:
    sites = "、".join(d["sites"])
    desc = d["desc"] + "<br>**特征**：" + d["feat"]
    md.append(f'| {d["id"]} | **{d["cn"]}**<br>{d["en"]} | {desc} | {sites} | {d["groupName"]} | '
              f'[看效果](demos/{SLUGS[d["id"]]}.html) |')
md.append("")
md.append("## 按分组查看")
for k, v in G.items():
    names = "、".join(d["cn"] for d in DATA if d["group"] == k)
    md.append(f"- **{v}**：{names}")
with open(os.path.join(OUT, "50-frontend-styles.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(md))

# ---------- HTML ----------
cards = []
for d in DATA:
    sites = "".join(
        f'<a class="site" href="https://{s}" target="_blank" rel="noopener">{H.escape(s)}</a>'
        for s in d["sites"])
    cards.append(f'''<tr data-g="{d["group"]}" data-k="{H.escape(d["cn"]+d["en"]+d["feat"]+d["desc"]+" ".join(d["sites"])).lower()}">
<td class="num">{d["id"]:02d}</td>
<td class="name"><b>{H.escape(d["cn"])}</b><span class="en">{H.escape(d["en"])}</span></td>
<td class="desc"><p>{H.escape(d["desc"])}</p><p class="feat">{H.escape(d["feat"])}</p></td>
<td class="sites">{sites}</td>
<td class="grp"><span class="tag">{H.escape(d["groupName"])}</span></td>
<td class="pv"><a href="demos/{SLUGS[d["id"]]}.html" title="打开 {H.escape(d["cn"])} demo"><img src="assets/thumbs/{d["id"]:02d}.jpg" alt="{H.escape(d["cn"])}" loading="lazy"></a></td>
</tr>''')


def _hex_rgb(h):
    h = h.lstrip("#")
    if len(h) == 3:
        h = "".join(c * 2 for c in h)
    try:
        return tuple(int(h[i:i+2], 16) / 255 for i in (0, 2, 4))
    except Exception:
        return (1.0, 1.0, 1.0)


def _luminance(h):
    r, g, b = _hex_rgb(h)
    f = lambda c: c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(r) + 0.7152 * f(g) + 0.0722 * f(b)


def feel_of(sid):
    """从 tokens 自动推导：明暗 / 软硬 / 繁简 / 冷暖。社区新增风格也能自动归类。"""
    th = THEMES[sid]
    tone = "light" if _luminance(th["bg"]) > 0.35 else "dark"
    radius = str(th["radius"])
    hard_shadow = bool(__import__("re").search(r"-?\d+px\s+-?\d+px\s+0\b", th["shadow"]))
    edge = "hard" if (radius in ("0", "0px", "none") or hard_shadow) else "soft"
    raw = th["raw"].lower()
    busy = bool(th["bgimg"]) or ("gradient" in raw) or any(
        k in th.get("raw", "") + th.get("bgimg", "") for k in [])
    deco = any(k in raw for k in ["gradient", "pattern", "texture", "scan", "grid", "noise"])
    feat = " ".join([])
    density = "busy" if busy or deco else "calm"
    r, g, b = _hex_rgb(th["accent"])
    hh, ll, ss = colorsys.rgb_to_hls(r, g, b)
    deg = hh * 360
    if ss < 0.12 or ll < 0.06 or ll > 0.96:
        hue = "neutral"
    elif deg >= 150 and deg < 280:
        hue = "cool"
    else:
        hue = "warm"
    return tone, edge, density, hue


DL_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" '
           'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">'
           '<path d="M12 3v12"/><path d="m7 11 5 5 5-5"/><path d="M5 21h14"/></svg>')

vcards = []
for d in DATA:
    _t, _e, _d, _h = feel_of(d["id"])
    _th = THEMES[d["id"]]
    _prompt = (
        "请用「%s」（%s）这套视觉风格，帮我做一个页面。\n\n"
        "它长什么样：%s\n"
        "要抓住这几点：%s\n\n"
        "配色：背景 %s｜卡片 %s｜文字 %s｜强调色 %s\n"
        "形状：圆角 %s｜卡片边 %s｜卡片阴影 %s\n\n"
        "不要出现：%s\n\n"
        "我的需求：<换成你要做的页面>"
    ) % (d["cn"], d["en"], d["desc"], d["feat"], _th["bg"], _th["surface"],
         _th["ink"], _th["accent"], _th["radius"], _th["cardborder"], _th["shadow"],
         (ANTI.get(d["id"]) or ""))
    _css = ("--bg:%s;--surface:%s;--ink:%s;--accent:%s;--radius:%s"
            % (THEMES[d["id"]]["bg"], THEMES[d["id"]]["surface"], THEMES[d["id"]]["ink"],
               THEMES[d["id"]]["accent"], THEMES[d["id"]]["radius"]))
    vcards.append(f'''<div class="vcell"
   data-g="{d["group"]}" data-tone="{_t}" data-edge="{_e}" data-density="{_d}" data-hue="{_h}"
   data-sid="{d["id"]:02d}"
   data-tok="{THEMES[d["id"]]["bg"]}|{THEMES[d["id"]]["surface"]}|{THEMES[d["id"]]["ink"]}|{THEMES[d["id"]]["accent"]}|{THEMES[d["id"]]["radius"]}|{H.escape(THEMES[d["id"]]["cardborder"])}|{H.escape(THEMES[d["id"]]["shadow"])}|{H.escape(ANTI.get(d["id"]) or "")}"
   data-css=":root{{ {_css} }}"
   data-k="{H.escape(d["cn"]+d["en"]+d["feat"]+d["desc"]+" ".join(d["sites"])).lower()}">
  <a class="vcard" href="demos/{SLUGS[d["id"]]}.html">
    <span class="vshot"><img src="assets/thumbs/{d["id"]:02d}.jpg" alt="{H.escape(d["cn"])} 界面预览" loading="lazy">
      <span class="vhover">
        <span class="sws"><i style="background:{THEMES[d["id"]]["bg"]}"></i><i style="background:{THEMES[d["id"]]["surface"]}"></i><i style="background:{THEMES[d["id"]]["accent"]}"></i><i style="background:{THEMES[d["id"]]["ink"]}"></i></span>
        <span class="vcopy" role="button" tabindex="0" title="复制一段可以直接粘给 AI 的话" data-i18n="home.copyAI">📋 复制给 AI</span>
      </span></span>
  <template class="ptpl">{H.escape(_prompt)}</template>
    <span class="vtop"><span class="vidx">{d["id"]:02d}</span>
      <span class="vchip" data-group="{d["group"]}">{H.escape(d["groupName"])}</span></span>
    <span class="vname"><b data-field="name">{H.escape(d["cn"])}</b><span class="ven">{H.escape(d["en"])}</span></span>
    <span class="vone" data-field="desc">{H.escape(d["desc"])}</span>
  </a>
  <a class="vdl" href="assets/zips/style-{SLUGS[d["id"]]}.zip" download
     title="下载 {H.escape(d["cn"])} 风格包（zip：spec + 提示词 + theme.css + demo）">{DL_ICON}<span data-i18n="home.download">导出风格包</span></a>
</div>''')

chips = [f'<button class="chip on" data-g="all" data-group="all">全部 <em>{len(DATA)}</em></button>']
for k, v in G.items():
    n = sum(1 for d in DATA if d["group"] == k)
    chips.append(f'<button class="chip" data-g="{k}" data-group="{k}">{H.escape(v)} <em>{n}</em></button>')

HTML = f'''<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>前端设计风格大全 · Style Atlas</title>
<style>
:root{{
  --paper:#fbfbf8; --ink:#15150f; --muted:#6d6d63; --line:#e2e1d9;
  --accent:#1d4ed8; --hl:#e9f0ff; --mono:ui-monospace,SFMono-Regular,"SF Mono",Menlo,monospace;
}}
*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);
  font-family:"PingFang SC","HarmonyOS Sans SC","Noto Sans SC",-apple-system,system-ui,sans-serif;
  -webkit-font-smoothing:antialiased;line-height:1.6}}
.wrap{{max-width:1560px;margin:0 auto;padding:58px 40px 96px}}
header{{border-bottom:2px solid var(--ink);padding-bottom:22px;margin-bottom:26px}}
.toplang{{display:flex;justify-content:flex-end;margin-bottom:10px}}
.langSel{{font:inherit;font-size:12px;padding:6px 10px;border:1px solid var(--line);border-radius:999px;
  background:#fff;color:var(--ink);cursor:pointer}}
html[lang="en"] h1 em,html[lang="fr"] h1 em,html[lang="de"] h1 em,html[lang="es"] h1 em,html[lang="pt-BR"] h1 em,html[lang="ru"] h1 em{{margin-left:.16em}}
html:not([lang="zh-CN"]) .ven{{display:none}}
html:not([lang="zh-CN"]) .sub strong::after{{content:" "}}
.kicker{{font-family:var(--mono);font-size:11px;letter-spacing:.16em;text-transform:uppercase;color:var(--muted)}}
h1{{font-size:clamp(30px,4.4vw,46px);line-height:1.1;letter-spacing:-.03em;margin:14px 0 12px;font-weight:800}}
h1 em{{font-style:normal;color:var(--accent)}}
.sub{{color:var(--muted);font-size:13.5px;max-width:760px}}
.sub a{{color:var(--accent);text-decoration:none;border-bottom:1px solid #c7d5f5}}
.bigcta{{display:flex;align-items:baseline;gap:12px;flex-wrap:wrap;margin-top:22px;
  padding:14px 18px;border:1px solid var(--ink);border-radius:8px;background:#fff;
  text-decoration:none;color:var(--ink)}}
.bigcta span{{font-weight:700;font-size:14px}}
.bigcta em{{font-style:normal;font-size:12.5px;color:var(--muted);font-family:var(--mono)}}
.bigcta:hover{{background:var(--ink);color:#fff}}
.bigcta:hover em{{color:#c9c9c0}}

/* ---------- 3 步说明 ---------- */
.steps3{{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:22px 0 0}}
.steps3 div{{display:flex;gap:10px;align-items:center;padding:11px 14px;border:1px solid var(--line);
  border-radius:10px;background:#fff;font-size:12.5px;color:#3c3c34}}
.steps3 b{{display:grid;place-items:center;width:20px;height:20px;border-radius:50%;
  background:var(--ink);color:#fff;font-size:11px;flex:0 0 auto}}
@media (max-width:820px){{.steps3{{grid-template-columns:1fr}}}}
/* ---------- 感觉选择器 ---------- */
.feel{{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:center;margin:24px 0 6px;
  padding:16px 18px;background:#fff;border:1px solid var(--line);border-radius:12px}}
.feelLab{{font-family:var(--mono);font-size:10.5px;letter-spacing:.14em;color:var(--muted);
  text-transform:uppercase}}
.seg{{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden}}
.sg{{font:inherit;font-size:12px;padding:5px 12px;border:0;background:none;color:#5c5c52;cursor:pointer}}
.sg.on{{background:var(--ink);color:#fff;font-weight:600}}
.lucky{{margin-left:auto;font:inherit;font-size:12.5px;padding:8px 16px;border-radius:999px;
  border:1px solid var(--ink);background:var(--ink);color:#fff;cursor:pointer;font-weight:600}}
.lucky:hover{{background:var(--accent);border-color:var(--accent)}}
/* ---------- 悬停色板 / 复制 ---------- */
.vhover{{position:absolute;left:8px;right:8px;bottom:8px;display:flex;align-items:center;
  justify-content:space-between;gap:8px;opacity:0;transition:.18s;pointer-events:none}}
.vcard:hover .vhover{{opacity:1;pointer-events:auto}}
.sws{{display:inline-flex;gap:4px;padding:5px 7px;border-radius:8px;background:rgba(255,255,255,.94);
  box-shadow:0 1px 4px rgba(0,0,0,.18)}}
.sws i{{width:14px;height:14px;border-radius:3px;display:block;border:1px solid rgba(0,0,0,.12)}}
.vcopy{{font-size:11px;font-weight:600;padding:5px 9px;border-radius:6px;cursor:pointer;
  background:rgba(255,255,255,.95);color:#15150f;box-shadow:0 1px 4px rgba(0,0,0,.18);
  white-space:nowrap}}
.vcopy:hover{{background:var(--ink);color:#fff}}
.toast{{position:fixed;left:50%;bottom:24px;transform:translate(-50%,16px);background:var(--ink);
  color:#fff;padding:10px 20px;border-radius:999px;font-size:12.5px;opacity:0;pointer-events:none;
  transition:.22s;z-index:120}}
.toast.show{{opacity:1;transform:translate(-50%,0)}}
@media (max-width:820px){{.lucky{{margin-left:0}}}}
.toolbar{{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:26px 0 10px}}
.chip{{font-family:inherit;font-size:12.5px;padding:6px 12px;border-radius:999px;cursor:pointer;
  border:1px solid var(--line);background:#fff;color:#3c3c34;transition:.15s}}
.chip em{{font-style:normal;font-family:var(--mono);font-size:11px;color:var(--muted);margin-left:4px}}
.chip:hover{{border-color:#b9b8ad}}
.chip.on{{background:var(--ink);color:#fff;border-color:var(--ink)}}
.chip.on em{{color:#bdbdb2}}
input[type=search]{{margin-left:auto;min-width:220px;padding:8px 14px;border:1px solid var(--line);
  border-radius:8px;background:#fff;font:inherit;font-size:13px;outline:none}}
input[type=search]:focus{{border-color:var(--accent);box-shadow:0 0 0 3px var(--hl)}}

/* ---------- 视图切换 ---------- */
.views{{display:flex;gap:2px;border:1px solid var(--line);border-radius:8px;overflow:hidden;
  background:#fff;margin-left:4px}}
.vbtn{{font:inherit;font-size:12px;padding:7px 14px;border:0;background:none;color:var(--muted);
  cursor:pointer}}
.vbtn.on{{background:var(--ink);color:#fff;font-weight:600}}
/* ---------- 大图网格 ---------- */
.vgrid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(min(300px,100%),1fr));gap:32px 22px}}
.vcell{{position:relative}}
.vcell.hide{{display:none}}
.vcard{{display:block;text-decoration:none;color:inherit}}
/* 悬浮导出按钮 */
.vdl{{position:absolute;right:8px;top:8px;z-index:3;display:inline-flex;align-items:center;gap:4px;
  padding:4px 8px;border-radius:6px;background:rgba(255,255,255,.94);color:#2b2b24;
  border:1px solid rgba(0,0,0,.14);box-shadow:0 1px 3px rgba(0,0,0,.13);
  font-size:10.5px;font-weight:600;text-decoration:none;white-space:nowrap;
  -webkit-backdrop-filter:blur(6px);backdrop-filter:blur(6px);
  transition:background .16s,color .16s,border-color .16s,box-shadow .16s}}
.vdl svg{{width:11px;height:11px;flex:0 0 auto}}
.vdl:hover{{background:#15803d;color:#fff;border-color:#15803d;
  box-shadow:0 2px 7px rgba(21,128,61,.3)}}
.vcard:hover .vshot{{border-color:rgba(0,0,0,.5);transform:translateY(-3px);
  box-shadow:0 14px 34px rgba(0,0,0,.14)}}
.vshot{{position:relative;display:block;border-radius:12px;overflow:hidden;
  border:1px solid var(--line);background:#fff;box-shadow:0 1px 2px rgba(0,0,0,.05);
  transition:border-color .18s,box-shadow .22s,transform .22s}}
.vshot img{{display:block;width:100%;aspect-ratio:16/9;object-fit:cover;object-position:top;
  transition:transform .5s cubic-bezier(.2,.8,.3,1)}}
.vcard:hover .vshot{{border-color:rgba(0,0,0,.5);transform:translateY(-3px);
  box-shadow:0 14px 34px rgba(0,0,0,.14)}}
.vcard:hover .vshot img{{transform:scale(1.02)}}
.vopen{{position:absolute;right:10px;bottom:10px;font-size:12px;font-weight:600;
  padding:6px 12px;border-radius:999px;background:rgba(12,12,14,.82);color:#fff;
  opacity:0;transform:translateY(6px);transition:.2s;backdrop-filter:blur(6px)}}
.vcard:hover .vopen{{opacity:1;transform:none}}
.vtop{{display:flex;align-items:center;gap:8px;margin:13px 0 5px}}
.vidx{{font-family:var(--mono);font-size:11px;color:#a3a399}}
.vchip{{margin-left:auto;font-size:10px;color:#5c5c52;border:1px solid var(--line);
  border-radius:999px;padding:2px 9px;white-space:nowrap}}
.vname{{display:flex;align-items:baseline;gap:9px;flex-wrap:wrap;margin-bottom:6px}}
.vname b{{font-size:15.5px;letter-spacing:-.01em;line-height:1.35}}
.ven{{font-family:var(--mono);font-size:10.5px;color:var(--muted)}}
.vone{{display:-webkit-box;-webkit-box-orient:vertical;-webkit-line-clamp:2;overflow:hidden;
  font-size:12.5px;line-height:1.6;color:var(--muted)}}

.tableBox.hide{{display:none}}
.countRow{{display:flex;align-items:center;justify-content:space-between;gap:12px;margin:10px 0 18px}}
.count{{font-family:var(--mono);font-size:11.5px;color:var(--muted)}}
table{{width:100%;border-collapse:collapse;font-size:13.5px}}
thead th{{position:sticky;top:0;background:var(--paper);text-align:left;font-size:11px;
  letter-spacing:.14em;text-transform:uppercase;color:var(--muted);font-weight:600;
  padding:10px 12px;border-bottom:1.5px solid var(--ink);z-index:2}}
tbody tr{{border-bottom:1px solid var(--line)}}
tbody tr:hover{{background:#f4f4ee}}
td{{padding:16px 12px;vertical-align:top}}
.num{{font-family:var(--mono);font-size:12px;color:#a3a399;width:44px;padding-top:18px}}
.name{{width:190px}}
.name b{{display:block;font-size:15px;letter-spacing:-.01em}}
.en{{display:block;font-family:var(--mono);font-size:10.5px;color:var(--muted);margin-top:3px;letter-spacing:.02em}}
.desc p{{margin:0}}
.desc .feat{{margin-top:6px;font-family:var(--mono);font-size:11.5px;line-height:1.75;color:#55554b}}
.sites{{width:190px}}
.site{{display:inline-block;font-family:var(--mono);font-size:11.5px;color:#2b2b24;
  background:#f0efe7;border-radius:4px;padding:1px 6px;margin:0 4px 5px 0;text-decoration:none}}
.site:hover{{background:var(--ink);color:#fff}}
.grp{{width:132px}}
.pv{{width:158px;padding-top:14px}}
.pv a{{display:block;width:132px;border-radius:6px;overflow:hidden;line-height:0;
  border:1px solid var(--line);background:#fff;transition:.16s}}
.pv img{{display:block;width:100%;height:74px;object-fit:cover;object-position:top}}
.pv a:hover{{border-color:var(--ink);transform:translateY(-2px);
  box-shadow:0 6px 16px rgba(0,0,0,.12)}}
.tag{{font-size:11px;color:#5c5c52;border-left:2px solid var(--line);padding-left:8px;display:inline-block;white-space:nowrap}}
tr.hide{{display:none}}
footer{{margin-top:40px;padding-top:18px;border-top:1px solid var(--line);
  font-size:12px;color:var(--muted);font-family:var(--mono)}}
@media (max-width:820px){{
  .wrap{{padding:40px 18px 64px}} .name,.grp,.sites,.pv{{width:auto}}
  thead{{display:none}} tbody tr{{display:block;padding:14px 0}}
  td{{display:block;padding:3px 0;border:0}} .num{{color:var(--accent)}}
  .pv a{{margin-top:8px;width:132px}}
  .pv img{{height:74px}}
  .pv{{width:auto}}
  input[type=search]{{margin-left:0;width:100%}}
}}
</style></head><body><div class="wrap">
<header>
  <div class="toplang" id="langSwitch"></div>
  <div class="kicker" data-i18n="home.kicker">FRONTEND DESIGN STYLES · STYLE ATLAS</div>
  <h1><span data-i18n="home.h1a">前端设计</span><em data-i18n="home.h1b">风格大全</em></h1>
  <p class="sub"><strong data-i18n="site.tagline">按感觉挑一个，直接拿走。</strong><span data-i18n="site.intro">不用先懂设计流派：每张图都是该风格真实渲染的一屏，看对眼就点进去，下载一个 zip 就带走全部代码与规格。需要 <strong>CSS 手法、色值、标杆网站</strong>时，切到右上角「列表」。 </span><span data-i18n="site.source">来源：</span><a href="https://www.bilibili.com/video/BV1pVKa6LEJF/" target="_blank" rel="noopener" data-i18n="site.srcVideo">视频</a> · <a href="https://github.com/rxw2023/Front-end-Design-Styles" target="_blank" rel="noopener" data-i18n="site.srcRepo">代码仓库</a> · <a href="https://github.com/nextlevelbuilder/ui-ux-pro-max-skill" target="_blank" rel="noopener">UI UX Pro Max Skill</a></p>
<div class="steps3">
  <div><b>1</b><span data-i18n="home.step1">看图挑一个</span></div>
  <div><b>2</b><span data-i18n="home.step2">点「下载风格包」，解压即用</span></div>
  <div><b>3</b><span data-i18n="home.step3">想做自己的页？复制给 AI</span></div>
</div>
<div class="feel">
  <div class="feelLab" data-i18n="home.feel.tone">明暗</div>
  <div class="seg" data-f="tone"><button class="sg on" data-v="all" data-i18n="home.feel.all">全部</button><button class="sg" data-v="light" data-i18n="home.feel.lightV">浅色</button><button class="sg" data-v="dark" data-i18n="home.feel.darkV">深色</button></div>
  <div class="feelLab" data-i18n="home.feel.edge">软硬</div>
  <div class="seg" data-f="edge"><button class="sg on" data-v="all" data-i18n="home.feel.all">全部</button><button class="sg" data-v="hard" data-i18n="home.feel.hard">硬边</button><button class="sg" data-v="soft" data-i18n="home.feel.soft">柔和</button></div>
  <div class="feelLab" data-i18n="home.feel.density">繁简</div>
  <div class="seg" data-f="density"><button class="sg on" data-v="all" data-i18n="home.feel.all">全部</button><button class="sg" data-v="calm" data-i18n="home.feel.calm">克制</button><button class="sg" data-v="busy" data-i18n="home.feel.busy">繁复</button></div>
  <button class="lucky" id="lucky" data-i18n="home.lucky">🎲 手气不错</button>
</div>
</header>
<div class="toolbar">{''.join(chips)}
  <input id="q" type="search" placeholder="搜索风格 / 特征 / 网站，如 渐变、圆角、apple" data-i18n-ph="home.search">
</div>
<div class="countRow">
  <div class="count" id="count">显示 {len(DATA)} / {len(DATA)}</div>
  <div class="views">
    <button class="vbtn on" data-v="grid" data-i18n="home.grid">大图</button>
    <button class="vbtn" data-v="table" data-i18n="home.table">列表</button>
  </div>
</div>

<div class="vgrid" id="vgrid">
{''.join(vcards)}
</div>

<a class="bigcta" href="previews.html">
  <span>▶ {len(DATA)} 宫格紧凑视图</span><em>一屏能扫 9 个，带分组筛选 · 每个 demo 都是 8 段完整页面</em>
</a>

<div class="tableBox hide" id="tableBox">
<table><thead><tr>
<th>#</th><th>风格名称</th><th>风格说明与特点</th><th>风格标杆网站</th><th>分组</th><th>预览</th>
</tr></thead><tbody id="tb">
{''.join(cards)}
</tbody></table>
</div>
<footer>前端设计风格大全 · 风格清单参考公开资料与视频配套仓库 · 标杆网站为风格参考，非唯一代表</footer>
</div>
<script src="assets/i18n.js" defer></script>
<script src="assets/app.js" defer></script></body></html>'''
with open(os.path.join(OUT, "50-frontend-styles.html"), "w", encoding="utf-8") as f:
    f.write(HTML)
with open(os.path.join(OUT, "index.html"), "w", encoding="utf-8") as f:
    f.write(HTML)

# ---------- XLSX ----------
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

wb = Workbook()
ws = wb.active
ws.title = "前端设计风格"

head = ["序号", "风格名称（中）", "风格名称（英）", "风格说明与特点", "关键特征", "风格标杆网站", "分组", "Demo 文件"]
ws.append(head)

INK = "15150F"
hfill = PatternFill("solid", fgColor="15150F")
thin = Side(style="thin", color="E2E1D9")
for c in range(1, len(head) + 1):
    cell = ws.cell(row=1, column=c)
    cell.font = Font(bold=True, color="FFFFFF", size=11, name="PingFang SC")
    cell.fill = hfill
    cell.alignment = Alignment(vertical="center", horizontal="left", indent=1)
    cell.border = Border(bottom=thin)
ws.row_dimensions[1].height = 30

alt = PatternFill("solid", fgColor="F7F7F2")
for i, d in enumerate(DATA, start=2):
    ws.append([d["id"], d["cn"], d["en"], d["desc"], d["feat"], "、".join(d["sites"]),
               d["groupName"], f'demos/{SLUGS[d["id"]]}.html'])
    for c in range(1, len(head) + 1):
        cell = ws.cell(row=i, column=c)
        cell.alignment = Alignment(vertical="top", wrap_text=True,
                                   horizontal="center" if c == 1 else "left")
        cell.font = Font(size=10.5, name="PingFang SC",
                         bold=(c == 2), color="15150F")
        cell.border = Border(bottom=thin)
        if i % 2 == 1:
            cell.fill = alt
    ws.row_dimensions[i].height = 46

widths = [6, 20, 26, 52, 60, 34, 16, 30]
for idx, w in enumerate(widths, start=1):
    ws.column_dimensions[get_column_letter(idx)].width = w
ws.freeze_panes = "A2"
ws.auto_filter.ref = f"A1:H{len(DATA)+1}"

ws2 = wb.create_sheet("按分组")
ws2.append(["分组", "数量", "包含风格"])
for c in range(1, 4):
    cell = ws2.cell(row=1, column=c)
    cell.font = Font(bold=True, color="FFFFFF", size=11)
    cell.fill = hfill
    cell.alignment = Alignment(vertical="center", indent=1)
ws2.row_dimensions[1].height = 28
r = 2
for k, v in G.items():
    names = "、".join(d["cn"] for d in DATA if d["group"] == k)
    ws2.append([v, sum(1 for d in DATA if d["group"] == k), names])
    ws2.cell(row=r, column=1).font = Font(bold=True, size=10.5)
    for c in range(1, 4):
        ws2.cell(row=r, column=c).alignment = Alignment(vertical="top", wrap_text=True)
        ws2.cell(row=r, column=c).border = Border(bottom=thin)
    ws2.row_dimensions[r].height = 40
    r += 1
for idx, w in enumerate([20, 8, 90], start=1):
    ws2.column_dimensions[get_column_letter(idx)].width = w
ws2.freeze_panes = "A2"

wb.save(os.path.join(OUT, "50种前端风格速查表.xlsx"))
print("ok")
