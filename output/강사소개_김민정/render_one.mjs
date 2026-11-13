// story_one.html / story_one_ivory.html → 같은 이름 .png (1080×1920)
// CHROMIUM_PATH=... node output/강사소개_김민정/render_one.mjs
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
for (const n of ["story_one", "story_one_ivory"]) {
  await p.goto(pathToFileURL(path.join(dir, n + ".html")).href); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  await (await p.$("section")).screenshot({ path: path.join(dir, n + ".png") });
}
await b.close(); console.log("done");
