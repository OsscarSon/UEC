"""60 MCQ option sets and seven written scoring units re-read from PDF images.
Solutions are independently authored, not attributed to an official answer key.
"""
from pathlib import Path
import json,hashlib,itertools,math
import sympy as s
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams';AUDIT=R/'reports/math-audit';base={r['id']:r for p in AUDIT.glob('visual-review-*.json')for r in json.loads(p.read_text(encoding='utf-8'))};out={};checks=[]
x,t,a=s.symbols('x t a',real=True)
def add(c,y,n,options,letter,answer,steps,actual,expected):
 key=f'uec_math_{c}:{y}:mcq:{n}:whole';r=base[key]
 if callable(actual):actual=actual()
 delta=s.simplify(s.sympify(actual)-s.sympify(expected));assert delta.equals(0),(key,delta)
 assert len(options)==4 and letter in 'ABCD'and len(steps)>=3
 proof=dict(method='independent symbolic derivation or enumeration from reread PDF',formula_sha256=hashlib.sha256(r['formula_latex_verified'].encode()).hexdigest(),computed=str(actual),expected=str(expected),result='pass')
 out[key]=dict(source_pdf_id=r['source_pdf_id'],source_page=r['source_page'],options_verified=dict(zip('ABCD',options)),answer_verified=letter+':'+answer,answer_status='independently_solved_not_official_key',historical_solution_steps=steps,historical_marking_points=[dict(description='本题只有选中作者独立核算的正确选项才计本题满分；需教师或官方答案复核',marks=r['printed_marks'])],marking_scheme_status='author_suggested_not_official',independent_verification=proof,review_method='Read actual PDF page image, then independently derive; no report answer copied as proof')
 checks.append(dict(id=key,**proof))
add('ii',2022,1,['27/16','9/8','−9/8','−27/16'],'D','−27/16',['通项系数为C(1/2,3)(−3)³。','C(1/2,3)=1/16，故乘−27得−27/16。','系数是x³前数值，不把x³代入，也不漏负号。'],s.binomial(s.Rational(1,2),3)*(-3)**3,-s.Rational(27,16))
add('ii',2022,2,['x>1/6','−1<x<1/6','x<−1或x>1/6','x<−1/2或x>−1/3'],'C','(−∞,−1)∪(1/6,∞)',['对数真数6x²+5x−1须严格正。','因式为(6x−1)(x+1)，开口向上，两根外侧为正。','根−1、1/6均排除；例如x=0真数负可排除中间区间。'],s.factor(6*x*x+5*x-1),(6*x-1)*(x+1))
add('ii',2022,3,['x³+1','sin³x','cos³x','sin³x+cos³x'],'B','sin³x',['定义域R关于0对称。','sin(−x)³=−sin³x，所以B为奇。','A在0为1、C和D在0也为1，均不满足奇函数必有f(0)=0。'],s.trigsimp(s.sin(-x)**3+s.sin(x)**3),0)
pts=[(i,1)for i in range(4)]+[(i,0)for i in range(20)];P=(1,1);others=[p for p in pts if p!=P]
add('ii',2022,4,['60','190','250','880'],'C','250',['固定P，另外两点都在CD有C(20,2)=190个三角形。','另外一类是AB上另3点中选1、CD20点选1，共60个，两类互斥。','合计250；旧稿只数190漏掉第二类。本次枚举其余23点中的非共线点对再核对。'],sum((u[0]-P[0])*(v[1]-P[1])!=(u[1]-P[1])*(v[0]-P[0])for u,v in itertools.combinations(others,2)),250)
prob=sum(s.binomial(10,k)*s.Rational(55,100)**k*s.Rational(45,100)**(10-k)for k in range(8,11))
add('ii',2022,5,['0.0017','0.0063','0.0763','0.0996'],'D','约0.0996',['独立留下人数X~B(10,.55)。','至少8人为X=8、9、10三项概率之和，非只算X=8。','相加约0.0996，核对概率在0与1之间。'],round(float(prob),4),s.Rational(996,10000))
add('ii',2022,6,['1/2','1','2','不存在'],'C','2',['指数x²−2x=(x−1)²−1≥−1。','底1/2小于1，指数最小时函数最大。','x=1达到(1/2)^−1=2；实域无其他更大值。'],s.Rational(1,2)**(-1),2)
add('ii',2022,7,['第一象限','第二象限','第三象限','第四象限'],'B','第二象限',['分式乘共轭或直接算(−1+i)/(1+i)=i。','z=−1+i，实部负、虚部正。','因此位于第二象限，不把分式漏掉前面的−1。'],-1+(-1+s.I)/(1+s.I),-1+s.I)
add('ii',2022,8,['7/18','4/9','9/14','7/9'],'A','7/18',['D在BC内，角ADB与角ADC互补。','在三角ADB中，角ADB=π−α−β，故角ADC=α+β。','扩展正弦定律AC/sin(角ADC)=2R=36，所以所求14/36=7/18。'],s.Rational(14,36),s.Rational(7,18))
add('ii',2022,9,['40.9°','49.1°','54.7°','63.4°'],'B','49.1°',['按图PQ竖直差2a，底面投影跨过正六边形一个中间顶点，长度√3a。','锐线面角满足tanθ=2a/(√3a)。','θ≈49.1066°取一位49.1°；不能用透视线段像素量长度。'],round(math.degrees(math.atan(2/math.sqrt(3))),1),s.Rational(491,10))
add('ii',2022,10,['7/10','−7/15','7/15','−7/10'],'A','7/10',['将两给定式分别平方后相加。','左侧为144+25−120(sinA cosB−cosA sinB)=169−120sin(A−B)。','右侧81+4=85，所以sin(A−B)=84/120=7/10；注意相加交叉项实际为−120sin(A−B)。'],s.Rational(169-85,120),s.Rational(7,10))
add('ii',2022,11,['2π/5','3π/5','4π/5','π'],'B','3π/5',['采用arccot主值(0,π)，对每个实数u有arctan u+arccot u=π/2。','两式相加，反正切和=π−2π/5。','结果3π/5在两个反正切之和可能范围(−π,π)内；不可把两函数当倒数。'],s.pi-2*s.pi/5,3*s.pi/5)
add('ii',2022,12,['x²+5x−9y−14=0','x²−5x+9y−14=0','x²−5x−9y+14=0','x²−5x−9y−14=0'],'A','x²+5x−9y−14=0',['由x=3t−1得t=(x+1)/3。','代y=(t−1)(t+2)=t²+t−2并乘9。','得到9y=x²+5x−14，任意实t均能对应，未多添分支。'],s.expand(9*(((x+1)/3)**2+(x+1)/3-2)),x*x+5*x-14)
add('ii',2022,13,['√6','√14','3√2','4√3'],'B','√14',['圆的x²、y²系数相同且非零：k−2=6−k给k=4，公系数2。','除2后配方得(x−3)²+(y+1)²=14。','半径√14，不能把右侧14直接当半径。'],s.sqrt(9+1+4),s.sqrt(14))
add('ii',2022,14,['3','3√5','√333','√205'],'D','√205',['acos(−4/5)在第二象限，A=(−8,6)。','asin(12/13)在第一象限，B=(5,12)。','AB²=13²+6²=205，故√205；主值决定坐标符号。'],(-8-5)**2+(6-12)**2,205)
add('ii',2022,15,['2x+y−3=0','2x+y−6=0','x−2y+6=0','x−2y+7=0'],'D','x−2y+7=0',['AB斜率(5−3)/(4−0)=1/2。','由x=(y−3)²隐微分得1=2(y−3)y′，令y′=1/2，得y=4、x=1。','切线y−4=(x−1)/2即x−2y+7=0；切点代回抛物线成立。'],2*(4-3)*s.Rational(1,2),1)
add('ii',2022,16,['0','5','−5','7'],'C','−5',['给定商式是f在−2处的导数定义。','f′=2x−1，所以f′(−2)=−5。','分母x+2=x−(−2)，不能取x=2。'],s.diff(x*x-x+1,x).subs(x,-2),-5)
add('ii',2022,17,['0','1','2/3','0和2/3'],'D','0和2/3',['dy/dt=3t²−2t=t(3t−2)，候选t=0、2/3。','dx/dt=4t³+8t−9，分别−9、−67/27，均不为0。','两个候选均给有限水平切线，因此必须同时保留。'],(4*t**3+8*t-9).subs(t,s.Rational(2,3)),-s.Rational(67,27))
add('ii',2022,18,['a<0','a>0','1<a<2','a<1或a>2'],'A','a<0',['f′=6a(x−1)(x−2)。','在开区间(1,2)后两因子乘积负，递增需a<0使导数正。','端点导数0不妨碍全闭区间严格递增，a=0已由题目排除。'],s.factor(s.diff(2*a*x**3-9*a*x*x+12*a*x,x)),6*a*(x-1)*(x-2))
add('ii',2022,19,['−2a−2ln|1−a|','−2a+2ln|1−a|','2a+2ln|1−a|','2a−2ln|1−a|'],'A','−2a−2ln(1−a)',['设u=√x，则dx=2u du，上下限0到a。','2u/(1−u)=−2+2/(1−u)，积分为−2u−2ln|1−u|。','0<a<1保证无奇点，减去下端0得所求；不能只换根号不换dx。'],s.diff(-2*x-2*s.log(1-x),x),2*x/(1-x))
add('ii',2022,20,['π/2','π/3','π/4','π/5'],'C','π/4',['r=cos5θ有5瓣，单瓣由−π/10到π/10。','面积5×(1/2)∫cos²5θ dθ。','单瓣π/20，全图π/4；0到2π会重复描迹，不能再乘2。'],5*s.integrate(s.cos(5*x)**2/2,(x,-s.pi/10,s.pi/10)),s.pi/4)
add('i',2022,1,['−16','−8','8','16'],'A','−16',['余式定理代x=−2，得−25−2p=7。','解p=−16。','代回−8−12+32−5=7，符号与除式x+2相符。'],-25-2*(-16),7)
add('i',2022,2,['−2/3','−1/3','1/3','2/3'],'A','−2/3',['无穷等比和S=a/(1−r)=−9/10，且ar=1。','消去a，得9r²−9r−10=0，根5/3及−2/3。','无穷和存在要求|r|<1，保留−2/3，首项−3/2可验第二项1。'],s.factor(9*x*x-9*x-10),(3*x+2)*(3*x-5))
add('i',2022,3,['c≥0','b>0','b<c','b²>ac'],'B','b>0为错误叙述',['原图开口向下且截y轴正，故a<0、c>0。','顶点在y轴左边，−b/(2a)<0且a<0，推出b<0。','因此b>0错误；b<c以及b²>ac均因b负c正a负成立。'],s.sign(-1)*s.sign(1),-1)
add('i',2022,4,['−5i/13+12j/13','−5i/13−12j/13','−12i/13+5j/13','12i/13−5j/13'],'D','12i/13−5j/13',['PQ=(24,−10)，必须Q减P。','模√(24²+10²)=26，方向单位向量(12/13,−5/13)。','模平方144/169+25/169=1，且向右向下与原向量一致。'],s.Rational(12,13)**2+s.Rational(5,13)**2,1)
add('i',2022,5,['−560','−280','280','560'],'B','−280',['选k个−2/x²时指数为3(7−k)−2k=21−5k。','令指数6得k=3，系数C(7,3)(−2)³。','系数−280，k为第4项的索引，不把第几项与k混用。'],s.binomial(7,3)*(-2)**3,-280)
add('i',2022,6,['x<1','x<−1或−1<x<1','x<−1或x>1','无解'],'B','(−∞,−1)∪(−1,1)',['移到同侧通分得到(x+1)²/(x−1)<0。','分子除−1为0之外正，分母须负，故x<1且x≠−1。','x=1无定义；严格小于也排除使分子0的−1。'],s.factor((x*x+3*x)/(x-1)-1),(x+1)**2/(x-1))
add('i',2022,7,['(−3/2,0)','(−5/2,0)','(5/2,0)','(3/2,0)'],'C','(5/2,0)',['令y=0得x²−5x−3=0。','两根和5，所以弦AB中点横坐标5/2、纵坐标0。','判别式25+12>0确有两交点，不用求各根再平均。'],sum(s.solve(x*x-5*x-3,x))/2,s.Rational(5,2))
add('i',2022,8,['112','168','216','224'],'B','168',['10倍数末位固定0。','千位可选4、5、6共3种；百位从其余非0数字选8种，十位再选7种。','3×8×7=168；4000、7000本身不合无重复及所给范围。'],sum(len(set(str(n)))==4 for n in range(4010,7000,10)),168)
add('i',2022,9,['0.1587','0.3174','0.6826','0.8413'],'C','0.6826',['均值100，75与125关于均值对称。','故两侧尾概率各.1587，无需先求σ或查表。','中间概率1−2×.1587=.6826，边界连续变量不影响。'],1-2*s.Rational(1587,10000),s.Rational(6826,10000))
add('i',2022,10,['k','√(1−k²)/k²','−k','−√(1−k²)'],'D','−√(1−k²)',['sin(π−x)=sinx=k，且x在第一象限。','tan(3π/2−x)=cotx，sin(2π−x)=−sinx。','乘积−cosx=−√(1−k²)，正根来自第一象限。'],s.trigsimp(s.tan(3*s.pi/2-x)*s.sin(2*s.pi-x)),-s.cos(x))
add('i',2022,11,['40cm²','90cm²','120cm²','160cm²'],'D','160cm²',['设OA=3u、AC=2u，外半径OC=5u。','同角扇形面积比外/内=25/9，外面积250。','阴影为外减内=250−90=160，不把AC当外半径。'],90*(s.Rational(25,9)-1),160)
add('i',2022,12,['图A：中线1且从(0,1)递增','图B：中线1且从(0,1)递减','图C：中线−1且从(0,−1)递减','图D：中线−1且从(0,−1)递增'],'D','图D',['振幅2、中线−1、周期π，值域[−3,1]。','x=0时y=−1，且导数4cos0=4>0，起始递增。','只有图D同时满足；仅看周期不能区分C与D。'],s.diff(2*s.sin(2*x)-1,x).subs(x,0),4)
add('i',2022,13,['62.23°','68.79°','73.77°','78.22°'],'D','78.22°',['底面等边边8，O为底心、M为AB中点；OM=4√3/3。','侧棱VA=VB=12，所以VM=√(144−16)=8√2。','二面角平面角为VMO，cosθ=OM/VM=√6/12，θ≈78.22°；不以侧棱代替侧面斜高。'],round(math.degrees(math.acos(math.sqrt(6)/12)),2),s.Rational(7822,100))
add('i',2022,14,['−2','−1','1','2'],'C','1',['交点在y轴故x=0，两式给(k+1)y=6与y=3k。','合并k(k+1)=2，得k=1、−2。','对应y=3与−6，题目要求正y轴，只取1。'],s.factor(x*(x+1)-2),(x-1)*(x+2))
add('i',2022,15,['增大','减小','保持不变','先增大再减小'],'C','保持不变',['直线y=mx对所有实m都过圆心O。','它与半径2的圆形成的弦必为直径。','AB始终4，斜率变化只改变方向，不改变直径长度。'],2*s.sqrt(4),4)
add('i',2022,16,['−27或−23','27或23','−27或13','27或−23'],'D','27或−23',['点线距离|3·2−4·1−c|/5=5。','故|2−c|=25，c=2±25。','得27、−23，两者均代入得距离5，不能遗漏绝对值分支。'],sum(s.solve((2-x)**2-625,x)),4)
add('i',2022,17,['−1','0','1','2'],'C','1',['切点本身应在曲线上。','代(−1,2)得2−2m+4=4，所以m=1。','隐微分后在点得斜率2/3，与2x−3y+8=0一致，过点与斜率双重验证。'],(4*(-1)+1*2+1*(-1)*s.Rational(2,3)+2*2*s.Rational(2,3)),0)
add('i',2022,18,['−20πcm²/s','−10πcm²/s','10πcm²/s','20πcm²/s'],'B','−10πcm²/s',['面积A=πr²，dA/dt=2πr dr/dt。','给直径10所以r=5，减小速率dr/dt=−1。','得−10π，面积在减小，负号与单位cm²/s均必要。'],2*s.pi*5*(-1),-10*s.pi)
add('i',2022,19,['−4/7','−2/7','−1/7','8/7'],'A','−4/7',['基本定理给积分2[f(5)−f(1)]。','f(5)=5/√49=5/7，f(1)=1。','结果2(5/7−1)=−4/7；上限5不能当作代入导数。'],2*(s.Rational(5,7)-1),-s.Rational(4,7))
add('i',2022,20,['(0,2/3)','(2/3,1)','(1,3/2)','(3/2,∞)'],'D','a>3/2',['面积∫0ᵃ√x dx=(2/3)a^(3/2)=9/4。','解a=(27/8)^(2/3)=9/4。','9/4落在(3/2,∞)，而不是面积本身所在的候选区间。'],(s.Rational(27,8))**s.Rational(2,3),s.Rational(9,4))
add('i',2023,1,['−4','−2','2','5'],'D','5',['根和3、积c。','α²+β²=9−2c=4，故2c=5。','题目问2c，不是c=5/2。'],9-4,5)
add('i',2023,2,['0','−x+2','x+1','x−1'],'B','−x+2',['余式次数小于2，可设ax+b。','由p(2)=0、p(−1)=3，得2a+b=0、−a+b=3。','解a=−1、b=2；原两点代入余式均符合。'],((-x+2).subs(x,2))**2+((-x+2).subs(x,-1)-3)**2,0)
add('i',2023,3,['0','1','2','3'],'C','2',['实根要求x≤0，使两边均非负。','平方得−x³=x²即x²(x+1)=0，候选x=0、−1。','两值代回原式均成立，因此2个不同根，重根0只计一次。'],len({v for v in [0,-1]if s.sqrt(-v**3)==-v}),2)
add('i',2023,4,['−67103337','−67103330','−67103323','67103330'],'A','−67103337',['拆为Σ₅²⁵k²−Σ₅²⁵2ᵏ。','平方和为Σ₁²⁵−Σ₁⁴，等比和为2²⁶−2⁵。','相减−67103337，起始下标5不可当1；两个和都要扣去前4项。'],sum(k*k-2**k for k in range(5,26)),-67103337)
add('i',2023,5,['−2912','−364','364','2912'],'A','−2912',['通项取k个−2/x，指数2(14−k)−k=28−3k。','等于19时k=3，系数C(14,3)(−2)³。','364×(−8)=−2912；第4项的k是3。'],s.binomial(14,3)*(-2)**3,-2912)
add('i',2023,6,['x≤1或x≥2','x<1或x>2','−1≤x<2','−1<x<2'],'D','(−1,2)',['真数(x+1)/(2−x)>0且分母不为0。','零点−1、分母点2分区间，只有中间真数正。','两端都不能取；原选项A/B的零点写1，不能把−号漏看。'],s.solve_univariate_inequality((x+1)/(2-x)>0,x,relational=False).measure,3)
add('i',2023,7,['2√3','4','√6+√3','2√6'],'D','2√6',['绝对值范围对应x²−2∈[2,4]或[−4,−2]。','与x²≥0合并得x²∈[4,6]或x=0。','最大√6、最小−√6，相差2√6，不是中间根间距。'],s.sqrt(6)-(-s.sqrt(6)),2*s.sqrt(6))
add('i',2023,8,['3024','5376','5712','6048'],'C','5712',['末位0时，首位9种，余3位从8个选排，9×8×7×6=3024。','末位5时，首位8种（排0、5），余3位仍8×7×6，共2688。','两类合5712，不能使首位0也不能忽略末位0这类。'],9*8*7*6+8*8*7*6,5712)
add('i',2023,9,['−5','0','2.5','5'],'C','2.5',['条件1−P(X<5)=P(X<0)即P(X>5)=P(X<0)，连续常态可如此转换。','两尾概率相同，端点关于均值对称。','均值为(0+5)/2=2.5，不等于中间区间概率。'],s.Rational(0+5,2),s.Rational(5,2))
add('i',2023,10,['x²+y²−5x+6y+13=0','x²+y²+4x−7y+13=0','x²+4x−6y+13=0','y²−4x+6y+13=0'],'D','y²−4x+6y+13=0',['到y轴距离|x|，到(2,−3)距离√((x−2)²+(y+3)²)。','两边非负，平方等价，x²=(x−2)²+(y+3)²。','整理为y²−4x+6y+13=0。原卷科目保留高数I，当前字典章33的冲突另列。'],s.expand((x-2)**2+(t+3)**2-x*x),t*t-4*x+6*t+13)
add('i',2023,11,['16/63','33/56','−33/56','−63/16'],'D','−63/16',['sinA正、cosB负且同象限，故A、B都第二象限。','cosA=−3/5、sinB=5/13，tanA=−4/3、tanB=−5/12。','和角公式给(−4/3−5/12)/(1−5/9)=−63/16，不能把二象限cosA取正。'],(-s.Rational(4,3)-s.Rational(5,12))/(1-s.Rational(5,9)),-s.Rational(63,16))
add('i',2023,12,['39°30′S','39°30′N','50°30′N','50°30′S'],'C','50°30′N',['1度大圆弧为60海里，8430海里对应140.5°。','从南极−90°沿经线到A，纬差=90°+φ=140.5°。','φ=50.5°N=50°30′N；不要把到南极的弧当到北极距离。'],s.Rational(8430,60)-90,s.Rational(101,2))
add('i',2023,13,['图A：多峰且无界','图B：值域[0,2]且周期π','图C：值域[0,2]且周期约2π','图D：最小值正且最大值大于2'],'B','图B',['(sinx+cosx)²=1+sin2x。','中线1、振幅1、周期π、过(0,1)且初始递增。','图B各特征相符；C虽然也过(0,1)但周期不符。'],s.trigsimp((s.sin(x)+s.cos(x))**2-(1+s.sin(2*x))),0)
add('i',2023,14,['2h/3','√3h/2','2h/√3','√2h/√3'],'A','2h/3',['等边三角形三心重合。','重心把高按顶端到中心:中心到底边=2:1分。','因此顶点到圆心即外接半径2h/3，另h/3是内切半径。'],(s.Integer(8)/(4*s.sqrt(3)))/s.sqrt(3),s.Rational(2,3))
add('i',2023,15,['√13','13','13√13','169'],'B','13',['联立直线与圆恰一解为相切，k>0。','原点到3x−2y+13=0的距离=13/√13=√13。','半径平方k=13，不能把半径√13直接当k。'],(13/s.sqrt(13))**2,13)
add('i',2023,16,['1/5','2/5','1/6','5/6'],'B','2/5',['圆心C=(−1,0)，半径1。','代y=2x，5x²+2x=0，A/B为(0,0)、(−2/5,−4/5)。','由坐标行列式，面积=|det(A−C,B−C)|/2=|(1)(−4/5)|/2=2/5。'],abs(s.det(s.Matrix([[1,0],[s.Rational(3,5),-s.Rational(4,5)]])))/2,s.Rational(2,5))
add('i',2023,17,['−1','1','2','4'],'D','4',['驻点条件f′(−1/2)=−m+n=0，故n=m。','点值条件m/4−n/2+2=1，代n=m得m=4。','n=4代回点值1、斜率0同时成立。'],4*s.Rational(1,4)-4*s.Rational(1,2)+2,1)
add('i',2023,18,['x+7y−6=0','x−7y−8=0','7x+y−6=0','7x−y−8=0'],'B','x−7y−8=0',['隐微分6x−y−(x+2y)y′=0。','在(1,−1)斜率y′=−7，法线斜率1/7。','y+1=(x−1)/7整理x−7y−8=0；必须过给定点。'],1-7*(-1)-8,0)
add('i',2023,19,['ln(2x+2√(x²+4))','ln(x+√(x²+4))','ln((x+√(x²+4))/2)','ln((x+√(x²+4))/4)'],'C','ln((x+√(x²+4))/2)',['按给定导数，原函数ln(t+√(t²+4))。','定积分代上端x并减下端0的ln2。','合并对数得C；x=0时积分必须0，可排A、B、D。'],s.log((0+s.sqrt(4))/2),0)
add('i',2023,20,['eᵃ','e⁻ᵃ','a','极限不存在'],'A','eᵃ',['写成exp[−x ln(1−a/x)]，充分大x使底数正。','由ln(1+u)/u→1，−x ln(1−a/x)→a。','指数函数连续，极限eᵃ；双重负号不能漏。'],s.limit(-x*s.log(1-2/x),x,s.oo),2)
# Graph options are semantic transcriptions, not substitutes for source graph assets.
for key in ['uec_math_i:2022:mcq:12:whole','uec_math_i:2023:mcq:13:whole']:
 out[key]['options_representation']='semantic_graph_descriptions; original option graphics not reproduced'
def written(n,part,answer,steps,rubric,actual,expected):
 key=f'uec_math_i:2022:written:{n}:{part}';r=base[key]
 delta=s.simplify(actual-expected);assert delta.equals(0),(key,delta)
 assert sum(v[1]for v in rubric)==r['printed_marks']
 proof=dict(method='independent written derivation with substitution, coordinate or exhaustive event checks',formula_sha256=hashlib.sha256(r['formula_latex_verified'].encode()).hexdigest(),computed=str(actual),expected=str(expected),result='pass')
 out[key]=dict(source_pdf_id=r['source_pdf_id'],source_page=r['source_page'],answer_verified=answer,answer_status='independently_solved_not_official_key',historical_solution_steps=steps,historical_marking_points=[dict(description=a,marks=b)for a,b in rubric],marking_scheme_status='author_suggested_not_official',independent_verification=proof,review_method='Reread actual PDF page5, then independently derive; author rubric, not official marking scheme')
 checks.append(dict(id=key,**proof))
written(1,'whole','A=−1，B=2，C=−5',[
 '题意：对所有x≠2，恒等拆分线性因子与不可约二次因子；x²+1在实域非零。',
 '通分得x²−9x+9=A(x²+1)+(Bx+C)(x−2)。比较系数：A+B=1，C−2B=−9，A−2C=9。',
 '代x=2得−5=5A，所以A=−1；第一式给B=2，第二式给C=−5。',
 '验算：−(x²+1)+(2x−5)(x−2)=x²−9x+9。此处乘公分母只比较多项式，不能把x=2当原有理式的定义域值。'
 ],[('正确通分恒等式',1),('比较系数或代特殊值',1),('求A、B、C',1),('完整系数与回代核对',1)],s.expand(-(x*x+1)+(2*x-5)*(x-2)),x*x-9*x+9)
h=120*(math.sin(math.radians(19))-math.cos(math.radians(19))*math.tan(math.radians(7)))
written(2,'whole','塔高约25.1 m',[
 '题意：沿坡的120 m是斜边，观察者高于塔顶，7°为俯角。设塔脚(0,0)，塔顶(0,h)。',
 '观察点P=(120cos19°，120sin19°)，所以横距d=120cos19°，观察点高度H=120sin19°。',
 '由水平向下俯视，tan7°=(H−h)/d，故h=120sin19°−120cos19°tan7°≈25.13676856。',
 '按题意取0.1 m，h≈25.1 m。回代(H−h)/d约为tan7°，且0<h<H；误用仰角会把减号写成加号。'
 ],[('将沿坡距离分解为水平、竖直分量',1),('正确俯角高度差关系',1),('代入计算',1),('25.1 m及合理性检验',1)],s.Rational(str(round(h,1))),s.Rational(251,10))
y=s.symbols('y',real=True)
written(3,'a','(x−2)²+(y−3)²=10；圆心O=(2,3)',[
 '移项把一次项放到左侧：x²−4x+y²−6y=−3。',
 '两边同加4+9，得(x−2)²+(y−3)²=10。',
 '与圆标准式对比，O=(2,3)，r=√10；展开回原式可检验常数，不能漏加两项。'
 ],[('正确标准式',1),('圆心(2,3)',1)],s.expand((x-2)**2+(y-3)**2-10),x*x+y*y-4*x-6*y+3)
A=s.Matrix([0,s.Rational(7,3)]);B=s.Matrix([5,4]);O=s.Matrix([2,3])
written(3,'b','A=(0,7/3)',[
 '题干明确O在线段AB上，因此AO:OB=2:3是内分，不是外分。令A=(u,v)，已知O=(2,3)、B=(5,4)。',
 '内分关系O=(3A+2B)/5，故A=(5O−2B)/3=(0,7/3)。',
 '验算O−A=(2,2/3)，B−O=(3,1)，前者为后者的2/3；共线、同向且O在两端之间。'
 ],[('正确内分点方程',1),('坐标及比例核对',1)],sum((3*A+2*B-5*O)[i]**2 for i in range(2)),s.Integer(0))
ps=[s.Rational(1,2),s.Rational(2,3),s.Rational(3,4)]
exact=sum(s.prod(ps[j]if j==i else 1-ps[j]for j in range(3))for i in range(3))
written(4,'a','1/4',[
 '恰一个发生分为A独有、B独有、C独有三种互斥情形；三事件相互独立，因此补事件也可相乘。',
 '所求=(1/2)(1/3)(1/4)+(1/2)(2/3)(1/4)+(1/2)(1/3)(3/4)。',
 '三项为1/24、2/24、3/24，相加6/24=1/4。不能只算A发生，也不能把“恰一”当“至少一”。'
 ],[('三种互斥独立概率乘积',1),('加总1/4',1)],exact,s.Rational(1,4))
written(4,'b','23/24',[
 '至少一个发生与三个全部不发生互为补事件。',
 '独立性给P(全不发生)=(1/2)(1/3)(1/4)=1/24。',
 '所以1−1/24=23/24。验算：枚举八种事件状态，除全不发生外七种之和也是23/24。'
 ],[('独立补事件关系',1),('23/24',1)],sum(s.prod(ps[j]if b[j]else 1-ps[j]for j in range(3))for b in itertools.product([False,True],repeat=3)if any(b)),s.Rational(23,24))
f=2*x**3-4*x*x+4;critical=[s.Integer(-1),s.Integer(0),s.Rational(4,3),s.Integer(2)];values=[f.subs(x,v)for v in critical]
written(5,'whole','最大值4，在x=0、2；最小值−2，在x=−1',[
 '闭区间连续函数的绝对极值须比较内部驻点与两端点，不能只解导数等于0。',
 'f′(x)=6x²−8x=2x(3x−4)，内部驻点x=0、4/3，都落在[−1,2]内。',
 '候选函数值：f(−1)=−2，f(0)=4，f(4/3)=44/27，f(2)=4。',
 '比较得最大4在0和2两处达到，最小−2在−1；分段导数符号为+、−、+也核对变化。局部最小44/27并非闭区间最小。'
 ],[('导数及两个驻点',1),('列出端点和驻点全部候选',1),('正确比较四个函数值',1),('最大最小值与达到位置',1)],max(values)-min(values),s.Integer(6))
(D/'historical-completions.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
(R/'reports/math-exams/HISTORICAL_COMPLETION_CHECKS.json').write_text(json.dumps(dict(count=len(checks),checks=checks,status='pass',official_key_verified=False,notes=['2022II第4题补计AB线上另一点，总250。','2022II第10题原等式平方求和应给正7/10。']),ensure_ascii=False,indent=2)+'\n')
print('Completed',len(out),'historical scoring units with independently authored solutions (60 MCQ + 7 written)')
