// 스토리 2장 버전 (메인 + 약력 한 장): story.html의 #R 장과, 약력 두 장을 한 장으로 합친 #D → story2_01.png, story2_02.png
// CHROMIUM_PATH=... node output/강사소개_한상희/story2.mjs
import path from "node:path";
import { readFileSync, writeFileSync } from "node:fs";
import { fileURLToPath, pathToFileURL } from "node:url";
import { createRequire } from "node:module";
const dir = path.dirname(fileURLToPath(import.meta.url));
const { chromium } = createRequire(path.join(dir, "../../package.json"))("playwright");

const src = readFileSync(path.join(dir, "story.html"), "utf8");
const head = src.slice(0, src.indexOf("</style>"));
const rStart = src.indexOf('<section class="s" id="R">');
const main = src.slice(rStart, src.indexOf("</section>", rStart) + "</section>".length);

const css = `
#D .body{top:420px}
#D .sec{grid-template-columns:200px 1fr;padding:18px 0}
#D .sec .lab{font-size:16px;padding-top:6px}
#D .sec li{font-size:25px;line-height:1.46}
#D .bt{top:1680px}
`;
const sec = (lab, items) => `<div class="sec"><span class="lab g">${lab}</span><ul>${items.map((x) => `<li>${x}</li>`).join("")}</ul></div>`;
const career = `<section class="s dt" id="D">
  <div class="top"><span class="lab g">ENOCH TEACHERS — DRUM</span><span class="lab g">CAREER</span></div>
  <div class="nm">HAN SANG HEE<small>한상희</small></div>
  <div class="body">
  ${sec("EDUCATION", ["경희대 대학원 실용음악과 출강 <i>(전)</i>", "호원대학교 실용음악과 졸업 <i>Drum Major · 차석입학</i>"])}
  ${sec("AWARDS", ["제3회 경향 실용음악 콩쿠르 드럼 부문 1위", "K-CCM AWARDS CCM 음원 부문 대상 <i>히스플랜</i>", "신한카드 루키 프로젝트 은상 <i>PERC%NT</i>", "KBS 밴드 서바이벌 Top밴드 16강"])}
  ${sec("BAND", ["번아웃하우스 <i>Burnout House · 1st EP 참여</i>", "발렌시아코트 드럼 멤버 <i>Valencia Coat</i>", "CCM팀 히스플랜 대표 <i>HISPLAN · 모든 앨범 편곡 및 드럼</i>"])}
  ${sec("LIVE", ["검정치마 전속 라이브 세션 <i>The Black Skirts</i>", "윤종신 '좋니 콘서트' 전국투어 오프닝 밴드 전속 드러머", "계범주 Billboard.com 라이브 세션 · 1st 단독 콘서트", "연정 전속 드러머 <i>GMF, 뷰민라 등</i>", "피아니스트 윤한 '퀸을 위하여' 50인조 오케스트라 협연", "장재인 · 민서 · 퍼센트 등 라이브 세션", "미스틱 엔터테인먼트 Mystic Open Run · 네이버 온스테이지", "옹기장이 카운트다운 콘서트"])}
  ${sec("RECORDING", ["블락비 <i>Nice Day</i> · 애프터스쿨 <i>화장을 하다 울었어</i>", "피아니스트 윤한 <i>B형 여자, Cafe de Wilsberg</i>", "루이 (긱스) 솔로 앨범 <i>Change The Game (Rock Ver.)</i>", "스페이스맨 싱글앨범 · 웹드라마 '너를 찾아서' OST <i>그런거야</i>", "장재인 <i>엽서</i> · 장희선 <i>Moonlight, 어는점</i> · 모니누와 <i>불꽃</i>", "연정 EP <i>GO</i> 전곡 세션"])}
  ${sec("PERC%NT", ["Blooming · Nine · 멍 · 불타올라라 연애세포 <i>드럼 세션</i>", "Super Hero · PVC – Music God <i>드럼 세션 · 편곡</i>", "YUIL <i>편곡 · 드럼 세션</i>"])}
  </div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Drum</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>`;

const out = path.join(dir, "story2.html");
writeFileSync(out, `${head}${css}</style></head><body>\n${main}\n${career}\n</body></html>\n`);
const b = await chromium.launch(process.env.CHROMIUM_PATH ? { executablePath: process.env.CHROMIUM_PATH } : {});
const p = await b.newPage({ viewport: { width: 1080, height: 1920 } });
await p.goto(pathToFileURL(out).href); await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
const ss = await p.$$("section");
for (const [i, s] of ss.entries()) await s.screenshot({ path: path.join(dir, `story2_0${i + 1}.png`) });
await b.close(); console.log(ss.length, "장");
