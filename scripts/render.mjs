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
  if (/[\u{1F300}-\u{1FAFF}\u{2600}-\u{27BF}]/u.test(text)) warnings.push(`${i + 1}장: 이모지 사용`);
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

const label = (s) => (s.label ? `<div class="label">${esc(s.label)}</div>` : "");
const note = (s) => (s.note ? `<p class="note">${rich(s.note)}</p>` : "");

const layouts = {
  cover: (s) => `
    ${deck.issueNo ? `<div class="issue-no">${esc(deck.issueNo)}</div>` : ""}
    ${s.en ? `<div class="en">${esc(s.en)}</div>` : ""}
    <h1 class="title">${rich(s.title)}</h1>
    ${s.subtitle ? `<p class="subtitle">${rich(s.subtitle)}</p>` : ""}`,

  point: (s) => `${label(s)}
    <h2 class="title">${rich(s.title)}</h2>
    ${s.body ? `<p class="body">${rich(s.body)}</p>` : ""}${note(s)}`,

  list: (s) => `${label(s)}
    <h2 class="title">${rich(s.title)}</h2>
    <div class="rows">${(s.items || [])
      .map((it, n) => {
        const o = typeof it === "string" ? { head: it } : it;
        return `<div class="row"><div class="n">${String(n + 1).padStart(2, "0")}</div><div>
          <div class="head">${rich(o.head || "")}</div>${o.text ? `<div class="text">${rich(o.text)}</div>` : ""}</div></div>`;
      })
      .join("")}</div>${note(s)}`,

  chords: (s) => `${label(s)}
    <h2 class="title">${rich(s.title)}</h2>
    <div class="chords" style="grid-template-columns:repeat(${(s.chords || []).length},1fr)">${(s.chords || [])
      .map(
        (c) => `<div class="chord"><div class="roman">${esc(c.roman || "")}</div>
        <div class="name">${esc(c.name)}</div><div class="notes">${esc(c.notes || "")}</div>
        ${c.fn ? `<div class="fn">${esc(c.fn)}</div>` : ""}</div>`
      )
      .join("")}</div>
    ${s.body ? `<p class="body">${rich(s.body)}</p>` : ""}${note(s)}`,

  compare: (s) => {
    const col = (c) => `<div class="col"><div class="head">${rich(c.head)}</div>
      <ul>${(c.items || []).map((x) => `<li>${rich(x)}</li>`).join("")}</ul></div>`;
    return `${label(s)}<h2 class="title">${rich(s.title)}</h2>
    <div class="compare">${col(s.left)}${col(s.right)}</div>${note(s)}`;
  },

  photo: async (s, i) => `
    ${await photo(i, s.image)}
    ${s.title ? `<h2 class="title">${rich(s.title)}</h2>` : ""}
    ${s.body ? `<p class="body">${rich(s.body)}</p>` : ""}`,

  instructor: async (s, i) => {
    const band = Array(8).fill(esc(s.subject || "")).join(" · ");
    return `<div class="poster">
      <div class="top"><div>${esc(s.subject || "")}</div><div>${esc(brand.nameEn)}</div></div>
      <div class="mid">${await photo(i, s.image)}
        <div class="names"><div class="name-en">${esc(s.nameEn)}</div>
          <div class="name-ko">${esc(s.nameKo)}</div>
          ${s.role ? `<div class="role">${rich(s.role)}</div>` : ""}</div></div>
      <div class="band">${band}</div></div>
    ${s.meta ? `<div class="meta">${s.meta.map((m) => `<div><b>${esc(m.k)}</b>${rich(m.v)}</div>`).join("")}</div>` : ""}`;
  },

  closing: (s) => `
    <div><div class="principle">${rich(s.principle || s.title || "")}</div>
      ${s.body ? `<p class="body">${rich(s.body)}</p>` : ""}</div>
    <div class="sign">
      <div class="signature">${esc(brand.signature)}</div>
      <div class="signature-en">${esc(brand.signatureEn)}</div>
      <dl class="info">
        <dt>주소</dt><dd>${esc(brand.address)}</dd>
        <dt>전화</dt><dd>${esc(brand.phone)}</dd>
        <dt>운영</dt><dd>${esc(brand.hours)}</dd>
        ${s.directions !== false ? `<dt>오시는 길</dt><dd>${esc(brand.directions)}</dd>` : ""}
      </dl></div>`,
};

const total = deck.slides.length;
if (total < 5 || total > 7) warnings.push(`장수 ${total}장 (기본 5–7장)`);

const cards = [];
for (const [i, s] of deck.slides.entries()) {
  const fn = layouts[s.layout];
  if (!fn) throw new Error(`${i + 1}장: 알 수 없는 layout "${s.layout}" (가능: ${Object.keys(layouts).join(", ")})`);
  check(i, s);
  const theme = s.theme || deck.theme || "ivory";
  const bare = s.layout === "instructor";
  cards.push(`<section class="card layout-${s.layout} theme-${theme}" id="card-${i + 1}">
    ${bare ? "" : `<div class="masthead"><span>${esc(deck.masthead || brand.nameEn)}</span><span>${esc(deck.section || "")}</span></div>`}
    ${await fn(s, i)}
    <div class="colophon"><span>${esc(brand.nameEn)}</span><span class="page">${String(i + 1).padStart(2, "0")} / ${String(total).padStart(2, "0")}</span></div>
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
