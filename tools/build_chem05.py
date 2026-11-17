import json,sys,os
sys.path.insert(0,os.path.dirname(__file__))
import lesson_chem05 as C
L=dict(syl="1.3.1–1.3.6（原子结构）",
 status="**原创，非官方。** 小节与你课本第5章的 4 节对应（标题取自课本目录）；内容按董总2026年版化学纲要 1.3 编写。5.1、5.3 是背景知识，纲要没有明确条目，是否考请问老师。还没和课本、老师核对，不一致以老师和课本为准。图为示意图。",
 sections=C.S, method=C.method, ex=C.ex, pr=C.pr, vid=C.vid)
js='window.LESSONS=window.LESSONS||{};\nLESSONS["化学5"]='+json.dumps(L,ensure_ascii=False,indent=0)+';\n'
open(os.path.join(os.path.dirname(__file__),'..','lessons','chem05.js'),'w',encoding='utf-8').write(js)
print(len(js))
