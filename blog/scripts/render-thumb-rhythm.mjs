#!/usr/bin/env node
// 009 리듬감 글 블로그 대문(썸네일) 이미지 (1080×1080, 네이버 정사각 썸네일)
// 사용법: node blog/scripts/render-thumb-rhythm.mjs → blog/posts/009/images/thumbnail.png
import { writeFile, readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { doodle } from "../../scripts/doodles.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const out = path.join(root, "blog/posts/009/images/thumbnail.png");
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;
const P = "#D9E1E8"; // 미스트 (009 카드와 같은 파스텔)

// 박 표시: 정박(큰 점) 사이에 작은 점 — "쿵 짝 쿵 짝"의 무게 차이
const beats = () => {
  let g = `<line x1="0" y1="40" x2="920" y2="40" stroke="#111" stroke-width="2"/>`;
  for (let i = 0; i < 8; i++) {
    const x = 30 + i * 122, big = i % 2 === 0;
    g += `<circle cx="${x}" cy="40" r="${big ? 26 : 10}" fill="${big ? "#111" : "#F1EDE4"}" stroke="#111" stroke-width="${big ? 0 : 3}"/>`;
  }
  return `<svg class="beats" width="920" height="80" viewBox="0 0 920 80">${g}</svg>`;
};

const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; --fg: #111; }
.page { width: 1080px; height: 1080px; padding: 72px 80px 64px; background: #F1EDE4; color: #111; position: relative; display: flex; flex-direction: column; overflow: hidden; }
.head { display: flex; justify-content: space-between; font-size: 18px; font-weight: 500; letter-spacing: 2.6px; text-transform: uppercase; padding-bottom: 18px; border-bottom: 2px solid #111; }
.band { margin: 64px -80px 0; padding: 56px 80px 60px; background: ${P}; position: relative; }
.en { font-size: 20px; font-weight: 600; letter-spacing: 6px; text-transform: uppercase; color: #55524D; }
.title { font-size: 230px; font-weight: 900; letter-spacing: -12px; line-height: 1; margin-top: 18px; margin-left: -8px; }
.sub { margin-top: 56px; font-size: 44px; font-weight: 700; letter-spacing: -1.4px; line-height: 1.35; }
.sub span { font-weight: 300; }
.beats { display: block; margin-top: 44px; }
.foot { margin-top: auto; display: flex; justify-content: space-between; font-size: 18px; color: #6E6A64; letter-spacing: 1px; }
</style></head><body><section class="page">
  <div class="head"><span>${brand.nameEn}</span><span>Rhythm</span></div>
  <div class="band">
    <div class="en">Rhythm · Gravity of the Beat</div>
    <div class="title">리듬감</div>
    ${doodle({ name: "notes", x: 760, y: 70, size: 190, rotate: 8 })}
  </div>
  <div class="sub">박자는 맞는데,<br><span>왜 느낌이 안 살까요?</span></div>
  ${beats()}
  <div class="foot"><span>${brand.name}</span><span>정박의 중력</span></div>
</section></body></html>`;

const tmp = path.join(os.tmpdir(), "enoch-thumb-rhythm.html");
await writeFile(tmp, html);
const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1080 } });
await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
await (await p.$("section.page")).screenshot({ path: out });
await browser.close();
console.log(path.relative(root, out));
