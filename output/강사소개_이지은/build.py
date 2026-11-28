# 강사 소개 이지은: 한상희 feed.html/story.html의 스타일을 바탕으로 feed.html(3장), story.html(2장)을 만든다.
# python3 output/강사소개_이지은/build.py && CHROMIUM_PATH=... node output/강사소개_이지은/render.mjs
import os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '..', '강사소개_한상희')

EDU = ['한양여자대학교 실용음악과 <i>보컬 전공</i>', '<i>장혜진 · 손무현 사사</i>']
WK = ['시흥 에녹실용음악학원 보컬 강사 <i>(현)</i>', '다수 실용음악학원 보컬 강사 <i>(전)</i>']


def sec(k, items, cls='k'):
    return f'<div class="sec"><span class="{cls}">{k}</span><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'


# ---------- feed ----------
f = open(os.path.join(BASE, 'feed.html'), encoding='utf-8').read()
head = f[:f.index('</style>')]
head = head.replace('강사 소개 한상희 피드', '강사 소개 이지은 피드').replace('한상희_01.jpg) 50% 28%', '이지은_01.jpg) 50% 22%')
head += '\n#f2 .sec{padding:36px 0}\n#f2 .sec li{font-size:28px}\n'
info = ('<div class="info"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span>'
        '<span style="text-align:right;font-family:var(--mono)">031 315 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">'
        'Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>')
band = 'VOCAL — 이지은 — ENOCH TEACHERS — ' * 4
feed = f'''</style></head><body>
<section class="s" id="f1">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — VOCAL</span></div>
  <div class="ph"></div>
  <div class="col">
    <div class="cell"><div class="k">Subject</div><div class="v">Vocal</div></div>
    <div class="cell"><div class="k">Lesson</div><div class="v">1:1</div></div>
    <div class="cell"><div class="k">Career</div><div class="t">한양여대 실용음악과 보컬 전공<br>장혜진 · 손무현 사사<br>실용음악학원 보컬 강사 경력</div></div>
  </div>
  <div class="en">JI EUN LEE</div>
  <div class="ko">이지은<span>보컬</span></div>
  <div class="band"><span>{band}</span></div>
</section>
<section class="s" id="f2">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — VOCAL</span></div>
  <div class="nm">JI EUN LEE<small>이지은</small></div>
  <div class="tbl">{sec("Education", EDU)}{sec("Teaching", WK)}</div>
  <div class="ft"><span>강사 소개 — 이지은</span><span>02 / 03</span></div>
</section>
<section class="s dark" id="f4">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>THE ENOCH WAY</span></div>
  <div class="ghost">ENOCH</div>
  <div class="h">내 목소리에 맞는 노래를,<br><em>1:1로.</em></div>
  <div class="p">같은 곡도, 사람마다 다르게 가르칩니다.<br>ENOCH 보컬 레슨은 입시 · 취미 · 성인 · 전문,<br>모든 과정이 <b>1:1</b>입니다.</div>
  {info}
  <div class="ft"><span>강사 소개 — 이지은</span><span>03 / 03</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'feed.html'), 'w', encoding='utf-8').write(head + feed)

# ---------- story ----------
s = open(os.path.join(BASE, 'story.html'), encoding='utf-8').read()
sh = s[:s.index('</style>')]
sh = sh.replace('강사 소개 한상희', '강사 소개 이지은').replace('한상희_01.jpg', '이지은_01.jpg').replace('background-position:55% 30%', 'background-position:50% 20%')
sh += '\n#D .body{top:520px}\n#D .sec{padding:52px 0}\n#D .sec li{font-size:34px;line-height:1.65}\n'
story = f'''</style></head><body>
<section class="s" id="R">
  <div class="top"><span class="lab g">ENOCH TEACHERS</span><span class="lab">VOCAL</span></div>
  <div class="side"><span></span><span class="lab g" style="writing-mode:vertical-rl;transform:rotate(180deg)">ENOCH MUSIC ACADEMY</span></div>
  <div class="ph"></div>
  <div class="en">JI EUN<br>LEE</div>
  <div class="ko g">이지은</div>
  <div class="cv"><span class="lab g">CAREER</span>한양여대 실용음악과 (보컬 전공)<br>장혜진 · 손무현 사사<br>다수 실용음악학원 보컬 강사 (전)</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Vocal</span><span class="g">1:1 Lesson</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
<section class="s dt" id="D">
  <div class="top"><span class="lab g">ENOCH TEACHERS — VOCAL</span><span class="lab g">CAREER</span></div>
  <div class="nm">JI EUN LEE<small>이지은</small></div>
  <div class="body">{sec("EDUCATION", EDU, "lab g")}{sec("TEACHING", WK, "lab g")}</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Vocal</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'story.html'), 'w', encoding='utf-8').write(sh + story)
print('feed.html, story.html')
