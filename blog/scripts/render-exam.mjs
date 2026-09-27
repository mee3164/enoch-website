#!/usr/bin/env node
// ENOCH 블로그 입시 정보 이미지 렌더러: blog/posts/<글번호>/exam.json → images/01.png ~ + images/preview.html
// 사용법: node blog/scripts/render-exam.mjs blog/posts/<글번호> [--html-only]
// 폭 1080px 고정, 높이는 내용에 맞춘다(최소 1350). 네이버 블로그 본문 이미지용.
import { readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";
import { doodle } from "../../scripts/doodles.mjs";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const [dirArg, ...flags] = process.argv.slice(2);
if (!dirArg) {
  console.error("사용법: node blog/scripts/render-exam.mjs blog/posts/<글번호> [--html-only]");
  process.exit(1);
}
const postDir = path.resolve(dirArg);
const outDir = path.join(postDir, "images");
const data = JSON.parse(await readFile(path.join(postDir, "exam.json"), "utf8"));
const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const fontUrl = pathToFileURL(path.join(root, "node_modules/pretendard/dist/web/variable/woff2/PretendardVariable.woff2")).href;

const PASTEL = { sage: "#DCE2D3", blush: "#EEDFD8", mist: "#D9E1E8", butter: "#F1E8CB", lilac: "#E3DDE9" };
const TBD = "요강 확인 필요";
const esc = (s = "") => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
// 값이 비었거나 "요강 확인 필요"면 회색으로 표시
const val = (s) => (!s || String(s).includes(TBD) ? `<span class="tbd">${esc(s || TBD)}</span>` : esc(s).replace(/\n/g, "<br>"));
const pastelOf = (p) => PASTEL[p] || PASTEL.sage;

const warnings = [];
const BANNED = ["최고", "1위", "유일", "합격 보장", "100%", "무조건", "완벽한", "특별한", "ENOCH가"];
for (const w of BANNED) if (JSON.stringify(data).includes(w)) warnings.push(`금지 표현 "${w}"`);

const css = `
@font-face { font-family: "Pretendard"; src: url("${fontUrl}") format("woff2"); font-weight: 100 900; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { background: #555; font-family: "Pretendard", sans-serif; word-break: keep-all; -webkit-font-smoothing: antialiased; }
.page { width: 1080px; min-height: 1350px; padding: 72px 80px 64px; background: #F1EDE4; color: #111; position: relative;
  display: flex; flex-direction: column; margin: 0 auto 40px; overflow: hidden; }
.page.black { background: #111; color: #F1EDE4; }
.mono { font-family: "Pretendard", sans-serif; letter-spacing: 2.6px; text-transform: uppercase; }
.head { display: flex; justify-content: space-between; font-size: 18px; font-weight: 500; padding-bottom: 18px; border-bottom: 2px solid currentColor; }
.foot { margin-top: auto; padding-top: 40px; display: flex; justify-content: space-between; align-items: flex-end; font-size: 17px; color: #6E6A64; gap: 40px; }
.black .foot { color: #9A958C; }
.foot .note { line-height: 1.6; }
.kicker { font-size: 20px; font-weight: 500; color: #6E6A64; margin-top: 64px; }
.title { font-size: 60px; font-weight: 800; line-height: 1.28; letter-spacing: -2px; margin-top: 18px; white-space: pre-line; }
.lead { font-size: 26px; font-weight: 400; color: #55524D; margin-top: 22px; line-height: 1.6; white-space: pre-line; }
.tbd { color: #9A958C; font-weight: 400; font-style: normal; }
.doodle-layer { position: absolute; inset: 0; pointer-events: none; }

/* cover */
.cover .title { font-size: 84px; letter-spacing: -3px; margin-top: 28px; }
.cover .band { margin: 56px -80px 0; padding: 48px 80px; display: grid; grid-template-columns: 1fr 1fr; gap: 30px 48px; }
.cover .band .item { border-top: 1.5px solid rgba(17,17,17,.8); padding-top: 16px; }
.cover .band .no { font-size: 17px; color: #55524D; font-weight: 500; letter-spacing: 2px; }
.cover .band .nm { font-size: 34px; font-weight: 800; margin-top: 6px; letter-spacing: -1px; }
.cover .band .un { font-size: 20px; color: #55524D; margin-top: 6px; line-height: 1.45; }
.cover .topics { margin-top: 40px; font-size: 24px; font-weight: 600; letter-spacing: 1px; }

/* schedule table */
table { width: 100%; border-collapse: collapse; margin-top: 44px; }
th { text-align: left; font-size: 19px; font-weight: 600; color: #3B3833; padding: 16px 14px; letter-spacing: 1px; }
td { font-size: 22px; line-height: 1.5; padding: 22px 14px; border-bottom: 1px solid rgba(17,17,17,.3); vertical-align: top; }
td.sch { width: 250px; }
td.sch b { display: block; font-size: 27px; font-weight: 800; letter-spacing: -.8px; }
td.sch span { display: block; font-size: 17px; color: #6E6A64; margin-top: 4px; line-height: 1.4; }
td.date { font-weight: 600; }

/* school */
.hero { margin: 48px -80px 0; padding: 52px 80px 48px; }
.hero .no { font-size: 20px; font-weight: 600; letter-spacing: 3px; }
.hero .nm { font-size: 72px; font-weight: 800; letter-spacing: -2.5px; margin-top: 14px; line-height: 1.15; }
.hero .un { font-size: 26px; font-weight: 500; margin-top: 14px; line-height: 1.45; }
.row { display: grid; grid-template-columns: 170px 1fr; gap: 28px; padding: 30px 0; border-bottom: 1px solid rgba(17,17,17,.28); }
.row:last-of-type { border-bottom: none; }
.row .lb { font-size: 19px; font-weight: 600; color: #6E6A64; letter-spacing: 1.5px; padding-top: 4px; }
.row .ct { font-size: 23px; line-height: 1.6; }
.row .ct b { font-weight: 700; }
.bar { display: flex; height: 50px; margin-top: 10px; border: 1.5px solid #111; }
.bar div { display: flex; align-items: center; padding: 0 16px; font-size: 19px; font-weight: 700; white-space: nowrap; overflow: hidden; }
.bar div + div { border-left: 1.5px solid #111; }
.tl { list-style: none; }
.tl li { display: grid; grid-template-columns: 150px 1fr; gap: 16px; padding: 5px 0; }
.tl li .ev { color: #55524D; font-weight: 500; }
.tl li .dt { font-weight: 700; }
.major { margin-bottom: 18px; }
.major:last-child { margin-bottom: 0; }
.major .mj { display: inline-block; font-size: 19px; font-weight: 700; padding: 3px 12px; margin-bottom: 8px; }
.major ul, .checks { list-style: none; }
.major li { padding-left: 20px; position: relative; font-size: 22px; line-height: 1.6; }
.major li::before { content: ""; position: absolute; left: 2px; top: 16px; width: 8px; height: 1.5px; background: #111; }
.checks li { padding-left: 38px; position: relative; font-size: 23px; line-height: 1.6; margin-bottom: 4px; }
.checks li::before { content: ""; position: absolute; left: 0; top: 7px; width: 20px; height: 20px; border: 1.8px solid #111; }
.small { font-size: 19px; color: #6E6A64; line-height: 1.55; margin-top: 8px; }

/* checklist page */
.cl { margin-top: 44px; display: grid; grid-template-columns: 1fr; gap: 0; }
.cl .grp { padding: 30px 0; border-bottom: 1px solid rgba(17,17,17,.28); }
.cl .grp h3 { font-size: 26px; font-weight: 800; margin-bottom: 14px; }

/* closing */
.black .kicker { color: #9A958C; }
.black .lead { color: #C9C4BB; }
.closing .ghost { position: absolute; right: -30px; bottom: 250px; font-size: 300px; font-weight: 900; color: #2A2825; letter-spacing: -12px; line-height: 1; }
.closing .sig { font-size: 30px; font-weight: 700; margin-top: 80px; position: relative; }
.closing .info { margin-top: 36px; font-size: 22px; line-height: 1.95; color: #C9C4BB; position: relative; }
.closing .info b { display: inline-block; width: 80px; color: #9A958C; font-weight: 500; }
`;

const total = data.pages.length;
const head = (black) => `<div class="head mono"><span>${esc(brand.nameEn)}</span><span>${esc(data.header || "")}</span></div>`;
const foot = (i, black) => `<div class="foot"><div class="note">${esc(data.asof)} 각 대학 모집요강 기준<br>정확한 내용은 꼭 각 대학 입학처 모집요강에서 한 번 더 확인해 주세요.</div><div class="mono">${String(i + 1).padStart(2, "0")} / ${String(total).padStart(2, "0")}</div></div>`;
const doodles = (list = []) => (list.length ? `<svg class="doodle-layer" width="1080" height="1350" viewBox="0 0 1080 1350">${list.map((d) => doodle(d)).join("")}</svg>` : "");
const schoolById = Object.fromEntries((data.schools || []).map((s) => [s.id, s]));

function cover(p, i) {
  const bg = pastelOf(p.pastel);
  const items = data.schools.map((s, n) => `<div class="item"><div class="no">${String(n + 1).padStart(2, "0")}</div><div class="nm">${esc(s.name)}</div><div class="un">${esc(s.unitShort || s.unit)}</div></div>`).join("");
  return `<section class="page cover">${head()}<div class="kicker mono">${esc(p.kicker)}</div><div class="title">${esc(p.title)}</div>
  <div class="band" style="background:${bg}">${items}</div><div class="topics">${esc(p.topics || "")}</div>${doodles(p.doodles)}${foot(i)}</section>`;
}

function schedule(p, i) {
  const bg = pastelOf(p.pastel);
  const rows = data.schools.map((s) => {
    const g = (k) => (s.summary || {})[k];
    return `<tr><td class="sch"><b>${esc(s.name)}</b><span>${esc(s.unitShort || s.unit)}</span></td><td class="date">${val(g("apply"))}</td><td class="date">${val(g("exam"))}</td><td class="date">${val(g("result"))}</td></tr>`;
  }).join("");
  return `<section class="page">${head()}<div class="kicker mono">${esc(p.kicker)}</div><div class="title">${esc(p.title)}</div>${p.lead ? `<div class="lead">${esc(p.lead)}</div>` : ""}
  <table><thead><tr style="background:${bg}"><th>대학</th><th>원서 접수</th><th>실기 고사</th><th>합격 발표</th></tr></thead><tbody>${rows}</tbody></table>${doodles(p.doodles)}${foot(i)}</section>`;
}

function school(p, i) {
  const s = schoolById[p.school];
  if (!s) throw new Error(`school 없음: ${p.school}`);
  const bg = pastelOf(s.pastel);
  const n = data.schools.indexOf(s) + 1;
  const rows = [];
  if (s.tracks?.length) {
    rows.push(`<div class="row"><div class="lb">전형</div><div class="ct">${s.tracks.map((t) => `<div><b>${esc(t.name)}</b>${t.quota ? ` · ${val(t.quota)}` : ""}</div>${t.ratio?.length ? `<div class="bar">${t.ratio.map(([k, v], j) => `<div style="flex:${Math.max(v, 12)};${j === 0 ? `background:${bg}` : ""}">${esc(k)} ${v}%</div>`).join("")}</div>` : ""}${t.note ? `<div class="small">${val(t.note)}</div>` : ""}`).join('<div style="height:18px"></div>')}</div></div>`);
  }
  if (s.csat !== undefined) rows.push(`<div class="row"><div class="lb">수능 최저</div><div class="ct">${val(s.csat)}</div></div>`);
  if (s.schedule?.length) rows.push(`<div class="row"><div class="lb">일정</div><div class="ct"><ul class="tl">${s.schedule.map(([ev, dt]) => `<li><span class="ev">${esc(ev)}</span><span class="dt">${val(dt)}</span></li>`).join("")}</ul></div></div>`);
  if (s.exams?.length) rows.push(`<div class="row"><div class="lb">실기 과제</div><div class="ct">${s.exams.map((e) => `<div class="major"><span class="mj" style="background:${bg}">${esc(e.major)}</span><ul>${e.items.map((x) => `<li>${val(x)}</li>`).join("")}</ul></div>`).join("")}</div></div>`);
  if (s.bring?.length) rows.push(`<div class="row"><div class="lb">준비물</div><div class="ct"><ul class="checks">${s.bring.map((x) => `<li>${val(x)}</li>`).join("")}</ul></div></div>`);
  if (s.notes?.length) rows.push(`<div class="row"><div class="lb">참고</div><div class="ct">${s.notes.map((x) => `<div class="small" style="margin-top:0">${val(x)}</div>`).join("")}</div></div>`);
  return `<section class="page">${head()}<div class="hero" style="background:${bg}"><div class="no mono">University ${String(n).padStart(2, "0")}</div><div class="nm">${esc(s.name)}</div><div class="un">${esc(s.unit)}${s.campus ? ` · ${esc(s.campus)}` : ""}</div></div>
  <div style="margin-top:16px">${rows.join("")}</div>${doodles(p.doodles)}${foot(i)}</section>`;
}

function checklist(p, i) {
  const bg = pastelOf(p.pastel);
  return `<section class="page">${head()}<div class="kicker mono">${esc(p.kicker)}</div><div class="title">${esc(p.title)}</div>${p.lead ? `<div class="lead">${esc(p.lead)}</div>` : ""}
  <div class="cl">${p.groups.map((g) => `<div class="grp"><h3><span style="background:${bg};padding:2px 10px">${esc(g.title)}</span></h3><ul class="checks">${g.items.map((x) => `<li>${val(x)}</li>`).join("")}</ul></div>`).join("")}</div>${doodles(p.doodles)}${foot(i)}</section>`;
}

function closing(p, i) {
  return `<section class="page black closing">${head(true)}<div class="ghost">ENOCH</div><div class="kicker mono">${esc(p.kicker)}</div><div class="title">${esc(p.title)}</div>${p.lead ? `<div class="lead">${esc(p.lead)}</div>` : ""}
  <div class="sig">${esc(brand.signature)}</div>
  <div class="info"><div><b>학원</b>${esc(brand.name)}</div><div><b>주소</b>${esc(brand.address)}</div><div><b>위치</b>대야역 도보 10–15분, 성원아파트 정류장 앞</div><div><b>전화</b>${esc(brand.phone)}</div><div><b>운영</b>${esc(brand.hours)}</div></div>${foot(i, true)}</section>`;
}

const R = { cover, schedule, school, checklist, closing };
const sections = data.pages.map((p, i) => {
  if (!R[p.type]) throw new Error(`알 수 없는 type: ${p.type}`);
  return R[p.type](p, i);
});
const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body>${sections.join("\n")}</body></html>`;
await mkdir(outDir, { recursive: true });
const previewPath = path.join(outDir, "preview.html");
await writeFile(previewPath, html);

if (!flags.includes("--html-only")) {
  const { chromium } = await import("playwright");
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: 1 });
  await page.goto(pathToFileURL(previewPath).href, { waitUntil: "load" });
  await page.evaluate(() => document.fonts.ready);
  const loaded = await page.evaluate(() => [...document.fonts].some((f) => f.family.includes("Pretendard") && f.status === "loaded"));
  if (!loaded) warnings.push("Pretendard 폰트를 불러오지 못함 (npm install 확인)");
  const els = await page.$$("section.page");
  for (let i = 0; i < els.length; i++) {
    const file = path.join(outDir, `${String(i + 1).padStart(2, "0")}.png`);
    await els[i].screenshot({ path: file });
    const box = await els[i].boundingBox();
    console.log(`${path.relative(root, file)}  1080×${Math.round(box.height)}`);
  }
  await browser.close();
}
if (warnings.length) console.log("\n경고:\n- " + warnings.join("\n- "));
