// 에디토리얼 타이포 상태를 투명 PNG(1080×1920)로 → _tmp/<name>.png
import path from "node:path";
import { writeFileSync } from "node:fs";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(dir, "../../package.json"));
const { chromium } = require("playwright");
const F = (w) => pathToFileURL(path.join(dir, `../../templates/fonts/Pretendard-${w}.woff2`)).href;
const css = `@font-face{font-family:B;src:url(${F("Bold")})}@font-face{font-family:M;src:url(${F("Medium")})}
*{margin:0}html,body{width:1080px;height:1920px;background:transparent;overflow:hidden}
.t{position:absolute;font-family:B;color:#F1EDE4;line-height:.86;letter-spacing:-.035em}
.s{position:absolute;font-family:M;color:#F1EDE4;font-size:34px;letter-spacing:.32em}`;
const MUSIC = `<div class="t" style="left:64px;top:230px;font-size:262px">MUSIC</div>`;
const PER = (n) => `<div class="t" style="left:64px;top:1080px;font-size:250px">${["PER", "FOR", "MANCE"].slice(0, n).join("<br>")}</div>`;
const S = {
  music: MUSIC,
  space: `<div class="s" style="left:72px;top:176px">A SPACE FOR</div>` + MUSIC,
  creation: `<div class="t" style="left:0;right:0;top:880px;text-align:center;font-size:150px;letter-spacing:.02em">CREATION</div>`,
  practice: `<div class="t" style="right:64px;top:300px;text-align:right;font-size:250px">PRAC<br>TICE</div>`,
  per1: PER(1), per2: PER(2), per3: PER(3),
  enoch: `<div style="position:absolute;inset:0;background:radial-gradient(ellipse 80% 22% at 50% 47%,rgba(0,0,0,.32),transparent)"></div><div class="t" style="left:0;right:0;top:760px;text-align:center;font-size:290px">ENOCH</div>
          <div class="s" style="left:0;right:0;top:1065px;text-align:center;font-size:30px;letter-spacing:.5em;padding-left:.5em">MUSIC ACADEMY</div>`,
};
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
for (const [k, html] of Object.entries(S)) {
  const f = path.join(dir, "_tmp", "t.html");
  writeFileSync(f, `<!doctype html><meta charset="utf-8"><style>${css}</style>${html}`);
  await p.goto(pathToFileURL(f).href); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(100);
  await p.screenshot({ path: path.join(dir, "_tmp", k + ".png"), omitBackground: true });
}
await b.close();
