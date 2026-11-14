# 스토리 2장 "비 오는 날의 연습" (1080×1920) — 작은 글자가 사진 사이로 흘러가는 브이로그 배치 (아이보리 · 블랙 · Pretendard)
# python3 output/릴스_비오는날/stories.py → stories.html → CHROMIUM_PATH=... node output/릴스_비오는날/stories.mjs → story_01.png, story_02.png
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def t(s, x, y, cls=''):
    return f'<div class="t {cls}" style="left:{x}px;top:{y}px">{s}</div>'


def photo(n, src, x, y, w, h, pos, below=False):
    ly = y + h + 14 if below else y - 40
    return (f'<div class="lab mono" style="left:{x}px;top:{ly}px">{n:02d}</div>'
            f'<div class="ph" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="src/{src}.jpg" style="object-position:{pos}"></div>')


FOOT = '<div class="ft mono">ENOCH MUSIC ACADEMY</div>'

# 글은 사진의 세로 가운데에 맞추고, 둘째 줄은 레퍼런스처럼 조금씩 밀어 흐름을 만든다
S = [
    # 1: 우산과 텀블러 (비 오는 창문) 하나 챙겨서 / 연습실로, — 비 오는 날의 / 연습 (피아노 위 텀블러)
    t('우산과 텀블러', 176, 700) + photo(1, 'rain', 400, 520, 300, 400, '50% 35%') + t('하나 챙겨서', 732, 700) + t('연습실로,', 800, 746)
    + t('비 오는 날의', 176, 1226, 'b') + t('연습', 440, 1272, 'b') + photo(2, 'coffee', 560, 1020, 400, 480, '22% 50%', below=True) + FOOT,
    # 2: 비 오는 날, (무대) 내 목소리에 / 집중하기 좋은 이유. — 덜 건조한 목 … 차분한 분위기 … (창가 식물)  [명사형 끝맺음]
    t('비 오는 날,', 200, 676, 'b') + photo(3, 'stage', 400, 500, 300, 380, '50% 40%') + t('내 목소리에', 732, 652, 'b') + t('집중하기 좋은 이유.', 732, 698, 'b')
    + t('덜 건조한 목,', 176, 1140) + t('편하게 나오는 소리.', 176, 1186) + photo(4, 'plant', 620, 1000, 340, 440, '22% 50%', below=True)
    + t('차분한 분위기 속', 236, 1296) + t('더 깊어지는 집중.', 296, 1342) + FOOT,
]

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>stories</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#ccc;font-family:P,sans-serif;word-break:keep-all}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:2px}}
section{{position:relative;width:1080px;height:1920px;background:#F4F1EA;color:#111;overflow:hidden;margin-bottom:20px}}
section>div{{position:absolute}}
.t{{font-size:30px;font-weight:400;letter-spacing:-.6px;white-space:nowrap}}
.t.b{{font-weight:600}}
.lab{{font-size:17px;color:#8A8A8A}}
.ph{{overflow:hidden;background:#E4DFD4}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.78) sepia(.08) contrast(1.02)}}
.ft{{left:0;right:0;top:1600px;text-align:center;font-size:17px;color:#8A8A8A}}
</style></head><body>{''.join(f'<section>{s}</section>' for s in S)}</body></html>'''
open(os.path.join(HERE, 'stories.html'), 'w', encoding='utf-8').write(html)
print('stories.html')
