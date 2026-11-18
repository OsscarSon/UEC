"""Reproducible V22 import. Originals and all legacy learning data are immutable."""
import csv, hashlib, json, math, pathlib, re, xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).resolve().parents[2]
ORIG = ROOT / 'illustrations/v22/original'
NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
ET.register_namespace('xlink', 'http://www.w3.org/1999/xlink')
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def dump(p,x): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def add(parent,tag,**attrs): return ET.SubElement(parent,'{'+NS+'}'+tag,{k.replace('_','-'):str(v) for k,v in attrs.items()})
def text(r,s,x,y,size=18,color='#17345d',anchor='start'):
    e=add(r,'text',x=x,y=y,font_size=size,fill=color,text_anchor=anchor,font_family='Noto Sans CJK SC, sans-serif');e.text=s;return e
def line(r,x1,y1,x2,y2,color,dash=False):
    a=add(r,'line',x1=x1,y1=y1,x2=x2,y2=y2,stroke=color,stroke_width=4)
    if dash:a.set('stroke-dasharray','9 5')
    dx,dy=x2-x1,y2-y1;l=math.hypot(dx,dy);ux,uy=dx/l,dy/l
    add(r,'polygon',points=f'{x2},{y2} {x2-12*ux+5*uy},{y2-12*uy-5*ux} {x2-12*ux-5*uy},{y2-12*uy+5*ux}',fill=color)
    return a
def replace_text(r,old,new,**attrs):
    found=False
    for e in r.iter('{'+NS+'}text'):
        if e.text==old:
            e.text=new; e.attrib.update({k.replace('_','-'):str(v) for k,v in attrs.items()});found=True
    assert found,old

manifest=json.loads((ORIG/'manifest.json').read_text())
assets=manifest['assets']
decisions={x['code']:x for x in csv.DictReader((ROOT/'tools/v22/decisions.tsv').open(),delimiter='\t')}
extra=0
for a in assets:
    name=pathlib.Path(a['path']).name
    match=re.match(r'([PB]\d{2}|C\d{2})_',name)
    if match: code=match[1]
    elif re.match(r'\d{2}_',name):code='C'+name[:2]
    else:extra+=1;code=f'C{26+extra}'
    a['code']=code
assert len(set(a['code'] for a in assets))==149 and set(a['code'] for a in assets)==set(decisions)

for a in assets:
    code=a['code'];d=decisions[code];src=ORIG/a['path'];assert sha(src)==a['sha256']
    raw=src.read_text();r=ET.fromstring(raw);fix=[]
    # The context belongs in the website caption, not in a clipped header label.
    for e in list(r):
        if e.tag.endswith('text') and float(e.get('x','0'))>=850 and float(e.get('y','999'))<100:
            r.remove(e);fix.append('移除右上角超出标题栏的重复课程标签，科目/小节在网页图题保留')
    if code=='P04':
        for e in list(r):
            if e.tag.split('}')[-1] in ['line','polygon']:r.remove(e)
        line(r,735,402,950,402,'#2563eb');line(r,355,402,140,402,'#dc4d54')
        replace_text(r,'A 对 B 的力','A 对 B 的力',x=840,y=310)
        replace_text(r,'B 对 A 的力','B 对 A 的力',x=245,y=464)
        fix.append('将等长反向力箭头置于各自受力物体，纠正作用点/受力对象表达')
    if code in ['P05','P16']:
        x,y,w=(362,368,160) if code=='P05' else (420,368.30973451327435,200)
        for e in list(r):
            tag=e.tag.split('}')[-1]
            if tag=='line' and abs(float(e.get('x1','-999'))-x)<.01:r.remove(e)
            elif tag=='polygon' and (code=='P05' or e.get('fill')=='#bfdefd'):r.remove(e)
        if code=='P16':add(r,'rect',x=376,y=y-27,width=88,height=54,rx=4,fill='#bfdefd',stroke='#2563eb',stroke_width=2,transform=f'rotate(-30 {x} {y})')
        dx=w*math.sqrt(3)/4;dy=w/4
        line(r,x,y,x,y+w,'#7155bb')
        line(r,x,y,x-dx,y-3*dy,'#177b59')
        line(r,x,y,x-dx,y+dy,'#ca4b52',True)
        line(r,x,y,x+dx,y+3*dy,'#bd7d13',True)
        add(r,'polyline',points=f'{x-dx},{y+dy} {x},{y+w} {x+dx},{y+3*dy}',fill='none',stroke='#8091a5',stroke_dasharray='4 5',stroke_width=2)
        for e in r.iter('{'+NS+'}text'):
            s=e.text or ''
            if s=='N':e.set('x',str(x-dx-22));e.set('y',str(y-3*dy-10))
            if s.startswith('mg sin'):e.set('x',str(x-dx-100));e.set('y',str(y+dy+25));e.set('fill','#ca4b52')
            if s=='mg cosθ':e.set('x',str(x+dx+10));e.set('y',str(y+3*dy+2));e.set('fill','#bd7d13')
            if s.startswith('mg（') or s=='mg = 20 N':e.set('fill','#7155bb')
            if s.startswith('mg（'):e.set('y','563')
            if s=='重力沿斜面分量':e.text='mg cos30°';e.set('x',str(x+dx+12));e.set('y',str(y+3*dy-20));e.set('fill','#bd7d13')
        if code=='P05':text(r,'θ = 30°',165,505,17)
        fix.append('按30°切向/法向重新计算箭头：N朝左上、重力法向分量朝右下；虚线分量之和等于重力；P16物块改为沿斜面的矩形')
    if code=='P13':replace_text(r,'B：xB = 30 + 3t','B：xB = 30 + 3t',x=390,y=455);fix.append('移开B曲线说明，避免遮盖交点坐标')
    if code=='P17':
        e=next(e for e in r if e.tag.endswith('polyline'))
        e.set('points',' '.join(p for p in e.get('points').split() if float(p.split(',')[0])<=600))
        fix.append('截断x=600/y=550落地点之后的错误地下轨迹，保留飞行区间0≤t≤2s')
    if code=='C17':
        for e in list(r):
            tag=e.tag.split('}')[-1]
            if tag in ['circle','line'] or (tag=='text' and (e.text in ['H','O','氢键（虚线）'])):r.remove(e)
        # O-H...O collinear; intramolecular H-O-H angle 104.5 degrees.
        molecules=[[(320,320,'O'),(420,320,'H'),(320+100*math.cos(math.radians(104.5)),320+100*math.sin(math.radians(104.5)),'H')],
                   [(775,320,'O'),(775+100*math.cos(math.radians(52.25)),320-100*math.sin(math.radians(52.25)),'H'),(775+100*math.cos(math.radians(52.25)),320+100*math.sin(math.radians(52.25)),'H')]]
        for m in molecules:
            for x,y,_ in m[1:]:add(r,'line',x1=m[0][0],y1=m[0][1],x2=x,y2=y,stroke='#405e81',stroke_width=5)
        add(r,'line',x1=445,y1=320,x2=743,y2=320,stroke='#9168bd',stroke_width=4,stroke_dasharray='10 8')
        for m in molecules:
            for x,y,s in m:
                add(r,'circle',cx=x,cy=y,r=28,fill='#fdd9d9' if s=='O' else '#e6effb',stroke='#7a9ac8',stroke_width=2);text(r,s,x,y+9,28,anchor='middle')
        text(r,'氢键：H···O（虚线）',575,280,20,'#7c3da1','middle')
        fix.append('重排两水分子：供体O—H···O共线；两分子各H—O—H=104.5°，实线键与虚线氢键不同')
    if code=='C18':
        replace_text(r,'碱性条件下氯气发生歧化反应','冷、稀碱条件下氯气歧化')
        fix.append('补冷稀碱条件，避免与热浓碱生成氯酸盐混淆')
    if code=='C22':
        replace_text(r,'电解槽中主要过程（简化）','电解槽概念图',font_size=25)
        replace_text(r,'碳阳极 (+)','碳阳极 (+)',x=490,y=252,font_size=20)
        fix.append('缩短面板标题并移开碳阳极标注，避免两行文字在同一位置重叠')
    if code in ['B04','B08','B28']:
        target={'B04':'ATP 水解的整体自由能变化可与细胞吸能过程耦联','B08':'放能反应与吸能过程通过细胞中的具体机制相耦联','B28':None}[code]
        if code=='B08':target=next(e.text for e in r.iter('{'+NS+'}text') if e.text and e.text.startswith('放能反应与吸能'))
        if target:replace_text(r,target,'常见细胞条件下水解ΔG<0；方向依浓度、pH等条件，须经具体机制耦联',font_size=16)
        else:
            e=next(e for e in r.iter('{'+NS+'}text') if e.text and '整体反应的 ΔG' in e.text);e.text='细胞常见条件ΔG<0；依浓度/pH';e.set('font-size','20')
        fix.append('限定ATP水解ΔG符号的细胞条件与浓度，不作任意环境绝对结论')
    if code in ['B07','B10','B20','B27','B43']:
        for e in r.iter('{'+NS+'}text'):
            if e.text and e.text.strip() in ['光合速率','相对光合速率','相对光合作用速率','光合作用速率']:
                e.text='总光合速率（示意）';e.set('font-size','16')
        fix.append('零起点曲线纵轴明确为总光合趋势示意，净交换须扣呼吸，不用于读实测值')
    if code=='B15':
        for e in r.iter('{'+NS+'}text'):
            if e.text and e.text.startswith('图中点数仅表达'):e.text='点数仅示高低浓度；右图是ATP驱动泵示例，离子应比较电化学势。';e.set('font-size','16')
        fix.append('限定右图为ATP驱动泵、离子需按电化学势判断')
    if code=='B17':
        replace_text(r,'不加入酶液','等体积同介质无酶液',font_size=18)
        replace_text(r,'比较气泡量','气泡只作定性观察',font_size=18)
        replace_text(r,'观察：相同时间产氧量','定量另收集O₂测初速',font_size=17)
        replace_text(r,'生物 3.1 / 3.3：比较有无过氧化氢酶条件下的产氧，注意设置对照','等体积介质对照；总液量/pH一致；用稀H₂O₂、护目镜，勿封死产气容器',font_size=17)
        fix.append('匹配对照溶液体积/介质，气泡仅定性，另行收集气体测初速，补稀试剂及护目安全条件')
    if code=='B19':
        replace_text(r,'输入：光、H2O、ADP、NADP+','输入：光、H₂O、ADP、Pi、NADP⁺',font_size=16)
        fix.append('补光反应无机磷酸输入，并调整字号')
    if code=='B22':
        replace_text(r,'三种机制并列：区分顺浓度梯度、逆梯度与是否直接消耗能量','中性物质看浓度，离子看电化学势；右图为ATP直接驱动泵示例',font_size=18)
        replace_text(r,'主动运输','主动运输：ATP泵',font_size=22)
        for e in list(r):
            if e.tag.endswith('circle') and e.get('fill')=='#d36265' and float(e.get('cx','0'))>800 and float(e.get('cy','0'))>450:r.remove(e)
        for x,y in [(925,290),(975,307),(1025,290),(915,498)]:add(r,'circle',cx=x,cy=y,r=7,fill='#d36265')
        text(r,'低浓度 → 高浓度',826,610,17,'#7750b0')
        fix.append('限定直接ATP驱动的主动运输类型，并补电化学梯度条件')
        fix.append('主动运输面板原上下各4个点不能表达逆浓度；改为下侧1点、上侧7点，向上泵送从低到高')
    if code=='P47':
        replace_text(r,'闭合回路中的磁通量随时间变化，才会产生感应电动势','变磁通可产生感应电动势；有闭合导电回路才有感应电流',font_size=17)
        add(r,'line',x1=500,y1=452,x2=532,y2=453,stroke='#173B63',stroke_width=3)
        add(r,'line',x1=662,y1=453,x2=700,y2=452,stroke='#173B63',stroke_width=3)
        for e in list(r):
            if e.tag.endswith('line') and e.get('stroke')=='#0B9488':r.remove(e)
            if e.tag.endswith('polygon') and e.get('fill')=='#0B9488':r.remove(e)
        text(r,'Φ(t) 随磁体位置改变',738,338,18,'#0B9488')
        fix.append('去除电动势必须闭合的错误必要条件，区分电动势与电流')
        fix.append('补线圈图标与检流计引线连接；磁通变化用文字表达，去掉易被误认为磁场方向的竖直箭头')
    if code=='B49':
        e=next(e for e in r if e.tag.endswith('rect') and e.get('y')=='486');e.set('y','544');e.set('height','42')
        replace_text(r,'基因型比例：1 AA : 2 Aa : 1 aa','基因型比例：1 AA : 2 Aa : 1 aa',y=573)
        fix.append('比例说明框移到棋盘格下，不再遮挡Aa/aa结果')
    if code=='B50':
        for e in r.iter('{'+NS+'}text'):
            if e.text and '营养级间能量传递效率' in e.text:e.text='示例：同面积、同一时间段的能量；营养级间传递效率假设10%';e.set('font-size','17')
        fix.append('补能量金字塔相同面积与相同时间的比较基准，10%只为示例')
    if code=='B58':
        replace_text(r,'气孔蒸发','叶肉细胞壁蒸发',font_size=16)
        replace_text(r,'水蒸气扩散','经气孔扩散',font_size=18)
        fix.append('蒸发位置改为叶肉细胞壁，水蒸气经气孔扩散，避免把气孔当液面')
    blocked=d['review'].startswith('BLOCKED')
    out=ROOT/'assets/v22'/a['subject']/pathlib.Path(a['path']).name
    if not blocked:
        out.parent.mkdir(parents=True,exist_ok=True)
        if fix:ET.ElementTree(r).write(out,encoding='utf-8',xml_declaration=True)
        else:out.write_bytes(src.read_bytes())
    a.update(review_status='BLOCKED' if blocked else 'FIXED' if fix else 'PASS',scientific_review=d['review'],fixes=fix,
             concept=d['concept'],section_id=None if d['section']=='-' else d['section'],module=int(d['module']),
             selected=d['selected']=='1',original_path=str(src.relative_to(ROOT)),original_sha256=sha(src),
             reviewed_path=None if blocked else str(out.relative_to(ROOT)),reviewed_sha256=None if blocked else sha(out))
    a['integration_status']='quarantined_science' if blocked else 'pending_mapping' if d['section']=='-' else 'integrated' if a['selected'] else 'alternate_not_displayed'
    a['mapping_evidence']='当前LESSONS真实小节及BATCH_NOTES学习目标/讲解；不使用图片内自报编号作为唯一证据' if d['section']!='-' else '知识点可识别，但当前笔记未保存可确认的对应小节；保留待映射，不新增编号'
    a['review_method']='逐图XML文字/几何检查、隔离img渲染接触表目视、公式/守恒/限定条件核算；不是教师或官方全面审定'
    a['visual_sheet']=f'contact-sheets/{(assets.index(a)//9)+1:02d}.webp'
    a['source_basis']={'physics':'https://openstax.org/books/college-physics-2e/pages/1-introduction-to-science-and-the-realm-of-physics-physical-quantities-and-units',
                       'chemistry':'https://openstax.org/books/chemistry-2e/pages/1-introduction',
                       'biology':'https://openstax.org/books/biology-2e/pages/1-introduction'}[a['subject']]
dump(ROOT/'reports/v22/ASSET_REVIEW.json',assets)
print('Prepared',len(assets),'individual reviews; run layout check then finalize.py')
