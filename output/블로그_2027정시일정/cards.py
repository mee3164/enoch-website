# 블로그 이미지: 2027 정시 실용음악과 학교별 카드 (원장님 요청: 학교별 카드)
# python3 output/블로그_2027정시일정/cards.py → blog.html, thumb.html → node blog.mjs
# 근거: output/입시자료/*.md (각 대학 2027 정시 모집요강)
import os
HERE = os.path.dirname(os.path.abspath(__file__))

D = [  # (마감 그룹, 학교, 학과·전형, 모집, 원서접수, 실기, 발표, 선발, [실기 핵심])
 ("1.7", "서경대학교", "실용음악학부 · 가군 실기우수자", "보컬 3 · 싱어송라이터 1<br><small>기악·작곡은 수시 미충원 시 선발</small>",
  "1.4(월) ~ 1.7(목) 18:00", "1단계 1.11 ~ 1.14<br>2단계 1.16 ~ 1.17", "2.5(금) 17:00", "1단계 실기 100 → 수능 20 + 실기 80",
  ["1단계 자유곡 / 2단계 보컬은 한글 가사곡, 싱어송라이터는 자작곡", "보컬 2분 내외, 반주는 피아노·어쿠스틱기타만", "모두 암보, 2단계 곡은 1단계와 다른 곡", "악보 1단계 3부 · 2단계 5부 미리 준비"]),
 ("1.7", "성신여자대학교", "현대실용음악학과 · 가군 수능(일반)", "보컬 4 · 악기 5<br><small>피아노 2 · 기타 1 · 베이스 1 · 드럼 1</small>",
  "1.4(월) ~ 1.7(목) 18:00", "1.13 ~ 1.16", "2.5(금) 10:00", "수능 55 + 실기 45 (수능 상위 3개 영역)",
  ["자유곡 1곡 2분 내외, 암보, 악보 제출 없음", "반주자 동행 불가 (MR · 자가반주 · 무반주)", "기타 · 베이스 이펙터 사용 금지", "MR은 1.8(금) 18:00까지 원서접수 사이트에 업로드"]),
 ("1.7", "홍익대학교", "공연예술학부 실용음악전공 · 나군", "싱어송라이터 2",
  "1.4(월) ~ 1.7(목) 18:00", "1.14 ~ 1.15", "2.5(금)", "수능 40 + 실기 60",
  ["자작곡 1곡 자가반주하며 가창, 암보 2분 이내", "키보드(고사장 설치) · 어쿠스틱기타만, MR · 반주자 불가", "심사위원용 악보 5부 미리 준비", "실기 후 제시어로 즉석 작사·작곡 과제 가능"]),
 ("1.7", "호원대학교", "실용음악학부 · 나군", "보컬 12 · 피아노 12 · 드럼 11 · 베이스 11 · 기타 11<br><small>싱어송라이터 10 · 프로덕션 4개 분야 30 · 그 외 악기 3</small>",
  "1.4(월) ~ 1.7(목) 18:00", "1.18 ~ 1.24 (시간 예약 1.13)", "2.5(금) 14:00", "학생부 28.6 + 실기 71.4 (보컬 · 사운드테크놀로지는 2단계)",
  ["보컬 1차 자유곡 / 2차 발라드 + 리듬 있는 곡", "드럼 개인 장비 불가(트윈페달만), 기타 페달 1개만", "프로덕션 음원 WAV, 모든 자작곡 AI 사용 금지", "MR은 휴대폰 저장, 스트리밍 불가"]),
 ("1.7", "경희대학교", "PostModern음악학과 · 나군 수능위주", "2명",
  "1.5(화) ~ 1.7(목) 18:00", "없음", "2.5(금) 18:00", "수능 100 (국어 60 · 탐구 40 + 영어 · 한국사)",
  ["정시는 실기고사 없이 수능 성적으로만 선발", "수학 미반영, 탐구 1과목 이상 응시 필수", "실기로 지원하려면 수시가 사실상 유일한 길"]),
 ("1.20", "동아방송예술대학교", "실용음악학부 · 일반전형", "보컬 남 5 · 여 5 / 기악 종목별 3<br><small>작곡: 프로듀서 7 · 전자음악 3 · 탑라이너 2 · 싱어송라이터 2</small>",
  "1.4(월) ~ 1.20(수) 23:59", "1단계 1.24 ~ 1.29<br>2단계 2.1 ~ 2.2", "2.5(금) 16:00", "1단계 실기 100 → 학생부 20 + 실기 80",
  ["보컬 1단계 자유곡 2분, 마이크 없음, MR 코러스 불가", "보컬 2단계 3곡(템포·리듬 다르게, 한글 가사 1곡 이상)", "기악 1단계 MR 불가, 필수자료 미제출 시 감점", "2단계는 심사위원 교체, 대표곡은 양쪽에 권장"]),
 ("1.20", "서울예술대학교", "실용음악전공 · 일반전형(실기우수)", "노래 남 2 · 여 2 · 작곡 3 · 피아노 4<br><small>드럼 · 베이스 · 기타 각 3 · 관악 1 · 전자음악/음향/DJ 2</small>",
  "1.4(월) ~ 1.20(수) 18:30", "1차 1.26 ~ 1.31<br>2차 2.4 ~ 2.5", "2.9(화) 16:00", "1차 실기 → 2차 실기 70 + 수능 30",
  ["노래: 가요 1곡 + 팝 1곡, 리듬·템포 다르게", "2차 실용음악통론 필기(40분), 볼펜 사용 시 0점", "기타: 기성곡 원곡 솔로 그대로 연주 금지", "MR은 원서접수 때 업로드 + 당일 USB, 악보 5부"]),
 ("1.20", "한양여자대학교", "실용음악과 · 일반전형", "보컬 10 · 컴퓨터음악작곡 9 · 기악 14",
  "1.4(월) ~ 1.20(수) 21:00", "1.25 ~ 1.27", "2.9(화) 14:00", "학생부 40 + 실기 60",
  ["보컬 · 기악 자유곡 3분 이내, 작곡은 자작곡 5분 이내", "MR은 1.22(금) 14~18시 홈페이지 업로드", "악보 3부 제출, 반주자 1명 동반 가능", "피아노 · 드럼 · 앰프는 고사장에 비치"]),
 ("1.20", "백석예술대학교", "실용음악과 · 일반전형", "보컬 39 · 건반 16 · 기타 17 · 베이스 14 · 드럼 14<br><small>프로덕션 4개 분야 68 · 관악 및 그 외 2</small>",
  "1.4(월) ~ 1.20(수) 24:00", "1.27 ~ 1.30", "2.5(금) 10:00", "학생부 10 + 수능 10 + 실기 80",
  ["보컬: 마이크 없이 자유곡(랩 제외) + 8마디 시창", "연주: 무반주 자유곡 + MR에 맞춘 코드 진행 연주", "드럼 개인 페달 불가, 기타 개인 이펙터 불가", "자유곡 1분 30초 이내, 악보 3부"]),
 ("1.20", "국제예술대학교", "실용음악과 · 일반전형", "보컬 · 건반 · 기타 · 베이스 · 드럼<br><small>작곡 · 싱어송라이터 · 프로듀싱 · 힙합 (인원은 홈페이지 공지 확인)</small>",
  "1.4(월) ~ 1.20(수) 24:00", "1.24 ~ 2.3", "2.5(금) 14:00", "학생부 30 + 실기 70 (보컬은 1단계 실기 100)",
  ["보컬 1단계 영상 제출(2분), 2단계 다른 곡 2곡", "드럼 개인 페달 불가, 기타는 고사장 이펙터만", "악보 · 포트폴리오 제출 없음", "MR은 휴대폰 저장, 비행기 모드로 재생"]),
]
N = len(D) + 1

CSS = """@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Light.woff2);font-weight:300}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Regular.woff2);font-weight:400}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-SemiBold.woff2);font-weight:600}
@font-face{font-family:P;src:url(../../templates/fonts/Pretendard-Bold.woff2);font-weight:700}
*{margin:0;padding:0;box-sizing:border-box}
body{background:#ccc}
section{width:1080px;height:1350px;position:relative;overflow:hidden;background:#F1EDE4;color:#111;font-family:P,sans-serif;word-break:keep-all;margin-bottom:20px}
.hd{position:absolute;left:80px;right:80px;top:46px;display:flex;justify-content:space-between;font-size:19px;font-weight:600;letter-spacing:3px;padding-bottom:22px;border-bottom:2px solid #111}
.lb{position:absolute;left:80px;font-size:21px;font-weight:400;letter-spacing:3px;color:#6E6A63}
.band{position:absolute;left:0;right:0;background:#EFE5CE}
.nt{position:absolute;left:80px;right:80px;bottom:48px;display:flex;justify-content:space-between;align-items:flex-end;font-size:18px;color:#7A766F;line-height:1.7}
.nt .pg{font-size:19px;letter-spacing:1px}
/* cover */
h1.t{position:absolute;left:78px;top:200px;font-size:104px;font-weight:700;letter-spacing:-4px;line-height:1.14}
.grid{position:absolute;left:80px;right:80px;display:grid;grid-template-columns:1fr 1fr;column-gap:52px}
.grid div{border-top:1.5px solid #8C877E;padding:14px 0 18px}
.grid i{display:block;font-style:normal;font-size:16px;letter-spacing:2px;color:#55524D}
.grid b{display:block;font-size:31px;font-weight:700;letter-spacing:-1px;margin-top:4px}
.grid span{display:block;font-size:19px;color:#6E6A63;margin-top:4px}
.sum{position:absolute;left:80px;font-size:25px;font-weight:600}
/* school */
.nm{position:absolute;left:78px;right:80px;top:180px;font-size:92px;font-weight:700;letter-spacing:-4px;line-height:1.1}
.sub{position:absolute;left:80px;right:80px;top:296px;font-size:28px;color:#55524D}
.dl{position:absolute;left:80px;top:356px;font-size:26px;font-weight:700}
.dl em{font-style:normal;display:inline-block;width:10px;height:10px;background:#111;margin-right:12px;vertical-align:4px}
table{position:absolute;left:80px;right:80px;width:920px;border-collapse:collapse}
td{border-top:1.5px solid #8C877E;padding:17px 0 18px;vertical-align:top;font-size:28px;line-height:1.38}
td.k{width:170px;font-size:16px;letter-spacing:2px;color:#55524D;padding-top:24px}
td.v{font-weight:700}
td small{display:block;font-size:21px;font-weight:400;color:#55524D;margin-top:4px}
.pt{position:absolute;left:80px;right:80px}
.pt .k{font-size:16px;letter-spacing:2px;color:#55524D;margin-bottom:14px}
.pt li{list-style:none;font-size:27px;font-weight:400;line-height:1.45;padding-left:24px;position:relative;margin-top:8px}
.pt li::before{content:"";position:absolute;left:0;top:16px;width:8px;height:8px;border-radius:50%;background:#111}
"""
NOTE = '2026.11.11 각 대학 2027 정시 모집요강 기준<br>정확한 내용은 꼭 각 대학 입학처 모집요강에서 한 번 더 확인해 주세요.'
HD = '<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>2027 정시 · 실용음악 입시</span></div>'
SHORT = {"서경대학교":"실용음악학부","성신여자대학교":"현대실용음악학과","홍익대학교":"공연예술학부 실용음악전공","호원대학교":"실용음악학부","경희대학교":"PostModern음악학과",
 "동아방송예술대학교":"실용음악학부","서울예술대학교":"실용음악전공","한양여자대학교":"실용음악과","백석예술대학교":"실용음악과","국제예술대학교":"실용음악과"}

def card(i, r):
    g, nm, sub, mo, ap, sil, bal, sel, pts = r
    rows = [("모집인원", mo), ("원서접수", ap), ("실기고사", sil), ("합격 발표", bal), ("선발", sel)]
    tr = ''.join(f'<tr><td class="k">{k}</td><td class="v">{v}</td></tr>' for k, v in rows)
    li = ''.join(f'<li>{p}</li>' for p in pts)
    return f"""<section>{HD}
<div class="lb" style="top:128px">ADMISSION GUIDE 2027 · {i-1:02d}</div>
<div class="nm">{nm}</div><div class="sub">{sub}</div>
<div class="dl"><em></em>원서접수 마감 {ap.split("~")[1].strip()}</div>
<div class="band" style="top:428px;height:530px"></div>
<table style="top:462px">{tr}</table>
<div class="pt" style="top:992px"><div class="k">실기 핵심</div><ul>{li}</ul></div>
<div class="nt"><span>{NOTE}</span><span class="pg">{i:02d} / {N:02d}</span></div>
</section>"""

def cover(sq=False):
    if sq:
        return f"""<section style="height:1080px">{HD}
<div class="lb" style="top:150px">ADMISSION GUIDE 2027</div>
<h1 class="t" style="top:230px;font-size:112px">2027학년도<br>실용음악과 정시<br>실기 한눈에 보기</h1>
<div class="band" style="top:690px;height:250px"></div>
<div class="sum" style="top:740px;font-size:40px;font-weight:700">10개 대학</div>
<div class="sum" style="top:810px;font-weight:400;color:#55524D">원서접수 · 실기 일정 · 선발 비율 · 실기 핵심</div>
<div class="nt"><span>ENOCH MUSIC ACADEMY · 031 315 3666</span><span></span></div></section>"""
    cells = ''.join(f'<div><i>{n+1:02d}</i><b>{r[1]}</b><span>{SHORT[r[1]]}</span></div>' for n, r in enumerate(D))
    return f"""<section>{HD}
<div class="lb" style="top:128px">ADMISSION GUIDE 2027</div>
<h1 class="t" style="top:176px;font-size:96px">2027학년도<br>실용음악과 정시<br>실기 한눈에 보기</h1>
<div class="band" style="top:540px;height:640px"></div>
<div class="grid" style="top:574px">{cells}</div>
<div class="sum" style="top:1196px">전형 · 일정 · 선발 비율 · 실기 핵심</div>
<div class="nt"><span>{NOTE}</span><span class="pg">01 / {N:02d}</span></div>
</section>"""

html = f'<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>2027 정시 학교별 카드</title><style>{CSS}</style></head><body>\n'
html += cover() + ''.join(card(i + 2, r) for i, r in enumerate(D)) + '</body></html>\n'
open(os.path.join(HERE, 'blog.html'), 'w', encoding='utf-8').write(html)
# thumb.html은 별도 파일(눈에 띄는 1:1 썸네일)로 관리
print('blog.html', N, '장 + thumb.html')
