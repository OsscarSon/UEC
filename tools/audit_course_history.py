"""Search all local history, not only implemented note files. Never infer textbook completeness."""
from pathlib import Path
import subprocess,json,csv,re,hashlib
R=Path(__file__).resolve().parents[1];O=R/'reports/batch03';O.mkdir(exist_ok=True)
def git(*a):return subprocess.check_output(['git',*a],cwd=R).decode()
commits=git('rev-list','--all').splitlines();blobs={};trees=[]
for c in commits:
 entries=git('ls-tree','-r',c).splitlines();trees.append(dict(commit=c,files=len(entries)))
 for line in entries:
  meta,path=line.split('\t',1);sha=meta.split()[2]
  if Path(path).suffix.lower() in ['.json','.js','.html','.csv','.md','.py','.txt']:
   blobs.setdefault(sha,dict(sha=sha,paths=set(),commits=set()))['paths'].add(path);blobs[sha]['commits'].add(c)
fsck=git('fsck','--no-reflogs','--unreachable');unreachable=[]
for line in fsck.splitlines():
 if line.startswith('unreachable blob '):
  sha=line.split()[-1];data=subprocess.check_output(['git','cat-file','blob',sha],cwd=R)
  try:t=data.decode()
  except UnicodeDecodeError:continue
  unreachable.append(dict(sha=sha,bytes=len(data),section_id_candidates=sorted(set(re.findall(r'["\']id["\']\s*:\s*["\'](\d+\.\d+(?:\.\d+)?)["\']',t)))))
rows=[]
for sha,b in blobs.items():
 text=git('cat-file','blob',sha)
 ids=sorted(set(re.findall(r'["\']?id["\']?\s*:\s*["\'](\d+\.\d+(?:\.\d+)?)["\']',text)))
 rows.append(dict(blob=sha,paths=';'.join(sorted(b['paths'])),revision_count=len(b['commits']),bytes=len(text.encode()),literal_section_ids=';'.join(ids),has_course_terms=bool(re.search('curriculum|LESSONS|课程|小节|课本|章节',text))))
with (O/'HISTORY_BLOB_SCAN.csv').open('w') as f:w=csv.DictWriter(f,fieldnames=rows[0]);w.writeheader();w.writerows(rows)
result=dict(commits=trees,text_blobs_examined=len(rows),unreachable_text_blobs=unreachable,fsck=fsck,scope='所有本地可达历史的文本blob；含index、课程JSON、扩展JS、生成器、报告；另读未引用文本对象。不是Claude私有会话或照片的完整搜索。',findings=['初始e77f7eb只有README；三个上传历史含116章目录及原52小节的笔记/生成源，没有查得其余章的真实小节照片或独立完整小节表。','当前58个是仓库可逐项列出的已保存小节，不是课本总小节数；缺笔记文件不证明教材没有小节。','化学6新增6节依据公开内容表，但未证实与用户照片的教材版本完全一致；保留现有结构，身份标记版本待核，不继续照搬其他教材目录。','未查得原Claude会话/目录照片；不能据此宣称照片不存在或教材不可靠。','35数学章真实章名/顺序仍保存；小节与I/II逐项归属未确认，保留兼容数据。'])
(O/'COURSE_HISTORY_AUDIT.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
(O/'COURSE_HISTORY_AUDIT.md').write_text('# 原课程全仓与历史检查\n\n'+result['scope']+'\n\n'+f'检查{len(commits)}个可达提交、{len(rows)}个不同文本blob、{len(unreachable)}个未引用文本blob。逐文件/版本证据见HISTORY_BLOB_SCAN.csv。\n\n'+'\n\n'.join(result['findings'])+'\n\n后续恢复依据应是同版教材目录或用户原照片；考试纲要只能核知识范围，不直接恢复课本编号。化学7/8公开目录候选继续研究版本对应，未据此擅自增节。尚未确认范围按原116章覆盖表逐章列出；这些是资料保存/对应缺口，不是教材来源被否定。\n')
print('History audit:',len(commits),'commits',len(rows),'text blobs',len(unreachable),'unreachable text blobs')
