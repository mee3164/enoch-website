import math, random
random.seed(7)
BG="#F4F2EC"; INK="#1a1a1a"
def f(v): return f"{v:.1f}"
def tube(d,w=4.6):
    return (f'<path d="{d}" stroke="{INK}" stroke-width="{w}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
            f'<path d="{d}" stroke="{BG}" stroke-width="{w-2.6:.1f}" fill="none" stroke-linecap="round" stroke-linejoin="round"/>')
def ell(cx,cy,rx,ry,cls="o",fill="none",extra=""):
    return f'<ellipse cx="{f(cx)}" cy="{f(cy)}" rx="{f(rx)}" ry="{f(ry)}" class="{cls}" fill="{fill}" {extra}/>'
def line(x1,y1,x2,y2,cls="f"):
    return f'<line x1="{f(x1)}" y1="{f(y1)}" x2="{f(x2)}" y2="{f(y2)}" class="{cls}"/>'
def sparkles(n,x0,y0,w,h):
    s=""
    for _ in range(n):
        x=x0+random.random()*w; y=y0+random.random()*h; r=random.random()
        if r<.55: s+=f'<circle cx="{f(x)}" cy="{f(y)}" r="{f(.8+random.random()*1.1)}" fill="{INK}"/>'
        elif r<.8:
            k=3+random.random()*3; s+=f'<path d="M{f(x-k)} {f(y)}H{f(x+k)}M{f(x)} {f(y-k)}V{f(y+k)}" class="x"/>'
        else:
            k=6+random.random()*5
            s+=f'<path d="M{f(x)} {f(y-k)}Q{f(x)} {f(y)} {f(x+k)} {f(y)}Q{f(x)} {f(y)} {f(x)} {f(y+k)}Q{f(x)} {f(y)} {f(x-k)} {f(y)}Q{f(x)} {f(y)} {f(x)} {f(y-k)}Z" fill="{INK}"/>'
    return s

DEFS=f'''<defs>
<filter id="w"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="3"/><feDisplacementMap in="SourceGraphic" scale="1.4"/></filter>
<pattern id="h1" width="4.5" height="4.5" patternUnits="userSpaceOnUse" patternTransform="rotate(38)"><line x1="0" y1="0" x2="0" y2="4.5" stroke="{INK}" stroke-width=".7"/></pattern>
<pattern id="h2" width="3" height="3" patternUnits="userSpaceOnUse" patternTransform="rotate(38)"><line x1="0" y1="0" x2="0" y2="3" stroke="{INK}" stroke-width=".8"/></pattern>
<pattern id="hx" width="4" height="4" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><path d="M0 0V4M0 0H4" stroke="{INK}" stroke-width=".6"/></pattern>
<pattern id="dots" width="5" height="5" patternUnits="userSpaceOnUse"><circle cx="2.5" cy="2.5" r=".9" fill="{INK}"/></pattern>
</defs>'''

# ---------- 1. Mic on boom stand ----------
def mic():
    s=sparkles(46,10,0,230,170)
    hub=(150,345)
    for fx,fy in [(62,430),(238,430),(166,438)]:
        s+=tube(f"M{hub[0]} {hub[1]} L{fx} {fy}",4.2)
        s+=f'<rect x="{fx-5}" y="{fy-2}" width="10" height="5" fill="{INK}"/>'
    s+=f'<rect x="141" y="336" width="18" height="16" class="o" fill="url(#h1)"/>'
    s+=tube("M150 336 V236",5.2)
    s+=f'<rect x="143" y="226" width="14" height="12" class="o" fill="url(#h2)"/><path d="M157 230 h8 v6 h-8" class="f"/>'
    s+=tube("M150 228 V176",4.2)
    # boom clutch + arm + counterweight
    s+=f'<circle cx="150" cy="172" r="8" class="o" fill="{BG}"/><circle cx="150" cy="172" r="3" fill="{INK}"/><path d="M150 172 l12 10" class="o"/>'
    s+=tube("M214 214 L72 108",4.4)
    s+=f'<g transform="rotate(37 214 214)"><rect x="200" y="206" width="30" height="16" class="o" fill="url(#hx)"/><path d="M206 206v16M212 206v16" class="x"/></g>'
    # mic (local coords: pointing up), placed at boom end
    m=f'<g transform="translate(64 102) rotate(-38)">'
    m+='<clipPath id="ball"><circle cx="0" cy="-74" r="25"/></clipPath>'
    m+=f'<circle cx="0" cy="-74" r="25" fill="{BG}"/>'
    m+=f'<g clip-path="url(#ball)" opacity=".85"><rect x="-30" y="-104" width="60" height="60" fill="url(#hx)"/></g>'
    m+=f'<path d="M-25 -74 A25 25 0 0 0 25 -74" class="x"/><path d="M-18 -91 Q0 -100 18 -91" stroke="{BG}" stroke-width="3" fill="none"/>'
    m+=f'<circle cx="0" cy="-74" r="25" class="o"/>'
    m+=f'<rect x="-21" y="-52" width="42" height="8" class="o" fill="{BG}"/><path d="M-21 -48 H21" class="x"/>'
    m+=f'<path d="M-17 -44 L-11 46 H11 L17 -44 Z" class="o" fill="{BG}"/>'
    m+=f'<path d="M5 -40 L9 44 H11 L17 -44 Z" fill="url(#h2)"/>'
    for y in range(-36,44,8): m+=f'<path d="M{f(-16+ (y+44)*0.066)} {y} q4 2 8 0" class="x"/>'
    m+=f'<rect x="-9" y="46" width="18" height="10" class="o" fill="url(#h1)"/>'
    m+=f'<path d="M-14 -2 H14 M-14 6 H14" class="f"/><rect x="-16" y="-6" width="32" height="16" class="o" fill="none"/>'
    m+='</g>'
    s+=m
    s+='<path d="M98 158 C88 200 40 230 52 300 C60 350 110 360 120 420 L126 438" class="f" stroke-dasharray="1 0"/>'
    s+='<path d="M98 158 C88 200 40 230 52 300 C60 350 110 360 120 420 L126 438" class="x" transform="translate(2 1)"/>'
    return s

# ---------- 2. Keyboard on X-stand ----------
def keyboard():
    s=sparkles(18,290,0,90,56)
    # music rack + sheet
    s+=tube("M160 64 L156 22",3.2)+tube("M230 64 L234 22",3.2)
    s+=f'<g transform="rotate(-3 195 30)"><rect x="150" y="0" width="92" height="44" class="o" fill="{BG}"/>'
    for i in range(2):
        for k in range(5): s+=line(156,10+i*18+k*2.6,236,10+i*18+k*2.6,"x")
    for x,y in [(166,13),(178,11),(196,15),(214,12),(226,30),(186,31),(204,29)]:
        s+=ell(x,y+4,2.6,1.8,"x",INK)+line(x+2.4,y+4,x+2.4,y-6,"x")
    s+='</g>'
    # body
    s+=f'<rect x="20" y="62" width="340" height="60" class="o" fill="{BG}"/>'
    s+=f'<rect x="20" y="122" width="340" height="7" class="o" fill="url(#h2)"/>'
    s+=f'<path d="M20 62 L14 68 V128 L20 129" class="o" fill="url(#h1)"/>'
    # panel
    for i in range(6):
        cx=36+i*15; s+=f'<circle cx="{cx}" cy="74" r="5" class="f" fill="{BG}"/>'+line(cx,74,cx+3*math.cos(i),74-3.5,"f")
    for i in range(5):
        x=134+i*9; s+=line(x,67,x,83,"x")+f'<rect x="{x-3}" y="{70+ (i*5)%10}" width="6" height="4" fill="{INK}"/>'
    s+=f'<rect x="186" y="66" width="62" height="17" class="o" fill="url(#h1)"/><rect x="190" y="69" width="30" height="5" fill="{BG}"/>'
    s+=f'<rect x="262" y="66" width="88" height="17" fill="url(#dots)"/><rect x="262" y="66" width="88" height="17" class="f"/>'
    s+=line(20,88,360,88,"f")
    # keys
    n=22; x0=26; w=(354-x0)/n
    s+=f'<rect x="{x0}" y="88" width="{354-x0}" height="32" fill="{BG}" class="f"/>'
    for i in range(1,n): s+=line(x0+i*w,88,x0+i*w,120,"x")
    for i in range(n):
        if i%7 in (0,1,3,4,5) and i<n-1:
            bx=x0+(i+1)*w-4.6
            s+=f'<rect x="{f(bx)}" y="88" width="9.2" height="19" fill="{INK}"/>'+line(bx+2.2,90,bx+2.2,104,"hl")
    # X stand
    s+=tube("M112 132 L272 280",5)+tube("M272 132 L112 280",5)
    s+=f'<circle cx="192" cy="206" r="7" class="o" fill="{BG}"/><circle cx="192" cy="206" r="2.4" fill="{INK}"/>'
    s+=tube("M86 132 H138",4)+tube("M246 132 H298",4)
    s+=tube("M84 282 H140",4)+tube("M244 282 H300",4)
    for x in (80,136,240,296): s+=f'<rect x="{x}" y="278" width="8" height="8" fill="{INK}"/>'
    # floating notes
    s+=f'<g transform="translate(330 20) rotate(12)">{ell(0,20,4.5,3.2,"f",INK)}{line(4,20,4,0,"f")}<path d="M4 0 q8 4 6 12" class="f"/></g>'
    s+=f'<g transform="translate(34 18) rotate(-10)">{ell(0,22,4,3,"f",INK)}{ell(16,18,4,3,"f",INK)}<path d="M4 22V2L20 -2V18M4 7L20 3" class="f"/></g>'
    return s

# ---------- 3. Acoustic guitar ----------
def guitar():
    body="M110 214 C70 214 52 236 54 268 C56 296 72 306 70 322 C68 338 44 352 44 388 C44 430 76 452 110 452 C144 452 176 430 176 388 C176 352 152 338 150 322 C148 306 164 296 166 268 C168 236 150 214 110 214 Z"
    s=sparkles(22,0,0,60,200)
    s+='<g transform="rotate(13 110 300)">'
    s+=f'<clipPath id="gb"><path d="{body}"/></clipPath>'
    s+=f'<path d="{body}" fill="{BG}"/>'
    s+='<g clip-path="url(#gb)">'
    for x in range(58,170,7): s+=f'<path d="M{x} 210 Q{x+3} 330 {x-1} 456" class="x" opacity=".55"/>'
    s+=f'<rect x="138" y="200" width="50" height="270" fill="url(#h1)" opacity=".9"/>'
    s+=f'<rect x="156" y="200" width="40" height="270" fill="url(#hx)"/>'
    s+='</g>'
    s+=f'<path d="{body}" class="o"/>'
    s+=f'<path d="{body}" class="f" transform="translate(110 333) scale(.955) translate(-110 -333)"/>'
    # pickguard
    s+=f'<path d="M128 314 C150 318 154 344 138 354 C124 361 116 342 128 314 Z" class="f" fill="url(#h2)"/>'
    # soundhole + rosette
    s+=f'<circle cx="110" cy="300" r="27" class="f"/><circle cx="110" cy="300" r="24.5" class="x" stroke-dasharray="1.5 1.5"/><circle cx="110" cy="300" r="22.5" class="f"/>'
    s+=f'<circle cx="110" cy="300" r="20" fill="{INK}"/>'
    # bridge
    s+=f'<path d="M84 398 Q110 392 136 398 V408 Q110 404 84 408 Z" class="o" fill="url(#h1)"/>'
    s+=line(96,396,124,396,"o")
    for i in range(6): s+=f'<circle cx="{f(96+i*5.6)}" cy="403" r="1.6" fill="{BG}" class="x"/>'
    # neck + frets
    s+=f'<path d="M101 70 L99 226 H121 L119 70 Z" class="o" fill="{BG}"/>'
    s+=f'<path d="M115 72 L117 226 H121 L119 70 Z" fill="url(#h2)"/>'
    L=323
    ys=[70+L*(1-2**(-k/12)) for k in range(1,12)]
    for y in ys: s+=line(100,y,120,y,"f")
    for k in (3,5,7,9):
        y=(ys[k-1]+ys[k-2])/2; s+=f'<circle cx="110" cy="{f(y)}" r="1.6" fill="{INK}"/>'
    s+=f'<rect x="100" y="68" width="20" height="3" fill="{INK}"/>'
    # headstock + tuners
    s+=f'<path d="M101 70 L96 12 Q110 4 124 12 L119 70 Z" class="o" fill="url(#h1)"/>'
    for y in (24,40,56):
        for x,kx in ((104,86),(116,134)):
            s+=f'<circle cx="{x}" cy="{y}" r="2.2" fill="{BG}" class="x"/>'+line(x,y,kx,y,"f")
            s+=ell(kx,y,5,3.4,"f",BG)
    # strings
    for i in range(6):
        xt=103+i*2.8; xb=96+i*5.6
        s+=line(xt,40 if i in(0,5) else 24+ (i%3)*16,xt,71,"x")+line(xt,71,xb,403,"x")
    s+='</g>'
    return s

# ---------- 4. Score + headphones ----------
def score():
    s=f'<g transform="rotate(-11 120 140)"><rect x="40" y="24" width="180" height="222" class="f" fill="{BG}"/>'
    for k in range(4):
        for j in range(5): s+=line(52,52+k*46+j*4.4,208,52+k*46+j*4.4,"x")
    s+='</g>'
    s+=f'<g transform="rotate(-4 120 140)"><path d="M28 30 H206 V226 L188 246 H28 Z" class="o" fill="{BG}"/>'
    s+=f'<path d="M206 226 L188 228 L188 246 Z" class="f" fill="url(#h2)"/>'
    s+=f'<text x="117" y="22" text-anchor="middle" font-family="CG" font-size="15" font-style="italic">Etude No.1</text>'
    random.seed(3)
    for k in range(4):
        y0=52+k*44
        for j in range(5): s+=line(40,y0+j*4.4,196,y0+j*4.4,"x")
        for bx in (40,92,144,196): s+=line(bx,y0,bx,y0+17.6,"f")
        if k==0: s+=f'<text x="46" y="{y0+8}" font-family="CG" font-size="11" font-weight="500">4</text><text x="46" y="{y0+17}" font-family="CG" font-size="11" font-weight="500">4</text>'
        for b in range(3):
            xs=[40+b*52+(12 if k==0 and b==0 else 8)+i*11 for i in range(4)]
            pos=[random.randint(-2,7) for _ in xs]
            tops=[]
            for x,p in zip(xs,pos):
                yy=y0+17.6-p*2.2
                s+=ell(x,yy,3.2,2.3,"x",INK,f'transform="rotate(-20 {f(x)} {f(yy)})"')
                s+=line(x+3,yy,x+3,yy-15,"x"); tops.append((x+3,yy-15))
            if b%2==0:
                s+=f'<path d="M{f(tops[0][0])} {f(tops[0][1])} L{f(tops[1][0])} {f(tops[1][1])}" stroke="{INK}" stroke-width="2"/>'
                s+=f'<path d="M{f(tops[2][0])} {f(tops[2][1])} L{f(tops[3][0])} {f(tops[3][1])}" stroke="{INK}" stroke-width="2"/>'
    s+='</g>'
    # headphones
    s+=tube("M196 178 C190 80 300 70 302 168",6)
    s+='<path d="M206 160 C204 98 288 92 292 156" class="x" stroke-dasharray="2 2.5"/>'
    for cx,cy in ((196,196),(302,186)):
        s+=f'<rect x="{cx-4}" y="{cy-34}" width="8" height="14" class="f" fill="url(#h2)"/>'
        s+=ell(cx,cy,19,28,"o",BG)+ell(cx,cy,19,28,"x","url(#h1)")+ell(cx,cy,12,19,"f",BG)+ell(cx,cy,6,10,"x","url(#hx)")
    coil="M196 224 "+" ".join(f"Q{f(190+8*math.sin(i))} {f(232+i*4)} {f(196+ (6 if i%2 else -6))} {f(234+i*4)}" for i in range(6))
    s+=f'<path d="{coil}" class="f"/><path d="M196 258 C200 280 260 270 280 256" class="f"/>'
    return s

# ---------- 5. Drum kit ----------
def shell(cx,top,rx,ry,h,lugs=4):
    s=f'<path d="M{cx-rx} {top} V{top+h} A{rx} {ry} 0 0 0 {cx+rx} {top+h} V{top}" class="o" fill="{BG}"/>'
    s+=f'<clipPath id="sh{cx}{top}"><path d="M{cx-rx} {top} V{top+h} A{rx} {ry} 0 0 0 {cx+rx} {top+h} V{top} Z"/></clipPath>'
    s+=f'<g clip-path="url(#sh{cx}{top})"><rect x="{cx+rx*.35}" y="{top-5}" width="{rx}" height="{h+ry+10}" fill="url(#h1)"/><rect x="{cx+rx*.7}" y="{top-5}" width="{rx}" height="{h+ry+10}" fill="url(#hx)"/></g>'
    for i in range(lugs):
        x=cx-rx+ (i+0.5)*(2*rx/lugs)
        s+=f'<rect x="{f(x-2.2)}" y="{f(top+h*.32)}" width="4.4" height="{f(h*.3)}" class="x" fill="{INK}"/>'
        s+=line(x,top+3,x,top+h*.32,"x")
    s+=ell(cx,top+h,rx,ry,"x",extra='stroke-dasharray="2 2"')
    s+=f'<path d="M{cx-rx} {top+h-3} A{rx} {ry} 0 0 0 {cx+rx} {top+h-3}" class="f"/>'
    s+=ell(cx,top,rx,ry,"o",BG)+ell(cx,top,rx-3,ry-1.6,"x")
    return s
def cymbal(cx,cy,rx,ry,rot):
    s=f'<g transform="rotate({rot} {cx} {cy})">'+ell(cx,cy,rx,ry,"o",BG)
    for k in range(1,6): s+=ell(cx,cy,rx*k/6,ry*k/6,"x")
    s+=f'<path d="M{cx-rx} {cy} A{rx} {ry} 0 0 0 {cx+rx} {cy} A{rx} {ry*0.6} 0 0 1 {cx-rx} {cy}" fill="url(#h1)"/>'
    s+=ell(cx,cy-1.5,rx*.16,ry*.4,"f",INK)+'</g>'
    return s
def tripod(x,y,floor):
    return tube(f"M{x} {y} V{floor-22}",3.6)+tube(f"M{x} {floor-24} L{x-20} {floor} M{x} {floor-24} L{x+20} {floor} M{x} {floor-24} L{x+4} {floor+3}",3.2)
def drums():
    FL=312; s=""
    s+=tripod(48,150,FL)+f'<path d="M30 {FL} L48 {FL-10} L60 {FL}" class="o" fill="url(#h1)"/>'
    s+=tube("M48 150 V100",2.6)
    s+=cymbal(48,108,44,7,0)+cymbal(48,100,44,7,0)
    s+=tripod(122,96,FL)+tube("M122 96 L132 74",3)+cymbal(134,64,54,11,-9)
    s+=tripod(372,104,FL)+tube("M372 104 L362 86",3)+cymbal(358,78,58,12,7)
    s+=f'<clipPath id="bd"><circle cx="212" cy="222" r="80"/></clipPath>'
    s+=f'<circle cx="212" cy="222" r="80" class="o" fill="{BG}"/>'
    s+=f'<g clip-path="url(#bd)"><circle cx="186" cy="200" r="86" fill="none" stroke="url(#h1)" stroke-width="58" opacity=".9"/></g>'
    s+=f'<circle cx="212" cy="222" r="80" class="o"/><circle cx="212" cy="222" r="73" class="f"/><circle cx="212" cy="222" r="69" class="x"/>'
    for i in range(12):
        a=i*math.pi/6+0.26; x=212+76.5*math.cos(a); y=222+76.5*math.sin(a)
        s+=f'<rect x="{f(x-2.5)}" y="{f(y-5)}" width="5" height="10" fill="{INK}" transform="rotate({f(math.degrees(a)+90)} {f(x)} {f(y)})"/>'
    s+=f'<circle cx="212" cy="222" r="34" class="f" fill="{BG}"/><circle cx="212" cy="222" r="30" class="x"/>'
    s+=f'<text x="212" y="226" text-anchor="middle" font-family="IBM Plex Mono,monospace" font-size="10.5" letter-spacing="2.6">ENOCH</text>'
    s+=tube("M150 276 L130 314",3.2)+tube("M274 276 L294 314",3.2)
    s+=tube("M212 142 V120 M212 124 L176 108 M212 124 L252 104",3.4)
    s+=shell(168,92,34,8,42)+shell(254,88,36,9,46)
    s+=tripod(96,200,FL)+shell(96,172,34,8,28,5)
    s+=f'<path d="M78 {172+20} h10 v8 h-10z" fill="{INK}"/>'
    s+=shell(336,178,38,9,72,4)
    for lx in (306,368): s+=tube(f"M{lx} 200 L{lx+(-6 if lx<330 else 6)} {FL}",3)
    # sticks resting on snare
    s+=f'<path d="M66 166 L130 150" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/><path d="M66 166 L130 150" stroke="{BG}" stroke-width="1.2"/>'
    s+=f'<path d="M70 172 L134 160" stroke="{INK}" stroke-width="3.4" stroke-linecap="round"/><path d="M70 172 L134 160" stroke="{BG}" stroke-width="1.2"/>'
    s+=line(0,FL+4,420,FL+4,"x")
    return s

def svg(x,y,w,h,content):
    return f'<svg class="ill" style="left:{x}px;top:{y}px" width="{w}" height="{h}" viewBox="0 0 {w} {h}" filter="url(#w)">{content}</svg>'

html=f'''<!doctype html><html><head><meta charset="utf-8">
<style>@font-face{{font-family:"CG";src:url(cg300.ttf);font-weight:300}}@font-face{{font-family:"CG";src:url(cg500.ttf);font-weight:500}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;background:{BG};color:#111;font-family:Pretendard,"Noto Sans KR",sans-serif;position:relative;overflow:hidden}}
.top{{position:absolute;top:70px;left:70px;right:70px;display:flex;justify-content:space-between;font-family:"IBM Plex Mono",monospace;font-size:23px;letter-spacing:4px}}
.grid{{position:absolute;left:62px;top:390px;width:956px;height:630px;background-image:linear-gradient(#C9CBD4 1px,transparent 1px),linear-gradient(90deg,#C9CBD4 1px,transparent 1px);background-size:159.33px 210px;border-right:1px solid #C9CBD4;border-bottom:1px solid #C9CBD4}}
.word{{position:absolute;left:0;right:0;top:640px;text-align:center;font-family:"CG",serif;font-weight:300;font-size:150px;letter-spacing:6px;line-height:1;white-space:nowrap}}
.cats{{position:absolute;left:0;right:0;top:1104px;text-align:center;font-family:"CG",serif;font-size:36px;font-weight:500;letter-spacing:.5px}}
.ko{{position:absolute;left:0;right:0;top:1170px;text-align:center}}
.ko b{{display:block;font-size:38px;font-weight:600;margin-bottom:14px}}
.ko span{{font-size:28px;color:#444}}
svg.ill{{position:absolute;overflow:visible}}
.o{{fill:none;stroke:{INK};stroke-width:1.7;stroke-linecap:round;stroke-linejoin:round}}
.f{{fill:none;stroke:{INK};stroke-width:1.05;stroke-linecap:round;stroke-linejoin:round}}
.x{{fill:none;stroke:{INK};stroke-width:.65;stroke-linecap:round}}
.hl{{stroke:{BG};stroke-width:.8}}
</style></head><body>
<svg width="0" height="0" style="position:absolute">{DEFS}</svg>
<div class="top"><span>ENOCH MUSIC ACADEMY</span><span>TRUE SOUND <b>SIHEUNG</b></span></div>
<div class="grid"></div>
{svg(80,140,280,440,mic())}
{svg(352,228,380,300,keyboard())}
{svg(800,120,220,470,guitar())}
{svg(60,815,320,290,score())}
{svg(596,770,420,320,drums())}
<div class="word">TRUE SOUND</div>
<div class="cats">Vocal · Guitar · Drum · Bass · Piano · MIDI · Composition</div>
<div class="ko"><b>나만의 진짜 소리를 찾는 곳.</b><span>일곱 과목, 입시 · 취미 · 성인 · 전문 모든 과정 1:1 레슨</span></div>
</body></html>'''
open("poster.html","w").write(html)
