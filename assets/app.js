/* 前端设计风格大全 · 首页交互 */
(function () {
  var vgrid = document.getElementById('vgrid');
  var vcs = [].slice.call(vgrid.querySelectorAll('.vcell'));
  var rows = [].slice.call(document.querySelectorAll('#tb tr'));
  var tableBox = document.getElementById('tableBox');
  var q = document.getElementById('q');
  var cnt = document.getElementById('count');
  var chips = [].slice.call(document.querySelectorAll('.chip'));
  var vbtns = [].slice.call(document.querySelectorAll('.vbtn'));
  var segs = [].slice.call(document.querySelectorAll('.seg[data-f]'));
  var lucky = document.getElementById('lucky');
  var TOTAL = vcs.length;

  var state = { g: 'all', kw: '', view: 'grid', tone: 'all', edge: 'all', density: 'all' };

  function kOf(e) { return e.dataset.k || ''; }

  function match(e) {
    if (state.g !== 'all' && e.dataset.g !== state.g) return false;
    if (state.tone !== 'all' && e.dataset.tone !== state.tone) return false;
    if (state.edge !== 'all' && e.dataset.edge !== state.edge) return false;
    if (state.density !== 'all' && e.dataset.density !== state.density) return false;
    if (state.kw && !kOf(e).includes(state.kw)) return false;
    return true;
  }

  function render() {
    var n = 0;
    vcs.forEach(function (e) {
      var ok = match(e);
      e.classList.toggle('hide', !ok);
      if (ok) n++;
    });
    rows.forEach(function (r) {
      var ok = match(r);
      r.classList.toggle('hide', !ok);
    });
    var d = (window.AtlasI18n && window.AtlasI18n.dict) || {};
    cnt.textContent = (d['home.count'] || '显示 {n} / {total}')
      .replace('{n}', n).replace('{total}', TOTAL);
    vgrid.classList.toggle('hide', state.view !== 'grid');
    tableBox.classList.toggle('hide', state.view !== 'table');
  }

  chips.forEach(function (c) {
    c.onclick = function () {
      chips.forEach(function (x) { x.classList.remove('on'); });
      c.classList.add('on');
      state.g = c.dataset.g;
      render();
    };
  });

  vbtns.forEach(function (b) {
    b.onclick = function () {
      vbtns.forEach(function (x) { x.classList.remove('on'); });
      b.classList.add('on');
      state.view = b.dataset.v;
      render();
    };
  });

  segs.forEach(function (seg) {
    var field = seg.dataset.f;
    [].slice.call(seg.querySelectorAll('.sg')).forEach(function (b) {
      b.onclick = function () {
        [].slice.call(seg.querySelectorAll('.sg')).forEach(function (x) { x.classList.remove('on'); });
        b.classList.add('on');
        state[field] = b.dataset.v;
        render();
      };
    });
  });

  if (q) {
    q.oninput = function () {
      state.kw = q.value.trim().toLowerCase();
      render();
    };
  }

  if (lucky) {
    lucky.onclick = function () {
      var pool = vcs.filter(function (e) { return !e.classList.contains('hide'); });
      if (!pool.length) return;
      var pick = pool[Math.floor(Math.random() * pool.length)];
      var a = pick.querySelector('.vcard');
      if (a) window.location.href = a.getAttribute('href');
    };
  }

  /* 复制 tokens */
  var toast = document.createElement('div');
  toast.className = 'toast';
  toast.textContent = '已复制，粘给 AI 即可';
  document.body.appendChild(toast);
  var tt;
  function showToast(msg) {
    toast.textContent = msg;
    toast.classList.add('show');
    clearTimeout(tt);
    tt = setTimeout(function () { toast.classList.remove('show'); }, 1800);
  }

  function copyText(text) {
    if (navigator.clipboard && navigator.clipboard.writeText) {
      return navigator.clipboard.writeText(text);
    }
    return new Promise(function (resolve, reject) {
      var ta = document.createElement('textarea');
      ta.value = text;
      ta.style.position = 'fixed';
      ta.style.opacity = '0';
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); resolve(); } catch (e) { reject(e); }
      document.body.removeChild(ta);
    });
  }

  vcs.forEach(function (cell) {
    var btn = cell.querySelector('.vcopy');
    if (!btn) return;
    function fire(e) {
      e.preventDefault();
      e.stopPropagation();
      var tpl = cell.querySelector('.ptpl');
      var txt = tpl ? tpl.content.textContent : (cell.dataset.css || '');
      copyText(txt).then(function () {
        showToast('已复制，粘给 AI 即可');
      }, function () {
        showToast('复制失败，请手动选中');
      });
    }
    btn.addEventListener('click', fire);
    btn.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' || e.key === ' ') fire(e);
    });
  });

  document.addEventListener('i18n:dict', function () { render(); });
  render();
})();
