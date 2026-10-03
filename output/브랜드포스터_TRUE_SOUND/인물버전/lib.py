import math
BG="#F4F2EC"; INK="#141414"
def f(v): return f"{v:.1f}"
def cr(pts, closed=False):
    """Catmull-Rom through pts -> cubic bezier path string (no M)."""
    P=pts[:]
    if closed: P=[P[-1]]+P+[P[0],P[1]]
    else: P=[P[0]]+P+[P[-1]]
    s=""
    for i in range(1,len(P)-2):
        p0,p1,p2,p3=P[i-1],P[i],P[i+1],P[i+2]
        c1=(p1[0]+(p2[0]-p0[0])/6,p1[1]+(p2[1]-p0[1])/6)
        c2=(p2[0]-(p3[0]-p1[0])/6,p2[1]-(p3[1]-p1[1])/6)
        s+=f" C{f(c1[0])} {f(c1[1])} {f(c2[0])} {f(c2[1])} {f(p2[0])} {f(p2[1])}"
    return s
def path(pts, closed=False):
    return f"M{f(pts[0][0])} {f(pts[0][1])}"+cr(pts,closed)+(" Z" if closed else "")
def limb(pts):
    """pts: list of (x,y,w). returns closed outline path."""
    L=[];R=[]
    n=len(pts)
    for i,(x,y,w) in enumerate(pts):
        a=pts[max(i-1,0)]; b=pts[min(i+1,n-1)]
        dx=b[0]-a[0]; dy=b[1]-a[1]; d=math.hypot(dx,dy) or 1
        nx,ny=-dy/d,dx/d
        L.append((x+nx*w/2,y+ny*w/2)); R.append((x-nx*w/2,y-ny*w/2))
    pts2=L+R[::-1]
    return f"M{f(pts2[0][0])} {f(pts2[0][1])}"+cr(L)+f" L{f(R[-1][0])} {f(R[-1][1])}"+cr(R[::-1])+" Z"
def shape(d, fill, sw=2.2, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{INK}" stroke-width="{sw}" stroke-linejoin="round" stroke-linecap="round" {extra}/>'
def stroke(d, sw=1.6, color=INK, extra=""):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'
def wash(d, clip_id, streaks):
    """marker highlight streaks clipped to shape"""
    s=f'<clipPath id="{clip_id}"><path d="{d}"/></clipPath><g clip-path="url(#{clip_id})">'
    for pts,w,op in streaks:
        s+=f'<path d="{path(pts)}" fill="none" stroke="#fff" stroke-width="{w}" stroke-linecap="round" opacity="{op}"/>'
    s+='</g>'
    return s
def hand(x,y,rot=0,s=1.0):
    return (f'<g transform="translate({f(x)} {f(y)}) rotate({rot}) scale({s})">'
            f'<path d="M-6 -7 C-1 -10 7 -8 8 -2 C9 4 5 9 -1 9 C-7 9 -10 3 -9 -2 Z" fill="#fbf8f2" stroke="{INK}" stroke-width="1.6"/>'
            f'<path d="M2 -6 q4 2 3 7 M-2 -5 q4 3 3 8" fill="none" stroke="{INK}" stroke-width="1"/></g>')
DEFS=f'''<defs>
<filter id="wob"><feTurbulence type="fractalNoise" baseFrequency="0.035" numOctaves="2" seed="9"/><feDisplacementMap in="SourceGraphic" scale="2.2"/></filter>
<pattern id="herr" width="8" height="8" patternUnits="userSpaceOnUse"><rect width="8" height="8" fill="#dcdad4"/><path d="M0 2 L4 0 L8 2 M0 6 L4 4 L8 6" fill="none" stroke="#8a8780" stroke-width=".8"/></pattern>
<pattern id="rib" width="4" height="10" patternUnits="userSpaceOnUse"><rect width="4" height="10" fill="#9b9993"/><line x1="1" y1="0" x2="1" y2="10" stroke="#76746e" stroke-width="1"/></pattern>
<pattern id="stripe" width="10" height="9" patternUnits="userSpaceOnUse"><rect width="10" height="9" fill="#f7f5ef"/><rect y="0" width="10" height="4" fill="#3a3a3a"/></pattern>
<pattern id="hh" width="3.4" height="3.4" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><line x1="0" y1="0" x2="0" y2="3.4" stroke="{INK}" stroke-width=".6"/></pattern>
</defs>'''
def poly(pts, closed=True, r=0):
    s=f"M{f(pts[0][0])} {f(pts[0][1])}"+"".join(f" L{f(x)} {f(y)}" for x,y in pts[1:])
    return s+(" Z" if closed else "")
def plimb(pts):
    L=[];R=[]; n=len(pts)
    for i,(x,y,w) in enumerate(pts):
        a=pts[max(i-1,0)]; b=pts[min(i+1,n-1)]
        dx=b[0]-a[0]; dy=b[1]-a[1]; d=math.hypot(dx,dy) or 1
        nx,ny=-dy/d,dx/d
        L.append((x+nx*w/2,y+ny*w/2)); R.append((x-nx*w/2,y-ny*w/2))
    return poly(L+R[::-1])
