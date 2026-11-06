// 표지(01.png)만 사진 전면형으로 다시 만든다 — npm run cardnews:render 뒤에 실행
// node output/노트_내향형보컬/cover.mjs
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(dir, "../../package.json"));
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}
.c{width:1080px;height:1350px;position:relative;overflow:hidden;background:#111;color:#F1EDE4;font-family:P,sans-serif;word-break:keep-all}
img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:50% 50%}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,17,17,.72) 0%,rgba(17,17,17,.35) 12%,rgba(17,17,17,0) 26%,rgba(17,17,17,0) 50%,rgba(17,17,17,.85) 82%)}
.hd,.ft{position:absolute;left:96px;right:96px;display:flex;justify-content:space-between;font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;font-size:20px;letter-spacing:2.4px}
.hd{top:64px;padding-bottom:18px;border-bottom:2px solid currentColor}.ft{bottom:64px;padding-top:18px;border-top:2px solid currentColor}
h1{position:absolute;left:96px;bottom:250px;font-size:72px;line-height:1.22;font-weight:700;letter-spacing:-2px}
p{position:absolute;left:96px;bottom:180px;font-size:36px;font-weight:300;color:#ddd}
</style></head><body><section class="c"><img src="src/silhouette_bw.jpg"><div class="shade"></div>
<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH NOTE — QUIET VOICE</span></div>
<h1>남 앞에서 노래하는 게<br>어색한 사람도,<br>노래를 배울 수 있을까요?</h1><p>스스로 내향형이라고 말하는 분들께.</p>
<div class="ft"><span>조용한 목소리</span><span>01 / 07</span></div></section></body></html>`;
writeFileSync(path.join(dir, "cover.html"), html);
const { chromium } = require("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto("file://" + path.join(dir, "cover.html")); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
await (await p.$(".c")).screenshot({ path: path.join(dir, "01.png") });
await b.close(); console.log("01.png (cover)");
