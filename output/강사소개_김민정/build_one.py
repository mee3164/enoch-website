# 김민정 스토리 한 장 버전 (검정 · 아이보리): 김민주 story_one 디자인을 그대로 쓰고 글만 바꾼다.
# python3 output/강사소개_김민주/build.py (템플릿 갱신) → python3 output/강사소개_김민정/build_one.py → node output/강사소개_김민정/render_one.mjs
import os
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, '..', '강사소개_김민주')

BODY = '''<section class="s" id="O">
  <div class="top"><span class="lab g">ENOCH TEACHERS</span><span class="lab">JAZZ PIANO</span></div>
  <div class="sb">재즈피아노<br>1:1 Lesson</div>
  <div class="ph"></div>
  <div class="en">KIM MIN JEONG</div>
  <div class="ko">김민정</div>
  <div class="hl"><div><b>단국대학교 뉴뮤직 재즈피아노 학사</b></div><div><b>한양대학교 대학원 재즈연주학과</b><span>석사과정 재학</span></div></div>
  <div class="body"><div class="sec"><span class="lab g">LIVE</span><ul><li>천안 국제 재즈스트리트 <i>김민정 퀄텟 연주</i></li><li>국립농업박물관 루닐스라운지 <i>연주</i></li><li>부기우기 · 엔트리 55 · 재즈라운지 <i>등 다수 재즈클럽 연주</i></li></ul></div></div>
  <div class="bt"><span><span class="lime">●</span>&nbsp; Jazz Piano</span><span class="g">나만의 진짜 소리를 찾는 곳</span></div>
</section></body></html>
'''

for name in ('story_one', 'story_one_ivory'):
    t = open(os.path.join(SRC, name + '.html'), encoding='utf-8').read()
    head = t[:t.index('<section')]
    head = head.replace('김민주_01.jpg', '김민정_01.jpg').replace('강사 소개 김민주', '강사 소개 김민정')
    head = head.replace('background-position:50% 22%', 'background-position:62% 38%')
    head += '\n<style>#O .ph{width:620px;height:780px;top:300px}\n#O .en{top:1100px;font-size:100px;line-height:1}\n#O .ko{top:1210px}\n#O .hl{top:1258px}\n#O .body{top:1508px}\n#O .sec{padding:16px 0}</style>\n'
    open(os.path.join(HERE, name + '.html'), 'w', encoding='utf-8').write(head + BODY)
print('story_one.html, story_one_ivory.html')
