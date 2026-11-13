# 릴스 타임감 그림체 시안 2종 — 같은 두 장면("누가 치면 듣기 좋고" / "누가 치면 어딘가 불안합니다")
#   A: 손그림 + 에녹이 연기 (흔들리는 선, 세이지 색면, 박에 맞춰 드럼)
#   C: 글자만 (단어가 박 위에 떨어짐 / 어긋남)
# python3 output/릴스_타임감/시안/build.py → A.html, C.html → node render.mjs A.html 6 A.mp4
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '디어에녹_01_무대떨림'))
from mascot import mascot  # noqa: E402

FONTS = ''.join(f'@font-face{{font-family:P;src:url(../../../templates/fonts/Pretendard-{n}.woff2);font-weight:{w}}}'
                for n, w in [('Light', 300), ('Regular', 400), ('SemiBold', 600), ('Bold', 700)])
BASE = f'''{FONTS}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;font-family:P,sans-serif;word-break:keep-all;position:relative;background:#F1EDE4;color:#111}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
.sc{{position:absolute;inset:0;opacity:0}}
.cnt{{position:absolute;left:84px;right:84px;top:250px;font-size:24px;display:flex;gap:6px;align-items:baseline;padding-bottom:18px;border-bottom:1.5px solid currentColor}}
.cnt b{{font-weight:600}} .cnt span{{margin-left:auto;opacity:.6}}'''
JSBASE = '''const $=id=>document.getElementById(id);
const cl=x=>Math.max(0,Math.min(1,x));
const ease=x=>1-Math.pow(1-cl(x),3);
const back=x=>{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);};'''
SC = 3.0              # 장면 길이
BEATS = [0.5, 1.0, 1.5, 2.0]          # 박 (120 BPM)
GOOD = BEATS
BAD = [0.41, 1.14, 1.43, 2.19]        # 어긋난 타격


def head(i):
    return f'<div class="cnt mono"><b>{i:02d}</b> / 09<span>TIMING · GROOVE</span></div>'


# ---------------------------------------------------------------- A
def build_a():
    eno_ok = mascot(0, 0, 1.0, face='happy', arms='none')
    eno_ng = mascot(0, 0, 1.0, face='nervous', arms='none', sweat=True)
    ink = '#111'

    def arm(side):
        # 어깨 기준 팔 + 스틱. side=-1 왼쪽, 1 오른쪽
        sx, sy = (-88, 10) if side < 0 else (92, 0)
        return (f'<g class="arm{"L" if side < 0 else "R"}" transform="translate({sx},{sy})"><g class="rot">'
                f'<path d="M0 0 C {side*30} 18, {side*50} 34, {side*62} 48"/>'
                f'<path d="M{side*62} 48 L {side*-8} 104" stroke-width="7"/>'
                f'<circle cx="{side*62}" cy="48" r="11" fill="#FFFDF7"/></g></g>')

    drum = (f'<g stroke="{ink}" stroke-width="6" fill="#FFFDF7" stroke-linejoin="round">'
            f'<path d="M-170 118 V 210 C -170 250, 170 250, 170 210 V 118" />'
            f'<ellipse cx="0" cy="118" rx="170" ry="36"/>'
            f'<path d="M-130 150 L -100 228 L -60 150 L -20 236 L 20 150 L 60 236 L 100 150 L 130 226" fill="none" stroke-width="4"/>'
            f'<path d="M-120 238 L -150 330 M 120 238 L 150 330 M 0 246 L 0 330" fill="none"/></g>')
    burst = f'<g class="burst" stroke="{ink}" stroke-width="5" stroke-linecap="round" opacity="0"><path d="M-40 70 l -24 -26 M 0 62 l 0 -34 M 40 70 l 24 -26"/></g>'
    notes = ''.join(f'<g class="nt" opacity="0"><g transform="scale(1.3)" stroke="{ink}" stroke-width="5" fill="none" stroke-linecap="round"><ellipse cx="0" cy="0" rx="14" ry="10" transform="rotate(-20)" fill="{ink}"/><path d="M12 -4 V -58 q 18 6 22 22"/></g></g>' for _ in range(4))

    def scene(i, sid, txt, eno, hits):
        return f'''<section class="sc" id="{sid}">{head(i)}
<div class="txt">{''.join('<span class="ln">' + ''.join(f'<i class="c">{c}</i>' for c in l) + '</span>' for l in txt.split('<br>'))}</div>
<svg class="ill" viewBox="0 0 1080 1920" width="1080" height="1920">
 <g filter="url(#rough)">
  <path class="blob" d="M250 1090 C 230 900, 420 820, 600 850 C 800 880, 900 980, 880 1160 C 860 1330, 690 1400, 520 1380 C 340 1360, 268 1250, 250 1090 Z" fill="#DCE2D3"/>
  <g class="notes">{notes}</g>
  <g class="who" transform="translate(560,1060) scale(1.45)"><g class="body">
   <g stroke="{ink}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round">{eno}</g>
   <g stroke="{ink}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round">{arm(-1)}{arm(1)}</g>
   {drum}{burst}
  </g></g>
  <g class="strip" stroke="{ink}" stroke-linecap="round">
   <path d="M84 1600 C 300 1597, 700 1603, 996 1600" stroke-width="3" opacity=".35" fill="none"/>
   {''.join(f'<circle cx="{84 + 912*(k+0.5)/4:.0f}" cy="1600" r="30" fill="#DCE2D3" stroke="none"/>' for k in range(4))}
   {''.join(f'<circle class="hit" cx="0" cy="1600" r="13" fill="{ink}" stroke="none" opacity="0"/>' for _ in range(4))}
  </g>
 </g>
</svg></section>'''

    html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>A</title><style>{BASE}
.txt{{position:absolute;left:80px;right:80px;top:350px;font-size:92px;font-weight:700;letter-spacing:-4px;line-height:1.14}}
.ln{{display:block;padding-bottom:6px;white-space:pre-wrap}}
.c{{font-style:normal;opacity:0}} .c.on{{opacity:1}}
.ill{{position:absolute;left:0;top:0}}
.lab{{position:absolute;left:84px;top:1660px;right:84px;display:flex;justify-content:space-between;font-size:20px;color:#9A958C}}
</style></head><body>
<svg width="0" height="0" style="position:absolute"><filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.025" numOctaves="2" seed="1"/><feDisplacementMap in="SourceGraphic" scale="7"/></filter></svg>
{scene(2, 'sA', '누가 치면<br>듣기 좋고', eno_ok, GOOD)}
{scene(3, 'sB', '누가 치면<br>어딘가 불안합니다', eno_ng, BAD)}
<div class="lab mono" id="lab"><span>BEAT</span><span>● HIT</span></div>
<script>{JSBASE}
const SC={SC}, BEATS={BEATS}, HITS={{sA:{GOOD},sB:{BAD}}};
// 음표가 날아가 앉는 자리: 좋은 장면은 가지런한 줄, 불안한 장면은 제멋대로
const LAND={{sA:[[190,790,0],[300,790,0],[410,790,0],[520,790,0]],sB:[[200,830,-28],[370,740,22],[510,880,-40],[860,1010,64]]}};
function type(sec,u){{const cs=sec.querySelectorAll('.c');const n=cs.length;const sh=Math.floor(cl((u-0.05)/0.75)*n)+(u>0.05?1:0);cs.forEach((c,k)=>c.classList.toggle('on',k<sh));}}
window.setT=function(t){{
  $('turb').setAttribute('seed', 1+Math.floor(t*10)%4);   // 선이 살짝 흔들리는 손그림 결
  ['sA','sB'].forEach((id,si)=>{{
    const s=$(id), u=t-si*SC, on=u>=0&&u<SC; s.style.opacity=on?1:0; if(!on)return;
    type(s,u);
    const hits=HITS[id], bad=id==='sB';
    // 팔: 타격 순간 0도, 아니면 들어 올림 (왼·오 번갈아)
    ['L','R'].forEach((sd,j)=>{{
      let a=1; hits.forEach((h,k)=>{{ if(k%2===j) a=Math.min(a, Math.abs(u-h)/0.2); }});
      const ang=(sd==='L'?1:-1)*(8+38*cl(a));
      s.querySelector('.arm'+sd+' .rot').setAttribute('transform',`rotate(${{ang}})`);
    }});
    // 몸: 좋은 장면은 박에 맞춰 끄덕, 불안한 장면은 떨림
    let bob=0; hits.forEach(h=>{{const d=u-h; if(d>=0&&d<0.25) bob=Math.max(bob,(1-d/0.25));}});
    const shake=bad?Math.sin(u*47)*5*cl(u-0.3):0;
    s.querySelector('.body').setAttribute('transform',`translate(${{shake}},${{bob*8}}) rotate(${{bad?Math.sin(u*31)*1.5:0}})`);
    // 타격 순간 튀는 선
    let bz=0; hits.forEach(h=>{{const d=u-h; if(d>=0&&d<0.16) bz=1;}});
    s.querySelector('.burst').setAttribute('opacity',bz);
    // 음표: 드럼에서 튀어나와 자리를 잡음
    s.querySelectorAll('.nt').forEach((n,k)=>{{
      const d=u-hits[k]; if(d<0){{n.setAttribute('opacity',0);return;}}
      const p=ease(d/0.45), [lx,ly,lr]=LAND[id][k], x0=560, y0=1200;
      let x=x0+(lx-x0)*p, y=y0+(ly-y0)*p-Math.sin(p*Math.PI)*120, r=lr*p;
      if(bad&&k===3&&d>0.5){{const f=d-0.5; y+=f*f*900; r+=f*200;}}        // 마지막 음은 떨어짐
      n.setAttribute('opacity',cl(d*8)); n.setAttribute('transform',`translate(${{x}},${{y}}) rotate(${{r}})`);
    }});
    // 아래 줄: 세이지 동그라미 = 박, 검은 점 = 실제로 친 순간
    s.querySelectorAll('.hit').forEach((c,k)=>{{
      const h=hits[k], x=84+912*((h-0.5)/0.5+0.5)/4; const d=u-h;
      c.setAttribute('cx',x); c.setAttribute('opacity',d>=0?1:0); c.setAttribute('r',13+10*Math.max(0,1-d*6));
    }});
  }});
}};
setT(0);
</script></body></html>'''
    open(os.path.join(HERE, 'A.html'), 'w', encoding='utf-8').write(html)


# ---------------------------------------------------------------- C
def build_c():
    def scene(i, sid, words, hits, offs):
        rows = ''.join(
            f'<div class="row" style="top:{560+k*230}px"><span class="bn mono">{k+1}</span>'
            f'<span class="w" data-x="{offs[k][0]}" data-y="{offs[k][1]}" data-r="{offs[k][2]}">{w}</span>'
            f'<span class="dv mono">{"" if hits[k]==BEATS[k] else ("+" if hits[k]>BEATS[k] else "−")+f"{abs(hits[k]-BEATS[k]):.2f}s"}</span></div>'
            for k, w in enumerate(words))
        return f'''<section class="sc" id="{sid}">{head(i)}<div class="guide"></div>{rows}</section>'''

    html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>C</title><style>{BASE}
.guide{{position:absolute;left:200px;top:520px;height:960px;width:1.5px;background:#111;opacity:.18}}
.row{{position:absolute;left:84px;right:84px;height:200px;border-bottom:1px solid rgba(17,17,17,.12)}}
.bn{{position:absolute;left:0;top:70px;font-size:26px;color:#B9B4AA}}
.bn.now{{color:#111;font-weight:600}}
.w{{position:absolute;left:116px;top:0;font-size:164px;font-weight:700;letter-spacing:-7px;line-height:1;opacity:0;transform-origin:0 80%;white-space:nowrap}}
.dv{{position:absolute;right:0;top:-34px;font-size:22px;color:#9A958C;opacity:0}}
.beat{{position:absolute;left:84px;right:84px;top:1600px;height:40px}}
.beat .ln0{{position:absolute;left:0;right:0;top:19px;height:2px;background:#111;opacity:.25}}
.beat .tk{{position:absolute;top:8px;width:2px;height:24px;background:#111;opacity:.5}}
.beat .dot{{position:absolute;top:6px;width:28px;height:28px;margin-left:-14px;border-radius:50%;background:#111}}
</style></head><body>
{scene(2, 'sA', ['누가', '치면', '듣기', '좋고'], GOOD, [(0, 0, 0)]*4)}
{scene(3, 'sB', ['누가', '치면', '어딘가', '불안합니다'], BAD, [(-26, 14, -2.5), (34, -10, 1.8), (-12, 22, -1.2), (22, 6, 2.2)])}
<div class="beat"><div class="ln0"></div>{''.join(f'<div class="tk" style="left:{(k+0.5)*25:.1f}%"></div>' for k in range(4))}<div class="dot" id="bd"></div></div>
<script>{JSBASE}
const SC={SC}, BEATS={BEATS}, HITS={{sA:{GOOD},sB:{BAD}}};
window.setT=function(t){{
  ['sA','sB'].forEach((id,si)=>{{
    const s=$(id), u=t-si*SC, on=u>=0&&u<SC; s.style.opacity=on?1:0; if(!on)return;
    const hits=HITS[id], bad=id==='sB';
    const nb=BEATS.findIndex(b=>u>=b&&u<b+0.5);
    s.querySelectorAll('.bn').forEach((b,k)=>b.classList.toggle('now',k===nb));
    s.querySelectorAll('.w').forEach((w,k)=>{{
      const d=u-hits[k]; if(d<0){{w.style.opacity=0;return;}}
      const p=cl(d/0.12), x=+w.dataset.x, y=+w.dataset.y, r=+w.dataset.r;
      const jit=bad?Math.sin(u*23+k*3)*3*cl(d-0.3):0;          // 어긋난 단어는 자리를 못 잡고 계속 흔들림
      w.style.opacity=p; w.style.transform=`translate(${{x+jit}}px,${{y+(1-p)*-60}}px) rotate(${{r}}deg) scale(${{1+0.12*(1-ease(d/0.2))}})`;
    }});
    s.querySelectorAll('.dv').forEach((v,k)=>v.style.opacity=cl((u-hits[k]-0.2)*4));
  }});
  const u=(t%SC), bp=Math.min(3.999,Math.max(0,(u-0.5)*2)); const k=Math.floor(bp), f=bp-k;
  $('bd').style.left=((k+0.5)*25)+'%'; $('bd').style.transform=`scale(${{u>=0.5&&u<2.5?1+0.4*Math.max(0,1-f*5):1}})`;
  $('bd').style.opacity=u>=0.5&&u<2.5?1:0.3;
}};
setT(0);
</script></body></html>'''
    open(os.path.join(HERE, 'C.html'), 'w', encoding='utf-8').write(html)


build_a()
build_c()
print('A.html C.html')
