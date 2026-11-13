# 릴스 "화려하게 쳐도 아마추어처럼 들리는 이유" (타임감과 그루브) — ENOCH 릴스 엔진(scripts/reel_kinetic.py) 사용
# 훅 카드 → 왼쪽 정렬 큰 문장 + 오른쪽 아래 일러스트 → 아래 박 줄 → 검정 마무리. 형광펜 없음, 한국어만.
# python3 output/릴스_타임감/build.py → reel.html → CHROMIUM_PATH=... node output/릴스_타임감/render.mjs
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'scripts'))
from reel_kinetic import build, ch, note, INK  # noqa: E402


def sheet(x):
    return (f'<g transform="translate({x},0)"><rect x="0" y="40" width="240" height="320" rx="8" fill="#FFFDF7"/>'
            + ''.join(f'<path d="M30 {100+i*50} H 210"/>' for i in range(5)) + f'{note(80,190,.8)}{note(150,240,.8)}</g>')


def circles(prefix, size=120):
    return '<div style="display:flex;gap:24px">' + ''.join(
        f'<i id="{prefix}{k}" style="width:{size}px;height:{size}px;border:6px solid {INK};border-radius:50%;background:#FFFDF7;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:48px;font-weight:700;color:{INK}">{k}</i>' for k in range(1, 5)) + '</div>'


ICON = {
 'Drum': f'<svg viewBox="0 0 200 200" width="110" height="110"><g stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round"><ellipse cx="100" cy="80" rx="62" ry="20"/><path d="M38 80 V 140 C 38 166, 162 166, 162 140 V 80"/><path d="M60 40 L 96 70 M140 40 L 104 70"/></g></svg>',
 'Bass': f'<svg viewBox="0 0 200 200" width="110" height="110"><g stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round" stroke-linejoin="round" transform="rotate(35 100 100)"><path d="M100 120 C 70 112, 58 140, 70 160 C 82 182, 118 182, 130 160 C 142 140, 130 112, 100 120 Z"/><path d="M100 120 V 24"/><rect x="90" y="10" width="20" height="22" rx="3"/></g></svg>',
 'Keys': f'<svg viewBox="0 0 200 200" width="110" height="110"><g stroke="{INK}" stroke-width="8" fill="none" stroke-linejoin="round"><rect x="24" y="70" width="152" height="70" rx="6"/><path d="M52 70 V 140 M80 70 V 140 M108 70 V 140 M136 70 V 140"/></g><g fill="{INK}"><rect x="44" y="70" width="14" height="40"/><rect x="72" y="70" width="14" height="40"/><rect x="128" y="70" width="14" height="40"/></g></svg>',
}
ICONS = '<div style="display:flex;gap:22px">' + ''.join(
    f'<div id="ic{k}" style="width:190px;height:190px;border:6px solid {INK};border-radius:24px;background:#FFFDF7;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:22px;font-weight:700;color:{INK};opacity:0">{svg}<span>{nm}</span></div>'
    for k, (nm, svg) in enumerate(ICON.items(), 1)) + '</div>'

METRO = f'''<svg viewBox="0 0 400 460" width="400" height="460"><g stroke="{INK}" stroke-width="8" fill="none" stroke-linejoin="round" stroke-linecap="round">
 <path d="M110 420 L 170 60 H 230 L 290 420 Z" fill="#FFFDF7"/><path d="M80 420 H 320"/><circle cx="200" cy="340" r="14" fill="{INK}"/>
 <g id="arm" style="transform-origin:200px 340px"><path d="M200 340 L 200 110"/><rect x="186" y="160" width="28" height="20" fill="{INK}"/></g></g></svg>'''

WAVE = f'''<svg viewBox="0 0 640 300" width="640" height="300"><g stroke="{INK}" stroke-width="9" fill="none" stroke-linecap="round">
 <path id="flat" d="M20 150 H 620" stroke="#B9B4AA"/>
 <path id="wave" d="M20 150 C 90 40, 170 40, 240 150 S 390 260, 460 150 S 580 40, 620 120" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></g></svg>'''


def beatjs(p, extra=''):
    return (f"for(let k=1;k<=4;k++){{const e=$('{p}'+k);const on=Math.floor((u*2)%4)===k-1&&u>0.3;"
            f"e.style.background=on?'#DCE2D3':'#FFFDF7';{extra}}}")


SCENES = [
 ("같은 곡,<br>같은 음인데", f'<svg viewBox="0 0 620 400" width="620" height="400"><g stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"><g id="sh1" style="transform-origin:150px 200px">{sheet(30)}</g><g id="sh2" style="transform-origin:470px 200px">{sheet(350)}</g></g></svg>',
  "pop($('sh1'),(u-0.3)/0.5); pop($('sh2'),(u-0.5)/0.5);", 'iv', 2.0),
 ("누가 치면<br>듣기 좋고", f'<div style="display:flex;align-items:flex-end"><div id="c2">{ch("happy","wave")}</div><svg viewBox="0 0 220 360" width="220" height="360" style="overflow:visible"><g id="n2">{note(40,260)}{note(140,170,1.2)}{note(60,80,.9)}</g></svg></div>',
  "$('c2').style.transform=`translateY(${-Math.abs(Math.sin(u*5))*24}px)`; $('n2').style.transform=`translateY(${-u*30}px)`;", 'iv', 1.9),
 ("누가 치면<br>어딘가 불안합니다", f'<div id="c3">{ch("nervous", "down", sweat=True)}</div>',
  "$('c3').style.transform=`translateX(${Math.sin(u*40)*6*cl(u-0.5)}px)`;", 'iv', 2.1),
 ("타임이 흔들리면<br>듣는 사람이<br>먼저 압니다", circles('w'),
  beatjs('w', "e.style.transform=`translate(${Math.sin(u*9+k*2)*12*cl(u-0.6)}px,${Math.cos(u*7+k)*10*cl(u-0.6)}px)`;"), 'iv', 2.3),
 ("음이 많아도<br>그루브가 없으면<br>금방 지루해지고", '<svg viewBox="0 0 640 300" width="640" height="300"><g id="many" opacity=".55">' + ''.join(note(40+i*76, 220) for i in range(8)) + '</g></svg>',
  "$('many').style.transform=`translateX(${-u*14}px)`;", 'iv', 2.4),
 ("음이 적어도<br>그루브가 있으면<br>귀가 따라옵니다", f'''<svg viewBox="0 0 640 320" width="640" height="320"><path d="M20 200 C 90 110, 170 110, 240 200 S 390 290, 460 200 S 580 110, 620 170" stroke="#B9B4AA" stroke-width="5" fill="none"/><g id="few1">{note(0,0,1.1)}</g><g id="few2">{note(0,0,1.1)}</g><g id="few3">{note(0,0,1.1)}</g></svg>''',
  "[['few1',140],['few2',330],['few3',520]].forEach(([id,x],k)=>{const y=200-Math.abs(Math.sin(u*Math.PI*2+k*2.1))*70;$(id).setAttribute('transform',`translate(${x},${y})`);});", 'iv', 2.4),
 ("고개를 끄덕이게 만드는 힘,<br>그게 그루브입니다", f'<div id="c9n">{ch("happy", "wave")}</div>',
  "$('c9n').style.transform=`rotate(${Math.sin(u*Math.PI*2*1.0)*8}deg) translateY(${Math.abs(Math.sin(u*Math.PI*2))*14}px)`;$('c9n').style.transformOrigin='50% 90%';", 'iv', 2.4),
 ("정확함은<br>믿음을 만들고", circles('y'), beatjs('y'), 'bk', 2.0),
 ("그루브는 음악을<br>살아 있게 만듭니다", WAVE,
  "$('wave').style.strokeDashoffset=1-ease((u-0.4)/1.1); $('flat').style.opacity=1-ease((u-0.4)/1.1)*0.7;", 'iv', 2.1),
]
END = "화려한 음 하나보다,<br>흔들리지 않는 한 박."
DUR = round(2.4 + sum(s[4] for s in SCENES) + 2.6, 2)
T = build(os.path.join(HERE, 'reel.html'), ('PRACTICE NOTE — TIMING · GROOVE', '화려하게 쳐도<br>아마추어처럼<br>들리는 이유'), SCENES, END, DUR, topic='TIMING · GROOVE')
print('reel.html', DUR, 's', T)
