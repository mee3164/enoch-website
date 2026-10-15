# ENOCH NOTE — 연습실로 오는 습관 (『아주 작은 습관의 힘』 6장 기반, deck.html 생성)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

FONT = '''@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Medium.woff2);font-weight:500}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}
@font-face{font-family:S;src:url(../../templates/fonts/dm-serif-display-latin-400-normal.woff2)}'''
CSS = '''*{box-sizing:border-box;margin:0;padding:0}
:root{--iv:#F1EDE4;--bk:#111;--g:#8A8A8A;--b:#55524D;--bu:#F1E8CB;--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace;--en:"Helvetica Neue",Helvetica,Arial,"Liberation Sans",P,sans-serif}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--iv);color:var(--bk);font-family:P,sans-serif;margin-bottom:40px;word-break:keep-all}
.s.dark{background:var(--bk);color:var(--iv)}
.hd{position:absolute;left:96px;right:96px;top:72px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:21px;letter-spacing:3px;padding-bottom:20px;border-bottom:1.5px solid currentColor}
.ft{position:absolute;left:96px;right:96px;bottom:60px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2px;padding-top:20px;border-top:1.5px solid currentColor}
.ft span:first-child{font-family:P,sans-serif;letter-spacing:0;font-size:21px}
.src{position:absolute;left:96px;right:96px;bottom:26px;font-size:13px;color:#A8A39A}
.k{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
.h{font-size:72px;font-weight:700;letter-spacing:-3.2px;line-height:1.22}
.h em{font-style:normal;font-weight:300}
.p{font-size:30px;line-height:1.75;color:var(--b);letter-spacing:-.6px}.p b{color:var(--bk)}
.dark .p{color:#C9C4BB}.dark .p b{color:var(--iv)}
.a{position:absolute}
.q{position:absolute;background:var(--bu);padding:44px 52px 40px 52px}
.q .t{font-size:38px;font-weight:500;line-height:1.55;letter-spacing:-1.2px}
.q .pg{margin-top:18px;font-size:20px;letter-spacing:-.2px;color:#7A7262}
.q:before{content:"“";position:absolute;left:30px;top:-46px;font-family:S,serif;font-size:150px;line-height:1;color:#B8A877}
.dark .q{background:#1E1D1B}.dark .q .pg{color:#9A958C}.dark .q:before{color:var(--bu)}
.row{display:flex;gap:30px;padding:24px 0;border-bottom:1px solid rgba(17,17,17,.15)}
.dark .row{border-bottom-color:rgba(241,237,228,.16)}
.row .n{width:200px;flex:none;font-size:28px;font-weight:700;letter-spacing:-.6px}
.row .t{font-size:28px;line-height:1.55;color:var(--b);letter-spacing:-.5px}
.dark .row .t{color:#C9C4BB}
'''
TOTAL = 7
HD = lambda r="ENOCH NOTE — PRACTICE ROOM": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT = lambda n: f'<div class="ft"><span>연습실로 오는 습관</span><span>0{n} / 0{TOTAL}</span></div>'
BOOK = '제임스 클리어, 『아주 작은 습관의 힘』, 이한이 옮김, 비즈니스북스'
SRC = lambda extra='': f'<div class="src">인용 출처: {BOOK}. {extra}</div>'
def quote(text, page, top, left=96, right=96):
    return f'<div class="q" style="left:{left}px;right:{right}px;top:{top}px"><div class="t">{text}</div><div class="pg">— {page}</div></div>'

S = []
# 01 표지
S.append(f"""<section class="s" id="c1">{HD()}
<img src="../../images/공간/복도_01.jpg" style="position:absolute;left:96px;top:150px;width:888px;height:650px;object-fit:cover;object-position:50% 45%;display:block;filter:saturate(.7) contrast(1.02)">
<div class="k a" style="left:96px;top:840px">Practice Room</div>
<div class="h a" style="left:92px;top:885px;font-size:80px;letter-spacing:-4px;line-height:1.18">왜 집보다 연습실에서,<br><em>연습이 더 잘 될까</em></div>
<div class="p a" style="left:96px;top:1120px;font-size:27px">의지보다 먼저, 장소가 행동을 정합니다.</div>
{FT(1)}<div class="src">사진: ENOCH 연습실 복도</div></section>""")

# 02 보이지 않는 손 + 레빈 공식
S.append(f"""<section class="s" id="c2">{HD()}
<div class="k a" style="left:96px;top:200px">Behavior = f (Person, Environment)</div>
<div class="a" style="left:92px;top:250px;font-family:var(--en);font-weight:700;font-size:150px;letter-spacing:-5px;line-height:1">B = <i style="font-family:Georgia,serif">f</i>(P, E)</div>
<div class="p a" style="left:96px;right:96px;top:440px">행동은 사람과, 그 사람을 둘러싼 환경이 함께 만든다는 공식.<br>1936년 심리학자 쿠르트 레빈의 말입니다.</div>
{quote("환경은 인간의 행동을 형성하는<br>보이지 않는 손이다.", "『아주 작은 습관의 힘』 116쪽", 720)}
{FT(2)}{SRC('116쪽.')}</section>""")

# 03 집이 어려운 이유
S.append(f"""<section class="s" id="c3">{HD()}
<div class="k a" style="left:96px;top:200px">Why Not Home</div>
<div class="h a" style="left:92px;top:250px">집에는,<br><em>다른 신호가 너무 많아요</em></div>
<div class="p a" style="left:96px;right:96px;top:520px">소파는 쉬는 곳, 침대는 눕는 곳, 휴대폰은 늘 손이 가는 곳.<br>악기를 꺼내기도 전에, 공간이 먼저 다른 일을 시킵니다.</div>
{quote("늘 비디오게임을 하던 거실에서는<br>주의를 분산시키는 것이 없다 해도<br>공부하기 어렵다.", "『아주 작은 습관의 힘』 123쪽", 830)}
{FT(3)}{SRC('123쪽.')}</section>""")

# 04 한 공간 한 가지 일
S.append(f"""<section class="s" id="c4">{HD()}
<div class="k a" style="left:96px;top:200px">One Space, One Thing</div>
<div class="a" style="left:92px;top:250px;font-size:120px;font-weight:700;letter-spacing:-6px;line-height:1.1">한 공간에서는<br><span style="font-weight:300">한 가지 일만</span></div>
<div class="a" style="left:96px;top:540px;font-size:22px;color:#7A7262">— 『아주 작은 습관의 힘』 124쪽</div>
<div class="p a" style="left:96px;right:96px;top:640px">연습실은 연습만 하는 곳.<br>문을 열고 들어오면, 무엇을 해야 할지 몸이 먼저 알거든요.<br><b>들어오는 순간이, 연습의 시작입니다.</b></div>
<div class="a" style="left:96px;right:96px;top:1000px;height:120px;background:var(--bu);display:flex;align-items:center;padding:0 48px;font-size:28px;letter-spacing:-.5px">새로운 환경에서 새로운 습관을 만들기 쉽다. <span style="color:#7A7262;font-size:20px;margin-left:16px">— 6장 요약</span></div>
{FT(4)}{SRC('124쪽, 6장 요약.')}</section>""")

# 05 집에서는 악기를 눈앞에 (검정)
S.append(f"""<section class="s dark" id="c5">{HD("AT HOME")}
<div class="k a" style="left:96px;top:200px;color:#9A958C">Make It Visible</div>
<div class="h a" style="left:92px;top:250px">집에서는,<br><em>악기를 눈앞에</em></div>
{quote("기타를 보이지 않는 곳에 넣어두면<br>연습하지 않게 된다.", "『아주 작은 습관의 힘』 119쪽", 540)}
{quote("기타 연습을 더욱 자주 하고 싶다면,<br>기타를 거실 한가운데 두어라.", "『아주 작은 습관의 힘』 120쪽", 860)}
{FT(5)}<div class="src" style="color:#6E6A64">인용 출처: {BOOK}. 119–120쪽.</div></section>""")

# 06 일단 오기
S.append(f"""<section class="s" id="c6">{HD()}
<div class="k a" style="left:96px;top:200px">Just Show Up</div>
<div class="h a" style="left:92px;top:250px">잘하는 것보다,<br><em>일단 오는 것부터</em></div>
<div class="a" style="left:96px;right:96px;top:560px;border-top:1.5px solid #111">
<div class="row"><span class="n">01 &nbsp;시간 정하기</span><span class="t">몇 시간 연습할지보다, <b style="color:#111">언제 갈지</b>를 먼저 정해 두기.</span></div>
<div class="row"><span class="n">02 &nbsp;전날 챙기기</span><span class="t">악보와 이어폰, 필요한 것을 전날 가방에. 가방이 신호가 됩니다.</span></div>
<div class="row"><span class="n">03 &nbsp;가볍게 시작</span><span class="t">도착하면 익숙한 곡 하나로 손부터 풀기. 시작이 쉬우면, 다음 곡으로 이어져요.</span></div>
</div>
{FT(6)}</section>""")

# 07 마무리 (검정)
S.append(f"""<section class="s dark" id="c7">{HD("THE ENOCH WAY")}
<div class="a" style="left:92px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h a" style="left:92px;top:450px">연습실 문을 여는 것까지가,<br><span style="color:var(--bu)">연습입니다.</span></div>
<div class="p a" style="left:96px;right:96px;top:720px">ENOCH 수강생은 운영시간 내<br>자유로운 연습실 이용이 가능합니다.<br>입시 · 취미 · 성인 · 전문, 모든 과정이 1:1.</div>
<div class="a" style="left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">평일 13–22시 · 토 10–18시 · 일 휴무</span></span></div>
{FT(7)}</section>""")

open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>연습실로 오는 습관</title><style>{FONT}{CSS}</style></head><body>' + ''.join(S) + '</body></html>')
