#!/usr/bin/env node
// 확정본과 새 결과물을 나란히 놓은 비교 이미지를 만든다.
// 사용법: node scripts/compare.mjs output/<주제 폴더> [templates/reference/ENOCH_ISSUE_01]
// 결과: output/<주제 폴더>/compare/01.png ... (왼쪽 확정본, 오른쪽 새 결과물)
// 장 번호가 같은 확정본이 없으면 레이아웃 이름이 같은 확정본 장을 찾아 쓴다.
import { readFile, readdir, mkdir } from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const [projectArg, refArg = "templates/reference/ENOCH_ISSUE_01"] = process.argv.slice(2);
if (!projectArg) {
  console.error("사용법: node scripts/compare.mjs output/<주제 폴더> [기준 폴더]");
  process.exit(1);
}
const projectDir = path.resolve(projectArg);
const refDir = path.resolve(root, refArg);

const imgs = async (dir) =>
  (await readdir(dir)).filter((f) => /^\d{2}\.(png|jpe?g)$/i.test(f)).sort();
const dataUrl = async (file) =>
  `data:image/${/png$/i.test(file) ? "png" : "jpeg"};base64,${(await readFile(file)).toString("base64")}`;

const mine = await imgs(projectDir);
const refs = await imgs(refDir);
const layoutsOf = async (dir) => {
  try {
    return JSON.parse(await readFile(path.join(dir, "slides.json"), "utf8")).slides.map((s) => s.layout);
  } catch {
    return [];
  }
};
const myLayouts = await layoutsOf(projectDir);
const refLayouts = await layoutsOf(refDir);

const { chromium } = await import("playwright");
const browser = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const page = await browser.newPage({ viewport: { width: 2200, height: 1440 } });
const outDir = path.join(projectDir, "compare");
await mkdir(outDir, { recursive: true });

for (const [i, f] of mine.entries()) {
  const layout = myLayouts[i];
  const nth = myLayouts.slice(0, i).filter((l) => l === layout).length;
  const refIdx = refLayouts.map((l, k) => (l === layout ? k : -1)).filter((k) => k >= 0);
  let r = refIdx.length ? refIdx[Math.min(nth, refIdx.length - 1)] : -1;
  if (r < 0) r = Math.min(i, refs.length - 1);
  const ref = refs[r];
  const cell = (src, label) => `<figure><figcaption>${label}</figcaption><img src="${src}"></figure>`;
  await page.setContent(`<html><body style="margin:0;background:#666;display:flex;gap:40px;padding:0 20px 20px;font:22px monospace;color:#fff">
    <style>figure{margin:0}figcaption{height:50px;line-height:50px}img{width:1060px;height:1325px;display:block}</style>
    ${cell(await dataUrl(path.join(refDir, ref)), `확정본 ${ref} (${refLayouts[r] || "-"})`)}
    ${cell(await dataUrl(path.join(projectDir, f)), `새 결과물 ${f} (${layout || "-"})`)}</body></html>`);
  await page.screenshot({ path: path.join(outDir, f.replace(/\.\w+$/, ".png")), fullPage: true });
}
await browser.close();
console.log(`비교 이미지 ${mine.length}장: ${path.relative(process.cwd(), outDir)}/`);
