// 베이스 레슨 릴스: 얼굴이 나오지 않게 손·악기 부분만 잘라 ENOCH 타이포 틀에 넣는다
// node output/릴스_베이스레슨/make.mjs <원본.mov>  → reel.mp4
import { execFileSync } from "node:child_process";
import { createRequire } from "node:module";
import path from "node:path";
import { fileURLToPath } from "node:url";
const dir = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(dir, "../../package.json"));
const { chromium } = require("playwright");
const src = process.argv[2];
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto("file://" + path.join(dir, "overlay.html")); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
await p.screenshot({ path: path.join(dir, "overlay.png") }); await b.close();
// 원본 1080×1920에서 y=990부터 760px(손·베이스~무릎)만 → 1080×760 창, 채도 낮추고 약한 그레인
execFileSync("ffmpeg", ["-y", "-loglevel", "error", "-i", path.join(dir, "overlay.png"), "-i", src,
  "-filter_complex", "[1:v]crop=1080:760:0:990,eq=saturation=0.72:contrast=1.06:brightness=-0.02,noise=alls=7:allf=t[v];[0:v][v]overlay=0:600,format=yuv420p[o]",
  "-map", "[o]", "-map", "1:a?", "-c:v", "libx264", "-crf", "18", "-c:a", "aac", "-shortest", "-movflags", "+faststart", path.join(dir, "reel.mp4")]);
console.log("reel.mp4");
