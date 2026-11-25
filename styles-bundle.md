# 前端设计风格大全 · AI 投喂包（单文件全量）

> 一次投喂，覆盖全部风格。用法见文末「怎么用」。

每种风格给出：分组 / 定位 / tokens（色值·形状·字体）/ 必用手法 / 组件配方 / 关键实现 / 禁止清单 / 无障碍下限 / 影像滤镜 / 参考站点 / 样例页路径。

---

## 索引（按编号）


01 新粗野主义 · Neo-Brutalism（粗野与反设计）
02 瑞士·国际主义平面设计 · Swiss Style（排版与网格）
03 日系编辑美学 · Japanese Editorial（排版与网格）
04 终端·开发者工具审美 · Terminal CLI Aesthetic（科技与未来）
05 玻璃拟态 + 复古未来 · Glassmorphism + Retrofuturism（质感与视觉基调）
06 体素美学 · Voxel Aesthetic（复古与怀旧）
07 新拟物化 · Neumorphism（质感与视觉基调）
08 复古 Windows 95 · Retro Win95（复古与怀旧）
09 有机自然 · Biophilic Design（自然·人文·无障碍）
10 3D 超写实 · 3D & Hyperrealism（科技与未来）
11 鲜艳块状 · Vibrant & Block-based（粗野与反设计）
12 OLED 暗黑 · Dark Mode OLED（质感与视觉基调）
13 无障碍伦理 · Accessible & Ethical（自然·人文·无障碍）
14 粘土风 · Claymorphism（质感与视觉基调）
15 极光界面 · Aurora UI（质感与视觉基调）
16 复古未来 · Retro-Futurism（复古与怀旧）
17 扁平设计 · Flat Design（质感与视觉基调）
18 液态玻璃 · Liquid Glass（质感与视觉基调）
19 动效驱动 · Motion-Driven（动态与交互）
20 微交互 · Micro-interactions（动态与交互）
21 包容性设计 · Inclusive Design（自然·人文·无障碍）
22 零界面 · Zero Interface（科技与未来）
23 柔和 UI 进化 · Soft UI Evolution（质感与视觉基调）
24 新粗野 2.0 · Neubrutalism（粗野与反设计）
25 便当盒网格 · Bento Box Grid（排版与网格）
26 Y2K 美学 · Y2K Aesthetic（复古与怀旧）
27 赛博朋克 · Cyberpunk UI（科技与未来）
28 AI 原生界面 · AI-Native UI（科技与未来）
29 孟菲斯设计 · Memphis Design（粗野与反设计）
30 蒸汽波 · Vaporwave（复古与怀旧）
31 维度层叠 · Dimensional Layering（质感与视觉基调）
32 极度极简 · Exaggerated Minimalism（排版与网格）
33 动态排版 · Kinetic Typography（排版与网格）
34 视差叙事 · Parallax Storytelling（动态与交互）
35 瑞士现代 2.0 · Swiss Modernism 2.0（排版与网格）
36 科幻 HUD · HUD / Sci-Fi FUI（科技与未来）
37 便当网格 2.0 · Bento Grids 2.0（排版与网格）
38 空间计算 · Spatial UI / VisionOS（科技与未来）
39 电子墨水 · E-Ink & Paper（自然·人文·无障碍）
40 Z 世代混沌 · Gen Z Chaos / Maximalism（粗野与反设计）
41 仿生有机 2.0 · Biomimetic / Organic 2.0（自然·人文·无障碍）
42 反精致粗糙 · Anti-Polish / Raw Aesthetic（粗野与反设计）
43 触觉数字 · Tactile Digital / Deformable UI（自然·人文·无障碍）
44 自然精粹 · Nature Distilled（自然·人文·无障碍）
45 光标交互 · Interactive Cursor Design（动态与交互）
46 语音优先 · Voice-First Multimodal（动态与交互）
47 3D 产品展示 · 3D Product Preview（科技与未来）
48 渐变网格 · Gradient Mesh / Aurora Evolved（质感与视觉基调）
49 色差 RGB 分裂 · Chromatic Aberration / RGB Split（粗野与反设计）
50 复古胶片 · Vintage Analog / Retro Film（复古与怀旧）

---

### 01 新粗野主义 · Neo-Brutalism
- 分组：粗野与反设计
- 定位：把网页当作未经打磨的原件，用粗黑边框和生硬投影表达诚实与反叛。
- tokens：bg `#f2f0e6` · surface `#fffdf5` · ink `#111111` · muted `#454540` · line `#111111` · accent `#f6d743` · on-accent `#111111`
- 形状：圆角 `0` · 卡片边 `3px solid #111` · 卡片影 `6px 6px 0 #111` · 按钮边 `2px solid #111` · 按钮影 `5px 5px 0 #111`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 大写 .18em
- 必用手法：3px 纯黑边框 / 零圆角块状卡片 / 6px 硬投影无模糊 / 点阵网格背景 / 等宽大写标签 / EXP.01 实验编号
- 组件：按钮=底 #f6d743 + 字 #111111 + 2px solid #111 + 硬影（模糊 0）；输入=底 #f2f0e6 + 边 1px #111111 + 零圆角；卡片=底 #fffdf5 + 3px solid #111 + 零圆角 + 6px 6px 0 #111；表格=表头/行底边 1px #111111
- 关键实现：点阵底纹 16px；硬影偏移 5–6px，模糊恒为 0
- 禁止：任何圆角、模糊阴影、渐变、浅灰文字、衬线字体
- 无障碍：正文对比 16.5:1 / 主色底字 13.2:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1) contrast(1.18)` + 主色双色调 opacity 0.12
- 参考：gumroad.com、theverge.com、balenciaga.com
- 样例页：`demos/01-neo-brutalism.html`

### 02 瑞士·国际主义平面设计 · Swiss Style
- 分组：排版与网格
- 定位：源自 1950s 苏黎世与巴塞尔，用网格和字号层级取代一切装饰。
- tokens：bg `#fcfcfc` · surface `#ffffff` · ink `#0a0a0a` · muted `#6b6b6b` · line `#e6e6e6` · accent `#e4002b` · on-accent `#ffffff`
- 形状：圆角 `0` · 卡片边 `none` · 卡片影 `none` · 按钮边 `0` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 0.94 · 标题字距 -.045em · 小标签 大写 .2em
- 必用手法：12 列网格 / 非对称 4+8 布局 / 900 字重无衬线标题 / 墨·灰·纸·线四色 / 目录式编号 / 全站 0 圆角
- 组件：按钮=底 #e4002b + 字 #ffffff + 无边框 + 无阴影；输入=底 #fcfcfc + 边 1px #e6e6e6 + 零圆角；卡片=底 #ffffff + 无边框 + 零圆角 + 无阴影；表格=表头/行底边 1px #e6e6e6
- 关键实现：零圆角 + 非对称 4+8 栅格 + 全站只有一个强调红
- 禁止：圆角、卡片阴影、装饰图形、居中对称的居中排版
- 无障碍：正文对比 19.3:1 / 主色底字 4.8:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1) contrast(1.06)`
- 参考：vitsœ.com、museum-gestaltung.ch、ibm.com/design/language
- 样例页：`demos/02-swiss-style.html`

### 03 日系编辑美学 · Japanese Editorial
- 分组：排版与网格
- 定位：把杂志版式搬上网页：暖纸底、极细分割线、一处荧光色点睛。
- tokens：bg `#f3f1ea` · surface `#fdfbf5` · ink `#22211d` · muted `#6b6759` · line `#d4d3cc` · accent `#dfff00` · on-accent `#22211d`
- 形状：圆角 `6px` · 卡片边 `1px solid var(--line)` · 卡片影 `0 1px 0 rgba(0,0,0,.03)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 600 · 元信息等宽 · 行高 1.35 · 标题字距 -.02em · 小标签 大写 .1em
- 必用手法：#f1f0ea 纸色底 / 低对比暖灰分割线 / 中日文混排+等宽数字 / 荧光黄标题下划线 / 超大留白 / 低饱和暖色谱
- 组件：按钮=底 #dfff00 + 字 #22211d + 无边框 + 无阴影；输入=底 #f3f1ea + 边 1px #d4d3cc + 圆角 10px；卡片=底 #fdfbf5 + 1px solid var(--line) + 圆角 6px + 0 1px 0 rgba(0,0,0,.03)；表格=表头/行底边 1px #d4d3cc
- 禁止：高饱和撞色、粗黑边、重阴影、等宽标题
- 无障碍：正文对比 14.3:1 / 主色底字 14.1:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(.85) sepia(.14) brightness(1.03)`
- 参考：muji.com、tsutaya.tsite.jp、ndc.co.jp
- 样例页：`demos/03-japanese-editorial.html`

### 04 终端·开发者工具审美 · Terminal CLI Aesthetic
- 分组：科技与未来
- 定位：把命令行搬进浏览器，用等宽字体和状态灯建立工程可信感。
- tokens：bg `#0d0f0e` · surface `#111514` · ink `#c5d0c0` · muted `#7f8b7d` · line `#242b22` · accent `#dfff00` · on-accent `#0d0f0e`
- 形状：圆角 `6px` · 卡片边 `1px solid #242b22` · 卡片影 `none` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 等宽 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.01em · 小标签 大写 .14em
- 必用手法：全站等宽字体 / $ 提示符与路径式文案 / 绿色脉冲状态点 / 墨黑+灰绿+酸黄冷工业色 / ASCII 装饰
- 组件：按钮=底 #dfff00 + 字 #0d0f0e + 无边框 + 无阴影；输入=底 #0d0f0e + 边 1px #242b22 + 圆角 10px；卡片=底 #111514 + 1px solid #242b22 + 圆角 6px + 无阴影；表格=表头/行底边 1px #242b22
- 禁止：衬线字体、圆角、亮色块、摄影图当主视觉
- 无障碍：正文对比 12.1:1 / 主色底字 16.9:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1) contrast(1.22) brightness(.82)` + 主色双色调 opacity 0.2
- 参考：vercel.com、charm.sh、railway.com
- 样例页：`demos/04-terminal-cli.html`

### 05 玻璃拟态 + 复古未来 · Glassmorphism + Retrofuturism
- 分组：质感与视觉基调
- 定位：毛玻璃卡片浮在发光背景上，再叠一层 CRT 扫描线，介于高级与怀旧之间。
- tokens：bg `#071018` · surface `rgba(255,255,255,.07)` · ink `#eef2ec` · muted `#9fb0ad` · line `rgba(255,255,255,.14)` · accent `#dfff00` · on-accent `#071018`
- 形状：圆角 `18px` · 卡片边 `1px solid rgba(255,255,255,.16)` · 卡片影 `0 24px 60px rgba(0,0,0,.45)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：backdrop-filter blur(16px) / 半透明卡片+1px 高光描边 / 扫描线 overlay / 酸黄×深蓝高对比
- 组件：按钮=底 #dfff00 + 字 #071018 + 无边框 + 无阴影；输入=底 #071018 + 边 1px rgba(255,255,255,.14) + 圆角 999px；卡片=底 rgba(255,255,255,.07) + 1px solid rgba(255,255,255,.16) + 圆角 18px + 0 24px 60px rgba(0,0,0,.45)；表格=表头/行底边 1px rgba(255,255,255,.14)
- 禁止：不透明实心卡片、无模糊、暖色调、细边框
- 无障碍：正文对比 16.9:1 / 主色底字 16.8:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.1) brightness(.92)`
- 参考：apple.com、microsoft.com、dribbble.com
- 样例页：`demos/05-glassmorphism-retro.html`

### 06 体素美学 · Voxel Aesthetic
- 分组：复古与怀旧
- 定位：用 16×16 的方块世界语言做界面，像在网页里开了一局沙盒游戏。
- tokens：bg `#1b2417` · surface `#2c3a24` · ink `#e8e4d4` · muted `#9aa88f` · line `#0e140b` · accent `#7B8F3A` · on-accent `#0e140b`
- 形状：圆角 `0` · 卡片边 `3px solid #0e140b` · 卡片影 `inset 0 -6px 0 rgba(0,0,0,.35),inset 0 4px 0 rgba(255,255,255,.07)` · 按钮边 `2px solid #0e140b` · 按钮影 `inset 0 -5px 0 rgba(0,0,0,.4),inset 0 3px 0 rgba(255,255,255,.18)`
- 字体：标题 等宽 800 · 元信息等宽 · 行高 1.12 · 标题字距 0 · 小标签 大写 .16em
- 必用手法：image-rendering: pixelated / 方块凸凹边框 / Press Start 2P 像素字 / 大地限色板 / steps() 帧动画
- 组件：按钮=底 #7B8F3A + 字 #0e140b + 2px solid #0e140b + 柔和阴影；输入=底 #1b2417 + 边 1px #0e140b + 零圆角；卡片=底 #2c3a24 + 3px solid #0e140b + 零圆角 + inset 0 -6px 0 rgba(0,0,0,.35),inset 0 4px 0 rgba(255,255,255,.07)；表格=表头/行底边 1px #0e140b
- 关键实现：方块 inset 边框（亮/暗双色）+ 16px 网格对齐
- 禁止：圆角、抗锯齿渐变、细字重、彩色渐变
- 无障碍：正文对比 12.6:1 / 主色底字 5.2:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.25) contrast(1.12)`
- 参考：minecraft.net、roblox.com、sandbox.game
- 样例页：`demos/06-voxel.html`

### 07 新拟物化 · Neumorphism
- 分组：质感与视觉基调
- 定位：元素与背景同色，只靠一明一暗两道光「挤」出立体感。
- tokens：bg `#e0e5ec` · surface `#e0e5ec` · ink `#3b4a5a` · muted `#78879a` · line `#d2d9e3` · accent `#5b7cfa` · on-accent `#ffffff`
- 形状：圆角 `20px` · 卡片边 `none` · 卡片影 `8px 8px 16px #c2c9d4,-8px -8px 16px #ffffff` · 按钮边 `none` · 按钮影 `6px 6px 12px #c2c9d4,-6px -6px 12px #ffffff`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：同色底 #e0e5ec / 双向软阴影 8px·16px / inset 按压凹陷 / 20px 大圆角 / 低对比灰蓝
- 组件：按钮=底 #5b7cfa + 字 #ffffff + 无边框 + 柔和阴影；输入=底 #e0e5ec + 边 1px #d2d9e3 + 圆角 14px；卡片=底 #e0e5ec + 无边框 + 圆角 20px + 8px 8px 16px #c2c9d4,-8px -8px 16px #ffffff；表格=表头/行底边 1px #d2d9e3
- 关键实现：同色背景 + 双向软阴影（暗右下/亮左上），按压用 inset
- 禁止：硬阴影、深色底、高对比描边、高饱和色
- 无障碍：正文对比 7.2:1 / 主色底字 3.7:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(.65) brightness(1.06)`
- 参考：neumorphism.io、figma.com、dribbble.com
- 样例页：`demos/07-neumorphism.html`

### 08 复古 Windows 95 · Retro Win95
- 分组：复古与怀旧
- 定位：完整复刻 1995 年的桌面系统：窗口、任务栏、开始按钮一个不少。
- tokens：bg `#008080` · surface `#c0c0c0` · ink `#000000` · muted `#202020` · line `#808080` · accent `#000080` · on-accent `#ffffff`
- 形状：圆角 `0` · 卡片边 `2px solid` · 卡片影 `none` · 按钮边 `2px solid` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.1 · 标题字距 0 · 小标签 .08em
- 必用手法：#008080 桌面 / outset·inset 3D 边框 / #c0c0c0 面板 / MS Sans Serif / 虚线 focus 框 / 像素图标
- 组件：按钮=底 #000080 + 字 #ffffff + 2px solid + 无阴影；输入=底 #008080 + 边 1px #808080 + 零圆角；卡片=底 #c0c0c0 + 2px solid + 零圆角 + 无阴影；表格=表头/行底边 1px #808080
- 关键实现：双色 inset 立体边框模拟凸起；标题栏 #000080；任务栏
- 禁止：圆角、扁平阴影、现代无衬线、渐变
- 无障碍：正文对比 4.4:1 / 主色底字 16.0:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1) contrast(1.3)`
- 参考：jdan.github.io/98.css、windows93.net、poolside.fm
- 样例页：`demos/08-retro-win95.html`

### 09 有机自然 · Biophilic Design
- 分组：自然·人文·无障碍
- 定位：把阳光、植物和手工纸的质感搬进屏幕，让界面会呼吸。
- tokens：bg `#f3f0e8` · surface `#fdfbf5` · ink `#2c332a` · muted `#6b7565` · line `#dedacd` · accent `#6b8a5e` · on-accent `#ffffff`
- 形状：圆角 `16px` · 卡片边 `1px solid var(--line)` · 卡片影 `0 10px 30px rgba(90,110,80,.10)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：奶油米+鼠尾草绿 / radial-gradient 树影光斑 / 纸感卡片 / 16px 大圆角 / 漫反射弱阴影
- 组件：按钮=底 #6b8a5e + 字 #ffffff + 无边框 + 无阴影；输入=底 #f3f0e8 + 边 1px #dedacd + 圆角 10px；卡片=底 #fdfbf5 + 1px solid var(--line) + 圆角 16px + 0 10px 30px rgba(90,110,80,.10)；表格=表头/行底边 1px #dedacd
- 关键实现：radial-gradient 光斑模拟树影；页眉底部 3px 绿线
- 禁止：纯黑、高饱和荧光、直角、重投影
- 无障碍：正文对比 11.4:1 / 主色底字 3.9:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.18) brightness(1.02)`
- 参考：patagonia.com、ecosia.org、airbnb.com
- 样例页：`demos/09-biophilic.html`

### 10 3D 超写实 · 3D & Hyperrealism
- 分组：科技与未来
- 定位：用透视、多层阴影和材质渐变，在平面上伪造真实的三维空间。
- tokens：bg `#f4f5f8` · surface `linear-gradient(160deg,#ffffff,#eef0f6)` · ink `#14161a` · muted `#6a6f7a` · line `rgba(20,30,60,.08)` · accent `#2b6cff` · on-accent `#ffffff`
- 形状：圆角 `22px` · 卡片边 `1px solid rgba(255,255,255,.9)` · 卡片影 `0 24px 60px rgba(20,30,60,.14),0 2px 6px rgba(20,30,60,.06)` · 按钮边 `none` · 按钮影 `0 10px 24px rgba(43,108,255,.35)`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：perspective 1000px / hover 多轴位移+旋转 / 多层 rgba 光照阴影 / 玻璃金属渐变 / 平滑缓动
- 组件：按钮=底 #2b6cff + 字 #ffffff + 无边框 + 柔和阴影；输入=底 #f4f5f8 + 边 1px rgba(20,30,60,.08) + 圆角 14px；卡片=底 linear-gradient(160deg,#ffffff,#eef0f6) + 1px solid rgba(255,255,255,.9) + 圆角 22px + 0 24px 60px rgba(20,30,60,.14),0 2px 6px rgba(20,30,60,.06)；表格=表头/行底边 1px rgba(20,30,60,.08)
- 关键实现：perspective 1000px + 多层光照阴影
- 禁止：扁平无层次、零阴影、纯二维色块
- 无障碍：正文对比 16.6:1 / 主色底字 4.5:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.05) contrast(1.05)`
- 参考：apple.com、tesla.com、spline.design
- 样例页：`demos/10-3d-hyperrealism.html`

### 11 鲜艳块状 · Vibrant & Block-based
- 分组：粗野与反设计
- 定位：大色块 + 撞色 + 粗边框，把页面做成一块块高饱和积木。
- tokens：bg `#ffffff` · surface `#ffffff` · ink `#111111` · muted `#6d6d63` · line `#111111` · accent `#ff6b6b` · on-accent `#111111`
- 形状：圆角 `0` · 卡片边 `3px solid #111` · 卡片影 `4px 8px 0 #111` · 按钮边 `3px solid #111` · 按钮影 `4px 6px 0 #111`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.04em · 小标签 .08em
- 必用手法：红黄高饱和撞色 / 4-8px 硬阴影 / 3px 黑边 / 零圆角 / 白底衬托色彩张力
- 组件：按钮=底 #ff6b6b + 字 #111111 + 3px solid #111 + 硬影（模糊 0）；输入=底 #ffffff + 边 1px #111111 + 零圆角；卡片=底 #ffffff + 3px solid #111 + 零圆角 + 4px 8px 0 #111；表格=表头/行底边 1px #111111
- 禁止：低饱和、细边框、留白过多、灰度照片
- 无障碍：正文对比 18.9:1 / 主色底字 6.8:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.45)`
- 参考：spotify.com、duolingo.com、mailchimp.com
- 样例页：`demos/11-vibrant-block.html`

### 12 OLED 暗黑 · Dark Mode OLED
- 分组：质感与视觉基调
- 定位：为纯黑屏幕优化的暗色方案：黑得彻底、亮得克制。
- tokens：bg `#000000` · surface `#0a0a0a` · ink `#ffffff` · muted `#9a9a9a` · line `#1a1a1a` · accent `#ffffff` · on-accent `#000000`
- 形状：圆角 `14px` · 卡片边 `1px solid #1a1a1a` · 卡片影 `none` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.03em · 小标签 .08em
- 必用手法：#000 纯黑底 / #0a0a0a 卡片+1px #1a1a1a 描边 / 白字灰文 / 反色按钮作视觉锚点 / 省电
- 组件：按钮=底 #ffffff + 字 #000000 + 无边框 + 无阴影；输入=底 #000000 + 边 1px #1a1a1a + 圆角 10px；卡片=底 #0a0a0a + 1px solid #1a1a1a + 圆角 14px + 无阴影；表格=表头/行底边 1px #1a1a1a
- 禁止：任何非黑背景、浅灰卡片、彩色强调色
- 无障碍：正文对比 21.0:1 / 主色底字 21.0:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:brightness(.72) contrast(1.15) saturate(.9)`
- 参考：linear.app、vercel.com、apple.com
- 样例页：`demos/12-dark-oled.html`

### 13 无障碍伦理 · Accessible & Ethical
- 分组：自然·人文·无障碍
- 定位：把可读性和可达性当第一美学，宁可朴素也不牺牲可用。
- tokens：bg `#ffffff` · surface `#ffffff` · ink `#000000` · muted `#3a3a3a` · line `#000000` · accent `#0033cc` · on-accent `#ffffff`
- 形状：圆角 `6px` · 卡片边 `2px solid #000` · 卡片影 `none` · 按钮边 `2px solid #000` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：WCAG AA·AAA 4.5:1 / 2px 粗边框 / Atkinson Hyperlegible 字体 / 44×44 触摸目标 / 可见 focus 环
- 组件：按钮=底 #0033cc + 字 #ffffff + 2px solid #000 + 无阴影；输入=底 #ffffff + 边 1px #000000 + 圆角 6px；卡片=底 #ffffff + 2px solid #000 + 圆角 6px + 无阴影；表格=表头/行底边 1px #000000
- 禁止：低对比、细边框、隐藏 focus、仅靠颜色传信息
- 无障碍：正文对比 21.0:1 / 主色底字 9.0:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:none`
- 参考：gov.uk、w3.org/WAI、apple.com/accessibility
- 样例页：`demos/13-accessible-ethical.html`

### 14 粘土风 · Claymorphism
- 分组：质感与视觉基调
- 定位：元素像被手指揉圆的粘土，柔软、有体积、没有一条硬边。
- tokens：bg `#f5d3ae` · surface `linear-gradient(145deg,#ffdcb8,#eec296)` · ink `#4a3324` · muted `#8a6a52` · line `rgba(74,51,36,.12)` · accent `#d2691e` · on-accent `#ffffff`
- 形状：圆角 `24px` · 卡片边 `none` · 卡片影 `10px 10px 20px #d9b48f,-10px -10px 20px #ffe6c9` · 按钮边 `none` · 按钮影 `8px 8px 16px #d9b48f,-8px -8px 16px #ffe6c9`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：双向软阴影+内阴影做体积 / 24px 超大圆角 / 暖杏→可可色 / 无边框只靠光影
- 组件：按钮=底 #d2691e + 字 #ffffff + 无边框 + 柔和阴影；输入=底 #f5d3ae + 边 1px rgba(74,51,36,.12) + 圆角 18px；卡片=底 linear-gradient(145deg,#ffdcb8,#eec296) + 无边框 + 圆角 24px + 10px 10px 20px #d9b48f,-10px -10px 20px #ffe6c9；表格=表头/行底边 1px rgba(74,51,36,.12)
- 关键实现：双向软阴影 + 24px 超大圆角；按压 inset
- 禁止：尖角、硬阴影、高饱和、1px 细边框
- 无障碍：正文对比 8.3:1 / 主色底字 3.6:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.15) sepia(.1)`
- 参考：claymorphism.io、dribbble.com、duolingo.com
- 样例页：`demos/14-claymorphism.html`

### 15 极光界面 · Aurora UI
- 分组：质感与视觉基调
- 定位：深色底上流动的极光色斑配毛玻璃，近年 SaaS 的「高级感模板」。
- tokens：bg `#06070a` · surface `rgba(255,255,255,.05)` · ink `#f2f6f4` · muted `#96a3a2` · line `rgba(255,255,255,.08)` · accent `#0d9488` · on-accent `#eafffb`
- 形状：圆角 `18px` · 卡片边 `1px solid rgba(255,255,255,.09)` · 卡片影 `0 24px 60px rgba(0,0,0,.5)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：多层 radial-gradient 光斑 / blur(10px) 毛玻璃 / 翡翠绿按钮 / 1px 微光描边
- 组件：按钮=底 #0d9488 + 字 #eafffb + 无边框 + 无阴影；输入=底 #06070a + 边 1px rgba(255,255,255,.08) + 圆角 999px；卡片=底 rgba(255,255,255,.05) + 1px solid rgba(255,255,255,.09) + 圆角 18px + 0 24px 60px rgba(0,0,0,.5)；表格=表头/行底边 1px rgba(255,255,255,.08)
- 关键实现：多层 radial-gradient 光斑 + blur(10px) 毛玻璃
- 禁止：纯色背景、不透明卡片、暖色、硬边
- 无障碍：正文对比 18.5:1 / 主色底字 3.6:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.2) brightness(.9)`
- 参考：stripe.com、linear.app、raycast.com
- 样例页：`demos/15-aurora-ui.html`

### 16 复古未来 · Retro-Futurism
- 分组：复古与怀旧
- 定位：80 年代人们想象的未来：太空紫、霓虹粉、会发光的按钮。
- tokens：bg `#1a0a2e` · surface `rgba(40,20,60,.8)` · ink `#ffe9f4` · muted `#b58fc2` · line `rgba(255,107,157,.28)` · accent `#ff6b9d` · on-accent `#1a0a2e`
- 形状：圆角 `16px` · 卡片边 `1px solid rgba(255,107,157,.35)` · 卡片影 `0 0 30px rgba(255,107,157,.22)` · 按钮边 `none` · 按钮影 `0 0 18px rgba(255,107,157,.5)`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：#1a0a2e 太空紫 / 霓虹粉发光辉影 / 半透明紫卡片 / 80s 科幻标题 / 比赛博朋克更暖
- 组件：按钮=底 #ff6b9d + 字 #1a0a2e + 无边框 + 发光（无偏移）；输入=底 #1a0a2e + 边 1px rgba(255,107,157,.28) + 圆角 10px；卡片=底 rgba(40,20,60,.8) + 1px solid rgba(255,107,157,.35) + 圆角 16px + 0 0 30px rgba(255,107,157,.22)；表格=表头/行底边 1px rgba(255,107,157,.28)
- 关键实现：霓虹发光 box-shadow 0 0 Npx；太空紫底
- 禁止：冷灰、无发光、扁平无辉光、极简排版
- 无障碍：正文对比 16.2:1 / 主色底字 7.0:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:hue-rotate(-10deg) saturate(1.3) brightness(.9)`
- 参考：spacex.com、tesla.com、awwwards.com
- 样例页：`demos/16-retro-futurism.html`

### 17 扁平设计 · Flat Design
- 分组：质感与视觉基调
- 定位：去掉一切阴影、渐变和纹理，只留颜色、形状和字。
- tokens：bg `#f7f8fa` · surface `#ffffff` · ink `#1b2733` · muted `#6b7b8c` · line `#e6eaee` · accent `#3490dc` · on-accent `#ffffff`
- 形状：圆角 `4px` · 卡片边 `1px solid #e6eaee` · 卡片影 `none` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：零阴影零渐变 / 纯色块 / 品牌蓝 #3490dc / 3-4px 小圆角 / 渲染极快
- 组件：按钮=底 #3490dc + 字 #ffffff + 无边框 + 无阴影；输入=底 #f7f8fa + 边 1px #e6eaee + 圆角 4px；卡片=底 #ffffff + 1px solid #e6eaee + 圆角 4px + 无阴影；表格=表头/行底边 1px #e6eaee
- 禁止：任何阴影、渐变、拟物质感、长投影
- 无障碍：正文对比 14.3:1 / 主色底字 3.4:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.2) contrast(1.05)`
- 参考：material.io、microsoft.com
- 样例页：`demos/17-flat-design.html`

### 18 液态玻璃 · Liquid Glass
- 分组：质感与视觉基调
- 定位：Apple 2025 年的设计语言：界面像一层会折射背景的液态玻璃。
- tokens：bg `#0b1020` · surface `rgba(255,255,255,.035)` · ink `#eaf0ff` · muted `#9fb0d0` · line `rgba(255,255,255,.12)` · accent `#a5b4fc` · on-accent `#0b1020`
- 形状：圆角 `18px` · 卡片边 `1px solid rgba(255,255,255,.14)` · 卡片影 `0 24px 60px rgba(0,0,0,.5)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：blur(20px) 强模糊 / 极透卡片 / 16px 大圆角模拟表面张力 / 随内容变色的微光描边 / 高光流动
- 组件：按钮=底 #a5b4fc + 字 #0b1020 + 无边框 + 无阴影；输入=底 #0b1020 + 边 1px rgba(255,255,255,.12) + 圆角 999px；卡片=底 rgba(255,255,255,.035) + 1px solid rgba(255,255,255,.14) + 圆角 18px + 0 24px 60px rgba(0,0,0,.5)；表格=表头/行底边 1px rgba(255,255,255,.12)
- 关键实现：blur(20px) + 1px 高光描边 + 极透卡片
- 禁止：不透明卡片、硬边、纯色底、重描边
- 无障碍：正文对比 16.6:1 / 主色底字 9.5:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.15) brightness(.85)`
- 参考：apple.com、apple.com/apple-vision-pro
- 样例页：`demos/18-liquid-glass.html`

### 19 动效驱动 · Motion-Driven
- 分组：动态与交互
- 定位：页面几乎靠动效讲故事，滚动、悬停、转场本身就是内容。
- tokens：bg `#000000` · surface `#0d0d0d` · ink `#ffffff` · muted `#9c9c9c` · line `#222222` · accent `#ff3b30` · on-accent `#ffffff`
- 形状：圆角 `16px` · 卡片边 `1px solid #222` · 卡片影 `none` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：弹簧缓动回弹 / hover 缩放旋转 / 滚动驱动动画 / 暗色舞台 / 尊重 prefers-reduced-motion
- 组件：按钮=底 #ff3b30 + 字 #ffffff + 无边框 + 无阴影；输入=底 #000000 + 边 1px #222222 + 圆角 12px；卡片=底 #0d0d0d + 1px solid #222 + 圆角 16px + 无阴影；表格=表头/行底边 1px #222222
- 关键实现：弹簧缓动 cubic-bezier(.34,1.56,.64,1)；必须做 reduced-motion 兜底
- 禁止：静态无反馈、无过渡、纯色平涂
- 无障碍：正文对比 21.0:1 / 主色底字 3.5:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:contrast(1.18) brightness(.85)`
- 参考：lusion.co、activetheory.net、awwwards.com
- 样例页：`demos/19-motion-driven.html`

### 20 微交互 · Micro-interactions
- 分组：动态与交互
- 定位：不追求视觉冲击，而是在每个按钮、每个状态里塞进恰到好处的反馈。
- tokens：bg `#fbfbfc` · surface `#ffffff` · ink `#16181d` · muted `#6a7080` · line `#eeeeee` · accent `#3b5bdb` · on-accent `#ffffff`
- 形状：圆角 `10px` · 卡片边 `1px solid #eee` · 卡片影 `0 2px 4px rgba(0,0,0,.04)` · 按钮边 `none` · 按钮影 `0 2px 4px rgba(59,91,219,.18)`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：按压 scale(0.95) / 200-300ms 标准缓动 / 渐进阴影 / hover 抬升 2px / 1px 精确描边
- 组件：按钮=底 #3b5bdb + 字 #ffffff + 无边框 + 柔和阴影；输入=底 #fbfbfc + 边 1px #eeeeee + 圆角 8px；卡片=底 #ffffff + 1px solid #eee + 圆角 10px + 0 2px 4px rgba(0,0,0,.04)；表格=表头/行底边 1px #eeeeee
- 禁止：跳变式状态切换、无过渡、强装饰
- 无障碍：正文对比 17.2:1 / 主色底字 5.7:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:none`
- 参考：stripe.com、linear.app、superhuman.com
- 样例页：`demos/20-micro-interactions.html`

### 21 包容性设计 · Inclusive Design
- 分组：自然·人文·无障碍
- 定位：假设用户有视力、运动、认知等各种差异，让所有人用同一个界面。
- tokens：bg `#ffffff` · surface `#ffffff` · ink `#111111` · muted `#4a4a4a` · line `#111111` · accent `#0055d4` · on-accent `#ffffff`
- 形状：圆角 `8px` · 卡片边 `2px solid #111` · 卡片影 `none` · 按钮边 `2px solid #111` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：高对比粗边框 / 大触摸目标 / 可见焦点导航 / ≥16px 字号+1.6 行高 / 信息不只靠颜色
- 组件：按钮=底 #0055d4 + 字 #ffffff + 2px solid #111 + 无阴影；输入=底 #ffffff + 边 1px #111111 + 圆角 8px；卡片=底 #ffffff + 2px solid #111 + 圆角 8px + 无阴影；表格=表头/行底边 1px #111111
- 禁止：低对比、隐藏 focus、小触摸目标、仅靠颜色
- 无障碍：正文对比 18.9:1 / 主色底字 6.5:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:none`
- 参考：microsoft.com/design/inclusive、gov.uk、apple.com/accessibility
- 样例页：`demos/21-inclusive-design.html`

### 22 零界面 · Zero Interface
- 分组：科技与未来
- 定位：界面退到近乎不存在，只留文字和留白，交互靠对话而非点击。
- tokens：bg `#ffffff` · surface `transparent` · ink `#111111` · muted `#8a8a8a` · line `#eeeeee` · accent `#111111` · on-accent `#ffffff`
- 形状：圆角 `0` · 卡片边 `none` · 卡片影 `none` · 按钮边 `1px solid #cccccc` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 600 · 元信息等宽 · 行高 1.12 · 标题字距 -.03em · 小标签 .08em
- 必用手法：透明无边框卡片 / 无装饰性 hover / 留白即层级 / 单一输入框 / 适合 AI 与语音场景
- 组件：按钮=底 #111111 + 字 #ffffff + 1px solid #cccccc + 无阴影；输入=底 #ffffff + 边 1px #eeeeee + 圆角 999px；卡片=底 transparent + 无边框 + 零圆角 + 无阴影；表格=表头/行底边 1px #eeeeee
- 禁止：边框、阴影、装饰元素、多层级
- 无障碍：正文对比 18.9:1 / 主色底字 18.9:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1) opacity(.9)`
- 参考：chatgpt.com、claude.ai、perplexity.ai
- 样例页：`demos/22-zero-interface.html`

### 23 柔和 UI 进化 · Soft UI Evolution
- 分组：质感与视觉基调
- 定位：新拟物与扁平之间的企业级折中：有一点软，但绝不牺牲清晰。
- tokens：bg `#eef0f4` · surface `#ffffff` · ink `#2a2f3a` · muted `#6f7787` · line `#e4e7ee` · accent `#6382dc` · on-accent `#ffffff`
- 形状：圆角 `14px` · 卡片边 `1px solid #e4e7ee` · 卡片影 `0 2px 12px rgba(40,50,80,.08)` · 按钮边 `none` · 按钮影 `0 2px 8px rgba(99,130,220,.25)`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：1px 边框+双层柔阴影 / 浅蓝灰底 #eef0f4 / 蓝紫按钮 #6382dc / 14px 圆角软垫感
- 组件：按钮=底 #6382dc + 字 #ffffff + 无边框 + 柔和阴影；输入=底 #eef0f4 + 边 1px #e4e7ee + 圆角 12px；卡片=底 #ffffff + 1px solid #e4e7ee + 圆角 14px + 0 2px 12px rgba(40,50,80,.08)；表格=表头/行底边 1px #e4e7ee
- 禁止：硬阴影、纯黑、高饱和、直角
- 无障碍：正文对比 11.8:1 / 主色底字 3.6:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(.95) brightness(1.03)`
- 参考：notion.so、linear.app、slack.com
- 样例页：`demos/23-soft-ui.html`

### 24 新粗野 2.0 · Neubrutalism
- 分组：粗野与反设计
- 定位：粗野主义的乐观版：奶油底、红黄撞色、粗黑边，年轻品牌的标准动作。
- tokens：bg `#fffaee` · surface `#ffffff` · ink `#111111` · muted `#6d6d63` · line `#111111` · accent `#ff6b6b` · on-accent `#111111`
- 形状：圆角 `0` · 卡片边 `3px solid #000` · 卡片影 `4px 4px 0 #000` · 按钮边 `3px solid #000` · 按钮影 `4px 4px 0 #000`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.03em · 小标签 .08em
- 必用手法：#fffaee 奶油底 / 红黄撞色 / 3px 黑边 / 4px 无模糊硬阴影 / 零圆角
- 组件：按钮=底 #ff6b6b + 字 #111111 + 3px solid #000 + 硬影（模糊 0）；输入=底 #fffaee + 边 1px #111111 + 零圆角；卡片=底 #ffffff + 3px solid #000 + 零圆角 + 4px 4px 0 #000；表格=表头/行底边 1px #111111
- 禁止：灰白底、冷色、细边框、保守排版
- 无障碍：正文对比 18.1:1 / 主色底字 6.8:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.35) contrast(1.1)`
- 参考：gumroad.com、clerk.com、cal.com
- 样例页：`demos/24-neubrutalism.html`

### 25 便当盒网格 · Bento Box Grid
- 分组：排版与网格
- 定位：像日式便当一样把不等大的圆角卡片拼在一起，一屏讲清所有卖点。
- tokens：bg `#f5f5f7` · surface `#ffffff` · ink `#1d1d1f` · muted `#6e6e73` · line `#e8e8ed` · accent `#0071e3` · on-accent `#ffffff`
- 形状：圆角 `18px` · 卡片边 `none` · 卡片影 `0 1px 3px rgba(0,0,0,.06)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.06 · 标题字距 -.035em · 小标签 .08em
- 必用手法：grid-column·row span 拼贴 / Apple 灰 #f5f5f7 / 18px 圆角 / 无边框靠留白分区 / 胶囊按钮
- 组件：按钮=底 #0071e3 + 字 #ffffff + 无边框 + 无阴影；输入=底 #f5f5f7 + 边 1px #e8e8ed + 圆角 999px；卡片=底 #ffffff + 无边框 + 圆角 18px + 0 1px 3px rgba(0,0,0,.06)；表格=表头/行底边 1px #e8e8ed
- 禁止：边框、浓阴影、非对齐、杂乱拼贴
- 无障碍：正文对比 15.5:1 / 主色底字 4.7:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.05)`
- 参考：apple.com、vercel.com、nothing.tech
- 样例页：`demos/25-bento-grid.html`

### 26 Y2K 美学 · Y2K Aesthetic
- 分组：复古与怀旧
- 定位：千禧年对未来的想象：冰蓝粉渐变、金属高光、圆润到发亮的控件。
- tokens：bg `#d1f7ff` · surface `rgba(255,255,255,.55)` · ink `#2b1b3a` · muted `#5f5470` · line `rgba(255,255,255,.7)` · accent `#ff69b4` · on-accent `#ffffff`
- 形状：圆角 `18px` · 卡片边 `1px solid rgba(255,255,255,.85)` · 卡片影 `0 12px 30px rgba(255,105,180,.28)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：冰蓝→樱花粉渐变 / 磨砂半透明 / 粉红 #ff69b4 主色+辉光 / 16px 胶囊圆角
- 组件：按钮=底 #ff69b4 + 字 #ffffff + 无边框 + 无阴影；输入=底 #d1f7ff + 边 1px rgba(255,255,255,.7) + 圆角 999px；卡片=底 rgba(255,255,255,.55) + 1px solid rgba(255,255,255,.85) + 圆角 18px + 0 12px 30px rgba(255,105,180,.28)；表格=表头/行底边 1px rgba(255,255,255,.7)
- 关键实现：冰蓝→樱花粉渐变 + 磨砂卡片 + 金属高光
- 禁止：暗色、低饱和、直角、无高光
- 无障碍：正文对比 14.0:1 / 主色底字 2.6:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.5) brightness(1.08) hue-rotate(-8deg)`
- 参考：poolsuite.net、mschf.com、apple.com
- 样例页：`demos/26-y2k.html`

### 27 赛博朋克 · Cyberpunk UI
- 分组：科技与未来
- 定位：高对比霓虹 + 纯黑 + 故障感，把反乌托邦科技做成视觉语言。
- tokens：bg `#0a0a0a` · surface `#0f0f12` · ink `#e9ffe9` · muted `#8a9a8a` · line `#ff00ff` · accent `#ff00ff` · on-accent `#0a0a0a`
- 形状：圆角 `0` · 卡片边 `1px solid #ff00ff` · 卡片影 `0 0 12px rgba(255,0,255,.35)` · 按钮边 `none` · 按钮影 `0 0 14px rgba(255,0,255,.55)`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 大写 .2em
- 必用手法：#0a0a0a 底+品红·亮绿霓虹 / 发光边框与文字辉光 / 等宽字体 / 零圆角 / glitch 抖动
- 组件：按钮=底 #ff00ff + 字 #0a0a0a + 无边框 + 发光（无偏移）；输入=底 #0a0a0a + 边 1px #ff00ff + 零圆角；卡片=底 #0f0f12 + 1px solid #ff00ff + 零圆角 + 0 0 12px rgba(255,0,255,.35)；表格=表头/行底边 1px #ff00ff
- 关键实现：发光边框 box-shadow 0 0 12px neon + 文字辉光
- 禁止：白底、圆角、柔和阴影、低饱和
- 无障碍：正文对比 18.8:1 / 主色底字 6.3:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.4) contrast(1.25) brightness(.8)` + 主色双色调 opacity 0.42
- 参考：cyberpunk.net、awwwards.com、mschf.com
- 样例页：`demos/27-cyberpunk.html`

### 28 AI 原生界面 · AI-Native UI
- 分组：科技与未来
- 定位：为 AI 产品长出来的视觉：蓝紫渐变、微光边框、对话优先的布局。
- tokens：bg `#fafbff` · surface `#ffffff` · ink `#141826` · muted `#666e85` · line `#e7e9f7` · accent `#667eea` · on-accent `#ffffff`
- 形状：圆角 `12px` · 卡片边 `1px solid #e7e9f7` · 卡片影 `0 6px 20px rgba(102,126,234,.10)` · 按钮边 `none` · 按钮影 `0 6px 18px rgba(102,126,234,.28)`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：#667eea→#764ba2 蓝紫渐变 / 卡片蓝紫描边+微光 / 亮白底 / 12px 流线圆角 / chat-first 布局
- 组件：按钮=底 #667eea + 字 #ffffff + 无边框 + 柔和阴影；输入=底 #fafbff + 边 1px #e7e9f7 + 圆角 10px；卡片=底 #ffffff + 1px solid #e7e9f7 + 圆角 12px + 0 6px 20px rgba(102,126,234,.10)；表格=表头/行底边 1px #e7e9f7
- 禁止：高饱和撞色、重描边、暗色底
- 无障碍：正文对比 17.1:1 / 主色底字 3.7:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.05) brightness(1.02)`
- 参考：openai.com、anthropic.com、v0.dev
- 样例页：`demos/28-ai-native.html`

### 29 孟菲斯设计 · Memphis Design
- 分组：粗野与反设计
- 定位：1981 年米兰的反现代主义：几何、撞色、波点，故意「不协调」。
- tokens：bg `#fdf6ec` · surface `#ffffff` · ink `#111111` · muted `#555550` · line `#111111` · accent `#ff6b6b` · on-accent `#111111`
- 形状：圆角 `16px` · 卡片边 `2px solid #111` · 卡片影 `6px 6px 0 #4ecdc4` · 按钮边 `2px solid #111` · 按钮影 `4px 4px 0 #111`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：粉·青·黄三色撞色 / 彩色硬阴影交替 / 波点锯齿装饰 / 错位拼贴 / 20px 胶囊按钮
- 组件：按钮=底 #ff6b6b + 字 #111111 + 2px solid #111 + 硬影（模糊 0）；输入=底 #fdf6ec + 边 1px #111111 + 圆角 999px；卡片=底 #ffffff + 2px solid #111 + 圆角 16px + 6px 6px 0 #4ecdc4；表格=表头/行底边 1px #111111
- 关键实现：彩色硬影交替（青/黑）+ 点阵贴纸装饰
- 禁止：克制配色、无装饰、直角、极简
- 无障碍：正文对比 17.6:1 / 主色底字 6.8:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.5) contrast(1.15)`
- 参考：memphis.it、dribbble.com、figma.com
- 样例页：`demos/29-memphis.html`

### 30 蒸汽波 · Vaporwave
- 分组：复古与怀旧
- 定位：80 年代合成器音乐 + 消费主义残影，粉紫霓虹里带一点虚无。
- tokens：bg `#1a0033` · surface `rgba(60,20,90,.55)` · ink `#ffe6ff` · muted `#c09ad0` · line `rgba(232,160,255,.35)` · accent `#e8a0ff` · on-accent `#1a0033`
- 形状：圆角 `10px` · 卡片边 `1px solid rgba(232,160,255,.4)` · 卡片影 `0 0 24px rgba(232,160,255,.25)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：粉紫霓虹 / 日英混排 / 大理石·棕榈·Windows 元素 / CRT 扫描线与色差 / 慢速循环
- 组件：按钮=底 #e8a0ff + 字 #1a0033 + 无边框 + 无阴影；输入=底 #1a0033 + 边 1px rgba(232,160,255,.35) + 圆角 999px；卡片=底 rgba(60,20,90,.55) + 1px solid rgba(232,160,255,.4) + 圆角 10px + 0 0 24px rgba(232,160,255,.25)；表格=表头/行底边 1px rgba(232,160,255,.35)
- 关键实现：粉紫霓虹 + CRT 扫描线 + 文字双色分离
- 禁止：亮色、锐利清晰、直角、无噪点
- 无障碍：正文对比 16.5:1 / 主色底字 10.0:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:hue-rotate(32deg) saturate(1.5) brightness(.9)` + 主色双色调 opacity 0.25
- 参考：poolsuite.net、mschf.com、awwwards.com
- 样例页：`demos/30-vaporwave.html`

### 31 维度层叠 · Dimensional Layering
- 分组：质感与视觉基调
- 定位：用递进阴影搭出清晰的 Z 轴，让信息有「离你多远」的层次。
- tokens：bg `#f0f0f5` · surface `#ffffff` · ink `#1a1d24` · muted `#5f6675` · line `#ececf2` · accent `#4f5bd5` · on-accent `#ffffff`
- 形状：圆角 `14px` · 卡片边 `1px solid #ececf2` · 卡片影 `0 1px 2px rgba(20,25,50,.06),0 4px 10px rgba(20,25,50,.06),0 12px 28px rgba(20,25,50,.08)` · 按钮边 `none` · 按钮影 `0 4px 12px rgba(79,91,213,.28)`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：1·2·4·8px 递进阴影 / #f0f0f5 浅灰舞台 / 大卡片悬浮 / 1px #eee 极浅描边
- 组件：按钮=底 #4f5bd5 + 字 #ffffff + 无边框 + 柔和阴影；输入=底 #f0f0f5 + 边 1px #ececf2 + 圆角 10px；卡片=底 #ffffff + 1px solid #ececf2 + 圆角 14px + 0 1px 2px rgba(20,25,50,.06),0 4px 10px rgba(20,25,50,.06),0 12px 28px rgba(20,25,50,.08)；表格=表头/行底边 1px #ececf2
- 禁止：扁平无层次、零阴影、纯色块
- 无障碍：正文对比 14.8:1 / 主色底字 5.5:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:none`
- 参考：linear.app、notion.so、stripe.com
- 样例页：`demos/31-dimensional-layering.html`

### 32 极度极简 · Exaggerated Minimalism
- 分组：排版与网格
- 定位：把极简推到极端：字大到占满屏，其余什么都没有。
- tokens：bg `#ffffff` · surface `#ffffff` · ink `#0a0a0a` · muted `#8a8a8a` · line `#eeeeee` · accent `#0a0a0a` · on-accent `#ffffff`
- 形状：圆角 `0` · 卡片边 `none` · 卡片影 `none` · 按钮边 `1px solid #0a0a0a` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 900 · 元信息等宽 · 行高 0.86 · 标题字距 -.055em · 小标签 .08em
- 必用手法：5rem·900 字重·-0.05em 字距 / 纯白底 / 无阴影无装饰 / 1px 细线分割 / 无 hover
- 组件：按钮=底 #0a0a0a + 字 #ffffff + 1px solid #0a0a0a + 无阴影；输入=底 #ffffff + 边 1px #eeeeee + 零圆角；卡片=底 #ffffff + 无边框 + 零圆角 + 无阴影；表格=表头/行底边 1px #eeeeee
- 禁止：阴影、圆角、装饰图形、彩色强调
- 无障碍：正文对比 19.8:1 / 主色底字 19.8:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1) contrast(1.12)`
- 参考：apple.com、muji.com、teenage.engineering
- 样例页：`demos/32-exaggerated-minimalism.html`

### 33 动态排版 · Kinetic Typography
- 分组：排版与网格
- 定位：让文字本身成为主角，靠大小、节奏和动画制造海报级冲击。
- tokens：bg `#0b0b0b` · surface `transparent` · ink `#ffffff` · muted `#a0a0a0` · line `#262626` · accent `#ff2d2d` · on-accent `#ffffff`
- 形状：圆角 `0` · 卡片边 `0` · 卡片影 `none` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 900 · 元信息等宽 · 行高 0.86 · 标题字距 -.045em · 小标签 .08em
- 必用手法：6rem+ 超大标题 / line-height 0.9 / 黑白极端对比 / 滚动与逐字动画 / 影视海报感
- 组件：按钮=底 #ff2d2d + 字 #ffffff + 无边框 + 无阴影；输入=底 #0b0b0b + 边 1px #262626 + 零圆角；卡片=底 transparent + 无边框 + 零圆角 + 无阴影；表格=表头/行底边 1px #262626
- 禁止：小字号、多层信息、装饰插图、柔和配色
- 无障碍：正文对比 19.7:1 / 主色底字 3.7:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1) contrast(1.3) brightness(.78)`
- 参考：grillitype.com、resn.co.nz、awwwards.com
- 样例页：`demos/33-kinetic-typography.html`

### 34 视差叙事 · Parallax Storytelling
- 分组：动态与交互
- 定位：用滚动速度差讲故事，像翻一本有纵深的长卷。
- tokens：bg `#f6efe3` · surface `rgba(255,255,255,.72)` · ink `#3a2f1f` · muted `#7a6a52` · line `#e0d5c0` · accent `#8b6914` · on-accent `#ffffff`
- 形状：圆角 `14px` · 卡片边 `1px solid rgba(255,255,255,.9)` · 卡片影 `0 12px 30px rgba(120,90,40,.12)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：多层滚动视差 / 半透明卡片透出背景 / 纵向渐变章节 / 长滚动节奏 / 品牌故事页
- 组件：按钮=底 #8b6914 + 字 #ffffff + 无边框 + 无阴影；输入=底 #f6efe3 + 边 1px #e0d5c0 + 圆角 8px；卡片=底 rgba(255,255,255,.72) + 1px solid rgba(255,255,255,.9) + 圆角 14px + 0 12px 30px rgba(120,90,40,.12)；表格=表头/行底边 1px #e0d5c0
- 禁止：纯色平铺、无纵深、扁平
- 无障碍：正文对比 11.4:1 / 主色底字 5.1:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:sepia(.16) saturate(1.1)`
- 参考：nytimes.com、apple.com、airbnb.com
- 样例页：`demos/34-parallax-storytelling.html`

### 35 瑞士现代 2.0 · Swiss Modernism 2.0
- 分组：排版与网格
- 定位：瑞士风格的极端化版本：去掉一切，只剩字重、行高和一条细线。
- tokens：bg `#fcfcfc` · surface `#ffffff` · ink `#0a0a0a` · muted `#666660` · line `#e6e6e6` · accent `#0a0a0a` · on-accent `#ffffff`
- 形状：圆角 `0` · 卡片边 `0` · 卡片影 `none` · 按钮边 `2px solid #0a0a0a` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 900 · 元信息等宽 · 行高 1.02 · 标题字距 -.03em · 小标签 .08em
- 必用手法：2px 顶部线分割 / 4rem·900 标题 / 0.85 行高 / 零阴影零圆角 / 纯白 #fcfcfc
- 组件：按钮=底 #0a0a0a + 字 #ffffff + 2px solid #0a0a0a + 无阴影；输入=底 #fcfcfc + 边 1px #e6e6e6 + 零圆角；卡片=底 #ffffff + 无边框 + 零圆角 + 无阴影；表格=表头/行底边 1px #e6e6e6
- 禁止：阴影、圆角、装饰图形、多色
- 无障碍：正文对比 19.3:1 / 主色底字 19.8:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1) contrast(1.15)`
- 参考：vitsœ.com、ibm.com/design/language、muji.com
- 样例页：`demos/35-swiss-modernism-2.html`

### 36 科幻 HUD · HUD / Sci-Fi FUI
- 分组：科技与未来
- 定位：电影里飞船控制台的界面语言：发光细线、角标框、滚动数据。
- tokens：bg `#001020` · surface `rgba(0,40,80,.35)` · ink `#d6f2ff` · muted `#6f9bb5` · line `rgba(0,170,255,.45)` · accent `#00aaff` · on-accent `#001020`
- 形状：圆角 `2px` · 卡片边 `1px solid rgba(0,170,255,.45)` · 卡片影 `0 0 20px rgba(0,170,255,.18),inset 0 0 30px rgba(0,170,255,.06)` · 按钮边 `none` · 按钮影 `0 0 14px rgba(0,170,255,.45)`
- 字体：标题 等宽 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 大写 .2em
- 必用手法：#001020 深空蓝 / 青色发光边框 / 等宽数据字体 / 环形与网格刻度 / 透明按钮
- 组件：按钮=底 #00aaff + 字 #001020 + 无边框 + 发光（无偏移）；输入=底 #001020 + 边 1px rgba(0,170,255,.45) + 圆角 2px；卡片=底 rgba(0,40,80,.35) + 1px solid rgba(0,170,255,.45) + 圆角 2px + 0 0 20px rgba(0,170,255,.18),inset 0 0 30px rgba(0,170,255,.06)；表格=表头/行底边 1px rgba(0,170,255,.45)
- 关键实现：四角角标框 + 环形雷达 + 等宽数据字
- 禁止：圆角、柔和阴影、亮色、衬线字体
- 无障碍：正文对比 16.4:1 / 主色底字 7.5:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(.55) brightness(.7) contrast(1.1)` + 主色双色调 opacity 0.38
- 参考：spacex.com、nasa.gov、cyberpunk.net
- 样例页：`demos/36-hud-sci-fi.html`

### 37 便当网格 2.0 · Bento Grids 2.0
- 分组：排版与网格
- 定位：便当网格的年轻化版本：暖灰底、iPhone 红点缀、更松快的圆角。
- tokens：bg `#f2f2f7` · surface `#ffffff` · ink `#111111` · muted `#6e6e73` · line `#e5e5ea` · accent `#ff3b30` · on-accent `#ffffff`
- 形状：圆角 `20px` · 卡片边 `none` · 卡片影 `none` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.03em · 小标签 .08em
- 必用手法：#f2f2f7 暖灰底 / 20px 大圆角 / 无边框靠底色分区 / grid span 拼接 / 彩色点缀
- 组件：按钮=底 #ff3b30 + 字 #ffffff + 无边框 + 无阴影；输入=底 #f2f2f7 + 边 1px #e5e5ea + 圆角 999px；卡片=底 #ffffff + 无边框 + 圆角 20px + 无阴影；表格=表头/行底边 1px #e5e5ea
- 禁止：边框、重阴影、低饱和、直角
- 无障碍：正文对比 16.9:1 / 主色底字 3.5:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.1)`
- 参考：apple.com、nothing.tech、arc.net
- 样例页：`demos/37-bento-2.html`

### 38 空间计算 · Spatial UI / VisionOS
- 分组：科技与未来
- 定位：为头显和空间屏设计：界面像悬在空气里的玻璃板，有厚度、有光照。
- tokens：bg `#05070f` · surface `rgba(255,255,255,.06)` · ink `#eaf0ff` · muted `#93a2c4` · line `rgba(255,255,255,.12)` · accent `#7c9cff` · on-accent `#05070f`
- 形状：圆角 `22px` · 卡片边 `1px solid rgba(255,255,255,.12)` · 卡片影 `0 30px 80px rgba(0,0,0,.6)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：blur(20px) 强模糊 / 22px 超大圆角 / 1px 微光玻璃轮廓 / 深空渐变 / 轻量景深
- 组件：按钮=底 #7c9cff + 字 #05070f + 无边框 + 无阴影；输入=底 #05070f + 边 1px rgba(255,255,255,.12) + 圆角 999px；卡片=底 rgba(255,255,255,.06) + 1px solid rgba(255,255,255,.12) + 圆角 22px + 0 30px 80px rgba(0,0,0,.6)；表格=表头/行底边 1px rgba(255,255,255,.12)
- 关键实现：blur(20px) + 22px 圆角 + 微光玻璃轮廓
- 禁止：不透明面板、硬边、纯色底、重描边
- 无障碍：正文对比 17.6:1 / 主色底字 7.7:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:brightness(.78) saturate(1.1)`
- 参考：apple.com/apple-vision-pro、meta.com
- 样例页：`demos/38-spatial-ui.html`

### 39 电子墨水 · E-Ink & Paper
- 分组：自然·人文·无障碍
- 定位：把屏幕做成纸：暖白底、衬线字、零阴影，为长时间阅读而生。
- tokens：bg `#faf8f0` · surface `#fffdf7` · ink `#2a2a26` · muted `#6b6b60` · line `#ddd8c8` · accent `#2a2a26` · on-accent `#faf8f0`
- 形状：圆角 `2px` · 卡片边 `0` · 卡片影 `none` · 按钮边 `1px solid #2a2a26` · 按钮影 `none`
- 字体：标题 衬线（Georgia/宋体） 400 · 元信息等宽 · 行高 1.8 · 标题字距 0 · 小标签 .08em
- 必用手法：#faf8f0 纸色 / Georgia 衬线 / 1.8 行高 / 零阴影 / 1px 细线分割 / 无动效
- 组件：按钮=底 #2a2a26 + 字 #faf8f0 + 1px solid #2a2a26 + 无阴影；输入=底 #faf8f0 + 边 1px #ddd8c8 + 圆角 2px；卡片=底 #fffdf7 + 无边框 + 圆角 2px + 无阴影；表格=表头/行底边 1px #ddd8c8
- 禁止：阴影、彩色强调、动效、渐变
- 无障碍：正文对比 13.5:1 / 主色底字 13.5:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1) contrast(1.22) brightness(1.04)`
- 参考：readwise.io/read、ia.net、amazon.com/kindle
- 样例页：`demos/39-e-ink-paper.html`

### 40 Z 世代混沌 · Gen Z Chaos / Maximalism
- 分组：粗野与反设计
- 定位：精心设计的「乱七八糟」：高饱和、错位、贴纸感，反叛一切高级感。
- tokens：bg `#0f0f0f` · surface `#ff5a1f` · ink `#111111` · muted `#3a3a3a` · line `#000000` · accent `#ffe600` · on-accent `#0f0f0f`
- 形状：圆角 `18px` · 卡片边 `2px solid #000` · 卡片影 `4px 4px 0 #000` · 按钮边 `2px solid #000` · 按钮影 `4px 4px 0 #000`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.03em · 小标签 大写 .2em
- 必用手法：亮黄·橙红高饱和 / 黑底白字混排 / 错位拼贴 / 粗边框+彩色硬阴影 / 30px 胶囊按钮
- 组件：按钮=底 #ffe600 + 字 #0f0f0f + 2px solid #000 + 硬影（模糊 0）；输入=底 #0f0f0f + 边 1px #000000 + 圆角 999px；卡片=底 #ff5a1f + 2px solid #000 + 圆角 18px + 4px 4px 0 #000；表格=表头/行底边 1px #000000
- 关键实现：粗黑边 + 彩色硬影 + 30px 胶囊按钮
- 禁止：克制、统一、对称、极简
- 无障碍：正文对比 1.0:1 / 主色底字 15.1:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.6) contrast(1.15)`
- 参考：mschf.com、gumroad.com、duolingo.com
- 样例页：`demos/40-genz-chaos.html`

### 41 仿生有机 2.0 · Biomimetic / Organic 2.0
- 分组：自然·人文·无障碍
- 定位：不只借用自然的颜色，而是借用自然的生长逻辑与结构。
- tokens：bg `#c9d6c0` · surface `rgba(255,255,255,.5)` · ink `#1e2a1e` · muted `#4d5c4a` · line `rgba(30,42,30,.12)` · accent `#2a4a2a` · on-accent `#ffffff`
- 形状：圆角 `20px` · 卡片边 `1px solid rgba(255,255,255,.6)` · 卡片影 `0 14px 40px rgba(30,50,30,.12)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：绿灰纵向渐变 / 半透明卡片像细胞壁 / 有机不规则圆角 / 生长与流动动画
- 组件：按钮=底 #2a4a2a + 字 #ffffff + 无边框 + 无阴影；输入=底 #c9d6c0 + 边 1px rgba(30,42,30,.12) + 圆角 14px；卡片=底 rgba(255,255,255,.5) + 1px solid rgba(255,255,255,.6) + 圆角 20px + 0 14px 40px rgba(30,50,30,.12)；表格=表头/行底边 1px rgba(30,42,30,.12)
- 关键实现：绿灰纵向渐变 + 半透明卡片 + 不规则有机圆角
- 禁止：纯几何、硬边、高对比黑白
- 无障碍：正文对比 9.9:1 / 主色底字 9.9:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.1) hue-rotate(-8deg)`
- 参考：biomimicry.org、patagonia.com、airbnb.com
- 样例页：`demos/41-biomimetic.html`

### 42 反精致粗糙 · Anti-Polish / Raw Aesthetic
- 分组：粗野与反设计
- 定位：刻意不做设计：虚线框、系统字体、零圆角，像线框图直接上线。
- tokens：bg `#ffffff` · surface `#ffffff` · ink `#111111` · muted `#666660` · line `#999999` · accent `#111111` · on-accent `#ffffff`
- 形状：圆角 `0` · 卡片边 `1px dashed #999999` · 卡片影 `none` · 按钮边 `1px solid #111111` · 按钮影 `none`
- 字体：标题 等宽 700 · 元信息等宽 · 行高 1.15 · 标题字距 0 · 小标签 .08em
- 必用手法：dashed 虚线边框 / 等宽或系统字体 / 零圆角零阴影 / 无 hover / 纯文本排版
- 组件：按钮=底 #111111 + 字 #ffffff + 1px solid #111111 + 无阴影；输入=底 #ffffff + 边 1px #999999 + 零圆角；卡片=底 #ffffff + 1px dashed #999999 + 零圆角 + 无阴影；表格=表头/行底边 1px #999999
- 禁止：圆角、渐变、精修阴影、装饰
- 无障碍：正文对比 18.9:1 / 主色底字 18.9:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:grayscale(1)`
- 参考：news.ycombinator.com、are.na、berkshirehathaway.com
- 样例页：`demos/42-anti-polish-raw.html`

### 43 触觉数字 · Tactile Digital / Deformable UI
- 分组：自然·人文·无障碍
- 定位：让屏幕上的东西摸起来像纸、像布、像木头，靠厚度和形变传递温度。
- tokens：bg `#f8f5f0` · surface `#fffdf9` · ink `#3a322a` · muted `#7a6f62` · line `#e6dfd2` · accent `#6b4a2f` · on-accent `#ffffff`
- 形状：圆角 `12px` · 卡片边 `1px solid #e6dfd2` · 卡片影 `0 1px 0 rgba(0,0,0,.04),0 3px 0 #e8e2d8` · 按钮边 `none` · 按钮影 `0 3px 0 #d9cbb8`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：底部 2px 实心投影做厚度 / active scale(0.98) 形变 / 棉纸亚麻底色 / 深棕木质按钮
- 组件：按钮=底 #6b4a2f + 字 #ffffff + 无边框 + 柔和阴影；输入=底 #f8f5f0 + 边 1px #e6dfd2 + 圆角 10px；卡片=底 #fffdf9 + 1px solid #e6dfd2 + 圆角 12px + 0 1px 0 rgba(0,0,0,.04),0 3px 0 #e8e2d8；表格=表头/行底边 1px #e6dfd2
- 禁止：纯数字质感、无触感、扁平、高饱和
- 无障碍：正文对比 11.6:1 / 主色底字 7.9:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:sepia(.26) saturate(1.05)`
- 参考：teenage.engineering、muji.com、braun.com
- 样例页：`demos/43-tactile-digital.html`

### 44 自然精粹 · Nature Distilled
- 分组：自然·人文·无障碍
- 定位：不画叶子不画山，只把自然提炼成比例、色温和克制的绿。
- tokens：bg `#f5f2eb` · surface `#fffdf8` · ink `#2d332a` · muted `#6f7566` · line `#e7e2d6` · accent `#5a6a4a` · on-accent `#ffffff`
- 形状：圆角 `10px` · 卡片边 `1px solid #ece7db` · 卡片影 `0 1px 2px rgba(60,70,50,.04)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：#f5f2eb 羊皮纸底 / 森林绿页眉 #5a6a4a / 0.03 极弱阴影 / 用色温而非阴影分区
- 组件：按钮=底 #5a6a4a + 字 #ffffff + 无边框 + 无阴影；输入=底 #f5f2eb + 边 1px #e7e2d6 + 圆角 8px；卡片=底 #fffdf8 + 1px solid #ece7db + 圆角 10px + 0 1px 2px rgba(60,70,50,.04)；表格=表头/行底边 1px #e7e2d6
- 禁止：高饱和、强对比、装饰图形
- 无障碍：正文对比 11.6:1 / 主色底字 5.8:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.14) sepia(.08)`
- 参考：aesop.com、kinfolk.com、patagonia.com
- 样例页：`demos/44-nature-distilled.html`

### 45 光标交互 · Interactive Cursor Design
- 分组：动态与交互
- 定位：把鼠标指针变成主角：准星、拖尾、磁吸，光标本身就是导航。
- tokens：bg `#1a1a2e` · surface `rgba(255,255,255,.05)` · ink `#e6e6ff` · muted `#9a9ac0` · line `rgba(255,255,255,.14)` · accent `#7b61ff` · on-accent `#ffffff`
- 形状：圆角 `14px` · 卡片边 `1px solid rgba(255,255,255,.12)` · 卡片影 `0 0 24px rgba(123,97,255,.22)` · 按钮边 `none` · 按钮影 `0 0 18px rgba(123,97,255,.45)`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：自定义或十字准星光标 / 拖尾与磁吸 / 发光微辉卡片 / 深紫科技底 / 隐藏默认指针
- 组件：按钮=底 #7b61ff + 字 #ffffff + 无边框 + 发光（无偏移）；输入=底 #1a1a2e + 边 1px rgba(255,255,255,.14) + 圆角 10px；卡片=底 rgba(255,255,255,.05) + 1px solid rgba(255,255,255,.12) + 圆角 14px + 0 0 24px rgba(123,97,255,.22)；表格=表头/行底边 1px rgba(255,255,255,.14)
- 禁止：默认光标、静态页面、无 hover 反馈
- 无障碍：正文对比 13.9:1 / 主色底字 4.2:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:brightness(.75) saturate(1.2)` + 主色双色调 opacity 0.28
- 参考：cuberto.com、lusion.co、aristidebenoist.com
- 样例页：`demos/45-interactive-cursor.html`

### 46 语音优先 · Voice-First Multimodal
- 分组：动态与交互
- 定位：为「说话」而设计的界面：一个入口、一圈声波，其余全部退场。
- tokens：bg `#0a0a1a` · surface `rgba(255,255,255,.045)` · ink `#ccd0ee` · muted `#7a80a8` · line `rgba(140,150,255,.18)` · accent `#6d7cff` · on-accent `#ffffff`
- 形状：圆角 `16px` · 卡片边 `1px solid rgba(140,150,255,.16)` · 卡片影 `0 0 40px rgba(109,124,255,.18)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：#0a0a1a 极深底 / 柔和蓝紫文字 / 声波纹扩散动效 / 16px 大圆角 / 单一语音入口
- 组件：按钮=底 #6d7cff + 字 #ffffff + 无边框 + 无阴影；输入=底 #0a0a1a + 边 1px rgba(140,150,255,.18) + 圆角 999px；卡片=底 rgba(255,255,255,.045) + 1px solid rgba(140,150,255,.16) + 圆角 16px + 0 0 40px rgba(109,124,255,.18)；表格=表头/行底边 1px rgba(140,150,255,.18)
- 禁止：密集信息、多个并列按钮、无主焦点
- 无障碍：正文对比 12.9:1 / 主色底字 3.5:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:brightness(.58) saturate(.8)` + 主色双色调 opacity 0.32
- 参考：pi.ai、chatgpt.com、alexa.amazon.com
- 样例页：`demos/46-voice-first.html`

### 47 3D 产品展示 · 3D Product Preview
- 分组：科技与未来
- 定位：像摄影棚一样把产品放在无影墙前，让 3D 模型成为唯一内容。
- tokens：bg `#fafafa` · surface `#ffffff` · ink `#111111` · muted `#6b6b6b` · line `#ececec` · accent `#111111` · on-accent `#ffffff`
- 形状：圆角 `14px` · 卡片边 `none` · 卡片影 `none` · 按钮边 `1px solid #111111` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.04em · 小标签 .08em
- 必用手法：浅色无影棚背景 / 产品居中悬浮+大投影 / 可旋转与配置器 / AR 预览 / 单色系统
- 组件：按钮=底 #111111 + 字 #ffffff + 1px solid #111111 + 无阴影；输入=底 #fafafa + 边 1px #ececec + 圆角 999px；卡片=底 #ffffff + 无边框 + 圆角 14px + 无阴影；表格=表头/行底边 1px #ececec
- 禁止：杂乱背景、多彩、装饰元素
- 无障碍：正文对比 18.1:1 / 主色底字 18.9:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:brightness(1.02)`
- 参考：apple.com、nike.com、ikea.com
- 样例页：`demos/47-3d-product.html`

### 48 渐变网格 · Gradient Mesh / Aurora Evolved
- 分组：质感与视觉基调
- 定位：极光 UI 的进化版：多层多色光斑交织，像一张会呼吸的渐变网格。
- tokens：bg `#0a0616` · surface `rgba(255,255,255,.04)` · ink `#f6efff` · muted `#a99cc4` · line `rgba(255,255,255,.12)` · accent `#ff7ab6` · on-accent `#0a0616`
- 形状：圆角 `16px` · 卡片边 `1px solid rgba(255,255,255,.10)` · 卡片影 `0 24px 60px rgba(0,0,0,.5)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 无衬线（系统/PingFang） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：多层 radial-gradient 网格叠加 / 0.04 极透玻璃卡片 / 描边随光斑变色 / 色彩反射按钮
- 组件：按钮=底 #ff7ab6 + 字 #0a0616 + 无边框 + 无阴影；输入=底 #0a0616 + 边 1px rgba(255,255,255,.12) + 圆角 999px；卡片=底 rgba(255,255,255,.04) + 1px solid rgba(255,255,255,.10) + 圆角 16px + 0 24px 60px rgba(0,0,0,.5)；表格=表头/行底边 1px rgba(255,255,255,.12)
- 禁止：纯色背景、不透明卡片、硬边
- 无障碍：正文对比 17.8:1 / 主色底字 8.3:1；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:saturate(1.25) brightness(.85)` + 主色双色调 opacity 0.26
- 参考：stripe.com、framer.com、linear.app
- 样例页：`demos/48-gradient-mesh.html`

### 49 色差 RGB 分裂 · Chromatic Aberration / RGB Split
- 分组：粗野与反设计
- 定位：把镜头色差这个「缺陷」变成设计语言，红绿蓝错位制造数字故障感。
- tokens：bg `#000000` · surface `#0c0c0c` · ink `#f2f2f2` · muted `#8a8a8a` · line `#333333` · accent `#ff0044` · on-accent `#ffffff`
- 形状：圆角 `0` · 卡片边 `1px solid #333333` · 卡片影 `2px 0 0 rgba(255,0,68,.7),-2px 0 0 rgba(0,229,255,.7)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 等宽 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：红·绿·蓝错位描边 / text-shadow 2px 0 红、-2px 0 蓝 / 黑底等宽字体 / hover 错位跳变
- 组件：按钮=底 #ff0044 + 字 #ffffff + 无边框 + 无阴影；输入=底 #000000 + 边 1px #333333 + 零圆角；卡片=底 #0c0c0c + 1px solid #333333 + 零圆角 + 2px 0 0 rgba(255,0,68,.7),-2px 0 0 rgba(0,229,255,.7)；表格=表头/行底边 1px #333333
- 关键实现：红/绿/蓝三色错位描边 + hover 错位幅度加大
- 禁止：柔和配色、圆角、低对比、无错位
- 无障碍：正文对比 18.8:1 / 主色底字 3.9:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:contrast(1.2) brightness(.9)` + 主色双色调 opacity 0.22
- 参考：awwwards.com、cyberpunk.net、mschf.com
- 样例页：`demos/49-chromatic-aberration.html`

### 50 复古胶片 · Vintage Analog / Retro Film
- 分组：复古与怀旧
- 定位：旧照片和旧书的气质：暖黄氧化色、胶片颗粒、棕色调。
- tokens：bg `#f5e8d0` · surface `#faf0dd` · ink `#3a2a10` · muted `#8a7550` · line `#e3d2b0` · accent `#8b6914` · on-accent `#f7efd9`
- 形状：圆角 `4px` · 卡片边 `1px solid #e8d8b4` · 卡片影 `0 1px 3px rgba(80,60,20,.10)` · 按钮边 `none` · 按钮影 `none`
- 字体：标题 衬线（Georgia/宋体） 800 · 元信息等宽 · 行高 1.12 · 标题字距 -.02em · 小标签 .08em
- 必用手法：#f5e8d0 暖黄纸色 / Georgia 衬线 / 胶片颗粒噪点 / #3a2a10 深棕页眉 / 古铜按钮
- 组件：按钮=底 #8b6914 + 字 #f7efd9 + 无边框 + 无阴影；输入=底 #f5e8d0 + 边 1px #e3d2b0 + 圆角 4px；卡片=底 #faf0dd + 1px solid #e8d8b4 + 圆角 4px + 0 1px 3px rgba(80,60,20,.10)；表格=表头/行底边 1px #e3d2b0
- 关键实现：胶片颗粒叠加层 + 深棕页眉 + 古铜按钮
- 禁止：纯白、高饱和、锐利边缘、无颗粒
- 无障碍：正文对比 11.4:1 / 主色底字 4.4:1（偏低，需加深文字或用描边补强）；focus 必须可见（≥2px 实线 + offset 2px）；触摸目标 ≥44px
- 影像：`filter:sepia(.35) saturate(.85) contrast(1.05)`
- 参考：aesop.com、kinfolk.com、nytimes.com
- 样例页：`demos/50-vintage-film.html`



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
