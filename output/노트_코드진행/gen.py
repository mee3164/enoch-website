# ENOCH NOTE — 코드 진행 (deck.html 생성)
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
.L{font-family:var(--en);font-weight:300;letter-spacing:-.04em}
.lab{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
.dark .lab{color:#8C8C8C}
.mi{background:#D9E1E8}.bu{background:#F1E8CB}.sg{background:#DCE2D3}
.dia{display:grid;grid-template-columns:repeat(7,1fr);border-top:1.5px solid #111;border-bottom:1.5px solid #111}
.dia div{text-align:center;padding:30px 0 26px;border-right:1px solid rgba(17,17,17,.18)}
.dia div:last-child{border-right:0}
.dia b{display:block;font-family:var(--en);font-size:54px;letter-spacing:-2px}
.dia i{display:block;font-style:normal;font-family:var(--mono);font-size:22px;color:var(--g);margin-top:12px}
.dia .on{background:#111;color:#F1EDE4}.dia .on i{color:#C9C4BB}
.g8{display:grid;grid-template-columns:repeat(4,1fr);border-top:1.5px solid #111}
.g8 div{padding:26px 0 22px 22px;border-bottom:1px solid rgba(17,17,17,.2);border-right:1px solid rgba(17,17,17,.2)}
.g8 div:nth-child(4n){border-right:0}
.g8 b{display:block;font-family:var(--en);font-size:96px;letter-spacing:-4px;line-height:.9}
.g8 i{font-style:normal;font-family:var(--mono);font-size:20px;color:#55524D}
.step{display:grid;grid-template-columns:150px 1fr;align-items:baseline;border-top:1.5px solid #111;padding:26px 0}
.step .n{font-family:var(--en);font-weight:300;font-size:90px;letter-spacing:-4px;line-height:.8}
.step .t{font-size:32px;font-weight:700;letter-spacing:-.8px}
.step .t span{display:block;font-size:25px;font-weight:400;color:var(--b);margin-top:8px}
'''
TOTAL=9
HD=lambda r="ENOCH NOTE — PROGRESSION": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT=lambda n: f'<div class="ft"><span>코드 진행</span><span>0{n} / 0{TOTAL}</span></div>'
INFO='<div class="a" style="left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>'
S=[]
# 01 표지
S.append(f"""<section class="s dark" id="c1">{HD()}
<div class="X" style="left:70px;top:170px;font-size:360px;color:#F1EDE4">I</div>
<div class="X" style="left:330px;top:170px;font-size:360px;color:#F1EDE4">V</div>
<div class="X" style="left:70px;top:500px;font-size:360px;color:#D9E1E8">vi</div>
<div class="X" style="left:470px;top:500px;font-size:360px;color:#D9E1E8">IV</div>
<div class="a" style="right:96px;top:190px;text-align:right;font-family:var(--mono);font-size:22px;letter-spacing:3px;color:#8C8C8C;line-height:1.9">C<br>G<br>Am<br>F</div>
<div class="lab a" style="left:96px;top:930px">Chord Progression</div>
<div class="h a" style="left:92px;top:975px;font-size:80px;letter-spacing:-4px;line-height:1.18">이 진행,<br><em>분명 들어 봤을 거예요</em></div>
{FT(1)}</section>""")
# 02 진행이란
S.append(f"""<section class="s" id="c2">{HD("WHAT IS A PROGRESSION")}
<div class="lab a" style="left:96px;top:200px">What is a Progression</div>
<div class="h a" style="left:92px;top:250px">코드 진행은,<br><em>코드가 놓이는 순서</em></div>
<div class="p a" style="left:96px;right:96px;top:470px">단어가 모여 문장이 되듯, 코드가 이어지면 진행이 됩니다.<br>같은 코드라도 <b>순서가 바뀌면</b> 이야기가 달라져요.</div>
<div class="a" style="left:96px;right:96px;top:700px;border-top:1.5px solid #111;border-bottom:1.5px solid #111;padding:60px 0 50px;display:flex;justify-content:space-between;align-items:baseline">
<span class="L" style="font-size:150px;line-height:.8">C</span><span class="L" style="font-size:70px;color:var(--g)">→</span><span class="L" style="font-size:150px;line-height:.8">G</span><span class="L" style="font-size:70px;color:var(--g)">→</span><span class="L" style="font-size:150px;line-height:.8">Am</span><span class="L" style="font-size:70px;color:var(--g)">→</span><span class="L" style="font-size:150px;line-height:.8">F</span>
</div>
{FT(2)}</section>""")
# 03 숫자로 부르기
S.append(f"""<section class="s" id="c3">{HD("NUMBERS")}
<div class="lab a" style="left:96px;top:200px">Numbers</div>
<div class="h a" style="left:92px;top:250px">코드를,<br><em>숫자로 부르는 이유</em></div>
<div class="p a" style="left:96px;right:96px;top:470px">C 키의 코드 일곱 개에 번호를 붙이면, 키가 바뀌어도 진행은 같은 숫자로 남습니다.</div>
<div class="a dia" style="left:96px;right:96px;top:620px">
<div class="on"><b>C</b><i>I</i></div><div><b>Dm</b><i>ii</i></div><div><b>Em</b><i>iii</i></div><div class="on"><b>F</b><i>IV</i></div><div class="on"><b>G</b><i>V</i></div><div class="on"><b>Am</b><i>vi</i></div><div><b>B°</b><i>vii°</i></div>
</div>
<div class="a" style="left:96px;right:96px;top:900px;display:grid;grid-template-columns:200px 1fr;row-gap:18px;font-size:30px;align-items:baseline">
<span class="lab">C Key</span><span><b>C – G – Am – F</b></span>
<span class="lab">G Key</span><span><b>G – D – Em – C</b></span>
<span class="lab">Numbers</span><span style="font-family:var(--mono);letter-spacing:2px">I – V – vi – IV</span>
</div>
{FT(3)}</section>""")
# 04 집 · 떠남 · 긴장
S.append(f"""<section class="s" id="c4">{HD("HOME · AWAY · TENSION")}
<div class="mi a" style="left:0;right:0;top:150px;height:520px"></div>
<div class="a" style="left:96px;right:96px;top:210px;display:grid;grid-template-columns:repeat(3,1fr)">
<div><div class="X" style="position:relative;font-size:210px">I</div><div class="lab" style="margin-top:34px;color:#55524D">Home</div><div style="font-size:30px;font-weight:700;margin-top:8px">집</div><div style="font-size:23px;color:#55524D;margin-top:6px">편안하게 머무는 곳</div></div>
<div><div class="X" style="position:relative;font-size:210px">IV</div><div class="lab" style="margin-top:34px;color:#55524D">Away</div><div style="font-size:30px;font-weight:700;margin-top:8px">떠남</div><div style="font-size:23px;color:#55524D;margin-top:6px">집을 나서는 느낌</div></div>
<div><div class="X" style="position:relative;font-size:210px">V</div><div class="lab" style="margin-top:34px;color:#55524D">Tension</div><div style="font-size:30px;font-weight:700;margin-top:8px">긴장</div><div style="font-size:23px;color:#55524D;margin-top:6px">돌아가고 싶어지는 힘</div></div>
</div>
<div class="lab a" style="left:96px;top:720px">Function</div>
<div class="h a" style="left:92px;top:770px">V에서 I로,<br><em>돌아오면 끝난 느낌</em></div>
<div class="p a" style="left:96px;right:96px;top:1010px">코드마다 맡은 역할이 있거든요. 진행은 집을 나섰다가,<br>긴장을 지나, 다시 집으로 돌아오는 짧은 여행입니다.</div>
{FT(4)}</section>""")
# 05 I–V–vi–IV (검정)
S.append(f"""<section class="s dark" id="c5">{HD("PROGRESSION 01")}
<div class="lab a" style="left:96px;top:190px">01 · The Four Chords</div>
<div class="a" style="left:96px;right:96px;top:260px;display:grid;grid-template-columns:1fr 1fr;row-gap:40px">
<div><div class="X" style="position:relative;font-size:250px;color:#F1EDE4">C</div><div class="lab" style="margin-top:20px;text-transform:none;font-size:26px">I</div></div>
<div><div class="X" style="position:relative;font-size:250px;color:#F1EDE4">G</div><div class="lab" style="margin-top:20px;text-transform:none;font-size:26px">V</div></div>
<div><div class="X" style="position:relative;font-size:250px;color:#F1EDE4">Am</div><div class="lab" style="margin-top:20px;text-transform:none;font-size:26px">vi</div></div>
<div><div class="X" style="position:relative;font-size:250px;color:#F1EDE4">F</div><div class="lab" style="margin-top:20px;text-transform:none;font-size:26px">IV</div></div>
</div>
<div class="p a" style="left:96px;right:96px;top:1000px">셀 수 없이 많은 노래가 이 네 코드로 만들어졌어요.<br>비틀스의 「Let It Be」도 이 진행으로 시작합니다.</div>
{FT(5)}</section>""")
# 06 캐논 진행
cn=[('C','I'),('G','V'),('Am','vi'),('Em','iii'),('F','IV'),('C','I'),('F','IV'),('G','V')]
g=''.join(f'<div><b>{c}</b><i>{n}</i></div>' for c,n in cn)
S.append(f"""<section class="s" id="c6">{HD("PROGRESSION 02")}
<div class="bu a" style="left:0;right:0;top:150px;height:350px"></div>
<div class="X" style="left:80px;top:215px;font-size:230px">Canon</div>
<div class="lab a" style="left:96px;top:540px">02 · Canon Progression</div>
<div class="a g8" style="left:96px;right:96px;top:600px">{g}</div>
<div class="p a" style="left:96px;right:96px;top:1000px">파헬벨의 「캐논」에서 이름을 따온 여덟 코드.<br>천천히 계단을 내려가듯, <b>발라드</b>에서 자주 들립니다.</div>
{FT(6)}</section>""")
# 07 ii–V–I (계단)
S.append(f"""<section class="s" id="c7">{HD("PROGRESSION 03")}
<div class="lab a" style="left:96px;top:200px">03 · Two-Five-One</div>
<div class="X" style="left:90px;top:300px;font-size:260px">ii</div>
<div class="X" style="left:390px;top:480px;font-size:260px">V</div>
<div class="X" style="left:720px;top:660px;font-size:260px">I</div>
<div class="a" style="left:100px;top:530px;font-family:var(--mono);font-size:24px;color:var(--g);letter-spacing:3px">Dm</div>
<div class="a" style="left:400px;top:710px;font-family:var(--mono);font-size:24px;color:var(--g);letter-spacing:3px">G</div>
<div class="a" style="left:730px;top:890px;font-family:var(--mono);font-size:24px;color:var(--g);letter-spacing:3px">C</div>
<div class="h a" style="left:92px;top:960px;font-size:56px;letter-spacing:-2.4px">재즈의 가장 기본이 되는 문장,<br><em>투 · 파이브 · 원</em></div>
{FT(7)}</section>""")
# 08 집에서 해 보기
S.append(f"""<section class="s" id="c8">{HD("TRY AT HOME")}
<div class="sg a" style="left:0;right:0;top:150px;height:300px"></div>
<div class="X" style="left:80px;top:205px;font-size:200px">C = I</div>
<div class="lab a" style="left:96px;top:500px">Try at Home</div>
<div class="h a" style="left:92px;top:545px">좋아하는 노래를,<br><em>숫자로 바꿔 보세요</em></div>
<div class="a" style="left:96px;right:96px;top:790px">
<div class="step"><span class="n">01</span><span class="t">코드표를 찾아 첫 코드 확인하기<span>대개 곡이 시작하고 끝나는 코드가 I이에요</span></span></div>
<div class="step" style="border-bottom:1.5px solid #111"><span class="n">02</span><span class="t">나머지를 번호로 바꿔 적기<span>익숙한 진행이 보이기 시작합니다</span></span></div>
</div>
{FT(8)}</section>""")
# 09 마무리
S.append(f"""<section class="s dark" id="c9">{HD("THE ENOCH WAY")}
<div class="a" style="left:92px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h a" style="left:92px;top:450px">같은 진행도,<br><span style="font-weight:300;color:#D9E1E8">이야기는 다르게.</span></div>
<div class="p a" style="left:96px;right:96px;top:720px">같은 코드 진행으로도 수많은 곡이 만들어집니다.<br>같은 곡도, 사람마다 다르게 가르칩니다. 모든 과정 <b>1:1</b>.</div>
{INFO}
{FT(9)}</section>""")
open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>코드 진행</title><style>{FONT}{CSS}</style></head><body>'+''.join(S)+'</body></html>')
