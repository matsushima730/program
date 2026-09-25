// 図解の場面を1コマずつ撮って mp4 にする（Playwright の Chromium）。
//   node render.js ja stills            → build/stills_ja/*.jpg（確認用の静止画）
//   node render.js ja video K N         → N 本並列のうち K 番目の担当場面を build/seg_ja/*.mp4 に
const { chromium } = require("/opt/node22/lib/node_modules/playwright");
const fs = require("fs"), path = require("path"), { spawn } = require("child_process");
const ROOT = __dirname;
const [lang, mode, K, N] = process.argv.slice(2);
const tl = JSON.parse(fs.readFileSync(path.join(ROOT, "build", `timeline_${lang}.json`), "utf8"));
const device = JSON.parse(fs.readFileSync(path.join(ROOT, "build", "content.json"), "utf8")).device[lang];
const FPS = tl.fps;

function cfgFor(i) {
  const s = tl.scenes[i];
  return { scene: s, lang, dur: s.dur, start: s.start, total: tl.total, chapters: tl.chapters, device,
           prevChrome: i > 0 && tl.scenes[i - 1].chapter !== 0, nextChrome: i < tl.scenes.length - 1 && tl.scenes[i + 1].chapter !== 0 };
}
async function openScene(browser, i) {
  const page = await browser.newPage({ viewport: { width: 1920, height: 1080 } });
  const errs = [];
  page.on("pageerror", (e) => errs.push(String(e)));
  await page.goto("file://" + path.join(ROOT, "web", "stage.html"));
  await page.evaluate(() => document.fonts.ready);
  await page.evaluate((cfg) => window.SETUP(cfg), cfgFor(i));
  await page.evaluate(() => Promise.all([...document.images].map((im) => im.complete ? 1 : new Promise((r) => { im.onload = r; im.onerror = r; }))));
  await page.evaluate(() => document.fonts.ready);
  if (errs.length) throw new Error(errs.join("\n"));
  return page;
}
function assign(n, k) {  // 尺の長い順に、いちばん空いている担当へ
  const load = Array(n).fill(0), own = Array(n).fill(0).map(() => []);
  tl.scenes.map((s, i) => [s.frames, i]).sort((a, b) => b[0] - a[0]).forEach(([f, i]) => { const j = load.indexOf(Math.min(...load)); load[j] += f; own[j].push(i); });
  return own[k].sort((a, b) => a - b);
}
(async () => {
  const browser = await chromium.launch({ args: ["--disable-gpu", "--font-render-hinting=none"] });
  if (mode === "stills") {
    const out = path.join(ROOT, "build", `stills_${lang}`); fs.mkdirSync(out, { recursive: true });
    const only = K ? K.split(",") : null;
    for (let i = 0; i < tl.scenes.length; i++) {
      const s = tl.scenes[i];
      if (only && !only.some((o) => s.id.startsWith(o))) continue;
      const page = await openScene(browser, i);
      const ts = [s.cues[1] ? s.cues[1].s + 0.3 : 3, s.dur - 1.2];
      for (const t of ts) {
        await page.evaluate((t) => window.RENDER(t), t);
        await page.screenshot({ path: path.join(out, `${s.id}_${t.toFixed(1)}.jpg`), type: "jpeg", quality: 85 });
      }
      await page.close();
      console.log("stills", s.id);
    }
  } else {
    const out = path.join(ROOT, "build", `seg_${lang}`); fs.mkdirSync(out, { recursive: true });
    for (const i of assign(+N, +K)) {
      const s = tl.scenes[i];
      const file = path.join(out, `${String(i).padStart(2, "0")}_${s.id}.mp4`);
      const page = await openScene(browser, i);
      const ff = spawn("ffmpeg", ["-v", "error", "-y", "-f", "image2pipe", "-framerate", String(FPS), "-c:v", "mjpeg", "-i", "-",
        "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", "-g", "30", "-r", String(FPS), "-threads", "1", file], { stdio: ["pipe", "inherit", "inherit"] });
      const t0 = Date.now();
      for (let f = 0; f < s.frames; f++) {
        await page.evaluate((t) => window.RENDER(t), f / FPS);
        const buf = await page.screenshot({ type: "jpeg", quality: 92 });
        if (!ff.stdin.write(buf)) await new Promise((r) => ff.stdin.once("drain", r));
      }
      ff.stdin.end();
      await new Promise((r, j) => ff.on("close", (code) => code === 0 ? r() : j(new Error("ffmpeg " + code))));
      await page.close();
      console.log(`[${K}] ${s.id} ${s.frames}f ${((Date.now() - t0) / 1000).toFixed(0)}s`);
    }
  }
  await browser.close();
})().catch((e) => { console.error(e); process.exit(1); });
