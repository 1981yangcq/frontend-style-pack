# 贡献一个风格

## 三步

### 1. 加一行数据

`styles.json` 末尾追加：

```json
{
  "id": 51,
  "cn": "你的风格名",
  "en": "Your Style",
  "group": "G1",
  "groupName": "排版与网格",
  "desc": "一句话说明它长什么样、给人什么感觉。",
  "feat": "手法1 / 手法2 / 手法3 / 手法4",
  "sites": ["example.com"]
}
```

分组用现有的 7 组之一：`G1` 排版与网格 · `G2` 质感与视觉基调 · `G3` 复古与怀旧 ·
`G4` 科技与未来 · `G5` 粗野与反设计 · `G6` 自然·人文·无障碍 · `G7` 动态与交互。

### 2. 加一套 tokens

`themes.py` 末尾追加一个 `T(...)`，至少给出：

```python
51: T(bg="#fafafa", surface="#fff", ink="#111", muted="#6b6b6b", line="#e5e5e5",
      accent="#2563eb", on_accent="#fff", radius="12px",
      cardborder="1px solid #e5e5e5", shadow="0 1px 2px rgba(0,0,0,.05)",
      btnborder="none", btnshadow="none", btnradius="10px",
      fonth=SANS, lhh="1.1", lsh="-.02em", h1w="700"),
```

### 3. 生成

```bash
pip install pillow
python build_demos.py     # 能生成 demos/51-xxx.html 就合格
python build_thumbs.py
python build_zips.py
python build.py
python build_readme.py
```

## 评审标准

- [ ] 有一眼可辨的**特征手法**，不是「换了个蓝色的 Bootstrap」
- [ ] 与现有 52 个风格**不重复**（`build.py` 的「感觉」筛选里，明暗/软硬/繁简组合要能区分）
- [ ] 对比度：正文 ≥ 4.5:1，focus 可见
- [ ] `demo.html` 里组件不塌、不溢出

## 提交

PR 标题：`feat: 新增风格「XXX」`
请附一张 `preview.jpg` 的截图。
