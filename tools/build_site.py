# -*- coding: utf-8 -*-
"""静态站点生成器：读 tools/site_data.py，产出 index.html / p/*.html / 404.html / assets/*。

用法：python3 tools/build_site.py   （在仓库根目录执行）
只依赖标准库。
"""
import html
import os
import re
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import site_data as D  # noqa: E402

GH = "https://github.com/ZhehaoTetsuhiro"
SITE = D.SITE_URL

# ------------------------------------------------------------------ 工具函数

def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def esc(s):
    return html.escape(s, quote=True)


def t(el_tag, zh, en, cls=None, extra="", html_mode=False):
    """生成一个双语叶子元素。html_mode=True 时用 innerHTML 注入（内容由我们控制）。"""
    cls_attr = f' class="{cls}"' if cls else ""
    html_attr = ' data-html="1"' if html_mode else ""
    return (f'<{el_tag}{cls_attr}{html_attr} data-zh="{esc(zh)}" data-en="{esc(en)}"{extra}>'
            f'{zh}</{el_tag}>')


def chips(pairs, cls="chip"):
    out = []
    for zh, en in pairs:
        out.append(f'<li class="{cls}">{t("span", zh, en)}</li>')
    return '<ul class="chip-row">' + "".join(out) + "</ul>"


# ------------------------------------------------------------------ 部件

def nav(base, active=""):
    links = [
        ("index.html#projects", "项目", "Projects", "projects"),
        ("index.html#about", "关于", "About", "about"),
        ("index.html#contact", "联系", "Contact", "contact"),
    ]
    items = []
    for href, zh, en, key in links:
        cls = ' class="is-active"' if active == key else ""
        items.append(f'<a href="{base}{href}"{cls}>{t("span", zh, en)}</a>')
    return f"""<header class="nav-wrap">
  <div class="nav glass">
    <a class="brand" href="{base}index.html">
      <span class="brand-mark">TH</span>
      <span class="brand-text">
        <b>{t("span", D.PROFILE["display_zh"], D.PROFILE["display_en"])}</b>
        <small>@{D.PROFILE['handle']}</small>
      </span>
    </a>
    <nav class="nav-links">{''.join(items)}</nav>
    <button id="lang-toggle" class="lang-toggle" type="button" aria-label="Switch language">EN</button>
  </div>
</header>"""


def footer(base):
    return f"""<footer class="footer glass">
  <p>{t("span",
        f"© 2026 {D.PROFILE['display_zh']}（{D.PROFILE['handle']}）· 本站由静态页面生成器构建，托管于 GitHub Pages",
        f"© 2026 {D.PROFILE['display_zh']} ({D.PROFILE['handle']}) · static site generated from a small Python script, hosted on GitHub Pages")}</p>
  <p class="footer-links">
    <a href="{base}index.html">{t("span", "首页", "Home")}</a>
    <a href="{GH}">{t("span", "GitHub", "GitHub")}</a>
    <a href="mailto:zhehaosdog@outlook.com">{t("span", "邮箱", "Email")}</a>
  </p>
</footer>"""


def contacts_block():
    out = []
    for c in D.PROFILE["contacts"]:
        inner = (f'<span class="contact-kind">{t("span", c["label_zh"], c["label_en"])}</span>'
                 f'<span class="contact-value">{esc(c["text"])}</span>')
        if c["url"]:
            out.append(f'<a class="contact glass" href="{c["url"]}">{inner}</a>')
        else:
            out.append(f'<div class="contact glass">{inner}</div>')
    return '<div class="contact-grid">' + "".join(out) + "</div>"


def card(p):
    """项目卡片（首页用）。"""
    tagline = strip_tags(p["tagline_zh"]), strip_tags(p["tagline_en"])
    tags = "".join(f'<li class="chip chip-sm">{t("span", a, b)}</li>' for a, b in p["tags"][:3])
    return f"""<a class="card glass" href="p/{p['slug']}.html" style="--accent:{p['accent']}">
  <span class="glyph">{p['glyph']}</span>
  <h3>{t("span", p["name_zh"], p["name_en"])}</h3>
  <p class="card-sub">{t("span", p["sub_zh"], p["sub_en"])}</p>
  <p class="card-tagline">{t("span", tagline[0], tagline[1])}</p>
  <ul class="chip-row">{tags}<li class="chip chip-sm chip-star" data-repo="{p['repo']}">★</li></ul>
  <span class="card-go">{t("span", "查看详情 →", "Details →")}</span>
</a>"""


def other_projects(base, current_slug):
    items = [p for p in D.PROJECTS if p["slug"] != current_slug]
    links = "".join(
        f'<a class="mini glass" href="{base}p/{p["slug"]}.html" style="--accent:{p["accent"]}">'
        f'<span class="glyph glyph-sm">{p["glyph"]}</span>'
        f'{t("span", p["name_zh"], p["name_en"])}</a>' for p in items)
    return f"""<section class="section">
  <h2 class="section-title">{t("span", "其它项目", "Other projects")}</h2>
  <div class="mini-grid">{links}</div>
</section>"""


# ------------------------------------------------------------------ 页面

def page(title_zh, title_en, desc_zh, desc_en, body, base=""):
    return f"""<!doctype html>
<html lang="zh-CN" data-lang="zh" data-title-zh="{esc(title_zh)}" data-title-en="{esc(title_en)}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title_zh)}</title>
<meta name="description" content="{esc(desc_zh)}">
<meta property="og:title" content="{esc(title_zh)}">
<meta property="og:description" content="{esc(desc_zh)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/">
<link rel="icon" href="{base}favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="{base}assets/style.css">
</head>
<body>
<div class="bg" aria-hidden="true"><span class="orb orb-1"></span><span class="orb orb-2"></span><span class="orb orb-3"></span></div>
{body}
<script src="{base}assets/i18n.js"></script>
</body>
</html>
"""


def build_index():
    p = D.PROFILE
    hero = f"""<section class="hero glass">
  <img class="avatar" src="{p['avatar']}" alt="avatar" width="132" height="132">
  <h1>{t("span", p["display_zh"], p["display_en"])}</h1>
  <p class="handle">@{p['handle']} · {t("span", p["location_zh"], p["location_en"])}</p>
  <p class="tagline">{t("span", p["tagline_zh"], p["tagline_en"])}</p>
  <div class="hero-actions">
    <a class="btn btn-primary" href="#projects">{t("span", "看项目", "Projects")}</a>
    <a class="btn" href="{GH}">{t("span", "GitHub 主页", "GitHub profile")}</a>
    <a class="btn" href="mailto:zhehaosdog@outlook.com">{t("span", "写邮件", "Email me")}</a>
  </div>
</section>"""

    projects = f"""<section class="section" id="projects">
  <h2 class="section-title">{t("span", "项目", "Projects")}
    <small>{t("span", f"{len(D.PROJECTS)} 个公开项目", f"{len(D.PROJECTS)} public projects")}</small></h2>
  <div class="card-grid">
    {''.join(card(pr) for pr in D.PROJECTS)}
  </div>
</section>"""

    bio = "".join(f"<p>{t('span', zh, en)}</p>" for zh, en in zip(p["bio_zh"], p["bio_en"]))
    stack = chips([("Go", "Go"), ("Lean 4", "Lean 4"), ("MicroPython", "MicroPython"),
                   ("Rust", "Rust"), ("LaTeX / TeX", "LaTeX / TeX"), ("CUDA / cuFFT", "CUDA / cuFFT"),
                   ("Docker", "Docker"), ("HTML / CSS / JS", "HTML / CSS / JS")])
    about = f"""<section class="section" id="about">
  <h2 class="section-title">{t("span", "关于", "About")}</h2>
  <div class="about glass">
    {bio}
    <p>{t("span", "常用的家伙：", "Tools of the trade:")}</p>
    {stack}
    <p class="muted">{t("span",
      "除上面这些公开项目，还有若干闭源项目在开发中（Lean 4 移植、光编程范式探索、另一个波动光学引擎等）。",
      "Beyond the public projects above, a few closed-source ones are in progress (a Lean 4 port, an exploration of optical computing as a programming paradigm, and another wave-optics engine).")}</p>
  </div>
</section>"""

    contact = f"""<section class="section" id="contact">
  <h2 class="section-title">{t("span", "联系", "Contact")}</h2>
  {contacts_block()}
</section>"""

    body = (nav("") + '<main class="wrap">' + hero + projects + about + contact + "</main>" + footer(""))
    return page(f"{p['display_zh']}（{p['handle']}）· 个人主页",
                f"{p['handle']} · home",
                f"{p['display_zh']}（{p['handle']}）的项目主页：{p['tagline_zh']}",
                f"Projects by {p['handle']}: {p['tagline_en']}",
                body)


def build_project(pr):
    base = "../"
    links = [
        (f"{GH}/{pr['repo']}", "源码仓库", "Source repository"),
        (f"{GH}/{pr['repo']}/releases", "Releases", "Releases"),
        (f"{GH}/{pr['repo']}/issues", "问题反馈", "Issues"),
        (f"{GH}/{pr['repo']}#readme", "完整文档", "Full documentation"),
    ]
    link_html = "".join(f'<a class="btn btn-sm" href="{u}">{t("span", a, b)}</a>' for u, a, b in links)

    facts = "".join(
        f'<tr><th>{t("span", a, b)}</th><td>{t("span", c, d, html_mode=True)}</td></tr>'
        for a, b, c, d in pr["facts"])

    detail = []
    for sec in pr["detail"]:
        h = t("h2", sec["h"][0], sec["h"][1])
        paras = "".join(f"<p>{t('span', a, b, html_mode=True)}</p>" for a, b in sec["p"])
        detail.append(f'<div class="detail-block">{h}{paras}</div>')

    dl = pr["downloads"]
    if dl["assets"]:
        rows = "".join(
            f'<tr><td><a href="{GH}/{pr["repo"]}/releases/download/{dl["version"]}/{name}">'
            f'<code>{esc(name)}</code></a></td><td>{t("span", note, note)}</td></tr>'
            for name, note in dl["assets"])
        assets_html = f"""<table class="dl-table">
      <thead><tr><th>{t("span", "文件", "File")}</th><th>{t("span", "平台 / 说明", "Platform / notes")}</th></tr></thead>
      <tbody>{rows}</tbody></table>
      <p class="muted">{t("span", "全部版本：", "All releases:")}
        <a href="{GH}/{pr['repo']}/releases">{GH}/{pr['repo']}/releases</a></p>"""
    else:
        assets_html = f"""<p class="muted">{t("span",
          "本项目没有预编译二进制发布，直接用下面的命令从源码起步。",
          "This project has no prebuilt binary release — start from source with the commands below.")}</p>"""

    cmds = "".join(f'<pre class="code"><code>{esc(c)}</code></pre>' for c in dl["cmds"])

    download = f"""<div class="detail-block" id="download">
    <h2>{t("span", "下载与安装", "Download & install")}</h2>
    <p>{t("span", dl["note_zh"], dl["note_en"], html_mode=True)}</p>
    {assets_html}
    {cmds}
  </div>"""

    head = f"""<section class="proj-hero glass" style="--accent:{pr['accent']}">
  <a class="back" href="{base}index.html">{t("span", "← 全部项目", "← All projects")}</a>
  <span class="glyph glyph-lg">{pr['glyph']}</span>
  <h1>{t("span", pr["name_zh"], pr["name_en"])}</h1>
  <p class="proj-sub">{t("span", pr["sub_zh"], pr["sub_en"])}</p>
  <p class="tagline">{t("span", pr["tagline_zh"], pr["tagline_en"], html_mode=True)}</p>
  {chips(pr["tags"])}
  <div class="hero-actions">{link_html}</div>
</section>"""

    body = (nav(base, "projects") + '<main class="wrap">' + head +
            f'<section class="section"><h2 class="section-title">{t("span", "速览", "At a glance")}</h2>'
            f'<table class="facts glass">{facts}</table></section>' +
            f'<section class="section"><h2 class="section-title">{t("span", "详细介绍", "In detail")}</h2>'
            f'<div class="detail glass">{"".join(detail)}{download}</div></section>' +
            other_projects(base, pr["slug"]) + "</main>" + footer(base))

    return page(f"{pr['name_zh']} — {strip_tags(pr['sub_zh'])}",
                f"{pr['name_en']} — {strip_tags(pr['sub_en'])}",
                f"{strip_tags(pr['tagline_zh'])}",
                f"{strip_tags(pr['tagline_en'])}",
                body, base=base)


AVATAR_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" width="128" height="128" role="img" aria-label="avatar">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#eaf6ff"/>
      <stop offset="0.55" stop-color="#bfe1ff"/>
      <stop offset="1" stop-color="#8fc7ff"/>
    </linearGradient>
    <radialGradient id="core" cx="0.5" cy="0.5" r="0.5">
      <stop offset="0" stop-color="#ffffff" stop-opacity="0.95"/>
      <stop offset="0.45" stop-color="#cfe9ff" stop-opacity="0.55"/>
      <stop offset="1" stop-color="#0a7cff" stop-opacity="0"/>
    </radialGradient>
  </defs>
  <rect width="128" height="128" rx="34" fill="url(#bg)"/>
  <circle cx="64" cy="64" r="54" fill="url(#core)"/>
  <g fill="none" stroke="#0a7cff" stroke-opacity="0.55">
    <circle cx="64" cy="64" r="7"  stroke-width="2.6" stroke-opacity="0.9"/>
    <circle cx="64" cy="64" r="15" stroke-width="2.2" stroke-opacity="0.62"/>
    <circle cx="64" cy="64" r="24" stroke-width="1.9" stroke-opacity="0.42"/>
    <circle cx="64" cy="64" r="34" stroke-width="1.6" stroke-opacity="0.28"/>
    <circle cx="64" cy="64" r="45" stroke-width="1.3" stroke-opacity="0.18"/>
    <circle cx="64" cy="64" r="56" stroke-width="1.1" stroke-opacity="0.12"/>
  </g>
  <g stroke="#ffffff" stroke-opacity="0.75" stroke-width="1.4" stroke-linecap="round">
    <path d="M8 64 H120"/>
    <path d="M64 8 V120"/>
  </g>
  <text x="64" y="76" text-anchor="middle" font-family="ui-monospace, SFMono-Regular, Menlo, monospace"
        font-size="30" font-weight="700" fill="#08325f" opacity="0.92">TT</text>
</svg>
"""

FAVICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64" width="64" height="64">
  <rect width="64" height="64" rx="16" fill="#cbe7ff"/>
  <g fill="none" stroke="#0a7cff">
    <circle cx="32" cy="32" r="5" stroke-width="3" stroke-opacity="0.9"/>
    <circle cx="32" cy="32" r="12" stroke-width="2.4" stroke-opacity="0.6"/>
    <circle cx="32" cy="32" r="20" stroke-width="2" stroke-opacity="0.38"/>
    <circle cx="32" cy="32" r="28" stroke-width="1.6" stroke-opacity="0.2"/>
  </g>
</svg>
"""

SITE_README = f"""# {D.PROFILE['display_zh']} · GitHub Pages

个人主页与项目页面的源材料。站点是**静态页面**，直接由仓库根目录的 HTML/CSS/JS 提供，
GitHub Pages 从 `main` 分支根目录发布。

- 线上地址：{SITE}
- 首页：`index.html`（个人简介 + 项目卡片）
- 项目页：`p/<slug>.html`（速览 / 详细介绍 / 下载与安装）
- 样式与脚本：`assets/`

## 修改内容

所有文字（中英双语）、项目信息、下载链接都集中在 `tools/site_data.py`；
改完后重新生成：

```bash
python3 tools/build_site.py     # 需要 Python 3，无第三方依赖
git add -A && git commit -m "更新站点" && git push
```

## 增加一个新项目

1. 在 `tools/site_data.py` 的 `PROJECTS` 里追加一项（slug / repo / 一句话 / 标签 / 详细介绍 / 下载）；
2. 跑 `python3 tools/build_site.py`；
3. 提交推送 —— 首页卡片与 `p/<slug>.html` 会一起生成。

语言切换靠元素上的 `data-zh` / `data-en` 属性 + `assets/i18n.js`，无需构建步骤。

## 换头像

把新头像放进 `tools/assets/avatar.jpg`（或改 `tools/site_data.py` 里 `PROFILE["avatar"]`
的路径），然后重新生成。当前头像是从 GitHub 账号头像取的：`https://github.com/ZhehaoTetsuhiro.png?size=512`。
"""


def main():
    written = []

    def out(rel, content):
        path = os.path.join(ROOT, rel)
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        written.append(rel)

    out("index.html", build_index())
    for pr in D.PROJECTS:
        out(f"p/{pr['slug']}.html", build_project(pr))

    out("404.html", page("页面没找到", "Page not found", "404", "404",
                         nav("") + """<main class="wrap"><section class="hero glass">
  <h1>404</h1>
  <p class="tagline">""" +
                         t("span", "这个页面不存在了。回首页看看项目吧。",
                           "This page does not exist. Head back home and browse the projects.") +
                         """</p>
  <div class="hero-actions"><a class="btn btn-primary" href="index.html">""" +
                         t("span", "回首页", "Back home") + "</a></div></section></main>" + footer("")))

    out("favicon.svg", FAVICON_SVG)
    out(".nojekyll", "")
    out("README.md", SITE_README)

    # 静态资源（CSS / JS）从 tools/assets 复制过来
    src_assets = os.path.join(HERE, "assets")
    if os.path.isdir(src_assets):
        dst = os.path.join(ROOT, "assets")
        os.makedirs(dst, exist_ok=True)
        for name in sorted(os.listdir(src_assets)):
            shutil.copy2(os.path.join(src_assets, name), os.path.join(dst, name))
            written.append(f"assets/{name}")

    print(f"生成 {len(written)} 个文件：")
    for w in written:
        print("  " + w)


if __name__ == "__main__":
    main()
