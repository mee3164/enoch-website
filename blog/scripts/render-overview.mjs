#!/usr/bin/env node
// ENOCH 블로그 '과목·과정 한눈에 보기' 이미지 (1080×1350) — 레슨 구성·라인업 이미지와 같은 결
// 사용법: node blog/scripts/render-overview.mjs [출력 경로]  (기본: blog/assets/academy/overview.png)
// 내용은 blog/GUIDE.md 1번 확인 사실만. 규모·방음·수강료는 넣지 않는다.
import { writeFile, mkdir, readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const out = path.resolve(process.argv[2] || path.join(root, "blog/assets/academy/overview.png"));
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;
const SUBJECTS = [["보컬", "Vocal"], ["기타", "Guitar"], ["드럼", "Drum"], ["베이스", "Bass"], ["재즈피아노", "Jazz Piano"], ["화성학", "Harmony"], ["작곡", "Composition"], ["미디", "MIDI"]];
const COURSES = [["입시", "Entrance"], ["취미", "Hobby"], ["성인", "Adult"], ["전문", "Pro"]];

const cell = ([ko, en]) => `<div class="cell"><b>${ko}</b><i>${en}</i></div>`;
const css = `
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1350px; padding: 80px 88px 72px; background: #F1EDE4; color: #111; display: flex; flex-direction: column; }
.top { display: flex; justify-content: space-between; font-size: 15px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; padding-bottom: 16px; border-bottom: 1px solid #111; }
.en { margin-top: 52px; font-size: 17px; font-weight: 500; letter-spacing: 6px; text-transform: uppercase; color: #8A8A8A; }
h1 { margin-top: 12px; font-size: 84px; font-weight: 800; letter-spacing: -3.6px; line-height: 1.04; }
.lead { margin-top: 18px; font-size: 30px; font-weight: 300; letter-spacing: -.8px; }
.label { display: flex; justify-content: space-between; align-items: baseline; margin-top: 44px; padding-bottom: 12px; border-bottom: 1px solid #111; font-size: 13px; font-weight: 500; letter-spacing: 3.5px; text-transform: uppercase; color: #8A8A8A; }
.label b { font-size: 20px; font-weight: 700; letter-spacing: -.3px; text-transform: none; color: #111; }
.grid { display: grid; grid-template-columns: repeat(4, 1fr); }
.cell { padding: 18px 0 16px; border-bottom: 1px solid rgba(17,17,17,.2); }
.cell b { display: block; font-size: 30px; font-weight: 700; letter-spacing: -.8px; }
.cell i { display: block; font-style: normal; margin-top: 4px; font-size: 12px; font-weight: 500; letter-spacing: 3px; text-transform: uppercase; color: #8A8A8A; }
.rows { margin-top: 44px; border-top: 1px solid #111; }
.row { display: grid; grid-template-columns: 150px 1fr; padding: 15px 0; border-bottom: 1px solid rgba(17,17,17,.2); font-size: 20px; line-height: 1.6; color: #2E2C29; }
.row .k { font-size: 13px; font-weight: 500; letter-spacing: 3.5px; text-transform: uppercase; color: #8A8A8A; padding-top: 5px; }
.row b { font-weight: 600; color: #111; }
.foot { margin-top: auto; padding-top: 24px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 15px; color: #8A8A8A; line-height: 1.7; }
.foot b { color: #111; font-weight: 600; font-size: 17px; }
`;
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body>
<section class="page">
  <div class="top"><span>${brand.nameEn}</span><span>Lessons at a Glance</span></div>
  <div class="en">Subjects &amp; Courses</div>
  <h1>과목·과정<br>한눈에 보기</h1>
  <div class="lead">1:1 레슨을 기본으로 합니다.</div>
  <div class="label"><b>과목</b><span>Subjects · ${SUBJECTS.length}</span></div>
  <div class="grid">${SUBJECTS.map(cell).join("")}</div>
  <div class="label"><b>과정</b><span>Courses · ${COURSES.length}</span></div>
  <div class="grid">${COURSES.map(cell).join("")}</div>
  <div class="rows">
    <div class="row"><div class="k">Practice</div><div>수강생은 운영시간 안에 <b>하루 1회, 1시간</b> 연습실 자유 이용</div></div>
    <div class="row"><div class="k">Trial</div><div><b>1:1 체험 레슨 40분</b> · 사전 예약 10,000원 (현장 결제 25,000원)</div></div>
    <div class="row"><div class="k">Hours</div><div>${brand.hours}</div></div>
    <div class="row"><div class="k">Address</div><div>${brand.address}<br>대야역 도보 10–15분, 성원아파트 정류장 앞</div></div>
  </div>
  <div class="foot"><span>${brand.signature}<br>${brand.name}</span><span><b>네이버 예약 · ${brand.phone}</b></span></div>
</section></body></html>`;
await mkdir(path.dirname(out), { recursive: true });
const tmp = path.join(os.tmpdir(), "enoch-overview.html");
await writeFile(tmp, html);
const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
await (await p.$("section.page")).screenshot({ path: out });
await browser.close();
console.log(path.relative(root, out));
