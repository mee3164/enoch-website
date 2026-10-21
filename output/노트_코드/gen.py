# ENOCH NOTE — 코드 (deck.html 생성)
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
CSS+='''.X{font-family:var(--en);font-weight:700;line-height:.8;letter-spacing:-.06em;position:absolute}
.lab{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
.dark .lab{color:#8C8C8C}
.mi{background:#D9E1E8}.bu{background:#F1E8CB}
.nrow{display:grid;grid-template-columns:260px 1fr;align-items:end;border-bottom:1px solid rgba(17,17,17,.18);padding:6px 0 18px}
.nrow .L{font-family:var(--en);font-weight:700;font-size:200px;line-height:.8;letter-spacing:-8px}
.nrow .t{font-size:30px;font-weight:700;letter-spacing:-.6px}
.nrow .t span{display:block;font-size:24px;font-weight:400;color:var(--b);margin-top:6px}
.step{display:grid;grid-template-columns:150px 1fr;align-items:baseline;border-top:1.5px solid #111;padding:26px 0}
.step .n{font-family:var(--en);font-weight:300;font-size:90px;letter-spacing:-4px;line-height:.8}
.step .t{font-size:32px;font-weight:700;letter-spacing:-.8px}
.step .t span{display:block;font-size:25px;font-weight:400;color:var(--b);margin-top:8px}
'''
TOTAL=8
HD=lambda r="ENOCH NOTE — CHORD": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT=lambda n,st='': f'<div class="ft" style="{st}"><span>코드</span><span>0{n} / 0{TOTAL}</span></div>'
INFO='<div class="a" style="left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>'
# 건반 SVG (C4~C5)
def kb(on, flat=None, w=888, h=300):
    names=['C','D','E','F','G','A','B','C2']
    ww=w/8; s=''
    for i,n in enumerate(names):
        s+=f'<rect x="{i*ww:.1f}" y="0" width="{ww:.1f}" height="{h}" fill="#FBF8F1" stroke="#111" stroke-width="1.5"/>'
        if n in on: s+=f'<circle cx="{i*ww+ww/2:.1f}" cy="{h-48}" r="20" fill="#111"/>'
        lab={'C':'도','D':'레','E':'미','F':'파','G':'솔','A':'라','B':'시','C2':'도'}[n]
        s+=f'<text x="{i*ww+ww/2:.1f}" y="{h+40}" text-anchor="middle" font-family="P,sans-serif" font-size="22" fill="#55524D">{lab}</text>'
    bl={'Db':1,'Eb':2,'Gb':4,'Ab':5,'Bb':6}
    for n,i in bl.items():
        x=i*ww-ww*0.3
        s+=f'<rect x="{x:.1f}" y="0" width="{ww*0.6:.1f}" height="{h*0.6}" fill="#111"/>'
        if flat==n: s+=f'<circle cx="{x+ww*0.3:.1f}" cy="{h*0.6-34}" r="18" fill="#F1EDE4"/>'
    return f'<svg class="a" width="{w}" height="{h+60}" viewBox="0 0 {w} {h+60}" style="left:96px;top:{{TOP}}px;overflow:visible">{s}</svg>'
S=[]
# 01 표지 (검정, 거대한 C + m)
S.append(f"""<section class="s dark" id="c1">{HD()}
<div class="X" style="left:40px;top:150px;font-size:900px;color:#F1EDE4">C</div>
<div class="X" style="left:640px;top:520px;font-size:430px;color:#D9E1E8">m</div>
<div class="lab a" style="left:96px;top:930px">Chord 101 · Major / Minor</div>
<div class="h a" style="left:92px;top:975px;font-size:84px;letter-spacing:-4.2px;line-height:1.18">한 음만 바꿨는데,<br><em>슬퍼집니다</em></div>
{FT(1)}</section>""")
# 02 코드는 세 음
S.append(f"""<section class="s" id="c2">{HD("WHAT IS A CHORD")}
<div class="lab a" style="left:96px;top:200px">What is a Chord</div>
<div class="h a" style="left:92px;top:250px">코드는,<br><em>함께 울리는 세 음</em></div>
<div class="p a" style="left:96px;right:96px;top:470px">한 음씩 건너뛰며 세 개를 쌓으면, 가장 기본이 되는 코드가 됩니다.</div>
<div class="a" style="left:96px;right:96px;top:560px">
<div class="nrow"><span class="L">G</span><span class="t">솔<span>5음 — 소리를 단단하게 받쳐 줘요</span></span></div>
<div class="nrow"><span class="L">E</span><span class="t">미<span>3음 — 밝을지 어두울지를 정합니다</span></span></div>
<div class="nrow" style="border-bottom:1.5px solid #111"><span class="L">C</span><span class="t">도<span>근음 — 코드의 이름이 되는 음</span></span></div>
</div>
{FT(2)}</section>""")
# 03 메이저
S.append(f"""<section class="s" id="c3">{HD("MAJOR")}
<div class="X" style="right:80px;top:150px;font-size:360px">C</div>
<div class="lab a" style="left:96px;top:200px">Major</div>
<div class="h a" style="left:92px;top:250px">밝게 들리는,<br><em>메이저</em></div>
"""+kb(['C','E','G']).replace('{TOP}','600')+f"""
<div class="a" style="left:96px;right:96px;top:1060px;display:flex;justify-content:space-between;font-size:27px;border-top:1.5px solid #111;padding-top:22px"><span>도 → 미 <b>반음 4개</b></span><span style="color:var(--g)">미 → 솔 반음 3개</span></div>
{FT(3)}</section>""")
# 04 마이너
S.append(f"""<section class="s" id="c4">{HD("MINOR")}
<div class="mi a" style="left:0;right:0;top:540px;height:470px"></div>
<div class="X" style="right:80px;top:190px;font-size:240px">Cm</div>
<div class="lab a" style="left:96px;top:200px">Minor</div>
<div class="h a" style="left:92px;top:250px">미 하나를 내리면,<br><em>마이너</em></div>
"""+kb(['C','G'],flat='Eb').replace('{TOP}','600')+f"""
<div class="a" style="left:96px;right:96px;top:1060px;display:flex;justify-content:space-between;font-size:27px;border-top:1.5px solid #111;padding-top:22px"><span>도 → 미♭ <b>반음 3개</b></span><span style="color:var(--g)">미♭ → 솔 반음 4개</span></div>
{FT(4)}</section>""")
# 05 위아래 분할
S.append(f"""<section class="s" id="c5">
<div class="a" style="left:0;right:0;top:675px;bottom:0;background:#111"></div>
{HD("ONE NOTE")}
<div class="X" style="left:70px;top:150px;font-size:440px">C</div>
<div class="a" style="right:96px;top:250px;text-align:right"><div class="lab">Major</div><div style="font-size:52px;font-weight:700;letter-spacing:-2px;margin-top:14px;line-height:1.3">밝고,<br>열린 느낌</div></div>
<div class="X" style="left:70px;top:745px;font-size:440px;color:#F1EDE4">Cm</div>
<div class="a" style="right:96px;top:850px;text-align:right;color:#F1EDE4"><div class="lab">Minor</div><div style="font-size:52px;font-weight:300;letter-spacing:-2px;margin-top:14px;line-height:1.3">어둡고,<br>쓸쓸한 느낌</div></div>
<div class="a" style="left:96px;right:96px;top:605px;font-family:var(--mono);font-size:20px;letter-spacing:3px;display:flex;justify-content:space-between"><span>E</span><span>— 반음 하나 —</span><span>E♭</span></div>
{FT(5,'color:#F1EDE4')}</section>""")
# 06 네 개의 코드 (검정)
S.append(f"""<section class="s dark" id="c6">{HD("THE FOUR CHORDS")}
<div class="lab a" style="left:96px;top:190px">The Four Chords</div>
<div class="a" style="left:86px;top:250px">
<div class="X" style="position:relative;font-size:205px;color:#F1EDE4">C</div>
<div class="X" style="position:relative;font-size:205px;color:#8A8A8A">G</div>
<div class="X" style="position:relative;font-size:205px;color:#F1EDE4">Am</div>
<div class="X" style="position:relative;font-size:205px;color:#8A8A8A">F</div>
</div>
<div class="a" style="right:96px;top:262px;text-align:right;font-family:var(--mono);font-size:30px;letter-spacing:4px;line-height:164px;color:#8C8C8C">I<br>V<br>vi<br>IV</div>
<div class="p a" style="left:96px;right:96px;top:950px">이 네 코드로, 셀 수 없이 많은 노래가 만들어졌어요.<br>비틀스의 「Let It Be」도 이 진행으로 시작합니다.</div>
{FT(6)}</section>""")
# 07 집에서 해 보기
S.append(f"""<section class="s" id="c7">{HD("TRY AT HOME")}
<div class="bu a" style="left:0;right:0;top:150px;height:330px"></div>
<div class="X" style="left:80px;top:205px;font-size:230px">C ↔ Cm</div>
<div class="lab a" style="left:96px;top:530px">Try at Home</div>
<div class="h a" style="left:92px;top:575px">같은 손 모양,<br><em>다른 기분</em></div>
<div class="a" style="left:96px;right:96px;top:820px">
<div class="step"><span class="n">01</span><span class="t">도 · 미 · 솔을 함께 누르기<span>피아노 앱이어도 충분해요</span></span></div>
<div class="step" style="border-bottom:1.5px solid #111"><span class="n">02</span><span class="t">미만 바로 왼쪽 검은 건반으로<span>둘을 번갈아 치며 기분이 어떻게 바뀌는지 들어 보세요</span></span></div>
</div>
{FT(7)}</section>""")
# 08 마무리
S.append(f"""<section class="s dark" id="c8">{HD("THE ENOCH WAY")}
<div class="a" style="left:92px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h a" style="left:92px;top:450px">같은 코드도,<br><span style="font-weight:300;color:#D9E1E8">사람마다 다르게 울립니다.</span></div>
<div class="p a" style="left:96px;right:96px;top:720px">같은 곡도, 사람마다 다르게 가르칩니다.<br>진도보다 이해를 먼저 봅니다. 모든 과정 <b>1:1</b>.</div>
{INFO}
{FT(8)}</section>""")
open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>코드</title><style>{FONT}{CSS}</style></head><body>'+''.join(S)+'</body></html>')
