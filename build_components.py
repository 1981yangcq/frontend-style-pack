# -*- coding: utf-8 -*-
"""为每种风格生成一页「组件总览」：建站常见组件 40+，全部由同一套 tokens 驱动。"""
import ast, io, json, os, re
from string import Template

from themes import THEMES, SLUGS
import rail

OUT = os.path.dirname(os.path.abspath(__file__))
STYLES = json.load(open(os.path.join(OUT, "styles.json"), encoding="utf-8"))

_src = io.open(os.path.join(OUT, "build_demos.py"), encoding="utf-8").read()
_m = re.search(r"XRAW = \{(.*?)\n\}", _src, re.S)
XRAW = ast.literal_eval("{" + _m.group(1) + "}") if _m else {}


def sec(n, title, en, body):
    return (f'<section class="sec" id="s{n}"><header class="secHead"><h2>{title}</h2>'
            f'<span>{en}</span></header>{body}</section>')


def spec(label, body, wide=False):
    cls = "spec panel wide" if wide else "spec panel"
    return f'<div class="{cls}"><span class="lab">{label}</span>{body}</div>'


S1 = sec(1, "按钮与操作", "BUTTONS / ACTIONS", '<div class="specs">'
    + spec("主要 / 次要 / 文字", """
<div class="row">
  <button class="btn">主要操作</button>
  <button class="btn ghost">次要</button>
  <button class="btn link">文字按钮 →</button>
</div>""")
    + spec("禁用 / 加载中", """
<div class="row">
  <button class="btn" disabled>禁用</button>
  <button class="btn" data-loading="1"><span class="spin"></span>处理中</button>
</div>""")
    + spec("危险操作", """
<div class="row">
  <button class="btn danger">删除项目</button>
  <button class="btn ghost danger-g">取消订阅</button>
</div>""")
    + spec("图标按钮 / 按钮组", """
<div class="row">
  <button class="btn icon" title="收藏">★</button>
  <div class="btngroup">
    <button class="btn ghost">日</button>
    <button class="btn ghost on">周</button>
    <button class="btn ghost">月</button>
  </div>
</div>""")
    + '</div>')

S2 = sec(2, "表单控件", "FORMS / INPUTS", '<div class="specs">'
    + spec("文本 / 搜索", """
<label class="fl">项目名称</label>
<input class="inp" placeholder="例如：arc-studio">
<label class="fl">搜索</label>
<div class="inp-ico"><span>⌕</span><input class="inp" placeholder="搜索组件…"></div>""")
    + spec("下拉 / 日期", """
<label class="fl">状态</label>
<select class="inp"><option>进行中</option><option>已完成</option><option>待开始</option></select>
<label class="fl">上线日期</label>
<input class="inp" type="date" value="2026-11-25">""")
    + spec("多行文本 / 字数", """
<label class="fl">备注</label>
<textarea class="inp" rows="3" placeholder="写点什么…"></textarea>
<span class="help right">0 / 200</span>""")
    + spec("勾选 / 单选", """
<label class="chk"><input type="checkbox" checked><span>启用网格对齐</span></label>
<label class="chk"><input type="checkbox"><span>显示隐藏文件</span></label>
<label class="chk"><input type="radio" name="r" checked><span>按月计费</span></label>
<label class="chk"><input type="radio" name="r"><span>按年计费（省 20%）</span></label>""")
    + spec("开关 / 滑块", """
<div class="row"><span class="sw on"><i></i></span><span class="tiny muted">自动同步</span></div>
<div class="row" style="margin-top:14px"><span class="sw"><i></i></span><span class="tiny muted">构建通知</span></div>
<input class="range" type="range" value="64">""")
    + spec("上传", """
<label class="drop"><b>拖拽文件到这里</b><span>或点击选择 · PNG / JPG ≤ 5MB</span>
<input type="file" hidden></label>
<div class="row" style="margin-top:10px"><span class="fileChip">logo.png<span>×</span></span></div>""")
    + spec("校验态", """
<label class="fl">邮箱</label>
<input class="inp invalid" value="team@arc">
<span class="err-msg">⚠ 邮箱格式不正确</span>
<label class="fl">密码</label>
<input class="inp valid" value="••••••••">
<span class="ok-msg">✓ 强度足够</span>""")
    + spec("分段控件", """
<div class="seg full"><button class="sg on">概览</button><button class="sg">数据</button>
<button class="sg">设置</button></div>""")
    + '</div>')

S3 = sec(3, "导航与结构", "NAVIGATION", '<div class="specs">'
    + spec("面包屑", """
<nav class="crumb"><a href="#">首页</a><span>/</span><a href="#">设计系统</a><span>/</span><b>组件</b></nav>""")
    + spec("标签页", """
<div class="tabs" data-tabs>
  <button class="tab on">全部</button><button class="tab">进行中</button>
  <button class="tab">已完成</button><button class="tab">归档</button>
</div>""")
    + spec("步骤条", """
<ol class="steps"><li class="done"><b>✓</b><span>需求</span></li>
<li class="on"><b>2</b><span>设计</span></li><li><b>3</b><span>上线</span></li></ol>""")
    + spec("分页", """
<div class="pager"><button class="pg">‹</button><button class="pg on">1</button>
<button class="pg">2</button><button class="pg">3</button><button class="pg">…</button>
<button class="pg">12</button><button class="pg">›</button></div>""")
    + spec("侧边导航", """
<nav class="side">
  <a class="on">概览</a><a>组件</a><a>模式</a><a>资源</a><a>设置</a>
</nav>""")
    + spec("顶部导航（紧凑）", """
<div class="miniNav"><b>ARC</b><span>产品</span><span>方案</span><span class="on">文档</span></div>""")
    + '</div>')

S4 = sec(4, "数据展示", "DATA / DISPLAY", '<div class="specs">'
    + spec("数据表格（工具栏 + 排序 + 行操作）", """
<div class="tblBar">
  <input class="inp sm" placeholder="筛选项目…">
  <div class="row"><button class="btn ghost sm">导出</button><button class="btn sm">新建</button></div>
</div>
<table class="tbl">
  <thead><tr><th>项目</th><th>负责人</th><th class="r sort">进度 ▾</th><th>状态</th><th></th></tr></thead>
  <tbody>
    <tr><td>官网改版</td><td><span class="av">李</span></td><td class="r">82%</td><td><span class="badge">进行中</span></td><td class="r"><button class="rowAct">⋯</button></td></tr>
    <tr><td>组件库</td><td><span class="av">王</span></td><td class="r">100%</td><td><span class="badge soft">已完成</span></td><td class="r"><button class="rowAct">⋯</button></td></tr>
    <tr><td>数据看板</td><td><span class="av">陈</span></td><td class="r">46%</td><td><span class="badge">进行中</span></td><td class="r"><button class="rowAct">⋯</button></td></tr>
  </tbody>
</table>""", wide=True)
    + spec("指标卡", """
<div class="stats">
  <div class="stat"><span>本月构建</span><b>12,480</b><em>+18%</em></div>
  <div class="stat"><span>平均耗时</span><b>1.28s</b><em class="down">−8%</em></div>
  <div class="stat"><span>可用性</span><b>99.98</b><em>稳定</em></div>
</div>""", wide=True)
    + spec("徽章 / 标签", """
<div class="row"><span class="badge">New</span><span class="badge soft">草稿</span>
<span class="badge ok">已完成</span><span class="badge warn">待审</span></div>""")
    + spec("头像组", """
<div class="avGroup"><span class="av">李</span><span class="av">王</span><span class="av">陈</span>
<span class="av avMore">+4</span></div>""")
    + spec("进度条", """
<div class="prog"><i style="width:64%"></i></div>
<span class="help">64% · 剩余 3 天</span>
<div class="prog thin"><i style="width:32%"></i></div>""")
    + spec("时间线", """
<ol class="tl"><li class="done"><b></b><span>提交需求<em>11-20</em></span></li>
<li class="done"><b></b><span>完成设计<em>11-22</em></span></li>
<li><b></b><span>等待上线<em>—</em></span></li></ol>""")
    + spec("评分", """
<div class="rate"><i>★</i><i>★</i><i>★</i><i>★</i><i class="off">★</i><span class="tiny muted">4.0</span></div>""")
    + '</div>')

S5 = sec(5, "反馈与状态", "FEEDBACK / STATES", '<div class="specs">'
    + spec("提示条", """
<div class="alert info"><b>提示</b>本周有 2 次构建失败。</div>
<div class="alert ok"><b>成功</b>配置已保存。</div>
<div class="alert err"><b>失败</b>网络超时，请重试。</div>""")
    + spec("空状态", """
<div class="empty"><i></i><b>还没有项目</b><span>创建第一个项目后会显示在这里</span>
<button class="btn sm">新建项目</button></div>""")
    + spec("骨架屏", """
<div class="skel"><i style="width:64%"></i><i style="width:100%"></i><i style="width:82%"></i><i style="width:45%"></i></div>""")
    + spec("加载", """
<div class="row"><span class="spin big"></span><span class="tiny muted">正在加载…</span></div>""")
    + spec("提示气泡", """
<div class="tipWrap"><button class="btn ghost sm">悬停看提示</button>
<span class="tip">这是一条提示信息</span></div>""")
    + spec("轻提示 Toast", """
<div class="row"><button class="btn sm" data-toast>显示 Toast</button></div>
<div class="toast" id="toast">已保存到「我的项目」</div>""")
    + spec("弹窗 / 抽屉", """
<div class="row"><button class="btn sm" data-modal>打开弹窗</button>
<button class="btn ghost sm" data-drawer>打开抽屉</button></div>""")
    + '</div>')

S6 = sec(6, "内容区块", "CONTENT BLOCKS", '<div class="specs">'
    + spec("特性网格", """
<div class="feat"><b>快</b><p>组件即拿即用，半天搭完一页。</p></div>
<div class="feat"><b>稳</b><p>一套 token 管住全站样式。</p></div>
<div class="feat"><b>省</b><p>改一处，50 个页面同步。</p></div>""", wide=True)
    + spec("价格卡", """
<div class="price"><span>Pro</span><b>¥128<em>/月</em></b>
<ul><li>无限项目</li><li>50 套主题</li><li>优先支持</li></ul>
<button class="btn">开始试用</button></div>""")
    + spec("证言", """
<blockquote class="quote">「上线周期从两周压到两天，风格还没跑偏。」
<footer><span class="av">周</span><b>周工</b><em>某 SaaS 前端负责人</em></footer></blockquote>""", wide=True)
    + spec("FAQ 手风琴", """
<details class="faq" open><summary>能改颜色吗？</summary><p>能。改 tokens 里的 --accent 即可全站生效。</p></details>
<details class="faq"><summary>支持暗色模式吗？</summary><p>复制一份 tokens，覆盖变量即可。</p></details>""", wide=True)
    + spec("客户 Logo 墙", """
<div class="logos"><span>ACME</span><span>NORTH</span><span>KITE</span><span>ORBIT</span><span>PLAIN</span></div>""", wide=True)
    + spec("行动号召", """
<div class="ctaBand"><b>现在就把风格包带走</b><span>一次投喂，覆盖 40+ 组件。</span>
<button class="btn">导出风格包</button></div>""", wide=True)
    + '</div>')


S7 = sec(7, "高级与业务组件", "ADVANCED / BUSINESS", '<div class="specs">'
    + spec("下拉菜单 / 操作菜单", """
<div class="menuWrap">
  <button class="btn ghost sm">更多操作 ▾</button>
  <div class="menu">
    <a class="mi">重命名</a><a class="mi">复制链接</a>
    <div class="miSep"></div>
    <a class="mi danger">删除项目</a>
  </div>
</div>""")
    + spec("多选 / 标签输入", """
<div class="combo">
  <span class="ctag">设计<span>×</span></span><span class="ctag">前端<span>×</span></span>
  <input class="cin" placeholder="添加标签…">
</div>
<div class="comboList">
  <a class="ci on">设计</a><a class="ci">前端</a><a class="ci">后端</a>
</div>""")
    + spec("日历", """
<div class="cal">
  <div class="calTop"><b>2026 年 11 月</b><span class="calNav">‹ ›</span></div>
  <div class="calHead"><span>一</span><span>二</span><span>三</span><span>四</span><span>五</span><span>六</span><span>日</span></div>
  <div class="calGrid">
    <i class="mut">26</i><i class="mut">27</i><i class="mut">28</i><i class="mut">29</i><i class="mut">30</i><i>1</i><i>2</i>
    <i>3</i><i>4</i><i>5</i><i>6</i><i>7</i><i>8</i><i>9</i>
    <i>10</i><i>11</i><i>12</i><i>13</i><i>14</i><i>15</i><i>16</i>
    <i>17</i><i>18</i><i>19</i><i>20</i><i>21</i><i>22</i><i>23</i>
    <i>24</i><i class="on">25</i><i>26</i><i>27</i><i>28</i><i>29</i><i>30</i>
  </div>
</div>""")
    + spec("树形导航", """
<ul class="tree">
  <li class="open"><b>设计系统</b>
    <ul><li class="on">颜色</li><li>排版</li><li class="open"><b>组件</b>
      <ul><li>按钮</li><li>表单</li></ul></li></ul>
  </li>
  <li><b>资源</b></li>
</ul>""")
    + spec("命令面板 ⌘K", """
<div class="cmd">
  <div class="cmdIn"><span>⌕</span><input placeholder="搜索命令…"><kbd>esc</kbd></div>
  <div class="cmdList">
    <a class="cmdItem on"><span>新建项目</span><kbd>⌘N</kbd></a>
    <a class="cmdItem"><span>导入风格包</span><kbd>⌘I</kbd></a>
    <a class="cmdItem"><span>切换深色模式</span><kbd>⌘D</kbd></a>
  </div>
</div>""")
    + spec("图表：柱 / 线 / 环", """
<div class="chartRow">
  <div class="chartBars"><i style="height:40%"></i><i style="height:72%"></i><i style="height:55%"></i>
    <i style="height:88%"></i><i style="height:64%"></i></div>
  <svg class="chartLine" viewBox="0 0 100 60" preserveAspectRatio="none">
    <polyline points="0,48 20,32 40,40 60,18 80,26 100,10" fill="none" stroke="currentColor" stroke-width="2"/>
  </svg>
  <div class="chartDonut"></div>
</div>""", wide=True)
    + spec("商品卡", """
<div class="prod">
  <div class="prodImg"></div>
  <div class="prodBody"><b>无线耳机 Pro</b><span>¥1,299</span>
    <button class="btn sm">加入购物车</button></div>
</div>""")
    + spec("购物车行 / 数量步进", """
<div class="cartRow">
  <div class="cartThumb"></div>
  <div class="cartInfo"><b>无线耳机 Pro</b><span>黑色 · 标准版</span></div>
  <div class="qty"><button>−</button><span>1</span><button>+</button></div>
  <b class="cartPrice">¥1,299</b>
</div>""", wide=True)
    + spec("登录 / 验证码", """
<label class="fl">邮箱</label><input class="inp" placeholder="you@company.com">
<label class="fl">密码</label><input class="inp" type="password" value="12345678">
<div class="row" style="justify-content:space-between;margin:10px 0 14px">
  <label class="chk" style="margin:0"><input type="checkbox"><span>记住我</span></label>
  <a class="btn link sm">忘记密码？</a></div>
<button class="btn" style="width:100%;justify-content:center">登录</button>
<div class="otp"><input maxlength="1" value="2"><input maxlength="1" value="8">
<input maxlength="1" value="4"><input maxlength="1" value="1">
<input maxlength="1"><input maxlength="1"></div>""")
    + spec("404 / 错误页", """
<div class="err404"><b>404</b><span>页面走丢了</span>
<button class="btn sm">回到首页</button></div>""")
    + spec("公告条 / Cookie", """
<div class="banner"><b>新版本 2.0 已发布</b><span>查看更新日志</span><span class="bx">×</span></div>
<div class="cookie"><span>我们使用 Cookie 改善体验。</span>
<button class="btn sm">接受</button><button class="btn ghost sm">设置</button></div>""", wide=True)
    + spec("聊天气泡 / 输入", """
<div class="chat">
  <div class="bub them">这套风格能直接用在后台吗？</div>
  <div class="bub me">可以，组件总览里都有实现。</div>
  <div class="chatIn"><input placeholder="输入消息…"><button class="btn sm">发送</button></div>
</div>""", wide=True)
    + '</div>')


S8 = sec(8, "数据密集与企业级", "ENTERPRISE / DATA-DENSE", '<div class="specs">'
    + spec("表格多选 + 批量操作条", """
<div class="tblBar">
  <div class="row"><span class="chkLine"><input type="checkbox" checked><span>已选 2 项</span></span></div>
  <div class="row"><button class="btn ghost sm">导出</button><button class="btn sm danger">批量删除</button></div>
</div>
<table class="tbl">
  <thead><tr><th style="width:24px"><input type="checkbox" checked></th><th>项目</th><th>负责人</th><th class="r">进度</th></tr></thead>
  <tbody>
    <tr><td><input type="checkbox" checked></td><td>官网改版</td><td><span class="av">李</span></td><td class="r">82%</td></tr>
    <tr><td><input type="checkbox" checked></td><td>组件库</td><td><span class="av">王</span></td><td class="r">100%</td></tr>
    <tr><td><input type="checkbox"></td><td>数据看板</td><td><span class="av">陈</span></td><td class="r">46%</td></tr>
  </tbody>
</table>""", wide=True)
    + spec("向导式表单", """
<div class="wiz">
  <div class="wizTop"><span class="on">1 基本信息</span><span>2 配置</span><span>3 确认</span></div>
  <div class="wizBody">
    <label class="fl">项目名</label><input class="inp" placeholder="arc-studio">
    <label class="fl">描述</label><input class="inp" placeholder="一句话说明">
  </div>
  <div class="row" style="justify-content:flex-end;margin-top:12px">
    <button class="btn ghost sm">上一步</button><button class="btn sm">下一步</button></div>
</div>""")
    + spec("看板卡", """
<div class="kbd">
  <div class="kcol"><span class="kcolT">待办 3</span>
    <div class="kcard"><b>登录页改版</b><span>李 · 11-26</span></div>
    <div class="kcard"><b>接口联调</b><span>王 · 11-27</span></div>
  </div>
  <div class="kcol"><span class="kcolT">进行中 2</span>
    <div class="kcard"><b>组件总览</b><span>陈 · 11-25</span></div>
  </div>
</div>""")
    + spec("通知中心", """
<div class="notif">
  <div class="notifTop"><b>通知</b><span class="nb">3 条未读</span></div>
  <a class="nItem on"><span class="nDot"></span><b>构建成功</b><span>2 分钟前</span></a>
  <a class="nItem on"><span class="nDot"></span><b>王 评论了你的设计</b><span>1 小时前</span></a>
  <a class="nItem"><span class="nDot off"></span><b>每周报告已生成</b><span>昨天</span></a>
</div>""")
    + spec("媒体 / 视频", """
<div class="media"><span class="play">▶</span><span class="mediaTag">02:14</span></div>
<div class="mediaRow">
  <div class="mThumb"></div><div class="mThumb"></div><div class="mThumb"></div>
</div>""")
    + spec("头像上传", """
<div class="avUp">
  <div class="avBig">李</div>
  <div class="avUpAct"><button class="btn ghost sm">更换头像</button>
  <span class="help">JPG / PNG · ≥ 256px</span></div>
</div>""")
    + spec("周视图日程", """
<div class="week">
  <div class="wHead"><span></span><span>一</span><span>二</span><span>三</span><span>四</span><span>五</span></div>
  <div class="wBody">
    <span class="wTime">09</span><span class="wCell"></span><span class="wCell"></span>
    <span class="wCell ev">评审</span><span class="wCell"></span><span class="wCell"></span>
    <span class="wTime">10</span><span class="wCell"></span><span class="wCell ev">站会</span>
    <span class="wCell"></span><span class="wCell"></span><span class="wCell"></span>
    <span class="wTime">11</span><span class="wCell ev">客户</span><span class="wCell"></span>
    <span class="wCell"></span><span class="wCell"></span><span class="wCell"></span>
  </div>
</div>""", wide=True)
    + spec("语言切换", """
<div class="lang"><span class="on">中文</span><span>EN</span><span>日本語</span></div>""")
    + '</div>')


S9 = sec(9, "页面骨架（P0）", "PAGE SKELETON", '<div class="specs">'
    + spec("页面头部", """
<div class="pageHead">
  <div class="phL">
    <nav class="crumb"><a href="#">项目</a><span>/</span><b>官网改版</b></nav>
    <h3>官网改版</h3>
    <p>2026 年品牌升级，预计 12 月上线。</p>
  </div>
  <div class="phR"><button class="btn ghost sm">分享</button><button class="btn sm">编辑项目</button></div>
</div>""", wide=True)
    + spec("筛选栏（含已选条件）", """
<div class="filters">
  <div class="inp-ico"><span>⌕</span><input class="inp" placeholder="搜索项目…"></div>
  <select class="inp sm"><option>全部状态</option><option>进行中</option></select>
  <select class="inp sm"><option>全部负责人</option></select>
  <button class="btn sm">筛选</button>
  <button class="btn ghost sm">重置</button>
</div>
<div class="row" style="margin-top:10px">
  <span class="fchip">状态：进行中 <b>×</b></span><span class="fchip">负责人：李 <b>×</b></span>
</div>""", wide=True)
    + spec("表格：粘性表头 + 列设置", """
<div class="tblTools">
  <span class="lab" style="margin:0">项目清单</span>
  <div class="colset">
    <button class="btn ghost sm">列设置 ▾</button>
    <div class="colPanel">
      <label class="chk"><input type="checkbox" checked><span>项目名</span></label>
      <label class="chk"><input type="checkbox" checked><span>负责人</span></label>
      <label class="chk"><input type="checkbox" checked><span>进度</span></label>
      <label class="chk"><input type="checkbox"><span>更新时间</span></label>
    </div>
  </div>
</div>
<div class="tblScroll">
  <table class="tbl">
    <thead><tr><th>项目</th><th>负责人</th><th class="r">进度</th></tr></thead>
    <tbody>
      <tr><td>官网改版</td><td>李</td><td class="r">82%</td></tr>
      <tr><td>组件库</td><td>王</td><td class="r">100%</td></tr>
      <tr><td>数据看板</td><td>陈</td><td class="r">46%</td></tr>
      <tr><td>移动端</td><td>赵</td><td class="r">12%</td></tr>
      <tr><td>品牌手册</td><td>周</td><td class="r">68%</td></tr>
      <tr><td>官网英文站</td><td>李</td><td class="r">30%</td></tr>
    </tbody>
  </table>
</div>""", wide=True)
    + spec("确认对话框（输入确认）", """
<div class="confirm">
  <h4>删除「官网改版」？</h4>
  <p>该操作不可撤销，28 个构建记录会一并删除。请输入 <code>DELETE</code> 确认。</p>
  <input class="inp" placeholder="DELETE">
  <div class="row" style="justify-content:flex-end;margin-top:12px">
    <button class="btn ghost sm">取消</button>
    <button class="btn sm danger">永久删除</button>
  </div>
</div>""")
    + spec("表单布局（左标签 / 分组 / 必填）", """
<form class="formGrid">
  <div class="fg">
    <label class="fgL">项目名 <i>*</i></label>
    <div class="fgR"><input class="inp" placeholder="arc-studio">
      <span class="help">用于 URL，创建后不可修改</span></div>
  </div>
  <div class="fg">
    <label class="fgL">团队</label>
    <div class="fgR"><select class="inp"><option>设计组</option><option>前端组</option></select></div>
  </div>
  <div class="fg">
    <label class="fgL">描述</label>
    <div class="fgR"><textarea class="inp" rows="2"></textarea></div>
  </div>
  <div class="fg">
    <label class="fgL">通知邮箱 <i>*</i></label>
    <div class="fgR"><input class="inp" placeholder="team@arc.studio"></div>
  </div>
  <div class="fgActions"><button class="btn ghost sm">取消</button><button class="btn sm">保存</button></div>
</form>""", wide=True)
    + '</div>')


S10 = sec(10, "表单补充", "FORMS / EXTENDED", '<div class="specs">'
    + spec("颜色选择器", """
<div class="row"><span class="swatch" style="background:#f6d743"></span>
<span class="swatch on" style="background:#111"></span><span class="swatch" style="background:#dc2626"></span>
<span class="swatch" style="background:#16a34a"></span>
<input class="inp" style="width:110px" value="#111111"></div>""")
    + spec("穿梭框", """
<div class="transfer">
  <div class="trBox"><span class="trT">待选 3</span>
    <label class="chk"><input type="checkbox" checked><span>按钮</span></label>
    <label class="chk"><input type="checkbox"><span>表格</span></label>
    <label class="chk"><input type="checkbox"><span>图表</span></label></div>
  <div class="trMid"><button class="btn ghost sm">›</button><button class="btn ghost sm">‹</button></div>
  <div class="trBox"><span class="trT">已选 1</span>
    <label class="chk"><input type="checkbox" checked><span>表单</span></label></div>
</div>""", wide=True)
    + spec("树形多选", """
<ul class="tree check"><li class="open"><label class="chk"><input type="checkbox" checked><span>设计系统</span></label>
  <ul><li><label class="chk"><input type="checkbox" checked><span>颜色</span></label></li>
  <li><label class="chk"><input type="checkbox"><span>排版</span></label></li></ul></li>
<li><label class="chk"><input type="checkbox"><span>资源</span></label></li></ul>""")
    + spec("富文本工具栏", """
<div class="rte">
  <div class="rteBar"><b>B</b><i>I</i><u>U</u><span class="rteSep"></span>H1<span>¶</span>
    <span class="rteSep"></span>🔗</div>
  <div class="rteBody" contenteditable="true">在这里输入正文…选中文字可用上方工具栏。</div>
</div>""", wide=True)
    + spec("代码编辑器", """
<div class="code">
  <div class="codeBar"><span>tokens.css</span><span class="codeDots">● ● ●</span></div>
  <pre><span class="c1">:root</span> {
  <span class="c2">--accent</span>: <span class="c3">#f6d743</span>;
  <span class="c2">--radius</span>: <span class="c3">0</span>;
}</pre>
</div>""", wide=True)
    + spec("上传进度 / 失败重试", """
<div class="upRow"><span class="upName">brand-kit.zip</span><span class="upBar"><i style="width:62%"></i></span><span class="upPct">62%</span></div>
<div class="upRow err"><span class="upName">logo.svg</span><span class="upMsg">上传失败</span>
<button class="btn ghost sm">重试</button></div>""", wide=True)
    + spec("表单错误汇总", """
<div class="alert err"><b>有 2 个字段需要修改</b>
<a class="errLink">项目名不能为空</a><a class="errLink">邮箱格式不正确</a></div>""")
    + '</div>')

S11 = sec(11, "导航补充", "NAVIGATION / EXTENDED", '<div class="specs">'
    + spec("侧栏可折叠分组", """
<nav class="sideGroup">
  <div class="sgItem open"><b>设计系统</b>
    <a class="on">概览</a><a>颜色</a><a>排版</a></div>
  <div class="sgItem"><b>组件</b><a>按钮</a><a>表单</a></div>
  <div class="sgItem"><b>资源</b></div>
</nav>""")
    + spec("锚点目录 TOC", """
<aside class="toc"><span class="lab">本页目录</span>
<a class="tocL on">1. 快速开始</a><a class="tocL">2. 安装</a>
<a class="tocL sub">2.1 包管理器</a><a class="tocL">3. 主题</a></aside>""")
    + spec("Skip link（无障碍）", """
<div class="skipWrap"><a class="skip" href="#">跳到主内容</a>
<span class="help">按 Tab 键时出现在左上角，键盘用户可跳过导航。</span></div>""")
    + '</div>')

S12 = sec(12, "数据补充", "DATA / EXTENDED", '<div class="specs">'
    + spec("表格行展开", """
<table class="tbl"><tbody>
  <tr><td style="width:22px">▸</td><td>官网改版</td><td class="r">82%</td></tr>
  <tr><td>▾</td><td>组件库</td><td class="r">100%</td></tr>
  <tr class="expRow"><td></td><td colspan="2">
    <div class="expBody"><span>负责人：王</span><span>创建：11-02</span><span>构建：42 次</span></div>
  </td></tr>
</tbody></table>""", wide=True)
    + spec("环形进度", """
<div class="row" style="gap:18px">
  <div class="ring" style="--p:72"><b>72%</b></div>
  <div class="ring sm" style="--p:40"><b>40%</b></div>
</div>""")
    + spec("图表提示 / 图例", """
<div class="chartTip">
  <div class="ctBars"><i style="height:40%"></i><i style="height:76%" class="on"></i><i style="height:58%"></i></div>
  <div class="ctPop"><b>11-24</b><span>构建 1,284 次</span></div>
</div>
<div class="row" style="margin-top:10px"><span class="lg on">构建</span><span class="lg">失败</span></div>""")
    + spec("空表格 / 加载表格", """
<table class="tbl tblEmpty"><thead><tr><th>项目</th><th>状态</th></tr></thead>
<tbody><tr><td colspan="2"><div class="empty small"><i></i><b>没有匹配的记录</b>
<span>换个筛选条件试试</span></div></td></tr></tbody></table>""")
    + spec("键值详情 Descriptions", """
<dl class="desc">
  <div><dt>项目 ID</dt><dd>arc-2026-01</dd></div>
  <div><dt>创建人</dt><dd>李</dd></div>
  <div><dt>创建时间</dt><dd>2026-11-02 10:24</dd></div>
  <div><dt>状态</dt><dd><span class="badge">进行中</span></dd></div>
</dl>""", wide=True)
    + spec("漏斗", """
<div class="funnel"><div style="width:100%"><b>12,480</b><span>访问</span></div>
<div style="width:72%"><b>8,986</b><span>试用</span></div>
<div style="width:44%"><b>5,492</b><span>下单</span></div>
<div style="width:24%"><b>2,995</b><span>付费</span></div></div>""")
    + spec("热力图", """
<div class="heat">
  <i style="--v:.2"></i><i style="--v:.6"></i><i style="--v:.9"></i><i style="--v:.3"></i><i style="--v:.7"></i>
  <i style="--v:.8"></i><i style="--v:1"></i><i style="--v:.4"></i><i style="--v:.5"></i><i style="--v:.2"></i>
  <i style="--v:.3"></i><i style="--v:.9"></i><i style="--v:.6"></i><i style="--v:1"></i><i style="--v:.4"></i>
</div>
<div class="row" style="margin-top:8px"><span class="tiny muted">低</span>
<span class="heatLeg"><i style="--v:.2"></i><i style="--v:.5"></i><i style="--v:.8"></i><i style="--v:1"></i></span>
<span class="tiny muted">高</span></div>""")
    + '</div>')

S13 = sec(13, "媒体", "MEDIA", '<div class="specs">'
    + spec("图片灯箱", """
<div class="lightbox"><div class="lbImg"></div><span class="lbNav">‹</span><span class="lbNav r">›</span>
<span class="lbCount">2 / 8</span></div>""")
    + spec("音频播放条", """
<div class="audio"><button class="btn icon sm">▶</button>
<span class="audioBar"><i style="width:38%"></i></span><span class="tiny muted">01:12 / 03:05</span></div>""", wide=True)
    + spec("头像裁剪", """
<div class="crop"><div class="cropImg"></div><div class="cropMask"></div></div>
<div class="row" style="margin-top:8px"><button class="btn ghost sm">重选</button>
<button class="btn sm">裁剪并保存</button></div>""")
    + spec("地图占位卡", """
<div class="mapCard"><div class="mapGrid"></div>
<div class="mapPin">📍</div><div class="mapInfo"><b>上海 · 静安</b><span>南京西路 1266 号</span></div></div>""", wide=True)
    + '</div>')

S14 = sec(14, "业务补充", "BUSINESS / EXTENDED", '<div class="specs">'
    + spec("结算汇总 / 优惠码", """
<div class="summary">
  <div class="sumRow"><span>商品小计</span><b>¥2,598</b></div>
  <div class="sumRow"><span>优惠（NEW20）</span><b class="down">−¥520</b></div>
  <div class="sumRow"><span>运费</span><b>¥0</b></div>
  <div class="sumRow total"><span>应付</span><b>¥2,078</b></div>
  <div class="coupon"><input class="inp sm" placeholder="输入优惠码">
    <button class="btn ghost sm">应用</button></div>
  <button class="btn" style="width:100%;justify-content:center;margin-top:10px">去支付</button>
</div>""")
    + spec("订单状态流", """
<ol class="orderFlow"><li class="done"><b>下单</b><span>11-20 10:24</span></li>
<li class="done"><b>付款</b><span>11-20 10:26</span></li>
<li class="on"><b>发货</b><span>预计 11-26</span></li>
<li><b>签收</b><span>—</span></li></ol>""", wide=True)
    + spec("SKU 选择器", """
<div class="sku"><span class="skuT">颜色</span>
  <div class="row"><span class="skuOpt on">黑</span><span class="skuOpt">白</span><span class="skuOpt dis">蓝</span></div>
  <span class="skuT">版本</span>
  <div class="row"><span class="skuOpt on">标准</span><span class="skuOpt">Pro</span></div>
</div>""")
    + spec("权限矩阵", """
<table class="tbl perm"><thead><tr><th>角色</th><th>读</th><th>写</th><th>管理</th></tr></thead>
<tbody><tr><td>管理员</td><td><input type="checkbox" checked></td><td><input type="checkbox" checked></td><td><input type="checkbox" checked></td></tr>
<tr><td>编辑</td><td><input type="checkbox" checked></td><td><input type="checkbox" checked></td><td><input type="checkbox"></td></tr>
<tr><td>访客</td><td><input type="checkbox" checked></td><td><input type="checkbox"></td><td><input type="checkbox"></td></tr></tbody></table>""")
    + spec("用量配额条", """
<div class="quota"><div class="qRow"><span>本月构建</span><b>3,120 / 5,000</b></div>
<div class="prog"><i style="width:62%"></i></div>
<div class="qRow"><span>成员席位</span><b>8 / 10</b></div>
<div class="prog warn"><i style="width:80%"></i></div></div>""")
    + spec("邀请成员", """
<div class="invite"><label class="fl">邮箱</label>
<div class="row"><input class="inp" placeholder="name@team.com" style="flex:1">
<select class="inp sm"><option>编辑</option><option>访客</option></select>
<button class="btn sm">邀请</button></div>
<div class="row" style="margin-top:10px"><span class="av">李</span><span class="tiny">已邀请 · 待接受</span></div></div>""", wide=True)
    + spec("审计日志", """
<table class="tbl"><thead><tr><th>时间</th><th>操作人</th><th>动作</th></tr></thead>
<tbody><tr><td>11-25 09:12</td><td>李</td><td>删除了「旧首页」</td></tr>
<tr><td>11-24 18:03</td><td>王</td><td>发布了 v2.4</td></tr></tbody></table>""", wide=True)
    + spec("导出（列选择）", """
<div class="exportBox"><label class="chk"><input type="checkbox" checked><span>项目名</span></label>
<label class="chk"><input type="checkbox" checked><span>负责人</span></label>
<label class="chk"><input type="checkbox"><span>更新时间</span></label>
<div class="row" style="margin-top:8px"><button class="btn sm">导出 CSV</button></div></div>""")
    + '</div>')

S15 = sec(15, "系统与杂项", "SYSTEM / UTILITY", '<div class="specs">'
    + spec("分割线 / 间距", """
<div class="hr"></div><div class="hr dash"></div><div class="hr thick"></div>
<span class="help">实线 / 虚线 / 粗线，全部用 --line 派生。</span>""")
    + spec("按钮带计数徽标", """
<div class="row"><button class="btn ghost sm">通知 <b class="cnt">3</b></button>
<button class="btn ghost sm">收件箱 <b class="cnt">12</b></button></div>""")
    + spec("复制按钮", """
<div class="row"><input class="inp sm" value="arc-2026-01" readonly>
<button class="btn ghost sm">复制</button></div>""")
    + spec("FAB 悬浮操作", """
<div class="fabWrap"><button class="fab">＋</button>
<span class="help">固定右下角的快捷创建入口。</span></div>""")
    + spec("快捷键标注", """
<div class="row"><span class="tiny muted">保存</span><kbd>⌘ S</kbd>
<span class="tiny muted">搜索</span><kbd>⌘ K</kbd><span class="tiny muted">关闭</span><kbd>Esc</kbd></div>""", wide=True)
    + spec("打印样式", """
<div class="printPrev"><div class="pvLine w60"></div><div class="pvLine w100"></div>
<div class="pvLine w80"></div><div class="pvLine w40"></div>
<span class="help">打印时去背景、去阴影、保留文字与分割线。</span></div>""")
    + '</div>')


S16 = sec(16, "内容与页面（补充）", "CONTENT / PAGES", '<div class="specs">'
    + spec("博客卡", """
<article class="post"><div class="postImg"></div>
  <div class="postBody"><span class="postTag">设计系统</span>
    <b>为什么我们放弃了设计稿</b>
    <p>从 Figma 到代码，中间丢掉的那一层。</p>
    <span class="postMeta">李 · 8 分钟阅读</span></div></article>""")
    + spec("团队卡", """
<div class="teams">
  <div class="team"><span class="av lg">李</span><b>李工</b><span>设计负责人</span></div>
  <div class="team"><span class="av lg">王</span><b>王工</b><span>前端</span></div>
  <div class="team"><span class="av lg">陈</span><b>陈工</b><span>产品</span></div>
</div>""", wide=True)
    + spec("招聘岗位列表", """
<div class="jobs">
  <a class="job"><b>高级前端工程师</b><span>上海 · 全职</span><em>→</em></a>
  <a class="job"><b>产品设计师</b><span>远程 · 全职</span><em>→</em></a>
  <a class="job"><b>设计实习生</b><span>上海 · 实习</span><em>→</em></a>
</div>""", wide=True)
    + spec("更新日志", """
<div class="clog">
  <div class="clogItem"><span class="clogV">v2.4</span><span class="clogD">11-20</span>
    <ul><li>新增组件总览</li><li>修复深色模式对比度</li></ul></div>
  <div class="clogItem"><span class="clogV">v2.3</span><span class="clogD">10-28</span>
    <ul><li>支持自定义 tokens</li></ul></div>
</div>""", wide=True)
    + spec("文档三栏布局", """
<div class="docs">
  <aside class="docsL"><b>指南</b><a class="on">快速开始</a><a>安装</a><a>主题</a></aside>
  <div class="docsC"><h4>快速开始</h4>
    <p>三分钟接入一套风格：复制 tokens，引入 theme.css，替换变量。</p>
    <div class="docsCode">:root { --accent: #f6d743; }</div></div>
  <aside class="docsR"><span class="lab">本页</span><a class="on">快速开始</a><a>下一步</a></aside>
</div>""", wide=True)
    + spec("套餐对比表", """
<table class="tbl cmp"><thead><tr><th>功能</th><th class="r">Free</th><th class="r">Pro</th><th class="r">Team</th></tr></thead>
<tbody>
  <tr><td>项目数</td><td class="r">3</td><td class="r">无限</td><td class="r">无限</td></tr>
  <tr><td>风格包</td><td class="r">—</td><td class="r">✓</td><td class="r">✓</td></tr>
  <tr><td>协作</td><td class="r">—</td><td class="r">—</td><td class="r">✓</td></tr>
</tbody></table>""", wide=True)
    + spec("500 / 离线页", """
<div class="err404"><b>500</b><span>服务器开小差了</span>
<button class="btn sm">重新加载</button></div>""")
    + '</div>')



BODY = (S1 + S2 + S3 + S4 + S5 + S6 + S7 + S8 + S9 + S10 + S11 + S12 + S13 + S14 + S15 + S16)

NAV = (
    '<a href="#s1">按钮与操作</a>' '<a href="#s2">表单控件</a>' '<a href="#s3">导航与结构</a>'
    '<a href="#s4">数据展示</a>' '<a href="#s5">反馈与状态</a>' '<a href="#s10">表单补充</a>'
    '<a href="#s11">导航补充</a>' '<a href="#s12">数据补充</a>' '<a href="#s13">媒体</a>'
    '<a href="#s6">内容区块</a>' '<a href="#s7">高级与业务</a>' '<a href="#s8">数据密集</a>'
    '<a href="#s9">页面骨架</a>' '<a href="#s14">业务补充</a>' '<a href="#s15">系统与杂项</a>'
    '<a href="#s16">内容补充</a>'
)

CSS = """
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--font-b);-webkit-font-smoothing:antialiased}
.wrap{max-width:1180px;margin:0 auto;padding:0 40px 80px}
.topbar{position:sticky;top:0;z-index:30;display:flex;align-items:center;gap:14px;
  padding:14px 40px;background:var(--bg);border-bottom:var(--nav-border);flex-wrap:wrap}
.topbar .bk{font-family:var(--font-k);font-size:12px;color:var(--muted);text-decoration:none}
.topbar .bk:hover{color:var(--accent)}
.topbar .st{font-family:var(--font-h);font-weight:800;font-size:16px}
.topbar .st em{font-style:normal;font-family:var(--font-k);font-size:11px;color:var(--muted);
  margin-left:8px;font-weight:400}
.topbar .right{margin-left:auto;display:flex;gap:8px;align-items:center}
.secnav{display:flex;gap:6px;flex-wrap:wrap;padding:16px 40px 0;max-width:1180px;margin:0 auto}
.secnav a{font-size:12px;text-decoration:none;color:var(--muted);padding:5px 11px;border-radius:999px;
  border:1px solid var(--line)}
.secnav a:hover{color:var(--ink);border-color:var(--ink)}
.sec{padding:36px 0 8px;border-top:var(--nav-border);margin-top:26px}
.secHead{display:flex;align-items:baseline;gap:12px;margin-bottom:18px}
.secHead h2{margin:0;font-family:var(--font-h);font-size:18px;font-weight:var(--h1-w)}
.secHead span{font-family:var(--font-k);font-size:10.5px;letter-spacing:.16em;color:var(--muted)}
.specs{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:14px}
.spec{background:var(--surface);border:var(--panel-border,var(--card-border));
  border-radius:var(--panel-radius,var(--radius));
  box-shadow:var(--panel-shadow,var(--shadow));padding:18px;position:relative}
.spec.wide{grid-column:1/-1}
.lab{display:block;font-family:var(--font-k);font-size:9.5px;letter-spacing:.16em;text-transform:uppercase;
  color:var(--muted);margin-bottom:12px}
.row{display:flex;gap:9px;align-items:center;flex-wrap:wrap}
.tiny{font-size:11px}.muted{color:var(--muted)}
.right{display:block;text-align:right}
.btn{background:var(--accent);color:var(--on-accent);border:var(--btn-border);border-radius:var(--btn-radius);
  box-shadow:var(--btn-shadow);padding:9px 18px;font:inherit;font-size:13px;font-weight:600;cursor:pointer;
  display:inline-flex;align-items:center;gap:6px;transition:.15s}
.btn:active{transform:translateY(1px)}
.btn:focus-visible{outline:2px solid var(--accent);outline-offset:2px}
.btn.ghost{background:transparent;color:var(--ink);border:1px solid var(--line);box-shadow:none}
.btn.link{background:none;border:0;box-shadow:none;color:var(--accent);padding:9px 4px}
.btn.danger{background:#dc2626;color:#fff;border-color:#dc2626}
.btn.danger-g{color:#dc2626;border-color:#dc2626}
.btn:disabled{opacity:.42;pointer-events:none}
.btn.sm{padding:6px 13px;font-size:12px}
.btn.icon{width:34px;height:34px;padding:0;justify-content:center}
.btngroup{display:inline-flex;border:1px solid var(--line);border-radius:var(--btn-radius);overflow:hidden}
.btngroup .btn{border:0;border-radius:0;box-shadow:none;background:transparent;color:var(--ink)}
.btngroup .btn.on{background:var(--accent);color:var(--on-accent)}
.fl{display:block;font-family:var(--font-k);font-size:10.5px;letter-spacing:.06em;color:var(--muted);margin:8px 0 5px}
.inp{width:100%;padding:9px 12px;font:inherit;font-size:13px;color:var(--ink);background:var(--bg);
  border:1px solid var(--line);border-radius:var(--btn-radius);outline:none}
.inp.sm{padding:6px 10px;font-size:12px;width:auto}
.inp:focus{border-color:var(--accent)}
.inp::placeholder{color:var(--muted);opacity:.75}
textarea.inp{resize:vertical;min-height:64px;font-family:inherit}
.inp.invalid{border-color:#dc2626}
.inp.valid{border-color:#16a34a}
.inp-ico{position:relative}
.inp-ico span{position:absolute;left:10px;top:50%;transform:translateY(-50%);color:var(--muted);font-size:14px}
.inp-ico .inp{padding-left:30px}
.chk{display:flex;gap:8px;align-items:center;font-size:13px;margin:7px 0}
.chk input{accent-color:var(--accent);width:15px;height:15px}
.help{display:block;font-size:11px;color:var(--muted);margin-top:6px}
.err-msg{display:block;font-size:11.5px;color:#dc2626;margin-top:5px}
.ok-msg{display:block;font-size:11.5px;color:#16a34a;margin-top:5px}
.sw{width:38px;height:21px;border-radius:999px;background:var(--line);position:relative;
  display:inline-block;cursor:pointer}
.sw i{position:absolute;top:3px;left:3px;width:15px;height:15px;border-radius:50%;
  background:var(--bg);transition:.15s}
.sw.on{background:var(--accent)}
.sw.on i{left:20px;background:var(--on-accent)}
.range{width:100%;margin-top:14px;accent-color:var(--accent)}
.drop{display:grid;gap:4px;place-items:center;padding:20px 12px;border:1px dashed var(--line);
  border-radius:var(--radius);cursor:pointer;text-align:center;font-size:12.5px}
.drop b{font-size:13px}
.drop span{font-size:11px;color:var(--muted)}
.fileChip{display:inline-flex;gap:8px;align-items:center;font-size:11.5px;padding:4px 10px;
  border:1px solid var(--line);border-radius:999px}
.fileChip span{color:var(--muted);cursor:pointer}
.seg{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden}
.seg.full{width:100%}.seg.full .sg{flex:1}
.sg{font:inherit;font-size:12px;padding:6px 14px;border:0;background:none;color:var(--muted);cursor:pointer}
.sg.on{background:var(--accent);color:var(--on-accent)}
.crumb{display:flex;gap:8px;font-family:var(--font-k);font-size:11.5px;color:var(--muted);align-items:center}
.crumb a{color:inherit;text-decoration:none}.crumb b{color:var(--ink)}
.tabs{display:flex;gap:2px;border-bottom:1px solid var(--line)}
.tab{font:inherit;font-size:12.5px;padding:8px 14px;border:0;background:none;color:var(--muted);
  cursor:pointer;border-bottom:2px solid transparent;margin-bottom:-1px}
.tab.on{color:var(--ink);border-bottom-color:var(--accent);font-weight:600}
.steps{list-style:none;display:flex;margin:0;padding:0;font-family:var(--font-k);
  font-size:11px;color:var(--muted)}
.steps li{flex:1;display:grid;gap:6px;position:relative}
.steps li b{width:24px;height:24px;border-radius:50%;border:1px solid var(--line);display:grid;
  place-items:center;background:var(--bg);z-index:1;font-size:11px}
.steps li:after{content:'';position:absolute;left:24px;top:12px;right:6px;height:1px;background:var(--line)}
.steps li:last-child:after{display:none}
.steps li.on b{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.steps li.done b{border-color:var(--accent);color:var(--accent)}
.pager{display:flex;gap:4px}
.pg{width:30px;height:30px;border:1px solid var(--line);background:transparent;color:var(--ink);
  border-radius:var(--btn-radius);font:inherit;font-size:12px;cursor:pointer}
.pg.on{background:var(--accent);color:var(--on-accent);border-color:var(--accent)}
.side{display:grid;gap:2px}
.side a{display:block;padding:8px 12px;font-size:12.5px;color:var(--muted);text-decoration:none;
  border-radius:var(--btn-radius);cursor:pointer}
.side a.on{background:var(--accent);color:var(--on-accent);font-weight:600}
.miniNav{display:flex;gap:14px;align-items:center;font-size:12.5px;color:var(--muted)}
.miniNav b{color:var(--ink)}
.miniNav .on{color:var(--accent);font-weight:600}
.tblBar{display:flex;justify-content:space-between;gap:10px;margin-bottom:10px;flex-wrap:wrap}
.tbl{width:100%;border-collapse:collapse;font-size:12.5px}
.tbl th{font-family:var(--font-k);font-size:9.5px;letter-spacing:.14em;text-transform:uppercase;
  color:var(--muted);text-align:left;padding:8px 10px;border-bottom:1px solid var(--line);font-weight:500}
.tbl th.sort{cursor:pointer}
.tbl td{padding:10px;border-bottom:1px solid var(--line)}
.tbl tr:last-child td{border-bottom:0}
.tbl .r{text-align:right}
.rowAct{background:none;border:0;color:var(--muted);cursor:pointer;font-size:14px;line-height:1}
.av{display:inline-grid;place-items:center;width:24px;height:24px;border-radius:50%;
  background:var(--accent);color:var(--on-accent);font-size:11px;font-weight:600}
.avGroup{display:flex}
.avGroup .av{margin-left:-6px;border:2px solid var(--surface)}
.avGroup .av:first-child{margin-left:0}
.avMore{background:var(--line);color:var(--ink)}
.badge{display:inline-block;font-family:var(--font-k);font-size:10px;letter-spacing:.06em;
  background:var(--accent);color:var(--on-accent);border-radius:999px;padding:2px 8px}
.badge.soft{background:transparent;color:var(--muted);border:1px solid var(--line)}
.badge.ok{background:#16a34a;color:#fff}
.badge.warn{background:#f59e0b;color:#111}
.stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.stat{border:1px solid var(--line);border-radius:var(--radius);padding:14px}
.stat span{display:block;font-size:11px;color:var(--muted)}
.stat b{display:block;font-family:var(--font-h);font-size:26px;letter-spacing:-.02em;margin:4px 0}
.stat em{font-style:normal;font-size:11px;color:#16a34a}
.stat em.down{color:#dc2626}
.prog{height:8px;border-radius:999px;background:var(--line);overflow:hidden}
.prog i{display:block;height:100%;background:var(--accent)}
.prog.thin{height:4px;margin-top:8px}
.tl{list-style:none;margin:0;padding:0;display:grid;gap:12px;font-size:12px}
.tl li{display:flex;gap:9px;align-items:flex-start;color:var(--muted)}
.tl li b{width:9px;height:9px;border-radius:50%;border:1px solid var(--line);margin-top:3px;flex:0 0 auto}
.tl li.done b{background:var(--accent);border-color:var(--accent)}
.tl li span{display:flex;justify-content:space-between;flex:1;gap:10px}
.tl em{font-style:normal;font-family:var(--font-k);font-size:10.5px}
.rate{display:flex;gap:3px;align-items:center;font-size:15px;color:var(--accent)}
.rate .off{color:var(--line)}
.alert{font-size:12.5px;padding:10px 12px;border-radius:var(--btn-radius);margin-bottom:8px;
  border:1px solid var(--line);border-left-width:3px}
.alert b{display:block;font-size:12px;margin-bottom:2px}
.alert.info{border-left-color:var(--accent)}
.alert.ok{border-left-color:#16a34a}
.alert.err{border-left-color:#dc2626}
.empty{display:grid;gap:6px;justify-items:center;text-align:center;padding:10px 0}
.empty i{width:30px;height:30px;border:1px solid var(--line);border-radius:8px;display:block}
.empty b{font-size:13px}
.empty span{font-size:11.5px;color:var(--muted)}
.skel{display:grid;gap:8px}
.skel i{height:9px;border-radius:4px;background:var(--line);opacity:.7;animation:sh 1.4s linear infinite}
@keyframes sh{50%{opacity:.35}}
.spin{width:13px;height:13px;border:2px solid currentColor;border-right-color:transparent;
  border-radius:50%;display:inline-block;animation:rot .7s linear infinite}
.spin.big{width:22px;height:22px;border-width:3px;color:var(--accent)}
@keyframes rot{to{transform:rotate(360deg)}}
.tipWrap{position:relative;display:inline-block}
.tip{position:absolute;left:50%;bottom:calc(100% + 8px);transform:translateX(-50%);white-space:nowrap;
  background:var(--ink);color:var(--bg);font-size:11px;padding:5px 9px;border-radius:6px;
  opacity:0;pointer-events:none;transition:.15s}
.tipWrap:hover .tip{opacity:1}
.toast{position:fixed;left:50%;bottom:24px;transform:translate(-50%,16px);background:var(--ink);
  color:var(--bg);padding:10px 20px;border-radius:999px;font-size:12.5px;opacity:0;pointer-events:none;
  transition:.22s;z-index:120}
.toast.show{opacity:1;transform:translate(-50%,0)}
.feat{border:1px solid var(--line);border-radius:var(--radius);padding:14px}
.feat b{display:block;font-family:var(--font-h);font-size:15px;margin-bottom:4px}
.feat p{margin:0;font-size:12px;color:var(--muted);line-height:1.6}
.price{border:1px solid var(--line);border-radius:var(--radius);padding:16px}
.price span{font-family:var(--font-k);font-size:10px;letter-spacing:.14em;color:var(--muted);
  text-transform:uppercase}
.price b{display:block;font-family:var(--font-h);font-size:28px;margin:6px 0 10px}
.price b em{font-style:normal;font-size:12px;color:var(--muted);font-weight:400}
.price ul{margin:0 0 14px;padding-left:16px;font-size:12px;color:var(--muted);line-height:1.8}
.quote{margin:0;font-family:var(--font-h);font-size:16px;line-height:1.65}
.quote footer{display:flex;gap:10px;align-items:center;margin-top:12px;font-family:var(--font-b)}
.quote footer b{font-size:12.5px}
.quote footer em{font-style:normal;font-size:11.5px;color:var(--muted)}
.faq{border-bottom:1px solid var(--line);padding:9px 0;font-size:12.5px}
.faq summary{cursor:pointer;font-weight:600}
.faq p{margin:7px 0 0;color:var(--muted);line-height:1.7}
.logos{display:flex;gap:26px;flex-wrap:wrap;align-items:center;justify-content:space-between;
  font-family:var(--font-k);font-size:12px;letter-spacing:.18em;color:var(--muted);opacity:.75}
.ctaBand{display:flex;gap:14px;align-items:center;flex-wrap:wrap;padding:18px;
  border:1px solid var(--line);border-radius:var(--radius)}
.ctaBand b{font-family:var(--font-h);font-size:15px}
.ctaBand span{font-size:12px;color:var(--muted)}
.ctaBand .btn{margin-left:auto}
.modal{position:fixed;inset:0;background:rgba(10,10,12,.5);display:grid;place-items:center;padding:20px;
  opacity:0;pointer-events:none;transition:.2s;z-index:130}
.modal.open{opacity:1;pointer-events:auto}
.modalCard{background:var(--surface);border:var(--card-border);border-radius:var(--radius);
  box-shadow:var(--shadow);padding:22px;max-width:360px;width:100%}
.modalCard h3{margin:0 0 8px;font-family:var(--font-h);font-size:16px}
.modalCard p{margin:0;font-size:12.5px;color:var(--muted);line-height:1.7}
.drawer{position:fixed;top:0;right:0;bottom:0;width:320px;max-width:88vw;background:var(--surface);
  border-left:var(--card-border);padding:22px;transform:translateX(100%);transition:.26s;z-index:131;
  box-shadow:-10px 0 40px rgba(0,0,0,.2)}
.drawer.open{transform:none}
.drawer h3{margin:0 0 8px;font-family:var(--font-h);font-size:16px}
.drawer p{font-size:12.5px;color:var(--muted);line-height:1.7}

/* ---------- 高级与业务 ---------- */
.menuWrap{position:relative;display:inline-block}
.menu{position:absolute;left:0;top:calc(100% + 6px);min-width:150px;background:var(--surface);
  border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:5px;z-index:5}
.mi{display:block;padding:7px 10px;font-size:12.5px;color:var(--ink);text-decoration:none;
  border-radius:calc(var(--radius) * .6);cursor:pointer}
.mi:hover{background:var(--bg)}
.mi.danger{color:#dc2626}
.miSep{height:1px;background:var(--line);margin:5px 2px}
.combo{display:flex;flex-wrap:wrap;gap:6px;align-items:center;padding:7px 9px;
  border:1px solid var(--line);border-radius:var(--btn-radius);background:var(--bg)}
.ctag{display:inline-flex;gap:6px;align-items:center;font-size:11.5px;padding:2px 8px;
  border-radius:999px;background:var(--accent);color:var(--on-accent)}
.ctag span{cursor:pointer;opacity:.8}
.cin{border:0;background:none;outline:none;font:inherit;font-size:12.5px;color:var(--ink);
  min-width:90px;flex:1}
.comboList{margin-top:8px;border:1px solid var(--line);border-radius:var(--btn-radius);overflow:hidden}
.ci{display:block;padding:7px 10px;font-size:12.5px;text-decoration:none;color:var(--ink)}
.ci:hover,.ci.on{background:var(--bg);font-weight:600}
.cal{border:1px solid var(--line);border-radius:var(--radius);padding:12px;background:var(--surface)}
.calTop{display:flex;justify-content:space-between;align-items:center;font-size:12.5px;margin-bottom:10px}
.calNav{font-family:var(--font-k);color:var(--muted);letter-spacing:.2em}
.calHead{display:grid;grid-template-columns:repeat(7,1fr);gap:2px;font-family:var(--font-k);
  font-size:9.5px;color:var(--muted);text-align:center;margin-bottom:4px}
.calGrid{display:grid;grid-template-columns:repeat(7,1fr);gap:2px}
.calGrid i{display:grid;place-items:center;height:26px;font-size:11.5px;font-style:normal;
  border-radius:calc(var(--radius) * .5);cursor:pointer}
.calGrid i:hover{background:var(--bg)}
.calGrid i.mut{color:var(--muted);opacity:.5}
.calGrid i.on{background:var(--accent);color:var(--on-accent);font-weight:600}
.tree,.tree ul{list-style:none;margin:0;padding:0}
.tree ul{padding-left:14px;border-left:1px solid var(--line);margin-left:5px}
.tree li{padding:5px 0;font-size:12.5px;color:var(--ink)}
.tree b{font-weight:600;cursor:pointer}
.tree li.open>b:before{content:"▾ "}
.tree li>b:before{content:"▸ "}
.tree li.on{color:var(--accent);font-weight:600}
.cmd{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:var(--surface)}
.cmdIn{display:flex;gap:8px;align-items:center;padding:9px 12px;border-bottom:1px solid var(--line)}
.cmdIn span{color:var(--muted)}
.cmdIn input{flex:1;border:0;background:none;outline:none;font:inherit;font-size:13px;color:var(--ink)}
kbd{font-family:var(--font-k);font-size:9.5px;border:1px solid var(--line);
  border-radius:4px;padding:1px 5px;color:var(--muted)}
.cmdList{padding:5px}
.cmdItem{display:flex;justify-content:space-between;align-items:center;padding:7px 9px;
  font-size:12.5px;text-decoration:none;color:var(--ink);border-radius:5px}
.cmdItem.on{background:var(--bg)}
.chartRow{display:grid;grid-template-columns:1.2fr 1fr .8fr;gap:18px;align-items:end;height:120px}
.chartBars{display:flex;align-items:flex-end;gap:6px;height:120px}
.chartBars i{flex:1;background:var(--accent);border-radius:3px 3px 0 0;opacity:.85}
.chartLine{width:100%;height:120px;color:var(--accent)}
.chartDonut{width:96px;height:96px;border-radius:50%;margin:auto;
  background:conic-gradient(var(--accent) 0 62%,var(--line) 62% 100%);
  -webkit-mask:radial-gradient(circle,transparent 56%,#000 57%);
  mask:radial-gradient(circle,transparent 56%,#000 57%)}
.prod{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:var(--surface);max-width:260px}
.prodImg{aspect-ratio:4/3;max-height:170px;background:linear-gradient(140deg,var(--accent),var(--line));opacity:.85}
.prodBody{padding:12px;display:grid;gap:4px}
.prodBody b{font-size:13px}
.prodBody span{font-family:var(--font-k);font-size:12px;color:var(--muted)}
.prodBody .btn{margin-top:6px;justify-content:center}
.cartRow{display:flex;gap:12px;align-items:center;padding:10px 0;border-bottom:1px solid var(--line)}
.cartThumb{width:46px;height:46px;border-radius:var(--btn-radius);
  background:linear-gradient(140deg,var(--accent),var(--line))}
.cartInfo{flex:1;display:grid;gap:2px}
.cartInfo b{font-size:12.5px}
.cartInfo span{font-size:11px;color:var(--muted)}
.qty{display:inline-flex;border:1px solid var(--line);border-radius:var(--btn-radius);overflow:hidden}
.qty button{border:0;background:none;width:26px;height:26px;cursor:pointer;color:var(--ink);font-size:13px}
.qty span{display:grid;place-items:center;min-width:26px;font-size:12px;border-left:1px solid var(--line);
  border-right:1px solid var(--line)}
.cartPrice{font-family:var(--font-k);font-size:12.5px}
.otp{display:flex;gap:8px;margin-top:14px}
.otp input{width:34px;height:38px;text-align:center;font:inherit;font-size:14px;color:var(--ink);
  background:var(--bg);border:1px solid var(--line);border-radius:var(--btn-radius)}
.err404{display:grid;gap:6px;justify-items:center;text-align:center;padding:6px 0}
.err404 b{font-family:var(--font-h);font-size:46px;line-height:1;letter-spacing:-.04em}
.err404 span{font-size:12.5px;color:var(--muted)}
.err404 .btn{margin-top:8px}
.banner{display:flex;gap:12px;align-items:center;padding:9px 12px;border-radius:var(--btn-radius);
  background:var(--accent);color:var(--on-accent);font-size:12px}
.banner b{font-size:12px}
.banner .bx{margin-left:auto;cursor:pointer;opacity:.7}
.cookie{display:flex;gap:10px;align-items:center;margin-top:10px;padding:10px 12px;
  border:1px solid var(--line);border-radius:var(--radius);font-size:12px;background:var(--surface)}
.cookie .btn{margin-left:auto}
.chat{display:grid;gap:8px}
.bub{max-width:80%;padding:8px 12px;border-radius:12px;font-size:12.5px;line-height:1.6}
.bub.them{background:var(--bg);border:1px solid var(--line);justify-self:start}
.bub.me{background:var(--accent);color:var(--on-accent);justify-self:end}
.chatIn{display:flex;gap:8px;margin-top:4px}
.chatIn input{flex:1;padding:8px 12px;border:1px solid var(--line);border-radius:999px;
  background:var(--bg);color:var(--ink);font:inherit;font-size:12.5px;outline:none}


/* ---------- 数据密集 ---------- */
.chkLine{display:flex;gap:8px;align-items:center;font-size:12px;color:var(--muted)}
.chkLine input,.tbl input[type=checkbox]{accent-color:var(--accent);width:14px;height:14px}
.wiz{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.wizTop{display:flex;gap:0;background:var(--bg);border-bottom:1px solid var(--line)}
.wizTop span{flex:1;text-align:center;padding:9px 4px;font-size:11.5px;color:var(--muted);
  font-family:var(--font-k);border-right:1px solid var(--line)}
.wizTop span:last-child{border-right:0}
.wizTop .on{color:var(--ink);font-weight:600;box-shadow:inset 0 -2px 0 var(--accent)}
.wizBody{padding:12px}
.kbd{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.kcol{background:var(--bg);border-radius:var(--radius);padding:8px;display:grid;gap:8px;align-content:start}
.kcolT{font-family:var(--font-k);font-size:10px;letter-spacing:.12em;color:var(--muted);text-transform:uppercase}
.kcard{background:var(--surface);border:1px solid var(--line);border-radius:calc(var(--radius) * .7);
  padding:9px 10px;display:grid;gap:3px}
.kcard b{font-size:12px}
.kcard span{font-size:10.5px;color:var(--muted);font-family:var(--font-k)}
.notif{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.notifTop{display:flex;justify-content:space-between;align-items:center;padding:10px 12px;
  border-bottom:1px solid var(--line);font-size:12.5px}
.nb{font-family:var(--font-k);font-size:10px;background:var(--accent);color:var(--on-accent);
  border-radius:999px;padding:1px 7px}
.nItem{display:grid;grid-template-columns:8px 1fr auto;gap:8px;align-items:center;
  padding:9px 12px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
.nItem:last-child{border-bottom:0}
.nItem b{font-size:12px;font-weight:500}
.nItem span:last-child{font-size:10.5px;color:var(--muted);font-family:var(--font-k)}
.nDot{width:6px;height:6px;border-radius:50%;background:var(--accent)}
.nDot.off{background:var(--line)}
.media{position:relative;aspect-ratio:16/9;background:linear-gradient(140deg,var(--accent),var(--line));
  border-radius:var(--radius);display:grid;place-items:center;overflow:hidden}
.play{width:44px;height:44px;border-radius:50%;background:rgba(255,255,255,.9);color:#111;
  display:grid;place-items:center;font-size:14px;padding-left:3px}
.mediaTag{position:absolute;right:8px;bottom:8px;font-family:var(--font-k);font-size:10px;
  background:rgba(0,0,0,.55);color:#fff;padding:2px 7px;border-radius:4px}
.mediaRow{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:8px}
.mThumb{aspect-ratio:1;border-radius:calc(var(--radius) * .6);background:var(--line);opacity:.8}
.avUp{display:flex;gap:14px;align-items:center}
.avBig{width:56px;height:56px;border-radius:50%;background:var(--accent);color:var(--on-accent);
  display:grid;place-items:center;font-size:20px;font-weight:600;flex:0 0 auto}
.avUpAct{display:grid;gap:6px;justify-items:start}
.week{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.wHead{display:grid;grid-template-columns:38px repeat(5,1fr);border-bottom:1px solid var(--line);
  background:var(--bg);font-family:var(--font-k);font-size:10px;color:var(--muted);text-align:center}
.wHead span{padding:6px 0;border-left:1px solid var(--line)}
.wHead span:first-child{border-left:0}
.wBody{display:grid;grid-template-columns:38px repeat(5,1fr);grid-auto-rows:26px}
.wTime{font-family:var(--font-k);font-size:9.5px;color:var(--muted);display:grid;place-items:center;
  border-left:0;border-bottom:1px solid var(--line)}
.wCell{border-left:1px solid var(--line);border-bottom:1px solid var(--line)}
.wCell.ev{background:var(--accent);color:var(--on-accent);font-size:10px;display:grid;place-items:center;
  border-radius:3px;margin:2px}
.lang{display:inline-flex;border:1px solid var(--line);border-radius:999px;overflow:hidden}
.lang span{font-size:11.5px;padding:5px 12px;color:var(--muted);cursor:pointer;border-right:1px solid var(--line)}
.lang span:last-child{border-right:0}
.lang .on{background:var(--accent);color:var(--on-accent);font-weight:600}

/* ---------- 页面骨架 ---------- */
.pageHead{display:flex;gap:16px;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;
  padding-bottom:14px;border-bottom:1px solid var(--line)}
.phL{min-width:0;flex:1}
.phR{flex:0 0 auto;display:flex;gap:8px}
.pageHead h3{margin:6px 0 4px;font-family:var(--font-h);font-size:20px;letter-spacing:-.02em}
.pageHead p{margin:0;font-size:12.5px;color:var(--muted)}
.filters{display:grid;grid-template-columns:1.4fr auto auto auto auto;gap:8px;align-items:center}
.fchip{display:inline-flex;gap:6px;align-items:center;font-size:11px;padding:3px 9px;
  border:1px solid var(--line);border-radius:999px;color:var(--muted)}
.fchip b{color:var(--ink);cursor:pointer;font-weight:400}
.tblTools{display:flex;justify-content:space-between;align-items:center;margin-bottom:8px}
.colset{position:relative}
.colPanel{position:absolute;right:0;top:calc(100% + 6px);width:170px;background:var(--surface);
  border:1px solid var(--line);border-radius:var(--radius);box-shadow:var(--shadow);padding:8px;z-index:5}
.colPanel .chk{margin:4px 0;font-size:12px}
.tblScroll{max-height:196px;overflow:auto;border:1px solid var(--line);border-radius:var(--radius)}
.tblScroll .tbl th{position:sticky;top:0;background:var(--surface);z-index:1}
.tblScroll .tbl td,.tblScroll .tbl th{padding:8px 10px}
.confirm{border:1px solid var(--line);border-radius:var(--radius);padding:16px;background:var(--surface)}
.confirm h4{margin:0 0 6px;font-family:var(--font-h);font-size:14px}
.confirm p{margin:0 0 12px;font-size:12px;color:var(--muted);line-height:1.7}
.confirm code{font-family:var(--font-k);font-size:11px;padding:1px 5px;border:1px solid var(--line);
  border-radius:4px;color:var(--ink)}
.formGrid{display:grid;gap:12px;max-width:620px}
.fg{display:grid;grid-template-columns:110px 1fr;gap:12px;align-items:start}
.fgL{font-size:12px;color:var(--muted);padding-top:9px;font-family:var(--font-k)}
.fgL i{color:#dc2626;font-style:normal}
.fgR{display:grid;gap:4px}
.fgActions{display:flex;gap:8px;justify-content:flex-end;grid-column:1/-1;margin-top:4px}

/* ---------- 补充组件 ---------- */
.swatch{width:24px;height:24px;border-radius:6px;display:inline-block;cursor:pointer;
  border:1px solid rgba(0,0,0,.15)}
.swatch.on{outline:2px solid var(--ink);outline-offset:2px}
.transfer{display:grid;grid-template-columns:1fr 44px 1fr;gap:10px;align-items:start}
.trBox{border:1px solid var(--line);border-radius:var(--radius);padding:10px;display:grid;gap:2px}
.trT{font-family:var(--font-k);font-size:10px;color:var(--muted);letter-spacing:.1em;margin-bottom:4px}
.trMid{display:grid;gap:6px;place-items:center;padding-top:30px}
.tree.check .chk{margin:3px 0}
.rte{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden}
.rteBar{display:flex;gap:12px;align-items:center;padding:7px 10px;border-bottom:1px solid var(--line);
  font-size:12px;background:var(--bg);flex-wrap:wrap}
.rteBar b,.rteBar i,.rteBar u{font-style:normal;cursor:pointer}
.rteSep{width:1px;height:14px;background:var(--line)}
.rteBody{padding:12px;min-height:72px;font-size:13px;outline:none}
.code{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:#0f1110}
.codeBar{display:flex;justify-content:space-between;padding:7px 10px;border-bottom:1px solid #242b22;
  font-family:var(--font-k);font-size:10.5px;color:#8b9b8f}
.codeDots{letter-spacing:3px;color:#39463f}
.code pre{margin:0;padding:12px;font-family:var(--font-k);font-size:11.5px;line-height:1.9;color:#c5d0c0}
.code .c1{color:#8ee06a}.code .c2{color:#dfff00}.code .c3{color:#ff9ecb}
.upRow{display:flex;gap:10px;align-items:center;padding:8px 0;font-size:12px}
.upName{font-family:var(--font-k);font-size:11px;min-width:110px}
.upBar{flex:1;height:6px;border-radius:999px;background:var(--line);overflow:hidden}
.upBar i{display:block;height:100%;background:var(--accent)}
.upPct{font-family:var(--font-k);font-size:10.5px;color:var(--muted)}
.upRow.err .upMsg{color:#dc2626;font-size:11.5px;margin-left:auto}
.errLink{display:block;font-size:11.5px;text-decoration:underline;color:inherit;margin-top:2px}
.sideGroup{display:grid;gap:2px;font-size:12.5px}
.sgItem b{display:block;padding:7px 8px;cursor:pointer;color:var(--ink)}
.sgItem a{display:block;padding:6px 8px 6px 20px;color:var(--muted);text-decoration:none;
  border-radius:var(--btn-radius);cursor:pointer}
.sgItem a.on{background:var(--accent);color:var(--on-accent)}
.sgItem:not(.open) a{display:none}
.toc{display:grid;gap:2px;border-left:1px solid var(--line);padding-left:10px}
.tocL{display:block;padding:4px 0;font-size:12px;color:var(--muted);text-decoration:none;cursor:pointer}
.tocL.on{color:var(--ink);font-weight:600}
.tocL.sub{padding-left:12px;font-size:11.5px}
.skipWrap{position:relative}
.skip{position:absolute;left:0;top:-40px;background:var(--accent);color:var(--on-accent);
  padding:6px 12px;border-radius:0 0 var(--radius) 0;font-size:12px;text-decoration:none;transition:.15s}
.skipWrap:hover .skip,.skip:focus{top:0}
.expRow td{background:var(--bg)}
.expBody{display:flex;gap:18px;flex-wrap:wrap;font-size:11.5px;color:var(--muted);padding:4px 0}
.ring{width:76px;height:76px;border-radius:50%;display:grid;place-items:center;position:relative;
  background:conic-gradient(var(--accent) calc(var(--p) * 1%),var(--line) 0)}
.ring::before{content:'';position:absolute;inset:8px;border-radius:50%;background:var(--surface)}
.ring b{position:relative;font-size:13px;font-family:var(--font-k)}
.ring.sm{width:56px;height:56px}
.ring.sm::before{inset:6px}
.ring.sm b{font-size:11px}
.chartTip{position:relative}
.ctBars{display:flex;gap:6px;align-items:flex-end;height:70px}
.ctBars i{flex:1;background:var(--accent);opacity:.55;border-radius:3px 3px 0 0}
.ctBars i.on{opacity:1}
.ctPop{position:absolute;left:34%;top:-8px;background:var(--ink);color:var(--bg);padding:5px 9px;
  border-radius:6px;font-size:10.5px;display:grid;gap:1px;white-space:nowrap}
.ctPop b{font-size:11px}
.lg{font-size:11px;color:var(--muted);display:inline-flex;gap:5px;align-items:center}
.lg::before{content:'';width:8px;height:8px;border-radius:2px;background:var(--accent);opacity:.55}
.lg.on::before{opacity:1}
.empty.small{padding:6px 0}
.tblEmpty td{border-bottom:0}
.desc{margin:0;display:grid;grid-template-columns:1fr 1fr;gap:10px 22px}
.desc dt{font-family:var(--font-k);font-size:10px;color:var(--muted);letter-spacing:.08em;margin-bottom:2px}
.desc dd{margin:0;font-size:12.5px}
.funnel{display:grid;gap:5px}
.funnel div{background:var(--accent);color:var(--on-accent);border-radius:4px;padding:5px 9px;
  display:flex;justify-content:space-between;font-size:11px}
.funnel b{font-family:var(--font-k)}
.heat{display:grid;grid-template-columns:repeat(5,1fr);gap:4px}
.heat i{aspect-ratio:1;border-radius:3px;background:var(--accent);opacity:calc(.12 + var(--v) * .88)}
.heatLeg{display:inline-flex;gap:3px}
.heatLeg i{width:11px;height:11px;border-radius:2px;background:var(--accent);opacity:calc(.12 + var(--v) * .88)}
.lightbox{position:relative;border-radius:var(--radius);overflow:hidden;background:#111}
.lbImg{aspect-ratio:16/9;background:linear-gradient(135deg,var(--accent),#222);opacity:.85}
.lbNav{position:absolute;left:8px;top:50%;transform:translateY(-50%);width:26px;height:26px;
  border-radius:50%;background:rgba(0,0,0,.5);color:#fff;display:grid;place-items:center;font-size:13px}
.lbNav.r{left:auto;right:8px}
.lbCount{position:absolute;right:8px;bottom:8px;font-family:var(--font-k);font-size:10px;
  background:rgba(0,0,0,.55);color:#fff;padding:2px 7px;border-radius:4px}
.audio{display:flex;gap:10px;align-items:center}
.audioBar{flex:1;height:5px;border-radius:999px;background:var(--line);overflow:hidden}
.audioBar i{display:block;height:100%;background:var(--accent)}
.crop{position:relative;width:96px;height:96px;border-radius:50%;overflow:hidden;
  background:linear-gradient(140deg,var(--accent),var(--line))}
.cropMask{position:absolute;inset:0;border-radius:50%;box-shadow:0 0 0 2px var(--ink) inset}
.mapCard{position:relative;height:150px;border-radius:var(--radius);overflow:hidden;background:var(--bg);
  border:1px solid var(--line)}
.mapGrid{position:absolute;inset:0;
  background-image:linear-gradient(var(--line) 1px,transparent 1px),
    linear-gradient(90deg,var(--line) 1px,transparent 1px);background-size:26px 26px;opacity:.6}
.mapPin{position:absolute;left:38%;top:34%;font-size:18px}
.mapInfo{position:absolute;left:8px;bottom:8px;background:var(--surface);border:1px solid var(--line);
  border-radius:calc(var(--radius) * .7);padding:7px 10px;display:grid;gap:1px;font-size:11.5px}
.mapInfo span{color:var(--muted);font-size:10.5px}
.summary{border:1px solid var(--line);border-radius:var(--radius);padding:14px;display:grid;gap:7px;
  background:var(--surface)}
.sumRow{display:flex;justify-content:space-between;font-size:12px;color:var(--muted)}
.sumRow b{color:var(--ink);font-family:var(--font-k);font-weight:500}
.sumRow b.down{color:#16a34a}
.sumRow.total{border-top:1px solid var(--line);padding-top:8px;margin-top:3px;font-size:13px}
.sumRow.total b{font-size:15px;font-weight:600}
.coupon{display:flex;gap:6px;margin-top:4px}
.orderFlow{list-style:none;margin:0;padding:0;display:flex;font-family:var(--font-k);font-size:10.5px}
.orderFlow li{flex:1;display:grid;gap:4px;position:relative;color:var(--muted)}
.orderFlow b{font-size:11px;color:var(--ink)}
.orderFlow li:after{content:'';position:absolute;left:0;top:-1px;right:0;height:2px;background:var(--line)}
.orderFlow li.done:after,.orderFlow li.on:after{background:var(--accent)}
.orderFlow li.done b{color:var(--accent)}
.sku{display:grid;gap:6px}
.skuT{font-family:var(--font-k);font-size:10px;color:var(--muted);letter-spacing:.08em;margin-top:4px}
.skuOpt{font-size:11.5px;padding:4px 12px;border:1px solid var(--line);border-radius:6px;cursor:pointer}
.skuOpt.on{background:var(--accent);color:var(--on-accent);border-color:var(--accent);font-weight:600}
.skuOpt.dis{opacity:.4;text-decoration:line-through;cursor:not-allowed}
.perm td{text-align:center}
.perm th:not(:first-child){text-align:center}
.quota{display:grid;gap:6px}
.qRow{display:flex;justify-content:space-between;font-size:11.5px;color:var(--muted)}
.qRow b{color:var(--ink);font-family:var(--font-k);font-weight:500;font-size:11px}
.prog.warn i{background:#f59e0b}
.invite{display:grid;gap:2px}
.exportBox{display:grid;gap:2px}
.hr{height:1px;background:var(--line);margin:10px 0}
.hr.dash{background:none;border-top:1px dashed var(--line);height:0}
.hr.thick{height:3px}
.cnt{display:inline-grid;place-items:center;min-width:16px;height:16px;padding:0 4px;margin-left:4px;
  border-radius:999px;background:var(--accent);color:var(--on-accent);font-size:9.5px;font-weight:600}
.fabWrap{display:grid;gap:8px;justify-items:start}
.fab{width:48px;height:48px;border-radius:50%;border:var(--btn-border);background:var(--accent);
  color:var(--on-accent);font-size:20px;cursor:pointer;box-shadow:var(--btn-shadow)}
.printPrev{border:1px solid var(--line);border-radius:var(--radius);padding:14px;display:grid;gap:7px;
  background:#fff}
.pvLine{height:6px;background:#d9d9d4;border-radius:3px}
.w60{width:60%}.w100{width:100%}.w80{width:80%}.w40{width:40%}

/* ---------- 内容补充 ---------- */
.post{border:1px solid var(--line);border-radius:var(--radius);overflow:hidden;background:var(--surface)}
.postImg{aspect-ratio:16/9;background:linear-gradient(135deg,var(--accent),var(--line));opacity:.85}
.postBody{padding:12px;display:grid;gap:5px}
.postTag{font-family:var(--font-k);font-size:9.5px;letter-spacing:.1em;color:var(--accent);text-transform:uppercase}
.postBody b{font-size:13px;line-height:1.4}
.postBody p{margin:0;font-size:11.5px;color:var(--muted);line-height:1.6}
.postMeta{font-family:var(--font-k);font-size:10px;color:var(--muted)}
.teams{display:flex;gap:22px;flex-wrap:wrap}
.team{display:grid;gap:3px;justify-items:center;text-align:center}
.av.lg{width:44px;height:44px;font-size:16px}
.team b{font-size:12.5px;margin-top:4px}
.team span{font-size:11px;color:var(--muted)}
.jobs{border-top:1px solid var(--line)}
.job{display:grid;grid-template-columns:1fr auto 20px;gap:12px;align-items:center;
  padding:11px 2px;border-bottom:1px solid var(--line);text-decoration:none;color:var(--ink)}
.job b{font-size:13px;font-weight:600}
.job span{font-size:11.5px;color:var(--muted);font-family:var(--font-k)}
.job em{font-style:normal;color:var(--muted)}
.clog{display:grid;gap:14px}
.clogItem{display:grid;grid-template-columns:52px 1fr;gap:4px 12px;align-items:baseline}
.clogV{font-family:var(--font-k);font-size:11px;font-weight:600;color:var(--accent)}
.clogD{display:none}
.clogItem ul{grid-column:2;margin:4px 0 0;padding-left:16px;font-size:12px;color:var(--muted);line-height:1.8}
.docs{display:grid;grid-template-columns:150px 1fr 140px;gap:18px;font-size:12.5px}
.docsL,.docsR{display:grid;gap:2px;align-content:start}
.docsL b{font-size:11px;margin-bottom:4px}
.docsL a,.docsR a{padding:4px 0;color:var(--muted);cursor:pointer;font-size:12px}
.docsL a.on,.docsR a.on{color:var(--ink);font-weight:600}
.docsC h4{margin:0 0 6px;font-family:var(--font-h);font-size:15px}
.docsC p{margin:0;color:var(--muted);line-height:1.7;font-size:12px}
.docsCode{margin-top:10px;padding:9px 11px;background:var(--bg);border:1px solid var(--line);
  border-radius:6px;font-family:var(--font-k);font-size:11.5px;color:var(--ink)}
.cmp th.r,.cmp td.r{text-align:right}
.cmp td.r{font-family:var(--font-k);font-size:12px}

.tab,.badge,.chip,.sg,.btn,.pill,.tag,.lab,.crumb a,.crumb b{white-space:nowrap}
.tabs{overflow:hidden}
.tab{font-size:10.5px;padding:0 7px}
.panel{overflow:hidden}

@media (max-width:760px){
  .wrap{padding:0 18px 60px}.topbar{padding:12px 18px}.secnav{padding:14px 18px 0}
  .specs{grid-template-columns:1fr}.stats{grid-template-columns:1fr}
  .filters{grid-template-columns:1fr}
  .fg{grid-template-columns:1fr}
  .fgL{padding-top:0}
}
"""

TPL = Template("""<!doctype html>
<html lang="zh-CN"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>$no $cn · 组件总览</title>
<style>
:root{
--bg:$bg;--surface:$surface;--ink:$ink;--muted:$muted;--line:$line;
--accent:$accent;--on-accent:$on_accent;--radius:$radius;
--card-border:$cardborder;--shadow:$shadow;--btn-border:$btnborder;--btn-shadow:$btnshadow;
--btn-radius:$btnradius;--font-h:$fonth;--font-b:$fonth;--font-k:$fontk;
--h1-w:$h1w;--nav-border:$navborder;
}
$css
$railcss
</style></head>
<body>
$railhtml
<div class="topbar">
  <a class="bk" href="$slug.html">← 返回 demo</a>
  <div class="st">$cn<em>$en</em></div>
  <div class="right">
    $switch
    <a class="btn ghost sm" href="../assets/zips/style-$slug.zip" download>⤓ 导出风格包</a>
  </div>
</div>
<nav class="secnav">$nav</nav>
<div class="wrap">
$body
</div>
<div class="modal" id="modal"><div class="modalCard">
  <h3>确认删除？</h3><p>删除后 30 天内可在回收站恢复，关联的构建记录会一并隐藏。</p>
  <div class="row" style="justify-content:flex-end;margin-top:16px">
    <button class="btn ghost sm" data-close>取消</button><button class="btn sm">删除</button>
  </div>
</div></div>
<div class="drawer" id="drawer">
  <h3>筛选</h3><p>这里是抽屉面板，适合放筛选条件或详情。</p>
  <div class="row" style="margin-top:14px"><button class="btn sm" data-close>应用</button></div>
</div>
<script>
(function(){
  var toast=document.getElementById('toast'),tt;
  document.querySelectorAll('[data-toast]').forEach(function(b){b.onclick=function(){
    if(!toast)return;toast.classList.add('show');clearTimeout(tt);
    tt=setTimeout(function(){toast.classList.remove('show')},2000);};});
  var modal=document.getElementById('modal'),drawer=document.getElementById('drawer');
  document.querySelectorAll('[data-modal]').forEach(function(b){b.onclick=function(){modal.classList.add('open')}});
  document.querySelectorAll('[data-drawer]').forEach(function(b){b.onclick=function(){drawer.classList.add('open')}});
  document.querySelectorAll('[data-close]').forEach(function(b){b.onclick=function(){
    modal.classList.remove('open');drawer.classList.remove('open')}});
  if(modal)modal.addEventListener('click',function(e){if(e.target===modal)modal.classList.remove('open')});
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){
    modal.classList.remove('open');drawer.classList.remove('open')}});
  document.querySelectorAll('.sw').forEach(function(s){s.onclick=function(){s.classList.toggle('on')}});
  document.querySelectorAll('.btngroup .btn').forEach(function(b){b.onclick=function(){
    b.parentNode.querySelectorAll('.btn').forEach(function(x){x.classList.remove('on')});b.classList.add('on');}});
  document.querySelectorAll('.seg .sg').forEach(function(b){b.onclick=function(){
    b.parentNode.querySelectorAll('.sg').forEach(function(x){x.classList.remove('on')});b.classList.add('on');}});
  document.querySelectorAll('[data-tabs] .tab').forEach(function(b){b.onclick=function(){
    b.parentNode.querySelectorAll('.tab').forEach(function(x){x.classList.remove('on')});b.classList.add('on');}});
  document.querySelectorAll('.side a').forEach(function(a){a.onclick=function(){
    a.parentNode.querySelectorAll('a').forEach(function(x){x.classList.remove('on')});a.classList.add('on');}});
})();
</script>
$railjs
</body></html>""")


PANEL_FX = {
    1: ".spec{border-width:2px;box-shadow:none}",
    6: ".spec{border:2px solid #0e140b;box-shadow:none}",
    11: ".spec{border:2px solid #111;box-shadow:none}",
    24: ".spec{border:2px solid #000;box-shadow:none}",
    29: ".spec{border:2px solid #111;box-shadow:none}",
    40: ".spec{border:2px solid #000;box-shadow:none}",
}


RAILDATA = json.dumps([[f"{x['id']:02d}", x["cn"], SLUGS[x["id"]]] for x in STYLES],
                      ensure_ascii=False, separators=(",", ":"))


def main():
    print("component source ready:", len(BODY), "bytes markup,", len(CSS), "bytes css")
    return
    n = 0
    for d in STYLES:
        sid = d["id"]
        th = THEMES[sid]
        slug = SLUGS[sid]
        railfooter = (
            '<a class="railFoot" href="' + slug + '.html">← 返回本风格 demo</a>'
            '<a class="railFoot" href="../50-frontend-styles.html">← 返回速查表</a>'
            '<a class="railFoot dl" href="../assets/zips/style-' + slug + '.zip" download>⤓ 导出风格包</a>')
        out = TPL.substitute(
            no=f"{sid:02d}", cn=d["cn"], en=d["en"], slug=slug,
            bg=th["bg"], surface=th["surface"], ink=th["ink"], muted=th["muted"],
            line=th["line"], accent=th["accent"], on_accent=th["on_accent"],
            radius=th["radius"], cardborder=th["cardborder"], shadow=th["shadow"],
            btnborder=th["btnborder"], btnshadow=th["btnshadow"], btnradius=th["btnradius"],
            fonth=th["fonth"], fontk=th["fontk"], h1w=th["h1w"], navborder=th["navborder"],
            css=chr(10).join([CSS, th["raw"], XRAW.get(sid, ""), PANEL_FX.get(sid, "")]),
            body=BODY, nav=NAV, switch="",
            railcss=rail.RAIL_CSS,
            railhtml=rail.rail_html(railfooter),
            railjs=rail.rail_js(RAILDATA, slug),
        )
        io.open(os.path.join(OUT, "demos", slug + "-components.html"),
                "w", encoding="utf-8").write(out)
        n += 1
    print("component pages:", n)


if __name__ == "__main__":
    main()
