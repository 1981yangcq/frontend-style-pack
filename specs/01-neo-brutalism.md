# 01 · 新粗野主义 Neo-Brutalism

> 把网页当作未经打磨的原件：粗黑边框、硬投影、零圆角，用"不修饰"表达诚实与反叛。
> 不是"随便乱来"，而是**用极端的规矩（3px 边、6px 影、全黑）去制造粗粝感**。

---

## 1. Tokens

| 角色 | 值 | 说明 |
|---|---|---|
| `--bg` | `#f2f0e6` | 纸张米色底，比纯白更"脏"一点 |
| `--surface` | `#fffdf5` | 卡片表面，仅比底色亮一档 |
| `--ink` | `#111111` | 文字与所有边框，统一用这一个黑 |
| `--muted` | `#454540` | 次要文字（不是浅灰！保持高对比） |
| `--line` | `#111111` | 分割线=黑，不弱化 |
| `--accent` | `#f6d743` | 酸黄，只做按钮/徽章，不做正文色 |
| `--on-accent` | `#111111` | 黄底上的字永远黑 |
| `--radius` | `0` | 全局零圆角，一个例外都不留 |
| `--card-border` | `3px solid #111` | 粗边，不是 1px |
| `--shadow` | `6px 6px 0 #111` | 硬投影，**模糊半径必须为 0** |
| `--btn-shadow` | `5px 5px 0 #111` | 按钮投影略小于卡片 |
| `--font-h` | `PingFang SC, Noto Sans SC, system-ui` | 标题无衬线，800 字重 |
| `--font-k` | `ui-monospace, Menlo` | 元信息/标签用等宽 |
| 标题字距 | `-0.02em` | 收紧，显敦实 |
| 标题行高 | `1.12` | 紧凑 |
| kicker 字距 | `0.18em` + `uppercase` | 拉开，与正文形成反差 |
| 间距 | `4 / 8 / 16 / 24 / 32` | 4 的倍数，不要奇数 |

背景底纹（可选但很出效果）：

```css
body{
  background-color:#f2f0e6;
  background-image:radial-gradient(rgba(17,17,17,.16) 1px, transparent 1.2px);
  background-size:16px 16px;
}
```

---

## 2. 移动语汇（必须出现的 5 件事）

1. **硬投影**：`box-shadow: Npx Npx 0 #111`，模糊值永远 0，偏移 4–8px。
2. **粗黑边**：卡片 3px，按钮 2px，分割线 2–3px，全部 `#111`。
3. **点阵/网格底纹**：16px 间距，透明度 10–18%。
4. **等宽大写标签**：`font-family: mono; text-transform: uppercase; letter-spacing: .18em; font-size: 10–11px`。
5. **编号系统**：`EXP. 01`、`01 / 02 / 03`，强化"实验档案"的未完成感。

---

## 3. 组件配方

### 按钮

```css
.btn{
  background:#f6d743; color:#111;
  border:2px solid #111; border-radius:0;
  box-shadow:5px 5px 0 #111;
  padding:12px 24px; font-weight:600;
  transition:transform .12s, box-shadow .12s;
}
.btn:hover{transform:translate(-2px,-2px); box-shadow:7px 7px 0 #111;}
.btn:active{transform:translate(3px,3px); box-shadow:2px 2px 0 #111;}
.btn:focus-visible{outline:3px solid #111; outline-offset:3px;}
.btn:disabled{opacity:.42; box-shadow:3px 3px 0 #111; pointer-events:none;}

/* 次要按钮：白底，同样是硬影 */
.btn.ghost{background:#fff; color:#111; box-shadow:4px 4px 0 #111;}
```

### 输入框

```css
.inp{
  background:#f2f0e6; color:#111;
  border:3px solid #111; border-radius:0;
  box-shadow:4px 4px 0 #111;
  padding:10px 14px;
}
.inp::placeholder{color:#454540; opacity:.75;}
.inp:focus{outline:3px solid #111; outline-offset:3px;}
.inp[aria-invalid="true"]{border-color:#c1121f; box-shadow:4px 4px 0 #c1121f;}
```

### 卡片

```css
.card{
  background:#fffdf5; border:3px solid #111; border-radius:0;
  box-shadow:6px 6px 0 #111; padding:24px;
}
.card h3{text-transform:uppercase; letter-spacing:.04em; font-weight:800;}
```

### 数据表格

```css
.tbl th{
  font-family:mono; font-size:10px; text-transform:uppercase;
  letter-spacing:.14em; border-bottom:3px solid #111; padding:8px 10px;
}
.tbl td{border-bottom:2px solid #111; padding:11px 10px;}
.tbl tr:last-child td{border-bottom:2px solid #111;}  /* 收官也留线，不要"消失" */
```

### 徽章 / 状态

```css
.badge{
  font-family:mono; font-size:10px; text-transform:uppercase; letter-spacing:.08em;
  background:#f6d743; color:#111; border:2px solid #111; border-radius:0;
  padding:2px 8px;
}
/* 次要态：白底 + 黑边，不要用浅灰 */
.badge.soft{background:#fff; color:#111;}
```

### 弹窗

```css
.modal{
  position:fixed; inset:0; background:rgba(17,17,17,.55);
  display:grid; place-items:center;
}
.modalCard{
  background:#fffdf5; border:3px solid #111; border-radius:0;
  box-shadow:8px 8px 0 #111; padding:24px; max-width:420px;
}
```

### Toast

```css
.toast{background:#111; color:#f2f0e6; border-radius:0; padding:11px 22px; font-family:mono;}
```

### 空态 / 加载态

```css
/* 空态：虚线框 + 等宽说明，不用插图 */
.empty{border:2px dashed #111; padding:26px; text-align:center; font-family:mono; font-size:12px;}
/* 加载：三根实心条直接闪，不要渐变 shimmer */
.skel i{display:block; height:10px; background:#111; opacity:.18; animation:blink 1s steps(2) infinite;}
```

---

## 4. 反模式（出现任何一条即判定失败）

- ❌ 任何 `border-radius` > 0
- ❌ 任何带模糊半径的阴影（`blur > 0`）
- ❌ 渐变（`linear-gradient` / `radial-gradient` 用作装饰背景，点阵除外）
- ❌ 半透明卡片、毛玻璃
- ❌ 浅灰文字（`#999` 这类）
- ❌ 衬线字体
- ❌ 超过 200ms 的缓动过渡、弹簧动画
- ❌ 圆角图标；图标一律方正或用像素图形
- ❌ "柔和阴影 + 微圆角"的 SaaS 味道——这是死敌

---

## 5. 无障碍兜底

| 项 | 要求 |
|---|---|
| 黑字黄底 | `#111` on `#f6d743` ≈ 14.9:1 ✅ |
| 正文对比 | `#111` on `#f2f0e6` ≈ 15.8:1 ✅ |
| 次要文字 | 不要低于 `#454540`（≈ 7.8:1） |
| focus | 3px 实线 + offset 3px，**不允许 outline:none** |
| 触摸目标 | 按钮最小高 44px，间距 ≥ 8px |
| 状态 | 不能只靠黄色区分，必须带文字标签 |

---

## 6. 影像处理

```css
.ph{filter:grayscale(1) contrast(1.18);}
.ph::after{background:#f6d743; mix-blend-mode:color; opacity:.12;} /* 轻微酸黄双色调 */
```

照片要"硬"：高对比黑白为主，黄调只做极轻的染色，不要做成复古胶片。

---

## 7. 参考站点

- `gumroad.com` —— 硬边卡片 + 高饱和色块的标准样板
- `theverge.com` —— 粗线条版式、大字重标题
- `balenciaga.com` —— 极简到粗暴的排版，黑白为主

---

## 8. 验收清单

- [ ] 全局抽查 5 个元素，`border-radius` 全为 0
- [ ] 抽查 3 个阴影，模糊值全为 0
- [ ] 主色只出现在按钮/徽章/强调条上，正文里没有黄色字
- [ ] 有至少一处等宽大写小标签
- [ ] 表格 10 行不塌，末行仍有分割线
- [ ] 按钮 hover 有位移 + 阴影加深，不是变色
- [ ] focus 环可见且是黑色实线
- [ ] 空态、错误态、加载态都不是"暂无数据"四个字
