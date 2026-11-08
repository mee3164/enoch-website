# 릴스 "재능보다 먼저 필요한 건, 버티는 힘" — 15초, 1080×1920, 모션 그래픽 + 에녹이 + 시설 사진
# python3 output/릴스_버티는힘/build.py  → reel.html  →  node output/릴스_버티는힘/render.mjs → reel.mp4
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '디어에녹_01_무대떨림'))
from mascot import mascot  # noqa: E402

def svg(face, arms, w=420, h=460, ink="#111"):
    return f'<svg viewBox="-170 -280 340 420" width="{w}" height="{h}">{mascot(0, 0, 1.0, face=face, arms=arms, ink=ink)}</svg>'

M = {k: svg(*v) for k, v in {"sad": ("sad", "down"), "calm": ("calm", "down"), "smile": ("smile", "wave"), "happy": ("happy", "up")}.items()}

cells = ''.join(f'<i style="--d:{i}"></i>' for i in range(28))

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;background:#F1EDE4;font-family:P,sans-serif;color:#111;word-break:keep-all}}
.sc{{position:absolute;inset:0;opacity:0}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
.hd{{position:absolute;left:84px;right:84px;top:150px;display:flex;justify-content:space-between;font-size:22px;padding-bottom:18px;border-bottom:2px solid currentColor}}
.t{{position:absolute;left:84px;right:84px;font-weight:700;letter-spacing:-2px;line-height:1.25}}
.s{{position:absolute;left:84px;right:84px;font-weight:300;font-size:40px;line-height:1.5;color:#55524D}}
.num{{position:absolute;left:84px;font-size:24px;color:#8A8A8A}}
.m{{position:absolute}}
/* 1 */
#s1{{background:#F1EDE4}}
/* 3 photo */
#s3{{background:#111;color:#F1EDE4}}
#s3 .ph{{position:absolute;inset:0;background:url(../../images/공간/피아노_02.jpg) 50% 50%/cover;filter:grayscale(.6) sepia(.15) brightness(.55)}}
#s3 .s{{color:#D9D4CA}}
.graph{{position:absolute;left:84px;right:84px;top:1240px;height:300px;border-left:2px solid currentColor;border-bottom:2px solid currentColor}}
.graph svg{{position:absolute;inset:0;overflow:visible}}
/* 4 bars */
#s4{{background:#111;color:#F1EDE4}}
#s4 .ph{{position:absolute;inset:0;background:url(../../images/공간/피아노방_02.jpg) 50% 60%/cover;filter:grayscale(.6) sepia(.15) brightness(.45)}}
.bar{{position:absolute;bottom:560px;width:220px;background:#F1EDE4}}
#b2{{background:#DDE37C}}
.bar b{{position:absolute;left:0;right:0;top:-70px;text-align:center;font-size:32px;font-weight:600}}
.bar span{{position:absolute;left:0;right:0;bottom:-64px;text-align:center;font-size:30px;font-weight:300}}
/* 5 calendar */
.cal{{position:absolute;left:84px;right:84px;top:980px;display:grid;grid-template-columns:repeat(7,1fr);gap:14px}}
.cal i{{display:block;aspect-ratio:1;border:2px solid #111;border-radius:2px;position:relative}}
.cal i::after{{content:"";position:absolute;inset:16px;background:#111;transform:scale(var(--f,0));transition:none}}
/* 6 closing */
#s6{{background:#111;color:#F1EDE4}}
#s6 .s{{color:#B9B4AA}}
.ghost{{position:absolute;left:70px;top:230px;font-weight:700;font-size:250px;letter-spacing:-8px;color:#262421}}
</style></head><body>

<section class="sc" id="s1">
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>PRACTICE NOTE</span></div>
  <div class="t" id="q1" style="top:520px;font-size:84px">“나는 재능이<br>없나 봐.”</div>
  <div class="s" id="q1s" style="top:800px">연습이 잘 안 되는 날,<br>한 번쯤 드는 생각.</div>
  <div class="m" id="m1" style="left:330px;top:1150px">{M["sad"]}</div>
</section>

<section class="sc" id="s2">
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>PRACTICE NOTE</span></div>
  <div class="t" style="top:520px;font-size:72px;font-weight:300" id="t2a">재능보다<br>먼저 필요한 건,</div>
  <div class="t" style="top:760px;font-size:150px;letter-spacing:-6px" id="t2b">버티는 힘.</div>
  <div class="m" id="m2" style="left:560px;top:1180px">{M["calm"]}</div>
</section>

<section class="sc" id="s3">
  <div class="ph" id="ph3"></div>
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>01</span></div>
  <div class="t" style="top:520px;font-size:78px" id="t3">안 보이는 구간에도,<br>쌓이고 있어요.</div>
  <div class="s" style="top:780px" id="s3s">제자리 같은 몇 달이<br>지나고 나면.</div>
  <div class="graph"><svg viewBox="0 0 912 300" preserveAspectRatio="none"><path id="line" d="M0 270 L 560 262 L 600 120 L 912 90" fill="none" stroke="#DDE37C" stroke-width="8" stroke-linecap="round" stroke-linejoin="round" pathLength="1" stroke-dasharray="1" stroke-dashoffset="1"/></svg></div>
</section>

<section class="sc" id="s4">
  <div class="ph" id="ph4"></div>
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>02</span></div>
  <div class="t" style="top:520px;font-size:78px" id="t4">비교 대신,<br>어제의 나와.</div>
  <div class="bar" id="b1" style="left:250px;height:0"><b>어제</b><span></span></div>
  <div class="bar" id="b2" style="left:610px;height:0"><b>오늘</b><span></span></div>
</section>

<section class="sc" id="s5">
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>03</span></div>
  <div class="t" style="top:470px;font-size:78px" id="t5">두 시간 가끔보다,<br>20분 매일.</div>
  <div class="s" style="top:720px" id="s5s">바쁜 날엔 “오늘은 5분만”.</div>
  <div class="cal">{cells}</div>
  <div class="m" id="m5" style="left:660px;top:1500px">{svg("smile", "wave", 300, 330)}</div>
</section>

<section class="sc" id="s6">
  <div class="ghost">ENOCH</div>
  <div class="t" style="top:640px;font-size:74px" id="t6">계속하는 사람에게,<br>다음 단계가 열립니다.</div>
  <div class="s" style="top:900px" id="s6s">지금 연습하고 있는 당신을 응원해요.</div>
  <div class="m" id="m6" style="left:330px;top:1080px">{svg("happy", "up", ink="#F1EDE4")}</div>
  <div class="mono" style="position:absolute;left:84px;right:84px;bottom:220px;display:flex;justify-content:space-between;font-size:22px;padding-top:18px;border-top:1px solid #444;color:#B9B4AA"><span>ENOCH MUSIC ACADEMY</span><span>031 315 3666</span></div>
</section>

<script>
const S=[["s1",0,2.4],["s2",2.4,4.9],["s3",4.9,7.6],["s4",7.6,10.1],["s5",10.1,12.6],["s6",12.6,15.01]];
const $=id=>document.getElementById(id);
const cl=x=>Math.max(0,Math.min(1,x));
const ease=x=>1-Math.pow(1-cl(x),3);
const back=x=>{{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);}};
function up(el,p,dy=40){{el.style.opacity=ease(p);el.style.transform=`translateY(${{(1-ease(p))*dy}}px)`;}}
function pop(el,p,extra=""){{const s=back(p);el.style.opacity=cl(p*3);el.style.transform=`scale(${{0.4+0.6*s}}) ${{extra}}`;el.style.transformOrigin="50% 100%";}}
window.setT=function(t){{
  for(const [id,a,b] of S) $(id).style.opacity=(t>=a&&t<b)?1:0;
  // 1
  up($("q1"),(t-0.15)/0.5); up($("q1s"),(t-0.6)/0.5);
  pop($("m1"),(t-0.3)/0.6, `rotate(${{Math.sin(t*5)*3}}deg)`);
  // 2
  let u=t-2.4; up($("t2a"),u/0.45);
  $("t2b").style.opacity=cl((u-0.5)/0.2); $("t2b").style.transform=`scale(${{1+0.25*(1-ease((u-0.5)/0.4))}})`; $("t2b").style.transformOrigin="0 50%";
  pop($("m2"),(u-0.9)/0.6, `translateY(${{Math.sin(u*4)*8}}px)`);
  // 3
  u=t-4.9; $("ph3").style.transform=`scale(${{1.08-0.08*cl(u/2.7)}})`;
  up($("t3"),u/0.5); up($("s3s"),(u-0.4)/0.5);
  $("line").style.strokeDashoffset=1-ease((u-0.6)/1.6);
  // 4
  u=t-7.6; $("ph4").style.transform=`scale(${{1.08-0.08*cl(u/2.5)}})`; up($("t4"),u/0.5);
  $("b1").style.height=(380*ease((u-0.5)/0.6))+"px";
  $("b2").style.height=(460*ease((u-0.9)/0.7))+"px";
  // 5
  u=t-10.1; up($("t5"),u/0.5); up($("s5s"),(u-0.35)/0.5);
  document.querySelectorAll(".cal i").forEach((c,i)=>c.style.setProperty("--f",ease((u-0.6-i*0.055)/0.18)));
  pop($("m5"),(u-1.2)/0.5, `rotate(${{Math.sin(u*6)*4}}deg)`);
  // 6
  u=t-12.6; up($("t6"),u/0.5); up($("s6s"),(u-0.4)/0.5);
  pop($("m6"),(u-0.6)/0.6, `translateY(${{-Math.abs(Math.sin(u*5))*24}}px)`);
}};
setT(0);
</script></body></html>
'''
open(os.path.join(HERE, 'reel.html'), 'w', encoding='utf-8').write(html)
print('reel.html')
