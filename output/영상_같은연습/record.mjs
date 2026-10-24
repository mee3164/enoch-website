// video.html → frames → video.mp4  (사용: node output/영상_같은연습/record.mjs [fps])
import { chromium } from "playwright";
import { mkdirSync, rmSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import path from "node:path";
const dir = path.dirname(fileURLToPath(import.meta.url));
const fps = +(process.argv[2] || 30);
const ffmpeg = process.env.FFMPEG || "ffmpeg";
const frames = path.join(dir, "_frames"); rmSync(frames, { recursive: true, force: true }); mkdirSync(frames);
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1080, height: 1920 } });
await page.goto(pathToFileURL(path.join(dir, "video.html")).href + "?record");
await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(800);
const end = await page.evaluate(() => END);
const el = await page.$("#v");
const n = Math.round(end * fps);
for (let i = 0; i <= n; i++) {
  await page.evaluate((t) => render(t), i / fps);
  await el.screenshot({ path: path.join(frames, String(i).padStart(5, "0") + ".jpg"), type: "jpeg", quality: 92 });
}
await browser.close();
execFileSync(ffmpeg, ["-y", "-loglevel", "error", "-framerate", String(fps), "-i", path.join(frames, "%05d.jpg"),
  "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "18", "-movflags", "+faststart", path.join(dir, "video.mp4")]);
rmSync(frames, { recursive: true, force: true });
console.log(`video.mp4 (${n + 1} frames, ${fps}fps)`);
