import math
CSS = open("../../templates/card.css").read()
W, H = 860, 560          # 그래프 영역
def xy(t, v): return 40 + t * (W - 60), H - 50 - v * (H - 110)
def curve(tau):
    pts = [xy(i/100, 1 - math.exp(-(i/100)/tau)) for i in range(101)]
    return "M" + " L".join(f"{x:.1f} {y:.1f}" for x, y in pts)
ear, hand = curve(0.22), curve(0.62)
x0, _ = xy(.22, 0); x1, _ = xy(.62, 0)
ey = xy(.95, 1-math.exp(-.95/.22))[1]; hy = xy(.95, 1-math.exp(-.95/.62))[1]
gx = xy(.42,0)[0]; g1 = xy(.42, 1-math.exp(-.42/.22))[1]; g2 = xy(.42, 1-math.exp(-.42/.62))[1]
svg = f'''<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" style="display:block;margin-top:56px;font-family:var(--ko)">
 <rect x="{x0:.1f}" y="40" width="{x1-x0:.1f}" height="{H-90}" fill="#E4DFD5"/>
 <text x="{(x0+x1)/2:.1f}" y="30" text-anchor="middle" font-size="22" fill="#55524D">정체기처럼 느껴지는 구간</text>
 <line x1="40" y1="{H-50}" x2="{W-10}" y2="{H-50}" stroke="#111" stroke-width="2"/>
 <line x1="40" y1="{H-50}" x2="40" y2="40" stroke="#111" stroke-width="2"/>
 <text x="{W-10}" y="{H-14}" text-anchor="end" font-size="22" fill="#6E6A64">연습 기간 →</text>
 <text x="52" y="58" font-size="22" fill="#6E6A64">실력 ↑</text>
 <path d="{ear}" fill="none" stroke="#111" stroke-width="5" stroke-linecap="round"/>
 <path d="{hand}" fill="none" stroke="#8A8A8A" stroke-width="5" stroke-dasharray="14 10" stroke-linecap="round"/>
 <line x1="{gx:.1f}" y1="{g1+8:.1f}" x2="{gx:.1f}" y2="{g2-8:.1f}" stroke="#111" stroke-width="1.5"/>
 <path d="M{gx-6:.1f} {g1+16:.1f} L{gx:.1f} {g1+6:.1f} L{gx+6:.1f} {g1+16:.1f} M{gx-6:.1f} {g2-16:.1f} L{gx:.1f} {g2-6:.1f} L{gx+6:.1f} {g2-16:.1f}" fill="none" stroke="#111" stroke-width="1.5"/>
 <text x="{gx+12:.1f}" y="{g2+46:.1f}" font-size="22" fill="#111">↑ 들리는 만큼 안 되는 차이</text>
 <text x="{W-14}" y="{ey-16:.1f}" text-anchor="end" font-size="26" font-weight="700" fill="#111">귀 (듣는 실력)</text>
 <text x="{W-14}" y="{hy+72:.1f}" text-anchor="end" font-size="26" font-weight="700" fill="#6E6A64">손 (연주 실력)</text>
</svg>'''
legend = '<div style="display:flex;gap:36px;margin-top:22px;font-size:22px;color:#55524D"><span><svg width="48" height="10"><line x1="2" y1="5" x2="46" y2="5" stroke="#111" stroke-width="5" stroke-linecap="round"/></svg> 귀 (듣는 실력)</span><span><svg width="48" height="10"><line x1="2" y1="5" x2="46" y2="5" stroke="#8A8A8A" stroke-width="5" stroke-dasharray="12 8"/></svg> 손 (연주 실력)</span></div>'
rows = [("실력의 변화", "눈에 띄게 늘어요", "늘어도 작게 느껴져요"),
        ("귀", "아직 들리는 게 적어요", "손보다 먼저 자라요"),
        ("자주 듣는 말", "재밌어요", "실력이 안 늘어요"),
        ("ENOCH에서는", "기본을 건너뛰지 않아요", "새 곡 트랜스크립션,\n맞는 연습법 찾기")]
table = '<div class="figtable"><div class="fr fh"><span></span><span>초기</span><span>중기</span></div>' + "".join(
    f'<div class="fr"><span class="k">{k}</span><span>{a}</span><span>{b}</span></div>' for k, a, b in rows) + "</div>"
extra = '''.figtable{margin-top:64px;border-top:2px solid var(--rule)}
.fr{display:grid;grid-template-columns:220px 1fr 1fr;gap:24px;padding:30px 0;border-bottom:1px solid var(--hair);font-size:30px;line-height:1.45;white-space:pre-line}
.fh{font-family:var(--mono);font-size:20px;letter-spacing:3px;color:var(--sub);padding:20px 0}
.fr .k{font-size:24px;color:var(--sub);padding-top:4px}
.fnote{margin-top:auto;margin-bottom:34px;padding-top:14px;font-size:20px;color:var(--sub)}'''
def card(n, kicker, title, inner, note):
    return f'''<section class="card layout-point theme-ivory"><div class="masthead"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH — PLATEAU</span></div>
<div class="kicker">{kicker}</div><h2 class="title">{title}</h2>{inner}<div class="fnote">{note}</div>
<div class="colophon"><span>정체기  停滯期</span><span class="page">{n}</span></div></section>'''
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra} body{{background:#555}}</style></head><body>' + \
  card("A", "Learning Curve", "귀가 손보다\n먼저 자라요", svg + legend, "개념도 · ENOCH의 설명을 그린 그림이며 실제 측정값이 아닙니다") + \
  card("B", "Early vs. Middle", "초기와 중기,\n무엇이 다를까요", table, "학습 곡선의 일반적인 흐름과 ENOCH의 설명을 정리한 표입니다") + '</body></html>'
open("figures.html", "w").write(html)
