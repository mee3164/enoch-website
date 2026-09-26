# enoch-website

에녹실용음악학원 — 인스타그램 카드뉴스 에이전트 팀

## 팀 구성

```
                 ┌──────────────────────────────┐
  사용자 요청 ──▶ │  프로듀서 (/cardnews 스킬)      │  단계 연결 · 재작업 판단 · 최종 보고
                 └──────────────┬───────────────┘
   ① 기획         ② 리서치        ③ 카피          ④ 디자인  ─┐
 strategist ─▶ researcher ─▶ copywriter ─▶ designer      ├─▶ ⑥ 검수 reviewer ─┐
                                        └▶ caption-writer ┘  (④⑤ 병렬)      │
                                           ⑤ 캡션                          │
                        ◀──────── 🔁 수정 요청 시 담당자에게 되돌림 (최대 2회) ─┘
```

| 에이전트 | 역할 | 산출물 |
|---|---|---|
| `cardnews-strategist` | 편집장. 월간 캘린더, 주제·타깃·핵심 메시지 기획 | `calendar/YYYY-MM.md`, `brief.md` |
| `cardnews-researcher` | 음악 이론·악기·입시·발매 사실 조사 및 검증 | `research.md` |
| `cardnews-copywriter` | 커버 훅, 슬라이드 원고, CTA | `slides.json` |
| `cardnews-designer` | 레이아웃·테마 결정, PNG 렌더링, 시각 검수 | `out/01.png ~`, `out/preview.html` |
| `cardnews-caption-writer` | 캡션, 해시태그, alt 텍스트, 릴스·스토리 연계 | `caption.md` |
| `cardnews-reviewer` | 이론 정확성·맞춤법·과장광고·저작권 최종 검수 | `review.md` |

에이전트 정의: `.claude/agents/`, 오케스트레이션: `.claude/skills/cardnews/SKILL.md`

## 사용법 (Claude Code)

```text
/cardnews 이번 달 콘텐츠 캘린더 짜줘
/cardnews 드럼 루디먼트 필수 5종, 10월 7일 게시
/cardnews 2026-09-28-two-five-one 커버 문구를 질문형으로 바꿔줘
```

직접 렌더링만 할 때:

```bash
npm install
npx playwright install chromium        # 최초 1회
npm run cardnews:render -- cardnews/projects/2026-09-28-two-five-one
```

## 폴더 구조

```
cardnews/
  brand/        brand-guide.md (톤·페르소나·금지사항), brand.json (연락처·색상)
  topics/       topic-bank.md (시리즈별 주제 풀, 사용 이력)
  calendar/     월간 캘린더
  templates/    card.css, SLIDES_SCHEMA.md (레이아웃 8종)
  scripts/      render.mjs (slides.json → PNG)
  projects/     게시물별 폴더 (brief / research / slides.json / caption / review / out)
```

## 시작 전 할 일
1. `cardnews/brand/brand.json`의 `TODO` 값(인스타 계정, 전화, 지역, 카카오톡 채널)을 실제 정보로 바꾸기
2. 브랜드 컬러가 있다면 `brand.json`과 `cardnews/templates/card.css`의 `:root` 변수 수정
3. 샘플 결과물 `cardnews/projects/2026-09-28-two-five-one/out/` 확인
