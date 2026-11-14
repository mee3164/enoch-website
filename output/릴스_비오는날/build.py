# 릴스 "비 오는 날의 연습" — 브이로그형: 글 사이에 실제 사진이 가운데서 열리는 구성 (카드뉴스와 같은 순서) (아이보리 · 블랙 · Pretendard)
# python3 output/릴스_비오는날/build.py → reel.html → CHROMIUM_PATH=... node output/릴스_비오는날/render.mjs
import os
HERE = os.path.dirname(os.path.abspath(__file__))

# 화면: (글 조각들 [(html, x, y)], 사진들 [(파일, x, y, w, h, 초점)])
SCREENS = [
    ([('우산 하나에 텀블러 챙겨서,', 120, 560), ('연습실 가는 길.', 120, 1320)],
     [('coffee', 300, 700, 480, 540, '22% 50%')]),
    ([('습도가 높은 날은', 120, 600), ('목이 덜<br>건조합니다', 600, 1080)],
     [('rain', 140, 740, 380, 480, '50% 35%')]),
    ([('빗소리는<br>일정해서', 120, 640), ('다른 소음이<br>덜 들려요', 400, 1070)],
     [('guitarroom', 560, 600, 380, 400, '55% 50%')]),
    ([('텀블러 속 커피가<br>반쯤 줄어드는 동안', 120, 560), ('같은 소절을<br>몇 번 더.', 120, 1300)],
     [('rack', 500, 780, 440, 440, '50% 70%')]),
    ([('오늘은 내 소리가', 120, 520), ('조금 더 잘<br>들리는 날.', 120, 1100)],
     [('stage', 460, 660, 500, 520, '50% 40%')]),
]
D_TITLE, D_SC, D_END = 2.0, 2.5, 2.4
DUR = round(D_TITLE + D_SC * len(SCREENS) + D_END, 2)


def bracket(x, y, w, h):
    g, t = 26, 24   # 사진과의 간격, 끝 꺾임 길이
    top, bot = y - 20, y + h + 20
    return (f'<svg class="br L" style="left:{x-g-t}px;top:{top}px" width="{t+2}" height="{bot-top}"><path d="M{t} 1 H 1 V {bot-top-1} H {t}"/></svg>'
            f'<svg class="br R" style="left:{x+w+g}px;top:{top}px" width="{t+2}" height="{bot-top}"><path d="M0 1 H {t+1} V {bot-top-1} H 0"/></svg>')


secs = ['<section class="sc" id="s0"><div class="lab mono" style="left:124px;top:700px">PRACTICE NOTE — RAINY DAY</div>'
        '<div class="title" style="left:120px;top:760px"><span class="ln">비 오는 날의</span><span class="ln">연습</span></div></section>']
n = 0
for i, (texts, photos) in enumerate(SCREENS, 1):
    h = []
    for k, (t, x, y) in enumerate(texts):
        h.append(f'<div class="tx t{k}" style="left:{x}px;top:{y}px">{t}</div>')
    for (src, x, y, w, hh, pos) in photos:
        n += 1
        h.append(f'<div class="lab mono pl" style="left:{x}px;top:{y-58}px">{n:02d}</div>')
        h.append(f'<div class="ph" style="left:{x}px;top:{y}px;width:{w}px;height:{hh}px" data-cx="{x + w/2}"><img src="src/{src}.jpg" style="object-position:{pos}"></div>')
    secs.append(f'<section class="sc" id="s{i}">{"".join(h)}</section>')
secs.append(f'<section class="sc" id="s{len(SCREENS)+1}"><div class="lab mono" style="left:124px;top:760px">ENOCH MUSIC ACADEMY</div>'
            '<div class="tx t0" style="left:120px;top:810px;font-weight:600">에녹실용음악학원 시흥점</div>'
            '<div class="tx t1 mono" style="left:124px;top:930px;font-size:34px;letter-spacing:2px">031 315 3666</div>'
            '<div class="tx t1" style="left:124px;top:1000px;font-size:30px;color:#8A8A8A;letter-spacing:-.5px">체험수업 · 네이버 플레이스 예약</div></section>')

T = [0, D_TITLE] + [round(D_TITLE + D_SC * k, 2) for k in range(1, len(SCREENS) + 1)] + [DUR + 0.01]

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>reel</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;background:#F1EDE4;color:#111;font-family:P,sans-serif;word-break:keep-all;position:relative}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
.sc{{position:absolute;inset:0;opacity:0}}
.lab{{position:absolute;font-size:22px;color:#8A8A8A}}
.title{{position:absolute;font-size:88px;font-weight:600;letter-spacing:-4px;line-height:1.1}}
.title .ln{{display:block}}
.tx{{position:absolute;font-size:56px;font-weight:400;letter-spacing:-2px;line-height:1.18;white-space:nowrap}}
.ph{{position:absolute;overflow:hidden;background:#E4DFD4}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.82) contrast(1.02)}}
.br{{position:absolute;overflow:visible}}
.br path{{fill:none;stroke:#111;stroke-width:3}}
</style></head><body>
{''.join(secs)}
<script>
const T={T};
const cl=x=>Math.max(0,Math.min(1,x)); const ease=x=>1-Math.pow(1-cl(x),3);
function rise(el,p){{el.style.opacity=ease(p);el.style.transform=`translateY(${{(1-ease(p))*18}}px)`;}}
window.setT=function(t){{
  for(let i=0;i<T.length-1;i++){{
    const s=document.getElementById('s'+i); const u=t-T[i], d=T[i+1]-T[i];
    const on=u>=0&&u<d; if(!on){{s.style.opacity=0;continue;}}
    s.style.opacity=Math.min(cl(u/0.18), cl((d-u)/0.2));
    s.querySelectorAll('.title .ln').forEach((e,k)=>rise(e,(u-0.1-k*0.25)/0.4));
    s.querySelectorAll('.lab').forEach(e=>e.style.opacity=ease((u-(i===0?0:0.45))/0.3));
    s.querySelectorAll('.tx.t0').forEach(e=>rise(e,(u-0.1)/0.35));
    s.querySelectorAll('.tx.t1').forEach(e=>rise(e,(u-0.8)/0.35));
    s.querySelectorAll('.brs').forEach((b,k)=>{{
      const p=ease((u-0.3-k*0.35)/0.4); const cx=+b.dataset.cx;
      const L=b.querySelector('.L'), R=b.querySelector('.R');
      const lx=parseFloat(L.style.left), rx=parseFloat(R.style.left);
      L.style.transform=`translateX(${{(cx-lx)*(1-p)*0.9}}px)`; R.style.transform=`translateX(${{(cx-rx)*(1-p)*0.9}}px)`;
      L.style.opacity=R.style.opacity=cl(p*3);
    }});
    s.querySelectorAll('.ph').forEach((ph,k)=>{{
      const p=ease((u-0.45-k*0.35)/0.45);
      ph.style.clipPath=`inset(0 ${{50*(1-p)}}% 0 ${{50*(1-p)}}%)`;
      ph.querySelector('img').style.transform=`scale(${{1.12-0.1*cl(u/d)}})`;
    }});
  }}
}};
setT(0);
</script></body></html>'''
open(os.path.join(HERE, 'reel.html'), 'w', encoding='utf-8').write(html)
print('reel.html', DUR, 's', T)
