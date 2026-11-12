# 강사 소개 김민주: 한상희 feed.html/story.html의 스타일을 바탕으로 feed.html(3장), story.html(2장)을 만든다.
# python3 output/강사소개_김민주/build.py && CHROMIUM_PATH=... node output/강사소개_김민주/render.mjs
import os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '..', '강사소개_한상희')

EDU = ['서울예술대학교 <i>실용음악과 졸업</i>', 'SJA 실용음악과 <i>학사 졸업</i>', '실기교사 <i>자격증 취득</i>']
WORK = ['이무진 「과제곡」 <i>편곡 · 유튜브 영상 오르간 세션 · 코러스</i>', '진화영 싱글 「빈 밤」 <i>피아노 레코딩</i>', '표표 「Boat」 <i>피아노 레코딩</i>', '서로의 서로 「그 때 그 약속은」 · 「그 때 그 노래가」 <i>발매</i>']
LIVE = ['언플러그드 · 웨스트브릿지 · 롤링홀 등 <i>클럽 공연 기획 · 아티스트 참여</i>']
TEACH = ['은평생활문화센터 <i>소속 강사</i>']
EDU_S = ['SJA 실용음악과 <i>학사 졸업</i>', '실기교사 <i>자격증 취득</i>']
WORK_S = WORK[1:]
AW = []


def sec(k, items, cls='k'):
    return f'<div class="sec"><span class="{cls}">{k}</span><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'


# ---------- feed ----------
f = open(os.path.join(BASE, 'feed.html'), encoding='utf-8').read()
head = f[:f.index('</style>')]
head = head.replace('강사 소개 한상희 피드', '강사 소개 김민주 피드').replace('한상희_01.jpg) 50% 28%', '김민주_01.jpg) 50% 22%')
head += '\n#f2 .sec{padding:30px 0}\n#f2 .sec li{font-size:25px}\n'
info = ('<div class="info"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span>'
        '<span style="text-align:right;font-family:var(--mono)">031 315 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">'
        'Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>')
band = 'SINGER-SONGWRITER — 김민주 — ENOCH TEACHERS — ' * 4
feed = f'''</style></head><body>
<section class="s" id="f1">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — COMPOSITION</span></div>
  <div class="ph"></div>
  <div class="col">
    <div class="cell"><div class="k">Subject</div><div class="v">Composition</div></div>
    <div class="cell"><div class="k">Lesson</div><div class="v">1:1</div></div>
    <div class="cell"><div class="k">Career</div><div class="t">서울예대 실용음악과 졸업<br>이무진 「과제곡」 편곡 · 오르간 세션<br>서로의 서로 앨범 발매<br>실기교사 자격증</div></div>
  </div>
  <div class="en">KIM MIN JU</div>
  <div class="ko">김민주<span>작곡 · 싱어송라이터</span></div>
  <div class="band"><span>{band}</span></div>
</section>
<section class="s" id="f2">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — COMPOSITION</span></div>
  <div class="nm">KIM MIN JU<small>김민주</small></div>
  <div class="tbl">{sec("Education", EDU)}{sec("Works", WORK)}{sec("Live", LIVE)}</div>
  <div class="ft"><span>강사 소개 — 김민주</span><span>02 / 03</span></div>
</section>
<section class="s dark" id="f4">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>THE ENOCH WAY</span></div>
  <div class="ghost">ENOCH</div>
  <div class="h">만들고, 부르는 법을.<br><em>1:1로.</em></div>
  <div class="p">같은 곡도, 사람마다 다르게 가르칩니다.<br>ENOCH 작곡 · 싱어송라이터 레슨은 입시 · 취미 · 성인 · 전문,<br>모든 과정이 <b>1:1</b>입니다.</div>
  {info}
  <div class="ft"><span>강사 소개 — 김민주</span><span>03 / 03</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'feed.html'), 'w', encoding='utf-8').write(head + feed)

# ---------- story ----------
s = open(os.path.join(BASE, 'story.html'), encoding='utf-8').read()
sh = s[:s.index('</style>')]
sh = sh.replace('강사 소개 한상희', '강사 소개 김민주').replace('한상희_01.jpg', '김민주_01.jpg').replace('background-position:55% 30%', 'background-position:50% 25%')
sh += '\n#D .hl{position:absolute;left:80px;right:80px;top:430px}\n#D .hl div{padding:30px 0;border-bottom:1px solid rgba(255,255,255,.22)}\n#D .hl b{display:block;font-size:52px;font-weight:700;letter-spacing:-1.5px;line-height:1.2}\n#D .hl span{display:block;font-size:30px;color:#B9B4AA;margin-top:10px}\n#D .body{top:850px}\n#D .sec{padding:28px 0}\n#D .sec li{font-size:28px;line-height:1.55}\n#R .cv .hi{display:block;font-size:34px;font-weight:700;color:#F3F1EC;line-height:1.3;margin-bottom:18px}\n'
story = f'''</style></head><body>
<section class="s" id="R">
  <div class="top"><span class="lab g">ENOCH TEACHERS</span><span class="lab">COMPOSITION</span></div>
  <div class="side"><span></span><span class="lab g" style="writing-mode:vertical-rl;transform:rotate(180deg)">ENOCH MUSIC ACADEMY</span></div>
  <div class="ph"></div>
  <div class="en">KIM<br>MIN JU</div>
  <div class="ko g">김민주</div>
  <div class="cv"><span class="lab g">CAREER</span><span class="hi">서울예술대학교<br>실용음악과 졸업</span><span class="hi">이무진 「과제곡」<br>편곡 · 오르간 세션</span></div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Composition · Singer-Songwriter</span><span class="g">1:1 Lesson</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
<section class="s dt" id="D">
  <div class="top"><span class="lab g">ENOCH TEACHERS — COMPOSITION</span><span class="lab g">CAREER</span></div>
  <div class="nm">KIM MIN JU<small>김민주</small></div>
  <div class="hl"><div><b>서울예술대학교 실용음악과 졸업</b></div><div><b>이무진 「과제곡」 편곡</b><span>유튜브 「과제곡」 영상 오르간 세션 · 코러스 참여</span></div></div>
  <div class="body">{sec("EDUCATION", EDU_S, "lab g")}{sec("WORKS", WORK_S, "lab g")}{sec("LIVE", LIVE, "lab g")}{sec("TEACHING", TEACH, "lab g")}</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Composition · Singer-Songwriter</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'story.html'), 'w', encoding='utf-8').write(sh + story)
print('feed.html, story.html')
