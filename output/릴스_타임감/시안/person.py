# 시안 P: 가는 펜 선 인물 일러스트(가상 인물, 이름 없음)가 드럼을 치는 장면 — 시안 A와 같은 두 장면
# python3 output/릴스_타임감/시안/person.py → P.html → node render.mjs P.html 6 시안P_인물.mp4
import os
from build import BASE, JSBASE, SC, BEATS, GOOD, BAD, head, HERE

INK = '#232323'
PAPER = '#FFFDF7'


def tube(d, w):
    # 테두리 있는 팔·다리: 두꺼운 잉크 선 위에 종이색 선
    return f'<path d="{d}" stroke="{INK}" stroke-width="{w+7}" fill="none" stroke-linecap="round"/><path d="{d}" stroke="{PAPER}" stroke-width="{w}" fill="none" stroke-linecap="round"/>'


def arm(side):
    s = side
    # 어깨(±104,-128) → 팔꿈치(±150,-20) → 손(±112,44), 스틱은 손에서 드럼 가운데로
    upper = tube(f'M{s*104} -128 C {s*132} -96, {s*148} -60, {s*150} -20', 34)
    sleeve = (f'<path d="M{s*80} -150 C {s*110} -152, {s*136} -132, {s*162} -82 L {s*126} -66 C {s*118} -88, {s*106} -108, {s*92} -116 Z" fill="{PAPER}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
              f'<path d="M{s*128} -112 q {s*8} 8 {s*10} 22" stroke="{INK}" stroke-width="2.5" fill="none"/>')
    fore = (tube(f'M{s*150} -20 C {s*146} 6, {s*132} 28, {s*114} 42', 28)
            + f'<path d="M{s*112} 42 L {s*20} 92" stroke="{INK}" stroke-width="8" stroke-linecap="round"/><path d="M{s*112} 42 L {s*30} 87" stroke="{PAPER}" stroke-width="3" stroke-linecap="round"/>'
            + f'<path d="M{s*98} 30 c {s*-6} 14, {s*0} 30, {s*16} 30 c {s*16} 0, {s*22} -14, {s*16} -28 c {s*-6} -10, {s*-26} -14, {s*-32} -2 z" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>'
            + f'<path d="M{s*104} 40 h {s*18} M {s*104} 48 h {s*16}" stroke="{INK}" stroke-width="2.5"/>')
    sd = 'L' if side < 0 else 'R'
    return (f'<g class="up{sd}" data-cx="{s*104}" data-cy="-128">{upper}'
            f'<g class="fo{sd}" data-cx="{s*150}" data-cy="-20">{fore}</g>{sleeve}</g>')


HAIR = (f'<path d="M-68 -258 C -82 -318, -44 -362, 6 -360 C 52 -364, 86 -330, 72 -262 C 66 -286, 52 -300, 40 -302 '
        f'C 30 -290, 6 -284, -14 -290 C -30 -296, -46 -300, -56 -292 C -62 -284, -66 -272, -68 -258 Z" fill="{PAPER}" stroke="{INK}" stroke-width="4" stroke-linejoin="round"/>'
        + ''.join(f'<path d="{d}" stroke="{INK}" stroke-width="2.5" fill="none" stroke-linecap="round"/>' for d in [
            'M-40 -340 C -30 -320, -30 -306, -40 -296', 'M-10 -352 C -2 -330, -4 -306, -16 -292', 'M24 -350 C 30 -330, 32 -312, 26 -298',
            'M52 -336 C 58 -318, 60 -300, 54 -290', 'M-60 -316 C -50 -306, -52 -290, -60 -280'])
        )
FACE = {
    'ok': (f'<path d="M-36 -248 q 12 -10 24 0 M 14 -248 q 12 -10 24 0" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
           f'<path d="M-36 -268 q 12 -6 22 -2 M 16 -270 q 10 -4 22 2" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>'
           f'<path d="M2 -236 q -6 18 2 22" stroke="{INK}" stroke-width="2.5" fill="none"/>'
           f'<path d="M-16 -200 Q 2 -184 20 -202" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'),
    'ng': (f'<circle cx="-24" cy="-246" r="4.5" fill="{INK}"/><circle cx="26" cy="-246" r="4.5" fill="{INK}"/>'
           f'<path d="M-38 -268 q 10 -8 24 -12 M 14 -280 q 14 4 24 12" stroke="{INK}" stroke-width="3" fill="none" stroke-linecap="round"/>'
           f'<path d="M2 -236 q -6 18 2 22" stroke="{INK}" stroke-width="2.5" fill="none"/>'
           f'<path d="M-14 -196 q 6 -8 12 0 t 12 0 t 10 -2" stroke="{INK}" stroke-width="3.5" fill="none" stroke-linecap="round"/>'
           f'<path d="M84 -284 c -10 14 -10 24 0 26 c 10 -2 10 -12 0 -26 z M 104 -250 c -7 10 -7 17 0 19 c 7 -2 7 -9 0 -19 z" fill="#D9E1E8" stroke="{INK}" stroke-width="3"/>'),
}


def person(mood):
    return f'''<g stroke-linejoin="round">
 <path d="M-22 -190 L -26 -150 M 22 -190 L 26 -150" stroke="{INK}" stroke-width="4"/>
 <path d="M-26 -160 C -60 -156, -92 -146, -104 -128 C -112 -90, -104 -40, -110 0 C -114 30, -116 50, -118 70 L 118 70 C 116 50, 114 30, 110 0 C 104 -40, 112 -90, 104 -128 C 92 -146, 60 -156, 26 -160 Z" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>
 <path d="M-26 -160 Q 0 -134 26 -160" fill="none" stroke="{INK}" stroke-width="4"/>
 <path d="M-60 -100 q 10 40 4 80 M 54 -90 q -6 30 2 70 M -20 -40 q 20 10 40 0" fill="none" stroke="{INK}" stroke-width="2.5" stroke-linecap="round"/>
 <ellipse cx="0" cy="-244" rx="60" ry="72" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>
 <path d="M-60 -250 c -16 -4 -18 22 -2 28 M 60 -250 c 16 -4 18 22 2 28" fill="{PAPER}" stroke="{INK}" stroke-width="4"/>
 {HAIR}{FACE[mood]}
 {arm(-1)}{arm(1)}
</g>'''


DRUM = f'''<g stroke="{INK}" stroke-linejoin="round" stroke-linecap="round">
 <path d="M-96 210 C -100 260, -104 300, -108 330 M 96 210 C 100 260, 104 300, 108 330" stroke-width="30" fill="none"/>
 <path d="M-96 210 C -100 260, -104 300, -108 330 M 96 210 C 100 260, 104 300, 108 330" stroke="{PAPER}" stroke-width="23" fill="none"/>
 <path d="M-92 236 C -94 270, -96 300, -98 322 M 92 236 C 94 270, 96 300, 98 322" stroke-width="2" fill="none"/>
 <path d="M-146 342 c -4 -20, 30 -26, 64 -16 c 8 4, 8 12, 4 18 h -66 z M 82 344 c -4 -6, -4 -14, 4 -18 c 34 -10, 68 -4, 64 16 z" fill="{PAPER}" stroke-width="4"/>
 <path d="M-170 96 V 196 C -170 236, 170 236, 170 196 V 96" fill="{PAPER}" stroke-width="5"/>
 <ellipse cx="0" cy="96" rx="170" ry="34" fill="{PAPER}" stroke-width="5"/>
 <ellipse cx="0" cy="96" rx="156" ry="27" fill="none" stroke-width="2"/>
 {''.join(f'<path d="M{x} 128 V {204 + (4 if abs(x) < 100 else -6)}" stroke-width="2.5" fill="none"/>' for x in (-120, -60, 0, 60, 120))}
 <path d="M-170 130 C -100 152, 100 152, 170 130 M -170 186 C -100 210, 100 210, 170 186" stroke-width="2.5" fill="none"/>
 <path d="M-120 228 L -160 340 M 120 228 L 160 340 M 0 236 L 0 340" stroke-width="4" fill="none"/>
</g>'''


def scene(i, sid, txt, mood):
    notes = ''.join(f'<g class="nt" opacity="0"><g transform="scale(1.2)" stroke="{INK}" stroke-width="4.5" fill="none" stroke-linecap="round"><ellipse cx="0" cy="0" rx="14" ry="10" transform="rotate(-20)" fill="{INK}"/><path d="M12 -4 V -58 q 18 6 22 22"/></g></g>' for _ in range(4))
    return f'''<section class="sc" id="{sid}">{head(i)}
<div class="txt">{''.join('<span class="ln">' + ''.join(f'<i class="c">{c}</i>' for c in l) + '</span>' for l in txt.split('<br>'))}</div>
<svg class="ill" viewBox="0 0 1080 1920" width="1080" height="1920">
 <g filter="url(#rough)">
  <path d="M230 1110 C 210 900, 420 800, 600 830 C 820 860, 920 980, 900 1170 C 880 1350, 700 1420, 520 1400 C 330 1380, 248 1270, 230 1110 Z" fill="#DCE2D3"/>
  <g class="notes">{notes}</g>
  <g transform="translate(540,1080) scale(1.15)"><g class="body">{person(mood)}{DRUM}
   <g class="burst" stroke="{INK}" stroke-width="4" stroke-linecap="round" opacity="0"><path d="M-50 56 l -22 -24 M 0 48 l 0 -32 M 50 56 l 22 -24"/></g></g></g>
  <g stroke="{INK}" stroke-linecap="round">
   <path d="M84 1600 C 300 1597, 700 1603, 996 1600" stroke-width="3" opacity=".35" fill="none"/>
   {''.join(f'<circle cx="{84 + 912*(k+0.5)/4:.0f}" cy="1600" r="30" fill="#DCE2D3" stroke="none"/>' for k in range(4))}
   {''.join(f'<circle class="hit" cx="0" cy="1600" r="13" fill="{INK}" stroke="none" opacity="0"/>' for _ in range(4))}
  </g>
 </g>
</svg></section>'''


html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>P</title><style>{BASE}
.txt{{position:absolute;left:80px;right:80px;top:350px;font-size:92px;font-weight:700;letter-spacing:-4px;line-height:1.14}}
.ln{{display:block;padding-bottom:6px;white-space:pre-wrap}}
.c{{font-style:normal;opacity:0}} .c.on{{opacity:1}}
.ill{{position:absolute;left:0;top:0}}
.lab{{position:absolute;left:84px;top:1660px;right:84px;display:flex;justify-content:space-between;font-size:20px;color:#9A958C}}
</style></head><body>
<svg width="0" height="0" style="position:absolute"><filter id="rough" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence id="turb" type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="1"/><feDisplacementMap in="SourceGraphic" scale="3.5"/></filter></svg>
{scene(2, 'sA', '누가 치면<br>듣기 좋고', 'ok')}
{scene(3, 'sB', '누가 치면<br>어딘가 불안합니다', 'ng')}
<div class="lab mono"><span>BEAT</span><span>● HIT</span></div>
<script>{JSBASE}
const SC={SC}, HITS={{sA:{GOOD},sB:{BAD}}};
const LAND={{sA:[[170,800,0],[280,800,0],[390,800,0],[500,800,0]],sB:[[180,840,-28],[330,750,22],[800,800,-40],[900,1010,64]]}};
function type(sec,u){{const cs=sec.querySelectorAll('.c');const n=cs.length;const sh=Math.floor(cl((u-0.05)/0.75)*n)+(u>0.05?1:0);cs.forEach((c,k)=>c.classList.toggle('on',k<sh));}}
function rot(el,a){{el.setAttribute('transform',`rotate(${{a}} ${{el.dataset.cx}} ${{el.dataset.cy}})`);}}
window.setT=function(t){{
  $('turb').setAttribute('seed', 1+Math.floor(t*8)%3);
  ['sA','sB'].forEach((id,si)=>{{
    const s=$(id), u=t-si*SC, on=u>=0&&u<SC; s.style.opacity=on?1:0; if(!on)return;
    type(s,u);
    const hits=HITS[id], bad=id==='sB';
    ['L','R'].forEach((sd,j)=>{{
      let a=1; hits.forEach((h,k)=>{{ if(k%2===j) a=Math.min(a, Math.abs(u-h)/0.2); }});
      const up=cl(a), sg=sd==='L'?-1:1;
      rot(s.querySelector('.up'+sd), sg*-10*up);      // 위팔은 살짝
      rot(s.querySelector('.fo'+sd), sg*55*up);        // 손목·아래팔이 스틱을 들어 올림
    }});
    let bob=0; hits.forEach(h=>{{const d=u-h; if(d>=0&&d<0.25) bob=Math.max(bob,(1-d/0.25));}});
    const shake=bad?Math.sin(u*47)*4*cl(u-0.3):0;
    s.querySelector('.body').setAttribute('transform',`translate(${{shake}},${{bob*6}}) rotate(${{bad?Math.sin(u*31)*1.2:0}})`);
    let bz=0; hits.forEach(h=>{{const d=u-h; if(d>=0&&d<0.16) bz=1;}});
    s.querySelector('.burst').setAttribute('opacity',bz);
    s.querySelectorAll('.nt').forEach((n,k)=>{{
      const d=u-hits[k]; if(d<0){{n.setAttribute('opacity',0);return;}}
      const p=ease(d/0.45), [lx,ly,lr]=LAND[id][k], x0=540, y0=1160;
      let x=x0+(lx-x0)*p, y=y0+(ly-y0)*p-Math.sin(p*Math.PI)*120, r=lr*p;
      if(bad&&k===3&&d>0.5){{const f=d-0.5; y+=f*f*900; r+=f*200;}}
      n.setAttribute('opacity',cl(d*8)); n.setAttribute('transform',`translate(${{x}},${{y}}) rotate(${{r}})`);
    }});
    s.querySelectorAll('.hit').forEach((c,k)=>{{
      const h=hits[k], x=84+912*((h-0.5)/0.5+0.5)/4; const d=u-h;
      c.setAttribute('cx',x); c.setAttribute('opacity',d>=0?1:0); c.setAttribute('r',13+10*Math.max(0,1-d*6));
    }});
  }});
}};
setT(0);
</script></body></html>'''
open(os.path.join(HERE, 'P.html'), 'w', encoding='utf-8').write(html)
print('P.html')
