# 강사 소개 이승진: 한상희 feed.html/story.html의 스타일을 바탕으로 feed.html(3장), story.html(2장)을 만든다.
# python3 output/강사소개_이승진/build.py && CHROMIUM_PATH=... node output/강사소개_이승진/render.mjs
import os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '..', '강사소개_한상희')

EDU = ['한양대학교 일반대학원 실용음악학과 <i>예술석사</i>', '한양대학교 ERICA 실용음악학과 <i>학사</i>', '<i>기타 전공</i>']
TEA = ['호원대학교 실용음악학부 객원교수 <i>(2026)</i>', '중학교 동아리 · 자유학기 강사 <i>(전)</i>', '<i>밴드부 · 통기타부</i>', '<i>일신중 · 광명북중 · 철산중 · 충현중</i>']
AW = ['부천아트밸리 프로그램 강사 표창장 <i>2021</i>', 'GYMF 대상 <i>FM, 2010</i>']


def sec(k, items, cls='k'):
    return f'<div class="sec"><span class="{cls}">{k}</span><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'


# ---------- feed ----------
f = open(os.path.join(BASE, 'feed.html'), encoding='utf-8').read()
head = f[:f.index('</style>')]
head = head.replace('강사 소개 한상희 피드', '강사 소개 이승진 피드').replace('한상희_01.jpg) 50% 28%', '이승진_01.jpg) 50% 34%')
head += '\n#f2 .sec{padding:36px 0}\n#f2 .sec li{font-size:28px}\n'
info = ('<div class="info"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span>'
        '<span style="text-align:right;font-family:var(--mono)">031 315 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">'
        'Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>')
band = 'GUITAR — 이승진 — ENOCH TEACHERS — ' * 4
feed = f'''</style></head><body>
<section class="s" id="f1">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — GUITAR</span></div>
  <div class="ph"></div>
  <div class="col">
    <div class="cell"><div class="k">Subject</div><div class="v">Guitar · 화성학</div></div>
    <div class="cell"><div class="k">Lesson</div><div class="v">1:1</div></div>
    <div class="cell"><div class="k">Career</div><div class="t">한양대 대학원 예술석사<br>한양대 ERICA 기타 전공<br>호원대 실용음악학부 객원교수<br>GYMF 대상 (2010)</div></div>
  </div>
  <div class="en">LEE SEUNGJIN</div>
  <div class="ko">이승진<span>기타 · 화성학</span></div>
  <div class="band"><span>{band}</span></div>
</section>
<section class="s" id="f2">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — GUITAR</span></div>
  <div class="nm">LEE SEUNGJIN<small>이승진</small></div>
  <div class="tbl">{sec("Education", EDU)}{sec("Teaching", TEA)}{sec("Awards", AW)}</div>
  <div class="ft"><span>강사 소개 — 이승진</span><span>02 / 03</span></div>
</section>
<section class="s dark" id="f4">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>THE ENOCH WAY</span></div>
  <div class="ghost">ENOCH</div>
  <div class="h">왜 이 코드인지까지,<br><em>1:1로.</em></div>
  <div class="p">같은 곡도, 사람마다 다르게 가르칩니다.<br>ENOCH 기타 · 화성학 레슨은 입시 · 취미 · 성인 · 전문,<br>모든 과정이 <b>1:1</b>입니다.</div>
  {info}
  <div class="ft"><span>강사 소개 — 이승진</span><span>03 / 03</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'feed.html'), 'w', encoding='utf-8').write(head + feed)

# ---------- story ----------
s = open(os.path.join(BASE, 'story.html'), encoding='utf-8').read()
sh = s[:s.index('</style>')]
sh = sh.replace('강사 소개 한상희', '강사 소개 이승진').replace('한상희_01.jpg', '이승진_01.jpg').replace('background-position:55% 30%', 'background-position:50% 30%')
sh += '\n#D .body{top:520px}\n#D .sec{padding:52px 0}\n#D .sec li{font-size:34px;line-height:1.65}\n'
story = f'''</style></head><body>
<section class="s" id="R">
  <div class="top"><span class="lab g">ENOCH TEACHERS</span><span class="lab">GUITAR</span></div>
  <div class="side"><span></span><span class="lab g" style="writing-mode:vertical-rl;transform:rotate(180deg)">ENOCH MUSIC ACADEMY</span></div>
  <div class="ph"></div>
  <div class="en">LEE<br>SEUNGJIN</div>
  <div class="ko g">이승진</div>
  <div class="cv"><span class="lab g">CAREER</span>한양대 대학원 실용음악학과 예술석사<br>한양대 ERICA 실용음악학과 (기타 전공)<br>호원대 실용음악학부 객원교수 (2026)<br>GYMF 대상 (FM, 2010)</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Guitar · 화성학</span><span class="g">1:1 Lesson</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
<section class="s dt" id="D">
  <div class="top"><span class="lab g">ENOCH TEACHERS — GUITAR</span><span class="lab g">CAREER</span></div>
  <div class="nm">LEE SEUNGJIN<small>이승진</small></div>
  <div class="body">{sec("EDUCATION", EDU, "lab g")}{sec("TEACHING", TEA, "lab g")}{sec("AWARDS", AW, "lab g")}</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Guitar · 화성학</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'story.html'), 'w', encoding='utf-8').write(sh + story)
print('feed.html, story.html')
