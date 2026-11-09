// 블로그 이미지(시설 사진 + 짧은 문구): blog.html의 각 section → blog_01.png ~
// + main.html → main_1x1.png (1080×1080 대표 사진)
// CHROMIUM_PATH=... node output/블로그_리얼드럼/blog.mjs
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto(pathToFileURL(path.join(dir, "blog.html")).href); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
const ss = await p.$$("section");
for (const [i, s] of ss.entries()) await s.screenshot({ path: path.join(dir, `blog_${String(i + 1).padStart(2, "0")}.png`) });
await p.setViewportSize({ width: 1080, height: 1080 }); await p.goto(pathToFileURL(path.join(dir, "main.html")).href); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
await (await p.$("section")).screenshot({ path: path.join(dir, "main_1x1.png") });
await b.close(); console.log(ss.length, "장");
