# slides.json 스키마

카피라이터가 작성하고 디자이너가 다듬는 카드뉴스 원고 파일입니다. `node cardnews/scripts/render.mjs <프로젝트 폴더>`로 PNG가 만들어집니다.

```jsonc
{
  "id": "2026-10-05-two-five-one",   // 폴더명과 동일
  "title": "II-V-I 진행",            // 미리보기 HTML 제목
  "series": "화성학 한 장",           // 커버 kicker 기본값
  "theme": "dark",                   // 덱 기본 테마: dark | light (슬라이드별 theme로 덮어쓰기 가능)
  "slides": [ /* 아래 레이아웃 객체들 */ ]
}
```

모든 텍스트 필드: `**강조**` → 포인트 컬러, `\n` → 줄바꿈. 모든 슬라이드는 `"theme": "light"` 옵션 가능.

| layout | 필드 | 용도 |
|---|---|---|
| `cover` | `kicker`?, `title`, `subtitle`?, `big`? (배경 대형 문자) | 1장 커버 |
| `point` | `label`?, `title`, `body`?, `note`? | 개념 하나 설명 |
| `list` | `label`?, `title`, `items`: `[{head, text}]` 또는 `["문장"]` (3~4개), `note`? | 단계, 체크리스트 |
| `compare` | `label`?, `title`, `left`: `{head, items[]}`, `right`: `{head, items[]}`, `note`? | A vs B (오른쪽이 강조) |
| `chords` | `label`?, `title`, `chords`: `[{name, roman?, notes?, fn?}]` (2~4개), `body`?, `note`? | 코드 진행 |
| `quiz` | `kicker`?, `title`, `options`: `["..."]` (2~4개), `note`? | 참여 유도 |
| `summary` | `title`, `items`, `label`? (기본 SUMMARY) | 요약 (list와 동일 모양) |
| `cta` | `title`, `body`?, `button`?, `contact`?, `saveHint`? (false면 저장 배지 숨김) | 마지막 장 |

## 글자 수 가이드 (렌더러가 경고)
- `title` 40자, `body` 110자, `note` 70자, `subtitle` 50자 이하
- 커버 `title`은 25자 이내 권장
