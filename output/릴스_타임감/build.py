# 릴스 "틀린 음보다 더 티 나는 것" (타임감과 그루브) — ENOCH 릴스 엔진(scripts/reel_kinetic.py) 사용
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
 ("차이는 음이 아니라<br>시간에 있어요", METRO,
  "$('arm').style.transform=`rotate(${Math.sin(u*Math.PI*2)*24}deg)`;", 'bk', 2.2),
 ("타임이 흔들리면<br>듣는 사람이<br>먼저 압니다", circles('w'),
  beatjs('w', "e.style.transform=`translate(${Math.sin(u*9+k*2)*12*cl(u-0.6)}px,${Math.cos(u*7+k)*10*cl(u-0.6)}px)`;"), 'iv', 2.3),
 ("합주에서는<br>한 사람의 박이<br>모두의 박이 됩니다", ICONS,
  "for(let k=1;k<=3;k++){pop($('ic'+k),(u-0.3-0.25*(k-1))/0.45); $('ic'+k).style.background=(u>1.2&&(u*2)%1<0.25)?'#DCE2D3':'#FFFDF7';}", 'iv', 2.4),
 ("그루브가 있으면<br>몸이 먼저<br>반응해요", f'<div id="c7">{ch("happy", "up")}</div>',
  "$('c7').style.transform=`translateY(${-Math.abs(Math.sin(u*6))*34}px) rotate(${Math.sin(u*6)*5}deg)`;", 'iv', 2.0),
 ("정확함은<br>믿음을 만들고", circles('y'), beatjs('y'), 'bk', 2.0),
 ("그루브는 음악을<br>살아 있게 만듭니다", WAVE,
  "$('wave').style.strokeDashoffset=1-ease((u-0.4)/1.1); $('flat').style.opacity=1-ease((u-0.4)/1.1)*0.7;", 'iv', 2.1),
]
END = "화려한 음 하나보다,<br>흔들리지 않는 한 박."
DUR = round(2.4 + sum(s[4] for s in SCENES) + 2.6, 2)
T = build(os.path.join(HERE, 'reel.html'), ('PRACTICE NOTE — TIMING', '틀린 음보다<br>더 티 나는 것'), SCENES, END, DUR, topic='TIMING · GROOVE')
print('reel.html', DUR, 's', T)
