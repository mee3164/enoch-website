# ENOCH NOTE — 남은 날짜 (deck.html 생성)
# 올리는 날에 맞춰: python3 gen.py 2026-10-21
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FONT='''@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Medium.woff2);font-weight:500}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}'''
CSS='''*{box-sizing:border-box;margin:0;padding:0}
:root{--iv:#F1EDE4;--bk:#111;--g:#8A8A8A;--b:#55524D;--bu:#F1E8CB;--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace;--en:"Helvetica Neue",Helvetica,Arial,"Liberation Sans",P,sans-serif}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;background:var(--iv);color:var(--bk);font-family:P,sans-serif;margin-bottom:40px;word-break:keep-all}
.s.dark{background:var(--bk);color:var(--iv)}
.hd{position:absolute;left:96px;right:96px;top:72px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:21px;letter-spacing:3px;padding-bottom:20px;border-bottom:1.5px solid currentColor}
.ft{position:absolute;left:96px;right:96px;bottom:60px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:20px;letter-spacing:2px;padding-top:20px;border-top:1.5px solid currentColor}
.ft span:first-child{font-family:P,sans-serif;letter-spacing:0;font-size:21px}
.k{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
.h{font-size:72px;font-weight:700;letter-spacing:-3.2px;line-height:1.22}
.h em{font-style:normal;font-weight:300}
.p{font-size:30px;line-height:1.75;color:var(--b);letter-spacing:-.6px}.p b{color:var(--bk)}
.dark .p{color:#C9C4BB}.dark .p b{color:var(--iv)}
.a{position:absolute}
.row{display:flex;gap:30px;padding:26px 0;border-bottom:1px solid rgba(17,17,17,.15)}
.dark .row{border-bottom-color:rgba(241,237,228,.16)}
.row .n{width:90px;flex:none;font-family:var(--en);font-size:44px;font-weight:700;letter-spacing:-2px;line-height:1}
.row .t{font-size:28px;line-height:1.55;color:var(--b);letter-spacing:-.5px}
.row .t b{color:var(--bk);font-size:32px;display:block;margin-bottom:4px}
.dark .row .t{color:#C9C4BB}.dark .row .t b{color:var(--iv)}
.paper{position:absolute;background:#FBF8F1 linear-gradient(rgba(17,17,17,.06) 1px,transparent 1px) 0 0/100% 44px;border:1.5px solid #111}
.hand{font-family:P,sans-serif;font-weight:400;color:#2B2A27}
.strike{position:absolute;left:40px;right:440px;top:56px;height:4px;background:#B23A2E;opacity:.85}
'''
import sys
from datetime import date
POST=date.fromisoformat(sys.argv[1]) if len(sys.argv)>1 else date(2026,10,19)
DAYS=(date(POST.year,12,31)-POST).days
WEEKS=DAYS//7
CSS+='''.dots{display:grid;grid-template-columns:repeat(7,40px);gap:16px 18px}
.dots i{width:40px;height:40px;border-radius:50%;border:2px solid #111;display:block}
.dots i.f{background:#111}
.wk{font-family:var(--mono);font-size:17px;letter-spacing:2px;color:var(--g);height:40px;line-height:40px}
.bu{background:var(--bu)}
'''
TOTAL=6
HD=lambda r="BEFORE THE YEAR ENDS": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
FT=lambda n: f'<div class="ft"><span>남은 날짜</span><span>0{n} / 0{TOTAL}</span></div>'
INFO='<div class="a" style="left:96px;right:96px;top:1040px;padding-top:22px;border-top:1px solid rgba(241,237,228,.3);display:flex;justify-content:space-between;font-size:22px;line-height:1.6"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>'
S=[]
# 01 표지
S.append(f"""<section class="s" id="c1">{HD()}
<img src="../../images/공간/기타앰프_01.jpg" style="position:absolute;left:96px;top:150px;width:888px;height:620px;object-fit:cover;object-position:50% 88%;display:block;filter:saturate(.8) contrast(1.03)">
<div class="k a" style="left:96px;top:810px">{DAYS} Days Left</div>
<div class="h a" style="left:92px;top:855px;font-size:84px;letter-spacing:-4.2px;line-height:1.18">올해,<br><em>아직 {DAYS}일 남았습니다</em></div>
<div class="p a" style="left:96px;top:1100px;font-size:28px">올해가 가기 전에, 한 곡.</div>
{FT(1)}</section>""")
# 02 73일 = 10주
rows=''
n=0
for w in range((DAYS+6)//7):
    cnt=min(7,DAYS-n); n+=cnt
    rows+=f'<span class="wk">W{w+1:02d}</span>'+''.join('<i></i>' for _ in range(cnt))+''.join('<span></span>' for _ in range(7-cnt))
S.append(f"""<section class="s" id="c2">{HD(f"{DAYS} DAYS = {WEEKS} WEEKS")}
<div class="k a" style="left:96px;top:200px">In Weeks</div>
<div class="h a" style="left:92px;top:250px">{DAYS}일은,<br><em>{WEEKS}주입니다</em></div>
<div class="p a" style="left:96px;top:480px;width:380px">일주일에 한 번이면,<br><b>{WEEKS}번.</b><br><br>하루씩 세면 짧아 보여도,<br>한 주씩 세면 꽤 길어요.</div>
<div class="a dots" style="right:96px;top:250px;grid-template-columns:70px repeat(7,40px)">{rows}</div>
{FT(2)}</section>""")
# 03 한 곡
S.append(f"""<section class="s" id="c3">{HD("ONE SONG")}
<div class="k a" style="left:96px;top:200px">Just One Song</div>
<div class="h a" style="left:92px;top:250px">목표는,<br><em>한 곡이면 충분합니다</em></div>
<div class="a" style="left:96px;right:96px;top:540px;border-top:1.5px solid #111">
<div class="row"><span class="n" style="width:230px;font-size:30px;letter-spacing:0;padding-top:6px">VOCAL</span><span class="t">좋아하는 노래, 처음부터 끝까지 불러 보기</span></div>
<div class="row"><span class="n" style="width:230px;font-size:30px;letter-spacing:0;padding-top:6px">GUITAR</span><span class="t">코드 몇 개로, 한 곡 쳐 보기</span></div>
<div class="row"><span class="n" style="width:230px;font-size:30px;letter-spacing:0;padding-top:6px">DRUM</span><span class="t">좋아하는 곡에 맞춰, 끝까지 쳐 보기</span></div>
<div class="row"><span class="n" style="width:230px;font-size:30px;letter-spacing:0;padding-top:6px">PIANO</span><span class="t">한 곡을, 두 손으로 쳐 보기</span></div>
<div class="row"><span class="n" style="width:230px;font-size:30px;letter-spacing:0;padding-top:6px">작곡 · MIDI</span><span class="t">내 곡 하나, 끝까지 만들어 보기</span></div>
</div>
{FT(3)}</section>""")
# 04 내년은 두 번째 곡부터
S.append(f"""<section class="s" id="c4">{HD("SONG No.2")}
<div class="bu a" style="left:96px;right:96px;top:150px;height:540px"></div>
<div class="a" style="left:140px;top:200px;font-family:var(--mono);font-size:22px;letter-spacing:4px;color:#55524D">JANUARY {POST.year+1}</div>
<div class="a" style="left:132px;top:300px;font-family:var(--en);font-weight:700;font-size:200px;letter-spacing:-9px;line-height:.9">SONG<br><span style="font-weight:300">No.2</span></div>
<div class="h a" style="left:92px;top:760px">올해 시작하면,<br><em>내년은 두 번째 곡부터</em></div>
<div class="p a" style="left:96px;right:96px;top:1010px">1월 1일에 "올해는 꼭" 하고 다짐하는 대신,<br>지금 첫 곡을 시작해 보세요.</div>
{FT(4)}</section>""")
# 05 ENOCH
S.append(f"""<section class="s" id="c5">{HD("THE ENOCH WAY")}
<div class="k a" style="left:96px;top:200px">1:1 Lesson</div>
<div class="a" style="left:88px;top:250px;font-family:var(--en);font-weight:700;font-size:330px;letter-spacing:-12px;line-height:.9">1:1</div>
<div class="h a" style="left:92px;top:600px">처음이어도,<br><em>내 속도로</em></div>
<div class="p a" style="left:96px;right:96px;top:850px">같은 곡도, 사람마다 다르게 가르칩니다.<br>입시 · 취미 · 성인 · 전문, <b>모든 과정이 1:1</b>이에요.</div>
{FT(5)}</section>""")
# 06 마무리
S.append(f"""<section class="s dark" id="c6">{HD("CONTACT")}
<div class="a" style="left:92px;top:150px;font-family:var(--en);font-weight:700;font-size:240px;letter-spacing:-8px;color:#2A2825;line-height:1">ENOCH</div>
<div class="h a" style="left:92px;top:450px">올해가 가기 전에,<br><span style="font-weight:300;color:var(--bu)">첫 곡을.</span></div>
<div class="p a" style="left:96px;right:96px;top:720px">카카오톡 채널 · 네이버 톡톡 · 체험수업 예약 · 상담 전화 · DM<br>나만의 진짜 소리를 찾는 곳.</div>
{INFO}
{FT(6)}</section>""")
open('deck.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>남은 날짜</title><style>{FONT}{CSS}</style></head><body>'+''.join(S)+'</body></html>')
