> 最新P0续作、全课程历史核查及未完成事项见 [本轮报告](reports/batch03/DELIVERY.md)。

> 当前版本：本轮209项主清单与114条独立中英文制作任务见 [主清单](illustrations/ILLUSTRATION_MASTER_MANIFEST.json) 和 [全部提示词](illustrations/PROMPTS_BATCH_ALL.md)。新增化学6的6项精确要求在上述文件逐项列出。以下203项为daa3637之前的完整审查快照；其中“未改图/未改笔记”只描述当时，不代表本轮。当前导入、SVG与验证见 [本轮报告](reports/batch02/DELIVERY.md)。

# 教学插图需求与现有图审查

审查日期：2026-11-18（Asia/Kuala_Lumpur）；PR #1 原分支 `codex/uec-2027-batch-notes-math-split`；被审查内容提交 `8b54cfed56bd10eedcf0387570a751bb3a34a89b`。

**本文件是制作需求，不是图片交付。此次生成、修改、删除图片均为0，笔记与网站运行文件均未修改。**

扫描116个原章级记录、52个真实小节；重点为本PR新增十二模块的41节。共203条教学图审查／制作计划：73条现有SVG、41条现有HTML/CSS知识结构图、54条新增制作需求、35条数学章级待确认计划。另列6个界面素材。203条绝不表示203张已完成图片。

高级数学（I）、（II）目前各有独立入口，但没有已核实章归属或真实小节。旧数学35章按原ID、名称、顺序保留，计划只绑定真实章；所有数学section_id均为null，不能按试卷一／二分科。73个理化生章也还没有真实小节，只有扫描阻碍记录，不虚构知识点、图或小节号。

## 统计与优先顺序

| 记录类型 | 数量 | 处理 |
| --- | --- | --- |
| 现有教学SVG | 73 | 仅审查／计划 |
| 现有模块03知识结构图 | 41 | 仅审查／计划 |
| 新增制作计划 | 54 | 仅审查／计划 |
| 数学章级待确认计划 | 35 | 仅审查／计划 |
| 非教学界面素材 | 6 | 保留，单独统计 |

| 动作 | 全部教学记录 | 现有SVG | 现有结构图 |
| --- | --- | --- | --- |
| 保留／复用 | 60 | 43 | 17 |
| 局部修正 | 32 | 24 | 8 |
| 重绘 | 22 | 6 | 16 |
| 新增需求 | 54 | 0 | 0 |
| 待核实，禁止先制作 | 35 | 0 | 0 |

| 类别 | 数量 |
| --- | --- |
| 精确科学SVG | 83 |
| 结构示意图 | 90 |
| 数学函数图 | 19 |
| 实验装置图 | 10 |
| 辅助插画 | 1 |

| 优先级 | 数量 | 含义 |
| --- | --- | --- |
| P0 | 10 | 现有科学表述/关键数学排版可能误导，先审定再用 |
| P1 | 95 | 核心教学理解或实验/图表推理明显依赖 |
| P2 | 98 | 有益补充或待确认主题，非优先制作 |
| P3 | 0 | 界面非教学素材 |

现有图43幅用于本批41节，另30幅属于化学5／生物3。所有73幅都有真实小节引用；建议跨节复用与当前实际渲染分别记录，不把未来回链说成现有功能。

## 使用与制作约束

- `retain`为可保留复用，`correct`为局部科学/标签修正需求，`redraw`为关系或结构须重绘；本轮均未执行。旧文件仍全部保留。
- 每项标签、几何、单位、对象、计量与模型条件应逐一核对。示意不等于精确比例；同图的定量箭头/坐标必须准确。辅助人物不能替代受力图或定量图。
- 数学函数图应按确认函数、定义域与参数由确定性计算生成；当前35条均被小节／归属缺失阻挡，不进入绘图。
- SVG建议画布1200×800；窄屏320–390 CSS px时拆为纵向面板或可展开查看，渲染标签至少12 CSS px，目标14；不能把大画布缩到手机后仍声称字号合格。所列为待验收要求，本轮未对未制作图做手机/电脑实测。
- 标注版与练习留空版共用同一正确数据/几何；只采用已有题给数据，不为凑图虚构实验值、误差棒、官方得分点、历年考频。版本是制作方式，不额外计作成品数。
- 实验图是装置/控制/测量的教学原理需求；缺器材、浓度或协议时必须待教师/实验资料确认，不补猜具体操作。
- JSON每项有来源锚点、模型条件、验收门槛、复用状态；来源登记的“部分核实”不等于整图或整课已经教研审定。

## 全部真实课程扫描

章级完整记录见 [CSV](reports/ILLUSTRATION_CHAPTER_SCAN.csv)，以下也列出116章。无小节的章不伪造图清单。

| 科目 | 原章号 | 原章名 | 真实小节数 | 状态 |
| --- | --- | --- | --- | --- |
| 物理 | 1 | 物理学简介 | 0 | 待真实小节 |
| 物理 | 2 | 物理量的测量、单位和数据处理 | 0 | 待真实小节 |
| 物理 | 3 | 直线运动 | 9 | 已逐节列图 |
| 物理 | 4 | 牛顿运动定律 | 8 | 已逐节列图 |
| 物理 | 5 | 静力学 | 0 | 待真实小节 |
| 物理 | 6 | 平面运动 | 0 | 待真实小节 |
| 物理 | 7 | 功与能 | 0 | 待真实小节 |
| 物理 | 8 | 动量守恒定律 | 0 | 待真实小节 |
| 物理 | 9 | 转动 | 0 | 待真实小节 |
| 物理 | 10 | 振动 | 0 | 待真实小节 |
| 物理 | 11 | 流体力学 | 0 | 待真实小节 |
| 物理 | 12 | 物质的性质 | 0 | 待真实小节 |
| 物理 | 13 | 温度与热量 | 0 | 待真实小节 |
| 物理 | 14 | 热的传递 | 0 | 待真实小节 |
| 物理 | 15 | 气体定律 | 0 | 待真实小节 |
| 物理 | 16 | 气体分子运动论与热力学 | 0 | 待真实小节 |
| 物理 | 17 | 机械波 | 0 | 待真实小节 |
| 物理 | 18 | 光的反射与折射 | 0 | 待真实小节 |
| 物理 | 19 | 棱镜和透镜 | 0 | 待真实小节 |
| 物理 | 20 | 光的波动性 | 0 | 待真实小节 |
| 物理 | 21 | 电场 | 0 | 待真实小节 |
| 物理 | 22 | 恒定电流 | 0 | 待真实小节 |
| 物理 | 23 | 电流与磁场 | 0 | 待真实小节 |
| 物理 | 24 | 电磁感应与交流电 | 0 | 待真实小节 |
| 物理 | 25 | 量子物理学 | 0 | 待真实小节 |
| 物理 | 26 | 原子与原子核物理学 | 0 | 待真实小节 |
| 物理 | 27 | 相对论简介 | 0 | 待真实小节 |
| 化学 | 1 | 绪论 | 0 | 待真实小节 |
| 化学 | 2 | 水和氢 | 0 | 待真实小节 |
| 化学 | 3 | 原子与分子 | 6 | 已逐节列图 |
| 化学 | 4 | 化学方程式与化学计算 | 7 | 已逐节列图 |
| 化学 | 5 | 原子结构 | 4 | 已逐节列图 |
| 化学 | 6 | 元素周期表 | 0 | 待真实小节 |
| 化学 | 7 | 化学键与分子间作用力 | 0 | 待真实小节 |
| 化学 | 8 | 氧化还原反应 | 0 | 待真实小节 |
| 化学 | 9 | IA族元素：钠和钾 | 0 | 待真实小节 |
| 化学 | 10 | IIA族元素：镁和钙 | 0 | 待真实小节 |
| 化学 | 11 | IIIA族元素：铝 | 0 | 待真实小节 |
| 化学 | 12 | IVA族元素：碳和硅 | 0 | 待真实小节 |
| 化学 | 13 | VA族元素：氮和磷 | 0 | 待真实小节 |
| 化学 | 14 | VIA族元素：氧和硫 | 0 | 待真实小节 |
| 化学 | 15 | VIIA族元素：卤素 | 0 | 待真实小节 |
| 化学 | 16 | 过渡元素 | 0 | 待真实小节 |
| 化学 | 17 | 气体 | 0 | 待真实小节 |
| 化学 | 18 | 溶液及其性质 | 0 | 待真实小节 |
| 化学 | 19 | 化学反应和能量 | 0 | 待真实小节 |
| 化学 | 20 | 化学反应速率 | 0 | 待真实小节 |
| 化学 | 21 | 化学平衡的移动 | 0 | 待真实小节 |
| 化学 | 22 | 水溶液中的离子平衡 | 0 | 待真实小节 |
| 化学 | 23 | 酸碱盐 | 0 | 待真实小节 |
| 化学 | 24 | 电化学 | 0 | 待真实小节 |
| 化学 | 25 | 核化学 | 0 | 待真实小节 |
| 化学 | 26 | 有机化学 | 0 | 待真实小节 |
| 化学 | 27 | 烷烃 | 0 | 待真实小节 |
| 化学 | 28 | 烯烃 | 0 | 待真实小节 |
| 化学 | 29 | 炔烃 | 0 | 待真实小节 |
| 化学 | 30 | 芳香烃 | 0 | 待真实小节 |
| 化学 | 31 | 卤代烃 | 0 | 待真实小节 |
| 化学 | 32 | 羟基化合物：醇、酚 | 0 | 待真实小节 |
| 化学 | 33 | 羰基化合物：醛、酮、碳水化合物 | 0 | 待真实小节 |
| 化学 | 34 | 有机酸及其衍生物 | 0 | 待真实小节 |
| 化学 | 35 | 有机高分子化合物 | 0 | 待真实小节 |
| 生物 | 1 | 生物是由什么组成的 | 6 | 已逐节列图 |
| 生物 | 2 | 细胞的结构与功能 | 5 | 已逐节列图 |
| 生物 | 3 | 细胞内物质和能量的转换 | 7 | 已逐节列图 |
| 生物 | 4 | 细胞分化 | 0 | 待真实小节 |
| 生物 | 5 | 食物的消化与物质代谢 | 0 | 待真实小节 |
| 生物 | 6 | 营养成分的运输 | 0 | 待真实小节 |
| 生物 | 7 | 动植物的协调与反应 | 0 | 待真实小节 |
| 生物 | 8 | 内环境的恒定和排泄系统 | 0 | 待真实小节 |
| 生物 | 9 | 健康与免疫 | 0 | 待真实小节 |
| 生物 | 10 | 生态系统 | 0 | 待真实小节 |
| 生物 | 11 | 生态保育与可持续发展 | 0 | 待真实小节 |
| 生物 | 12 | 生殖 | 0 | 待真实小节 |
| 生物 | 13 | 细胞分裂 | 0 | 待真实小节 |
| 生物 | 14 | 遗传的物质基础 | 0 | 待真实小节 |
| 生物 | 15 | 基因与遗传定律 | 0 | 待真实小节 |
| 生物 | 16 | 应用遗传学 | 0 | 待真实小节 |
| 生物 | 17 | 生物多样性 | 0 | 待真实小节 |
| 生物 | 18 | 细菌与病毒 | 0 | 待真实小节 |
| 生物 | 19 | 演化 | 0 | 待真实小节 |
| 数学 | 1 | 直角坐标系与直线 | 0 | 待真实小节 |
| 数学 | 2 | 一元二次方程式与二次函数 | 0 | 待真实小节 |
| 数学 | 3 | 多项式 | 0 | 待真实小节 |
| 数学 | 4 | 无理式 | 0 | 待真实小节 |
| 数学 | 5 | 函数 | 0 | 待真实小节 |
| 数学 | 6 | 不等式 | 0 | 待真实小节 |
| 数学 | 7 | 逻辑 | 0 | 待真实小节 |
| 数学 | 8 | 角度与弧度 | 0 | 待真实小节 |
| 数学 | 9 | 任意角的三角函数 | 0 | 待真实小节 |
| 数学 | 10 | 三角学的应用 | 0 | 待真实小节 |
| 数学 | 11 | 三角恒等式与三角方程式 | 0 | 待真实小节 |
| 数学 | 12 | 指数与对数 | 0 | 待真实小节 |
| 数学 | 13 | 数列与级数 | 0 | 待真实小节 |
| 数学 | 14 | 行列式 | 0 | 待真实小节 |
| 数学 | 15 | 矩阵 | 0 | 待真实小节 |
| 数学 | 16 | 圆 | 0 | 待真实小节 |
| 数学 | 17 | 平面向量 | 0 | 待真实小节 |
| 数学 | 18 | 立体几何 | 0 | 待真实小节 |
| 数学 | 19 | 排列组合 | 0 | 待真实小节 |
| 数学 | 20 | 二项式定理 | 0 | 待真实小节 |
| 数学 | 21 | 极限 | 0 | 待真实小节 |
| 数学 | 22 | 微分及其应用（一） | 0 | 待真实小节 |
| 数学 | 23 | 不定积分及其应用 | 0 | 待真实小节 |
| 数学 | 24 | 定积分及其应用 | 0 | 待真实小节 |
| 数学 | 25 | 统计学 | 0 | 待真实小节 |
| 数学 | 26 | 概率 | 0 | 待真实小节 |
| 数学 | 27 | 线性回归 | 0 | 待真实小节 |
| 数学 | 28 | 微分及其应用（二） | 0 | 待真实小节 |
| 数学 | 29 | 积分法 | 0 | 待真实小节 |
| 数学 | 30 | 微分方程式 | 0 | 待真实小节 |
| 数学 | 31 | 数学方法 | 0 | 待真实小节 |
| 数学 | 32 | 坐标变换 | 0 | 待真实小节 |
| 数学 | 33 | 圆锥曲线 | 0 | 待真实小节 |
| 数学 | 34 | 复数 | 0 | 待真实小节 |
| 数学 | 35 | 空间向量 | 0 | 待真实小节 |

### 52个真实小节

| 科目/原章 | 真实小节 | 原小节名 | 本批41节 | 当前SVG数 | 对应图记录 |
| --- | --- | --- | --- | --- | --- |
| 物理3 | 3.1 | 机械运动 | 是 | 0 | ILL-MAP-PHY-3_1、ILL-PLAN-PHY-3_1-01 |
| 物理3 | 3.2 | 参照物、坐标系和参照系 | 是 | 1 | ILL-ASSET-P3_2、ILL-MAP-PHY-3_2、ILL-PLAN-PHY-3_2-01 |
| 物理3 | 3.3 | 路程和位移 | 是 | 1 | ILL-ASSET-P3_3、ILL-MAP-PHY-3_3、ILL-PLAN-PHY-3_3-01 |
| 物理3 | 3.4 | 匀速直线运动　速度和速率 | 是 | 0 | ILL-ASSET-P3_5A、ILL-ASSET-P3_5B、ILL-MAP-PHY-3_4、ILL-PLAN-PHY-3_4-01 |
| 物理3 | 3.5 | 匀速直线运动的图象 | 是 | 2 | ILL-ASSET-P3_5A、ILL-ASSET-P3_5B、ILL-MAP-PHY-3_5、ILL-PLAN-PHY-3_5-01 |
| 物理3 | 3.6 | 变速直线运动　平均速度和瞬时速度 | 是 | 1 | ILL-ASSET-P3_6、ILL-MAP-PHY-3_6、ILL-PLAN-PHY-3_6-01 |
| 物理3 | 3.7 | 变速直线运动的加速度 | 是 | 1 | ILL-ASSET-P3_7、ILL-MAP-PHY-3_7、ILL-PLAN-PHY-3_7-01 |
| 物理3 | 3.8 | 匀加速直线运动 | 是 | 1 | ILL-ASSET-P3_8、ILL-MAP-PHY-3_8、ILL-PLAN-PHY-3_8-01、ILL-PLAN-PHY-3_8-02 |
| 物理3 | 3.9 | 自由落体运动 | 是 | 1 | ILL-ASSET-P3_9、ILL-MAP-PHY-3_9、ILL-PLAN-PHY-3_9-01、ILL-PLAN-PHY-3_9-02 |
| 物理4 | 4.1 | 力与运动 | 是 | 0 | ILL-MAP-PHY-4_1、ILL-PLAN-PHY-4_1-01 |
| 物理4 | 4.2 | 力的种类 | 是 | 1 | ILL-ASSET-P4_2、ILL-MAP-PHY-4_2、ILL-PLAN-PHY-4_2-01、ILL-PLAN-PHY-4_2-02 |
| 物理4 | 4.3 | 力的合成与分解 | 是 | 2 | ILL-ASSET-P4_3A、ILL-ASSET-P4_3B、ILL-MAP-PHY-4_3、ILL-PLAN-PHY-4_3-01 |
| 物理4 | 4.4 | 牛顿第一运动定律 | 是 | 0 | ILL-MAP-PHY-4_4、ILL-PLAN-PHY-4_4-01 |
| 物理4 | 4.5 | 惯性与质量 | 是 | 0 | ILL-MAP-PHY-4_5、ILL-PLAN-PHY-4_5-01 |
| 物理4 | 4.6 | 动量 | 是 | 1 | ILL-ASSET-P4_6、ILL-MAP-PHY-4_6、ILL-PLAN-PHY-4_6-01 |
| 物理4 | 4.7 | 牛顿第二运动定律 | 是 | 2 | ILL-ASSET-P4_7A、ILL-ASSET-P4_7B、ILL-MAP-PHY-4_7、ILL-PLAN-PHY-4_7-01、ILL-PLAN-PHY-4_7-02 |
| 物理4 | 4.8 | 牛顿第三运动定律 | 是 | 1 | ILL-ASSET-P4_8、ILL-MAP-PHY-4_8、ILL-PLAN-PHY-4_8-01 |
| 化学3 | 3.1 | 原子学说与分子学说 | 是 | 1 | ILL-ASSET-C3_1、ILL-MAP-CHEM-3_1、ILL-PLAN-CHEM-3_1-01 |
| 化学3 | 3.2 | 物质组成及化学反应中的基本定律 | 是 | 1 | ILL-ASSET-C3_2、ILL-MAP-CHEM-3_2、ILL-PLAN-CHEM-3_2-01 |
| 化学3 | 3.3 | 原子与相对原子质量 | 是 | 1 | ILL-ASSET-C3_3、ILL-ASSET-C5_2A、ILL-MAP-CHEM-3_3、ILL-PLAN-CHEM-3_3-01、ILL-PLAN-CHEM-3_3-02 |
| 化学3 | 3.4 | 化学式与式量 | 是 | 0 | ILL-MAP-CHEM-3_4、ILL-PLAN-CHEM-3_4-01 |
| 化学3 | 3.5 | 确定化学式的方法 | 是 | 1 | ILL-ASSET-C3_5、ILL-MAP-CHEM-3_5、ILL-PLAN-CHEM-3_5-01、ILL-PLAN-CHEM-3_5-02 |
| 化学3 | 3.6 | 物质的量 | 是 | 1 | ILL-ASSET-C3_6、ILL-MAP-CHEM-3_6、ILL-PLAN-CHEM-3_6-01、ILL-PLAN-CHEM-3_6-02 |
| 化学4 | 4.1.1 | 表示化学反应的语言——化学方程式 | 是 | 1 | ILL-ASSET-C4_1、ILL-MAP-CHEM-4_1_1、ILL-PLAN-CHEM-4_1_1-01 |
| 化学4 | 4.1.2 | 化学反应的类型 | 是 | 1 | ILL-ASSET-C4_2、ILL-MAP-CHEM-4_1_2、ILL-PLAN-CHEM-4_1_2-01 |
| 化学4 | 4.1.3 | 化学方程式的配平 | 是 | 1 | ILL-ASSET-C4_3、ILL-MAP-CHEM-4_1_3、ILL-PLAN-CHEM-4_1_3-01 |
| 化学4 | 4.2.1 | 计算反应物和生成物的量 | 是 | 1 | ILL-ASSET-C4_4、ILL-MAP-CHEM-4_2_1、ILL-PLAN-CHEM-4_2_1-01 |
| 化学4 | 4.2.2 | 关于不纯物的计算 | 是 | 0 | ILL-MAP-CHEM-4_2_2、ILL-PLAN-CHEM-4_2_2-01 |
| 化学4 | 4.2.3 | 利用限量反应物的计算 | 是 | 1 | ILL-ASSET-C4_5、ILL-MAP-CHEM-4_2_3、ILL-PLAN-CHEM-4_2_3-01 |
| 化学4 | 4.2.4 | 产率的计算 | 是 | 0 | ILL-MAP-CHEM-4_2_4、ILL-PLAN-CHEM-4_2_4-01 |
| 化学5 | 5.1 | 原子模型 | 否 | 2 | ILL-ASSET-C5_1A、ILL-ASSET-C5_1B |
| 化学5 | 5.2 | 原子序数、质量数和同位素 | 否 | 2 | ILL-ASSET-C5_2A、ILL-ASSET-C5_2B |
| 化学5 | 5.3 | 核外电子的能阶 | 否 | 2 | ILL-ASSET-C5_3A、ILL-ASSET-C5_3B |
| 化学5 | 5.4 | 原子核外电子的排布 | 否 | 4 | ILL-ASSET-C5_4A、ILL-ASSET-C5_4B、ILL-ASSET-C5_4C、ILL-ASSET-C5_4D |
| 生物1 | 1.1 | 生命离不开水 | 是 | 1 | ILL-ASSET-B1_1、ILL-MAP-BIO-1_1、ILL-PLAN-BIO-1_1-01 |
| 生物1 | 1.2 | 生物体必需的无机盐 | 是 | 0 | ILL-MAP-BIO-1_2、ILL-PLAN-BIO-1_2-01 |
| 生物1 | 1.3 | 能量的主要来源——糖类 | 是 | 2 | ILL-ASSET-B1_3A、ILL-ASSET-B1_3B、ILL-ASSET-B1_SUM、ILL-MAP-BIO-1_3、ILL-PLAN-BIO-1_3-01、ILL-PLAN-BIO-1_3-02 |
| 生物1 | 1.4 | 贮存能量的物质——脂质 | 是 | 2 | ILL-ASSET-B1_4A、ILL-ASSET-B1_4B、ILL-ASSET-B1_SUM、ILL-MAP-BIO-1_4、ILL-PLAN-BIO-1_4-01、ILL-PLAN-BIO-1_4-02 |
| 生物1 | 1.5 | 生命活动的承担者——蛋白质 | 是 | 2 | ILL-ASSET-B1_5A、ILL-ASSET-B1_5B、ILL-ASSET-B1_SUM、ILL-MAP-BIO-1_5、ILL-PLAN-BIO-1_5-01、ILL-PLAN-BIO-1_5-02 |
| 生物1 | 1.6 | 遗传信息的携带者——核酸 | 是 | 3 | ILL-ASSET-B1_6A、ILL-ASSET-B1_6B、ILL-ASSET-B1_SUM、ILL-MAP-BIO-1_6、ILL-PLAN-BIO-1_6-01、ILL-PLAN-BIO-1_6-02 |
| 生物2 | 2.1 | 细胞是生物的基本单位 | 是 | 1 | ILL-ASSET-B2_1、ILL-MAP-BIO-2_1、ILL-PLAN-BIO-2_1-01、ILL-PLAN-BIO-2_1-02 |
| 生物2 | 2.2 | 细胞膜——物质进出的门户 | 是 | 2 | ILL-ASSET-B1_4B、ILL-ASSET-B2_2A、ILL-ASSET-B2_2B、ILL-MAP-BIO-2_2、ILL-PLAN-BIO-2_2-01、ILL-PLAN-BIO-2_2-02、ILL-PLAN-BIO-2_2-03 |
| 生物2 | 2.3 | 细胞器——系统内的分工协作 | 是 | 3 | ILL-ASSET-B2_3A、ILL-ASSET-B2_3B、ILL-ASSET-B2_3C、ILL-PLAN-BIO-2_1-02、ILL-MAP-BIO-2_3、ILL-PLAN-BIO-2_3-01 |
| 生物2 | 2.4 | 细胞核——细胞的控制中心 | 是 | 1 | ILL-ASSET-B1_6B、ILL-ASSET-B2_4、ILL-MAP-BIO-2_4、ILL-PLAN-BIO-2_4-01 |
| 生物2 | 2.5 | 细胞壁——细胞的保护外墙 | 是 | 1 | ILL-ASSET-B2_5、ILL-PLAN-BIO-2_2-01、ILL-MAP-BIO-2_5 |
| 生物3 | 3.1 | 生物催化剂——酶 | 否 | 2 | ILL-ASSET-B3_1A、ILL-ASSET-B3_1B |
| 生物3 | 3.2 | 影响酶活性的因素 | 否 | 5 | ILL-ASSET-B3_2A、ILL-ASSET-B3_2B、ILL-ASSET-B3_2C、ILL-ASSET-B3_2D、ILL-ASSET-B3_2E |
| 生物3 | 3.3 | 酶在生产生活中的应用 | 否 | 1 | ILL-ASSET-B3_3 |
| 生物3 | 3.4 | 细胞的能量通货——ATP | 否 | 1 | ILL-ASSET-B3_4 |
| 生物3 | 3.5 | 生命活动的能量来自哪里——呼吸作用 | 否 | 2 | ILL-ASSET-B3_5A、ILL-ASSET-B3_5B |
| 生物3 | 3.6 | 植物的光合作用 | 否 | 5 | ILL-ASSET-B3_6A、ILL-ASSET-B3_6B、ILL-ASSET-B3_6C、ILL-ASSET-B3_6D、ILL-ASSET-B3_6E |
| 生物3 | 3.7 | 环境因素对光合作用的影响 | 否 | 4 | ILL-ASSET-B3_7A、ILL-ASSET-B3_7B、ILL-ASSET-B3_7C、ILL-ASSET-B3_SUM |

## 十二模块的图示覆盖

[492项逐模块检查CSV](reports/ILLUSTRATION_MODULE_COVERAGE.csv)覆盖41×12；每行列知识范围、当前渲染图ID、拟复用/新增ID及缺口。当前SVG只在M05、知识结构图只在M03渲染；跨模块和跨小节引用是计划。其余11个旧小节只审现有图，不套用不存在的十二模块。

| 模块 | 图示判断 |
| --- | --- |
| 01 学习目标 | 无需独立图片；目标需对接可观察的图形判断 |
| 02 前置知识 | 可回链已存在前置/本节图，不造前置节号 |
| 03 知识结构图 | 41项均有当前HTML/CSS图，按因果/分类/条件/步骤决定保留或重构 |
| 04 深度讲解 | 核查结构、机制、数量与适用条件；采用逐项图要求 |
| 05 图解与公式／实验 | 73现有SVG科学/标签审查，54新增需求补主要缺口；非每节均需实验 |
| 06 典型例题 | 沿用现有3例数据；空间与数量关系用对应图，纯计算无需凑图 |
| 07 UEC题型攻略 | 复用曲线/受力/计量/装置图训练题干选法；不画未证实考频/评分 |
| 08 易错易混 | 正确图与错解/错误箭头对照，错误层须明确标记 |
| 09 分层练习 | 4道已有题有图必要时使用留空版，不能直接泄露答案 |
| 10 完整解析 | 与M09相同参数，显示推理标注；不另算成品 |
| 11 考前速记 | 文字可简洁；回链核心图，无需装饰图 |
| 12 掌握度检测 | 已有题的视觉判断可用留空版；目标映射和反馈缺口见质量报告 |

## 科学与范围来源登记

学校资料只说明兴华校内安排；2026董总文件只说明当前已取得的官方身份/范围，2027适用性仍待确认。OpenStax/BIPM/NIST用于科学原则，不用于推定学校考试或UEC考频。两份另传Research报告的核验记录仍见 [RESEARCH_VERIFICATION](reports/RESEARCH_VERIFICATION.md)，本清单不把二手报告当作精确图形的唯一依据。

### SOURCE repo_curriculum

- 仓库真实章级目录：data/curriculum.json
- 定位：原数组索引/subject/chapter；查阅：2026-11-18；状态：`verified`；用途：`course_identity`。
- 边界：只证实已有章名和顺序，不证明I/II归属。

### SOURCE repo_lessons

- 仓库真实小节及现有图引用：lessons/*.js
- 定位：sections[].id/t/body/figs；查阅：2026-11-18；状态：`verified`；用途：`course_identity`。
- 边界：来源由每条source_anchors定位；不把正文自身当独立科学权威。

### SOURCE kit_standard

- 用户ZIP十二模块与四原则：user_attachment:UEC_2027_Codex_Batch_Notes_Kit_v2.zip
- 定位：12_MODULE_NOTE_STANDARD.md；FOUR_NONNEGOTIABLE_RULES.md；查阅：2026-11-18；状态：`verified`；用途：`pedagogical_standard`。
- 边界：十二模块结构齐备不等于教学深度合格；没有实验时不可虚构。

### SOURCE dz_physics

- 董总2026physics纲要：https://uec.dongzong.my/wp-content/uploads/2026/07/S12-2026-0623.pdf
- 定位：PDF第2页起相关条目；查阅：2026-11-17；状态：`partially_verified`；用途：`UEC_2026_only`。
- 边界：范围和能力依据，不是具体图形模板或2027版本锁定。

### SOURCE dz_chemistry

- 董总2026chemistry纲要：https://uec.dongzong.my/wp-content/uploads/2026/07/S11-2026-0623.pdf
- 定位：PDF第2页起相关条目；查阅：2026-11-17；状态：`partially_verified`；用途：`UEC_2026_only`。
- 边界：范围和能力依据，不是具体图形模板或2027版本锁定。

### SOURCE dz_biology

- 董总2026biology纲要：https://uec.dongzong.my/wp-content/uploads/2026/07/S10-2026-0623.pdf
- 定位：PDF第2页起相关条目；查阅：2026-11-17；状态：`partially_verified`；用途：`UEC_2026_only`。
- 边界：范围和能力依据，不是具体图形模板或2027版本锁定。

### SOURCE dz_adv_math_i

- 董总2026adv_math_i评量规格：https://uec.dongzong.my/wp-content/uploads/2026/07/S06-2026-0730.pdf
- 定位：PDF第1页；查阅：2026-11-17；状态：`partially_verified`；用途：`subject_identity_only`。
- 边界：证明两个科目各有试卷一、二；不提供旧35章逐小节一对一分配。

### SOURCE dz_adv_math_ii

- 董总2026adv_math_ii评量规格：https://uec.dongzong.my/wp-content/uploads/2026/07/S07-2026-0730.pdf
- 定位：PDF第1页；查阅：2026-11-17；状态：`partially_verified`；用途：`subject_identity_only`。
- 边界：证明两个科目各有试卷一、二；不提供旧35章逐小节一对一分配。

### SOURCE school

- 兴华2027选科与校内安排：user_attachment:HinHua_2027_subjects_scope_exam_arrangements.pdf
- 定位：第2–3页分科与高三数学主题，第4页化学；查阅：2026-11-17；状态：`verified`；用途：`HinHua_school_only`。
- 边界：学校课题主题可支持待确认计划；不能代替正式UEC范围或数学小节目录。

### SOURCE bipm

- BIPM SI mole：https://www.bipm.org/en/si-base-units/mole
- 定位：现代SI指定实体与精确NA；查阅：2026-11-17；状态：`verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE nist

- NIST CODATA常数表：https://physics.nist.gov/cuu/pdf/all.pdf
- 定位：PDF第6页R与理想气体Vm；查阅：2026-11-17；状态：`verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE chem_standard

- 董总化学课程标准：https://elearning.dongzong.my/pluginfile.php/136742/mod_resource/content/3/Curriculum%20Standard%20for%20Chemistry.pdf
- 定位：PDF第2–3页原子分子/化学计算；查阅：2026-11-17；状态：`partially_verified`；用途：`curriculum`。
- 边界：已取得相关页；版本年与学校实际课本仍待核实。

### SOURCE os_motion

- OpenStax College Physics 2e运动学：https://openstax.org/books/college-physics-2e/pages/2-introduction-to-one-dimensional-kinematics
- 定位：第2章及相关分项；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_mechanics

- OpenStax College Physics 2e第二定律与系统：https://openstax.org/books/college-physics-2e/pages/4-3-newtons-second-law-of-motion-concept-of-a-system
- 定位：4.3，其他具体实验方案需另核；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_water

- OpenStax Biology 2e 2-2-water：https://openstax.org/books/biology-2e/pages/2-2-water
- 定位：2-2-water；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_carbon

- OpenStax Biology 2e 2-3-carbon：https://openstax.org/books/biology-2e/pages/2-3-carbon
- 定位：2-3-carbon；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_carbohydrates

- OpenStax Biology 2e 3-2-carbohydrates：https://openstax.org/books/biology-2e/pages/3-2-carbohydrates
- 定位：3-2-carbohydrates；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_lipids

- OpenStax Biology 2e 3-3-lipids：https://openstax.org/books/biology-2e/pages/3-3-lipids
- 定位：3-3-lipids；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_proteins

- OpenStax Biology 2e 3-4-proteins：https://openstax.org/books/biology-2e/pages/3-4-proteins
- 定位：3-4-proteins；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_nucleic

- OpenStax Biology 2e 3-5-nucleic-acids：https://openstax.org/books/biology-2e/pages/3-5-nucleic-acids
- 定位：3-5-nucleic-acids；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_microscope

- OpenStax Biology 2e 4-1-studying-cells：https://openstax.org/books/biology-2e/pages/4-1-studying-cells
- 定位：4-1-studying-cells；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_prokaryotes

- OpenStax Biology 2e 4-2-prokaryotic-cells：https://openstax.org/books/biology-2e/pages/4-2-prokaryotic-cells
- 定位：4-2-prokaryotic-cells；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_cells

- OpenStax Biology 2e 4-3-eukaryotic-cells：https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells
- 定位：4-3-eukaryotic-cells；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_membranes

- OpenStax Biology 2e 5-1-components-and-structure：https://openstax.org/books/biology-2e/pages/5-1-components-and-structure
- 定位：5-1-components-and-structure；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_passive

- OpenStax Biology 2e 5-2-passive-transport：https://openstax.org/books/biology-2e/pages/5-2-passive-transport
- 定位：5-2-passive-transport；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_active

- OpenStax Biology 2e 5-3-active-transport：https://openstax.org/books/biology-2e/pages/5-3-active-transport
- 定位：5-3-active-transport；查阅：2026-11-17；状态：`partially_verified`；用途：`science`。
- 边界：科学事实/模型核对，不证明2027考试范围；制作前仍须复核精确图形。

### SOURCE os_enzymes

- OpenStax biology-2e 6-5-enzymes：https://openstax.org/books/biology-2e/pages/6-5-enzymes
- 定位：6-5-enzymes；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_respiration

- OpenStax biology-2e 7-4-oxidative-phosphorylation：https://openstax.org/books/biology-2e/pages/7-4-oxidative-phosphorylation
- 定位：7-4-oxidative-phosphorylation；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_fermentation

- OpenStax biology-2e 7-5-metabolism-without-oxygen：https://openstax.org/books/biology-2e/pages/7-5-metabolism-without-oxygen
- 定位：7-5-metabolism-without-oxygen；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_atp

- OpenStax biology-2e 6-4-atp-adenosine-triphosphate：https://openstax.org/books/biology-2e/pages/6-4-atp-adenosine-triphosphate
- 定位：6-4-atp-adenosine-triphosphate；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_calvin

- OpenStax biology-2e 8-3-using-light-energy-to-make-organic-molecules：https://openstax.org/books/biology-2e/pages/8-3-using-light-energy-to-make-organic-molecules
- 定位：8-3-using-light-energy-to-make-organic-molecules；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_light

- OpenStax biology-2e 8-2-the-light-dependent-reactions-of-photosynthesis：https://openstax.org/books/biology-2e/pages/8-2-the-light-dependent-reactions-of-photosynthesis
- 定位：8-2-the-light-dependent-reactions-of-photosynthesis；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_isotopes

- OpenStax chemistry-2e 2-3-atomic-structure-and-symbolism：https://openstax.org/books/chemistry-2e/pages/2-3-atomic-structure-and-symbolism
- 定位：2-3-atomic-structure-and-symbolism；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_electrons

- OpenStax chemistry-2e 6-4-electronic-structure-of-atoms-electron-configurations：https://openstax.org/books/chemistry-2e/pages/6-4-electronic-structure-of-atoms-electron-configurations
- 定位：6-4-electronic-structure-of-atoms-electron-configurations；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_bohr

- OpenStax chemistry-2e 6-2-the-bohr-model：https://openstax.org/books/chemistry-2e/pages/6-2-the-bohr-model
- 定位：6-2-the-bohr-model；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_quantum

- OpenStax chemistry-2e 6-3-development-of-quantum-theory：https://openstax.org/books/chemistry-2e/pages/6-3-development-of-quantum-theory
- 定位：6-3-development-of-quantum-theory；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问标题与相关内容；仅核对相关原则，未审定整章或复制插图。

### SOURCE os_atomic_history

- OpenStax chemistry-2e 2-1-early-ideas-in-atomic-theory：https://openstax.org/books/chemistry-2e/pages/2-1-early-ideas-in-atomic-theory
- 定位：Dalton postulates、守恒、定比/倍比；普通化学变化模型；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问相关正文核对原则；不复制原图或指定题例，不代表2027考试范围或整课审定。

### SOURCE os_formula_mass

- OpenStax chemistry-2e 3-1-formula-mass-and-the-mole-concept：https://openstax.org/books/chemistry-2e/pages/3-1-formula-mass-and-the-mole-concept
- 定位：Formula Mass及mol/实体换算；现代精确NA另以BIPM为准；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问相关正文核对原则；不复制原图或指定题例，不代表2027考试范围或整课审定。

### SOURCE os_empirical

- OpenStax chemistry-2e 3-2-determining-empirical-and-molecular-formulas：https://openstax.org/books/chemistry-2e/pages/3-2-determining-empirical-and-molecular-formulas
- 定位：质量组成、实验式和分子式计算；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问相关正文核对原则；不复制原图或指定题例，不代表2027考试范围或整课审定。

### SOURCE os_equations

- OpenStax chemistry-2e 4-1-writing-and-balancing-chemical-equations：https://openstax.org/books/chemistry-2e/pages/4-1-writing-and-balancing-chemical-equations
- 定位：系数、原子守恒、完整及净离子方程式；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问相关正文核对原则；不复制原图或指定题例，不代表2027考试范围或整课审定。

### SOURCE os_reaction_types

- OpenStax chemistry-2e 4-2-classifying-chemical-reactions：https://openstax.org/books/chemistry-2e/pages/4-2-classifying-chemical-reactions
- 定位：沉淀/酸碱/氧化还原分类标准与反应条件；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问相关正文核对原则；不复制原图或指定题例，不代表2027考试范围或整课审定。

### SOURCE os_stoichiometry

- OpenStax chemistry-2e 4-3-reaction-stoichiometry：https://openstax.org/books/chemistry-2e/pages/4-3-reaction-stoichiometry
- 定位：计量系数与mol、质量转换；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问相关正文核对原则；不复制原图或指定题例，不代表2027考试范围或整课审定。

### SOURCE os_yields

- OpenStax chemistry-2e 4-4-reaction-yields：https://openstax.org/books/chemistry-2e/pages/4-4-reaction-yields
- 定位：Limiting Reactant与Percent Yield；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问相关正文核对原则；不复制原图或指定题例，不代表2027考试范围或整课审定。

### SOURCE os_plant_nutrition

- OpenStax biology-2e 31-1-nutritional-requirements-of-plants：https://openstax.org/books/biology-2e/pages/31-1-nutritional-requirements-of-plants
- 定位：Essential Nutrients、Mg功能、缺素及水培相关段落；查阅：2026-11-18；状态：`partially_verified`；用途：`science`。
- 边界：本轮访问相关正文核对原则；不复制原图或指定题例，不代表2027考试范围或整课审定。

## 完整逐图要求

以下每条ID与JSON一一对应。所有“新增／重绘／修正”均未制作；精确来源与待核实边界均保留。

### ILL-ASSET-P3_2 · 图 3-2　一维坐标系：原点、正方向、单位长度，位移 = 末位置坐标 − 初位置坐标

- 归属：物理／原第3章 直线运动／3.2 参照物、坐标系和参照系。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：把坐标、方向与位移对应到同一数轴
- 绘图要求：
  - 保留A=-2m、B=3m及向右+5m位移箭头
  - 原点0与坐标单位m同时保留，红蓝颜色之外还用A/B区分
- 必须文字标注：x/m；O；A(-2m)；B(3m)；Δx=+5m；正方向。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p3_2.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.2]；data/notes/phys03.json /3.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P3_3 · 图 3-3　路程是曲线的长度，位移是从 A 指向 B 的有向线段

- 归属：物理／原第3章 直线运动／3.3 路程和位移。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：区分曲线路程与初末位移
- 绘图要求：
  - 蓝曲线长度不标虚构数值，红箭头从A直指B
  - 明确轨迹示意并非x-t图；保留位移大小≤路程
- 必须文字标注：A；B；路程；位移；位移大小≤路程。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p3_3.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.3]；data/notes/phys03.json /3.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P3_5A · 图 3-5a　s–t 图：斜率 = 速度

- 归属：物理／原第3章 直线运动／3.5 匀速直线运动的图象。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：从位置时间图的割线斜率读取匀速速度
- 绘图要求：
  - 保留两点Δs、Δt投影，纵轴s表示相对原点的位置/位移约定需统一
  - 无数值刻度时标符号示意，不能被当作例题数值图
- 必须文字标注：t/s；s/m；Δs；Δt；v=Δs/Δt。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p3_5a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.5]；data/notes/phys03.json /3.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

建议跨节引用（尚未渲染）：物理3／3.4。

### ILL-ASSET-P3_5B · 图 3-5b　v–t 图：矩形面积 = 位移

- 归属：物理／原第3章 直线运动／3.5 匀速直线运动的图象。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：用速度时间矩形面积表示位移
- 绘图要求：
  - 水平速度v对应恒速；阴影宽为t、高为v
  - 面积标v·t，补充图注该面板为v>0情境，不代替负面积题
- 必须文字标注：t/s；v/(m/s)；v；t；s=vt。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p3_5b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.5]；data/notes/phys03.json /3.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

建议跨节引用（尚未渲染）：物理3／3.4。

### ILL-ASSET-P3_6 · 图 3-6　s–t 曲线：割线斜率是平均速度，切线斜率是瞬时速度

- 归属：物理／原第3章 直线运动／3.6 变速直线运动　平均速度和瞬时速度。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：区分割线平均速度与切线瞬时速度
- 绘图要求：
  - 沿用现有抛物线几何与割线/切线，给曲线一个明确函数和坐标变换后复核切线导数
  - 标出割线两个端点、切点的时间区间；当前只有颜色与斜率结论，无法直接验证数值
  - 不以示意图伪装测量数据
- 必须文字标注：s/m；t/s；平均速度对应区间；切点时刻；割线；切线。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p3_6.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.6]；data/notes/phys03.json /3.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P3_7 · 图 3-7　v–t 图：斜率 = Δv/Δt = 加速度

- 归属：物理／原第3章 直线运动／3.7 变速直线运动的加速度。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：把v-t斜率对应加速度
- 绘图要求：
  - 保留非零截距u，防止误用v/t
  - Δv和Δt都取相同两个点，线性图仅表示恒a
- 必须文字标注：v/(m/s)；t/s；Δv；Δt；a=Δv/Δt。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p3_7.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.7]；data/notes/phys03.json /3.7。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P3_8 · 图 3-8　v–t 图线下的面积 = 位移：梯形 = 矩形 ut + 三角形 ½at²

- 归属：物理／原第3章 直线运动／3.8 匀加速直线运动。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：用梯形分拆推导恒加速度位移式
- 绘图要求：
  - 矩形面积ut与上方三角形面积½at²不重叠、不重复
  - 明确当前为u≥0、a>0面板；反向运动另用分段图
- 必须文字标注：u；v；t；ut；½at²；s=(u+v)t/2。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p3_8.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.8]；data/notes/phys03.json /3.8。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P3_9 · 图 3-9　频闪示意：相等时间内位移比 1 : 3 : 5 : 7

- 归属：物理／原第3章 直线运动／3.9 自由落体运动。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：用等时间频闪间距说明自由落体
- 绘图要求：
  - 各点位置距起点应按0、1、4、9、16等比例；段距1:3:5:7
  - t=0为静止释放、近地恒g、阻力忽略；g箭头竖直向下
- 必须文字标注：0；T；2T；3T；4T；1:3:5:7；g。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p3_9.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.9]；data/notes/phys03.json /3.9。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P4_2 · 图 4-2　斜面上下滑物块的受力图：mg 竖直向下，N 垂直斜面向外，f 沿斜面向上

- 归属：物理／原第4章 牛顿运动定律／4.2 力的种类。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：隔离斜面物块并识别实际外力
- 绘图要求：
  - 重力竖直向下，支持力垂面向外，滑动摩擦沿面向上
  - 明示物块相对斜面向下滑；不要再画ma作力
- 必须文字标注：mg；N；f_k；θ；相对下滑。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p4_2.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.2]；data/notes/phys04.json /4.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P4_3A · 图 4-3a　平行四边形法则：对角线是合力 R

- 归属：物理／原第4章 牛顿运动定律／4.3 力的合成与分解。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：用平行四边形合成两力
- 绘图要求：
  - 由共同起点画F1、F2，两虚线平行于对应邻边
  - θ弧线必须跨F1与F2，不是F1与R；合力端点为向量和
- 必须文字标注：F₁；F₂；R；θ；共同作用点。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p4_3a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.3]；data/notes/phys04.json /4.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P4_3B · 图 4-3b　斜面上重力的分解：沿斜面 mg sinθ，垂直斜面 mg cosθ

- 归属：物理／原第4章 牛顿运动定律／4.3 力的合成与分解。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：解释斜面重力的两个正交分量
- 绘图要求：
  - mg竖直向下；mg sinθ向下坡；mg cosθ压向斜面
  - 分量仅为同一重力的投影，图注注明不能与mg同时再加一次
- 必须文字标注：mg；mg sinθ；mg cosθ；θ；投影轴。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p4_3b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.3]；data/notes/phys04.json /4.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P4_6 · 图 4-6　撞墙反弹：动量变化 = 末动量 − 初动量（矢量差）

- 归属：物理／原第4章 牛顿运动定律／4.6 动量。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：把反弹动量变化画成有向差
- 绘图要求：
  - 初+3、末-2、变化-5kg·m/s长度同一比例尺
  - Δp为末减初；零点、右正方向和单位保留
- 必须文字标注：p初=+3.0kg·m/s；p末=-2.0kg·m/s；Δp=-5.0kg·m/s；右正。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p4_6.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.6]；data/notes/phys04.json /4.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P4_7A · 图 4-7a　连接体：整体求 a，隔离求 T

- 归属：物理／原第4章 牛顿运动定律／4.7 牛顿第二运动定律。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：区分连接体整体与隔离法
- 绘图要求：
  - 现图可保留装置概览，但求张力另设两块各自水平受力图
  - 在同一比例中给前块F、反向T，后块正向T；竖直mg/N标为平衡或单独面板
  - 不得把内部两T画到同一物体上
- 必须文字标注：m₁；m₂；F；T；a；光滑水平面。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p4_7a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.7]；data/notes/phys04.json /4.7。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P4_7B · 图 4-7b　滑轮：两物体加速度大小相同

- 归属：物理／原第4章 牛顿运动定律／4.7 牛顿第二运动定律。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：识别阿特伍德装置力与约束
- 绘图要求：
  - 保留两侧T、m1g、m2g实际箭头，另把a箭头放置受力图外并用不同线型
  - m1>m2时两a大小相等方向相反；轻绳、无伸长、滑轮理想条件写图注
  - 未来按具体质量计算箭头比例，不把两个T与两重力画等长
- 必须文字标注：T；m₁g；m₂g；a；m₁>m₂；轻绳/理想滑轮。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p4_7b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.7]；data/notes/phys04.json /4.7。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-P4_8 · 图 4-8　左：书受到的一对平衡力；右：作用力与反作用力 N 与 N′

- 归属：物理／原第4章 牛顿运动定律／4.8 牛顿第三运动定律。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：区分同体平衡力与不同受体的作用反作用
- 绘图要求：
  - 左右分面：左图N和mg都作用书；右图N作用书、N′作用桌
  - 每根箭头注明施力者/受力者，不因共线而相互抵消
- 必须文字标注：地球对书mg；桌对书N；书对桌N′；同体平衡；不同受体配对。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/p4_8.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.8]；data/notes/phys04.json /4.8。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C3_1 · 图 3-1　同温同压下，相同体积含相同分子数：1 体积 H₂ + 1 体积 Cl₂ → 2 体积 HCl

- 归属：化学／原第3章 原子与分子／3.1 原子学说与分子学说。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：用气体分子图解释阿伏加德罗关系
- 绘图要求：
  - 左右各4个H2/Cl2分子，产物8个HCl，原子颜色数守恒
  - 体积1:1:2限定同温同压气态模型；非实验操作指引，不画点火步骤
- 必须文字标注：同温同压；H₂；Cl₂；HCl；1:1:2体积比；原子图例。
- 科学依据：chem_standard（curriculum；partially_verified）；os_atomic_history（science_not_exam_scope；partially_verified）；os_equations（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c3_1.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.1]；data/notes/chem03.json /3.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C3_2 · 图 3-2　倍比定律：碳的质量固定为 12 g 时，两种氧化物中氧的质量比是 1 : 2

- 归属：化学／原第3章 原子与分子／3.2 物质组成及化学反应中的基本定律。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：固定一种元素质量后比较倍比
- 绘图要求：
  - C两行均12g；O分别16、32g，条长按质量同一比例
  - 只能比较固定C后的氧质量，不直接拿任意样品总量比
- 必须文字标注：CO；CO₂；C 12g；O 16g；O 32g；1:2。
- 科学依据：chem_standard（curriculum；partially_verified）；os_atomic_history（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c3_2.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.2]；data/notes/chem03.json /3.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C3_3 · 图 3-3　相对原子质量：以 ¹²C 质量的 1/12 为一格（1 u），其他原子数格数

- 归属：化学／原第3章 原子与分子／3.3 原子与相对原子质量。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：区分相对原子质量比与质量单位
- 绘图要求：
  - 碳-12画12个相同格，H约1格、O约16格
  - 单格表示1u，Ar本身无单位；核大小/格子不是原子真实形状
- 必须文字标注：¹²C；1u=m(¹²C)/12；Ar(H)≈1；Ar(O)≈16；Ar无单位。
- 科学依据：chem_standard（curriculum；partially_verified）；os_isotopes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c3_3.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.3]；data/notes/chem03.json /3.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C3_5 · 图 3-5　由元素质量（或百分比）求化学式的步骤

- 归属：化学／原第3章 原子与分子／3.5 确定化学式的方法。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：从质量比转换成原子数比及分子式
- 绘图要求：
  - 保留除Ar、除最小值、整体化整数和Mr/实验式量的条件分支
  - 1.5/1.33不能就地四舍五入；分子式倍数仅在给出Mr时确定
- 必须文字标注：元素质量；m/Ar；最简比；实验式；Mr/实验式量。
- 科学依据：chem_standard（curriculum；partially_verified）；os_empirical（science_not_exam_scope；partially_verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c3_5.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.5]；data/notes/chem03.json /3.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C3_6 · 图 3-6　以 n 为中心：质量、微粒数、气体体积的换算

- 归属：化学／原第3章 原子与分子／3.6 物质的量。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：以mol为中心整合质量、实体和气体体积
- 绘图要求：
  - 四组箭头乘除方向正确；保留温度、压力和仅气体的边界
  - 现代NA精确值放图注，计算按题给值；Vm不是固定22.4
  - 现文件可复用，未来无须为增加数量另画同义关系图
- 必须文字标注：m/g；n/mol；N/个；V/L；M；N_A；V_m；273.15K/101.325kPa。
- 科学依据：chem_standard（curriculum；partially_verified）；bipm（science；verified）；nist（science；verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c3_6.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.6]；data/notes/chem03.json /3.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C4_1 · 图 4-1　化学方程式的量的含义：系数比 = 物质的量比

- 归属：化学／原第4章 化学方程式与化学计算／4.1.1 表示化学反应的语言——化学方程式。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：把系数、mol、质量和气体体积区分
- 绘图要求：
  - 表内2:1:2分子/mol与4:32:36质量分别标单位
  - 表头显式写H2(g)、O2(g)、H2O(g)；现底注虽已加条件，水物态应同时出现在表头防误读
  - 仅展示理论气态同温同压体积比，不与0℃液水情境混用
- 必须文字标注：2H₂(g)+O₂(g)→2H₂O(g)；粒子数比；mol；g；同温同压、均气态。
- 科学依据：chem_standard（curriculum；partially_verified）；os_equations（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c4_1.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.1.1]；data/notes/chem04.json /4.1.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C4_2 · 图 4-2　四种基本反应类型的示意

- 归属：化学／原第4章 化学方程式与化学计算／4.1.2 化学反应的类型。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：按反应形式比较四类模式
- 绘图要求：
  - A/B/C/D为元素或物质类别符号示意，不冒充真实分子空间结构
  - 逐行原子符号计数一致；增加图注分类可与氧化还原/中和重叠
- 必须文字标注：化合；分解；置换；复分解；A/B/C/D图例。
- 科学依据：chem_standard（curriculum；partially_verified）；os_reaction_types（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c4_2.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.1.2]；data/notes/chem04.json /4.1.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C4_3 · 图 4-3　配平 C₂H₆ 的燃烧：先配 C，再配 H，最后配 O

- 归属：化学／原第4章 化学方程式与化学计算／4.1.3 化学方程式的配平。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：按C-H-O次序示范系数配平
- 绘图要求：
  - 每行只改系数不改下标，临时7/2后全乘2
  - 最终2C2H6+7O2→4CO2+6H2O，C4/H12/O14核对
- 必须文字标注：先C；再H；后O；同乘2；C/H/O原子守恒。
- 科学依据：chem_standard（curriculum；partially_verified）；os_equations（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c4_3.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.1.3]；data/notes/chem04.json /4.1.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C4_4 · 图 4-4　按方程式计算：先转成 n，再用系数比，最后转出所求量

- 归属：化学／原第4章 化学方程式与化学计算／4.2.1 计算反应物和生成物的量。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：在mol层跨方程式做计量
- 绘图要求：
  - 乘c/a明确分子分母分别是目标/已知物系数
  - 各次质量/体积换算标自己的M或Vm，气体条件先确认
- 必须文字标注：m/V/N→n(A)；系数比c/a；n(B)→目标量；物质和单位。
- 科学依据：chem_standard（curriculum；partially_verified）；os_stoichiometry（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c4_4.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.2.1]；data/notes/chem04.json /4.2.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C4_5 · 图 4-5　N₂ + 3H₂ → 2NH₃：6 个 H₂ 先用完，决定只能生成 4 个 NH₃，剩 1 个 N₂

- 归属：化学／原第4章 化学方程式与化学计算／4.2.3 利用限量反应物的计算。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：用离散粒子识别限量与剩余
- 绘图要求：
  - 初3N2与6H2，末4NH3与1N2，每个N/H原子数逐个核对
  - H2先用完，n/系数比较2<3；不要把剩余N2算作不曾反应
- 必须文字标注：N₂+3H₂→2NH₃；3N₂；6H₂；4NH₃；剩1N₂；H₂限量。
- 科学依据：chem_standard（curriculum；partially_verified）；os_yields（science_not_exam_scope；partially_verified）；os_stoichiometry（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c4_5.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.2.3]；data/notes/chem04.json /4.2.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C5_1A · 图 5-1a　原子模型的演变：汤姆生 → 卢瑟福 → 玻尔

- 归属：化学／原第5章 原子结构／5.1 原子模型。
- 类型／动作／优先级：结构示意图；重绘；P0。
- 教学目的：以各模型要解释的证据比较原子模型
- 绘图要求：
  - 玻尔氢原子面板一次只画一个电子，现图三个轨道各画电子易被读成三电子氢原子
  - 把可取能级与同一电子的不同状态分开，历史模型不等同现代真实轨迹
  - 汤姆生/卢瑟福模型分别注明历史假设
- 必须文字标注：汤姆生；卢瑟福；玻尔(氢/单电子示例)；证据；局限。
- 科学依据：os_bohr（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_1a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.1]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C5_1B · 图 5-1b　α 粒子散射实验：三种现象，三个结论

- 归属：化学／原第5章 原子结构／5.1 原子模型。
- 类型／动作／优先级：实验装置图；局部修正；P1。
- 教学目的：将α散射观察与原子核模型推理分开
- 绘图要求：
  - 现图可作粒子路径，但补出准直、薄金箔、环形探测位置的概念布局
  - 多数直穿/少数大角/极少回散不是画三个等概率样本
  - 不提供放射源获取、剂量或操作指引，仅历史原理图
- 必须文字标注：准直α束；薄金箔；探测屏；直穿/偏转/回散；路径示意。
- 科学依据：os_bohr（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_1b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.1]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C5_2A · 图 5-2a　原子符号与三种基本粒子

- 归属：化学／原第5章 原子结构／5.2 原子序数、质量数和同位素。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：计算同位素与离子中粒子数
- 绘图要求：
  - 23/11Na+的质子11、中子12、电子10必须一致
  - A和Z为整数计数，不能把A当精确相对原子质量
- 必须文字标注：A=23；Z=11；+电荷；p=11；n=12；e=10。
- 科学依据：os_isotopes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_2a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.2]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

建议跨节引用（尚未渲染）：化学3／3.3。

### ILL-ASSET-C5_2B · 图 5-2b　氯的质谱图：同位素丰度与相对原子质量

- 归属：化学／原第5章 原子结构／5.2 原子序数、质量数和同位素。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：从质谱丰度推平均质量并限制m/z的解释
- 绘图要求：
  - 横轴应标m/z，只有单电荷离子近似时峰位才可用35、37质量数近似
  - 丰度75.8/24.2为教学近似须注明，非本次仪器实测
  - 加权使用同位素相对质量；以质量数代用时标近似
- 必须文字标注：m/z；相对丰度/%；单电荷假设；³⁵Cl/³⁷Cl；平均近似。
- 科学依据：os_isotopes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_2b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.2]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C5_3A · 图 5-3a　连续光谱、发射光谱（线状光谱）和吸收光谱

- 归属：化学／原第5章 原子结构／5.3 核外电子的能阶。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：对齐发射亮线与吸收暗线
- 绘图要求：
  - 400-700nm用同一线性坐标映射，410/434/486/656位置一致
  - 颜色仅辅助且加数值；只表示部分可见氢谱线
- 必须文字标注：波长/nm；410；434；486；656；连续/发射/吸收。
- 科学依据：os_bohr（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_3a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.3]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C5_3B · 图 5-3b　氢原子能级图与三个线系

- 归属：化学／原第5章 原子结构／5.3 核外电子的能阶。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：把电子跃迁方向与正光子能量关联
- 绘图要求：
  - 纵轴现为非比例须保留警告，建议将实际E=-13.6/n²按比例与放大高能区分面
  - 向下发射、向上吸收，光子能量取正差值
  - 巴耳末可见图仅列已绘谱线，不把全线系所有跃迁都称可见光
- 必须文字标注：E/eV；n=1…∞；ΔE=hν>0；发射/吸收；非比例或断轴说明。
- 科学依据：os_bohr（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_3b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.3]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C5_4A · 图 5-4a　s 轨域与 p 轨域的形状

- 归属：化学／原第5章 原子结构／5.4 原子核外电子的排布。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：将轨域概率分布与固定轨道区分
- 绘图要求：
  - s球/pxpy pz空间方向采用等概率包络示意，边界不是硬壳
  - 标所选包络约定概率，例如90%，不能称全部电子只在边界内
  - n/l量子数和轨域数适用范围在图注说明
- 必须文字标注：s；pₓ/p_y/p_z；概率包络；非固定轨迹；坐标轴。
- 科学依据：os_quantum（science；partially_verified）；os_electrons（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_4a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.4]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C5_4B · 图 5-4b　构造原理：电子填入的顺序

- 归属：化学／原第5章 原子结构／5.4 原子核外电子的排布。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：用构造顺序辅助书写中性原子电子组态
- 绘图要求：
  - 对角箭头顺序与1s2s2p3s3p4s3d…文字一致
  - 注明为常见基态排布助记；Cr/Cu例外及阳离子失电子顺序另处理
- 必须文字标注：n；s/p/d/f；填入方向；4s/3d；模型边界。
- 科学依据：os_quantum（science；partially_verified）；os_electrons（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_4b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.4]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C5_4C · 图 5-4c　能级高低：4s 低于 3d；每个方框一个轨域

- 归属：化学／原第5章 原子结构／5.4 原子核外电子的排布。
- 类型／动作／优先级：精确科学SVG；局部修正；P0。
- 教学目的：避免把4s/3d相对能量当成全元素通则
- 绘图要求：
  - 4s低于3d只在该填充近似/具体中性原子语境使用
  - 加入过渡金属与离子能级顺序会变的醒目标注，不能从图直接推Fe失电子顺序
  - 框数s1/p3/d5/f7与容量核对
- 必须文字标注：能量；中性原子近似；4s/3d；离子需另判断；轨域数/容量。
- 科学依据：os_quantum（science；partially_verified）；os_electrons（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_4c.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.4]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-C5_4D · 图 5-4d　轨域表示式：正确与错误

- 归属：化学／原第5章 原子结构／5.4 原子核外电子的排布。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：用反例辨识鲍利与汉德规则
- 绘图要求：
  - 同框至多反向两箭头，简并轨域先单占同自旋
  - 正确与错误示例同时注明规则原因；自旋箭头不是电子空间移动轨迹
- 必须文字标注：1s；2s；2p；C/N/O/Be；鲍利；汉德；未成对电子。
- 科学依据：os_quantum（science；partially_verified）；os_electrons（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/c5_4d.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem05.js sections[id=5.4]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B1_1 · 图 1-1　水分子的极性与分子间的氢键（虚线）

- 归属：生物／原第1章 生物是由什么组成的／1.1 生命离不开水。
- 类型／动作／优先级：结构示意图；局部修正；P2。
- 教学目的：由水分子极性解释分子间氢键
- 绘图要求：
  - 将共价O-H实线与分子间O···H虚线明确区分
  - 弯曲形标不按键角比例；若加104.5°必须按近似角度重新计算位置，不能把当前近直角当精确结构
  - δ标为部分电荷，不画完整O2-/H+离子
- 必须文字标注：O；H；δ−；δ+；共价键；氢键；示意、非比例。
- 科学依据：os_water（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_1.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.1]；data/notes/bio01.json /1.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B1_3A · 图 1-3a　糖类的分类：单糖 → 二糖 → 多糖

- 归属：生物／原第1章 生物是由什么组成的／1.3 能量的主要来源——糖类。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：区分糖类分类与特定缩合关系
- 绘图要求：
  - 分类树与反应箭头拆成不同图层/面板
  - 明确葡+葡→麦芽糖、葡+果→蔗糖、葡+半乳→乳糖；淀粉/糖原/纤维素分别由葡萄糖单元构成
  - 删去二糖整行指向多糖整行的缩合箭头；只加警告脚注仍有误读风险
- 必须文字标注：单糖；二糖；多糖；糖苷键；各二糖组成；贮能/结构功能。
- 科学依据：os_carbohydrates（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_3a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.3]；data/notes/bio01.json /1.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B1_3B · 图 1-3b　缩合反应与水解作用（以两个葡萄糖为例）

- 归属：生物／原第1章 生物是由什么组成的／1.3 能量的主要来源——糖类。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：显示糖苷键形成与水解方向
- 绘图要求：
  - 六边形G为葡萄糖简图，不代表准确碳原子键线结构
  - 正向缩合失一水、逆向水解耗水；酯键、肽键、磷酸二酯键作比较例不能混同
- 必须文字标注：G；糖苷键；缩合−H₂O；水解+H₂O；简图图例。
- 科学依据：os_carbohydrates（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_3b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.3]；data/notes/bio01.json /1.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B1_4A · 图 1-4a　三甘油酯：1 个甘油 + 3 个脂肪酸，通过 3 个酯键连接

- 归属：生物／原第1章 生物是由什么组成的／1.4 贮存能量的物质——脂质。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：解释三甘油酯结构与饱和度
- 绘图要求：
  - 1甘油与3脂肪酸通过3酯键相连
  - 顺式双键弯折与饱和直链作定性比较；不要把所有不饱和双键都画为相同几何
- 必须文字标注：甘油；脂肪酸×3；酯键×3；饱和；顺式不饱和；脱3H₂O。
- 科学依据：os_lipids（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_4a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.4]；data/notes/bio01.json /1.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B1_4B · 图 1-4b　磷脂的结构，以及在水中形成的双层

- 归属：生物／原第1章 生物是由什么组成的／1.4 贮存能量的物质——脂质。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：用两亲性解释双层自组装
- 绘图要求：
  - 两侧均是水相，亲水头朝水、疏水尾相向
  - 符号P表示含磷头基示意，不等于头部只有单个裸磷原子
- 必须文字标注：水；亲水头；疏水尾；磷脂双层；两亲性。
- 科学依据：os_lipids（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_4b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.4]；data/notes/bio01.json /1.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

建议跨节引用（尚未渲染）：生物2／2.2。

### ILL-ASSET-B1_5A · 图 1-5a　氨基酸的通式，以及肽键的形成

- 归属：生物／原第1章 生物是由什么组成的／1.5 生命活动的承担者——蛋白质。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：定位氨基酸基团及肽键
- 绘图要求：
  - 中心碳连氨基、羧基、H、R，R可为H
  - 肽键红色仅覆盖-C(=O)-NH-连接，缩合脱水计量一致；酸碱离子化状态按简式图注
- 必须文字标注：氨基；羧基；R基；肽键；二肽；H₂O。
- 科学依据：os_proteins（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_5a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.5]；data/notes/bio01.json /1.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B1_5B · 图 1-5b　蛋白质的四个结构层次与维持它们的作用力

- 归属：生物／原第1章 生物是由什么组成的／1.5 生命活动的承担者——蛋白质。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把蛋白四层结构与稳定作用对应
- 绘图要求：
  - 二级示例应画可辨α螺旋或β折叠而非任意锯齿
  - 四级必须表现独立多肽亚基，不只四色圆块；图注并非每种蛋白都有四级
  - 相互作用位置区分主链氢键与R基作用，二硫键不是所有蛋白必有
- 必须文字标注：一级序列；二级α/β；三级折叠；四级亚基；肽键/氢键/二硫键。
- 科学依据：os_proteins（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_5b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.5]；data/notes/bio01.json /1.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B1_6A · 图 1-6a　核苷酸的组成

- 归属：生物／原第1章 生物是由什么组成的／1.6 遗传信息的携带者——核酸。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：标识核苷酸三个组成与DNA/RNA差异
- 绘图要求：
  - 磷酸、五碳糖、碱基连接位置作组成示意而非完整结构式
  - DNA/RNA糖与T/U区别独立列表，不能只凭A判断核酸种类
- 必须文字标注：磷酸；五碳糖；碱基；脱氧核糖/核糖；ATGC/AUGC。
- 科学依据：os_nucleic（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_6a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.6]；data/notes/bio01.json /1.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B1_6B · 图 1-6b　DNA 的双链与碱基配对（反向平行）

- 归属：生物／原第1章 生物是由什么组成的／1.6 遗传信息的携带者——核酸。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：说明DNA反向平行与互补配对
- 绘图要求：
  - 两链方向相反；A-T两虚线、G-C三虚线
  - 糖磷酸骨架与碱基间氢键区分；梯形平面是双螺旋展开简图
- 必须文字标注：5′；3′；A-T；G-C；2/3氢键；糖磷酸骨架。
- 科学依据：os_nucleic（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_6b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.6]；data/notes/bio01.json /1.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

建议跨节引用（尚未渲染）：生物2／2.4。

### ILL-ASSET-B1_SUM · 图 1-6c　本章四类有机分子对照表

- 归属：生物／原第1章 生物是由什么组成的／1.6 遗传信息的携带者——核酸。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：总览四类有机物但保留脂质例外
- 绘图要求：
  - 脂质栏以三甘油酯为例的脚注须保留
  - 标磷脂含P、部分含N，不能写所有脂质都是甘油+脂肪酸
  - 此图主小节1.6、关联1.3/1.4/1.5，只记一张不重复复制
- 必须文字标注：糖类；脂质＊；蛋白质；核酸；单体/组成；连接键；例外注。
- 科学依据：os_nucleic（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b1_sum.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.6]；data/notes/bio01.json /1.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

建议跨节引用（尚未渲染）：生物1／1.3；生物1／1.4；生物1／1.5。

### ILL-ASSET-B2_1 · 图 2-1　原核细胞与真核细胞（示意）

- 归属：生物／原第2章 细胞的结构与功能／2.1 细胞是生物的基本单位。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：以核膜与细胞器比较原核/真核
- 绘图要求：
  - 原核要有DNA、核糖体、细胞膜，示意细菌壁需标典型而非所有原核
  - 两细胞绘图大小不表示真实等比例；形态不能替代谱系判断
- 必须文字标注：拟核；质粒(可有)；核糖体；细胞核；细胞膜；典型示意。
- 科学依据：os_microscope（science；partially_verified）；os_prokaryotes（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b2_1.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.1]；data/notes/bio02.json /2.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B2_2A · 图 2-2a　流动镶嵌模型

- 归属：生物／原第2章 细胞的结构与功能／2.2 细胞膜——物质进出的门户。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把膜组分位置与选择透过性关联
- 绘图要求：
  - 磷脂头尾、整合/外周蛋白、外侧糖链不颠倒
  - 胆固醇仅作为动物典型膜示例；通道开口示意不把所有整合蛋白视为空洞
- 必须文字标注：细胞外；细胞质；磷脂双层；整合蛋白；糖链；胆固醇。
- 科学依据：os_membranes（science；partially_verified）；os_passive（science；partially_verified）；os_active（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b2_2a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.2]；data/notes/bio02.json /2.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B2_2B · 图 2-2b　四种跨膜运输方式的比较

- 归属：生物／原第2章 细胞的结构与功能／2.2 细胞膜——物质进出的门户。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：比较扩散、一级主动运输和膜泡运输的物理路径
- 绘图要求：
  - 扩散箭头由高到低；一级主动从低到高并标ATP；离子梯度应考虑电化学条件
  - 胞吞/胞吐必须画膜内陷/膜融合前后，当前圆囊泡加直箭头不足以表示机制
  - 另设二级主动示意或明确本图不涵盖其能量耦联
- 必须文字标注：高/低；简单扩散；易化扩散；一级主动；ATP；胞吞内陷；胞吐融合。
- 科学依据：os_membranes（science；partially_verified）；os_passive（science；partially_verified）；os_active（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b2_2b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.2]；data/notes/bio02.json /2.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B2_3A · 图 2-3a　动物细胞的细胞器（示意）

- 归属：生物／原第2章 细胞的结构与功能／2.3 细胞器——系统内的分工协作。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：识别典型动物细胞器空间位置
- 绘图要求：
  - 各编号指向对应结构；粗面ER核糖体在外侧，不放入ER腔内
  - 画细胞膜而非细胞壁，示意图不表示所有动物细胞都有每种细胞器
- 必须文字标注：核；粗面ER；高尔基体；线粒体；溶酶体；中心体；核糖体。
- 科学依据：os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b2_3a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.3]；data/notes/bio02.json /2.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B2_3B · 图 2-3b　线粒体与叶绿体的结构

- 归属：生物／原第2章 细胞的结构与功能／2.3 细胞器——系统内的分工协作。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：由膜折叠与区室解释线粒体/叶绿体功能
- 绘图要求：
  - 线粒体嵴应连续连接内膜，不能用悬空短线代替内膜折叠
  - 叶绿体类囊体/基粒与双层包膜分开；光反应定位类囊体膜、碳反应定位基质
  - 核查引线终点及边缘标签，不让“基质”落到膜外
- 必须文字标注：外膜；内膜/嵴；线粒体基质；类囊体膜；基粒；叶绿体基质。
- 科学依据：os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b2_3b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.3]；data/notes/bio02.json /2.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B2_3C · 图 2-3c　分泌蛋白的合成、加工与运输

- 归属：生物／原第2章 细胞的结构与功能／2.3 细胞器——系统内的分工协作。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：区分分泌蛋白物流、供能与膜回收
- 绘图要求：
  - 核糖体翻译→ER→运输囊泡→高尔基体→分泌囊泡→胞吐应完整
  - 现末端囊泡字样放在细胞膜之后易误读，需把货物途径与膜融合边界重排
  - ATP旁路注明线粒体等供能来源；膜面积动态变化不画永久单向增减
- 必须文字标注：核糖体；粗面ER；囊泡；高尔基体；分泌囊泡；胞吐；ATP旁路/回收。
- 科学依据：os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b2_3c.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.3]；data/notes/bio02.json /2.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B2_4 · 图 2-4　细胞核的结构

- 归属：生物／原第2章 细胞的结构与功能／2.4 细胞核——细胞的控制中心。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把核膜核孔与染色质保留、RNA输出区分
- 绘图要求：
  - 核孔必须贯通双层核膜，ER连续到外核膜
  - 引线分开染色质与核孔，避免紫色染色质线视觉上穿孔进入ER
  - 把RNA/蛋白双向选择交通加小箭头，勿写任何DNA永不出核的绝对论
- 必须文字标注：双层核膜；核孔；核仁；染色质；外核膜-ER；RNA输出/蛋白输入。
- 科学依据：os_cells（science；partially_verified）；os_nucleic（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b2_4.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.4]；data/notes/bio02.json /2.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B2_5 · 图 2-5　相邻两个植物细胞之间的壁（剖面示意）

- 归属：生物／原第2章 细胞的结构与功能／2.5 细胞壁——细胞的保护外墙。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：说明壁层顺序和细胞间通道
- 绘图要求：
  - 从各细胞内部向外是膜、次生壁(若有)、初生壁、胞间层；另一侧镜像
  - 补出连续细胞膜衬里的胞间连丝，不把蓝色实体柱当自由敞孔
  - 强调并非所有植物细胞具次生壁；膜与壁两种边界不同
- 必须文字标注：细胞膜；次生壁(可有)；初生壁；胞间层；胞间连丝；细胞A/B。
- 科学依据：os_cells（science；partially_verified）；os_carbohydrates（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b2_5.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.5]；data/notes/bio02.json /2.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_1A · 图 3-1a　锁钥模型与诱导契合模型：酶–底物复合物形成，产物离开，酶不变

- 归属：生物／原第3章 细胞内物质和能量的转换／3.1 生物催化剂——酶。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：比较锁钥与诱导契合模型
- 绘图要求：
  - 三个阶段底物/产物与酶的颜色和数目连续
  - 诱导契合只表现可逆构象调整，不把酶整体水解
  - 标模型简化而非真实比例分子
- 必须文字标注：酶；底物；活性部位；ES复合物；产物；构象调整。
- 科学依据：os_enzymes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_1a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.1]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_1B · 图 3-1b　活化能：酶降低活化能，但不改变反应物和产物的能量

- 归属：生物／原第3章 细胞内物质和能量的转换／3.1 生物催化剂——酶。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：说明催化降低路径势垒而非改变总能差
- 绘图要求：
  - 两曲线相同反应物/产物能级，活化能都从反应物能级量起
  - 纵轴说明能量示意，不将无刻度曲线当定量测量
- 必须文字标注：反应进程；能量；Ea有酶/无酶；反应物；产物；总能差不变。
- 科学依据：os_enzymes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_1b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.1]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_2A · 图 3-2a　温度对酶活性的影响：低温不变性，高温变性

- 归属：生物／原第3章 细胞内物质和能量的转换／3.2 影响酶活性的因素。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：限制酶活性温度曲线的外推
- 绘图要求：
  - 最适约37℃只作特定酶/条件示例，不能代表全部人体酶
  - 删或限定每10℃速率倍增与高温必不可逆的绝对注释
  - 没有实测数据时写定性模型，不给伪实测刻度/误差线
- 必须文字标注：温度/℃；相对活性；具体酶/条件；可逆低温抑制；高温失活边界。
- 科学依据：os_enzymes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_2a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.2]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_2B · 图 3-2b　pH 对三种酶活性的影响

- 归属：生物／原第3章 细胞内物质和能量的转换／3.2 影响酶活性的因素。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：比较不同酶的最适pH
- 绘图要求：
  - 三条曲线共享同一pH轴，峰约2/7/8作为教学示意
  - 注明测定底物/缓冲条件未给，不能据曲线精确读活性数值
- 必须文字标注：pH；相对酶活性；胃蛋白酶；唾液淀粉酶；胰蛋白酶；示意。
- 科学依据：os_enzymes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_2b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.2]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_2C · 图 3-2c　底物浓度（左）与酶浓度（右）对反应速率的影响

- 归属：生物／原第3章 细胞内物质和能量的转换／3.2 影响酶活性的因素。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：把底物饱和与酶量比例的条件分开
- 绘图要求：
  - 左面固定酶量，右面底物过量、取初速
  - 平台不是反应停止；增加酶量影响Vmax不画成无限所有情境线性
- 必须文字标注：底物浓度；酶浓度；初速；固定酶量；底物过量；Vmax。
- 科学依据：os_enzymes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_2c.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.2]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_2D · 图 3-2d　竞争性与非竞争性抑制剂的作用方式

- 归属：生物／原第3章 细胞内物质和能量的转换／3.2 影响酶活性的因素。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：限定竞争性与纯非竞争性抑制简图
- 绘图要求：
  - 竞争性标活性位竞争；纯非竞争性不等于所有变构效应/不可逆变性
  - 不要把抑制必然画成底物永远无法结合，须区分结合与催化活性
  - 与速率图的Vmax/Km假设对应
- 必须文字标注：底物；活性位；竞争性；纯非竞争性模型；结合/催化；能否由加底物减弱。
- 科学依据：os_enzymes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_2d.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.2]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_2E · 图 3-2e　抑制剂对反应速率的影响（示意）

- 归属：生物／原第3章 细胞内物质和能量的转换／3.2 影响酶活性的因素。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：用明确动力学假设比较抑制曲线
- 绘图要求：
  - 采用同一底物轴，竞争性相同Vmax、表观Km增大；纯非竞争性Vmax降低、Km不变
  - 这些为理想模型，不推广到全部抑制机制
  - 没有原始数据只标示意，不伪装拟合
- 必须文字标注：[S]；初速v；Vmax；表观Km；竞争性/纯非竞争性；模型示意。
- 科学依据：os_enzymes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_2e.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.2]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_3 · 图 3-3　固定化酶：酶固定在凝胶珠上，底物流入，产物流出，酶留在柱内

- 归属：生物／原第3章 细胞内物质和能量的转换／3.3 酶在生产生活中的应用。
- 类型／动作／优先级：实验装置图；局部修正；P1。
- 教学目的：区分固定化酶柱、酶保留与扩散限制
- 绘图要求：
  - 标底物流入、产物流出、支持网/凝胶珠、流向
  - 不保证产物绝对无酶：需注明理想无泄漏与后续检测条件
  - 本图为装置原理，温度/pH/流速条件需另经来源确认
- 必须文字标注：底物入口；凝胶珠；固定化酶；支承网；产物出口；理想无泄漏。
- 科学依据：os_enzymes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_3.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.3]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_4 · 图 3-4　ATP 的结构和 ATP–ADP 循环

- 归属：生物／原第3章 细胞内物质和能量的转换／3.4 细胞的能量通货——ATP。
- 类型／动作／优先级：精确科学SVG；局部修正；P0。
- 教学目的：避免把断键本身说成释放能量
- 绘图要求：
  - 腺嘌呤+核糖+3磷酸的连接完整，水解箭头需有H2O与产物
  - 能量来自整体水解反应自由能下降，不能把能量箭头从单独断开的高能键直接引出
  - 标准ΔG与细胞条件区分，能量流不作为物质循环箭头
- 必须文字标注：ATP；ADP+Pi；H₂O；整体水解ΔG<0；耦联；再合成需能量。
- 科学依据：os_atp（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_4.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.4]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_5A · 图 3-5a　细胞呼吸总览：糖酵解、连接反应与克氏循环、电子传递链；无氧呼吸的两条途径

- 归属：生物／原第3章 细胞内物质和能量的转换／3.5 生命活动的能量来自哪里——呼吸作用。
- 类型／动作／优先级：结构示意图；局部修正；P0。
- 教学目的：分开糖酵解、发酵与有氧路径的净能量账本
- 绘图要求：
  - 糖酵解净2ATP只记一次；丙酮酸到乳酸/乙醇支路不再另产2ATP
  - 标发酵再生NAD+及细胞质位置，不能把“无氧”概括所有微生物厌氧呼吸
  - 30-32为现代真核近似，旧教材36-38与题设需核实，不混加
- 必须文字标注：葡萄糖；糖酵解净2ATP；丙酮酸；发酵/NAD+再生；线粒体路径；ATP估算条件。
- 科学依据：os_respiration（science；partially_verified）；os_fermentation（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_5a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.5]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_5B · 图 3-5b　线粒体的结构：嵴上有电子传递链和 ATP 合成酶，基质进行克氏循环

- 归属：生物／原第3章 细胞内物质和能量的转换／3.5 生命活动的能量来自哪里——呼吸作用。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把H+梯度与内膜连续结构连起来
- 绘图要求：
  - 嵴必须为内膜连续折叠；膜间隙与基质为不同区室
  - 泵H+方向基质→膜间隙，ATP合酶回流相反，电子/质子不同线型
  - 外膜不能直接替代内膜标电子传递链
- 必须文字标注：外膜；内膜/嵴；基质；膜间隙；H+泵出/回流；ATP合成酶。
- 科学依据：os_respiration（science；partially_verified）；os_fermentation（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_5b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.5]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_6A · 图 3-6a　叶绿体的结构：类囊体膜进行光反应，基质进行暗反应

- 归属：生物／原第3章 细胞内物质和能量的转换／3.6 植物的光合作用。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：定位光反应与碳同化区室
- 绘图要求：
  - 包膜两层与类囊体膜分开，基粒为堆叠而非额外第三层包膜
  - 光反应标签落在类囊体膜，卡尔文循环标签落在基质
- 必须文字标注：外/内膜；类囊体膜；基粒；基质；光反应；卡尔文循环。
- 科学依据：os_light（science；partially_verified）；os_calvin（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_6a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.6]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_6B · 图 3-6b　光反应与暗反应的关系

- 归属：生物／原第3章 细胞内物质和能量的转换／3.6 植物的光合作用。
- 类型／动作／优先级：结构示意图；局部修正；P0。
- 教学目的：准确表达两阶段的物质和能量交换
- 绘图要求：
  - 水光解若用方程式须配平2H2O→4H++4e-+O2；现未配平式不能当正式方程式
  - ATP/NADPH向卡尔文循环，ADP/Pi/NADP+返回；暗反应不标为只能黑暗进行
  - 箭头分清O2来自水、糖中碳来自CO2
- 必须文字标注：类囊体膜；基质；ATP/NADPH；ADP/Pi/NADP+；水光解配平式。
- 科学依据：os_light（science；partially_verified）；os_calvin（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_6b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.6]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_6C · 图 3-6c　卡尔文循环：固定、还原、再生

- 归属：生物／原第3章 细胞内物质和能量的转换／3.6 植物的光合作用。
- 类型／动作／优先级：精确科学SVG；重绘；P0。
- 教学目的：统一卡尔文循环的碳计数基准
- 绘图要求：
  - 采用3CO2+3RuBP→6个3-PGA→6个G3P；5个G3P再生3RuBP、1个G3P净输出
  - 全部碳数15+3=18=6×3守恒，不能把单次1RuBP/2TP与三次的5/6分配混画
  - 在同一3CO2基准标9ATP、6NADPH；葡萄糖等价需两份净G3P
- 必须文字标注：3CO₂；3RuBP(5C)；6PGA(3C)；6G3P；5再生/1输出；9ATP/6NADPH。
- 科学依据：os_light（science；partially_verified）；os_calvin（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_6c.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.6]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_6D · 图 3-6d　光合色素的吸收光谱（示意，峰值为近似值）

- 归属：生物／原第3章 细胞内物质和能量的转换／3.6 植物的光合作用。
- 类型／动作／优先级：精确科学SVG；保留／复用；P2。
- 教学目的：比较色素吸收谱的波段而非伪定量峰值
- 绘图要求：
  - 400-700nm坐标一致，图注近似示意
  - 不把所有绿光吸收画成绝对零；吸收谱与作用光谱不混称
- 必须文字标注：波长/nm；相对吸收；叶绿素a/b；类胡萝卜素；示意峰。
- 科学依据：os_light（science；partially_verified）；os_calvin（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_6d.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.6]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_6E · 图 3-6e　纸层析分离色素与 Rf

- 归属：生物／原第3章 细胞内物质和能量的转换／3.6 植物的光合作用。
- 类型／动作／优先级：实验装置图；保留／复用；P2。
- 教学目的：明确层析原点、前沿与Rf测量
- 绘图要求：
  - 起始线在溶剂液面之上；a与b都从同一原点到色素带中心/前沿
  - 色带顺序只作指定体系例，不推广所有溶剂
  - 安全注远离火源、教师确认溶剂；不补猜配方浓度
- 必须文字标注：溶剂液面；起始线；前沿；a；b；Rf=a/b；色带中心。
- 科学依据：os_light（science；partially_verified）；os_calvin（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_6e.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.6]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_7A · 图 3-7a　光照强度与净光合速率：光补偿点、光饱和点（阳生与阴生植物）

- 归属：生物／原第3章 细胞内物质和能量的转换／3.7 环境因素对光合作用的影响。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：从净交换零点判断补偿点
- 绘图要求：
  - 若净CO2吸收为正，暗处截距为-R，不应直接写等于正的呼吸速率
  - 补偿点在y=0处，光饱和以曲线趋平台描述
  - 阴/阳生植物趋势为典型示意，不作所有物种定量定律
- 必须文字标注：净CO₂交换；光强；0；暗呼吸截距-R；光补偿点；光饱和。
- 科学依据：os_light（science；partially_verified）；os_calvin（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_7a.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.7]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_7B · 图 3-7b　限制因素：先看哪一个因素处在曲线的上升段

- 归属：生物／原第3章 细胞内物质和能量的转换／3.7 环境因素对光合作用的影响。
- 类型／动作／优先级：精确科学SVG；局部修正；P1。
- 教学目的：用受控曲线比较支持限制因素判断
- 绘图要求：
  - 低/高CO2曲线除CO2外其他条件相同，才能据差异解释
  - 上升段仅说明增加该变量有响应，不能无条件等同唯一限制因子
  - 平台可来自其他因子或损伤，结合题设，不写万能读图口诀
- 必须文字标注：光强；光合速率；CO₂处理条件；响应段；平台；其他控制量。
- 科学依据：os_light（science；partially_verified）；os_calvin（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_7b.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.7]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_7C · 图 3-7c　O₂ 浓度对呼吸作用的影响（示意）

- 归属：生物／原第3章 细胞内物质和能量的转换／3.7 环境因素对光合作用的影响。
- 类型／动作／优先级：精确科学SVG；局部修正；P0。
- 教学目的：避免从CO2最低点直接推最佳储藏条件
- 绘图要求：
  - 三曲线叠加须使用同一单位并声明底物/发酵模式假设
  - 删除总CO2最低必等于有机物消耗最少/最佳保鲜的直接结论，不同底物RQ与组织伤害需另证据
  - 曲线仅模型，不给未经测量的推荐氧浓度
- 必须文字标注：O₂浓度；CO₂释放速率；有氧/发酵贡献；模型条件；不直接推保鲜最优。
- 科学依据：os_light（science；partially_verified）；os_calvin（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_7c.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.7]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-ASSET-B3_SUM · 图 3-sum　光合作用与呼吸作用的关系：物质循环，能量不循环

- 归属：生物／原第3章 细胞内物质和能量的转换／3.7 环境因素对光合作用的影响。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：区分物质循环与单向能量流
- 绘图要求：
  - CO2/H2O与有机物/O2物质箭头可闭合，能量箭头光→化学能→功/热不能闭环
  - 典型真核光合/呼吸定位，不推广所有生物结构
- 必须文字标注：物质箭头；能量箭头；光；有机物；ATP；热；不循环。
- 科学依据：os_light（science；partially_verified）；os_calvin（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`assets/fig/b3_sum.svg`。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio03.js sections[id=3.7]。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-3_1 · 3.1 机械运动：模块03知识结构

- 归属：物理／原第3章 直线运动／3.1 机械运动。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 改为“研究目标/尺度→是否需要尺寸”决策分支，分别通向可用与不可用质点，不把所有运动都先当质点。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：研究对象；比较尺寸与问题尺度；质点模型；位置随时间变化。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理3-3.1-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys03.js sections[id=3.1]；data/notes/phys03.json /3.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_1-01 · 火车完全过隧道的始末状态

- 归属：物理／原第3章 直线运动／3.1 机械运动。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：让尺寸是否可忽略由所求量决定
- 绘图要求：
  - 按本节例题车长100m、隧道300m画起止两帧，车头总移动400m
  - 选同一个代表点跟踪，车尾离开而非车头到出口；标图非真实透视比例
- 必须文字标注：车头/车尾；100m；300m；400m；初态/末态。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.1]；data/notes/phys03.json /3.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-3_2 · 3.2 参照物、坐标系和参照系：模块03知识结构

- 归属：物理／原第3章 直线运动／3.2 参照物、坐标系和参照系。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 参照物与原点/方向/单位为并列条件，位置与相对量为结果；原点平移、匀速参考系转换不可混为同一个动作。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：参照物；坐标原点与正方向；位置坐标；相对位置与速度。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理3-3.2-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys03.js sections[id=3.2]；data/notes/phys03.json /3.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_2-01 · 移动原点与相对位置的两套坐标

- 归属：物理／原第3章 直线运动／3.2 参照物、坐标系和参照系。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：验证原点平移不改变相对位置
- 绘图要求：
  - 共线A=50m、B=20m，新原点在旧x=100m，新的A=-50、B=-80
  - 两轴同方向同单位同尺度；相对位移都+30m
- 必须文字标注：旧/新原点；A/B；50/20/-50/-80m；x_A-x_B=+30m。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.2]；data/notes/phys03.json /3.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-3_3 · 3.3 路程和位移：模块03知识结构

- 归属：物理／原第3章 直线运动／3.3 路程和位移。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留分段计路程与末减初两条操作的顺序提示；配图/公式中的绝对值必须完整，并明确两者是不同计算分支。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：轨迹分段；各段长度相加为路程；末减初为位移；比较大小。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理3-3.3-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys03.js sections[id=3.3]；data/notes/phys03.json /3.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_3-01 · 一维折返路径与位移账本

- 归属：物理／原第3章 直线运动／3.3 路程和位移。
- 类型／动作／优先级：精确科学SVG；新增需求；P0。
- 教学目的：把有向差与非负路径分开
- 绘图要求：
  - 使用例题-2→5→1m，两段7m、4m，路程11m、位移+3m
  - 回程用独立弧线而非覆盖首段；绝对值须完整排版，不能继承当前竖线拆段错误
- 必须文字标注：-2/5/1m；7m；4m；路程11m；Δx=+3m。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.3]；data/notes/phys03.json /3.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-3_4 · 3.4 匀速直线运动　速度和速率：模块03知识结构

- 归属：物理／原第3章 直线运动／3.4 匀速直线运动　速度和速率。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留恒v→位置式→同一时刻位置相等→时间范围检查；原点、迟发时间和同向/相向分支由例题图补足。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：速度大小方向恒定；x＝x₀＋vt；两位置相等；相遇条件。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理3-3.4-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys03.js sections[id=3.4]；data/notes/phys03.json /3.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_4-01 · 追及位置图及延迟出发图

- 归属：物理／原第3章 直线运动／3.4 匀速直线运动　速度和速率。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：用同一时间变量和位置交点求相遇
- 绘图要求：
  - 主面板x_A=6t、x_B=60+4t，0≤t≤35s，交点(30s,180m)
  - 延迟面板另用已有标准例题A=4t、B=6(t-5)，B轨迹仅t≥5s，交点t=15s；两面板不能混用数据
- 必须文字标注：t/s；x/m；初始间距60m；相遇(30,180)；迟发t=5s；第二案例独立。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.4]；data/notes/phys03.json /3.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-3_5 · 3.5 匀速直线运动的图象：模块03知识结构

- 归属：物理／原第3章 直线运动／3.5 匀速直线运动的图象。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 必须先分x-t与v-t两支：前者斜率为v，后者斜率为a/面积为位移；交点意义分别标，不能串成所有图都用面积。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：识别坐标轴；s–t斜率；v–t有向面积；判交点意义。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理3-3.5-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys03.js sections[id=3.5]；data/notes/phys03.json /3.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_5-01 · 含负速度的分段v-t面积图

- 归属：物理／原第3章 直线运动／3.5 匀速直线运动的图象。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：图上同时读取净位移与路程
- 绘图要求：
  - 0–3s速度+4、3–5s速度-2m/s，正面积12m、负面积-4m
  - 无物理瞬时跳变机制时标理想分段模型，不用竖直连线面积
  - 同图标位移8m、路程16m，练习版隐藏两结果
- 必须文字标注：v/(m/s)；t/s；+4；-2；12m；-4m；s=8m；路程16m。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.5]；data/notes/phys03.json /3.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-3_6 · 3.6 变速直线运动　平均速度和瞬时速度：模块03知识结构

- 归属：物理／原第3章 直线运动／3.6 变速直线运动　平均速度和瞬时速度。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留平均到瞬时的趋近链，另分总位移/时间与路程/时间；只有恒a可接(u+v)/2。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：选定时间区间；总位移／总时间；缩小区间；瞬时速度。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理3-3.6-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys03.js sections[id=3.6]；data/notes/phys03.json /3.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_6-01 · 等路程往返的时间权重图

- 归属：物理／原第3章 直线运动／3.6 变速直线运动　平均速度和瞬时速度。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：解释平均速度为零但平均速率非零
- 绘图要求：
  - 用100m去程5m/s、原路回程2m/s，时间20s和50s
  - x-t斜率+5与-2、末位置0，平均速度0、平均速率200/70≈2.86
  - 时间轴必须按20:50比例，不画等长时间框
- 必须文字标注：100m；20s；50s；总70s；位移0；路程200m；2.86m/s。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.6]；data/notes/phys03.json /3.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-3_7 · 3.7 变速直线运动的加速度：模块03知识结构

- 归属：物理／原第3章 直线运动／3.7 变速直线运动的加速度。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留u/v带符号→Δv→a→比较v与a方向；零速边界提示回看前后过程，不能以a正负一键判加减。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：初末速度矢量；Δv＝v−u；除时间；比较v和a方向。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理3-3.7-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys03.js sections[id=3.7]；data/notes/phys03.json /3.7。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_7-01 · 速度与加速度符号的四象限比较

- 归属：物理／原第3章 直线运动／3.7 变速直线运动的加速度。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：避免以a正负单独判断加减速
- 绘图要求：
  - 四个小面板独立标v/a箭头与速率增减
  - 引用已有v=-5、a=-2案例，1s后v=-7；转向前后不得用同一加减速标签
  - 速度为0的瞬间单独说明，不能从v·a=0推持久状态
- 必须文字标注：v>0/v<0；a>0/a<0；同向速率增；反向速率减；v=0边界。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.7]；data/notes/phys03.json /3.7。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-3_8 · 3.8 匀加速直线运动：模块03知识结构

- 归属：物理／原第3章 直线运动／3.8 匀加速直线运动。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留恒a假设→v式→面积式→消元的推导链；停车、转向、撤力列为模型终止或分段检查。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：恒a；v＝u＋at；有向梯形面积；位移公式；消元与条件检查。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理3-3.8-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys03.js sections[id=3.8]；data/notes/phys03.json /3.8。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_8-01 · 刹停后模型终止的分段运动图

- 归属：物理／原第3章 直线运动／3.8 匀加速直线运动。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：让停车时间限制在图上可见
- 绘图要求：
  - u=20、a=-5，0–4s线性降至0，4–6s保持0
  - 面积40m；虚线延伸到负速必须划作错误外推而非真实轨迹
  - 配s-t停后水平，明确车不会因刹车模型无限延续而倒行
- 必须文字标注：t停=4s；0–6s；v=0；正确面积40m；错误外推。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.8]；data/notes/phys03.json /3.8。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_8-02 · 等时间位移差aT²的面积推导

- 归属：物理／原第3章 直线运动／3.8 匀加速直线运动。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：用同宽速度面积带推导逐段位移差
- 绘图要求：
  - 在恒a的v-t直线下画相邻两段宽T的有向面积，第二段比第一段多aT²
  - u可非零，不把1:3:5限定比推广到所有初速
  - 若速度跨0，注明比较的是有向位移差而非路程差
- 必须文字标注：T；s₁/s₂；恒a；s₂-s₁=aT²；有向位移。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.8]；data/notes/phys03.json /3.8。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-3_9 · 3.9 自由落体运动：模块03知识结构

- 归属：物理／原第3章 直线运动／3.9 自由落体运动。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 仅受重力近地模型下分u=0自由落体与u≠0竖直抛体，地面高度边界必须在各分支内明确。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：仅重力且近地；a向下恒g；自由落体或上抛；边界与图线。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理3-3.9-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys03.js sections[id=3.9]；data/notes/phys03.json /3.9。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_9-01 · 上升气球释放物体的高度与速度图

- 归属：物理／原第3章 直线运动／3.9 自由落体运动。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：展示释放瞬间继承初速度及落地边界
- 绘图要求：
  - 用h0=75m、u=+10、g=10的原例；h(t)=75+10t-5t²，0≤t≤5
  - 顶点(1s,80m)、落地(5s,0m)，v=10-10t、落地-40m/s
  - 地面高度与相对位移使用不同符号，a一直向下
- 必须文字标注：75m；u=+10m/s；80m；地面0；t=1/5s；v=-40m/s。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.9]；data/notes/phys03.json /3.9。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-3_9-02 · 测g的释放、计时与h-t²处理装置计划

- 归属：物理／原第3章 直线运动／3.9 自由落体运动。
- 类型／动作／优先级：实验装置图；新增需求；P1。
- 教学目的：把测量量、变量控制与误差接到推导
- 绘图要求：
  - 仅示意可调高度、球、释放/计时传感、缓冲接收，器材型号和高度待教师确认
  - 三联图为装置、数据表空白、h对t²拟合；斜率g/2
  - 不画高处抛物操作；释放初速、零点和反应延迟列为误差源
- 必须文字标注：h/m；t/s；t²/s²；斜率=g/2；释放初速≈0；误差源。
- 科学依据：os_motion（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：05、07、09、10、12。
- 原文定位：lessons/phys03.js sections[id=3.9]；data/notes/phys03.json /3.9。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图；器材/条件与教师或适用实验资料确认；只画原理，不补猜药品配方或危险操作。。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-4_1 · 4.1 力与运动：模块03知识结构

- 归属：物理／原第4章 牛顿运动定律／4.1 力与运动。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留相互作用→同一物体外力→合力→a→速度变化；不能把速度直接画成合力的产物。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：相互作用；同一物体受力；矢量合力；加速度；速度变化。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理4-4.1-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys04.js sections[id=4.1]；data/notes/phys04.json /4.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_1-01 · 同一对象的实际力、合力与速度变化

- 归属：物理／原第4章 牛顿运动定律／4.1 力与运动。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：区分F合=0与无受力、a与v
- 绘图要求：
  - 两帧使用本节2kg块，匀速时10N右/10N左；撤拉后4N左，a=-2
  - v箭头独立于力箭头，ma放方程旁，不能加入受力图
- 必须文字标注：2kg；10N/10N；4N；ΣF；v；a；ma不是另一个力。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.1]；data/notes/phys04.json /4.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-4_2 · 4.2 力的种类：模块03知识结构

- 归属：物理／原第4章 牛顿运动定律／4.2 力的种类。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留重力、接触、摩擦判断的受力清点顺序，摩擦处分静/滑动两支并先验接触条件。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：找重力；逐个接触找弹力；判断相对滑动或趋势；选摩擦模型。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理4-4.2-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys04.js sections[id=4.2]；data/notes/phys04.json /4.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_2-01 · 静摩擦自适应与临界范围

- 归属：物理／原第4章 牛顿运动定律／4.2 力的种类。
- 类型／动作／优先级：精确科学SVG；新增需求；P0。
- 教学目的：先求需求再比较上限
- 绘图要求：
  - m=2kg、g=10、μs=.4时N=20、f_s,max=8N；5N外拉对应f_s=5
  - 静摩擦段f_s=F在0…8内；动摩擦只标μkN符号，不擅自为该例补μk数值
  - 绝对值界限完整显示，不继承f_s竖线拆段
- 必须文字标注：F/N；f/N；f_s≤8N；5N需求；静/动模型分界。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.2]；data/notes/phys04.json /4.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_2-02 · 弹簧原长与形变量测量

- 归属：物理／原第4章 牛顿运动定律／4.2 力的种类。
- 类型／动作／优先级：实验装置图；新增需求；P1。
- 教学目的：避免把总长当作胡克定律x
- 绘图要求：
  - 用自然长.20m、拉长至.25m、k=200N/m，标x=.05m、弹力10N
  - 尺刻度、固定端与恢复方向清楚，弹性限度条件醒目
  - 是本节已给数据的读图计划，不补猜实验操作参数
- 必须文字标注：l₀=.20m；l=.25m；x=.05m；k=200N/m；F=10N；恢复方向。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.2]；data/notes/phys04.json /4.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图；器材/条件与教师或适用实验资料确认；只画原理，不补猜药品配方或危险操作。。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-4_3 · 4.3 力的合成与分解：模块03知识结构

- 归属：物理／原第4章 牛顿运动定律／4.3 力的合成与分解。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留选轴→投影→各轴求和→求合矢量；分量只是原力的表示，不与原力重复计数。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：选轴与角；分力投影；逐轴代数和；合力大小和方向。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理4-4.3-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys04.js sections[id=4.3]；data/notes/phys04.json /4.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_3-01 · 数值矢量合成及分量复原

- 归属：物理／原第4章 牛顿运动定律／4.3 力的合成与分解。
- 类型／动作／优先级：精确科学SVG；新增需求；P0。
- 教学目的：使合力大小与方向可验算
- 绘图要求：
  - 用6N东、8N北，统一比例，R=10N、东偏北53.1°
  - 分解/合成两图只算一次原力；夹角范围公式须显示完整绝对值
  - 屏幕轴可非物理空间坐标，但箭头投影正交
- 必须文字标注：6N东；8N北；R=10N；53.1°；投影轴；不重复计力。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.3]；data/notes/phys04.json /4.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-4_4 · 4.4 牛顿第一运动定律：模块03知识结构

- 归属：物理／原第4章 牛顿运动定律／4.4 牛顿第一运动定律。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 把真实减阻证据→理想外推→零合力保持速度标成推理关系，不画成现实中已经完全无阻的实验步骤。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：减少阻力的证据；理想无阻情境；速度不变；第一定律与惯性系。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理4-4.4-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys04.js sections[id=4.4]；data/notes/phys04.json /4.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_4-01 · 伽利略理想斜面逐步放平

- 归属：物理／原第4章 牛顿运动定律／4.4 牛顿第一运动定律。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：解释由实验趋势到无阻极限的推理
- 绘图要求：
  - 三面板同一释放高度、右斜面逐渐变平；理想无耗散能达到原高度
  - 水平极限标理想无阻，不伪装真实实测永动装置
  - 现实阻力对应停止与理想外推分开
- 必须文字标注：同一初始高度；逐渐减小倾角；阻力趋小；水平无阻极限；理想推理。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.4]；data/notes/phys04.json /4.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-4_5 · 4.5 惯性与质量：模块03知识结构

- 归属：物理／原第4章 牛顿运动定律／4.5 惯性与质量。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 分开惯性现象解释链和同F比较m/a的测量链；质量与重量是不同分支，速度不指向惯性大小。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：原运动状态；外力改变部分运动；其余部分保持趋势；质量量度抗变化。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理4-4.5-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys04.js sections[id=4.5]；data/notes/phys04.json /4.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_5-01 · 刹车乘客的前后状态辅助图

- 归属：物理／原第4章 牛顿运动定律／4.5 惯性与质量。
- 类型／动作／优先级：辅助插画；新增需求；P2。
- 教学目的：用身体与车的不同速度变化解释前倾
- 绘图要求：
  - 人物只作轮廓不画“惯性力”向前箭头；原向前速度与安全带向后实际作用由精确SVG覆盖
  - 两帧同一地面参考系，注明不是质量或惯性被消灭
  - 辅助人物不可取代受力图；未来也不需要AI生成定量箭头
- 必须文字标注：刹车前/后；原速度向前；安全带作用；地面参考系；惯性是性质。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1000×700；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.5]；data/notes/phys04.json /4.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设；辅助人物不携带科学定量信息；力与速度箭头必须为单独精确矢量层。。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-4_6 · 4.6 动量：模块03知识结构

- 归属：物理／原第4章 牛顿运动定律／4.6 动量。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 先画确定系统/质量条件，再到p、Δp、平均外力；开放变质量分支只标需计通量，不把末尾提醒当成所有系统通用公式。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：p＝mv；末减初求Δp；平均合力Δp/Δt；系统边界与动量通量。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理4-4.6-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys04.js sections[id=4.6]；data/notes/phys04.json /4.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_6-01 · 动量与动能的同p不同m对照

- 归属：物理／原第4章 牛顿运动定律／4.6 动量。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：把矢量动量和标量动能分开
- 绘图要求：
  - 本节标准例p=6kg·m/s，m=2和3kg，v=3和2m/s，E=9和6J
  - p箭头同长度，能量条不同；能量没有方向正负
  - 平均碰撞力若关联已有反弹例，标接触0.020s只确定平均力，不画任意瞬时曲线
- 必须文字标注：p=6kg·m/s；m=2/3kg；v=3/2m/s；E=9/6J；矢量/标量。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.6]；data/notes/phys04.json /4.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-4_7 · 4.7 牛顿第二运动定律：模块03知识结构

- 归属：物理／原第4章 牛顿运动定律／4.7 牛顿第二运动定律。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留对象→受力图→逐轴方程→解与约束检验；整体/隔离分别对应a/内力，不凭整体式直接获得T。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：选对象和系统；受力图；逐轴方程；求a和内力；运动学与接触检查。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理4-4.7-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys04.js sections[id=4.7]；data/notes/phys04.json /4.7。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_7-01 · 电梯上行减速的速度、加速度与受力

- 归属：物理／原第4章 牛顿运动定律／4.7 牛顿第二运动定律。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：以加速度方向而非运动方向判断秤读数
- 绘图要求：
  - m=60kg、g=10、v向上但a=2向下；N=480N、mg=600N
  - v、a放隔离体外，只有N/mg作用于人；箭头力比例480:600
  - 只给支持力读数N，不把kg标尺和N混写
- 必须文字标注：v向上；a向下2m/s²；60kg；N=480N；mg=600N；失重。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.7]；data/notes/phys04.json /4.7。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_7-02 · 检验F-ma的测量路径与变量控制

- 归属：物理／原第4章 牛顿运动定律／4.7 牛顿第二运动定律。
- 类型／动作／优先级：实验装置图；新增需求；P1。
- 教学目的：把装置、控制总质量与图线斜率关联
- 绘图要求：
  - 示意小车、低摩擦轨道、测力与测速传感；器材配置待实验手册/教师确认
  - 优先直接测拉力，若用悬挂mg近似须画出近似条件与系统质量，不能将二者默认为相等
  - F变、总质量不变；另图a-1/m在F固定；数据轴单位完整
- 必须文字标注：F/N；a/(m/s²)；总质量固定；a-F；F固定时a-1/m；摩擦/传感误差。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：05、07、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.7]；data/notes/phys04.json /4.7。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图；器材/条件与教师或适用实验资料确认；只画原理，不补猜药品配方或危险操作。。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-PHY-4_8 · 4.8 牛顿第三运动定律：模块03知识结构

- 归属：物理／原第4章 牛顿运动定律／4.8 牛顿第三运动定律。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留交换施受者→核对受体→各自方程的判断顺序；关系图与单物体受力图不互相替代。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：明确A作用B；寻找B作用A；不同受力对象；分别列运动方程。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-物理4-4.8-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/phys04.js sections[id=4.8]；data/notes/phys04.json /4.8。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-PHY-4_8-01 · 书、桌、地球的相互作用关系图

- 归属：物理／原第4章 牛顿运动定律／4.8 牛顿第三运动定律。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：同时找到支持力与重力各自的反作用
- 绘图要求：
  - 节点为书/桌/地球，每条作用画双向带受力者标签的配对箭头
  - 同一节点的N和mg可平衡，跨节点配对不能在单物体受力图中抵消
  - 箭头关系图不代表真实空间距离或力大小
- 必须文字标注：桌→书N；书→桌N′；地球→书mg；书→地球引力；受力对象。
- 科学依据：os_mechanics（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/phys04.js sections[id=4.8]；data/notes/phys04.json /4.8。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-3_1 · 3.1 原子学说与分子学说：模块03知识结构

- 归属：化学／原第3章 原子与分子／3.1 原子学说与分子学说。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 用“宏观证据支持/粒子模型解释/适用边界”关系标签，区别证据与反应过程的时间顺序。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：宏观质量守恒；原子重排；分子组成改变；原子学说的边界。
- 科学依据：chem_standard（curriculum；partially_verified）；os_atomic_history（science_not_exam_scope；partially_verified）；os_equations（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学3-3.1-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem03.js sections[id=3.1]；data/notes/chem03.json /3.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-3_1-01 · 制水反应的原子重排与分子数变化

- 归属：化学／原第3章 原子与分子／3.1 原子学说与分子学说。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：让原子守恒与分子数可变同时可见
- 绘图要求：
  - 取4H2+2O2→4H2O，前后H8、O4，分子数6变4
  - 同色代表同元素，数量精确；不把连线当精确键角
  - 只作计量示意，不绘点燃/制备的危险操作
- 必须文字标注：H/O图例；4H₂；2O₂；4H₂O；原子守恒；分子数可变。
- 科学依据：chem_standard（curriculum；partially_verified）；os_atomic_history（science_not_exam_scope；partially_verified）；os_equations（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.1]；data/notes/chem03.json /3.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-3_2 · 3.2 物质组成及化学反应中的基本定律：模块03知识结构

- 归属：化学／原第3章 原子与分子／3.2 物质组成及化学反应中的基本定律。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 以物质组成与反应为根，分质量守恒/定比/倍比；每支写固定条件，不把三条定律画成先后步骤。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：系统边界；质量守恒；同一化合物定比；不同化合物倍比。
- 科学依据：chem_standard（curriculum；partially_verified）；os_atomic_history（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学3-3.2-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem03.js sections[id=3.2]；data/notes/chem03.json /3.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-3_2-01 · 开放与封闭系统的质量边界

- 归属：化学／原第3章 原子与分子／3.2 物质组成及化学反应中的基本定律。
- 类型／动作／优先级：实验装置图；新增需求；P1。
- 教学目的：解释逸出气体造成称量范围差异
- 绘图要求：
  - 同一反应概念分两面板，开放时气体跨边界，完整物料系统包含逸出气体
  - 若示意气体捕集仅用可膨胀收集容器，不画产气刚性密封高压装置
  - 反应药品、浓度与实际操作需教师确认，本图只展示系统边界而非实验指引
- 必须文字标注：系统边界；反应前/后；逸出气体；容器内称量；完整物料质量；非操作图。
- 科学依据：chem_standard（curriculum；partially_verified）；os_atomic_history（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.2]；data/notes/chem03.json /3.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图；器材/条件与教师或适用实验资料确认；只画原理，不补猜药品配方或危险操作。。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-3_3 · 3.3 原子与相对原子质量：模块03知识结构

- 归属：化学／原第3章 原子与分子／3.3 原子与相对原子质量。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 区分Z/A粒子计数、单原子质量比和元素丰度平均三个层次；Ar无单位，A为整数不等于精确原子质量。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：质子中子电子；质量单位u；单原子相对质量；同位素加权平均。
- 科学依据：chem_standard（curriculum；partially_verified）；os_isotopes（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学3-3.3-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem03.js sections[id=3.3]；data/notes/chem03.json /3.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-3_3-01 · 同位素丰度与加权平均的教学图

- 归属：化学／原第3章 原子与分子／3.3 原子与相对原子质量。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：把单个质量与元素统计平均分开
- 绘图要求：
  - 用题给35/37与75%/25%，两峰/两类计数符号一一对应，平均35.5
  - 标教学近似质量而非实测谱图，横轴若m/z需写单电荷假设
  - 平均位于35与37之间，无35.5中子或半个原子
- 必须文字标注：35/37；75%/25%；加权平均35.5；Ar无单位；教学近似。
- 科学依据：chem_standard（curriculum；partially_verified）；os_isotopes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.3]；data/notes/chem03.json /3.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-3_3-02 · 原子、同位素与离子的粒子组成

- 归属：化学／原第3章 原子与分子／3.3 原子与相对原子质量。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：把Z/A与电子增减区分
- 绘图要求：
  - 用本节²³₁₁Na及³⁷₁₇Cl⁻计数例，核内p/n与核外e分层表示，不能用多个电子固定轨道假装现代真实轨迹
  - 同位素变中子、离子变电子分两独立转换箭头
  - 核与原子不按大小比例，并用明确计数表保证符号和数量一致
- 必须文字标注：Z；A；p/n/e；Na:11/12/11；Cl⁻:17/20/18；非比例核/电子云。
- 科学依据：chem_standard（curriculum；partially_verified）；os_isotopes（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.3]；data/notes/chem03.json /3.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-3_4 · 3.4 化学式与式量：模块03知识结构

- 归属：化学／原第3章 原子与分子／3.4 化学式与式量。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留识别式→括号展开→式量→质量分数；分子式与离子化合物式的对象类型在第一步说明。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：化学式表示对象；统计原子数；求式量；元素质量分数。
- 科学依据：chem_standard（curriculum；partially_verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学3-3.4-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem03.js sections[id=3.4]；data/notes/chem03.json /3.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-3_4-01 · 括号与结晶水的原子计数树

- 归属：化学／原第3章 原子与分子／3.4 化学式与式量。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：防止括号和水合系数的作用域错误
- 绘图要求：
  - 三面板Ca(OH)2→Ca1O2H2；Al2(SO4)3→Al2S3O12；CuSO4·5H2O→Cu1S1O9H10
  - 各括号外系数箭头只作用于其组内所有原子，先计数后求式量
  - 单位无量纲Mr/式量与g·mol⁻¹的M分开
- 必须文字标注：括号作用域；Ca/O/H；Al/S/O；Cu/S/O/H；结晶水×5；式量/M区别。
- 科学依据：chem_standard（curriculum；partially_verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.4]；data/notes/chem03.json /3.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-3_5 · 3.5 确定化学式的方法：模块03知识结构

- 归属：化学／原第3章 原子与分子／3.5 确定化学式的方法。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 根节点分“已知离子电荷→电荷守恒式”和“元素质量→除Ar→实验式”；质量支再分给Mr/未给Mr。不得把交叉电荷法伪接到元素质量算法中。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：元素质量；除Ar得原子数比；约为整数比；实验式；用Mr确定倍数。
- 科学依据：chem_standard（curriculum；partially_verified）；os_empirical（science_not_exam_scope；partially_verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学3-3.5-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem03.js sections[id=3.5]；data/notes/chem03.json /3.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-3_5-01 · 燃烧分析的碳氢氧质量流

- 归属：化学／原第3章 原子与分子／3.5 确定化学式的方法。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：避免把氧化产物中的氧全归原样品
- 绘图要求：
  - 用原例.600g样品、.880gCO2、.360gH2O；mC=.240、mH=.040、样品mO=.320
  - 外加O2另画来源，不能将产物O全部连到样品O
  - n比.020:.040:.020=1:2:1，Mr60才推C2H4O2
- 必须文字标注：0.600g样品；外加O₂；CO₂/H₂O数据；m(C/H/O)；原样品O差值；CH₂O→C₂H₄O₂。
- 科学依据：chem_standard（curriculum；partially_verified）；os_empirical（science_not_exam_scope；partially_verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.5]；data/notes/chem03.json /3.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-3_5-02 · 离子电荷最小公倍数与化学式

- 归属：化学／原第3章 原子与分子／3.5 确定化学式的方法。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：说明交叉下标的电荷守恒依据
- 绘图要求：
  - 本节Ca²⁺与PO₄³⁻需3个Ca、2个磷酸根，总+6/-6，式Ca₃(PO₄)₂
  - 磷酸根内部P/O不改，整体超过1才加括号；交叉后需约简
  - 电荷条符号不是离子真实尺寸，不引入未知教材小节
- 必须文字标注：Ca²⁺×3；PO₄³⁻×2；总+6/-6；Ca₃(PO₄)₂；括号作用域。
- 科学依据：chem_standard（curriculum；partially_verified）；os_empirical（science_not_exam_scope；partially_verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.5]；data/notes/chem03.json /3.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-3_6 · 3.6 物质的量：模块03知识结构

- 归属：化学／原第3章 原子与分子／3.6 物质的量。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 现链漏气体入口；以n为中心接m/N/V及实体下标，可直接引用保留图c3_6，不另造同义SVG。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：质量m÷M；物质的量n；粒子数N＝nN_A；指定原子或离子数。
- 科学依据：chem_standard（curriculum；partially_verified）；bipm（science；verified）；nist（science；verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学3-3.6-m3"] .concept-flow`；优先引用 ILL-ASSET-C3_6。
- 模块用途：03。
- 原文定位：lessons/chem03.js sections[id=3.6]；data/notes/chem03.json /3.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-3_6-01 · 指定实体与化学式下标的计数层级

- 归属：化学／原第3章 原子与分子／3.6 物质的量。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：把分子mol转换为原子mol再到原子数
- 绘图要求：
  - 采用本节0.250mol H2SO4，O原子为1.00mol、NA按题给6.02e23
  - 画一个分子组成示意配倍数关系，不试图把0.25mol画成真实粒子点数
  - 离子数不得仅按该式断言，溶液电离另需模型
- 必须文字标注：0.250mol H₂SO₄分子；每分子4O；1.00mol O原子；6.02×10²³个O原子。
- 科学依据：chem_standard（curriculum；partially_verified）；bipm（science；verified）；nist（science；verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.6]；data/notes/chem03.json /3.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-3_6-02 · 同温不同标准压力的理想摩尔体积

- 归属：化学／原第3章 原子与分子／3.6 物质的量。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：阻止把22.4当无条件常数
- 绘图要求：
  - 1mol、T=273.15K，p=101.325kPa时Vm≈22.414L；p=100kPa时≈22.711L
  - 数值来自NIST并由RT/p核算；若画同截面积活塞高度，比例按22.414:22.711计算
  - 固液图必须与气体Vm公式用叉线分开，不能给液水同体积
- 必须文字标注：1mol理想气体；273.15K；101.325/100kPa；22.414/22.711L；V_m=RT/p。
- 科学依据：chem_standard（curriculum；partially_verified）；bipm（science；verified）；nist（science；verified）；os_formula_mass（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem03.js sections[id=3.6]；data/notes/chem03.json /3.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-4_1_1 · 4.1.1 表示化学反应的语言——化学方程式：模块03知识结构

- 归属：化学／原第4章 化学方程式与化学计算／4.1.1 表示化学反应的语言——化学方程式。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 分出分子方程与净离子方程两条书写链；离子支补拆强电解质/删旁观/验电荷，不能只用普通配平流程。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：事实与条件；反应物和生成物；守恒配平；读出物质的量比。
- 科学依据：chem_standard（curriculum；partially_verified）；os_equations（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学4-4.1.1-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem04.js sections[id=4.1.1]；data/notes/chem04.json /4.1.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-4_1_1-01 · 净离子反应与旁观离子去留

- 归属：化学／原第4章 化学方程式与化学计算／4.1.1 表示化学反应的语言——化学方程式。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：使拆、删、验原子与电荷的步骤可追踪
- 绘图要求：
  - 使用AgNO3+NaCl原例，反应前画Ag+/Cl-/Na+/NO3-，沉淀AgCl为晶格集合简图
  - Na+和NO3-保留在溶液，不画它们消失；晶格简图不是独立AgCl分子
  - 底部净式Ag++Cl-→AgCl(s)，电荷左右0
- 必须文字标注：Ag⁺；Cl⁻；Na⁺；NO₃⁻；AgCl(s)；旁观离子；电荷守恒。
- 科学依据：chem_standard（curriculum；partially_verified）；os_equations（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.1.1]；data/notes/chem04.json /4.1.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-4_1_2 · 4.1.2 化学反应的类型：模块03知识结构

- 归属：化学／原第4章 化学方程式与化学计算／4.1.2 化学反应的类型。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 按形式、氧化数、酸碱三种不同标准分支，允许同一反应落在多类；反应发生条件与命名分开。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：确定分类标准；检查反应特征；允许分类重叠；用方程式支持。
- 科学依据：chem_standard（curriculum；partially_verified）；os_reaction_types（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学4-4.1.2-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem04.js sections[id=4.1.2]；data/notes/chem04.json /4.1.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-4_1_2-01 · 反应形式与氧化还原分类的重叠

- 归属：化学／原第4章 化学方程式与化学计算／4.1.2 化学反应的类型。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：纠正把不同分类标准当互斥类别
- 绘图要求：
  - 用已有2Mg+O2→2MgO同时归化合与氧化还原；AgCl沉淀归复分解而无氧化数变化
  - 采用双标准表或交叉集合，不能声称四种形式涵盖一切反应
  - 净反应判断加水溶液条件，不仅交换化学式
- 必须文字标注：分类标准；化合/复分解；氧化还原；氧化数变/不变；反例。
- 科学依据：chem_standard（curriculum；partially_verified）；os_reaction_types（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.1.2]；data/notes/chem04.json /4.1.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-4_1_3 · 4.1.3 化学方程式的配平：模块03知识结构

- 归属：化学／原第4章 化学方程式与化学计算／4.1.3 化学方程式的配平。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留固定式→列守恒→系数→最简→逐元素/电荷核查；不得连接到改下标的伪步骤。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：固定正确化学式；选择元素列守恒；求系数；最简化；全元素复核。
- 科学依据：chem_standard（curriculum；partially_verified）；os_equations（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学4-4.1.3-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem04.js sections[id=4.1.3]；data/notes/chem04.json /4.1.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-4_1_3-01 · 配平错误前后的原子账本

- 归属：化学／原第4章 化学方程式与化学计算／4.1.3 化学方程式的配平。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：让错误氧数被显式发现
- 绘图要求：
  - 本节检测错式2Fe+3O2→Fe2O3，Fe左右2但O6对3
  - 更正4Fe+3O2→2Fe2O3后Fe4、O6均平
  - 只高亮系数变化，化学式下标锁定，不能画改下标的伪修正
- 必须文字标注：错误O6≠3；正确O6=6；Fe原子数；只改系数；下标不动。
- 科学依据：chem_standard（curriculum；partially_verified）；os_equations（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.1.3]；data/notes/chem04.json /4.1.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-4_2_1 · 4.2.1 计算反应物和生成物的量：模块03知识结构

- 归属：化学／原第4章 化学方程式与化学计算／4.2.1 计算反应物和生成物的量。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留已知量→mol→系数比→目标mol→单位；前置已配平、完全反应/实际消耗量条件。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：已知质量或体积；已知mol；反应系数比；目标mol；目标质量或体积。
- 科学依据：chem_standard（curriculum；partially_verified）；os_stoichiometry（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学4-4.2.1-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem04.js sections[id=4.2.1]；data/notes/chem04.json /4.2.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-4_2_1-01 · 铝制氢例题的单位与系数路径

- 归属：化学／原第4章 化学方程式与化学计算／4.2.1 计算反应物和生成物的量。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：把质量到mol再到气体体积逐步拆开
- 绘图要求：
  - 引用5.40g Al/27.0=.200mol，2Al:3H2给.300mol，Vm=24.0得7.20L
  - 每箭头写运算及单位约分；不得把22.4换入题给24.0
  - 原料完全反应与酸足量条件保留
- 必须文字标注：5.40g Al；M=27.0g/mol；0.200mol；3/2；0.300mol H₂；V_m=24.0；7.20L。
- 科学依据：chem_standard（curriculum；partially_verified）；os_stoichiometry（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.2.1]；data/notes/chem04.json /4.2.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-4_2_2 · 4.2.2 关于不纯物的计算：模块03知识结构

- 归属：化学／原第4章 化学方程式与化学计算／4.2.2 关于不纯物的计算。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留样品→杂质假设→有效质量→反应→反推纯度；杂质参与反应时加“资料不足/需另模型”出口。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：总样品；反应性与杂质假设；纯物质质量；化学计量；反算纯度。
- 科学依据：chem_standard（curriculum；partially_verified）；os_stoichiometry（science_not_exam_scope；partially_verified）；os_yields（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学4-4.2.2-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem04.js sections[id=4.2.2]；data/notes/chem04.json /4.2.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-4_2_2-01 · 纯度与惰性杂质的质量分流

- 归属：化学／原第4章 化学方程式与化学计算／4.2.2 关于不纯物的计算。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：分开有效投料与总样品质量
- 绘图要求：
  - 25g样品分20gCaCO3与5g惰性杂质，纯度80%；纯盐分解理论CO2=8.8g、CaO=11.2g
  - 杂质直接留到残渣，不画参与产气
  - 所有条块同质量比例尺，总质量25=11.2+8.8+5
- 必须文字标注：25.0g样品；20.0g CaCO₃；5.0g杂质；80%；8.80g CO₂；11.2g CaO。
- 科学依据：chem_standard（curriculum；partially_verified）；os_stoichiometry（science_not_exam_scope；partially_verified）；os_yields（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.2.2]；data/notes/chem04.json /4.2.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-4_2_3 · 4.2.3 利用限量反应物的计算：模块03知识结构

- 归属：化学／原第4章 化学方程式与化学计算／4.2.3 利用限量反应物的计算。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留各自mol→n/系数→最小ξ→产物/剩余；所有分支共用同一ξ，不能分别算产物后相加。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：分别求初始mol；除各自系数；最小值决定反应进度；产物与剩余。
- 科学依据：chem_standard（curriculum；partially_verified）；os_yields（science_not_exam_scope；partially_verified）；os_stoichiometry（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学4-4.2.3-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem04.js sections[id=4.2.3]；data/notes/chem04.json /4.2.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-4_2_3-01 · 按n/系数归一化比较限量物

- 归属：化学／原第4章 化学方程式与化学计算／4.2.3 利用限量反应物的计算。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：解释为什么不能直接比mol大小
- 绘图要求：
  - 引用1molN2、2molH2，归一化分别1和2/3mol反应进度
  - H2先耗尽，NH3=4/3mol、N2剩1/3；同一ξ应用于所有物质
  - 归一化条长度按1:2/3，不能把反应进度轴当质量
- 必须文字标注：n₀/系数；N₂:1；H₂:2/3；ξ=2/3mol；NH₃=4/3mol；N₂剩1/3mol。
- 科学依据：chem_standard（curriculum；partially_verified）；os_yields（science_not_exam_scope；partially_verified）；os_stoichiometry（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.2.3]；data/notes/chem04.json /4.2.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-CHEM-4_2_4 · 4.2.4 产率的计算：模块03知识结构

- 归属：化学／原第4章 化学方程式与化学计算／4.2.4 产率的计算。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留有效投料→限量物→理论量→实际纯产品→产率，逆算需求另标反向除以η而非乘η。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：有效投料；限量判断；理论产量；实际纯产品；产率与误差解释。
- 科学依据：chem_standard（curriculum；partially_verified）；os_yields（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-化学4-4.2.4-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/chem04.js sections[id=4.2.4]；data/notes/chem04.json /4.2.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-CHEM-4_2_4-01 · 理论与实际纯产品的产率分母

- 归属：化学／原第4章 化学方程式与化学计算／4.2.4 产率的计算。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：区分损失比例与产率
- 绘图要求：
  - 原例理论10.0g、实际8.20g，条形长度同尺度；差1.80g只标未获得部分，不擅断原因
  - 分子为同一纯产品实际质量，分母为正确限量物推得理论量
  - 湿产品/杂质另设误差方向注，不把表观>100%当真实超产
- 必须文字标注：理论10.0g；实际纯品8.20g；差1.80g；产率82.0%；纯产品条件。
- 科学依据：chem_standard（curriculum；partially_verified）；os_yields（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/chem04.js sections[id=4.2.4]；data/notes/chem04.json /4.2.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-1_1 · 1.1 生命离不开水：模块03知识结构

- 归属：生物／原第1章 生物是由什么组成的／1.1 生命离不开水。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 极性/氢键分支到溶解、比热、汽化、内聚和冰密度，再逐项连功能；两种热量模型不可合成单线。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：极性水分子；分子间氢键；热学与溶解性质；生命中的作用。
- 科学依据：os_water（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物1-1.1-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio01.js sections[id=1.1]；data/notes/bio01.json /1.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_1-01 · 同Q同m的比热比较数据图

- 归属：生物／原第1章 生物是由什么组成的／1.1 生命离不开水。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：区分温升与汽化吸热
- 绘图要求：
  - 用标准例相同m和吸热Q、水升2℃、油升4℃，温升条比1:2、比热比2:1
  - 注明无相变和热损相同假设，不能从同热源自动推出同Q
  - 与蒸发面板仅以概念分支关联，不混Q=mcΔT与mL
- 必须文字标注：同Q/同m；ΔT水=2℃；ΔT油=4℃；比热比2:1；无相变。
- 科学依据：os_water（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.1]；data/notes/bio01.json /1.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-1_2 · 1.2 生物体必需的无机盐：模块03知识结构

- 归属：生物／原第1章 生物是由什么组成的／1.2 生物体必需的无机盐。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 离子形式分结构成分、渗透、缓冲、调节各支，缺素/补回作为证据层，不把每个离子都连到全部功能。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：离子或盐形式；结构组分／调节作用；缺素实验；证据与限制。
- 科学依据：os_water（science；partially_verified）；os_plant_nutrition（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物1-1.2-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio01.js sections[id=1.2]；data/notes/bio01.json /1.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_2-01 · 缺Mg与恢复供应的受控比较

- 归属：生物／原第1章 生物是由什么组成的／1.2 生物体必需的无机盐。
- 类型／动作／优先级：实验装置图；新增需求；P1。
- 教学目的：把必需元素证据与控制变量对应
- 绘图要求：
  - 三组完整、缺Mg、补回Mg，画相同起始状态，不凭空给植株高度或症状
  - 题给平均干重6/3/5g只作为原创题数据，样本量/误差未知不画显著性星号
  - 培养液配方/浓度、重复数待教师与教材确认，不在图中补猜
- 必须文字标注：完整营养；−Mg；恢复Mg；同品种/苗龄/光温；平均干重6/3/5g；重复与误差待定。
- 科学依据：os_water（science；partially_verified）；os_plant_nutrition（science_not_exam_scope；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.2]；data/notes/bio01.json /1.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图；器材/条件与教师或适用实验资料确认；只画原理，不补猜药品配方或危险操作。。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-1_3 · 1.3 能量的主要来源——糖类：模块03知识结构

- 归属：生物／原第1章 生物是由什么组成的／1.3 能量的主要来源——糖类。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 分类树与缩合/水解反应分层；贮能和结构功能分支，不暗示任意单糖/二糖能直接成为任意多糖。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：单糖；缩合成糖苷键；多糖结构差异；贮能或支持功能。
- 科学依据：os_carbohydrates（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物1-1.3-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio01.js sections[id=1.3]；data/notes/bio01.json /1.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_3-01 · 单链与多链缩合的连接计数

- 归属：生物／原第1章 生物是由什么组成的／1.3 能量的主要来源——糖类。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：把脱水n-m从可数图推导
- 绘图要求：
  - 主面板5个葡萄糖成单链4条糖苷键、4水，Mr=5×180−4×18=828
  - 辅助面板10单体成两条无环链，总连接8；不要画成环
  - 六边形为单体符号，非准确结构式，链数边界醒目
- 必须文字标注：n个单体；m条无环链；键/水=n-m；5/1/4；Mr828。
- 科学依据：os_carbohydrates（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.3]；data/notes/bio01.json /1.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_3-02 · 淀粉、糖原与纤维素的结构功能对照

- 归属：生物／原第1章 生物是由什么组成的／1.3 能量的主要来源——糖类。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：连接键型与分支导致的功能差异
- 绘图要求：
  - 用明确符号表示α连接与β连接，纤维素邻链间氢键与共价糖苷键分线型
  - 糖原支化多，淀粉注明直链/支链成分差异，不能写淀粉全无分支
  - 详细碳位编号需化学结构来源确认；无证据只画定性连接示意
- 必须文字标注：α/β连接；糖苷键；分支；邻链氢键；贮能/支撑；示意。
- 科学依据：os_carbohydrates（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.3]；data/notes/bio01.json /1.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-1_4 · 1.4 贮存能量的物质——脂质：模块03知识结构

- 归属：生物／原第1章 生物是由什么组成的／1.4 贮存能量的物质——脂质。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 分三甘油酯/磷脂/固醇，各接结构、极性和功能；固醇不可置于甘油+脂肪酸的线性路径。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：脂质类型；非极性或两亲性结构；聚集形式；储能／膜／调节功能。
- 科学依据：os_lipids（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物1-1.4-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio01.js sections[id=1.4]；data/notes/bio01.json /1.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_4-01 · 相同能量下脂肪与糖所需质量

- 归属：生物／原第1章 生物是由什么组成的／1.4 贮存能量的物质——脂质。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：将储能效率与具体题给值关联
- 绘图要求：
  - 采用题给39与17kJ/g，为78kJ分别需2.00、4.59g
  - 两条质量条共用g标尺、能量目标一致；不伪装食品实测成分表
  - 只比较给定完全氧化模型，不推所有组织优先燃料
- 必须文字标注：78kJ；39/17kJ·g⁻¹；脂肪2.00g；糖4.59g；题给模型。
- 科学依据：os_lipids（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.4]；data/notes/bio01.json /1.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_4-02 · 胆固醇四环骨架与其他脂质的区别

- 归属：生物／原第1章 生物是由什么组成的／1.4 贮存能量的物质——脂质。
- 类型／动作／优先级：结构示意图；新增需求；P2。
- 教学目的：阻止把全部脂质都套为甘油和脂肪酸
- 绘图要求：
  - 以胆固醇为例正确画三个六元环加一个五元环的稠合骨架，OH及侧链位置须按可靠结构来源确认
  - 不把性激素或维生素D画成与胆固醇完全相同，尤其不能把开环衍生物硬画成同一四环
  - 旁注三甘油酯/磷脂组成作比较，不重复制全套相同图
- 必须文字标注：胆固醇示例；6-6-6-5稠环；OH(待结构复核)；非甘油脂肪酸聚合物。
- 科学依据：os_lipids（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.4]；data/notes/bio01.json /1.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-1_5 · 1.5 生命活动的承担者——蛋白质：模块03知识结构

- 归属：生物／原第1章 生物是由什么组成的／1.5 生命活动的承担者——蛋白质。
- 类型／动作／优先级：结构示意图；局部修正；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 结构一到四级是层次不是所有蛋白都经历四级；变性与肽键水解分不同出口，不能同义。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：氨基酸序列；局部结构；整体折叠／亚基；形状与功能；变性或水解。
- 科学依据：os_proteins（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物1-1.5-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio01.js sections[id=1.5]；data/notes/bio01.json /1.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_5-01 · 多肽链数、端基与脱水计数

- 归属：生物／原第1章 生物是由什么组成的／1.5 生命活动的承担者——蛋白质。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：让n-m和主链端基条件可见
- 绘图要求：
  - 用已有6氨基酸成2条无环链，画总4肽键、水4，单体Mr100时总Mr528
  - 每链主链端各一；R基可额外含氨基/羧基，不能把总端基数当绝对总官能团数
  - 额外交联与环肽不套本图
- 必须文字标注：n=6；m=2；肽键4；脱水4；主链两端；Mr528；非环无额外交联。
- 科学依据：os_proteins（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.5]；data/notes/bio01.json /1.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_5-02 · 变性与肽键水解的不同结果

- 归属：生物／原第1章 生物是由什么组成的／1.5 生命活动的承担者——蛋白质。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：把构象改变与主链断裂视觉分离
- 绘图要求：
  - 同一肽链：构象改变支路保留主链连接；水解支路断特定肽键并加水
  - 变性可逆性依条件，不用不可逆图标包办全部蛋白
  - 不把二硫键、氢键或肽键都画成同色同义，精确结构仅在来源核实后添加
- 必须文字标注：完整肽链；空间构象改变；肽键水解；水；不同键型；条件性可逆。
- 科学依据：os_proteins（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.5]；data/notes/bio01.json /1.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-1_6 · 1.6 遗传信息的携带者——核酸：模块03知识结构

- 归属：生物／原第1章 生物是由什么组成的／1.6 遗传信息的携带者——核酸。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 核苷酸组成后分DNA/RNA，DNA互补双链与序列信息分别解释；总体配对数量规律不能套单链。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：核苷酸组成；糖磷酸骨架；碱基序列；互补双链；遗传信息。
- 科学依据：os_nucleic（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物1-1.6-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio01.js sections[id=1.6]；data/notes/bio01.json /1.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_6-01 · 双链DNA碱基与氢键计数账本

- 归属：生物／原第1章 生物是由什么组成的／1.6 遗传信息的携带者——核酸。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：避免把核苷酸数、碱基对与氢键混数
- 绘图要求：
  - 总1000核苷酸，A/T各200、G/C各300，共500对
  - AT200对、GC300对，对应400+900=1300氢键；不要把G与C各当300对再重复
  - 这是一组原创题数据的计数表，不是基因组实测比例
- 必须文字标注：1000核苷酸；500对；AT200对；GC300对；2/3氢键；总1300。
- 科学依据：os_nucleic（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.6]；data/notes/bio01.json /1.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-1_6-02 · 糖磷酸骨架与碱基配对的键位比较

- 归属：生物／原第1章 生物是由什么组成的／1.6 遗传信息的携带者——核酸。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：区分同链共价连接与链间氢键
- 绘图要求：
  - 按可靠结构源标糖的3′与5′方向、磷酸二酯连接及碱基氢键
  - DNA/RNA糖与T/U变化只在对应位置显示，不能改写全部骨架连法
  - 若只是组成图必须写示意，不凭空补原子键角；DNA解链不等于骨架水解
- 必须文字标注：3′/5′；磷酸二酯键；糖/磷酸；碱基氢键；DNA/RNA差异；解链/水解。
- 科学依据：os_nucleic（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio01.js sections[id=1.6]；data/notes/bio01.json /1.6。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-2_1 · 2.1 细胞是生物的基本单位：模块03知识结构

- 归属：生物／原第2章 细胞的结构与功能／2.1 细胞是生物的基本单位。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 细胞学说/观察方法/原核真核/尺度约束分不同关系支；特化无核与原核无核膜分开，避免单项分类。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：细胞学说；显微证据；原核与真核；特化例外；大小与交换限制。
- 科学依据：os_microscope（science；partially_verified）；os_prokaryotes（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物2-2.1-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio02.js sections[id=2.1]；data/notes/bio02.json /2.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-2_1-01 · 显微图比例尺与表面积体积比

- 归属：生物／原第2章 细胞的结构与功能／2.1 细胞是生物的基本单位。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：让长度换算与尺寸限制有图可验
- 绘图要求：
  - 比例尺图长20mm代表10µm，细胞图长60mm，绘制长度比例1:3并标实际30µm
  - mm为题给印刷测量值，不保证浏览器显示物理毫米
  - 另一面板立方体边1/2：SA6/24、V1/8、SA/V6/3，单位长度⁻¹
- 必须文字标注：比例尺10µm；图长比1:3；实际30µm；边a/2a；SA/V=6/a。
- 科学依据：os_microscope（science；partially_verified）；os_prokaryotes（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.1]；data/notes/bio02.json /2.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-2_1-02 · 典型动植物细胞与特化例外

- 归属：生物／原第2章 细胞的结构与功能／2.1 细胞是生物的基本单位。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：补足植物细胞结构并避免单结构归类
- 绘图要求：
  - 并列典型光合植物与动物细胞，植物壁、中央液泡、叶绿体可见，动物无壁
  - 另用小面板根细胞无叶绿体、成熟哺乳红细胞无核，说明不能单项判断谱系
  - 各结构比例仅示意；本图可关联2.3的液泡/叶绿体功能，不重复复制为新课程节
- 必须文字标注：膜/壁；中央液泡；叶绿体；动物细胞；根细胞例外；成熟红细胞例外。
- 科学依据：os_microscope（science；partially_verified）；os_prokaryotes（science；partially_verified）；os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.1]；data/notes/bio02.json /2.1。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

建议跨节引用（尚未渲染）：生物2／2.3。

### ILL-MAP-BIO-2_2 · 2.2 细胞膜——物质进出的门户：模块03知识结构

- 归属：生物／原第2章 细胞的结构与功能／2.2 细胞膜——物质进出的门户。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 脂双层/蛋白结构分支到简单/易化/一级/二级主动/膜泡运输；渗透再接细胞体积变化与壁约束。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：两亲磷脂双层；疏水屏障与膜蛋白；被动／主动运输；渗透和体积变化。
- 科学依据：os_membranes（science；partially_verified）；os_passive（science；partially_verified）；os_active（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物2-2.2-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio02.js sections[id=2.2]；data/notes/bio02.json /2.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-2_2-01 · 动物与植物细胞渗透前后比较

- 归属：生物／原第2章 细胞的结构与功能／2.2 细胞膜——物质进出的门户。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：比较同一水移动机制下壁的机械作用
- 绘图要求：
  - 低渗/近等渗/高渗三列，动物对应膨胀或溶血/平衡/皱缩，植物对应膨压/较低膨压/质壁分离
  - 水双向小箭头与净移动粗箭头分开，平衡不是分子静止
  - 膜与壁分开画，先确认溶质难透膜与外压条件
- 必须文字标注：低/等/高渗；水净移动；细胞膜；植物壁；膨压；质壁分离；动物无壁。
- 科学依据：os_membranes（science；partially_verified）；os_passive（science；partially_verified）；os_active（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.2]；data/notes/bio02.json /2.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

建议跨节引用（尚未渲染）：生物2／2.5。

### ILL-PLAN-BIO-2_2-02 · 马铃薯质量变化与控制变量

- 归属：生物／原第2章 细胞的结构与功能／2.2 细胞膜——物质进出的门户。
- 类型／动作／优先级：实验装置图；新增需求；P1。
- 教学目的：把渗透推断连到测量与误差
- 绘图要求：
  - 等尺寸同来源条块、定温定时容器、前后天平、统一吸干表面液方式
  - 引用2.00→2.20g=+10%原题；不编造外液绝对浓度或水势值
  - 图注区分观测增重与机理推断，给空白记录表与重复提醒
- 必须文字标注：同来源/尺寸；温度/时间/液量；初2.00g/末2.20g；+10%；表面液处理。
- 科学依据：os_membranes（science；partially_verified）；os_passive（science；partially_verified）；os_active（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.2]；data/notes/bio02.json /2.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图；器材/条件与教师或适用实验资料确认；只画原理，不补猜药品配方或危险操作。。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-2_2-03 · 载体饱和与主动运输的证据边界

- 归属：生物／原第2章 细胞的结构与功能／2.2 细胞膜——物质进出的门户。
- 类型／动作／优先级：精确科学SVG；新增需求；P1。
- 教学目的：说明平台不能单独证明主动运输
- 绘图要求：
  - 定性比较简单扩散和载体介导易化扩散对驱动力的响应，平台来自有限转运能力
  - 纵轴用通量/速率，横轴具体浓度差或底物浓度需先按题设确认，不混电化学梯度与浓度
  - 能量抑制和逆梯度证据另列，示意曲线不伪造实测数据
- 必须文字标注：浓度条件(待题设)；通量/速率；简单扩散；载体介导易化扩散；平台≠主动；模型示意。
- 科学依据：os_membranes（science；partially_verified）；os_passive（science；partially_verified）；os_active（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.2]；data/notes/bio02.json /2.2。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-2_3 · 2.3 细胞器——系统内的分工协作：模块03知识结构

- 归属：生物／原第2章 细胞的结构与功能／2.3 细胞器——系统内的分工协作。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留分泌货物的线性交通；ATP供能、膜回收只画旁路，不作货物串联站。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：核糖体合成；粗面内质网加工；囊泡；高尔基体；分泌囊泡；胞吐。
- 科学依据：os_cells（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物2-2.3-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio02.js sections[id=2.3]；data/notes/bio02.json /2.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-2_3-01 · 脉冲追踪的区室时间顺序

- 归属：生物／原第2章 细胞的结构与功能／2.3 细胞器——系统内的分工协作。
- 类型／动作／优先级：结构示意图；新增需求；P1。
- 教学目的：从时间信息推理货物途径并保留证据边界
- 绘图要求：
  - 原题2min粗面ER、10min高尔基体、20min囊泡；画时间标注，不画未给比例的“放射性峰”
  - 细胞外终点若未测只用待确认虚线，不把先后出现说成全部蛋白通路
  - 放射性仅历史/资料示意，不提供实验操作
- 必须文字标注：2min ER；10min高尔基体；20min囊泡；标记氨基酸；时序证据；终点待证。
- 科学依据：os_cells（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.3]；data/notes/bio02.json /2.3。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-2_4 · 2.4 细胞核——细胞的控制中心：模块03知识结构

- 归属：生物／原第2章 细胞的结构与功能／2.4 细胞核——细胞的控制中心。
- 类型／动作／优先级：结构示意图；保留／复用；P2。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 保留DNA→RNA交流→蛋白表达→功能的概览；核实验与细胞质残留属于证据/限制旁支。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：DNA与染色质；转录及核质交流；蛋白质表达；细胞功能。
- 科学依据：os_cells（science；partially_verified）；os_nucleic（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`yes`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物2-2.4-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio02.js sections[id=2.4]；data/notes/bio02.json /2.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-PLAN-BIO-2_4-01 · 去核实验对照与结论边界

- 归属：生物／原第2章 细胞的结构与功能／2.4 细胞核——细胞的控制中心。
- 类型／动作／优先级：实验装置图；新增需求；P1。
- 教学目的：把核作用证据与手术损伤混淆分开
- 绘图要求：
  - 并列保核、去核、假手术组，时间序列观察作为空白设计，不虚构存活时间和具体性状数值
  - 注明需真实实验来源确认条件，已有RNA/蛋白的短期效应不被删除
  - 不能把细胞质作用抹掉或画成核移走后立即全功能归零
- 必须文字标注：保核；去核；假手术；相同培养条件；时间序列；手术损伤控制。
- 科学依据：os_cells（science；partially_verified）；os_nucleic（science；partially_verified）。
- 推荐格式／尺寸：SVG；1200×800；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`no`；当前没有满足该教学目的的同节图；可复用基础颜色与符号，不能把计划当成成品。。
- 模块用途：04、05、06、08、09、10、12。
- 原文定位：lessons/bio02.js sections[id=2.4]；data/notes/bio02.json /2.4。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图；器材/条件与教师或适用实验资料确认；只画原理，不补猜药品配方或危险操作。。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MAP-BIO-2_5 · 2.5 细胞壁——细胞的保护外墙：模块03知识结构

- 归属：生物／原第2章 细胞的结构与功能／2.5 细胞壁——细胞的保护外墙。
- 类型／动作／优先级：结构示意图；重绘；P1。
- 教学目的：把本节关系类型、适用条件与学习路径呈现为知识结构，而非装饰性箭头。
- 绘图要求：
  - 结构层次、机械支撑、透过性与胞间交流分别连功能；膨压来自膜渗透和壁约束共同作用，不画“壁阻止水进入”。
  - 关系标签应写因果、条件、分类或计算步骤；不同关系不混用同一种无说明箭头。
- 必须文字标注：纤维素网络与基质；壁的支持约束；膨压；膜与壁不同作用。
- 科学依据：os_cells（science；partially_verified）；os_carbohydrates（science；partially_verified）。
- 推荐格式／尺寸：HTML/CSS（可复用SVG引用，不强求另存一张图片）；960×640；标签渲染至少12 CSS px。多面板窄屏纵向排列；不得仅缩小整幅造成文字不可读。
- 现有图能否复用：`partial`；保留现有文件；按本条决定复用、局部改标或重绘；本轮不执行绘图。 当前：`batch-ui.js`，选择器：`[id="unit-生物2-2.5-m3"] .concept-flow`。
- 模块用途：03。
- 原文定位：lessons/bio02.js sections[id=2.5]；data/notes/bio02.json /2.5。
- 制作前门槛：按所列科学来源核对每个标签与几何/计量条件；确认源小节与例题数据未变；独立验算数值、单位、箭头及区室；在手机和电脑检查文字/图例；不得声称为官方真题图或2027必考图。
- 验收：符合drawing_requirements的每条约束；文字可选取，图形元素与文字分层；颜色外再以线型/形状区分；练习留空版须与解答标注版分开，且只取已有题设。
- 当前状态：`not_executed_review_only`；无新输出文件。

### ILL-MATH-C01-PENDING · 直线与坐标条件图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第1章 直角坐标系与直线／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第1章“直角坐标系与直线”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得本章真实小节和给定直线条件后再作图；横纵坐标、截距、斜率的标注必须来自已确认题设，不自行指定方程。
  - 禁止先填如1.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：x轴；y轴；原点；斜率/截距(待题设)。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /81；reports/math_subject_mapping.csv 数学1。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C02-PENDING · 二次函数与方程根的关系图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第2章 一元二次方程式与二次函数／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第2章“一元二次方程式与二次函数”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 确认二次函数式、定义域与判别式议题后绘制抛物线，核对顶点、对称轴、零点；不为未知小节强选具体参数。
  - 禁止先填如2.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：x；y；顶点/对称轴；零点/根(待定)。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /82；reports/math_subject_mapping.csv 数学2。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C03-PENDING · 多项式零点与符号图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第3章 多项式／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第3章“多项式”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 先确认实际小节中是否涉及图像和根的重数，再用已核实多项式表达式绘制；不得从章名推定必须考某次多项式。
  - 禁止先填如3.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：定义域；零点；次数/重数(待证)；符号区间。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /83；reports/math_subject_mapping.csv 数学3。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C04-PENDING · 根式条件与平方验根图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第4章 无理式／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第4章“无理式”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得根式与方程原题后，显示根式定义域及原方程交点；平方后的额外解只能作为待检验点，不能假定某个题号。
  - 禁止先填如4.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：根式定义域；原式；候选解；验根。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /84；reports/math_subject_mapping.csv 数学4。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C05-PENDING · 函数映射与定义域值域图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第5章 函数／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第5章“函数”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得函数规则及定义域后画映射/坐标图，区分函数本身与图像；单射、反函数等是否属于本章小节需另证据。
  - 禁止先填如5.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：定义域；对应规则；值域；横纵轴。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /85；reports/math_subject_mapping.csv 数学5。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C06-PENDING · 不等式符号区间图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第6章 不等式／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第6章“不等式”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 确认具体不等式后标临界点、空心实心端点、不可取点；不擅加分式/参数不等式为真实小节。
  - 禁止先填如6.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：临界点；开闭端点；符号；解集。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /86；reports/math_subject_mapping.csv 数学6。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C07-PENDING · 命题逻辑关系示意（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第7章 逻辑／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：结构示意图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第7章“逻辑”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得真实小节涉及的联结词和命题例后设计真值表/集合关系；图不代替形式证明，不从章名新增逻辑符号范围。
  - 禁止先填如7.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：命题p/q(待定)；条件；真假；推理关系。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /87；reports/math_subject_mapping.csv 数学7。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C08-PENDING · 圆心角、弧长与弧度图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第8章 角度与弧度／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：精确科学SVG；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第8章“角度与弧度”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 确认实际图形后以同一圆心画半径r、弧长s、角θ，只有核实到弧度定义后使用s=rθ；角度单位不能混用。
  - 禁止先填如8.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：圆心；r；s；θ；角单位。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /88；reports/math_subject_mapping.csv 数学8。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C09-PENDING · 任意角三角函数与单位圆（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第9章 任意角的三角函数／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第9章“任意角的三角函数”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 先确认小节中单位圆与函数图对应范围，若使用单位圆必须标坐标和正方向，函数周期/弧度坐标从实际公式计算。
  - 禁止先填如9.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：单位圆(待范围)；x/y；θ正向；sin/cos等(待范围)。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /89；reports/math_subject_mapping.csv 数学9。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C10-PENDING · 三角测量已知与未知图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第10章 三角学的应用／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：精确科学SVG；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第10章“三角学的应用”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得真实应用题及三角形数据后画比例合理的示意，标已知边角与待求量；不编造测距情境为原有小节。
  - 禁止先填如10.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：顶点；已知边角；待求量；示意非比例。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /90；reports/math_subject_mapping.csv 数学10。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C11-PENDING · 恒等变形与三角方程解图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第11章 三角恒等式与三角方程式／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第11章“三角恒等式与三角方程式”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 确认具体恒等式与方程后才选函数交点图；周期、定义域与根的范围必须完整，不以有限视窗代替全部解。
  - 禁止先填如11.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：函数式(待定)；区间；周期；候选交点/全部解条件。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /91；reports/math_subject_mapping.csv 数学11。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C12-PENDING · 指数与对数的定义域渐近线图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第12章 指数与对数／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第12章“指数与对数”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得底数和实际小节后绘图，底数正且不为1、对数真数正等条件需核实写入；不任意为题库指定函数。
  - 禁止先填如12.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：底数条件；定义域；渐近线；交点。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /92；reports/math_subject_mapping.csv 数学12。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C13-PENDING · 数列项与部分和的比较图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第13章 数列与级数／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：精确科学SVG；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第13章“数列与级数”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 确认数列类型和项/和的学习点后画离散点与项数，不把数列无条件连成连续函数；无限级数收敛条件须另据小节。
  - 禁止先填如13.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：n∈正整数；a_n；S_n(若适用)；题设条件。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /93；reports/math_subject_mapping.csv 数学13。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C14-PENDING · 行列式结构与符号运算图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第14章 行列式／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：结构示意图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第14章“行列式”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 只在取得真实目录与题设后画元素位置、展开符号或几何解释；不能因章名断言课程包含高阶行列式。
  - 禁止先填如14.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：行/列；元素；运算/展开(待定)；维度。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /94；reports/math_subject_mapping.csv 数学14。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C15-PENDING · 矩阵维数与运算对应图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第15章 矩阵／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：结构示意图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第15章“矩阵”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 核实运算种类后画行列配对与维数条件；若涉及变换再画向量作用，不能自行将变换新增为小节。
  - 禁止先填如15.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：m×n；行/列；运算维数条件；结果维数。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /95；reports/math_subject_mapping.csv 数学15。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C16-PENDING · 圆的方程与几何条件图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第16章 圆／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第16章“圆”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得圆方程、直线等题设后核对圆心半径、相交/相切条件；坐标范围和尺度统一，不能只画装饰圆。
  - 禁止先填如16.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：圆心；半径；坐标轴；条件点/线(待定)。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /96；reports/math_subject_mapping.csv 数学16。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C17-PENDING · 平面向量分量与运算图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第17章 平面向量／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：精确科学SVG；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第17章“平面向量”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得向量及运算范围后按分量计算端点，方向、起点、自由向量表示一致；不能把线段长度都当成有向量。
  - 禁止先填如17.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：起点/端点；向量名；x/y分量；正方向。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /97；reports/math_subject_mapping.csv 数学17。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C18-PENDING · 立体几何投影与位置关系图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第18章 立体几何／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：精确科学SVG；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第18章“立体几何”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 确认实体、点线面条件后选择投影与可见性虚线，直角等记号仅来自题设或证明；不虚构空间角或平行关系。
  - 禁止先填如18.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：点/线/面；已知关系；遮挡虚线；非比例投影。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /98；reports/math_subject_mapping.csv 数学18。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C19-PENDING · 排列组合的选择过程图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第19章 排列组合／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：结构示意图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第19章“排列组合”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得真实计数情境后画树图/格子或分类流程，区分顺序、是否放回与重复；不能从章名推断具体模型。
  - 禁止先填如19.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：有无顺序；是否重复/放回；分支条件；计数合并。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /99；reports/math_subject_mapping.csv 数学19。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C20-PENDING · 二项式展开项与系数图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第20章 二项式定理／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：结构示意图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第20章“二项式定理”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 确认本节公式范围和给定指数后，再画项索引和系数来源；不能以任意帕斯卡三角行当官方要求。
  - 禁止先填如20.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：项索引；系数；两部分幂次；指数范围。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /100；reports/math_subject_mapping.csv 数学20。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C21-PENDING · 极限邻域与函数值区别图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第21章 极限／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第21章“极限”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得具体函数和趋近点后标空实心点、左右趋近；所画视窗不能替代极限证明，是否需ε-δ须教材证据。
  - 禁止先填如21.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：趋近点；函数值；左右趋势；定义域缺口。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /101；reports/math_subject_mapping.csv 数学21。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C22-PENDING · 微分斜率与应用图（一）（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第22章 微分及其应用（一）／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第22章“微分及其应用（一）”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 按真实小节选择函数及点，切线由导数计算、割线由两点计算；极值等应用需实际目录支持，不用标题补造编号。
  - 禁止先填如22.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：f(x)；切点；割线/切线；导数/条件。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /102；reports/math_subject_mapping.csv 数学22。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C23-PENDING · 原函数族与导数关系图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第23章 不定积分及其应用／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第23章“不定积分及其应用”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 确认被积函数、定义区间及应用后画原函数族；任意常数C与分段定义域不能略去，切勿用面积图直接当不定积分定义。
  - 禁止先填如23.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：被积函数；原函数F+C；区间；C。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /103；reports/math_subject_mapping.csv 数学23。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C24-PENDING · 定积分有向面积与区间图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第24章 定积分及其应用／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第24章“定积分及其应用”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得积分式与界限后区分正负面积和几何面积；间断/奇点按题设处理，不能任意补连续性条件。
  - 禁止先填如24.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：a/b；f(x)；正/负区域；有向积分。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /104；reports/math_subject_mapping.csv 数学24。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C25-PENDING · 统计数据展示与参数图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第25章 统计学／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：精确科学SVG；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第25章“统计学”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 先取得真实数据表和统计量范围，注明样本量、单位与分组方式；禁止为插图编造实测分布或显著性。
  - 禁止先填如25.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：变量/单位；n；频数/频率；统计量(待范围)。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /105；reports/math_subject_mapping.csv 数学25。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C26-PENDING · 概率样本空间与条件事件图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第26章 概率／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：结构示意图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第26章“概率”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 确认试验、等可能性和事件条件后画树图/集合图；概率分支和为1，是否独立不能凭图形假设。
  - 禁止先填如26.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：样本空间；事件；条件；分支概率。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /106；reports/math_subject_mapping.csv 数学26。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C27-PENDING · 线性回归散点与拟合图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第27章 线性回归／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第27章“线性回归”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 只能用明确来源或明确原创题给数据；拟合系数独立重算，残差方向与预测区间注明，不把相关关系画成因果。
  - 禁止先填如27.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：变量/单位；数据来源；回归线；残差；外推限制。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /107；reports/math_subject_mapping.csv 数学27。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C28-PENDING · 微分应用图（二）（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第28章 微分及其应用（二）／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第28章“微分及其应用（二）”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 章名证实有该主题但不证实具体小节；取得问题后再画函数、导数及应用量，补全定义域与端点比较。
  - 禁止先填如28.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：函数/导数(待定)；区间；端点；单位/条件。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）；school（p3_high_school_topic_only_not_subsections；verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /108；reports/math_subject_mapping.csv 数学28。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C29-PENDING · 积分法的变换与积分区间图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第29章 积分法／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第29章“积分法”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 核实具体积分方法与公式后决定是否需要坐标变换/面积辅助；只画被确认的内容，不推定学校I/II科目归属。
  - 禁止先填如29.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：积分变量；定义域；界限(若有)；变换条件。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）；school（p3_high_school_topic_only_not_subsections；verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /109；reports/math_subject_mapping.csv 数学29。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C30-PENDING · 微分方程解曲线与初值图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第30章 微分方程式／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第30章“微分方程式”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 取得真实方程、初值和方法范围后绘制经求解验证的曲线；斜率场是否属于课程未确认，不能先生成并称已覆盖。
  - 禁止先填如30.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：方程(待定)；初值；变量/单位；解的适用区间。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）；school（p3_high_school_topic_only_not_subsections；verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /110；reports/math_subject_mapping.csv 数学30。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C31-PENDING · 数学方法的证明或解题关系图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第31章 数学方法／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：结构示意图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第31章“数学方法”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 学校原件列数学方法、仓库有31章，但未提供方法清单；必须先确认具体方法才选归纳/反证/其他图式，不补猜。
  - 禁止先填如31.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：方法名称(待确认)；前提；步骤；结论。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）；school（p3_high_school_topic_only_not_subsections；verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /111；reports/math_subject_mapping.csv 数学31。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C32-PENDING · 坐标变换前后同一点的两套表示（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第32章 坐标变换／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：精确科学SVG；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第32章“坐标变换”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 学校原件与章名支持主题，变换类别、公式与范围仍待确认；取得原题后核对同一点坐标及轴方向。
  - 禁止先填如32.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：旧/新轴；原点；同一点；变换参数(待定)。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）；school（p3_high_school_topic_only_not_subsections；verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /112；reports/math_subject_mapping.csv 数学32。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C33-PENDING · 圆锥曲线方程与几何量图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第33章 圆锥曲线／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：数学函数图；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第33章“圆锥曲线”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 学校列圆锥曲线，仓库有33章，但哪些曲线及学习细目未确认；取得式后独立核对顶点、焦点、准线等实际所需量。
  - 禁止先填如33.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：曲线类型(待定)；坐标轴；参数；题设几何量。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）；school（p3_high_school_topic_only_not_subsections；verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /113；reports/math_subject_mapping.csv 数学33。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C34-PENDING · 复数的代数与几何表示图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第34章 复数／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：精确科学SVG；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第34章“复数”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 学校列复数，仓库有34章，无真实34.1等编号；确认表示法后才画复平面或运算，不能先造极形式小节。
  - 禁止先填如34.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：实轴；虚轴；z(待题设)；模/辐角(待范围)。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）；school（p3_high_school_topic_only_not_subsections；verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /114；reports/math_subject_mapping.csv 数学34。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

### ILL-MATH-C35-PENDING · 空间向量投影与方向图（仅章级待确认）

- 归属：数学旧资料（高数I/II归属未确认）／原第35章 空间向量／真实小节不存在（编号null；I／II待核实）。
- 类型／动作／优先级：精确科学SVG；待核实，禁止先制作；P2。
- 教学目的：待取得真实小节和适用依据后，为已有第35章“空间向量”选择必要的教学图；本条不是已完成小节。
- 绘图要求：
  - 学校列空间向量，实际运算范围待目录；按已确认分量计算三维端点，遮挡和投影可辨，不能凭画法推正交。
  - 禁止先填如35.1的小节号；禁止按卷一/卷二分配I/II；现有volume也不是充分归科证据。
  - 函数/数据/几何参数缺失时不绘制，不虚构题设。
- 必须文字标注：x/y/z；向量；分量；方向/位置关系(待证)。
- 科学依据：repo_curriculum（existing_chapter_title_only；verified）；dz_adv_math_i（subject_identity_only_not_chapter_allocation；partially_verified）；dz_adv_math_ii（subject_identity_only_not_chapter_allocation；partially_verified）；school（p3_high_school_topic_only_not_subsections；verified）。
- 推荐格式／尺寸：SVG（参数确认后，函数图须由确定性计算生成）；1200×800；标签渲染至少12 CSS px。尺寸只是制作建议；未确定函数或装置参数不进入绘图。
- 现有图能否复用：`no`；目前无数学真实小节图；学科导航图不构成教学素材。。
- 模块用途：待真实小节后再确定，不套十二模块。
- 原文定位：data/curriculum.json /115；reports/math_subject_mapping.csv 数学35。
- 制作前门槛：取得兴华实际教材版本及真实小节目录；核实2027适用课程标准及I/II对应；确定实际知识点、原题/原创数据、定义域和参数；审定后再分配真实section_id与科目。
- 验收：本轮必须section_id=null；不将待确认计划计入真实课程或已完成图片。
- 当前状态：`blocked_missing_sections_and_attribution`；无新输出文件。

## 六个界面素材（不计入203项教学记录）

### UI-ASSET-ICON · icon.png导航/界面素材

- 科目：全站或数学组导航；章／节：无（null），仅为界面素材。类型：辅助插画；动作：保留；优先级：P3。
- 目的：仅用于科目导航、应用标识或掌握度界面，不承载教学论证。
- 要求：本轮不改图、不新生成；不得作为科学结构图、函数图或高数I/II小节图的替代。
- 标签：需要可访问文本替代说明，不用图像文字证明知识。
- 科学依据：不承载科学命题，`repo_lessons`仅证明界面引用范围。
- 格式／尺寸：PNG；原图512×512，本轮保留。
- 复用：可；`assets/icon.png`；无新输出。

### UI-ASSET-MATH · math.webp导航/界面素材

- 科目：全站或数学组导航；章／节：无（null），仅为界面素材。类型：辅助插画；动作：保留；优先级：P3。
- 目的：仅用于科目导航、应用标识或掌握度界面，不承载教学论证。
- 要求：本轮不改图、不新生成；不得作为科学结构图、函数图或高数I/II小节图的替代。
- 标签：需要可访问文本替代说明，不用图像文字证明知识。
- 科学依据：不承载科学命题，`repo_lessons`仅证明界面引用范围。
- 格式／尺寸：WEBP；原图256×256，本轮保留。
- 复用：可；`assets/math.webp`；无新输出。

### UI-ASSET-MASTERY · mastery.webp导航/界面素材

- 科目：全站或数学组导航；章／节：无（null），仅为界面素材。类型：辅助插画；动作：保留；优先级：P3。
- 目的：仅用于科目导航、应用标识或掌握度界面，不承载教学论证。
- 要求：本轮不改图、不新生成；不得作为科学结构图、函数图或高数I/II小节图的替代。
- 标签：需要可访问文本替代说明，不用图像文字证明知识。
- 科学依据：不承载科学命题，`repo_lessons`仅证明界面引用范围。
- 格式／尺寸：WEBP；原图512×512，本轮保留。
- 复用：可；`assets/mastery.webp`；无新输出。

### UI-ASSET-BIOLOGY · biology.webp导航/界面素材

- 科目：生物；章／节：无（null），仅为界面素材。类型：辅助插画；动作：保留；优先级：P3。
- 目的：仅用于科目导航、应用标识或掌握度界面，不承载教学论证。
- 要求：本轮不改图、不新生成；不得作为科学结构图、函数图或高数I/II小节图的替代。
- 标签：需要可访问文本替代说明，不用图像文字证明知识。
- 科学依据：不承载科学命题，`repo_lessons`仅证明界面引用范围。
- 格式／尺寸：WEBP；原图256×256，本轮保留。
- 复用：可；`assets/biology.webp`；无新输出。

### UI-ASSET-PHYSICS · physics.webp导航/界面素材

- 科目：物理；章／节：无（null），仅为界面素材。类型：辅助插画；动作：保留；优先级：P3。
- 目的：仅用于科目导航、应用标识或掌握度界面，不承载教学论证。
- 要求：本轮不改图、不新生成；不得作为科学结构图、函数图或高数I/II小节图的替代。
- 标签：需要可访问文本替代说明，不用图像文字证明知识。
- 科学依据：不承载科学命题，`repo_lessons`仅证明界面引用范围。
- 格式／尺寸：WEBP；原图256×256，本轮保留。
- 复用：可；`assets/physics.webp`；无新输出。

### UI-ASSET-CHEMISTRY · chemistry.webp导航/界面素材

- 科目：化学；章／节：无（null），仅为界面素材。类型：辅助插画；动作：保留；优先级：P3。
- 目的：仅用于科目导航、应用标识或掌握度界面，不承载教学论证。
- 要求：本轮不改图、不新生成；不得作为科学结构图、函数图或高数I/II小节图的替代。
- 标签：需要可访问文本替代说明，不用图像文字证明知识。
- 科学依据：不承载科学命题，`repo_lessons`仅证明界面引用范围。
- 格式／尺寸：WEBP；原图256×256，本轮保留。
- 复用：可；`assets/chemistry.webp`；无新输出。

## 验证及剩余工作

运行 `python tools/audit_illustrations.py` 可复核真实章／节、ID、来源、字段、73个SVG引用、41个结构图、35个无伪造编号计划、492项覆盖，以及受保护原文件与被审查提交的字节一致性。脚本只输出文本/JSON/CSV，不调用绘图器或浏览器。加 `--regression` 可同时重跑原有静态/计算/SVG边界检查。

[验证结果](reports/ILLUSTRATION_VALIDATION.json)记录实际检查；[原检查重跑记录](reports/ILLUSTRATION_REGRESSION.json)记录结构、80项计算和43幅SVG文字边界检查；[内容深度审查](reports/CONTENT_DEPTH_AUDIT.md)列41节扩写建议和12节抽查证据。脚本数值检查只核对计划中的选定计算/守恒，不等于未制作图已经通过视觉验收或整课科学审定。

尚待：审定P0科学/排版问题；后续获授权再修正/绘图、补题型攻略与目标映射；取得真实数学小节目录及I／II对照；核实2027适用官方版本；补审73个尚无真实小节的理化生章。此次不以新笔记或新图片填补这些阻碍。
