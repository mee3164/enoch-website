# ENOCH LISTENING — Funk · R&B · Neo Soul (deck.html 생성)
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from _parts import HEAD, A6, A7
CSS2 = '''
.al{position:absolute;left:96px;right:96px;display:flex;gap:40px;padding-top:30px;border-top:1.5px solid var(--bk)}
.al .n{font-family:S,serif;line-height:1;margin-bottom:10px}
.al .t span{font-weight:300;color:var(--g);letter-spacing:-.5px;margin-left:10px}
.sec{position:absolute;left:96px;right:96px;top:180px;display:flex;justify-content:space-between;align-items:baseline}
.sec .h{font-size:60px;letter-spacing:-2.5px}
.s{word-break:keep-all}
</style>'''
FT = lambda n: f'<div class="ft"><span>Funk · R&amp;B · Neo Soul</span><span>0{n} / 07</span></div>'
CREDIT = '<div style="position:absolute;left:96px;right:96px;bottom:26px;font-size:13px;letter-spacing:.2px;color:#A8A39A">앨범 이미지 출처: Apple Music · 앨범 아트워크의 저작권은 각 음반사에 있습니다.</div>'
HD = lambda r="ENOCH LISTENING": f'<div class="hd"><span>ENOCH MUSIC ACADEMY</span><span>{r}</span></div>'
IMG = lambda c: f'../../images/앨범/{c}.jpg'

def album(top, n, cov, artist, title, year, track, listen, size=240, tsize=46):
    d = int(size * 0.96); off = int(size * 0.29)
    rec = (f'<div style="position:relative;width:{size+off+20}px;height:{size}px;flex:none">'
           f'<div style="position:absolute;left:{off}px;top:{(size-d)//2}px;width:{d}px;height:{d}px;border-radius:50%;background:#111">'
           f'<div style="position:absolute;left:{d*0.34:.0f}px;top:{d*0.34:.0f}px;width:{d*0.32:.0f}px;height:{d*0.32:.0f}px;border-radius:50%;background:#F1E8CB"></div></div>'
           f'<img src="{IMG(cov)}" style="position:absolute;left:0;top:0;width:{size}px;height:{size}px;object-fit:cover;display:block"></div>')
    return (f'<div class="al" style="top:{top}px">{rec}<div>'
            f'<div class="n" style="font-size:{int(tsize*1.1)}px">{n}</div><div class="ar">{artist}</div>'
            f'<div class="t" style="font-size:{tsize}px">{title}<span style="font-size:{int(tsize*0.62)}px">{year}</span></div>'
            f'<div class="row"><b>TRACK</b><span>{track}</span></div><div class="row"><b>LISTEN</b><span>{listen}</span></div></div></div>')

COVERS = ["stevie_wonder_hotter_than_july", "marvin_gaye_midnight_love", "james_ingram_its_your_night",
          "rick_james_street_songs", "zapp_zapp", "erykah_badu_baduizm", "musiq_soulchild_aijuswanaseing"]
S = []
grid = ''.join(f'<img src="{IMG(c)}" style="width:210px;height:210px;object-fit:cover;display:block">' for c in COVERS)
grid += '<div style="width:210px;height:210px;background:#111;color:#F1EDE4;display:flex;flex-direction:column;justify-content:flex-end;padding:20px;font-family:S,serif;font-size:64px;line-height:1">7<span style="font-family:var(--mono);font-size:16px;letter-spacing:2.5px;margin-top:10px">RECORDS</span></div>'
S.append(f'''<section class="s" id="a1">{HD()}
<div style="position:absolute;left:96px;top:160px;display:grid;grid-template-columns:repeat(4,210px);gap:16px">{grid}</div>
<div class="k" style="position:absolute;left:96px;top:690px">Funk · R&amp;B · Neo Soul</div>
<div class="h" style="position:absolute;left:92px;top:740px;font-size:92px;letter-spacing:-4.5px;line-height:1.15">Groove를 배우는<br><em>일곱 장의 Record</em></div>
<div class="p" style="position:absolute;left:96px;top:1000px">80년대 Funk · R&amp;B에서 Neo Soul까지.<br>한 장씩 꺼내 들어 보세요.</div>
{CREDIT}
{FT(1)}</section>''')
row = lambda k, t: f'<div style="display:flex;gap:40px;padding:28px 0;border-bottom:1px solid rgba(17,17,17,.15)"><span class="k" style="width:140px;flex:none;padding-top:8px">{k}</span><span class="p">{t}</span></div>'
S.append(f'''<section class="s" id="a2">{HD()}
<div class="k" style="position:absolute;left:96px;top:200px">Why These Records</div>
<div class="h" style="position:absolute;left:92px;top:250px">80년대의 Rhythm,<br><em>Neo Soul까지</em></div>
<div class="p" style="position:absolute;left:96px;right:96px;top:520px">80년대엔 Drum Machine과 Synthesizer가 R&amp;B 한가운데로 들어왔습니다.<br>90년대 후반 Neo Soul은 옛 Soul과 Funk의 결을 다시 꺼내 왔고요.<br>시대는 달라도, Groove를 듣는 귀는 같아요.</div>
<div style="position:absolute;left:96px;right:96px;top:800px;border-top:1.5px solid #111">
{row("Bass","Riff 하나가 곡 전체를 끌고 갑니다.")}
{row("Drums","Drum Machine과 사람이 친 Drum,<br>박의 느낌을 비교해 보세요.")}
{row("Voice","Rhythm 위에서 말하듯 부르는 Vocal과 겹겹이 쌓인 Chorus.")}
</div>{FT(2)}</section>''')
S.append(f'''<section class="s" id="a3">{HD()}
<div class="sec"><div class="h">80s R&amp;B</div><div class="k">Records 01 — 03</div></div>
{album(290,"01",COVERS[0],"Stevie Wonder","Hotter Than July","1980","Master Blaster (Jammin')","Reggae Rhythm 위에 얹힌 Bass와 Chorus",size=200,tsize=40)}
{album(600,"02",COVERS[1],"Marvin Gaye","Midnight Love","1982","Sexual Healing","Drum Machine 위에서 Vocal이 박을 타는 방식",size=200,tsize=40)}
{album(910,"03",COVERS[2],"James Ingram","It's Your Night","1983","Yah Mo B There","두 Vocal이 주고받는 소리와 화음",size=200,tsize=40)}
{CREDIT}
{FT(3)}</section>''')
S.append(f'''<section class="s" id="a4">{HD()}
<div class="sec"><div class="h">80s Funk</div><div class="k">Records 04 — 05</div></div>
{album(300,"04",COVERS[3],"Rick James","Street Songs","1981","Give It to Me Baby","반복되는 Bass Riff와 Brass")}
{album(740,"05",COVERS[4],"Zapp","Zapp","1980","More Bounce to the Ounce","Talk Box, 단순한 Riff가 만드는 Groove")}
{CREDIT}
{FT(4)}</section>''')
S.append(f'''<section class="s" id="a5">{HD()}
<div class="sec"><div class="h">Neo Soul</div><div class="k">Records 06 — 07</div></div>
{album(300,"06",COVERS[5],"Erykah Badu","Baduizm","1997","On &amp; On","뒤로 살짝 기대는 듯한 느긋한 박")}
{album(740,"07",COVERS[6],"Musiq Soulchild","Aijuswanaseing","2000","Just Friends (Sunny)","말하듯 짧게 끊어 부르는 Phrasing")}
{CREDIT}
{FT(5)}</section>''')
a6 = A6.replace('<span>80년대 Funk · R&amp;B</span>', '<span>Funk · R&amp;B · Neo Soul</span>')
a7 = A7.replace('<span>80년대 Funk · R&amp;B</span>', '<span>Funk · R&amp;B · Neo Soul</span>')
open('deck.html', 'w').write(HEAD + CSS2 + '</head><body>' + ''.join(S) + a6 + a7 + '</body></html>')
