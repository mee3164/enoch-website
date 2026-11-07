// 표지(01.png)를 사진형으로 다시 만든다 — npm run cardnews:render, singers.mjs 뒤에 실행
// node output/노트_무대가두려웠던가수/cover.mjs
// 사진: Adele, 2009 — Christopher Macsurak / CC BY 2.0 (흑백 보정·자르기). src/cover_adele.jpg는 저장소에 올리지 않는다.
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
.c{width:1080px;height:1350px;position:relative;overflow:hidden;background:#F1EDE4;color:#111;font-family:P,sans-serif;word-break:keep-all}
.mono{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace}
.hd,.ft{position:absolute;left:96px;right:96px;display:flex;justify-content:space-between;font-size:20px;letter-spacing:2.4px}
.hd{top:76px;padding-bottom:18px;border-bottom:2px solid #111}.ft{bottom:76px;padding-top:18px;border-top:2px solid #111}
.ph{position:absolute;left:96px;top:150px;width:888px;height:676px;overflow:hidden}
.ph img{width:100%;height:100%;object-fit:cover;object-position:50% 40%;filter:grayscale(1) sepia(.18) contrast(1.05)}
.cr{position:absolute;right:96px;top:836px;font-size:15px;letter-spacing:1px;color:#8A8A8A}
.k{position:absolute;left:96px;top:890px;font-size:19px;letter-spacing:2.4px;color:#8A8A8A}
h1{position:absolute;left:96px;top:942px;font-size:60px;line-height:1.24;font-weight:700;letter-spacing:-2px}
p{position:absolute;left:96px;top:1112px;font-size:32px;font-weight:300;color:#555}
</style></head><body><section class="c">
<div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH NOTE — SHY SINGERS</span></div>
<div class="ph"><img src="src/cover_adele.jpg"></div>
<div class="cr mono">Photo: Christopher Macsurak / CC BY 2.0</div>
<div class="k mono">ADELE · ELLIE GOULDING · CAMILA CABELLO · KELLY CLARKSON</div>
<h1>그래미 받은 가수가<br>“관객이 무서워요”라고 했습니다.</h1>
<p>무대가 두려웠던 가수, 네 명의 이야기.</p>
<div class="ft mono"><span>무대가 두려웠던 가수</span><span>01 / 08</span></div></section></body></html>`;
writeFileSync(path.join(dir, "cover.html"), html);
const { chromium } = require("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto("file://" + path.join(dir, "cover.html")); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
await (await p.$(".c")).screenshot({ path: path.join(dir, "01.png") });
await b.close(); console.log("01.png (cover)");
