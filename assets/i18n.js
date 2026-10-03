/* 双语切换 + GitHub 星标数（可选增强，失败静默） */
(function () {
  "use strict";

  var STORE = "tt-lang";
  var LABEL = { zh: "EN", en: "中文" };

  function apply(lang) {
    if (lang !== "en" && lang !== "zh") lang = "zh";
    var root = document.documentElement;
    root.lang = lang === "zh" ? "zh-CN" : "en";
    root.setAttribute("data-lang", lang);

    document.querySelectorAll("[data-zh]").forEach(function (el) {
      var v = el.getAttribute(lang === "zh" ? "data-zh" : "data-en");
      if (v === null) return;
      if (el.hasAttribute("data-html")) el.innerHTML = v;
      else el.textContent = v;
    });

    var tz = root.getAttribute("data-title-zh");
    var te = root.getAttribute("data-title-en");
    document.title = lang === "zh" ? tz : te;

    var btn = document.getElementById("lang-toggle");
    if (btn) {
      btn.textContent = LABEL[lang];
      btn.setAttribute("aria-label", lang === "zh" ? "Switch to English" : "切换到中文");
    }
    try { localStorage.setItem(STORE, lang); } catch (e) {}
  }

  var saved = null;
  try { saved = localStorage.getItem(STORE); } catch (e) {}
  if (!saved) saved = (navigator.language || "zh").toLowerCase().indexOf("zh") === 0 ? "zh" : "en";
  apply(saved);

  document.addEventListener("click", function (ev) {
    var btn = ev.target.closest && ev.target.closest("#lang-toggle");
    if (!btn) return;
    apply(document.documentElement.getAttribute("data-lang") === "zh" ? "en" : "zh");
  });

  /* 星标数：一次 API 调用，失败就保留静态占位符 */
  var targets = document.querySelectorAll(".chip-star[data-repo]");
  if (!targets.length || !window.fetch) return;
  fetch("https://api.github.com/users/ZhehaoTetsuhiro/repos?per_page=100&type=public", {
    headers: { Accept: "application/vnd.github+json" }
  })
    .then(function (r) { return r.ok ? r.json() : null; })
    .then(function (list) {
      if (!Array.isArray(list)) return;
      var byName = {};
      list.forEach(function (r) { byName[r.name] = r.stargazers_count; });
      targets.forEach(function (el) {
        var n = byName[el.getAttribute("data-repo")];
        if (typeof n === "number") el.setAttribute("data-stars", n > 0 ? "★ " + n : "★ 0");
      });
    })
    .catch(function () {});
})();
