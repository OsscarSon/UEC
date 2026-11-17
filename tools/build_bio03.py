import json,sys,os
sys.path.insert(0,os.path.dirname(__file__))
import lesson_bio03_a as A, lesson_bio03_b as B
L=dict(
 syl="2.3.1–2.3.9（细胞内物质和能量的转换）",
 status="**原创，非官方。** 小节与你课本第3章的 7 节一一对应（标题取自课本目录）；内容按董总2026年版生物纲要 2.3 编写，还没和课本、老师核对，不一致以老师和课本为准。图为示意图。",
 sections=A.S+B.S, method=B.method, ex=B.ex, pr=B.pr, vid=B.vid)
js='window.LESSONS=window.LESSONS||{};\nLESSONS["生物3"]='+json.dumps(L,ensure_ascii=False,indent=0)+';\n'
open(os.path.join(os.path.dirname(__file__),'..','lessons','bio03.js'),'w',encoding='utf-8').write(js)
print(len(js),'bytes; sections',len(L['sections']),'ex',len(L['ex']),'pr',len(L['pr']))
