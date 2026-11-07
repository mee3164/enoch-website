# 강사 소개 김민정: 한상희 feed.html/story.html의 스타일을 바탕으로 feed.html(3장), story.html(2장)을 만든다.
# python3 output/강사소개_김민정/build.py && CHROMIUM_PATH=... node output/강사소개_김민정/render.mjs
import os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '..', '강사소개_한상희')

EDU = ['단국대학교 뉴뮤직 <i>재즈피아노 학사</i>', '한양대학교 대학원 재즈연주학과 <i>석사과정 재학</i>']
TEA = ['천안 국제 재즈스트리트 <i>김민정 퀄텟</i>', '국립농업박물관 루닐스라운지', '부기우기 · 엔트리 55 · 재즈라운지 <i>등 재즈클럽 다수</i>']
AW = []


def sec(k, items, cls='k'):
    return f'<div class="sec"><span class="{cls}">{k}</span><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'


# ---------- feed ----------
f = open(os.path.join(BASE, 'feed.html'), encoding='utf-8').read()
head = f[:f.index('</style>')]
head = head.replace('강사 소개 한상희 피드', '강사 소개 김민정 피드').replace('한상희_01.jpg) 50% 28%', '김민정_01.jpg) 55% 42%')
head += '\n#f2 .sec{padding:48px 0}\n#f2 .sec li{font-size:28px}\n'
info = ('<div class="info"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span>'
        '<span style="text-align:right;font-family:var(--mono)">031 315 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">'
        'Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>')
band = 'JAZZ PIANO — 김민정 — ENOCH TEACHERS — ' * 4
feed = f'''</style></head><body>
<section class="s" id="f1">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — PIANO</span></div>
  <div class="ph"></div>
  <div class="col">
    <div class="cell"><div class="k">Subject</div><div class="v">Jazz Piano</div></div>
    <div class="cell"><div class="k">Lesson</div><div class="v">1:1</div></div>
    <div class="cell"><div class="k">Career</div><div class="t">단국대 뉴뮤직 재즈피아노 학사<br>한양대 대학원 재즈연주학과 석사과정<br>천안 국제 재즈스트리트 퀄텟 연주<br>재즈클럽 다수 연주</div></div>
  </div>
  <div class="en">KIM MIN JEONG</div>
  <div class="ko">김민정<span>재즈피아노</span></div>
  <div class="band"><span>{band}</span></div>
</section>
<section class="s" id="f2">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — PIANO</span></div>
  <div class="nm">KIM MIN JEONG<small>김민정</small></div>
  <div class="tbl">{sec("Education", EDU)}{sec("Live", TEA)}</div>
  <div class="ft"><span>강사 소개 — 김민정</span><span>02 / 03</span></div>
</section>
<section class="s dark" id="f4">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>THE ENOCH WAY</span></div>
  <div class="ghost">ENOCH</div>
  <div class="h">무대에서 쌓은 재즈를,<br><em>1:1로.</em></div>
  <div class="p">같은 곡도, 사람마다 다르게 가르칩니다.<br>ENOCH 피아노 레슨은 입시 · 취미 · 성인 · 전문,<br>모든 과정이 <b>1:1</b>입니다.</div>
  {info}
  <div class="ft"><span>강사 소개 — 김민정</span><span>03 / 03</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'feed.html'), 'w', encoding='utf-8').write(head + feed)

# ---------- story ----------
s = open(os.path.join(BASE, 'story.html'), encoding='utf-8').read()
sh = s[:s.index('</style>')]
sh = sh.replace('강사 소개 한상희', '강사 소개 김민정').replace('한상희_01.jpg', '김민정_01.jpg').replace('background-position:55% 30%', 'background-position:52% 45%')
sh += '\n#D .body{top:600px}\n#D .sec{padding:52px 0}\n#D .sec li{font-size:34px;line-height:1.65}\n'
story = f'''</style></head><body>
<section class="s" id="R">
  <div class="top"><span class="lab g">ENOCH TEACHERS</span><span class="lab">PIANO</span></div>
  <div class="side"><span></span><span class="lab g" style="writing-mode:vertical-rl;transform:rotate(180deg)">ENOCH MUSIC ACADEMY</span></div>
  <div class="ph"></div>
  <div class="en">KIM<br>MIN JEONG</div>
  <div class="ko g">김민정</div>
  <div class="cv"><span class="lab g">CAREER</span>단국대 뉴뮤직 재즈피아노 학사<br>한양대 대학원 재즈연주학과 석사과정<br>천안 국제 재즈스트리트 퀄텟 연주<br>재즈클럽 다수 연주</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Jazz Piano</span><span class="g">1:1 Lesson</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
<section class="s dt" id="D">
  <div class="top"><span class="lab g">ENOCH TEACHERS — PIANO</span><span class="lab g">CAREER</span></div>
  <div class="nm">KIM MIN JEONG<small>김민정</small></div>
  <div class="body">{sec("EDUCATION", EDU, "lab g")}{sec("LIVE", TEA, "lab g")}</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Jazz Piano</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'story.html'), 'w', encoding='utf-8').write(sh + story)
print('feed.html, story.html')
