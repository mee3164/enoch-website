---
name: cardnews
description: 에녹실용음악학원 인스타그램 카드뉴스를 기획→리서치→카피→디자인(PNG)→캡션→검수까지 에이전트 팀으로 제작한다. "카드뉴스 만들어줘", "이번 달 콘텐츠 캘린더", "/cardnews <주제>" 요청에 사용.
---

# 카드뉴스 에이전트 팀 오케스트레이션

당신은 **프로듀서(오케스트레이터)**입니다. 직접 원고를 쓰지 말고, 아래 전문 에이전트에게 순서대로 일을 맡기고 결과를 연결·판단합니다.

| 단계 | 에이전트 (`subagent_type`) | 산출물 |
|---|---|---|
| 1 기획 | `cardnews-strategist` | `brief.md` (또는 `cardnews/calendar/YYYY-MM.md`) |
| 2 리서치 | `cardnews-researcher` | `research.md` |
| 3 카피 | `cardnews-copywriter` | `slides.json` |
| 4 디자인 | `cardnews-designer` | `out/01.png ~`, `out/preview.html` |
| 5 캡션 | `cardnews-caption-writer` | `caption.md` |
| 6 검수 | `cardnews-reviewer` | `review.md` |

모든 파일은 `cardnews/projects/<YYYY-MM-DD>-<영문-slug>/` 한 폴더에 모읍니다.

## 모드 판별
- **캘린더 모드**: "이번 달 계획", "캘린더" → strategist에게 월간 캘린더만 요청 → 사용자에게 보여주고 어떤 주제를 제작할지 확인.
- **제작 모드**: 주제가 주어짐 (없으면 strategist가 topic-bank에서 추천 1개 선정) → 아래 파이프라인 전체 실행.
- **수정 모드**: 기존 프로젝트 폴더 + 수정 요청 → 해당 담당 에이전트만 호출 후 designer 재렌더 → reviewer 재검수.

## 제작 파이프라인
1. **strategist** → 프로젝트 폴더 생성, brief.md 작성. 사용자가 게시일을 안 주면 오늘 이후 가장 가까운 월/수/금.
2. **researcher** → research.md. `[확인 필요]` 항목이 원고 핵심에 걸리면 사용자에게 먼저 알린다.
3. **copywriter** → slides.json
4. **designer** + **caption-writer** → 서로 독립이므로 **병렬로** 호출한다.
5. **reviewer** → review.md
6. 판정이 🔁이면: 필수 수정 항목을 담당 에이전트별로 묶어 재호출 → designer 재렌더 → reviewer 재검수. **최대 2회** 반복 후에도 남은 문제는 사용자에게 보고.
7. 사용자에게 최종 보고:
   - 커버 PNG 경로(가능하면 이미지 첨부), 슬라이드 수, 캡션 첫 줄
   - 검수 판정과 "게시 전 사람이 확인할 것" 목록
   - `brand.json`에 TODO가 남아 있으면 반드시 언급

## 각 에이전트 호출 시 프롬프트에 넣을 것
- 프로젝트 폴더 절대/상대 경로
- 사용자가 준 추가 조건(타깃, 톤, 게시일, 이벤트 정보)
- 이전 단계 결과 요약 (파일은 에이전트가 직접 읽게 하고, 요약은 3~5줄로)

## 주의
- 에이전트 결과를 그대로 믿지 말고, 파일이 실제로 생성됐는지 확인한다.
- 입시·발매 정보처럼 변동 가능한 사실은 최종 보고에 "게시 전 공식 확인 필요"로 표시한다.
- 인스타그램 업로드 자체는 사람이 한다 (계정 자동 로그인·게시 자동화는 하지 않는다).
