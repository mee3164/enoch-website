# 스토리 2장 "비 오는 날의 연습" (1080×1920) — 작은 글자가 사진 사이로 흘러가는 브이로그 배치 (아이보리 · 블랙 · Pretendard)
# python3 output/릴스_비오는날/stories.py → stories.html → CHROMIUM_PATH=... node output/릴스_비오는날/stories.mjs → story_01.png, story_02.png
import os
HERE = os.path.dirname(os.path.abspath(__file__))


def t(s, x, y, cls=''):
    return f'<div class="t {cls}" style="left:{x}px;top:{y}px">{s}</div>'


def photo(n, src, x, y, w, h, pos, below=False, paren=False):
    ly = y + h + 14 if below else y - 40
    out = (f'<div class="lab mono" style="left:{x}px;top:{ly}px">{n:02d}</div>'
           f'<div class="ph" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="src/{src}.jpg" style="object-position:{pos}"></div>')
    if paren:   # 사진 양옆 얇은 둥근 괄호 (사진 높이의 72%)
        ph = round(h * 0.72); top = y + (h - ph) // 2
        out += (f'<svg class="pr" style="left:{x-46}px;top:{top}px" width="30" height="{ph}"><path d="M28 2 Q 2 {ph/2} 28 {ph-2}"/></svg>'
                f'<svg class="pr" style="left:{x+w+16}px;top:{top}px" width="30" height="{ph}"><path d="M2 2 Q 28 {ph/2} 2 {ph-2}"/></svg>')
    return out


FOOT = '<div class="ft mono">ENOCH MUSIC ACADEMY</div>'


# 괄호는 첫 사진(비 오는 창문)에만. 괄호 자리만큼 그 줄의 글을 벌린다
d = 36
S = [
    # 1: 우산과 텀블러 ( 비 오는 창문 ) 하나 챙겨서 / 연습실로, — 몰입하기 좋은 / 차분한 분위기. (피아노 위 텀블러)
    t('우산과 텀블러', 76, 700) + photo(1, 'rain', 320, 420, 440, 580, '50% 35%', paren=True) + t('하나 챙겨서', 830, 700) + t('연습실로,', 880, 746)
    + t('몰입하기 좋은', 176, 1286) + t('차분한 분위기.', 300, 1332) + photo(2, 'coffee', 580, 1100, 380, 420, '22% 50%', below=True) + FOOT,
    # 2: 오늘 같은 날, (무대) 내 목소리에 / 집중하기 좋은 이유. — 덜 건조한 목, / 편하게 나오는 소리. (창가 식물)  [명사형 끝맺음]
    t('오늘 같은 날,', 176, 676, 'b') + photo(3, 'stage', 400, 500, 300, 380, '50% 40%') + t('내 목소리에', 732, 652, 'b') + t('집중하기 좋은 이유.', 732, 698, 'b')
    + t('덜 건조한 목,', 176, 1196) + t('편하게 나오는 소리.', 236, 1242) + photo(4, 'plant', 620, 1000, 340, 440, '22% 50%', below=True)
    + FOOT,
]
NAMES = ['story_01', 'story_02']

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
.pr{{position:absolute;overflow:visible}}
.pr path{{fill:none;stroke:#111;stroke-width:2.5;stroke-linecap:round}}
.ft{{left:0;right:0;top:1600px;text-align:center;font-size:17px;color:#8A8A8A}}
</style></head><body>{''.join(f'<section data-name="{n}">{s}</section>' for n, s in zip(NAMES, S))}</body></html>'''
open(os.path.join(HERE, 'stories.html'), 'w', encoding='utf-8').write(html)
print('stories.html')
