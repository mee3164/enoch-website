import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '디어에녹_01_무대떨림'))
from mascot import mascot

FONT = '''@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Medium.woff2);font-weight:500}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}
@font-face{font-family:H;src:url(../../templates/fonts/caveat-latin-700-normal.woff2)}
@font-face{font-family:S;src:url(../../templates/fonts/dm-serif-display-latin-400-normal.woff2)}'''
CSS = '''*{box-sizing:border-box;margin:0;padding:0}
:root{--iv:#F1EDE4;--bk:#111;--g:#8A8A8A;--b:#55524D;--lime:#DDE37C;--paper:#FFFDF7;--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--iv);color:var(--bk);font-family:P,sans-serif;margin-bottom:40px}
.s.dark{background:var(--bk);color:var(--iv)}
.hd{position:absolute;left:96px;right:96px;top:72px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:21px;letter-spacing:3px;padding-bottom:20px;border-bottom:1.5px solid currentColor}
.ft{position:absolute;left:96px;right:96px;bottom:60px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2px;padding-top:20px;border-top:1.5px solid currentColor}
.ft span:first-child{font-family:P,sans-serif;letter-spacing:0;font-size:21px}
.panel{position:absolute;left:96px;right:96px;top:150px;height:880px;border:3px solid var(--bk);background:var(--paper);overflow:hidden}
.say{position:absolute;left:96px;right:96px;top:1062px;height:160px;display:flex;align-items:center;gap:18px}
.say svg{flex:none}
.say .t{position:relative;flex:1;background:var(--paper);border:3px solid var(--bk);border-radius:36px;padding:24px 34px;font-size:32px;font-weight:700;letter-spacing:-1.2px;line-height:1.4}
.say .t:before{content:"";position:absolute;left:-17px;top:50%;margin-top:-14px;width:24px;height:24px;background:var(--paper);border-left:3px solid var(--bk);border-bottom:3px solid var(--bk);transform:rotate(45deg)}
.say .t small{display:block;font-size:24px;font-weight:400;color:var(--b);letter-spacing:-.4px;margin-top:4px}
.name{position:absolute;font-family:var(--mono);font-size:18px;letter-spacing:2px;color:var(--g)}
.bub{position:absolute;background:var(--paper);border:3px solid #111;border-radius:40px;padding:20px 30px;font-size:32px;font-weight:700;letter-spacing:-1px}
.k{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
mark{background:linear-gradient(transparent 58%,var(--lime) 58%,var(--lime) 92%,transparent 92%);color:inherit;padding:0 4px}
.p{font-size:31px;line-height:1.75;color:var(--b);letter-spacing:-.6px}.p b{color:var(--bk)}
.num{font-family:S,serif;color:var(--lime);font-size:80px;width:70px;line-height:1}
'''
TOTAL = 7
H = lambda r='DEAR ENOCH 02': f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
F = lambda n: f'<div class="ft"><span>Dear ENOCH — 시험장 떨림</span><span>0{n} / 0{TOTAL}</span></div>'
def svg(inner, w=888, h=880): return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" style="position:absolute;left:0;top:0">{inner}</svg>'

# 에녹이가 말하는 칸 (진행자)
def say(text, small='', face='smile', arms='wave'):
    me = f'<svg width="150" height="160" viewBox="0 0 150 160">{mascot(68,98,0.36,face,arms)}</svg>'
    sm = f'<small>{small}</small>' if small else ''
    return f'<div class="say">{me}<div class="t">{text}{sm}</div></div>'

ST = 'stroke="#111" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"'
def note(x, y, s=1):
    return f'<g transform="translate({x},{y}) scale({s})"><ellipse cx="0" cy="0" rx="14" ry="10" transform="rotate(-20)" fill="#111"/><path d="M12 -4 V -50" stroke="#111" stroke-width="4"/></g>'

# 연습실: 마이크 스탠드, 보면대, 헤드폰, 음표
practice = (
    '<circle cx="444" cy="380" r="300" fill="#DDE37C" opacity=".28"/>'
    f'<path d="M0 760 H 888" {ST}/>'
    f'<g {ST}><path d="M300 760 V 380"/><path d="M250 760 h 100"/><rect x="282" y="310" width="36" height="70" rx="18" fill="#FFFDF7"/></g>'
    f'<g {ST}><path d="M580 760 V 500"/><path d="M540 760 h 80"/><path d="M500 500 h 160 l -20 -110 h -120 z" fill="#FFFDF7"/>'
    '<path d="M535 425 h 90 M 530 455 h 100" stroke-width="3"/></g>'
    f'<g {ST}><path d="M120 200 v 40"/><path d="M90 300 a 30 34 0 0 1 60 0"/><rect x="80" y="296" width="18" height="36" rx="8" fill="#FFFDF7"/><rect x="142" y="296" width="18" height="36" rx="8" fill="#FFFDF7"/></g>'
    f'<g {ST} transform="translate(780,600) rotate(-8)"><path d="M0 -300 V -60" stroke-width="7"/><rect x="-14" y="-330" width="28" height="40" rx="6" fill="#FFFDF7"/>'
    '<path d="M0 -100 C -46 -100, -50 -40, -26 -20 C -70 0, -66 100, 0 100 C 66 100, 70 0, 26 -20 C 50 -40, 46 -100, 0 -100 Z" fill="#FFFDF7"/><circle cx="0" cy="-30" r="16"/><path d="M-20 40 h 40"/></g>'
    + note(420, 220, 1.6) + note(700, 180, 1.3) + note(640, 330, 1.1) + note(200, 520, 1.2)
)
# 시험장: 심사석, 바닥 표시, 시계
def exam(dim=False):
    o = []
    if dim: o.append('<rect width="888" height="880" fill="#111" opacity=".06"/>')
    o.append(f'<path d="M0 520 H 888" {ST}/>')
    o.append(f'<g {ST}><path d="M110 360 H 778 V 470 H 110 Z" fill="#FFFDF7"/><path d="M140 470 V 520 M 748 470 V 520"/></g>')
    for i, x in enumerate((210, 444, 678)):
        o.append(f'<g {ST}><path d="M{x-70} 360 l 14 -48 h 112 l 14 48" fill="#FFFDF7"/></g>')
        o.append(f'<text x="{x}" y="348" font-family="P" font-size="22" font-weight="700" text-anchor="middle" fill="#111">심사</text>')
        o.append(f'<g {ST} stroke-width="3"><path d="M{x-40} 400 h 60 M {x-40} 424 h 44"/></g>')
    o.append(f'<g {ST}><circle cx="760" cy="140" r="52" fill="#FFFDF7"/><path d="M760 140 V 108 M 760 140 L 784 152"/></g>')
    o.append(f'<g {ST}><path d="M250 640 v 120 M 330 640 v 120 M 240 640 h 100"/><path d="M250 640 V 560"/></g>')
    o.append(f'<g {ST}><path d="M620 760 V 600"/><path d="M590 760 h 60"/><rect x="606" y="556" width="28" height="48" rx="14" fill="#FFFDF7"/></g>')
    o.append(f'<g {ST}><path d="M380 760 l 128 0 M 444 730 v 60" stroke-width="7"/></g>')
    o.append('<text x="444" y="840" font-family="P" font-size="26" font-weight="700" text-anchor="middle" fill="#111">07</text>')
    return ''.join(o)

thought = lambda x, y, w, t: (f'<g><rect x="{x}" y="{y}" width="{w}" height="84" rx="42" fill="#FFFDF7" stroke="#111" stroke-width="4"/>'
                              f'<text x="{x+w/2}" y="{y+54}" font-family="P" font-size="32" font-weight="700" text-anchor="middle" fill="#111">{t}</text></g>')

S = []
# 1 표지
S.append(f'''<section class="s" id="t1">{H()}
<div class="k" style="position:absolute;left:96px;top:190px">Dear ENOCH · 고민 02</div>
<div style="position:absolute;left:92px;top:240px;font-size:80px;font-weight:700;letter-spacing:-4px;line-height:1.22">“연습실에서는 괜찮은데,<br><mark>시험장에서</mark><br>너무 떨려요.”</div>
<svg width="460" height="520" style="position:absolute;left:96px;top:680px">{mascot(230,330,1.2,"smile","wave")}</svg>
<div class="bub" style="left:560px;top:760px">에녹이가<br>같이 볼게요.</div>
<div class="name" style="left:280px;top:1190px">에녹이 · ENOCH</div>
{F(1)}</section>''')
# 2 연습실
S.append(f'''<section class="s" id="t2">{H()}
<div class="panel">{svg(practice)}<div class="bub" style="left:50px;top:50px">연습실</div></div>
{say("연습실에선 노래도 연주도 술술 나와요.", "익숙한 방, 익숙한 악기. 몇 번을 다시 해도 괜찮은 곳이거든요.", "happy")}
{F(2)}</section>''')
# 3 시험장
S.append(f'''<section class="s" id="t3">{H()}
<div class="panel">{svg(exam())}<div class="bub" style="left:50px;top:50px">시험장</div></div>
{say("그런데 시험장 문을 여는 순간.", "처음 보는 방, 심사석, 낯선 마이크와 의자. 한 번뿐인 기회.", "nervous", "down")}
{F(3)}</section>''')
# 4 머릿속
S.append(f'''<section class="s" id="t4">{H()}
<div class="panel">{svg(exam(True) + thought(70,90,300,"한 번뿐인데") + thought(400,210,330,"다 보고 있어") + thought(150,580,360,"틀리면 어떡하지") + thought(560,640,250,"숨이…"))}</div>
{say("머릿속이 이런 말로 가득 차요.", "목소리도 손끝도, 연습실과 다르게 움직이고요.", "nervous", "front")}
{F(4)}</section>''')
# 5 답
S.append(f'''<section class="s" id="t5">{H("ENOCH'S ANSWER")}
<div class="k" style="position:absolute;left:96px;top:200px">에녹이의 답 · Answer</div>
<div style="position:absolute;left:92px;top:250px;font-size:78px;font-weight:700;letter-spacing:-4px;line-height:1.22">실력이 없어서가 아니라,<br><mark>낯설어서</mark>입니다</div>
<div class="p" style="position:absolute;left:96px;right:96px;top:560px">연습실은 매일 가는 곳이고,<br>시험장은 그날 처음 보는 곳.<br>게다가 한 번뿐이라는 생각이 더해지면 몸이 먼저 굳어요.<br><br>떨림을 없애기보다, <b>시험장과 비슷한 상황에<br>미리 익숙해지는 것</b>이 도움이 됩니다.</div>
<svg width="300" height="300" style="position:absolute;right:80px;top:930px">{mascot(150,190,0.8,"calm","hug")}</svg>
{F(5)}</section>''')
# 6 해보기
row = lambda n, t, d, last=False: f'<div style="display:flex;gap:32px;padding:30px 0;border-top:1px solid rgba(241,237,228,.3){";border-bottom:1px solid rgba(241,237,228,.3)" if last else ""}"><span class="num">{n}</span><div><div style="font-size:36px;font-weight:700">{t}</div><div style="margin-top:10px;font-size:28px;color:#C9C4BB;line-height:1.5">{d}</div></div></div>'
S.append(f'''<section class="s dark" id="t6">{H("TRY THIS WEEK")}
<div style="position:absolute;left:92px;top:200px;font-size:80px;font-weight:700;letter-spacing:-4px;line-height:1.2">시험장을,<br>미리 만나 보기</div>
<div style="position:absolute;left:96px;right:96px;top:480px">
{row(1,'딱 한 번만','연습 중 한 번은 다시 하지 않기로 정해 보세요.<br>노래든 연주든, 실수해도 끝까지.')}
{row(2,'처음 보는 사람 앞에서','익숙하지 않은 사람 앞에서 노래하거나 연주해 보면,<br>시험장의 낯섦과 조금 가까워져요.')}
{row(3,'들어가는 순간부터','문을 열고 들어가서 첫 음을 내기까지. 그 순서도 연습의 일부입니다.',True)}
</div>
<svg width="200" height="220" style="position:absolute;right:70px;top:150px">{mascot(100,150,0.55,"smile","wave",ink="#F1EDE4")}</svg>
{F(6)}</section>''')
# 7 마무리
S.append(f'''<section class="s dark" id="t7">{H("THE ENOCH WAY")}
<div style="position:absolute;left:92px;top:200px;font-size:80px;font-weight:700;letter-spacing:-4px;line-height:1.2">고민,<br><span style="color:var(--lime)">보내 주세요.</span></div>
<div class="p" style="position:absolute;left:96px;right:96px;top:470px;color:#C9C4BB">음악 하면서 생긴 고민을 스토리 질문으로 받습니다.<br>골라서, 에녹이가 Dear ENOCH로 답할게요.<br><br>같은 곡도, 사람마다 다르게 가르칩니다.<br>입시 과정도 모두 <b style="color:#F1EDE4">1:1</b>.</div>
<svg width="320" height="400" style="position:absolute;right:90px;top:760px">{mascot(160,260,0.95,"happy","up",ink="#F1EDE4")}</svg>
<div style="position:absolute;left:96px;top:1040px;font-size:22px;line-height:1.6">에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층 · 010 3949 3666</span></div>
{F(7)}</section>''')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
open('toon.html', 'w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>Dear ENOCH 02</title><style>{FONT}{CSS}</style></head><body>' + ''.join(S) + '</body></html>')
