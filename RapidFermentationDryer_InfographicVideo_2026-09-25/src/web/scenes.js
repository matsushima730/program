// 18場面の図解。文言は content.py（timeline の screen）から受け取り、ここには書かない。
// 各場面は出す時刻を文の頭（c(i)）や文の途中（at(i, 割合)）に合わせる。
"use strict";
const C = {
  ink: "#1E2A24", muted: "#5C6B63", line: "#C9D2CB", card: "#FFFFFF", bg: "#F4F6F1",
  green: "#2E6B4A", greenD: "#1D4A33", greenL: "#DCEADF", amber: "#D38B22", amberL: "#F7E7CB",
  soil: "#8A5A3C", soilL: "#EEDFD3", water: "#2B7BB0", waterL: "#D7E8F4", red: "#B5513A", redL: "#F4DDD5",
  gray: "#87928B", grayL: "#E6EAE6",
};
const TAU = Math.PI * 2;

// 立ちのぼる粒（泡・蒸気・においの印）。u は 0→1 の周期位置
function risers(g, n, make) { const a = []; for (let i = 0; i < n; i++) a.push(make(i)); return a; }

// ---------------------------------------------------------------- 01 表紙
SCENES.s01_title = (ctx) => {
  const { root, T, c, at, dur, lang, chapters } = ctx;
  const bg = div(root, "abs", { left: "0", top: "0", width: "1920px", height: "1080px", overflow: "hidden" });
  const img = el("img", bg, null, { position: "absolute", left: "0", top: "-470px", width: "1920px", height: "1920px", transformOrigin: "70% 60%" });
  img.src = "img/field.png";
  div(bg, "abs", { left: "0", top: "0", width: "1920px", height: "1080px",
    background: "linear-gradient(90deg, rgba(16,42,29,.95) 0%, rgba(16,42,29,.84) 45%, rgba(16,42,29,.30) 100%)" });
  const box = div(root, "abs", { left: "140px", top: "250px", width: "1400px" });
  const kick = div(box, null, { fontSize: "32px", fontWeight: 700, color: C.amber, letterSpacing: ".06em" }, T.kicker);
  const title = div(box, null, { fontSize: lang === "ja" ? "104px" : "84px", fontWeight: 700, color: "#fff", lineHeight: 1.12, marginTop: "18px", maxWidth: "1300px" }, T.title);
  const rule = div(box, null, { width: "140px", height: "7px", background: C.amber, borderRadius: "4px", margin: "34px 0 30px" });
  const sub = div(box, null, { fontSize: "44px", color: "#fff", lineHeight: 1.4 }, T.sub);
  const note = div(root, "abs", { left: "140px", top: "1000px", fontSize: "20px", color: "rgba(255,255,255,.7)" }, T.note);
  // 目次（3文目で出す）
  const toc = div(root, "abs", { left: "140px", top: "690px", width: "1640px", display: "flex", gap: "18px" });
  const items = chapters.map((ch, i) => {
    const it = div(toc, null, { flex: "1", background: "rgba(255,255,255,.10)", border: "1px solid rgba(255,255,255,.28)", borderRadius: "18px", padding: "22px 24px", minHeight: "130px" });
    div(it, null, { fontSize: "30px", fontWeight: 700, color: C.amber }, String(i + 1).padStart(2, "0"));
    div(it, null, { fontSize: lang === "ja" ? "34px" : "29px", fontWeight: 700, color: "#fff", marginTop: "10px", lineHeight: 1.25 }, ch.name);
    return it;
  });
  return (t) => {
    img.style.transform = `scale(${1 + 0.07 * t / dur})`;
    show(kick, P(t, 0.3, 0.8));
    show(title, P(t, 0.6, 0.9));
    rule.style.width = 140 * P(t, 1.1, 0.8) + "px";
    show(sub, P(t, 1.3, 0.8));
    note.style.opacity = P(t, 1.6, 0.8) * (1 - P(t, c(2) - 0.6, 0.5));
    // 目次が出るとき、表題を上へ寄せる
    const m = P(t, c(2) - 0.5, 0.9);
    box.style.transform = `translateY(${-110 * m}px)`;
    items.forEach((it, i) => show(it, P(t, c(2) + 0.25 + i * 0.35, 0.6), { dy: 30 }));
  };
};

// ---------------------------------------------------------------- 02 4つのリスク
SCENES.s02_risks = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const cx = 960, cy = 555;
  const grp = sv("g", {}, g);
  sv("circle", { cx, cy, r: 200, fill: C.soilL }, grp);
  sv("path", { d: `M790 ${cy + 85} Q 840 ${cy - 40} 925 ${cy - 58} Q 990 ${cy - 90} 1060 ${cy - 40} Q 1120 ${cy} 1130 ${cy + 85} Z`, fill: C.soil }, grp);
  const scraps = [[880, cy + 20, C.green], [955, cy - 30, C.amber], [1030, cy + 10, C.green], [990, cy + 45, "#C96E3A"], [920, cy + 55, C.amber], [1065, cy + 50, "#6E8B3D"]];
  scraps.forEach(([x, y, f], i) => sv("ellipse", { cx: x, cy: y, rx: 20, ry: 11, fill: f, transform: `rotate(${i * 37 - 40} ${x} ${y})` }, grp));
  sv("line", { x1: 770, y1: cy + 88, x2: 1150, y2: cy + 88, stroke: C.soil, "stroke-width": 4, "stroke-linecap": "round" }, grp);
  const drops = risers(grp, 4, (i) => sv("path", { d: "M0 -14 C 6 -4 9 2 9 6 A 9 9 0 0 1 -9 6 C -9 2 -6 -4 0 -14 Z", fill: C.water }, grp));
  const waves = risers(grp, 3, (i) => sv("path", { d: "", fill: "none", stroke: C.gray, "stroke-width": 4, "stroke-linecap": "round" }, grp));
  const lab = div(root, "abs center", { left: `${cx - 200}px`, top: `${cy + 215}px`, width: "400px", fontSize: "32px", fontWeight: 700, lineHeight: 1.3 }, nl(T.center));
  const pos = [[120, 250], [1280, 250], [120, 650], [1280, 650]];
  const cards = T.cards.map((k, i) => {
    const [x, y] = pos[i];
    const cd = div(root, "card", { left: x + "px", top: y + "px", width: "520px", height: "250px" });
    iconCircle(cd, k.icon, 70, 72, 44, C.redL, C.red);
    div(cd, "abs t-title", { left: "134px", top: "0", height: "144px", width: "360px", display: "flex", alignItems: "center", fontSize: k.title.length > 12 ? "34px" : "40px", lineHeight: 1.1 }, k.title);
    div(cd, "abs", { left: "36px", top: "136px", width: "456px", fontSize: "28px", lineHeight: 1.4, color: C.ink }, k.text);
    return cd;
  });
  const links = pos.map(([x, y], i) => {
    const x2 = i % 2 === 0 ? x + 520 : x, y2 = y + 125;
    const ang = Math.atan2(y2 - cy, x2 - cx);
    return sv("line", { x1: cx + 205 * Math.cos(ang), y1: cy + 205 * Math.sin(ang), x2, y2, stroke: C.red, "stroke-width": 3, "stroke-dasharray": "8 10", opacity: 0 }, g);
  });
  const times = [c(1), at(1, 0.45), c(2), c(3)];
  return (t) => {
    show(h, P(t, 0.2));
    showSvg(grp, P(t, 0.4, 0.8), { dy: 0 });
    lab.style.opacity = P(t, 0.6, 0.8);
    drops.forEach((e, i) => { const u = (t * 0.45 + i / 4) % 1; e.setAttribute("transform", `translate(${840 + i * 80} ${cy + 100 + u * 70})`); e.setAttribute("opacity", (1 - u) * P(t, times[2], 0.6) * 0.9); });
    waves.forEach((e, i) => {
      const u = (t * 0.35 + i / 3) % 1, x0 = 900 + i * 60, y0 = cy - 80 - u * 110;
      let d = `M${x0} ${y0}`; for (let k = 1; k <= 8; k++) d += ` L${x0 + Math.sin(k * 0.9 + t * 3) * 10} ${y0 - k * 7}`;
      e.setAttribute("d", d); e.setAttribute("opacity", Math.sin(u * Math.PI) * P(t, times[0], 0.6));
    });
    cards.forEach((cd, i) => show(cd, P(t, times[i] - 0.15, 0.7), { dx: i % 2 === 0 ? -30 : 30, dy: 0 }));
    links.forEach((l, i) => l.setAttribute("opacity", P(t, times[i], 0.6)));
  };
};

// ---------------------------------------------------------------- 03 メタンは酸欠から
SCENES.s03_methane = (ctx) => {
  const { root, fg: g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const panels = [{ x: 120, side: T.left, col: C.red, colL: C.redL }, { x: 990, side: T.right, col: C.green, colL: C.greenL }];
  const P0 = panels.map((p, k) => {
    const cd = div(root, "card", { left: p.x + "px", top: "235px", width: "810px", height: "610px" });
    const tt = div(cd, "abs t-title", { left: "40px", top: "30px", fontSize: "36px", display: "flex", alignItems: "center", gap: "14px" },
      `<span style="width:16px;height:16px;border-radius:50%;background:${p.col};display:inline-block"></span>${p.side.title}`);
    const steps = p.side.steps.map((s, i) => {
      const last = i === 2;
      return div(cd, "abs", { left: "40px", top: `${358 + i * 78}px`, width: "730px", height: "64px", borderRadius: "14px", display: "flex", alignItems: "center", gap: "16px", padding: "0 20px",
        background: last ? p.colL : C.bg, fontSize: "30px", fontWeight: last ? 700 : 400, color: last ? p.col : C.ink },
        `<span style="font-weight:700;color:${p.col};font-size:26px;min-width:28px">${i + 1}</span>${s}`);
    });
    return { cd, steps };
  });
  // 左：積み上げた山の断面。上面だけに空気、内側からメタンの泡
  const L = sv("g", {}, g), R = sv("g", {}, g);
  sv("path", { d: "M220 560 Q 300 390 525 370 Q 750 390 830 560 Z", fill: C.soil }, L);
  sv("path", { d: "M300 555 Q 360 450 525 438 Q 690 450 750 555 Z", fill: "#6B432C" }, L);
  sv("line", { x1: 190, y1: 560, x2: 860, y2: 560, stroke: C.soil, "stroke-width": 4 }, L);
  const o2L = [[330, 395], [420, 368], [640, 370], [725, 392], [525, 350]].map(([x, y]) => sv("circle", { cx: x, cy: y, r: 9, fill: C.water, opacity: 0.8 }, L));
  const mkBubble = (grp, label, col) => { const b = sv("g", {}, grp); sv("circle", { r: 26, fill: "#fff", stroke: col, "stroke-width": 3 }, b); const tx = sv("text", { "text-anchor": "middle", y: 8, "font-size": 20, "font-weight": 700, fill: col }, b); tx.textContent = label; return b; };
  const ch4 = [0, 1, 2].map((i) => mkBubble(L, "CH₄", C.red));
  // 右：回る槽の中に空気が行き渡る
  sv("rect", { x: 1180, y: 390, width: 430, height: 170, rx: 85, fill: C.greenL, stroke: C.green, "stroke-width": 4 }, R);
  sv("path", { d: "M1225 520 Q 1395 470 1565 520 L 1565 525 Q 1565 548 1545 552 L 1245 552 Q 1225 548 1225 525 Z", fill: C.soil }, R);
  const rot = sv("g", {}, R);
  sv("path", { d: "M1395 405 A 70 70 0 1 1 1330 450", fill: "none", stroke: C.green, "stroke-width": 5, "stroke-linecap": "round" }, rot);
  arrowHead(rot, 1330, 452, 125, 16, C.green);
  const o2R = [0, 1, 2, 3, 4, 5, 6].map(() => sv("circle", { r: 9, fill: C.water, opacity: 0.85 }, R));
  const outs = [mkBubble(R, "CO₂", C.gray), mkBubble(R, "H₂O", C.water), mkBubble(R, "CO₂", C.gray)];
  const banner = div(root, "abs center", { left: "120px", top: "870px", width: "1680px", height: "96px", borderRadius: "18px", background: C.greenD, color: "#fff", fontSize: "32px", fontWeight: 700, padding: "0 40px", lineHeight: 1.3 }, T.banner);
  return (t) => {
    show(h, P(t, 0.2));
    show(P0[0].cd, P(t, c(0) - 0.2, 0.7), { dx: -30, dy: 0 });
    showSvg(L, P(t, c(0), 0.7), { dy: 0 });
    P0[0].steps.forEach((s, i) => show(s, P(t, [at(0, 0.2), at(1, 0.1), at(1, 0.55)][i], 0.6), { dy: 14 }));
    ch4.forEach((b, i) => { const u = (t * 0.28 + i / 3) % 1; b.setAttribute("transform", `translate(${440 + i * 85} ${510 - u * 160})`); b.setAttribute("opacity", Math.sin(u * Math.PI) * P(t, at(1, 0.4), 0.8)); });
    show(P0[1].cd, P(t, c(2) - 0.2, 0.7), { dx: 30, dy: 0 });
    showSvg(R, P(t, c(2), 0.7), { dy: 0 });
    P0[1].steps.forEach((s, i) => show(s, P(t, [at(2, 0.15), at(2, 0.4), at(2, 0.7)][i], 0.6), { dy: 14 }));
    rot.setAttribute("transform", `rotate(${t * 90} 1395 475)`);
    o2R.forEach((e, i) => { const a = t * 1.3 + i * TAU / 7; e.setAttribute("cx", 1395 + 170 * Math.cos(a)); e.setAttribute("cy", 475 + 55 * Math.sin(a)); });
    outs.forEach((b, i) => { const u = (t * 0.3 + i / 3) % 1; b.setAttribute("transform", `translate(${1680 + (i - 1) * 45} ${520 - u * 170})`); b.setAttribute("opacity", Math.sin(u * Math.PI) * P(t, at(2, 0.7), 0.8)); });
    show(banner, P(t, c(3) - 0.1, 0.7), { dy: 20 });
  };
};

// ---------------------------------------------------------------- 04 全体像
SCENES.s04_overview = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const xs = [120, 567, 1013, 1460], y = 270, w = 340, hh = 290;
  const nodes = T.nodes.map((n, i) => {
    const main = i === 1;
    const cd = div(root, "card", { left: xs[i] + "px", top: y + "px", width: w + "px", height: hh + "px", background: main ? C.green : C.card });
    iconCircle(cd, n.icon, w / 2, 66, 44, main ? "rgba(255,255,255,.16)" : C.greenL, main ? "#fff" : C.green);
    div(cd, "abs center t-title", { left: "16px", top: "124px", width: (w - 32) + "px", fontSize: main ? "30px" : "36px", color: main ? "#fff" : C.ink, lineHeight: 1.2 }, n.title);
    div(cd, "abs center", { left: "20px", top: "176px", width: (w - 40) + "px", fontSize: main ? "24px" : "25px", color: main ? "rgba(255,255,255,.9)" : C.muted, lineHeight: 1.35 }, n.text);
    return cd;
  });
  const arrows = [0, 1, 2].map((i) => {
    const x1 = xs[i] + w + 12, x2 = xs[i + 1] - 14, yy = y + hh / 2;
    const gg = sv("g", { opacity: 0 }, g);
    const p = sv("path", { d: `M${x1} ${yy} L${x2 - 10} ${yy}`, stroke: C.soil, "stroke-width": 6, fill: "none", "stroke-linecap": "round" }, gg);
    arrowHead(gg, x2, yy, 0, 20, C.soil);
    const dots = [0, 1, 2].map(() => sv("circle", { r: 7, fill: C.amber }, gg));
    return { gg, p, dots };
  });
  // 蒸気と排気の枝
  const bx = [300, 760], by = 710;
  const branch = sv("g", { opacity: 0 }, g);
  const dx = xs[1] + w / 2;
  const bp = bx.map((x) => sv("path", { d: `M${dx} ${y + hh} V ${by - 60} H ${x + 210} V ${by - 8}`, stroke: C.water, "stroke-width": 4, "stroke-dasharray": "10 10", fill: "none" }, branch));
  const bdots = [0, 1].map((k) => [0, 1, 2].map(() => sv("circle", { r: 6, fill: k === 0 ? C.water : C.gray }, branch)));
  const bb = [T.vapor, T.air].map((b, i) => {
    const cd = div(root, "card", { left: bx[i] + "px", top: by + "px", width: "420px", height: "160px", background: i === 0 ? C.waterL : C.grayL, boxShadow: "none" });
    iconCircle(cd, i === 0 ? "droplet" : "wind", 62, 80, 38, "#fff", i === 0 ? C.water : C.gray);
    div(cd, "abs t-title", { left: "118px", top: "30px", width: "240px", fontSize: "30px" }, b.title);
    div(cd, "abs", { left: "118px", top: "74px", width: "290px", fontSize: "24px", lineHeight: 1.35, color: C.ink }, b.text);
    return cd;
  });
  const tn = [c(1), at(1, 0.3), c(2), at(2, 0.6)];
  return (t) => {
    show(h, P(t, 0.2));
    nodes.forEach((n, i) => show(n, P(t, tn[i] - 0.1, 0.7), { dy: 30 }));
    arrows.forEach((a, i) => {
      const p = P(t, tn[i + 1] - 0.3, 0.6); a.gg.setAttribute("opacity", p);
      a.dots.forEach((dd, k) => { const pt = along(a.p, t * 0.55 + k / 3); dd.setAttribute("cx", pt.x); dd.setAttribute("cy", pt.y); });
    });
    const pb = P(t, c(3) - 0.2, 0.7); branch.setAttribute("opacity", pb);
    bp.forEach((p, k) => { p.style.strokeDashoffset = -t * 30; bdots[k].forEach((dd, j) => { const pt = along(p, t * 0.35 + j / 3); dd.setAttribute("cx", pt.x); dd.setAttribute("cy", pt.y); }); });
    bb.forEach((b, i) => show(b, P(t, c(3) + i * 0.9, 0.7)));
  };
};

// ---------------------------------------------------------------- 05 2つのはたらき
SCENES.s05_two_actions = (ctx) => {
  const { root, fg: g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const mk = (x, col, colL, s) => {
    const cd = div(root, "card", { left: x + "px", top: "240px", width: "780px", height: "470px" });
    const col2 = div(cd, "abs", { left: "400px", top: "0", height: "470px", width: "356px", display: "flex", flexDirection: "column", justifyContent: "center", gap: "26px" });
    div(col2, "t-title", { fontSize: s.title.length > 16 ? "34px" : "38px", color: col, lineHeight: 1.2 }, s.title);
    div(col2, null, { fontSize: "30px", lineHeight: 1.5 }, s.text);
    div(cd, "abs", { left: "30px", top: "30px", width: "340px", height: "410px", borderRadius: "16px", background: colL });
    return cd;
  };
  const A = mk(120, C.water, C.waterL, T.a), B = mk(1020, C.green, C.greenL, T.b);
  // 左の絵：槽と圧力計、上がる蒸気
  const LA = sv("g", {}, g);
  sv("rect", { x: 185, y: 470, width: 250, height: 170, rx: 26, fill: "#fff", stroke: C.water, "stroke-width": 5 }, LA);
  sv("path", { d: "M192 580 Q 310 555 428 580 L 428 612 Q 428 633 408 633 L 212 633 Q 192 633 192 612 Z", fill: C.soil }, LA);
  sv("rect", { x: 292, y: 400, width: 36, height: 72, fill: "#fff", stroke: C.water, "stroke-width": 5 }, LA);
  sv("circle", { cx: 400, cy: 360, r: 44, fill: "#fff", stroke: C.water, "stroke-width": 5 }, LA);
  const needle = sv("line", { x1: 400, y1: 360, x2: 400, y2: 326, stroke: C.red, "stroke-width": 5, "stroke-linecap": "round" }, LA);
  sv("circle", { cx: 400, cy: 360, r: 6, fill: C.water }, LA);
  const vap = [0, 1, 2, 3, 4].map(() => sv("circle", { r: 9, fill: "#fff", stroke: C.water, "stroke-width": 3 }, LA));
  // 右の絵：有機物の粒と微生物
  const RB = sv("g", {}, g);
  const blobs = [[1150, 470, 46], [1270, 560, 38], [1170, 610, 34], [1280, 420, 30]].map(([x, y, r]) => ({ e: sv("circle", { cx: x, cy: y, r, fill: C.soil }, RB), x, y, r }));
  const microbes = [0, 1, 2, 3, 4, 5, 6, 7].map((i) => { const m = sv("g", {}, RB); sv("ellipse", { rx: 14, ry: 9, fill: C.green }, m); sv("circle", { cx: 4, cy: -2, r: 2.5, fill: "#fff" }, m); return m; });
  const plus = div(root, "icoc abs", { left: "916px", top: "431px", width: "88px", height: "88px", background: C.amber, color: "#fff", fontSize: "60px", fontWeight: 700 }, "+");
  const res = div(root, "abs", { left: "120px", top: "760px", width: "1680px", height: "150px" });
  const f = div(res, "card", { left: "0", top: "0", width: "600px", height: "150px", background: C.soilL, boxShadow: "none" });
  iconCircle(f, "droplets", 80, 75, 44, "#fff", C.water);
  div(f, "abs t-title", { left: "150px", top: "50px", fontSize: "36px" }, T.from);
  const ar = div(res, "abs center", { left: "640px", top: "40px", width: "400px", height: "70px" },
    `<svg width="400" height="70"><line x1="10" y1="35" x2="360" y2="35" stroke="${C.soil}" stroke-width="8" stroke-linecap="round"/><polygon points="392,35 356,12 356,58" fill="${C.soil}"/></svg>`);
  const to = div(res, "card", { left: "1080px", top: "0", width: "600px", height: "150px", background: C.amberL, boxShadow: "none" });
  iconCircle(to, "package", 80, 75, 44, "#fff", C.amber);
  div(to, "abs t-title", { left: "150px", top: "50px", fontSize: "36px" }, T.to);
  return (t) => {
    show(h, P(t, 0.2));
    const pa = P(t, c(1) - 0.2, 0.7), pb = P(t, c(2) - 0.2, 0.7);
    show(A, pa, { dx: -30, dy: 0 }); showSvg(LA, pa, { dy: 0, dx: -30 });
    const low = P(t, at(1, 0.35), 1.5);
    const ang = lerp(-10, -140, low) * Math.PI / 180;
    needle.setAttribute("x2", 400 + 34 * Math.cos(ang)); needle.setAttribute("y2", 360 + 34 * Math.sin(ang));
    vap.forEach((e, i) => { const u = (t * 0.5 + i / 5) % 1; const x = 250 + i * 34 + Math.sin(t * 2 + i) * 6; e.setAttribute("cx", x); e.setAttribute("cy", 570 - u * 80); e.setAttribute("opacity", Math.sin(u * Math.PI) * low); });
    show(B, pb, { dx: 30, dy: 0 }); showSvg(RB, pb, { dy: 0, dx: 30 });
    const act = P(t, at(2, 0.5), 3);
    blobs.forEach((b) => b.e.setAttribute("r", b.r * (1 - 0.35 * act)));
    microbes.forEach((m, i) => { const a = t * (0.6 + (i % 3) * 0.15) + i * TAU / 8; m.setAttribute("transform", `translate(${1215 + 115 * Math.cos(a)} ${515 + 115 * Math.sin(a)}) rotate(${a * 57 + 90})`); m.setAttribute("opacity", 0.4 + 0.6 * P(t, at(2, 0.3), 1)); });
    show(plus, P(t, c(2) - 0.4, 0.5), { dy: 0, s: 0.5 });
    show(res, P(t, c(3), 0.8), { dy: 30 });
  };
};

// ---------------------------------------------------------------- 06 減圧と沸点
SCENES.s06_boiling = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const ox = 260, oy = 860, W = 860, H = 540;
  const f = (u) => 0.08 + 0.84 * (1 - Math.pow(1 - u, 2.3));
  const X = (u) => ox + W * u, Y = (v) => oy - H * v;
  const ax = sv("g", {}, g);
  sv("line", { x1: ox, y1: oy, x2: ox + W + 30, y2: oy, stroke: C.ink, "stroke-width": 4 }, ax);
  sv("line", { x1: ox, y1: oy, x2: ox, y2: oy - H - 40, stroke: C.ink, "stroke-width": 4 }, ax);
  arrowHead(ax, ox + W + 44, oy, 0, 18, C.ink); arrowHead(ax, ox, oy - H - 54, -90, 18, C.ink);
  const lab = (x, y, s, o = {}) => div(root, "abs", Object.assign({ left: x + "px", top: y + "px", fontSize: "26px", color: C.muted, whiteSpace: "nowrap" }, o), s);
  const axl = [lab(ox + 24, oy - H - 70, T.y, { fontSize: "30px", fontWeight: 700, color: C.ink }), lab(ox - 90, oy - H - 12, T.high), lab(ox - 90, oy - 40, T.low),
    lab(ox + W - 260, oy + 22, T.x, { fontSize: "30px", fontWeight: 700, color: C.ink, width: "300px", textAlign: "right" }), lab(ox + 10, oy + 22, T.low)];
  let d = ""; for (let i = 0; i <= 60; i++) { const u = i / 60; d += (i ? " L" : "M") + X(u).toFixed(1) + " " + Y(f(u)).toFixed(1); }
  const curve = sv("path", { d, fill: "none", stroke: C.water, "stroke-width": 7, "stroke-linecap": "round" }, g);
  const pts = [{ u: 0.88, key: "p_atm", col: C.ink }, { u: 0.55, key: "p_mtn", col: C.green }, { u: 0.14, key: "p_vac", col: C.water }].map((p) => {
    const gg = sv("g", { opacity: 0 }, g);
    const x = X(p.u), y = Y(f(p.u));
    sv("line", { x1: x, y1: y, x2: x, y2: oy, stroke: p.col, "stroke-width": 2.5, "stroke-dasharray": "6 8" }, gg);
    sv("line", { x1: ox, y1: y, x2: x, y2: y, stroke: p.col, "stroke-width": 2.5, "stroke-dasharray": "6 8" }, gg);
    const ring = sv("circle", { cx: x, cy: y, r: 22, fill: "none", stroke: p.col, "stroke-width": 3 }, gg);
    sv("circle", { cx: x, cy: y, r: 12, fill: p.col }, gg);
    return Object.assign(p, { gg, x, y, ring });
  });
  const tl = [];
  tl.push(div(root, "abs", { left: pts[0].x - 470 + "px", top: pts[0].y - 92 + "px", width: "440px", height: "74px", display: "flex", alignItems: "flex-end", justifyContent: "flex-end", textAlign: "right", fontSize: "27px", fontWeight: 700, lineHeight: 1.3 }, T.p_atm));
  tl.push(div(root, "abs", { left: pts[1].x - 24 - 360 + "px", top: pts[1].y - 62 + "px", width: "360px", fontSize: "28px", fontWeight: 700, color: C.green, display: "flex", gap: "10px", alignItems: "center", justifyContent: "flex-end" }, icon("mountain", 40, C.green, 2) + `<span>${T.p_mtn}</span>`));
  tl.push(div(root, "abs", { left: pts[2].x + 36 + "px", top: pts[2].y - 20 + "px", width: "380px", fontSize: "30px", fontWeight: 700, color: C.water, lineHeight: 1.3 }, T.p_vac));
  const note = lab(1270, 710, T.note, { fontSize: "24px", border: `2px solid ${C.line}`, borderRadius: "10px", padding: "4px 14px" });
  const call = div(root, "card", { left: "1270px", top: "360px", width: "530px", height: "320px", background: C.greenD });
  iconCircle(call, "temperature-minus", 90, 90, 52, "rgba(255,255,255,.14)", "#fff");
  div(call, "abs t-title", { left: "44px", top: "166px", width: "450px", fontSize: "36px", color: "#fff", lineHeight: 1.35 }, T.callout);
  return (t) => {
    show(h, P(t, 0.2));
    ax.setAttribute("opacity", P(t, 0.5, 0.6)); axl.forEach((e) => (e.style.opacity = P(t, 0.7, 0.6)));
    drawLine(curve, P(t, c(1) - 0.2, 2.2));
    const tp = [at(1, 0.3), c(2), at(1, 0.75)];
    pts.forEach((p, i) => { const q = P(t, tp[i], 0.6); p.gg.setAttribute("opacity", q); p.ring.setAttribute("r", 20 + 6 * Math.sin(t * 3 + i)); tl[i].style.opacity = q; });
    note.style.opacity = P(t, 1.0, 0.6);
    show(call, P(t, c(3) - 0.1, 0.8), { dx: 40, dy: 0 });
  };
};

// ---------------------------------------------------------------- 07 装置の断面
SCENES.s07_cutaway = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const X0 = 380, X1 = 1540, Y0 = 410, Y1 = 710, R = (Y1 - Y0) / 2, CY = (Y0 + Y1) / 2;
  const cap = (x0, y0, x1, y1) => { const r = (y1 - y0) / 2; return `M${x0 + r} ${y0} H${x1 - r} A${r} ${r} 0 0 1 ${x1 - r} ${y1} H${x0 + r} A${r} ${r} 0 0 1 ${x0 + r} ${y0} Z`; };
  const V = sv("g", {}, g);
  const defs = sv("defs", {}, g);
  const cp = sv("clipPath", { id: "inner" }, defs); sv("path", { d: cap(X0, Y0, X1, Y1) }, cp);
  const jacket = sv("path", { d: cap(X0 - 26, Y0 - 26, X1 + 26, Y1 + 26), fill: C.amberL, stroke: C.amber, "stroke-width": 4 }, V);
  sv("path", { d: cap(X0, Y0, X1, Y1), fill: "#fff", stroke: C.greenD, "stroke-width": 5 }, V);
  const inner = sv("g", { "clip-path": "url(#inner)" }, V);
  const mat = sv("path", { d: "", fill: C.soil, opacity: 0.9 }, inner);
  const helixB = sv("path", { d: "", fill: "none", stroke: "#7FA78F", "stroke-width": 9, "stroke-linecap": "round" }, inner);
  const spokes = sv("path", { d: "", fill: "none", stroke: C.greenD, "stroke-width": 4 }, inner);
  const helixF = sv("path", { d: "", fill: "none", stroke: C.green, "stroke-width": 11, "stroke-linecap": "round" }, inner);
  const vap = [0, 1, 2, 3, 4, 5].map(() => sv("circle", { r: 10, fill: "#fff", stroke: C.water, "stroke-width": 3 }, V));
  // 中空の回転軸
  sv("rect", { x: X0 - 90, y: CY - 13, width: X1 - X0 + 180, height: 26, rx: 6, fill: "#9AA5A0" }, V);
  sv("rect", { x: X0 - 90, y: CY - 5, width: X1 - X0 + 180, height: 10, fill: "#D5DCD8" }, V);
  sv("rect", { x: X1 + 90, y: CY - 44, width: 90, height: 88, rx: 12, fill: "#6F7B75" }, V);
  // 投入口・排出口・蒸気の出口
  sv("path", { d: `M${X0 + 70} ${Y0 - 150} L${X0 + 230} ${Y0 - 150} L${X0 + 190} ${Y0 - 26} L${X0 + 110} ${Y0 - 26} Z`, fill: C.grayL, stroke: C.gray, "stroke-width": 4 }, V);
  sv("path", { d: `M${X1 - 170} ${Y1 + 26} L${X1 - 90} ${Y1 + 26} L${X1 - 90} ${Y1 + 96} L${X1 - 170} ${Y1 + 96} Z`, fill: C.grayL, stroke: C.gray, "stroke-width": 4 }, V);
  const pipe = sv("path", { d: `M1000 ${Y0 - 26} V ${Y0 - 130} H 1230`, fill: "none", stroke: C.water, "stroke-width": 26, "stroke-linejoin": "round" }, V);
  sv("path", { d: `M1000 ${Y0 - 26} V ${Y0 - 130} H 1230`, fill: "none", stroke: "#fff", "stroke-width": 14, "stroke-linejoin": "round" }, V);
  arrowHead(V, 1270, Y0 - 130, 0, 24, C.water);
  const heat = []; for (let i = 0; i < 12; i++) { const x = X0 + 100 + i * 85; heat.push(sv("path", { d: `M${x - 12} ${Y0 - 6} l12 -12 l12 12 M${x - 12} ${Y1 + 18} l12 12 l12 -12`, fill: "none", stroke: C.red, "stroke-width": 4, "stroke-linecap": "round", opacity: 0 }, V)); }
  const lab = (x, y, s, o = {}) => div(root, "abs", Object.assign({ left: x + "px", top: y + "px", fontSize: "28px", fontWeight: 700 }, o), s);
  const labs = [lab(X0 - 190, Y0 - 150, T.inlet, { width: "240px", textAlign: "right" }), lab(X1 - 60, Y1 + 50, T.outlet), lab(1060, Y0 - 196, T.vapor, { color: C.water })];
  const note = div(root, "abs", { left: "1300px", top: "232px", fontSize: "24px", color: C.muted, border: `2px solid ${C.line}`, borderRadius: "10px", padding: "4px 14px" }, T.note);
  const mpos = [[X0 + 40, Y0 - 44], [X0 - 60, CY - 46], [760, CY - 120], [960, Y0 - 150]];
  const marks = mpos.map(([x, y], i) => div(root, "icoc abs", { left: x - 26 + "px", top: y - 26 + "px", width: "52px", height: "52px", background: C.amber, color: "#fff", fontSize: "30px", fontWeight: 700 }, String(i + 1)));
  const legend = T.callouts.map((s, i) => div(root, "abs", { left: `${120 + (i % 2) * 860}px`, top: `${838 + Math.floor(i / 2) * 62}px`, width: "830px", display: "flex", gap: "14px", alignItems: "flex-start", fontSize: "26px", lineHeight: 1.35 },
    `<span class="icoc" style="flex:0 0 44px;height:44px;background:${C.amber};color:#fff;font-weight:700;font-size:26px">${i + 1}</span><span style="padding-top:5px">${s}</span>`));
  const k = TAU / 330, A = 112;
  return (t) => {
    show(h, P(t, 0.2));
    showSvg(V, P(t, c(0) - 0.2, 0.8), { dy: 0 });
    labs.forEach((e) => (e.style.opacity = P(t, c(0) + 0.4, 0.6)));
    note.style.opacity = P(t, c(0) + 0.8, 0.6);
    const w = t * 2.2;
    let dm = `M${X0} ${Y1 + 10} L${X0} ${CY + 30}`; for (let x = X0; x <= X1; x += 20) dm += ` L${x} ${CY + 30 + 10 * Math.sin(x * 0.02 + t * 2.5)}`; dm += ` L${X1} ${Y1 + 10} Z`;
    mat.setAttribute("d", dm);
    let f1 = "", f2 = "", sp = "";
    for (let x = X0 + 30; x <= X1 - 30; x += 8) { const s = Math.sin(k * (x - X0) + w); const y1 = CY - A * s, y2 = CY + A * s; const front = Math.cos(k * (x - X0) + w) > 0; f1 += (x === X0 + 30 ? "M" : "L") + x + " " + y1.toFixed(1) + " "; f2 += (x === X0 + 30 ? "M" : "L") + x + " " + y2.toFixed(1) + " "; }
    for (let x = X0 + 70; x <= X1 - 60; x += 82) { const s = Math.sin(k * (x - X0) + w); sp += `M${x} ${CY} L${x} ${(CY - A * s).toFixed(1)} M${x} ${CY} L${x} ${(CY + A * s).toFixed(1)} `; }
    helixF.setAttribute("d", f1); helixB.setAttribute("d", f2); spokes.setAttribute("d", sp);
    const hp = P(t, c(1), 0.8);
    heat.forEach((e, i) => e.setAttribute("opacity", hp * (0.45 + 0.55 * Math.max(0, Math.sin(t * 3 - i * 0.6)))));
    jacket.setAttribute("fill", hp > 0.5 ? "#F9DDB0" : C.amberL);
    const vp = P(t, c(3) - 0.2, 0.8);
    vap.forEach((e, i) => { const u = (t * 0.45 + i / 6) % 1; const sx = 820 + i * 55; const x = lerp(sx, 1000, clamp(u * 1.3)); const y = lerp(CY + 10, Y0 - 90, u); e.setAttribute("cx", x); e.setAttribute("cy", y); e.setAttribute("opacity", vp * Math.sin(u * Math.PI)); });
    const mt = [c(1), at(1, 0.55), c(2), c(3)];
    marks.forEach((m, i) => show(m, P(t, mt[i] - 0.1, 0.5), { dy: 0, s: 0.6 }));
    legend.forEach((l, i) => show(l, P(t, mt[i], 0.6), { dy: 16 }));
  };
};

// ---------------------------------------------------------------- 08 3段階の運転
SCENES.s08_three_stages = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const cols = [C.water, C.green, C.water], colsL = [C.waterL, C.greenL, C.waterL];
  const xs = [120, 695, 1270], W = 530;
  const cards = T.stages.map((s, i) => {
    const cd = div(root, "card", { left: xs[i] + "px", top: "240px", width: W + "px", height: "290px" });
    div(cd, "icoc abs", { left: "34px", top: "34px", width: "72px", height: "72px", background: cols[i], color: "#fff", fontSize: "40px", fontWeight: 700 }, s.no);
    div(cd, "abs t-title", { left: "126px", top: "46px", width: "380px", fontSize: "40px" }, s.title);
    div(cd, "abs", { left: "36px", top: "140px", width: "460px", fontSize: "30px", lineHeight: 1.45 }, s.text);
    return cd;
  });
  const chev = [0, 1].map((i) => div(root, "abs", { left: xs[i] + W + 4 + "px", top: "355px" }, `<svg width="40" height="60"><polyline points="8,6 32,30 8,54" fill="none" stroke="${C.gray}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/></svg>`));
  const modes = T.stages.map((s, i) => div(root, "abs center t-title", { left: xs[i] + "px", top: "552px", width: W + "px", height: "54px", borderRadius: "12px", background: colsL[i], color: cols[i], fontSize: "26px" }, s.mode));
  const ch = sv("g", {}, g);
  const y0 = 690, y1 = 900;
  sv("line", { x1: 120, y1: y1, x2: 1800, y2: y1, stroke: C.line, "stroke-width": 3 }, ch);
  [xs[1] - 22, xs[2] - 22].forEach((x) => sv("line", { x1: x, y1: y0 - 10, x2: x, y2: y1, stroke: C.line, "stroke-width": 2, "stroke-dasharray": "6 8" }, ch));
  const pts = []; const seg = [[120, 695, 0.0, 0.55], [695, 1270, 0.55, 0.72], [1270, 1800, 0.72, 0.96]];
  seg.forEach(([a, b, v0, v1], k) => { for (let i = 0; i <= 30; i++) { const u = i / 30; const x = lerp(a, b, u); const e = k === 1 ? u : 1 - Math.pow(1 - u, 1.8); pts.push([x, lerp(y0 + (y1 - y0 - 20) * v0, y0 + (y1 - y0 - 20) * v1, e)]); } });
  const line = sv("path", { d: "M" + pts.map((p) => p[0].toFixed(1) + " " + p[1].toFixed(1)).join(" L"), fill: "none", stroke: C.soil, "stroke-width": 7, "stroke-linecap": "round" }, ch);
  const head = sv("circle", { r: 12, fill: C.soil }, ch);
  const mlab = div(root, "abs", { left: "140px", top: "636px", fontSize: "24px", color: C.muted, display: "flex", gap: "8px", alignItems: "center" }, icon("droplet", 28, C.soil, 2) + `<span>${T.moisture}</span>`);
  const note = div(root, "abs", { left: "120px", top: "930px", width: "1680px", fontSize: "26px", color: C.muted, textAlign: "center" }, T.note);
  const ts = [c(1), c(2), c(3)];
  return (t) => {
    show(h, P(t, 0.2));
    cards.forEach((cd, i) => show(cd, P(t, ts[i] - 0.15, 0.7), { dy: 30 }));
    chev.forEach((e, i) => (e.style.opacity = P(t, ts[i + 1] - 0.3, 0.5)));
    modes.forEach((e, i) => show(e, P(t, ts[i] + 0.3, 0.6), { dy: 10 }));
    ch.setAttribute("opacity", P(t, c(1), 0.6)); mlab.style.opacity = P(t, c(1), 0.6);
    const prog = ts.reduce((acc, s, i) => acc + P(t, s + 0.2, 2.2), 0) / 3;
    drawLine(line, prog);
    const pt = line.getPointAtLength(Math.max(0.01, line._len * prog)); head.setAttribute("cx", pt.x); head.setAttribute("cy", pt.y);
    head.setAttribute("r", 11 + 3 * Math.sin(t * 4));
    show(note, P(t, c(4) - 0.1, 0.7), { dy: 14 });
  };
};

// ---------------------------------------------------------------- 09 水の回収
SCENES.s09_water = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const Y = 470;
  const V = sv("g", {}, g);
  sv("rect", { x: 120, y: Y - 90, width: 280, height: 180, rx: 90, fill: "#fff", stroke: C.greenD, "stroke-width": 5 }, V);
  sv("path", { d: `M140 ${Y + 20} Q 260 ${Y - 5} 380 ${Y + 20} L 380 ${Y + 30} Q 370 ${Y + 82} 300 ${Y + 84} L 200 ${Y + 84} Q 130 ${Y + 82} 140 ${Y + 30} Z`, fill: C.soil }, V);
  const vl = div(root, "abs center t-title", { left: "120px", top: `${Y + 110}px`, width: "280px", fontSize: "30px" }, T.vessel);
  const card = (x, w, s, ic, bg, fg) => { const cd = div(root, "card", { left: x + "px", top: Y - 125 + "px", width: w + "px", height: "250px" }); iconCircle(cd, ic, w / 2, 58, 38, bg, fg); const col = div(cd, "abs", { left: "14px", top: "104px", width: w - 28 + "px", height: "136px", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", textAlign: "center", gap: "6px" }); div(col, "t-title", { fontSize: s.title.length > 12 ? "26px" : "30px", lineHeight: 1.15 }, s.title); div(col, null, { fontSize: "23px", color: C.muted, lineHeight: 1.3 }, s.text); return cd; };
  const cond = card(560, 340, T.cond, "snowflake", C.waterL, C.water);
  const sep = card(1060, 320, T.sep, "tornado", C.waterL, C.water);
  const pump = card(1540, 260, T.pump, "wind", C.grayL, C.gray);
  const mkPath = (d, col, dash) => sv("path", { d, fill: "none", stroke: col, "stroke-width": 5, "stroke-dasharray": dash || "none", opacity: 0 }, g);
  const pA = mkPath(`M405 ${Y} H 545`, C.gray, "10 10"), pB = mkPath(`M905 ${Y} H 1045`, C.water), pC = mkPath(`M1220 ${Y + 120} V 700`, C.water), pD = mkPath(`M1385 ${Y} H 1525`, C.gray, "10 10");
  const steamLab = div(root, "abs center t-title", { left: "405px", top: `${Y - 70}px`, width: "140px", fontSize: "26px", color: C.gray }, T.steam);
  const puffs = [0, 1, 2].map(() => sv("circle", { r: 12, fill: "#fff", stroke: C.gray, "stroke-width": 3 }, g));
  const drops = (n) => [...Array(n)].map(() => sv("path", { d: "M0 -12 C 5 -3 8 2 8 5 A 8 8 0 0 1 -8 5 C -8 2 -5 -3 0 -12 Z", fill: C.water }, g));
  const dB = drops(3), dC = drops(3);
  const airs = [0, 1, 2].map(() => sv("circle", { r: 8, fill: C.gray }, g));
  const tank = sv("g", {}, g);
  sv("rect", { x: 1090, y: 700, width: 260, height: 180, rx: 20, fill: "#fff", stroke: C.water, "stroke-width": 5 }, tank);
  const level = sv("rect", { x: 1095, y: 800, width: 250, height: 75, rx: 16, fill: C.water, opacity: 0.8 }, tank);
  const tl = div(root, "abs t-title", { left: "1380px", top: "760px", fontSize: "32px", color: C.water, display: "flex", gap: "10px", alignItems: "center" }, icon("droplet", 40, C.water, 2) + `<span>${T.water}</span>`);
  const note = div(root, "abs", { left: "120px", top: "925px", width: "1680px", fontSize: "26px", color: C.muted, textAlign: "center" }, T.note);
  const put = (e, p) => { e.setAttribute("transform", `translate(${p.x} ${p.y})`); };
  return (t) => {
    show(h, P(t, 0.2));
    const t1 = c(1) - 0.2, t2 = at(1, 0.4), t3 = c(2), t4 = at(2, 0.55);
    showSvg(V, P(t, c(0), 0.7), { dy: 0 }); vl.style.opacity = P(t, c(0), 0.7);
    const pa = P(t, t1, 0.6); pA.setAttribute("opacity", pa); steamLab.style.opacity = pa; pA.style.strokeDashoffset = -t * 30;
    puffs.forEach((e, i) => { const u = (t * 0.6 + i / 3) % 1; const p = along(pA, u); e.setAttribute("cx", p.x); e.setAttribute("cy", p.y - 16 * Math.sin(u * Math.PI)); e.setAttribute("r", 8 + 8 * u); e.setAttribute("opacity", pa * Math.sin(u * Math.PI)); });
    show(cond, P(t, t2 - 0.3, 0.7));
    const pb = P(t, t2 + 0.4, 0.6); pB.setAttribute("opacity", pb);
    dB.forEach((e, i) => { const u = (t * 0.6 + i / 3) % 1; put(e, along(pB, u)); e.setAttribute("opacity", pb * Math.sin(u * Math.PI)); });
    show(sep, P(t, t3 - 0.1, 0.7));
    const pc = P(t, t4, 0.6); pC.setAttribute("opacity", pc); tank.setAttribute("opacity", pc); tl.style.opacity = pc;
    dC.forEach((e, i) => { const u = (t * 0.7 + i / 3) % 1; put(e, along(pC, u)); e.setAttribute("opacity", pc * Math.sin(u * Math.PI)); });
    const lv = 40 + 70 * clamp((t - t4) / 12); level.setAttribute("y", 875 - lv); level.setAttribute("height", lv);
    show(pump, P(t, t4 + 0.8, 0.7));
    const pd = P(t, t4 + 1.0, 0.6); pD.setAttribute("opacity", pd); pD.style.strokeDashoffset = -t * 30;
    airs.forEach((e, i) => { const u = (t * 0.6 + i / 3) % 1; const p = along(pD, u); e.setAttribute("cx", p.x); e.setAttribute("cy", p.y); e.setAttribute("opacity", pd * Math.sin(u * Math.PI)); });
    show(note, P(t, c(3), 0.7), { dy: 14 });
  };
};

// ---------------------------------------------------------------- 10 におい対策
SCENES.s10_odor = (ctx) => {
  const { root, g, fg, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const xs = T.steps.map((_, i) => 120 + i * 344), W = 300, Y = 320;
  const steps = T.steps.map((s, i) => {
    const cd = div(root, "card", { left: xs[i] + "px", top: Y + "px", width: W + "px", height: "200px" });
    iconCircle(cd, s.icon, W / 2, 62, 40, i === 0 ? C.greenL : C.waterL, i === 0 ? C.green : C.water);
    div(cd, "abs center t-title", { left: "12px", top: "118px", width: W - 24 + "px", fontSize: "28px", lineHeight: 1.25 }, s.title);
    return cd;
  });
  const arr = [0, 1, 2, 3].map((i) => div(root, "abs", { left: xs[i] + W + 6 + "px", top: Y + 80 + "px" }, `<svg width="34" height="40"><polyline points="6,4 26,20 6,36" fill="none" stroke="${C.gray}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/></svg>`));
  const wave = sv("path", { d: "", fill: "none", stroke: "#8B6BA8", "stroke-width": 5, "stroke-linecap": "round" }, g);
  const wl = div(root, "abs", { left: "120px", top: "228px", fontSize: "24px", fontWeight: 700, color: "#8B6BA8" }, T.odor);
  const cmp = [[120, T.compare_a, T.compare_a_text, C.red], [990, T.compare_b, T.compare_b_text, C.green]].map(([x, tt, tx, col], i) => {
    const cd = div(root, "card", { left: x + "px", top: "580px", width: "810px", height: "330px" });
    div(cd, "abs t-title", { left: "36px", top: "28px", fontSize: "32px", color: col }, tt);
    div(cd, "abs", { left: "430px", top: "110px", width: "360px", fontSize: "27px", lineHeight: 1.45 }, tx);
    return cd;
  });
  const A = sv("g", {}, fg), B = sv("g", {}, fg);
  sv("path", { d: "M170 860 Q 230 740 330 730 Q 430 740 490 860 Z", fill: C.soil }, A);
  const ripA = [0, 1, 2].map(() => sv("path", { d: "", fill: "none", stroke: "#8B6BA8", "stroke-width": 4 }, A));
  sv("rect", { x: 1040, y: 740, width: 250, height: 120, rx: 60, fill: C.greenL, stroke: C.green, "stroke-width": 4 }, B);
  sv("path", { d: "M1165 740 V 690 H 1330 V 740", fill: "none", stroke: C.green, "stroke-width": 8 }, B);
  sv("rect", { x: 1300, y: 740, width: 70, height: 110, rx: 8, fill: "#fff", stroke: C.green, "stroke-width": 4 }, B);
  sv("path", { d: "M1310 770 H 1360 M1310 795 H 1360 M1310 820 H 1360", stroke: C.green, "stroke-width": 3 }, B);
  const ripB = [0, 1, 2].map(() => sv("circle", { r: 10, fill: "none", stroke: "#8B6BA8", "stroke-width": 3 }, B));
  const ts = [c(1), at(2, 0.05), at(2, 0.3), at(2, 0.55), at(2, 0.8)];
  return (t) => {
    show(h, P(t, 0.2));
    steps.forEach((s, i) => show(s, P(t, ts[i] - 0.1, 0.6), { dy: 24 }));
    arr.forEach((a, i) => (a.style.opacity = P(t, ts[i + 1] - 0.3, 0.4)));
    const shown = ts.reduce((n, s) => n + (t > s ? 1 : 0), 0);
    const xEnd = 120 + Math.min(5, shown + P(t, ts[Math.min(4, shown)], 1)) * 344 - 44;
    let d = "M120 278"; for (let x = 120; x <= Math.max(121, xEnd); x += 6) { const amp = 24 * (1 - (x - 120) / 1700) + 2; d += ` L${x} ${(278 + amp * Math.sin(x * 0.045 - t * 5)).toFixed(1)}`; }
    wave.setAttribute("d", d); wave.setAttribute("opacity", P(t, c(1), 0.6)); wl.style.opacity = P(t, c(1), 0.6);
    const pc = P(t, c(3) - 0.2, 0.7);
    cmp.forEach((cd, i) => show(cd, pc, { dy: 30 })); A.setAttribute("opacity", pc); B.setAttribute("opacity", pc);
    ripA.forEach((e, i) => { const u = (t * 0.4 + i / 3) % 1; const r = 60 + u * 130; e.setAttribute("d", `M${330 - r} 850 A ${r} ${r * 0.8} 0 0 1 ${330 + r} 850`); e.setAttribute("opacity", (1 - u) * 0.9); });
    ripB.forEach((e, i) => { const u = (t * 0.5 + i / 3) % 1; e.setAttribute("cx", 1100 + i * 60); e.setAttribute("cy", 800); e.setAttribute("r", 6 + u * 22); e.setAttribute("opacity", (1 - u) * 0.9); });
  };
};

// ---------------------------------------------------------------- 11 3つの出口
SCENES.s11_outlets = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const inp = div(root, "card center t-title", { left: "150px", top: "290px", width: "290px", height: "520px", background: C.soil, color: "#fff", fontSize: "36px", lineHeight: 1.35 }, nl(T.input));
  const defs = sv("defs", {}, g);
  const cols = [[C.amberL, C.amber, "package"], [C.waterL, C.water, "droplet"], [C.grayL, C.gray, "wind"]];
  const oy = [270, 470, 670], ih = [[330, 450], [490, 610], [650, 770]];
  const bands = T.outs.map((o, i) => {
    const [a, b] = ih[i], y0 = oy[i] + 20, y1 = oy[i] + 140;
    const cp = sv("clipPath", { id: "cl" + i }, defs); const r = sv("rect", { x: 440, y: 0, width: 0, height: 1080 }, cp);
    const d = `M440 ${a} C 760 ${a} 760 ${y0} 1080 ${y0} L1080 ${y1} C 760 ${y1} 760 ${b} 440 ${b} Z`;
    const band = sv("path", { d, fill: cols[i][0], stroke: cols[i][1], "stroke-width": 3, "clip-path": `url(#cl${i})` }, g);
    const mid = sv("path", { d: `M440 ${(a + b) / 2} C 760 ${(a + b) / 2} 760 ${(y0 + y1) / 2} 1080 ${(y0 + y1) / 2}`, fill: "none", stroke: "none" }, g);
    const dots = [0, 1, 2, 3].map(() => sv("circle", { r: 8, fill: cols[i][1] }, g));
    const cd = div(root, "card", { left: "1080px", top: oy[i] + "px", width: "430px", height: "160px" });
    iconCircle(cd, cols[i][2], 68, 80, 40, cols[i][0], cols[i][1]);
    const col = div(cd, "abs", { left: "128px", top: "0", width: "290px", height: "160px", display: "flex", flexDirection: "column", justifyContent: "center", gap: "6px" });
    div(col, "t-title", { fontSize: "30px", lineHeight: 1.15 }, o.title);
    div(col, null, { fontSize: "23px", color: C.muted, lineHeight: 1.3 }, o.text);
    return { r, band, mid, dots, cd };
  });
  const chk = div(root, "card", { left: "1545px", top: "290px", width: "255px", height: "520px", background: C.greenD });
  iconCircle(chk, "clipboard-check", 130, 90, 50, "rgba(255,255,255,.14)", "#fff");
  div(chk, "abs t-title", { left: "26px", top: "170px", width: "210px", fontSize: "30px", color: "#fff", lineHeight: 1.45 }, T.check);
  const note = div(root, "abs", { left: "120px", top: "860px", width: "1680px", fontSize: "26px", color: C.muted, textAlign: "center" }, T.note);
  const tb = [at(1, 0.15), at(1, 0.45), at(1, 0.75)];
  return (t) => {
    show(h, P(t, 0.2));
    show(inp, P(t, c(0), 0.7), { dx: -30, dy: 0 });
    bands.forEach((b, i) => {
      const p = P(t, tb[i] - 0.3, 1.0); b.r.setAttribute("width", 640 * p);
      b.dots.forEach((dd, k) => { const u = (t * 0.35 + k / 4) % 1; const pt = along(b.mid, u); dd.setAttribute("cx", pt.x); dd.setAttribute("cy", pt.y); dd.setAttribute("opacity", P(t, tb[i] + 0.6, 0.5) * Math.sin(u * Math.PI)); });
      show(b.cd, P(t, tb[i] + 0.3, 0.6), { dx: 30, dy: 0 });
    });
    show(note, P(t, c(2) - 0.1, 0.6), { dy: 12 });
    show(chk, P(t, c(3) - 0.1, 0.7), { dx: 30, dy: 0 });
  };
};

// ---------------------------------------------------------------- 12 運転監視
SCENES.s12_monitor = (ctx) => {
  const { root, fg: g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const cols = [C.red, C.water, C.water, "#8B6BA8", C.amber];
  const base = [0.55, 0.3, 0.62, 0.28, 0.66];
  const gs = T.gauges.map((name, i) => {
    const cx = 288 + i * 336, cy = 440, r = 108;
    const cd = div(root, "card", { left: cx - 150 + "px", top: "250px", width: "300px", height: "400px" });
    const G = sv("g", {}, g);
    const arc = (a0, a1) => { const p0 = [cx + r * Math.cos(a0), cy + r * Math.sin(a0)], p1 = [cx + r * Math.cos(a1), cy + r * Math.sin(a1)]; return `M${p0[0]} ${p0[1]} A ${r} ${r} 0 ${a1 - a0 > Math.PI ? 1 : 0} 1 ${p1[0]} ${p1[1]}`; };
    const A0 = 0.75 * Math.PI, SW = 1.5 * Math.PI;
    sv("path", { d: arc(A0, A0 + SW), fill: "none", stroke: C.grayL, "stroke-width": 18, "stroke-linecap": "round" }, G);
    const val = sv("path", { d: "", fill: "none", stroke: cols[i], "stroke-width": 18, "stroke-linecap": "round" }, G);
    const nd = sv("line", { x1: cx, y1: cy, x2: cx, y2: cy - 80, stroke: C.ink, "stroke-width": 6, "stroke-linecap": "round" }, G);
    sv("circle", { cx, cy, r: 12, fill: C.ink }, G);
    const ic = div(root, "abs", { left: cx - 26 + "px", top: cy + 34 + "px" }, icon(T.gauge_icons[i], 52, cols[i], 2));
    const lb = div(root, "abs center t-title", { left: cx - 140 + "px", top: "580px", width: "280px", fontSize: T.gauges[i].length > 12 ? "26px" : "30px", lineHeight: 1.2 }, name);
    return { cd, G, val, nd, ic, lb, cx, cy, r, arc, A0, SW, i };
  });
  const qt = div(root, "card center t-title", { left: "120px", top: "710px", width: "270px", height: "170px", background: C.greenD, color: "#fff", fontSize: "32px", lineHeight: 1.3 }, T.qc_title);
  const qi = ["test-pipe", "filter", "notes", "microscope", "clipboard-check"];
  const qs = T.qc.map((s, i) => {
    const x = 420 + i * 278;
    const e = div(root, "abs", { left: x + "px", top: "710px", width: "268px", height: "170px" },
      `<svg width="268" height="170" style="position:absolute;left:0;top:0"><polygon points="0,0 236,0 268,85 236,170 0,170 ${i ? "32,85" : "0,85"}" fill="${C.card}" stroke="${C.line}" stroke-width="2"/></svg>`);
    div(e, "abs", { left: "112px", top: "22px" }, icon(qi[i], 46, C.green, 2));
    div(e, "abs center t-title", { left: "30px", top: "86px", width: "210px", fontSize: "26px", lineHeight: 1.2 }, s);
    return e;
  });
  return (t) => {
    show(h, P(t, 0.2));
    gs.forEach((q, i) => {
      const p = P(t, at(1, i / 5.5) - 0.1, 0.6);
      show(q.cd, p, { dy: 24 }); showSvg(q.G, p, { dy: 24 }); show(q.ic, p, { dy: 24 }); show(q.lb, p, { dy: 24 });
      const v = clamp(base[i] * P(t, at(1, i / 5.5), 1.2) + 0.035 * Math.sin(t * 1.7 + i * 1.3));
      q.val.setAttribute("d", v > 0.001 ? q.arc(q.A0, q.A0 + q.SW * v) : "");
      const a = q.A0 + q.SW * v; q.nd.setAttribute("x2", q.cx + 76 * Math.cos(a)); q.nd.setAttribute("y2", q.cy + 76 * Math.sin(a));
    });
    show(qt, P(t, c(2) - 0.2, 0.6), { dx: -20, dy: 0 });
    qs.forEach((e, i) => show(e, P(t, at(2, 0.05 + i * 0.16), 0.6), { dx: -20, dy: 0 }));
  };
};

// ---------------------------------------------------------------- 13 受入原料と資源化先
SCENES.s13_inputs_outputs = (ctx) => {
  const { root, g, T, c, at, device } = ctx;
  const h = heading(root, T.heading);
  const colT = (x, s, col) => div(root, "abs t-title", { left: x + "px", top: "236px", width: "480px", fontSize: "28px", color: col }, s);
  const inT = colT(120, T.in_title, C.soil), outT = colT(1320, T.out_title, C.green);
  const row = (x, it, bg, fg) => { const cd = div(root, "card", { left: x + "px", width: "480px", height: "92px" }); iconCircle(cd, it.icon, 52, 46, 32, bg, fg); div(cd, "abs t-title", { left: "104px", top: "0", height: "92px", width: "360px", display: "flex", alignItems: "center", fontSize: "28px", lineHeight: 1.2 }, it.title); return cd; };
  const Y = (i) => 290 + i * 112;
  const ins = T.inputs.map((it, i) => { const e = row(120, it, C.soilL, C.soil); e.style.top = Y(i) + "px"; return e; });
  const outs = T.outputs.map((it, i) => { const e = row(1320, it, C.greenL, C.green); e.style.top = Y(i) + "px"; return e; });
  const dev = div(root, "card", { left: "790px", top: "440px", width: "340px", height: "260px", background: C.green });
  const cog = div(dev, "abs", { left: "130px", top: "34px", width: "80px", height: "80px" }, icon("settings-cog", 80, "#fff", 1.6));
  div(dev, "abs center t-title", { left: "20px", top: "130px", width: "300px", height: "100px", fontSize: device.length > 12 ? "28px" : "34px", color: "#fff", lineHeight: 1.25 }, device);
  const conIn = T.inputs.map((_, i) => sv("path", { d: `M600 ${Y(i) + 46} C 700 ${Y(i) + 46} 690 570 790 570`, fill: "none", stroke: C.soil, "stroke-width": 3, opacity: 0 }, g));
  const conOut = T.outputs.map((_, i) => sv("path", { d: `M1130 570 C 1230 570 1220 ${Y(i) + 46} 1320 ${Y(i) + 46}`, fill: "none", stroke: C.green, "stroke-width": 3, opacity: 0 }, g));
  const dIn = conIn.map(() => sv("circle", { r: 7, fill: C.soil, opacity: 0 }, g)), dOut = conOut.map(() => sv("circle", { r: 7, fill: C.green, opacity: 0 }, g));
  const note = div(root, "abs", { left: "120px", top: "885px", width: "1680px", fontSize: "26px", color: C.muted, textAlign: "center" }, T.note);
  return (t) => {
    show(h, P(t, 0.2));
    show(dev, P(t, c(0) - 0.2, 0.7), { dy: 0, s: 0.2 });
    cog.style.transform = `rotate(${t * 40}deg)`;
    inT.style.opacity = P(t, c(0), 0.5); outT.style.opacity = P(t, c(1), 0.5);
    ins.forEach((e, i) => { const p = P(t, at(0, 0.12 + i * 0.16), 0.6); show(e, p, { dx: -30, dy: 0 }); conIn[i].setAttribute("opacity", p); const u = (t * 0.4 + i * 0.2) % 1; const pt = along(conIn[i], u); dIn[i].setAttribute("cx", pt.x); dIn[i].setAttribute("cy", pt.y); dIn[i].setAttribute("opacity", p * Math.sin(u * Math.PI)); });
    outs.forEach((e, i) => { const p = P(t, at(1, 0.12 + i * 0.15), 0.6); show(e, p, { dx: 30, dy: 0 }); conOut[i].setAttribute("opacity", p); const u = (t * 0.4 + i * 0.2) % 1; const pt = along(conOut[i], u); dOut[i].setAttribute("cx", pt.x); dOut[i].setAttribute("cy", pt.y); dOut[i].setAttribute("opacity", p * Math.sin(u * Math.PI)); });
    show(note, P(t, c(2), 0.7), { dy: 14 });
  };
};

// ---------------------------------------------------------------- 14 地域の循環
SCENES.s14_loop = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const cx = 960, cy = 612, R = 285;
  const ring = sv("circle", { cx, cy, r: R, fill: "none", stroke: C.amberL, "stroke-width": 26 }, g);
  const flow = sv("circle", { cx, cy, r: R, fill: "none", stroke: C.amber, "stroke-width": 7, "stroke-dasharray": "3 34", "stroke-linecap": "round" }, g);
  const angs = T.nodes.map((_, i) => -90 + i * 72);
  const heads = angs.map((a) => { const m = (a + 36) * Math.PI / 180; return arrowHead(g, cx + R * Math.cos(m), cy + R * Math.sin(m), a + 36 + 90, 22, C.amber); });
  const cols = [C.soil, C.green, C.amber, C.green, C.red];
  const nodes = T.nodes.map((n, i) => {
    const a = angs[i] * Math.PI / 180, x = cx + R * Math.cos(a), y = cy + R * Math.sin(a);
    const halo = sv("circle", { cx: x, cy: y, r: 84, fill: cols[i], opacity: 0 }, g);
    const nd = div(root, "icoc abs", { left: x - 72 + "px", top: y - 72 + "px", width: "144px", height: "144px", background: "#fff", border: `5px solid ${cols[i]}` }, icon(n.icon, 70, cols[i], 1.8));
    const right = i <= 2;
    const lb = div(root, "abs", { left: (right ? x + 92 : x - 92 - 360) + "px", top: y - (i === 0 ? 92 : 44) + "px", width: "360px", textAlign: right ? "left" : "right" },
      `<div style="font-size:30px;font-weight:700;line-height:1.2">${n.title}</div><div style="font-size:24px;color:${C.muted};margin-top:6px">${n.text}</div>`);
    return { nd, lb, halo };
  });
  const center = div(root, "abs center t-title", { left: cx - 230 + "px", top: cy - 90 + "px", width: "460px", height: "180px", fontSize: "30px", lineHeight: 1.45, color: C.greenD }, nl(T.center));
  const tn = [c(0) + 0.3, at(1, 0.05), at(1, 0.3), at(1, 0.55), at(1, 0.78)];
  return (t) => {
    show(h, P(t, 0.2));
    const pr = P(t, 0.4, 1.2); ring.setAttribute("opacity", pr); flow.setAttribute("opacity", pr);
    flow.style.strokeDashoffset = -t * 40;
    heads.forEach((e) => e.setAttribute("opacity", pr));
    nodes.forEach((n, i) => { const p = P(t, tn[i], 0.6); show(n.nd, p, { dy: 0, s: 0.4 }); show(n.lb, p, { dy: 14 });
      const cyc = (t - c(2)) / 1.1; const on = cyc > 0 ? Math.max(0, 1 - Math.abs(((cyc % 5) + 5) % 5 - i) * 1.4) : 0; n.halo.setAttribute("opacity", 0.22 * on); });
    show(center, P(t, c(2) - 0.1, 0.8), { dy: 16 });
  };
};

// ---------------------------------------------------------------- 15 GHG 算定の範囲
SCENES.s15_ghg_boundary = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const bnd = sv("rect", { x: 110, y: 400, width: 1700, height: 270, rx: 28, fill: "rgba(220,234,223,.35)", stroke: C.greenD, "stroke-width": 4, "stroke-dasharray": "16 12" }, g);
  const tab = div(root, "abs chip", { left: "140px", top: "378px", background: C.greenD, color: "#fff", fontSize: "24px", padding: "6px 18px" }, T.boundary);
  const xs = T.chain.map((_, i) => 170 + i * 415), W = 340;
  const boxes = T.chain.map((s, i) => {
    const cd = div(root, "card", { left: xs[i] + "px", top: "450px", width: W + "px", height: "180px" });
    iconCircle(cd, T.chain_icons[i], 56, 90, 34, C.greenL, C.green);
    div(cd, "abs t-title", { left: "104px", top: "0", height: "180px", width: "224px", display: "flex", alignItems: "center", fontSize: "27px", lineHeight: 1.25 }, s);
    return cd;
  });
  const ar = [0, 1, 2].map((i) => div(root, "abs", { left: xs[i] + W + 12 + "px", top: "515px" }, `<svg width="54" height="50"><line x1="4" y1="25" x2="36" y2="25" stroke="${C.soil}" stroke-width="7" stroke-linecap="round"/><polygon points="52,25 34,10 34,40" fill="${C.soil}"/></svg>`));
  const addT = div(root, "abs t-title", { left: "120px", top: "250px", fontSize: "26px", color: C.red }, T.added_title);
  const adds = T.added.map((s, i) => {
    const x = xs[i + 1] + W / 2;
    const e = div(root, "abs", { left: x - 190 + "px", top: "290px", width: "380px", display: "flex", flexDirection: "column", alignItems: "center" },
      `<span class="chip" style="background:${C.redL};color:${C.red};font-size:24px;white-space:nowrap">${s}</span><svg width="30" height="56"><line x1="15" y1="54" x2="15" y2="14" stroke="${C.red}" stroke-width="5" stroke-dasharray="6 6"/><polygon points="15,2 4,18 26,18" fill="${C.red}"/></svg>`);
    return e;
  });
  const cmp = div(root, "card", { left: "170px", top: "715px", width: "760px", height: "140px" });
  iconCircle(cmp, "barrier-block", 70, 70, 40, C.grayL, C.gray);
  div(cmp, "abs", { left: "134px", top: "26px", fontSize: "24px", color: C.muted }, T.compare_title);
  div(cmp, "abs t-title", { left: "134px", top: "62px", width: "600px", fontSize: "32px" }, T.compare);
  const avo = div(root, "abs", { left: "960px", top: "745px", display: "flex", alignItems: "center", gap: "18px" },
    `<svg width="90" height="50"><line x1="4" y1="25" x2="70" y2="25" stroke="${C.green}" stroke-width="7" stroke-linecap="round"/><polygon points="88,25 68,10 68,40" fill="${C.green}"/></svg><span class="chip" style="background:${C.greenL};color:${C.greenD};font-size:30px;padding:14px 28px">${T.avoided}</span>`);
  const note = div(root, "abs", { left: "120px", top: "900px", width: "1680px", fontSize: "26px", color: C.muted, textAlign: "center" }, T.note);
  const tb = [at(1, 0.05), at(1, 0.28), at(1, 0.5), at(1, 0.75)];
  return (t) => {
    show(h, P(t, 0.2));
    drawLine(bnd, P(t, c(0) + 0.6, 2.0)); bnd.setAttribute("fill-opacity", P(t, c(0) + 2, 1)); tab.style.opacity = P(t, c(0) + 1.4, 0.6);
    boxes.forEach((b, i) => show(b, P(t, tb[i] - 0.1, 0.6), { dy: 20 }));
    ar.forEach((a, i) => (a.style.opacity = P(t, tb[i + 1] - 0.3, 0.4)));
    addT.style.opacity = P(t, c(2), 0.6);
    adds.forEach((a, i) => show(a, P(t, at(2, 0.05 + i * 0.2), 0.6), { dy: 20 }));
    show(cmp, P(t, at(2, 0.5), 0.6), { dy: 20 });
    show(avo, P(t, at(2, 0.72), 0.6), { dx: -20, dy: 0 });
    show(note, P(t, c(3) - 0.1, 0.7), { dy: 14 });
  };
};

// ---------------------------------------------------------------- 16 二つの価値
SCENES.s16_value = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const mk = (x, s, col, colL) => {
    const cd = div(root, "card", { left: x + "px", top: "235px", width: "680px", height: "480px" });
    iconCircle(cd, s.icon, 340, 100, 60, colL, col);
    div(cd, "abs center t-title", { left: "30px", top: "190px", width: "620px", fontSize: "44px", color: col }, s.title);
    div(cd, "abs center", { left: "40px", top: "256px", width: "600px", fontSize: "28px", lineHeight: 1.45 }, s.text);
    div(cd, "abs center", { left: "0", top: "392px", width: "680px" }, `<span class="chip" style="background:${colL};color:${col}">${s.tag}</span>`);
    return cd;
  };
  const A = mk(226, T.a, C.soil, C.soilL), B = mk(1014, T.b, C.green, C.greenL);
  const plus = div(root, "icoc abs", { left: "916px", top: "431px", width: "88px", height: "88px", background: C.amber, color: "#fff", fontSize: "60px", fontWeight: 700 }, "+");
  const base = div(root, "abs center t-title", { left: "190px", top: "760px", width: "1540px", height: "112px", borderRadius: "20px", background: C.greenD, color: "#fff", fontSize: "38px" }, T.base);
  return (t) => {
    show(h, P(t, 0.2));
    show(A, P(t, c(1) - 0.2, 0.7), { dy: 40 });
    show(B, P(t, c(2) - 0.2, 0.7), { dy: 40 });
    show(plus, P(t, c(2) + 0.3, 0.5), { dy: 0, s: 0.5 });
    show(base, P(t, c(3) - 0.1, 0.7), { dy: 30 });
    const f = P(t, c(3) + 0.8, 1) * 4 * Math.sin(t * 1.6);
    A.style.marginTop = f + "px"; B.style.marginTop = -f + "px";
  };
};

// ---------------------------------------------------------------- 17 関係者
SCENES.s17_stakeholders = (ctx) => {
  const { root, g, T, c, at } = ctx;
  const h = heading(root, T.heading);
  const cx = 960, cy = 605, RX = 530, RY = 300;
  const ring = sv("ellipse", { cx, cy, rx: RX, ry: RY, fill: "none", stroke: C.amberL, "stroke-width": 14 }, g);
  const flow = sv("ellipse", { cx, cy, rx: RX, ry: RY, fill: "none", stroke: C.amber, "stroke-width": 6, "stroke-dasharray": "3 30", "stroke-linecap": "round" }, g);
  const cols = [C.soil, C.water, C.green, C.amber, C.red];
  const pos = T.nodes.map((_, i) => { const a = (-90 + i * 72) * Math.PI / 180; return [cx + RX * Math.cos(a), cy + RY * Math.sin(a)]; });
  const spokes = pos.map(([x, y]) => sv("line", { x1: cx, y1: cy, x2: x, y2: y, stroke: C.line, "stroke-width": 3, "stroke-dasharray": "8 8" }, g));
  const sd = pos.map(() => sv("circle", { r: 7, fill: C.green }, g));
  const cen = div(root, "icoc abs", { left: cx - 130 + "px", top: cy - 130 + "px", width: "260px", height: "260px", background: C.green, flexDirection: "column", color: "#fff", gap: "8px" },
    icon("settings-cog", 70, "#fff", 1.6) + `<div style="font-size:${T.center.length > 8 ? 22 : 26}px;font-weight:700;text-align:center;line-height:1.25;padding:0 18px">${T.center}</div>`);
  const cards = T.nodes.map((n, i) => {
    const [x, y] = pos[i];
    const cd = div(root, "card", { left: x - 230 + "px", top: y - 62 + "px", width: "460px", height: "124px", border: `3px solid ${cols[i]}` });
    iconCircle(cd, n.icon, 62, 62, 38, "#fff", cols[i], 1.9);
    div(cd, "abs", { left: "112px", top: "0", height: "124px", width: "334px", display: "flex", flexDirection: "column", justifyContent: "center" },
      `<div style="font-size:28px;font-weight:700;line-height:1.2">${n.title}</div><div style="font-size:21px;color:${C.muted};margin-top:4px;line-height:1.3">${n.text}</div>`);
    return cd;
  });
  const tn = [at(1, 0.02), at(1, 0.4), at(1, 0.55), at(1, 0.72), at(1, 0.86)];
  return (t) => {
    show(h, P(t, 0.2));
    show(cen, P(t, c(0) - 0.1, 0.7), { dy: 0, s: 0.3 });
    cards.forEach((cd, i) => { const p = P(t, tn[i] - 0.1, 0.6); show(cd, p, { dy: 20 }); spokes[i].setAttribute("opacity", p);
      const u = (t * 0.45 + i * 0.2) % 1; const [x, y] = pos[i]; const out = i % 2 === 0; const k = out ? u : 1 - u;
      sd[i].setAttribute("cx", lerp(cx, x, k)); sd[i].setAttribute("cy", lerp(cy, y, k)); sd[i].setAttribute("opacity", p * Math.sin(u * Math.PI)); });
    const pr = P(t, c(2) - 0.2, 1); ring.setAttribute("opacity", pr); flow.setAttribute("opacity", pr); flow.style.strokeDashoffset = -t * 40;
  };
};

// ---------------------------------------------------------------- 18 結び
SCENES.s18_closing = (ctx) => {
  const { root, T, c, dur, lang } = ctx;
  const bg = div(root, "abs", { left: "0", top: "0", width: "1920px", height: "1080px", overflow: "hidden" });
  const img = el("img", bg, null, { position: "absolute", left: "0", top: "-560px", width: "1920px", height: "1920px", transformOrigin: "40% 50%" });
  img.src = "img/field.png";
  div(bg, "abs", { left: "0", top: "0", width: "1920px", height: "1080px", background: "linear-gradient(90deg, rgba(16,42,29,.94) 0%, rgba(16,42,29,.80) 50%, rgba(16,42,29,.35) 100%)" });
  const colm = div(root, "abs", { left: "140px", top: "250px", width: "1500px", display: "flex", flexDirection: "column", alignItems: "flex-start" });
  const msg = div(colm, "t-title", { fontSize: lang === "ja" ? "78px" : "68px", color: "#fff", lineHeight: 1.2 }, T.message);
  const ttl = div(colm, "t-title", { fontSize: "38px", color: C.amber, marginTop: "26px" }, T.title);
  const logo = div(colm, null, { background: "#fff", borderRadius: "20px", padding: "22px 30px", display: "flex", alignItems: "center", marginTop: "64px" });
  const im = el("img", logo, null, { height: lang === "ja" ? "120px" : "110px", display: "block" }); im.src = "img/" + T.logo;
  if (lang !== "ja") div(logo, "t-title", { fontSize: "30px", color: "#2B3A6B", marginLeft: "26px", paddingLeft: "26px", borderLeft: "2px solid #D5DAE6" }, T.company);
  const note = div(root, "abs", { left: "140px", top: "960px", width: "1640px", fontSize: "21px", color: "rgba(255,255,255,.72)", lineHeight: 1.45 }, T.note);
  const shade = div(root, "abs", { left: "0", top: "0", width: "1920px", height: "1080px", background: "#0E2419", opacity: 0 });
  return (t) => {
    img.style.transform = `scale(${1.04 + 0.05 * t / dur})`;
    show(msg, P(t, 0.4, 0.9));
    show(ttl, P(t, 0.9, 0.8));
    show(logo, P(t, 1.5, 0.8));
    note.style.opacity = P(t, 2.0, 0.8);
    shade.style.opacity = clamp((t - (dur - 1.6)) / 1.2);
  };
};
