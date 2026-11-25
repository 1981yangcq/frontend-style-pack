# -*- coding: utf-8 -*-
"""左侧缩略图导航的单一来源。

直接复用 build_demos.py 里已经验证过的 CSS / HTML / JS 片段，
避免两份实现漂移；组件总览页通过 suffix 复用同一套导航。
"""
import io, os, re

HERE = os.path.dirname(os.path.abspath(__file__))
_SRC = io.open(os.path.join(HERE, "build_demos.py"), encoding="utf-8").read()

RAIL_CSS = re.search(r"/\* RAIL-CSS-START.*?/\* RAIL-CSS-END \*/", _SRC, re.S).group(0)

_HEAD = re.search(
    r'<div class="rail" id="rail">.*?<div class="railList" id="railList"></div>',
    _SRC, re.S).group(0)

_JS = re.search(r'<script>\s*\(function\(\)\{\s*var EMBED.*?\}\)\(\);\s*</script>',
                _SRC, re.S).group(0)


def rail_html(footer):
    """footer: 底部若干 <a class="railFoot"> 片段"""
    return _HEAD + "\n  " + footer + "\n</div>\n"


def rail_js(raildata, slug, suffix=""):
    js = _JS.replace("$raildata", raildata).replace('"$slug"', '"%s"' % slug)
    if suffix:
        js = js.replace("a.href=d[2]+'.html'", "a.href=d[2]+'%s.html'" % suffix)
    return js
