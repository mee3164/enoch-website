# 칠판 설명 영상 (에녹이 모양은 ../디어에녹_01_무대떨림/mascot.py 기준)
# "같은 연습, 다른 결과" — 에녹이 진행 (1080×1920, 릴스)
# python3 gen.py → video.html (브라우저에서 열면 재생) → node record.mjs 로 MP4
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))

INK = '#111'; SAGE = '#DCE2D3'; GRAY = '#8A8A8A'; IV = '#F1EDE4'
END = 14.5
uid = [0]
def nid():
    uid[0] += 1; return uid[0]

def draw(d, t0, dur, sw=5, color=INK, fill='none', extra=''):
    return (f'<path d="{d}" pathLength="1" data-k="draw" data-t0="{t0}" data-dur="{dur}" '
            f'stroke="{color}" stroke-width="{sw}" fill="{fill}" stroke-linecap="round" stroke-linejoin="round" '
            f'style="stroke-dasharray:1 1;stroke-dashoffset:1" {extra}/>')

def pen(x, y, txt, size, t0, dur, anchor='middle', color=INK, font='N', w=None):
    i = nid()
    W = w or len(txt) * size * 0.62 + 40
    x0 = x - (W / 2 if anchor == 'middle' else (W - 20 if anchor == 'end' else 20))
    return (f'<clipPath id="c{i}"><rect data-k="wipe" data-t0="{t0}" data-dur="{dur}" data-w="{W:.0f}" '
            f'x="{x0:.0f}" y="{y - size * 1.2:.0f}" width="0" height="{size * 1.7:.0f}"/></clipPath>'
            f'<text x="{x}" y="{y}" font-size="{size}" text-anchor="{anchor}" fill="{color}" '
            f'font-family="{font}" clip-path="url(#c{i})">{txt}</text>')

def fade(inner, t0, dur=0.3):
    return f'<g data-k="fade" data-t0="{t0}" data-dur="{dur}" opacity="0">{inner}</g>'

def show(inner, a, b):
    return f'<g data-k="show" data-a="{a}" data-b="{b}" opacity="0">{inner}</g>'

def star(cx, cy, r):
    import math
    pts = []
    for k in range(10):
        rr = r if k % 2 == 0 else r * 0.45
        a = -math.pi / 2 + k * math.pi / 5
        pts.append(f'{cx + rr * math.cos(a):.0f} {cy + rr * math.sin(a):.0f}')
    return 'M' + ' L'.join(pts) + ' Z'

# ── 칠판 (고정) ─────────────────────────────
BX0, BX1, BY0, BY1 = 90, 990, 330, 1050
board = (f'<path d="M{BX0} {BY0+2} L{BX1-1} {BY0} L{BX1+1} {BY1-1} L{BX0-1} {BY1+1} Z" stroke="{INK}" stroke-width="6" fill="#FFFDF7"/>'
         f'<path d="M{BX0+14} {BY0+15} L{BX1-15} {BY0+13} L{BX1-13} {BY1-14} L{BX0+15} {BY1-13} Z" stroke="{INK}" stroke-width="3" fill="none"/>'
         f'<path d="M150 {BY1+2} L150 1112 L520 1112 L520 {BY1+2}" stroke="{INK}" stroke-width="5" fill="none"/>'
         f'<path d="M{BX0+15} 410 L{BX1-15} 408" stroke="{INK}" stroke-width="3"/>')

def header(label, n, a, b):
    circ = ''
    for k in range(1, 4):
        cx = 830 + (k - 1) * 46
        if k == n:
            circ += f'<circle cx="{cx}" cy="374" r="19" fill="{SAGE}" stroke="{INK}" stroke-width="3"/>'
        circ += f'<text x="{cx}" y="386" font-size="32" text-anchor="middle" font-family="N" fill="{INK}">{k}</text>'
    if n == 0: circ = ''
    return show(f'<text x="128" y="388" font-size="40" font-family="N" fill="{INK}">{label}</text>{circ}', a, b)

S = []
# ① 같은 연습 (0–3)
S.append(header('1. 같은 연습', 1, 0, 3))
S.append(show(
    pen(540, 520, '같은 곡, 같은 시간', 72, 0.1, 0.5)
    + pen(205, 690, 'A', 60, 0.5, 0.15)
    + draw('M260 672 C 400 668, 600 676, 740 670', 0.55, 0.5)
    + pen(500, 640, '1시간', 40, 0.8, 0.2, color=GRAY)
    + pen(205, 850, 'B', 60, 0.75, 0.15)
    + draw('M260 832 C 400 828, 600 836, 740 830', 0.8, 0.5)
    + pen(500, 800, '1시간', 40, 1.0, 0.2, color=GRAY)
    + pen(870, 560, '결과', 42, 1.5, 0.2, color=GRAY)
    + draw('M850 690 L870 650 L890 690 Z', 1.7, 0.3)
    + draw(star(870, 830, 30), 2.0, 0.35, fill='none')
    , 0, 3))
# ② 연구 (3–9.5)
S.append(header('2. 피아노 연습 연구', 2, 3, 9.5))
S.append(show(fade(f'<text x="952" y="1012" font-size="30" text-anchor="end" font-family="N" fill="{GRAY}">Duke, Simmons &amp; Cash (2009)</text>', 3.1), 3, 9.5))
keys = ''.join(f'M{300 + k * 60} 580 L{300 + k * 60} 740 ' for k in range(1, 8))
blacks = ''.join(f'<rect x="{348 + k * 60}" y="580" width="24" height="95" fill="{INK}"/>' for k in (0, 1, 3, 4, 5))
S.append(show(
    pen(540, 500, '피아노 전공생 17명', 66, 3.1, 0.5)
    + draw('M300 580 L780 580 L780 740 L300 740 Z', 3.6, 0.35)
    + draw(keys, 3.9, 0.35, sw=3)
    + fade(blacks, 4.2)
    , 3, 5.2))
staff = ''.join(f'M180 {700 + k * 20} L900 {700 + k * 20} ' for k in range(5))
bars = ''.join(f'M{x} 700 L{x} 780 ' for x in (180, 360, 540, 720, 900))
notes = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="13" ry="9" transform="rotate(-20 {x} {y})" fill="{INK}"/>'
                for x, y in ((230, 760), (290, 740), (410, 730), (470, 750), (590, 720), (650, 740), (770, 760), (840, 740)))
S.append(show(
    pen(250, 530, '오래 반복', 58, 5.3, 0.4, anchor='start')
    + draw('M520 515 c 20 -40 50 -40 40 0 c -10 40 30 40 40 0 c 10 -40 50 -40 40 0 c -10 40 30 40 40 0 c 10 -40 50 -40 40 0 c -10 40 30 40 40 0 c 10 -40 50 -40 40 0', 5.6, 0.6, sw=4)
    + draw('M230 470 L900 570 M900 470 L230 570', 6.3, 0.3, sw=6, color=GRAY)
    + fade(f'<ellipse cx="540" cy="740" rx="200" ry="78" fill="{SAGE}" opacity=".85"/>', 7.4, 0.3)
    + draw(staff, 6.8, 0.3, sw=2)
    + draw(bars, 7.0, 0.2, sw=3)
    + fade(notes, 7.1, 0.2)
    + draw('M345 745 C 340 650, 740 640, 738 740 C 736 835, 350 840, 352 735', 7.4, 0.4, sw=5)
    + pen(540, 900, '틀린 두 마디', 56, 7.8, 0.35)
    + draw('M470 630 C 480 590, 600 590, 610 630 M600 612 L612 632 L590 636', 8.1, 0.35, sw=4)
    , 5.2, 9.5))
# ③ 오늘의 연습 (9.5–12)
S.append(header('3. 오늘의 연습', 3, 9.5, 12))
S.append(show(
    pen(540, 590, '얼마나 오래', 70, 9.6, 0.4, color=GRAY)
    + draw('M330 570 L752 566', 10.0, 0.3, sw=6)
    + fade(f'<path d="M540 640 L540 690 M520 672 L540 692 L560 672" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/>', 10.2, 0.2)
    + draw('M290 800 C 450 812, 640 790, 790 806', 10.8, 0.3, sw=22, color=SAGE)
    + pen(540, 790, '무엇을 고칠지', 92, 10.3, 0.5)
    , 9.5, 12))
# ④ 마무리 (12–END)
S.append(header('ENOCH의 방식', 0, 12, END + 1))
S.append(show(
    pen(540, 620, '진도보다 이해를', 84, 12.1, 0.5)
    + pen(540, 740, '먼저 봅니다.', 84, 12.5, 0.45)
    + draw(star(250, 880, 26), 13.0, 0.3, sw=4)
    + draw('M790 860 c 30 -10 50 10 40 30 c -10 20 -40 15 -40 -5 c 0 -25 40 -35 60 -15', 13.1, 0.35, sw=4)
    , 12, END + 1))

# ── 에녹이 (오른쪽 아래) — 말할 때 입이 열리고, 지시봉으로 칠판을 가리킨다 ──
MX, MY, MS = 835, 1240, 0.82
SHX, SHY = MX - 80 * MS, MY - 6 * MS          # 왼쪽 어깨 (지시봉 팔의 회전 중심)
def body():
    g = [f'<g transform="translate({MX},{MY}) scale({MS})" stroke="{INK}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" fill="none">',
         '<path d="M70 -10 V -250"/><path d="M70 -250 C 110 -220, 140 -200, 120 -140"/>',
         '<path d="M-30 58 L -38 110 M 30 58 L 36 110"/><path d="M-38 110 h -26 M 36 110 h 26"/>',
         '<path d="M 92 0 C 120 20, 128 50, 122 72"/>',
         '<ellipse cx="0" cy="0" rx="95" ry="70" transform="rotate(-18)" fill="#FFFDF7"/>',
         '<g stroke="none" fill="#DDE37C"><ellipse cx="-50" cy="22" rx="16" ry="10"/><ellipse cx="44" cy="4" rx="16" ry="10"/></g>',
         # 눈: 뜬 눈 / 깜빡 / 웃는 눈
         '<g id="eo" fill="#111" stroke="none"><ellipse cx="-30" cy="-8" rx="7" ry="9"/><ellipse cx="22" cy="-22" rx="7" ry="9"/></g>',
         '<path id="ec" d="M-38 -6 h 16 M 14 -20 h 16" stroke-width="5" opacity="0"/>',
         '<path id="eh" d="M-38 -4 q 8 -10 16 0 M 14 -18 q 8 -10 16 0" stroke-width="5" opacity="0"/>',
         # 입: 다문 입 / 벌린 입
         '<path id="mc" d="M-14 16 Q 0 28 14 10" stroke-width="5"/>',
         '<g id="mo" opacity="0"><path d="M-16 10 Q 0 6 16 4 Q 18 30 0 34 Q -18 32 -16 10 Z" fill="#111" stroke-width="4"/>'
         '<path d="M-8 28 Q 0 22 9 27" stroke="#EEDFD8" stroke-width="5"/></g>',
         '</g>']
    return ''.join(g)
arm = (f'<g id="arm" transform="translate({SHX:.0f} {SHY:.0f}) rotate(-120)">'
       f'<path d="M0 0 C 22 -10, 44 -6, 64 0" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"/>'
       f'<path id="stk" d="M70 0 L420 0" stroke="#7A6A55" stroke-width="7" stroke-linecap="round"/>'
       f'<circle id="tip" cx="422" cy="0" r="8" fill="{INK}"/>'
       f'<circle cx="68" cy="0" r="12" fill="#FFFDF7" stroke="{INK}" stroke-width="5"/></g>')
M = arm + body()
# 지시봉이 가리킬 곳 (초, x, y) — 칠판에 그림이 그려지는 자리를 따라간다
POINT = [(0, 540, 520), (0.55, 500, 670), (0.8, 500, 830), (1.6, 870, 690), (2.0, 870, 830),
         (3.1, 540, 500), (3.7, 540, 660),
         (5.3, 330, 530), (5.7, 680, 515), (6.8, 540, 740), (7.9, 540, 890),
         (9.6, 540, 580), (10.3, 540, 790),
         (12.1, 540, 610), (12.5, 540, 730)]
SUBS = [(0, 3, '같은 시간 연습해도, 결과는 다릅니다.'),
        (3, 5.2, '피아노 전공생 17명을 지켜본 연구에서'),
        (5.2, 7.2, '오래 친 사람보다'),
        (7.2, 9.5, '틀린 곳을 고친 사람이 잘 쳤어요.'),
        (9.5, 12, '얼마나 오래보다, 무엇을 고칠지.'),
        (12, END + 1, '에녹실용음악학원 시흥점 · 모든 과정 1:1')]
subs = ''.join(f'<div class="sub" data-k="show" data-a="{a}" data-b="{b}" style="opacity:0">{t}</div>' for a, b, t in SUBS)

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>같은 연습, 다른 결과 — 영상</title>
<link rel="stylesheet" href="../../templates/fonts/nanum-pen-script/400.css">
<style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Medium.woff2);font-weight:500}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#ddd}}
#v{{width:1080px;height:1920px;position:relative;overflow:hidden;background:{IV};font-family:P,sans-serif;color:{INK};word-break:keep-all}}
svg{{position:absolute;inset:0}}
#v>*{{transform:translateY(50px)}}
text[font-family=N]{{font-family:'Nanum Pen Script'}}
.kick{{position:absolute;top:150px;width:100%;text-align:center;font-size:26px;letter-spacing:.3em;color:{GRAY};font-weight:500}}
.title{{position:absolute;top:196px;width:100%;text-align:center;font-size:66px;font-weight:700;letter-spacing:-.02em}}
.sub{{position:absolute;top:1390px;left:60px;right:60px;text-align:center;font-size:46px;font-weight:600;letter-spacing:-.01em;line-height:1.35}}
.brand{{position:absolute;top:1530px;width:100%;text-align:center;font-size:32px;font-weight:600}}
#warm{{position:absolute;left:-9999px;font-family:'Nanum Pen Script'}}
</style></head><body>
<div id="v">
<div class="kick">ENOCH NOTE</div>
<div class="title">같은 연습, 다른 결과</div>
<svg viewBox="0 0 1080 1920" width="1080" height="1920">
<defs><filter id="wob"><feTurbulence type="fractalNoise" baseFrequency="0.018" numOctaves="2" seed="7"/><feDisplacementMap in="SourceGraphic" scale="5"/></filter></defs>
<g filter="url(#wob)">{board}{''.join(S)}</g>
<g id="mb">{M}</g>
</svg>
{subs}
<div class="brand">나만의 진짜 소리를 찾는 곳.</div>
</div>
<div id="warm"></div>
<script>
const END={END}; const SUBT={[[a,b] for a,b,_ in SUBS]}; const POINT={[list(p) for p in POINT]}; const SH=[{SHX},{SHY}];
const cl=x=>Math.max(0,Math.min(1,x)); const ease=p=>1-Math.pow(1-p,2);
function render(t){{
  for(const e of document.querySelectorAll('[data-k]')){{
    const k=e.dataset.k;
    if(k==='show'){{const a=+e.dataset.a,b=+e.dataset.b;let o=cl((t-a)/0.25)*cl((b-t)/0.25);if(a===0&&t<0.25)o=1;e.style.opacity=o;}}
    else{{const p=ease(cl((t-e.dataset.t0)/e.dataset.dur));
      if(k==='draw')e.style.strokeDashoffset=1-p;
      else if(k==='wipe')e.setAttribute('width',p*e.dataset.w);
      else if(k==='fade')e.setAttribute('opacity',p);}}
  }}
  document.getElementById('mb').setAttribute('transform',`translate(0 ${{(Math.sin(t*Math.PI*2/1.4)*4).toFixed(2)}})`);
  // 말하기: 자막이 떠 있는 동안 입을 여닫는다
  let talk=false; for(const [a,b] of SUBT) if(t>a+0.1&&t<b-0.45) talk=true;
  const syl=Math.floor(t*9); const open=talk&&((syl*7919+13)%5)<3;
  document.getElementById('mo').setAttribute('opacity',open?1:0);
  document.getElementById('mc').setAttribute('opacity',open?0:1);
  // 눈: 마지막 장면은 웃는 눈, 그 전에는 가끔 깜빡
  const happy=t>=12.6, blink=!happy&&(t%2.6)>2.48;
  document.getElementById('eh').setAttribute('opacity',happy?1:0);
  document.getElementById('ec').setAttribute('opacity',blink?1:0);
  document.getElementById('eo').setAttribute('opacity',(!happy&&!blink)?1:0);
  // 지시봉: 어깨에서 목표 지점 방향으로 돌린다
  const ang=([,x,y])=>Math.atan2(y-SH[1],x-SH[0])*180/Math.PI;
  let i=0; while(i+1<POINT.length&&POINT[i+1][0]<=t) i++;
  const prev=i>0?ang(POINT[i-1]):ang(POINT[0]), cur=ang(POINT[i]);
  const p=ease(cl((t-POINT[i][0])/0.35));
  const wob=Math.sin(t*Math.PI*2/0.9)*1.5;
  // 지시봉 길이: 목표 바로 앞(약 70px)에서 멈춰 글자를 가리지 않게
  const dist=([,x,y])=>Math.hypot(x-SH[0],y-SH[1]);
  const L=Math.max(260,Math.min(430,(dist(POINT[i>0?i-1:0])+(dist(POINT[i])-dist(POINT[i>0?i-1:0]))*p)-70));
  document.getElementById('stk').setAttribute('d',`M70 0 L${{L.toFixed(1)}} 0`);
  document.getElementById('tip').setAttribute('cx',(L+2).toFixed(1));
  document.getElementById('arm').setAttribute('transform',`translate(${{SH[0]}} ${{SH[1]}}) rotate(${{(prev+(cur-prev)*p+wob).toFixed(2)}})`);
}}
document.getElementById('warm').textContent=[...document.querySelectorAll('text')].map(e=>e.textContent).join('');
window.render=render;
if(!location.search.includes('record')){{const s=performance.now();(function f(){{render(((performance.now()-s)/1000)%(END+1));requestAnimationFrame(f)}})();}}
else render(0);
</script></body></html>'''
open(os.path.join(HERE, 'video.html'), 'w').write(html)
print('video.html')
