#!/usr/bin/env node
// 카드뉴스 렌더러: <project>/slides.json → <project>/out/preview.html + 01.png, 02.png ...
// 사용법: node cardnews/scripts/render.mjs cardnews/projects/<id> [--html-only]
import { readFile, writeFile, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const root = path.resolve(here, "..");

const [projectArg, ...flags] = process.argv.slice(2);
if (!projectArg) {
  console.error("사용법: node cardnews/scripts/render.mjs cardnews/projects/<id> [--html-only]");
  process.exit(1);
}
const projectDir = path.resolve(projectArg);
const htmlOnly = flags.includes("--html-only");

const brand = JSON.parse(await readFile(path.join(root, "brand/brand.json"), "utf8"));
const css = await readFile(path.join(root, "templates/card.css"), "utf8");
const deck = JSON.parse(await readFile(path.join(projectDir, "slides.json"), "utf8"));

// 글자 수 가이드 (브랜드 가이드 4장) — 넘으면 경고만 하고 렌더는 계속한다.
const LIMITS = { title: 40, body: 110, note: 70, subtitle: 50 };
const warnings = [];

const esc = (s = "") =>
  String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
// **강조** → 하이라이트
const rich = (s = "") => esc(s).replace(/\*\*(.+?)\*\*/g, '<span class="hl">$1</span>');
const plain = (s = "") => String(s).replace(/\*\*/g, "").replace(/\n/g, "");

function check(i, slide) {
  for (const [key, max] of Object.entries(LIMITS)) {
    if (slide[key] && plain(slide[key]).length > max) {
      warnings.push(`슬라이드 ${i + 1} ${key}: ${plain(slide[key]).length}자 (권장 ${max}자 이하)`);
    }
  }
}

const layouts = {
  cover: (s) => `
    <div class="brand-top">${esc(brand.nameEn)}</div>
    <span class="kicker">${esc(s.kicker || deck.series || "")}</span>
    <h1 class="title">${rich(s.title)}</h1>
    ${s.subtitle ? `<p class="subtitle">${rich(s.subtitle)}</p>` : ""}
    ${s.big ? `<div class="big">${esc(s.big)}</div>` : ""}`,

  point: (s) => `
    ${s.label ? `<div class="label">${esc(s.label)}</div>` : ""}
    <h2 class="title">${rich(s.title)}</h2>
    ${s.body ? `<p class="body">${rich(s.body)}</p>` : ""}
    ${s.note ? `<p class="note">${rich(s.note)}</p>` : ""}`,

  list: (s) => `
    ${s.label ? `<div class="label">${esc(s.label)}</div>` : ""}
    <h2 class="title">${rich(s.title)}</h2>
    <div class="items">${(s.items || [])
      .map((it, n) => {
        const o = typeof it === "string" ? { text: it } : it;
        return `<div class="item ${o.head ? "" : "plain"}"><div class="num">${n + 1}</div><div>
          ${o.head ? `<div class="head">${rich(o.head)}</div>` : ""}
          <div class="text">${rich(o.text || "")}</div></div></div>`;
      })
      .join("")}</div>
    ${s.note ? `<p class="note">${rich(s.note)}</p>` : ""}`,

  compare: (s) => {
    const col = (c, cls) => `<div class="col ${cls}"><div class="head">${rich(c.head)}</div>
      <ul>${(c.items || []).map((x) => `<li>${rich(x)}</li>`).join("")}</ul></div>`;
    return `
    ${s.label ? `<div class="label">${esc(s.label)}</div>` : ""}
    <h2 class="title">${rich(s.title)}</h2>
    <div class="compare">${col(s.left, "left")}${col(s.right, "right")}</div>
    ${s.note ? `<p class="note">${rich(s.note)}</p>` : ""}`;
  },

  chords: (s) => `
    ${s.label ? `<div class="label">${esc(s.label)}</div>` : ""}
    <h2 class="title">${rich(s.title)}</h2>
    <div class="chords">${(s.chords || [])
      .map(
        (c, n) => `${n ? '<div class="arrow">→</div>' : ""}<div class="chord">
        <div class="roman">${esc(c.roman || "")}</div>
        <div class="name">${esc(c.name)}</div>
        <div class="notes">${esc(c.notes || "")}</div>
        ${c.fn ? `<div class="fn">${esc(c.fn)}</div>` : ""}</div>`
      )
      .join("")}</div>
    ${s.body ? `<p class="body">${rich(s.body)}</p>` : ""}
    ${s.note ? `<p class="note">${rich(s.note)}</p>` : ""}`,

  quiz: (s) => `
    <span class="kicker">${esc(s.kicker || "QUIZ")}</span>
    <h2 class="title" style="margin-top:40px">${rich(s.title)}</h2>
    <div class="options">${(s.options || [])
      .map((o, n) => `<div class="option"><b>${"ABCDE"[n]}</b>${rich(o)}</div>`)
      .join("")}</div>
    ${s.note ? `<p class="note">${rich(s.note)}</p>` : ""}`,

  summary: (s) => layouts.list({ ...s, label: s.label || "SUMMARY" }),

  cta: (s) => `
    ${s.saveHint !== false ? `<div class="save-hint">🔖 저장해 두고 꺼내 보세요</div>` : ""}
    <h2 class="title">${rich(s.title)}</h2>
    ${s.body ? `<p class="body">${rich(s.body)}</p>` : ""}
    ${s.button ? `<div class="button">${esc(s.button)}</div>` : ""}
    <p class="contact">${esc(brand.name)}  ${esc(brand.instagram)}
${esc(s.contact || `문의 ${brand.phone} · 카카오톡 ${brand.kakao}`)}</p>`,
};

const total = deck.slides.length;
const cards = deck.slides.map((s, i) => {
  const fn = layouts[s.layout];
  if (!fn) throw new Error(`슬라이드 ${i + 1}: 알 수 없는 layout "${s.layout}" (가능: ${Object.keys(layouts).join(", ")})`);
  check(i, s);
  const theme = s.theme || deck.theme || "dark";
  return `<section class="card layout-${s.layout} theme-${theme}" id="card-${i + 1}">
    ${fn(s)}
    <div class="footer"><span>${esc(brand.instagram)}</span><span class="page">${i + 1} / ${total}</span></div>
  </section>`;
});

const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8">
<title>${esc(deck.title || deck.id)}</title><style>${css}</style></head>
<body class="preview">${cards.join("\n")}</body></html>`;

const outDir = path.join(projectDir, "out");
await mkdir(outDir, { recursive: true });
await writeFile(path.join(outDir, "preview.html"), html);
console.log(`✔ HTML 미리보기: ${path.relative(process.cwd(), path.join(outDir, "preview.html"))}`);

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
  // 폰트 CDN이 막힌 환경에서도 로컬 폰트로 계속 진행한다.
  await page.setContent(html, { waitUntil: "load", timeout: 15000 }).catch(() => {});
  await page.evaluate(() => document.fonts.ready);
  for (let i = 0; i < total; i++) {
    const file = path.join(outDir, `${String(i + 1).padStart(2, "0")}.png`);
    await page.locator(`#card-${i + 1}`).screenshot({ path: file });
  }
  await browser.close();
  console.log(`✔ PNG ${total}장: ${path.relative(process.cwd(), outDir)}/01.png ~ ${String(total).padStart(2, "0")}.png`);
}

const todo = ["instagram", "phone", "location", "kakao"].filter((k) => String(brand[k]).includes("TODO"));
if (todo.length) warnings.push(`brand.json에 TODO가 남아 있습니다: ${todo.join(", ")} — 게시 전 실제 정보로 바꿔 주세요`);

if (warnings.length) {
  console.warn("\n⚠ 경고 (디자이너/카피라이터 확인 필요):");
  warnings.forEach((w) => console.warn("  - " + w));
}
