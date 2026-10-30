// 표지 매거진 시안 3종 → cover_A.png · cover_B.png · cover_C.png
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(dir, "../../package.json"));
const IV = "#F1EDE4", BK = "#111", GY = "#8A8A8A";
const IMG = `src/cover_full.jpg`;
const covers = {
// A: 사진 전면 + 상단 큰 제호 + 하단 커버라인 (잡지 표지)
A: `<section class="c A"><img class="bg" src="${IMG}"><div class="shade"></div>
<div class="mast">ENOCH</div>
<div class="row"><span>NOTE — WHY 1:1</span><span>LESSON ISSUE</span></div>
<div class="lines">
  <p class="kick">COVER STORY</p>
  <h1>1:1로 배우면<br>빨리 느는 이유,</h1>
  <p class="sub">알고 나면 납득되는 3가지</p>
  <ul><li><b>01</b> 한 사람만 보는 시간</li><li><b>02</b> 옆에서 들어 주는 사람</li><li><b>03</b> 나에게 맞는 난이도</li></ul>
</div>
<div class="bar"><span>ENOCH MUSIC ACADEMY · SIHEUNG</span><span>01 / 06</span></div></section>`,
// B: 거대한 1:1 타이포 + 사진이 숫자 사이로
B: `<section class="c B"><div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH NOTE — WHY 1:1</span></div>
<div class="photo"><img src="${IMG}"></div>
<div class="giant">1:1</div>
<div class="txt"><h1>1:1로 배우면<br>빨리 느는 이유,</h1><p class="sub">알고 나면 납득되는 3가지</p></div>
<div class="ft"><span>왜 1:1일까</span><span>01 / 06</span></div></section>`,
// C: 좌우 분할 에디토리얼 — 세로 사진 + 세로 글자 + 우측 제목
C: `<section class="c C"><div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ISSUE — WHY 1:1</span></div>
<div class="photo"><img src="${IMG}"></div>
<div class="vert">ONE TO ONE — ENOCH NOTE</div>
<div class="right"><p class="kick">THE LESSON</p><p class="num">3</p><h1>1:1로<br>배우면<br>빨리 느는<br>이유</h1><p class="sub">알고 나면<br>납득되는 3가지</p></div>
<div class="ft"><span>왜 1:1일까</span><span>01 / 06</span></div></section>`,
};
const CSS = `
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}
:root{--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace}
*{margin:0;padding:0;box-sizing:border-box}
.c{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:P,sans-serif;word-break:keep-all;background:${IV};color:${BK}}
img{display:block}
.hd,.ft,.row,.bar{position:absolute;left:72px;right:72px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2.4px}
.hd{top:56px;padding-bottom:16px;border-bottom:2px solid currentColor}.ft{bottom:56px;padding-top:16px;border-top:2px solid currentColor}
.gray{filter:grayscale(1) contrast(1.08)}
/* A */
.A{background:${BK};color:${IV}}
.A .bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.1) brightness(.85)}
.A .shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.55) 0%,rgba(0,0,0,0) 28%,rgba(0,0,0,0) 45%,rgba(0,0,0,.85) 78%,rgba(0,0,0,.92) 100%)}
.A .mast{position:absolute;left:58px;top:40px;font-size:268px;font-weight:700;letter-spacing:-12px;line-height:.9}
.A .row{top:300px;padding-top:14px;border-top:2px solid ${IV}}
.A .lines{position:absolute;left:72px;right:72px;bottom:120px}
.A .kick{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:#bbb;margin-bottom:16px}
.A h1{font-size:76px;line-height:1.15;font-weight:700;letter-spacing:-2px}
.A .sub{font-size:36px;font-weight:300;margin-top:14px;color:#ddd}
.A ul{list-style:none;display:flex;gap:28px;margin-top:34px;padding-top:18px;border-top:1px solid rgba(241,237,228,.5);font-size:22px;color:#ddd}
.A ul b{font-family:var(--mono);font-weight:400;margin-right:6px;color:#999}
.A .bar{bottom:56px;font-size:18px;color:#aaa}
/* B */
.B .photo{position:absolute;left:72px;right:72px;top:118px;height:640px;overflow:hidden}
.B .photo img{width:100%;height:100%;object-fit:cover;object-position:50% 35%;filter:grayscale(1) contrast(1.08)}
.B .giant{position:absolute;left:52px;top:800px;font-size:360px;font-weight:700;letter-spacing:-18px;line-height:.8;color:${BK}}
.B .txt{position:absolute;left:600px;right:72px;top:830px}
.B h1{font-size:50px;line-height:1.2;font-weight:700;letter-spacing:-1px}
.B .sub{font-size:28px;font-weight:300;margin-top:14px;color:#444}
/* C */
.C .photo{position:absolute;left:72px;top:118px;width:560px;height:1120px;overflow:hidden}
.C .photo img{width:100%;height:100%;object-fit:cover;object-position:45% 50%;filter:grayscale(1) contrast(1.08)}
.C .vert{position:absolute;left:652px;top:118px;writing-mode:vertical-rl;font-family:var(--mono);font-size:18px;letter-spacing:4px;color:${GY}}
.C .right{position:absolute;left:700px;right:72px;top:118px;bottom:120px;display:flex;flex-direction:column;justify-content:flex-end}
.C .kick{font-family:var(--mono);font-size:18px;letter-spacing:3px;color:${GY}}
.C .num{font-size:200px;font-weight:700;line-height:.9;letter-spacing:-8px;margin:8px 0 24px}
.C h1{font-size:56px;line-height:1.18;font-weight:700;letter-spacing:-1.5px}
.C .sub{font-size:26px;font-weight:300;margin-top:20px;color:#444;line-height:1.4;padding-top:18px;border-top:2px solid ${BK}}
`;
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${CSS}</style></head><body>${Object.values(covers).join("")}</body></html>`;
writeFileSync(path.join(dir, "cover.html"), html);
const { chromium } = require("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto("file://" + path.join(dir, "cover.html")); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(400);
const els = await p.$$(".c"); const keys = Object.keys(covers);
for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: path.join(dir, `cover_${keys[i]}.png`) });
await b.close(); console.log("covers", keys.join(" "));
