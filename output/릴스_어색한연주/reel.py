# 릴스 "박도 맞고 코드도 맞는데, 왜 어딘가 어색할까" (1080×1920, 모션)
# 표지: 무대 드럼 사진(images/공간/무대드럼_02.jpg) 천천히 줌 + 아래 그라데이션 위 흰 제목
# 본문: 아이보리, 줄마다 아래에서 올라오는 글 + 제목은 왼쪽에서 밀려 나오며 드러남
# 모티프: 화면 아래 '박 막대' 4개 — 02장에서 하나가 아주 조금 어긋났다가(미세한 어색함), 마지막에 다시 맞물림
# python3 output/릴스_어색한연주/reel.py → reel.html → CHROMIUM_PATH=... node output/릴스_어색한연주/render.mjs reel.html <초> reel.mp4
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def ln(html, top, cls='p', d=0.0, left=96):
    return f'<div class="a {cls}" data-d="{d}" style="left:{left}px;top:{top}px">{html}</div>'


def head(html, top, d=0.0, cls='h'):
    return f'<div class="w {cls}" data-d="{d}" style="top:{top}px"><div class="wi">{html}</div></div>'


def items(rows, top, d0, gap=150, step=0.45):
    out = ''
    for k, t in enumerate(rows):
        out += (f'<div class="a it" data-d="{d0 + k*step}" style="left:96px;top:{top + k*gap}px">'
                f'<span class="n mono">{k+1:02d}</span><span>{t}</span></div>')
    return out


SC = [
    # (길이, 종류, 내용)
    (3.4, 'cover', ''),
    (4.2, 'iv', head('틀린 데는 없어요.', 520, 0.1) + ln('박도 정확하고,<br>코드에도 맞게 쳤습니다.', 640, 'p', 0.5)
     + ln('그런데 이상하게 곡이 덜 흐르는 느낌.', 900, 'p', 1.5) + ln('미세하게 아쉬운 연주.', 1000, 'pb', 2.1)),
    (4.4, 'iv', ln('LIKE A SENTENCE', 470, 'lab mono', 0.0) + head('연주에도 말처럼<br>문장이 있습니다', 520, 0.1)
     + ln('단어도 맞고 문법도 맞는데,<br>그 대화의 말투가 아닌 말.', 790, 'p', 0.9)
     + ln('연주도 그렇습니다.<br>맞는 문장인데, <b>그 곡의 말투가 아닐 때</b><br>어색하게 들려요.', 1000, 'p', 1.9)),
    (5.0, 'iv', ln('WHEN IT HAPPENS', 420, 'lab mono', 0.0) + head('대부분은<br>이럴 때가 많아요', 470, 0.1)
     + items(['다른 곡에서 연습한 프레이즈를<br>그대로 가져와 끼워 넣었을 때',
              '내 파트는 맞는데,<br>다른 악기와 서로 다른 말투일 때',
              '소리의 길이와 세기, 박에 들어가는 느낌이<br>그 곡의 결과 조금 다를 때'], 760, 0.8, 190, 0.7)),
    (4.2, 'iv', ln('WHY', 470, 'lab mono', 0.0) + head('늘 치던 문장만<br>나오는 이유', 520, 0.1)
     + ln('손에 익은 패턴도, 연습한 프레이즈도,<br>이론도 아는데. 막상 곡이 시작되면<br>늘 치던 것만 나옵니다.', 790, 'p', 0.8)
     + ln('아는 게 부족한 게 아니라,<br><b>꺼내 쓰는 연습이 부족했던 것.</b>', 1060, 'p', 2.0)),
    (4.2, 'iv', ln('HOW', 470, 'lab mono', 0.0) + head('문장은<br>이렇게 생깁니다', 520, 0.1)
     + ln('좋아하는 연주를 많이 듣고,<br>그대로 따라 쳐 보고,<br>실제 곡 안에서 몇 번이고 꺼내 써 보는 것.', 790, 'p', 0.8)
     + ln('하나를 오래 쓰는 쪽이 먼저 손에 붙어요.<br>그렇게 써 본 문장은 <b>고르기 전에 먼저 나옵니다.</b>', 1080, 'p', 2.0)),
    (5.0, 'iv', ln('IN THE SONG\'S VOICE', 400, 'lab mono', 0.0) + head('그 곡의 말투로<br>연주하려면', 450, 0.1)
     + items(['들어가기 전에, 곡의 분위기를<br>한 단어로 정해 보기',
              '내 악기와 다른 악기가<br>어떻게 맞물리는지 들어 보기',
              '같은 패턴을 길이 · 세기 · 박의 느낌을<br>바꿔 가며 쳐 보기'], 720, 0.7, 180, 0.6)
     + ln('많이 아는 것만큼, <b>언제 꺼내고<br>언제 비워 둘지 아는 것.</b>', 1290, 'p', 2.8)),
    (4.0, 'bk', '<div class="ghost">ENOCH</div>' + ln('맞는 연주에서,<br>어울리는 연주로.', 640, 'end', 0.2)
     + ln('연주는 고르는 일이 아니라<br><b>함께 말하는 일</b>입니다.', 870, 'p', 1.0)
     + ln('진도보다 이해를 먼저 봅니다.', 1080, 'p sm', 1.6)
     + ln('에녹실용음악학원 시흥점', 1240, 'inf', 2.0) + ln('031 315 3666', 1290, 'inf mono', 2.1)
     + ln('체험수업 · 네이버 플레이스 예약', 1340, 'inf', 2.2)),
]
T = [0.0]
for d, _, _ in SC:
    T.append(round(T[-1] + d, 2))
DUR = T[-1]
N = len(SC)

secs = []
for i, (_, kind, body) in enumerate(SC):
    if kind == 'cover':
        secs.append('<section class="sc cv" id="s0"><div class="ph"><img src="../../images/공간/무대드럼_02.jpg"></div><div class="shade"></div>'
                    '<div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>PRACTICE NOTE</span></div>'
                    + head('박도 맞고 코드도 맞는데,', 1270, 0.5, 'h cvt') + head('왜 어딘가 어색할까', 1360, 0.9, 'h cvt big') + '</section>')
    else:
        cnt = f'<div class="cnt mono"><span>{i:02d} / {N-1:02d}</span><span>PRACTICE NOTE</span></div>'
        secs.append(f'<section class="sc {kind}" id="s{i}">{cnt if kind == "iv" else ""}{body}</section>')

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>reel</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;background:#F1EDE4;font-family:P,sans-serif;word-break:keep-all;position:relative}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
.sc{{position:absolute;inset:0;opacity:0;background:#F1EDE4;color:#111}}
.sc.bk{{background:#111;color:#F1EDE4}}
.sc>div{{position:absolute}}
.ph{{inset:0;overflow:hidden}}
.ph img{{width:100%;height:100%;object-fit:cover;object-position:35% 72%;filter:saturate(.8) sepia(.08)}}
.shade{{inset:0;background:linear-gradient(180deg,rgba(17,17,17,.45) 0%,rgba(17,17,17,0) 18%,rgba(17,17,17,0) 45%,rgba(17,17,17,.82) 72%,#111 100%)}}
.hd{{left:96px;right:96px;top:200px;display:flex;justify-content:space-between;font-size:20px;color:#F1EDE4;padding-bottom:16px;border-bottom:1.5px solid rgba(241,237,228,.8)}}
.cnt{{left:96px;right:96px;top:200px;display:flex;justify-content:space-between;font-size:20px;color:#8A8A8A;padding-bottom:16px;border-bottom:1.5px solid #111}}
.w{{left:96px;right:60px;overflow:hidden}}
.wi{{display:block}}
.h .wi{{font-size:64px;font-weight:700;letter-spacing:-2.5px;line-height:1.22}}
.cvt .wi{{color:#F1EDE4;font-size:56px;font-weight:600}}
.cvt.big .wi{{font-size:84px;font-weight:700;letter-spacing:-3.5px}}
.lab{{font-size:20px;color:#8A8A8A}}
.p{{right:96px;font-size:38px;color:#333;letter-spacing:-1px;line-height:1.55}}
.bk .p{{color:#C9C4BB}}
.p b,.pb{{font-weight:700;color:#111}}
.bk .p b{{color:#F1EDE4}}
.pb{{right:96px;font-size:44px;letter-spacing:-1.5px}}
.p.sm{{font-size:30px;color:#8A8A8A}}
.it{{right:96px;display:flex;gap:28px;font-size:38px;color:#333;letter-spacing:-1px;line-height:1.45;padding-top:18px;border-top:1px solid #C9C3B8}}
.it .n{{font-size:22px;color:#8A8A8A;padding-top:12px}}
.ghost{{left:60px;top:300px;font-size:270px;font-weight:700;letter-spacing:-12px;color:#262421}}
.end{{right:96px;font-size:72px;font-weight:700;letter-spacing:-3px;line-height:1.25;color:#F1EDE4}}
.inf{{font-size:28px;color:#B9B4AA}}
.inf.mono{{color:#F1EDE4;letter-spacing:2px}}
/* 박 막대 + 진행 줄 */
#beats{{position:absolute;left:96px;right:96px;top:1640px;height:60px;z-index:5}}
#beats i{{position:absolute;bottom:0;width:10px;height:60px;margin-left:-5px;background:currentColor}}
#bar{{position:absolute;left:0;top:1880px;height:6px;background:#111;z-index:6}}
</style></head><body>{''.join(secs)}
<div id="beats">{''.join(f'<i id="b{k}" style="left:{12.5 + k*25}%"></i>' for k in range(4))}</div><div id="bar"></div>
<script>
const T={T}, DUR={DUR};
const cl=x=>Math.max(0,Math.min(1,x)); const ease=x=>1-Math.pow(1-cl(x),3);
const $=id=>document.getElementById(id);
window.setT=function(t){{
  let cur=0;
  for(let i=0;i<T.length-1;i++){{
    const s=$('s'+i), u=t-T[i], d=T[i+1]-T[i];
    if(u<0||u>=d){{s.style.opacity=0;continue;}} cur=i;
    s.style.opacity=i===0?cl((d-u)/0.3):Math.min(cl(u/0.3),cl((d-u)/0.3));
    s.querySelectorAll('.a').forEach(e=>{{const p=ease((u-(+e.dataset.d))/0.5);e.style.opacity=p;e.style.transform=`translateY(${{(1-p)*24}}px)`;}});
    s.querySelectorAll('.w').forEach(e=>{{const p=ease((u-(+e.dataset.d))/0.6);const wi=e.querySelector('.wi');wi.style.transform=`translateX(${{(1-p)*-60}}px)`;e.style.opacity=cl(p*1.5);e.style.clipPath=`inset(0 ${{(1-p)*100}}% 0 0)`;}});
    const img=s.querySelector('.ph img'); if(img) img.style.transform=`scale(${{1.14-0.1*cl(u/d)}})`;
  }}
  // 박 막대: 박(120BPM)마다 하나씩 튐. 01–03장(어색함)에서는 3번째 막대만 아주 조금 늦고 짧게, 마지막 장에서 다시 맞물림
  const bt=$('beats'); const dark=cur===0||cur===T.length-2; bt.style.color=dark?'#F1EDE4':'#111';
  bt.style.opacity=cur===0?cl((t-1.2)/0.5)*0.9:1;
  const off=(cur>=1&&cur<=3)?1:0; const k=Math.floor((t*2)%4), f=(t*2)%1;
  for(let j=0;j<4;j++){{const e=$('b'+j); const lag=(j===2&&off)?0.18:0; const ff=((t*2-lag)%1+1)%1; const on=Math.floor(((t*2-lag)%4+4)%4)===j;
    const h=on?(1-ease(ff/0.5))*1+0.25:0.25; e.style.height=(60*h)+'px'; e.style.marginLeft=(j===2&&off?-5+8:-5)+'px'; e.style.opacity=on?1:0.35;}}
  $('bar').style.width=(cl(t/DUR)*1080)+'px'; $('bar').style.background=dark?'#F1EDE4':'#111';
}};
setT(0);
</script></body></html>'''
open(os.path.join(HERE, 'reel.html'), 'w', encoding='utf-8').write(html)
print('reel.html', DUR, 's', T)
