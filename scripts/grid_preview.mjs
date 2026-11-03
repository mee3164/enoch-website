// 인스타 프로필 미리보기: 올릴 편 + 이미 올린 편 표지를 3칸 격자(3:4로 잘린 모양)로 붙여 본다
// node scripts/grid_preview.mjs <출력.png> <최신 폴더> <그다음 폴더> ...   (왼쪽 위가 가장 최신)
// 폴더 대신 이미지 경로를 줘도 된다. 폴더면 그 안의 01.png를 쓴다.
import { existsSync, statSync, writeFileSync } from "node:fs";
import path from "node:path";
import { pathToFileURL, fileURLToPath } from "node:url";
import { createRequire } from "node:module";
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const require = createRequire(path.join(root, "package.json"));
const [out, ...items] = process.argv.slice(2);
const imgs = items.map((p) => {
  const a = path.resolve(p);
  return existsSync(a) && statSync(a).isDirectory() ? path.join(a, "01.png") : a;
});
const cell = 360, gap = 4, cols = 3, rows = Math.ceil(imgs.length / cols);
const html = `<!doctype html><meta charset="utf-8"><style>
*{margin:0}body{background:#fff}
.g{display:grid;grid-template-columns:repeat(${cols},${cell}px);gap:${gap}px;width:${cols * cell + 2 * gap}px}
.g div{width:${cell}px;height:${cell * 4 / 3}px;background:#ddd center/cover no-repeat}
</style><div class="g">${imgs.map((i) => `<div style="background-image:url('${pathToFileURL(i).href}')"></div>`).join("")}</div>`;
const tmp = path.join(path.dirname(path.resolve(out)), "_grid_preview.html");
writeFileSync(tmp, html);
const { chromium } = require("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: cols * cell + 2 * gap, height: rows * (cell * 4 / 3 + gap) } });
await p.goto(pathToFileURL(tmp).href); await p.waitForTimeout(400);
await (await p.$(".g")).screenshot({ path: out });
await b.close();
console.log(out, `${imgs.length}칸`);
