# 插图小工具：与 assets/fig/ 里现有 SVG 同一风格（白底圆角卡片、同一字体与配色）
import math, html
FONT='-apple-system,PingFang SC,Noto Sans SC,sans-serif'
COL={'a':'#222','b':'#2563eb','r':'#dc2626','g':'#16a34a','o':'#ea580c','p':'#7c3aed','k':'#6b7280'}
def esc(t): return html.escape(str(t),quote=False)
class Fig:
    def __init__(s,w,h): s.w,s.h,s.p=w,h,[]
    def add(s,x): s.p.append(x)
    def text(s,x,y,t,size=13,anchor='middle',fill='#222',bold=False,rot=None):
        tr=f' transform="rotate({rot} {x} {y})"' if rot else ''
        s.add(f'<text x="{x}" y="{y}" text-anchor="{anchor}" fill="{fill}" font-size="{size}" font-weight="{"bold" if bold else "normal"}"{tr}>{esc(t)}</text>')
    def lines(s,x,y,arr,size=12,dy=16,anchor='middle',fill='#222',bold=False):
        for i,t in enumerate(arr): s.text(x,y+i*dy,t,size,anchor,fill,bold)
    def line(s,x1,y1,x2,y2,c='#222',w=1.6,dash=None,arrow=None,both=False):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        m=f' marker-end="url(#{arrow})"' if arrow else ''
        ms=f' marker-start="url(#s{arrow})"' if (arrow and both) else ''
        s.add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}"{d}{m}{ms}/>')
    def rect(s,x,y,w,h,fill='#fff',stroke='#222',sw=1.5,rx=8,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        s.add(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def circle(s,x,y,r,fill='#fff',stroke='#222',sw=1.5):
        s.add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>')
    def ellipse(s,x,y,rx,ry,fill='#fff',stroke='#222',sw=1.5,dash=None):
        d=f' stroke-dasharray="{dash}"' if dash else ''
        s.add(f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')
    def poly(s,pts,fill='none',stroke='#222',sw=1.5,close=True):
        P=' '.join(f'{a:.1f},{b:.1f}' for a,b in pts)
        tag='polygon' if close else 'polyline'
        s.add(f'<{tag} points="{P}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"/>')
    def path(s,d,fill='none',stroke='#222',sw=1.8,dash=None,arrow=None):
        da=f' stroke-dasharray="{dash}"' if dash else ''
        m=f' marker-end="url(#{arrow})"' if arrow else ''
        s.add(f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{da}{m} stroke-linejoin="round" stroke-linecap="round"/>')
    def box(s,x,y,w,h,t,fill='#eff6ff',stroke='#93c5fd',size=13,bold=False,sub=None,subsize=11):
        s.rect(x,y,w,h,fill,stroke,1.5,8)
        if sub: 
            s.text(x+w/2,y+h/2-3,t,size,'middle','#222',bold); s.text(x+w/2,y+h/2+13,sub,subsize,'middle','#555')
        else: s.text(x+w/2,y+h/2+size*0.36,t,size,'middle','#222',bold)
    def axes(s,x0,y0,x1,y1,xl='',yl='',size=12):
        s.line(x0,y0,x1,y0,arrow='a'); s.line(x0,y0,x0,y1,arrow='a')
        if xl: s.text(x1,y0+16,xl,size,'end')
        if yl: s.text(x0+6,y1+4,yl,size,'start')
    def curve(s,pts,stroke='#2563eb',sw=2.4,dash=None):
        s.path('M'+' L'.join(f'{a:.1f},{b:.1f}' for a,b in pts),stroke=stroke,sw=sw,dash=dash)
    def svg(s):
        mk=''
        for k,c in COL.items():
            mk+=f'<marker id="{k}" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0L10 5L0 10z" fill="{c}"/></marker>'
            mk+=f'<marker id="s{k}" viewBox="0 0 10 10" refX="1" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M10 0L0 5L10 10z" fill="{c}"/></marker>'
        return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {s.w} {s.h}" font-family="{FONT}" font-size="13"><defs>{mk}</defs>'
                f'<rect width="{s.w}" height="{s.h}" rx="10" fill="#fff" stroke="#ddd"/>'+''.join(s.p)+'</svg>')
    def save(s,path):
        open(path,'w',encoding='utf-8').write(s.svg())
def gauss(x,mu,sg,h): return h*math.exp(-((x-mu)**2)/(2*sg*sg))
