// feed.html → feed_01~03.png (1080×1350), story.html → story_01~02.png (1080×1920)
// CHROMIUM_PATH=... node output/강사소개_손주희/render.mjs
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
for (const [file, pre, w, h] of [["feed.html", "feed", 1080, 1350], ["story.html", "story", 1080, 1920]]) {
  const p = await b.newPage({ viewport: { width: w, height: h } });
  await p.goto(pathToFileURL(path.join(dir, file)).href);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  for (const [i, s] of (await p.$$("section")).entries()) await s.screenshot({ path: path.join(dir, `${pre}_0${i + 1}.png`) });
  await p.close();
}
await b.close();
console.log("done");
// 한 장 버전: story_one.html → story_one.png
{
  const b2 = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const q = await b2.newPage({ viewport: { width: 1080, height: 1920 } });
  await q.goto(pathToFileURL(path.join(dir, "story_one.html")).href); await q.evaluate(() => document.fonts.ready); await q.waitForTimeout(300);
  await (await q.$("section")).screenshot({ path: path.join(dir, "story_one.png") }); await b2.close();
}
// 아이보리 한 장 버전: story_ivory.html → story_ivory.png
{
  const b2 = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const q = await b2.newPage({ viewport: { width: 1080, height: 1920 } });
  await q.goto(pathToFileURL(path.join(dir, "story_ivory.html")).href); await q.evaluate(() => document.fonts.ready); await q.waitForTimeout(300);
  await (await q.$("section")).screenshot({ path: path.join(dir, "story_ivory.png") }); await b2.close();
}
// 한 장 아이보리: story_one_ivory.html → story_one_ivory.png
{
  const b2 = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const q = await b2.newPage({ viewport: { width: 1080, height: 1920 } });
  await q.goto(pathToFileURL(path.join(dir, "story_one_ivory.html")).href); await q.evaluate(() => document.fonts.ready); await q.waitForTimeout(300);
  await (await q.$("section")).screenshot({ path: path.join(dir, "story_one_ivory.png") }); await b2.close();
}
