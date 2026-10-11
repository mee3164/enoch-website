# ENOCH 마스코트 '노트' — 8분음표 모양 단순 선 그림 (SVG 조각 생성)
def mascot(x=0, y=0, s=1.0, face="smile", arms="down", sweat=False, shake=False, flip=False, ink="#111"):
    k = 6/s if s else 6
    g = []
    g.append(f'<g transform="translate({x},{y}) scale({-s if flip else s},{s})" stroke="{ink}" stroke-width="{6}" stroke-linecap="round" stroke-linejoin="round" fill="none">')
    # 기둥 + 깃발
    g.append('<path d="M70 -10 V -250"/>')
    g.append('<path d="M70 -250 C 110 -220, 140 -200, 120 -140"/>')
    # 다리
    g.append('<path d="M-30 58 L -38 110 M 30 58 L 36 110"/><path d="M-38 110 h -26 M 36 110 h 26"/>')
    # 팔
    if arms == "down":
        g.append('<path d="M-88 10 C -120 30, -125 60, -118 80"/><path d="M 92 0 C 120 20, 128 50, 122 72"/>')
    elif arms == "up":
        g.append('<path d="M-88 -10 C -130 -40, -140 -80, -130 -110"/><path d="M 92 -20 C 130 -60, 140 -90, 132 -120"/>')
    front = None
    if arms == "front":
        front = '<path d="M-90 10 C -120 0, -138 -20, -142 -44"/><path d="M 94 -6 C 124 -16, 140 -36, 144 -60"/><g fill="#FFFDF7"><circle cx="-142" cy="-52" r="12"/><circle cx="144" cy="-68" r="12"/></g>'
    elif arms == "hug":
        front = '<path d="M-78 30 C -60 64, -26 72, -4 64"/><path d="M 84 16 C 74 56, 40 70, 10 66"/>'
    # 머리(음표 머리) — 몸통
    g.append('<ellipse cx="0" cy="0" rx="95" ry="70" transform="rotate(-18)" fill="#FFFDF7"/>')
    if front: g.append(front)
    # 볼
    g.append('<g stroke="none" fill="#DDE37C"><ellipse cx="-50" cy="22" rx="16" ry="10"/><ellipse cx="44" cy="4" rx="16" ry="10"/></g>')
    # 얼굴
    if face == "smile":
        g.append('<g fill="#111" stroke="none"><ellipse cx="-30" cy="-8" rx="7" ry="9"/><ellipse cx="22" cy="-22" rx="7" ry="9"/></g><path d="M-14 16 Q 0 28 14 10" stroke-width="5"/>')
    elif face == "nervous":
        g.append('<g fill="#111" stroke="none"><circle cx="-30" cy="-8" r="5"/><circle cx="22" cy="-22" r="5"/></g><path d="M-20 18 q 6 -8 12 0 t 12 0 t 12 0" stroke-width="5"/>')
    elif face == "sad":
        g.append('<path d="M-38 -6 q 8 6 16 0 M 14 -20 q 8 6 16 0" stroke-width="5"/><path d="M-12 22 Q 2 10 16 18" stroke-width="5"/>')
    elif face == "happy":
        g.append('<path d="M-38 -4 q 8 -10 16 0 M 14 -18 q 8 -10 16 0" stroke-width="5"/><path d="M-16 12 Q 0 32 18 6" stroke-width="5"/>')
    elif face == "calm":
        g.append('<path d="M-38 -4 h 16 M 14 -18 h 16" stroke-width="5"/><path d="M-12 16 Q 0 22 12 12" stroke-width="5"/>')
    if sweat:
        g.append('<path d="M 112 -60 c -10 14 -10 24 0 26 c 10 -2 10 -12 0 -26 z" fill="#FFFDF7" stroke-width="4"/><path d="M -118 -40 c -8 12 -8 20 0 22 c 8 -2 8 -10 0 -22 z" fill="#FFFDF7" stroke-width="4"/>')
    if shake:
        if arms == "front":
            g.append('<g stroke-width="4"><path d="M -168 -80 l -10 -8 M -176 -54 l -14 0 M -168 -28 l -10 8"/><path d="M 170 -96 l 10 -8 M 178 -70 l 14 0 M 170 -44 l 10 8"/></g>')
        else:
            g.append('<g stroke-width="4"><path d="M -150 60 l 10 -6 M -152 82 l 12 0 M -148 104 l 10 6"/><path d="M 150 50 l -10 -6 M 154 72 l -12 0 M 150 94 l -10 6"/></g>')
    g.append('</g>')
    return "".join(g)
