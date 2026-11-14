# 카드뉴스 "비 오는 날의 연습" (1080×1350, 6장) — 릴스와 같은 브이로그형: 글 사이 대괄호 안 실제 사진
# python3 output/릴스_비오는날/cards.py → cards.html → CHROMIUM_PATH=... node output/릴스_비오는날/cards.mjs → card_01.png ~
import os, json
HERE = os.path.dirname(os.path.abspath(__file__))
B = json.load(open(os.path.join(HERE, '..', '..', 'templates', 'brand.json'), encoding='utf-8'))

N = 6


def bracket(x, y, w, h):
    g, t = 26, 24
    top, bot = y - 20, y + h + 20
    return (f'<svg class="br" style="left:{x-g-t}px;top:{top}px" width="{t+2}" height="{bot-top}"><path d="M{t} 1 H 1 V {bot-top-1} H {t}"/></svg>'
            f'<svg class="br" style="left:{x+w+g}px;top:{top}px" width="{t+2}" height="{bot-top}"><path d="M0 1 H {t+1} V {bot-top-1} H 0"/></svg>')


def photo(n, src, x, y, w, h, pos):
    return (f'<div class="lab mono" style="left:{x}px;top:{y-56}px">{n:02d}</div>'
            f'<div class="ph" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="src/{src}.jpg" style="object-position:{pos}"></div>'
            )


def tx(t, x, y, cls=''):
    return f'<div class="tx {cls}" style="left:{x}px;top:{y}px">{t}</div>'


def card(i, body, dark=False):
    return (f'<section class="{"dk" if dark else ""}"><div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>PRACTICE NOTE — RAINY DAY</span></div>'
            f'{body}<div class="ft"><span>비 오는 날의 연습</span><span class="mono">{i:02d} / {N:02d}</span></div></section>')


C = [
    card(1, tx('비 오는 날의<br>연습', 84, 200, 'ttl') + tx('우산 하나,<br>텀블러 하나.', 84, 960, 'sm')
         + photo(1, 'rain', 560, 520, 400, 540, '50% 40%')),
    card(2, tx('습도가 높은 날은', 84, 230) + photo(2, 'plant', 130, 440, 480, 380, '30% 50%')
         + tx('목이 덜<br>건조합니다', 560, 900)),
    card(3, tx('빗소리는<br>일정해서', 84, 230) + photo(3, 'guitarroom', 560, 300, 400, 440, '55% 50%')
         + tx('다른 소음이<br>덜 들려요', 300, 880)),
    card(4, tx('텀블러 속 커피가<br>반쯤 줄어드는 동안', 84, 200) + photo(4, 'coffee', 500, 500, 440, 440, '40% 50%')
         + tx('같은 소절을<br>몇 번 더.', 84, 1010)),
    card(5, tx('오늘은 내 소리가', 84, 200) + photo(5, 'rack', 130, 400, 300, 320, '50% 70%')
         + photo(6, 'stage', 600, 520, 360, 420, '50% 40%') + tx('조금 더 잘<br>들리는 날.', 84, 880)),
    card(6, '<div class="ghost">ENOCH</div>'
         f'<div class="sig">{B.get("signature", "나만의 진짜 소리를 찾는 곳.")}</div>'
         '<div class="info">'
         '<p><b>주소</b>경기도 시흥시 은행로 157 2층</p>'
         '<p><b>전화</b>031 315 3666</p>'
         '<p><b>운영</b>평일 13:00–22:00 · 토 10:00–18:00 · 일요일 휴무</p>'
         '<p><b>과목</b>Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡 — 1:1 레슨</p>'
         '<p><b>예약</b>체험수업 네이버 플레이스 · 방문 상담 네이버 톡톡 · 카카오톡 채널 · 전화</p></div>', dark=True),
]

html = f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>cards</title><style>
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}}
@font-face{{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#ccc;font-family:P,sans-serif;word-break:keep-all}}
.mono{{font-family:"IBM Plex Mono","DejaVu Sans Mono",monospace;letter-spacing:3px}}
section{{position:relative;width:1080px;height:1350px;background:#F1EDE4;color:#111;overflow:hidden;margin-bottom:20px}}
section.dk{{background:#111;color:#F1EDE4}}
.hd{{position:absolute;left:84px;right:84px;top:72px;display:flex;justify-content:space-between;font-size:20px;padding-bottom:16px;border-bottom:1.5px solid currentColor}}
.ft{{position:absolute;left:84px;right:84px;bottom:64px;display:flex;justify-content:space-between;font-size:22px;color:#8A8A8A}}
.ft .mono{{font-size:20px}}
.tx{{position:absolute;font-size:56px;font-weight:400;letter-spacing:-2px;line-height:1.18;white-space:nowrap}}
.tx.ttl{{font-size:88px;font-weight:600;letter-spacing:-4px;line-height:1.08}}
.tx.sm{{font-size:40px;letter-spacing:-1.5px;color:#555}}
.lab{{position:absolute;font-size:22px;color:#8A8A8A}}
.ph{{position:absolute;overflow:hidden;background:#E4DFD4}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.82) contrast(1.02)}}
.br{{position:absolute;overflow:visible}}
.br path{{fill:none;stroke:#111;stroke-width:3}}
.ghost{{position:absolute;left:60px;top:170px;font-size:270px;font-weight:700;letter-spacing:-12px;color:#262421}}
.sig{{position:absolute;left:84px;top:560px;font-size:52px;font-weight:600;letter-spacing:-2.5px}}
.info{{position:absolute;left:84px;right:84px;top:820px;font-size:24px;line-height:1.9;color:#B9B4AA;border-top:1px solid #444;padding-top:24px}}
.info b{{display:inline-block;width:90px;font-weight:600;color:#F1EDE4}}
</style></head><body>{''.join(C)}</body></html>'''
open(os.path.join(HERE, 'cards.html'), 'w', encoding='utf-8').write(html)
print('cards.html')
