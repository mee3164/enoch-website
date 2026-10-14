#!/usr/bin/env node
// 오시는 길 이미지 (1080×1350). 지도는 그리지 않는다(실제 지도는 네이버 지도 삽입으로). 확인된 위치 정보만.
// 사용법: node blog/scripts/render-location.mjs → blog/assets/academy/location.png
import { writeFile, readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const out = path.join(root, "blog/assets/academy/location.png");
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;

const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1350px; padding: 80px 88px 72px; background: #F1EDE4; color: #111; display: flex; flex-direction: column; }
.top { display: flex; justify-content: space-between; font-size: 15px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; padding-bottom: 16px; border-bottom: 1px solid #111; }
.en { margin-top: 56px; font-size: 17px; font-weight: 500; letter-spacing: 6px; text-transform: uppercase; color: #8A8A8A; }
h1 { margin-top: 12px; font-size: 92px; font-weight: 800; letter-spacing: -4px; line-height: 1; }
.addr { margin-top: 36px; font-size: 40px; font-weight: 700; letter-spacing: -1.2px; line-height: 1.3; }
.addr span { display: block; margin-top: 8px; font-size: 26px; font-weight: 300; color: #55524D; letter-spacing: -.5px; }
.steps { margin-top: 52px; border-top: 1px solid #111; }
.step { display: grid; grid-template-columns: 64px 180px 1fr; padding: 24px 0; border-bottom: 1px solid rgba(17,17,17,.2); align-items: baseline; }
.n { font-size: 14px; font-weight: 500; letter-spacing: 2px; color: #8A8A8A; }
.k b { font-size: 25px; font-weight: 700; } .k i { display: block; font-style: normal; margin-top: 4px; font-size: 12px; font-weight: 500; letter-spacing: 3px; text-transform: uppercase; color: #8A8A8A; }
.v { font-size: 23px; line-height: 1.55; color: #2E2C29; }
.v b { font-weight: 700; color: #111; }
.foot { margin-top: auto; padding-top: 24px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 16px; color: #8A8A8A; line-height: 1.7; }
.foot b { color: #111; font-weight: 600; font-size: 22px; letter-spacing: .5px; }
</style></head><body><section class="page">
  <div class="top"><span>${brand.nameEn}</span><span>Location</span></div>
  <div class="en">How to Find Us</div>
  <h1>오시는 길</h1>
  <div class="addr">${brand.address}<span>${brand.name}</span></div>
  <div class="steps">
    <div class="step"><div class="n">01</div><div class="k"><b>지하철</b><i>Subway</i></div><div class="v"><b>대야역</b>에서 걸어서 <b>10–15분</b></div></div>
    <div class="step"><div class="n">02</div><div class="k"><b>버스</b><i>Bus</i></div><div class="v"><b>성원아파트 정류장</b> 바로 앞 건물</div></div>
    <div class="step"><div class="n">03</div><div class="k"><b>건물</b><i>Building</i></div><div class="v">1층에 <b>역전우동 · 오피스문구점</b>이 있는 건물<br>그 위 <b>2층</b>입니다</div></div>
    <div class="step"><div class="n">04</div><div class="k"><b>운영</b><i>Hours</i></div><div class="v">${brand.hours}</div></div>
  </div>
  <div class="foot"><span>${brand.signature}<br>네이버 지도에서 "${brand.name}" 검색</span><span><b>${brand.phone}</b></span></div>
</section></body></html>`;

const tmp = path.join(os.tmpdir(), "enoch-location.html");
await writeFile(tmp, html);
const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
await (await p.$("section.page")).screenshot({ path: out });
await browser.close();
console.log(path.relative(root, out));
