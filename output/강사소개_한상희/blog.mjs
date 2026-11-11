// 블로그 이미지(시설 사진 + 짧은 문구): blog.html의 각 section → blog_01.png ~
// (블로그 이미지 9장)
// CHROMIUM_PATH=... node output/강사소개_한상희/blog.mjs
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
await b.close(); console.log(ss.length, "장");

// 썸네일 1:1: thumb.html → thumb.png (표지 1:1, 검정 버전은 thumb_dark.html)
{
  const b2 = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const q = await b2.newPage({ viewport: { width: 1080, height: 1080 } });
  await q.goto(pathToFileURL(path.join(dir, "thumb.html")).href); await q.evaluate(() => document.fonts.ready); await q.waitForTimeout(300);
  await (await q.$("section")).screenshot({ path: path.join(dir, "thumb.png") }); await b2.close();
}
