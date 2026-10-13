# 수노 프로듀싱 16회 앨범 제작 커리큘럼 (deck.html 생성)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
STEPS = [
  ("01", "Direction", "방향을 정합니다", [
    ("오리엔테이션", "음역대 분석 · 곡의 주제 정하기"),
    ("레퍼런스", "레퍼런스 곡 분석 · 사운드 방향 설정"),
    ("곡 선정", "곡 선정 · 코드 진행 설계"),
    ("탑라인", "멜로디 만들기 · 가이드 녹음")]),
  ("02", "Writing", "곡을 씁니다", [
    ("탑라인 II", "멜로디 다듬기 · 가이드 녹음"),
    ("작사 I", "이야기를 가사로 옮기기"),
    ("작사 II", "가사 완성 · 발음과 리듬 맞추기"),
    ("송폼 · 편곡", "곡의 구조와 악기 구성")]),
  ("03", "Arrangement", "곡을 다듬습니다", [
    ("송폼 · 편곡 II", "편곡 완성"),
    ("디테일 I", "사운드 · 구성 세부 수정"),
    ("디테일 II", "최종 수정"),
    ("아티스트 아이덴티티", "아티스트명 · 콘셉트 · 커버 아트 · 곡 소개글")]),
  ("04", "Release", "세상에 내놓습니다", [
    ("레코딩", "보컬 레코딩 · 90분"),
    ("믹싱 · 마스터링", "30분"),
    ("완성 · 피드백", "최종 음원 확인"),
    ("발매", "음원 발매")]),
]
FONT = ''.join(f"@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-{n}.woff2);font-weight:{w}}}" for n, w in [("Light",300),("Regular",400),("Medium",500),("SemiBold",600),("Bold",700)])
CSS = '''*{box-sizing:border-box;margin:0;padding:0}
:root{--iv:#F1EDE4;--bk:#111;--g:#8A8A8A;--b:#55524D;--bt:#F1E8CB;--hair:rgba(17,17,17,.16);--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace;--en:"Helvetica Neue",Helvetica,Arial,"Liberation Sans",P,sans-serif}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--iv);color:var(--bk);font-family:P,sans-serif;margin-bottom:40px;word-break:keep-all}
.s.dark{background:var(--bk);color:var(--iv)}
.hd{position:absolute;left:96px;right:96px;top:72px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:21px;letter-spacing:3px;padding-bottom:20px;border-bottom:1.5px solid currentColor}
.ft{position:absolute;left:96px;right:96px;bottom:60px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2px;padding-top:20px;border-top:1.5px solid currentColor}
.ft span:first-child{font-family:P,sans-serif;letter-spacing:0;font-size:21px}
.k{font-family:var(--mono);font-size:19px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
.h{font-size:76px;font-weight:700;letter-spacing:-3.4px;line-height:1.18}
.h em{font-style:normal;font-weight:300}
.p{font-size:29px;line-height:1.72;color:var(--b);letter-spacing:-.6px}.p b{color:var(--bk)}
.dark .p{color:#C9C4BB}.dark .p b{color:var(--iv)}
.step{position:absolute;left:96px;right:96px}
.step .top{display:flex;align-items:baseline;gap:22px;padding-bottom:16px;border-bottom:1.5px solid var(--bk)}
.step .no{font-family:var(--en);font-size:64px;font-weight:700;letter-spacing:-2px;line-height:1}
.step .en{font-family:var(--en);font-size:30px;font-weight:700;letter-spacing:-.5px;text-transform:uppercase}
.step .ko{margin-left:auto;font-size:24px;color:var(--b)}
.row{display:grid;grid-template-columns:90px 260px 1fr;padding:17px 0;border-bottom:1px solid var(--hair);align-items:baseline}
.row .n{font-family:var(--mono);font-size:20px;color:var(--g);letter-spacing:1px}
.row .t{font-size:27px;font-weight:600;letter-spacing:-.6px}
.row .d{font-size:23px;color:var(--b);letter-spacing:-.4px}
.dark .step .top{border-bottom-color:var(--iv)}
.dark .row{border-bottom-color:rgba(241,237,228,.16)}
.dark .row .d{color:#C9C4BB}
.hl{background:var(--bt);margin:0 -20px;padding:17px 20px}
.dark .hl{background:#2A2825}
/* 한 장 요약 */
#full .step .top{padding-bottom:10px}
#full .step .no{font-size:40px}#full .step .en{font-size:22px}#full .step .ko{font-size:19px}
#full .row{grid-template-columns:56px 200px 1fr;padding:9px 0}
#full .hl{padding:9px 20px}
#full .row .n{font-size:16px}#full .row .t{font-size:21px}#full .row .d{font-size:18px}
'''
H = lambda r="ENOCH PRODUCING": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
F = lambda n, t=5: f'<div class="ft"><span>SUNO PRODUCING — 앨범 제작 과정</span><span>0{n} / 0{t}</span></div>'

def step(i, top, start, hl_last=False):
    no, en, ko, rows = STEPS[i]
    r = ''
    for j, (t, d) in enumerate(rows):
        cls = ' hl' if (hl_last and i == 3 and j == 3) else ''
        r += f'<div class="row{cls}"><span class="n">{start+j:02d}</span><span class="t">{t}</span><span class="d">{d}</span></div>'
    return f'<div class="step" style="top:{top}px"><div class="top"><span class="no">{no}</span><span class="en">{en}</span><span class="ko">{ko}</span></div>{r}</div>'

S = []
S.append(f'''<section class="s" id="c1">{H()}
<div class="k" style="position:absolute;left:96px;top:190px">Album Course · ENOCH MUSIC ACADEMY</div>
<div style="position:absolute;left:88px;top:260px;font-family:var(--en);font-weight:700;font-size:150px;letter-spacing:-6px;line-height:.9">SUNO<br>PRODUCING</div>
<div style="position:absolute;left:92px;top:560px;font-family:var(--en);font-weight:300;font-size:140px;letter-spacing:-6px;line-height:.9;color:var(--g)">16 SESSIONS</div>
<div style="position:absolute;left:96px;right:96px;top:860px;border-top:1.5px solid var(--bk);display:grid;grid-template-columns:repeat(4,1fr)">''' + ''.join(f'<div style="padding-top:16px;font-family:var(--en);font-size:20px;font-weight:700;letter-spacing:.5px">{no}&nbsp;&nbsp;{en.upper()}</div>' for no,en,_,_ in STEPS) + f'''</div>
<div class="h" style="position:absolute;left:92px;top:960px;font-size:72px;letter-spacing:-3.2px;line-height:1.16">16회 만에,<br><em>내 이름의 한 곡</em></div>
<div class="p" style="position:absolute;left:96px;top:1150px;font-size:26px">주제를 정하는 날부터 음원이 발매되는 날까지.</div>
<div style="position:absolute;left:0;right:0;bottom:0;height:64px;background:var(--bk);color:var(--iv);font-family:var(--mono);font-size:20px;letter-spacing:4px;white-space:nowrap;display:flex;align-items:center"><span style="padding-left:30px">DIRECTION — WRITING — ARRANGEMENT — RELEASE — SUNO PRODUCING — DIRECTION — WRITING — ARRANGEMENT — RELEASE</span></div>
</section>''')
S.append(f'''<section class="s" id="c2">{H()}
<div class="k" style="position:absolute;left:96px;top:200px">The Course</div>
<div class="h" style="position:absolute;left:92px;top:250px">방향부터 발매까지,<br><em>네 단계</em></div>
<div class="p" style="position:absolute;left:96px;right:96px;top:520px">한 사람의 목소리와 이야기에서 출발합니다.<br>음역대를 확인하고, 하고 싶은 이야기를 정한 뒤<br>곡을 쓰고, 다듬고, 녹음해서 발매까지.</div>
<div style="position:absolute;left:96px;right:96px;top:820px;display:grid;grid-template-columns:repeat(4,1fr);border-top:1.5px solid var(--bk)">
''' + ''.join(f'<div style="padding:24px 18px 0 0;border-right:1px solid var(--hair);{"border-right:0;" if i==3 else ""}{"padding-left:18px;" if i else ""}"><div style="font-family:var(--en);font-size:56px;font-weight:700;letter-spacing:-2px">{no}</div><div style="font-family:var(--en);font-size:22px;font-weight:700;text-transform:uppercase;margin-top:8px">{en}</div><div style="font-size:22px;color:var(--b);margin-top:8px">{ko}</div><div class="k" style="margin-top:26px;font-size:16px">Session {i*4+1:02d}–{i*4+4:02d}</div></div>' for i,(no,en,ko,_) in enumerate(STEPS)) + f'''</div>
{F(2)}</section>''')
S.append(f'''<section class="s" id="c3">{H("CURRICULUM 01 — 02")}
{step(0, 180, 1)}{step(1, 680, 5)}
{F(3)}</section>''')
S.append(f'''<section class="s" id="c4">{H("CURRICULUM 03 — 04")}
{step(2, 180, 9)}{step(3, 680, 13, True)}
{F(4)}</section>''')
S.append(f'''<section class="s dark" id="c5">{H("THE ENOCH WAY")}
<div style="position:absolute;left:84px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h" style="position:absolute;left:92px;top:450px">같은 도구라도,<br><span style="color:var(--bt)">이야기는 한 사람의 것.</span></div>
<div class="p" style="position:absolute;left:96px;right:96px;top:720px">같은 곡도, 사람마다 다르게 가르칩니다.<br>SUNO PRODUCING 과정도 처음부터 끝까지 <b>1:1</b>입니다.</div>
<div style="position:absolute;left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>
{F(5)}</section>''')
# 블로그·플레이스용 한 장 요약
S.append(f'''<section class="s" id="full">{H("SUNO PRODUCING — 16 SESSIONS")}
<div class="h" style="position:absolute;left:92px;top:150px;font-size:54px;letter-spacing:-2.2px"><span style="font-family:var(--en)">SUNO PRODUCING</span> <em>앨범 제작 과정</em></div>
{step(0, 250, 1)}{step(1, 490, 5)}{step(2, 730, 9)}{step(3, 970, 13, True)}
<div style="position:absolute;left:96px;right:96px;bottom:60px;display:flex;justify-content:space-between;font-size:20px;padding-top:18px;border-top:1.5px solid var(--bk)"><span>에녹실용음악학원 시흥점 · 모든 과정 1:1</span><span style="font-family:var(--mono)">010 3949 3666</span></div>
</section>''')
open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>수노 프로듀싱 커리큘럼</title><style>{FONT}{CSS}</style></head><body>'+''.join(S)+'</body></html>')
