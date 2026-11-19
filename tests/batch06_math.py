"""Independent symbolic verification of explicitly transcribed batch06 math answers."""
from pathlib import Path
import sympy as s
import json,math
R=Path(__file__).resolve().parents[1];out=R/'reports/batch06'
x=s.symbols('x',real=True);z=s.symbols('z',positive=True);k=s.symbols('k',integer=True,nonnegative=True)
checks=[]
def C(name,ok,detail=''):
 assert bool(ok),(name,detail)
 checks.append(dict(name=name,status='pass',detail=detail))
def Z(name,expr):C(name,s.simplify(s.trigsimp(expr))==0,str(expr))
# Derivatives of independently entered answer expressions; log-absolute cases also tested on negative branches.
for name,f,answer in [
 ('28.2 e0',s.sin(3*x*x),6*x*s.cos(3*x*x)),
 ('28.2 p0',s.cos(2*x-1),-2*s.sin(2*x-1)),
 ('28.2 p1-square',s.sin(x)**2,2*s.sin(x)*s.cos(x)),
 ('28.2 p1-composite',s.sin(x*x),2*x*s.cos(x*x)),
 ('28.2 p2',s.tan(x),s.sec(x)**2),
 ('28.2 degree input',s.sin(s.pi*x/180),s.pi*s.cos(s.pi*x/180)/180),
 ('28.3 e0',s.log(2*x*x+3),4*x/(2*x*x+3)),
 ('28.3 e1',s.log(5*z-1)/s.log(3),5/((5*z-1)*s.log(3))),
 ('28.3 e2',z**z,z**z*(s.log(z)+1)),
 ('28.3 p0 positive branch',s.log(z),1/z),
 ('28.3 p0 negative argument branch',s.log(-x+2),1/(x-2)),
 ('28.3 p2',z*z*s.sqrt(z+1),z*(5*z+4)/(2*s.sqrt(z+1))),
 ('28.3 p3',s.log(1/z),-1/z),
 ('28.4 e0',2**(x*x+1),2*x*s.log(2)*2**(x*x+1)),
 ('28.4 e1',x*s.exp(-x),(1-x)*s.exp(-x)),
 ('28.4 e2',50*s.exp(s.Rational(3,10)*x),15*s.exp(s.Rational(3,10)*x)),
 ('28.4 p0',s.exp(4-3*x),-3*s.exp(4-3*x)),
 ('28.4 p1',s.Rational(1,2)**x,s.Rational(1,2)**x*s.log(s.Rational(1,2))),
 ('28.4 p2',s.exp(2*x)+3**x,2*s.exp(2*x)+3**x*s.log(3)),
 ('28.6 rational derivative',x*x/(x-1),x*(x-2)/(x-1)**2),
]:Z(name,s.diff(f,z if z in f.free_symbols else x)-answer)
# Each tuple is (section and question, original integrand, authored primitive).
for name,f,F in [
 ('29.1 e0',6*x*x-4*x+5,2*x**3-2*x*x+5*x),
 ('29.1 e1',2*x/(x*x+4),s.log(x*x+4)),
 ('29.1 e2',1/(x*x+16),s.atan(x/4)/4),
 ('29.1 p0',s.exp(-3*x),-s.exp(-3*x)/3),
 ('29.1 p1 positive',1/z,s.log(z)),
 ('29.1 p1 negative',1/x,s.log(-x)),
 ('29.1 p2',s.cos(4*x+1),s.sin(4*x+1)/4),
 ('29.2 e0 positive branch',1/(z*(z+2)),s.log(z)/2-s.log(z+2)/2),
 ('29.2 e1 positive branch',1/(z*(z+1)**2),s.log(z)-s.log(z+1)+1/(z+1)),
 ('29.2 e2 x>1',x*x/(x-1),x*x/2+x+s.log(x-1)),
 ('29.2 p1',(2*x+3)/(x*x+1),s.log(x*x+1)+3*s.atan(x)),
 ('29.2 p2',1/(x-3)**2,-1/(x-3)),
 ('29.3 e0',s.sin(x)**3*s.cos(x),s.sin(x)**4/4),
 ('29.3 e1',s.sin(x)**2,x/2-s.sin(2*x)/4),
 ('29.3 e2',s.tan(x)**2*s.sec(x)**2,s.tan(x)**3/3),
 ('29.3 p0',s.sin(x)*s.cos(x)**2,-s.cos(x)**3/3),
 ('29.3 p1',s.cos(x)**2,x/2+s.sin(2*x)/4),
 ('29.3 p2',s.sin(2*x)*s.cos(3*x),-s.cos(5*x)/10+s.cos(x)/2),
 ('29.4 e0 |x|<5',1/s.sqrt(25-x*x),s.asin(x/5)),
 ('29.4 e1 |x|<4',s.sqrt(16-x*x),x*s.sqrt(16-x*x)/2+8*s.asin(x/4)),
 ('29.4 e2 x>3',1/s.sqrt(x*x-9),s.log(x+s.sqrt(x*x-9))),
 ('29.4 p2',1/(x*x+9),s.atan(x/3)/3),
 ('29.4 p3 |x|<3',x/s.sqrt(9-x*x),-s.sqrt(9-x*x)),
 ('29.5 e0',x*s.exp(3*x),s.exp(3*x)*(x/3-s.Rational(1,9))),
 ('29.5 e1',z*s.log(z),z*z*s.log(z)/2-z*z/4),
 ('29.5 e2',s.exp(2*x)*s.cos(x),s.exp(2*x)*(2*s.cos(x)+s.sin(x))/5),
 ('29.5 p0',s.log(z),z*s.log(z)-z),
 ('29.5 p1',x*s.cos(2*x),x*s.sin(2*x)/2+s.cos(2*x)/4),
 ('29.5 p3',s.atan(x),x*s.atan(x)-s.log(1+x*x)/2),
]:Z(name,s.diff(F,z if z in F.free_symbols else x)-f)
for name,F,val,sign in [
 ('28.5 e0',(s.exp(2*x)-1)/x,2,'+'),
 ('28.5 e1',(1-s.cos(3*x))/x**2,s.Rational(9,2),'+'),
 ('28.5 e2',(1+2*x)**(1/x),s.exp(2),'+'),
 ('28.5 p0',s.log(x)/x,0,'infinity'),
 ('28.5 p1',(x*x+1)/(x+1),1,'+'),
 ('28.5 p2',x*s.log(x),0,'+'),
 ('28.5 p3',s.sin(5*x)/s.sin(2*x),s.Rational(5,2),'+'),
]:Z(name,s.limit(F,x,s.oo if sign=='infinity' else 0,dir='+' if sign=='infinity' else sign)-val)
# Differential equation and initial-value verification, evaluated on the stated regular interval.
for name,y,P,Q,t0,y0 in [
 ('30.1 e0',3*x*x+2,0,6*x,1,5),
 ('30.1 e1',s.exp(2*x),-2,0,0,1),
 ('30.2 e0',2*s.exp(3*x*x/2),-3*x,0,0,2),
 ('30.2 p0',x*x-1,0,2*x,0,-1),
 ('30.2 p1',-3*s.exp(-2*x),2,0,0,-3),
 ('30.3 e0',3-2*s.exp(-2*x),2,6,0,1),
 ('30.3 e1 x>0',x*x/3+s.Rational(5,3)/x,1/x,x,1,2),
 ('30.3 p3',x*s.exp(x),-1,s.exp(x),0,0),
 ('30.4 cooling',20+60*s.exp(-s.log(2)*x/10),s.log(2)/10,2*s.log(2),0,80),
 ('30.4 mixing',200*(1-s.exp(-x/20)),s.Rational(1,20),10,0,0),
]:
 Z(name+' equation',s.diff(y,x)+P*y-Q);Z(name+' initial',y.subs(x,t0)-y0)
for name,y,rhs in [
 ('30.1 e2 x<1',1/(1-x),lambda y:y*y),
 ('30.2 e1 x<1',2+1/(1-x),lambda y:(y-2)**2),
 ('30.2 zero equilibrium',s.Integer(0),lambda y:y*(y-1)),
 ('30.2 one equilibrium',s.Integer(1),lambda y:y*(y-1)),
]:Z(name,s.diff(y,x)-rhs(y))
for name,computed,expected in [
 ('29.1 definite',s.integrate(3*x*x,(x,0,1)),1),
 ('29.3 definite',s.integrate(s.sin(x)*s.cos(x),(x,0,s.pi/2)),s.Rational(1,2)),
 ('29.5 definite',s.integrate(x*s.exp(x),(x,0,s.log(2))),2*s.log(2)-1),
 ('31.1 odd sum successor',k*k+2*k+1,(k+1)**2),
 ('31.1 divisibility successor',7*(7**k-1)+6,7**(k+1)-1),
 ('31.1 ordinary sum successor',k*(k+1)/2+k+1,(k+1)*(k+2)/2),
 ('31.2 square difference',2*(x*x+z*z)-(x+z)**2,(x-z)**2),
 ('31.3 composite construction',59*509,30031),
 ('31.4 Newton first',s.Rational(2)+(s.Rational(5)/2-2)/2,s.Rational(9,4)),
 ('31.4 Newton second',(s.Rational(9,4)+5/s.Rational(9,4))/2,s.Rational(161,72)),
 ('31.4 Newton residual',(s.Rational(161,72))**2-5,s.Rational(1,5184)),
]:Z(name,computed-expected)
C('31.4 bisection bracket',s.Rational(3,2)**2<3<s.Rational(7,4)**2)
C('31.4 minimum shrink count',1/2**9>.001 and 1/2**10<=.001)
C('31.4 discontinuity is not root',s.solveset(1/x,x,domain=s.S.Reals)==s.EmptySet)
C('31.1 step inequality',s.ask(s.Q.nonnegative(k)) is True)
# Fresh independent inputs for angles, passive coordinate changes and logic.
X,Y=s.symbols('X Y',real=True)
Z('8.1 degrees to rad',-150*s.pi/180+5*s.pi/6)
Z('8.1 coterminal',17*s.pi/6-2*s.pi-5*s.pi/6)
Z('8.1 accumulated rpm angle',180/s.Integer(60)*2*s.pi*10-60*s.pi)
Z('8.2 arc',6*2*s.pi/3-4*s.pi)
Z('8.2 area',s.Rational(1,2)*36*2*s.pi/3-12*s.pi)
Z('8.2 fixed perimeter square',s.Rational(1,2)*x*(20-2*x)-(25-(x-5)**2))
Z('32.1 translated circle',(X+2)**2+(Y-3)**2-4*(X+2)+6*(Y-3)-12-(X*X+Y*Y-25))
oldx=(X-Y)/s.sqrt(2);oldy=(X+Y)/s.sqrt(2)
Z('32.2 rotated ellipse',5*oldx**2-6*oldx*oldy+5*oldy**2-(2*X**2+8*Y**2))
Z('32.2 orthogonal invariant',oldx**2+oldy**2-X**2-Y**2)
C('7.1 universal counterexample',(-3)**2>4 and not(-3>2))
C('7.4 real counterexample',(-3)**2==9 and -3!=3)
C('7.5 sample conjecture failure',40**2+40+41==41**2)
import itertools
for p,q in itertools.product([False,True],repeat=2):
 C('7.2 de Morgan conjunction '+str((p,q)),(not(p and q))==((not p)or(not q)))
 C('7.2 de Morgan disjunction '+str((p,q)),(not(p or q))==((not p)and(not q)))
 C('7.5 modus ponens '+str((p,q)),not(((not p)or q)and p)or q)
 C('7.5 modus tollens '+str((p,q)),not(((not p)or q)and(not q))or(not p))
Z('9.1 coordinate radius',s.sqrt((-5)**2+12**2)-13)
Z('9.2 large angle',s.sin(765*s.pi/180)-s.sqrt(2)/2)
Z('9.2 composite reduction',s.sin(s.pi+x)*s.cos(-x)+s.cos(s.pi-x)*s.sin(-x))
Z('9.4 arcsin fold',s.asin(s.sin(5*s.pi/6))-s.pi/6)
Z('9.4 arccos fold',s.acos(s.cos(5*s.pi/3))-s.pi/3)
Z('9.4 arctan fold',s.atan(s.tan(3*s.pi/4))+s.pi/4)
Z('10.1 AAS side',6/s.sin(s.pi/6)*s.sin(s.pi/4)-6*s.sqrt(2))
C('10.1 SSA two branches valid',s.asin(s.Rational(4,5))+s.pi/6<s.pi and s.pi-s.asin(s.Rational(4,5))+s.pi/6<s.pi)
C('10.1 SSA impossible',8*s.sin(s.pi/6)/3>1)
Z('10.2 SAS',25+49-70*s.cos(s.pi/3)-39)
Z('10.2 SSS cosine',s.Rational(13**2+14**2-15**2,2*13*14)-s.Rational(5,13))
Z('10.3 Heron',s.sqrt(12*5*4*3)-12*s.sqrt(5))
Z('10.3 cross check area',s.sqrt(21*8*7*6)-84)
Z('10.4 tower',30*s.tan(s.pi/4)+s.Rational(3,2)-s.Rational(63,2))
Z('10.4 two observations',10*s.tan(s.pi/3)-30*s.tan(s.pi/6))
Z('11.1 secant identity',(1/s.cos(x)-1)*(1/s.cos(x)+1)-s.tan(x)**2)
Z('11.2 sine15',s.sin(s.pi/12)-(s.sqrt(6)-s.sqrt(2))/4)
Z('11.2 sine sum',s.Rational(3,5)*s.Rational(12,13)+s.Rational(4,5)*s.Rational(5,13)-s.Rational(56,65))
Z('11.2 cosine sum',s.Rational(4,5)*s.Rational(12,13)-s.Rational(3,5)*s.Rational(5,13)-s.Rational(33,65))
Z('11.2 tangent75',s.tan(5*s.pi/12)-(2+s.sqrt(3)))
Z('11.3 lower power',s.sin(x)**2*s.cos(x)**2-(1-s.cos(4*x))/8)
for v in [s.pi/12,5*s.pi/12,13*s.pi/12,17*s.pi/12]:Z('11.4 double sine root '+str(v),s.sin(2*v)-s.Rational(1,2))
for v in [s.pi/2,7*s.pi/6,11*s.pi/6]:Z('11.4 polynomial root '+str(v),2*s.sin(v)**2-s.sin(v)-1)
for v in [0,s.pi/3,s.pi,5*s.pi/3]:Z('11.4 zero factor retained '+str(v),s.sin(2*v)-s.sin(v))
C('11.4 squared extraneous rejected',s.sin(s.pi/2)!=-1 and s.sin(3*s.pi/2)==-1)
(out/'MATH_VERIFICATION.json').write_text(json.dumps(dict(status='pass',checks=checks,scope='Independently entered symbolic derivatives, primitives, limits, ODEs and numerical arithmetic. Domains and proof logic additionally reviewed in prose; this is not a teacher or official approval.',teacher_approved=False),ensure_ascii=False,indent=2)+'\n')
print('PASS',len(checks),'independent mathematical checks')

