import random
from lib import *
from figs import singer, guitarist, keyboardist, bassist, drummer
random.seed(11)
def sparkles(n,x0,y0,w,h):
    s=""
    for _ in range(n):
        x=x0+random.random()*w; y=y0+random.random()*h; r=random.random()
        if r<.55: s+=f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(.9+random.random()*1.2)}" fill="{INK}"/>'
        elif r<.8:
            k=3+random.random()*3; s+=f'<path d="M{f(x-k)} {f(y)}H{f(x+k)}M{f(x)} {f(y-k)}V{f(y+k)}" stroke="{INK}" stroke-width=".8"/>'
        else:
            k=6+random.random()*6
            s+=f'<path d="M{f(x)} {f(y-k)}Q{f(x)} {f(y)} {f(x+k)} {f(y)}Q{f(x)} {f(y)} {f(x)} {f(y+k)}Q{f(x)} {f(y)} {f(x-k)} {f(y)}Q{f(x)} {f(y)} {f(x)} {f(y-k)}Z" fill="{INK}"/>'
    return s
def fig(fn,x,y,w,h,sc):
    return f'<svg class="ill" style="left:{x}px;top:{y}px" width="{w*sc:.0f}" height="{h*sc:.0f}" viewBox="0 0 {w} {h}"><g filter="url(#wob)">{fn()}</g></svg>'
spark=f'<svg class="ill" style="left:0;top:0" width="1080" height="1350">{sparkles(34,400,130,300,110)}{sparkles(10,60,120,120,60)}</svg>'
html=f'''<!doctype html><html><head><meta charset="utf-8">
<style>@font-face{{font-family:"CG";src:url(cg300.ttf);font-weight:300}}@font-face{{font-family:"CG";src:url(cg500.ttf);font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{BG};color:#111;font-family:Pretendard,"Noto Sans KR",sans-serif;position:relative;overflow:hidden}}
.top{{position:absolute;top:70px;left:70px;right:70px;display:flex;justify-content:space-between;font-family:"IBM Plex Mono",monospace;font-size:23px;letter-spacing:4px}}
.grid{{position:absolute;left:62px;top:390px;width:956px;height:630px;background-image:linear-gradient(#C9CBD4 1px,transparent 1px),linear-gradient(90deg,#C9CBD4 1px,transparent 1px);background-size:159.33px 210px;border-right:1px solid #C9CBD4;border-bottom:1px solid #C9CBD4}}
.word{{position:absolute;left:0;right:0;top:640px;text-align:center;font-family:"CG",serif;font-weight:300;font-size:150px;letter-spacing:6px;line-height:1;white-space:nowrap}}
.cats{{position:absolute;left:0;right:0;top:1104px;text-align:center;font-family:"CG",serif;font-size:36px;font-weight:500;letter-spacing:.5px}}
.ko{{position:absolute;left:0;right:0;top:1170px;text-align:center}}
.ko b{{display:block;font-size:38px;font-weight:600;margin-bottom:14px}}
.ko span{{font-size:28px;color:#444}}
svg.ill{{position:absolute;overflow:visible}}
</style></head><body>
<svg width="0" height="0" style="position:absolute">{DEFS}</svg>
<div class="top"><span>ENOCH MUSIC ACADEMY</span><span>TRUE SOUND <b>SIHEUNG</b></span></div>
<div class="grid"></div>
<div class="word">TRUE SOUND</div>
{spark}
{fig(guitarist,96,128,260,420,1.08)}
{fig(keyboardist,372,232,340,310,1.0)}
{fig(bassist,826,118,200,440,1.06)}
{fig(singer,92,758,220,340,.98)}
{fig(drummer,690,752,280,340,1.0)}
<div class="cats">Vocal · Guitar · Drum · Bass · Piano · MIDI · Composition</div>
<div class="ko"><b>나만의 진짜 소리를 찾는 곳.</b><span>일곱 과목, 입시 · 취미 · 성인 · 전문 모든 과정 1:1 레슨</span></div>
</body></html>'''
open("poster.html","w").write(html)
