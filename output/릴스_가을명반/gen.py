# 릴스 — 가을이 지나가기 전에, 들어야 할 국내 명반 7장 (1080×1920)
# python3 gen.py → reel.html   /   node record.mjs → reel.mp4
# 커버: ../../images/앨범/<file> 이 있으면 쓰고, 없으면 글자형 슬리브로 대신한다.
import os, html
HERE = os.path.dirname(os.path.abspath(__file__))
COV = os.path.join(HERE, '../../images/앨범')
A = [  # 아티스트, 앨범, 연도, 장르, 들어 볼 곡, 선정 근거, 커버 파일
 ('들국화', '들국화', 1985, 'Rock', '행진', '2007 한국대중음악 100대 명반 1위', 'kr_deulgukhwa_1.jpg'),
 ('어떤날', '어떤날 1960 · 1965', 1986, 'Folk · Guitar', '그날', '한국대중음악 100대 명반 선정', 'kr_eotteonnal_1.jpg'),
 ('유재하', '사랑하기 때문에', 1987, 'Ballad', '가리워진 길', '음악 관계자 10명이 꼽은 우리 가요 선정', 'kr_yoojaeha.jpg'),
 ('한영애', '바라본다', 1988, 'Blues · Rock', '누구 없소', '2007 한국대중음악 100대 명반 선정', 'kr_hanyoungae_2.jpg'),
 ('김현철', '김현철 Vol.1', 1989, 'City Pop', '춘천 가는 기차', '한국대중음악 100대 명반 선정', 'kr_kimhyunchul_1.jpg'),
 ('김광석', '다시 부르기 2', 1995, 'Folk', '너무 아픈 사랑은 사랑이 아니었음을', '2018 한국 대중음악 명반 100 선정', 'kr_kimkwangseok_re2.jpg'),
 ('이소라', '눈썹달', 2004, 'Ballad', '바람이 분다', '2007 한국대중음악 100대 명반 선정', 'kr_leesora_6.jpg'),
]
e = html.escape
T0, STEP, D = 2.6, 3.6, 3.85
END = T0 + STEP * len(A) + 3.4

def cover(i, a, t):
    f = os.path.join(COV, a[6])
    if os.path.exists(f):
        inner = f'<img src="../../images/앨범/{a[6]}">'
    else:  # 글자형 슬리브 (커버를 받으면 자동으로 바뀜)
        dark = i % 2 == 0
        bg, fg, sub = ('#1b1a18', '#F1EDE4', '#8a857e') if dark else ('#E6E0D4', '#111', '#6E6A64')
        inner = (f'<div class="slv" style="background:{bg};color:{fg}"><div class="sa">{e(a[0])}</div>'
                 f'<div class="st">{e(a[1])}</div><div class="sy" style="color:{sub}">{a[2]}</div></div>')
    return f'<div class="cov" style="--t:{t:.2f}s">{inner}<div class="rec"></div></div>'

S = []
fan = ''
for k, a in enumerate(A):
    f = os.path.join(COV, a[6]); ang = (k - 3) * 4
    src = f'<img src="../../images/앨범/{a[6]}">' if os.path.exists(f) else f'<div class="slv mini" style="background:{"#1b1a18" if k%2==0 else "#E6E0D4"};color:{"#F1EDE4" if k%2==0 else "#111"}"><div class="sa">{e(a[0])}</div></div>'
    fan += f'<div class="fj" style="left:{96+88*k}px;top:{1040+abs(k-3)*18}px;transform:rotate({ang}deg);z-index:{10-abs(k-3)}"><div class="fi" style="--t:{0.35+0.09*k:.2f}s">{src}</div></div>'
S.append(f'''<section class="sc" style="--s:0s;--d:2.85s;background:#F1EDE4;color:#111;animation-name:sc0">
  <div class="abs k" style="top:300px;color:#6E6A64">ENOCH Listening · Korean Classics</div>
  <div class="abs" style="top:370px;font-size:104px;font-weight:700;letter-spacing:-5px;line-height:1.15">가을이<br>지나가기 전에,</div>
  <div class="abs" style="top:620px;font-size:104px;font-weight:300;letter-spacing:-5px;line-height:1.15">들어야 할<br>국내 명반 7장</div>
  <div class="abs r" style="top:1540px;font-size:32px;color:#55524D;text-align:center;--t:1.2s">평론가와 음악 관계자들이 꼽은 앨범들</div>
  {fan}
</section>''')
for i, a in enumerate(A):
    s = T0 + STEP * i; dark = i % 2 == 1
    bg, fg, mut = ('#111', '#F1EDE4', '#9A958C') if dark else ('#F1EDE4', '#111', '#6E6A64')
    S.append(f'''<section class="sc" style="--s:{s:.2f}s;--d:{D}s;background:{bg};color:{fg}">
  <div class="abs k r" style="top:300px;color:{mut};--t:{s+.05:.2f}s">{e(a[3])} · Record 0{i+1} / 07</div>
  {cover(i, a, s+.1)}
  <div class="abs k r" style="top:1150px;color:{mut};--t:{s+.45:.2f}s">{e(a[0])}</div>
  <div class="abs r" style="top:1195px;font-weight:700;font-size:76px;letter-spacing:-2.5px;line-height:1.1;--t:{s+.55:.2f}s">{e(a[1])} <span style="font-weight:300;font-size:44px;color:{mut}">{a[2]}</span></div>
  <div class="abs r" style="top:1330px;font-size:34px;--t:{s+.8:.2f}s"><span class="k" style="color:{mut};margin-right:18px">Track</span>{e(a[4])}</div>
  <div class="abs r" style="top:1410px;font-size:26px;color:{mut};--t:{s+1.0:.2f}s">{e(a[5])}</div>
  <div class="abs" style="top:1500px;font-size:20px;color:{mut};opacity:.7">앨범 아트워크의 저작권은 각 음반사에 있습니다.</div>
</section>''')
s = T0 + STEP * len(A)
S.append(f'''<section class="sc" style="--s:{s:.2f}s;--d:3.4s;background:#111;color:#F1EDE4;animation-name:fin">
  <div class="abs r" style="top:330px;font-weight:700;font-size:250px;letter-spacing:-9px;color:#2A2825;line-height:1;--t:{s+.1:.2f}s">ENOCH</div>
  <div class="abs r" style="top:640px;font-size:96px;font-weight:700;letter-spacing:-4px;line-height:1.16;--t:{s+.3:.2f}s">한 곡을,<br><span style="color:#F1E8CB">세 번 들어 보기.</span></div>
  <div class="abs r" style="top:930px;font-size:38px;line-height:1.7;color:#C9C4BB;--t:{s+.8:.2f}s">처음엔 그냥, 두 번째는 한 악기만,<br>세 번째는 한 소절 따라 해 보기.</div>
  <div class="abs r" style="top:1200px;font-size:30px;line-height:1.6;--t:{s+1.2:.2f}s">곡 목록은 캡션에 · 에녹실용음악학원 시흥점</div>
</section>''')

CSS = f'''
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
:root{{--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace}}
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1080px;height:1920px;overflow:hidden;background:#111;font-family:P,sans-serif;word-break:keep-all}}
.sc{{position:absolute;inset:0;opacity:0;animation:scene var(--d) linear var(--s) both}}
@keyframes scene{{0%{{opacity:0}}5%{{opacity:1}}95%{{opacity:1}}100%{{opacity:0}}}}
@keyframes sc0{{0%{{opacity:1}}95%{{opacity:1}}100%{{opacity:0}}}}
@keyframes fin{{0%{{opacity:0}}8%{{opacity:1}}100%{{opacity:1}}}}
.r{{opacity:0;animation:rise .6s cubic-bezier(.2,.7,.2,1) var(--t) both}}
@keyframes rise{{from{{opacity:0;transform:translateY(40px)}}to{{opacity:1;transform:none}}}}
.abs{{position:absolute;left:96px;right:96px}}
.k{{font-family:var(--mono);font-size:24px;letter-spacing:4px;text-transform:uppercase}}
.cov{{position:absolute;left:96px;top:380px;width:700px;height:700px;opacity:0;animation:slide .8s cubic-bezier(.2,.7,.2,1) var(--t) both}}
.cov img,.cov .slv{{position:absolute;inset:0;width:700px;height:700px;object-fit:cover;z-index:2}}
.slv{{display:flex;flex-direction:column;justify-content:flex-end;padding:56px}}
.slv .sa{{font-size:120px;font-weight:700;letter-spacing:-6px;line-height:1}}
.slv .st{{font-size:40px;font-weight:300;margin-top:18px}}
.slv .sy{{font-family:var(--mono);font-size:26px;letter-spacing:4px;margin-top:14px}}
.slv.mini{{padding:28px}}.slv.mini .sa{{font-size:64px;letter-spacing:-3px}}
.rec{{position:absolute;left:0;top:20px;width:660px;height:660px;border-radius:50%;background:radial-gradient(circle,#F1E8CB 0 17%,#111 17.5% 100%);z-index:1;animation:out 1s cubic-bezier(.2,.7,.2,1) calc(var(--t) + .5s) both}}
@keyframes slide{{from{{opacity:0;transform:translateX(160px)}}to{{opacity:1;transform:none}}}}
@keyframes out{{from{{transform:translateX(0)}}to{{transform:translateX(230px)}}}}
.bar{{position:absolute;left:0;top:0;height:8px;background:#F1E8CB;animation:prog {END:.1f}s linear both;z-index:9}}
@keyframes prog{{from{{width:0}}to{{width:100%}}}}
.fj{{position:absolute;width:360px;height:360px}}
.fj img,.fj .slv{{width:360px;height:360px;object-fit:cover;display:flex}}
.fi{{animation:fin2 .7s cubic-bezier(.2,.7,.2,1) var(--t) both}}
@keyframes fin2{{from{{opacity:0;transform:translateY(120px)}}to{{opacity:1;transform:none}}}}
'''
open(os.path.join(HERE, 'reel.html'), 'w').write(
    f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>가을 명반 7장</title><style>{CSS}</style></head><body>'
    + '\n'.join(S) + '<div class="bar"></div><script>window.END=' + f'{END:.2f}' + '</script></body></html>')
print('reel.html', f'{END:.1f}s')
