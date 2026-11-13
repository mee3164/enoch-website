// reel.html을 프레임별로 찍어 reel.mp4(31초, 30fps, 1080×1920, 무음)로 만든다
// CHROMIUM_PATH=... node output/릴스_타임감/render.mjs [미리보기 시점들...]
import path from "node:path";
import { mkdirSync, rmSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const FPS = 30, DUR = 31.2;
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto(pathToFileURL(path.join(dir, "reel.html")).href);
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
const peek = process.argv.slice(2).map(Number);
if (peek.length) {
  for (const t of peek) { await p.evaluate((t) => setT(t), t); await p.screenshot({ path: path.join(dir, `_peek_${t}.png`) }); }
} else {
  const fr = path.join(dir, "_frames"); rmSync(fr, { recursive: true, force: true }); mkdirSync(fr);
  for (let i = 0; i < FPS * DUR; i++) {
    await p.evaluate((t) => setT(t), i / FPS);
    await p.screenshot({ path: path.join(fr, `${String(i).padStart(4, "0")}.jpg`), type: "jpeg", quality: 92 });
  }
  execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(FPS), "-i", path.join(fr, "%04d.jpg"),
    "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", path.join(dir, "reel.mp4")]);
  rmSync(fr, { recursive: true, force: true });
  console.log("reel.mp4");
}
await b.close();
