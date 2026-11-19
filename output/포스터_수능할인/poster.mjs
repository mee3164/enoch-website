// poster.html → poster.png (블로그 썸네일 1080×1080). CHROMIUM_PATH=... node output/포스터_수능할인/poster.mjs
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto(pathToFileURL(path.join(dir, "poster.html")).href); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
await (await p.$("section")).screenshot({ path: path.join(dir, "poster.png") });
await b.close(); console.log("poster.png");
