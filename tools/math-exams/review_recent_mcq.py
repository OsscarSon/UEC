"""Three recent MCQ papers read directly from private rendered source pages.

PDF page numbers below refer to supplied files, not printed page numbers.
No answer is promoted merely because it occurs in an uploaded report.
"""
import review_support as S
from review_support import *
S.Y=2025
exam('uec_math_i','2025高级数学(I)SC06试卷一.pdf')
mc(1,2,3,r'p(x)=(x^2+3x-2)(2x-1)+3x+1;\ p(1/2)','商余式代值',r'-5/3|-1/2|0|5/2','D')
mc(2,2,2,r'4/3,-5/2\text{为}\alpha x^2+\beta x-10=0\text{两根};\alpha+\beta','韦达与系数',r'-7/6|-1/2|13/2|13','C')
mc(3,2,13,r'S_\infty:S_3=64:63,\ a=12;\ ar^2','无穷等比级数',r'-27/4|-3/4|3/4|27/4','C')
mc(4,2,13,r'\sum_{k=1}^{50}(3k+1)^2','平方和展开',r'74000|202775|206550|394025','D')
mc(5,2,5,r'g(x)=1/x+3,\ x\ne0;\ g^{-1}(x)=x','反函数不动点',r'1|0\text{或}1|(3\pm\sqrt5)/2|(3\pm\sqrt{13})/2','D')
mc(6,2,14,r'\det\begin{pmatrix}a&b&c\\d&e&f\\g&h&i\end{pmatrix}=5;\ \det\begin{pmatrix}d&-e&f\\2g&-2h&2i\\a&-b&c\end{pmatrix}','行列式循环换行与倍乘',r'-40|-10|10|40','B')
mc(7,2,12,r'\log_7a=1/\log_{121}49','对数换底',r'0<a<10|10<a<20|20<a<100|100<a<1000','B')
mc(8,3,18,r'P,Q\text{在赤道，最短距离3645海里，P东经}30^\circ20\prime','经度与海里',r'\text{东经}90^\circ5\prime|\text{东经}60^\circ45\prime|\text{西经}30^\circ25\prime|\text{西经}91^\circ5\prime','C')
mc(9,3,9,r'a,b>0,\ \sin20^\circ=a/b;\tan160^\circ','象限与同角关系',r'a/\sqrt{a^2+b^2}|-b/\sqrt{a^2+b^2}|-b/\sqrt{a^2-b^2}|-a/\sqrt{b^2-a^2}','D')
mc(10,3,10,r'AB:AC=1:\sqrt5,\cos A=1/(2\sqrt5),\text{周长}=19;\ AB','余弦定律与周长',r'2\sqrt5-1|2\sqrt5+1|19/(2\sqrt5)|\sqrt{19}','A')
mc(11,3,11,r'\sin2x=0,\ -3\pi\le x\le3\pi;\text{解数}','周期与端点计数',r'6|7|12|13','D')
mc(12,3,16,r'3x+4y+k=0\text{与}x^2+y^2+4x-6y-12=0\text{相切}','圆心到直线距离',r'-31\text{或}-19|31\text{或}-19|-31\text{或}19|31\text{或}19','C')
mc(13,3,1,r'(3,0),(3,5),(0,-4),(x,0)\text{构成面积36的凸四边形}','面积与凸性筛根',r'-5\text{或}-11|5\text{或}-11|-5|-5\text{或}11','C',note='必须保留凸四边形条件；x=11时(3,0)在另外三点的三角形内部，不能只按面积绝对值保留。')
mc(14,3,1,r'x+2y=5,\ x+2y=-3;\text{距离}','平行线距离',r'8|2|8/\sqrt3|8/\sqrt5','D')
mc(15,4,26,r'X=500\text{或}-150,\ E(X)=32;\ P(X=500)','二点分布期望',r'.06|.28|.34|.52','B')
mc(16,4,19,r'\text{watermelon全部字母排列，两个e必须分开}','重复排列扣除相邻',r'141120|1451520|1814400|16329600','B')
mc(17,4,28,r'f(x)=1/x;\ f^{(10)}(x)','高阶导数',r'10!/x^{11}|-10!/x^{10}|10!/x^{10}|11!/x^{11}','A')
mc(18,4,28,r'x^3-xy+y^2=3,\ (x,y)=(1,2);\ dy/dx','隐函数导数',r'-1/3|-5/3|-13/5|-1','A')
mc(19,4,24,r'\int_0^{\pi/4}\sin^2x\,dx','降幂定积分',r'\pi/8-1/4|\pi/8|\pi/4-1/2|\pi/4','A')
mc(20,4,24,r'\int_0^1 f(x)dx=3\pi;\ \int_0^{1/\pi}f(\pi x)dx','定积分线性换元',r'3/\pi|3|3\pi|3\pi^2','B')
(O/'visual-review-2025-ueci-mcq.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
rows.clear();S.Y=2024
exam('uec_math_ii','2024 高数2 试卷一.pdf')
mc(1,1,7,r'\neg(x^2=9)','命题否定',r'x\ne-3\text{或}x=3|x=-3\text{且}x\ne3|x\ne-3\text{或}x\ne3|x\ne-3\text{且}x\ne3','D')
mc(2,1,4,r'\sum_{k=1}^n\frac1{\sqrt{2k-1}+\sqrt{2k+1}}','有理化裂项',r'(1+\sqrt{2n+1})/2|\sqrt{2n-1}/2|(1-\sqrt{2n-1})/2|(\sqrt{2n+1}-1)/2','D',secondary=[13])
mc(3,1,13,r'0<r<1;\ \sum_{k=1}^{\infty}r^k\sin(k\pi/2)','交错子列等比和',r'1/(1+r^2)|r/(1+r^2)|1/(1-r^2)|r/(1-r^2)','B')
mc(4,1,3,r'f(x)=x^{200},\ g(x)=x^2-1;\ f\text{除以}g\text{的余式}','多项式余式',r'-1|1|100x-1|100x+1','B')
mc(5,1,34,r'z=\cos(2\pi/7)+i\sin(2\pi/7);\ z+z^2+\cdots+z^7','单位根求和',r'0|1|\cos(2\pi/7)+i\sin(2\pi/7)|\cos(4\pi/7)+i\sin(4\pi/7)','A')
mc(6,1,3,r'a,b,c\text{为}2x^3-2x^2+x-3=0\text{三根};\ (a+b+c)(ab+bc+ca)','三次韦达',r'-2|-1/2|1/2|2','C')
mc(7,1,19,r'1,2,3,4\text{构成无重复四位数；全部数之和}','数位对称计数',r'24|55550|66660|99990','C')
mc(8,1,17,r'|a|=2|b|,\ |a-2b|=\sqrt2|a|;\angle(a,b)','向量模平方',r'120^\circ|90^\circ|60^\circ|0^\circ','B')
mc(9,2,10,r'\text{等边三角形内切圆半径}r\text{与外接圆半径}R;\ r:R','等边三角形圆半径',r'1:2|1:\sqrt2|1:\sqrt3|\sqrt3:2','A')
mc(10,2,9,r'\sin^{-1}\alpha+\cos^{-1}\beta+\tan^{-1}\gamma=\pi/4;\ \sin^{-1}(-\alpha)+\cos^{-1}(-\beta)+\tan^{-1}(-\gamma)','反三角主值对称',r'-3\pi/4|-\pi/4|\pi/4|3\pi/4','D')
mc(11,2,10,r'\sin(A+B):\sin(B+C):\sin(A+C)=7:8:13;\ a:b:c','三角内角与正弦定律',r'7:8:13|7:13:8|8:13:7|13:8:7','C')
mc(12,2,33,r'\text{右开口抛物线，焦点F；候选竖直线A,B,C,D，识别准线}','焦准对称几何',r'A|B|C|D','C',figure='图中L为水平对称轴；F在顶点右侧，准线在左侧且到顶点距离等于焦距，对应C；不能把L当准线。')
mc(13,2,16,r'A=(-2,0),B=(6,6),\ \angle APB=90^\circ;\text{轨迹}','直径圆轨迹',r'x^2+y^2-4x-6y-87=0|x^2+y^2-4x+6y-87=0|x^2+y^2-4x-6y-12=0|x^2+y^2-4x+6y-12=0','C',note='轨迹的完整集合还排除A、B本身，因端点处角未定义；选择的是所在圆方程。')
mc(14,2,32,r'x=3\sin\theta+4\cos\theta,\ y=4\sin\theta-3\cos\theta,\ 0\le\theta\le2\pi','参数轨迹消参',r'\text{圆}|\text{椭圆}|\text{双曲线}|\text{抛物线}','A')
mc(15,3,32,r'A=(1,7)\mapsto A\prime=(2,-5);\ y^2=x^2+1\text{平移坐标轴后}','坐标平移',r'(y\prime+12)^2=(x\prime-1)^2+1|(y\prime-12)^2=(x\prime-1)^2+1|(y\prime+12)^2=(x\prime+1)^2+1|(y\prime-12)^2=(x\prime+1)^2+1','A')
mc(16,3,22,r'y=x^3-3x^2+3x;\text{极值点数}','驻点不等于极值',r'0|1|2|3','A')
mc(17,3,21,r'\lim_{x\to\infty}\ln(1+5x)/x','对数增长极限',r'-\infty|0|1/5|\infty','B')
mc(18,3,28,r'\left.\frac d{dx}\frac{(x+1)^3}{(2x-1)^4(x+2)}\right|_{x=2}','对数求导与乘除',r'-23/144|-5/144|1/144|7/144','A')
mc(19,3,24,r'y=xe^{-x},\ x\in[0,1];\text{与x轴面积}','分部积分面积',r'2/e|1-2/e|1/e|1-1/e','B')
mc(20,3,24,r'r^2=\sqrt3\sin2\theta;\text{第一象限一瓣面积}','极坐标面积',r'\sqrt3|\sqrt3/4|\sqrt3/3|\sqrt3/2','D',secondary=[32],figure='图1双纽线第一象限一瓣涂阴影；第三象限另一瓣不计，积分界0至π/2。')
# This supplied PDF starts at printed p5 and has no cover. The 2-mark
# allocation is inferred from its paired, visually read P2 cover's 40%
# MCQ weighting and the twenty actual questions; distinguish that inference.
for r in rows:
 r['inferred_marks']=r['printed_marks'];r['printed_marks']=None
 r['evidence_fields']['marks']='paired_cover_40_percent_and_20_questions_inference'
 r['evidence_fields']['year']='paired_filename_and_written_cover_not_missing_mcq_cover'
 r['notes']+=' 所供选择卷缺封面；年份按配对文件、2分按配对40%与20题推定，不冒充本页明印分值。'
(O/'visual-review-2024-uecii-mcq.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
rows.clear();S.Y=2025
exam('uec_math_ii','2025 高数2 试卷一.pdf')
mc(1,5,34,r'\sum_{k=1}^{50}(-i)^k','虚数幂周期',r'1-i|-1-i|1+i|-1+i','B')
mc(2,5,7,r'(\neg p)\land(\neg q)','德摩根律',r'p\lor q|p\land q|\neg(p\lor q)|\neg(p\land q)','C')
mc(3,5,17,r'a=(1,3),b=(-1,2),c=(1,1),\ (ma-nb)\perp c','向量垂直参数',r'm=-1,n=2|m=2,n=-1/2|m=1,n=1/4|m=-3/2,n=-6','D')
mc(4,5,12,r'x^{\log_2x}=8x^2;\text{全部根的积}','对数换元方程',r'1/4|1|2|4','D')
mc(5,5,19,r'|A|=6,|B|=10,\ f:A\to B\text{单射};\text{映射数}','单射排列计数',r'6^{10}|10^6|\binom{10}6|{}^{10}P_6','D',secondary=[5])
mc(6,5,4,r'\sqrt{|x|}=x;\text{实根数}','根式方程符号约束',r'1|2|3|4','B')
mc(7,5,5,r'\text{判断奇函数}','函数奇偶与定义域',r'e^x/(1-e^{2x})|e^{2x}/(1-e^x)|e^x/(1-e^x)|e^{2x}/(1-e^{2x})','A')
mc(8,5,10,r'A\text{在楼西方，仰角}\alpha;\ A\text{向南走}d\text{米，仰角}\beta;\text{楼高}','二维水平位移与仰角',r'd/\sqrt{\cot^2\beta-\cot^2\alpha}|d/\sqrt{\cot^2\alpha-\cot^2\beta}|d/\sqrt{\tan^2\beta-\tan^2\alpha}|d/\sqrt{\tan^2\alpha-\tan^2\beta}','A')
mc(9,6,10,r'\text{凸四边形}ABCD:\ AB=4,BC=3,CD=7,DA=6,AC=3;\text{面积}','对角线拆分海伦面积',r'8\sqrt2|7\sqrt3|6\sqrt5|5\sqrt7','C')
mc(10,6,11,r'\sin\theta\cos\theta\cos2\theta\cdots\cos(2^n\theta)','倍角连乘',r'2^{-n-1}\sin(2^{n+1}\theta)|2^{-n}\sin(2^{n+1}\theta)|(1/2)\sin(2^{n+1}\theta)|(1/2)\sin(2^n\theta)','A')
mc(11,6,9,r'\text{I:对所有}x\in(-\pi/2,\pi/2),\sin(\sin^{-1}x)=x;\ \text{II:}x\in[-1,1],\sin^{-1}(\sin x)=x;\ \text{III:}x\in[0,\pi],\cos^{-1}(\cos x)=x','反三角定义域与主值',r'0|1|2|3','C',note='I的量词区间含|x|>1，反正弦未定义，不能只套互逆关系；II、III正确。')
mc(12,6,32,r'(-\sqrt3,-1)\text{的极坐标}','极坐标象限',r'(2,-\pi/6)|(2,\pi/6)|(2,5\pi/6)|(2,7\pi/6)','D')
mc(13,6,1,r'P=(-1+r\cos(\pi/6),2+r\sin(\pi/6)),\ r\in\mathbb R;\text{轨迹}','参数直线消参',r'x-\sqrt3y+2\sqrt3+1=0|y-2=(\sqrt3/2)(x+1)|(x+1)^2/2+(y-2)^2/\sqrt3=1|(y-2)^2=(\sqrt3/2)(x+1)','A')
mc(14,7,33,r'F_1=(0,-2),F_2=(0,2),\ x^2/a^2+y^2/b^2=1;\text{I }a>b;\text{II不能唯一确定椭圆; III焦距和4}','椭圆焦点与参数自由度',r'\mathrm{I}|\mathrm{II}|\mathrm{I,II}|\mathrm{II,III}','B')
mc(15,7,32,r'f(x,y)=0;\text{新原点位于原坐标}(-2,5);\text{新方程}','坐标系平移',r'f(x\prime-2,y\prime+5)=0|f(x\prime+2,y\prime-5)=0|f(-x\prime-2,-y\prime+5)=0|f(-x\prime+2,-y\prime-5)=0','A')
mc(16,7,21,r'\lim_{n\to\infty}\frac1{n^2}\sum_{k=1}^n(2k+1)','和式极限',r'\text{不存在}|0|1|2','C')
mc(17,7,28,r'f(x)=x^{\sin x},\ x>0;\ f\prime(\pi)','变指数对数求导',r'\ln\pi|-\ln\pi|0|1','B')
mc(18,7,30,r'y(t)=te^t;\text{满足哪一微分方程}','代入验证微分方程',r'y\prime\prime+y\prime=0|y\prime\prime-2y\prime=e^t|y\prime\prime+y=e^t|y\prime\prime-y\prime=e^t','D')
mc(19,7,24,r'y=4-x^2\text{与x轴区域绕y轴转}180^\circ;\text{体积}','半转双侧区域重叠',r'4\pi|6\pi|8\pi|64\pi/3','C',figure='原卷无图；区域左右两半同时旋转180°后覆盖完整圆盘截面，不能把完整旋转体积机械除二。')
mc(20,7,24,r't>1;\ \int_1^t\ln x\,dx','分部定积分',r't\ln t|t\ln t-t|t\ln t-(t-1)|t\ln t-(t+1)','C')
(O/'visual-review-2025-uecii-mcq.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('Read and recorded 60 recent UEC MCQ units; 2024 missing-cover inference explicit.')
