# 릴스 "자연스러운 그루브 내는 법" — 19초, 1080×1920, 아이보리 바탕 · 고정 제목 · 장면별 선 일러스트(에녹이 · 악기 · 소품) · 한/영 자막
# 참고: 원장님이 보낸 설명형 릴스 구조(고정 제목 + 가운데 그림 + 아래 자막). 문장·그림은 새로 만듦.
# python3 output/릴스_그루브/build.py → reel.html → CHROMIUM_PATH=... node output/릴스_그루브/render.mjs
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '디어에녹_01_무대떨림'))
from mascot import mascot  # noqa: E402


def ch(face, arms, w=360, h=400):
    return f'<svg viewBox="-170 -280 340 420" width="{w}" height="{h}" style="overflow:visible">{mascot(0, 0, 1.0, face=face, arms=arms)}</svg>'


INK = '#111'
NOTE = lambda x, y, s=1: f'<g transform="translate({x},{y}) scale({s})" stroke="{INK}" stroke-width="5" fill="none" stroke-linecap="round"><ellipse cx="0" cy="0" rx="14" ry="10" transform="rotate(-20)" fill="{INK}"/><path d="M12 -4 V -58 q 18 6 22 22"/></g>'

# 장면: (자막, 영어, 그림 HTML)
SC = [
 ("박자는 맞는데,", "The timing is right,",
  f'''<svg viewBox="0 0 900 560" class="ill"><g stroke="{INK}" stroke-width="7" fill="none" stroke-linejoin="round" stroke-linecap="round">
   <path d="M330 470 L 400 120 H 470 L 540 470 Z" fill="#FFFDF7"/><path d="M300 470 H 570"/><circle cx="435" cy="380" r="16" fill="{INK}"/>
   <g id="arm" style="transform-origin:435px 380px"><path d="M435 380 L 435 150"/><rect x="420" y="200" width="30" height="22" fill="{INK}"/></g></g></svg>'''),
 ("어딘가 딱딱하게 들릴 때.", "but it still sounds stiff.",
  f'''<div class="row"><div id="c2">{ch("sad", "down")}</div><svg viewBox="0 0 420 300" width="420" height="300"><g stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round">
   <path d="M20 150 H 400"/>{''.join(f'<path d="M{20+i*76} 120 V 180"/>' for i in range(6))}</g></svg></div>'''),
 ("그루브는 정확함만으로 생기지 않아요", "Groove isn't only about precision",
  f'''<svg viewBox="0 0 900 400" class="ill"><g stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round">
   <path id="flat" d="M60 200 H 840" stroke="#B9B4AA"/>
   <path id="wave" d="M60 200 C 150 80, 240 80, 330 200 S 510 320, 600 200 S 780 80, 840 170" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></g></svg>'''),
 ("몸이 먼저 타는 느낌에 가깝습니다", "It's closer to something your body feels",
  f'''<div class="row"><div id="c4">{ch("happy", "up")}</div><svg viewBox="0 0 300 360" width="300" height="360" style="overflow:visible"><g id="n4">{NOTE(60,260)}{NOTE(170,170,1.2)}{NOTE(90,90,.9)}</g></svg></div>'''),
 ("그래서 먼저, 많이 들어 보세요", "So first, listen. A lot.",
  f'''<svg viewBox="0 0 900 520" class="ill"><g stroke="{INK}" stroke-width="8" fill="none" stroke-linecap="round">
   <path d="M290 330 V 270 C 290 120, 610 120, 610 270 V 330"/>
   <rect x="250" y="300" width="80" height="140" rx="30" fill="#F1E8CB"/><rect x="570" y="300" width="80" height="140" rx="30" fill="#F1E8CB"/></g>
   <g id="n5">{NOTE(720,250)}{NOTE(790,170,.9)}{NOTE(160,230,.9)}</g></svg>'''),
 ("박을 몸으로 짚어 보고", "Feel each beat in your body,",
  '<div class="beats">' + ''.join(f'<i id="b{k}"><span>{k}</span></i>' for k in range(1, 5)) + '</div>'),
 ("센 박과 여린 박을 살려 보기", "bring out the strong and soft beats,",
  '<div class="bars">' + ''.join(f'<div class="bar" id="h{k}" data-h="{h}"><b>{t}</b></div>' for k, (h, t) in enumerate([(300, '강'), (130, '약'), (220, '중강'), (130, '약')], 1)) + '</div>'),
 ("다른 악기와 맞춰 보면 더 잘 느껴져요", "and play along with other instruments.",
  f'''<div class="icons"><div class="ic" id="i1"><svg viewBox="0 0 200 200"><g stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round"><ellipse cx="100" cy="80" rx="62" ry="20"/><path d="M38 80 V 140 C 38 166, 162 166, 162 140 V 80"/><path d="M60 40 L 96 70 M140 40 L 104 70"/></g></svg><b>Drum</b></div>
   <div class="ic" id="i2"><svg viewBox="0 0 200 200"><g stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round" transform="rotate(35 100 100)"><path d="M100 120 C 70 112, 58 140, 70 160 C 82 182, 118 182, 130 160 C 142 140, 130 112, 100 120 Z"/><path d="M100 120 V 24"/><rect x="90" y="10" width="20" height="22" rx="3"/><path d="M88 150 H 112"/></g></svg><b>Bass</b></div>
   <div class="ic" id="i3"><svg viewBox="0 0 200 200"><g stroke="{INK}" stroke-width="7" fill="none" stroke-linejoin="round"><rect x="24" y="70" width="152" height="70" rx="6"/><path d="M52 70 V 140 M80 70 V 140 M108 70 V 140 M136 70 V 140"/></g><g fill="{INK}"><rect x="44" y="70" width="14" height="40"/><rect x="72" y="70" width="14" height="40"/><rect x="128" y="70" width="14" height="40"/></g></svg><b>Keys</b></div></div>'''),
 ("그루브는 외우는 게 아니라", "Groove isn't something you memorize,",
  f'''<svg viewBox="0 0 900 520" class="ill"><g stroke="{INK}" stroke-width="7" fill="none" stroke-linecap="round">
   <rect x="300" y="80" width="300" height="380" rx="10" fill="#FFFDF7"/>{''.join(f'<path d="M340 {150+i*56} H 560"/>' for i in range(5))}
   <path id="x1" d="M260 60 L 640 480" stroke="#C0392B" stroke-width="12" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/>
   <path id="x2" d="M640 60 L 260 480" stroke="#C0392B" stroke-width="12" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></g></svg>'''),
 ("몸에 쌓이는 것.", "it builds up in you.",
  f'''<div class="row"><div id="c10">{ch("happy", "up", 420, 460)}</div></div><svg viewBox="0 0 900 200" class="ns" ><g id="n10">{NOTE(160,150)}{NOTE(300,90,.9)}{NOTE(620,110,1.1)}{NOTE(760,160,.9)}</g></svg>'''),
]
T = [0, 1.9, 3.8, 5.9, 7.9, 9.8, 11.6, 13.5, 15.4, 17.0, 19.01]
DUR = 19

secs = ''.join(f'<section class="sc" id="s{i+1}"><div class="stage">{ill}</div><div class="cap"><b id="k{i+1}">{ko}</b><span id="e{i+1}">{en}</span></div></section>' for i, (ko, en, ill) in enumerate(SC))

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>릴스 그루브</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;background:#F1EDE4;color:#111;font-family:P,sans-serif;word-break:keep-all;position:relative}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
.hd{{position:absolute;left:84px;right:84px;top:180px;display:flex;justify-content:space-between;font-size:22px;padding-bottom:16px;border-bottom:2px solid #111}}
.tt{{position:absolute;left:0;right:0;top:270px;text-align:center;font-size:96px;font-weight:700;letter-spacing:-4px;line-height:1.16}}
.tt mark{{background:linear-gradient(transparent 58%,#F1E8CB 58%);color:inherit;padding:0 6px}}
.st{{position:absolute;left:0;right:0;top:500px;text-align:center;font-size:28px;color:#8A8A8A}}
.sc{{position:absolute;left:0;right:0;top:600px;height:1000px;opacity:0}}
.stage{{position:absolute;left:0;right:0;top:40px;height:640px;display:flex;align-items:center;justify-content:center}}
.ill{{width:900px;height:auto;max-height:600px;overflow:visible}}
.row{{display:flex;align-items:center;gap:30px}}
.cap{{position:absolute;left:60px;right:60px;top:720px;text-align:center}}
.cap b{{display:block;font-size:56px;font-weight:700;letter-spacing:-2px}}
.cap span{{display:block;margin-top:16px;font-size:28px;color:#8A8A8A}}
.beats{{display:flex;gap:40px}}
.beats i{{width:170px;height:170px;border:7px solid #111;border-radius:50%;display:flex;align-items:center;justify-content:center;font-style:normal;font-size:64px;font-weight:700;background:#FFFDF7}}
.bars{{display:flex;align-items:flex-end;gap:50px;height:420px}}
.bar{{width:140px;height:0;background:#111;position:relative}}
.bar b{{position:absolute;left:0;right:0;top:-64px;text-align:center;font-size:40px;font-weight:700}}
.icons{{display:flex;gap:44px}}
.ic{{width:250px;height:250px;border:7px solid #111;border-radius:50%;background:#F1E8CB;display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0}}
.ic svg{{width:150px;height:150px}}
.ic b{{font-size:26px;font-weight:700;margin-top:-8px}}
.ns{{position:absolute;left:90px;top:-10px;width:900px;overflow:visible}}
.ft{{position:absolute;left:84px;right:84px;top:1650px;display:flex;justify-content:space-between;font-size:22px;color:#8A8A8A;padding-top:16px;border-top:1px solid #C9C3B8}}
</style></head><body>
<div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>PRACTICE NOTE</span></div>
<div class="tt">자연스러운<br><mark>그루브</mark> 내는 법</div>
<div class="st">How to find a natural groove</div>
{secs}
<div class="ft"><span>에녹실용음악학원 시흥점</span><span class="mono">031 315 3666</span></div>
<script>
const T={T};
const $=id=>document.getElementById(id);
const cl=x=>Math.max(0,Math.min(1,x));
const ease=x=>1-Math.pow(1-cl(x),3);
const back=x=>{{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);}};
function up(el,p,dy=30){{if(!el)return;el.style.opacity=ease(p);el.style.transform=`translateY(${{(1-ease(p))*dy}}px)`;}}
function pop(el,p,extra=""){{if(!el)return;el.style.opacity=cl(p*3);el.style.transform=`scale(${{0.3+0.7*back(p)}}) ${{extra}}`;}}
window.setT=function(t){{
  for(let i=0;i<10;i++){{const s=$('s'+(i+1));const a=T[i],b=T[i+1];const on=t>=a&&t<b;s.style.opacity=on?1:0;
    const u=t-a; up($('k'+(i+1)),u/0.35,24); up($('e'+(i+1)),(u-0.12)/0.35,16);}}
  let u;
  u=t-T[0]; $('arm').style.transform=`rotate(${{Math.sin(u*Math.PI*2*1.05)*24}}deg)`;
  u=t-T[1]; pop($('c2'),u/0.5);
  u=t-T[2]; $('wave').style.strokeDashoffset=1-ease((u-0.3)/1.2); $('flat').style.opacity=1-ease((u-0.3)/1.2)*0.7;
  u=t-T[3]; pop($('c4'),u/0.5,`translateY(${{-Math.abs(Math.sin(u*6))*30}}px) rotate(${{Math.sin(u*6)*5}}deg)`); $('n4').style.transform=`translateY(${{-u*30}}px)`; $('n4').style.opacity=cl(u*2);
  u=t-T[4]; $('n5').style.opacity=cl((u-0.2)*2); $('n5').style.transform=`translateY(${{-u*40}}px)`;
  u=t-T[5]; for(let k=1;k<=4;k++){{const e=$('b'+k);const ph=(u*2.2)%4;const on=Math.floor(ph)===k-1&&u>0.2;e.style.background=on?'#F1E8CB':'#FFFDF7';e.style.transform=`scale(${{on?1.15:1}})`;}}
  u=t-T[6]; for(let k=1;k<=4;k++){{const e=$('h'+k);e.style.height=(+e.dataset.h*ease((u-0.15*k)/0.5))+'px';}}
  u=t-T[7]; for(let k=1;k<=3;k++) pop($('i'+k),(u-0.1-0.35*(k-1))/0.45);
  u=t-T[8]; $('x1').style.strokeDashoffset=1-ease((u-0.4)/0.35); $('x2').style.strokeDashoffset=1-ease((u-0.7)/0.35);
  u=t-T[9]; pop($('c10'),u/0.5,`translateY(${{-Math.abs(Math.sin(u*5))*36}}px)`); $('n10').style.opacity=cl((u-0.3)*2); $('n10').style.transform=`translateY(${{-u*30}}px)`;
}};
setT(0);
</script></body></html>
'''
open(os.path.join(HERE, 'reel.html'), 'w', encoding='utf-8').write(html)
print('reel.html', DUR, 's')
