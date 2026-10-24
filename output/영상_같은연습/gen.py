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
# ① 막히는 자리 (0–4) — 파트마다 한 곡 안에 꼭 막히는 곳
S.append(header('1. 막히는 자리', 1, 0, 4))
S.append(show(
    pen(150, 530, '보컬', 64, 0.15, 0.2, anchor='start')
    + pen(150, 595, '고음 한 소절', 46, 0.30, 0.3, anchor='start', color=GRAY)
    + pen(570, 530, '기타', 64, 0.60, 0.2, anchor='start')
    + pen(570, 595, '코드 바뀌는 곳', 46, 0.75, 0.3, anchor='start', color=GRAY)
    + pen(150, 690, '드럼', 64, 1.05, 0.2, anchor='start')
    + pen(150, 755, '필인 들어가는 마디', 46, 1.20, 0.3, anchor='start', color=GRAY)
    + pen(570, 690, '베이스', 64, 1.50, 0.2, anchor='start')
    + pen(570, 755, '박이 밀리는 곳', 46, 1.65, 0.3, anchor='start', color=GRAY)
    + pen(150, 850, '피아노', 64, 1.95, 0.2, anchor='start')
    + pen(150, 915, '두 손이 엇갈리는 곳', 46, 2.10, 0.3, anchor='start', color=GRAY)
    + pen(570, 850, '작곡', 64, 2.40, 0.2, anchor='start')
    + pen(570, 915, '다음 마디', 46, 2.55, 0.3, anchor='start', color=GRAY)
    , 0, 4))
# ② 연습하는 법 (4–9.5) — 처음부터 다시 ✕ / 막힌 곳만 ○
boxes = ''.join(f'M{140 + k * 100} 640 L{140 + k * 100} 730 ' for k in range(1, 8))
S.append(header('2. 연습하는 법', 2, 4, 9.5))
S.append(show(
    pen(540, 520, '처음부터 다시', 58, 4.6, 0.35)
    + draw('M920 625 C 760 560, 320 560, 165 622 M182 600 L163 624 L190 632', 4.9, 0.5, sw=4)
    + draw('M300 470 L780 610 M780 470 L300 610', 5.6, 0.3, sw=6, color=GRAY)
    + fade(f'<rect x="540" y="640" width="100" height="90" fill="{SAGE}"/>', 6.1, 0.3)
    + draw('M140 640 L940 640 L940 730 L140 730 Z', 4.1, 0.4, sw=4)
    + draw(boxes, 4.4, 0.25, sw=3)
    + draw('M522 690 C 515 615, 662 612, 660 688 C 658 760, 520 762, 526 684', 6.1, 0.4, sw=5)
    + pen(560, 830, '막힌 곳만', 62, 6.6, 0.35)
    + draw('M730 790 a 26 26 0 1 1 -6 34 M716 832 L724 822 L734 832', 7.0, 0.4, sw=4)
    , 4, 9.5))
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
POINT = [(0.15, 440, 620), (0.6, 880, 620), (1.05, 440, 780), (1.5, 880, 780), (1.95, 440, 940), (2.4, 880, 940),
         (4.1, 540, 690), (4.9, 540, 590), (6.1, 590, 690), (6.6, 590, 830),
         (9.6, 540, 580), (10.3, 540, 790),
         (12.1, 540, 610), (12.5, 540, 730)]
SUBS = [(0, 2, '곡마다 꼭 막히는 자리가 있어요.'),
        (2, 4, '악기마다 모양만 다를 뿐입니다.'),
        (4, 6, '처음부터 다시 하기보다'),
        (6, 9.5, '막힌 자리만 떼어 연습해 보세요.'),
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
