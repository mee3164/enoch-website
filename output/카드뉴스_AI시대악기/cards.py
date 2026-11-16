# 카드뉴스 "AI가 곡을 만드는 시대, 악기를 배우는 것이 더 중요한 이유" (1080×1350, 8장)
# 01 메인은 연주 사진(얼굴 아래로 자름, src/main.jpg — 인물 사진이라 저장소에 올리지 않음), 03 · 04 · 06은 공간 사진. 05 · 08은 검정, 02 · 07은 글만.
# python3 output/카드뉴스_AI시대악기/cards.py → cards.html → CHROMIUM_PATH=... node output/카드뉴스_AI시대악기/cards.mjs → 01.png ~ 08.png
import os
HERE = os.path.dirname(os.path.abspath(__file__))
N = 8
TOPIC = 'AI 시대, 악기를 배우는 이유'


def ph(src, x, y, w, h, pos='50% 50%', extra=''):
    path = src if '/' in src else f'../../images/공간/{src}'
    return f'<div class="ph" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"><img src="{path}" style="object-position:{pos};{extra}"></div>'


def card(i, body, dark=False):
    return (f'<section class="{"dk" if dark else ""}"><div class="hd mono"><span>ENOCH MUSIC ACADEMY</span><span>PRACTICE NOTE — AI &amp; MUSIC</span></div>'
            f'{body}<div class="ft"><span>{TOPIC}</span><span class="mono">{i:02d} / {N:02d}</span></div></section>')


def reason(n, title, photo, body, body_top):
    return (f'<div class="lab mono" style="top:170px">REASON {n:02d}</div>'
            f'<div class="h2" style="top:210px">{title}</div>{photo}'
            f'<div class="p" style="top:{body_top}px">{body}</div>')


C = [
    card(1, ph('src/main.jpg', 84, 150, 912, 760, '50% 40%', 'filter:saturate(.8) sepia(.06) brightness(1.18)')
         + '<div class="sub" style="top:968px">AI가 곡을 만드는 시대,</div>'
         + '<div class="h1" style="top:1020px">악기를 배우는 것이<br>더 중요한 이유</div>'),
    card(2, '<div class="p big" style="top:330px">버튼 몇 번이면<br>노래 한 곡이 완성되는 요즘.</div>'
         '<div class="p big" style="top:560px">곡을 갖는 것은<br>결과 하나를 얻는 일이지만,</div>'
         '<div class="p big" style="top:790px">직접 연주할 수 있게 되는 건<br><b>내가 듣는 세계가 넓어지는 일입니다.</b></div>'),
    card(3, reason(1, '듣는 귀가 달라집니다', ph('기타앰프_01.jpg', 84, 330, 912, 560, '50% 55%'),
                   '직접 연주해 본 사람은 음악을 다르게 듣습니다.<br>좋아하던 노래를 다시 들었을 때,<br>처음 듣는 소리가 들리는 것.<br>그건 직접 해 본 사람만 얻는 귀예요.', 940)),
    card(4, reason(2, '나만의 소리는<br>대신 정해 줄 수 없어요', ph('보컬부스_01.jpg', 84, 410, 912, 520, '50% 45%'),
                   '같은 곡도 연주하는 사람마다 다르게 들립니다.<br>어디서 숨을 쉬고, 어디에 힘을 줄지.<br>그 선택이 쌓여 내 소리가 됩니다.', 980)),
    card(5, '<div class="lab mono" style="top:470px;color:#8A8A8A">REASON 03</div>'
         '<div class="h0" style="top:520px">과정이<br>사람을 바꿉니다</div>', dark=True),
    card(6, '<div class="p" style="top:200px">어제 안 되던 소절이<br>오늘은 조금 되는 날.<br>그런 날이 쌓이면<br><b>음악만큼, 나도 달라집니다.</b></div>'
         + ph('피아노방_01.jpg', 84, 520, 912, 480, '50% 62%')
         + '<div class="p" style="top:1050px">결과는 대신 만들어 줄 수 있어도<br>그 시간까지 대신 겪어 줄 수는 없거든요.</div>'),
    card(7, '<div class="p big" style="top:470px">누구나 결과를 가질 수 있는 시대일수록,<br><b>직접 소리를 낼 수 있는 사람의 가치는<br>더 커집니다.</b></div>'),
    card(8, '<div class="ghost">ENOCH</div>'
         '<div class="sig">같은 곡도, 사람마다 다르게.<br>나만의 진짜 소리를 찾는 곳.</div>'
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
section>div{{position:absolute;left:84px}}
.hd{{right:84px;top:72px;display:flex;justify-content:space-between;font-size:20px;padding-bottom:16px;border-bottom:1.5px solid currentColor}}
.ft{{right:84px;bottom:64px;display:flex;justify-content:space-between;font-size:22px;color:#8A8A8A}}
.ft .mono{{font-size:20px}}
.lab{{font-size:20px;color:#8A8A8A}}
.sub{{font-size:34px;color:#555;letter-spacing:-1px}}
.h1{{font-size:64px;font-weight:600;letter-spacing:-2.5px;line-height:1.2}}
.h2{{font-size:52px;font-weight:600;letter-spacing:-2px;line-height:1.22}}
.h0{{font-size:96px;font-weight:600;letter-spacing:-4px;line-height:1.15}}
.p{{right:84px;font-size:32px;font-weight:400;color:#333;letter-spacing:-.8px;line-height:1.6}}
.p.big{{font-size:42px;color:#111;letter-spacing:-1.5px;line-height:1.45}}
.p b{{font-weight:600;color:#111}}
.ph{{overflow:hidden;background:#E4DFD4}}
.ph img{{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.8) sepia(.06)}}
.ghost{{left:60px!important;top:170px;font-size:270px;font-weight:700;letter-spacing:-12px;color:#262421}}
.sig{{top:540px;font-size:50px;font-weight:600;letter-spacing:-2px;line-height:1.35}}
.info{{right:84px;top:840px;font-size:24px;line-height:1.9;color:#B9B4AA;border-top:1px solid #444;padding-top:24px}}
.info b{{display:inline-block;width:90px;font-weight:600;color:#F1EDE4}}
</style></head><body>{''.join(C)}</body></html>'''
open(os.path.join(HERE, 'cards.html'), 'w', encoding='utf-8').write(html)
print('cards.html')
