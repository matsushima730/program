// 共通の部品：要素の生成、時刻から見た目を決める関数、画面の枠（装置名・章・進捗バー）。
// 各場面は SCENES[id](ctx) で要素を組み、update(t) を返す。t は場面の頭からの秒。
// 時間は外から与える（アニメーションは使わない）ので、1コマずつ同じ絵が再現できる。
"use strict";
const SVGNS = "http://www.w3.org/2000/svg";
const clamp = (x, a = 0, b = 1) => Math.max(a, Math.min(b, x));
const ease = (x) => 1 - Math.pow(1 - clamp(x), 3);
const inout = (x) => { x = clamp(x); return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2; };
const P = (t, t0, d = 0.6) => ease((t - t0) / d);
const lerp = (a, b, p) => a + (b - a) * p;

function el(tag, parent, cls, style, html) {
  const e = document.createElement(tag);
  if (cls) e.className = cls;
  if (style) Object.assign(e.style, style);
  if (html !== undefined) e.innerHTML = html;
  if (parent) parent.appendChild(e);
  return e;
}
function div(parent, cls, style, html) { return el("div", parent, cls, style, html); }
function sv(tag, attrs, parent) {
  const e = document.createElementNS(SVGNS, tag);
  for (const k in attrs || {}) e.setAttribute(k, attrs[k]);
  if (parent) parent.appendChild(e);
  return e;
}
function icon(name, size, color, sw = 1.8) {
  const inner = (window.ICONS || {})[name];
  if (!inner) throw new Error("icon missing: " + name);
  return `<svg viewBox="0 0 24 24" width="${size}" height="${size}" fill="none" stroke="${color}" stroke-width="${sw}" stroke-linecap="round" stroke-linejoin="round">${inner}</svg>`;
}
function iconCircle(parent, name, x, y, r, bg, fg, sw = 1.7) {
  return div(parent, "icoc abs", { left: x - r + "px", top: y - r + "px", width: 2 * r + "px", height: 2 * r + "px", background: bg }, icon(name, r * 1.1, fg, sw));
}
function nl(s) { return String(s).replace(/\n/g, "<br>"); }
// 出し方：不透明度＋位置（dx, dy）＋拡大（s）
function show(e, p, o = {}) {
  const dy = o.dy === undefined ? 26 : o.dy, dx = o.dx || 0, s = o.s || 0;
  e.style.opacity = p;
  e.style.transform = `translate(${dx * (1 - p)}px, ${dy * (1 - p)}px) scale(${1 - s * (1 - p)})`;
  if (o.origin) e.style.transformOrigin = o.origin;
}
function showSvg(e, p, o = {}) {
  const dy = o.dy === undefined ? 20 : o.dy, dx = o.dx || 0;
  e.setAttribute("opacity", p);
  e.setAttribute("transform", `translate(${dx * (1 - p)}, ${dy * (1 - p)})`);
}
// 線を描き出す（stroke-dasharray）
function drawLine(e, p) {
  if (!e._len) { e._len = e.getTotalLength(); e.style.strokeDasharray = e._len; }
  e.style.strokeDashoffset = e._len * (1 - clamp(p));
}
// 経路に沿って動く粒
function along(path, u) { const L = path._len || (path._len = path.getTotalLength()); return path.getPointAtLength(((u % 1) + 1) % 1 * L); }
function arrowHead(parent, x, y, ang, size, color) {
  const a = ang * Math.PI / 180, s = size;
  const pts = [[x, y], [x - s * Math.cos(a) + s * 0.6 * Math.sin(a), y - s * Math.sin(a) - s * 0.6 * Math.cos(a)],
               [x - s * Math.cos(a) - s * 0.6 * Math.sin(a), y - s * Math.sin(a) + s * 0.6 * Math.cos(a)]];
  return sv("polygon", { points: pts.map(p => p.join(",")).join(" "), fill: color }, parent);
}
function heading(root, text) {
  const h = div(root, "heading", null, `${text}<span class="bar"></span>`);
  return h;
}
// 文の開始時刻 c(i)、文の長さ d(i)、文の途中 at(i, 割合)
function cueFns(cues) {
  const c = (i) => (cues[Math.min(i, cues.length - 1)] || { s: 0 }).s;
  const d = (i) => (cues[Math.min(i, cues.length - 1)] || { d: 3 }).d;
  const at = (i, f) => c(i) + d(i) * f;
  return { c, d, at };
}

let CURRENT = null;
window.SETUP = function (cfg) {
  // cfg: {scene, lang, dur, start, total, chapters, chapterNames, device, chrome, sceneIndex}
  document.documentElement.lang = cfg.lang;
  const root = document.getElementById("scene");
  root.innerHTML = "";
  const g = sv("svg", { class: "g", width: 1920, height: 1080, viewBox: "0 0 1920 1080" }, root);
  const fg = sv("svg", { class: "g", width: 1920, height: 1080, viewBox: "0 0 1920 1080" });  // カードの上に描く絵
  const ctx = Object.assign({ root, g, fg, T: cfg.scene.screen, cues: cfg.scene.cues }, cfg, cueFns(cfg.scene.cues));
  const builder = window.SCENES[cfg.scene.id];
  if (!builder) throw new Error("no scene " + cfg.scene.id);
  const update = builder(ctx);
  root.appendChild(fg);
  // 画面の枠
  document.getElementById("brandName").textContent = cfg.device;
  const ch = cfg.scene.chapter;
  document.getElementById("chapNum").textContent = ch ? String(ch).padStart(2, "0") + " / " + String(cfg.chapters.length).padStart(2, "0") : "";
  document.getElementById("chapName").textContent = ch ? cfg.chapters[ch - 1].name : "";
  const prog = document.getElementById("progress");
  prog.innerHTML = "";
  const segs = cfg.chapters.map((c) => {
    const s = div(prog, "seg", { flex: String(c.end - c.start) });
    return { c, fill: el("i", s) };
  });
  const chrome = document.getElementById("chrome");
  const hasChrome = ch !== 0;
  CURRENT = { update, dur: cfg.scene.dur, start: cfg.scene.start, segs, chrome, hasChrome, root, id: cfg.scene.id,
              prevChrome: cfg.prevChrome, nextChrome: cfg.nextChrome };
  return true;
};
window.RENDER = function (t) {
  const S = CURRENT;
  S.update(t);
  // 場面の出入り：中身だけ溶かす（枠は続けて出ている）
  const fin = 0.5, fout = 0.45;
  const a = Math.min(clamp(t / fin), clamp((S.dur - t) / fout));
  S.root.style.opacity = a;
  // 枠：表紙・結びの前後だけ溶かす
  let ca = S.hasChrome ? 1 : 0;
  if (S.hasChrome && !S.prevChrome) ca = Math.min(ca, clamp(t / 0.8));
  if (S.hasChrome && !S.nextChrome) ca = Math.min(ca, clamp((S.dur - t) / 0.6));
  S.chrome.style.opacity = ca;
  // 表紙の入りと結びの終わりは濃い緑から／へ（白い地を一瞬見せない）
  const stage = document.getElementById("stage");
  if (S.id === "s01_title") stage.style.background = t < S.dur / 2 ? "#0E2419" : "";
  if (S.id === "s18_closing") stage.style.background = t > S.dur / 2 ? "#0E2419" : "";
  const gt = S.start + t;
  for (const s of S.segs) s.fill.style.width = (clamp((gt - s.c.start) / (s.c.end - s.c.start)) * 100) + "%";
  return true;
};
window.SCENES = {};
