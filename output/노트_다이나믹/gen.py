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
<div class="h a" style="left:92px;top:885px;font-size:86px;letter-spacing:-4.2px;line-height:1.16">후렴이<br><em>안 터지는 이유</em></div>
<div class="p a" style="left:96px;top:1120px;font-size:27px">답은 후렴이 아니라, 곡 전체에 있습니다.</div>
{FT(1)}</section>""")

# 02 사전 (검정)
marks = [("pp","아주 여리게",44),("p","여리게",64),("mp","조금 여리게",84),("mf","조금 세게",104),("f","세게",124),("ff","아주 세게",144)]
bars = ''.join(f'<div style="display:flex;align-items:flex-end;flex-direction:column;justify-content:flex-end;width:130px"><div style="width:130px;height:{h*2}px;background:{"#D9E1E8" if i==3 else "#2A2825"}"></div><div style="margin-top:16px;font-family:Georgia,serif;font-style:italic;font-weight:700;font-size:44px;align-self:flex-start">{m}</div><div style="font-size:21px;color:#9A958C;align-self:flex-start;margin-top:4px">{t}</div></div>' for i,(m,t,h) in enumerate(marks))
S.append(f"""<section class="s dark" id="c2">{HD("DICTIONARY")}
<div class="a" style="left:92px;top:190px;font-family:var(--en);font-weight:700;font-size:150px;letter-spacing:-6px;line-height:1">DYNAMICS</div>
<div class="a" style="left:96px;top:370px;font-size:44px;font-weight:700;letter-spacing:-1.5px">다이나믹 <span style="font-weight:300;color:#9A958C;font-size:36px">셈여림</span></div>
<div class="p a" style="left:96px;right:96px;top:450px">소리의 세고 여림. 곡 안에서는 크기와 에너지가<br>오르내리는 흐름 전체를 말해요.</div>
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

# 04 크기 · 밀도 · 음역
lev=[("01","크기","Volume","같은 구간을 더 세게, 더 여리게."),("02","밀도","Density","음의 개수, 리듬의 촘촘함, 함께 연주하는 악기 수."),("03","음역","Register","낮고 좁게 머물다가, 높고 넓게 열기.")]
rows4=''.join(f'<div class="row" style="padding:30px 0"><span class="n" style="width:250px">{n} &nbsp;{k} <span style="font-family:var(--mono);font-weight:400;font-size:17px;letter-spacing:2px;color:#8A8A8A;display:block;margin-top:6px">{e.upper()}</span></span><span class="t" style="font-size:29px">{t}</span></div>' for n,k,e,t in lev)
S.append(f"""<section class="s" id="c4">{HD()}
<div class="k a" style="left:96px;top:200px">Three Levers</div>
<div class="h a" style="left:92px;top:250px">볼륨만으로는,<br><em>터지지 않아요</em></div>
<div class="p a" style="left:96px;right:96px;top:520px">곡의 에너지는 세 가지가 함께 움직일 때 커집니다.</div>
<div class="a" style="left:96px;right:96px;top:640px;border-top:1.5px solid #111">{rows4}</div>
{FT(4)}</section>""")

# 05 곡에 지도 그리기 (검정)
S.append(f"""<section class="s dark" id="c5">{HD("TRY AT HOME")}
<div class="k a" style="left:96px;top:200px;color:#9A958C">Practice</div>
<div class="h a" style="left:92px;top:250px">연습하는 곡에,<br><em>지도를 그려 보기</em></div>
<div class="a" style="left:96px;right:96px;top:540px;border-top:1.5px solid rgba(241,237,228,.6)">
<div class="row"><span class="n">01 &nbsp;나누기</span><span class="t">인트로 · 벌스 · 프리코러스 · 후렴 · 브리지로 구간을 나눠 적기.</span></div>
<div class="row"><span class="n">02 &nbsp;숫자 적기</span><span class="t">구간마다 에너지를 <b>1부터 10까지</b> 숫자로. 전부 8이면 지도가 없는 거예요.</span></div>
<div class="row"><span class="n">03 &nbsp;정점 하나</span><span class="t">가장 큰 곳을 하나 정하기. 거기까지 아껴 두는 게 핵심입니다.</span></div>
<div class="row"><span class="n">04 &nbsp;녹음</span><span class="t">처음부터 끝까지 녹음해서, 적은 숫자대로 오르내리는지 들어 보기.</span></div>
</div>
{FT(5)}</section>""")

# 06 악기별
parts=[("보컬","벌스는 말하듯 가깝게, 후렴은 소리를 열고 길게."),("기타","벌스는 뮤트나 아르페지오로 비우고, 후렴은 오픈 코드 스트로크로 채우기."),("베이스","벌스는 긴 음 · 적은 음으로, 후렴은 8분음표로 밀어 주기."),("드럼","벌스는 하이햇 · 크로스 스틱, 후렴은 라이드 · 크래시와 오픈 하이햇으로."),("피아노","벌스는 가운데 음역에서 적게, 후렴은 보이싱을 넓히고 왼손 옥타브로.")]
rows=''.join(f'<div class="row"><span class="n">{a}</span><span class="t">{b}</span></div>' for a,b in parts)
S.append(f"""<section class="s" id="c6">{HD()}
<div class="k a" style="left:96px;top:200px">Verse → Chorus</div>
<div class="h a" style="left:92px;top:250px">벌스에서 비워 두면,<br><em>후렴이 커집니다</em></div>
<div class="p a" style="left:96px;top:500px;font-size:24px;color:#8A8A8A">예를 들면, 이렇게.</div>
<div class="a" style="left:96px;right:96px;top:570px;border-top:1.5px solid #111">{rows}</div>
{FT(6)}</section>""")

# 07 마무리 (검정)
S.append(f"""<section class="s dark" id="c7">{HD("THE ENOCH WAY")}
<div class="a" style="left:92px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h a" style="left:92px;top:450px">언제 크게 칠지 알 때,<br><span style="color:var(--mi)">후렴이 터집니다.</span></div>
<div class="p a" style="left:96px;right:96px;top:740px">진도보다 이해를 먼저 봅니다.<br>ENOCH 레슨은 입시 · 취미 · 성인 · 전문, 모든 과정이 1:1.</div>
<div class="a" style="left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>
{FT(7)}</section>""")

open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>다이나믹</title><style>{FONT}{CSS}</style></head><body>' + ''.join(S) + '</body></html>')
