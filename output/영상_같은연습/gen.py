# 칠판 설명 영상 "같은 연습, 다른 결과" — 에녹이 진행 (1080×1920, 릴스)
# python3 gen.py → video.html (브라우저에서 열면 재생) → node record.mjs 로 MP4
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '../디어에녹_01_무대떨림'))
from mascot import mascot

INK = '#111'; SAGE = '#DCE2D3'; GRAY = '#8A8A8A'; IV = '#F1EDE4'
END = 22.5
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
# ① 같은 연습 (0–6)
S.append(header('1. 같은 연습', 1, 0, 6))
S.append(show(
    pen(540, 520, '같은 곡, 같은 시간', 72, 0.3, 0.9)
    + pen(205, 690, 'A', 60, 1.1, 0.2)
    + draw('M260 672 C 400 668, 600 676, 740 670', 1.2, 0.9)
    + pen(500, 640, '1시간', 40, 1.6, 0.3, color=GRAY)
    + pen(205, 850, 'B', 60, 1.5, 0.2)
    + draw('M260 832 C 400 828, 600 836, 740 830', 1.6, 0.9)
    + pen(500, 800, '1시간', 40, 2.0, 0.3, color=GRAY)
    + pen(870, 560, '결과', 42, 3.2, 0.3, color=GRAY)
    + draw('M850 690 L870 650 L890 690 Z', 3.6, 0.5)
    + draw(star(870, 830, 30), 4.0, 0.5, fill='none')
    , 0, 6))
# ② 연구 (6–15)
S.append(header('2. 피아노 연습 연구', 2, 6, 15))
S.append(show(fade(f'<text x="952" y="1012" font-size="30" text-anchor="end" font-family="N" fill="{GRAY}">Duke, Simmons &amp; Cash (2009)</text>', 6.2), 6, 15))
keys = ''.join(f'M{300 + k * 60} 580 L{300 + k * 60} 740 ' for k in range(1, 8))
blacks = ''.join(f'<rect x="{348 + k * 60}" y="580" width="24" height="95" fill="{INK}"/>' for k in (0, 1, 3, 4, 5))
S.append(show(
    pen(540, 500, '피아노 전공생 17명', 66, 6.3, 0.9)
    + draw('M300 580 L780 580 L780 740 L300 740 Z', 7.1, 0.6)
    + draw(keys, 7.6, 0.6, sw=3)
    + fade(blacks, 8.1)
    , 6, 9.5))
staff = ''.join(f'M180 {700 + k * 20} L900 {700 + k * 20} ' for k in range(5))
bars = ''.join(f'M{x} 700 L{x} 780 ' for x in (180, 360, 540, 720, 900))
notes = ''.join(f'<ellipse cx="{x}" cy="{y}" rx="13" ry="9" transform="rotate(-20 {x} {y})" fill="{INK}"/>'
                for x, y in ((230, 760), (290, 740), (410, 730), (470, 750), (590, 720), (650, 740), (770, 760), (840, 740)))
S.append(show(
    pen(250, 530, '오래 반복', 58, 9.7, 0.6, anchor='start')
    + draw('M520 515 c 20 -40 50 -40 40 0 c -10 40 30 40 40 0 c 10 -40 50 -40 40 0 c -10 40 30 40 40 0 c 10 -40 50 -40 40 0 c -10 40 30 40 40 0 c 10 -40 50 -40 40 0', 10.3, 1.0, sw=4)
    + draw('M230 470 L900 570 M900 470 L230 570', 11.4, 0.5, sw=6, color=GRAY)
    + fade(f'<ellipse cx="540" cy="740" rx="200" ry="78" fill="{SAGE}" opacity=".85"/>', 13.3, 0.4)
    + draw(staff, 12.2, 0.5, sw=2)
    + draw(bars, 12.6, 0.3, sw=3)
    + fade(notes, 12.8)
    + draw('M345 745 C 340 650, 740 640, 738 740 C 736 835, 350 840, 352 735', 13.3, 0.6, sw=5)
    + pen(540, 900, '틀린 두 마디', 56, 13.9, 0.5)
    + draw('M470 630 C 480 590, 600 590, 610 630 M600 612 L612 632 L590 636', 14.3, 0.5, sw=4)
    , 9.5, 15))
# ③ 오늘의 연습 (15–18)
S.append(header('3. 오늘의 연습', 3, 15, 18))
S.append(show(
    pen(540, 590, '얼마나 오래', 70, 15.2, 0.6, color=GRAY)
    + draw('M330 570 L752 566', 15.9, 0.4, sw=6)
    + fade(f'<path d="M540 640 L540 690 M520 672 L540 692 L560 672" stroke="{INK}" stroke-width="4" fill="none" stroke-linecap="round"/>', 16.2)
    + draw('M290 800 C 450 812, 640 790, 790 806', 17.0, 0.4, sw=22, color=SAGE)
    + pen(540, 790, '무엇을 고칠지', 92, 16.4, 0.7)
    , 15, 18))
# ④ 마무리 (18–END)
S.append(header('ENOCH의 방식', 0, 18, END + 1))
S.append(show(
    pen(540, 620, '진도보다 이해를', 84, 18.3, 0.7)
    + pen(540, 740, '먼저 봅니다.', 84, 19.0, 0.6)
    + draw(star(250, 880, 26), 19.7, 0.4, sw=4)
    + draw('M790 860 c 30 -10 50 10 40 30 c -10 20 -40 15 -40 -5 c 0 -25 40 -35 60 -15', 19.9, 0.5, sw=4)
    + fade(f'<text x="540" y="975" font-size="26" letter-spacing="8" text-anchor="middle" font-family="P" font-weight="500" fill="{GRAY}">ENOCH MUSIC ACADEMY</text>', 20.3)
    , 18, END + 1))

# ── 에녹이 (오른쪽 아래, 장면마다 표정) ─────────
MX, MY, MS = 835, 1240, 0.82
def m(a, b, **kw):
    return show(mascot(MX, MY, MS, **kw), a, b)
M = (m(0, 6, face='calm', arms='down') + m(6, 9.5, face='smile', arms='down')
     + m(9.5, 15, face='smile', arms='wave', flip=True) + m(15, 18, face='smile', arms='down')
     + m(18, END + 1, face='happy', arms='up'))

SUBS = [(0, 3, '같은 곡을, 같은 시간 동안 연습해도'),
        (3, 6, '결과는 사람마다 다릅니다.'),
        (6, 9.5, '피아노 전공생 17명의 연습을 지켜본 연구가 있어요.'),
        (9.5, 12, '잘 친 사람은, 오래 친 사람이 아니었습니다.'),
        (12, 15, '틀린 자리를 찾아, 그 자리를 고친 사람.'),
        (15, 18, '얼마나 오래보다, 무엇을 고칠지 보세요.'),
        (18, END + 1, '에녹실용음악학원 시흥점 · 모든 과정 1:1')]
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
const END={END};
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
  document.getElementById('mb').setAttribute('transform',`translate(0 ${{(Math.sin(t*Math.PI*2/1.4)*5).toFixed(2)}})`);
}}
document.getElementById('warm').textContent=[...document.querySelectorAll('text')].map(e=>e.textContent).join('');
window.render=render;
if(!location.search.includes('record')){{const s=performance.now();(function f(){{render(((performance.now()-s)/1000)%(END+1));requestAnimationFrame(f)}})();}}
else render(0);
</script></body></html>'''
open(os.path.join(HERE, 'video.html'), 'w').write(html)
print('video.html')
