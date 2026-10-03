# 犬忠铭天 · GitHub Pages

个人主页与项目页面的源材料。站点是**静态页面**，直接由仓库根目录的 HTML/CSS/JS 提供，
GitHub Pages 从 `main` 分支根目录发布。

- 线上地址：https://zhehaotetsuhiro.github.io
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
