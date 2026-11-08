# ENOCH NOTE — 또렷한 목표: 카드뉴스 8장 (1080×1350) + 장마다 모션(5초)
# python3 output/노트_또렷한목표/build.py → cards.html
# node output/노트_또렷한목표/render.mjs      → 01.png~08.png (마지막 프레임), motion/01.mp4~08.mp4
import os
HERE = os.path.dirname(os.path.abspath(__file__))
N = 8
TITLE = '또렷한 목표'

def hd(dark=False):
    return '<div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH NOTE — CLEAR GOAL</span></div>'

def ft(i):
    return f'<div class="ft mono"><span>{TITLE}</span><span>{i:02d} / {N:02d}</span></div>'

wave = ''.join(f'<i style="height:{int(30 + 70 * abs(__import__("math").sin(k * 0.73) * __import__("math").cos(k * 0.21)))}%"></i>' for k in range(60))
wave2 = ''.join(f'<i style="height:{int(25 + 60 * abs(__import__("math").sin(k * 0.61 + 1) * __import__("math").cos(k * 0.17)))}%"></i>' for k in range(60))

rows = [("노래 잘하고 싶다", "이 곡을 원키로, 후렴까지 음정 흔들리지 않고"),
        ("기타 잘 치고 싶다", "이 곡 코드 전환을, 박자 놓치지 않고 끝까지"),
        ("드럼 빠르게 치고 싶다", "16분음표를 BPM 100에서, 고르게 1분"),
        ("피아노로 반주하고 싶다", "코드 악보만 보고, 이 노래 반주 한 바퀴")]
tbl = ''.join(f'<div class="row" data-k="{k}"><span class="a">{a}</span><span class="arr">→</span><span class="b">{b}</span></div>' for k, (a, b) in enumerate(rows))

parts = [("소리", "밝은지, 어두운지, 숨이 섞였는지"), ("음정 · 리듬", "정확해서인지, 일부러 밀고 당겨서인지"),
         ("표현", "세게 · 여리게, 끝음, 쉼"), ("기술", "고음, 빠른 패시지, 특정 주법")]
ptbl = ''.join(f'<div class="pr" data-k="{k}"><b>{a}</b><span>{b}</span></div>' for k, (a, b) in enumerate(parts))

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>ENOCH NOTE — 또렷한 목표</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;background:#F1EDE4}}
.c{{position:absolute;inset:0;background:#F1EDE4;color:#111;font-family:P,sans-serif;word-break:keep-all;display:none;overflow:hidden}}
.c.on{{display:block}}
.dark{{background:#111;color:#F1EDE4}}
.sage{{background:#DCE2D3}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace}}
.hd,.ft{{position:absolute;left:96px;right:96px;display:flex;justify-content:space-between;font-size:20px;letter-spacing:2.4px}}
.hd{{top:64px;padding-bottom:18px;border-bottom:2px solid currentColor}}
.ft{{bottom:64px;padding-top:18px;border-top:2px solid currentColor}}
.ft span:first-child{{font-family:P,sans-serif;letter-spacing:4px}}
.k{{position:absolute;left:96px;top:250px;font-size:20px;letter-spacing:3px;color:#8A8A8A}}
.dark .k{{color:#9A958C}}
.h{{position:absolute;left:96px;right:96px;top:300px;font-size:68px;font-weight:700;line-height:1.24;letter-spacing:-2px}}
.p{{position:absolute;left:96px;right:96px;font-size:30px;font-weight:300;line-height:1.65;color:#55524D}}
.dark .p{{color:#C9C4BB}}
/* 1 표지 */
#c1{{background:#111;color:#F1EDE4}}
#c1 .ph{{position:absolute;inset:0;background:url(../../images/공간/피아노_01.jpg) 40% 50%/cover;filter:grayscale(.85) sepia(.18) brightness(.6)}}
#c1 .sh{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.45),rgba(0,0,0,0) 22%,rgba(0,0,0,0) 45%,rgba(0,0,0,.8))}}
#c1 .h{{top:auto;bottom:330px;font-size:84px}}
#c1 .p{{top:auto;bottom:250px;color:#D9D4CA}}
/* 2 흐림 → 또렷 */
.blurw{{position:absolute;left:96px;right:96px;top:640px;font-size:96px;font-weight:700;letter-spacing:-3px;color:#8A8A8A}}
.sharp{{position:absolute;left:96px;right:96px;top:800px;font-size:52px;font-weight:600;line-height:1.35;letter-spacing:-1.5px}}
.sharp u{{text-decoration:none;background:linear-gradient(transparent 62%,#DDE37C 62%) no-repeat 0 0/var(--u,0%) 100%}}
/* 3 파형 */
.wv{{position:absolute;left:96px;right:96px;height:220px;display:flex;align-items:center;gap:6px}}
.wv i{{flex:1;background:#111;border-radius:2px;opacity:.25}}
.wv i.hl{{opacity:1}}
.sel{{position:absolute;top:-20px;bottom:-20px;border:3px solid #111;background:rgba(221,227,124,.35)}}
.tc{{position:absolute;font-size:22px;letter-spacing:1px}}
/* 4 쪼개기 */
.pr{{position:absolute;left:96px;right:96px;display:grid;grid-template-columns:260px 1fr;padding:28px 0;border-top:1px solid rgba(17,17,17,.25)}}
.pr b{{font-size:36px;font-weight:700}}
.pr span{{font-size:28px;font-weight:300;color:#55524D;padding-top:6px}}
/* 5 두 파형 */
.lab{{position:absolute;left:96px;font-size:20px;letter-spacing:2.4px;color:#9A958C}}
.dark .wv i{{background:#F1EDE4}}
.diff{{position:absolute;width:64px;height:64px;border-radius:50%;background:#DDE37C;color:#111;font-size:30px;font-weight:700;display:flex;align-items:center;justify-content:center}}
/* 6 추상 → 구체 */
.row{{position:absolute;left:96px;right:96px;display:grid;grid-template-columns:300px 60px 1fr;align-items:start;padding:30px 0;border-top:1px solid rgba(17,17,17,.25)}}
.row .a{{font-size:28px;color:#8A8A8A;font-weight:400}}
.row .arr{{font-size:30px;color:#111}}
.row .b{{font-size:30px;font-weight:600;line-height:1.4;letter-spacing:-.6px}}
/* 7 장면 · 기간 */
.chip{{position:absolute;font-size:34px;font-weight:600;padding:22px 32px;border:2px solid #111;background:#F1EDE4}}
/* 8 마무리 */
#c8 .ghost{{position:absolute;left:84px;top:150px;font-size:240px;font-weight:700;letter-spacing:-8px;color:#2A2825;line-height:1}}
#c8 .info{{position:absolute;left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6}}
</style></head><body>

<section class="c" id="c1"><div class="ph" id="ph1"></div><div class="sh"></div>{hd()}
  <div class="h" id="h1">원하는 실력,<br>먼저 또렷하게.</div>
  <div class="p" id="p1">막연한 목표를, 연습할 수 있는 한 문장으로.</div>{ft(1)}</section>

<section class="c" id="c2">{hd()}<div class="k mono">VAGUE TO CLEAR</div>
  <div class="h" id="h2">"잘하고 싶다"는<br>방향이지, 목표가 아니에요.</div>
  <div class="blurw" id="bw">잘하고 싶다</div>
  <div class="sharp" id="sp"><u id="u2">이 곡 후렴을, 처음부터 끝까지<br>흔들리지 않고 부르기</u></div>
  <div class="p" style="top:1000px" id="p2">목표가 구체적이어야, 오늘 할 연습도 구체적이 됩니다.</div>{ft(2)}</section>

<section class="c" id="c3">{hd()}<div class="k mono">STEP 01 — REFERENCE</div>
  <div class="h" id="h3">좋아하는 곡을,<br>"구간"까지 좁혀요.</div>
  <div class="wv" id="wv3" style="top:640px">{wave}<div class="sel" id="sel3" style="left:44%;width:0"></div></div>
  <div class="tc mono" id="tc3" style="top:900px;left:96px">1:12 — 1:25</div>
  <div class="p" style="top:980px" id="p3">"이 사람이 좋다"에서 "이 8마디가 좋다"로.<br>목표가 손에 잡히기 시작합니다.</div>{ft(3)}</section>

<section class="c" id="c4">{hd()}<div class="k mono">STEP 02 — WHY</div>
  <div class="h" id="h4">"좋다"를<br>단어로 쪼개 보세요.</div>
  <div id="pt4">{ptbl}</div>
  <div class="p" style="top:1110px" id="p4">"멋있다"가 "고음에서 힘이 안 들어간 소리"가 됩니다.</div>{ft(4)}</section>

<section class="c dark" id="c5">{hd()}<div class="k mono">STEP 03 — COMPARE</div>
  <div class="h" id="h5">내 녹음과<br>나란히 들어 보세요.</div>
  <div class="lab mono" style="top:600px">REFERENCE</div><div class="wv" style="top:630px;height:150px" id="wa">{wave}</div>
  <div class="lab mono" style="top:820px">MY TAKE</div><div class="wv" style="top:850px;height:150px" id="wb">{wave2}</div>
  <div class="diff" id="d1" style="left:230px;top:770px">1</div><div class="diff" id="d2" style="left:520px;top:770px">2</div><div class="diff" id="d3" style="left:810px;top:770px">3</div>
  <div class="p" style="top:1060px" id="p5">차이를 딱 세 가지만 적기. 그게 지금의 목표예요.</div>{ft(5)}</section>

<section class="c" id="c6">{hd()}<div class="k mono">ABSTRACT → CLEAR</div>
  <div class="h" id="h6" style="font-size:60px">녹음해 보면 바로<br>"됐다 / 아직"이 보이는 문장.</div>
  <div id="rw6">{tbl}</div>{ft(6)}</section>

<section class="c sage" id="c7">{hd()}<div class="k mono">SCENE · TIME</div>
  <div class="h" id="h7">언제, 어디서,<br>누구 앞에서.</div>
  <div class="chip" id="ch1" style="left:96px;top:620px">입시 실기 자유곡</div>
  <div class="chip" id="ch2" style="left:470px;top:720px">친구 결혼식 축가</div>
  <div class="chip" id="ch3" style="left:150px;top:830px">밴드 합주 한 곡</div>
  <div class="chip" id="ch4" style="left:560px;top:930px">3개월 뒤, 이 구간</div>
  <div class="p" style="top:1080px" id="p7">장면과 기간이 붙으면, 필요한 실력이 정해집니다.<br>막막하면 내 녹음에서 듣기 싫은 부분부터 적어 보세요.</div>{ft(7)}</section>

<section class="c dark" id="c8"><div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>THE ENOCH WAY</span></div>
  <div class="ghost">ENOCH</div>
  <div class="h" id="h8" style="top:450px;font-size:70px">원하는 걸 또렷하게 알면,<br>오늘 할 연습이 보입니다.</div>
  <div class="p" style="top:720px" id="p8">같은 곡도, 사람마다 다르게 가르칩니다.<br>ENOCH은 모든 과정을 <b style="color:#F1EDE4">1:1</b>로 진행해요.</div>
  <div class="info"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span class="mono" style="text-align:right">031 315 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>
  {ft(8)}</section>

<script>
const $=id=>document.getElementById(id);
const cl=x=>Math.max(0,Math.min(1,x)), ease=x=>1-Math.pow(1-cl(x),3);
function up(el,p,dy=36){{if(!el)return;el.style.opacity=ease(p);el.style.transform=`translateY(${{(1-ease(p))*dy}}px)`;}}
window.show=i=>document.querySelectorAll(".c").forEach((c,k)=>c.classList.toggle("on",k===i-1));
window.setT=function(i,t){{
  show(i);
  ["h","p"].forEach(x=>{{}});
  up($("h"+i),(t-0.1)/0.6);
  if(i===1){{$("ph1").style.transform=`scale(${{1.1-0.1*ease(t/5)}})`;up($("p1"),(t-0.6)/0.6);}}
  if(i===2){{const b=$("bw");b.style.opacity=cl((t-0.5)/0.3)*(1-cl((t-1.8)/0.6)*0.65);b.style.filter=`blur(${{6*ease((t-0.6)/0.8)}}px)`;
    up($("sp"),(t-1.8)/0.6);$("u2").style.setProperty("--u",(100*ease((t-2.5)/0.9))+"%");up($("p2"),(t-3.2)/0.5);}}
  if(i===3){{const bars=$("wv3").querySelectorAll("i");const s=Math.floor(bars.length*0.44),e=Math.floor(bars.length*0.6);
    const w=ease((t-0.9)/0.8);$("sel3").style.width=(16*w)+"%";bars.forEach((b,k)=>{{b.classList.toggle("hl",k>=s&&k<s+(e-s)*w);b.style.transform=`scaleY(${{0.3+0.7*ease((t-0.3-k*0.008)/0.5)}})`;}});
    up($("tc3"),(t-1.6)/0.4);up($("p3"),(t-2.2)/0.5);}}
  if(i===4){{document.querySelectorAll("#pt4 .pr").forEach((r,k)=>{{r.style.top=(600+k*118)+"px";up(r,(t-0.8-k*0.35)/0.45,24);}});up($("p4"),(t-2.6)/0.5);}}
  if(i===5){{["wa","wb"].forEach((id,j)=>$(id).querySelectorAll("i").forEach((b,k)=>{{b.style.opacity=.85;b.style.transform=`scaleY(${{0.2+0.8*ease((t-0.4-j*0.4-k*0.008)/0.5)}})`;}}));
    [1,2,3].forEach(k=>{{const d=$("d"+k);const p=cl((t-1.8-k*0.35)/0.3);d.style.opacity=p;d.style.transform=`scale(${{0.5+0.5*ease(p)+0.12*Math.sin(Math.PI*p)}})`;}});up($("p5"),(t-3.0)/0.5);}}
  if(i===6){{document.querySelectorAll("#rw6 .row").forEach((r,k)=>{{r.style.top=(560+k*150)+"px";const p=(t-0.8-k*0.5);up(r,p/0.4,20);
    const b=r.querySelector(".b");b.style.opacity=ease((p-0.35)/0.4);b.style.transform=`translateX(${{(1-ease((p-0.35)/0.4))*-30}}px)`;}});}}
  if(i===7){{[1,2,3,4].forEach(k=>{{const el=$("ch"+k);const p=cl((t-0.8-k*0.3)/0.4);el.style.opacity=p;el.style.transform=`translateY(${{(1-ease(p))*30}}px) rotate(${{(k%2?-1:1)*2*(1-ease(p))}}deg)`;
    if(k===4){{el.style.background=p>=1?"#111":"#F1EDE4";el.style.color=p>=1?"#F1EDE4":"#111";}}}});up($("p7"),(t-2.6)/0.5);}}
  if(i===8){{up($("p8"),(t-0.8)/0.6);}}
}};
show(1);
</script></body></html>
'''
open(os.path.join(HERE, 'cards.html'), 'w', encoding='utf-8').write(html)
print('cards.html')
