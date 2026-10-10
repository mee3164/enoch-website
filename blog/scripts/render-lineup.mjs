#!/usr/bin/env node
// ENOCH LESSONS 라인업 이미지 (1080×1350). 이름 규칙: blog/PACKAGING.md 6번
// 사용법: node blog/scripts/render-lineup.mjs → blog/assets/academy/lineup.png
// 새 이름 옆에는 항상 "1:1 ○○ 수업"을 함께 쓴다 (고객이 헷갈리지 않게).
import { writeFile, readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const out = path.join(root, "blog/assets/academy/lineup.png");
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;

const LESSONS = [
  ["VOICE", "보컬"],
  ["GROOVE", "드럼"],
  ["STRINGS", "기타"],
  ["JAZZ KEYS", "재즈피아노"],
  ["HARMONY", "화성학"],
  ["SONGWRITING", "작곡"],
  ["STUDIO", "미디"],
];

const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1350px; padding: 80px 88px 72px; background: #111; color: #F1EDE4; display: flex; flex-direction: column; }
.top { display: flex; justify-content: space-between; font-size: 15px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; padding-bottom: 16px; border-bottom: 1px solid rgba(241,237,228,.8); }
.en { margin-top: 56px; font-size: 17px; font-weight: 500; letter-spacing: 6px; text-transform: uppercase; color: #8F8A82; }
h1 { margin-top: 12px; font-size: 96px; font-weight: 800; letter-spacing: -4px; line-height: 1; }
.lead { margin-top: 20px; font-size: 30px; font-weight: 300; letter-spacing: -.8px; }
.list { margin-top: 48px; border-top: 1px solid rgba(241,237,228,.8); }
.row { display: grid; grid-template-columns: 56px 1fr auto; align-items: baseline; padding: 28px 0; border-bottom: 1px solid rgba(241,237,228,.2); }
.n { font-size: 14px; font-weight: 500; letter-spacing: 2px; color: #8F8A82; }
.name { font-size: 46px; font-weight: 800; letter-spacing: -1.2px; line-height: 1.1; }
.name small { font-size: 46px; font-weight: 200; letter-spacing: -1px; color: #8F8A82; margin-right: 14px; }
.ko { font-size: 22px; font-weight: 500; color: #F1EDE4; }
.ko span { color: #8F8A82; font-weight: 400; margin-right: 8px; }
.foot { margin-top: auto; padding-top: 28px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 15px; color: #8F8A82; line-height: 1.7; }
.foot b { color: #F1EDE4; font-weight: 600; }
</style></head><body><section class="page">
  <div class="top"><span>${brand.nameEn}</span><span>Lessons</span></div>
  <div class="en">The ENOCH Lessons</div>
  <h1>ENOCH 레슨</h1>
  <div class="lead">모든 과정 1:1 레슨</div>
  <div class="list">
    ${LESSONS.map(([en, ko], i) => `<div class="row"><div class="n">${String(i + 1).padStart(2, "0")}</div><div class="name"><small>ENOCH</small>${en}</div><div class="ko"><span>1:1</span>${ko} 수업</div></div>`).join("")}
  </div>
  <div class="foot"><span>${brand.signature}<br>${brand.address}</span><span><b>${brand.phone}</b></span></div>
</section></body></html>`;

const tmp = path.join(os.tmpdir(), "enoch-lineup.html");
await writeFile(tmp, html);
const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
await (await p.$("section.page")).screenshot({ path: out });
await browser.close();
console.log(path.relative(root, out));
