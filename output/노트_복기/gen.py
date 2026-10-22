# ENOCH NOTE — 끝난 뒤에 하는 연습 (deck.html 생성)
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
CSS+='''.bl{background:#EEDFD8}
.q{border-top:1.5px solid #111}
.q div{display:grid;grid-template-columns:90px 1fr;padding:30px 0;border-bottom:1px solid rgba(17,17,17,.15);align-items:baseline}
.q .n{font-family:var(--en);font-weight:300;font-size:56px;letter-spacing:-2px;line-height:.8}
.q .t{font-size:32px;font-weight:700;letter-spacing:-.8px}
.q .t span{display:block;height:44px;border-bottom:1.5px dashed rgba(17,17,17,.35);margin-top:18px}
'''
TOTAL=7
HD=lambda r="ENOCH NOTE — AFTER THE STAGE": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT=lambda n: f'<div class="ft"><span>끝난 뒤에 하는 연습</span><span>0{n} / 0{TOTAL}</span></div>'
INFO='<div class="a" style="left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>'
S=[]
# 01 표지
S.append(f"""<section class="s" id="c1">{HD()}
<img src="../../images/공간/무대_02.jpg" style="position:absolute;left:96px;top:150px;width:888px;height:640px;object-fit:cover;object-position:50% 62%;display:block;filter:grayscale(.45) sepia(.12) contrast(1.04)">
<div class="k a" style="left:96px;top:830px">After the Stage</div>
<div class="h a" style="left:92px;top:875px;font-size:84px;letter-spacing:-4.2px;line-height:1.18">끝난 뒤에 하는,<br><em>연습</em></div>
<div class="p a" style="left:96px;top:1110px;font-size:28px">그날의 무대를 돌아보는 일에 대하여</div>
{FT(1)}</section>""")
# 02 결과와 상관없이
S.append(f"""<section class="s dark" id="c2">{HD("WHATEVER THE RESULT")}
<div class="k a" style="left:96px;top:200px">Whatever the Result</div>
<div class="h a" style="left:92px;top:250px">그날의 무대는,<br><em>한 번뿐이었습니다</em></div>
<div class="p a" style="left:96px;right:96px;top:560px">결과는 이미 정해졌어요.<br>하지만 그날을 <b>어떻게 기억할지</b>는, 아직 내가 정할 수 있습니다.</div>
<div class="p a" style="left:96px;right:96px;top:800px;font-size:28px;color:#9A958C">어떤 결과였든, 돌아볼 가치가 있는 무대였거든요.</div>
{FT(2)}</section>""")
# 03 혼내는 시간이 아닙니다
S.append(f"""<section class="s" id="c3">{HD("NOT TO BLAME")}
<div class="k a" style="left:96px;top:200px">Not to Blame</div>
<div class="h a" style="left:92px;top:250px">복기는,<br><em>나를 혼내는 시간이 아닙니다</em></div>
<div class="a" style="left:96px;right:96px;top:560px;display:grid;grid-template-columns:1fr 1fr;border-top:1.5px solid #111">
<div style="padding:34px 30px 34px 0;border-right:1px solid rgba(17,17,17,.15)"><div class="k">✕ 혼내기</div><div style="font-size:36px;font-weight:300;color:#8A8A8A;margin-top:18px;line-height:1.4;text-decoration:line-through">왜 그것밖에<br>못 했을까</div></div>
<div style="padding:34px 0 34px 30px"><div class="k" style="color:#111">○ 이해하기</div><div style="font-size:36px;font-weight:700;margin-top:18px;line-height:1.4">그 순간,<br>왜 그랬을까</div></div>
</div>
<div class="p a" style="left:96px;right:96px;top:950px">잘못한 것만 세면, 다음 무대가 더 무거워져요.<br>이해하고 나면, 같은 순간이 와도 덜 흔들립니다.</div>
{FT(3)}</section>""")
# 04 세 가지 질문
S.append(f"""<section class="s" id="c4">{HD("THREE QUESTIONS")}
<div class="k a" style="left:96px;top:200px">Three Questions</div>
<div class="h a" style="left:92px;top:250px">나에게 묻는,<br><em>세 가지</em></div>
<div class="a q" style="left:96px;right:96px;top:520px">
<div><span class="n">01</span><span class="t">그날 가장 떨렸던 순간은?<span></span></span></div>
<div><span class="n">02</span><span class="t">그래도 해낸 것 하나는?<span></span></span></div>
<div><span class="n">03</span><span class="t">다음 무대의 나에게 해 주고 싶은 말은?<span></span></span></div>
</div>
{FT(4)}</section>""")
# 05 해낸 것부터
S.append(f"""<section class="s" id="c5">{HD("START WITH WHAT WENT WELL")}
<div class="bl a" style="left:0;right:0;top:150px;height:470px"></div>
<div class="a" style="left:96px;top:205px;font-family:var(--en);font-weight:300;font-size:120px;letter-spacing:-5px;line-height:1">I did it.</div>
<div class="a" style="left:96px;right:96px;top:380px;font-size:30px;line-height:1.9;color:#55524D">끝까지 연주했다 · 대기실을 버텼다<br>시험장 문을 열고 들어갔다</div>
<div class="k a" style="left:96px;top:680px">Start with What Went Well</div>
<div class="h a" style="left:92px;top:725px">해낸 것부터,<br><em>적어 보세요</em></div>
<div class="p a" style="left:96px;right:96px;top:965px">사람은 아쉬운 장면을 더 오래 기억해요.<br>그래서 일부러, 해낸 것부터 꺼내 봅니다.</div>
{FT(5)}</section>""")
# 06 감정에도 시간이
S.append(f"""<section class="s" id="c6">{HD("TAKE YOUR TIME")}
<div class="k a" style="left:96px;top:200px">Take Your Time</div>
<div class="h a" style="left:92px;top:250px">바로 돌아보지 않아도,<br><em>괜찮습니다</em></div>
<div class="a" style="left:96px;right:96px;top:560px;display:flex;align-items:center;gap:0;border-top:1.5px solid #111;border-bottom:1.5px solid #111;padding:46px 0">
<div style="flex:1;text-align:center"><div class="k">Day 0</div><div style="font-size:34px;font-weight:300;margin-top:14px">무대</div></div>
<div style="flex:1;text-align:center"><div class="k">Day 1 – 2</div><div style="font-size:34px;font-weight:700;margin-top:14px">쉬기</div></div>
<div style="flex:1;text-align:center"><div class="k">After</div><div style="font-size:34px;font-weight:300;margin-top:14px">적어 보기</div></div>
</div>
<div class="p a" style="left:96px;right:96px;top:880px">마음이 조금 가라앉았을 때 적어도 늦지 않아요.<br>쉬는 것도, 다음 무대를 위한 시간이거든요.</div>
{FT(6)}</section>""")
# 07 마무리
S.append(f"""<section class="s dark" id="c7">{HD("THE ENOCH WAY")}
<div class="a" style="left:92px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h a" style="left:92px;top:450px">그날의 무대도,<br><span style="font-weight:300;color:#EEDFD8">나의 소리였습니다.</span></div>
<div class="p a" style="left:96px;right:96px;top:720px">진도보다 이해를 먼저 봅니다.<br>나만의 진짜 소리를 찾는 곳.</div>
{INFO}
{FT(7)}</section>""")
open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>끝난 뒤에 하는 연습</title><style>{FONT}{CSS}</style></head><body>'+''.join(S)+'</body></html>')
