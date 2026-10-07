#!/usr/bin/env node
// ENOCH 블로그 기타 코드 차트 이미지 (1080×1350)
// 사용법: node blog/scripts/render-chords.mjs [출력 경로]  (기본: blog/assets/guitar/chords-basic.png)
// 운지는 표준 오픈 코드. frets: 6번 줄(굵은 E) → 1번 줄(가는 e), x=치지 않음, 0=개방현.
import { writeFile, mkdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { doodle } from "../../scripts/doodles.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const out = path.resolve(process.argv[2] || path.join(root, "blog/assets/guitar/chords-basic.png"));
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;

// fingers: 같은 순서로 손가락 번호 (1 검지, 2 중지, 3 약지, 4 새끼), 0/x 자리는 null
const CHORDS = [
  { name: "C", frets: ["x", 3, 2, 0, 1, 0], fingers: [null, 3, 2, null, 1, null], hl: true },
  { name: "G", frets: [3, 2, 0, 0, 0, 3], fingers: [2, 1, null, null, null, 3], hl: true },
  { name: "D", frets: ["x", "x", 0, 2, 3, 2], fingers: [null, null, null, 1, 3, 2] },
  { name: "Em", frets: [0, 2, 2, 0, 0, 0], fingers: [null, 2, 3, null, null, null] },
  { name: "Am", frets: ["x", 0, 2, 2, 1, 0], fingers: [null, null, 2, 3, 1, null] },
  { name: "E", frets: [0, 2, 2, 1, 0, 0], fingers: [null, 2, 3, 1, null, null] },
  { name: "A", frets: ["x", 0, 2, 2, 2, 0], fingers: [null, null, 1, 2, 3, null] },
  { name: "Dm", frets: ["x", "x", 0, 2, 3, 1], fingers: [null, null, null, 2, 3, 1] },
];

const PASTEL = "#DCE2D3";

// 다이어그램 하나: 가로 6줄(세로선), 4프렛
function diagram(c) {
  const W = 190, H = 230, left = 20, top = 40, gap = (W - left * 2) / 5, fh = (H - top - 14) / 4;
  const x = (i) => left + i * gap;
  let g = "";
  // 프렛선 (맨 위는 굵은 너트)
  for (let f = 0; f <= 4; f++) g += `<line x1="${x(0)}" y1="${top + f * fh}" x2="${x(5)}" y2="${top + f * fh}" stroke="#111" stroke-width="${f === 0 ? 7 : 1.6}"/>`;
  // 줄
  for (let i = 0; i < 6; i++) g += `<line x1="${x(i)}" y1="${top}" x2="${x(i)}" y2="${top + 4 * fh}" stroke="#111" stroke-width="1.6"/>`;
  c.frets.forEach((f, i) => {
    if (f === "x") g += `<text x="${x(i)}" y="${top - 12}" text-anchor="middle" font-size="22" font-weight="600" fill="#111">×</text>`;
    else if (f === 0) g += `<circle cx="${x(i)}" cy="${top - 19}" r="7.5" fill="none" stroke="#111" stroke-width="2"/>`;
    else {
      const cy = top + (f - 0.5) * fh;
      g += `<circle cx="${x(i)}" cy="${cy}" r="14" fill="#111"/>`;
      if (c.fingers[i]) g += `<text x="${x(i)}" y="${cy + 6}" text-anchor="middle" font-size="17" font-weight="700" fill="#F1EDE4">${c.fingers[i]}</text>`;
    }
  });
  return `<div class="chord${c.hl ? " hl" : ""}"><div class="cn">${c.name}</div><svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}">${g}</svg></div>`;
}

const css = `
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #555; font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1350px; padding: 72px 80px 64px; background: #F1EDE4; color: #111; position: relative; display: flex; flex-direction: column; overflow: hidden; }
.head { display: flex; justify-content: space-between; font-size: 18px; font-weight: 500; letter-spacing: 2.6px; text-transform: uppercase; padding-bottom: 18px; border-bottom: 2px solid #111; }
.kicker { font-size: 22px; font-weight: 500; color: #6E6A64; margin-top: 44px; }
.title { font-size: 64px; font-weight: 800; letter-spacing: -2.4px; line-height: 1.2; margin-top: 12px; }
.lead { font-size: 25px; color: #55524D; margin-top: 14px; line-height: 1.55; }
.grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px 0; margin-top: 28px; }
.chord { display: flex; flex-direction: column; align-items: center; padding: 14px 0 6px; }
.chord.hl { background: ${PASTEL}; }
.cn { font-size: 40px; font-weight: 800; letter-spacing: -1px; }
.legend { margin-top: 18px; font-size: 19px; color: #6E6A64; display: flex; gap: 26px; }
.try { margin: 24px -80px 0; padding: 24px 80px; background: ${PASTEL}; }
.try .t { font-size: 21px; font-weight: 700; color: #3B3833; }
.try .b { font-size: 28px; font-weight: 800; margin-top: 10px; line-height: 1.45; }
.try .s { font-size: 21px; color: #55524D; margin-top: 8px; line-height: 1.55; }
.foot { margin-top: auto; padding-top: 26px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 19px; color: #6E6A64; line-height: 1.6; }
.foot b { color: #111; font-size: 22px; }
`;

const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body>
<section class="page">
  <div class="head"><span>${brand.nameEn}</span><span>Guitar Chord Chart</span></div>
  <div class="kicker">${brand.name} · 기타 입문</div>
  <div class="title">처음 익히는 기본 코드 8</div>
  <div class="lead">색으로 표시한 C와 G부터 시작해 보세요.<br>코드 수보다, 한 코드를 깨끗하게 울리는 것이 먼저입니다.</div>
  <div class="grid">${CHORDS.map(diagram).join("")}</div>
  <div class="legend"><span>왼쪽 줄 = 6번(굵은 줄)</span><span>● 안 숫자 = 손가락 (1 검지 · 2 중지 · 3 약지)</span><span>○ 개방현 · × 치지 않음</span></div>
  <div class="try">
    <div class="t">오늘 해 볼 한 가지</div>
    <div class="b">메트로놈 60, G ↔ C 한 코드에 네 박씩 5분</div>
    <div class="s">손끝이 아프면 바로 멈추고 쉬었다가, 짧게 자주 칩니다.</div>
  </div>
  <div class="foot"><div><b>기타 1:1 체험 레슨 40분 · 학원 기타로 체험 가능</b><br>네이버 예약 또는 ${brand.phone} · ${brand.address}</div><div>${brand.signature}</div></div>
  ${doodle({ name: "guitar", x: 860, y: 150, size: 130, rotate: 12, color: "#111", fill: PASTEL })}
</section></body></html>`;

await mkdir(path.dirname(out), { recursive: true });
const tmp = out.replace(/\.png$/, ".html");
await writeFile(tmp, html);
const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
await (await p.$("section.page")).screenshot({ path: out });
await browser.close();
console.log(path.relative(root, out));
