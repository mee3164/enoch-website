# 선교 장학 이벤트 포스터 (feed 1080x1350, story 1080x1920)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
FONT='''@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Medium.woff2);font-weight:500}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}'''
CSS='''*{box-sizing:border-box;margin:0;padding:0}
:root{--iv:#F1EDE4;--bk:#111;--g:#8A8A8A;--b:#55524D;--sg:#DCE2D3;--mono:"IBM Plex Mono","DejaVu Sans Mono",monospace;--en:"Helvetica Neue",Helvetica,Arial,"Liberation Sans",P,sans-serif}
.s{width:1080px;position:relative;overflow:hidden;background:var(--iv);color:var(--bk);font-family:P,sans-serif;margin-bottom:40px;word-break:keep-all}
.a{position:absolute;left:96px;right:96px}
.hd{position:absolute;left:96px;right:96px;display:flex;justify-content:space-between;font-family:var(--mono);font-size:21px;letter-spacing:3px;padding-bottom:20px;border-bottom:1.5px solid currentColor}
.k{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--g);text-transform:uppercase}
.row{display:flex;gap:28px;padding:16px 0;border-bottom:1px solid rgba(17,17,17,.15)}
.row .n{width:120px;flex:none;font-family:var(--mono);font-size:18px;letter-spacing:3px;color:var(--g);padding-top:6px}
.row .t{font-size:26px;line-height:1.45;letter-spacing:-.5px}
.row .t i{font-style:normal;color:var(--b);font-size:23px}
'''
# 손그림: 음표에서 피어나는 새싹과 꽃 (흔들리는 선)
DOODLE='''<svg width="{w}" height="{h}" viewBox="0 0 300 380" fill="none" stroke="#111" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round">
<ellipse cx="92" cy="318" rx="44" ry="31" transform="rotate(-22 92 318)" fill="#111"/>
<path d="M131 306 C 133 240, 129 180, 134 112"/>
<path d="M133 214 C 170 200, 196 214, 206 238 C 176 246, 148 236, 133 214 Z" fill="#DCE2D3"/>
<path d="M132 168 C 98 150, 72 160, 62 184 C 92 192, 118 186, 132 168 Z" fill="#DCE2D3"/>
<path d="M134 112 C 120 96, 120 74, 136 66 C 150 74, 152 96, 134 112 Z" fill="#F1EDE4"/>
<path d="M134 112 C 112 108, 98 92, 104 76 C 120 76, 132 92, 134 112 Z" fill="#F1EDE4"/>
<path d="M134 112 C 154 104, 166 88, 160 72 C 144 74, 134 92, 134 112 Z" fill="#F1EDE4"/>
<circle cx="134" cy="96" r="7" fill="#111"/>
<path d="M210 120 l6 -16 l6 16 l16 6 l-16 6 l-6 16 l-6 -16 l-16 -6 z" stroke-width="2.4"/>
<path d="M58 92 l4 -10 l4 10 l10 4 l-10 4 l-4 10 l-4 -10 l-10 -4 z" stroke-width="2.2"/>
<path d="M230 260 c 10 -6 20 -2 22 8" stroke-width="2.4"/>
</svg>'''
def body(kind):
    H = 1350 if kind=='feed' else 1920
    o = 0 if kind=='feed' else 230   # 스토리는 위 안전영역만큼 내림
    d = DOODLE.format(w=230 if kind=='feed' else 260, h=291 if kind=='feed' else 329)
    rows='''<div class="row"><span class="n">혜택</span><span class="t"><b>취미반 3개월 수강료 40% 지원</b><br><i>월 <s style="color:#8A8A8A">18만 원</s> → <b style="color:#111">월 10.8만 원</b></i></span></div>
<div class="row"><span class="n">대상</span><span class="t">교회 담임목사님 추천서 또는<br>세례증명서를 제출할 수 있는 분</span></div>
<div class="row"><span class="n">신청</span><span class="t">인스타그램 DM · 네이버 톡톡 · 카카오톡 채널<br><i>방문 시 추천서 또는 세례증명서를 지참해 주세요.</i></span></div>'''
    big = 210 if kind=='feed' else 250
    return f'''<section class="s" id="{kind}" style="height:{H}px">
<div class="hd" style="top:{72+o}px"><span>ENOCH MUSIC ACADEMY</span><span>SCHOLARSHIP</span></div>
<div class="a k" style="top:{180+o}px">Mission Scholarship · 선교 장학</div>
<div class="a" style="top:{225+o}px;font-size:{74 if kind=='feed' else 78}px;font-weight:700;letter-spacing:-3.4px;line-height:1.2">달란트를<br><span style="font-weight:300">멋지게 피워낼 수 있도록</span></div>
<div class="a" style="top:{430+o if kind=='feed' else 470+o}px;font-size:28px;color:#55524D;letter-spacing:-.5px">에녹실용음악학원이 작은 응원을 더합니다.</div>
<div style="position:absolute;right:{70 if kind=='feed' else 60}px;top:{150+o if kind=='feed' else 170+o}px">{d}</div>
<div class="a" style="top:{500+o if kind=='feed' else 580+o}px;display:flex;align-items:flex-end;gap:28px;background:var(--sg);padding:26px 40px 30px;left:96px;right:96px">
  <div style="font-family:var(--en);font-weight:700;font-size:{big}px;letter-spacing:-10px;line-height:.85">40<span style="font-size:{big//2}px;letter-spacing:-4px">%</span></div>
  <div style="padding-bottom:16px"><div class="k" style="color:#5E6B55">3 Months · Hobby Class</div><div style="font-size:34px;font-weight:700;letter-spacing:-1px;margin-top:8px">취미반 수강료 지원</div><div style="font-size:24px;color:#55524D;margin-top:6px">악기 · 보컬, 3개월간</div></div>
</div>
<div class="a" style="top:{800+o if kind=='feed' else 940+o}px;border-top:1.5px solid #111">{rows}<div style="padding-top:16px;font-size:21px;color:#8A8A8A">* 인원 한정으로, 선착순 조기 마감될 수 있습니다.</div></div>
<div class="a" style="top:{1235+o if kind=='feed' else 1400+o}px;padding-top:18px;border-top:1.5px solid #111;display:flex;justify-content:space-between;font-size:21px;line-height:1.55"><span><b>에녹실용음악학원 시흥점</b><br><span style="color:#55524D">경기도 시흥시 은행로 157 2층</span></span><span style="text-align:right;font-family:var(--mono)">010 3949 3666<br><span style="font-family:P,sans-serif;color:#55524D;font-size:19px">Vocal · Guitar · Drum · Bass · Piano · MIDI · 작곡</span></span></div>
</section>'''
open('poster.html','w').write(f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>선교 장학 포스터</title><style>{FONT}{CSS}</style></head><body>{body("feed")}{body("story")}</body></html>')
