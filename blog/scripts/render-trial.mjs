#!/usr/bin/env node
// ENOCH 블로그 체험 레슨 안내 이미지: blog/assets/trial/trial-<id>.png (1080×1350)
// 사용법: node blog/scripts/render-trial.mjs
// 금액·조건은 blog/GUIDE.md 1번 "체험 레슨"과 반드시 같게 유지한다.
import { writeFile, mkdir, readFile } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { doodle } from "../../scripts/doodles.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const outDir = path.join(root, "blog/assets/trial");
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;

const TRIAL = {
  minutes: "40분",
  reserve: "10,000원",
  onsite: "25,000원",
  discount: "10,000원",
};

// 과목별 변형. lead는 세계관(내 소리) 한 줄 — 수업 방식은 쓰지 않는다.
const VARIANTS = [
  { id: "common", kicker: "Trial Lesson", subject: "1:1 체험 레슨", lead: "내 소리를 먼저 들어 보는 40분.", pastel: "#F1E8CB", doodle: "notes" },
  { id: "vocal", kicker: "Vocal Trial Lesson", subject: "보컬 1:1 체험 레슨", lead: "내 목소리를 먼저 들어 보는 40분.", pastel: "#EEDFD8", doodle: "mic" },
  { id: "guitar", kicker: "Guitar Trial Lesson", subject: "기타 1:1 체험 레슨", lead: "내 손에 맞는 소리를 먼저 찾아보는 40분.", pastel: "#DCE2D3", doodle: "guitar" },
  { id: "drum", kicker: "Drum Trial Lesson", subject: "드럼 1:1 체험 레슨", lead: "내 박자를 먼저 들어 보는 40분.", pastel: "#D9E1E8", doodle: "drum" },
];

const esc = (s = "") => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");

const css = `
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #555; font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; height: 1350px; padding: 72px 80px 64px; background: #F1EDE4; color: #111; position: relative; display: flex; flex-direction: column; overflow: hidden; margin: 0 auto 40px; }
.mono { letter-spacing: 2.6px; text-transform: uppercase; }
.head { display: flex; justify-content: space-between; font-size: 18px; font-weight: 500; padding-bottom: 18px; border-bottom: 2px solid #111; }
.kicker { font-size: 22px; font-weight: 500; color: #6E6A64; margin-top: 64px; }
.title { font-size: 92px; font-weight: 800; letter-spacing: -3.5px; line-height: 1.12; margin-top: 18px; }
.lead { font-size: 32px; font-weight: 500; margin-top: 26px; color: #3B3833; }
.band { margin: 54px -80px 0; padding: 48px 80px; }
.row { display: grid; grid-template-columns: 200px 1fr; align-items: baseline; padding: 22px 0; border-bottom: 1.5px solid rgba(17,17,17,.75); }
.row:first-child { border-top: 1.5px solid rgba(17,17,17,.75); }
.lb { font-size: 22px; font-weight: 600; color: #3B3833; letter-spacing: 1px; }
.v { font-size: 40px; font-weight: 800; letter-spacing: -1px; }
.v small { font-size: 26px; font-weight: 500; color: #55524D; letter-spacing: 0; margin-left: 10px; }
.note { margin-top: 30px; font-size: 26px; font-weight: 500; line-height: 1.6; }
.book { margin-top: auto; display: flex; justify-content: space-between; align-items: flex-end; gap: 40px; }
.book .how { font-size: 30px; font-weight: 800; line-height: 1.5; }
.book .how span { display: block; font-size: 22px; font-weight: 500; color: #55524D; margin-top: 8px; line-height: 1.6; }
.book .sig { text-align: right; font-size: 20px; color: #6E6A64; line-height: 1.6; }
.doodle-layer { position: absolute; inset: 0; pointer-events: none; }
`;

const page = (v) => `<section class="page">
  <div class="head mono"><span>${esc(brand.nameEn)}</span><span>${esc(v.kicker)}</span></div>
  <div class="kicker">${esc(brand.name)}</div>
  <div class="title">${esc(v.subject)}</div>
  <div class="lead">${esc(v.lead)}</div>
  <div class="band" style="background:${v.pastel}">
    <div class="row"><div class="lb">수업 시간</div><div class="v">1:1 ${TRIAL.minutes}</div></div>
    <div class="row"><div class="lb">사전 예약</div><div class="v">${TRIAL.reserve}</div></div>
    <div class="row"><div class="lb">현장 결제</div><div class="v">${TRIAL.onsite}</div></div>
    <div class="note">체험 레슨 후 바로 등록하시면<br>수강료에서 ${TRIAL.discount}을 할인해 드립니다.</div>
  </div>
  <div class="book">
    <div class="how">네이버 예약 또는 전화 ${esc(brand.phone)}<span>${esc(brand.address)} · 대야역 도보 10–15분<br>평일 13:00–22:00 / 토 10:00–18:00 / 일요일 휴무</span></div>
    <div class="sig">${esc(brand.signature)}</div>
  </div>
  ${doodle({ name: v.doodle, x: 800, y: 975, size: 190, rotate: -8, color: "#111", fill: v.pastel })}
</section>`;

await mkdir(outDir, { recursive: true });
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body>${VARIANTS.map(page).join("\n")}</body></html>`;
const preview = path.join(outDir, "preview.html");
await writeFile(preview, html);

const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1200, height: 1400 } });
await p.goto(pathToFileURL(preview).href, { waitUntil: "load" });
await p.evaluate(() => document.fonts.ready);
const els = await p.$$("section.page");
for (let i = 0; i < els.length; i++) {
  const file = path.join(outDir, `trial-${VARIANTS[i].id}.png`);
  await els[i].screenshot({ path: file });
  console.log(path.relative(root, file));
}
await browser.close();
