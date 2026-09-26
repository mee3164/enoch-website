# enoch-website

에녹실용음악학원 저장소. 현재는 인스타그램 카드뉴스 제작 에이전트 팀(`cardnews/`)이 들어 있습니다.

## 카드뉴스
- 제작 요청("카드뉴스 만들어줘", "이번 달 캘린더")은 `.claude/skills/cardnews/SKILL.md` 절차를 따르고, `.claude/agents/cardnews-*` 에이전트에게 단계별로 맡긴다.
- 브랜드 기준: `cardnews/brand/brand-guide.md`, 학원 정보: `cardnews/brand/brand.json`
- 게시물 1개 = `cardnews/projects/<YYYY-MM-DD>-<slug>/` 폴더 1개 (brief → research → slides.json → out/*.png → caption → review)
- 렌더링: `npm run cardnews:render -- cardnews/projects/<id>` (최초 1회 `npm install && npx playwright install chromium`)
- 모든 콘텐츠는 한국어, 해요체. 음악 이론 사실은 research.md 근거 없이 쓰지 않는다.
