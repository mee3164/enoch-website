# 강사 소개 손주희: 한상희 feed.html/story.html의 스타일을 바탕으로 feed.html(3장), story.html(2장)을 만든다.
# python3 output/강사소개_손주희/build.py && CHROMIUM_PATH=... node output/강사소개_손주희/render.mjs
import os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '..', '강사소개_한상희')

EDU = ['호원대학교 <i>실용음악학과 졸업</i>']
WORK = ['에피톤 프로젝트 · 홍광호 · 1041 <i>등 다수 아티스트 앨범 작업 · 공연</i>']
LIVE = ['유희열의 스케치북 <i>및 다수 방송 · 콘서트 참여</i>']
ART = ['싱어송라이터 ‘손주희’ <i>개인 음악 활동 중</i>']
TEACH = []
EDU_S = EDU
WORK_S = WORK
AW = []


def sec(k, items, cls='k'):
    return f'<div class="sec"><span class="{cls}">{k}</span><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'


# ---------- feed ----------
f = open(os.path.join(BASE, 'feed.html'), encoding='utf-8').read()
head = f[:f.index('</style>')]
head = head.replace('강사 소개 한상희 피드', '강사 소개 손주희 피드').replace('한상희_01.jpg) 50% 28%', '손주희_01.jpg) 60% 30%')
head += '\n#f2 .sec{padding:30px 0}\n#f2 .sec li{font-size:25px}\n'
info = ('<div class="info"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span>'
        '<span style="text-align:right;font-family:var(--mono)">031 315 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">'
        'Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>')
band = 'VOCAL — 손주희 — ENOCH TEACHERS — ' * 4
feed = f'''</style></head><body>
<section class="s" id="f1">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — VOCAL</span></div>
  <div class="ph"></div>
  <div class="col">
    <div class="cell"><div class="k">Subject</div><div class="v">Vocal</div></div>
    <div class="cell"><div class="k">Lesson</div><div class="v">1:1</div></div>
    <div class="cell"><div class="k">Career</div><div class="t">호원대 실용음악학과 졸업<br>유희열의 스케치북 등 방송 · 콘서트<br>에피톤 프로젝트 · 홍광호 · 1041<br>싱어송라이터 ‘손주희’ 활동</div></div>
  </div>
  <div class="en">SON JU HUI</div>
  <div class="ko">손주희<span>보컬</span></div>
  <div class="band"><span>{band}</span></div>
</section>
<section class="s" id="f2">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — VOCAL</span></div>
  <div class="nm">SON JU HUI<small>손주희</small></div>
  <div class="tbl">{sec("Education", EDU)}{sec("Broadcast · Live", LIVE)}{sec("Works", WORK)}{sec("Artist", ART)}</div>
  <div class="ft"><span>강사 소개 — 손주희</span><span>02 / 03</span></div>
</section>
<section class="s dark" id="f4">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>THE ENOCH WAY</span></div>
  <div class="ghost">ENOCH</div>
  <div class="h">무대에서 다듬은 목소리를,<br><em>1:1로.</em></div>
  <div class="p">같은 곡도, 사람마다 다르게 가르칩니다.<br>ENOCH 보컬 레슨은 입시 · 취미 · 성인 · 전문,<br>모든 과정이 <b>1:1</b>입니다.</div>
  {info}
  <div class="ft"><span>강사 소개 — 손주희</span><span>03 / 03</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'feed.html'), 'w', encoding='utf-8').write(head + feed)

# ---------- story ----------
s = open(os.path.join(BASE, 'story.html'), encoding='utf-8').read()
sh = s[:s.index('</style>')]
sh = sh.replace('강사 소개 한상희', '강사 소개 손주희').replace('한상희_01.jpg', '손주희_01.jpg').replace('background-position:55% 30%', 'background-position:62% 30%')
sh += '\n#D .hl{position:absolute;left:80px;right:80px;top:430px}\n#D .hl div{padding:30px 0;border-bottom:1px solid rgba(255,255,255,.22)}\n#D .hl b{display:block;font-size:52px;font-weight:700;letter-spacing:-1.5px;line-height:1.2}\n#D .hl span{display:block;font-size:30px;color:#B9B4AA;margin-top:10px}\n#D .body{top:850px}\n#D .sec{padding:28px 0}\n#D .sec li{font-size:28px;line-height:1.55}\n#R .cv .hi{display:block;font-size:34px;font-weight:700;color:#F3F1EC;line-height:1.3;margin-bottom:18px}\n'
story = f'''</style></head><body>
<section class="s" id="R">
  <div class="top"><span class="lab g">ENOCH TEACHERS</span><span class="lab">VOCAL</span></div>
  <div class="side"><span></span><span class="lab g" style="writing-mode:vertical-rl;transform:rotate(180deg)">ENOCH MUSIC ACADEMY</span></div>
  <div class="ph"></div>
  <div class="en">SON<br>JU HUI</div>
  <div class="ko g">손주희</div>
  <div class="cv"><span class="lab g">CAREER</span><span class="hi">호원대학교<br>실용음악학과 졸업</span><span class="hi">유희열의 스케치북<br>방송 · 콘서트 참여</span></div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Vocal</span><span class="g">1:1 Lesson</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
<section class="s dt" id="D">
  <div class="top"><span class="lab g">ENOCH TEACHERS — VOCAL</span><span class="lab g">CAREER</span></div>
  <div class="nm">SON JU HUI<small>손주희</small></div>
  <div class="hl"><div><b>호원대학교 실용음악학과 졸업</b></div><div><b>유희열의 스케치북 참여</b><span>그 외 다수 방송 · 콘서트</span></div></div>
  <div class="body">{sec("WORKS", WORK_S, "lab g")}{sec("ARTIST", ART, "lab g")}</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Vocal</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'story.html'), 'w', encoding='utf-8').write(sh + story)
print('feed.html, story.html')

# ---------- story 한 장 버전 (story_one.html → story_one.png) ----------
one_css = sh.split('<style>')[1] if '<style>' in sh else ''
one = sh.split('</title>')[0] + '</title><style>' + one_css + '''
#O .top{position:absolute;left:80px;right:80px;top:230px;display:flex;justify-content:space-between;padding-bottom:20px;border-bottom:1px solid rgba(255,255,255,.22)}
#O .ph{position:absolute;right:80px;top:310px;width:460px;height:560px;background:url(../../images/강사/손주희_01.jpg) no-repeat;background-size:cover;background-position:62% 30%}
#O .en{position:absolute;left:76px;top:640px;font-size:96px;font-weight:700;line-height:.92;letter-spacing:-3px}
#O .ko{position:absolute;left:82px;top:830px;font-size:30px;letter-spacing:12px;color:#8C8C8C}
#O .sb{position:absolute;left:82px;top:330px;font-size:26px;line-height:1.6;color:#B9B4AA}
#O .hl{position:absolute;left:80px;right:80px;top:910px}
#O .hl div{padding:22px 0;border-top:1px solid rgba(255,255,255,.22)}
#O .hl b{display:block;font-size:46px;font-weight:700;letter-spacing:-1.5px;line-height:1.2}
#O .hl span{display:block;font-size:26px;color:#B9B4AA;margin-top:8px}
#O .body{position:absolute;left:80px;right:80px;top:1150px;border-top:1px solid rgba(255,255,255,.22)}
#O .sec{grid-template-columns:200px 1fr;padding:18px 0}
#O .sec li{font-size:26px;line-height:1.5}
#O .bt{position:absolute;left:80px;right:80px;top:1680px;padding-top:20px;display:flex;justify-content:space-between;font-size:22px;border-top:1px solid rgba(255,255,255,.22)}
</style></head><body>
<section class="s" id="O">
  <div class="top"><span class="lab g">ENOCH TEACHERS</span><span class="lab">VOCAL</span></div>
  <div class="sb">보컬<br>싱어송라이터<br>1:1 Lesson</div>
  <div class="ph"></div>
  <div class="en">SON<br>JU HUI</div>
  <div class="ko">손주희</div>
  <div class="hl"><div><b>호원대학교 실용음악학과 졸업</b></div><div><b>유희열의 스케치북 참여</b><span>그 외 다수 방송 · 콘서트</span></div></div>
  <div class="body">''' + sec("WORKS", WORK_S, "lab g") + sec("ARTIST", ART, "lab g") + '''</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Vocal</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section></body></html>
'''
open(os.path.join(HERE, 'story_one.html'), 'w', encoding='utf-8').write(one)
print('story_one.html')
