// 렌더: node render.mjs reel.html <초> reel.mp4  /  미리보기: node render.mjs reel.html peek t1 t2 ...
// 무손실 PNG 프레임 → libx264 crf 14
import path from "node:path";
import { mkdirSync, rmSync } from "node:fs";
import { execFileSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const [html, a2, ...rest] = process.argv.slice(2);
const FPS = 30;
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto(pathToFileURL(path.join(dir, html)).href);
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
if (a2 === "peek") {
  for (const t of rest.map(Number)) { await p.evaluate((t) => setT(t), t); await p.screenshot({ path: path.join(dir, `_peek_${html}_${t}.png`) }); }
} else {
  const out = rest[0], DUR = Number(a2);
  const fr = path.join(dir, "_frames"); rmSync(fr, { recursive: true, force: true }); mkdirSync(fr);
  for (let i = 0; i < Math.round(FPS * DUR); i++) {
    await p.evaluate((t) => setT(t), i / FPS);
    await p.screenshot({ path: path.join(fr, `${String(i).padStart(4, "0")}.png`) });
  }
  execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-framerate", String(FPS), "-i", path.join(fr, "%04d.png"),
    "-c:v", "libx264", "-preset", "slow", "-crf", "14", "-pix_fmt", "yuv420p", "-movflags", "+faststart", path.join(dir, out)]);
  rmSync(fr, { recursive: true, force: true });
  console.log(out);
}
await b.close();
