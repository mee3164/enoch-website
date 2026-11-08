# 릴스 "몇 달째 제자리라면" — 제목은 올라오고 나머지 글은 타이핑, 길이는 글자 수에 맞춰 자동 계산, 1080×1920, 모션 그래픽 + 시설 사진 (노트_또렷한목표 카드뉴스의 릴스 버전)
# python3 output/릴스_또렷한목표/build.py → reel.html → node output/릴스_또렷한목표/render.mjs → reel.mp4
import os, math
HERE = os.path.dirname(os.path.abspath(__file__))

def bars(seed, n=48):
    return ''.join(f'<i style="height:{int(25 + 70 * abs(math.sin(k * 0.73 + seed) * math.cos(k * 0.21 + seed)))}%"></i>' for k in range(n))

def photo(name, pos='50% 50%', b=.5):
    return f'<div class="ph" style="background-image:url(../../images/공간/{name});background-position:{pos};filter:grayscale(.75) sepia(.18) brightness({b})"></div><div class="sh"></div>'

chips = ['입시 실기 자유곡', '친구 결혼식 축가', '밴드 합주 한 곡', '3개월 뒤, 이 구간']
parts = ['소리', '음정 · 리듬', '표현', '기술']

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1920px;overflow:hidden;background:#111;font-family:P,sans-serif;word-break:keep-all}}
.sc{{position:absolute;inset:0;opacity:0;overflow:hidden;color:#F1EDE4;background:#111}}
.iv{{background:#F1EDE4;color:#111}}
.ph{{position:absolute;inset:-4%;background-size:cover}}
.sh{{position:absolute;inset:0;background:linear-gradient(180deg,rgba(0,0,0,.45),rgba(0,0,0,0) 20%,rgba(0,0,0,0) 45%,rgba(0,0,0,.75))}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
.hd{{position:absolute;left:84px;right:84px;top:150px;display:flex;justify-content:space-between;font-size:22px;padding-bottom:18px;border-bottom:2px solid currentColor}}
.k{{position:absolute;left:84px;top:300px;font-size:24px;opacity:.75}}
.t{{position:absolute;left:84px;right:84px;font-weight:700;letter-spacing:-2px;line-height:1.24}}
.s{{position:absolute;left:84px;right:84px;font-weight:300;font-size:40px;line-height:1.5;opacity:.85}}
.wv{{position:absolute;left:84px;right:84px;height:240px;display:flex;align-items:center;gap:7px}}
.wv i{{flex:1;background:currentColor;border-radius:2px;opacity:.3}}
.wv i.hl{{opacity:1;background:#DDE37C}}
.sel{{position:absolute;top:-24px;bottom:-24px;border:3px solid #DDE37C}}
.diff{{position:absolute;width:84px;height:84px;border-radius:50%;background:#DDE37C;color:#111;font-size:40px;font-weight:700;display:flex;align-items:center;justify-content:center}}
.word{{position:absolute;left:84px;font-size:72px;font-weight:700;letter-spacing:-2px}}
.chip{{position:absolute;font-size:42px;font-weight:600;padding:26px 38px;border:2px solid #F1EDE4;background:rgba(17,17,17,.55)}}
.ghost{{position:absolute;left:70px;top:230px;font-weight:700;font-size:250px;letter-spacing:-8px;color:#262421}}
u{{text-decoration:none;background:linear-gradient(transparent 62%,#DDE37C 62%) no-repeat 0 0/var(--u,0%) 100%}}
</style></head><body>

<section class="sc" id="s1">{photo('피아노_01.jpg', '40% 50%', .55)}
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH NOTE</span></div>
  <div class="t" id="t1" style="top:1020px;font-size:96px">몇 달째 제자리라면,<br>이걸 먼저<br>확인해 보세요.</div>
  <div class="s" id="s1s" style="top:1460px">막연한 목표를, 연습할 수 있는 한 문장으로.</div>
</section>

<section class="sc iv" id="s2">
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>VAGUE → CLEAR</span></div>
  <div class="t" id="t2" style="top:420px;font-size:80px">"잘하고 싶다"는<br>방향이지,<br>목표가 아니에요.</div>
  <div class="t" id="bw" style="top:930px;font-size:120px;color:#8A8A8A">잘하고 싶다</div>
  <div class="t" id="sp" style="top:1160px;font-size:64px;line-height:1.35"><u id="u2">가장 자신 없는 한 소절을,<br>이번 주 안에.</u></div>
</section>

<section class="sc" id="s3">{photo('보컬부스_03.jpg', '50% 50%', .45)}
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>STEP 01</span></div>
  <div class="t" id="t3" style="top:420px;font-size:84px">좋아하는 곡을,<br>"구간"까지 좁혀요.</div>
  <div class="wv" id="wv3" style="top:900px">{bars(0)}<div class="sel" id="sel3" style="left:44%;width:0"></div></div>
  <div class="mono" id="tc3" style="position:absolute;left:84px;top:1200px;font-size:30px">1:12 — 1:25</div>
  <div class="s" id="s3s" style="top:1300px">"이 사람이 좋다"에서<br>"이 8마디가 좋다"로.</div>
</section>

<section class="sc" id="s4">{photo('기타존_01.jpg', '50% 50%', .42)}
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>STEP 02</span></div>
  <div class="t" id="t4" style="top:420px;font-size:84px">"좋다"를<br>단어로 쪼개 보세요.</div>
  {''.join(f'<div class="word" id="w{k}" style="top:{860 + k * 150}px">{p}</div>' for k, p in enumerate(parts))}
</section>

<section class="sc" id="s5">{photo('미디룸_01.jpg', '50% 50%', .38)}
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>STEP 03</span></div>
  <div class="t" id="t5" style="top:420px;font-size:84px">내 녹음과<br>나란히 들어 보세요.</div>
  <div class="mono" style="position:absolute;left:84px;top:820px;font-size:22px;opacity:.7">REFERENCE</div>
  <div class="wv" id="wa" style="top:850px;height:170px">{bars(0)}</div>
  <div class="mono" style="position:absolute;left:84px;top:1080px;font-size:22px;opacity:.7">MY TAKE</div>
  <div class="wv" id="wb" style="top:1110px;height:170px">{bars(1.3)}</div>
  <div class="diff" id="d1" style="left:210px;top:1010px">1</div><div class="diff" id="d2" style="left:500px;top:1010px">2</div><div class="diff" id="d3" style="left:790px;top:1010px">3</div>
  <div class="s" id="s5s" style="top:1400px">차이를 딱 세 가지만 적기.<br>그게 지금의 목표예요.</div>
</section>

<section class="sc" id="s6">{photo('무대_02.jpg', '50% 55%', .4)}
  <div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>SCENE · TIME</span></div>
  <div class="t" id="t6" style="top:420px;font-size:84px">언제, 어디서,<br>누구 앞에서.</div>
  {''.join(f'<div class="chip" id="c{k}" style="left:{[84, 380, 140, 420][k]}px;top:{860 + k * 150}px">{c}</div>' for k, c in enumerate(chips))}
  <div class="s" id="s6s" style="top:1480px">장면과 기간이 붙으면,<br>필요한 실력이 정해집니다.</div>
</section>

<section class="sc" id="s7">
  <div class="ghost">ENOCH</div>
  <div class="t" id="t7" style="top:640px;font-size:76px">원하는 걸 또렷하게 알면,<br>오늘 할 연습이 보입니다.</div>
  <div class="s" id="s7s" style="top:900px">같은 곡도, 사람마다 다르게 가르칩니다.<br>모든 과정 1:1.</div>
  <div class="mono" style="position:absolute;left:84px;right:84px;bottom:220px;display:flex;justify-content:space-between;font-size:22px;padding-top:18px;border-top:1px solid #444;color:#B9B4AA"><span>ENOCH MUSIC ACADEMY</span><span>031 315 3666</span></div>
</section>

<script>
const SPEED=16, S=["s1","s2","s3","s4","s5","s6","s7"];
const $=id=>document.getElementById(id);
const cl=x=>Math.max(0,Math.min(1,x)), ease=x=>1-Math.pow(1-cl(x),3);
const back=x=>{{x=cl(x);const c=1.7;return 1+(c+1)*Math.pow(x-1,3)+c*Math.pow(x-1,2);}};
function up(el,p,dy=40){{el.style.opacity=ease(p);el.style.transform=`translateY(${{(1-ease(p))*dy}}px)`;}}
// 타이핑: 태그(<br>, <u>)는 그대로 두고 글자만 하나씩. 끝에 깜빡이는 커서
const FULL={{}};
function tok(id){{if(!FULL[id]) FULL[id]=$(id).innerHTML.split(/(<[^>]+>)/).flatMap(x=>x.startsWith("<")?[x]:[...x]); return FULL[id];}}
function len(id){{return tok(id).filter(x=>!x.startsWith("<")).length/SPEED;}}
function typeT(id,u,cursor=true){{const el=$(id), tk=tok(id), chars=tk.filter(x=>!x.startsWith("<")).length, n=Math.floor(cl(u*SPEED/chars)*chars);
  let c=0,out="";for(const x of tk){{if(x.startsWith("<")){{out+=x;continue;}} if(c<n){{out+=x;c++;}}}}
  const show=cursor&&u>=0&&((n<chars&&u<chars/SPEED)||(u<chars/SPEED+0.6&&Math.floor(u*2.4)%2===0));
  el.innerHTML=out+`<span style="display:inline-block;width:.06em;height:.9em;margin-left:.06em;vertical-align:-.08em;background:currentColor;opacity:${{show?1:0}}"></span>`;
  el.style.opacity=u<0?0:1; return chars/SPEED;}}
// 장면 길이: 글자 수에 맞춰 계산
const G=0.2, HOLD=1.1;
// 타이핑(T)과 한 번에 뜨기(F)를 섞는다. 핵심 문장만 타이핑, 나머지는 통째로 올라오기
const F=0.6;   // 통째로 뜨는 문장에 주는 시간
const PLAN={{
 s1:()=>0.8+F+HOLD,                                   // 제목 F, 설명 F
 s2:()=>len("t2")+G+0.9+len("sp")+0.8+HOLD,          // 제목 T, 흐린 말 F, 핵심 문장 T
 s3:()=>F+1.0+len("tc3")+G+F+HOLD,                    // 제목 F, 타임코드 T, 설명 F
 s4:()=>len("t4")+G+4*0.3+HOLD,                       // 제목 T, 단어 4개 F(차례로)
 s5:()=>F+1.4+len("s5s")+HOLD,                        // 제목 F, 핵심 문장 T
 s6:()=>len("t6")+1.4+F+HOLD,                         // 제목 T, 설명 F
 s7:()=>F+G+len("s7s")+HOLD+0.8}};                    // 제목 F, 마지막 문장 T
const START={{}}; let acc=0; S.forEach(id=>{{START[id]=acc; acc+=PLAN[id]();}}); window.TOTAL=acc;
window.setT=function(t){{
  S.forEach((id,k)=>{{const a=START[id], b=a+PLAN[id](); const on=t>=a&&(t<b||k===S.length-1); const el=$(id); el.style.opacity=on?1:0;
    const ph=el.querySelector(".ph"); if(ph) ph.style.transform=`scale(${{1.06-0.06*cl((t-a)/(b-a))}})`;}});
  // 1
  let u=t-START.s1; up($("t1"),(u-0.1)/0.6); up($("s1s"),(u-0.8)/F);
  // 2
  u=t-START.s2; let c=0; typeT("t2",u-c); c+=len("t2")+G;
  const bw=$("bw"); bw.style.opacity=ease((u-c)/0.3)*(1-0.7*cl((u-c-0.4)/0.5)); bw.style.filter=`blur(${{8*ease((u-c-0.4)/0.5)}}px)`; c+=0.9;
  typeT("sp",u-c); c+=len("sp"); $("u2").style.setProperty("--u",(100*ease((u-c)/0.7))+"%");
  // 3
  u=t-START.s3; c=0; up($("t3"),u/F); c+=F;
  const bars=$("wv3").querySelectorAll("i"), s0=Math.floor(bars.length*.44), s1=Math.floor(bars.length*.6), w=ease((u-c-0.3)/0.6);
  $("sel3").style.width=(16*w)+"%"; bars.forEach((b,k)=>{{b.classList.toggle("hl",k>=s0&&k<s0+(s1-s0)*w); b.style.transform=`scaleY(${{0.25+0.75*ease((u-c+0.2-k*0.008)/0.4)}})`;}});
  c+=1.0; typeT("tc3",u-c,false); c+=len("tc3")+G; up($("s3s"),(u-c)/F);
  // 4
  u=t-START.s4; c=0; typeT("t4",u); c+=len("t4")+G;
  [0,1,2,3].forEach(k=>{{const el=$("w"+k),p=(u-c-k*0.3)/0.3; el.style.opacity=cl(p*2); el.style.transform=`translateX(${{(1-back(p))*-80}}px)`;}});
  // 5
  u=t-START.s5; c=0; up($("t5"),u/F); c+=F;
  ["wa","wb"].forEach((id,j)=>$(id).querySelectorAll("i").forEach((b,k)=>{{b.style.opacity=.85;b.style.transform=`scaleY(${{0.2+0.8*ease((u-c+0.1-j*0.3-k*0.008)/0.4)}})`;}}));
  [1,2,3].forEach(k=>{{const dd=$("d"+k),p=cl((u-c-0.5-k*0.22)/0.25); dd.style.opacity=p; dd.style.transform=`scale(${{0.5+0.5*ease(p)+0.15*Math.sin(Math.PI*p)}})`;}});
  c+=1.4; typeT("s5s",u-c);
  // 6
  u=t-START.s6; c=0; typeT("t6",u); c+=len("t6");
  [0,1,2,3].forEach(k=>{{const el=$("c"+k),p=cl((u-c-0.1-k*0.25)/0.3); el.style.opacity=p; el.style.transform=`translateY(${{(1-ease(p))*40}}px) rotate(${{(k%2?-1:1)*3*(1-ease(p))}}deg)`;
    if(k===3){{el.style.background=p>=1?"#DDE37C":"rgba(17,17,17,.55)"; el.style.color=p>=1?"#111":"#F1EDE4"; el.style.borderColor=p>=1?"#DDE37C":"#F1EDE4";}}}});
  c+=1.4; up($("s6s"),(u-c)/F);
  // 7
  u=t-START.s7; c=0; up($("t7"),u/F); c+=F+G; typeT("s7s",u-c);
}};
setT(0);
</script></body></html>
'''
open(os.path.join(HERE, 'reel.html'), 'w', encoding='utf-8').write(html)
print('reel.html')
