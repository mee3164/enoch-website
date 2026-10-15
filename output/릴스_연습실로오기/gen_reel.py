# 릴스: 왜 집에선 연습이 안 될까? (reel.html 생성) — 사진 먼저, 짧은 컷, 18초
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
T = 20.9
def lines(txts, top, start, size, weights, color='#111', lh=1.14, gap=.1):
    out=''; y=top
    for i,t in enumerate(txts):
        out+=f'<div class="ln" style="top:{y}px;height:{int(size*lh)+8}px"><div class="li" style="font-size:{size}px;font-weight:{weights[i]};color:{color};--t:{start+gap*i:.2f}s">{t}</div></div>'
        y+=int(size*lh)
    return out
def room(x,y,title,items,start,fill):
    out=f'<div class="room dr" style="left:{x}px;top:{y}px;--t:{start-.4:.2f}s"><div class="rt">{title}</div>'
    for i,(ix,iy,w,h,label,anim) in enumerate(items):
        f = fill if label!='악기 케이스' else 'transparent'
        col = '#111' if label!='악기 케이스' else '#9A958C'
        fs = 'font-size:44px;font-weight:700;' if label=='스마트폰' else ''
        out+=f'<div class="it pop" style="left:{ix}px;top:{iy}px;width:{w}px;height:{h}px;background:{f};color:{col};--t:{start+.2*i:.2f}s"><div class="in {anim}" style="--t2:{start+.2*i+.35:.2f}s;{fs}">{label}</div></div>'
    return out+'<div class="door"></div></div>'
home=room(140,620,'집',[(30,40,330,120,'소파',''),(470,40,170,240,'침대',''),(170,250,260,190,'스마트폰','buzz'),(420,470,220,140,'악기 케이스','fade')],7.3,'#CFC9BE')

SHOTS=[('미디룸_01.jpg','MIDI','만들고','50% 40%'),('보컬부스_01.jpg','VOCAL','부르고','50% 45%'),('드럼룸_01.jpg','DRUM','두드리고','50% 55%'),('피아노_01.jpg','PIANO','연주하고','55% 50%')]
M0=9.9; STEP=1.05
mont=''
for i,(f,en,ko,pos) in enumerate(SHOTS):
    t=M0+.15+i*STEP
    t3 = f'--t3:{t+STEP-.2:.2f}s;' if i<len(SHOTS)-1 else ''
    mont+=f'<div class="shot" style="--t:{t:.2f}s;z-index:{i+1}"><img src="../../images/공간/{f}" style="object-position:{pos};--t:{t:.2f}s"></div>'
    mont+=f'<div class="lab" style="--t:{t+.15:.2f}s;{t3}z-index:{i+10}"><div class="k" style="color:#F1E8CB">{en} ROOM</div><div style="font-size:110px;font-weight:700;letter-spacing:-4px;color:#F1EDE4;margin-top:6px">{ko}</div></div>'
C0 = M0 + .15 + len(SHOTS)*STEP   # 복도
E0 = C0 + 3.0                     # 마무리

html=f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>릴스 연습실로 오는 습관</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
@property --n{{syntax:'<integer>';inherits:false;initial-value:0}}
:root{{--en:"Helvetica Neue",Helvetica,Arial,"Liberation Sans",P,sans-serif;--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1920px;overflow:hidden;background:#111;font-family:P,sans-serif;word-break:keep-all;color:#111}}
.sc{{position:absolute;inset:0;animation:wipe .55s cubic-bezier(.7,0,.2,1) var(--s) both;clip-path:inset(0 0 0 100%)}}
@keyframes wipe{{from{{clip-path:inset(0 0 0 100%)}}to{{clip-path:inset(0 0 0 0)}}}}
.a{{position:absolute;left:96px;right:96px}}
.k{{font-family:var(--mono);font-size:26px;letter-spacing:4px;text-transform:uppercase;color:#6E6A64}}
.r{{opacity:0;animation:rise .5s cubic-bezier(.2,.7,.2,1) var(--t) both}}
@keyframes rise{{from{{opacity:0;transform:translateY(40px)}}to{{opacity:1;transform:none}}}}
.ln{{position:absolute;left:96px;right:60px;overflow:hidden}}
.li{{letter-spacing:-.045em;line-height:1.14;transform:translateY(110%);animation:up .55s cubic-bezier(.2,.8,.2,1) var(--t) both;white-space:nowrap}}
@keyframes up{{to{{transform:none}}}}
.wig{{display:inline-block;animation:wig .45s ease-in-out var(--t) 3 both;transform-origin:50% 80%}}
@keyframes wig{{0%,100%{{transform:rotate(0)}}25%{{transform:rotate(-6deg)}}75%{{transform:rotate(6deg)}}}}
.under{{position:absolute;height:10px;background:#F1E8CB;transform-origin:left;transform:scaleX(0);animation:sx .5s cubic-bezier(.6,0,.2,1) var(--t) both}}
@keyframes sx{{to{{transform:scaleX(1)}}}}
.room{{position:absolute;width:800px;height:680px;border:4px solid #111}}
.dr{{clip-path:inset(0 100% 0 0);animation:draw .5s cubic-bezier(.6,0,.2,1) var(--t) both}}
@keyframes draw{{to{{clip-path:inset(-70px -10px -10px -10px)}}}}
.rt{{position:absolute;left:0;top:-58px;font-size:40px;font-weight:700}}
.it{{position:absolute;border:2.5px solid #111}}
.it .in{{width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:30px}}
.pop{{opacity:0;animation:pop .4s cubic-bezier(.2,.9,.3,1.4) var(--t) both}}
@keyframes pop{{from{{opacity:0;transform:scale(.4) rotate(-8deg)}}to{{opacity:1;transform:none}}}}
.buzz{{animation:buzz .1s linear var(--t2) 24 both}}
@keyframes buzz{{0%,100%{{transform:translateX(0)}}50%{{transform:translateX(7px)}}}}
.fade{{animation:fd 1s ease var(--t2) both}}
@keyframes fd{{to{{opacity:.3;filter:blur(1.5px)}}}}
.door{{position:absolute;right:120px;bottom:-4px;width:120px;height:4px;background:#F1EDE4}}
.num{{font-family:var(--en);font-weight:700;letter-spacing:-8px;line-height:1}}
.cnt{{animation:cnt 1.3s cubic-bezier(.2,.7,.2,1) var(--t) both;counter-reset:n var(--n)}}
.cnt:before{{content:counter(n)}}
@keyframes cnt{{from{{--n:0}}to{{--n:25}}}}
.grow{{transform-origin:left;animation:gx 1.1s cubic-bezier(.2,.7,.2,1) var(--t) both}}
@keyframes gx{{from{{transform:scaleX(.15)}}to{{transform:scaleX(1)}}}}
.src{{position:absolute;left:96px;right:96px;top:1600px;font-size:20px;color:#8A8A8A}}
.prog{{position:absolute;left:0;top:0;height:8px;background:#F1E8CB;animation:prog {T}s linear both;z-index:99}}
@keyframes prog{{from{{width:0}}to{{width:100%}}}}
.bg{{position:absolute;inset:0;overflow:hidden}}
.bg img{{width:1080px;height:1920px;object-fit:cover}}
.kb0{{animation:kb0 2.6s linear 0s both}}
@keyframes kb0{{from{{transform:scale(1.12)}}to{{transform:scale(1)}}}}
.kb{{animation:kb 3s linear {C0:.2f}s both}}
@keyframes kb{{from{{transform:scale(1.18) translateY(30px)}}to{{transform:scale(1)}}}}
.door2{{position:absolute;top:0;bottom:0;width:50%;background:#111;animation:op .8s cubic-bezier(.7,0,.2,1) {C0+.2:.2f}s both;z-index:3}}
@keyframes op{{to{{transform:translateX(var(--x))}}}}
.shot{{position:absolute;inset:0;overflow:hidden;clip-path:inset(100% 0 0 0);animation:shotin .45s cubic-bezier(.7,0,.2,1) var(--t) both}}
@keyframes shotin{{to{{clip-path:inset(0 0 0 0)}}}}
.shot img{{width:1080px;height:1920px;object-fit:cover;filter:saturate(.85) brightness(.62);animation:kb2 1.6s linear var(--t) both}}
@keyframes kb2{{from{{transform:scale(1.15)}}to{{transform:scale(1.02)}}}}
.lab{{position:absolute;left:96px;right:96px;top:1160px;opacity:0;animation:labin .4s cubic-bezier(.2,.7,.2,1) var(--t) both, labgo .2s linear var(--t3,99s) forwards}}
@keyframes labin{{from{{opacity:0;transform:translateX(-60px)}}to{{opacity:1;transform:none}}}}
@keyframes labgo{{to{{opacity:0}}}}
.ghost span{{display:inline-block;opacity:0;animation:rise .45s cubic-bezier(.2,.7,.2,1) var(--t) both}}
.shade{{position:absolute;left:0;right:0}}
@property --m{{syntax:'<integer>';inherits:false;initial-value:0}}
.cnt2{{animation:cnt2 1.1s cubic-bezier(.2,.7,.2,1) var(--t) both;counter-reset:m var(--m)}}
.cnt2:before{{content:"−" counter(m)}}
@keyframes cnt2{{from{{--m:0}}to{{--m:11}}}}
.bars{{position:absolute;left:96px;right:96px;top:1240px;height:160px;display:flex;align-items:flex-end;gap:40px}}
.bar2{{flex:1;transform-origin:bottom;animation:gy 1.1s cubic-bezier(.2,.7,.2,1) var(--t) both}}
@keyframes gy{{from{{transform:scaleY(var(--f))}}to{{transform:scaleY(var(--to))}}}}
</style></head><body>

<!-- 01 훅: 사진 위 질문 (첫 프레임부터 보임) -->
<section style="position:absolute;inset:0;z-index:1">
  <div class="bg"><img class="kb0" src="../../images/공간/보컬부스_01.jpg" style="object-position:50% 50%;filter:saturate(.8) brightness(.55)"></div>
  <div class="shade" style="top:300px;height:900px;background:linear-gradient(rgba(10,10,10,.7),rgba(10,10,10,.3))"></div>
  <div class="a k" style="top:380px;color:#F1E8CB">ENOCH Note · Practice Room</div>
  <div class="a" style="top:440px;font-size:150px;font-weight:700;letter-spacing:-7px;line-height:1.12;color:#F1EDE4">왜 집에선<br>연습이<br><span style="font-weight:300">안 될<span class="wig" style="--t:.5s">까?</span></span></div>
  <div class="under" style="left:96px;top:968px;width:560px;--t:.2s"></div>
  <div class="a r" style="top:1050px;font-size:44px;color:#F1EDE4;--t:.9s">답은, 의지가 아니라 <b style="color:#F1E8CB">장소</b>에 있어요.</div>
</section>

<!-- 02 실험 숫자 (4.5초) -->
<section class="sc" style="--s:2.4s;--d:{T-2.4}s;background:#F1EDE4;z-index:2">
  <div class="a k r" style="top:330px;--t:2.6s">An Experiment</div>
  {lines(['병원 식당에서,','생수를 잘 보이는 곳에','두었을 뿐인데'],390,2.7,76,[700,300,300])}
  <div class="a r" style="top:820px;border-top:3px solid #111;padding-top:30px;--t:3.5s"><div class="k">Water · 3 Months</div><div class="num" style="font-size:260px;margin-top:10px">+<span class="cnt" style="--t:3.7s"></span>.8<span style="font-size:120px">%</span></div><div style="font-size:40px;color:#55524D;margin-top:6px">생수 판매</div></div>
  <div class="a r" style="top:1450px;font-size:34px;color:#55524D;--t:4.4s"><span class="k">Soda</span> <span style="font-family:var(--en);font-weight:700;font-size:64px;letter-spacing:-3px;color:#111;margin-left:16px"><span class="cnt2" style="--t:4.6s"></span>.4%</span> &nbsp;탄산음료 판매</div>
  <div class="bars"><div class="bar2" style="height:160px;background:#F1E8CB;border:2.5px solid #111;--t:3.7s;--f:.2;--to:1"></div><div class="bar2" style="height:160px;background:#CFC9BE;border:2.5px solid #111;--t:4.6s;--f:1;--to:.55"></div></div>
  <div class="src" style="top:1610px">제임스 클리어, 『아주 작은 습관의 힘』 114–115쪽 (이한이 옮김, 비즈니스북스)</div>
</section>

<!-- 03 집: 스마트폰 -->
<section class="sc" style="--s:6.9s;--d:{T-6.9}s;background:#F1EDE4;z-index:3">
  {lines(['집은,','쉬는 곳이니까요'],330,7.1,84,[700,300])}
  {home}
  <div class="a r" style="top:1380px;font-size:38px;color:#55524D;--t:8.5s">소파에 기대면, 악기보다 스마트폰이 먼저 손에 잡힙니다.</div>
</section>

<!-- 04 공간 사진 몽타주 -->
<section class="sc" style="--s:{M0}s;--d:{T-M0}s;background:#111;z-index:4">
  {mont}
  <div class="shade" style="top:0;height:760px;background:linear-gradient(rgba(10,10,10,.85),rgba(10,10,10,0));z-index:15"></div>
  <div class="shade" style="top:1050px;height:500px;background:linear-gradient(rgba(10,10,10,0),rgba(10,10,10,.75) 40%,rgba(10,10,10,.75) 70%,rgba(10,10,10,0));z-index:9"></div>
  <div class="ln" style="top:330px;height:120px;z-index:20"><div class="li" style="font-size:96px;font-weight:700;color:#F1EDE4;--t:{M0+.2:.2f}s">연습실은,</div></div>
  <div class="ln" style="top:440px;height:120px;z-index:20"><div class="li" style="font-size:96px;font-weight:300;color:#F1EDE4;--t:{M0+.32:.2f}s">음악하는 곳.</div></div>
  <div class="src" style="color:#9A958C;z-index:20">사진: ENOCH 미디룸 · 보컬 부스 · 드럼룸 · 피아노</div>
</section>

<!-- 05 복도: 문 열림 -->
<section class="sc" style="--s:{C0}s;--d:{T-C0}s;background:#111;z-index:5">
  <div class="bg"><img class="kb" src="../../images/공간/복도_01.jpg" style="filter:saturate(.7) brightness(.6)"></div>
  <div class="door2" style="left:0;--x:-100%"></div><div class="door2" style="right:0;--x:100%"></div>
  {lines(['연습실 문을 여는','것까지가,','<span style="color:#F1E8CB">연습입니다.</span>'],980,C0+.7,104,[700,700,700],'#F1EDE4',1.18,.14)}
</section>

<!-- 06 마무리 -->
<section class="sc" style="--s:{E0}s;--d:{T-E0}s;background:#111;color:#F1EDE4;z-index:6">
  <div class="a ghost" style="top:330px;font-family:var(--en);font-weight:700;font-size:250px;letter-spacing:-9px;color:#2A2825;line-height:1">{''.join(f'<span style="--t:{E0+.15+.06*i:.2f}s">{c}</span>' for i,c in enumerate('ENOCH'))}</div>
  {lines(['운영시간 내','자유로운 연습실 이용이','<span style="color:#F1E8CB">가능합니다.</span>'],640,E0+.3,64,[700,700,700],'#F1EDE4',1.3,.1)}
  <div class="a r" style="top:940px;font-size:38px;line-height:1.7;color:#C9C4BB;--t:{E0+.8:.2f}s">입시 · 취미 · 성인 · 전문, 모든 과정 1:1</div>
  <div class="a r" style="top:1180px;padding-top:26px;border-top:1px solid rgba(241,237,228,.3);font-size:34px;line-height:1.7;--t:{E0+1.0:.2f}s">에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층 · 010 3949 3666</span></div>
</section>
<div class="prog"></div>
</body></html>'''
open('reel.html','w').write(html)
print(round(C0,2), round(E0,2), T)
