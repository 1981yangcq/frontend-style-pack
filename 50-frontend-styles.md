# 前端设计风格大全

> 对应视频：https://www.bilibili.com/video/BV1pVKa6LEJF/ ｜ 原始代码仓库：https://github.com/rxw2023/Front-end-Design-Styles ｜ 风格体系参考：UI UX Pro Max Skill

| # | 风格名称 | 风格说明与特点 | 风格标杆网站 | 分组 | Demo |
|---|---|---|---|---|---|
| 1 | **新粗野主义**<br>Neo-Brutalism | 把网页当作未经打磨的原件，用粗黑边框和生硬投影表达诚实与反叛。<br>**特征**：3px 纯黑边框 / 零圆角块状卡片 / 6px 硬投影无模糊 / 点阵网格背景 / 等宽大写标签 / EXP.01 实验编号 | gumroad.com、theverge.com、balenciaga.com | 粗野与反设计 | [看效果](demos/01-neo-brutalism.html) |
| 2 | **瑞士·国际主义平面设计**<br>Swiss Style | 源自 1950s 苏黎世与巴塞尔，用网格和字号层级取代一切装饰。<br>**特征**：12 列网格 / 非对称 4+8 布局 / 900 字重无衬线标题 / 墨·灰·纸·线四色 / 目录式编号 / 全站 0 圆角 | vitsœ.com、museum-gestaltung.ch、ibm.com/design/language | 排版与网格 | [看效果](demos/02-swiss-style.html) |
| 3 | **日系编辑美学**<br>Japanese Editorial | 把杂志版式搬上网页：暖纸底、极细分割线、一处荧光色点睛。<br>**特征**：#f1f0ea 纸色底 / 低对比暖灰分割线 / 中日文混排+等宽数字 / 荧光黄标题下划线 / 超大留白 / 低饱和暖色谱 | muji.com、tsutaya.tsite.jp、ndc.co.jp | 排版与网格 | [看效果](demos/03-japanese-editorial.html) |
| 4 | **终端·开发者工具审美**<br>Terminal CLI Aesthetic | 把命令行搬进浏览器，用等宽字体和状态灯建立工程可信感。<br>**特征**：全站等宽字体 / $ 提示符与路径式文案 / 绿色脉冲状态点 / 墨黑+灰绿+酸黄冷工业色 / ASCII 装饰 | vercel.com、charm.sh、railway.com | 科技与未来 | [看效果](demos/04-terminal-cli.html) |
| 5 | **玻璃拟态 + 复古未来**<br>Glassmorphism + Retrofuturism | 毛玻璃卡片浮在发光背景上，再叠一层 CRT 扫描线，介于高级与怀旧之间。<br>**特征**：backdrop-filter blur(16px) / 半透明卡片+1px 高光描边 / 扫描线 overlay / 酸黄×深蓝高对比 | apple.com、microsoft.com、dribbble.com | 质感与视觉基调 | [看效果](demos/05-glassmorphism-retro.html) |
| 6 | **体素美学**<br>Voxel Aesthetic | 用 16×16 的方块世界语言做界面，像在网页里开了一局沙盒游戏。<br>**特征**：image-rendering: pixelated / 方块凸凹边框 / Press Start 2P 像素字 / 大地限色板 / steps() 帧动画 | minecraft.net、roblox.com、sandbox.game | 复古与怀旧 | [看效果](demos/06-voxel.html) |
| 7 | **新拟物化**<br>Neumorphism | 元素与背景同色，只靠一明一暗两道光「挤」出立体感。<br>**特征**：同色底 #e0e5ec / 双向软阴影 8px·16px / inset 按压凹陷 / 20px 大圆角 / 低对比灰蓝 | neumorphism.io、figma.com、dribbble.com | 质感与视觉基调 | [看效果](demos/07-neumorphism.html) |
| 8 | **复古 Windows 95**<br>Retro Win95 | 完整复刻 1995 年的桌面系统：窗口、任务栏、开始按钮一个不少。<br>**特征**：#008080 桌面 / outset·inset 3D 边框 / #c0c0c0 面板 / MS Sans Serif / 虚线 focus 框 / 像素图标 | jdan.github.io/98.css、windows93.net、poolside.fm | 复古与怀旧 | [看效果](demos/08-retro-win95.html) |
| 9 | **有机自然**<br>Biophilic Design | 把阳光、植物和手工纸的质感搬进屏幕，让界面会呼吸。<br>**特征**：奶油米+鼠尾草绿 / radial-gradient 树影光斑 / 纸感卡片 / 16px 大圆角 / 漫反射弱阴影 | patagonia.com、ecosia.org、airbnb.com | 自然·人文·无障碍 | [看效果](demos/09-biophilic.html) |
| 10 | **3D 超写实**<br>3D & Hyperrealism | 用透视、多层阴影和材质渐变，在平面上伪造真实的三维空间。<br>**特征**：perspective 1000px / hover 多轴位移+旋转 / 多层 rgba 光照阴影 / 玻璃金属渐变 / 平滑缓动 | apple.com、tesla.com、spline.design | 科技与未来 | [看效果](demos/10-3d-hyperrealism.html) |
| 11 | **鲜艳块状**<br>Vibrant & Block-based | 大色块 + 撞色 + 粗边框，把页面做成一块块高饱和积木。<br>**特征**：红黄高饱和撞色 / 4-8px 硬阴影 / 3px 黑边 / 零圆角 / 白底衬托色彩张力 | spotify.com、duolingo.com、mailchimp.com | 粗野与反设计 | [看效果](demos/11-vibrant-block.html) |
| 12 | **OLED 暗黑**<br>Dark Mode OLED | 为纯黑屏幕优化的暗色方案：黑得彻底、亮得克制。<br>**特征**：#000 纯黑底 / #0a0a0a 卡片+1px #1a1a1a 描边 / 白字灰文 / 反色按钮作视觉锚点 / 省电 | linear.app、vercel.com、apple.com | 质感与视觉基调 | [看效果](demos/12-dark-oled.html) |
| 13 | **无障碍伦理**<br>Accessible & Ethical | 把可读性和可达性当第一美学，宁可朴素也不牺牲可用。<br>**特征**：WCAG AA·AAA 4.5:1 / 2px 粗边框 / Atkinson Hyperlegible 字体 / 44×44 触摸目标 / 可见 focus 环 | gov.uk、w3.org/WAI、apple.com/accessibility | 自然·人文·无障碍 | [看效果](demos/13-accessible-ethical.html) |
| 14 | **粘土风**<br>Claymorphism | 元素像被手指揉圆的粘土，柔软、有体积、没有一条硬边。<br>**特征**：双向软阴影+内阴影做体积 / 24px 超大圆角 / 暖杏→可可色 / 无边框只靠光影 | claymorphism.io、dribbble.com、duolingo.com | 质感与视觉基调 | [看效果](demos/14-claymorphism.html) |
| 15 | **极光界面**<br>Aurora UI | 深色底上流动的极光色斑配毛玻璃，近年 SaaS 的「高级感模板」。<br>**特征**：多层 radial-gradient 光斑 / blur(10px) 毛玻璃 / 翡翠绿按钮 / 1px 微光描边 | stripe.com、linear.app、raycast.com | 质感与视觉基调 | [看效果](demos/15-aurora-ui.html) |
| 16 | **复古未来**<br>Retro-Futurism | 80 年代人们想象的未来：太空紫、霓虹粉、会发光的按钮。<br>**特征**：#1a0a2e 太空紫 / 霓虹粉发光辉影 / 半透明紫卡片 / 80s 科幻标题 / 比赛博朋克更暖 | spacex.com、tesla.com、awwwards.com | 复古与怀旧 | [看效果](demos/16-retro-futurism.html) |
| 17 | **扁平设计**<br>Flat Design | 去掉一切阴影、渐变和纹理，只留颜色、形状和字。<br>**特征**：零阴影零渐变 / 纯色块 / 品牌蓝 #3490dc / 3-4px 小圆角 / 渲染极快 | material.io、microsoft.com | 质感与视觉基调 | [看效果](demos/17-flat-design.html) |
| 18 | **液态玻璃**<br>Liquid Glass | Apple 2025 年的设计语言：界面像一层会折射背景的液态玻璃。<br>**特征**：blur(20px) 强模糊 / 极透卡片 / 16px 大圆角模拟表面张力 / 随内容变色的微光描边 / 高光流动 | apple.com、apple.com/apple-vision-pro | 质感与视觉基调 | [看效果](demos/18-liquid-glass.html) |
| 19 | **动效驱动**<br>Motion-Driven | 页面几乎靠动效讲故事，滚动、悬停、转场本身就是内容。<br>**特征**：弹簧缓动回弹 / hover 缩放旋转 / 滚动驱动动画 / 暗色舞台 / 尊重 prefers-reduced-motion | lusion.co、activetheory.net、awwwards.com | 动态与交互 | [看效果](demos/19-motion-driven.html) |
| 20 | **微交互**<br>Micro-interactions | 不追求视觉冲击，而是在每个按钮、每个状态里塞进恰到好处的反馈。<br>**特征**：按压 scale(0.95) / 200-300ms 标准缓动 / 渐进阴影 / hover 抬升 2px / 1px 精确描边 | stripe.com、linear.app、superhuman.com | 动态与交互 | [看效果](demos/20-micro-interactions.html) |
| 21 | **包容性设计**<br>Inclusive Design | 假设用户有视力、运动、认知等各种差异，让所有人用同一个界面。<br>**特征**：高对比粗边框 / 大触摸目标 / 可见焦点导航 / ≥16px 字号+1.6 行高 / 信息不只靠颜色 | microsoft.com/design/inclusive、gov.uk、apple.com/accessibility | 自然·人文·无障碍 | [看效果](demos/21-inclusive-design.html) |
| 22 | **零界面**<br>Zero Interface | 界面退到近乎不存在，只留文字和留白，交互靠对话而非点击。<br>**特征**：透明无边框卡片 / 无装饰性 hover / 留白即层级 / 单一输入框 / 适合 AI 与语音场景 | chatgpt.com、claude.ai、perplexity.ai | 科技与未来 | [看效果](demos/22-zero-interface.html) |
| 23 | **柔和 UI 进化**<br>Soft UI Evolution | 新拟物与扁平之间的企业级折中：有一点软，但绝不牺牲清晰。<br>**特征**：1px 边框+双层柔阴影 / 浅蓝灰底 #eef0f4 / 蓝紫按钮 #6382dc / 14px 圆角软垫感 | notion.so、linear.app、slack.com | 质感与视觉基调 | [看效果](demos/23-soft-ui.html) |
| 24 | **新粗野 2.0**<br>Neubrutalism | 粗野主义的乐观版：奶油底、红黄撞色、粗黑边，年轻品牌的标准动作。<br>**特征**：#fffaee 奶油底 / 红黄撞色 / 3px 黑边 / 4px 无模糊硬阴影 / 零圆角 | gumroad.com、clerk.com、cal.com | 粗野与反设计 | [看效果](demos/24-neubrutalism.html) |
| 25 | **便当盒网格**<br>Bento Box Grid | 像日式便当一样把不等大的圆角卡片拼在一起，一屏讲清所有卖点。<br>**特征**：grid-column·row span 拼贴 / Apple 灰 #f5f5f7 / 18px 圆角 / 无边框靠留白分区 / 胶囊按钮 | apple.com、vercel.com、nothing.tech | 排版与网格 | [看效果](demos/25-bento-grid.html) |
| 26 | **Y2K 美学**<br>Y2K Aesthetic | 千禧年对未来的想象：冰蓝粉渐变、金属高光、圆润到发亮的控件。<br>**特征**：冰蓝→樱花粉渐变 / 磨砂半透明 / 粉红 #ff69b4 主色+辉光 / 16px 胶囊圆角 | poolsuite.net、mschf.com、apple.com | 复古与怀旧 | [看效果](demos/26-y2k.html) |
| 27 | **赛博朋克**<br>Cyberpunk UI | 高对比霓虹 + 纯黑 + 故障感，把反乌托邦科技做成视觉语言。<br>**特征**：#0a0a0a 底+品红·亮绿霓虹 / 发光边框与文字辉光 / 等宽字体 / 零圆角 / glitch 抖动 | cyberpunk.net、awwwards.com、mschf.com | 科技与未来 | [看效果](demos/27-cyberpunk.html) |
| 28 | **AI 原生界面**<br>AI-Native UI | 为 AI 产品长出来的视觉：蓝紫渐变、微光边框、对话优先的布局。<br>**特征**：#667eea→#764ba2 蓝紫渐变 / 卡片蓝紫描边+微光 / 亮白底 / 12px 流线圆角 / chat-first 布局 | openai.com、anthropic.com、v0.dev | 科技与未来 | [看效果](demos/28-ai-native.html) |
| 29 | **孟菲斯设计**<br>Memphis Design | 1981 年米兰的反现代主义：几何、撞色、波点，故意「不协调」。<br>**特征**：粉·青·黄三色撞色 / 彩色硬阴影交替 / 波点锯齿装饰 / 错位拼贴 / 20px 胶囊按钮 | memphis.it、dribbble.com、figma.com | 粗野与反设计 | [看效果](demos/29-memphis.html) |
| 30 | **蒸汽波**<br>Vaporwave | 80 年代合成器音乐 + 消费主义残影，粉紫霓虹里带一点虚无。<br>**特征**：粉紫霓虹 / 日英混排 / 大理石·棕榈·Windows 元素 / CRT 扫描线与色差 / 慢速循环 | poolsuite.net、mschf.com、awwwards.com | 复古与怀旧 | [看效果](demos/30-vaporwave.html) |
| 31 | **维度层叠**<br>Dimensional Layering | 用递进阴影搭出清晰的 Z 轴，让信息有「离你多远」的层次。<br>**特征**：1·2·4·8px 递进阴影 / #f0f0f5 浅灰舞台 / 大卡片悬浮 / 1px #eee 极浅描边 | linear.app、notion.so、stripe.com | 质感与视觉基调 | [看效果](demos/31-dimensional-layering.html) |
| 32 | **极度极简**<br>Exaggerated Minimalism | 把极简推到极端：字大到占满屏，其余什么都没有。<br>**特征**：5rem·900 字重·-0.05em 字距 / 纯白底 / 无阴影无装饰 / 1px 细线分割 / 无 hover | apple.com、muji.com、teenage.engineering | 排版与网格 | [看效果](demos/32-exaggerated-minimalism.html) |
| 33 | **动态排版**<br>Kinetic Typography | 让文字本身成为主角，靠大小、节奏和动画制造海报级冲击。<br>**特征**：6rem+ 超大标题 / line-height 0.9 / 黑白极端对比 / 滚动与逐字动画 / 影视海报感 | grillitype.com、resn.co.nz、awwwards.com | 排版与网格 | [看效果](demos/33-kinetic-typography.html) |
| 34 | **视差叙事**<br>Parallax Storytelling | 用滚动速度差讲故事，像翻一本有纵深的长卷。<br>**特征**：多层滚动视差 / 半透明卡片透出背景 / 纵向渐变章节 / 长滚动节奏 / 品牌故事页 | nytimes.com、apple.com、airbnb.com | 动态与交互 | [看效果](demos/34-parallax-storytelling.html) |
| 35 | **瑞士现代 2.0**<br>Swiss Modernism 2.0 | 瑞士风格的极端化版本：去掉一切，只剩字重、行高和一条细线。<br>**特征**：2px 顶部线分割 / 4rem·900 标题 / 0.85 行高 / 零阴影零圆角 / 纯白 #fcfcfc | vitsœ.com、ibm.com/design/language、muji.com | 排版与网格 | [看效果](demos/35-swiss-modernism-2.html) |
| 36 | **科幻 HUD**<br>HUD / Sci-Fi FUI | 电影里飞船控制台的界面语言：发光细线、角标框、滚动数据。<br>**特征**：#001020 深空蓝 / 青色发光边框 / 等宽数据字体 / 环形与网格刻度 / 透明按钮 | spacex.com、nasa.gov、cyberpunk.net | 科技与未来 | [看效果](demos/36-hud-sci-fi.html) |
| 37 | **便当网格 2.0**<br>Bento Grids 2.0 | 便当网格的年轻化版本：暖灰底、iPhone 红点缀、更松快的圆角。<br>**特征**：#f2f2f7 暖灰底 / 20px 大圆角 / 无边框靠底色分区 / grid span 拼接 / 彩色点缀 | apple.com、nothing.tech、arc.net | 排版与网格 | [看效果](demos/37-bento-2.html) |
| 38 | **空间计算**<br>Spatial UI / VisionOS | 为头显和空间屏设计：界面像悬在空气里的玻璃板，有厚度、有光照。<br>**特征**：blur(20px) 强模糊 / 22px 超大圆角 / 1px 微光玻璃轮廓 / 深空渐变 / 轻量景深 | apple.com/apple-vision-pro、meta.com | 科技与未来 | [看效果](demos/38-spatial-ui.html) |
| 39 | **电子墨水**<br>E-Ink & Paper | 把屏幕做成纸：暖白底、衬线字、零阴影，为长时间阅读而生。<br>**特征**：#faf8f0 纸色 / Georgia 衬线 / 1.8 行高 / 零阴影 / 1px 细线分割 / 无动效 | readwise.io/read、ia.net、amazon.com/kindle | 自然·人文·无障碍 | [看效果](demos/39-e-ink-paper.html) |
| 40 | **Z 世代混沌**<br>Gen Z Chaos / Maximalism | 精心设计的「乱七八糟」：高饱和、错位、贴纸感，反叛一切高级感。<br>**特征**：亮黄·橙红高饱和 / 黑底白字混排 / 错位拼贴 / 粗边框+彩色硬阴影 / 30px 胶囊按钮 | mschf.com、gumroad.com、duolingo.com | 粗野与反设计 | [看效果](demos/40-genz-chaos.html) |
| 41 | **仿生有机 2.0**<br>Biomimetic / Organic 2.0 | 不只借用自然的颜色，而是借用自然的生长逻辑与结构。<br>**特征**：绿灰纵向渐变 / 半透明卡片像细胞壁 / 有机不规则圆角 / 生长与流动动画 | biomimicry.org、patagonia.com、airbnb.com | 自然·人文·无障碍 | [看效果](demos/41-biomimetic.html) |
| 42 | **反精致粗糙**<br>Anti-Polish / Raw Aesthetic | 刻意不做设计：虚线框、系统字体、零圆角，像线框图直接上线。<br>**特征**：dashed 虚线边框 / 等宽或系统字体 / 零圆角零阴影 / 无 hover / 纯文本排版 | news.ycombinator.com、are.na、berkshirehathaway.com | 粗野与反设计 | [看效果](demos/42-anti-polish-raw.html) |
| 43 | **触觉数字**<br>Tactile Digital / Deformable UI | 让屏幕上的东西摸起来像纸、像布、像木头，靠厚度和形变传递温度。<br>**特征**：底部 2px 实心投影做厚度 / active scale(0.98) 形变 / 棉纸亚麻底色 / 深棕木质按钮 | teenage.engineering、muji.com、braun.com | 自然·人文·无障碍 | [看效果](demos/43-tactile-digital.html) |
| 44 | **自然精粹**<br>Nature Distilled | 不画叶子不画山，只把自然提炼成比例、色温和克制的绿。<br>**特征**：#f5f2eb 羊皮纸底 / 森林绿页眉 #5a6a4a / 0.03 极弱阴影 / 用色温而非阴影分区 | aesop.com、kinfolk.com、patagonia.com | 自然·人文·无障碍 | [看效果](demos/44-nature-distilled.html) |
| 45 | **光标交互**<br>Interactive Cursor Design | 把鼠标指针变成主角：准星、拖尾、磁吸，光标本身就是导航。<br>**特征**：自定义或十字准星光标 / 拖尾与磁吸 / 发光微辉卡片 / 深紫科技底 / 隐藏默认指针 | cuberto.com、lusion.co、aristidebenoist.com | 动态与交互 | [看效果](demos/45-interactive-cursor.html) |
| 46 | **语音优先**<br>Voice-First Multimodal | 为「说话」而设计的界面：一个入口、一圈声波，其余全部退场。<br>**特征**：#0a0a1a 极深底 / 柔和蓝紫文字 / 声波纹扩散动效 / 16px 大圆角 / 单一语音入口 | pi.ai、chatgpt.com、alexa.amazon.com | 动态与交互 | [看效果](demos/46-voice-first.html) |
| 47 | **3D 产品展示**<br>3D Product Preview | 像摄影棚一样把产品放在无影墙前，让 3D 模型成为唯一内容。<br>**特征**：浅色无影棚背景 / 产品居中悬浮+大投影 / 可旋转与配置器 / AR 预览 / 单色系统 | apple.com、nike.com、ikea.com | 科技与未来 | [看效果](demos/47-3d-product.html) |
| 48 | **渐变网格**<br>Gradient Mesh / Aurora Evolved | 极光 UI 的进化版：多层多色光斑交织，像一张会呼吸的渐变网格。<br>**特征**：多层 radial-gradient 网格叠加 / 0.04 极透玻璃卡片 / 描边随光斑变色 / 色彩反射按钮 | stripe.com、framer.com、linear.app | 质感与视觉基调 | [看效果](demos/48-gradient-mesh.html) |
| 49 | **色差 RGB 分裂**<br>Chromatic Aberration / RGB Split | 把镜头色差这个「缺陷」变成设计语言，红绿蓝错位制造数字故障感。<br>**特征**：红·绿·蓝错位描边 / text-shadow 2px 0 红、-2px 0 蓝 / 黑底等宽字体 / hover 错位跳变 | awwwards.com、cyberpunk.net、mschf.com | 粗野与反设计 | [看效果](demos/49-chromatic-aberration.html) |
| 50 | **复古胶片**<br>Vintage Analog / Retro Film | 旧照片和旧书的气质：暖黄氧化色、胶片颗粒、棕色调。<br>**特征**：#f5e8d0 暖黄纸色 / Georgia 衬线 / 胶片颗粒噪点 / #3a2a10 深棕页眉 / 古铜按钮 | aesop.com、kinfolk.com、nytimes.com | 复古与怀旧 | [看效果](demos/50-vintage-film.html) |

## 按分组查看
- **排版与网格**：瑞士·国际主义平面设计、日系编辑美学、便当盒网格、极度极简、动态排版、瑞士现代 2.0、便当网格 2.0
- **质感与视觉基调**：玻璃拟态 + 复古未来、新拟物化、OLED 暗黑、粘土风、极光界面、扁平设计、液态玻璃、柔和 UI 进化、维度层叠、渐变网格
- **复古与怀旧**：体素美学、复古 Windows 95、复古未来、Y2K 美学、蒸汽波、复古胶片
- **科技与未来**：终端·开发者工具审美、3D 超写实、零界面、赛博朋克、AI 原生界面、科幻 HUD、空间计算、3D 产品展示
- **粗野与反设计**：新粗野主义、鲜艳块状、新粗野 2.0、孟菲斯设计、Z 世代混沌、反精致粗糙、色差 RGB 分裂
- **自然·人文·无障碍**：有机自然、无障碍伦理、包容性设计、电子墨水、仿生有机 2.0、触觉数字、自然精粹
- **动态与交互**：动效驱动、微交互、视差叙事、光标交互、语音优先