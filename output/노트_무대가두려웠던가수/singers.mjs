// 가수 장(nameEn이 있는 장, 02–06)을 같은 틀로 다시 만든다 — npm run cardnews:render 뒤에 실행
// node output/노트_무대가두려웠던가수/singers.mjs
// 틀: 키커 → 위 블록(사진 + credit / 사진 없으면 영어 원문을 크게) → 영문 이름 + 한글 이름 → 영어 원문 한 줄(사진 장만) → 번역(굵게) → 본문 → 출처
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath } from "node:url";
import path from "node:path";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(dir, "../..");
const require = createRequire(path.join(root, "package.json"));
const deck = JSON.parse(readFileSync(path.join(dir, "slides.json"), "utf8"));
const brand = JSON.parse(readFileSync(path.join(root, "templates/brand.json"), "utf8"));
const css = readFileSync(path.join(root, "templates/card.css"), "utf8");
const esc = (s = "") => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const rich = (s = "") => esc(s).replace(/\*\*(.+?)\*\*/g, '<span class="em">$1</span>');
const two = (n) => String(n).padStart(2, "0");
const total = deck.slides.length;

const local = `
.layout-singer { padding: 0; display: block; }
.sg-k { position: absolute; left: 96px; top: 166px; }
.sg-top { position: absolute; left: 96px; width: 888px; top: 214px; height: 484px; }
.sg-photo { width: 100%; height: 100%; background-size: cover; background-position: center; filter: grayscale(1) sepia(.18) contrast(1.02); }
.sg-credit { position: absolute; right: 0; top: 496px; font-family: var(--mono); font-size: 15px; letter-spacing: 1px; color: var(--sub); }
.sg-quote { height: 100%; display: flex; align-items: flex-end; padding-bottom: 40px; border-bottom: 1.5px solid var(--rule);
  font-family: var(--en); font-weight: 700; letter-spacing: -2px; line-height: 1.04; white-space: pre-line; }
.sg-low { position: absolute; left: 96px; right: 96px; top: 756px; }
.sg-name { display: flex; align-items: baseline; gap: 22px; }
.sg-en { font-family: var(--en); font-size: 50px; font-weight: 700; letter-spacing: -1.5px; line-height: 1; text-transform: uppercase; }
.sg-ko { font-size: 26px; font-weight: 300; color: var(--sub); letter-spacing: 1px; }
.sg-qen { margin-top: 26px; font-family: var(--mono); font-size: 20px; letter-spacing: .4px; color: var(--sub); }
.sg-title { margin-top: 18px; font-size: 44px; font-weight: 800; line-height: 1.34; letter-spacing: -1.4px; white-space: pre-line; }
.sg-name + .sg-title { margin-top: 30px; }
.sg-body { margin-top: 22px; }
.sg-body .body { font-size: 26px; line-height: 1.72; }
.sg-body .body + .body { margin-top: 10px; }
.sg-src { position: absolute; left: 96px; right: 96px; top: 1178px; font-family: var(--mono); font-size: 17px; letter-spacing: 1px; color: var(--sub); }
`;

const img = (rel) => `data:image/jpeg;base64,${readFileSync(path.join(root, rel)).toString("base64")}`;
const cards = [];
deck.slides.forEach((s, i) => {
  if (!s.nameEn) return;
  const q = String(s.quoteEn || "").replace(/^"|"$/g, "");
  const top = s.image
    ? `<div class="sg-top"><div class="sg-photo" style="background-image:url(${img(s.image)});background-position:${s.imagePosition || "center"}"></div>
       ${s.credit ? `<div class="sg-credit">${esc(s.credit)}</div>` : ""}</div>`
    : `<div class="sg-top"><div class="sg-quote" style="font-size:${s.quoteSize || 72}px">“${esc(s.quoteBreak || q)}”</div></div>`;
  cards.push(`<section class="card layout-singer theme-${s.theme || deck.theme || "ivory"}" id="card-${i + 1}">
    <div class="masthead"><span>${esc(brand.nameEn)}</span><span>${esc(deck.masthead)}</span></div>
    <div class="kicker sg-k">${esc(s.kicker)}</div>
    ${top}
    <div class="sg-low">
      <div class="sg-name"><span class="sg-en">${esc(s.nameEn)}</span><span class="sg-ko">${esc(s.nameKo)}</span></div>
      ${s.image ? `<div class="sg-qen">“${esc(q)}”</div>` : ""}
      <h2 class="sg-title">${rich(s.title)}</h2>
      <div class="sg-body">${(Array.isArray(s.body) ? s.body : [s.body]).map((p) => `<p class="body">${rich(p)}</p>`).join("")}</div>
    </div>
    <div class="sg-src">${esc(s.source || "")}</div>
    <div class="colophon"><span>${esc(deck.footer)}</span><span class="page">${two(i + 1)} / ${two(total)}</span></div>
  </section>`);
});

const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}${local}</style></head><body class="preview">${cards.join("\n")}</body></html>`;
writeFileSync(path.join(dir, "singers.html"), html);
const { chromium } = require("playwright");
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1350 } });
await p.goto("file://" + path.join(dir, "singers.html"), { waitUntil: "load", timeout: 20000 }).catch(() => {});
await p.evaluate(() => document.fonts.ready);
await p.waitForTimeout(500);
for (const [i, s] of deck.slides.entries()) {
  if (!s.nameEn) continue;
  await p.locator(`#card-${i + 1}`).screenshot({ path: path.join(dir, `${two(i + 1)}.png`) });
  console.log(`${two(i + 1)}.png (${s.nameEn})`);
}
await b.close();
