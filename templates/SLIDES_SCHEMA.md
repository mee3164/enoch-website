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
| `principle` | `kicker`, `no`(예 `01`), `title`(원칙 문장), `en`?(영문 한 줄), `body`?(풀이, 문자열 또는 배열) | 원칙·선언 한 장에 하나 |
| `typecover` | `kicker`, `index`?(목차 항목 배열 — 위쪽 빈 자리에 2열 격자로), `ghost`?(위쪽 빈 자리에 흐린 큰 글자, 예 `"3"`), `en`(큰 영문, `\n` 가능 — 글자 수에 맞춰 크기 자동), `title`(굵은 한글), `sub`?, `ticker`? | 사진 없는 표지 — 정보형·철학·입시 편 (ENOCH ISSUE 표지에는 쓰지 않음) |
| `point` | `kicker`, `title`, `body` (문자열 또는 배열) | 한 장 한 메시지 |
| `chords` | `kicker`, `title`, `chords`[{roman, name, notes, fn}], `body`? | 코드 진행 |
| `photo` | `image`, `title`?, `body`? | 실제 사진 한 장 |
| `instructor` | `nameEn`, `nameKo`, `subject`, `image`, `role`?, `meta`[{k, v}]? | 강사 소개 포스터 (인용문 없음) |

## 확정본의 리듬 (새 편도 따른다)
- 표지(ivory, 사진) → 도입(note) → 정의(dictionary, **black**) → 본문 3–5장(ivory) → 실천(steps, **black**) → ENOCH의 방식(way) → 마무리(closing, **black**)
- black 장은 한 편에 2–3장, 연속으로 두지 않는다.
- 장수: 기본 5–7장, ENOCH ISSUE처럼 긴 편은 확정본과 같은 10장까지.

## 렌더러 경고
장수(5–10장 밖), 글자 수, 금지 표현, 이모지, 없는 사진, 알 수 없는 건반 음 이름
