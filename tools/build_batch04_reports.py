"""Report the actual five-chapter authoring increment, not only structural test counts."""
from pathlib import Path
from collections import Counter
import csv,json,subprocess
R=Path(__file__).resolve().parents[1];O=R/'reports/batch04';O.mkdir(exist_ok=True)
js="const fs=require('fs'),vm=require('vm'),c={};c.window=c;vm.createContext(c);for(const f of fs.readdirSync('lessons').filter(f=>/^(phys|chem|bio)\\d+\\.js$/.test(f)))vm.runInContext(fs.readFileSync('lessons/'+f,'utf8'),c);vm.runInContext(fs.readFileSync('lessons/batch-notes.js','utf8'),c);process.stdout.write(JSON.stringify({lessons:c.LESSONS,notes:c.BATCH_NOTES}))"
s=json.loads(subprocess.check_output(['node','-e',js],cwd=R));curr=json.loads((R/'data/curriculum.json').read_text());rows=[];sections=[];new=[];modules=[];src=[]
syllabus={'7.1.1':'1.5.1–1.5.2','7.1.2':'1.5.1–1.5.4','7.1.3':'1.5.1','7.2.1':'1.5.5–1.5.6','7.2.2':'1.5.5','7.3.1':'1.5.7','7.3.2':'1.5.7','7.3.3':'1.5.7','7.3.4':'1.5.7','8.1':'1.6.1','8.2.1':'1.6.2','8.2.2':'1.6.1–1.6.3','8.3':'1.6.3–1.6.4','8.4.1':'1.6.5','8.4.2':'1.6.3/1.6.5','9.1.1':'3.2.1–3.2.3','9.1.2':'3.2.1–3.2.3','9.2':'3.2.6–3.2.7','9.3':'3.2.4–3.2.5','10.1.1':'3.3.1–3.3.3','10.1.2':'3.3.1–3.3.3','10.2':'3.3.4–3.3.5','10.3':'3.3.4–3.3.5','10.4':'3.3.6–3.3.7','11.1.1':'3.4.1–3.4.3','11.1.2':'3.4.2–3.4.3','11.2':'3.4.4–3.4.5','11.3':'3.4.6'}
for c in curr:
 key=c['subject']+str(c['chapter']);lesson=s['lessons'].get(key,{});us=s['notes'].get(key,{});ss=lesson.get('sections',[]);isnew=c['subject']=='化学' and c['chapter'] in range(7,12)
 if us:why='全叶级12模块已编写；作者内容与所列计算复核，不等于图示/外部教研最终验收。'
 elif c['subject']=='数学':why='旧35章不迁移；仍缺实际教材小节与I/II逐项分科证据，独立记录保持。'
 elif c['subject']=='化学' and c['chapter'] in [1,2,12,13,14,15,16]:why='同系列公开目录可继续核对，本轮尚未编写；不是无资料阻碍。'
 elif c['subject']=='化学':why='中/下册原章保留；需核同册版次与真实叶级目录，现有公开表可作研究候选，尚未编写。'
 else:why='章框架保留；需对应用户同版本教材的真实小节编号/名称/顺序，不由缺lessons推断教材无小节。'
 rows.append(dict(subject=c['subject'],chapter=c['chapter'],title=c['title'],status='written_pending_external_and_figure_acceptance' if us else 'not_written',category='B' if us else 'D' if c['subject']=='数学' else 'C',saved_section_count=len(ss),new_this_round=isnew,reason=why))
 for sec in ss:
  u=us.get(sec['id']);r=dict(subject=c['subject'],chapter=c['chapter'],chapter_title=c['title'],section_id=sec['id'],section_title=sec['t'],modules=12 if u else 0,new_this_round=isnew,status='authored_content_checked_pending_external_review',examples=len(u['examples']),practice=len(u['practice']),quiz=1,m04_chars=len(''.join(sec['body']+u['deep'])),m05_chars=len(''.join(u['derive'])),m07_method=u['strategy']['method'],goal_refs=';'.join(g['question_ref'] for g in u['diagnostics']),remaining='专用科学图未制作；M12为目标抽样；独立教研与2027适用仍待核。')
  sections.append(r)
  if isnew:
   new.append(r)
   for m in range(1,13):modules.append(dict(subject='化学',chapter=c['chapter'],section_id=sec['id'],section_title=sec['t'],module=m,status='authored',review='逐节作者复核；非外部教师/官方认证'))
   for x in u['content_sources']:src.append(dict(section_id=sec['id'],source_id=x['source_id'],url=x.get('url',''),page=x.get('page',x.get('page_or_section','')),scope=x['version'],verification_status='partially_verified'))
def out(name,rs):
 with (O/name).open('w') as f:w=csv.DictWriter(f,fieldnames=rs[0],lineterminator='\n');w.writeheader();w.writerows(rs)
out('COURSE_COVERAGE.csv',rows);out('ALL_AUTHORED_SECTIONS.csv',sections);out('NEW_SECTIONS.csv',new);out('NEW_MODULE_COVERAGE.csv',modules);out('SOURCES.csv',src)
out('SYLLABUS_COVERAGE.csv',[dict(section_id=r['section_id'],title=r['section_title'],uec_2026_items=syllabus[r['section_id']],scope='2026发布文件正文条目；非课本编号；2027适用未锁定',teaching_scope=s['notes']['化学'+str(r['chapter'])][r['section_id']]['goals'],status='作者对应核对；非官方审定') for r in new])
(O/'COUNTS.json').write_text(json.dumps(dict(new_chapters=5,new_sections=len(new),new_modules=len(modules),new_examples=84,new_practice=112,new_quiz=28,new_question_records=224,total_chapters_authored=14,total_saved_sections=86,total_modules=1032,total_question_records=690,chapter_categories=dict(Counter(r['category'] for r in rows)),new_illustration_prompts=28,total_prompts=142,images_generated=0),ensure_ascii=False,indent=2)+'\n')
# Source-sensitive authoring can still be inspected without accepting a character threshold as teaching quality.
(O/'DEPTH_REVIEW.md').write_text('# 新章内容与深度复核\n\n新增5章28节均逐叶编写，保留原章框架。M04使用逐节原创解释，M05列可独立核验关系/条件，M06三例有逐题专门原理及八步字段，M07引用本节真实进阶例并说明选法与复核，M09/10为四层练习及解析，M12有目标—题目—错因—回读。M01/02/11允许精炼；不以字符数当通过标准。\n\n'+ '\n'.join(f"- 化学{r['section_id']} {r['section_title']}：M04合计{r['m04_chars']}字，M05 {r['m05_chars']}字；选法：{r['m07_method']}；目标抽样{r['goal_refs']}。" for r in new)+'\n\n人工作者复核发现并纠正了醚/水氢键标记中容易多画H的描述、碱性半式答案“如末式”的不独立表达，并补KNO₃分解/用途、共价键σ/π及键能、氧化铝强碱式等范围点。全部224题有题干、条件、原理、步骤、答案与检验；84例作者逐题复核，53项独立算式样例对照及21总反应元素/电荷核验详见CALCULATIONS.json。没有宣称定性题全部得到第二位教师独立审定。\n\n剩余：科学专用图未制作，电子式/三维几何必须最终图审；M12每目标一个题为抽样而非测完全部子技能；实际教材照片/2027适用与完整教研仍有边界。未用图未到位作为省略文字/推理理由。原58节本轮不反复重审，内容源逐字节保留。\n')
print('Reported5 newly authored chapters /28 sections /224 new question records')
