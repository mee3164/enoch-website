// collage.html → collage.png (1080×1920)
// CHROMIUM_PATH=... node output/합격_2026_콜라주/render.mjs
import path from "node:path"; import { fileURLToPath, pathToFileURL } from "node:url"; import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto(pathToFileURL(path.join(dir, "collage.html")).href); await p.waitForTimeout(400);
await p.screenshot({ path: path.join(dir, "collage.png") }); await b.close();
