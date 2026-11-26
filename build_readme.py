# -*- coding: utf-8 -*-
"""生成 README.md（简体中文，默认）与 docs/i18n/README.<lang>.md（其余 9 种语言）。

文案在 i18n/readme.json；风格表直接复用 i18n/<lang>.json 里已有的名称与描述，
所以新增语言时只需要填 readme.json 里的 ~40 条文案，50 行表格自动出。
"""
import io, json, os

OWNER = "1981yangcq"
REPO = "frontend-style-pack"
BASE = f"https://{OWNER}.github.io/{REPO}/"
REL = f"https://github.com/{OWNER}/{REPO}/releases/latest/download/"
BLOB = f"https://github.com/{OWNER}/{REPO}/blob/main/"

OUT = os.path.dirname(os.path.abspath(__file__))
STYLES = json.load(open(os.path.join(OUT, "styles.json"), encoding="utf-8"))
from themes import SLUGS

PROSE = json.load(open(os.path.join(OUT, "i18n", "readme.json"), encoding="utf-8"))

LANGS = [
    ("zh-CN", "简体中文", "README.md"),
    ("zh-TW", "繁體中文", "docs/i18n/README.zh-TW.md"),
    ("en",    "English", "docs/i18n/README.en.md"),
    ("es",    "Español", "docs/i18n/README.es.md"),
    ("fr",    "Français", "docs/i18n/README.fr.md"),
    ("pt-BR", "Português (BR)", "docs/i18n/README.pt-BR.md"),
    ("ru",    "Русский", "docs/i18n/README.ru.md"),
    ("de",    "Deutsch", "docs/i18n/README.de.md"),
    ("ja",    "日本語", "docs/i18n/README.ja.md"),
    ("ko",    "한국어", "docs/i18n/README.ko.md"),
]

FEATURED = ["01", "03", "27", "08", "05", "47"]


def pack(lang):
    return json.load(open(os.path.join(OUT, "i18n", lang + ".json"), encoding="utf-8"))


def langbar(current, label):
    cells = []
    for code, name, path in LANGS:
        if code == current:
            cells.append("**" + name + "**")
        else:
            cells.append("[" + name + "](" + BLOB + path + ")")
    return " · ".join(cells)


def featured_grid(prefix="", names=None, q="", lang="zh-CN"):
    rows = []
    for i in range(0, len(FEATURED), 3):
        cells = []
        for sid in FEATURED[i:i + 3]:
            st = [s for s in STYLES if f"{s['id']:02d}" == sid][0]
            url = BASE + "demos/" + SLUGS[st["id"]] + ".html" + q
            tdir = "assets/thumbs/" if lang == "zh-CN" else "assets/thumbs/" + lang + "/"
            cells.append(
                '<a href="%s"><img src="%s%s%s.jpg" width="100%%" alt="%s"></a>'
                % (url, prefix, tdir, sid, (names or {}).get(sid, st["cn"])))
        rows.append("| " + " | ".join(cells) + " |")
    return "\n".join(rows)


def style_rows(lang, p, q=""):
    pk = pack(lang)
    out = []
    for s in STYLES:
        sid = f"{s['id']:02d}"
        e = pk["styles"][sid]
        out.append(
            "| %s | **%s**<br><sub>%s</sub> | %s | [%s](%sdemos/%s.html) · [%s](%sstyle-%s.zip) |"
            % (sid, e["name"], e["en"], e["desc"], p["preview"], BASE + q, SLUGS[s["id"]],
               p["download"], REL, SLUGS[s["id"]]))
    return "\n".join(out)


def build(lang, prefix=""):
    p = PROSE.get(lang) or PROSE['zh-CN']
    q = "" if lang == "zh-CN" else ("?lang=" + lang)
    pk = pack(lang)
    L = []
    A = L.append
    A('<div align="center">')
    A('')
    A('# ' + p["title"])
    A('')
    A('**' + p["tagline"] + '**')
    A('')
    A(p["intro"])
    A('')
    A('<img src="%sdocs/hero/hero-%s.jpg" width="100%%" alt="%s">' % (prefix, lang, p["title"]))
    A('')
    A('[**🌐 %s**](%s) · [**🇨🇳 %s**](https://sunsong.surge.sh%s) · [**⬇ %s**](https://github.com/%s/%s/releases/) · [**📖 %s**](%sspecs/README.md)'
      % (p["link_preview"], BASE + q, p["mirror"], q, p["packs"], OWNER, REPO, p["ai_use"], prefix))
    A('')
    A('</div>')
    A('')
    A("**" + p["language"] + "**" + p.get("colon", "：") + langbar(lang, p["language"]))
    A('')
    A('---')
    A('')
    A('## ' + p["hit_h"])
    A('')
    A('> ' + p["hit_hint"])
    A('')
    A('| | | |')
    A('|---|---|---|')
    A(featured_grid(prefix, {k: v["name"] for k, v in pk["styles"].items()}, q, lang))
    A('')
    A('---')
    A('')
    A('## ' + p["what_h"])
    A('')
    A(p["what_p"])
    A('')
    A('| ' + p["who_h1"] + ' | ' + p["who_h2"] + ' |')
    A('|---|---|')
    for a, b in p["who_rows"]:
        A('| **' + a + '** | ' + b + ' |')
    A('')
    A('> ' + p["note"])
    A('')
    A('---')
    A('')
    A('## ' + p["steps_h"])
    A('')
    for i, s in enumerate(p["steps"], 1):
        A('%d. %s' % (i, s))
    A('')
    A('---')
    A('')
    A('## ' + p["styles_h"])
    A('')
    A('> ' + p["styles_hint"])
    A('')
    A('| # | ' + p["style"] + ' | ' + p["one_line"] + ' | ' + p["links"] + ' |')
    A('|---|---|---|---|')
    A(style_rows(lang, p, q))
    A('')
    A('---')
    A('')
    A('## ' + p["pack_h"])
    A('')
    A('| ' + p["file"] + ' | ' + p["desc"] + ' |')
    A('|---|---|')
    for f, d in p["pack_rows"]:
        A('| `' + f + '` | ' + d + ' |')
    A('')
    A('---')
    A('')
    A('## ' + p["ai_h"])
    A('')
    A(p["ai_p"])
    A('')
    A('```')
    A(p["ai_example"])
    A('```')
    A('')
    A('---')
    A('')
    A('## ' + p["run_h"])
    A('')
    A(p["run_p"])
    A('')
    A('```bash')
    A('pip install pillow')
    A('python build_demos.py      # 50 页')
    A('python build_thumbs.py')
    A('python build_zips.py')
    A('python build.py            # 首页')
    A('```')
    A('')
    A('---')
    A('')
    A('## ' + p["contrib_h"])
    A('')
    A(p["contrib_p"])
    A('')
    A('---')
    A('')
    A('## ' + p["license_h"])
    A('')
    for line in p["license_lines"]:
        A('- ' + line)
    A('')
    return "\n".join(L)


def main():
    n = 0
    for code, name, path in LANGS:
        text = build(code, "" if code == "zh-CN" else "../../")
        full = os.path.join(OUT, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        io.open(full, "w", encoding="utf-8").write(text)
        n += 1
        print("README", code, len(text) // 1024, "KB →", path)
    print("done", n)


if __name__ == "__main__":
    main()
