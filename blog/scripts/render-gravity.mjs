#!/usr/bin/env node
// 009 「박자는 맞는데, 왜 느낌이 안 살까요? — 정박의 중력」 블로그용 카드 4장 (1080×1350)
// 사용법: node blog/scripts/render-gravity.mjs  → blog/posts/009/images/card-01.png ~ card-04.png
import { writeFile, mkdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { doodle } from "../../scripts/doodles.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const outDir = path.join(root, "blog/posts/009/images");
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;
const P = "#D9E1E8"; // 미스트
const TOTAL = 4;

const css = `
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; background: #555; }
.page { width: 1080px; height: 1350px; padding: 72px 80px 64px; background: #F1EDE4; color: #111; position: relative; display: flex; flex-direction: column; overflow: hidden; margin-bottom: 40px; }
.head { display: flex; justify-content: space-between; font-size: 18px; font-weight: 500; letter-spacing: 2.6px; text-transform: uppercase; padding-bottom: 18px; border-bottom: 2px solid #111; }
.kicker { font-size: 22px; font-weight: 600; color: #6E6A64; margin-top: 56px; }
.title { font-size: 66px; font-weight: 800; letter-spacing: -2.4px; line-height: 1.24; margin-top: 14px; white-space: pre-line; }
.lead { font-size: 28px; color: #55524D; margin-top: 22px; line-height: 1.6; white-space: pre-line; }
.foot { margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end; font-size: 18px; color: #6E6A64; letter-spacing: 1px; }
.band { margin: 44px -80px 0; padding: 44px 80px; background: ${P}; }
/* cover */
.cover .title { font-size: 84px; letter-spacing: -3.4px; margin-top: 40px; }
.cover .sub { font-size: 30px; font-weight: 500; color: #3B3833; margin-top: 30px; line-height: 1.6; }
.cover .tag { margin-top: 26px; font-size: 24px; font-weight: 700; letter-spacing: 1px; }
/* checklist */
.checks { list-style: none; }
.checks li { position: relative; padding: 26px 0 26px 64px; border-bottom: 1.5px solid rgba(17,17,17,.6); font-size: 34px; font-weight: 700; line-height: 1.45; }
.checks li:first-child { border-top: 1.5px solid rgba(17,17,17,.6); }
.checks li::before { content: ""; position: absolute; left: 0; top: 34px; width: 34px; height: 34px; border: 2.5px solid #111; background: #F1EDE4; }
.checks li::after { content: ""; position: absolute; left: 9px; top: 38px; width: 12px; height: 22px; border: solid #111; border-width: 0 4px 4px 0; transform: rotate(45deg); }
.note { margin-top: 30px; font-size: 26px; color: #3B3833; line-height: 1.6; }
/* steps */
.step { display: grid; grid-template-columns: 96px 1fr; gap: 20px; padding: 26px 0; border-bottom: 1.5px solid rgba(17,17,17,.55); }
.step:first-child { border-top: 1.5px solid rgba(17,17,17,.55); }
.step .n { font-size: 56px; font-weight: 800; line-height: 1; }
.step h3 { font-size: 32px; font-weight: 800; }
.step p { font-size: 23px; line-height: 1.6; margin-top: 8px; color: #2E2C29; }
.step .ok { margin-top: 10px; font-size: 21px; font-weight: 700; color: #3B3833; }
.kung { display: inline-flex; align-items: baseline; gap: 14px; margin-top: 8px; }
.kung b { font-size: 34px; font-weight: 900; } .kung i { font-style: normal; font-size: 20px; font-weight: 500; color: #55524D; }
`;

const head = (i) => `<div class="head"><span>${brand.nameEn}</span><span>Rhythm · Gravity of the Beat</span></div>`;
const foot = (i) => `<div class="foot"><span>${brand.name}</span><span>${String(i).padStart(2, "0")} / ${String(TOTAL).padStart(2, "0")}</span></div>`;

// 3장 개념도: 정박(큰 원)과 사이 음(작은 원)이 다음 정박으로 끌려가는 그림
function gravitySvg() {
  const W = 920, H = 470, y = 250, beats = [90, 460, 830];
  let g = `<line x1="40" y1="${y}" x2="${W - 40}" y2="${y}" stroke="#111" stroke-width="2"/>`;
  beats.forEach((x, i) => {
    g += `<circle cx="${x}" cy="${y}" r="46" fill="#111"/><text x="${x}" y="${y + 9}" text-anchor="middle" font-size="26" font-weight="800" fill="#F1EDE4">쿵</text>`;
    g += `<text x="${x}" y="${y + 100}" text-anchor="middle" font-size="24" font-weight="700" fill="#111">정박</text>`;
    if (i < beats.length - 1) {
      const nx = beats[i + 1];
      [0.27, 0.5, 0.73].forEach((t, k) => {
        const sx = x + (nx - x) * t;
        const r = 15 + k * 3; // 다음 정박에 가까울수록 조금씩 끌려가는 느낌
        g += `<circle cx="${sx}" cy="${y}" r="${r}" fill="${P}" stroke="#111" stroke-width="2.5"/>`;
        g += `<text x="${sx}" y="${y + 6}" text-anchor="middle" font-size="16" font-weight="700" fill="#111">따</text>`;
      });
      // 다음 정박으로 끌려가는 화살표 (곡선)
      const cx = (x + nx) / 2;
      g += `<path d="M ${x + 60} ${y - 70} Q ${cx} ${y - 170} ${nx - 62} ${y - 64}" fill="none" stroke="#111" stroke-width="3" stroke-dasharray="2 10" stroke-linecap="round"/>`;
      g += `<path d="M ${nx - 62} ${y - 64} l -22 -6 m 22 6 l -10 -20" fill="none" stroke="#111" stroke-width="3" stroke-linecap="round"/>`;
      g += `<text x="${cx}" y="${y + 100}" text-anchor="middle" font-size="22" font-weight="500" fill="#55524D">사이 음</text>`;
    }
  });
  return `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${g}</svg>`;
}

const pages = [
  // 1. 표지
  `<section class="page cover">${head(1)}
    <div class="kicker">리듬감 · 정박의 중력</div>
    <div class="title">박자는 맞는데,\n왜 느낌이\n안 살까요?</div>
    <div class="sub">메트로놈에 정확히 맞췄는데도<br>"딱딱하다"는 말을 들을 때.</div>
    <div class="band" style="margin-top:60px"><div class="tag">답은 박의 정확도보다, 음의 '무게'에 있어요.</div></div>
    <div style="margin-top:auto;margin-bottom:40px;display:flex;align-items:center;gap:26px">
      <span style="width:96px;height:96px;border-radius:50%;background:#111;color:#F1EDE4;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:800">쿵</span>
      ${[0,1,2].map(() => '<span style="width:44px;height:44px;border-radius:50%;background:' + P + ';border:2.5px solid #111;display:flex;align-items:center;justify-content:center;font-size:17px;font-weight:700">따</span>').join("")}
      <span style="width:96px;height:96px;border-radius:50%;background:#111;color:#F1EDE4;display:flex;align-items:center;justify-content:center;font-size:34px;font-weight:800">쿵</span>
      <span style="font-size:22px;color:#55524D;margin-left:10px;line-height:1.5">정박은 무겁게,<br>사이 음은 가볍게</span>
    </div>
    ${doodle({ name: "notes", x: 820, y: 210, size: 150, rotate: -8, color: "#111", fill: P })}
    <div class="foot" style="margin-top:0"><span>${brand.name}</span><span>01 / 04</span></div></section>`,
  // 2. 체크
  `<section class="page">${head(2)}
    <div class="kicker">CHECK</div>
    <div class="title">이런 모습이라면\n리듬의 '무게'를 놓치고 있어요</div>
    <div class="band"><ul class="checks">
      <li>모든 음을 같은 세기, 같은 무게로 친다</li>
      <li>음을 하나씩 찍듯이 쳐서 흐름이 끊긴다</li>
      <li>메트로놈엔 맞는데, 듣기엔 딱딱하다</li>
      <li>강세가 고르게 퍼져, 어디가 정박인지 들리지 않는다</li>
    </ul></div>
    <div class="note">하나라도 해당된다면, 박자보다 무게를 먼저 다시 볼 때예요.</div>
    <div style="margin-top:70px;font-size:40px;font-weight:800;letter-spacing:-1.2px;line-height:1.4">박자는 이미 맞아요.<br>이제 무게를 볼 차례예요.</div>
    ${foot(2)}</section>`,
  // 3. 개념
  `<section class="page">${head(3)}
    <div class="kicker">CONCEPT</div>
    <div class="title">정박의 중력에\n나머지 음이 빨려 들어가요</div>
    <div class="lead">정박은 박이 '쿵' 떨어지는 자리.\n그 사이의 음들은 다음 정박을 향해 끌려가듯 모여들어요.</div>
    <div class="band" style="display:flex;justify-content:center;padding:30px 80px 10px">${gravitySvg()}</div>
    <div class="note">정박은 무겁게 내려앉고, 사이 음은 가볍게 흘러가요.<br>이 무게의 차이에서 그루브가 들리기 시작해요.</div>
    ${foot(3)}</section>`,
  // 4. 연습 3단계
  `<section class="page">${head(4)}
    <div class="kicker">PRACTICE · 메트로놈 60</div>
    <div class="title" style="font-size:58px">몸으로 익히는 3단계</div>
    <div style="margin-top:34px">
      <div class="step"><div class="n">①</div><div><h3>발로</h3>
        <p>한 발에 무게를 싣고 서 있다가, 다음 정박에 다른 발로 무게를 옮겨요. 사이 음 동안 다음 발 쪽으로 천천히 기울고, 정박에 '툭' 내려앉아요.</p>
        <div class="ok">잘 된 것 · 정박마다 몸이 내려앉는 느낌이 메트로놈과 함께 와요</div></div></div>
      <div class="step"><div class="n">②</div><div><h3>발 + 목소리로</h3>
        <p>무게를 옮기면서 한 박을 넷으로 나눠 소리 내요. '쿵'만 크게, '따'는 속삭이듯. 마지막 '따'는 다음 '쿵'으로 기울어지듯 이어요.</p>
        <div class="kung"><b>쿵</b><i>따</i><i>따</i><i>따</i><b>쿵</b></div>
        <div class="ok">잘 된 것 · '따' 세 개가 다음 '쿵'을 향해 굴러가듯 들려요</div></div></div>
      <div class="step"><div class="n">③</div><div><h3>악기로</h3>
        <p>같은 강약을 그대로 옮겨요. 정박은 무겁게, 사이 음은 가볍게, 다음 정박에 '착지'하듯. 녹음해서 들어 봐요.</p>
        <div class="ok">잘 된 것 · 정박이 또렷하고, 사이 음이 그쪽으로 흘러가요</div></div></div>
    </div>
    <div class="band" style="margin-top:36px;padding:30px 80px"><div class="tag" style="font-size:25px;font-weight:700;line-height:1.6">빠르기보다 무게의 차이가 먼저예요.<br>60에서 편해진 뒤에 빠르기를 조금씩 올려요.</div></div>
    ${foot(4)}</section>`,
];

await mkdir(outDir, { recursive: true });
const preview = path.join(outDir, "preview.html");
await writeFile(preview, `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body>${pages.join("\n")}</body></html>`);
const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto(pathToFileURL(preview).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
const els = await p.$$("section.page");
for (let i = 0; i < els.length; i++) {
  const f = path.join(outDir, `card-${String(i + 1).padStart(2, "0")}.png`);
  await els[i].screenshot({ path: f });
  console.log(path.relative(root, f));
}
await browser.close();
