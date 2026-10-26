# ENOCH 모바일 홈페이지 생성기
# python3 site/build.py → site/dist/ (index.html + img/ + fonts/)
# 학원 정보: templates/brand.json · 강사: site/data/teachers.json · 상담 링크: site/data/contact.json
import json, os, shutil, html
from PIL import Image, ImageOps

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DIST = os.path.join(HERE, 'dist')
B = json.load(open(os.path.join(ROOT, 'templates/brand.json')))
T = json.load(open(os.path.join(HERE, 'data/teachers.json')))
C = json.load(open(os.path.join(HERE, 'data/contact.json')))
SITE_URL = C.get('siteUrl', '')

e = html.escape
os.makedirs(os.path.join(DIST, 'img'), exist_ok=True)
os.makedirs(os.path.join(DIST, 'fonts'), exist_ok=True)
for w in ('Light', 'Regular', 'Medium', 'SemiBold', 'Bold'):
    shutil.copy(os.path.join(ROOT, f'templates/fonts/Pretendard-{w}.woff2'), os.path.join(DIST, 'fonts'))

def img(src, name, w, ratio=None, gray=False, focus=(0.5, 0.35), zoom=1.0):
    """사진을 웹용으로 줄여 dist/img/에 저장하고 경로를 돌려준다."""
    im = ImageOps.exif_transpose(Image.open(os.path.join(ROOT, src))).convert('RGB')
    if ratio:
        tw, th = w, int(w * ratio)
        if zoom > 1:
            W, H = im.size; cw, ch = W / zoom, H / zoom
            x0 = min(max(W * focus[0] - cw / 2, 0), W - cw); y0 = min(max(H * focus[1] - ch / 2, 0), H - ch)
            im = im.crop((int(x0), int(y0), int(x0 + cw), int(y0 + ch)))
        im = ImageOps.fit(im, (tw, th), method=Image.LANCZOS, centering=focus)
    else:
        im.thumbnail((w, w * 3), Image.LANCZOS)
    if gray:
        im = ImageOps.colorize(ImageOps.grayscale(im), black='#141210', white='#F4EFE6', mid='#8C8378')
    out = f'img/{name}.jpg'
    im.save(os.path.join(DIST, out), quality=82, optimize=True, progressive=True)
    return out

HERO = img('images/공간/로고월_01.jpg', 'hero', 1080, 1.2, gray=True)
SPACES = [('images/공간/복도_02.jpg', 'space-hall', '복도'),
          ('images/공간/피아노룸_01.jpg', 'space-piano', '피아노 레슨실'),
          ('images/공간/드럼룸_02.jpg', 'space-drum', '드럼 레슨실'),
          ('images/공간/보컬부스_03.jpg', 'space-vocal', '보컬 부스'),
          ('images/공간/미디룸_01.jpg', 'space-midi', '미디 작업실'),
          ('images/공간/상담실_01.jpg', 'space-consult', '상담실')]
SUBJ_KO = {'Vocal': '보컬', 'Guitar': '기타', 'Drum': '드럼', 'Bass': '베이스', 'Piano': '피아노', 'MIDI': '미디', 'Composition': '작곡'}

# ── 섹션 ───────────────────────────────
def label(no, en):
    return f'<p class="label"><span>{no}</span>{en}</p>'

principles = [('진도보다 이해를 먼저 봅니다.', 'Understanding before progress.'),
              ('같은 곡도, 사람마다 다르게 가르칩니다.', 'The same song, taught differently to each person.'),
              ('기본은 건너뛰지 않습니다.', "We don't skip the basics.")]
sec_principle = f'''<section id="about" class="sec">
{label('01', 'THE ENOCH WAY')}
<h2>음악을 배우는 방식이<br>사람마다 다르다는 것.</h2>
<ol class="principles">{''.join(f'<li><span class="no">0{i+1}</span><p class="ko">{k}</p><p class="en">{en}</p></li>' for i, (k, en) in enumerate(principles))}</ol>
</section>'''

subjects = ['Vocal', 'Guitar', 'Drum', 'Bass', 'Piano', 'MIDI', 'Composition']
sec_lesson = f'''<section id="lesson" class="sec">
{label('02', 'LESSON')}
<h2>모든 과정,<br>1:1 레슨입니다.</h2>
<ul class="subjects">{''.join(f'<li><span class="en">{s}</span><span class="ko">{SUBJ_KO[s]}</span></li>' for s in subjects)}</ul>
<div class="courses">
  <div><h3>입시</h3><p>시험장에서도 연습한 만큼 연주할 수 있도록, 주기적으로 모의고사를 진행합니다.</p></div>
  <div><h3>취미</h3><p>처음 악기를 잡는 날부터, 좋아하는 곡을 내 소리로 연주하는 날까지.</p></div>
  <div><h3>성인</h3><p>퇴근 후, 주말에도. 각자의 시간과 속도에 맞춰 수업합니다.</p></div>
  <div><h3>전문</h3><p>무대와 작업을 준비하는 사람을 위한 과정입니다.</p></div>
</div>
</section>'''

def teacher(t):
    p = img(t['photo'], 't-' + t['id'], 720, 1.25, focus=tuple(t.get('focus', (0.5, 0.35))), zoom=t.get('zoom', 1.0))
    car = ''.join(f'<li>{e(c)}</li>' for c in t['career'])
    return f'''<article class="teacher" id="t-{t['id']}">
  <img src="{p}" alt="{e(t['nameKo'])} {SUBJ_KO.get(t['subject'], t['subject'])} 강사" loading="lazy" width="720" height="900">
  <p class="subj"><i></i>{t['subject']}</p>
  <h3 class="en">{e(t['nameEn'])}</h3>
  <p class="ko">{e(t['nameKo'])}</p>
  <p class="career-h">CAREER</p>
  <ul class="career">{car}</ul>
</article>'''

sec_teachers = f'''<section id="teachers" class="sec">
{label('03', 'TEACHERS')}
<h2>함께 가르치는 사람들</h2>
<p class="lead">파트별 강사가 1:1로 수업합니다. 옆으로 넘겨 보세요.</p>
<div class="rail">{''.join(teacher(t) for t in T)}</div>
</section>'''

spaces = ''.join(f'<figure><img src="{img(s, n, 900, 1.25)}" alt="{c}" loading="lazy" width="900" height="1125"><figcaption>{c}</figcaption></figure>' for s, n, c in SPACES)
sec_space = f'''<section id="space" class="sec">
{label('04', 'SPACE')}
<h2>분위기에<br>가장 신경 썼어요.</h2>
<p class="lead">수강생은 운영시간 안에 연습실을 자유롭게 이용할 수 있습니다.</p>
<div class="rail">{spaces}</div>
</section>'''

sec_visit = f'''<section id="visit" class="sec">
{label('05', 'VISIT')}
<h2>오시는 길</h2>
<dl class="info">
  <dt>주소</dt><dd>{e(B['address'])}</dd>
  <dt>찾아오기</dt><dd>{e(B['directions'])}</dd>
  <dt>운영시간</dt><dd>평일 13:00–22:00<br>토요일 10:00–18:00<br>일요일 휴무</dd>
  <dt>전화</dt><dd><a href="tel:{B['phone'].replace(' ', '')}">{e(B['phone'])}</a></dd>
</dl>
<div class="maps">
  <a href="{e(C['naverMap'])}" target="_blank" rel="noopener">네이버 지도</a>
  <a href="{e(C['kakaoMap'])}" target="_blank" rel="noopener">카카오맵</a>
  <a href="{e(C['googleMap'])}" target="_blank" rel="noopener">구글 지도</a>
</div>
</section>'''

def cta(href, text, cls):
    if href:
        ext = '' if href.startswith('tel:') else ' target="_blank" rel="noopener"'
        return f'<a class="{cls}" href="{e(href)}"{ext}>{text}</a>'
    return f'<a class="{cls} todo" href="#contact" aria-disabled="true">{text}<small>준비 중</small></a>'
TEL = 'tel:' + B['phone'].replace(' ', '')
ctas = cta(C['kakao'], '카카오톡', 'kakao') + cta(C['naverTalk'], '네이버 톡톡', 'naver') + cta(TEL, '전화 상담', 'tel')

sec_contact = f'''<section id="contact" class="sec dark">
{label('06', 'CONTACT')}
<h2>상담은<br>편한 방법으로.</h2>
<p class="lead">원하는 과목과 목표, 가능한 시간만 알려 주세요.</p>
<div class="ctas big">{ctas}</div>
</section>'''

footer = f'''<footer>
<p class="ghost">ENOCH</p>
<p class="sig">{e(B['signature'])}<br><span>{e(B['signatureEn'])}</span></p>
<p class="small">{e(B['name'])} · {e(B['nameEn'])}<br>{e(B['address'])} · {e(B['phone'])}<br>{e(B['subjects'])}</p>
</footer>'''

# ── 구조화 데이터 (검색엔진·AI가 읽는 학원 정보) ─────────
ld = {
    "@context": "https://schema.org",
    "@type": "MusicSchool",
    "name": B['name'], "alternateName": [B['nameEn'], "에녹실용음악학원"],
    "description": "경기도 시흥시 대야역 인근 실용음악학원. 보컬·기타·드럼·베이스·피아노·미디·작곡, 입시·취미·성인·전문 과정 모두 1:1 레슨.",
    "slogan": B['signature'],
    "telephone": "+82-10-3949-3666",
    "address": {"@type": "PostalAddress", "streetAddress": "은행로 157 2층", "addressLocality": "시흥시",
                "addressRegion": "경기도", "addressCountry": "KR"},
    "openingHoursSpecification": [
        {"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "13:00", "closes": "22:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Saturday", "opens": "10:00", "closes": "18:00"}],
    "areaServed": ["시흥시", "대야동", "은행동"],
    "hasOfferCatalog": {"@type": "OfferCatalog", "name": "1:1 레슨",
        "itemListElement": [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"{SUBJ_KO[s]} 1:1 레슨"}} for s in subjects]
        + [{"@type": "Offer", "itemOffered": {"@type": "Service", "name": f"실용음악 {c} 과정"}} for c in ('입시', '취미', '성인', '전문')]},
    "employee": [{"@type": "Person", "name": t['nameKo'], "alternateName": t['nameEn'].title(),
                  "jobTitle": f"{SUBJ_KO.get(t['subject'], t['subject'])} 강사"} for t in T],
}
if SITE_URL: ld["url"] = SITE_URL
same = [u for u in (C.get('instagram'), C.get('naverMap')) if u]
if same: ld["sameAs"] = same

TITLE = '에녹실용음악학원 시흥점 | 시흥 대야역 실용음악학원 · 보컬 기타 드럼 베이스 피아노 미디 작곡 1:1'
DESC = '경기도 시흥시 은행로 157 2층, 대야역 인근 실용음악학원. 보컬·기타·드럼·베이스·피아노·미디·작곡, 입시·취미·성인·전문 과정 모두 1:1 레슨. 나만의 진짜 소리를 찾는 곳.'

CSS = '''
@font-face{font-family:P;src:url(fonts/Pretendard-Light.woff2) format("woff2");font-weight:300;font-display:swap}
@font-face{font-family:P;src:url(fonts/Pretendard-Regular.woff2) format("woff2");font-weight:400;font-display:swap}
@font-face{font-family:P;src:url(fonts/Pretendard-Medium.woff2) format("woff2");font-weight:500;font-display:swap}
@font-face{font-family:P;src:url(fonts/Pretendard-SemiBold.woff2) format("woff2");font-weight:600;font-display:swap}
@font-face{font-family:P;src:url(fonts/Pretendard-Bold.woff2) format("woff2");font-weight:700;font-display:swap}
:root{--iv:#F1EDE4;--bk:#111;--gy:#8A8A8A;--ln:#cfc8bb;--sage:#DCE2D3;--lime:#DDE37C;
--mono:"IBM Plex Mono","SF Mono",Menlo,Consolas,monospace}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth;-webkit-text-size-adjust:100%}
body{background:var(--iv);color:var(--bk);font-family:P,-apple-system,"Apple SD Gothic Neo",sans-serif;word-break:keep-all;line-height:1.6;padding-bottom:84px}
a{color:inherit}
img{max-width:100%;height:auto}
.wrap{max-width:560px;margin:0 auto;background:var(--iv)}
header{position:sticky;top:0;z-index:20;display:flex;justify-content:space-between;align-items:center;padding:16px 20px;background:rgba(241,237,228,.92);backdrop-filter:blur(8px);border-bottom:1px solid var(--bk);font-family:var(--mono);font-size:11px;letter-spacing:.18em}
header a{text-decoration:none}
nav.toc{display:flex;gap:16px;overflow-x:auto;padding:10px 20px;font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:var(--gy);border-bottom:1px solid var(--ln);scrollbar-width:none}
nav.toc a{text-decoration:none;white-space:nowrap}
.hero{padding:20px 20px 40px}
.hero img{width:100%;aspect-ratio:5/6;object-fit:cover;display:block}
.hero .big{font-weight:700;font-size:min(27vw,150px);letter-spacing:-.04em;line-height:.9;margin:22px 0 14px}
.hero .sig{font-size:24px;font-weight:600;line-height:1.35}
.hero .sig-en{color:var(--gy);font-weight:300;margin-top:4px}
.hero .name{margin-top:22px;padding-top:14px;border-top:1px solid var(--bk);display:flex;justify-content:space-between;font-size:13px}
.ticker{overflow:hidden;white-space:nowrap;border-top:1px solid var(--bk);border-bottom:1px solid var(--bk);font-family:var(--mono);font-size:12px;letter-spacing:.2em;padding:9px 0}
.ticker span{display:inline-block;animation:tk 30s linear infinite}
@keyframes tk{to{transform:translateX(-50%)}}
.sec{padding:56px 20px;border-bottom:1px solid var(--ln)}
.label{font-family:var(--mono);font-size:11px;letter-spacing:.2em;color:var(--gy);margin-bottom:14px}
.label span{color:var(--bk);margin-right:10px}
h2{font-size:30px;line-height:1.3;font-weight:700;letter-spacing:-.02em;margin-bottom:20px}
.lead{color:#555;font-weight:300;margin:-6px 0 22px}
.principles{list-style:none;border-top:1px solid var(--bk)}
.principles li{padding:18px 0;border-bottom:1px solid var(--ln);display:grid;grid-template-columns:44px 1fr}
.principles .no{font-family:var(--mono);font-size:12px;padding-top:4px;grid-row:span 2}
.principles .ko{font-size:19px;font-weight:600}
.principles .en{font-size:13px;color:var(--gy);font-weight:300}
.subjects{list-style:none;display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--bk);margin-bottom:28px}
.subjects li{padding:14px 0;border-bottom:1px solid var(--ln);display:flex;align-items:baseline;gap:8px}
.subjects li:nth-child(odd){padding-right:10px}
.subjects .en{font-weight:700;font-size:20px;letter-spacing:-.01em}
.subjects .ko{font-size:13px;color:var(--gy)}
.courses{display:grid;gap:10px}
.courses div{background:var(--sage);padding:18px}
.courses h3{font-size:17px;margin-bottom:4px}
.courses p{font-size:14px;color:#3d4238;font-weight:400}
.rail{display:flex;gap:14px;overflow-x:auto;scroll-snap-type:x mandatory;scroll-padding:0 20px;margin:0 -20px;padding:0 20px 6px;scrollbar-width:none}
.rail::-webkit-scrollbar{display:none}
.teacher{flex:0 0 82%;scroll-snap-align:start;border-top:1px solid var(--bk);padding-top:14px}
.teacher img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block;filter:grayscale(.15)}
.teacher .subj{font-family:var(--mono);font-size:11px;letter-spacing:.2em;margin-top:14px;display:flex;align-items:center;gap:8px;text-transform:uppercase}
.teacher .subj i{width:7px;height:7px;border-radius:50%;background:var(--bk)}
.teacher .en{font-size:30px;font-weight:700;letter-spacing:-.02em;line-height:1.05;margin-top:6px}
.teacher .ko{letter-spacing:.4em;font-size:14px;margin-top:4px}
.teacher .career-h{font-family:var(--mono);font-size:10px;letter-spacing:.2em;color:var(--gy);margin-top:16px;padding-top:10px;border-top:1px solid var(--ln)}
.teacher .career{list-style:none;font-size:13px;color:#444;font-weight:300;margin-top:6px}
.teacher .career li{padding:3px 0}
figure{flex:0 0 78%;scroll-snap-align:start}
figure img{width:100%;aspect-ratio:4/5;object-fit:cover;display:block}
figcaption{font-family:var(--mono);font-size:11px;letter-spacing:.14em;color:var(--gy);margin-top:8px}
.info{display:grid;grid-template-columns:80px 1fr;border-top:1px solid var(--bk)}
.info dt,.info dd{padding:14px 0;border-bottom:1px solid var(--ln)}
.info dt{font-family:var(--mono);font-size:11px;letter-spacing:.1em;color:var(--gy);padding-top:17px}
.info dd{font-size:15px}
.maps{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-top:22px}
.maps a{border:1px solid var(--bk);text-align:center;padding:12px 4px;font-size:13px;text-decoration:none}
.dark{background:var(--bk);color:var(--iv);border:0}
.dark .label span{color:var(--iv)}
.dark .lead{color:#aaa}
.ctas{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}
.ctas a{display:flex;flex-direction:column;align-items:center;justify-content:center;text-decoration:none;font-weight:600;font-size:14px;height:52px;line-height:1.2}
.ctas .kakao{background:#F1E8CB;color:#111}
.ctas .naver{background:var(--sage);color:#111}
.ctas .tel{background:var(--iv);color:#111}
.ctas.big a{height:64px;font-size:15px}
.ctas small{font-size:10px;font-weight:400;opacity:.6}
.dock{position:fixed;left:0;right:0;bottom:0;z-index:30;background:var(--bk);padding:10px 12px calc(10px + env(safe-area-inset-bottom))}
.dock .ctas{max-width:536px;margin:0 auto}
footer{background:var(--bk);color:var(--iv);padding:40px 20px 60px;border-top:1px solid #333}
footer .ghost{font-weight:700;font-size:min(27vw,150px);letter-spacing:-.04em;color:#222;line-height:1}
footer .sig{font-size:22px;font-weight:600;margin:20px 0 26px;line-height:1.4}
footer .sig span{font-size:14px;color:#999;font-weight:300}
footer .small{font-size:12px;color:#999;line-height:1.8;border-top:1px solid #333;padding-top:16px}
'''

TICK = ' — '.join(['ENOCH MUSIC ACADEMY', 'FIND YOUR OWN TRUE SOUND', '나만의 진짜 소리를 찾는 곳'] * 4)
page = f'''<!doctype html>
<html lang="ko">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>{e(TITLE)}</title>
<meta name="description" content="{e(DESC)}">
<meta name="theme-color" content="#111111">
<meta property="og:type" content="website">
<meta property="og:title" content="{e(B['name'])}">
<meta property="og:description" content="{e(DESC)}">
<meta property="og:image" content="{HERO}">
<meta property="og:locale" content="ko_KR">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header><a href="#top">ENOCH MUSIC ACADEMY</a><a href="#contact">상담 →</a></header>
<nav class="toc"><a href="#about">ABOUT</a><a href="#lesson">LESSON</a><a href="#teachers">TEACHERS</a><a href="#space">SPACE</a><a href="#visit">VISIT</a><a href="#contact">CONTACT</a></nav>
<main id="top">
<section class="hero">
<img src="{HERO}" alt="에녹실용음악학원 시흥점 ENOCH 로고 월" width="1080" height="1296">
<h1 class="big">ENOCH</h1>
<p class="sig">{e(B['signature'])}</p>
<p class="sig-en">{e(B['signatureEn'])}</p>
<p class="name"><span>{e(B['name'])}</span><span>시흥 · 대야역</span></p>
</section>
<div class="ticker"><span>{TICK} — {TICK} — </span></div>
{sec_principle}
{sec_lesson}
{sec_teachers}
{sec_space}
{sec_visit}
{sec_contact}
</main>
{footer}
</div>
<div class="dock"><div class="ctas">{ctas}</div></div>
</body>
</html>'''
open(os.path.join(DIST, 'index.html'), 'w').write(page)
print('site/dist/index.html', f'teachers {len(T)}')
