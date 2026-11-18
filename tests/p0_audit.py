from pathlib import Path
import json,hashlib,subprocess,math
R=Path(__file__).resolve().parents[1];r=json.loads((R/'illustrations/P0_REVIEW.json').read_text());assert len(r)==10
for x in r:assert hashlib.sha256((R/x['path']).read_bytes()).hexdigest()==x['sha256']
assert sum(x['status']=='approved_for_limited_use' for x in r)==5
for p in (R/'assets/fig').glob('*.svg'):
 old=subprocess.check_output(['git','show','2ca164e:assets/fig/'+p.name],cwd=R);assert p.read_bytes()==old
checks={'three reversals distance':(abs(5+2)+abs(1-5)+abs(-3-1),15),'displacement':(-3-(-2),-1),'static max':(.4*2*10,8),'nonorthogonal force':(math.hypot(15,5*math.sqrt(3)),10*math.sqrt(3)),'contact force':(3*(10/5),6),'ATP coupling':(20-30,-10),'ATP turnover':(.1/.01,10),'Calvin carbon':(3+3*5,18),'Calvin output':(6*3-5*3,3),'photosynthesis net':(8-2,6)}
for k,(a,b) in checks.items():assert math.isclose(a,b,rel_tol=1e-10),k
# The rejected diagram has a real geometric mismatch; don't mark its text answer as a geometry pass.
angle=math.degrees(math.atan2(400,360));assert abs(angle-math.degrees(math.atan2(8,6)))>5
out={'result':'pass','numeric_checks':{k:a for k,(a,b) in checks.items()},'rejected_force_drawing_angle_degrees':angle,'scope':'8道重写题的所列数值样例、73旧SVG字节不变、10导入SVG哈希；不代替生物全部机制/教师审定。'}
(R/'reports/batch03/CALCULATION_RESULTS.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n');print('PASS P0 provenance, original SVG protection and independent numeric samples')
