#!/usr/bin/env node
// ENOCH 블로그 '과목·과정 한눈에 보기' 이미지 (1080×1350)
// 사용법: node blog/scripts/render-overview.mjs [출력 경로]  (기본: blog/assets/academy/overview.png)
// 내용은 blog/GUIDE.md 1번 확인 사실만. 규모·방음·수강료는 넣지 않는다.
import { writeFile, mkdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { doodle } from "../../scripts/doodles.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const out = path.resolve(process.argv[2] || path.join(root, "blog/assets/academy/overview.png"));
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;
const PASTEL = "#E3DDE9";
const SUBJECTS = ["보컬", "기타", "드럼", "베이스", "피아노", "미디", "작곡"];
const COURSES = ["입시", "취미", "성인", "전문"];

const css = `
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1350px; padding: 72px 80px 64px; background: #F1EDE4; color: #111; position: relative; display: flex; flex-direction: column; overflow: hidden; }
.head { display: flex; justify-content: space-between; font-size: 18px; font-weight: 500; letter-spacing: 2.6px; text-transform: uppercase; padding-bottom: 18px; border-bottom: 2px solid #111; }
.kicker { font-size: 22px; font-weight: 500; color: #6E6A64; margin-top: 52px; }
.title { font-size: 70px; font-weight: 800; letter-spacing: -2.6px; line-height: 1.18; margin-top: 12px; }
.lead { font-size: 28px; font-weight: 500; color: #3B3833; margin-top: 18px; }
.band { margin: 38px -80px 0; padding: 40px 80px 36px; background: ${PASTEL}; }
.sec { display: grid; grid-template-columns: 150px 1fr; align-items: center; padding: 18px 0; border-bottom: 1.5px solid rgba(17,17,17,.75); }
.sec:first-child { border-top: 1.5px solid rgba(17,17,17,.75); }
.lb { font-size: 22px; font-weight: 700; color: #3B3833; }
.chips { display: flex; flex-wrap: wrap; gap: 10px 12px; }
.chip { font-size: 30px; font-weight: 800; padding: 6px 18px; border: 2px solid #111; background: #F1EDE4; }
.one { font-size: 32px; font-weight: 800; }
.info { margin-top: 26px; }
.row { display: grid; grid-template-columns: 150px 1fr; padding: 13px 0; border-bottom: 1px solid rgba(17,17,17,.3); font-size: 24px; line-height: 1.5; }
.row .k { font-weight: 700; color: #3B3833; }
.row .v b { font-weight: 800; }
.prin { margin-top: 30px; }
.prin .t { font-size: 20px; font-weight: 700; color: #6E6A64; margin-bottom: 8px; }
.prin .p { font-size: 27px; font-weight: 700; line-height: 1.6; }
.prin .p span { color: #8A8A8A; font-weight: 600; margin-right: 12px; }
.foot { margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end; font-size: 20px; color: #6E6A64; }
.foot b { color: #111; font-size: 24px; }
`;
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body>
<section class="page">
  <div class="head"><span>${brand.nameEn}</span><span>Lessons at a Glance</span></div>
  <div class="kicker">${brand.name}</div>
  <div class="title">과목·과정 한눈에 보기</div>
  <div class="lead">${brand.signature}</div>
  <div class="band">
    <div class="sec"><div class="lb">과목 7</div><div class="chips">${SUBJECTS.map((s) => `<span class="chip">${s}</span>`).join("")}</div></div>
    <div class="sec"><div class="lb">과정 4</div><div class="chips">${COURSES.map((s) => `<span class="chip">${s}</span>`).join("")}</div></div>
    <div class="sec"><div class="lb">수업</div><div class="one">모든 과정 1:1 레슨</div></div>
  </div>
  <div class="info">
    <div class="row"><div class="k">연습실</div><div class="v">수강생은 운영시간 안에 <b>하루 1회, 1시간</b> 자유 이용</div></div>
    <div class="row"><div class="k">체험</div><div class="v"><b>1:1 체험 레슨 40분</b> · 사전 예약 10,000원 (현장 결제 25,000원)</div></div>
    <div class="row"><div class="k">운영</div><div class="v">${brand.hours}</div></div>
    <div class="row"><div class="k">위치</div><div class="v">${brand.address}<br>대야역 도보 10–15분, 성원아파트 정류장 앞</div></div>
  </div>
  <div class="prin"><div class="t">ENOCH의 세 가지 원칙</div><div class="p"><span>01</span>진도보다 이해를 먼저 봅니다.</div><div class="p"><span>02</span>같은 곡도, 사람마다 다르게 가르칩니다.</div><div class="p"><span>03</span>기본은 건너뛰지 않습니다.</div></div>
  <div class="foot"><div><b>네이버 예약 또는 ${brand.phone}</b></div><div>${brand.name}</div></div>
  ${doodle({ name: "notes", x: 840, y: 170, size: 150, rotate: -6, color: "#111", fill: PASTEL })}
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
