import sys,os,math
sys.path.insert(0,os.path.dirname(__file__))
from figlib import *
OUT=os.path.join(os.path.dirname(__file__),'..','assets','fig')

# ---------- 图 5-1a 原子模型的演变
f=Fig(360,230)
tit=[(62,'汤姆生模型 1904'),(180,'卢瑟福模型 1911'),(298,'玻尔模型 1913')]
for cx,t in tit: f.text(cx,22,t,12,'middle','#222',True)
f.circle(62,100,42,'#fee2e2','#dc2626',2)
for dx,dy in [(-18,-14),(14,-20),(22,10),(-6,6),(-24,18),(6,26),(-10,-30)]: f.circle(62+dx,100+dy,4,'#2563eb','#2563eb',1)
f.text(62,160,'正电荷均匀分布',11,'middle','#dc2626'); f.text(62,176,'电子嵌在其中',11,'middle','#2563eb'); f.text(62,194,'“枣糕模型”',10,'middle','#555')
f.ellipse(180,100,44,44,'none','#9ca3af',1.2,'3 3'); f.circle(180,100,4,'#dc2626','#dc2626',1)
for a in (30,150,270): f.circle(180+44*math.cos(math.radians(a)),100-44*math.sin(math.radians(a)),4,'#2563eb','#2563eb',1)
f.text(180,160,'极小的带正电的核',11,'middle','#dc2626'); f.text(180,176,'电子绕核运动',11,'middle','#2563eb'); f.text(180,192,'原子内部大部分是空的',10,'middle','#555')
for r in (16,30,44): f.ellipse(298,100,r,r,'none','#9ca3af',1.2)
f.circle(298,100,4,'#dc2626','#dc2626',1)
f.circle(298+16,100,3.5,'#2563eb','#2563eb',1); f.circle(298-21,100-21,3.5,'#2563eb','#2563eb',1); f.circle(298+31,100+31,3.5,'#2563eb','#2563eb',1)
f.path('M322,66 Q334,56 326,48',stroke='#ea580c',sw=1.6,arrow='o')
f.text(298,160,'电子在特定能级上运动',10,'middle','#2563eb'); f.text(298,176,'跃迁时吸收或放出光子',10,'middle','#ea580c'); f.text(298,194,'能解释氢原子光谱',10,'middle','#555')
f.text(180,220,'每个模型都是为了解释当时的实验事实而提出的',11,'middle','#555')
f.save(OUT+'/c5_1a.svg')

# ---------- 图 5-1b α 粒子散射实验
f=Fig(360,290)
f.rect(12,112,52,36,'#f3f4f6','#6b7280',1.5,4); f.text(38,134,'α 源',12)
f.line(64,130,176,130,'#16a34a',2,arrow='g')
f.rect(176,52,10,156,'#fde68a','#d97706',1.5,1); f.text(181,40,'金箔',12,'middle','#a16207',True)
for y in range(64,204,14): f.circle(181,y,2.2,'#dc2626','#dc2626',1)
f.path('M186,130 L330,130',stroke='#16a34a',sw=2,arrow='g'); f.text(344,116,'绝大多数',11,'end','#16a34a',True); f.text(344,150,'几乎不偏转',11,'end','#16a34a')
f.path('M184,118 L270,86',stroke='#2563eb',sw=2,arrow='b'); f.text(344,76,'少数：较大角度偏转',11,'end','#2563eb',True)
f.path('M180,164 L256,214',stroke='#2563eb',sw=2,arrow='b')
f.path('M130,168 L178,172 L112,214',stroke='#dc2626',sw=2,arrow='r'); f.text(104,232,'极少数被反弹回来',11,'middle','#dc2626',True)
f.lines(14,262,['结论：原子中心有一个体积很小、带正电、','质量很大的核（原子核）'],11,16,'start','#555')
f.save(OUT+'/c5_1b.svg')

# ---------- 图 5-2a 原子符号与三种粒子
f=Fig(360,280)
f.text(48,64,'23',20,'middle','#dc2626',True); f.text(48,92,'11',20,'middle','#2563eb',True); f.text(100,86,'Na',34,'middle','#222',True); f.text(140,60,'+',18,'middle','#16a34a',True)
f.text(48,38,'质量数 A',11,'middle','#dc2626'); f.text(48,116,'原子序数 Z',11,'middle','#2563eb'); f.text(140,38,'电荷',11,'middle','#16a34a')
f.lines(190,50,['质子数 Z = 11','中子数 N = A − Z = 12','电子数 = Z − 电荷 = 10'],12,19,'start','#222')
for t,x in [('粒子',54),('电荷',150),('相对质量',250)]: f.text(x,140,t,12,'middle','#222',True)
f.line(14,146,346,146,'#999',1)
for i,(a,b,c,col) in enumerate([('质子 p⁺','+1','1','#dc2626'),('中子 n','0','1','#555'),('电子 e⁻','−1','1/1836 ≈ 0.0005','#2563eb')]):
    y=168+i*28; f.text(54,y,a,13,'middle',col,True); f.text(150,y,b,13,'middle',col); f.text(250,y,c,12,'middle','#222')
f.text(180,248,'原子质量几乎全集中在原子核；质量数 A = 质子数 + 中子数',11,'middle','#555')
f.text(180,266,'核电荷数 = 质子数 = 原子序数 Z（中性原子的电子数也等于 Z）',11,'middle','#555')
f.save(OUT+'/c5_2a.svg')

# ---------- 图 5-2b 氯的质谱（同位素丰度）
f=Fig(360,260)
f.axes(50,205,340,28,'','相对丰度 / %'); f.text(340,226,'质量数（m/z）',12,'end')
f.rect(120,205-75.8*1.6,34,75.8*1.6,'#bfdbfe','#2563eb',1.8,2); f.rect(214,205-24.2*1.6,34,24.2*1.6,'#bbf7d0','#16a34a',1.8,2)
f.text(137,205-75.8*1.6-6,'75.8',12,'middle','#2563eb',True); f.text(231,205-24.2*1.6-6,'24.2',12,'middle','#16a34a',True)
f.text(137,222,'35',12,'middle'); f.text(231,222,'37',12,'middle')
f.text(137,238,'³⁵Cl',12,'middle','#2563eb',True); f.text(231,238,'³⁷Cl',12,'middle','#16a34a',True)
f.lines(300,60,['Ar = 35 × 0.758','+ 37 × 0.242','≈ 35.5'],12,18,'end','#222')
f.save(OUT+'/c5_2b.svg')

# ---------- 图 5-3a 连续光谱、发射光谱、吸收光谱
f=Fig(360,272)
f.add('<defs><linearGradient id="sp2" x1="0" x2="1"><stop offset="0" stop-color="#7c3aed"/><stop offset="0.2" stop-color="#2563eb"/><stop offset="0.38" stop-color="#06b6d4"/><stop offset="0.5" stop-color="#16a34a"/><stop offset="0.62" stop-color="#eab308"/><stop offset="0.78" stop-color="#f97316"/><stop offset="1" stop-color="#dc2626"/></linearGradient></defs>')
X=lambda l:30+(l-400)*1.0
f.text(14,24,'连续光谱（白光、炽热固体）',12,'start','#222',True)
f.add('<rect x="30" y="32" width="300" height="34" fill="url(#sp2)"/>')
f.text(14,90,'氢原子的发射光谱（线状光谱）',12,'start','#222',True)
f.rect(30,98,300,34,'#111827','#111827',0,0)
for l,c in [(410,'#7c3aed'),(434,'#4f46e5'),(486,'#06b6d4'),(656,'#ef4444')]:
    f.rect(X(l)-1.5,98,3,34,c,c,0,0); f.text(X(l),146,str(l),10,'middle',c)
f.text(14,172,'吸收光谱（连续光谱中缺少某些波长）',12,'start','#222',True)
f.add('<rect x="30" y="180" width="300" height="34" fill="url(#sp2)"/>')
for l in (410,434,486,656): f.rect(X(l)-1.5,180,3,34,'#111827','#111827',0,0)
for l in (400,450,500,550,600,650,700): f.text(X(l),230,str(l),10)
f.text(330,246,'波长 / nm',11,'end')
f.text(180,264,'每种元素的线状光谱位置不同，像“指纹”，可以用来鉴定元素',10,'middle','#555')
f.save(OUT+'/c5_3a.svg')

# ---------- 图 5-3b 氢原子能级图
f=Fig(360,340)
E={1:-13.6,2:-3.40,3:-1.51,4:-0.85,5:-0.54,6:-0.38}
Y=lambda n:46+236/n
f.line(14,46,346,46,'#999',1,'4 3'); f.text(346,40,'n = ∞，E = 0（电离）',10,'end','#555')
for n,e in E.items():
    f.line(28,Y(n),304,Y(n),'#222',1.8); dy={4:5,5:3,6:1}.get(n,4); f.text(24,Y(n)+dy,f'n={n}',9 if n>=4 else 11,'end','#222',True); f.text(310,Y(n)+dy,f'{e:.2f} eV',9 if n>=4 else 10,'start','#555')
for x,n in ((56,2),(78,3),(100,4)): f.line(x,Y(n),x,Y(1)-2,'#7c3aed',1.8,arrow='p')
f.text(78,Y(1)+18,'莱曼系：→ n = 1（紫外）',11,'middle','#7c3aed',True)
for x,n,c,m in ((150,3,'#ef4444','r'),(172,4,'#06b6d4','b'),(194,5,'#4f46e5','b'),(216,6,'#7c3aed','p')):
    f.line(x,Y(n),x,Y(2)-2,c,2,arrow=m)
f.text(186,Y(2)+16,'巴耳末系：→ n = 2（可见光）',11,'middle','#ef4444',True)
f.text(186,Y(2)+31,'656（红）、486、434、410 nm',10,'middle','#555')
for x,n in ((262,4),(284,5)): f.line(x,Y(n),x,Y(3)-2,'#16a34a',1.8,arrow='g')
f.text(274,Y(3)+16,'帕邢系：→ n = 3',10,'middle','#16a34a',True); f.text(274,Y(3)+29,'（红外）',10,'middle','#16a34a')
f.text(180,318,'向下箭头：电子从高能级跃迁到低能级，放出 1 个光子，能量差 = hν',10,'middle','#555')
f.text(180,332,'纵向间距为示意，不按能量比例',10,'middle','#555')
f.save(OUT+'/c5_3b.svg')

# ---------- 图 5-4a 轨域的形状
f=Fig(360,250)
f.text(70,22,'s 轨域',13,'middle','#222',True); f.text(250,22,'p 轨域（三个方向）',13,'middle','#222',True)
f.circle(70,100,40,'#dbeafe','#2563eb',2); f.circle(70,100,3,'#2563eb','#2563eb',1)
f.text(70,160,'球形，没有方向性',11,'middle','#222'); f.text(70,176,'1s、2s、3s … 越来越大',10,'middle','#555'); f.text(70,192,'每个能层只有 1 个 s 轨域',10,'middle','#555')
cx,cy=250,98
f.line(cx-72,cy,cx+72,cy,'#9ca3af',1,'3 2'); f.line(cx,cy-62,cx,cy+62,'#9ca3af',1,'3 2'); f.line(cx-50,cy+50,cx+50,cy-50,'#9ca3af',1,'3 2')
for dx in (-26,26): f.ellipse(cx+dx,cy,26,11,'#fecaca','#dc2626',1.8)
for dy in (-26,26): f.ellipse(cx,cy+dy,11,26,'#bbf7d0','#16a34a',1.8)
for s in (-1,1): 
    f.add(f'<ellipse cx="{cx+s*18}" cy="{cy-s*18}" rx="22" ry="9" fill="#bfdbfe" stroke="#2563eb" stroke-width="1.8" transform="rotate(-45 {cx+s*18} {cy-s*18})"/>')
f.text(cx+76,cy+4,'x',11,'start','#dc2626',True); f.text(cx+4,cy-62,'y',11,'start','#16a34a',True); f.text(cx+52,cy-52,'z',11,'start','#2563eb',True)
f.text(cx,180,'哑铃形：pₓ、p_y、p_z',11,'middle','#222'); f.text(cx,196,'3 个轨域，能量相同（简并）',10,'middle','#555'); f.text(cx,212,'2p、3p … 每个能层（n ≥ 2）有 3 个',10,'middle','#555')
f.text(180,240,'轨域：电子出现概率最大的空间区域（电子云的“边界”）',11,'middle','#555')
f.save(OUT+'/c5_4a.svg')

# ---------- 图 5-4b 构造原理（填充顺序）图
f=Fig(360,336)
rows={1:['1s'],2:['2s','2p'],3:['3s','3p','3d'],4:['4s','4p','4d','4f'],5:['5s','5p','5d','5f'],6:['6s','6p','6d'],7:['7s','7p']}
colx={'s':80,'p':150,'d':220,'f':290}
f.text(180,18,'沿红色箭头，从 ① 到 ⑦ 依次填入',12,'middle','#222',True)
pos={}
for n,items in rows.items():
    y=46+(n-1)*40
    for it in items: pos[it]=(colx[it[1]],y)
dx,dy=-70,40
for k in range(1,8):  # 对角线：n + l = k
    items=[(n,l) for l,c in enumerate('spdf') for n in [k-l] if 1<=n<=7 and n>l and f'{n}{c}' in pos]
    if not items: continue
    items.sort(); a=pos[f'{items[0][0]}{"spdf"[items[0][1]]}']; b=pos[f'{items[-1][0]}{"spdf"[items[-1][1]]}']
    sx,sy=a[0]-dx/2,a[1]-dy/2; ex,ey=b[0]+dx/2,b[1]+dy/2
    f.line(sx,sy,ex,ey,'#dc2626',1.8,arrow='r')
    f.circle(sx,sy,8,'#fff','#dc2626',1.4); f.text(sx,sy+4,str(k),10,'middle','#dc2626',True)
for n in rows: f.text(24,46+(n-1)*40+5,f'n={n}',11,'end','#555',True)
for it,(x,y) in pos.items():
    f.rect(x-20,y-14,40,28,'#eff6ff','#93c5fd',1.5,6); f.text(x,y+5,it,13,'middle','#222',True)
f.text(180,326,'顺序：1s 2s 2p 3s 3p 4s 3d 4p 5s 4d 5p 6s …（4s 在 3d 之前）',10,'middle','#555')
f.save(OUT+'/c5_4b.svg')

# ---------- 图 5-4c 能级高低与轨域数
f=Fig(360,330)
f.line(40,306,40,26,'#222',1.6,arrow='a'); f.text(46,32,'能量',12,'start')
levels=[('1s',1,282),('2s',1,240),('2p',3,214),('3s',1,172),('3p',3,146),('4s',1,134),('3d',5,108),('4p',3,76)]
levels=[('1s',1,284),('2s',1,244),('2p',3,218),('3s',1,176),('3p',3,150),('4s',1,114),('3d',5,88),('4p',3,60)]
for name,k,y in levels:
    f.text(62,y+16,name,12,'end','#222',True)
    for i in range(k): f.rect(70+i*30,y,24,22,'#fff','#2563eb',1.6,2)
f.text(236,100,'4s 比 3d 低：',11,'start','#dc2626',True); f.text(236,116,'K、Ca 先填 4s',10,'start','#dc2626')
for i,t in enumerate(['s：1 个轨域，2 个电子','p：3 个轨域，6 个电子','d：5 个轨域，10 个电子','f：7 个轨域，14 个电子']): f.text(236,176+i*16,t,10,'start','#222')
f.text(236,284,'每个方框 = 1 个轨域',10,'start','#555'); f.text(236,300,'每个轨域最多 2 个电子',10,'start','#555')
f.save(OUT+'/c5_4c.svg')

# ---------- 图 5-4d 轨域表示式：对与错
f=Fig(360,330)
def box(x,y,spin,w=28):
    f.rect(x,y,w,26,'#fff','#222',1.5,2)
    if spin=='ud': f.text(x+w/2,y+19,'↑↓',14,'middle','#2563eb',True)
    elif spin=='u': f.text(x+w/2,y+19,'↑',14,'middle','#2563eb',True)
    elif spin=='uu': f.text(x+w/2,y+19,'↑↑',14,'middle','#dc2626',True)
def row(y,name,s1,s2,p,tag,col='#16a34a',note=''):
    f.text(10,y+19,name,13,'start','#222',True)
    box(38,y,s1); box(72,y,s2)
    for i,s in enumerate(p): box(112+i*30,y,s,26)
    f.text(206,y+16,tag,11,'start',col,True)
    if note: f.text(206,y+32,note,10,'start','#555')
f.text(52,18,'1s',11,'middle','#555'); f.text(86,18,'2s',11,'middle','#555'); f.text(151,18,'2p',11,'middle','#555')
f.text(10,38,'正确',12,'start','#16a34a',True)
row(46,'C','ud','ud',['u','u',''],'✓ 2 个未成对电子')
row(86,'N','ud','ud',['u','u','u'],'✓ 3 个未成对电子')
row(126,'O','ud','ud',['ud','u','u'],'✓ 2 个未成对电子')
f.text(10,186,'错误',12,'start','#dc2626',True)
row(194,'N','ud','ud',['ud','u',''],'✗ 违反汉德规则','#dc2626','应分占三个 2p 轨域，自旋平行')
row(234,'Be','ud','uu',[],'✗ 违反鲍利不相容','#dc2626','同一轨域两个电子自旋要相反')
row(274,'C','ud','ud',['u','','u'],'✓ 也正确','#16a34a','2p 三个轨域能量相同')
f.text(180,322,'箭头 ↑ ↓ 表示电子的两种自旋方向',10,'middle','#555')
f.save(OUT+'/c5_4d.svg')

print('c5 done')
