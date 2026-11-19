"""2024 I supplied six-page scan: both covers absent, question fields read."""
import review_support as S
from review_support import *
S.Y=2024
exam('uec_math_i','2024 高级数学 I.pdf')
mc(1,1,2,r'4x^2+9=8x+m\text{无实根};\ m','二次判别式',r'm<5|m>5|m<64|m>64',None)
mc(2,1,3,r'(x^2-x-2)\mid(2x^3-9x^2+px+q);\ p-q','因式定理联立',r'-11|-7|0|7',None)
mc(3,1,5,r'f(x)=\begin{cases}x+1,&x\le2\\1,&x>2\end{cases};\ f^5(0)','分段函数复合',r'0|1|2|3',None)
mc(4,1,5,r'f(x)=2\sqrt{x-1}+4,\ x\ge1;\text{值域}', '根式函数值域',r'y\ge4|y\ge1|y\ge6|\mathbb R',None)
mc(5,1,15,r'\begin{pmatrix}1&x&x^2\\0&1&x\\4&2&1\end{pmatrix}\text{不可逆};\ x','矩阵可逆条件',r'1/2\text{或}-1/2|-1/2|1/2|-1\text{或}0',None)
mc(6,1,20,r'(x^3-1/x)^{100}\text{不出现哪项}','二项指数整数约束',r'x^{-88}|\text{常数项}|x^{236}|x^{239}',None)
mc(7,1,13,r'a_1=5\text{的无穷等比级数和不可能落在哪区间}','收敛和范围',r'[-5,5]|(-\infty,5/2]|(-\infty,5]|[5,\infty)',None)
mc(8,1,25,r'n\text{人原均分}m;\ 10\text{人各增2分，其余各减2分；新均分}','加权总分变换',r'm-2+20/n|m-2+40/n|m+2-20/n|m+2-40/n',None)
mc(9,2,26,r'A\text{袋4红2蓝3青，B袋3红3蓝2青；等概率选袋再选球}','全概率与样本空间',r'31/40|29/72|59/144|7/17',None)
mc(10,2,1,r'2x+y=5,\ x-y=6;\text{锐夹角}','两直线夹角',r'18.43^\circ|45^\circ|56.31^\circ|71.57^\circ',None)
mc(11,2,18,r'A(30^\circ N,110^\circ W),B(30^\circ N,70^\circ E);\text{大圆最短海里距离}','大圆与对跖经线',r'9353|7200|6235|3600',None)
mc(12,2,10,r'\text{三角形边长}2,3,4;\text{最大角}','余弦定律',r'75.52^\circ|90^\circ|104.48^\circ|105.42^\circ',None)
mc(13,2,11,r'\tan(\alpha+\beta)=-11/2,\tan(\alpha-\beta)=2;\tan2\alpha','和角公式',r'-15/2|3/4|-3/4|-7/24',None)
mc(14,2,11,r'2\sin^2x-2\cos^2x=1,\ x\in[-\pi,\pi];\text{解数}','倍角方程区间',r'2|4|5|6',None)
mc(15,2,1,r'(x_0,y_0)\text{到}x=-x_0\text{距离}','距离非负',r'2x_0|-2x_0|-2|x_0|||-2x_0|',None)
# Literal vertical bars in the last option need an explicit four-element map.
rows[-1]['options_verified']={'A':'2x_0','B':'-2x_0','C':'-2|x_0|','D':'|-2x_0|'}
mc(16,3,16,r'2x^2+2y^2-3x+4y=0;\text{半径}','配方前先标准化',r'5/2|5/4|25/8|5/(2\sqrt2)',None)
mc(17,3,21,r'\lim_{x\to\pi}\frac{\sin(x/2)}{x/2}','连续点极限',r'0|2/\pi|\pi/2|1',None)
mc(18,3,24,r'f(x)=x^2+\sqrt{x+1};\int_0^3f\prime(x)dx','微积分基本定理',r'10|11|41/3|43/3',None)
mc(19,3,22,r'y=e^{4x}+\ln2;\ y\prime\prime-2y\prime','指数二阶导数',r'8e^{4x}-1|-e^{4x}-\ln2|8e^{4x}|16e^{4x}',None)
mc(20,3,24,r'R:\ 0\le x\le2,\ 0\le y\le x^2;\ x=k\text{平分面积}','定积分平分区域',r'1|\sqrt[3]2|\sqrt[3]3|\sqrt[3]4',None,figure='图1第一象限抛物线下、x轴上、x=2左侧的区域；x=k竖线平分面积，不是平分横轴长度。')
for r in rows:
 r['inferred_marks']=2;r['printed_marks']=None;r['evidence_fields']['marks']='missing_mcq_cover_not_confirmed'
wr(1,'a',4,1,5,r'f(x)=1-2/(2x-1);\text{定义域}','分母排除')
wr(1,'b',4,1,5,r'f(x)=1-2/(2x-1);\ f(2x)','函数输入代换')
wr(1,'c',4,2,5,r'f(x)=1-2/(2x-1);\ f^{-1}(x)','反函数与值域')
wr(2,'whole',4,4,8,r'\angle APB=60^\circ;\text{圆心O、半径2的内切圆在圆心P扇形PQR内；阴影面积}','扇形内切圆复合面积',figure='图1A、B为圆与PA、PB切点，O在角平分线上，圆同时内切弧QR；阴影在切线PA/PB、弧QR与圆右侧长弧AB之间，两块阴影，不包含靠P的空白三角弓区。')
wr(3,'whole',4,4,1,r'A=(1,0),B=(3,-3),\ P\in AB,\ AP:PB=1:2,\ P\in\{y=mx\};\ m','内分点与过原点直线')
wr(4,'whole',4,4,26,r'X\sim N(\mu,\sigma^2),\ P(X>120)=.1151,\ P(X>95)=.9032;\mu,\sigma','常态反标准化')
wr(5,'whole',4,4,22,r'f(x)=4x^3-3x^2-6x+1;\text{增减区间}','一阶导数符号')
wr(6,'a',5,4,12,r'\log_5x-6\log_x5=1','换底与对数方程')
wr(6,'b(i)',5,4,2,r'y=mx-4\text{与}y=4x^2\text{有两个交点};\ m<-8\text{或}m>8','直线抛物线相交判别式')
wr(6,'b(ii)',5,2,2,r'P=(x_1,y_1),Q=(x_2,y_2)\text{为上述两交点};\ m=4x_1+4x_2','韦达证明')
wr(7,'a',5,4,6,r'x+y>2,\ 2x-y\le4,\ x-2y\ge-4;\text{画区域及离原点最远点}','线性约束与几何最值',figure='第一边界x+y=2严格不包含，另两条包含；需按约束交集定位顶点。')
V=r'a=(2,-3),b=(0,4),c=(8,5),d=(2,k)'
wr(7,'b(i)',5,4,17,V+r';\ ma+nb\text{是与c平行的单位向量}','平行单位向量正负分支')
wr(7,'b(ii)',5,2,17,V+r';\ a\perp d;\ k','向量点积')
fig='图2长方体底面ABCD，顶面EFGH，AB=8,BC=6,CG=4；考察三角形BGD，公共底面对角线BD。'
wr(8,'a(i)',5,4,18,r'AB=8,BC=6,CG=4;\ [\triangle BGD]','空间三角形面积',figure=fig)
wr(8,'a(ii)',5,3,18,r'AB=8,BC=6,CG=4;\angle(BGD,ABCD)','二面角',figure=fig)
wr(8,'b',5,3,11,r'\sin^4x+\cos^4x=1-(1/2)\sin^22x','三角恒等证明')
boat=r'16\text{人中8仅右排、7仅左排、1两排均可；选12人分左右各6}'
wr(9,'a(i)',5,4,19,boat+r';\text{选法数}','分情况选人')
wr(9,'a(ii)',5,2,19,boat+r';\text{座位安排数}','选人与排列两阶段')
wr(9,'b',5,4,26,r'\text{公平硬币投掷3次，求正面数期望}','二项期望')
wr(10,'a',6,3,1,r'A=(-1,2),B=(0,4);\text{垂直平分线}l:\ 2x+4y=11','中点与法向证明')
wr(10,'b',6,4,1,r'C\in l:\ 2x+4y=11,\ [\triangle ABC]=10;\ C','直线点与面积绝对值')
wr(10,'c',6,3,16,r'\text{圆心}A=(-1,2),\text{切线}2x+4y=11;\text{圆标准式}','点线距离求半径')
wr(11,'a(i)',6,1,29,r'(x^2+8x+9)/(x^2+3x+2)=1+3/(x+2)+A/(x+1);\ A','部分分式系数')
wr(11,'a(ii)',6,3,29,r'\int_0^1(x^2+8x+9)/(x^2+3x+2)dx','部分分式定积分')
wr(11,'b(i)',6,3,22,r'V=x^3;\ x:2\text{cm}\to2.01\text{cm};\ dV\text{近似}','微分近似单位')
wr(11,'b(ii)',6,3,22,r'V=x^3,\ dx/dt=2\text{cm/s},\ V=27\text{cm}^3;\ dV/dt','相关变化率单位')
wr(12,'a(i)',6,3,22,r'y=2e^{3x^2}+5;\text{驻点}','复合指数导数')
wr(12,'a(ii)',6,2,22,r'y=2e^{3x^2}+5;\text{判极大或极小}','驻点分类')
wr(12,'b',6,5,24,r'y=\sin2x\text{第一正瓣与x轴围域，绕x轴}360^\circ','三角曲线旋转体积',figure='图3从0到π/2的一整正瓣阴影；旋转半径sin2x，体积积分π∫sin²2x dx，不是积分sin2x。')
for r in rows:
 r['evidence_fields']['year']='source_filename_2024_without_printed_cover'
 r['notes']+=' 本扫描无两卷封面；年份依文件名，作答分值/选答规则读自题页，选择每题2分仅推定。'
(O/'visual-review-2024-ueci.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2)+'\n')
print('2024 I:',len(rows),'units; missing covers explicit, printed written90, MCQ marks unknown')
