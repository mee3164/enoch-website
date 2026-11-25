# 강사 소개 송은하: 한상희 feed.html/story.html의 스타일을 바탕으로 feed.html(3장), story.html(2장)을 만든다.
# python3 output/강사소개_송은하/build.py && CHROMIUM_PATH=... node output/강사소개_송은하/render.mjs
import os
HERE = os.path.dirname(os.path.abspath(__file__))
BASE = os.path.join(HERE, '..', '강사소개_한상희')

EDU = ['서울예술대학교 실용음악과 <i>작곡 전공 졸업</i>', '백석예술대학교 실용음악과 <i>피아노 전공 졸업</i>']
WK = ['김다빈 EP 「별빛 달빛 그리움」', 'BOYEH 「그래, 천천히 안녕」', '<i>음원 세션 및 작 · 편곡 참여</i>']
CH = ['왕성교회 Sunday Main Service <i>· 9 yrs</i>', '주안장로교회 Sunday Main Service <i>· (전) 4 yrs</i>']


def sec(k, items, cls='k'):
    return f'<div class="sec"><span class="{cls}">{k}</span><ul>' + ''.join(f'<li>{x}</li>' for x in items) + '</ul></div>'


# ---------- feed ----------
f = open(os.path.join(BASE, 'feed.html'), encoding='utf-8').read()
head = f[:f.index('</style>')]
head = head.replace('강사 소개 한상희 피드', '강사 소개 송은하 피드').replace('한상희_01.jpg) 50% 28%', '송은하_01.jpg) 50% 26%')
head += '\n#f2 .sec{padding:36px 0}\n#f2 .sec li{font-size:28px}\n'
info = ('<div class="info"><span>에녹실용음악학원 시흥점<br><span style="color:#9A958C">경기도 시흥시 은행로 157 2층</span></span>'
        '<span style="text-align:right;font-family:var(--mono)">031 315 3666<br><span style="color:#9A958C;font-family:P,sans-serif;font-size:19px">'
        'Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>')
band = 'PIANO — 송은하 — ENOCH TEACHERS — ' * 4
feed = f'''</style></head><body>
<section class="s" id="f1">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — PIANO</span></div>
  <div class="ph"></div>
  <div class="col">
    <div class="cell"><div class="k">Subject</div><div class="v">Piano · 작곡 · 화성학</div></div>
    <div class="cell"><div class="k">Lesson</div><div class="v">1:1</div></div>
    <div class="cell"><div class="k">Career</div><div class="t">서울예대 실용음악과 작곡 전공<br>백석예대 실용음악과 피아노 전공<br>김다빈 · BOYEH 세션 · 작편곡<br>Worship Pianist | 왕성교회 · 9 yrs</div></div>
  </div>
  <div class="en">SONG EUN HA</div>
  <div class="ko">송은하<span>피아노 · 작곡 · 화성학</span></div>
  <div class="band"><span>{band}</span></div>
</section>
<section class="s" id="f2">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH TEACHERS — PIANO</span></div>
  <div class="nm">SONG EUN HA<small>송은하</small></div>
  <div class="tbl">{sec("Education", EDU)}{sec("Works", WK)}{sec("Worship Pianist", CH)}</div>
  <div class="ft"><span>강사 소개 — 송은하</span><span>02 / 03</span></div>
</section>
<section class="s dark" id="f4">
  <div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>THE ENOCH WAY</span></div>
  <div class="ghost">ENOCH</div>
  <div class="h">치는 법에서, 쓰는 법까지.<br><em>1:1로.</em></div>
  <div class="p">같은 곡도, 사람마다 다르게 가르칩니다.<br>ENOCH 피아노 · 작곡 · 화성학 레슨은 입시 · 취미 · 성인 · 전문,<br>모든 과정이 <b>1:1</b>입니다.</div>
  {info}
  <div class="ft"><span>강사 소개 — 송은하</span><span>03 / 03</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'feed.html'), 'w', encoding='utf-8').write(head + feed)

# ---------- story ----------
s = open(os.path.join(BASE, 'story.html'), encoding='utf-8').read()
sh = s[:s.index('</style>')]
sh = sh.replace('강사 소개 한상희', '강사 소개 송은하').replace('한상희_01.jpg', '송은하_01.jpg').replace('background-position:55% 30%', 'background-position:50% 24%')
sh += '\n#D .body{top:520px}\n#D .sec{padding:52px 0}\n#D .sec li{font-size:34px;line-height:1.65}\n'
story = f'''</style></head><body>
<section class="s" id="R">
  <div class="top"><span class="lab g">ENOCH TEACHERS</span><span class="lab">PIANO</span></div>
  <div class="side"><span></span><span class="lab g" style="writing-mode:vertical-rl;transform:rotate(180deg)">ENOCH MUSIC ACADEMY</span></div>
  <div class="ph"></div>
  <div class="en">SONG<br>EUN HA</div>
  <div class="ko g">송은하</div>
  <div class="cv"><span class="lab g">CAREER</span>서울예대 실용음악과 (작곡 전공)<br>백석예대 실용음악과 (피아노 전공)<br>김다빈 · BOYEH 음원 세션 · 작편곡<br>Worship Pianist | 왕성교회 · 9 yrs</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Piano · 작곡 · 화성학</span><span class="g">1:1 Lesson</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
<section class="s dt" id="D">
  <div class="top"><span class="lab g">ENOCH TEACHERS — PIANO</span><span class="lab g">CAREER</span></div>
  <div class="nm">SONG EUN HA<small>송은하</small></div>
  <div class="body">{sec("EDUCATION", EDU, "lab g")}{sec("WORKS", WK, "lab g")}{sec("WORSHIP PIANIST", CH, "lab g")}</div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Piano · 작곡 · 화성학</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section>
</body></html>
'''
open(os.path.join(HERE, 'story.html'), 'w', encoding='utf-8').write(sh + story)
print('feed.html, story.html')
