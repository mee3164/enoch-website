# ENOCH 릴스 엔진 (키네틱 타이포 + 보조 일러스트) — 1080×1920
# 설명형 릴스를 만들 때 쓰는 ENOCH 고유 구성:
#   훅 카드(검정, 큰 제목) → 장면마다 왼쪽 정렬 큰 문장이 줄 단위로 올라옴 → 일러스트는 오른쪽 아래 보조
#   → 화면 아래 '박 줄'(점 하나가 4박을 계속 오감)이 영상 내내 흐름 → 마지막 검정 카드(ENOCH 고스트 + 연락처)
# 형광펜 · 가운데 고정 제목 · 한/영 2단 자막은 쓰지 않는다.
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'output', '디어에녹_01_무대떨림'))
from mascot import mascot  # noqa: E402

INK = '#111'


def ch(face, arms, w=420, h=460, sweat=False, ink=INK):
    return f'<svg viewBox="-170 -280 340 420" width="{w}" height="{h}" style="overflow:visible">{mascot(0, 0, 1.0, face=face, arms=arms, sweat=sweat, ink=ink)}</svg>'


def note(x, y, s=1, ink=INK):
    return f'<g transform="translate({x},{y}) scale({s})" stroke="{ink}" stroke-width="5" fill="none" stroke-linecap="round"><ellipse cx="0" cy="0" rx="14" ry="10" transform="rotate(-20)" fill="{ink}"/><path d="M12 -4 V -58 q 18 6 22 22"/></g>'


def lines(text):
    # 타이핑: 글자마다 span.c (공백 포함), 줄은 .ln
    return ''.join('<span class="ln">' + ''.join(f'<i class="c">{c}</i>' for c in l) + '</span>' for l in text.split('<br>'))


def build(path, hook, scenes, end, dur, topic='PRACTICE NOTE'):
    """hook: (작은 라벨, 제목 HTML) / scenes: [(문장, 일러스트 HTML, JS(u), 'iv'|'bk', 길이초)] / end: 마지막 문장"""
    T = [0.0, 2.4]
    for sc in scenes:
        T.append(round(T[-1] + sc[4], 2))
    T.append(dur + 0.01)
    n = len(scenes)
    secs = [f'<section class="sc bk" id="s0"><div class="lab mono">{hook[0]}</div><div class="big">{lines(hook[1])}</div><div class="cue mono">ENOCH MUSIC ACADEMY</div></section>']
    for i, (txt, ill, _js, bg, _d) in enumerate(scenes, 1):
        secs.append(f'<section class="sc {bg}" id="s{i}"><div class="cnt mono"><b>{i:02d}</b> / {n:02d}<span>{topic}</span></div>'
                    f'<div class="txt">{lines(txt)}</div><div class="ill" id="ill{i}">{ill}</div></section>')
    secs.append(f'<section class="sc bk" id="s{n+1}"><div class="ghost">ENOCH</div><div class="txt end">{lines(end)}</div>'
                f'<div class="info"><span>에녹실용음악학원 시흥점</span><span class="mono">031 315 3666</span></div></section>')
    js = '\n'.join(f'  u=t-T[{i}]; {sc[2]}' for i, sc in enumerate(scenes, 1))
    html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>reel</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;font-family:P,sans-serif;word-break:keep-all;position:relative;background:#F1EDE4}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
.sc{{position:absolute;inset:0;opacity:0}}
.iv{{background:#F1EDE4;color:#111}}
.bk{{background:#111;color:#F1EDE4}}
.ln{{display:block;padding-bottom:6px;white-space:pre-wrap}}
.c{{font-style:normal;opacity:0}}
.c.on{{opacity:1}}
.c.last::after{{content:'';display:inline-block;width:.08em;height:.9em;background:currentColor;margin-left:.06em;vertical-align:-.08em;opacity:var(--blink,1)}}
#s0 .lab{{position:absolute;left:84px;top:300px;font-size:24px;color:#9A958C}}
#s0 .big{{position:absolute;left:80px;right:60px;top:380px;font-size:132px;font-weight:700;letter-spacing:-6px;line-height:1.08}}
#s0 .cue{{position:absolute;left:84px;bottom:300px;font-size:22px;color:#9A958C}}
.cnt{{position:absolute;left:84px;right:84px;top:250px;font-size:24px;display:flex;gap:6px;align-items:baseline;padding-bottom:18px;border-bottom:1.5px solid currentColor}}
.cnt b{{font-size:24px;font-weight:600}}
.cnt span{{margin-left:auto;opacity:.6}}
.txt{{position:absolute;left:80px;right:80px;top:350px;font-size:92px;font-weight:700;letter-spacing:-4px;line-height:1.14}}
.ill{{position:absolute;right:84px;top:880px;width:640px;height:600px;display:flex;align-items:flex-end;justify-content:flex-end}}
.ill svg{{overflow:visible}}
.bk .ill{{filter:invert(.93)}}
.beat{{position:absolute;left:84px;right:84px;top:1560px;height:40px;z-index:5}}
.beat i{{position:absolute;top:18px;width:4px;height:4px}}
.beat .ln0{{position:absolute;left:0;right:0;top:19px;height:2px;background:currentColor;opacity:.25}}
.beat .tk{{position:absolute;top:8px;width:2px;height:24px;background:currentColor;opacity:.5}}
.beat .dot{{position:absolute;top:6px;width:28px;height:28px;margin-left:-14px;border-radius:50%;background:currentColor}}
.ghost{{position:absolute;left:60px;top:250px;font-size:250px;font-weight:700;letter-spacing:-10px;color:#262421}}
.txt.end{{top:620px;font-size:86px}}
.info{{position:absolute;left:84px;right:84px;top:1240px;display:flex;justify-content:space-between;font-size:24px;color:#B9B4AA;padding-top:18px;border-top:1px solid #444}}
</style></head><body>
{''.join(secs)}
<div class="beat" id="beat"><div class="ln0"></div>{''.join(f'<div class="tk" style="left:{k*33.33:.2f}%"></div>' for k in range(4))}<div class="dot" id="bd"></div></div>
<script>
const T={T};
const $=id=>document.getElementById(id);
const cl=x=>Math.max(0,Math.min(1,x));
const ease=x=>1-Math.pow(1-cl(x),3);
const back=x=>{{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);}};
function pop(el,p,extra=""){{if(!el)return;el.style.opacity=cl(p*3);el.style.transform=`scale(${{0.3+0.7*back(p)}}) ${{extra}}`;}}
function rise(sec,u,d){{const cs=sec.querySelectorAll('.c');const n=cs.length;const span=Math.max(0.8,Math.min(1.5,d*0.62));const shown=Math.floor(cl((u-0.12)/span)*n+(u>0.12?1:0));
  cs.forEach((c,k)=>{{c.classList.toggle('on',k<shown);c.classList.toggle('last',k===Math.min(shown,n)-1);}});
  sec.style.setProperty('--blink',(shown>=n&&Math.floor(u*2.5)%2)?0:1);}}
const N={n};
window.setT=function(t){{
  let cur=0; for(let i=0;i<=N+1;i++){{const s=$('s'+i);const on=t>=T[i]&&t<T[i+1];s.style.opacity=on?1:0;if(on){{cur=i;rise(s,t-T[i],T[i+1]-T[i]);}}}}
  const bt=$('beat'); bt.style.display=(cur===0||cur===N+1)?'none':'block';
  bt.style.color=$('s'+cur).classList.contains('bk')?'#F1EDE4':'#111';
  const bp=(t*2)%4; const k=Math.floor(bp), f=bp-k; $('bd').style.left=(Math.min(k+ease(f/0.35),3)*33.33)+'%';
  $('bd').style.transform=`scale(${{1+0.35*Math.max(0,1-f*5)}})`;
  for(let i=1;i<=N;i++){{const il=$('ill'+i); il.style.opacity=cl((t-T[i]-0.25)*3);}}
  let u;
{js}
}};
setT(0);
</script></body></html>
'''
    open(path, 'w', encoding='utf-8').write(html)
    return T
