"""Only default formats directly evidenced for each exam category; no cross-exam fallback."""
from pathlib import Path
import json,hashlib
R=Path(__file__).resolve().parents[2];D=R/'data/math-exams';f=json.loads((D/'format-observations.json').read_text());out={}
for c,year in [('semester_final',2026),('graduation_math_ii',2025),('preexam_math_ii',2025),('uec_math_i',2026),('uec_math_ii',2026)]:
 s=next(s for s in f if s['exam_type']==c and s['year']==year);old=year==2025
 assert s['mcq_count']==(20 if old else 15)and s['mcq_weight']==(40 if old else 30)and s['written_count']==12
 assert s['written_weight']==(60 if old else 70)and s['printed_written_marks']==(120 if old else 70)and s['paper_minutes']==[60,120],('source format changed; re-review profile',c)
 out[c]=dict(id=c+'-'+str(year),year=year,exam_type=c,title=str(year)+('已核实旧制四组选答'if old else '已核实新制全部必答'),evidence='source_pdf_cover_visually_read',source_pdf_id=s['source_pdf_id'],cover_pages=s['cover_pdf_pages'],mcq_count=20 if old else 15,mcq_marks=40 if old else 30,written_count=12,written_marks=60 if old else 70,printed_written_marks=120 if old else 70,written_sequence=[10]*12 if old else [4]*5+[6]*5+[10]*2,required_written=6 if old else 12,selection_rule='四组各至少1至多2，共6题'if old else 'all',groups=[dict(id=g,title=t,start=a,end=b,min=1,max=2)for g,t,a,b in [('trig','三角学',1,2),('algebra','代数',3,6),('geometry','解析几何',7,8),('calculus','微积分',9,12)]]if old else [],paper_minutes=[60,120],break_minutes=60 if c=='semester_final'else 15,scope_status='school candidate pool, not certified progress syllabus'if c in['semester_final','graduation_math_ii','preexam_math_ii']else 'current site candidate chapters; conflicts retained in research',notes=s['notes']+(['校内卷一08:00–09:00、卷二10:00起，间隔60分钟；结束12.00a.m.笔误仍待学校确认。']if c=='semester_final'else [])+(['未提供2026本类别原卷；不会把统考新制套入。']if old else []))
version='formats-'+hashlib.sha256(json.dumps(out,sort_keys=True,ensure_ascii=False).encode()).hexdigest()[:12];payload=dict(version=version,profiles=out)
(D/'assembly-profiles.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n');(D/'assembly-profiles.js').write_text('window.MATH_ASSEMBLY_PROFILES='+json.dumps(payload,ensure_ascii=False,separators=(',',':'))+';\n')
print('Built five independently sourced category profiles')
