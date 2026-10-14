# ENOCH NOTE — 다이나믹 (deck.html 생성)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

FONT = '''@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Medium.woff2);font-weight:500}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}'''
CSS = '''*{box-sizing:border-box;margin:0;padding:0}
:root{--iv:#F1EDE4;--bk:#111;--g:#8A8A8A;--b:#55524D;--mi:#D9E1E8;--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace;--en:"Helvetica Neue",Helvetica,Arial,"Liberation Sans",P,sans-serif}
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
.row{display:flex;gap:30px;padding:22px 0;border-bottom:1px solid rgba(17,17,17,.15)}
.dark .row{border-bottom-color:rgba(241,237,228,.16)}
.row .n{width:190px;flex:none;font-size:28px;font-weight:700;letter-spacing:-.6px}
.row .t{font-size:27px;line-height:1.55;color:var(--b);letter-spacing:-.5px}
.dark .row .t{color:#C9C4BB}
.row .t b{color:var(--bk)}.dark .row .t b{color:var(--iv)}
'''
TOTAL = 7
HD = lambda r="ENOCH NOTE — DYNAMICS": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT = lambda n: f'<div class="ft"><span>다이나믹</span><span>0{n} / 0{TOTAL}</span></div>'

S = []
# 01 표지
S.append(f"""<section class="s" id="c1">{HD()}
<img src="../../images/공간/무대_01.png" style="position:absolute;left:96px;top:150px;width:888px;height:650px;object-fit:cover;object-position:50% 52%;display:block;filter:saturate(.55) contrast(1.02)">
<div class="k a" style="left:96px;top:840px">Dynamics</div>
<div class="h a" style="left:92px;top:885px;font-size:86px;letter-spacing:-4.2px;line-height:1.16">음은 다 맞는데,<br><em>왜 밋밋할까?</em></div>
<div class="p a" style="left:96px;top:1120px;font-size:27px">답은 소리의 크기, 다이나믹에 있습니다.</div>
{FT(1)}</section>""")

# 02 사전 (검정)
marks = [("pp","아주 여리게",44),("p","여리게",64),("mp","조금 여리게",84),("mf","조금 세게",104),("f","세게",124),("ff","아주 세게",144)]
bars = ''.join(f'<div style="display:flex;align-items:flex-end;flex-direction:column;justify-content:flex-end;width:130px"><div style="width:130px;height:{h*2}px;background:{"#D9E1E8" if i==3 else "#2A2825"}"></div><div style="margin-top:16px;font-family:Georgia,serif;font-style:italic;font-weight:700;font-size:44px;align-self:flex-start">{m}</div><div style="font-size:21px;color:#9A958C;align-self:flex-start;margin-top:4px">{t}</div></div>' for i,(m,t,h) in enumerate(marks))
S.append(f"""<section class="s dark" id="c2">{HD("DICTIONARY")}
<div class="a" style="left:92px;top:190px;font-family:var(--en);font-weight:700;font-size:150px;letter-spacing:-6px;line-height:1">DYNAMICS</div>
<div class="a" style="left:96px;top:370px;font-size:44px;font-weight:700;letter-spacing:-1.5px">다이나믹 <span style="font-weight:300;color:#9A958C;font-size:36px">셈여림</span></div>
<div class="p a" style="left:96px;right:96px;top:450px">소리의 세고 여림. 같은 음, 같은 박자라도<br>크기가 달라지면 전혀 다른 말처럼 들려요.</div>
<div class="a" style="left:96px;right:96px;top:700px;display:flex;justify-content:space-between;align-items:flex-end;height:420px">{bars}</div>
{FT(2)}</section>""")

# 03 곡 전체
secs = [("Intro",40),("Verse",55),("Pre",95),("Chorus",175),("Verse 2",70),("Bridge",110),("Last Chorus",205),("Outro",45)]
W=888; step=W/len(secs)
pts=' '.join(f'{step*i+step/2:.0f},{260-h}' for i,(n,h) in enumerate(secs))
lbl=''.join(f'<text x="{step*i+step/2:.0f}" y="300" text-anchor="middle">{n}</text>' for i,(n,h) in enumerate(secs))
S.append(f"""<section class="s" id="c3">{HD()}
<div class="k a" style="left:96px;top:200px">The Whole Song</div>
<div class="h a" style="left:92px;top:250px">후렴이 크게 들리는 건,<br><em>벌스가 작아서</em></div>
<div class="p a" style="left:96px;right:96px;top:520px">처음부터 끝까지 같은 크기면, 가장 중요한 순간이 묻혀 버립니다.<br>곡 전체를 하나의 선으로 그려 보세요. <b>어디서 낮추고, 어디서 터뜨릴지.</b></div>
<svg width="888" height="320" viewBox="0 0 888 320" class="a" style="left:96px;top:800px">
<rect x="{step*6:.0f}" y="0" width="{step:.0f}" height="270" fill="#D9E1E8"/>
<path d="M0 260 H 888" stroke="#111" stroke-width="1.5"/>
<polyline points="{pts}" fill="none" stroke="#111" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
<g font-family="P" font-size="20" fill="#55524D">{lbl}</g></svg>
{FT(3)}</section>""")

# 04 솔로 기승전결
ks=[("기","起","짧은 동기 하나로 시작. 여백을 남겨 둡니다.",50),("승","承","그 동기를 반복하고 조금씩 바꾸며 쌓아요.",100),("전","轉","가장 높거나, 가장 큰 순간.",190),("결","結","다시 내려와 숨을 고르며 닫기.",70)]
bars4=''.join(f'<div style="flex:1;height:{h}px;background:{"#D9E1E8" if a=="전" else "#DCD6CB"}"></div>' for a,b,c,h in ks)
cols=''.join(f'<div style="flex:1;border-top:1.5px solid #111;padding-top:22px"><div style="font-size:64px;font-weight:700;letter-spacing:-2px">{a}<span style="font-size:24px;font-weight:300;color:#8A8A8A;margin-left:10px">{b}</span></div><div style="margin-top:14px;font-size:25px;line-height:1.55;color:#55524D;letter-spacing:-.5px">{c}</div></div>' for a,b,c,h in ks)
S.append(f"""<section class="s" id="c4">{HD()}
<div class="k a" style="left:96px;top:200px">Solo</div>
<div class="h a" style="left:92px;top:250px">처음부터 다 보여 주면,<br><em>갈 곳이 없어요</em></div>
<div class="p a" style="left:96px;right:96px;top:520px">솔로도 한 편의 이야기. 기승전결이 있을 때, 듣는 사람이 따라옵니다.</div>
<div class="a" style="left:96px;right:96px;top:640px;height:200px;display:flex;gap:28px;align-items:flex-end">{bars4}</div>
<div class="a" style="left:96px;right:96px;top:860px;display:flex;gap:28px;align-items:flex-start">{cols}</div>
{FT(4)}</section>""")

# 05 공통 연습 (검정)
S.append(f"""<section class="s dark" id="c5">{HD("TRY AT HOME")}
<div class="k a" style="left:96px;top:200px;color:#9A958C">Practice</div>
<div class="h a" style="left:92px;top:250px">한 소절을,<br><em>세 가지 크기로</em></div>
<div class="a" style="left:96px;right:96px;top:540px;border-top:1.5px solid rgba(241,237,228,.6)">
<div class="row"><span class="n">01 &nbsp;세 번</span><span class="t">같은 소절을 <b>여리게 · 보통 · 세게</b>, 세 번 연주해 보세요.</span></div>
<div class="row"><span class="n">02 &nbsp;템포 그대로</span><span class="t">메트로놈을 켜 두기. 세지면 빨라지고, 여려지면 느려지기 쉽거든요.</span></div>
<div class="row"><span class="n">03 &nbsp;녹음</span><span class="t">녹음해서 들어 보기. 생각한 차이보다 실제 차이는 작게 들립니다.</span></div>
<div class="row"><span class="n">04 &nbsp;곡에 옮기기</span><span class="t">연습하는 곡에 크기를 연필로 적어 두고, 그 표시대로 한 번.</span></div>
</div>
{FT(5)}</section>""")

# 06 악기별
parts=[("보컬","한 음을 길게 내며 작게 → 크게 → 작게. 크기가 바뀌어도 음정과 음색이 흔들리지 않는지 들어 보기."),("기타","볼륨 노브는 그대로, 피킹 세기만으로 같은 리프를 세 단계로. 게인이 높으면 차이가 줄어드니 클린 톤에서."),("베이스","먼저 고르게. 한 줄에서 8분음표를 같은 세기로, 손가락마다 크기가 튀지 않는지. 그다음 세 단계로."),("드럼","스틱 높이로 세기를 나누기. 악센트는 높게, 고스트 노트는 낮게. 하이햇과 심벌이 킥 · 스네어를 덮지 않게."),("피아노","보이싱 안에서도 크기를 나누기. 탑 노트(멜로디)는 또렷하게, 내성은 한 단계 작게.")]
rows=''.join(f'<div class="row"><span class="n">{a}</span><span class="t">{b}</span></div>' for a,b in parts)
S.append(f"""<section class="s" id="c6">{HD()}
<div class="k a" style="left:96px;top:200px">By Instrument</div>
<div class="h a" style="left:92px;top:250px">악기마다,<br><em>크기를 바꾸는 손</em></div>
<div class="a" style="left:96px;right:96px;top:540px;border-top:1.5px solid #111">{rows}</div>
{FT(6)}</section>""")

# 07 마무리 (검정)
S.append(f"""<section class="s dark" id="c7">{HD("THE ENOCH WAY")}
<div class="a" style="left:92px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h a" style="left:92px;top:450px">크기를 다룰 때,<br><span style="color:var(--mi)">소리가 말을 합니다.</span></div>
<div class="p a" style="left:96px;right:96px;top:740px">기본은 건너뛰지 않습니다.<br>ENOCH 레슨은 입시 · 취미 · 성인 · 전문, 모든 과정이 1:1.</div>
<div class="a" style="left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>
{FT(7)}</section>""")

open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>다이나믹</title><style>{FONT}{CSS}</style></head><body>' + ''.join(S) + '</body></html>')
