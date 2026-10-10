#!/usr/bin/env node
// ENOCH 학원 정보 시그니처 이미지 (Magazine B 무드, 1080×1350) — 아이보리판·블랙판
// 사용법: node blog/scripts/render-signature.mjs → blog/assets/academy/signature-ivory.png, signature-black.png
// 문구는 원장님 지정 문구 그대로 (2026-10-10). 바꾸지 않는다.
import { writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import os from "node:os";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const outDir = path.join(root, "blog/assets/academy");
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;

const THEMES = {
  ivory: { bg: "#F1EDE4", fg: "#111111", sub: "#8A8A8A", rule: "rgba(17,17,17,.85)", hair: "rgba(17,17,17,.22)" },
  black: { bg: "#111111", fg: "#F1EDE4", sub: "#8F8A82", rule: "rgba(241,237,228,.8)", hair: "rgba(241,237,228,.2)" },
};

const css = (t) => `
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1350px; padding: 84px 88px 80px; background: ${t.bg}; color: ${t.fg}; display: flex; flex-direction: column; position: relative; overflow: hidden; }
.top { display: flex; justify-content: space-between; font-size: 15px; font-weight: 500; letter-spacing: 4px; text-transform: uppercase; padding-bottom: 16px; border-bottom: 1px solid ${t.rule}; }
.mark { margin-top: 150px; font-size: 238px; font-weight: 800; letter-spacing: -11px; line-height: .82; margin-left: -10px; }
.en { margin-top: 26px; font-size: 16px; font-weight: 500; letter-spacing: 6px; text-transform: uppercase; color: ${t.sub}; }
.name { margin-top: 92px; font-size: 30px; font-weight: 700; letter-spacing: -.6px; }
.sig { margin-top: 14px; font-size: 44px; font-weight: 300; letter-spacing: -1.6px; }
.info { margin-top: auto; border-top: 1px solid ${t.rule}; }
.row { display: grid; grid-template-columns: 150px 1fr; padding: 18px 0; border-bottom: 1px solid ${t.hair}; font-size: 20px; line-height: 1.6; font-weight: 400; }
.row .k { font-size: 13px; font-weight: 500; letter-spacing: 3.5px; text-transform: uppercase; color: ${t.sub}; padding-top: 5px; }
.row .v b { font-weight: 600; }
.foot { margin-top: 22px; display: flex; justify-content: space-between; font-size: 13px; letter-spacing: 3.5px; text-transform: uppercase; color: ${t.sub}; }
`;

const page = (t) => `<section class="page">
  <div class="top"><span>Enoch Music Academy</span><span>Siheung</span></div>
  <div class="mark">ENOCH</div>
  <div class="en">Find your own true sound.</div>
  <div class="name">에녹실용음악학원 시흥점</div>
  <div class="sig">나만의 진짜 소리를 찾는 곳.</div>
  <div class="info">
    <div class="row"><div class="k">Address</div><div class="v">경기도 시흥시 은행로 157 2층<br>(대야역 도보 10–15분, 성원아파트 정류장 앞)</div></div>
    <div class="row"><div class="k">Contact</div><div class="v"><b>010 3949 3666</b></div></div>
    <div class="row"><div class="k">Hours</div><div class="v">평일 13:00–22:00 / 토 10:00–18:00 / 일요일 휴무</div></div>
    <div class="row"><div class="k">Lessons</div><div class="v">Vocal · Guitar · Drum · Bass · Jazz Piano · MIDI · 작곡 · 화성학<br><b>— 1:1 레슨을 기본으로 합니다</b></div></div>
  </div>
  <div class="foot"><span>Private Lessons</span><span>1:1</span></div>
</section>`;

await mkdir(outDir, { recursive: true });
const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
for (const [name, t] of Object.entries(THEMES)) {
  const tmp = path.join(os.tmpdir(), `enoch-signature-${name}.html`);
  await writeFile(tmp, `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css(t)}</style></head><body>${page(t)}</body></html>`);
  await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
  await p.evaluate(() => document.fonts.ready);
  const f = path.join(outDir, `signature-${name}.png`);
  await (await p.$("section.page")).screenshot({ path: f });
  console.log(path.relative(root, f));
}
await browser.close();
