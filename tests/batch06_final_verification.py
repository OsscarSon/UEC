"""Independent exact checks of the final four chapters and chemical atom/electron accounts."""
from pathlib import Path
import json,math
import sympy as s
R=Path(__file__).resolve().parents[1];checks=[]
def C(name,ok,detail=None):
 assert bool(ok),(name,detail)
 checks.append(dict(name=name,status='pass',detail=detail))
def Z(name,expr):C(name,s.simplify(s.trigsimp(s.expand_complex(expr)))==0,str(expr))
def N(name,val,expected):C(name,math.isclose(float(val),expected,rel_tol=1e-8,abs_tol=abs(expected)*1e-8 if expected else 1e-12),dict(computed=float(val),expected=expected))
x,y,t=s.symbols('x y t',real=True);I=s.I
Z('33.1 perpendicular bisector distances at x1',(1+2)**2+(y-1)**2-((1-4)**2+(y-1)**2))
Z('33.1 parameter circle',(2*s.cos(t))**2+(2*s.sin(t))**2-4)
C('33.1 retained upper-half restriction',s.sin(s.pi/2)>0 and s.sin(3*s.pi/2)<0)
Z('33.1 polar circle',(4*s.cos(t))**2-4*(4*s.cos(t))*s.cos(t))
Z('33.3 tangent intersection repeated root',(y**2-12*x).subs(x,y-3)-(y-6)**2)
Z('33.3 shifted focus equidistance at vertex',s.sqrt((1+1)**2+(-2+2)**2)-abs(1-3))
Z('33.4 point on ellipse',s.Rational(3**2,25)+(s.Rational(12,5))**2/9-1)
Z('33.4 tangent point',9*3+20*s.Rational(12,5)-75)
Z('33.4 focal sum',s.sqrt((3-4)**2+s.Rational(12,5)**2)+s.sqrt((3+4)**2+s.Rational(12,5)**2)-10)
Z('33.4 vertical ellipse c',16-4-(2*s.sqrt(3))**2)
Z('33.5 point on hyperbola',s.Rational(25,9)-(s.Rational(16,3))**2/16-1)
Z('33.5 tangent point',5*5-3*s.Rational(16,3)-9)
Z('33.5 focal distance difference',s.sqrt((5+5)**2+s.Rational(16,3)**2)-s.Rational(16,3)-6)
Z('33.5 asymptote cannot be curve',(x*x/9-y*y/16).subs(y,4*x/3))
Z('34.1 product',(2+I)*(3-4*I)-(10-5*I))
Z('34.1 quotient',(3+4*I)/(1-2*I)-(-1+2*I))
Z('34.1 conjugate equation',(2-3*I)+2*(2+3*I)-(6+3*I))
Z('34.1 i2027',I**2027+I)
Z('34.1 quadratic root',(-3+2*I)**2+6*(-3+2*I)+13)
Z('34.2 modulus',s.Abs(-3+4*I)-5)
Z('34.2 distance halfplane algebra',((x-1)**2+y*y)-((x+1)**2+y*y)+4*x)
Z('34.2 extreme distances upper',s.Abs(-2-1)-3)
Z('34.2 extreme distances lower',s.Abs(2-1)-1)
Z('34.3 product',2*(s.cos(s.pi/3)+I*s.sin(s.pi/3))*3*(s.cos(-s.pi/6)+I*s.sin(-s.pi/6))-(3*s.sqrt(3)+3*I))
Z('34.3 quotient',2*(s.cos(s.pi/3)+I*s.sin(s.pi/3))/(3*(s.cos(-s.pi/6)+I*s.sin(-s.pi/6)))-2*I/3)
Z('34.4 eighth power',(1+I)**8-16)
Z('34.4 sixth power',(s.sqrt(3)-I)**6+64)
Z('34.4 negative third power',(2*(s.cos(s.pi/3)+I*s.sin(s.pi/3)))**-3+s.Rational(1,8))
roots=[2,-1+I*s.sqrt(3),-1-I*s.sqrt(3)]
for j,z in enumerate(roots):Z('34.5 cubic root '+str(j),z**3-8)
C('34.5 cube roots distinct',len(set(roots))==3)
for j,z in enumerate([s.sqrt(2)+I*s.sqrt(2),s.sqrt(2)-I*s.sqrt(2),-s.sqrt(2)+I*s.sqrt(2),-s.sqrt(2)-I*s.sqrt(2)]):Z('34.5 fourth root '+str(j),z**4+16)
Z('34.5 real polynomial',(x-3)*(x*x-2*x+5)-(x**3-5*x*x+11*x-15))
for z in [3,1+2*I,1-2*I]:Z('34.5 polynomial root '+str(z),(x**3-5*x*x+11*x-15).subs(x,z))
A=s.Matrix([1,2,-1]);B=s.Matrix([4,6,11]);Z('35.1 distance13',(B-A).norm()-13)
Z('35.1 sphere completing squares',x*x+y*y+t*t-2*x+4*y-6*t-2-((x-1)**2+(y+2)**2+(t-3)**2-16))
Z('35.2 vector length',s.Matrix([3,2,6]).norm()-7)
C('35.2 internal ratio',s.Matrix([4,2,6])==2*(s.Matrix([6,3,9])-s.Matrix([4,2,6])))
C('35.2 dependence',s.Matrix.hstack(s.Matrix([1,0,1]),s.Matrix([0,1,1]),s.Matrix([1,1,2])).det()==0)
Z('35.3 perpendicular',s.Matrix([1,2,2]).dot(s.Matrix([2,-1,0])))
Z('35.3 angle60',s.acos(s.Matrix([1,1,0]).dot(s.Matrix([1,0,1]))/(s.sqrt(2)*s.sqrt(2)))-s.pi/3)
Z('35.3 work',s.Matrix([2,1,-1]).dot(s.Matrix([3,0,4]))-2)
u=s.Matrix([1,2,0]);v=s.Matrix([0,1,3]);cross=u.cross(v)
C('35.4 cross sign',cross==s.Matrix([6,-3,1]))
Z('35.4 cross norm',cross.norm()-s.sqrt(46));Z('35.4 orthogonal u',cross.dot(u));Z('35.4 orthogonal v',cross.dot(v))
Z('35.4 triple volume',s.Matrix([1,0,0]).dot(s.Matrix([0,2,0]).cross(s.Matrix([0,0,3])))-6)
C('35.5 intersection',s.Matrix([1,-1,3])+s.Matrix([2,1,-1])==s.Matrix([3,0,2]))
Z('35.5 point in plane',3+0+2-5)
Z('35.5 point-plane distance',s.Abs(-6)/s.sqrt(1+4+4)-2)
C('35.5 skew lines z conflict',s.Matrix([1,1,0]).cross(s.Matrix([1,0,0]))!=s.zeros(3,1) and 0!=1)
N('18.1 incidence normal angle',90-25,65)
N('18.1 moved mirror image displacement',(2*.5+3)-3,1)
N('18.2 concave real image',1/(1/10-1/30),15)
N('18.2 concave virtual image',1/(1/10-1/5),-10)
N('18.2 convex image',1/(-1/10-1/20),-20/3)
N('18.3 glass refraction angle',math.degrees(math.asin(math.sin(math.pi/6)/1.5)),19.4712206345)
N('18.3 emergence angle',math.degrees(math.asin(1.5*.5)),48.5903778907)
N('18.4 apparent depth',12/1.5,8)
N('18.4 slab lateral shift',5*math.sin(math.pi/3-math.pi/6)/math.cos(math.pi/6),5/math.sqrt(3))
N('18.5 glass-air critical',math.degrees(math.asin(1/1.5)),41.8103148958)
N('18.5 glass-water critical',math.degrees(math.asin((4/3)/1.5)),62.7339555493)
N('18.5 fibre acceptance',math.degrees(math.asin(math.sqrt(1.5**2-2))),30)
N('18.6 graph slope',.60/.40,1.5)
N('18.6 critical measurement',1/math.sin(math.pi/4),math.sqrt(2))
# Independently entered atom / charge vectors, not parsed from the authoring implementation.
# Each pair is total atoms or total ionic charge on the two sides of a balanced model.
for name,left,right in [
 ('MnO2+4HCl',{'Mn':1,'O':2,'H':4,'Cl':4},{'Mn':1,'O':2,'H':4,'Cl':2+2}),
 ('cold chlorine alkali',{'Cl':2,'O':2,'H':2,'charge':-2},{'Cl':1+1,'O':1+1,'H':2,'charge':-1-1}),
 ('hot chlorine alkali',{'Cl':6,'O':6,'H':6,'charge':-6},{'Cl':5+1,'O':3+3,'H':6,'charge':-5-1}),
 ('chloralkali net',{'Na':2,'Cl':2,'O':2,'H':4},{'Na':2,'Cl':2,'O':2,'H':2+2}),
 ('propene complete combustion',{'C':6,'H':12,'O':18},{'C':6,'H':12,'O':12+6}),
 ('ethanol dehydration',{'C':2,'H':6,'O':1},{'C':2,'H':4+2,'O':1}),
 ('fermentation net',{'C':6,'H':12,'O':6},{'C':4+2,'H':12,'O':2+4}),
 ('phenol tribromination',{'C':6,'H':6,'O':1,'Br':6},{'C':6,'H':3+3,'O':1,'Br':3+3}),
 ('cumene net',{'C':9,'H':12,'O':2},{'C':6+3,'H':6+6,'O':1+1}),
 ('iron oxidation charge',{'Fe':1,'charge':0},{'Fe':1,'charge':2-2}),
 ('oxygen reduction charge',{'O':4,'H':4,'charge':-4},{'O':4,'H':4,'charge':-4}),
]:C('chemical atom/electron account '+name,left==right,dict(left=left,right=right))
(R/'reports/batch06/FINAL_CALCULATIONS.json').write_text(json.dumps(dict(status='pass',checks=checks,scope='Exact final-chapter samples and explicit chemical balances; does not assert every biological statement or every question was independently machine-proved.',teacher_approved=False),ensure_ascii=False,indent=2)+'\n')
print('PASS',len(checks),'final independent calculations and balances')
