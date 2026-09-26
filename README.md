# enoch-website

에녹실용음악학원 시흥점(ENOCH MUSIC ACADEMY) 인스타그램 카드뉴스 제작 저장소. 기준 문서는 [CLAUDE.md](CLAUDE.md)입니다.

## 팀 (CLAUDE.md 6번)

```
/cardnews <주제>  (프로듀서: 순서 연결 · 재작업 판단 · 보고)
   │
   ├─ 1 기획자      cardnews-strategist   → brief.md    장별 구성안, 사실 확인, 학원에 확인할 것
   ├─ 2 카피라이터  cardnews-copywriter   → slides.json, caption.md
   ├─ 3 디자이너    cardnews-designer     → 01.png ~    templates/ 로 출력, 눈으로 점검
   └─ 4 검수자      cardnews-reviewer     → review.md   검수 체크리스트
          └─ 수정 요청이면 담당에게 되돌림 (최대 2회)
```

## 사용법 (Claude Code)

```text
/cardnews ENOCH ISSUE No.02 리듬
/cardnews 강사 소개 — 드럼 홍길동 (사진: images/강사/hong.jpg)
/cardnews 다음 달 발행 계획 (주 2회)
/cardnews output/ENOCH_ISSUE_02_리듬 3장 문구 수정: ...
```

PNG만 다시 만들 때:

```bash
npm install
npx playwright install chromium   # 처음 한 번
npm run cardnews:render -- output/<주제 폴더>
node scripts/compare.mjs output/<주제 폴더>   # 확정본과 나란히 비교
```

## 폴더

```
CLAUDE.md          기준 문서 (브랜드 정보, 원칙, 말투, 디자인, 검수 체크리스트)
images/            실제 사진만 — 강사/ 공간/ 학생/ 로고/
templates/         card.css (디자인), brand.json (학원 정보), SLIDES_SCHEMA.md (레이아웃)
  reference/ENOCH_ISSUE_01/  확정본 10장 + slides.json — 이후 모든 편의 디자인 기준
scripts/           render.mjs (slides.json → 1080×1350 PNG), compare.mjs (확정본과 나란히)
plans/             topic-bank.md (주제 목록), YYYY-MM.md (발행 계획)
output/<주제>/     brief.md, slides.json, caption.md, review.md, 01.png ~
.claude/           팀원 정의(agents/)와 제작 절차(skills/cardnews/)
```
