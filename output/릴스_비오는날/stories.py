# 스토리 2장 "비 오는 날의 연습" (1080×1920) — 카드뉴스·릴스와 같은 브이로그형 (아이보리 · 블랙 · Pretendard, 사진 테두리 없음)
# python3 output/릴스_비오는날/stories.py → stories.html → CHROMIUM_PATH=... node output/릴스_비오는날/stories.mjs → story_01.png, story_02.png
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def photo(n, src, x, y, w, h, pos):
    return (f'<div class="lab mono" style="left:{x}px;top:{y-48}px">{n:02d}</div>'
            f'<div class="ph" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="src/{src}.jpg" style="object-position:{pos}"></div>')


def story(i, body):
    return (f'<section><div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>RAINY DAY {i:02d} / 02</span></div>{body}'
            '<div class="ft"><span>에녹실용음악학원 시흥점</span><span class="mono">031 315 3666</span></div></section>')


S = [
    story(1, '<div class="sub" style="left:100px;top:330px">우산과 텀블러 하나 챙겨서 연습실로,</div>'
             '<div class="ttl" style="left:96px;top:400px">비 오는 날의<br>연습</div>'
             + photo(1, 'rain', 100, 720, 480, 640, '50% 35%')
             + photo(2, 'coffee', 620, 980, 360, 420, '22% 50%')),
    story(2, '<div class="hl" style="left:100px;top:330px">비 오는 날은<br>내 소리에 집중하기 좋습니다.</div>'
             '<div class="sub" style="left:100px;top:510px;line-height:1.55">목이 덜 건조해서 소리 내기 편하고,<br>빗소리는 일정해서 다른 소음이 덜 들려요.</div>'
             + photo(3, 'stage', 100, 760, 520, 560, '50% 40%')
             + photo(4, 'plant', 660, 1000, 320, 420, '22% 50%')),
]

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>stories</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#ccc;font-family:P,sans-serif;word-break:keep-all}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
section{{position:relative;width:1080px;height:1920px;background:#F1EDE4;color:#111;overflow:hidden;margin-bottom:20px}}
section>div{{position:absolute}}
.hd{{left:100px;right:100px;top:220px;display:flex;justify-content:space-between;font-size:20px;padding-bottom:16px;border-bottom:1.5px solid #111}}
.ft{{left:100px;right:100px;top:1560px;display:flex;justify-content:space-between;font-size:24px;color:#8A8A8A;padding-top:18px;border-top:1px solid #C9C3B8}}
.ft .mono{{font-size:22px;color:#111}}
.sub{{font-size:40px;color:#555;letter-spacing:-1.5px;white-space:nowrap}}
.ttl{{font-size:96px;font-weight:600;letter-spacing:-4.5px;line-height:1.1}}
.hl{{font-size:60px;font-weight:600;letter-spacing:-2.5px;line-height:1.25;white-space:nowrap}}
.lab{{font-size:20px;color:#8A8A8A}}
.ph{{overflow:hidden;background:#E4DFD4}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.82) contrast(1.02)}}
</style></head><body>{''.join(S)}</body></html>'''
open(os.path.join(HERE, 'stories.html'), 'w', encoding='utf-8').write(html)
print('stories.html')
