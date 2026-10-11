import sys; sys.path.insert(0,'.')
from mascot import mascot
FONT='''@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Medium.woff2);font-weight:500}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}
@font-face{font-family:H;src:url(../../templates/fonts/caveat-latin-700-normal.woff2)}
@font-face{font-family:S;src:url(../../templates/fonts/dm-serif-display-latin-400-normal.woff2)}'''
CSS='''*{box-sizing:border-box;margin:0;padding:0}
:root{--iv:#F1EDE4;--bk:#111;--g:#8A8A8A;--b:#55524D;--lime:#DDE37C;--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--iv);color:var(--bk);font-family:P,sans-serif;margin-bottom:40px}
.s.dark{background:var(--bk);color:var(--iv)}
.hd{position:absolute;left:96px;right:96px;top:72px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:21px;letter-spacing:3px;padding-bottom:20px;border-bottom:1.5px solid currentColor}
.ft{position:absolute;left:96px;right:96px;bottom:60px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2px;padding-top:20px;border-top:1.5px solid currentColor}
.ft span:first-child{font-family:P,sans-serif;letter-spacing:0;font-size:21px}
.panel{position:absolute;left:96px;right:96px;top:150px;height:960px;border:3px solid var(--bk);background:#FFFDF7;overflow:hidden}
.cap{position:absolute;left:96px;right:96px;top:1132px;font-size:36px;font-weight:700;letter-spacing:-1.5px}
.cap small{display:block;font-size:24px;font-weight:400;color:var(--g);letter-spacing:-.4px;margin-top:6px}
.bub{position:absolute;background:#FFFDF7;border:3px solid #111;border-radius:40px;padding:22px 30px;font-size:34px;font-weight:700;letter-spacing:-1px}
.k{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
mark{background:linear-gradient(transparent 58%,var(--lime) 58%,var(--lime) 92%,transparent 92%);color:inherit;padding:0 4px}
.p{font-size:31px;line-height:1.75;color:var(--b);letter-spacing:-.6px}.p b{color:var(--bk)}
.num{font-family:S,serif;color:var(--lime);font-size:80px;width:70px;line-height:1}
'''
H=lambda r='DEAR ENOCH': f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
F=lambda n: f'<div class="ft"><span>Dear ENOCH — 무대 떨림</span><span>0{n} / 07</span></div>'
def svg(inner,w=888,h=960): return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:0;top:0">{inner}</svg>'
notes='<g fill="#111"><ellipse cx="0" cy="0" rx="14" ry="10" transform="rotate(-20)"/></g><path d="M12 -4 V -50" stroke="#111" stroke-width="4"/>'
def note(x,y,s=1): return f'<g transform="translate({x},{y}) scale({s})">{notes}</g>'
mic='<g stroke="#111" stroke-width="6" fill="none" stroke-linecap="round"><path d="M0 0 V 300"/><path d="M-50 300 h 100"/><rect x="-20" y="-70" width="40" height="70" rx="20" fill="#FFFDF7"/></g>'
sections=[]
# 1 표지
sections.append(f'''<section class="s" id="t1">{H()}
<div class="k" style="position:absolute;left:96px;top:190px">Dear ENOCH · 고민 01</div>
<div style="position:absolute;left:92px;top:240px;font-size:84px;font-weight:700;letter-spacing:-4px;line-height:1.2">“연습 땐 잘 되는데,<br><mark>무대에만 서면</mark><br>손이 떨려요.”</div>
<svg width="888" height="560" style="position:absolute;left:96px;top:640px">{mascot(470,320,1.25,"nervous","front",sweat=True,shake=True)}</svg>
{F(1)}</section>''')
# 2 연습실
sections.append(f'''<section class="s" id="t2">{H()}
<div class="panel">{svg(mascot(420,620,1.4,"happy","up") + f'<g transform="translate(700,560)">{mic}</g>' + note(180,300,1.6)+note(260,200,1.2)+note(640,240,1.4))}
<div class="bub" style="left:60px;top:60px">연습실에선 완벽해!</div></div>
<div class="cap">연습실에선 몇 번을 불러도 괜찮다.<small>혼자일 땐, 손도 목소리도 편하다.</small></div>
{F(2)}</section>''')
# 3 무대
aud=''.join(f'<circle cx="{60+i*70}" cy="{880+ (i%2)*20}" r="26" fill="#111" opacity=".85"/>' for i in range(12))
light='<path d="M444 -10 L 200 760 L 690 760 Z" fill="#DDE37C" opacity=".35"/>'
sections.append(f'''<section class="s" id="t3">{H()}
<div class="panel">{svg(light + mascot(444,560,1.3,"nervous","down",sweat=True) + aud)}
<div class="bub" style="right:60px;top:60px">…어?</div></div>
<div class="cap">그런데 무대에 오르는 순간.<small>조명이 켜지고, 사람들이 보인다.</small></div>
{F(3)}</section>''')
# 4 손 떨림
sections.append(f'''<section class="s" id="t4">{H()}
<div class="panel">{svg(mascot(444,520,1.9,"nervous","front",sweat=True,shake=True))}
<div style="position:absolute;right:70px;bottom:60px;font-family:H,cursive;font-size:96px;transform:rotate(-6deg)">덜덜덜…</div></div>
<div class="cap">손끝이 떨리고, 숨이 짧아진다.<small>나만 이런 걸까?</small></div>
{F(4)}</section>''')
# 5 답 (노트)
sections.append(f'''<section class="s" id="t5">{H("ENOCH'S ANSWER")}
<div class="k" style="position:absolute;left:96px;top:200px">Answer</div>
<div style="position:absolute;left:92px;top:250px;font-size:80px;font-weight:700;letter-spacing:-4px;line-height:1.2">떨리는 건,<br><mark>잘하고 싶어서</mark>입니다</div>
<div class="p" style="position:absolute;left:96px;right:96px;top:560px">무대에서 떨리는 건 많은 사람이 겪는 일입니다.<br>긴장하면 숨이 짧아지고, 손끝에 힘이 들어가거든요.<br><br>그래서 목표는 떨림을 없애는 게 아니라,<br><b>떨려도 연주할 수 있을 만큼 익숙해지는 것.</b></div>
<svg width="320" height="360" style="position:absolute;right:80px;top:840px">{mascot(160,230,0.9,"calm","hug")}</svg>
{F(5)}</section>''')
row=lambda n,t,d,last=False: f'<div style="display:flex;gap:32px;padding:30px 0;border-top:1px solid rgba(241,237,228,.3){";border-bottom:1px solid rgba(241,237,228,.3)" if last else ""}"><span class="num">{n}</span><div><div style="font-size:36px;font-weight:700">{t}</div><div style="margin-top:10px;font-size:28px;color:#C9C4BB;line-height:1.5">{d}</div></div></div>'
sections.append(f'''<section class="s dark" id="t6">{H("TRY THIS WEEK")}
<div style="position:absolute;left:92px;top:200px;font-size:80px;font-weight:700;letter-spacing:-4px;line-height:1.2">작은 무대를,<br>자주</div>
<div style="position:absolute;left:96px;right:96px;top:480px">
{row(1,'한 사람 앞에서','가족이나 친구 한 명 앞에서 한 곡. 관객이 한 명이어도 무대입니다.')}
{row(2,'카메라 켜고','휴대폰으로 녹화하면서 처음부터 끝까지. 멈추지 않는 연습이 됩니다.')}
{row(3,'시작 전 한 숨','첫 음 전에 숨을 길게 내쉬어 보세요. 몸이 조금 내려앉아요.',True)}
</div>{F(6)}</section>''')
sections.append(f'''<section class="s dark" id="t7">{H("THE ENOCH WAY")}
<div style="position:absolute;left:92px;top:200px;font-size:80px;font-weight:700;letter-spacing:-4px;line-height:1.2">고민,<br><span style="color:var(--lime)">보내 주세요.</span></div>
<div class="p" style="position:absolute;left:96px;right:96px;top:470px;color:#C9C4BB">음악 하면서 생긴 고민을 스토리 질문으로 받습니다.<br>골라서, Dear ENOCH로 답할게요.<br><br>같은 곡도, 사람마다 다르게 가르칩니다.<br>ENOCH은 모든 과정이 <b style="color:#F1EDE4">1:1</b>.</div>
<svg width="320" height="340" style="position:absolute;right:90px;top:760px">{mascot(160,250,0.95,"happy","up",ink="#F1EDE4")}</svg>
<div style="position:absolute;left:96px;top:1040px;font-size:22px;line-height:1.6">에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층 · 010 3949 3666</span></div>
{F(7)}</section>''')
# 캐릭터 시트
faces=["smile","happy","nervous","sad","calm"]
sheet=''.join(mascot(110+i*170,420,0.55,f,"down" if f!="happy" else "up",sweat=(f=="nervous")) for i,f in enumerate(faces))
sections.append(f'''<section class="s" id="sheet">{H("MASCOT — NOTE")}
<div style="position:absolute;left:92px;top:200px;font-size:80px;font-weight:700;letter-spacing:-4px">노트, <span style="font-weight:400">ENOCH의 음표</span></div>
<div class="p" style="position:absolute;left:96px;top:330px">8분음표 모양의 마스코트. 사람이 아니라서, 누구의 고민이든 대신 겪어 줍니다.</div>
<svg width="888" height="560" style="position:absolute;left:96px;top:480px">{sheet}</svg>
<div style="position:absolute;left:96px;right:96px;top:1080px;display:flex;justify-content:space-between" class="k"><span>smile</span><span>happy</span><span>nervous</span><span>sad</span><span>calm</span></div>
</section>''')
open('toon.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{FONT}{CSS}</style></head><body>'+''.join(sections)+'</body></html>')
