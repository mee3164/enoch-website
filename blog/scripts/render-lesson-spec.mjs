#!/usr/bin/env node
// THE ENOCH LESSON — 레슨 명세서 (1080×1350). 포장 전략: blog/PACKAGING.md
// 사용법: node blog/scripts/render-lesson-spec.mjs → blog/assets/academy/lesson-spec.png
// 항목은 GUIDE 1번의 확인된 사실만. 새 사실이 확인되면 ROWS에 추가한다.
import { writeFile, readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const out = path.join(root, "blog/assets/academy/lesson-spec.png");
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;

const ROWS = [
  ["1:1", "Private", "선생님 한 명, 학생 한 명.<br>모든 과정이 1:1 레슨입니다."],
  ["원칙", "Principles", "진도보다 이해를 먼저 봅니다.<br>같은 곡도, 사람마다 다르게 가르칩니다.<br>기본은 건너뛰지 않습니다."],
  ["소리 기록", "Recording", "보컬 레슨에서는 녹음해서<br>내 소리를 직접 들어 봅니다."],
  ["장비", "Equipment", "콘덴서 마이크 · 팝필터 · 헤드폰 · 스피커"],
  ["연습실", "Practice Room", "수강생은 운영시간 안에 하루 1회,<br>1시간 자유롭게 이용합니다."],
  ["첫 만남", "First Lesson", "1:1 체험 레슨 40분.<br>기타는 학원 기타로, 드럼은 스틱을 빌려 드립니다."],
];

const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1350px; padding: 80px 88px 72px; background: #F1EDE4; color: #111; display: flex; flex-direction: column; }
.top { display: flex; justify-content: space-between; font-size: 15px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; padding-bottom: 16px; border-bottom: 1px solid #111; }
.en { margin-top: 56px; font-size: 17px; font-weight: 500; letter-spacing: 6px; text-transform: uppercase; color: #8A8A8A; }
h1 { margin-top: 14px; font-size: 92px; font-weight: 800; letter-spacing: -4px; line-height: 1; }
.lead { margin-top: 22px; font-size: 34px; font-weight: 300; letter-spacing: -1px; }
.list { margin-top: 44px; border-top: 1px solid #111; }
.row { display: grid; grid-template-columns: 64px 220px 1fr; padding: 22px 0; border-bottom: 1px solid rgba(17,17,17,.2); align-items: start; }
.n { font-size: 14px; font-weight: 500; letter-spacing: 2px; color: #8A8A8A; padding-top: 6px; }
.k b { display: block; font-size: 25px; font-weight: 700; letter-spacing: -.5px; }
.k i { display: block; font-style: normal; margin-top: 4px; font-size: 12px; font-weight: 500; letter-spacing: 3px; text-transform: uppercase; color: #8A8A8A; }
.v { font-size: 21px; line-height: 1.6; color: #2E2C29; padding-top: 1px; }
.foot { margin-top: auto; padding-top: 28px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 15px; color: #8A8A8A; letter-spacing: .5px; line-height: 1.7; }
.foot b { color: #111; font-weight: 600; }
</style></head><body><section class="page">
  <div class="top"><span>${brand.nameEn}</span><span>Lesson Spec</span></div>
  <div class="en">The ENOCH Lesson</div>
  <h1>레슨 한 번에<br>담긴 것</h1>
  <div class="lead">${brand.signature}</div>
  <div class="list">
    ${ROWS.map(([k, e, v], i) => `<div class="row"><div class="n">${String(i + 1).padStart(2, "0")}</div><div class="k"><b>${k}</b><i>${e}</i></div><div class="v">${v}</div></div>`).join("")}
  </div>
  <div class="foot"><span>Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡<br>${brand.address}</span><span><b>${brand.phone}</b></span></div>
</section></body></html>`;

const tmp = path.join(os.tmpdir(), "enoch-lesson-spec.html");
await writeFile(tmp, html);
const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
await (await p.$("section.page")).screenshot({ path: out });
await browser.close();
console.log(path.relative(root, out));
