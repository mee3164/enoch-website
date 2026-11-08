// cards.html → 01.png~08.png (각 장의 마지막 프레임) + motion/01.mp4~08.mp4 (각 5초, 30fps, 1080×1350)
// CHROMIUM_PATH=... node output/노트_또렷한목표/render.mjs [--png]   (--png: 정지 PNG만)
import path from "node:path";
import { mkdirSync, rmSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const N = 8, FPS = 30, DUR = 5, pngOnly = process.argv.includes("--png");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto(pathToFileURL(path.join(dir, "cards.html")).href);
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
mkdirSync(path.join(dir, "motion"), { recursive: true });
for (let i = 1; i <= N; i++) {
  const n = String(i).padStart(2, "0");
  await p.evaluate(([i, t]) => setT(i, t), [i, DUR]);
  await p.screenshot({ path: path.join(dir, `${n}.png`) });
  if (pngOnly) continue;
  const fr = path.join(dir, "_frames"); rmSync(fr, { recursive: true, force: true }); mkdirSync(fr);
  for (let f = 0; f < FPS * DUR; f++) {
    await p.evaluate(([i, t]) => setT(i, t), [i, f / FPS]);
    await p.screenshot({ path: path.join(fr, `${String(f).padStart(4, "0")}.jpg`), type: "jpeg", quality: 92 });
  }
  execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(FPS), "-i", path.join(fr, "%04d.jpg"),
    "-c:v", "libx264", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", path.join(dir, "motion", `${n}.mp4`)]);
  rmSync(fr, { recursive: true, force: true });
  console.log(`${n}.mp4`);
}
await b.close();
