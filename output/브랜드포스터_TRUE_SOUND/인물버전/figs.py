from lib import *
SKIN="#fbf8f2"; BLK="#2b2b2b"; GRY="#7d7b76"; LG="#b9b7b1"

def face_glasses(cx,cy,rx=13.5,ry=16.5, glasses=True, smile=True):
    s=shape(path([(cx,cy-ry),(cx+rx,cy-3),(cx+rx*.7,cy+ry*.8),(cx,cy+ry),(cx-rx*.7,cy+ry*.8),(cx-rx,cy-3)],True),SKIN,1.8)
    if glasses:
        s+=f'<circle cx="{cx-5.5}" cy="{cy-1}" r="4.6" fill="none" stroke="{INK}" stroke-width="1.5"/><circle cx="{cx+5.5}" cy="{cy-1}" r="4.6" fill="none" stroke="{INK}" stroke-width="1.5"/>'
        s+=stroke(f"M{cx-1} {cy-1} h2",1.3)
    else:
        s+=stroke(f"M{cx-7} {cy} q2.5 2 5 0 M{cx+2} {cy} q2.5 2 5 0",1.3)
    s+=f'<circle cx="{cx-8}" cy="{cy+5}" r="2.6" fill="#e9d3c8" opacity=".8"/><circle cx="{cx+8}" cy="{cy+5}" r="2.6" fill="#e9d3c8" opacity=".8"/>'
    s+=stroke(f"M{cx-3} {cy+9} q3 {2.5 if smile else 0} 6 0",1.3)
    return s

# ---- D: singer walking (long hair, oversized blazer, crop top, wide pants), holding mic
def singer():
    s=""
    # trousers: one wide shape, inner seam, crotch at ~205
    pants=[(90,156),(142,156),(146,214),(160,316),(126,320),(116,222),(106,320),(70,318),(84,214)]
    s+=shape(poly(pants),GRY,2)
    s+=wash(poly(pants),"dP",[([(84,180),(80,250),(78,310)],7,.4),([(132,200),(146,260),(150,312)],6,.35),([(100,175),(96,250)],3,.3)])
    s+=stroke("M100 168 L94 310 M132 168 L142 312",1,"#555")
    # shoes
    s+=shape("M68 316 C64 328 72 334 96 334 C110 334 112 326 108 318 Z","#f7f5ef",1.8)
    s+=shape("M124 318 C120 330 130 334 154 334 C166 334 166 324 160 316 Z","#f7f5ef",1.8)
    # crop top, midriff, waistband
    s+=shape(poly([(98,84),(126,84),(128,126),(96,126)]),"#1d1d1d",1.6)
    s+=shape(poly([(96,126),(128,126),(130,148),(94,148)]),SKIN,1.4)
    s+=f'<circle cx="112" cy="138" r="1.1" fill="{INK}"/>'
    s+=shape(poly([(90,148),(142,148),(142,158),(90,158)]),"#5f5d58",1.6)
    # blazer halves
    jl=[(100,72),(74,80),(66,92),(62,198),(92,204),(96,132),(90,112),(100,84)]
    jr=[(124,72),(150,80),(160,92),(166,196),(136,204),(130,132),(136,112),(124,84)]
    s+=shape(poly(jl),BLK,2.2); s+=wash(poly(jl),"jL",[([(70,100),(68,150),(66,192)],7,.25),([(82,96),(84,130)],3,.3)])
    s+=shape(poly(jr),BLK,2.2); s+=wash(poly(jr),"jR",[([(154,100),(158,150),(160,190)],8,.22)])
    s+=stroke("M90 112 L98 120 M136 112 L128 120",1.3,"#aaa")
    # hanging sleeve (right) with cuff
    s+=shape(poly([(150,80),(166,90),(176,194),(152,198),(148,130)]),BLK,2.2)
    s+=wash(poly([(150,80),(166,90),(176,194),(152,198),(148,130)]),"sR",[([(164,100),(170,180)],5,.25)])
    s+=stroke("M153 188 L175 184",1.2,"#999")
    # neck + head
    s+=shape(poly([(107,60),(117,60),(118,76),(106,76)]),SKIN,1.4)
    s+='<g transform="translate(0 6) ">'
    s+=face_glasses(112,46)
    s+=stroke(path([(99,42),(101,28),(112,22),(123,28),(125,42)]),2.2)
    s+=stroke("M112 22 L111 33",1.4)
    # long hair strands over shoulders
    s+=stroke(path([(100,34),(94,60),(84,100),(70,150)]),2)
    s+=stroke(path([(103,40),(100,70),(96,96)]),1.6)
    s+=stroke(path([(124,34),(132,62),(142,100),(156,140)]),2)
    s+=stroke(path([(121,40),(124,70),(126,90)]),1.6)
    s+='</g>'
    # mic arm (left): upper arm down, forearm up to chin
    s+=shape(plimb([(72,86,22),(66,148,20),(98,108,15)]),BLK,2.2)
    s+=wash(plimb([(72,86,22),(66,148,20),(98,108,15)]),"aL",[([(66,100),(64,140)],5,.25)])
    s+=f'<g transform="rotate(-22 104 84)"><rect x="100.5" y="72" width="7" height="26" rx="3" fill="#2a2a2a" stroke="{INK}" stroke-width="1.4"/><circle cx="104" cy="69" r="7" fill="#e8e6e0" stroke="{INK}" stroke-width="1.6"/><circle cx="104" cy="69" r="7" fill="url(#hh)"/></g>'
    s+=hand(102,100,-35,1.05)
    return s


def gtr(tx,ty,rot,sc,bass=False):
    body=("M110 214 C70 214 52 236 54 268 C56 296 72 306 70 322 C68 338 44 352 44 388 C44 430 76 452 110 452 C144 452 176 430 176 388 C176 352 152 338 150 322 C148 306 164 296 166 268 C168 236 150 214 110 214 Z" if not bass else
          "M110 250 C84 250 76 226 62 222 C48 220 50 250 58 274 C64 296 46 330 46 372 C46 424 76 448 110 448 C146 448 176 426 176 380 C176 340 160 318 162 296 C164 270 176 250 168 232 C160 216 142 246 110 250 Z")
    g=f'<g transform="translate({tx} {ty}) rotate({rot}) scale({sc}) translate(-110 -333)">'
    g+=shape(body,"#2c2c2c" if bass else "#ece4d4",2.2/sc)
    g+=wash(body,f"gb{tx}{ty}",[([(70,260),(60,330),(64,420)],18,.18),([(150,250),(160,330)],8,.15)]) if not bass else wash(body,f"gb{tx}{ty}",[([(70,300),(62,380)],14,.28)])
    if not bass:
        g+=f'<circle cx="110" cy="300" r="20" fill="{INK}"/><circle cx="110" cy="300" r="25" fill="none" stroke="{INK}" stroke-width="{1/sc:.2f}"/>'
        g+=f'<path d="M84 398 Q110 392 136 398 V408 Q110 404 84 408 Z" fill="{INK}"/>'
    else:
        g+=f'<rect x="88" y="330" width="44" height="14" fill="#ddd" stroke="{INK}" stroke-width="{1.4/sc:.2f}"/><rect x="88" y="380" width="44" height="12" fill="#ddd" stroke="{INK}" stroke-width="{1.4/sc:.2f}"/>'
        g+=f'<path d="M126 268 C150 270 160 300 150 330 L140 300 Z" fill="#f4f2ec" stroke="{INK}" stroke-width="{1.2/sc:.2f}"/>'
    top=(40 if bass else 70)
    g+=shape(f"M101 {top} L99 {250 if bass else 226} H121 L119 {top} Z","#3b342c",1.8/sc)
    for k in range(1,14 if bass else 12):
        y=top+(300 if bass else 323)*(1-2**(-k/12))
        if y< (250 if bass else 226): g+=f'<line x1="100" y1="{y:.1f}" x2="120" y2="{y:.1f}" stroke="#bbb" stroke-width="{1/sc:.2f}"/>'
    g+=shape(f"M101 {top} L96 {top-56} Q110 {top-64} 124 {top-56} L119 {top} Z","#1e1e1e",1.8/sc)
    n=4 if bass else 6
    for i in range(n):
        xb=(98+i*8) if bass else 96+i*5.6
        g+=f'<line x1="{103+i*(14/(n-1)):.1f}" y1="{top-50}" x2="{xb:.1f}" y2="{386 if bass else 403}" stroke="#f0ede6" stroke-width="{.8/sc:.2f}"/>'
    g+='</g>'
    return g

def messy_hair(cx,cy):
    d=path([(cx-16,cy+6),(cx-20,cy-10),(cx-10,cy-22),(cx+4,cy-24),(cx+18,cy-16),(cx+20,cy+2),(cx+14,cy-6),(cx+4,cy-12),(cx-8,cy-8),(cx-12,cy+4)],True)
    s=shape(d,"#222",1.8)
    s+=stroke(f"M{cx-12} {cy-14} q8 -6 18 -2 M{cx-6} {cy-18} q10 -4 18 4",1,"#888")
    return s

# ---- A: guitarist sitting on a stool
def guitarist():
    s=""
    # stool
    s+=stroke("M138 254 L124 416 M184 254 L198 416 M160 258 L160 416 M130 352 H194",2.2)
    s+=shape("M128 250 Q160 242 192 250 L192 258 Q160 266 128 258 Z","#3a3a3a",2)
    # back leg (foot on rest)
    s+=shape(plimb([(150,250,36),(118,268,32),(128,344,27)]),"url(#herr)",2.2)
    s+=shape("M112 340 C108 354 118 358 146 356 C150 350 148 342 142 340 Z","#1c1c1c",1.6)
    # front leg
    s+=shape(plimb([(168,242,40),(102,250,35),(98,330,31),(96,392,31)]),"url(#herr)",2.2)
    s+=shape("M80 390 C74 404 84 410 116 408 C122 400 118 392 112 390 Z","#1c1c1c",1.6)
    # torso turtleneck + overshirt
    s+=shape(poly([(130,104),(192,104),(194,246),(128,246)]),"#1f1f1f",2.2)
    s+=shape(poly([(126,106),(146,102),(150,246),(124,248)]),"#a3a19b",2)
    s+=shape(poly([(196,106),(176,102),(172,246),(198,248)]),"#a3a19b",2)
    s+=wash(poly([(126,106),(146,102),(150,246),(124,248)]),"oA",[([(132,120),(130,230)],4,.4)])
    s+=shape(poly([(150,84),(170,84),(172,104),(148,104)]),"#1f1f1f",1.8)
    # head looking down at guitar
    s+='<g transform="translate(0 9) ">'
    s+=face_glasses(158,66,13.5,16.5,glasses=False)
    s+=messy_hair(158,58)
    s+='</g>'
    # guitar on lap
    s+=gtr(126,234,-66,.55)
    # fretting arm
    s+=shape(plimb([(130,112,22),(114,192,20),(56,180,16)]),"#a3a19b",2.2)
    s+=hand(50,180,80,1.05)
    # strumming arm
    s+=shape(plimb([(192,112,22),(204,194,20),(142,226,16)]),"#a3a19b",2.2)
    s+=wash(plimb([(192,112,22),(204,194,20),(142,226,16)]),"aA",[([(198,130),(204,186)],5,.35)])
    s+=hand(136,228,30,1.05)
    return s

# ---- B: keyboardist behind keyboard
def keyboardist():
    s=""
    # torso: cardigan over white shirt
    s+=shape(poly([(122,96),(218,96),(228,196),(112,196)]),"url(#rib)",2.2)
    s+=shape(poly([(156,94),(184,94),(178,196),(162,196)]),"#f7f5ef",1.6)
    s+=stroke("M156 94 L168 124 L184 94",1.6)
    for y in (130,150,170): s+=f'<circle cx="179" cy="{y}" r="2" fill="{INK}"/>'
    s+=shape(poly([(162,78),(178,78),(180,96),(160,96)]),SKIN,1.4)
    # head with bob hair
    s+='<g transform="translate(0 11) ">'
    s+=shape(path([(146,60),(146,34),(170,22),(194,34),(194,60),(196,74),(182,72),(170,44),(156,66),(144,74)],True),"#1e1e1e",2)
    s+=face_glasses(170,56,13.5,16.5,glasses=False)
    s+=shape(path([(156,52),(160,34),(176,30),(188,40),(184,48),(170,42),(160,50)],True),"#1e1e1e",1.4)
    s+=f'<circle cx="157" cy="66" r="2" fill="{INK}"/><circle cx="183" cy="66" r="2" fill="{INK}"/>'
    s+='</g>'
    # arms to keys
    s+=shape(plimb([(126,104,26),(110,160,26),(134,198,18)]),"url(#rib)",2.2)
    s+=shape(plimb([(214,104,26),(232,160,26),(208,198,18)]),"url(#rib)",2.2)
    # keyboard
    s+=shape(poly([(20,186),(320,186),(320,228),(20,228)]),"#f7f5ef",2.2)
    s+=shape(poly([(20,186),(320,186),(320,200),(20,200)]),"#3a3a3a",1.8)
    for i in range(6): s+=f'<circle cx="{34+i*12}" cy="193" r="3.2" fill="#f7f5ef" stroke="{INK}" stroke-width=".8"/>'
    n=26; w=300/n
    for i in range(1,n): s+=f'<line x1="{20+i*w:.1f}" y1="200" x2="{20+i*w:.1f}" y2="228" stroke="{INK}" stroke-width=".8"/>'
    for i in range(n-1):
        if i%7 in (0,1,3,4,5): s+=f'<rect x="{20+(i+1)*w-3.5:.1f}" y="200" width="7" height="16" fill="{INK}"/>'
    s+=hand(134,206,0,1.1)+hand(208,206,0,1.1)
    s+=stroke("M100 230 L240 300 M240 230 L100 300 M84 300 H120 M222 300 H258",3.2)
    return s

# ---- C: bassist standing with beanie
def bassist():
    s=""
    s+=shape(poly([(66,226),(134,226),(140,300),(146,416),(110,418),(100,310),(92,418),(56,416),(60,300)]),"#262626",2.2)
    s+=wash(poly([(66,226),(134,226),(140,300),(146,416),(110,418),(100,310),(92,418),(56,416),(60,300)]),"pC",[([(64,250),(62,400)],6,.25),([(130,250),(138,400)],5,.2)])
    s+=shape("M52 414 C46 430 56 436 92 434 C98 426 96 416 92 414 Z","#f7f5ef",1.8)+stroke("M58 428 H90",1)
    s+=shape("M108 416 C104 430 114 436 150 434 C156 426 152 416 146 414 Z","#f7f5ef",1.8)+stroke("M114 428 H148",1)
    s+=shape(poly([(80,86),(120,86),(124,230),(76,230)]),"#f7f5ef",1.8)
    jl=[(82,84),(56,92),(50,104),(50,232),(84,236),(86,140),(92,96)]
    jr=[(118,84),(144,92),(150,104),(152,232),(116,236),(114,140),(108,96)]
    for nm,j in (("cl",jl),("cr",jr)):
        s+=shape(poly(j),"#1d1d1d",2.2); s+=wash(poly(j),"j"+nm,[([(60,110),(58,220)] if nm=="cl" else [(140,110),(146,220)],6,.3)])
    s+=shape(poly([(92,64),(108,64),(110,86),(90,86)]),SKIN,1.4)
    # headphones around neck
    s+=stroke("M80 86 Q100 100 120 86",4)+shape("M74 78 h10 v16 h-10z","#333",1.4)+shape("M116 78 h10 v16 h-10z","#333",1.4)
    s+='<g transform="translate(0 11) ">'
    s+=face_glasses(100,46,13.5,16.5,glasses=True)
    s+=shape("M86 40 C84 14 116 14 114 40 Z","#3a3a3a",2)+shape("M84 36 H116 V44 H84 Z","#555",1.6)
    s+=f'<circle cx="100" cy="16" r="5" fill="#3a3a3a" stroke="{INK}" stroke-width="1.4"/>'
    s+='</g>'
    s+=stroke("M82 92 L132 250",4,"#111")
    s+=gtr(112,262,-38,.58,bass=True)
    s+=shape(plimb([(58,96,22),(56,176,20),(38,156,15)]),"#1d1d1d",2.2)
    s+=hand(36,152,-60,1.05)
    s+=shape(plimb([(144,96,22),(158,190,20),(122,252,15)]),"#1d1d1d",2.2)
    s+=hand(118,256,20,1.05)
    return s

# ---- E: drummer walking, bucket hat, trench, sticks + snare
def drummer():
    s=""
    s+=shape(poly([(96,196),(160,196),(168,240),(196,312),(162,318),(132,250),(118,318),(82,314),(96,250)]),"#1f1f1f",2.2)
    s+=wash(poly([(96,196),(160,196),(168,240),(196,312),(162,318),(132,250),(118,318),(82,314),(96,250)]),"pE",[([(92,230),(88,300)],6,.3),([(170,250),(186,306)],5,.25)])
    s+=shape("M78 312 C72 326 84 330 120 328 C124 320 120 312 116 312 Z","#151515",1.6)
    s+=shape("M160 316 C156 330 168 334 204 330 C206 320 200 310 194 310 Z","#151515",1.6)
    s+=shape(poly([(112,86),(152,86),(156,206),(108,206)]),"url(#stripe)",1.8)
    cl=[(112,80),(86,90),(78,104),(64,250),(108,258),(112,140),(120,96)]
    cr=[(150,80),(176,90),(184,104),(208,246),(156,256),(150,140),(144,96)]
    for nm,c in (("el",cl),("er",cr)):
        s+=shape(poly(c),"#a9a59c",2.2); s+=wash(poly(c),"c"+nm,[([(82,110),(74,240)] if nm=="el" else [(182,110),(198,236)],8,.4)])
    s+=stroke("M100 180 L110 186 M168 180 L158 186 M86 200 L106 200",1.2)
    s+=shape(poly([(124,62),(140,62),(142,86),(122,86)]),SKIN,1.4)
    s+='<g transform="translate(0 11) ">'
    s+=face_glasses(132,46,13.5,16.5,glasses=False)
    s+=shape("M112 38 C110 16 154 16 152 38 Z","#2a2a2a",2)+shape("M102 40 Q132 30 162 40 L160 46 Q132 38 104 46 Z","#2a2a2a",1.8)
    s+='</g>'
    # snare under left arm
    s+=shape("M40 168 L40 196 Q74 210 108 196 L108 168 Z","#d9d6cf",2)
    s+=shape("M40 168 Q74 154 108 168 Q74 182 40 168 Z","#f7f5ef",2)
    for x in (52,74,96): s+=stroke(f"M{x} 176 V202",2.4)
    s+=shape(plimb([(90,96,22),(72,150,20),(96,184,16)]),"#a9a59c",2.2)
    s+=hand(98,184,0,1.05)
    # sticks in right hand
    s+=shape(plimb([(174,96,22),(196,160,20),(206,206,16)]),"#a9a59c",2.2)
    s+=stroke("M196 214 L250 160",3.6)+stroke("M202 218 L258 172",3.6)
    s+=hand(204,212,30,1.05)
    return s

if __name__=="__main__":
    for nm,fn,w,h in (("singer",singer,220,340),("guitarist",guitarist,260,420),("keyboardist",keyboardist,340,310),("bassist",bassist,200,440),("drummer",drummer,280,340)):
        out=f'<html><body style="margin:0;background:{BG}"><svg width="{w*2}" height="{h*2}" viewBox="0 0 {w} {h}">{DEFS}<g filter="url(#wob)">{fn()}</g></svg></body></html>'
        open(f"t_{nm}.html","w").write(out)
