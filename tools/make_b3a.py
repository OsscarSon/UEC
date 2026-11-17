import sys,os,math
sys.path.insert(0,os.path.dirname(__file__))
from figlib import *
OUT=os.path.join(os.path.dirname(__file__),'..','assets','fig')
BL,BS='#dbeafe','#2563eb'; OF,OS='#fed7aa','#ea580c'; RF,RS='#fecaca','#dc2626'

def enzyme(f,x,y,nw,nd,lab=None):
    """酶：蓝色块，顶部有凹槽（活性部位）。x,y=左上角；凹槽宽 nw、深 nd"""
    cx=x+45
    f.poly([(x,y),(cx-nw/2,y),(cx,y+nd),(cx+nw/2,y),(x+90,y),(x+90,y+55),(x,y+55)],BL,BS,2)
    if lab: f.text(cx,y+40,lab,12)
def sub(f,cx,top,part='all',fill=OF,stroke=OS):
    """底物：向下的三角形（宽30，高22）。part=left/right 为产物的一半"""
    L,R,B=(cx-15,top),(cx+15,top),(cx,top+22)
    if part=='all':
        f.poly([L,R,B],fill,stroke,2); f.line(cx,top,cx,top+22,stroke,1.2,'3 2')
    elif part=='left': f.poly([L,(cx,top),B],fill,stroke,2)
    else: f.poly([(cx,top),R,B],fill,stroke,2)

# ---------- 图 3-1a 锁钥模型与诱导契合模型
f=Fig(360,330)
f.text(12,22,'锁钥模型',13,'start','#2563eb',True)
f.text(12,178,'诱导契合模型',13,'start','#2563eb',True)
for r,(y0,induced) in enumerate([(70,False),(226,True)]):
    for i,x0 in enumerate([20,135,250]):
        cx=x0+45
        if i==0:
            enzyme(f,x0,y0,30 if not induced else 46,22 if not induced else 12,'酶')
            sub(f,cx,y0-42)
            f.text(cx,y0+78,'① 底物接近活性部位',11,fill='#555')
        elif i==1:
            enzyme(f,x0,y0,30,22,'酶')
            sub(f,cx,y0)
            f.text(cx,y0+78,'② 酶–底物复合物',11,fill='#555')
            if induced: f.text(cx,y0-12,'活性部位改变形状',11,fill='#dc2626')
        else:
            enzyme(f,x0,y0,30 if not induced else 46,22 if not induced else 12,'酶')
            sub(f,cx-12,y0-44,'left'); sub(f,cx+12,y0-44,'right')
            f.text(cx,y0+78,'③ 产物离开，酶不变',11,fill='#555')
    f.line(116,y0+25,132,y0+25,'#222',1.6,arrow='a'); f.line(231,y0+25,247,y0+25,'#222',1.6,arrow='a')
f.text(180,318,'活性部位的形状由酶的三级结构决定；底物与它互补',11,fill='#555')
f.save(OUT+'/b3_1a.svg')

# ---------- 图 3-1b 活化能
f=Fig(360,250)
f.axes(50,208,342,25,'','能量')
f.text(342,226,'反应进程',12,'end')
def bez(x0,y0,x1,y1,x2,y2,x3,y3,n=40):
    return [((1-t)**3*x0+3*(1-t)**2*t*x1+3*(1-t)*t*t*x2+t**3*x3, (1-t)**3*y0+3*(1-t)**2*t*y1+3*(1-t)*t*t*y2+t**3*y3) for t in [i/n for i in range(n+1)]]
nw=bez(60,150,110,150,120,55,175,55)+bez(175,55,230,55,240,185,310,185)[1:]
we=bez(60,150,110,150,120,100,175,100)+bez(175,100,230,100,240,185,310,185)[1:]
f.curve(nw,'#dc2626',2.4); f.curve(we,'#2563eb',2.4)
f.line(60,150,100,150,'#999',1,'4 3'); f.line(310,185,336,185,'#999',1,'4 3')
f.line(72,55,175,55,'#dc2626',1,'3 3'); f.line(96,100,175,100,'#2563eb',1,'3 3')
f.line(72,150,72,57,'#dc2626',1.8,arrow='r'); f.line(96,150,96,102,'#2563eb',1.8,arrow='b')
f.text(72,48,'Ea',12,'middle','#dc2626',True); f.text(96,94,'Ea',12,'middle','#2563eb',True)
f.text(332,42,'Ea = 活化能',12,'end','#222',True)
f.text(332,60,'无酶：Ea 大',12,'end','#dc2626'); f.text(332,76,'有酶：Ea 小',12,'end','#2563eb')
f.text(82,170,'反应物',12,'middle'); f.text(310,178,'产物',12,'middle')
f.text(190,244,'酶降低活化能，不改变反应物和产物的能量，也不改变平衡点',11,fill='#555')
f.save(OUT+'/b3_1b.svg')

# ---------- 图 3-2a 温度与酶活性
f=Fig(360,266)
f.axes(50,210,345,30,'','酶活性'); f.text(345,240,'温度 / °C',12,'end')
f.rect(50,34,148,176,'#eff6ff','none',0,0); f.rect(215,34,125,176,'#fef2f2','none',0,0)
pts=bez(50,205,100,200,150,150,198,60)+bez(198,60,215,32,228,70,240,140)[1:]+bez(240,140,248,185,252,205,262,207)[1:]
f.curve(pts,'#2563eb',2.6)
f.line(198,60,198,210,'#222',1.2,'4 3')
for t in (0,20,37,60): f.text(50+t*4,226,str(t),11)
f.text(198,26,'最适温度（约 37 °C，人体酶）',12,'middle','#16a34a',True)
f.lines(122,90,['低温：分子运动慢，','活性低，但不变性','（回暖可恢复）'],11,15,'middle','#2563eb')
f.lines(288,90,['高温：酶变性','（空间结构被破坏）','不可逆'],11,15,'middle','#dc2626')
f.text(190,256,'温度每升高约 10 °C，速率约增加 1 倍，直到接近最适温度',11,fill='#555')
f.save(OUT+'/b3_2a.svg')

# ---------- 图 3-2b pH 与酶活性
f=Fig(360,266)
f.axes(50,205,345,28,'','酶活性'); f.text(345,240,'pH',12,'end')
def bell(mu,sg): return [(50+p*20, 205-gauss(p,mu,sg,150)) for p in [i*0.2 for i in range(0,71)]]
f.curve(bell(2,1.1),'#dc2626'); f.curve(bell(7,1.2),'#16a34a'); f.curve(bell(8.3,1.1),'#2563eb')
for p in (0,2,4,6,8,10,12,14): f.text(50+p*20,222,str(p),11)
f.text(108,60,'胃蛋白酶',12,'start','#dc2626',True); f.text(108,75,'最适 pH ≈ 2',11,'start','#dc2626')
f.text(205,34,'唾液淀粉酶（≈7）',12,'end','#16a34a',True)
f.text(268,52,'胰蛋白酶',12,'start','#2563eb',True); f.text(268,67,'最适 pH ≈ 8',11,'start','#2563eb')
f.text(190,258,'每种酶有自己的最适 pH；过酸或过碱会使酶变性',11,fill='#555')
f.save(OUT+'/b3_2b.svg')

# ---------- 图 3-2c 底物浓度与酶浓度
f=Fig(360,240)
f.text(95,24,'底物浓度的影响（酶量固定）',12,'middle','#222',True); f.text(268,24,'酶浓度的影响（底物充足）',12,'middle','#222',True)
f.axes(30,195,170,35,'底物浓度','速率')
mm=lambda S,V,K:V*S/(K+S)
f.curve([(30+S*1.45, 195-mm(S,130,20)*1.0) for S in [i*1 for i in range(0,97)]],'#2563eb')
f.curve([(30+S*1.45, 195-mm(S,150,20)*1.0) for S in [i*1 for i in range(0,97)]],'#16a34a',2.2,'5 3')
f.line(30,65,170,65,'#16a34a',1,'3 3'); 
f.text(165,52,'加倍酶量：平台更高',10,'end','#16a34a')
f.text(165,113,'酶被饱和：',10,'end','#2563eb'); f.text(165,126,'限制因素 = 酶量',10,'end','#2563eb')
f.text(52,170,'限制因素 =',10,'start','#555'); f.text(52,182,'底物浓度',10,'start','#555')
f.axes(205,195,345,35,'酶浓度','速率')
f.curve([(205,195),(335,60)],'#2563eb')
f.text(330,95,'成正比',11,'end','#2563eb'); f.text(275,218,'（底物过量时）',10)
f.text(180,236,'',10)
f.save(OUT+'/b3_2c.svg')

# ---------- 图 3-2d 抑制剂
f=Fig(360,232)
cols=[(20,'正常'),(135,'竞争性抑制剂'),(250,'非竞争性抑制剂')]
for i,(x0,t) in enumerate(cols):
    cx=x0+45; f.text(cx,22,t,12,'middle','#222',True)
    if i==0:
        enzyme(f,x0,95,30,22,'酶'); sub(f,cx,95)
        f.lines(cx,178,['底物进入活性部位','反应正常进行'],11,15,'middle','#555')
    elif i==1:
        enzyme(f,x0,95,30,22,'酶'); sub(f,cx,95,'all',RF,RS)
        sub(f,cx-48,40,'all'); f.line(cx-33,58,cx-22,78,'#ea580c',1.4,arrow='o')
        f.text(cx+30,70,'抑制剂',11,'start','#dc2626'); f.text(cx+30,84,'占据活性部位',11,'start','#dc2626')
        f.lines(cx,178,['与底物竞争活性部位','增加底物可减弱抑制'],11,15,'middle','#555')
    else:
        f.poly([(x0,95),(x0+20,95),(x0+45,105),(x0+70,95),(x0+90,95),(x0+90,150),(x0,150)],BL,BS,2)
        f.text(cx,132,'酶',12)
        f.circle(cx,162,9,RF,RS,2); f.text(cx+16,166,'抑制剂',11,'start','#dc2626')
        f.line(cx,153,cx,150,'#dc2626',1.4)
        sub(f,cx,44); f.line(cx,70,cx,88,'#ea580c',1.4,arrow='o'); f.text(cx+14,86,'✕',14,'start','#dc2626',True)
        f.lines(cx,198,['结合在活性部位以外，','酶变形；增加底物无效'],11,15,'middle','#555')
f.save(OUT+'/b3_2d.svg')

# ---------- 图 3-2e 抑制剂对速率的影响
f=Fig(360,240)
f.axes(50,200,340,28,'底物浓度','反应速率')
S=[i for i in range(0,101)]
f.curve([(50+s*2.7,200-mm(s,150,15)) for s in S],'#2563eb')
f.curve([(50+s*2.7,200-mm(s,150,60)) for s in S],'#dc2626',2.4)
f.curve([(50+s*2.7,200-mm(s,80,15)) for s in S],'#ea580c',2.4)
f.line(50,50,330,50,'#999',1,'4 3')
f.text(330,44,'Vmax（无抑制剂）',11,'end','#555')
for i,(c,t) in enumerate([('#2563eb','无抑制剂'),('#dc2626','竞争性：Vmax 不变，需更多底物'),('#ea580c','非竞争性：Vmax 降低')]):
    f.line(96,160+i*17,118,160+i*17,c,2.6); f.text(124,164+i*17,t,11,'start',c)
f.text(195,230,'曲线为示意图，用来比较形状',11,fill='#555')
f.save(OUT+'/b3_2e.svg')

# ---------- 图 3-3 固定化酶
f=Fig(360,270)
f.rect(120,60,120,150,'#f8fafc','#94a3b8',2,10)
import random; random.seed(7)
for r in range(6):
    for c in range(4):
        x=140+c*27+(r%2)*6; y=80+r*22
        f.circle(x,y,9,'#fde68a','#d97706',1.5); f.circle(x-2,y-2,2,'#2563eb','#2563eb',1); f.circle(x+3,y+2,2,'#2563eb','#2563eb',1)
f.line(180,22,180,58,'#ea580c',2.2,arrow='o'); f.text(180,16,'底物溶液流入',12,'middle','#ea580c',True)
f.line(180,212,180,248,'#16a34a',2.2,arrow='g'); f.text(180,262,'产物流出（不含酶，易纯化）',12,'middle','#16a34a',True)
f.circle(272,110,9,'#fde68a','#d97706',1.5); f.circle(270,108,2,'#2563eb','#2563eb',1); f.circle(275,112,2,'#2563eb','#2563eb',1)
f.text(288,114,'凝胶珠',11,'start','#555'); f.text(256,138,'酶固定在珠上',11,'start','#2563eb')

f.lines(20,92,['酶留在柱内','可重复使用','可连续生产'],11,16,'start','#2563eb')
f.save(OUT+'/b3_3.svg')

# ---------- 图 3-4 ATP 的结构与 ATP–ADP 循环
f=Fig(360,336)
f.text(180,22,'ATP 的结构',13,'middle','#222',True)
f.box(18,44,76,50,'腺嘌呤','#dcfce7','#16a34a',12,sub='adenine',subsize=10)
f.poly([(124,52),(150,68),(142,92),(106,92),(98,68)],'#fef3c7','#d97706',2); f.text(124,76,'核糖',12)
f.line(94,69,99,69,'#222',1.6)
for i,x in enumerate((184,236,288)):
    f.circle(x,69,19,'#fee2e2','#dc2626',2); f.text(x,74,'P',14,'middle','#dc2626',True)
f.line(150,69,165,69,'#222',1.6)
f.path('M203,69 q7,-9 14,0 t14,0',stroke='#dc2626',sw=1.8); f.path('M255,69 q7,-9 14,0 t14,0',stroke='#dc2626',sw=1.8)
f.text(210,104,'~',14,'middle','#dc2626',True); f.text(262,104,'~',14,'middle','#dc2626',True)
f.text(236,120,'~ = 高能磷酸键（水解时释放能量）',11,'middle','#dc2626')
f.line(18,100,150,100,'#555',1.2); f.text(84,115,'腺苷 adenosine',11,'middle','#555')
f.text(18,138,'AMP = 腺苷 + 1 个磷酸；ADP = 腺苷 + 2 个磷酸',11,'start','#555'); f.text(18,152,'ATP = 腺苷 + 3 个磷酸',11,'start','#555')
f.text(180,176,'ATP–ADP 循环',13,'middle','#222',True)
f.box(30,194,100,46,'ATP','#fee2e2','#dc2626',16,True)
f.box(230,194,100,46,'ADP + Pi','#fef3c7','#d97706',15,True)
f.path('M130,208 C170,186 190,186 228,208',stroke='#dc2626',sw=2,arrow='r')
f.path('M228,228 C190,252 170,252 132,228',stroke='#16a34a',sw=2,arrow='g')
f.lines(180,274,['水解（+H₂O，ATP 酶）：释放能量 → 供生命活动'],11,15,'middle','#dc2626')
f.lines(180,294,['磷酸化：吸收能量（呼吸、光合）→ 重新合成 ATP'],11,15,'middle','#16a34a')
f.text(180,318,'细胞里 ATP 很少，但分解与合成极快，不断循环',11,'middle','#555')
f.save(OUT+'/b3_4.svg')
print('b3a done')
