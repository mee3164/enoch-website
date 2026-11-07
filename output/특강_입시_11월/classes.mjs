// 특강별 포스터 6장 (학원 내부 게시용, A4 세로 1240×1754 @2x) → posters/01.png ~ 06.png
// node output/특강_입시_11월/classes.mjs   (사진은 src/에 두고, 저장소에는 올리지 않는다)
import { writeFileSync, mkdirSync } from "node:fs";
import path from "node:path"; import { fileURLToPath, pathToFileURL } from "node:url"; import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");
const C = [
  { en: "HARMONY", ko: "전통 화성학", weeks: "8주 과정", img: "01_harmony.jpg", pos: "50% 50%",
    lead: "2차 시험 실기·필기 대비", desc: ["화성의 원리를 처음부터 차근차근 정리합니다.", "실기와 필기에서 묻는 내용을 함께 다룹니다."],
    who: "모든 전공 입시생", time: "8주 · 주 1회 (총 8회)", start: "11월 16일" },
  { en: "VOCAL\nENSEMBLE", ko: "보컬 앙상블", weeks: "4주 과정", img: "02_vocal.jpg", pos: "50% 40%",
    lead: "블렌딩 · 시창 · 다성부 코러스 · 무대 매너", desc: ["여러 목소리가 하나로 섞이는 법을 연습합니다.", "시창과 코러스, 무대에서의 태도까지 함께 다룹니다."],
    who: "보컬 · 싱어송라이터 전공", time: "4주 · 주 1회 (총 4회)", start: "11월 16일" },
  { en: "BAND\nENSEMBLE", ko: "악기 앙상블", weeks: "합주 · 4주 과정", img: "03_band.jpg", pos: "50% 55%",
    lead: "리듬 섹션 간의 호흡, 장르별 실전 초견 합주", desc: ["Jazz · Pop · Funk 등 장르별로 합주합니다.", "처음 보는 악보로 맞춰 보는 초견 합주를 대비합니다."],
    who: "기악 · 보컬 · 싱어송라이터 전공", time: "4주 · 주 1회 (총 4회)", start: "추후 공지" },
  { en: "JAM\nSESSION", ko: "잼", weeks: "즉흥연주 · 4주 과정", img: "04_jam.jpg", pos: "50% 45%",
    lead: "즉흥 · 반주 섹션 간의 호흡, 장르별 실전 초견 합주", desc: ["Jazz · Pop · Funk 등 장르별로 즉흥 연주를 합니다.", "반주와 솔로를 주고받는 호흡을 익힙니다."],
    who: "기악 전공 (기타 · 드럼 · 베이스 · 건반)", time: "4주 · 주 1회 (총 4회)", start: "추후 공지" },
  { en: "SCORE\nWRITING", ko: "악보 제작", weeks: "채보 · 사보 · 4주 과정", img: "05_score.jpg", pos: "45% 50%",
    lead: "장르별 악보 제작, 입시곡 악보 제작", desc: ["들은 음악을 악보로 옮기는 채보를 연습합니다.", "입시곡 악보를 깔끔하게 정리하는 사보를 다룹니다."],
    who: "기악 · 보컬 · 싱어송라이터 전공", time: "4주 · 주 1회 (총 4회)", start: "추후 공지" },
  { en: "MIDI\nBASICS", ko: "미디 기초", weeks: "시퀀싱 · 4주 과정", img: "06_midi.jpg", pos: "60% 50%",
    lead: "미디 기초와 베이직 다지기", desc: ["작곡 프로그램의 기본 사용법부터 시작합니다.", "개인 노트북 지참 또는 단체실 이용 (노트북이 없어도 괜찮습니다)."],
    who: "작곡에 관심 있는 누구나", time: "4주 · 주 1회 (총 4회)", start: "추후 공지" },
];
const F = (w) => pathToFileURL(path.join(dir, `../../templates/fonts/Pretendard-${w}.woff2`)).href;
const css = `@font-face{font-family:P;src:url(${F("Light")});font-weight:300}@font-face{font-family:P;src:url(${F("Regular")});font-weight:400}
@font-face{font-family:P;src:url(${F("SemiBold")});font-weight:600}@font-face{font-family:P;src:url(${F("Bold")});font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}body{width:1240px;height:1754px}
.c{width:1240px;height:1754px;position:relative;overflow:hidden;background:#F1EDE4;color:#111;font-family:P,sans-serif;word-break:keep-all}
.mono{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace}
.hd,.ft{position:absolute;left:84px;right:84px;display:flex;justify-content:space-between;font-size:20px;letter-spacing:2.6px}
.hd{top:66px;padding-bottom:18px;border-bottom:2px solid #111}.ft{bottom:62px;padding-top:18px;border-top:2px solid #111;font-size:19px;letter-spacing:1.4px}
.ph{position:absolute;left:84px;right:84px;top:136px;height:720px;overflow:hidden;background:#222}
.ph img{width:100%;height:100%;object-fit:cover;filter:grayscale(1) sepia(.16) contrast(1.04)}
.no{position:absolute;left:84px;top:896px;font-size:20px;letter-spacing:2.6px;color:#8A8A8A}
.en{position:absolute;left:84px;top:938px;font-weight:700;font-size:112px;line-height:.9;letter-spacing:-3.5px;white-space:pre-line}
.ko{position:absolute;right:84px;top:946px;text-align:right}.ko b{display:block;font-size:56px;font-weight:700;letter-spacing:-1.5px}
.ko span{display:block;margin-top:10px;font-size:24px;color:#8A8A8A;font-weight:400}
.lead{position:absolute;left:84px;right:84px;top:1176px;padding:20px 0;border-top:1px solid #111;border-bottom:1px solid #111;font-size:30px;font-weight:600;letter-spacing:-.5px}
.desc{position:absolute;left:84px;right:84px;top:1272px;font-size:25px;font-weight:300;color:#333;line-height:1.7}
.grid{position:absolute;left:84px;right:84px;top:1390px;display:grid;grid-template-columns:1.25fr 1fr 1fr;gap:0}
.grid>div{padding:18px 20px 18px 0;border-top:1px solid #c9c3b8}.grid .k{font-size:15px;letter-spacing:2.4px;color:#8A8A8A;margin-bottom:8px}
.grid .v{font-size:24px;font-weight:600;line-height:1.35}
.note{position:absolute;left:84px;right:84px;top:1556px;display:flex;justify-content:space-between;font-size:21px;line-height:1.55;color:#333}
.note b{font-weight:700;color:#111}`;
mkdirSync(path.join(dir, "posters"), { recursive: true });
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1240, height: 1754 }, deviceScaleFactor: 2 });
for (const [i, c] of C.entries()) {
  const n = String(i + 1).padStart(2, "0");
  const html = `<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>${css}</style></head><body><section class="c">
<div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>ADMISSION — SPECIAL CLASS ${n}</span></div>
<div class="ph"><img src="src/${c.img}" style="object-position:${c.pos}"></div>
<div class="no mono">SPECIAL CLASS ${n} / 06</div>
<div class="en">${c.en}</div>
<div class="ko"><b>${c.ko}</b><span>${c.weeks}</span></div>
<div class="lead">${c.lead}</div>
<div class="desc">${c.desc.join("<br>")}</div>
<div class="grid"><div><div class="k mono">FOR</div><div class="v">${c.who}</div></div><div><div class="k mono">SCHEDULE</div><div class="v">${c.time}</div></div><div><div class="k mono">START</div><div class="v">${c.start}</div></div></div>
<div class="note"><span><b>신청</b> 사무실 방문 접수 · 상시 접수 · 선착순<br>단체 수업으로 진행되어 결석 시 보강이 어렵습니다.</span><span style="text-align:right"><b>031 315 3666</b><br>경기도 시흥시 은행로 157 2층</span></div>
<div class="ft mono"><span>에녹실용음악학원 시흥점</span><span>평일 13:00–22:00 · 토 10:00–18:00</span></div>
</section></body></html>`;
  const f = path.join(dir, `_class.html`); writeFileSync(f, html);
  await p.goto(pathToFileURL(f).href); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(200);
  await p.screenshot({ path: path.join(dir, "posters", `${n}.png`) }); console.log(`posters/${n}.png ${c.ko}`);
}
await b.close();
