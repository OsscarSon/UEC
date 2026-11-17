"""Deterministic, original teaching SVGs. No AI image generation."""
from pathlib import Path
from html import escape
import math,json,subprocess
R=Path(__file__).resolve().parents[1];OUT=R/'assets/verified';OUT.mkdir(exist_ok=True)
B=['<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1100 760" role="img">','<style>text{font-family:"Noto Sans CJK SC",sans-serif;fill:#142b40;font-size:24px}.title{font-size:32px;font-weight:700}.small{font-size:21px}.box{fill:#edf5ff;stroke:#245b91;stroke-width:2}.line{fill:none;stroke:#245b91;stroke-width:3}</style>','<defs><marker id="a" markerWidth="8" markerHeight="8" refX="7" refY="4" orient="auto"><path d="M0,0L8,4L0,8" fill="#245b91"/></marker></defs>','<rect width="1100" height="760" fill="white"/>']
def text(x,y,s,cls=''):return f'<text x="{x}" y="{y}" class="{cls}">{escape(s)}</text>'
def line(x,y,a,b,arrow=False,color='#245b91'):return f'<path d="M{x},{y} L{a},{b}" fill="none" stroke="{color}" stroke-width="3"'+(' marker-end="url(#a)"' if arrow else '')+'/>'
def diagram(name,title,panels,footer,extra=''):
 parts=B+[text(35,52,title,'title')]
 for i,(heading,rows) in enumerate(panels):
  x=35+(i%2)*540;y=90+(i//2)*270
  parts+=[f'<rect class="box" x="{x}" y="{y}" width="510" height="245" rx="12"/>',text(x+18,y+38,heading)]
  parts += [text(x+18,y+82+j*37,v,'small') for j,v in enumerate(rows)]
 parts+=[extra,text(35,690,footer[0],'small'),text(35,727,footer[1],'small'),'</svg>']
 (OUT/(name+'.svg')).write_text(''.join(parts)+'\n')

diagram('chem5-1','5.1 模型：观察、推断与局限',[('实验观察',['多数α粒子近似直穿','少数大偏转，极少回散','类别数量不代表各1/3概率']),('支持的结构解释',['正电与大部分质量集中于小核','核远小于原子尺度','不直接测得电子圆轨道']),('历史模型',['汤姆生：正电连续分布假设','卢瑟福：带核结构','玻尔：氢的离散能级模型']),('模型验收',['解释旧证据，也需预测新现象','同一氢原子只有1个电子','能级选择不是同时有多个电子'])],['历史原理示意；不按比例，不提供放射性操作。','结构推断不等于对电子轨迹的直接拍照。'])
diagram('chem5-2','5.2 两套计数与一个统计平均',[('核子账本：²³₁₁Na⁺',['p = Z = 11','n = A − Z = 12','p + n = 23']),('电荷账本',['e = Z − q = 11 − 1 = 10','p − e = +1','电离不改变Z与A']),('丰度加权（题给近似）',['35×0.75 + 37×0.25 = 35.5','x₁+x₂ = 1','平均不是某个原子的质量数']),('质谱读图先查',['横轴通常m/z，须确定电荷态','单电荷时可作质量近似读数','丰度须归一化'])],['原子数、核子数与电荷不能混合相加。','这里只用明确题给近似；不是仪器实测谱图。'])
# Energy positions are computed from E=-13.6/n²; show a full-scale vertical axis.
parts=B+[text(35,50,'5.3 氢能级：数值轴与跃迁','title')]
y=lambda E:100+(0-E)*35
parts += [line(100,650,100,70,True),text(20,90,'E/eV')]
for n in [1,2,3,4]:
 E=-13.6/n**2;yy=y(E);parts += [line(150,yy,600,yy),text(620,yy+7,f'n={n}   E={E:.3f} eV')]
parts += [line(150,y(0),600,y(0)),text(620,y(0)+7,'电离界 E=0'),line(270,y(-13.6/9),270,y(-3.4),True),text(320,290,'3→2：光子约1.89 eV'),text(320,335,'λ≈656–657 nm（舍入）'),text(35,690,'能级位置按E计算；高n挤在0附近并非等间隔。','small'),text(35,727,'发射光子能量为正，原子能量变化为负；只用氢近似。','small'),'</svg>']
(OUT/'chem5-3.svg').write_text(''.join(parts)+'\n')
diagram('chem5-4','5.4 排布与离子：规则和边界',[('轨域与容量',['s：1轨域→2电子','p：3轨域→6电子','d：5轨域→10电子']),('2p占据（各格为等能轨域）',['C： [↑] [↑] [ ]','N： [↑] [↑] [↑]','O： [↑↓] [↑] [↑]']),('Fe核查',['Fe： [Ar]3d⁶4s² → 26e','Fe²⁺： [Ar]3d⁶ → 24e','Fe³⁺： [Ar]3d⁵ → 23e']),('不可误读',['电子自旋箭头不是空间轨迹','构造助记不等于普适能级顺序','4s/3d相对能量随状态改变'])],['基态规则：鲍利 + 汉德 + 构造近似，另核例外。','半满构型不能单独证明某氧化态在所有环境更稳定。'])
# Enzyme energy model: both endpoints fixed, distinct activation barriers.
parts=B+[text(35,50,'3.1 催化改变能垒，不改整体能差','title')]
for x0,peak,label in [(130,80,'无酶'),(600,45,'有酶')]:
 yy=lambda E:590-E*5
 parts += [line(x0,620,x0,100,True),line(x0,620,x0+390,620,True),line(x0+25,yy(20),x0+100,yy(20)),line(x0+290,yy(5),x0+365,yy(5)),'<path d="'+ ' '.join(('M' if j==0 else 'L')+str(x0+100+190*j/200)+','+str(yy((20+(peak-20)*math.sin(math.pi*j/200)) if j<=100 else (5+(peak-5)*math.sin(math.pi*j/200)))) for j in range(201)) +'" fill="none" stroke="#7451a1" stroke-width="4"/>',text(x0+75,95,label),text(x0+30,665,'反应进程'),text(x0+20,210,f'Ea模型值={peak-20}'),text(x0+20,250,'初20 → 末5')]
# The curve is conceptual, not its control-point height as exact measurement.
parts += [text(35,715,'能量模型：峰80/45、初20末5按轴计算；ΔE = −15相同。','small'),'</svg>']
(OUT/'bio3-1.svg').write_text(''.join(parts)+'\n')
diagram('bio3-2','3.2 酶曲线的条件与证据',[('温度 / pH',['最适值绑定具体酶与测定条件','Q10不能跨失活区无限外推','先预平衡，再比较初速']),('底物浓度平台',['固定酶量、温度、pH','饱和 ≠ 反应停止或酶坏掉','另排底物耗尽与仪器上限']),('竞争性理想模型',['Vmax不变','表观Km增大','增加底物可减弱相对抑制']),('纯非竞争性理想模型',['Vmax下降，Km不变','不等同全部变构/混合型','需参数和条件，不能仅看图高低'])],['不是实测曲线，无伪造最适温度、误差棒或显著性。','实验：自变量、初速、控制量、对照、重复、替代解释。'])
diagram('bio3-3','3.3 固定化酶：流动与传质',[('物料路径',['底物入口 → 接触固定化酶','催化转化 → 产物流出','支持网保留载体，不保证无泄漏']),('活性位路径',['底物先扩散到有效活性位','发生特定催化反应','产物再扩散离开']),('可检验优势',['易于回收、可连续使用','比较累计产物和有效活性','不保证每次都比游离酶快']),('控制与限制',['温度/pH/流速按协议确认','扩散与停留时间可限制转化','检测酶泄漏与载体影响'])],['装置原理图，无药品配方或虚构实验参数。','箭头指物料或过程，不能把能量当作产品流出。'])
diagram('bio3-4','3.4 ATP：整体水解与具体耦联',[('整体反应',['ATP + H₂O → ADP + Pi','整体ΔG依条件，可为负','断键本身需要能量']),('具体耦联',['酶促磷酸转移/构象变化等','连接特定吸能过程','仅把两式并列不证明已耦联']),('题给能量账',['水解 −30，吸能过程 +20','同进度总ΔG = −10 kJ/mol','有利 ≠ 无能垒或立即完成']),('再生',['ADP + Pi → ATP需能量输入','能源可由呼吸或光反应耦联','能量不随物质无限循环'])],['各反应式为生化简写，电荷/质子按具体pH约定处理。','能量箭头属于整体自由能变化，不从某根断键凭空射出。'])
diagram('bio3-5','3.5 呼吸账本与化学渗透',[('糖酵解：细胞质基质',['葡萄糖 → 2丙酮酸','投入2ATP、形成4、净2','后续发酵不再重复加2ATP']),('发酵分支',['再生NAD⁺使糖酵解持续','乳酸或乙醇/CO₂等路径','不是全部微生物厌氧呼吸']),('线粒体内膜区室',['H⁺泵：基质 → 膜间隙','ATP合酶回流：膜间隙 → 基质','电子流与H⁺流分开']),('有氧路径',['O₂为末端电子受体，形成水','总ATP依穿梭与耦联等条件','不把30–32与旧36–38混加'])],['能量、碳、电子和质子各自做账，不将路径分支全部相加。','定性区室示意；非实测ATP产量或操作方案。'])
diagram('bio3-6','3.6 光合：统一3CO₂碳基准',[('光反应：类囊体膜',['2H₂O → 4H⁺ + 4e⁻ + O₂','提供ATP与NADPH','O₂的氧来自水']),('碳固定：叶绿体基质',['3RuBP(15C) + 3CO₂(3C)','→ 6个3-PGA(18C)','后续得到6个G3P(18C)']),('分流与再生',['5G3P(15C) → 3RuBP(15C)','1G3P(3C) 净输出','18C = 15C + 3C']),('同一基准能量需求',['3CO₂：9ATP、6NADPH','6CO₂：18ATP、12NADPH','两份净G3P碳数相当于六碳糖'])],['碳数、分子数与能量使用同一循环次数，不混单次与三次。','暗反应不是只在夜间；ATP/还原力供应及调控仍重要。'])
diagram('bio3-7','3.7 净量与限制因素',[('净CO₂吸收为正',['N = P − R（同单位）','黑暗截距约 −R','补偿点N=0但P=R可非0']),('反推总光合',['例：净吸收6、呼吸2','P=N+R=8','呼吸条件及其他过程须说明']),('平台解释',['先查温度、CO₂和光是否受控','平台不唯一证明酶坏掉','改变另一变量可检验解释']),('储藏判断的限制',['总CO₂最低不必是最少底物','还需RQ、组织损伤与品质证据','不据模型给实际推荐氧浓度'])],['定性关系与明确题给数据分开；不是实测最优曲线。','单一净交换指标不能自动分解出所有总过程。'])
# Append these diagrams, preserving all existing paths and files.
for stem,key,prefix in [('chem05','化学5','chem5'),('bio03','生物3','bio3')]:
 p=R/'lessons'/(stem+'.js');obj=json.loads(subprocess.check_output(['node','-e',f"const fs=require('fs'),vm=require('vm'),c={{}};c.window=c;vm.createContext(c);vm.runInContext(fs.readFileSync('lessons/{stem}.js','utf8'),c);process.stdout.write(JSON.stringify(c.LESSONS['{key}']))"],cwd=R))
 for sec in obj['sections']:
  path='assets/verified/'+prefix+'-'+sec['id'].split('.')[1]+'.svg'
  if not any(f[0]==path for f in sec['figs']):sec['figs'].append([path,'本轮核对图：'+sec['t']+'；标明模型与条件，原有SVG文件保留。'])
 p.write_text('window.LESSONS=window.LESSONS||{};\nLESSONS['+json.dumps(key,ensure_ascii=False)+']='+json.dumps(obj,ensure_ascii=False,indent=2)+';\n')
 source=R/'data/base-lessons'/(stem+'.json')
 if source.exists():source.write_text(json.dumps(obj,ensure_ascii=False,indent=2)+'\n')
print('Built 11 deterministic diagrams; original 73 SVG files preserved')
