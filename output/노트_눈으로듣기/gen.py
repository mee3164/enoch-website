# ENOCH NOTE — 소리를 껐는데 (Tsay 2013) (deck.html 생성)
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
CSS+='''.X{font-family:var(--en);font-weight:700;letter-spacing:-.05em;line-height:.85}
.src{position:absolute;left:96px;right:96px;bottom:130px;font-size:18px;color:#9A958C;letter-spacing:-.2px}
.dark .src{color:#77736C}
.bar{display:grid;grid-template-columns:200px 1fr 90px;align-items:center;gap:18px;margin-bottom:26px}
.bar .l{font-size:28px;font-weight:600;letter-spacing:-.6px}
.bar .b{height:46px;background:#D9D5CD}
.bar .v{font-family:var(--en);font-size:38px;font-weight:300;text-align:right}
.mi{background:#D9E1E8}.bu{background:#F1E8CB}
.step{display:grid;grid-template-columns:110px 1fr;align-items:baseline;border-top:1.5px solid #111;padding:26px 0}
.step .n{font-family:var(--en);font-weight:300;font-size:70px;letter-spacing:-3px;line-height:.8}
.step .t{font-size:31px;font-weight:700;letter-spacing:-.8px}
.step .t span{display:block;font-size:24px;font-weight:400;color:var(--b);margin-top:8px}
'''
TOTAL=7
HD=lambda r="ENOCH NOTE — SIGHT & SOUND": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT=lambda n: f'<div class="ft"><span>소리를 껐는데</span><span>0{n} / 0{TOTAL}</span></div>'
INFO='<div class="a" style="left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>'
BIG=lambda txt,top=250: f'<div class="a" style="left:92px;right:96px;top:{top}px;font-size:72px;font-weight:700;letter-spacing:-3px;line-height:1.25">{txt}</div>'
SRC='<div class="src">Tsay (2013), PNAS · 국제 클래식 콩쿠르 실제 영상</div>'
S=[]
# 01 표지
S.append(f"""<section class="s dark" id="c1">{HD()}
<div class="a X" style="left:80px;top:200px;font-size:300px;color:#F1EDE4">MUTE</div>
<div class="a" style="left:96px;top:470px;width:888px;height:8px;background:#F1EDE4"></div>
<div class="a k" style="left:96px;top:520px">Sound off · Video on</div>
<div class="h a" style="left:92px;top:900px;font-size:80px;letter-spacing:-4px;line-height:1.18">소리를 껐는데,<br><em>우승자를 맞혔습니다</em></div>
{FT(1)}</section>""")
# 02 실험
S.append(f"""<section class="s" id="c2">{HD("THE STUDY")}
<div class="k a" style="left:96px;top:200px">The Study</div>
{BIG('콩쿠르 연주 영상,<br><span style="font-weight:300">누가 우승했을까요?</span>')}
<div class="a" style="left:96px;right:96px;top:600px;display:grid;grid-template-columns:1fr 1fr;border-top:1.5px solid #111">
<div style="padding:40px 30px 40px 0;border-right:1px solid rgba(17,17,17,.15)"><div class="k">소리만 듣고</div><div style="font-size:44px;font-weight:300;color:#9A958C;margin-top:18px;line-height:1.35">찍은 것과<br>비슷했어요</div></div>
<div style="padding:40px 0 40px 30px"><div class="k" style="color:#111">소리 끄고 영상만</div><div style="font-size:44px;font-weight:700;margin-top:18px;line-height:1.35">가장 잘<br>맞혔어요</div></div>
</div>
{SRC}
{FT(2)}</section>""")
# 03 눈으로도 듣는다
S.append(f"""<section class="s dark" id="c3">{HD("EYES ARE LISTENING")}
<div class="a" style="left:96px;right:96px;top:330px;text-align:center">
<div class="X" style="font-size:150px;color:#F1EDE4">EAR</div>
<div class="X" style="font-size:90px;color:#77736C;margin:30px 0">+</div>
<div class="X" style="font-size:150px;color:#F1EDE4">EYE</div>
</div>
<div class="a" style="left:0;right:0;top:960px;text-align:center;font-size:40px;font-weight:300;color:#DCD7CD">연주는, <b style="color:#F1EDE4;font-weight:700">귀와 눈으로 함께</b> 듣습니다.</div>
{FT(3)}</section>""")
# 04 무엇이 보일까
S.append(f"""<section class="s" id="c4">{HD("WHAT THEY SEE")}
<div class="k a" style="left:96px;top:200px">What They See</div>
{BIG('무대에서 보이는 것도,<br><span style="font-weight:300">연주입니다</span>')}
<div class="a" style="left:96px;right:96px;top:600px">
<div class="step"><span class="n">01</span><span class="t" style="font-size:40px">무대에 들어서는 걸음</span></div>
<div class="step"><span class="n">02</span><span class="t" style="font-size:40px">첫 음 전의 숨</span></div>
<div class="step" style="border-bottom:1.5px solid #111"><span class="n">03</span><span class="t" style="font-size:40px">곡에 빠져 있는 얼굴</span></div>
</div>
{FT(4)}</section>""")
# 05 그래도 소리
S.append(f"""<section class="s" id="c5">{HD("SOUND FIRST")}
<div class="bu a" style="left:0;right:0;top:560px;height:420px"></div>
<div class="k a" style="left:96px;top:200px">But</div>
{BIG('그래도,<br><span style="font-weight:300">소리가 먼저입니다</span>')}
<div class="a" style="left:96px;right:96px;top:640px;font-size:40px;font-weight:300;line-height:1.6">보이는 건, 소리를 <b style="font-weight:700">대신하지 않아요.</b><br>준비된 소리 위에서만, <b style="font-weight:700">빛납니다.</b></div>
<div class="src">이 연구에는 반론도 있어요. 소리로 판단한다는 연구도 많습니다.</div>
{FT(5)}</section>""")
# 06 해 보기
S.append(f"""<section class="s" id="c6">{HD("TRY TODAY")}
<div class="mi a" style="left:0;right:0;top:150px;height:300px"></div>
<div class="a" style="left:96px;top:215px;font-family:var(--en);font-weight:300;font-size:130px;letter-spacing:-5px;line-height:1">Try today.</div>
<div class="a" style="left:96px;right:96px;top:560px">
<div class="step"><span class="n">01</span><span class="t" style="font-size:40px">내 연주를 찍어 보기</span></div>
<div class="step"><span class="n">02</span><span class="t" style="font-size:40px">소리를 끄고 보기</span></div>
<div class="step" style="border-bottom:1.5px solid #111"><span class="n">03</span><span class="t" style="font-size:40px">어떻게 보이는지 적기</span></div>
</div>
{FT(6)}</section>""")
# 07 마무리
S.append(f"""<section class="s dark" id="c7">{HD("THE ENOCH WAY")}
<div class="a" style="left:92px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h a" style="left:92px;top:450px">기본은,<br><span style="font-weight:300;color:#F1E8CB">건너뛰지 않습니다.</span></div>
<div class="p a" style="left:96px;right:96px;top:720px">시험장에서도 연습한 만큼 연주할 수 있도록,<br>주기적으로 모의고사를 진행합니다.</div>
{INFO}
{FT(7)}</section>""")
open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>소리를 껐는데</title><style>{FONT}{CSS}</style></head><body>'+''.join(S)+'</body></html>')
