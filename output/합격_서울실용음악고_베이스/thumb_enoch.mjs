// thumb_enoch.html → section마다 data-name.png (1080×1350). CHROMIUM_PATH=... node output/합격_서울실용음악고_베이스/poster.mjs
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1080 } });
await p.goto(pathToFileURL(path.join(dir, "thumb_enoch.html")).href);
await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
const ss = await p.$$("section");
for (let i = 0; i < ss.length; i++) await ss[i].screenshot({ path: path.join(dir, (await ss[i].getAttribute("data-name")) + ".png") });
await b.close(); console.log(ss.length, "thumbs");
