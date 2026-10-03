# slides.json 스키마

**기준 디자인은 확정본 `templates/reference/ENOCH_ISSUE_01/` (01–10)입니다.** 레이아웃은 모두 확정본의 장 유형에서 나왔고, 새 편은 이 레이아웃을 조합해서 만듭니다. 확정본을 그대로 옮긴 예시가 `templates/reference/ENOCH_ISSUE_01/slides.json`에 있습니다.

```jsonc
{
  "title": "ENOCH ISSUE No.02 리듬",
  "masthead": "ISSUE No.02 — RHYTHM",          // 머리말 오른쪽 (왼쪽은 항상 ENOCH MUSIC ACADEMY)
  "footer": "리듬",                              // 꼬리말 왼쪽: 한글 + 한자(한자어일 때만, 예 "화성  和聲")
  "ticker": "ENOCH ISSUE No.02 — RHYTHM — 리듬", // 표지 하단 반복 띠
  "theme": "ivory",                              // ivory | black (장마다 "theme"로 바꿈)
  "slides": [ ... ]
}
```

문구 공통: `**굵게**`, `\n` 줄바꿈. `kicker`는 영문 대문자 모노 라벨(예: `Editor's Note`).

## 확정본 장 유형

| layout | 확정본 | 필드 | 테마 |
|---|---|---|---|
| `cover` | 01 | `image`, `imagePosition`?(예 `"30% center"`, 사진 자르는 위치), `imageSize`?(확대, 예 `"300%"` — 사진 폭 대비 배율, 기본 cover), `en`(큰 영문), `ko`, `sub`, `issue`(예 `"ISSUE\nNo.01"`) | ivory |
| `note` | 02 | `kicker`, `title`, `paragraphs`[] (2–3문단), `sign`?(기본 — ENOCH MUSIC ACADEMY, false면 숨김) | ivory |
| `dictionary` | 03 | `kicker`, `word`, `hanja`?, `en`, `pos`?, `definition`, `terms`[{ko, en, text}] (2개) | black |
| `numbers` | 04 | `kicker`(제목 오른쪽), `title`, `items`[{num, head, text}] (3개) | ivory |
| `keyboard` | 05 | `kicker`, `title`, `boards`[{en, ko, notes: ["C","Eb","G"], caption}] (1–2개) | ivory |
| `beats` | (05 변형) | `kicker`, `title`, `boards`[{en, ko, meter(예 `4/4`), steps(8·16·12), perBeat?, rows[{name, hits:[칸 번호], accents?:[큰 점], soft?:[테두리 점]}], caption, rowH?(행 높이, 기본 92), headH?(머리 칸 높이, 기본 48)}] (1–2개). 칸 번호는 1부터, 8칸이면 1·3·5·7이 1·2·3·4박. accents 칸은 hits에도 넣어야 큰 점이 된다 | ivory |
| `parts` | 06·07 | `kicker`, `title`, `items`[{en, ko, text}] (3개, 4개면 자동으로 촘촘하게), `start`?(번호 시작) | ivory |
| `steps` | 08 | `kicker`, `title`, `lead`?, `items`[{head, text}] (3개) | black |
| `way` | 09 | `kicker`, `title`, `items`["문장"] (3개) | ivory |
| `closing` | 10 | `ghost`?(기본 ENOCH), `principle`?(기본 시그니처 문구), `principleEn`? — 주소·전화·과목은 자동 | black |

## 보조 유형 (확정본 톤으로 맞춤)

| layout | 필드 | 용도 |
|---|---|---|
| `principle` | `kicker`, `no`(예 `01`), `title`(원칙 문장), `en`?(영문 한 줄), `body`?(풀이, 문자열 또는 배열), `variant`?(`split` 위쪽 색면 · `outline` 외곽선 숫자 · `circle` 원 안 숫자), `block`?(색면·원 색: `sage` `blush` `mist` `butter` `lilac`) | 원칙·선언 한 장에 하나 |
| `typecover` | `kicker`, `index`?(목차 항목 배열 — 위쪽 빈 자리에 2열 격자로), `ghost`?(위쪽 빈 자리에 흐린 큰 글자, 예 `"3"`), `en`(큰 영문, `\n` 가능 — 글자 수에 맞춰 크기 자동), `enSize`?(px, 넓은 글자가 많아 오른쪽 여백을 넘을 때만 직접 지정), `title`(굵은 한글), `sub`?, `ticker`? | 사진 없는 표지 — 정보형·철학·입시 편 (ENOCH ISSUE 표지에는 쓰지 않음) |
| `point` | `kicker`, `title`, `body` (문자열 또는 배열) | 한 장 한 메시지 |
| `chords` | `kicker`, `title`, `chords`[{roman, name, notes, fn}], `body`? | 코드 진행 |
| `photo` | `image`, `imagePosition`?, `imageSize`?, `imageHeight`?(사진 높이 px, 기본 790 — 본문이 길면 줄인다), `title`?, `body`? | 실제 사진 한 장 |
| `quote` | `title`(가운데 큰 문장, `\n`으로 2–3줄), `label`?(위 라벨, 기본 `ENOCH MUSIC ACADEMY` — 이슈 번호 등), `by`?(출처 한 줄, 앞에 — 자동), `note`?(아래 회색 정보), `size`?(문장 크기 px, 기본 96) | 타이포그래피 시리즈 — 사진·두들 없음, 머리말·꼬리말 대신 라벨/출처. 테마 `bluegray` 권장 |
| `instructor` | `nameEn`, `nameKo`, `subject`, `image`, `role`?, `meta`[{k, v}]? | 강사 소개 포스터 (인용문 없음) |

## 확정본의 리듬 (새 편도 따른다)
- 표지(ivory, 사진) → 도입(note) → 정의(dictionary, **black**) → 본문 3–5장(ivory) → 실천(steps, **black**) → ENOCH의 방식(way) → 마무리(closing, **black**)
- black 장은 한 편에 2–3장, 연속으로 두지 않는다.
- 장수: 기본 5–7장, ENOCH ISSUE처럼 긴 편은 확정본과 같은 10장까지.

## 렌더러 경고
장수(5–10장 밖), 글자 수, 금지 표현, 이모지, 없는 사진, 알 수 없는 건반 음 이름

## 타이포그래피 시리즈 (quote · bluegray)
Magazine B "Quote of the Day" 결. 사진 요소 없이 문장이 주인공.
- 테마 `bluegray`: 배경 #B8C5D6, 글자는 검정(#111) · 회색(#4A4A4A)만.
- 구조: 위 라벨 22px 모노 대문자 → 가운데 문장 96px 굵게, 위아래 여백 80px, 가운데 정렬 → 아래 출처 26px · 정보 22px 회색.
  (요청 기준 12 / 48–56 / 11px은 작은 화면 기준 비율이라, 1080px 카드에서는 휴대폰 피드에서 읽히도록 약 2배로 잡았다. 장마다 `size`로 조절.)
- 마무리 장은 `closing`(black) 또는 `quote`로 학원 정보를 `note`에 넣는다.

```jsonc
{ "layout": "quote", "theme": "bluegray", "label": "ENOCH MUSIC ACADEMY — PRINCIPLE 01",
  "title": "진도보다\n이해를 먼저 봅니다.", "by": "ENOCH의 원칙", "note": "Understanding before progress." }
```

## 파스텔 테마 (시안 단계 — CLAUDE.md 반영 전)
`theme`: `sage`(세이지) · `blush`(블러시) · `mist`(미스트) · `butter`(버터) · `lilac`(라일락). 채도를 낮춘 배경 + 같은 계열의 짙은 글자.

## 두들 (손그림 장식) · 손그림 테두리
- 장마다 `"doodles": [{ "name", "x", "y", "size", "rotate"?, "fill"?, "color"?, "stroke"?, "opacity"? }]` — 좌표는 카드 왼쪽 위 기준 px. 글자 위에 겹치지 않게 빈 자리에 둔다.
- `name`: spiral · note · notes · mic · drum · guitar · keys · headphones · ticket · score · route · shirt · moon · star · squiggle · heart
- `fill`: 파스텔 이름(sage · blush · mist · butter · lilac · cream) 또는 색 코드
- `"frame": true` (장 또는 덱 전체) — 카드 안쪽을 두르는 손그림 두 줄 테두리
- 사람·강사·공간은 그리지 않는다. 사람과 공간은 실제 사진만 (CLAUDE.md 5번).
