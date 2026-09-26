#!/usr/bin/env node
// ENOCH 카드뉴스 렌더러: output/<주제>/slides.json → output/<주제>/preview.html + 01.png, 02.png ...
// 사용법: node scripts/render.mjs output/<주제 폴더> [--html-only]
import { readFile, writeFile, access } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");

const [projectArg, ...flags] = process.argv.slice(2);
if (!projectArg) {
  console.error("사용법: node scripts/render.mjs output/<주제 폴더> [--html-only]");
  process.exit(1);
}
const projectDir = path.resolve(projectArg);
const htmlOnly = flags.includes("--html-only");

const brand = JSON.parse(await readFile(path.join(root, "templates/brand.json"), "utf8"));
const css = await readFile(path.join(root, "templates/card.css"), "utf8");
const deck = JSON.parse(await readFile(path.join(projectDir, "slides.json"), "utf8"));

const warnings = [];
const LIMITS = { title: 40, body: 110, note: 70, subtitle: 50 };
// CLAUDE.md 3번 금지 표현 — 걸리면 경고만 하고 검수자가 판단한다.
const BANNED = ["완벽한", "특별한", "의 모든 것", "최고의", "1위", "무조건", "100%", "이번 호", "다음 호", "ENOCH가"];

const esc = (s = "") =>
  String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
// **강조** → 굵게. 포인트 컬러는 쓰지 않는다 (굵기 대비로 위계).
const rich = (s = "") => esc(s).replace(/\*\*(.+?)\*\*/g, '<span class="em">$1</span>');
const plain = (s = "") => String(s).replace(/\*\*/g, "").replace(/\n/g, "");

function check(i, slide) {
  for (const [key, max] of Object.entries(LIMITS)) {
    if (slide[key] && plain(slide[key]).length > max) {
      warnings.push(`${i + 1}장 ${key}: ${plain(slide[key]).length}자 (권장 ${max}자 이하)`);
    }
  }
  const text = JSON.stringify(slide);
  for (const w of BANNED) if (text.includes(w)) warnings.push(`${i + 1}장: 금지 표현 "${w}"`);
  if (/\p{Extended_Pictographic}/u.test(text.replace(/[♩♪♫♬♭♮♯©®™]/g, ""))) warnings.push(`${i + 1}장: 이모지 사용`);
}

// 실제 사진만 사용한다. 파일이 없으면 자리표시자를 그리고 필요한 사진을 알린다.
const mime = { ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png", ".webp": "image/webp" };
async function photo(i, rel, cls = "photo") {
  if (!rel) return "";
  const file = path.resolve(root, rel);
  try {
    await access(file);
    const data = (await readFile(file)).toString("base64");
    return `<div class="${cls}" style="background-image:url(data:${mime[path.extname(file).toLowerCase()] || "image/jpeg"};base64,${data})"></div>`;
  } catch {
    warnings.push(`${i + 1}장: 사진 필요 — ${rel}`);
    return `<div class="photo-missing"><div>사진 필요</div><div>${esc(rel)}</div></div>`;
  }
}

const kicker = (s) => (s.kicker ? `<div class="kicker">${esc(s.kicker)}</div>` : "");
const title = (s) => (s.title ? `<h2 class="title">${rich(s.title)}</h2>` : "");
const paras = (x) => (Array.isArray(x) ? x : x ? [x] : []).map((p) => `<p class="body">${rich(p)}</p>`).join("");
const two = (n) => String(n).padStart(2, "0");

// 한 옥타브 건반 (확정본 05장). notes: ["C","E","G"], ["C","Eb","G"] 등
const WHITE = { C: 0, D: 1, E: 2, F: 3, G: 4, A: 5, B: 6 };
const BLACK = { "C#": 1, Db: 1, "D#": 2, Eb: 2, "F#": 4, Gb: 4, "G#": 5, Ab: 5, "A#": 6, Bb: 6 };
function keyboard(notes = []) {
  const W = 888, H = 252, kw = W / 7, bw = 74, bh = 156;
  const norm = (n) => String(n).replace("♭", "b").replace("♯", "#");
  let svg = `<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}"><rect x="0.75" y="0.75" width="${W - 1.5}" height="${H - 1.5}" fill="none" stroke="var(--fg)" stroke-width="1.5"/>`;
  for (let k = 1; k < 7; k++) svg += `<line x1="${k * kw}" y1="0" x2="${k * kw}" y2="${H}" stroke="var(--fg)" stroke-width="1.5"/>`;
  for (const b of [1, 2, 4, 5, 6]) svg += `<rect x="${b * kw - bw / 2}" y="0" width="${bw}" height="${bh}" fill="var(--fg)"/>`;
  for (const raw of notes) {
    const n = norm(raw);
    if (n in WHITE) svg += `<circle cx="${WHITE[n] * kw + kw / 2}" cy="209" r="14" fill="var(--fg)"/>`;
    else if (n in BLACK) svg += `<circle cx="${BLACK[n] * kw}" cy="123" r="13" fill="var(--bg)"/>`;
    else warnings.push(`건반 음 이름 "${raw}"을 알 수 없습니다 (C, Eb, F# 형식)`);
  }
  return svg + "</svg>";
}

const layouts = {
  // 01 표지: 사진 + 큰 영문 + 부제 + 하단 반복 띠
  cover: async (s, i) => {
    const tick = s.ticker || deck.ticker || `${brand.nameEn}`;
    return `
    ${s.image ? (await photo(i, s.image, "cover-photo")).replace('class="photo-missing"', 'class="photo-missing cover-photo"') : ""}
    <div class="cover-en">${esc(s.en)}</div>
    <div class="cover-sub"><div class="ko"><b>${esc(s.ko || "")}</b>${s.sub ? ` — ${esc(s.sub)}` : ""}</div>
      ${s.issue ? `<div class="issue">${esc(s.issue).replace(/\n/g, "<br>")}</div>` : ""}</div>
    <div class="ticker">${Array(6).fill(esc(tick)).join(" — ")}</div>`;
  },

  // 02 EDITOR'S NOTE: 제목 + 문단 + 서명
  note: (s) => `${kicker(s)}${title(s)}${paras(s.paragraphs || s.body)}
    ${s.sign !== false ? `<div class="sign">— ${esc(s.sign || brand.nameEn)}</div>` : ""}`,

  // 03 DICTIONARY: 큰 단어 + 한자 + 영문·품사 + 정의 + 용어 행
  dictionary: (s) => `${kicker(s)}
    <div class="dict-word"><div class="ko">${esc(s.word)}</div>${s.hanja ? `<div class="hanja">${esc(s.hanja)}</div>` : ""}</div>
    <div class="dict-en"><span class="en">${esc(s.en || "")}</span>${s.pos ? `<span class="pos">${esc(s.pos)}</span>` : ""}</div>
    <p class="dict-def">${rich(s.definition || "")}</p>
    ${s.terms ? `<div class="terms">${s.terms
      .map((t) => `<div class="term"><div class="k">${esc(t.ko)}${t.en ? `<small>${esc(t.en)}</small>` : ""}</div><div class="v">${rich(t.text)}</div></div>`)
      .join("")}</div>` : ""}`,

  // 04 IN NUMBERS: 제목 + 오른쪽 키커 + 큰 숫자 행
  numbers: (s) => `<div class="head-row"><h2 class="title">${rich(s.title)}</h2>${kicker(s)}</div>
    <div class="rows">${(s.items || [])
      .map((it) => `<div class="r"><div class="num">${esc(it.num)}</div><div><div class="h">${rich(it.head)}</div><div class="t">${rich(it.text || "")}</div></div></div>`)
      .join("")}</div>`,

  // 05 DIAGRAM: 건반 도식 (1–2개)
  keyboard: (s) => `${kicker(s)}${title(s)}
    ${(s.boards || [])
      .map((b) => `<div class="kb"><div class="kb-head"><div class="en">${esc(b.en || "")} <span>${esc(b.ko || "")}</span></div>
        <div class="notes">${esc((b.notes || []).join(" — ").replace(/b(?=\s|$)/g, "♭"))}</div></div>
        ${keyboard(b.notes)}${b.caption ? `<div class="kb-cap">${rich(b.caption)}</div>` : ""}</div>`)
      .join("")}`,

  // 06·07 PARTS: 번호 + 큰 영문 + 한글 + 설명 (4행 이상이면 촘촘하게)
  parts: (s) => `${kicker(s)}${title(s)}
    <div class="rows">${(s.items || [])
      .map((it, n) => `<div class="r"><div class="no">${esc(it.no || two((s.start || 1) + n))}</div><div>
        <div class="part-en">${esc(it.en)}<span>${esc(it.ko || "")}</span></div><div class="part-t">${rich(it.text || "")}</div></div></div>`)
      .join("")}</div>`,

  // 08 STEPS: STEP 01 + 굵은 제목 + 설명
  steps: (s) => `${kicker(s)}${title(s)}${s.lead ? `<p class="lead">${rich(s.lead)}</p>` : ""}
    <div class="rows">${(s.items || [])
      .map((it, n) => `<div class="r"><div class="step">STEP ${two(n + 1)}</div><div><div class="h">${rich(it.head)}</div><div class="t">${rich(it.text || "")}</div></div></div>`)
      .join("")}</div>`,

  // 09 THE ENOCH WAY: 번호 + 굵은 한 문장
  way: (s) => `${kicker(s)}${title(s)}
    <div class="rows">${(s.items || [])
      .map((it, n) => `<div class="r"><div class="no">${two(n + 1)}</div><div class="s">${rich(typeof it === "string" ? it : it.text)}</div></div>`)
      .join("")}</div>`,

  // 10 마무리: 고스트 워드 + 시그니처 + 학원 정보
  closing: (s) => `<div class="ghost">${esc(s.ghost || "ENOCH")}</div>
    <div class="closing-ko">${rich(s.principle || brand.signature).replace(/\n/g, "<br>")}</div>
    <div class="closing-en">${esc(s.principleEn || brand.signatureEn)}</div>
    <div class="closing-info"><div><div class="name">${esc(brand.name)}</div><div class="addr">${esc(brand.address)}</div></div>
      <div class="right"><div class="tel">${esc(brand.phone)}</div><div class="subj">${esc(s.subjects || brand.subjects)}</div></div></div>`,

  // 범용: 한 장 한 메시지
  point: (s) => `${kicker(s)}${title(s)}<div style="margin-top:56px">${paras(s.body)}</div>`,

  // 범용: 코드 진행
  chords: (s) => `${kicker(s)}${title(s)}
    <div class="chords" style="grid-template-columns:repeat(${(s.chords || []).length},1fr)">${(s.chords || [])
      .map((c) => `<div class="chord"><div class="roman">${esc(c.roman || "")}</div><div class="name">${esc(c.name)}</div>
        <div class="notes">${esc(c.notes || "")}</div>${c.fn ? `<div class="fn">${esc(c.fn)}</div>` : ""}</div>`)
      .join("")}</div>${paras(s.body)}`,

  // 실제 사진 한 장
  photo: async (s, i) => `${await photo(i, s.image)}${title(s)}${paras(s.body)}`,

  // 강사 소개 포스터 (인용문 없음)
  instructor: async (s, i) => {
    const band = Array(8).fill(esc(s.subject || "")).join(" — ");
    return `<div class="poster">
      <div class="top"><div>${esc(s.subject || "")}</div><div>${esc(brand.nameEn)}</div></div>
      <div class="mid">${await photo(i, s.image)}
        <div class="names"><div class="name-en" style="font-size:${Math.min(92, Math.floor(560 / Math.max(...String(s.nameEn).split(/\s+/).map((w) => w.length))))}px">${esc(s.nameEn)}</div><div class="name-ko">${esc(s.nameKo)}</div>
          ${s.role ? `<div class="role">${rich(s.role)}</div>` : ""}</div></div>
      <div class="band">${band}</div></div>
    ${s.meta ? `<div class="meta">${s.meta.map((m) => `<div><b>${esc(m.k)}</b>${rich(m.v)}</div>`).join("")}</div>` : ""}`;
  },
};

const total = deck.slides.length;
if (total < 5 || total > 10) warnings.push(`장수 ${total}장 (기본 5–7장, 확정본 No.01은 10장)`);

const cards = [];
for (const [i, s] of deck.slides.entries()) {
  const fn = layouts[s.layout];
  if (!fn) throw new Error(`${i + 1}장: 알 수 없는 layout "${s.layout}" (가능: ${Object.keys(layouts).join(", ")})`);
  check(i, s);
  const theme = s.theme || deck.theme || "ivory";
  const extra = s.layout === "parts" && (s.items || []).length > 3 ? " compact" : "";
  const head = s.layout === "instructor" ? "" : `<div class="masthead"><span>${esc(brand.nameEn)}</span><span>${esc(deck.masthead || "")}</span></div>`;
  const foot = s.layout === "cover" ? "" : `<div class="colophon"><span>${esc(deck.footer || "")}</span><span class="page">${two(i + 1)} / ${two(total)}</span></div>`;
  cards.push(`<section class="card layout-${s.layout}${extra} theme-${theme}" id="card-${i + 1}">
    ${head}
    ${await fn(s, i)}
    ${foot}
  </section>`);
}

const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8">
<title>${esc(deck.title || path.basename(projectDir))}</title><style>${css}</style></head>
<body class="preview">${cards.join("\n")}</body></html>`;

await writeFile(path.join(projectDir, "preview.html"), html);
console.log(`HTML 미리보기: ${path.relative(process.cwd(), path.join(projectDir, "preview.html"))}`);

if (!htmlOnly) {
  let chromium;
  try {
    ({ chromium } = await import("playwright"));
  } catch {
    console.error("playwright가 없습니다. `npm install` 후 `npx playwright install chromium`을 실행하세요. (--html-only 로 HTML만 생성 가능)");
    process.exit(1);
  }
  const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  // 폰트 CDN에 닿지 못해도 로컬 폰트로 계속 진행한다.
  await page.setContent(html, { waitUntil: "load", timeout: 15000 }).catch(() => {});
  await page.evaluate(() => document.fonts.ready);
  for (let i = 0; i < total; i++) {
    await page.locator(`#card-${i + 1}`).screenshot({ path: path.join(projectDir, `${String(i + 1).padStart(2, "0")}.png`) });
  }
  await browser.close();
  console.log(`PNG ${total}장: ${path.relative(process.cwd(), projectDir)}/01.png ~ ${String(total).padStart(2, "0")}.png`);
}

if (warnings.length) {
  console.warn("\n확인 필요:");
  warnings.forEach((w) => console.warn("  - " + w));
}
