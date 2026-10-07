#!/usr/bin/env node
// ENOCH 블로그 드럼 8비트 기본 리듬 이미지 (1080×1350)
// 사용법: node blog/scripts/render-beat.mjs [출력 경로]  (기본: blog/assets/drum/beat-8basic.png)
// 표준 8비트: 하이햇 8분음표, 스네어 2·4박, 킥 1·3박 (오른손잡이 기준)
import { writeFile, mkdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { doodle } from "../../scripts/doodles.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const out = path.resolve(process.argv[2] || path.join(root, "blog/assets/drum/beat-8basic.png"));
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;
const PASTEL = "#D9E1E8";
const COUNT = ["1", "&", "2", "&", "3", "&", "4", "&"];
const KO = ["하나", "그리고", "둘", "그리고", "셋", "그리고", "넷", "그리고"];
const ROWS = [
  { name: "하이햇", sub: "오른손", hits: [1, 1, 1, 1, 1, 1, 1, 1], mark: "x" },
  { name: "스네어", sub: "왼손", hits: [0, 0, 1, 0, 0, 0, 1, 0], mark: "o" },
  { name: "킥", sub: "오른발", hits: [1, 0, 0, 0, 1, 0, 0, 0], mark: "o" },
];
const cell = (on, mark, i) => `<div class="c${i % 2 ? " off" : ""}">${on ? (mark === "x" ? '<span class="x">×</span>' : '<span class="dot"></span>') : ""}</div>`;
const css = `
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1350px; padding: 72px 80px 64px; background: #F1EDE4; color: #111; position: relative; display: flex; flex-direction: column; overflow: hidden; }
.head { display: flex; justify-content: space-between; font-size: 18px; font-weight: 500; letter-spacing: 2.6px; text-transform: uppercase; padding-bottom: 18px; border-bottom: 2px solid #111; }
.kicker { font-size: 22px; font-weight: 500; color: #6E6A64; margin-top: 52px; }
.title { font-size: 70px; font-weight: 800; letter-spacing: -2.6px; line-height: 1.18; margin-top: 12px; }
.lead { font-size: 26px; color: #55524D; margin-top: 16px; line-height: 1.55; }
.band { margin: 44px -80px 0; padding: 44px 80px 40px; background: ${PASTEL}; }
.grid { display: grid; grid-template-columns: 190px repeat(8, 1fr); }
.hd { text-align: center; padding-bottom: 12px; }
.hd b { display: block; font-size: 34px; font-weight: 800; }
.hd small { display: block; font-size: 16px; color: #55524D; margin-top: 2px; }
.lb { display: flex; flex-direction: column; justify-content: center; border-top: 1.5px solid rgba(17,17,17,.75); padding: 0 0 0 4px; height: 118px; }
.lb b { font-size: 32px; font-weight: 800; } .lb small { font-size: 18px; color: #55524D; margin-top: 4px; }
.c { height: 118px; border-top: 1.5px solid rgba(17,17,17,.75); border-left: 1px solid rgba(17,17,17,.25); display: flex; align-items: center; justify-content: center; }
.c.off { background: rgba(255,255,255,.28); }
.grid > .c:nth-child(9n) { border-right: 1px solid rgba(17,17,17,.25); }
.last { border-bottom: 1.5px solid rgba(17,17,17,.75); }
.dot { width: 44px; height: 44px; border-radius: 50%; background: #111; display: block; }
.x { font-size: 54px; font-weight: 700; line-height: 1; }
.legend { margin-top: 18px; font-size: 19px; color: #3B3833; display: flex; gap: 28px; }
.try { margin-top: 36px; }
.try .t { font-size: 21px; font-weight: 700; color: #3B3833; }
.try .b { font-size: 28px; font-weight: 800; margin-top: 10px; line-height: 1.5; }
.try .s { font-size: 21px; color: #55524D; margin-top: 8px; line-height: 1.6; }
.foot { margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end; font-size: 19px; color: #6E6A64; line-height: 1.6; }
.foot b { color: #111; font-size: 22px; }
`;
const rows = ROWS.map((r, ri) => {
  const last = ri === ROWS.length - 1 ? " last" : "";
  return `<div class="lb${last}"><b>${r.name}</b><small>${r.sub}</small></div>` +
    r.hits.map((h, i) => cell(h, r.mark, i).replace('class="c', `class="c${last}`)).join("");
}).join("");
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body>
<section class="page">
  <div class="head"><span>${brand.nameEn}</span><span>Drum Basic Beat</span></div>
  <div class="kicker">${brand.name} · 드럼 입문</div>
  <div class="title">8비트 기본 리듬</div>
  <div class="lead">대중음악에서 아주 흔히 듣는 기본 리듬입니다.<br>세게보다 고르게, 한 칸씩 정확히 맞추는 것이 먼저입니다.</div>
  <div class="band">
    <div class="grid">
      <div></div>${COUNT.map((c, i) => `<div class="hd"><b>${c}</b><small>${KO[i]}</small></div>`).join("")}
      ${rows}
    </div>
    <div class="legend"><span>× 하이햇 (왼발로 페달을 밟아 닫은 상태)</span><span>● 스네어 · 킥</span><span>4/4박자 1마디</span></div>
  </div>
  <div class="try">
    <div class="t">드럼이 없어도 오늘 해 볼 수 있어요</div>
    <div class="b">오른손·왼손은 무릎, 오른발은 바닥을 가볍게</div>
    <div class="s">메트로놈을 느리게 켜고, 칸이 어긋나지 않게 맞춘 뒤 조금씩 빠르게 합니다.</div>
  </div>
  <div class="foot"><div><b>드럼 1:1 체험 레슨 40분 · 체험 때 스틱 대여</b><br>네이버 예약 또는 ${brand.phone} · ${brand.address}</div><div>${brand.signature}</div></div>
  ${doodle({ name: "drum", x: 850, y: 160, size: 140, rotate: -6, color: "#111", fill: PASTEL })}
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
