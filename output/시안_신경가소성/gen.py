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

# ---- C: 신경가소성 개념도 (뉴런 두 개의 연결이 연습에 따라 바뀌는 과정)
def neuron_pair(stage):
    ink = "#111"; y = 60
    w_ax = {1: 1.6, 2: 3.2, 3: 4.6}[stage]
    dash = ' stroke-dasharray="4 6"' if stage == 1 else ""
    g = ""
    for a in (120, 150, 180, 210, 240):
        r = math.radians(a)
        g += f'<line x1="40" y1="{y}" x2="{40+38*math.cos(r):.1f}" y2="{y-38*math.sin(r):.1f}" stroke="{ink}" stroke-width="1.6"/>'
    g += f'<circle cx="40" cy="{y}" r="18" fill="#F1EDE4" stroke="{ink}" stroke-width="2"/><circle cx="40" cy="{y}" r="6" fill="{ink}"/>'
    g += f'<line x1="58" y1="{y}" x2="292" y2="{y}" stroke="{ink}" stroke-width="{w_ax}"{dash}/>'
    if stage >= 2:
        n = 4 if stage == 2 else 6
        seg = 200 / n
        for k in range(n):
            x = 72 + k*seg; hh = 14 if stage == 2 else 18
            g += f'<rect x="{x:.1f}" y="{y-hh/2}" width="{seg-8:.1f}" height="{hh}" rx="{hh/2}" fill="#C9C4BB" stroke="{ink}" stroke-width="1.2"/>'
    ends = {1: [0], 2: [-10, 10], 3: [-16, 0, 16]}[stage]
    for dy in ends:
        g += f'<path d="M292 {y} Q302 {y+dy} 312 {y+dy}" fill="none" stroke="{ink}" stroke-width="{max(1.4, w_ax-1.4):.1f}"{dash}/>'
        g += f'<circle cx="314" cy="{y+dy}" r="{3 if stage==1 else 4.5}" fill="{ink}"/>'
        g += f'<line x1="318" y1="{y+dy}" x2="340" y2="{y}" stroke="{ink}" stroke-width="1.2"/>'
    g += f'<line x1="340" y1="{y}" x2="372" y2="{y}" stroke="{ink}" stroke-width="1.6"/>'
    for a in (20, -20, 60, -60):
        r = math.radians(a)
        g += f'<line x1="390" y1="{y}" x2="{390+38*math.cos(r):.1f}" y2="{y-38*math.sin(r):.1f}" stroke="{ink}" stroke-width="1.6"/>'
    g += f'<circle cx="390" cy="{y}" r="18" fill="#F1EDE4" stroke="{ink}" stroke-width="2"/><circle cx="390" cy="{y}" r="6" fill="{ink}"/>'
    if stage == 3:
        g += f'<path d="M130 {y-34} H190 M182 {y-40} L190 {y-34} L182 {y-28}" fill="none" stroke="{ink}" stroke-width="1.4"/>'
        g += f'<text x="198" y="{y-28}" font-size="18" fill="#55524D">빠르게</text>'
    return f'<svg width="440" height="120" viewBox="0 0 440 120">{g}</svg>'
steps = [(1, "처음", "연결이 약해서 신호가\n잘 전해지지 않아요."),
         (2, "반복", "자주 쓰는 연결이 굵어지고,\n신호 길이 수초로 감싸여요."),
         (3, "익숙해짐", "신호가 빠르고 정확해져서,\n생각하지 않아도 손이 움직여요.")]
neuro = '<p class="ndef">신경가소성(Neuroplasticity) — 쓰는 만큼 뇌의 연결이 바뀌는 성질</p><div class="nrows">' + "".join(
    f'<div class="nrow"><div class="ndia">{neuron_pair(n)}</div><div class="ntxt"><b>0{n} {h}</b><span>{t}</span></div></div>' for n, h, t in steps) + '</div>'
extra += """
.ndef{margin-top:24px;font-size:26px;color:var(--body)}
.nrows{margin-top:32px;border-top:2px solid var(--rule)}
.nrow{display:grid;grid-template-columns:460px 1fr;align-items:center;gap:24px;padding:16px 0;border-bottom:1px solid var(--hair)}
.ntxt b{display:block;font-family:var(--mono);font-weight:400;font-size:20px;letter-spacing:3px;color:var(--sub);margin-bottom:10px}
.ntxt span{font-size:27px;line-height:1.5;white-space:pre-line}"""

def card(n, kicker, title, inner, note):
    return f'''<section class="card layout-point theme-ivory"><div class="masthead"><span>ENOCH MUSIC ACADEMY</span><span>ENOCH — PLATEAU</span></div>
<div class="kicker">{kicker}</div><h2 class="title">{title}</h2>{inner}<div class="fnote">{note}</div>
<div class="colophon"><span>정체기  停滯期</span><span class="page">{n}</span></div></section>'''
html = f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}{extra} body{{background:#555}}</style></head><body>' + \
  card("A", "Learning Curve", "귀가 손보다\n먼저 자라요", svg + legend, "개념도 · ENOCH의 설명을 그린 그림이며 실제 측정값이 아닙니다") + \
  card("B", "Early vs. Middle", "초기와 중기,\n무엇이 다를까요", table, "학습 곡선의 일반적인 흐름과 ENOCH의 설명을 정리한 표입니다") + \
  card("C", "Neuroplasticity", "연습하면\n뇌의 연결이 바뀌어요", neuro, "개념도 · 실제 뉴런의 모양과 크기를 단순화한 그림입니다") + '</body></html>'
open("figures.html", "w").write(html)
