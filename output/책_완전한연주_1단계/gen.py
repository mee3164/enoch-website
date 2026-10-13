# ENOCH BOOK 01 — 『완전한 연주』 4장 1단계 (deck.html 생성)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

FONT = '''@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Medium.woff2);font-weight:500}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}
@font-face{font-family:S;src:url(../../templates/fonts/dm-serif-display-latin-400-normal.woff2)}'''
CSS = '''*{box-sizing:border-box;margin:0;padding:0}
:root{--iv:#F1EDE4;--bk:#111;--g:#8A8A8A;--b:#55524D;--li:#E3DDE9;--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--iv);color:var(--bk);font-family:P,sans-serif;margin-bottom:40px;word-break:keep-all}
.s.dark{background:var(--bk);color:var(--iv)}
.hd{position:absolute;left:96px;right:96px;top:72px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:21px;letter-spacing:3px;padding-bottom:20px;border-bottom:1.5px solid currentColor}
.ft{position:absolute;left:96px;right:96px;bottom:60px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2px;padding-top:20px;border-top:1.5px solid currentColor}
.ft span:first-child{font-family:P,sans-serif;letter-spacing:0;font-size:21px}
.src{position:absolute;left:96px;right:96px;bottom:26px;font-size:13px;color:#A8A39A}
.k{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
.h{font-size:72px;font-weight:700;letter-spacing:-3.2px;line-height:1.22}
.h em{font-style:normal;font-weight:300}
.p{font-size:30px;line-height:1.75;color:var(--b);letter-spacing:-.6px}.p b{color:var(--bk)}
.dark .p{color:#C9C4BB}.dark .p b{color:var(--iv)}
.q{position:relative;background:var(--li);padding:44px 52px 40px 52px}
.q .t{font-size:38px;font-weight:500;line-height:1.55;letter-spacing:-1.2px}
.q .pg{margin-top:18px;font-size:20px;letter-spacing:-.2px;color:#6E6878}
.q:before{content:"“";position:absolute;left:30px;top:-46px;font-family:S,serif;font-size:150px;line-height:1;color:#8E84A0}
'''
TOTAL = 7
HD = lambda r="ENOCH NOTE — STAGE FRIGHT": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT = lambda n: f'<div class="ft"><span>힘을 빼는 연습</span><span>0{n} / 0{TOTAL}</span></div>'
SRC = '<div class="src">인용 출처: 케니 워너, 『완전한 연주』, 이혜주 옮김, 현익출판. 쪽수는 각 인용 아래 표기.</div>'
SRC_PHOTO = '<div class="src">책 사진: ENOCH 촬영 · 『완전한 연주』 케니 워너 지음, 이혜주 옮김, 현익출판.</div>'

# 위에서 본 그랜드 피아노 + 손그림 잎 (표지를 베끼지 않은 ENOCH 선 그림)
PIANO = '''<svg width="380" height="440" viewBox="0 0 380 440"><g fill="none" stroke="#111" stroke-width="3" stroke-linecap="round" stroke-linejoin="round">
<path d="M30 400 V 60 Q 30 20 80 20 Q 160 20 200 120 Q 230 190 300 220 Q 350 245 350 300 V 400 Z" fill="#E3DDE9"/>
<path d="M30 352 H 350"/><path d="M30 400 H 350"/>
<g stroke-width="2.5"><path d="M110 330 C 100 260, 140 220, 120 160"/><path d="M120 160 c -30 10 -40 40 -20 60 c 10 -30 20 -40 20 -60 z" fill="#F1EDE4"/>
<path d="M112 250 c 30 -10 50 10 50 40 c -30 0 -45 -15 -50 -40 z" fill="#F1EDE4"/><path d="M104 300 c -30 -5 -45 15 -40 40 c 25 -5 38 -20 40 -40 z" fill="#F1EDE4"/>
<path d="M230 330 C 240 290, 270 280, 280 250"/><circle cx="282" cy="242" r="12" fill="#F1EDE4"/><path d="M240 300 c 20 -20 45 -15 50 5 c -20 10 -40 8 -50 -5 z" fill="#F1EDE4"/>
<path d="M70 90 c 20 10 30 30 20 50 M 70 90 c 25 -5 45 5 50 25"/></g></g>
<g fill="#111">''' + ''.join(f'<rect x="{44 + i*22}" y="352" width="10" height="28"/>' for i in range(14)) + '''</g>
<g stroke="#111" stroke-width="1.5">''' + ''.join(f'<path d="M{30 + i*16} 352 V 400"/>' for i in range(1, 20)) + '</g></svg>'

def quote(text, page, top, left=96, right=96):
    return f'<div class="q" style="position:absolute;left:{left}px;right:{right}px;top:{top}px"><div class="t">{text}</div><div class="pg">— {page}</div></div>'

S = []
S.append(f"""<section class="s" id="b1">{HD()}
<div style="position:absolute;left:560px;right:0;top:118px;bottom:0;background:var(--li)"></div>
<div style="position:absolute;left:620px;top:330px">{PIANO}</div>
<div class="k" style="position:absolute;left:96px;top:200px">Before the Exam</div>
<div class="h" style="position:absolute;left:92px;top:250px;width:470px;font-size:84px;letter-spacing:-4.2px;line-height:1.18">잘하려고<br>할수록,<br><em>더 떨린다면</em></div>
<div class="p" style="position:absolute;left:96px;top:880px;width:440px">시험장에서 손이 굳고<br>숨이 짧아지는 사람에게.</div>
{FT(1)}</section>""")

S.append(f"""<section class="s" id="b2">{HD()}
<div class="k" style="position:absolute;left:96px;top:200px">Let Go</div>
<div class="h" style="position:absolute;left:92px;top:250px">떨리는 건,<br><em>잘하고 싶어서</em></div>
<div class="p" style="position:absolute;left:96px;right:96px;top:520px">'잘해야 한다'는 마음이 클수록 어깨와 손에 힘이 들어갑니다.<br>한 재즈 피아니스트는 그 마음부터 내려놓으라고 말해요.</div>
{quote("위대한 연주자가 되려는<br>욕구를 떠나보내라", "케니 워너, 『완전한 연주』 185쪽", 800)}
{FT(2)}{SRC}</section>""")

S.append(f"""<section class="s" id="b3">{HD()}
<div class="k" style="position:absolute;left:96px;top:200px">Body First</div>
<div class="h" style="position:absolute;left:92px;top:250px">마음보다,<br><em>몸을 풀기</em></div>
<div class="p" style="position:absolute;left:96px;right:96px;top:520px">마음은 마음대로 안 되지만, 몸은 풀 수 있거든요.</div>
<div style="position:absolute;left:96px;right:96px;top:680px;border-top:1.5px solid #111">
<div style="display:flex;gap:40px;padding:30px 0;border-bottom:1px solid rgba(17,17,17,.15)"><span class="k" style="width:120px;flex:none;padding-top:8px">Breath</span><span class="p">깊이 들이쉬고, 아주 오래 천천히 내쉽니다.</span></div>
<div style="display:flex;gap:40px;padding:30px 0;border-bottom:1px solid rgba(17,17,17,.15)"><span class="k" style="width:120px;flex:none;padding-top:8px">Body</span><span class="p">머리 꼭대기부터 어깨, 손가락,<br>발끝까지 한 곳씩 힘을 풀어요.</span></div>
<div style="display:flex;gap:40px;padding:30px 0;border-bottom:1px solid rgba(17,17,17,.15)"><span class="k" style="width:120px;flex:none;padding-top:8px">Mind</span><span class="p">떠오르는 생각은 붙잡지 않고, 흘려보내기.</span></div>
</div>
{FT(3)}<div class="src">케니 워너, 『완전한 연주』 185–186쪽 요약.</div></section>""")

S.append(f"""<section class="s" id="b4">{HD()}
<div class="k" style="position:absolute;left:96px;top:200px">On the Instrument</div>
<div class="h" style="position:absolute;left:92px;top:250px">악기 위에서는,<br><em>힘을 쓰지 않고</em></div>
<div class="p" style="position:absolute;left:96px;right:96px;top:520px"><b>피아노</b> — 손가락을 건반에 그냥 떨어뜨립니다.<br><b>보컬</b> — 발을 단단히 딛고 서서,<br>내쉬는 숨이 노래가 된다고 상상해요.</div>
{quote("우리는 지금 힘들이지 않는<br>동작의 수월성을 배우는 중이다.", "케니 워너, 『완전한 연주』 188쪽", 860)}
{FT(4)}{SRC}</section>""")

row = lambda n, t, d, last=False: f'<div style="display:flex;gap:32px;padding:28px 0;border-top:1px solid rgba(241,237,228,.3){";border-bottom:1px solid rgba(241,237,228,.3)" if last else ""}"><span style="font-family:S,serif;color:var(--li);font-size:72px;width:64px;line-height:1">{n}</span><div><div style="font-size:36px;font-weight:700">{t}</div><div style="margin-top:10px;font-size:28px;color:#C9C4BB;line-height:1.5">{d}</div></div></div>'
S.append(f"""<section class="s dark" id="b5">{HD("TRY BEFORE THE EXAM")}
<div class="h" style="position:absolute;left:92px;top:200px">시험장 들어가기 전,<br><em>2분</em></div>
<div style="position:absolute;left:96px;right:96px;top:470px">
{row(1,'길게 내쉬기','들이쉰 것보다 더 오래, 천천히 내쉬어 보세요.')}
{row(2,'머리부터 발끝까지','어깨, 손, 다리. 한 곳씩 힘을 풀어 봅니다.')}
{row(3,'잘해야 한다는 생각','잠깐만 내려놓기. 오늘은 그냥 연주하러 온 사람.',True)}
</div>
<div class="p" style="position:absolute;left:96px;right:96px;top:1080px;font-size:24px;color:#9A958C">책은 이 연습을 2–5분씩 나눠, 하루에 여러 번 해도 좋다고 합니다.</div>
{FT(5)}</section>""")

S.append(f"""<section class="s" id="b6">{HD("FROM THE BOOK")}
<div style="position:absolute;left:0;width:520px;top:118px;height:640px;background:var(--li)"></div>
<img src="../../images/책/완전한연주_표지.jpg" style="position:absolute;left:96px;top:220px;width:340px;height:454px;object-fit:cover;object-position:50% 45%;display:block">
<div class="k" style="position:absolute;left:600px;top:220px">From the Book</div>
<div class="h" style="position:absolute;left:596px;top:270px;font-size:60px;letter-spacing:-2.6px">이 이야기가<br><em>나온 책</em></div>
<div class="p" style="position:absolute;left:600px;right:80px;top:470px;font-size:27px">『완전한 연주』<br>케니 워너 지음<br>이혜주 옮김 · 현익출판</div>
<div class="p" style="position:absolute;left:600px;right:80px;top:680px;font-size:25px">재즈 피아니스트가 연주 불안을 겪는 음악가에게 쓴 책. 오늘 이야기는 4장 '단계적 연습'의 1단계에서 가져왔어요.</div>
{quote("1단계는 당신을 내면의 자신에게<br>소개하는 훈련이다.", "181쪽", 900)}
{FT(6)}{SRC_PHOTO}</section>""")

S.append(f"""<section class="s dark" id="b7">{HD("THE ENOCH WAY")}
<div style="position:absolute;left:92px;top:150px;font-family:'Helvetica Neue',Arial,sans-serif;font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825">ENOCH</div>
<div class="h" style="position:absolute;left:92px;top:450px">떨릴수록,<br><span style="color:var(--li)">힘을 빼는 연습.</span></div>
<div class="p" style="position:absolute;left:96px;right:96px;top:740px">같은 곡도, 사람마다 다르게 가르칩니다.<br>ENOCH 입시 과정은 모두 1:1,<br>모의고사도 진행합니다.</div>
<div style="position:absolute;left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>
{FT(7)}</section>""")

open('deck.html', 'w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>힘을 빼는 연습</title><style>{FONT}{CSS}</style></head><body>' + ''.join(S) + '</body></html>')
