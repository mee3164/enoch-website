# 릴스 "AI가 곡을 만드는 시대, 악기를 배우는 것이 더 중요한 이유" (1080×1920) — 카드뉴스 8장과 같은 글 · 같은 사진
# 글은 줄마다 차례로 올라오고, 사진은 가운데서 양옆으로 열리며 천천히 줌아웃. 마무리는 검정.
# python3 output/카드뉴스_AI시대악기/reel.py → reel.html → CHROMIUM_PATH=... node output/카드뉴스_AI시대악기/render.mjs reel.html 28.0 reel.mp4
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def a(html, top, cls='', d=0.0, left=84):
    return f'<div class="a {cls}" data-d="{d}" style="left:{left}px;top:{top}px">{html}</div>'


def ph(src, top, h, d=0.3, pos='50% 50%', extra=''):
    path = src if '/' in src else f'../../images/공간/{src}'
    return f'<div class="ph" data-d="{d}" style="left:84px;top:{top}px;width:912px;height:{h}px"><img src="{path}" style="object-position:{pos};{extra}"></div>'


HD = '<div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>PRACTICE NOTE — AI &amp; MUSIC</span></div>'

# (길이, 검정 여부, 내용)
SC = [
    (3.2, False, ph('src/main.jpg', 300, 900, 0.1, '50% 40%', 'filter:saturate(.8) sepia(.06) brightness(1.18)')
     + a('AI가 곡을 만드는 시대,', 1270, 'sub', 0.6) + a('악기를 배우는 것이<br>더 중요한 이유', 1330, 'h1', 0.9)),
    (3.6, False, a('버튼 몇 번이면<br>노래 한 곡이 완성되는 요즘.', 560, 'big', 0.1)
     + a('곡을 갖는 것은<br>결과 하나를 얻는 일이지만,', 820, 'big', 0.9)
     + a('직접 연주할 수 있게 되는 건<br><b>내가 듣는 세계가 넓어지는 일입니다.</b>', 1080, 'big', 1.7)),
    (3.8, False, a('REASON 01', 380, 'lab mono', 0.0) + a('듣는 귀가 달라집니다', 424, 'h2', 0.15)
     + ph('기타앰프_01.jpg', 560, 640, 0.4, '50% 55%')
     + a('직접 연주해 본 사람은 음악을 다르게 듣습니다.<br>좋아하던 노래를 다시 들었을 때,<br>처음 듣는 소리가 들리는 것.<br>그건 직접 해 본 사람만 얻는 귀예요.', 1260, 'p', 1.0)),
    (3.8, False, a('REASON 02', 340, 'lab mono', 0.0) + a('나만의 소리는<br>대신 정해 줄 수 없어요', 384, 'h2', 0.15)
     + ph('보컬부스_01.jpg', 600, 600, 0.4, '50% 45%')
     + a('같은 곡도 연주하는 사람마다 다르게 들립니다.<br>어디서 숨을 쉬고, 어디에 힘을 줄지.<br>그 선택이 쌓여 내 소리가 됩니다.', 1260, 'p', 1.0)),
    (3.0, False, a('REASON 03', 380, 'lab mono', 0.0) + a('대신 해 줄 수<br>없는 시간이<br>있습니다', 430, 'h0', 0.25)),
    (4.0, False, a('어제 안 되던 소절이<br>오늘은 조금 되는 날.<br>그런 날이 쌓이면<br><b>음악만큼, 나도 달라집니다.</b>', 360, 'p lg', 0.1)
     + ph('피아노방_01.jpg', 760, 560, 0.8, '50% 62%')
     + a('결과는 대신 만들어 줄 수 있어도<br>그 시간까지 대신 겪어 줄 수는 없거든요.', 1380, 'p lg', 1.8)),
    (3.0, False, a('누구나 결과를 가질 수 있는<br>시대일수록,', 760, 'big', 0.1)
     + a('<b>직접 소리를 낼 수 있는 사람의 가치는<br>더 커집니다.</b>', 920, 'big', 0.9)),
    (3.6, True, '<div class="ghost">ENOCH</div>' + a('같은 곡도, 사람마다 다르게.<br>나만의 진짜 소리를 찾는 곳.', 720, 'sig', 0.2)
     + a('에녹실용음악학원 시흥점', 1020, 'inf', 0.8) + a('031 315 3666', 1070, 'inf mono', 0.9)
     + a('경기도 시흥시 은행로 157 2층', 1120, 'inf', 1.0) + a('체험수업 · 네이버 플레이스 예약', 1170, 'inf', 1.1)),
]
T = [0.0]
for d, _, _ in SC:
    T.append(round(T[-1] + d, 2))
DUR = T[-1]
T[-1] += 0.01

secs = ''.join(f'<section class="sc{" dk" if dk else ""}" id="s{i}">{HD}{body}</section>' for i, (_, dk, body) in enumerate(SC))
html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>reel</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;background:#F1EDE4;font-family:P,sans-serif;word-break:keep-all;position:relative}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
.sc{{position:absolute;inset:0;opacity:0;background:#F1EDE4;color:#111}}
.sc.dk{{background:#111;color:#F1EDE4}}
.sc>div{{position:absolute}}
.hd{{left:84px;right:84px;top:200px;display:flex;justify-content:space-between;font-size:20px;padding-bottom:16px;border-bottom:1.5px solid currentColor}}
.lab{{font-size:22px;color:#8A8A8A}}
.sub{{font-size:38px;color:#555;letter-spacing:-1px}}
.h1{{font-size:72px;font-weight:600;letter-spacing:-3px;line-height:1.2}}
.h2{{font-size:56px;font-weight:600;letter-spacing:-2px;line-height:1.22}}
.h0{{font-size:112px;font-weight:700;letter-spacing:-4px;line-height:1.25}}
.p{{right:84px;font-size:34px;color:#333;letter-spacing:-.8px;line-height:1.6}}
.p.lg{{font-size:40px;letter-spacing:-1.2px}}
.big{{right:84px;font-size:46px;letter-spacing:-1.6px;line-height:1.45}}
.sc b{{font-weight:600}}
.ph{{overflow:hidden;background:#E4DFD4}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.8) sepia(.06)}}
.ghost{{left:60px;top:330px;font-size:270px;font-weight:700;letter-spacing:-12px;color:#262421}}
.sig{{font-size:56px;font-weight:600;letter-spacing:-2px;line-height:1.35}}
.inf{{font-size:30px;color:#B9B4AA;letter-spacing:-.5px}}
.inf.mono{{color:#F1EDE4;letter-spacing:2px}}
</style></head><body>{secs}
<script>
const T={T};
const cl=x=>Math.max(0,Math.min(1,x)); const ease=x=>1-Math.pow(1-cl(x),3);
window.setT=function(t){{
  for(let i=0;i<T.length-1;i++){{
    const s=document.getElementById('s'+i), u=t-T[i], d=T[i+1]-T[i];
    if(u<0||u>=d){{s.style.opacity=0;continue;}}
    s.style.opacity=i===0?cl((d-u)/0.25):Math.min(cl(u/0.25),cl((d-u)/0.25));
    s.querySelectorAll('.a').forEach(e=>{{const p=ease((u-(+e.dataset.d))/0.45);e.style.opacity=p;e.style.transform=`translateY(${{(1-p)*20}}px)`;}});
    s.querySelectorAll('.ph').forEach(e=>{{const p=ease((u-(+e.dataset.d))/0.6);e.style.clipPath=`inset(0 ${{50*(1-p)}}% 0 ${{50*(1-p)}}%)`;
      e.querySelector('img').style.transform=`scale(${{1.1-0.08*cl(u/d)}})`;}});
  }}
}};
setT(0);
</script></body></html>'''
open(os.path.join(HERE, 'reel.html'), 'w', encoding='utf-8').write(html)
print('reel.html', DUR, 's', T)
