// 브랜드 필름 문구를 투명 PNG(1080×1920)로 만든다 → _tmp/t_*.png
import path from "node:path";
import { writeFileSync } from "node:fs";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const require = createRequire(path.join(dir, "../../package.json"));
const { chromium } = require("playwright");
const T = {
  w_music: ["MUSIC"],
  w_create: ["CREATE"],
  w_practice: ["PRACTICE"],
  w_perform: ["PERFORM"],
  w_enoch: ["ENOCH", "MUSIC ACADEMY"],
};
const css = `@font-face{font-family:P;src:url(${pathToFileURL(path.join(dir, "../../templates/fonts/Pretendard-Medium.woff2")).href})}
@font-face{font-family:L;src:url(${pathToFileURL(path.join(dir, "../../templates/fonts/Pretendard-Light.woff2")).href})}
*{margin:0}html,body{background:transparent;width:1080px;height:1920px}
.sh{position:absolute;left:0;right:0;top:1250px;height:670px;background:linear-gradient(180deg,rgba(0,0,0,0),rgba(0,0,0,.42) 45%,rgba(0,0,0,.42) 70%,rgba(0,0,0,0))}
.w{position:absolute;left:0;right:0;top:1470px;text-align:center;color:#F1EDE4;text-shadow:0 1px 24px rgba(0,0,0,.55)}
.a{font-family:P;font-size:44px;letter-spacing:.5em;padding-left:.5em}.b{font-family:L;font-size:26px;letter-spacing:.4em;margin-top:24px;opacity:.85}`;
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
for (const [k, [a, s]] of Object.entries(T)) {
  writeFileSync(path.join(dir, "_tmp", "t.html"), `<!doctype html><meta charset="utf-8"><style>${css}</style><div class="sh"></div><div class="w"><div class="a">${a}</div>${s ? `<div class="b">${s}</div>` : ""}</div>`);
  await p.goto(pathToFileURL(path.join(dir, "_tmp", "t.html")).href);
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(150);
  await p.screenshot({ path: path.join(dir, "_tmp", k + ".png"), omitBackground: true });
}
await b.close();
