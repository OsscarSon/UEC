import sys,os,math
sys.path.insert(0,os.path.dirname(__file__))
from figlib import *
OUT=os.path.join(os.path.dirname(__file__),'..','assets','fig')
def bez(x0,y0,x1,y1,x2,y2,x3,y3,n=40):
    return [((1-t)**3*x0+3*(1-t)**2*t*x1+3*(1-t)*t*t*x2+t**3*x3, (1-t)**3*y0+3*(1-t)**2*t*y1+3*(1-t)*t*t*y2+t**3*y3) for t in [i/n for i in range(n+1)]]
def cross(pts,y):
    for (a,b),(c,d) in zip(pts,pts[1:]):
        if (b-y)*(d-y)<=0 and b!=d: return a+(c-a)*(y-b)/(d-b)

# ---------- 图 3-5a 呼吸作用总览
f=Fig(360,430)
f.box(100,10,160,36,'葡萄糖 C₆H₁₂O₆','#fef3c7','#d97706',13,True)
f.line(180,46,180,66,arrow='a')
f.box(40,66,280,50,'① 糖酵解 glycolysis','#eff6ff','#93c5fd',13,True,'细胞质基质 · 不需要 O₂ · 净得 2 ATP + 2 NADH')
f.line(180,116,180,136,arrow='a')
f.box(110,136,140,32,'2 丙酮酸（3C）','#fef3c7','#d97706',13,True)
f.line(150,168,92,200,arrow='a'); f.line(210,168,268,200,arrow='a')
f.text(88,194,'有 O₂',12,'end','#16a34a',True); f.text(272,194,'缺 O₂',12,'start','#dc2626',True)
f.box(8,204,164,60,'② 连接反应 + 克氏循环','#f0fdf4','#86efac',12,True,'线粒体基质 · 放出 CO₂ · 共 2 ATP',10)
f.line(90,264,90,284,arrow='a')
f.box(8,284,164,60,'③ 电子传递链','#f0fdf4','#86efac',12,True,'内膜 · 约 26–28 ATP · O₂ → H₂O',10)
f.line(90,344,90,362,arrow='g')
f.box(8,362,164,34,'有氧呼吸共约 30–32 ATP','#dcfce7','#16a34a',12,True)
f.text(90,414,'（旧教材常写 36–38，以课本为准）',10,'middle','#555')
f.box(188,204,164,54,'动物、乳酸菌','#fef2f2','#fca5a5',12,True,'→ 乳酸 + 2 ATP',11)
f.box(188,268,164,54,'酵母、植物（根淹水）','#fef2f2','#fca5a5',12,True,'→ 乙醇 + CO₂ + 2 ATP',11)
f.lines(270,342,['无氧呼吸：只有糖酵解','的 2 ATP；在细胞质基质','进行，不用氧'],10,14,'middle','#dc2626')
f.lines(270,392,['作用：把 NADH 变回 NAD⁺，','让糖酵解继续进行'],10,14,'middle','#555')
f.save(OUT+'/b3_5a.svg')

# ---------- 图 3-5b 线粒体
f=Fig(360,270)
f.ellipse(180,128,140,74,'#e0f2fe','#0284c7',2.4)
f.ellipse(180,128,124,58,'#fef9c3','#ea580c',2.4)
for x in (112,148,184,220,256):   # 嵴：从内膜向内的折叠
    f.rect(x-6,70,12,44,'#fff7ed','#ea580c',1.8,6)
for x in (130,166,202,238):
    f.rect(x-6,142,12,44,'#fff7ed','#ea580c',1.8,6)
f.ellipse(180,128,124,58,'none','#ea580c',2.4)
f.line(70,50,98,74,'#555',1); f.text(66,46,'外膜',12,'end','#0284c7',True)
f.line(52,128,66,128,'#555',1); f.text(48,132,'内膜',12,'end','#ea580c',True)
f.line(148,60,148,40,'#555',1); f.text(148,32,'嵴 cristae',12,'middle','#ea580c',True)
f.text(148,18,'电子传递链、ATP 合成酶',11,'middle','#ea580c')
f.text(180,127,'基质',13,'middle','#a16207',True); f.text(180,139,'克氏循环；含 DNA、核糖体',10,'middle','#a16207')
f.line(296,64,318,44,'#555',1); f.text(352,28,'膜间隙',12,'end','#0284c7',True); f.text(352,42,'H⁺ 在此积累',10,'end','#0284c7')
f.lines(180,236,['电子传递链把 H⁺ 泵入膜间隙；H⁺ 经 ATP 合成酶流回基质时合成 ATP'],11,15,'middle','#555')
f.lines(180,254,['（线粒体基质：连接反应与克氏循环；内膜折叠成嵴，面积大，酶多）'],10,14,'middle','#555')
f.save(OUT+'/b3_5b.svg')

# ---------- 图 3-6a 叶绿体
f=Fig(360,300)
f.ellipse(180,138,150,84,'#f0fdf4','#16a34a',2.4); f.ellipse(180,138,140,74,'none','#16a34a',1.6)
def grana(cx,cy,n=5):
    for i in range(n):
        f.rect(cx-22,cy-n*6+i*12,44,9,'#86efac','#16a34a',1.4,4)
for (cx,cy) in [(90,130),(180,112),(268,134),(135,170),(222,176)]: grana(cx,cy,5 if cy<150 else 4)
f.path('M112,130 C140,128 150,120 158,114',stroke='#16a34a',sw=1.2); f.path('M202,114 C230,118 246,126 246,134',stroke='#16a34a',sw=1.2)
f.path('M112,134 C120,150 128,160 130,168',stroke='#16a34a',sw=1.2); f.path('M160,170 C190,174 200,176 200,176',stroke='#16a34a',sw=1.2)
f.ellipse(300,168,11,7,'#fff','#9ca3af',1.4); f.text(300,189,'淀粉粒',10,'middle','#555')
f.line(52,60,62,90,'#555',1); f.text(12,52,'外膜、内膜',12,'start','#16a34a',True)
f.line(180,56,180,86,'#555',1); f.text(180,48,'基粒（类囊体堆叠）',12,'middle','#16a34a',True)
f.line(260,96,236,112,'#555',1)
f.lines(36,228,['类囊体膜','光合色素、电子传递链、','ATP 合成酶 → 光反应'],11,15,'start','#16a34a')
f.lines(206,228,['基质 stroma','含酶、DNA、核糖体','→ 暗反应（卡尔文循环）'],11,15,'start','#2563eb')
f.line(118,226,128,206,'#16a34a',1); f.line(290,226,262,200,'#2563eb',1)
f.text(180,288,'叶绿体：双层膜；内部有类囊体堆成的基粒，周围是基质',11,'middle','#555')
f.save(OUT+'/b3_6a.svg')

# ---------- 图 3-6b 光反应与暗反应总览
f=Fig(360,280)
f.box(8,76,130,124,'','#f0fdf4','#86efac')
f.text(73,96,'光反应',14,'middle','#16a34a',True); f.text(73,112,'类囊体膜',11,'middle','#555')
f.lines(73,136,['光能激发叶绿素','H₂O → O₂ + H⁺ + e⁻','合成 ATP、NADPH'],10,16,'middle','#222')
f.box(222,76,130,124,'','#eff6ff','#93c5fd')
f.text(287,96,'暗反应',14,'middle','#2563eb',True); f.text(287,112,'卡尔文循环 · 基质',11,'middle','#555')
f.lines(287,136,['CO₂ 固定','还原：用 ATP、NADPH','合成糖类'],10,16,'middle','#222')
f.line(138,118,222,118,'#16a34a',2,arrow='g'); f.text(180,110,'ATP、NADPH',11,'middle','#16a34a',True)
f.line(222,170,138,170,'#2563eb',2,arrow='b'); f.text(180,162,'ADP + Pi、',11,'middle','#2563eb'); f.text(180,186,'NADP⁺',11,'middle','#2563eb')
f.line(60,36,60,74,'#d97706',2.2,arrow='o'); f.text(60,28,'光能',12,'middle','#d97706',True)
f.line(98,48,98,74,'#2563eb',2,arrow='b'); f.text(104,44,'H₂O',12,'start','#2563eb',True)
f.line(60,202,60,240,'#16a34a',2,arrow='g'); f.text(60,256,'O₂',12,'middle','#16a34a',True)
f.line(287,36,287,74,'#555',2,arrow='a'); f.text(287,28,'CO₂',12,'middle','#222',True)
f.line(287,202,287,240,'#dc2626',2,arrow='r'); f.text(287,256,'糖类（淀粉、蔗糖等）',12,'middle','#dc2626',True)
f.text(180,274,'光能 → ATP、NADPH 中的化学能 → 糖类中稳定的化学能',10,'middle','#555')
f.save(OUT+'/b3_6b.svg')

# ---------- 图 3-6c 卡尔文循环
f=Fig(360,330)
f.box(115,36,130,44,'RuBP（5C）','#eff6ff','#93c5fd',13,True)
f.box(225,160,125,44,'2 × GP（3C）','#fef3c7','#d97706',13,True,'又叫 PGA',10)
f.box(10,160,125,44,'2 × TP（3C）','#dcfce7','#16a34a',13,True,'又叫 G3P',10)
f.path('M245,62 C292,66 300,112 292,158',stroke='#222',sw=2,arrow='a')
f.lines(282,100,['① CO₂ 固定','CO₂ + RuBP','（酶：Rubisco）'],10,14,'end','#222')
f.line(225,182,137,182,'#222',2,arrow='a')
f.text(181,172,'② 还原',11,'middle','#222',True); f.text(181,198,'消耗 ATP、NADPH',10,'middle','#dc2626')
f.path('M60,158 C48,110 82,76 113,62',stroke='#222',sw=2,arrow='a')
f.lines(18,100,['③ 再生 RuBP','消耗 ATP','（5/6 的 TP）'],10,14,'start','#222')
f.line(72,206,72,244,'#16a34a',2.2,arrow='g')
f.text(72,260,'1/6 的 TP 离开循环',11,'middle','#16a34a',True); f.text(72,275,'→ 葡萄糖、淀粉、脂质、氨基酸',10,'middle','#16a34a')
f.text(250,235,'每固定 3 个 CO₂：',11,'start','#555',True)
f.text(250,251,'9 ATP + 6 NADPH',11,'start','#dc2626'); f.text(250,267,'→ 净得 1 个 TP',11,'start','#555')
f.text(180,310,'合成 1 个葡萄糖要固定 6 个 CO₂ → 18 ATP + 12 NADPH',11,'middle','#555')
f.save(OUT+'/b3_6c.svg')

# ---------- 图 3-6d 吸收光谱
f=Fig(360,270)
f.add('<defs><linearGradient id="spec" x1="0" x2="1"><stop offset="0" stop-color="#7c3aed"/><stop offset="0.2" stop-color="#2563eb"/><stop offset="0.38" stop-color="#06b6d4"/><stop offset="0.5" stop-color="#16a34a"/><stop offset="0.62" stop-color="#eab308"/><stop offset="0.78" stop-color="#f97316"/><stop offset="1" stop-color="#dc2626"/></linearGradient></defs>')
X=lambda l:50+(l-400)*0.95
f.line(50,190,342,190,arrow='a'); f.line(50,190,50,30,arrow='a'); f.text(56,34,'吸收量',12,'start')
f.add(f'<rect x="50" y="194" width="{X(700)-50}" height="10" fill="url(#spec)"/>')
for l in (400,450,500,550,600,650,700): f.text(X(l),222,str(l),11)
f.text(342,238,'波长 / nm',12,'end')
L=range(400,701,4)
f.curve([(X(l),190-gauss(l,430,17,125)-gauss(l,662,12,105)-8) for l in L],'#16a34a',2.4)
f.curve([(X(l),190-gauss(l,453,16,100)-gauss(l,642,12,55)-6) for l in L],'#84cc16',2.4)
f.curve([(X(l),190-gauss(l,450,22,80)-gauss(l,480,16,60)-2) for l in L],'#f97316',2.4)
f.text(214,46,'叶绿素 a',11,'start','#16a34a',True); f.text(214,60,'叶绿素 b',11,'start','#65a30d',True); f.text(214,74,'类胡萝卜素',11,'start','#f97316',True)
f.text(X(560),150,'绿光吸收少，',11,'middle','#222'); f.text(X(560),165,'大部分被反射',11,'middle','#222')
f.text(X(440),256,'蓝紫光',11,'middle','#2563eb',True); f.text(X(660),256,'红光',11,'middle','#dc2626',True)
f.text(180,12,'',10)
f.save(OUT+'/b3_6d.svg')

# ---------- 图 3-6e 纸层析
f=Fig(360,330)
f.text(180,20,'纸层析分离叶绿体色素',13,'middle','#222',True)
f.rect(140,36,80,226,'#fffbeb','#d6d3d1',1.5,2)
f.line(110,52,250,52,'#2563eb',1.2,'4 3'); f.text(256,56,'溶剂前沿',11,'start','#2563eb')
f.line(110,232,250,232,'#555',1.2,'4 3'); f.text(256,236,'起始线（铅笔）',11,'start','#555')
spots=[(76,'#f97316','胡萝卜素','橙黄色'),(110,'#eab308','叶黄素','黄色'),(152,'#0d9488','叶绿素 a','蓝绿色'),(190,'#84cc16','叶绿素 b','黄绿色')]
for y,c,n,d in spots:
    f.ellipse(180,y,26,8,c,c,1)
    f.text(256,y+4,n,12,'start','#222',True); f.text(318,y+4,d,10,'start','#555')
f.ellipse(180,232,6,3,'#16a34a','#16a34a',1)
f.line(122,232,122,52,'#222',1.2,arrow='a',both=True); f.text(116,146,'b',13,'end','#222',True)
f.line(130,232,130,76,'#dc2626',1.2,arrow='r',both=True); f.text(138,160,'a',13,'start','#dc2626',True)
f.rect(100,262,160,52,'#e0f2fe','#7dd3fc',1.5,4); f.line(180,262,180,238,'#d6d3d1',1.5)
f.text(180,294,'层析液',12,'middle','#0369a1')
f.text(14,22,'Rf = a ÷ b',12,'start','#dc2626',True)
f.text(14,38,'移得越远，Rf 越大',10,'start','#555')
f.save(OUT+'/b3_6e.svg')

# ---------- 图 3-7a 光照强度与净光合速率（阳生 vs 阴生）
f=Fig(360,290)
f.line(50,150,342,150,arrow='a'); f.line(50,238,50,28,arrow='a')
f.text(56,34,'CO₂ 吸收量（净光合速率）',11,'start'); f.text(342,170,'光照强度',12,'end')
f.text(46,60,'吸收',10,'end','#555'); f.text(46,236,'释放',10,'end','#555')
sun=bez(50,194,100,192,150,90,215,64)+bez(215,64,250,52,290,52,332,52)[1:]
shd=bez(50,176,80,172,110,130,150,112)+bez(150,112,180,98,250,98,332,98)[1:]
f.curve(sun,'#2563eb',2.6); f.curve(shd,'#16a34a',2.6)
cs=cross(sun,150); cd=cross(shd,150)
for c,col in ((cs,'#2563eb'),(cd,'#16a34a')): f.circle(c,150,4.2,col,col,1)
f.line(215,64,215,150,'#2563eb',1,'4 3'); f.line(150,112,150,150,'#16a34a',1,'4 3')
f.text(cs,166,'光补偿点',11,'middle','#2563eb',True); f.text(cs,180,'（阳生）',10,'middle','#2563eb')
f.text(cd-8,130,'光补偿点',11,'end','#16a34a',True); f.text(cd-8,143,'（阴生）',10,'end','#16a34a')
f.text(215,166,'光饱和点',11,'middle','#2563eb',True); f.text(215,180,'（阳生）',10,'middle','#2563eb')
f.text(150,100,'光饱和点（阴生）',10,'middle','#16a34a')
f.text(335,44,'阳生植物',12,'end','#2563eb',True); f.text(335,92,'阴生植物',12,'end','#16a34a',True)
f.line(38,150,38,194,'#555',1,arrow='a',both=True); f.text(28,172,'呼吸速率',10,'middle','#555',rot=-90)
f.text(60,216,'纵轴截距（无光时）= 呼吸速率',10,'start','#555')
f.lines(180,252,['光补偿点：光合速率 = 呼吸速率，净 CO₂ 交换 = 0；','之后光合 > 呼吸，有机物积累'],10,14,'middle','#555')
f.save(OUT+'/b3_7a.svg')

# ---------- 图 3-7b 限制因素
f=Fig(360,270)
f.axes(50,220,342,26,'','光合速率'); f.text(342,240,'光照强度',12,'end')
S=bez(50,218,80,196,110,172,150,152)
low=S+bez(150,152,180,142,210,140,332,140)[1:]
high=S+bez(150,152,190,128,235,96,282,82)[1:]+bez(282,82,300,76,318,74,332,74)[1:]
f.curve(low,'#dc2626',2.6); f.curve(high,'#2563eb',2.6)
f.text(332,132,'低 CO₂',12,'end','#dc2626',True); f.text(332,66,'高 CO₂',12,'end','#2563eb',True)
f.text(96,120,'A 段：限制因素',11,'middle','#222',True); f.text(96,135,'= 光照强度',11,'middle','#222',True)
f.line(96,140,100,176,'#999',1,'3 2')
f.lines(236,172,['B 段：低 CO₂ 曲线平台','限制因素 = CO₂ 浓度'],10,14,'middle','#dc2626')
f.lines(232,50,['高 CO₂ 曲线继续上升','直到下一个限制因素出现'],10,14,'middle','#2563eb')
f.text(190,262,'曲线上升段，限制因素 = 横坐标；平台段 = 其他因素（看图中另一条曲线）',10,'middle','#555')
f.save(OUT+'/b3_7b.svg')

# ---------- 图 3-7c 氧浓度与 CO₂ 释放
f=Fig(360,270)
f.axes(50,215,342,26,'','CO₂ 释放量'); f.text(342,236,'O₂ 浓度 / %',12,'end')
Y=lambda v:215-v*14
an=lambda x:10*math.exp(-x/2); ae=lambda x:8*(1-math.exp(-x/3))
xs=[i*0.5 for i in range(0,41)]
X2=lambda x:50+x*14
f.curve([(X2(x),Y(an(x))) for x in xs],'#dc2626',2.2,'5 3')
f.curve([(X2(x),Y(ae(x))) for x in xs],'#2563eb',2.2)
f.curve([(X2(x),Y(an(x)+ae(x))) for x in xs],'#222',3)
tot=[(x,an(x)+ae(x)) for x in xs]; mx,mv=min(tot,key=lambda t:t[1])
f.circle(X2(mx),Y(mv),5,'#16a34a','#16a34a',1); f.line(X2(mx),Y(mv),X2(mx),215,'#16a34a',1,'4 3')
f.text(166,Y(mv)-52,'总释放量最低点',11,'start','#16a34a',True); f.text(166,Y(mv)-38,'有机物消耗最少，适合贮藏',10,'start','#16a34a'); f.line(164,Y(mv)-34,X2(mx)+5,Y(mv)-6,'#16a34a',1)
f.line(X2(10),Y(0.4),X2(10),215,'#999',1,'4 3'); f.text(X2(10),230,'此后只有有氧呼吸',10,'middle','#555')
f.text(60,Y(10)-12,'无氧呼吸（虚线）',11,'start','#dc2626',True)
f.text(332,Y(ae(20))-8,'有氧呼吸',11,'end','#2563eb',True); f.text(332,Y(an(20)+ae(20))-30,'总 CO₂（黑线）',11,'end','#222',True)
f.text(190,262,'示意图；曲线形状用来说明趋势，数值不是实测',10,'middle','#555')
f.save(OUT+'/b3_7c.svg')

# ---------- 图 3-sum 光合作用与呼吸作用的关系
f=Fig(360,320)
f.box(8,84,126,132,'','#f0fdf4','#86efac'); f.box(226,84,126,132,'','#fff7ed','#fdba74')
f.text(71,104,'光合作用',14,'middle','#16a34a',True); f.text(71,120,'叶绿体',11,'middle','#555')
f.lines(71,142,['需要光','CO₂ + H₂O','→ 有机物 + O₂','光能 → 化学能'],11,17,'middle','#222')
f.text(289,104,'有氧呼吸',14,'middle','#ea580c',True); f.text(289,120,'细胞质基质、线粒体',10,'middle','#555')
f.lines(289,142,['有光无光都进行','有机物 + O₂','→ CO₂ + H₂O','化学能 → ATP + 热'],11,17,'middle','#222')
f.line(136,122,224,122,'#16a34a',2,arrow='g'); f.text(180,114,'有机物、O₂',11,'middle','#16a34a',True)
f.line(224,176,136,176,'#ea580c',2,arrow='o'); f.text(180,168,'CO₂、H₂O',11,'middle','#ea580c',True)
f.line(71,40,71,82,'#d97706',2.2,arrow='o'); f.text(71,32,'光能',12,'middle','#d97706',True)
f.line(289,218,289,256,'#dc2626',2.2,arrow='r'); f.text(289,272,'ATP（供生命活动）+ 热',11,'middle','#dc2626',True)
f.text(180,300,'物质可以循环利用；能量不循环：光能 → 化学能 → ATP 和热',10,'middle','#555')
f.save(OUT+'/b3_sum.svg')
print('b3b done')
