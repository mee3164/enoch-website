#!/usr/bin/env node
// ENOCH TEACHERS 공통 카드 다시 만들기 — LESSON(1:1) 장. 1080×1350 (마무리 THE ENOCH WAY 장은 필요할 때만, 5번째 인자 --way)
// 강사 카드 원본의 LESSON 장에 "모든 과정이 1:1" 문구가 있어 "1:1 레슨을 기본으로 합니다"로 바꾼 판 (2026-10-14).
// 사용법: node blog/scripts/render-teacher-cards.mjs <글 폴더> <한글 이름> <전체 장수> "<마무리 문장, 줄은 | 로>" [--way]
// 예: node blog/scripts/render-teacher-cards.mjs blog/posts/015 김건우 9 "직접 만들고|발매해 온 음악,|1:1로."
//   → <글 폴더>/images/card-{전체-1}.png (LESSON). --way를 붙이면 card-{전체}.png (THE ENOCH WAY, 마지막 줄은 가는 글씨)도 만든다.
import { writeFile, readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const [dir, nameKo, totalArg, wayArg, wayFlag] = process.argv.slice(2);
if (!dir || !nameKo || !totalArg || !wayArg) { console.error("사용법: render-teacher-cards.mjs <글 폴더> <한글 이름> <전체 장수> \"<줄1|줄2|줄3>\""); process.exit(1); }
const total = Number(totalArg), pad = (n) => String(n).padStart(2, "0");
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;
const SUBJECTS = "Vocal · Guitar · Drum · Bass · Jazz Piano · MIDI · 작곡 · 화성학";
const way = wayArg.split("|");

const css = `
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
:root { --mono: "IBM Plex Mono", "DejaVu Sans Mono", monospace; --en: "Helvetica Neue", Helvetica, Arial, "Liberation Sans", "Pretendard", sans-serif; }
.ivory { --bg: #F1EDE4; --fg: #111111; --body: #55524D; --sub: #6E6A64; --rule: rgba(17,17,17,.9); --hair: rgba(17,17,17,.3); --ghost: #E4DFD5; }
.black { --bg: #111111; --fg: #F1EDE4; --body: #C9C4BB; --sub: #9A958C; --rule: rgba(241,237,228,.85); --hair: rgba(241,237,228,.28); --ghost: #2A2825; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.card { position: relative; width: 1080px; height: 1350px; overflow: hidden; background: var(--bg); color: var(--fg); padding: 0 96px; }
.masthead, .colophon { position: absolute; left: 96px; right: 96px; display: flex; justify-content: space-between; font-family: var(--mono); font-size: 20px; letter-spacing: 2.4px; }
.masthead { top: 70px; height: 48px; border-bottom: 1.5px solid var(--rule); padding-bottom: 14px; align-items: flex-end; }
.colophon { top: 1244px; border-top: 1.5px solid var(--rule); padding-top: 18px; font-family: "Pretendard", sans-serif; font-size: 19px; letter-spacing: 0; }
.colophon .page { font-family: var(--mono); letter-spacing: 3px; }
.kicker { position: absolute; top: 190px; font-family: var(--mono); font-size: 20px; letter-spacing: 3.2px; color: var(--sub); }
/* LESSON */
.big { position: absolute; top: 236px; left: 96px; font-family: var(--mono); font-size: 312px; font-weight: 700; line-height: 1; letter-spacing: -62px; margin-left: -14px; }
.l-title { position: absolute; top: 600px; left: 96px; font-size: 46px; font-weight: 800; line-height: 1.38; letter-spacing: -1.6px; }
.l-sub { position: absolute; top: 762px; left: 96px; font-size: 27px; font-weight: 300; line-height: 1.7; color: var(--body); letter-spacing: -0.4px; }
/* WAY */
.ghost { position: absolute; top: 172px; left: 90px; font-family: var(--en); font-size: 236px; font-weight: 700; line-height: .8; letter-spacing: -6px; color: var(--ghost); }
.w-title { position: absolute; top: 452px; left: 96px; font-size: 66px; font-weight: 800; line-height: 1.38; letter-spacing: -2px; }
.w-title .light { font-weight: 300; }
.w-sig { position: absolute; top: 806px; left: 96px; font-size: 26px; font-weight: 300; color: var(--body); }
.info { position: absolute; left: 96px; right: 96px; top: 1040px; border-top: 1px solid var(--hair); padding-top: 26px; display: flex; justify-content: space-between; }
.info .name { font-size: 21px; font-weight: 500; } .info .addr { margin-top: 10px; font-size: 20px; font-weight: 300; color: var(--body); }
.info .right { text-align: right; } .info .tel { font-family: var(--mono); font-size: 22px; letter-spacing: 1.5px; }
.info .subj { margin-top: 10px; font-size: 17px; font-weight: 300; color: var(--body); }
`;
const head = (r) => `<div class="masthead"><span>ENOCH MUSIC ACADEMY</span><span>${r}</span></div>`;
const foot = (n) => `<div class="colophon"><span>강사 소개 — ${nameKo}</span><span class="page">${pad(n)} / ${pad(total)}</span></div>`;

const lesson = `<section class="card ivory">${head("LESSON")}
  <div class="kicker">LESSON</div>
  <div class="big">1:1</div>
  <div class="l-title">입시 · 취미 · 성인 · 전문,<br>1:1 레슨을 기본으로 합니다.</div>
  <div class="l-sub">같은 곡도, 사람마다 다르게 가르칩니다.<br>원하시면 2:1 레슨도 신청할 수 있습니다.</div>
  ${foot(total - 1)}</section>`;
const wayCard = `<section class="card black">${head("THE ENOCH WAY")}
  <div class="ghost">ENOCH</div>
  <div class="w-title">${way.map((l, i) => i === way.length - 1 ? `<span class="light">${l}</span>` : l).join("<br>")}</div>
  <div class="w-sig">${brand.signature}</div>
  <div class="info"><div><div class="name">${brand.name}</div><div class="addr">${brand.address}</div></div>
    <div class="right"><div class="tel">${brand.phone}</div><div class="subj">${SUBJECTS}</div></div></div>
  ${foot(total)}</section>`;

const { chromium } = await import("playwright");
const browser = await chromium.launch();
const p = await browser.newPage({ viewport: { width: 1080, height: 1350 } });
for (const [n, body] of wayFlag === "--way" ? [[total - 1, lesson], [total, wayCard]] : [[total - 1, lesson]]) {
  const tmp = path.join(os.tmpdir(), `enoch-teacher-card-${n}.html`);
  await writeFile(tmp, `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body>${body}</body></html>`);
  await p.goto(pathToFileURL(tmp).href, { waitUntil: "load" });
  await p.evaluate(() => document.fonts.ready);
  const out = path.join(root, dir, `images/card-${pad(n)}.png`);
  await (await p.$("section.card")).screenshot({ path: out });
  console.log(path.relative(root, out));
}
await browser.close();
