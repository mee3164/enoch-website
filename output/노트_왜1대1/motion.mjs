// 그래프가 있는 2·4장을 움직이는 영상으로 → 02_motion.mp4 · 04_motion.mp4 (1080×1350, 6초, 마지막 장면에서 멈춤)
// 먼저 node gen.mjs 로 deck.html을 만든 뒤 실행
import { execFileSync } from "node:child_process";
import { mkdirSync, rmSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(dir, "../../package.json"));
const { chromium } = require("playwright");
const FPS = 30, DUR = 6;
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto("file://" + path.join(dir, "deck.html"));
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);

// 장면 정의: 각 요소에 [시작초, 길이] — draw(선 그리기) / fade(나타나기)
await p.evaluate(() => {
  const ease = (x) => 1 - Math.pow(1 - Math.min(1, Math.max(0, x)), 3);
  const secs = [...document.querySelectorAll(".c")];
  const prep = (svg, plan) => [...svg.querySelectorAll("path,line,circle,text")].map((el, i) => {
    const [kind, t0, d] = plan(el, i);
    if (kind === "draw") { el.setAttribute("pathLength", "1"); el.style.strokeDasharray = el.getAttribute("stroke-dasharray") ? "" : "1 1"; }
    return { el, kind, t0, d, dashed: !!el.getAttribute("stroke-dasharray") };
  });
  // 2장: 교실 곡선 → 화살표 → 1:1 곡선·면 → 점선·라벨, 98%는 숫자가 올라감
  const s2 = secs[1], svg2 = s2.querySelector(".fig svg");
  const P2 = prep(svg2, (el, i) => {
    const tag = el.tagName;
    if (tag === "text") return ["fade", i === 6 ? 0.9 : 2.6, 0.5];
    if (tag === "line") return ["fade", tag === "line" && i === 3 ? 0 : (i === 4 ? 0.9 : 2.6), 0.5];
    if (i === 0) return ["draw", 0.2, 1.2];        // 교실 곡선
    if (i === 1) return ["draw", 2.0, 1.2];        // 1:1 곡선
    if (i === 2) return ["fade", 2.6, 0.8];        // 1:1 면
    return ["draw", 1.5, 0.6];                     // 화살표
  });
  const num = s2.querySelector(".num");
  // 4장: A 곡선 → B 곡선 → 점·라벨
  const s4 = secs[3], svg4 = s4.querySelector(".fig svg");
  const P4 = prep(svg4, (el, i) => {
    const tag = el.tagName;
    if (i === 0) return ["draw", 0.3, 1.4];
    if (i === 1) return ["draw", 1.6, 1.4];
    if (tag === "circle") return ["fade", i === 2 ? 1.6 : 2.9, 0.4];
    if (tag === "line") return ["fade", 0, 0.4];
    if (tag === "text") return ["fade", el.textContent.startsWith("A") ? 1.7 : el.textContent.startsWith("B") ? 3.0 : 0, 0.5];
    return ["fade", 0, 0.3];
  });
  const apply = (P, t) => P.forEach(({ el, kind, t0, d }) => {
    const k = ease((t - t0) / d);
    if (kind === "draw") el.style.strokeDashoffset = String(1 - k); else el.style.opacity = String(k);
  });
  window.renderAt = (which, t) => {
    if (which === 2) { apply(P2, t); num.innerHTML = Math.round(98 * ease((t - 0.2) / 3.0)) + "<span>%</span>"; }
    else apply(P4, t);
  };
});

for (const which of [2, 4]) {
  const fr = path.join(dir, `_frames${which}`); rmSync(fr, { recursive: true, force: true }); mkdirSync(fr);
  const el = (await p.$$(".c"))[which - 1];
  for (let i = 0; i < FPS * DUR; i++) {
    await p.evaluate(([w, t]) => window.renderAt(w, t), [which, i / FPS]);
    await el.screenshot({ path: path.join(fr, String(i).padStart(4, "0") + ".png") });
  }
  execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(FPS), "-i", path.join(fr, "%04d.png"),
    "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", path.join(dir, `0${which}_motion.mp4`)]);
  rmSync(fr, { recursive: true, force: true });
  console.log(`0${which}_motion.mp4`);
}
await b.close();
