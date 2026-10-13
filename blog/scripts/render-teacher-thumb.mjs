#!/usr/bin/env node
// ENOCH TEACHERS 블로그 썸네일 (1080×1080). 강사 카드 01장의 사진 칸을 잘라 정사각형으로 다시 짠다.
// 사용법: node blog/scripts/render-teacher-thumb.mjs <글 폴더> "<영문 이름>" "<과목>" "<한글 이름>" [사진 세로 시작 y, 기본 200]
// 예: node blog/scripts/render-teacher-thumb.mjs blog/posts/011 "SOO IN LEE" 보컬 이수인 200
//   → <글 폴더>/images/thumbnail.png  (카드 01장 사진 칸 기준 좌표: x 96–984, y 150–990)
import { writeFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const [dir, nameEn, subject, nameKo, cropYArg] = process.argv.slice(2);
if (!dir || !nameEn) { console.error("사용법: render-teacher-thumb.mjs <글 폴더> <영문 이름> <과목> <한글 이름> [y]"); process.exit(1); }
const postDir = path.resolve(root, dir);
const card = pathToFileURL(path.join(postDir, "images/card-01.png")).href;
const out = path.join(postDir, "images/thumbnail.png");
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;

const BOX_W = 952, BOX_H = 720, SRC_X = 96, SRC_W = 888;
const k = BOX_W / SRC_W, cropY = Number(cropYArg ?? 200);

const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1080px; padding: 60px 64px; background: #F1EDE4; color: #111; display: flex; flex-direction: column; }
.top { display: flex; justify-content: space-between; font-size: 17px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; padding-bottom: 14px; border-bottom: 1px solid #111; }
.photo { margin-top: 26px; width: ${BOX_W}px; height: ${BOX_H}px; overflow: hidden; position: relative; background: #000; }
.photo img { position: absolute; width: ${1080 * k}px; left: ${-SRC_X * k}px; top: ${-cropY * k}px; }
.name { margin-top: 28px; font-size: 96px; font-weight: 800; letter-spacing: -4px; line-height: .95; }
.sub { margin-top: 18px; display: flex; justify-content: space-between; align-items: baseline; font-size: 30px; font-weight: 500; }
.sub .ko { font-size: 19px; font-weight: 500; color: #8A8A8A; }
</style></head><body><section class="page">
  <div class="top"><span>Enoch Music Academy</span><span>Enoch Teachers</span></div>
  <div class="photo"><img src="${card}"></div>
  <div class="name">${nameEn}</div>
  <div class="sub"><div>${subject} ${nameKo}</div><span class="ko">에녹실용음악학원 시흥점</span></div>
</section></body></html>`;

const tmp = path.join(os.tmpdir(), "enoch-teacher-thumb.html");
await writeFile(tmp, html);
const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1080 } });
await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
await (await p.$("section.page")).screenshot({ path: out });
await browser.close();
console.log(path.relative(root, out));
