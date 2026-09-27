// 손그림 느낌의 두들(선 그림) 모음 — 흔들리는 선(feTurbulence) 필터로 손으로 그린 듯한 결을 낸다.
// 사람·강사·공간은 그리지 않는다 (CLAUDE.md 5번). 악기·음표·장식 요소만.
// 사용: slides.json의 장마다 "doodles": [{ "name": "spiral", "x": 700, "y": 160, "size": 260, "rotate": -8, "fill": "blush" }]

const FILTER = (id, seed) => `<filter id="${id}" x="-10%" y="-10%" width="120%" height="120%">
  <feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="${seed}"/>
  <feDisplacementMap in="SourceGraphic" scale="5"/></filter>`;

function spiralPath(turns = 3.2, r = 90) {
  let d = "";
  const steps = 160;
  for (let i = 0; i <= steps; i++) {
    const t = (i / steps) * turns * Math.PI * 2;
    const rr = (r * i) / steps;
    const x = 100 + rr * Math.cos(t), y = 100 + rr * Math.sin(t);
    d += (i ? " L" : "M") + x.toFixed(1) + " " + y.toFixed(1);
  }
  return d;
}

// 각 두들은 viewBox 0 0 200 200 기준. F = 채움색(파스텔), S = 선색
const SHAPES = {
  spiral: () => `<path d="${spiralPath()}" fill="none"/>`,
  note: (F) => `<ellipse cx="72" cy="150" rx="30" ry="22" transform="rotate(-20 72 150)" fill="${F}"/>
    <path d="M100 142 L100 30 Q130 45 150 80" fill="none"/>`,
  notes: (F) => `<ellipse cx="50" cy="160" rx="26" ry="19" transform="rotate(-20 50 160)" fill="${F}"/>
    <ellipse cx="140" cy="140" rx="26" ry="19" transform="rotate(-20 140 140)" fill="${F}"/>
    <path d="M74 153 L74 40 L164 22 L164 133 M74 62 L164 44" fill="none"/>`,
  mic: (F) => `<rect x="70" y="18" width="60" height="90" rx="30" fill="${F}"/>
    <path d="M78 50 H122 M78 70 H122 M52 88 Q52 140 100 140 Q148 140 148 88 M100 140 V180 M70 182 H130" fill="none"/>`,
  drum: (F) => `<path d="M30 80 V150 Q100 185 170 150 V80" fill="${F}"/>
    <ellipse cx="100" cy="80" rx="70" ry="24" fill="#F6F1E7"/>
    <path d="M30 150 Q100 185 170 150 M50 95 L60 165 M100 104 V178 M150 95 L140 165 M70 20 L110 72 M150 18 L108 70" fill="none"/>`,
  guitar: (F) => `<path d="M88 120 C40 110 40 190 95 186 C150 190 150 125 112 120 C120 100 110 92 100 96 C90 92 80 100 88 120 Z" fill="${F}"/>
    <circle cx="100" cy="150" r="14" fill="none"/><path d="M100 96 L100 18 M92 18 H108 M94 186 V120 M106 186 V120" fill="none"/>`,
  keys: (F) => `<rect x="14" y="60" width="172" height="90" fill="${F}"/>
    <path d="M38 60 V150 M62 60 V150 M86 60 V150 M110 60 V150 M134 60 V150 M158 60 V150" fill="none"/>
    <path d="M30 60 h14 v52 h-14 z M54 60 h14 v52 h-14 z M102 60 h14 v52 h-14 z M126 60 h14 v52 h-14 z M150 60 h14 v52 h-14 z" fill="currentColor"/>`,
  headphones: (F) => `<path d="M40 130 V100 Q40 30 100 30 Q160 30 160 100 V130" fill="none"/>
    <rect x="26" y="112" width="34" height="58" rx="12" fill="${F}"/><rect x="140" y="112" width="34" height="58" rx="12" fill="${F}"/>`,
  ticket: (F) => `<path d="M20 60 H180 V88 Q164 100 180 112 V140 H20 V112 Q36 100 20 88 Z" fill="${F}"/>
    <path d="M130 64 V136" fill="none" stroke-dasharray="6 8"/><path d="M42 88 H108 M42 112 H96" fill="none"/>`,
  score: (F) => `<rect x="36" y="16" width="128" height="168" fill="${F}"/>
    <path d="M52 50 H148 M52 60 H148 M52 70 H148 M52 110 H148 M52 120 H148 M52 130 H148" fill="none" stroke-width="3"/>
    <ellipse cx="80" cy="68" rx="9" ry="7" fill="currentColor"/><path d="M89 66 V36" fill="none"/>
    <ellipse cx="120" cy="128" rx="9" ry="7" fill="currentColor"/><path d="M129 126 V96" fill="none"/>`,
  route: () => `<path d="M30 170 Q60 120 100 140 Q150 165 150 100 Q150 50 100 60" fill="none" stroke-dasharray="10 10"/>
    <path d="M100 20 Q130 20 130 50 Q130 72 100 100 Q70 72 70 50 Q70 20 100 20 Z" fill="none"/><circle cx="100" cy="50" r="10" fill="currentColor"/>`,
  shirt: (F) => `<path d="M70 30 L40 45 L20 85 L48 98 L55 80 V175 H145 V80 L152 98 L180 85 L160 45 L130 30 Q100 55 70 30 Z" fill="${F}"/>`,
  moon: (F) => `<path d="M130 30 A72 72 0 1 0 170 140 A56 56 0 1 1 130 30 Z" fill="${F}"/>
    <path d="M40 40 l6 14 l14 6 l-14 6 l-6 14 l-6 -14 l-14 -6 l14 -6 Z" fill="none"/>`,
  star: () => `<path d="M100 20 L112 86 L180 100 L112 114 L100 180 L88 114 L20 100 L88 86 Z" fill="none"/>`,
  squiggle: () => `<path d="M10 110 Q35 70 60 110 T110 110 T160 110 T200 100" fill="none"/>`,
  heart: (F) => `<path d="M100 170 C20 110 30 40 80 45 Q95 48 100 70 Q105 48 120 45 C170 40 180 110 100 170 Z" fill="${F}"/>`,
};

const PASTEL = { sage: "#DCE2D3", blush: "#EEDFD8", mist: "#D9E1E8", butter: "#F1E8CB", lilac: "#E3DDE9", cream: "#EAD9B0", none: "none" };

let seq = 0;
export function doodle({ name, x = 0, y = 0, size = 200, rotate = 0, fill = "none", color, stroke = 7, opacity = 1 }) {
  const shape = SHAPES[name];
  if (!shape) return `<!-- 알 수 없는 두들: ${name} -->`;
  const id = `wob${++seq}`;
  const F = PASTEL[fill] || fill;
  const S = color || "var(--fg)";
  return `<svg class="doodle" viewBox="0 0 200 200" width="${size}" height="${size}"
    style="position:absolute;left:${x}px;top:${y}px;transform:rotate(${rotate}deg);opacity:${opacity};color:${S};overflow:visible;pointer-events:none">
    <defs>${FILTER(id, seq)}</defs>
    <g filter="url(#${id})" stroke="${S}" stroke-width="${stroke}" stroke-linecap="round" stroke-linejoin="round">${shape(F)}</g></svg>`;
}

// 카드 안쪽을 두르는 손그림 테두리 (두 줄)
export function frame({ color = "var(--fg)", inset = 34 } = {}) {
  const id = `wob${++seq}`;
  const w = 1080 - inset * 2, h = 1350 - inset * 2;
  return `<svg class="doodle-frame" width="1080" height="1350" style="position:absolute;left:0;top:0;pointer-events:none">
    <defs>${FILTER(id, seq).replace('scale="5"', 'scale="7"').replace("0.035", "0.012")}</defs>
    <g filter="url(#${id})" fill="none" stroke="${color}" stroke-width="3">
      <rect x="${inset}" y="${inset}" width="${w}" height="${h}"/>
      <rect x="${inset + 12}" y="${inset + 12}" width="${w - 24}" height="${h - 24}" stroke-width="1.6"/></g></svg>`;
}

export const DOODLE_NAMES = Object.keys(SHAPES);
