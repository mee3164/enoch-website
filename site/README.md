# ENOCH 모바일 홈페이지 (시안)

카드뉴스와 같은 결(CLAUDE.md 4·10번)로 만든 한 페이지짜리 모바일 홈페이지.

```
python3 site/build.py      # → site/dist/ (index.html · img/ · fonts/) — Pillow 필요
```
`site/dist/` 폴더를 그대로 올리면 된다 (GitHub Pages · Netlify 등 정적 호스팅).

## 고치는 곳
- 학원 정보(주소·전화·시간·오시는 길): `templates/brand.json` — 카드뉴스와 같은 파일
- 상담 버튼 링크: `site/data/contact.json` — `kakao`(카카오톡 채널), `naverTalk`(네이버 톡톡). 비어 있으면 "준비 중"으로 표시. 도메인이 생기면 `siteUrl`도 넣는다.
- 강사: `site/data/teachers.json`

## 강사 추가하기
1. 사진을 `images/강사/이름_01.jpg`로 넣는다.
2. `site/data/teachers.json`에 한 줄 추가:
```json
{"id": "영문아이디", "nameKo": "홍길동", "nameEn": "HONG GILDONG", "subject": "Piano",
 "photo": "images/강사/홍길동_01.jpg", "career": ["약력 1", "약력 2"]}
```
   - `subject`: Vocal · Guitar · Drum · Bass · Piano · MIDI · Composition
   - 사진 자르는 위치를 바꾸려면 `"focus": [가로 0–1, 세로 0–1]`, 확대는 `"zoom": 1.5`
3. `python3 site/build.py` 다시 실행. 검색엔진용 학원 정보(구조화 데이터)의 강사 목록도 함께 바뀐다.

## 검색·AI용
- `<title>`·description에 지역(시흥·대야역)·과목·1:1을 넣었다.
- schema.org `MusicSchool` 구조화 데이터: 주소·전화·운영시간·과목·강사.
- 공개 후: Google Search Console · 네이버 서치어드바이저에 등록, 구글 비즈니스 프로필 웹사이트 칸에 주소 입력.
