/* 运行时 i18n：一套页面，9 种语言。语言包在 /i18n/<lang>.json */
(function () {
  var LANGS = [
    ['zh-CN', '简体中文'], ['en', 'English'], ['ja', '日本語'], ['ko', '한국어'],
    ['es', 'Español'], ['pt-BR', 'Português (BR)'], ['fr', 'Français'],
    ['de', 'Deutsch'], ['ru', 'Русский']
  ];
  var SUPPORTED = LANGS.map(function (l) { return l[0]; });

  function detect() {
    var q = new URLSearchParams(location.search).get('lang');
    if (q && SUPPORTED.indexOf(q) > -1) return q;
    var saved = localStorage.getItem('atlas-lang');
    if (saved && SUPPORTED.indexOf(saved) > -1) return saved;
    var nav = (navigator.language || 'zh-CN');
    if (SUPPORTED.indexOf(nav) > -1) return nav;
    var short = nav.split('-')[0];
    for (var i = 0; i < SUPPORTED.length; i++) {
      if (SUPPORTED[i].split('-')[0] === short) return SUPPORTED[i];
    }
    return 'zh-CN';
  }

  var lang = detect();

  function buildSwitcher() {
    var host = document.getElementById('langSwitch');
    if (!host) return;
    var sel = document.createElement('select');
    sel.className = 'langSel';
    sel.setAttribute('aria-label', 'Language');
    LANGS.forEach(function (p) {
      var o = document.createElement('option');
      o.value = p[0];
      o.textContent = p[1];
      if (p[0] === lang) o.selected = true;
      sel.appendChild(o);
    });
    sel.onchange = function () {
      localStorage.setItem('atlas-lang', sel.value);
      var u = new URL(location.href);
      u.searchParams.set('lang', sel.value);
      location.href = u.toString();
    };
    host.appendChild(sel);
  }


  /* 文本节点按词表替换：不为每个标签加属性，词表本身就是翻译文件 */
  function translateRoot(root, map) {
    if (!map) return 0;
    var walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null);
    root.querySelectorAll && root.querySelectorAll('[placeholder]').forEach(function (el) {
      var v = map[el.placeholder];
      if (v) el.placeholder = v;
    });
    var nodes = [], n, hit = 0;
    while ((n = walker.nextNode())) nodes.push(n);
    nodes.forEach(function (node) {
      var raw = node.nodeValue;
      var key = (raw || '').trim();
      if (!key || key.length > 220) return;
      var to = map[key];
      if (to != null && to !== key) {
        var lead = raw.match(/^\s*/)[0];
        var trail = raw.match(/\s*$/)[0];
        node.nodeValue = lead + to + trail;
        hit++;
      }
    });
    return hit;
  }

  function apply(dict) {
    document.documentElement.lang = lang;
    window.AtlasI18n = window.AtlasI18n || {};
    window.AtlasI18n.dict = dict;
    document.dispatchEvent(new CustomEvent('i18n:dict'));

    document.querySelectorAll('[data-i18n]').forEach(function (el) {
      var k = el.getAttribute('data-i18n');
      if (dict[k] != null) el.textContent = dict[k];
    });
    document.querySelectorAll('[data-i18n-ph]').forEach(function (el) {
      var k = el.getAttribute('data-i18n-ph');
      if (dict[k] != null) el.placeholder = dict[k];
    });

    document.querySelectorAll('[data-group]').forEach(function (el) {
      var g = el.getAttribute('data-group');
      if (dict['groups.' + g]) {
        var em = el.querySelector('em');
        var n = em ? em.outerHTML : '';
        el.innerHTML = dict['groups.' + g] + ' ' + n;
      }
    });

    var pt = dict['prompt.template'] || '';
    translateRoot(document.body, dict.text);
    if (dict.text) {
      document.querySelectorAll('[placeholder]').forEach(function (el) {
        var v = dict.text[el.placeholder];
        if (v) el.placeholder = v;
      });
    }

    document.querySelectorAll('.vcell[data-sid]').forEach(function (cell) {
      var sid = cell.getAttribute('data-sid');
      var entry = dict.styles && dict.styles[sid];
      if (!entry) return;
      var nm = cell.querySelector('[data-field="name"]');
      var ds = cell.querySelector('[data-field="desc"]');
      if (nm) nm.textContent = entry.name;
      if (ds) ds.textContent = entry.desc;

      var tok = (cell.getAttribute('data-tok') || '').split('|');
      var tpl = cell.querySelector('template.ptpl');
      if (tpl && pt && tok.length >= 8) {
        tpl.innerHTML = pt
          .replace('{name}', entry.name)
          .replace('{desc}', entry.desc)
          .replace('{feat}', entry.feat)
          .replace('{bg}', tok[0]).replace('{surface}', tok[1])
          .replace('{ink}', tok[2]).replace('{accent}', tok[3])
          .replace('{radius}', tok[4]).replace('{border}', tok[5])
          .replace('{shadow}', tok[6]).replace('{anti}', tok[7]);
      }
    });

    if (dict['site.title']) {
      document.title = (document.body.getAttribute('data-page') === 'demo')
        ? document.title
        : dict['site.title'] + ' · ' + (dict['site.sub'] || '');
    }
    document.dispatchEvent(new CustomEvent('i18n:applied', { detail: { lang: lang, dict: dict } }));
  }

  function init() {
    buildSwitcher();
    if (lang === 'zh-CN') { document.documentElement.lang = 'zh-CN'; apply({}); return; }
    var base = location.pathname.indexOf('/demos/') > -1 ? '../' : '';
    fetch(base + 'i18n/' + lang + '.json')
      .then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) { if (d) apply(d); })
      .catch(function () { /* file:// 或离线时保持原文 */ });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
  window.AtlasI18n = {
    lang: lang,
    apply: apply,
    dict: null,
    translateRoot: function (root) { translateRoot(root, window.AtlasI18n.dict && window.AtlasI18n.dict.text); },
    translateShadow: function (root) { translateRoot(root, window.AtlasI18n.dict && window.AtlasI18n.dict.text); }
  };
})();
