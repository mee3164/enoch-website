// 1:1로 배우면 빨리 느는 이유, 알고 나면 납득되는 3가지 (1080×1350 × 6)
// node output/노트_왜1대1/gen.mjs → deck.html + 01.png ~ 06.png
// 사진: src/ (레슨 영상에서 얼굴이 나오지 않게 자른 장면 — 공개 저장소에는 올리지 않음)
import { writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createRequire } from "node:module";

const dir = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(dir, "../../package.json"));
const brand = require("./templates/brand.json");
const TOTAL = 6;
const IV = "#F1EDE4", BK = "#111", GY = "#8A8A8A", MIST = "#D9E1E8";

const HEAD = (r) => `<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>${r}</span></div>`;
const FOOT = (n) => `<div class="ft"><span>왜 1:1일까</span><span>0${n} / 0${TOTAL}</span></div>`;

// 종 모양 두 개 (개념도) — 교실 평균 vs 1:1 평균
function bells() {
  const W = 888, H = 300, base = 270;
  const curve = (mu, sd, amp) => {
    let d = "";
    for (let x = 0; x <= W; x += 6) {
      const y = base - amp * Math.exp(-((x - mu) ** 2) / (2 * sd * sd));
      d += (x ? " L" : "M") + x + " " + y.toFixed(1);
    }
    return d;
  };
  const sd = 90, a = 300, b = 480;
  return `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">
    <path d="${curve(a, sd, 220)} L${W} ${base} L0 ${base} Z" fill="none" stroke="${GY}" stroke-width="3"/>
    <path d="${curve(b, sd, 220)}" fill="none" stroke="${BK}" stroke-width="5"/>
    <path d="${curve(b, sd, 220)} L${W} ${base} L0 ${base} Z" fill="${MIST}" opacity=".7"/>
    <line x1="0" y1="${base}" x2="${W}" y2="${base}" stroke="${BK}" stroke-width="2"/>
    <line x1="${a}" y1="${base}" x2="${a}" y2="40" stroke="${GY}" stroke-width="2" stroke-dasharray="6 6"/>
    <line x1="${b}" y1="${base}" x2="${b}" y2="40" stroke="${BK}" stroke-width="2" stroke-dasharray="6 6"/>
    <text x="${a - 12}" y="30" text-anchor="end" font-size="22" fill="${GY}">교실 수업 평균</text>
    <text x="${b + 12}" y="30" font-size="22" fill="${BK}" font-weight="700">1:1 평균</text>
    <path d="M${a + 10} 140 L${b - 14} 140 M${b - 26} 130 L${b - 12} 140 L${b - 26} 150" stroke="${BK}" stroke-width="3" fill="none"/>
  </svg>`;
}

// 난이도-배움 곡선 (개념도) — 사람마다 다른 정점
function hills() {
  const W = 888, H = 300, base = 250;
  const hill = (mu, color, w) => {
    let d = "";
    for (let x = 0; x <= W; x += 6) {
      const y = base - 190 * Math.exp(-((x - mu) ** 2) / (2 * 120 * 120));
      d += (x ? " L" : "M") + x + " " + y.toFixed(1);
    }
    return `<path d="${d}" fill="none" stroke="${color}" stroke-width="${w}"/>`;
  };
  return `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H + 40}">
    ${hill(300, GY, 3)}${hill(590, BK, 5)}
    <circle cx="300" cy="${base - 190}" r="10" fill="${GY}"/><circle cx="590" cy="${base - 190}" r="12" fill="${BK}"/>
    <text x="300" y="${base - 210}" text-anchor="middle" font-size="22" fill="${GY}">A에게 알맞은 난이도</text>
    <text x="590" y="${base - 210}" text-anchor="middle" font-size="22" fill="${BK}" font-weight="700">B에게 알맞은 난이도</text>
    <line x1="0" y1="${base}" x2="${W}" y2="${base}" stroke="${BK}" stroke-width="2"/>
    <text x="0" y="${base + 34}" font-size="20" fill="${GY}" font-family="var(--mono)">EASY</text>
    <text x="${W}" y="${base + 34}" text-anchor="end" font-size="20" fill="${GY}" font-family="var(--mono)">HARD</text>
  </svg>`;
}

const cards = [];
// 01 표지 — 사진 전면, 글자는 덜어낸 버전
cards.push(`<section class="c dark cov">
<img class="bgfull" src="src/cover_full.jpg"><div class="shade"></div>
${HEAD("ENOCH NOTE — WHY 1:1")}
<h1 class="covt">1:1로 배우면<br>빨리 느는 이유,</h1>
<p class="covs">알고 나면 납득되는 3가지</p>
${FOOT(1)}</section>`);

// 02 블룸
cards.push(`<section class="c">${HEAD("STUDY 01 — ONE TO ONE")}
<p class="kick">Study 01</p>
<p class="num">98<span>%</span></p>
<h2>1:1로 배운 학생의 평균이,<br>교실 수업 학생의 98%보다 높았습니다.</h2>
<div class="fig">${bells()}</div>
<p class="note">Bloom (1984) · 개념도 — 측정 그래프가 아닙니다.<br>후속 연구들에선 차이가 이보다 작게 나왔지만, 1:1 튜터링의 효과는 꾸준히 확인됩니다.</p>
${FOOT(2)}</section>`);

// 03 피드백
cards.push(`<section class="c">${HEAD("STUDY 02 — FEEDBACK")}
<p class="kick">Study 02</p>
<h2 class="big2">혼자서는 들리지 않는 것을,<br>옆에서 들어 주는 사람.</h2>
<img class="hand" src="src/hand.jpg">
<p class="body">배움에 영향을 주는 요인을 모아 본 연구에서, 피드백은 효과가 큰 쪽에 꼽힙니다. 특히 <b>무엇을, 어떻게 고칠지</b> 알려 주는 피드백이 효과가 컸어요.</p>
<p class="note n3">Hattie &amp; Timperley (2007) · 196개 연구를 모은 분석</p>
${FOOT(3)}</section>`);

// 04 난이도
cards.push(`<section class="c">${HEAD("STUDY 03 — CHALLENGE POINT")}
<p class="kick">Study 03</p>
<h2 class="big2">너무 쉬우면 늘지 않고,<br>너무 어려우면 무너집니다.</h2>
<div class="fig f4">${hills()}</div>
<p class="body b4">배우기 가장 좋은 난이도는 그 사람의 실력에 따라 다르다는 이론이 있습니다. 실력이 늘면, 알맞은 난이도도 함께 옮겨 가요.</p>
<p class="note n4">Guadagnoli &amp; Lee (2004) · 운동 학습 이론 · 개념도</p>
${FOOT(4)}</section>`);

// 05 정리 (검정)
cards.push(`<section class="c dark">${HEAD("SUMMARY")}
<p class="kick">Summary</p>
<h2 class="big2">세 가지를<br>한 사람에게 맞추는 방식.</h2>
<ol class="sum">
<li><span>01</span><div><b>한 사람만 보는 시간</b><p>수업 내내 시선이 한 사람에게 있습니다.</p></div></li>
<li><span>02</span><div><b>그 자리에서 고치는 피드백</b><p>틀린 곳을 연습이 굳기 전에 바로잡을 수 있어요.</p></div></li>
<li><span>03</span><div><b>그 사람에게 맞는 난이도</b><p>같은 곡도, 사람마다 다른 지점에서 시작합니다.</p></div></li>
</ol>
<p class="note n5">위 연구는 일반 학습·운동 학습 연구입니다.</p>
${FOOT(5)}</section>`);

// 06 마무리 (검정)
cards.push(`<section class="c dark">${HEAD("THE ENOCH WAY")}
<p class="ghost">ENOCH</p>
<h2 class="close">같은 곡도,<br>사람마다 다르게 가르칩니다.</h2>
<p class="body b6">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡<br><b>모든 과정 1:1 레슨.</b></p>
<div class="info"><div><p>${brand.name}</p><p>${brand.address}</p></div><div class="r"><p class="tel">${brand.phone}</p><p>${brand.hours}</p></div></div>
${FOOT(6)}</section>`);

const CSS = `
.cov .hd,.cov .ft,.cov .covt,.cov .covs{z-index:2}
.bgfull{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;filter:grayscale(1) contrast(1.05) brightness(.92)}
.shade{position:absolute;inset:0;background:linear-gradient(180deg,rgba(17,17,17,.45) 0%,rgba(17,17,17,0) 20%,rgba(17,17,17,0) 52%,rgba(17,17,17,.82) 82%)}
.covt{position:absolute;left:96px;bottom:250px;font-size:76px;line-height:1.2;font-weight:700;letter-spacing:-2px}
.covs{position:absolute;left:96px;bottom:180px;font-size:36px;font-weight:300;color:#ddd}

@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}
:root{--mono:"IBM Plex Mono","SF Mono",Menlo,"DejaVu Sans Mono",monospace}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#ccc}
svg text{font-family:P,sans-serif}
.c{width:1080px;height:1350px;position:relative;overflow:hidden;background:${IV};color:${BK};font-family:P,sans-serif;word-break:keep-all;margin-bottom:40px}
.c.dark{background:${BK};color:${IV}}
.hd,.ft{position:absolute;left:96px;right:96px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2.4px}
.hd{top:64px;padding-bottom:18px;border-bottom:2px solid currentColor}
.ft{bottom:64px;padding-top:18px;border-top:2px solid currentColor}
.kick{position:absolute;left:96px;top:150px;font-family:var(--mono);font-size:21px;letter-spacing:3.2px;color:${GY};text-transform:uppercase}
.cover{position:absolute;left:96px;top:130px;width:888px;height:700px;object-fit:cover;object-position:50% 40%;filter:grayscale(.85) sepia(.15) contrast(1.05)}
.k1{top:870px}
h1{position:absolute;left:96px;top:912px;font-size:76px;line-height:1.2;font-weight:700;letter-spacing:-2px}
.h1sub{position:absolute;left:96px;top:1110px;font-size:40px;font-weight:300;color:#444}
.num{position:absolute;left:90px;top:186px;font-size:200px;font-weight:700;letter-spacing:-8px;line-height:1}
.num span{font-size:110px}
h2{position:absolute;left:96px;top:410px;font-size:46px;line-height:1.35;font-weight:700;letter-spacing:-1px}
.big2{top:196px;font-size:60px;line-height:1.28;letter-spacing:-1.5px}
.fig{position:absolute;left:96px;top:600px}
.f4{top:450px}
.note{position:absolute;left:96px;right:96px;top:950px;font-size:22px;line-height:1.7;color:${GY}}
.hand{position:absolute;left:96px;top:420px;width:888px;height:430px;object-fit:cover;object-position:50% 40%;filter:grayscale(.85) sepia(.15) contrast(1.05)}
.body{position:absolute;left:96px;right:96px;top:890px;font-size:30px;line-height:1.65;color:#444;font-weight:400}
.body b{color:${BK};font-weight:700}
.n3{top:1150px}
.b4{top:860px}.n4{top:1150px}
.dark .body{color:#bbb}.dark .body b{color:${IV}}
.sum{position:absolute;left:96px;right:96px;top:470px;list-style:none;border-top:1px solid #444}
.sum li{display:grid;grid-template-columns:90px 1fr;padding:30px 0;border-bottom:1px solid #444}
.sum span{font-family:var(--mono);font-size:22px;color:${GY};padding-top:6px}
.sum b{font-size:36px;font-weight:700}
.sum p{font-size:26px;color:#aaa;margin-top:8px;font-weight:300}
.n5{top:1150px;color:#777}
.ghost{position:absolute;left:84px;top:110px;font-size:250px;font-weight:700;letter-spacing:-8px;color:#222}
.dark h2.close{top:470px;font-size:60px;line-height:1.3}
.b6{top:700px}
.info{position:absolute;left:96px;right:96px;bottom:150px;display:flex;justify-content:space-between;font-size:20px;color:#bbb;line-height:1.7;border-top:1px solid #444;padding-top:20px}
.info .r{text-align:right}.info .tel{font-family:var(--mono);font-size:24px;color:${IV};letter-spacing:2px}
`;
writeFileSync(path.join(dir, "deck.html"), `<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>왜 1:1일까</title><style>${CSS}</style></head><body>${cards.join("\n")}</body></html>`);

const { chromium } = require("playwright");
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await page.goto("file://" + path.join(dir, "deck.html"));
await page.evaluate(() => document.fonts.ready); await page.waitForTimeout(500);
const els = await page.$$(".c");
for (let i = 0; i < els.length; i++) await els[i].screenshot({ path: path.join(dir, `0${i + 1}.png`) });
await browser.close();
console.log(`deck.html + ${els.length} PNG`);
