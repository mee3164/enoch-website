// 오늘은 한 칸 — 30칸 달력이 장마다 채워지는 카드뉴스 (1080×1350 × 6)
// node output/노트_오늘은한칸/gen.mjs → deck.html + 01.png ~ 06.png
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createRequire } from "node:module";

const dir = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(dir, "../../package.json"));
const brand = require("./templates/brand.json");
const TOTAL = 6;
const IV = "#F1EDE4", BK = "#111", GY = "#8A8A8A", SAGE = "#DCE2D3";

// ── 달력 칸 ─────────────────────────────
// state: 1 채운 날 · 0 빈 날 · 2 잘 안 된 날(빗금) · 3 오늘(굵은 테두리)
function grid({ x, y, count = 30, cell = 104, gap = 14, cols = 6, states = [], ink = BK, fill = SAGE, ring = [], num = true }) {
  let s = `<g transform="translate(${x} ${y})" filter="url(#wob)">`;
  for (let i = 0; i < count; i++) {
    const cx = (i % cols) * (cell + gap), cy = Math.floor(i / cols) * (cell + gap);
    const st = states[i] ?? 0;
    const j = ((i * 37) % 7) - 3; // 칸마다 조금씩 다른 손 떨림
    const box = `M${cx + 1} ${cy + j * 0.4} L${cx + cell - 1 + j * 0.3} ${cy + 1} L${cx + cell} ${cy + cell - 1 - j * 0.3} L${cx - j * 0.2} ${cy + cell} Z`;
    if (st === 1) s += `<path d="${box}" fill="${fill}" stroke="none"/>`;
    s += `<path d="${box}" fill="none" stroke="${ink}" stroke-width="${st === 3 ? 6 : 2.5}" stroke-linejoin="round"/>`;
    const MIN = [20, 15, 30, 10, 25, 20, 40, 15, 30, 20, 10, 25];
    if (st === 1) s += `<text x="${cx + cell / 2}" y="${cy + cell * 0.72}" text-anchor="middle" font-size="${cell * 0.4}" fill="${ink}" font-family="'Nanum Pen Script'">${MIN[(i * 5) % MIN.length]}분</text>`;
    if (st === 2) {
      let h = "";
      for (let k = 1; k < 6; k++) h += `M${cx + (cell * k) / 6} ${cy + 6} L${cx + 6} ${cy + (cell * k) / 6} `;
      for (let k = 1; k < 6; k++) h += `M${cx + cell - 6} ${cy + (cell * k) / 6} L${cx + (cell * k) / 6} ${cy + cell - 6} `;
      s += `<path d="${h}" stroke="${GY}" stroke-width="2.5" fill="none" stroke-linecap="round"/>`;
      s += `<rect x="${cx + cell * 0.22}" y="${cy + cell * 0.42}" width="${cell * 0.56}" height="${cell * 0.38}" fill="${IV}"/><text x="${cx + cell / 2}" y="${cy + cell * 0.72}" text-anchor="middle" font-size="${cell * 0.4}" fill="${GY}" font-family="'Nanum Pen Script'">5분</text>`;
    }
    if (num) s += `<text x="${cx + 10}" y="${cy + 24}" font-size="17" fill="${GY}" font-family="var(--mono)">${i + 1}</text>`;
    if (ring.includes(i)) s += `<ellipse cx="${cx + cell / 2}" cy="${cy + cell / 2}" rx="${cell * 0.78}" ry="${cell * 0.72}" fill="none" stroke="${ink}" stroke-width="4" transform="rotate(-8 ${cx + cell / 2} ${cy + cell / 2})"/>`;
  }
  return s + "</g>";
}
const S = (str) => [...str].map((c) => ({ "#": 1, ".": 0, "~": 2, "o": 3 })[c]).filter((v) => v !== undefined);

const HEAD = `<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH NOTE — PRACTICE</span></div>`;
const FOOT = (n) => `<div class="ft"><span>오늘의 연습, 한 칸</span><span>0${n} / 0${TOTAL}</span></div>`;
const svg = (all) => { const ds = all.match(/<svg class="doodle"[\s\S]*?<\/svg>/g) || []; let inner = all; ds.forEach((d) => (inner = inner.replace(d, ""))); return `<svg class="art" viewBox="0 0 1080 1350" width="1080" height="1350">
<defs><filter id="wob" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="4"/></filter></defs>${inner}</svg>${ds.join("")}`; };
// 6칸 × 5줄 = 756 × 616 → 가운데 정렬 x 162
const GX = 193, GY0 = 470;

const cards = [];
// 01 표지
cards.push(`<section class="c">${svg(
  grid({ x: GX, y: 520, states: S("o"), ring: [] }) + `<text x="${GX + 52}" y="${520 + 75}" text-anchor="middle" font-size="42" fill="${BK}" font-family="'Nanum Pen Script'" filter="url(#wob)">10분</text>`
)}${HEAD}
<p class="kick">Practice Log</p>
<h1 class="big">오늘의 연습,<br>한 칸.</h1>
<p class="sub">매일의 연습이 쌓여, 내가 됩니다.</p>
${FOOT(1)}</section>`);

// 02 빠진 날
cards.push(`<section class="c">${svg(
  grid({ x: GX, y: GY0, states: S("###.##.##o"), ring: [3, 6] })
)}${HEAD}
<p class="kick">Missed Days</p>
<h2>빠진 날이 있어도,<br>채운 칸은<br>지워지지 않습니다.</h2>
<p class="body">어제 연습을 못 했다면, 오늘 한 칸이면 돼요.</p>
${FOOT(2)}</section>`);

// 03 잘 안 된 날
cards.push(`<section class="c">${svg(
  grid({ x: GX, y: GY0, states: S("###.##.####~##o"), ring: [11] })
)}${HEAD}
<p class="kick">On Shaky Days</p>
<h2>잘 안 된 날도<br>한 칸입니다.</h2>
<p class="body">그날도 악기 앞에 앉았으니까요.<br>빗금 친 칸도, 쌓인 칸입니다.</p>
${FOOT(3)}</section>`);

// 04 속도는 사람마다 — 달력 두 개
const small = (x, y, st, label) =>
  grid({ x, y, cell: 62, gap: 8, states: S(st), num: false }) +
  `<text x="${x}" y="${y - 22}" font-size="24" font-family="var(--mono)" letter-spacing="3" fill="${GY}">${label}</text>`;
cards.push(`<section class="c">${svg(
  small(96, 520, "##.#.##.#.##.##o", "MY DAYS") +
  small(572, 520, "######.#####.###~##o", "SOMEONE ELSE")
)}${HEAD}
<p class="kick">Your Own Pace</p>
<h2>칸을 채우는 속도는<br>사람마다 다릅니다.</h2>
<p class="body">비교는 어제의 내 칸과만.<br>같은 곡도, 사람마다 다르게 가르치는 이유.</p>
${FOOT(4)}</section>`);

// 05 한 달 뒤
cards.push(`<section class="c">${svg(
  grid({ x: GX, y: GY0, states: S("###.##.####~########.####~###o") })
)}${HEAD}
<p class="kick">A Month Later</p>
<h2>한 달 뒤,<br>이만큼.</h2>
<p class="body"><b>지금, 잘하고 있어요.</b></p>
${FOOT(5)}</section>`);

// 06 마무리 (검정) — 사진 한 장
cards.push(`<section class="c dark">${svg(
  grid({ x: 860, y: 640, count: 1, cell: 120, cols: 1, states: [3], ink: IV, num: false })
)}${HEAD}
<div class="pics"><img src="../../images/기타/라이프_악보카페_02.jpg" style="object-position:50% 32%"></div>
<h2 class="close">하루 한 칸을<br>채울 자리.</h2>
<p class="body">ENOCH 수강생은 운영시간 안에 연습실을 자유롭게 이용할 수 있습니다.<br>같은 곡도, 사람마다 다르게 가르칩니다.</p>
<div class="info"><div><p>${brand.name}</p><p>${brand.address}</p></div><div class="r"><p class="tel">${brand.phone}</p><p>${brand.subjects}</p></div></div>
${FOOT(6)}</section>`);

const CSS = `
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}
:root{--mono:"IBM Plex Mono","SF Mono",Menlo,"DejaVu Sans Mono",monospace}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#ccc}
.c{--fg:#111;width:1080px;height:1350px;position:relative;overflow:hidden;background:${IV};color:${BK};font-family:P,sans-serif;word-break:keep-all;margin-bottom:40px}
.c.dark{--fg:#F1EDE4;background:${BK};color:${IV}}
.art{position:absolute;inset:0}
.hd,.ft{position:absolute;left:96px;right:96px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2.4px}
.hd{top:64px;padding-bottom:18px;border-bottom:2px solid currentColor}
.ft{bottom:64px;padding-top:18px;border-top:2px solid currentColor}
.kick{position:absolute;left:96px;top:150px;font-family:var(--mono);font-size:21px;letter-spacing:3.2px;color:${GY};text-transform:uppercase}
.big{position:absolute;left:96px;top:196px;font-size:118px;line-height:1.08;font-weight:700;letter-spacing:-3px}
.sub{position:absolute;left:520px;top:340px;font-size:34px;font-weight:400;color:#555}
h2{position:absolute;left:96px;top:196px;font-size:60px;line-height:1.28;font-weight:700;letter-spacing:-1.5px}
.body{position:absolute;left:96px;top:1225px;font-size:28px;line-height:1.6;color:#555;font-weight:400}
.body b{color:${BK};font-weight:700;font-size:34px}
.c .body{top:1090px}
.dark .ghost{position:absolute;left:84px;top:110px;font-size:250px;font-weight:700;letter-spacing:-8px;color:#222}
.dark h2.close{top:640px}\n.pics{position:absolute;left:96px;right:96px;top:140px;height:440px;display:grid;grid-template-columns:1fr;gap:0}.pics img{width:100%;height:440px;display:block;object-fit:cover;filter:saturate(.7) contrast(1.02)}
.dark .body{top:830px;bottom:auto;color:#bbb;font-size:30px}
.info{position:absolute;left:96px;right:96px;bottom:150px;display:flex;justify-content:space-between;font-size:20px;color:#bbb;line-height:1.7;border-top:1px solid #444;padding-top:20px}
.info .r{text-align:right}.info .tel{font-family:var(--mono);font-size:24px;color:${IV};letter-spacing:2px}
`;
writeFileSync(path.join(dir, "deck.html"), `<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>오늘은 한 칸</title><link rel="stylesheet" href="../../templates/fonts/nanum-pen-script/400.css"><style>${CSS}</style></head><body>${cards.join("\n")}</body></html>`);

const { chromium } = require("playwright");
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await page.goto("file://" + path.join(dir, "deck.html"));
await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(500);
const els = await page.$$(".c");
for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: path.join(dir, `0${i + 1}.png`) });
await browser.close();
console.log(`deck.html + ${els.length} PNG`);
