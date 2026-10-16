# ENOCH NOTE — 연습일지 (deck.html 생성)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FONT='''@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Medium.woff2);font-weight:500}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}'''
CSS='''*{box-sizing:border-box;margin:0;padding:0}
:root{--iv:#F1EDE4;--bk:#111;--g:#8A8A8A;--b:#55524D;--bu:#F1E8CB;--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace;--en:"Helvetica Neue",Helvetica,Arial,"Liberation Sans",P,sans-serif}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--iv);color:var(--bk);font-family:P,sans-serif;margin-bottom:40px;word-break:keep-all}
.s.dark{background:var(--bk);color:var(--iv)}
.hd{position:absolute;left:96px;right:96px;top:72px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:21px;letter-spacing:3px;padding-bottom:20px;border-bottom:1.5px solid currentColor}
.ft{position:absolute;left:96px;right:96px;bottom:60px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2px;padding-top:20px;border-top:1.5px solid currentColor}
.ft span:first-child{font-family:P,sans-serif;letter-spacing:0;font-size:21px}
.k{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
.h{font-size:72px;font-weight:700;letter-spacing:-3.2px;line-height:1.22}
.h em{font-style:normal;font-weight:300}
.p{font-size:30px;line-height:1.75;color:var(--b);letter-spacing:-.6px}.p b{color:var(--bk)}
.dark .p{color:#C9C4BB}.dark .p b{color:var(--iv)}
.a{position:absolute}
.row{display:flex;gap:30px;padding:26px 0;border-bottom:1px solid rgba(17,17,17,.15)}
.dark .row{border-bottom-color:rgba(241,237,228,.16)}
.row .n{width:90px;flex:none;font-family:var(--en);font-size:44px;font-weight:700;letter-spacing:-2px;line-height:1}
.row .t{font-size:28px;line-height:1.55;color:var(--b);letter-spacing:-.5px}
.row .t b{color:var(--bk);font-size:32px;display:block;margin-bottom:4px}
.dark .row .t{color:#C9C4BB}.dark .row .t b{color:var(--iv)}
.paper{position:absolute;background:#FBF8F1 linear-gradient(rgba(17,17,17,.06) 1px,transparent 1px) 0 0/100% 44px;border:1.5px solid #111}
.hand{font-family:P,sans-serif;font-weight:400;color:#2B2A27}
'''
TOTAL=7
HD=lambda r="ENOCH NOTE — PRACTICE LOG": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT=lambda n: f'<div class="ft"><span>연습일지</span><span>0{n} / 0{TOTAL}</span></div>'
S=[]
# 01 표지
S.append(f"""<section class="s" id="c1">{HD()}
<img src="../../images/공간/피아노_01.jpg" style="position:absolute;left:96px;top:150px;width:888px;height:620px;object-fit:cover;object-position:50% 50%;display:block;filter:saturate(.6) contrast(1.02)">
<div class="k a" style="left:96px;top:810px">For Exam Students</div>
<div class="h a" style="left:92px;top:855px;font-size:84px;letter-spacing:-4.2px;line-height:1.18">같은 시간 연습했는데,<br><em>왜 나만 제자리일까?</em></div>
<div class="p a" style="left:96px;top:1100px;font-size:28px">입시생이 연습일지를 꼭 써야 하는 이유</div>
{FT(1)}<div class="a" style="left:96px;bottom:26px;font-size:13px;color:#A8A39A">사진: ENOCH 피아노</div></section>""")
# 02 이유 3가지
S.append(f"""<section class="s" id="c2">{HD()}
<div class="k a" style="left:96px;top:200px">Why · 3 Reasons</div>
<div class="h a" style="left:92px;top:250px">연습은 사라지고,<br><em>기록은 남습니다</em></div>
<div class="a" style="left:96px;right:96px;top:540px;border-top:1.5px solid #111">
<div class="row"><span class="n">01</span><span class="t"><b>어제를 기억하게 돼요</b>무엇이 안 됐는지, 하루만 지나도 흐려지거든요. 적어 두면 오늘 어디서 시작할지 보입니다.</span></div>
<div class="row"><span class="n">02</span><span class="t"><b>나만의 방법이 쌓여요</b>시도한 것과 그 결과가 남으면, 그게 곧 나에게 맞는 연습법이 됩니다.</span></div>
<div class="row"><span class="n">03</span><span class="t"><b>고민이 생겨요</b>쓰려면 생각해야 하고, 생각해야 다음 연습이 보여요.</span></div>
</div>
{FT(2)}</section>""")
# 03 일지 양식
S.append(f"""<section class="s" id="c3">{HD()}
<div class="k a" style="left:96px;top:200px">Template</div>
<div class="h a" style="left:92px;top:250px">이 네 줄이면,<br><em>충분해요</em></div>
<div class="paper" style="left:96px;right:96px;top:520px;height:500px;padding:40px 48px">
  <div style="display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2px;color:#8A8A8A"><span>DATE ____ / ____</span><span>TIME ____ MIN</span></div>
  <div style="margin-top:34px;font-size:22px;font-weight:700;letter-spacing:4px;color:#8A8A8A">연습 전</div>
  <div style="margin-top:12px;background:var(--bu);padding:18px 22px;font-size:30px;font-weight:700;letter-spacing:-.6px">① 오늘의 목표 <span style="font-weight:400;font-size:24px;color:#55524D">— 지금 가장 안 되는 한 곳은?</span></div>
  <div style="margin-top:34px;font-size:22px;font-weight:700;letter-spacing:4px;color:#8A8A8A">연습 후</div>
  <div style="margin-top:14px;font-size:30px;font-weight:700;letter-spacing:-.6px;line-height:2.1">② 방금 연습한 것<br>③ 잘된 것 · 안 된 것<br>④ 다음에 할 것</div>
</div>
{FT(3)}</section>""")
# 04 기록 루틴 5단계 (검정)
steps=[("01","찍기","연습 전, 지금 상태를 녹음 · 녹화 (Before)"),("02","듣고 적기","들으면서 안 되는 곳을 일지에"),("03","한 가지만","그중 하나만 골라 집중 연습"),("04","다시 찍기","같은 부분을 다시 녹음 · 녹화 (After)"),("05","비교하기","전과 후를 나란히 듣고, 다음 목표 적기")]
rows=''.join(f'<div class="row" style="padding:20px 0"><span class="n" style="font-size:36px;color:#F1E8CB">{n}</span><span class="t"><b style="font-size:30px">{a}</b>{b}</span></div>' for n,a,b in steps)
S.append(f"""<section class="s dark" id="c4">{HD("ROUTINE")}
<div class="k a" style="left:96px;top:200px;color:#9A958C">Record → Compare</div>
<div class="h a" style="left:92px;top:250px">기록이 연습을 바꾸는,<br><em>5단계</em></div>
<div class="a" style="left:96px;right:96px;top:500px;border-top:1.5px solid rgba(241,237,228,.6)">{rows}</div>
<div class="a" style="left:96px;right:96px;top:1190px;font-size:22px;color:#9A958C">05에서 적은 목표가, 다음 날의 01이 됩니다. ↺</div>
{FT(4)}</section>""")
# 05 목표 거꾸로
S.append(f"""<section class="s" id="c5">{HD()}
<div class="k a" style="left:96px;top:200px">Goal Setting</div>
<div class="h a" style="left:92px;top:250px">목표는,<br><em>거꾸로 세웁니다</em></div>
<div class="a" style="left:96px;right:96px;top:540px;display:flex;flex-direction:column;gap:18px">
  <div style="border-top:1.5px solid #111;padding:24px 0;display:flex;justify-content:space-between;align-items:center"><div><div class="k">Long Term</div><div style="font-size:34px;font-weight:700;margin-top:6px">실기 시험일</div></div><div style="font-size:26px;color:#55524D">곡 완성 · 무대에서 연주</div></div>
  <div style="text-align:center;font-size:30px;color:#8A8A8A;line-height:1">↓</div>
  <div style="border-top:1.5px solid #111;padding:24px 0;display:flex;justify-content:space-between;align-items:center"><div><div class="k">This Month</div><div style="font-size:34px;font-weight:700;margin-top:6px">이번 달</div></div><div style="font-size:26px;color:#55524D">암보 · 녹음해 보기 · 모의고사</div></div>
  <div style="text-align:center;font-size:30px;color:#8A8A8A;line-height:1">↓</div>
  <div style="border-top:1.5px solid #111;border-bottom:1.5px solid #111;background:var(--bu);padding:24px 30px;display:flex;justify-content:space-between;align-items:center"><div><div class="k" style="color:#7A7262">Today</div><div style="font-size:34px;font-weight:700;margin-top:6px">오늘</div></div><div style="font-size:26px;color:#55524D">30분 단위로, 무엇을 어떻게</div></div>
</div>
{FT(5)}</section>""")
# 06 실제 예시
S.append(f"""<section class="s" id="c6">{HD()}
<div class="k a" style="left:96px;top:200px">Example</div>
<div class="h a" style="left:92px;top:250px">예를 들면,<br><em>이렇게 적어요</em></div>
<div class="paper" style="left:96px;right:96px;top:520px;height:470px;padding:36px 46px">
  <div style="display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2px;color:#8A8A8A"><span>10 / 16 · 입시곡 1</span><span>90 MIN</span></div>
  <div class="hand" style="margin-top:22px;background:var(--bu);padding:14px 20px;font-size:28px"><b>목표</b> &nbsp;B파트 8마디, 템포가 흔들린다</div>
  <div class="hand" style="margin-top:22px;font-size:27px;line-height:1.95">
    <span style="font-family:var(--mono);font-size:20px;color:#8A8A8A">30분</span> &nbsp;전체 한 번 녹음 → 들으며 체크<br>
    <span style="font-family:var(--mono);font-size:20px;color:#8A8A8A">30분</span> &nbsp;B파트만, 메트로놈 70부터 천천히<br>
    <span style="font-family:var(--mono);font-size:20px;color:#8A8A8A">30분</span> &nbsp;80까지 올리고 다시 녹음<br>
    <b>잘된 것</b> &nbsp;박이 안정됨 &nbsp;·&nbsp; <b>안 된 것</b> &nbsp;마지막 두 마디<br>
    <b>다음에</b> &nbsp;마지막 두 마디부터, 80으로 시작
  </div>
</div>
{FT(6)}</section>""")
# 07 마무리
S.append(f"""<section class="s dark" id="c7">{HD("THE ENOCH WAY")}
<div class="a" style="left:92px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h a" style="left:92px;top:450px">어제의 연습이,<br><span style="color:var(--bu)">오늘의 기준이 됩니다.</span></div>
<div class="p a" style="left:96px;right:96px;top:720px">진도보다 이해를 먼저 봅니다.<br>시험장에서도 연습한 만큼 연주할 수 있도록,<br>주기적으로 모의고사를 진행합니다.</div>
<div class="a" style="left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>
{FT(7)}</section>""")
open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>연습일지</title><style>{FONT}{CSS}</style></head><body>'+''.join(S)+'</body></html>')
