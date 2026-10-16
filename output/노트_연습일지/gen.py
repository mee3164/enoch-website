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
.strike{position:absolute;left:40px;right:440px;top:56px;height:4px;background:#B23A2E;opacity:.85}
'''
TOTAL=7
HD=lambda r="ENOCH NOTE — PRACTICE LOG": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT=lambda n: f'<div class="ft"><span>연습일지</span><span>0{n} / 0{TOTAL}</span></div>'
S=[]
# 01 표지
S.append(f"""<section class="s" id="c1">{HD()}
<img src="../../images/학생/연습일지_01.png" style="position:absolute;left:96px;top:150px;width:888px;height:620px;object-fit:cover;object-position:50% 42%;display:block;filter:saturate(.7) contrast(1.03)">
<div class="k a" style="left:96px;top:810px">Practice Log</div>
<div class="h a" style="left:92px;top:855px;font-size:84px;letter-spacing:-4.2px;line-height:1.18">어제 뭘 연습했는지,<br><em>기억나세요?</em></div>
<div class="p a" style="left:96px;top:1100px;font-size:28px">입시생이 연습일지를 꼭 써야 하는 이유</div>
{FT(1)}<div class="a" style="left:96px;bottom:26px;font-size:13px;color:#A8A39A">사진: 연습일지</div></section>""")
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
# 04 그냥 쓴 일지 vs 잘 쓴 일지 (검정) — motion_04.html에서 같은 마크업에 애니메이션
GOOD=["<span style='font-family:var(--mono);font-size:20px;color:#8A8A8A;letter-spacing:2px'>10 / 16 · 90 MIN</span>","B파트 8마디, 템포 <b>70 → 80</b>","마지막 두 마디가 흔들림","내일은 <b>그 두 마디부터, 80으로</b>"]
C4 = f"""<section class="s dark" id="c4">{HD("BEFORE · AFTER")}
<div class="k a" style="left:96px;top:200px;color:#9A958C">Same Day, Two Logs</div>
<div class="h a" style="left:92px;top:250px">"연습함"은,<br><em>일지가 아닙니다</em></div>
<div class="a k rv" style="left:96px;top:520px;color:#9A958C;--t:.5s">그냥 쓴 일지</div>
<div class="paper rv" style="left:96px;right:96px;top:560px;height:150px;padding:34px 44px;background:#E9E5DC;--t:.6s"><div class="hand wr" style="font-size:32px;color:#55524D;--t:.9s;--w:1.1s">오늘 3시간 연습함. 잘 안 됨.</div><div class="strike" style="--t:2.2s"></div></div>
<div class="a k rv" style="left:96px;top:760px;color:#F1E8CB;--t:2.6s">잘 쓴 일지</div>
<div class="paper rv" style="left:96px;right:96px;top:800px;height:300px;padding:30px 44px;--t:2.7s">""" + ''.join(f'<div class="hand wr" style="font-size:31px;line-height:1.95;--t:{3.0+i*.75:.2f}s;--w:.7s">{g}</div>' for i,g in enumerate(GOOD)) + f"""</div>
{FT(4)}</section>"""
S.append(C4)
# 05 기록이 쌓이면 보이는 것 — motion_05.html에서 같은 마크업에 애니메이션
days=[("월",70),("화",72),("수",75),("목",75),("금",80),("토",82),("일",85)]
W,H=820,360; x0=40; step=(W-80)/6
def y(v): return 70+(85-v)/(85-65)*(H-120)
pts=' '.join(f'{x0+i*step:.0f},{y(v):.0f}' for i,(d,v) in enumerate(days))
dots=''.join(f'<g class="pt" style="--t:{1.2+i*.25:.2f}s"><circle cx="{x0+i*step:.0f}" cy="{y(v):.0f}" r="{9 if i<6 else 13}" fill="{"#111" if i<6 else "#F1E8CB"}" stroke="#111" stroke-width="3"/><text x="{x0+i*step:.0f}" y="{y(v)-22:.0f}" text-anchor="middle" font-size="24" font-weight="700" fill="#111">{v}</text></g><text x="{x0+i*step:.0f}" y="{H+10}" text-anchor="middle" font-size="24" fill="#55524D">{d}</text>' for i,(d,v) in enumerate(days))
GRAPH=f'<svg width="{W}" height="{H+30}" viewBox="0 0 {W} {H+30}" font-family="P,sans-serif"><path d="M0 {H-30} H {W}" stroke="#111" stroke-width="1.5"/><polyline class="ln2" points="{pts}" fill="none" stroke="#111" stroke-width="4" stroke-linejoin="round" stroke-linecap="round" pathLength="1"/>{dots}</svg>'
C5 = f"""<section class="s" id="c5">{HD()}
<div class="k a" style="left:96px;top:200px">One Week · Same 8 Bars</div>
<div class="h a" style="left:92px;top:250px">기록이 쌓이면,<br><em>나아진 게 보입니다</em></div>
<div class="a rv" style="left:96px;right:96px;top:540px;font-size:24px;color:#55524D;--t:.3s"><span class="k" style="font-size:18px">BPM</span> &nbsp;B파트 8마디, 일주일 동안 적은 템포</div>
<div class="a" style="left:130px;top:610px">{GRAPH}</div>
<div class="p a rv" style="left:96px;right:96px;top:1060px;font-size:28px;--t:3.2s">어제보다 나아진 게 눈에 보이면, <b>오늘도 하게 되거든요.</b></div>
{FT(5)}</section>"""
S.append(C5)
# 05 목표 거꾸로
S.append(f"""<section class="s" id="c6">{HD()}
<div class="k a" style="left:96px;top:200px">Goal Setting</div>
<div class="h a" style="left:92px;top:250px">목표는,<br><em>거꾸로 세웁니다</em></div>
<div class="a" style="left:96px;right:96px;top:540px;display:flex;flex-direction:column;gap:18px">
  <div style="border-top:1.5px solid #111;padding:24px 0;display:flex;justify-content:space-between;align-items:center"><div><div class="k">Long Term</div><div style="font-size:34px;font-weight:700;margin-top:6px">실기 시험일</div></div><div style="font-size:26px;color:#55524D">시험장에서 연주</div></div>
  <div style="text-align:center;font-size:30px;color:#8A8A8A;line-height:1">↓</div>
  <div style="border-top:1.5px solid #111;padding:24px 0;display:flex;justify-content:space-between;align-items:center"><div><div class="k">This Month</div><div style="font-size:34px;font-weight:700;margin-top:6px">이번 달</div></div><div style="display:grid;grid-template-columns:auto auto;gap:8px 10px"><span style="font-size:24px;padding:6px 14px;border:1.5px solid #111;text-align:center">입시곡</span><span style="font-size:24px;padding:6px 14px;border:1.5px solid #111;text-align:center">즉흥연주</span><span style="font-size:24px;padding:6px 14px;border:1.5px solid #111;text-align:center">청음</span><span style="font-size:24px;padding:6px 14px;border:1.5px solid #111;text-align:center">화성학</span></div></div>
  <div style="text-align:center;font-size:30px;color:#8A8A8A;line-height:1">↓</div>
  <div style="border-top:1.5px solid #111;border-bottom:1.5px solid #111;background:var(--bu);padding:24px 30px;display:flex;justify-content:space-between;align-items:center"><div><div class="k" style="color:#7A7262">Today</div><div style="font-size:34px;font-weight:700;margin-top:6px">오늘</div></div><div style="font-size:26px;color:#55524D">30분 단위로, 무엇을 어떻게</div></div>
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

# 모션 버전 (4장만, 1080x1350 영상용)
ANIM = """.rv{opacity:0;animation:rv .5s cubic-bezier(.2,.7,.2,1) var(--t) both}
@keyframes rv{from{opacity:0;transform:translateY(24px)}to{opacity:1;transform:none}}
.wr{clip-path:inset(0 100% 0 0);animation:wr var(--w) linear var(--t) both}
@keyframes wr{to{clip-path:inset(0 0 0 0)}}
.strike{transform-origin:left;transform:scaleX(0);animation:st .45s ease-out var(--t) both}
@keyframes st{to{transform:scaleX(1)}}
.paper.rv{animation-name:rv}
"""
open('motion_04.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>연습일지 4장 모션</title><style>{FONT}{CSS}{ANIM}body{{margin:0}}.s{{margin:0}}</style></head><body>'+C4+'</body></html>')

ANIM5 = ANIM + """.ln2{stroke-dasharray:1;stroke-dashoffset:1;animation:dl 1.9s ease-in-out .9s both}
@keyframes dl{to{stroke-dashoffset:0}}
.pt{opacity:0;animation:rv .35s cubic-bezier(.2,.9,.3,1.3) var(--t) both;transform-box:fill-box;transform-origin:center}
"""
open('motion_05.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>연습일지 5장 모션</title><style>{FONT}{CSS}{ANIM5}body{{margin:0}}.s{{margin:0}}</style></head><body>'+C5+'</body></html>')
