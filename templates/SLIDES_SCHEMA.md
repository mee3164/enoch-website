# slides.json 스키마

카피라이터가 문구를 쓰고, 디자이너가 레이아웃·테마를 다듬는 파일입니다. `npm run cardnews:render -- output/<주제 폴더>`로 같은 폴더에 `01.png ~`가 만들어집니다.

```jsonc
{
  "title": "ENOCH ISSUE No.01 화성",   // 미리보기 제목
  "masthead": "ENOCH ISSUE No.01",     // 머리말 왼쪽 (기본값: ENOCH MUSIC ACADEMY)
  "section": "HARMONY",                // 머리말 오른쪽
  "issueNo": "01",                     // 표지의 큰 숫자 (ENOCH ISSUE일 때만)
  "theme": "ivory",                    // ivory | white | black (장마다 "theme"로 바꿀 수 있음)
  "slides": [ /* 5–7장 */ ]
}
```

문구 필드 공통: `**굵게**` → 굵기 강조(포인트 컬러 없음), `\n` → 줄바꿈.

| layout | 필드 | 용도 |
|---|---|---|
| `cover` | `en`?, `title`, `subtitle`? | 표지 |
| `point` | `label`?, `title`, `body`?, `note`? | 한 장 한 메시지 |
| `list` | `label`?, `title`, `items`: `[{head, text?}]` 또는 `["..."]` (3–4개), `note`? | 순서, 항목 |
| `chords` | `label`?, `title`, `chords`: `[{roman?, name, notes?, fn?}]` (2–4개), `body`?, `note`? | 코드 진행 |
| `compare` | `label`?, `title`, `left`/`right`: `{head, items[]}`, `note`? | 두 가지 비교 |
| `photo` | `image` (예: `images/공간/연습실1.jpg`), `title`?, `body`? | 실제 사진 한 장 |
| `instructor` | `nameEn`, `nameKo`, `subject`, `image`, `role`?, `meta`?: `[{k, v}]` (최대 3개) | 강사 소개 포스터 (인용문 넣지 않음) |
| `closing` | `principle` (ENOCH 원칙 문장 등), `body`?, `directions`? (false면 오시는 길 숨김) | 마무리: 시그니처 문구 + 주소·전화·운영시간 자동 삽입 |

- 사진 경로가 없으면 PNG에 "사진 필요" 자리표시자가 그려지고 경고가 나옵니다. 사진을 새로 만들어 넣지 않습니다.
- 렌더러 경고 항목: 장수(5–7장 밖), 글자 수(title 40 / body 110 / note 70 / subtitle 50자), 금지 표현, 이모지, 없는 사진
