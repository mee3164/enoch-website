// reel.html(CSS 애니메이션) → reel.mp4 : 애니메이션 시간을 직접 맞춰 프레임을 찍는다
import { mkdirSync, rmSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import path from "node:path";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(dir, "../../package.json"));
const { chromium } = require("playwright");
const fps = 30, fr = path.join(dir, "_frames"); rmSync(fr, { recursive: true, force: true }); mkdirSync(fr);
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto(pathToFileURL(path.join(dir, "reel.html")).href); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(500);
const end = await p.evaluate(() => window.END);
await p.evaluate(() => document.getAnimations().forEach((a) => a.pause()));
const n = Math.round(end * fps);
for (let i = 0; i <= n; i++) {
  await p.evaluate((ms) => document.getAnimations().forEach((a) => (a.currentTime = ms)), (i / fps) * 1000);
  await p.screenshot({ path: path.join(fr, String(i).padStart(5, "0") + ".jpg"), type: "jpeg", quality: 92 });
}
await b.close();
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(fps), "-i", path.join(fr, "%05d.jpg"), "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", path.join(dir, "reel.mp4")]);
rmSync(fr, { recursive: true, force: true });
console.log("reel.mp4", n + 1, "frames");
