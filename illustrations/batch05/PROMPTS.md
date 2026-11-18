# 新增章节的独立教学绘图提示词

共94条复合教学图任务；复用8幅已审核V22图，未生成新图。原142任务和缺口保持历史记录。每条为独立可复制规范，XML/路径合格不等于科学准确。

## 生物 第10章 · 10.1 种群

ID：B05-BIO10-10-1；优先级：P0；状态：not_produced。

用途：由出生死亡迁入迁出分析种群变化；比较成长模型与抽样估计的条件。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：N-t指数/逻辑斯谛图；增长率对N图；B/I/D/E收支；标记重捕比例。

关系：K/2为固定参数总增长率峰；每个体增长率不同；m=0时不能除法估无限大。

文字：N、t、K、K/2、rN(1−N/K)、M/N≈m/n。

公式与单位：种群收支：N末=N初+B+I−D−E；密度=N/相应面积或体积。；理想固定倍增：N=N₀×2^(t/g)；逻辑斯谛模型增长速率rN(1−N/K)，固定参数时在K/2最大。；标记重捕估计N≈M×n/m，其中M首标记数、n重捕总数、m重捕中带标记数，m>0且假设需审。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第10章《生态系统》真实小节10.1《种群》制作《种群成长模型与收支》教学图。学习目的：由出生死亡迁入迁出分析种群变化；比较成长模型与抽样估计的条件。本图是有条件的科学模型，非实测图或官方考题。必须出现：N-t指数/逻辑斯谛图；增长率对N图；B/I/D/E收支；标记重捕比例。必须保持关系：K/2为固定参数总增长率峰；每个体增长率不同；m=0时不能除法估无限大。中文标签逐字采用：N、t、K、K/2、rN(1−N/K)、M/N≈m/n。公式及条件：种群收支：N末=N初+B+I−D−E；密度=N/相应面积或体积。；理想固定倍增：N=N₀×2^(t/g)；逻辑斯谛模型增长速率rN(1−N/K)，固定参数时在K/2最大。；标记重捕估计N≈M×n/m，其中M首标记数、n重捕总数、m重捕中带标记数，m>0且假设需审。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 10, authentic subsection 10.1. Display the original Chinese title exactly: 种群成长模型与收支. Topic-specific scientific requirements and instructional purpose: Plot population size versus time for explicitly idealized exponential and logistic models, separately plot logistic total growth rate versus N with its peak at K/2, and distinguish per-capita growth. Include birth/death/immigration/emigration accounting and conditional mark-recapture proportions. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: N-t指数/逻辑斯谛图；增长率对N图；B/I/D/E收支；标记重捕比例. Preserve the following Chinese label strings exactly: N、t、K、K/2、rN(1−N/K)、M/N≈m/n. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 种群收支：N末=N初+B+I−D−E；密度=N/相应面积或体积。；理想固定倍增：N=N₀×2^(t/g)；逻辑斯谛模型增长速率rN(1−N/K)，固定参数时在K/2最大。；标记重捕估计N≈M×n/m，其中M首标记数、n重捕总数、m重捕中带标记数，m>0且假设需审。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：K/2为固定参数总增长率峰；每个体增长率不同；m=0时不能除法估无限大。不得把种群画成另一知识主题；不得改动N、t、K、K/2、rN(1−N/K)、M/N≈m/n的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- K/2为固定参数总增长率峰
- 每个体增长率不同
- m=0时不能除法估无限大
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/45-3-environmental-limits-to-population-growth
- https://openstax.org/books/biology-2e/pages/45-1-population-demography

旧图复用：需新准确图；表内10.1.1仅知识点，不伪造额外课本小节。实际匹配：无。

## 生物 第10章 · 10.2 生态系统

ID：B05-BIO10-10-2；优先级：P0；状态：not_produced。

用途：辨认生态系统组成与营养关系；用食物网和环境证据解释系统变化。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：生产者；草食与肉食消费者；分解者；碎屑食者；无机环境；太阳/化学能。

关系：资源到消费者箭头；多个营养级到分解网络；无机养分回生产者；能量输入与热分散分开。

文字：群落、非生物环境、物质、能量、未按大小比例。

公式与单位：生态系统=生物群落+非生物环境及其联系；边界一般有物质和能量交换。；食物箭头：资源→摄食者，分解网络接收来自多个营养级的死有机物。；干扰分析：列直接作用 → 食物网间接路径 → 非生物与时间尺度 → 提可测预测及对照。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第10章《生态系统》真实小节10.2《生态系统》制作《生态系统功能网络》教学图。学习目的：辨认生态系统组成与营养关系；用食物网和环境证据解释系统变化。本图是有条件的科学模型，非实测图或官方考题。必须出现：生产者；草食与肉食消费者；分解者；碎屑食者；无机环境；太阳/化学能。必须保持关系：资源到消费者箭头；多个营养级到分解网络；无机养分回生产者；能量输入与热分散分开。中文标签逐字采用：群落、非生物环境、物质、能量、未按大小比例。公式及条件：生态系统=生物群落+非生物环境及其联系；边界一般有物质和能量交换。；食物箭头：资源→摄食者，分解网络接收来自多个营养级的死有机物。；干扰分析：列直接作用 → 食物网间接路径 → 非生物与时间尺度 → 提可测预测及对照。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 10, authentic subsection 10.2. Display the original Chinese title exactly: 生态系统功能网络. Topic-specific scientific requirements and instructional purpose: Draw an ecosystem with producers, multiple consumer levels, decomposers, detritivores and abiotic pools. Food arrows go from resource to consumer; dead matter reaches decomposers from all levels. Keep nutrient return separate from energy input and heat loss, and do not make decomposers the exclusive final link of one chain. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 生产者；草食与肉食消费者；分解者；碎屑食者；无机环境；太阳/化学能. Preserve the following Chinese label strings exactly: 群落、非生物环境、物质、能量、未按大小比例. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 生态系统=生物群落+非生物环境及其联系；边界一般有物质和能量交换。；食物箭头：资源→摄食者，分解网络接收来自多个营养级的死有机物。；干扰分析：列直接作用 → 食物网间接路径 → 非生物与时间尺度 → 提可测预测及对照。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：资源到消费者箭头；多个营养级到分解网络；无机养分回生产者；能量输入与热分散分开。不得把生态系统画成另一知识主题；不得改动群落、非生物环境、物质、能量、未按大小比例的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 资源到消费者箭头
- 多个营养级到分解网络
- 无机养分回生产者
- 能量输入与热分散分开
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/46-1-ecology-of-ecosystems

旧图复用：V22食物网可核箭头后局部复用；不改旧缺口记录。实际匹配：无。

## 生物 第10章 · 10.3 物质循环与能量流动

ID：B05-BIO10-10-3；优先级：P0；状态：not_produced。

用途：以收支区分生产量同化与呼吸；正确追踪碳氮磷循环和营养级能流。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：GPP/R/NPP收支；摄入排出呼吸生产；碳循环；氮化学形态；磷地质库。

关系：20000−12000=8000；1000=400+450+150；硝化与反硝化方向分开；能量热不闭合回生产者。

文字：GPP、NPP、R、NH₄⁺、NO₂⁻、NO₃⁻、N₂、条件性箭头。

公式与单位：NPP=GPP−R生产者；消费者简化A=I−F，P=A−R。；相邻营养级传递效率=上层相应生产量/下层相应生产量×100%，边界和时间相同。；硝化：NH₄⁺→NO₂⁻→NO₃⁻（相应需氧微生物过程）；反硝化与之不是同义，固氮从N₂进入生物可利用库。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第10章《生态系统》真实小节10.3《物质循环与能量流动》制作《能流收支与碳氮磷循环》教学图。学习目的：以收支区分生产量同化与呼吸；正确追踪碳氮磷循环和营养级能流。本图是有条件的科学模型，非实测图或官方考题。必须出现：GPP/R/NPP收支；摄入排出呼吸生产；碳循环；氮化学形态；磷地质库。必须保持关系：20000−12000=8000；1000=400+450+150；硝化与反硝化方向分开；能量热不闭合回生产者。中文标签逐字采用：GPP、NPP、R、NH₄⁺、NO₂⁻、NO₃⁻、N₂、条件性箭头。公式及条件：NPP=GPP−R生产者；消费者简化A=I−F，P=A−R。；相邻营养级传递效率=上层相应生产量/下层相应生产量×100%，边界和时间相同。；硝化：NH₄⁺→NO₂⁻→NO₃⁻（相应需氧微生物过程）；反硝化与之不是同义，固氮从N₂进入生物可利用库。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 10, authentic subsection 10.3. Display the original Chinese title exactly: 能流收支与碳氮磷循环. Topic-specific scientific requirements and instructional purpose: Use separate panels for GPP 20000 minus respiration 12000 equals NPP 8000, and consumer intake 1000=egestion 400+respiration 450+production 150. Draw carbon, nitrogen and phosphorus pools with correctly directed labelled transformations; distinguish nitrogen fixation, nitrification and denitrification and never close heat loss into a lossless energy cycle. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: GPP/R/NPP收支；摄入排出呼吸生产；碳循环；氮化学形态；磷地质库. Preserve the following Chinese label strings exactly: GPP、NPP、R、NH₄⁺、NO₂⁻、NO₃⁻、N₂、条件性箭头. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: NPP=GPP−R生产者；消费者简化A=I−F，P=A−R。；相邻营养级传递效率=上层相应生产量/下层相应生产量×100%，边界和时间相同。；硝化：NH₄⁺→NO₂⁻→NO₃⁻（相应需氧微生物过程）；反硝化与之不是同义，固氮从N₂进入生物可利用库。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：20000−12000=8000；1000=400+450+150；硝化与反硝化方向分开；能量热不闭合回生产者。不得把物质循环与能量流动画成另一知识主题；不得改动GPP、NPP、R、NH₄⁺、NO₂⁻、NO₃⁻、N₂、条件性箭头的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 20000−12000=8000
- 1000=400+450+150
- 硝化与反硝化方向分开
- 能量热不闭合回生产者
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/46-2-energy-flow-through-ecosystems
- https://openstax.org/books/biology-2e/pages/46-3-biogeochemical-cycles

旧图复用：V22 B50、B54可复核用于部分能量碳循环；氮磷仍需图。实际匹配：无。

## 生物 第10章 · 10.4 生态系统类型

ID：B05-BIO10-10-4；优先级：P1；状态：not_produced。

用途：以水分温度盐度等解释系统差异；比较自然与人工系统并评价类型推断限制。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：森林草原荒漠寒冷地；河流湖泊；海洋河口湿地；农田城市；温度水分盐度光梯度。

关系：类型边界有过渡；湖泊分层依条件；人工有跨界输入输出；生产率与总量分开。

文字：限制因素、季节性、单位面积、总量、示意非全球实测分布。

公式与单位：类型推断：温度/水分及季节性 + 土壤/底质 + 水流/盐度/光 + 生物与管理历史。；水体生产需光或化学能源、营养等条件；面积大不等于单位面积生产高。；比较相同指标、单位与时间；自然/人工描述管理来源，不否定生态系统组成。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第10章《生态系统》真实小节10.4《生态系统类型》制作《生态系统类型与限制梯度》教学图。学习目的：以水分温度盐度等解释系统差异；比较自然与人工系统并评价类型推断限制。本图是有条件的科学模型，非实测图或官方考题。必须出现：森林草原荒漠寒冷地；河流湖泊；海洋河口湿地；农田城市；温度水分盐度光梯度。必须保持关系：类型边界有过渡；湖泊分层依条件；人工有跨界输入输出；生产率与总量分开。中文标签逐字采用：限制因素、季节性、单位面积、总量、示意非全球实测分布。公式及条件：类型推断：温度/水分及季节性 + 土壤/底质 + 水流/盐度/光 + 生物与管理历史。；水体生产需光或化学能源、营养等条件；面积大不等于单位面积生产高。；比较相同指标、单位与时间；自然/人工描述管理来源，不否定生态系统组成。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 10, authentic subsection 10.4. Display the original Chinese title exactly: 生态系统类型与限制梯度. Topic-specific scientific requirements and instructional purpose: Create a comparison matrix of terrestrial, freshwater, marine, estuarine, wetland and managed ecosystems linked to water, temperature, salinity, light and nutrient limitations. Mark gradients and conditional lake stratification, and distinguish production per unit area from total production. Do not present schematic landscapes as measured global distributions. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 森林草原荒漠寒冷地；河流湖泊；海洋河口湿地；农田城市；温度水分盐度光梯度. Preserve the following Chinese label strings exactly: 限制因素、季节性、单位面积、总量、示意非全球实测分布. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 类型推断：温度/水分及季节性 + 土壤/底质 + 水流/盐度/光 + 生物与管理历史。；水体生产需光或化学能源、营养等条件；面积大不等于单位面积生产高。；比较相同指标、单位与时间；自然/人工描述管理来源，不否定生态系统组成。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：类型边界有过渡；湖泊分层依条件；人工有跨界输入输出；生产率与总量分开。不得把生态系统类型画成另一知识主题；不得改动限制因素、季节性、单位面积、总量、示意非全球实测分布的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 类型边界有过渡
- 湖泊分层依条件
- 人工有跨界输入输出
- 生产率与总量分开
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/44-3-terrestrial-biomes
- https://openstax.org/books/biology-2e/pages/44-4-aquatic-biomes

旧图复用：可用已审核生态示意局部；不以装饰景观代替限制关系。实际匹配：无。

## 生物 第11章 · 11.1 人类对生态环境的影响

ID：B05-BIO11-11-1；优先级：P0；状态：not_produced。

用途：用机制解释人类活动的生态后果；评估环境数据的因果边界。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：营养径流；藻类；死亡有机物；分解者；溶氧曲线；三营养级。

关系：耗氧连到呼吸和分解而非肥料直接吸氧；食物链放大用相同mg/kg。

文字：营养输入、分解耗氧、条件性缺氧、浓度≠总量。

公式与单位：富营养化的条件链：外源营养输入增加 → 初级生产或藻量变化 → 死亡有机物与分解耗氧增加 → 特定条件下溶氧下降。；浓度=污染物质量/样品质量；营养级间比较必须使用相同基准单位。；相对变化=(处理后−基准)/基准；相关数据仍需可比设计才能支持因果解释。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第11章《生态保育与可持续发展》真实小节11.1《人类对生态环境的影响》制作《富营养化因果链与浓度比较》教学图。学习目的：用机制解释人类活动的生态后果；评估环境数据的因果边界。本图是有条件的科学模型，非实测图或官方考题。必须出现：营养径流；藻类；死亡有机物；分解者；溶氧曲线；三营养级。必须保持关系：耗氧连到呼吸和分解而非肥料直接吸氧；食物链放大用相同mg/kg。中文标签逐字采用：营养输入、分解耗氧、条件性缺氧、浓度≠总量。公式及条件：富营养化的条件链：外源营养输入增加 → 初级生产或藻量变化 → 死亡有机物与分解耗氧增加 → 特定条件下溶氧下降。；浓度=污染物质量/样品质量；营养级间比较必须使用相同基准单位。；相对变化=(处理后−基准)/基准；相关数据仍需可比设计才能支持因果解释。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 11, authentic subsection 11.1. Display the original Chinese title exactly: 富营养化因果链与浓度比较. Topic-specific scientific requirements and instructional purpose: Show nutrient enrichment, algal growth, organic matter decomposition and conditional oxygen depletion. Use a separate food-chain panel with consistent mg/kg concentration units; do not equate concentration with total mass. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 营养径流；藻类；死亡有机物；分解者；溶氧曲线；三营养级. Preserve the following Chinese label strings exactly: 营养输入、分解耗氧、条件性缺氧、浓度≠总量. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 富营养化的条件链：外源营养输入增加 → 初级生产或藻量变化 → 死亡有机物与分解耗氧增加 → 特定条件下溶氧下降。；浓度=污染物质量/样品质量；营养级间比较必须使用相同基准单位。；相对变化=(处理后−基准)/基准；相关数据仍需可比设计才能支持因果解释。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：耗氧连到呼吸和分解而非肥料直接吸氧；食物链放大用相同mg/kg。不得把人类对生态环境的影响画成另一知识主题；不得改动营养输入、分解耗氧、条件性缺氧、浓度≠总量的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 耗氧连到呼吸和分解而非肥料直接吸氧
- 食物链放大用相同mg/kg
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/47-3-threats-to-biodiversity

旧图复用：V22生态图局部可复用但需新增机制。实际匹配：无。

## 生物 第11章 · 11.2 生态保育

ID：B05-BIO11-11-2；优先级：P1；状态：not_produced。

用途：比较就地与迁地保护的作用；依据目标设计保育监测和权衡。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：就地生境；种子库；恢复地；廊道；监测指标。

关系：就地与迁地互补而非等价；廊道有收益与风险；投入与成效分开。

文字：遗传、物种、生态系统、前后与参照、长期监测。

公式与单位：多样性至少分遗传、物种、生态系统三个层次，指标之间不可互相完全替代。；简化前后—参照比较：措施区变化−参照区变化，可帮助扣除共同趋势，但依赖参照可比等假设。；保育决策链：明确对象与威胁 → 选措施 → 定可测指标与时间 → 监测 → 调整。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第11章《生态保育与可持续发展》真实小节11.2《生态保育》制作《保育措施与评价矩阵》教学图。学习目的：比较就地与迁地保护的作用；依据目标设计保育监测和权衡。本图是有条件的科学模型，非实测图或官方考题。必须出现：就地生境；种子库；恢复地；廊道；监测指标。必须保持关系：就地与迁地互补而非等价；廊道有收益与风险；投入与成效分开。中文标签逐字采用：遗传、物种、生态系统、前后与参照、长期监测。公式及条件：多样性至少分遗传、物种、生态系统三个层次，指标之间不可互相完全替代。；简化前后—参照比较：措施区变化−参照区变化，可帮助扣除共同趋势，但依赖参照可比等假设。；保育决策链：明确对象与威胁 → 选措施 → 定可测指标与时间 → 监测 → 调整。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 11, authentic subsection 11.2. Display the original Chinese title exactly: 保育措施与评价矩阵. Topic-specific scientific requirements and instructional purpose: Compare in-situ habitat protection, ex-situ seed banking and restoration. Link each measure to a specific threat and measurable outcome, with benefits and limitations; do not present corridors as universally risk-free. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 就地生境；种子库；恢复地；廊道；监测指标. Preserve the following Chinese label strings exactly: 遗传、物种、生态系统、前后与参照、长期监测. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 多样性至少分遗传、物种、生态系统三个层次，指标之间不可互相完全替代。；简化前后—参照比较：措施区变化−参照区变化，可帮助扣除共同趋势，但依赖参照可比等假设。；保育决策链：明确对象与威胁 → 选措施 → 定可测指标与时间 → 监测 → 调整。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：就地与迁地互补而非等价；廊道有收益与风险；投入与成效分开。不得把生态保育画成另一知识主题；不得改动遗传、物种、生态系统、前后与参照、长期监测的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 就地与迁地互补而非等价
- 廊道有收益与风险
- 投入与成效分开
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/47-4-preserving-biodiversity

旧图复用：未有完整对应图。实际匹配：无。

## 生物 第11章 · 11.3 低碳生活与可持续发展

ID：B05-BIO11-11-3；优先级：P1；状态：not_produced。

用途：按系统边界比较减排方案；区分碳流、能流与可持续性指标。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：原料制造；运输；能源生产；使用；处置回收；碳汇。

关系：各环节排放累加；相同服务与年限比较；碳汇标时间和不确定性。

文字：kg CO₂e、功能单位、直接/间接、活动量×因子、非通用因子。

公式与单位：估计排放E=活动量A×排放因子f；多来源时E总=ΣAᵢfᵢ，单位必须相消。；减排率=(基线排放−方案排放)/基线排放；相同服务量与同一系统边界是可比前提。；碳收支与能量收支分别追踪：碳可在库间循环，能量转换后向环境分散，不能画成完全闭合能量循环。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第11章《生态保育与可持续发展》真实小节11.3《低碳生活与可持续发展》制作《低碳方案的系统边界》教学图。学习目的：按系统边界比较减排方案；区分碳流、能流与可持续性指标。本图是有条件的科学模型，非实测图或官方考题。必须出现：原料制造；运输；能源生产；使用；处置回收；碳汇。必须保持关系：各环节排放累加；相同服务与年限比较；碳汇标时间和不确定性。中文标签逐字采用：kg CO₂e、功能单位、直接/间接、活动量×因子、非通用因子。公式及条件：估计排放E=活动量A×排放因子f；多来源时E总=ΣAᵢfᵢ，单位必须相消。；减排率=(基线排放−方案排放)/基线排放；相同服务量与同一系统边界是可比前提。；碳收支与能量收支分别追踪：碳可在库间循环，能量转换后向环境分散，不能画成完全闭合能量循环。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 11, authentic subsection 11.3. Display the original Chinese title exactly: 低碳方案的系统边界. Topic-specific scientific requirements and instructional purpose: Draw a lifecycle boundary including raw materials, manufacture, energy supply, transport, use and end of life. Compare equal services over equal lifetimes using explicitly hypothetical emission factors. Mark carbon-sink storage time and uncertainty. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 原料制造；运输；能源生产；使用；处置回收；碳汇. Preserve the following Chinese label strings exactly: kg CO₂e、功能单位、直接/间接、活动量×因子、非通用因子. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 估计排放E=活动量A×排放因子f；多来源时E总=ΣAᵢfᵢ，单位必须相消。；减排率=(基线排放−方案排放)/基线排放；相同服务量与同一系统边界是可比前提。；碳收支与能量收支分别追踪：碳可在库间循环，能量转换后向环境分散，不能画成完全闭合能量循环。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：各环节排放累加；相同服务与年限比较；碳汇标时间和不确定性。不得把低碳生活与可持续发展画成另一知识主题；不得改动kg CO₂e、功能单位、直接/间接、活动量×因子、非通用因子的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 各环节排放累加
- 相同服务与年限比较
- 碳汇标时间和不确定性
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/46-3-biogeochemical-cycles

旧图复用：V22碳循环可作原理背景，非足够全生命周期图。实际匹配：无。

## 生物 第13章 · 13.1 有丝分裂

ID：B05-BIO13-13-1；优先级：P0；状态：reuse_partial_remaining_pending。

用途：按着丝粒与DNA分子分别计数；解释阶段变化和检查点作用。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：2n=4复制前后；中期；后期全细胞/每极；分裂沟；细胞板。

关系：复制后DNA加倍但染色体数不变；后期DNA总量守恒；植物不画分裂沟。

文字：2n、2C、4C、着丝粒、姐妹、细胞板。

公式与单位：未复制二倍体为2n条、2C；S期后为2n条、4C，每条有两条姐妹。；后期全细胞为4n条子染色体、DNA总量仍4C；每极得到2n条、2C。n与C分别描述套数和DNA量，不可互换。；分裂指数=分裂期细胞数/总观察细胞数。只有随机取样、近似稳态等条件下，阶段比例才可辅助估计相对停留时间。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第13章《细胞分裂》真实小节13.1《有丝分裂》制作《有丝分裂计数与胞质分裂》教学图。学习目的：按着丝粒与DNA分子分别计数；解释阶段变化和检查点作用。本图是有条件的科学模型，非实测图或官方考题。必须出现：2n=4复制前后；中期；后期全细胞/每极；分裂沟；细胞板。必须保持关系：复制后DNA加倍但染色体数不变；后期DNA总量守恒；植物不画分裂沟。中文标签逐字采用：2n、2C、4C、着丝粒、姐妹、细胞板。公式及条件：未复制二倍体为2n条、2C；S期后为2n条、4C，每条有两条姐妹。；后期全细胞为4n条子染色体、DNA总量仍4C；每极得到2n条、2C。n与C分别描述套数和DNA量，不可互换。；分裂指数=分裂期细胞数/总观察细胞数。只有随机取样、近似稳态等条件下，阶段比例才可辅助估计相对停留时间。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 13, authentic subsection 13.1. Display the original Chinese title exactly: 有丝分裂计数与胞质分裂. Topic-specific scientific requirements and instructional purpose: Track chromosome and DNA counts in a 2n=4 mitosis model. Separate whole-cell anaphase from each pole and compare animal cleavage furrow with plant cell plate. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 2n=4复制前后；中期；后期全细胞/每极；分裂沟；细胞板. Preserve the following Chinese label strings exactly: 2n、2C、4C、着丝粒、姐妹、细胞板. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 未复制二倍体为2n条、2C；S期后为2n条、4C，每条有两条姐妹。；后期全细胞为4n条子染色体、DNA总量仍4C；每极得到2n条、2C。n与C分别描述套数和DNA量，不可互换。；分裂指数=分裂期细胞数/总观察细胞数。只有随机取样、近似稳态等条件下，阶段比例才可辅助估计相对停留时间。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：复制后DNA加倍但染色体数不变；后期DNA总量守恒；植物不画分裂沟。不得把有丝分裂画成另一知识主题；不得改动2n、2C、4C、着丝粒、姐妹、细胞板的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 复制后DNA加倍但染色体数不变
- 后期DNA总量守恒
- 植物不画分裂沟
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/10-2-the-cell-cycle

旧图复用：V22 B42计数图可复用，胞质分裂需另图。实际匹配：assets/v22/biology/B42_mitosis_chromosome_count_2n4.svg。

## 生物 第13章 · 13.2 减数分裂

ID：B05-BIO13-13-2；优先级：P0；状态：reuse_partial_remaining_pending。

用途：辨认两次分裂的分离对象；用染色体行为解释遗传变异。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：两对同源染色体；联会与非姐妹交换；减Ⅰ；减Ⅱ；四个产物。

关系：只在分裂前复制一次；减Ⅰ同源分离；减Ⅱ姐妹分离。

文字：2n=4、4C、n=2、2C、1C。

公式与单位：正常二倍体：2n、2C → DNA复制 → 2n、4C → 减Ⅰ → n、2C → 减Ⅱ → n、1C。；无交换的来源组合数为2ⁿ，n是同源染色体对数；这是多次减数分裂可能产生的来源组合。；若n=2，第一次分裂某对不分离，最终四个产物对该染色体的拷贝数为2、2、0、0，而正常应各为1。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第13章《细胞分裂》真实小节13.2《减数分裂》制作《减数分裂的分离对象与DNA量》教学图。学习目的：辨认两次分裂的分离对象；用染色体行为解释遗传变异。本图是有条件的科学模型，非实测图或官方考题。必须出现：两对同源染色体；联会与非姐妹交换；减Ⅰ；减Ⅱ；四个产物。必须保持关系：只在分裂前复制一次；减Ⅰ同源分离；减Ⅱ姐妹分离。中文标签逐字采用：2n=4、4C、n=2、2C、1C。公式及条件：正常二倍体：2n、2C → DNA复制 → 2n、4C → 减Ⅰ → n、2C → 减Ⅱ → n、1C。；无交换的来源组合数为2ⁿ，n是同源染色体对数；这是多次减数分裂可能产生的来源组合。；若n=2，第一次分裂某对不分离，最终四个产物对该染色体的拷贝数为2、2、0、0，而正常应各为1。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 13, authentic subsection 13.2. Display the original Chinese title exactly: 减数分裂的分离对象与DNA量. Topic-specific scientific requirements and instructional purpose: Show one DNA replication followed by homolog separation in meiosis I and sister separation in meiosis II. Use two homolog pairs and label DNA content per cell. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 两对同源染色体；联会与非姐妹交换；减Ⅰ；减Ⅱ；四个产物. Preserve the following Chinese label strings exactly: 2n=4、4C、n=2、2C、1C. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 正常二倍体：2n、2C → DNA复制 → 2n、4C → 减Ⅰ → n、2C → 减Ⅱ → n、1C。；无交换的来源组合数为2ⁿ，n是同源染色体对数；这是多次减数分裂可能产生的来源组合。；若n=2，第一次分裂某对不分离，最终四个产物对该染色体的拷贝数为2、2、0、0，而正常应各为1。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：只在分裂前复制一次；减Ⅰ同源分离；减Ⅱ姐妹分离。不得把减数分裂画成另一知识主题；不得改动2n=4、4C、n=2、2C、1C的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 只在分裂前复制一次
- 减Ⅰ同源分离
- 减Ⅱ姐妹分离
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/11-1-the-process-of-meiosis

旧图复用：可复核复用V22 B46、B56。实际匹配：assets/v22/biology/B46_meiosis_chromosome_number_example_2n4.svg, assets/v22/biology/B56_meiosis_crossing_over_nonsister_chromatids.svg。

## 生物 第13章 · 13.3 癌症的发生

ID：B05-BIO13-13-3；优先级：P1；状态：not_produced。

用途：解释周期调控失常与肿瘤发展的关系；区分风险因素、相关性与诊断证据。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：正常生长信号；检查点；损伤修复；异常克隆；局部侵袭；转移。

关系：损伤不必然癌变；多环节失调增加异常扩增可能；转移为同一个体内过程。

文字：正常调控、修复/停滞/死亡、异常扩增、证据不足不能诊断。

公式与单位：调控模型：促进生长的信号受调节 + 抑制与修复机制 → 协调细胞数量；多环节失调可能促成异常克隆扩增。；净细胞数量变化=新产生细胞数−死亡或离开系统的细胞数；分裂比例不是净增长率。；相对风险比较需要明确观察人数、事件数及可比条件，观察性相关不能单独证明某一分子机制。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第13章《细胞分裂》真实小节13.3《癌症的发生》制作《周期调控失常与证据边界》教学图。学习目的：解释周期调控失常与肿瘤发展的关系；区分风险因素、相关性与诊断证据。本图是有条件的科学模型，非实测图或官方考题。必须出现：正常生长信号；检查点；损伤修复；异常克隆；局部侵袭；转移。必须保持关系：损伤不必然癌变；多环节失调增加异常扩增可能；转移为同一个体内过程。中文标签逐字采用：正常调控、修复/停滞/死亡、异常扩增、证据不足不能诊断。公式及条件：调控模型：促进生长的信号受调节 + 抑制与修复机制 → 协调细胞数量；多环节失调可能促成异常克隆扩增。；净细胞数量变化=新产生细胞数−死亡或离开系统的细胞数；分裂比例不是净增长率。；相对风险比较需要明确观察人数、事件数及可比条件，观察性相关不能单独证明某一分子机制。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 13, authentic subsection 13.3. Display the original Chinese title exactly: 周期调控失常与证据边界. Topic-specific scientific requirements and instructional purpose: Compare regulated growth with a multistep loss of control. Show repair, arrest and cell death as alternative responses to DNA damage; distinguish local invasion from metastasis within one individual. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 正常生长信号；检查点；损伤修复；异常克隆；局部侵袭；转移. Preserve the following Chinese label strings exactly: 正常调控、修复/停滞/死亡、异常扩增、证据不足不能诊断. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 调控模型：促进生长的信号受调节 + 抑制与修复机制 → 协调细胞数量；多环节失调可能促成异常克隆扩增。；净细胞数量变化=新产生细胞数−死亡或离开系统的细胞数；分裂比例不是净增长率。；相对风险比较需要明确观察人数、事件数及可比条件，观察性相关不能单独证明某一分子机制。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：损伤不必然癌变；多环节失调增加异常扩增可能；转移为同一个体内过程。不得把癌症的发生画成另一知识主题；不得改动正常调控、修复/停滞/死亡、异常扩增、证据不足不能诊断的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 损伤不必然癌变
- 多环节失调增加异常扩增可能
- 转移为同一个体内过程
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/10-4-cancer-and-the-cell-cycle

旧图复用：无完全匹配旧图。实际匹配：无。

## 生物 第18章 · 18.1 细菌的结构与特征

ID：B05-BIO18-18-1；优先级：P0；状态：not_produced。

用途：由结构推断细菌的生命活动；区分原核结构与真核细胞器。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：细胞膜；肽聚糖壁；拟核；核糖体；可选质粒荚膜鞭毛。

关系：DNA无核膜包围；核糖体无膜；可选结构须标部分细菌具有。

文字：拟核、核糖体、细胞膜、细胞壁、部分细菌具有。

公式与单位：球形模型表面积A=4πr²、体积V=4πr³/3，所以A/V=3/r；半径减半，表面积体积比加倍。；细菌能量代谢的论证应从膜、酶和反应途径出发，不能由“无粒线体”推出“无ATP”。；结构识别须区分必备的细胞膜、核糖体等与部分细菌才有的质粒、荚膜和鞭毛。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第18章《细菌与病毒》真实小节18.1《细菌的结构与特征》制作《典型细菌结构及适用边界》教学图。学习目的：由结构推断细菌的生命活动；区分原核结构与真核细胞器。本图是有条件的科学模型，非实测图或官方考题。必须出现：细胞膜；肽聚糖壁；拟核；核糖体；可选质粒荚膜鞭毛。必须保持关系：DNA无核膜包围；核糖体无膜；可选结构须标部分细菌具有。中文标签逐字采用：拟核、核糖体、细胞膜、细胞壁、部分细菌具有。公式及条件：球形模型表面积A=4πr²、体积V=4πr³/3，所以A/V=3/r；半径减半，表面积体积比加倍。；细菌能量代谢的论证应从膜、酶和反应途径出发，不能由“无粒线体”推出“无ATP”。；结构识别须区分必备的细胞膜、核糖体等与部分细菌才有的质粒、荚膜和鞭毛。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 18, authentic subsection 18.1. Display the original Chinese title exactly: 典型细菌结构及适用边界. Topic-specific scientific requirements and instructional purpose: Draw a typical bacterium without a nucleus or mitochondria. Label nucleoid, ribosomes, membrane and peptidoglycan wall. Clearly mark capsule, plasmid and flagellum as optional structures. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 细胞膜；肽聚糖壁；拟核；核糖体；可选质粒荚膜鞭毛. Preserve the following Chinese label strings exactly: 拟核、核糖体、细胞膜、细胞壁、部分细菌具有. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 球形模型表面积A=4πr²、体积V=4πr³/3，所以A/V=3/r；半径减半，表面积体积比加倍。；细菌能量代谢的论证应从膜、酶和反应途径出发，不能由“无粒线体”推出“无ATP”。；结构识别须区分必备的细胞膜、核糖体等与部分细菌才有的质粒、荚膜和鞭毛。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：DNA无核膜包围；核糖体无膜；可选结构须标部分细菌具有。不得把细菌的结构与特征画成另一知识主题；不得改动拟核、核糖体、细胞膜、细胞壁、部分细菌具有的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- DNA无核膜包围
- 核糖体无膜
- 可选结构须标部分细菌具有
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/22-2-structure-of-prokaryotes-bacteria-and-archaea

旧图复用：V22现有图需逐结构对照后决定。实际匹配：无。

## 生物 第18章 · 18.2 细菌的生长条件

ID：B05-BIO18-18-2；优先级：P0；状态：not_produced。

用途：用条件解释生长曲线与实验结果；按可比设计评价抑菌实验。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：时间轴；活菌数对数轴；四时期；浊度与CFU对照。

关系：对数期直线对应原数量指数增加；稳定期净增长近零；死细胞可仍贡献浊度。

文字：调整期、对数期、稳定期、衰亡期、log活菌数。

公式与单位：理想倍增：N=N₀×2ᵏ，k=t/g，g为稳定条件下代时；只适用于相应指数阶段。；平板计数估算原液浓度=菌落数/(接种体积×稀释倍数)，单位CFU/mL；依赖可培养、分散和计数范围等条件。；净数量变化=繁殖产生−死亡；不同测量方式可能给不同曲线。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第18章《细菌与病毒》真实小节18.2《细菌的生长条件》制作《细菌生长曲线与测量边界》教学图。学习目的：用条件解释生长曲线与实验结果；按可比设计评价抑菌实验。本图是有条件的科学模型，非实测图或官方考题。必须出现：时间轴；活菌数对数轴；四时期；浊度与CFU对照。必须保持关系：对数期直线对应原数量指数增加；稳定期净增长近零；死细胞可仍贡献浊度。中文标签逐字采用：调整期、对数期、稳定期、衰亡期、log活菌数。公式及条件：理想倍增：N=N₀×2ᵏ，k=t/g，g为稳定条件下代时；只适用于相应指数阶段。；平板计数估算原液浓度=菌落数/(接种体积×稀释倍数)，单位CFU/mL；依赖可培养、分散和计数范围等条件。；净数量变化=繁殖产生−死亡；不同测量方式可能给不同曲线。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 18, authentic subsection 18.2. Display the original Chinese title exactly: 细菌生长曲线与测量边界. Topic-specific scientific requirements and instructional purpose: Plot viable bacterial count on a logarithmic vertical axis against time, showing lag, exponential, stationary and death phases. Explain that turbidity and CFU measure different things. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 时间轴；活菌数对数轴；四时期；浊度与CFU对照. Preserve the following Chinese label strings exactly: 调整期、对数期、稳定期、衰亡期、log活菌数. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 理想倍增：N=N₀×2ᵏ，k=t/g，g为稳定条件下代时；只适用于相应指数阶段。；平板计数估算原液浓度=菌落数/(接种体积×稀释倍数)，单位CFU/mL；依赖可培养、分散和计数范围等条件。；净数量变化=繁殖产生−死亡；不同测量方式可能给不同曲线。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：对数期直线对应原数量指数增加；稳定期净增长近零；死细胞可仍贡献浊度。不得把细菌的生长条件画成另一知识主题；不得改动调整期、对数期、稳定期、衰亡期、log活菌数的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 对数期直线对应原数量指数增加
- 稳定期净增长近零
- 死细胞可仍贡献浊度
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/22-3-prokaryotic-metabolism
- https://openstax.org/books/microbiology/pages/9-1-how-microbes-grow

旧图复用：无完全匹配旧图。实际匹配：无。

## 生物 第18章 · 18.3 病毒的结构与特征

ID：B05-BIO18-18-3；优先级：P0；状态：not_produced。

用途：由核酸与衣壳描述病毒；解释病毒为何依赖宿主而非自行分裂。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：无包膜病毒；有包膜病毒；细菌；基因组；衣壳；核糖体。

关系：病毒图不画核糖体或完整胞质；包膜标部分具有；外形不统一。

文字：DNA或RNA基因组、衣壳、部分病毒有包膜、非按比例。

公式与单位：结构最低模型：病毒基因组 + 衣壳；部分另有包膜及表面蛋白。；基因组类型须具体到所讨论病毒，不能把DNA病毒和RNA病毒的路线合并成一张无条件流程图。；病毒增殖不是细胞二分裂：宿主内合成组分 → 组装 → 释放，依赖条件须逐项说明。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第18章《细菌与病毒》真实小节18.3《病毒的结构与特征》制作《病毒、细菌与细胞结构对比》教学图。学习目的：由核酸与衣壳描述病毒；解释病毒为何依赖宿主而非自行分裂。本图是有条件的科学模型，非实测图或官方考题。必须出现：无包膜病毒；有包膜病毒；细菌；基因组；衣壳；核糖体。必须保持关系：病毒图不画核糖体或完整胞质；包膜标部分具有；外形不统一。中文标签逐字采用：DNA或RNA基因组、衣壳、部分病毒有包膜、非按比例。公式及条件：结构最低模型：病毒基因组 + 衣壳；部分另有包膜及表面蛋白。；基因组类型须具体到所讨论病毒，不能把DNA病毒和RNA病毒的路线合并成一张无条件流程图。；病毒增殖不是细胞二分裂：宿主内合成组分 → 组装 → 释放，依赖条件须逐项说明。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 18, authentic subsection 18.3. Display the original Chinese title exactly: 病毒、细菌与细胞结构对比. Topic-specific scientific requirements and instructional purpose: Compare an explicitly identified non-enveloped virus, enveloped virus and bacterium. Do not give virions ribosomes, cytoplasm or peptidoglycan. Mark figures as not to scale and distinguish genome from replication intermediates. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 无包膜病毒；有包膜病毒；细菌；基因组；衣壳；核糖体. Preserve the following Chinese label strings exactly: DNA或RNA基因组、衣壳、部分病毒有包膜、非按比例. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 结构最低模型：病毒基因组 + 衣壳；部分另有包膜及表面蛋白。；基因组类型须具体到所讨论病毒，不能把DNA病毒和RNA病毒的路线合并成一张无条件流程图。；病毒增殖不是细胞二分裂：宿主内合成组分 → 组装 → 释放，依赖条件须逐项说明。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：病毒图不画核糖体或完整胞质；包膜标部分具有；外形不统一。不得把病毒的结构与特征画成另一知识主题；不得改动DNA或RNA基因组、衣壳、部分病毒有包膜、非按比例的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 病毒图不画核糖体或完整胞质
- 包膜标部分具有
- 外形不统一
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/21-1-viral-evolution-morphology-and-classification

旧图复用：须核现有病毒图类型后复用。实际匹配：无。

## 生物 第18章 · 18.4 病毒的增殖与传播

ID：B05-BIO18-18-4；优先级：P0；状态：not_produced。

用途：按条件说明病毒生命周期；区分个体内增殖与个体间传播。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：噬菌体裂解/溶原分支；宿主细胞边界；动物病毒出芽；宿主间传播单独框。

关系：不得把所有病毒画成注入式噬菌体；复制与传播分开；逆转录方向RNA到DNA。

文字：吸附、合成、组装、释放、前噬菌体、非所有病毒相同。

公式与单位：裂解模型：吸附 → 遗传物质进入 → 组分合成 → 组装 → 释放；进入细胞的成分须依病毒类型画清。；若理想每个感染细胞释放b个可感染颗粒，连续k轮的数量上限模型可写N₀bᵏ；前提是宿主充足、颗粒全部成功感染等，不可当作真实传播预测。；个体内病毒复制、感染性颗粒数、个体间新病例是不同变量，不能无条件互换。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第18章《细菌与病毒》真实小节18.4《病毒的增殖与传播》制作《病毒增殖类型与传播层次》教学图。学习目的：按条件说明病毒生命周期；区分个体内增殖与个体间传播。本图是有条件的科学模型，非实测图或官方考题。必须出现：噬菌体裂解/溶原分支；宿主细胞边界；动物病毒出芽；宿主间传播单独框。必须保持关系：不得把所有病毒画成注入式噬菌体；复制与传播分开；逆转录方向RNA到DNA。中文标签逐字采用：吸附、合成、组装、释放、前噬菌体、非所有病毒相同。公式及条件：裂解模型：吸附 → 遗传物质进入 → 组分合成 → 组装 → 释放；进入细胞的成分须依病毒类型画清。；若理想每个感染细胞释放b个可感染颗粒，连续k轮的数量上限模型可写N₀bᵏ；前提是宿主充足、颗粒全部成功感染等，不可当作真实传播预测。；个体内病毒复制、感染性颗粒数、个体间新病例是不同变量，不能无条件互换。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 18, authentic subsection 18.4. Display the original Chinese title exactly: 病毒增殖类型与传播层次. Topic-specific scientific requirements and instructional purpose: Draw explicitly separated examples of phage lytic and lysogenic cycles and enveloped animal-virus budding. Distinguish intracellular replication from between-host transmission; label reverse transcription RNA to DNA only in the appropriate example. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 噬菌体裂解/溶原分支；宿主细胞边界；动物病毒出芽；宿主间传播单独框. Preserve the following Chinese label strings exactly: 吸附、合成、组装、释放、前噬菌体、非所有病毒相同. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 裂解模型：吸附 → 遗传物质进入 → 组分合成 → 组装 → 释放；进入细胞的成分须依病毒类型画清。；若理想每个感染细胞释放b个可感染颗粒，连续k轮的数量上限模型可写N₀bᵏ；前提是宿主充足、颗粒全部成功感染等，不可当作真实传播预测。；个体内病毒复制、感染性颗粒数、个体间新病例是不同变量，不能无条件互换。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：不得把所有病毒画成注入式噬菌体；复制与传播分开；逆转录方向RNA到DNA。不得把病毒的增殖与传播画成另一知识主题；不得改动吸附、合成、组装、释放、前噬菌体、非所有病毒相同的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 不得把所有病毒画成注入式噬菌体
- 复制与传播分开
- 逆转录方向RNA到DNA
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/21-2-virus-infections-and-hosts

旧图复用：现有生命周期图须按类型复核。实际匹配：无。

## 生物 第19章 · 19.1 原始生命的演化

ID：B05-BIO19-19-1；优先级：P1；状态：not_produced。

用途：区分生命起源假说与可观察证据；解释细胞复杂性演化的主要条件。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：非生物合成实验；有机小分子；膜样隔离；RNA信息/催化；内共生独立证据框。

关系：不能从产物直接画成确定生命路线；假说用虚线和条件；内共生对象限定且多证据。

文字：模型条件、实验支持、尚待研究、不是完整生命、内共生。

公式与单位：证据层次：实验特定条件下生成有机物 ≠ 已制造完整生命 ≠ 已证明地球唯一历史路线。；隔离、遗传复制、催化与能量利用须相互协调，不能由一个膜泡推全套生命活动。；内共生理论用多类结构、遗传与演化证据综合评价；现代相似性不等于原始事件可以直接重看。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第19章《演化》真实小节19.1《原始生命的演化》制作《生命起源的证据层次》教学图。学习目的：区分生命起源假说与可观察证据；解释细胞复杂性演化的主要条件。本图是有条件的科学模型，非实测图或官方考题。必须出现：非生物合成实验；有机小分子；膜样隔离；RNA信息/催化；内共生独立证据框。必须保持关系：不能从产物直接画成确定生命路线；假说用虚线和条件；内共生对象限定且多证据。中文标签逐字采用：模型条件、实验支持、尚待研究、不是完整生命、内共生。公式及条件：证据层次：实验特定条件下生成有机物 ≠ 已制造完整生命 ≠ 已证明地球唯一历史路线。；隔离、遗传复制、催化与能量利用须相互协调，不能由一个膜泡推全套生命活动。；内共生理论用多类结构、遗传与演化证据综合评价；现代相似性不等于原始事件可以直接重看。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 19, authentic subsection 19.1. Display the original Chinese title exactly: 生命起源的证据层次. Topic-specific scientific requirements and instructional purpose: Separate experimentally supported abiotic synthesis from hypothesized steps toward replication, compartmentalization and metabolism. Use conditional dashed links rather than a proven linear origin sequence. Show multiple lines of endosymbiotic evidence without reusing quarantined inaccurate mitochondrial artwork. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 非生物合成实验；有机小分子；膜样隔离；RNA信息/催化；内共生独立证据框. Preserve the following Chinese label strings exactly: 模型条件、实验支持、尚待研究、不是完整生命、内共生. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 证据层次：实验特定条件下生成有机物 ≠ 已制造完整生命 ≠ 已证明地球唯一历史路线。；隔离、遗传复制、催化与能量利用须相互协调，不能由一个膜泡推全套生命活动。；内共生理论用多类结构、遗传与演化证据综合评价；现代相似性不等于原始事件可以直接重看。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：不能从产物直接画成确定生命路线；假说用虚线和条件；内共生对象限定且多证据。不得把原始生命的演化画成另一知识主题；不得改动模型条件、实验支持、尚待研究、不是完整生命、内共生的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 不能从产物直接画成确定生命路线
- 假说用虚线和条件
- 内共生对象限定且多证据
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/23-1-eukaryotic-origins
- https://openstax.org/books/biology-2e/pages/22-1-prokaryotic-diversity

旧图复用：不得复用已隔离粒线体错误图；应另行准确结构任务。实际匹配：无。

## 生物 第19章 · 19.2 生物演化的证据

ID：B05-BIO19-19-2；优先级：P0；状态：not_produced。

用途：综合化石解剖与分子证据解释亲缘；区分同源同功及树图的推断边界。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：脊椎前肢对应骨；鸟昆虫翅功能对照；A/B/C分叉树；节点旋转同拓扑。

关系：同源可异功能；同功不自动同源；旋转不改亲缘；节点不是进步阶梯。

文字：共同祖先、对应骨骼、最近共同祖先、同一拓扑、未按时间比例。

公式与单位：证据推断链：观察特征/序列 → 判是否可比较及同源 → 建共同祖先关系 → 用独立资料核查。；亲缘远近看最近共同祖先，不看树图左右距离或末端摆放高低。；序列相似率=对应位点相同数/可比位点数；需对齐及模型条件，不等于单独证明全部历史。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第19章《演化》真实小节19.2《生物演化的证据》制作《同源证据与系统树读法》教学图。学习目的：综合化石解剖与分子证据解释亲缘；区分同源同功及树图的推断边界。本图是有条件的科学模型，非实测图或官方考题。必须出现：脊椎前肢对应骨；鸟昆虫翅功能对照；A/B/C分叉树；节点旋转同拓扑。必须保持关系：同源可异功能；同功不自动同源；旋转不改亲缘；节点不是进步阶梯。中文标签逐字采用：共同祖先、对应骨骼、最近共同祖先、同一拓扑、未按时间比例。公式及条件：证据推断链：观察特征/序列 → 判是否可比较及同源 → 建共同祖先关系 → 用独立资料核查。；亲缘远近看最近共同祖先，不看树图左右距离或末端摆放高低。；序列相似率=对应位点相同数/可比位点数；需对齐及模型条件，不等于单独证明全部历史。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 19, authentic subsection 19.2. Display the original Chinese title exactly: 同源证据与系统树读法. Topic-specific scientific requirements and instructional purpose: Align homologous vertebrate forelimb bones without requiring identical functions; contrast flight analogy in bird and insect wings. Draw an A/B sister-group tree with C branching earlier and a rotated equivalent tree, keeping topology unchanged and avoiding a progress ladder. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 脊椎前肢对应骨；鸟昆虫翅功能对照；A/B/C分叉树；节点旋转同拓扑. Preserve the following Chinese label strings exactly: 共同祖先、对应骨骼、最近共同祖先、同一拓扑、未按时间比例. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 证据推断链：观察特征/序列 → 判是否可比较及同源 → 建共同祖先关系 → 用独立资料核查。；亲缘远近看最近共同祖先，不看树图左右距离或末端摆放高低。；序列相似率=对应位点相同数/可比位点数；需对齐及模型条件，不等于单独证明全部历史。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：同源可异功能；同功不自动同源；旋转不改亲缘；节点不是进步阶梯。不得把生物演化的证据画成另一知识主题；不得改动共同祖先、对应骨骼、最近共同祖先、同一拓扑、未按时间比例的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 同源可异功能
- 同功不自动同源
- 旋转不改亲缘
- 节点不是进步阶梯
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/18-1-understanding-evolution

旧图复用：现有生物图须按骨连接与树拓扑复核再用。实际匹配：无。

## 生物 第19章 · 19.3 自然选择学说

ID：B05-BIO19-19-3；优先级：P0；状态：not_produced。

用途：用可遗传变异与繁殖差异解释适应；区分选择、定向意图和个体变化。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：初始不同类型；环境压力；差异繁殖；后代频率；非定向变异入口。

关系：选择不是把所有个体改造；可遗传性连到后代；每个体与总贡献区分。

文字：变异、可遗传、差异繁殖、频率变化、不由需要定向产生。

公式与单位：选择机制链：可遗传变异 → 环境下繁殖成功差异 → 后代遗传贡献不同 → 群体组成改变。；相对繁殖成功需同环境同时间尺度比较，不等于单纯存活人数。；比例变化本身不足识别机制；需排查迁移、漂变及测量偏差等。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第19章《演化》真实小节19.3《自然选择学说》制作《自然选择的完整机制链》教学图。学习目的：用可遗传变异与繁殖差异解释适应；区分选择、定向意图和个体变化。本图是有条件的科学模型，非实测图或官方考题。必须出现：初始不同类型；环境压力；差异繁殖；后代频率；非定向变异入口。必须保持关系：选择不是把所有个体改造；可遗传性连到后代；每个体与总贡献区分。中文标签逐字采用：变异、可遗传、差异繁殖、频率变化、不由需要定向产生。公式及条件：选择机制链：可遗传变异 → 环境下繁殖成功差异 → 后代遗传贡献不同 → 群体组成改变。；相对繁殖成功需同环境同时间尺度比较，不等于单纯存活人数。；比例变化本身不足识别机制；需排查迁移、漂变及测量偏差等。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 19, authentic subsection 19.3. Display the original Chinese title exactly: 自然选择的完整机制链. Topic-specific scientific requirements and instructional purpose: Show heritable variation before and during selection, differential reproductive contribution under an environment, and changed offspring frequencies. Do not depict every individual intentionally transforming into the favoured type. Distinguish per-individual success from total offspring numbers. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 初始不同类型；环境压力；差异繁殖；后代频率；非定向变异入口. Preserve the following Chinese label strings exactly: 变异、可遗传、差异繁殖、频率变化、不由需要定向产生. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 选择机制链：可遗传变异 → 环境下繁殖成功差异 → 后代遗传贡献不同 → 群体组成改变。；相对繁殖成功需同环境同时间尺度比较，不等于单纯存活人数。；比例变化本身不足识别机制；需排查迁移、漂变及测量偏差等。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：选择不是把所有个体改造；可遗传性连到后代；每个体与总贡献区分。不得把自然选择学说画成另一知识主题；不得改动变异、可遗传、差异繁殖、频率变化、不由需要定向产生的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 选择不是把所有个体改造
- 可遗传性连到后代
- 每个体与总贡献区分
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/19-3-adaptive-evolution

旧图复用：现有选择图需核是否误画个体主动变色。实际匹配：无。

## 生物 第19章 · 19.4 现代综合演化理论

ID：B05-BIO19-19-4；优先级：P0；状态：not_produced。

用途：计算种群等位基因频率及平衡期望；区分选择漂变基因流与变异来源。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：AA/Aa/aa个体；A/a拷贝计数；p+q；p²/2pq/q²配子结合表；选择/漂变/迁移分支。

关系：杂合各一拷贝；二倍体分母2N；q²到q需模型条件；漂变非定向优劣。

文字：p=.65、q=.35、2pq、期望非保证、模型条件。

公式与单位：二倍体常染色体两等位：p=(2N_AA+N_Aa)/(2N)，q=1−p。；随机结合模型：(p+q)²=p²+2pq+q²=1；三项分别为AA、Aa、aa期望频率。；若模型适用且隐性表型=aa，q=√f(隐性)；这依遗传方式、外显和群体条件。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中生物第19章《演化》真实小节19.4《现代综合演化理论》制作《等位基因计数与平衡模型》教学图。学习目的：计算种群等位基因频率及平衡期望；区分选择漂变基因流与变异来源。本图是有条件的科学模型，非实测图或官方考题。必须出现：AA/Aa/aa个体；A/a拷贝计数；p+q；p²/2pq/q²配子结合表；选择/漂变/迁移分支。必须保持关系：杂合各一拷贝；二倍体分母2N；q²到q需模型条件；漂变非定向优劣。中文标签逐字采用：p=.65、q=.35、2pq、期望非保证、模型条件。公式及条件：二倍体常染色体两等位：p=(2N_AA+N_Aa)/(2N)，q=1−p。；随机结合模型：(p+q)²=p²+2pq+q²=1；三项分别为AA、Aa、aa期望频率。；若模型适用且隐性表型=aa，q=√f(隐性)；这依遗传方式、外显和群体条件。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high biology teaching diagram for chapter 19, authentic subsection 19.4. Display the original Chinese title exactly: 等位基因计数与平衡模型. Topic-specific scientific requirements and instructional purpose: Count two allele copies per diploid individual, one A and one a in each heterozygote. Show p^2,2pq,q^2 as conditional Hardy-Weinberg expectations with explicit assumptions, and separate mutation, recombination, gene flow, drift and selection. Do not equate dominant phenotype frequency with p. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: AA/Aa/aa个体；A/a拷贝计数；p+q；p²/2pq/q²配子结合表；选择/漂变/迁移分支. Preserve the following Chinese label strings exactly: p=.65、q=.35、2pq、期望非保证、模型条件. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 二倍体常染色体两等位：p=(2N_AA+N_Aa)/(2N)，q=1−p。；随机结合模型：(p+q)²=p²+2pq+q²=1；三项分别为AA、Aa、aa期望频率。；若模型适用且隐性表型=aa，q=√f(隐性)；这依遗传方式、外显和群体条件。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：杂合各一拷贝；二倍体分母2N；q²到q需模型条件；漂变非定向优劣。不得把现代综合演化理论画成另一知识主题；不得改动p=.65、q=.35、2pq、期望非保证、模型条件的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 杂合各一拷贝
- 二倍体分母2N
- q²到q需模型条件
- 漂变非定向优劣
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77546/mod_resource/content/1/高中生物.pdf
- https://openstax.org/books/biology-2e/pages/19-1-population-evolution

旧图复用：V22 B55可复核后补充，勿把模型当所有群体事实。实际匹配：无。

## 化学 第1章 · 1.1 化学是一门实用的、创造性的科学

ID：B05-CHEM01-1-1；优先级：P2；状态：not_produced。

用途：以组成结构性质变化说明化学问题；用对照与收支评价材料设计的证据。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：宏观样品；微观结构模型；符号与方程；干湿质量；性能矩阵。

关系：三层证据互相支持；湿质量扣干料；单指标不等于全优。

文字：组成、结构、性质、条件、g水/g干料、对照。

公式与单位：化学解释链：宏观性质 ↔ 组成/微观结构 ↔ 符号模型及变化条件。；质量型吸水指标示例=(湿后质量−干质量)/干质量，单位可为g水/g干料，测法须明确。；评价方案需同功能、同条件对照，理论可行不等于已验证产品全部性能。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第1章《绪论》真实小节1.1《化学是一门实用的、创造性的科学》制作《化学的三层表达与材料评价》教学图。学习目的：以组成结构性质变化说明化学问题；用对照与收支评价材料设计的证据。本图是有条件的科学模型，非实测图或官方考题。必须出现：宏观样品；微观结构模型；符号与方程；干湿质量；性能矩阵。必须保持关系：三层证据互相支持；湿质量扣干料；单指标不等于全优。中文标签逐字采用：组成、结构、性质、条件、g水/g干料、对照。公式及条件：化学解释链：宏观性质 ↔ 组成/微观结构 ↔ 符号模型及变化条件。；质量型吸水指标示例=(湿后质量−干质量)/干质量，单位可为g水/g干料，测法须明确。；评价方案需同功能、同条件对照，理论可行不等于已验证产品全部性能。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 1, authentic subsection 1.1. Display the original Chinese title exactly: 化学的三层表达与材料评价. Topic-specific scientific requirements and instructional purpose: Connect macroscopic observations, microscopic composition/structure and symbolic models. Show wet mass as dry material plus absorbed water, with normalized uptake in grams water per gram dry material. Separate one measured benefit from broader performance trade-offs. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 宏观样品；微观结构模型；符号与方程；干湿质量；性能矩阵. Preserve the following Chinese label strings exactly: 组成、结构、性质、条件、g水/g干料、对照. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 化学解释链：宏观性质 ↔ 组成/微观结构 ↔ 符号模型及变化条件。；质量型吸水指标示例=(湿后质量−干质量)/干质量，单位可为g水/g干料，测法须明确。；评价方案需同功能、同条件对照，理论可行不等于已验证产品全部性能。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：三层证据互相支持；湿质量扣干料；单指标不等于全优。不得把化学是一门实用的、创造性的科学画成另一知识主题；不得改动组成、结构、性质、条件、g水/g干料、对照的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 三层证据互相支持
- 湿质量扣干料
- 单指标不等于全优
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/1-1-chemistry-in-context

旧图复用：适合简洁结构图；辅助插画不替代测量关系。实际匹配：无。

## 化学 第1章 · 1.2 化学发展成为一门中心科学

ID：B05-CHEM01-1-2；优先级：P2；状态：not_produced。

用途：用跨学科问题解释化学的桥梁作用；区分不同层次的测量与推断。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：结构反应中心；物理能量；生命过程；地球环境；材料工程；单位桥接。

关系：连接而非取代；浓度乘体积得量；每mol能乘mol得能；跨层需独立证据。

文字：结构—性质、化学形态、系统边界、mg/L×L、kJ/mol×mol。

公式与单位：跨层解释：微观结构/反应 → 材料或细胞过程 → 系统表现，各箭头需证据。；总量=浓度×体积等关系只有单位与对象相容时成立。；每摩尔能量×摩尔数=相应总能量，不能把J与mol当可直接相加的量。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第1章《绪论》真实小节1.2《化学发展成为一门中心科学》制作《化学与其他学科的证据接口》教学图。学习目的：用跨学科问题解释化学的桥梁作用；区分不同层次的测量与推断。本图是有条件的科学模型，非实测图或官方考题。必须出现：结构反应中心；物理能量；生命过程；地球环境；材料工程；单位桥接。必须保持关系：连接而非取代；浓度乘体积得量；每mol能乘mol得能；跨层需独立证据。中文标签逐字采用：结构—性质、化学形态、系统边界、mg/L×L、kJ/mol×mol。公式及条件：跨层解释：微观结构/反应 → 材料或细胞过程 → 系统表现，各箭头需证据。；总量=浓度×体积等关系只有单位与对象相容时成立。；每摩尔能量×摩尔数=相应总能量，不能把J与mol当可直接相加的量。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 1, authentic subsection 1.2. Display the original Chinese title exactly: 化学与其他学科的证据接口. Topic-specific scientific requirements and instructional purpose: Map chemistry as a bridge among physics, biological processes, environmental speciation and materials engineering. Show explicit unit bridges concentration times volume and energy-per-mole times amount. Do not depict one molecular observation as automatically proving whole-organism or ecosystem outcomes. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 结构反应中心；物理能量；生命过程；地球环境；材料工程；单位桥接. Preserve the following Chinese label strings exactly: 结构—性质、化学形态、系统边界、mg/L×L、kJ/mol×mol. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 跨层解释：微观结构/反应 → 材料或细胞过程 → 系统表现，各箭头需证据。；总量=浓度×体积等关系只有单位与对象相容时成立。；每摩尔能量×摩尔数=相应总能量，不能把J与mol当可直接相加的量。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：连接而非取代；浓度乘体积得量；每mol能乘mol得能；跨层需独立证据。不得把化学发展成为一门中心科学画成另一知识主题；不得改动结构—性质、化学形态、系统边界、mg/L×L、kJ/mol×mol的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 连接而非取代
- 浓度乘体积得量
- 每mol能乘mol得能
- 跨层需独立证据
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/1-1-chemistry-in-context

旧图复用：可用关系图，辅助插画不替代单位与证据链。实际匹配：无。

## 化学 第1章 · 1.3 化学与人类社会发展密切相关

ID：B05-CHEM01-1-3；优先级：P1；状态：not_produced。

用途：联系化学应用与物料资源限制；用多指标证据比较社会技术方案。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：水处理颗粒/溶解物；100mg分流20/80；复用与一次包装；设备节能与城市规模。

关系：稀释不销毁质量；去除转污泥仍需处置；按每次服务比较；局部效率不等全系统量。

文字：物料去向、功能单位、20+80=100、g/次、边界。

公式与单位：公平比较需同功能单位、同使用寿命和明确生产—使用—处置边界。；去除率=(输入量−输出量)/输入量；浓度降低不等于污染物质量已消失，稀释与转移需区分。；效率、危害、暴露和资源是不同指标，不能自动互代。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第1章《绪论》真实小节1.3《化学与人类社会发展密切相关》制作《化学应用的物料与功能单位》教学图。学习目的：联系化学应用与物料资源限制；用多指标证据比较社会技术方案。本图是有条件的科学模型，非实测图或官方考题。必须出现：水处理颗粒/溶解物；100mg分流20/80；复用与一次包装；设备节能与城市规模。必须保持关系：稀释不销毁质量；去除转污泥仍需处置；按每次服务比较；局部效率不等全系统量。中文标签逐字采用：物料去向、功能单位、20+80=100、g/次、边界。公式及条件：公平比较需同功能单位、同使用寿命和明确生产—使用—处置边界。；去除率=(输入量−输出量)/输入量；浓度降低不等于污染物质量已消失，稀释与转移需区分。；效率、危害、暴露和资源是不同指标，不能自动互代。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 1, authentic subsection 1.3. Display the original Chinese title exactly: 化学应用的物料与功能单位. Topic-specific scientific requirements and instructional purpose: Show water treatment as distinct removal/transfer/transformation steps, with100 mg partitioned into20 mg water and80 mg sludge. Compare reusable and single-use packaging per service rather than per item, and separate device efficiency from citywide demand. Do not depict dilution as destruction. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 水处理颗粒/溶解物；100mg分流20/80；复用与一次包装；设备节能与城市规模. Preserve the following Chinese label strings exactly: 物料去向、功能单位、20+80=100、g/次、边界. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 公平比较需同功能单位、同使用寿命和明确生产—使用—处置边界。；去除率=(输入量−输出量)/输入量；浓度降低不等于污染物质量已消失，稀释与转移需区分。；效率、危害、暴露和资源是不同指标，不能自动互代。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：稀释不销毁质量；去除转污泥仍需处置；按每次服务比较；局部效率不等全系统量。不得把化学与人类社会发展密切相关画成另一知识主题；不得改动物料去向、功能单位、20+80=100、g/次、边界的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 稀释不销毁质量
- 去除转污泥仍需处置
- 按每次服务比较
- 局部效率不等全系统量
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://www.acs.org/green-chemistry-sustainability/principles/12-principles-of-green-chemistry.html

旧图复用：无完全匹配旧图；收支结构图优于装饰插画。实际匹配：无。

## 化学 第1章 · 1.4.1 元素

ID：B05-CHEM01-1-4-1；优先级：P0；状态：not_produced。

用途：以质子数区分元素并分清原子离子同位素；正确读取元素符号及元素与单质的关系。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：Na/Na⁺核电子表；同位素Z/N表；Co与CO；O₂/O₃/H₂O；系数下标。

关系：Z不变仍同元素；同位素同Z不同N；Co与CO不可混；2乘全H₂O。

文字：Z、N、e⁻、A=Z+N、元素≠单质、假想丰度。

公式与单位：Z=质子数；质量数A=Z+中子数N；中性原子电子数Z，离子另按电荷。；同位素：同Z不同N；元素符号大小写要准确。；给定近似同位素质量mᵢ及数目分数fᵢ，平均质量=Σfᵢmᵢ，Σfᵢ=1。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第1章《绪论》真实小节1.4.1《元素》制作《元素粒子与符号层次》教学图。学习目的：以质子数区分元素并分清原子离子同位素；正确读取元素符号及元素与单质的关系。本图是有条件的科学模型，非实测图或官方考题。必须出现：Na/Na⁺核电子表；同位素Z/N表；Co与CO；O₂/O₃/H₂O；系数下标。必须保持关系：Z不变仍同元素；同位素同Z不同N；Co与CO不可混；2乘全H₂O。中文标签逐字采用：Z、N、e⁻、A=Z+N、元素≠单质、假想丰度。公式及条件：Z=质子数；质量数A=Z+中子数N；中性原子电子数Z，离子另按电荷。；同位素：同Z不同N；元素符号大小写要准确。；给定近似同位素质量mᵢ及数目分数fᵢ，平均质量=Σfᵢmᵢ，Σfᵢ=1。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 1, authentic subsection 1.4.1. Display the original Chinese title exactly: 元素粒子与符号层次. Topic-specific scientific requirements and instructional purpose: Separate element identity by proton number from ion charge and isotope neutron number. Contrast Co with CO, and O2/O3 with oxygen bound in H2O. Show that2H2O contains4 H and2 O atoms and label any isotope abundance example as hypothetical, not natural data. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: Na/Na⁺核电子表；同位素Z/N表；Co与CO；O₂/O₃/H₂O；系数下标. Preserve the following Chinese label strings exactly: Z、N、e⁻、A=Z+N、元素≠单质、假想丰度. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: Z=质子数；质量数A=Z+中子数N；中性原子电子数Z，离子另按电荷。；同位素：同Z不同N；元素符号大小写要准确。；给定近似同位素质量mᵢ及数目分数fᵢ，平均质量=Σfᵢmᵢ，Σfᵢ=1。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：Z不变仍同元素；同位素同Z不同N；Co与CO不可混；2乘全H₂O。不得把元素画成另一知识主题；不得改动Z、N、e⁻、A=Z+N、元素≠单质、假想丰度的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- Z不变仍同元素
- 同位素同Z不同N
- Co与CO不可混
- 2乘全H₂O
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/2-3-atomic-structure-and-symbolism

旧图复用：原子结构旧图可局部复用但需核电荷和数目。实际匹配：无。

## 化学 第1章 · 1.4.2 物质的分类

ID：B05-CHEM01-1-4-2；优先级：P0；状态：not_produced。

用途：按组成区分纯物质单质化合物和混合物；把均一性化学结合与分离证据分开。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：O₂纯样；H₂O纯样；H₂/O₂混合；NaCl晶格；盐水分散。

关系：H₂/O₂未反应不画水；O₂/O₃可一元素多组分；盐晶格不画独立NaCl分子。

文字：纯物质、单质、化合物、混合物、均一≠纯。

公式与单位：纯物质→单质或化合物；混合物可均相或非均相，均一不等于纯。；质量分数w=m组分/m混合物；需同质量单位。；化合物中的元素结合不等于游离单质混合，化学式与组成比例只能在相应物质身份下解释。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第1章《绪论》真实小节1.4.2《物质的分类》制作《物质分类与粒子模型》教学图。学习目的：按组成区分纯物质单质化合物和混合物；把均一性化学结合与分离证据分开。本图是有条件的科学模型，非实测图或官方考题。必须出现：O₂纯样；H₂O纯样；H₂/O₂混合；NaCl晶格；盐水分散。必须保持关系：H₂/O₂未反应不画水；O₂/O₃可一元素多组分；盐晶格不画独立NaCl分子。中文标签逐字采用：纯物质、单质、化合物、混合物、均一≠纯。公式及条件：纯物质→单质或化合物；混合物可均相或非均相，均一不等于纯。；质量分数w=m组分/m混合物；需同质量单位。；化合物中的元素结合不等于游离单质混合，化学式与组成比例只能在相应物质身份下解释。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 1, authentic subsection 1.4.2. Display the original Chinese title exactly: 物质分类与粒子模型. Topic-specific scientific requirements and instructional purpose: Build a classification tree with accurate particle examples: pure O2, pure H2O, unreacted H2/O2 mixture, extended NaCl ionic lattice and salt solution. Show that O2/O3 can be a mixture of one element and that visual homogeneity does not prove purity. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: O₂纯样；H₂O纯样；H₂/O₂混合；NaCl晶格；盐水分散. Preserve the following Chinese label strings exactly: 纯物质、单质、化合物、混合物、均一≠纯. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 纯物质→单质或化合物；混合物可均相或非均相，均一不等于纯。；质量分数w=m组分/m混合物；需同质量单位。；化合物中的元素结合不等于游离单质混合，化学式与组成比例只能在相应物质身份下解释。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：H₂/O₂未反应不画水；O₂/O₃可一元素多组分；盐晶格不画独立NaCl分子。不得把物质的分类画成另一知识主题；不得改动纯物质、单质、化合物、混合物、均一≠纯的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- H₂/O₂未反应不画水
- O₂/O₃可一元素多组分
- 盐晶格不画独立NaCl分子
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/1-2-phases-and-classification-of-matter

旧图复用：已有分类图可核粒子结构后复用。实际匹配：无。

## 化学 第1章 · 1.4.3 物质三态

ID：B05-CHEM01-1-4-3；优先级：P0；状态：not_produced。

用途：用粒子运动解释三态及相变；区分质量粒子数与体积压力的变化。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：等数同型粒子的固液气；六方向相变箭头；加热平台；封闭气压缩。

关系：同数同大小表示单位；气态间距增大非粒子变大；气→固凝华；平台仍传能。

文字：熔化、凝固、汽化、液化、升华、凝华、非按比例。

公式与单位：六种相变按起终态：熔化/凝固、汽化/液化、升华/凝华。；无化学变化且不漏物：m和相应粒子总数保持，V可改变。；固定n、T理想气PV为常量；相变平台仍可吸放热，不以ΔT=0推能量转移0。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第1章《绪论》真实小节1.4.3《物质三态》制作《三态粒子与相变守恒》教学图。学习目的：用粒子运动解释三态及相变；区分质量粒子数与体积压力的变化。本图是有条件的科学模型，非实测图或官方考题。必须出现：等数同型粒子的固液气；六方向相变箭头；加热平台；封闭气压缩。必须保持关系：同数同大小表示单位；气态间距增大非粒子变大；气→固凝华；平台仍传能。中文标签逐字采用：熔化、凝固、汽化、液化、升华、凝华、非按比例。公式及条件：六种相变按起终态：熔化/凝固、汽化/液化、升华/凝华。；无化学变化且不漏物：m和相应粒子总数保持，V可改变。；固定n、T理想气PV为常量；相变平台仍可吸放热，不以ΔT=0推能量转移0。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 1, authentic subsection 1.4.3. Display the original Chinese title exactly: 三态粒子与相变守恒. Topic-specific scientific requirements and instructional purpose: Draw equal numbers of identical particles across solid, liquid and gas panels, changing arrangement and spacing rather than particle size. Label all six phase transitions correctly, especially deposition gas-to-solid, and show that a heating plateau can still involve energy transfer. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 等数同型粒子的固液气；六方向相变箭头；加热平台；封闭气压缩. Preserve the following Chinese label strings exactly: 熔化、凝固、汽化、液化、升华、凝华、非按比例. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 六种相变按起终态：熔化/凝固、汽化/液化、升华/凝华。；无化学变化且不漏物：m和相应粒子总数保持，V可改变。；固定n、T理想气PV为常量；相变平台仍可吸放热，不以ΔT=0推能量转移0。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：同数同大小表示单位；气态间距增大非粒子变大；气→固凝华；平台仍传能。不得把物质三态画成另一知识主题；不得改动熔化、凝固、汽化、液化、升华、凝华、非按比例的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 同数同大小表示单位
- 气态间距增大非粒子变大
- 气→固凝华
- 平台仍传能
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/1-2-phases-and-classification-of-matter

旧图复用：旧三态图可核粒子数与箭头名称后复用。实际匹配：无。

## 化学 第1章 · 1.4.4 物理性质和化学性质

ID：B05-CHEM01-1-4-4；优先级：P1；状态：not_produced。

用途：区分性质描述与变化事件；以新物质和证据判断变化并追踪体系收支。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：物理/化学性质列表；沸腾与酸放气对照；玻璃碎裂；无色中和候选；100g到96+4收支。

关系：气泡不唯一判化学；能力与事件分开；开放体系计逸出；热不独占反应。

文字：新物质证据、物理变化、化学变化、100=96+4、观察≠唯一结论。

公式与单位：性质是可描述能力/特征；变化是发生的过程，不能只按词语相似分类。；生成新化学物质是化学变化核心；颜色/热/气泡等为线索，需条件与其他证据。；完整体系质量收支：初物质=最终留存+逸出/转移等（无核过程的课程条件）。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第1章《绪论》真实小节1.4.4《物理性质和化学性质》制作《性质变化与证据判断》教学图。学习目的：区分性质描述与变化事件；以新物质和证据判断变化并追踪体系收支。本图是有条件的科学模型，非实测图或官方考题。必须出现：物理/化学性质列表；沸腾与酸放气对照；玻璃碎裂；无色中和候选；100g到96+4收支。必须保持关系：气泡不唯一判化学；能力与事件分开；开放体系计逸出；热不独占反应。中文标签逐字采用：新物质证据、物理变化、化学变化、100=96+4、观察≠唯一结论。公式及条件：性质是可描述能力/特征；变化是发生的过程，不能只按词语相似分类。；生成新化学物质是化学变化核心；颜色/热/气泡等为线索，需条件与其他证据。；完整体系质量收支：初物质=最终留存+逸出/转移等（无核过程的课程条件）。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 1, authentic subsection 1.4.4. Display the original Chinese title exactly: 性质变化与证据判断. Topic-specific scientific requirements and instructional purpose: Contrast properties with events, and compare boiling-water bubbles with chemically generated gas. Include a broken-glass reversibility counterexample and an open-system mass balance100=96+4 g. Show that colour, heat or bubbles alone are not unique proof of a chemical reaction. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 物理/化学性质列表；沸腾与酸放气对照；玻璃碎裂；无色中和候选；100g到96+4收支. Preserve the following Chinese label strings exactly: 新物质证据、物理变化、化学变化、100=96+4、观察≠唯一结论. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 性质是可描述能力/特征；变化是发生的过程，不能只按词语相似分类。；生成新化学物质是化学变化核心；颜色/热/气泡等为线索，需条件与其他证据。；完整体系质量收支：初物质=最终留存+逸出/转移等（无核过程的课程条件）。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：气泡不唯一判化学；能力与事件分开；开放体系计逸出；热不独占反应。不得把物理性质和化学性质画成另一知识主题；不得改动新物质证据、物理变化、化学变化、100=96+4、观察≠唯一结论的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 气泡不唯一判化学
- 能力与事件分开
- 开放体系计逸出
- 热不独占反应
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/1-3-physical-and-chemical-properties

旧图复用：无完全对应旧图；对照图和收支准确即可。实际匹配：无。

## 化学 第2章 · 2.1.1 水的物理性质

ID：B05-CHEM02-2-1-1；优先级：P0；状态：not_produced。

用途：用极性和氢键解释水的物性；在温压和相态条件内计算热量密度。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：水分子间氢键；冰与液水相对结构；100g体积比较；单相加热段；相变条件框。

关系：普通汽化仍H₂O；冰密度较小体积较大；Q=mcΔT不含潜热；沸点注明压力。

文字：分子间氢键、O—H共价键、0.92 g/mL为题设、101.325kPa、约4°C密度最大。

公式与单位：ρ=m/V；相变无物质损失时m可不变而V因ρ改变。；Q=mcΔT仅用于无相变、比热近似恒定的温变段。；纯水约0°C熔点与100°C沸点对应约101.325 kPa参考；其他压力与溶质需另审。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第2章《水和氢》真实小节2.1.1《水的物理性质》制作《水的氢键物性与相变》教学图。学习目的：用极性和氢键解释水的物性；在温压和相态条件内计算热量密度。本图是有条件的科学模型，非实测图或官方考题。必须出现：水分子间氢键；冰与液水相对结构；100g体积比较；单相加热段；相变条件框。必须保持关系：普通汽化仍H₂O；冰密度较小体积较大；Q=mcΔT不含潜热；沸点注明压力。中文标签逐字采用：分子间氢键、O—H共价键、0.92 g/mL为题设、101.325kPa、约4°C密度最大。公式及条件：ρ=m/V；相变无物质损失时m可不变而V因ρ改变。；Q=mcΔT仅用于无相变、比热近似恒定的温变段。；纯水约0°C熔点与100°C沸点对应约101.325 kPa参考；其他压力与溶质需另审。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 2, authentic subsection 2.1.1. Display the original Chinese title exactly: 水的氢键物性与相变. Topic-specific scientific requirements and instructional purpose: Distinguish intermolecular hydrogen bonds from intramolecular O-H bonds, compare the less dense ice network with liquid water qualitatively, and show 100 g occupying about108.7 mL at the stated ice density0.92 g/mL. Label pressure-dependent phase points and keep latent heat separate from mcDeltaT. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 水分子间氢键；冰与液水相对结构；100g体积比较；单相加热段；相变条件框. Preserve the following Chinese label strings exactly: 分子间氢键、O—H共价键、0.92 g/mL为题设、101.325kPa、约4°C密度最大. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: ρ=m/V；相变无物质损失时m可不变而V因ρ改变。；Q=mcΔT仅用于无相变、比热近似恒定的温变段。；纯水约0°C熔点与100°C沸点对应约101.325 kPa参考；其他压力与溶质需另审。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：普通汽化仍H₂O；冰密度较小体积较大；Q=mcΔT不含潜热；沸点注明压力。不得把水的物理性质画成另一知识主题；不得改动分子间氢键、O—H共价键、0.92 g/mL为题设、101.325kPa、约4°C密度最大的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 普通汽化仍H₂O
- 冰密度较小体积较大
- Q=mcΔT不含潜热
- 沸点注明压力
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/10-1-intermolecular-forces

旧图复用：已有水氢键图可复核复用；密度与相变需准确新图。实际匹配：无。

## 化学 第2章 · 2.1.2 水的化学性质

ID：B05-CHEM02-2-1-2；优先级：P0；状态：not_produced。

用途：按条件描述水与金属氧化物的反应；由电解与氧化还原追踪原子和电子。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：Na水反应；铁蒸气Fe₃O₄；适当水电解两极；H₂/O₂量比；氧化数变化。

关系：H₂:O₂体积2:1同T/P；质量1:8；氢在阴极氧在阳极的相应模型；电解质不任意。

文字：2H₂O→2H₂+O₂、高温水蒸气、Fe₃O₄、惰性电极/适当电解质、非通用盐水模型。

公式与单位：2Na+2H₂O→2NaOH+H₂；3Fe+4H₂O(g)→Fe₃O₄+4H₂（相应高温）。；CaO+H₂O→Ca(OH)₂；CO₂+H₂O⇌H₂CO₃（不能全写单向完全）。；2H₂O→2H₂+O₂：同T/P理想气V比2:1，m比4:32=1:8。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第2章《水和氢》真实小节2.1.2《水的化学性质》制作《水反应与电解条件》教学图。学习目的：按条件描述水与金属氧化物的反应；由电解与氧化还原追踪原子和电子。本图是有条件的科学模型，非实测图或官方考题。必须出现：Na水反应；铁蒸气Fe₃O₄；适当水电解两极；H₂/O₂量比；氧化数变化。必须保持关系：H₂:O₂体积2:1同T/P；质量1:8；氢在阴极氧在阳极的相应模型；电解质不任意。中文标签逐字采用：2H₂O→2H₂+O₂、高温水蒸气、Fe₃O₄、惰性电极/适当电解质、非通用盐水模型。公式及条件：2Na+2H₂O→2NaOH+H₂；3Fe+4H₂O(g)→Fe₃O₄+4H₂（相应高温）。；CaO+H₂O→Ca(OH)₂；CO₂+H₂O⇌H₂CO₃（不能全写单向完全）。；2H₂O→2H₂+O₂：同T/P理想气V比2:1，m比4:32=1:8。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 2, authentic subsection 2.1.2. Display the original Chinese title exactly: 水反应与电解条件. Topic-specific scientific requirements and instructional purpose: Draw the specified water reactions with correct conditions, especially Fe3O4 from hot iron and steam. For the appropriate inert-electrode water-electrolysis model, show hydrogen at the cathode and oxygen at the anode, volume ratio2:1 at equal T/P but mass ratio1:8. Do not imply arbitrary chloride electrolyte gives the same products. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: Na水反应；铁蒸气Fe₃O₄；适当水电解两极；H₂/O₂量比；氧化数变化. Preserve the following Chinese label strings exactly: 2H₂O→2H₂+O₂、高温水蒸气、Fe₃O₄、惰性电极/适当电解质、非通用盐水模型. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 2Na+2H₂O→2NaOH+H₂；3Fe+4H₂O(g)→Fe₃O₄+4H₂（相应高温）。；CaO+H₂O→Ca(OH)₂；CO₂+H₂O⇌H₂CO₃（不能全写单向完全）。；2H₂O→2H₂+O₂：同T/P理想气V比2:1，m比4:32=1:8。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：H₂:O₂体积2:1同T/P；质量1:8；氢在阴极氧在阳极的相应模型；电解质不任意。不得把水的化学性质画成另一知识主题；不得改动2H₂O→2H₂+O₂、高温水蒸气、Fe₃O₄、惰性电极/适当电解质、非通用盐水模型的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- H₂:O₂体积2:1同T/P
- 质量1:8
- 氢在阴极氧在阳极的相应模型
- 电解质不任意
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/17-7-electrolysis

旧图复用：现有电解图须核极性、气体与电解质后复用。实际匹配：无。

## 化学 第2章 · 2.2.1 氢气的制取

ID：B05-CHEM02-2-2-1；优先级：P0；状态：not_produced。

用途：按金属酸与电解条件选择制氢方法；由气路和限量计量评价实验结果。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：Zn稀酸反应器；敞口长颈漏斗液封；分液漏斗另图；导气出口；排水收集；初始空气框。

关系：Zn:H₂=1:1；HCl:Zn=2:1；不把两种漏斗混画；不点燃反应瓶。

文字：稀非氧化性酸、液封、通畅气路、规范检验、指定温压。

公式与单位：Zn+2HCl→ZnCl₂+H₂；Zn+H₂SO₄(稀)→ZnSO₄+H₂。；n理论H₂=min(nZn,nHCl/2)；若用酸类型不同，先核反应路径。；气路检查包括密封、出口、漏斗控制、收集朝向及初始空气，不能凭方程决定全部装置正确。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第2章《水和氢》真实小节2.2.1《氢气的制取》制作《氢气制取的反应与气路》教学图。学习目的：按金属酸与电解条件选择制氢方法；由气路和限量计量评价实验结果。本图是有条件的科学模型，非实测图或官方考题。必须出现：Zn稀酸反应器；敞口长颈漏斗液封；分液漏斗另图；导气出口；排水收集；初始空气框。必须保持关系：Zn:H₂=1:1；HCl:Zn=2:1；不把两种漏斗混画；不点燃反应瓶。中文标签逐字采用：稀非氧化性酸、液封、通畅气路、规范检验、指定温压。公式及条件：Zn+2HCl→ZnCl₂+H₂；Zn+H₂SO₄(稀)→ZnSO₄+H₂。；n理论H₂=min(nZn,nHCl/2)；若用酸类型不同，先核反应路径。；气路检查包括密封、出口、漏斗控制、收集朝向及初始空气，不能凭方程决定全部装置正确。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 2, authentic subsection 2.2.1. Display the original Chinese title exactly: 氢气制取的反应与气路. Topic-specific scientific requirements and instructional purpose: Show zinc reacting with dilute nonoxidizing acid, distinguish an open thistle funnel requiring a liquid seal from a stopcock dropping funnel, and trace the gas outlet and appropriate collection route. Mark initial air and verification requirements; never show ignition at the reaction vessel or a blocked sealed gas path. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: Zn稀酸反应器；敞口长颈漏斗液封；分液漏斗另图；导气出口；排水收集；初始空气框. Preserve the following Chinese label strings exactly: 稀非氧化性酸、液封、通畅气路、规范检验、指定温压. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: Zn+2HCl→ZnCl₂+H₂；Zn+H₂SO₄(稀)→ZnSO₄+H₂。；n理论H₂=min(nZn,nHCl/2)；若用酸类型不同，先核反应路径。；气路检查包括密封、出口、漏斗控制、收集朝向及初始空气，不能凭方程决定全部装置正确。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：Zn:H₂=1:1；HCl:Zn=2:1；不把两种漏斗混画；不点燃反应瓶。不得把氢气的制取画成另一知识主题；不得改动稀非氧化性酸、液封、通畅气路、规范检验、指定温压的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- Zn:H₂=1:1
- HCl:Zn=2:1
- 不把两种漏斗混画
- 不点燃反应瓶
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/18-5-occurrence-preparation-and-compounds-of-hydrogen

旧图复用：需要可靠装置原图；未审核图不放正式页面。实际匹配：无。

## 化学 第2章 · 2.2.2 氢气的性质

ID：B05-CHEM02-2-2-2；优先级：P0；状态：not_produced。

用途：由分子和反应条件说明氢的物化性质；用氧化数与计量解释燃烧和还原。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：H₂/O₂到水；CuO黑到Cu色；H/Cu氧化数箭头；冷凝水对照；相态条件框。

关系：CuO:H₂:Cu:H₂O=1:1:1:1；H氧化Cu还原；冷凝不自动唯一来源；不任意加热含空气系统。

文字：加热条件、H0→+1、Cu+2→0、水蒸气/液水区分、对照。

公式与单位：2H₂+O₂→2H₂O；同温压n/V比2:1:2只对相应气态计量条件使用。；CuO+H₂→Cu+H₂O（加热等适用条件）；H0→+1，Cu+2→0。；NaH等金属氢化物中H可为−1，H₂单质为0；氧化数依化合物。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第2章《水和氢》真实小节2.2.2《氢气的性质》制作《氢的燃烧与还原》教学图。学习目的：由分子和反应条件说明氢的物化性质；用氧化数与计量解释燃烧和还原。本图是有条件的科学模型，非实测图或官方考题。必须出现：H₂/O₂到水；CuO黑到Cu色；H/Cu氧化数箭头；冷凝水对照；相态条件框。必须保持关系：CuO:H₂:Cu:H₂O=1:1:1:1；H氧化Cu还原；冷凝不自动唯一来源；不任意加热含空气系统。中文标签逐字采用：加热条件、H0→+1、Cu+2→0、水蒸气/液水区分、对照。公式及条件：2H₂+O₂→2H₂O；同温压n/V比2:1:2只对相应气态计量条件使用。；CuO+H₂→Cu+H₂O（加热等适用条件）；H0→+1，Cu+2→0。；NaH等金属氢化物中H可为−1，H₂单质为0；氧化数依化合物。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 2, authentic subsection 2.2.2. Display the original Chinese title exactly: 氢的燃烧与还原. Topic-specific scientific requirements and instructional purpose: Balance hydrogen combustion and CuO reduction, mark H from0 to+1 and Cu from+2 to0, and distinguish water-vapour versus liquid-water energy conventions. If depicting apparatus, show verified gas-flow and air-removal conditions and include a background-moisture control rather than treating any condensate as unique proof. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: H₂/O₂到水；CuO黑到Cu色；H/Cu氧化数箭头；冷凝水对照；相态条件框. Preserve the following Chinese label strings exactly: 加热条件、H0→+1、Cu+2→0、水蒸气/液水区分、对照. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 2H₂+O₂→2H₂O；同温压n/V比2:1:2只对相应气态计量条件使用。；CuO+H₂→Cu+H₂O（加热等适用条件）；H0→+1，Cu+2→0。；NaH等金属氢化物中H可为−1，H₂单质为0；氧化数依化合物。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：CuO:H₂:Cu:H₂O=1:1:1:1；H氧化Cu还原；冷凝不自动唯一来源；不任意加热含空气系统。不得把氢气的性质画成另一知识主题；不得改动加热条件、H0→+1、Cu+2→0、水蒸气/液水区分、对照的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- CuO:H₂:Cu:H₂O=1:1:1:1
- H氧化Cu还原
- 冷凝不自动唯一来源
- 不任意加热含空气系统
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/18-5-occurrence-preparation-and-compounds-of-hydrogen

旧图复用：暂无已审装置图；结构气路必须参考可靠教师图。实际匹配：无。

## 化学 第2章 · 2.2.3 氢气的用途

ID：B05-CHEM02-2-2-3；优先级：P1；状态：not_produced。

用途：将氢的反应性质连到合成燃料还原用途；以能量收支评价氢能源和环境边界。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：合成氨1:3:2；有机加氢；CuO还原；燃料电池输入输出；制氢储运使用边界。

关系：理论与实际转化分开；242kJ基准生成水蒸气；60%给145.2kJ电；使用端不代表全周期。

文字：能源载体、η、物料比、上游能量、相态基准。

公式与单位：N₂+3H₂⇌2NH₃：理论n比1:3:2，实际转化率另给。；燃料电池效率η=有用电能/题定化学能输入；E电=ηE输入。；0°C101.325kPa的理想近似体积V=n×22.4 L；质量与体积能量指标不同。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第2章《水和氢》真实小节2.2.3《氢气的用途》制作《氢用途与能量边界》教学图。学习目的：将氢的反应性质连到合成燃料还原用途；以能量收支评价氢能源和环境边界。本图是有条件的科学模型，非实测图或官方考题。必须出现：合成氨1:3:2；有机加氢；CuO还原；燃料电池输入输出；制氢储运使用边界。必须保持关系：理论与实际转化分开；242kJ基准生成水蒸气；60%给145.2kJ电；使用端不代表全周期。中文标签逐字采用：能源载体、η、物料比、上游能量、相态基准。公式及条件：N₂+3H₂⇌2NH₃：理论n比1:3:2，实际转化率另给。；燃料电池效率η=有用电能/题定化学能输入；E电=ηE输入。；0°C101.325kPa的理想近似体积V=n×22.4 L；质量与体积能量指标不同。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 2, authentic subsection 2.2.3. Display the original Chinese title exactly: 氢用途与能量边界. Topic-specific scientific requirements and instructional purpose: Map hydrogen uses to specific reactions and conditions: ammonia synthesis, hydrogenation, selected oxide reduction and electrochemical energy conversion. Show a stated water-vapour energy basis242 kJ/mol with60% electrical output145.2 kJ, and include production, storage and transport in lifecycle boundaries rather than claiming universal zero emissions. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 合成氨1:3:2；有机加氢；CuO还原；燃料电池输入输出；制氢储运使用边界. Preserve the following Chinese label strings exactly: 能源载体、η、物料比、上游能量、相态基准. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: N₂+3H₂⇌2NH₃：理论n比1:3:2，实际转化率另给。；燃料电池效率η=有用电能/题定化学能输入；E电=ηE输入。；0°C101.325kPa的理想近似体积V=n×22.4 L；质量与体积能量指标不同。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：理论与实际转化分开；242kJ基准生成水蒸气；60%给145.2kJ电；使用端不代表全周期。不得把氢气的用途画成另一知识主题；不得改动能源载体、η、物料比、上游能量、相态基准的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 理论与实际转化分开
- 242kJ基准生成水蒸气
- 60%给145.2kJ电
- 使用端不代表全周期
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://dokumen.pub/e329b58567bfcaac79ff8da5a0ecc507.html
- https://openstax.org/books/chemistry-2e/pages/17-5-batteries-and-fuel-cells

旧图复用：暂无对应图；可用清晰收支结构图，非装饰氢能插画。实际匹配：无。

## 化学 第26章 · 26.1 有机化合物

ID：B05-CHEM26-26-1；优先级：P0；状态：not_produced。

用途：按组成与结构解释有机化合物分类；由燃烧数据求最简式并检查证据限制。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：分类集合；CO₂/H₂O燃烧产物；C/H/O摩尔比；最简式；分子式；结构证据。

关系：烃仅C/H；nH=2nH₂O；氧差值需元素范围条件；分子式不能自动唯一结构。

文字：有机物、烃、CH₂O、C₂H₄O₂、定量收集。

公式与单位：完全燃烧且定量收集：n(C)=n(CO₂)，n(H)=2n(H₂O)。；仅含C/H/O时，m(O)=m样−m(C)−m(H)，再n(O)=m(O)/16 g·mol⁻¹。；分子式=(最简式)ₖ，k=M分子/M最简式；k应为正整数，结构仍需其他证据。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第26章《有机化学》真实小节26.1《有机化合物》制作《组成、分子式与结构的信息层次》教学图。学习目的：按组成与结构解释有机化合物分类；由燃烧数据求最简式并检查证据限制。本图是有条件的科学模型，非实测图或官方考题。必须出现：分类集合；CO₂/H₂O燃烧产物；C/H/O摩尔比；最简式；分子式；结构证据。必须保持关系：烃仅C/H；nH=2nH₂O；氧差值需元素范围条件；分子式不能自动唯一结构。中文标签逐字采用：有机物、烃、CH₂O、C₂H₄O₂、定量收集。公式及条件：完全燃烧且定量收集：n(C)=n(CO₂)，n(H)=2n(H₂O)。；仅含C/H/O时，m(O)=m样−m(C)−m(H)，再n(O)=m(O)/16 g·mol⁻¹。；分子式=(最简式)ₖ，k=M分子/M最简式；k应为正整数，结构仍需其他证据。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 26, authentic subsection 26.1. Display the original Chinese title exactly: 组成、分子式与结构的信息层次. Topic-specific scientific requirements and instructional purpose: Show hydrocarbons as the carbon-and-hydrogen-only subset, with CO2 and carbonates treated as conventional inorganic exceptions. Trace quantitative combustion products to C/H atom amounts, then empirical and molecular formulas; require extra evidence for unique connectivity. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 分类集合；CO₂/H₂O燃烧产物；C/H/O摩尔比；最简式；分子式；结构证据. Preserve the following Chinese label strings exactly: 有机物、烃、CH₂O、C₂H₄O₂、定量收集. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 完全燃烧且定量收集：n(C)=n(CO₂)，n(H)=2n(H₂O)。；仅含C/H/O时，m(O)=m样−m(C)−m(H)，再n(O)=m(O)/16 g·mol⁻¹。；分子式=(最简式)ₖ，k=M分子/M最简式；k应为正整数，结构仍需其他证据。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：烃仅C/H；nH=2nH₂O；氧差值需元素范围条件；分子式不能自动唯一结构。不得把有机化合物画成另一知识主题；不得改动有机物、烃、CH₂O、C₂H₄O₂、定量收集的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 烃仅C/H
- nH=2nH₂O
- 氧差值需元素范围条件
- 分子式不能自动唯一结构
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/chemistry-2e/pages/20-1-hydrocarbons

旧图复用：可复用物质的量流程局部，非完整有机分类图。实际匹配：无。

## 化学 第26章 · 26.2 有机物的特质

ID：B05-CHEM26-26-2；优先级：P1；状态：not_produced。

用途：用结构与分子间作用解释常见性质趋势；识别概括规律的例外并评价实验结论。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：分子内共价键；分子间氢键；水与小分子醇；长链醇；分子与离子溶液。

关系：相变不画C—C键普遍断裂；OH亲水性须结合碳链；导电依可移动离子。

文字：共价键、分子间作用、非极性部分、可移动离子、趋势非绝对。

公式与单位：分子内键决定连接；熔沸常涉及分子间作用，两者不能混同。；同类结构比较氢键、极性、相对分子质量和形状，避免单因素无条件推断。；电导须有可移动载流子；水溶性与导电性不是同一性质。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第26章《有机化学》真实小节26.2《有机物的特质》制作《结构与宏观性质的条件关系》教学图。学习目的：用结构与分子间作用解释常见性质趋势；识别概括规律的例外并评价实验结论。本图是有条件的科学模型，非实测图或官方考题。必须出现：分子内共价键；分子间氢键；水与小分子醇；长链醇；分子与离子溶液。必须保持关系：相变不画C—C键普遍断裂；OH亲水性须结合碳链；导电依可移动离子。中文标签逐字采用：共价键、分子间作用、非极性部分、可移动离子、趋势非绝对。公式及条件：分子内键决定连接；熔沸常涉及分子间作用，两者不能混同。；同类结构比较氢键、极性、相对分子质量和形状，避免单因素无条件推断。；电导须有可移动载流子；水溶性与导电性不是同一性质。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 26, authentic subsection 26.2. Display the original Chinese title exactly: 结构与宏观性质的条件关系. Topic-specific scientific requirements and instructional purpose: Distinguish intramolecular covalent bonds from intermolecular hydrogen bonding during boiling. Contrast a small alcohol with a long hydrocarbon chain bearing OH, and neutral molecular solutes with ion-producing solutes. Never imply all organic compounds are insoluble or nonconducting. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 分子内共价键；分子间氢键；水与小分子醇；长链醇；分子与离子溶液. Preserve the following Chinese label strings exactly: 共价键、分子间作用、非极性部分、可移动离子、趋势非绝对. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 分子内键决定连接；熔沸常涉及分子间作用，两者不能混同。；同类结构比较氢键、极性、相对分子质量和形状，避免单因素无条件推断。；电导须有可移动载流子；水溶性与导电性不是同一性质。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：相变不画C—C键普遍断裂；OH亲水性须结合碳链；导电依可移动离子。不得把有机物的特质画成另一知识主题；不得改动共价键、分子间作用、非极性部分、可移动离子、趋势非绝对的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 相变不画C—C键普遍断裂
- OH亲水性须结合碳链
- 导电依可移动离子
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/chemistry-2e/pages/20-2-alcohols-and-ethers

旧图复用：氢键旧图可局部复用，需核乙醇羟基连接。实际匹配：无。

## 化学 第26章 · 26.3 有机物的分类

ID：B05-CHEM26-26-3；优先级：P0；状态：not_produced。

用途：按骨架与官能团分别分类；以连接关系解释同分子式不同类别。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：乙醇/二甲醚；羧酸/酯；醛/酮；丙烯/环丙烷。

关系：同式不一定同连接；羧酸OH不画成独立醇；每个C和O满足价键。

文字：醇、醚、羧酸、酯、醛、酮、分子式≠唯一结构。

公式与单位：分类至少分两轴：碳骨架（链/环等）与官能团（醇/醚/醛/酮/酸/酯等）。；CnH₂n可对应单环饱和烃或单烯烃等相应模型，不能仅由通式唯一判类别。；画结构后核每个C常见四价、O常见二价、H一价；官能团按连接环境识别。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第26章《有机化学》真实小节26.3《有机物的分类》制作《有机分类的连接判据》教学图。学习目的：按骨架与官能团分别分类；以连接关系解释同分子式不同类别。本图是有条件的科学模型，非实测图或官方考题。必须出现：乙醇/二甲醚；羧酸/酯；醛/酮；丙烯/环丙烷。必须保持关系：同式不一定同连接；羧酸OH不画成独立醇；每个C和O满足价键。中文标签逐字采用：醇、醚、羧酸、酯、醛、酮、分子式≠唯一结构。公式及条件：分类至少分两轴：碳骨架（链/环等）与官能团（醇/醚/醛/酮/酸/酯等）。；CnH₂n可对应单环饱和烃或单烯烃等相应模型，不能仅由通式唯一判类别。；画结构后核每个C常见四价、O常见二价、H一价；官能团按连接环境识别。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 26, authentic subsection 26.3. Display the original Chinese title exactly: 有机分类的连接判据. Topic-specific scientific requirements and instructional purpose: Compare ethanol with dimethyl ether, carboxylic acid with ester, aldehyde with ketone, and propene with cyclopropane. Render explicit correct connectivity and valence; do not classify a carboxylic OH as an alcohol or infer a unique structure from a molecular formula. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 乙醇/二甲醚；羧酸/酯；醛/酮；丙烯/环丙烷. Preserve the following Chinese label strings exactly: 醇、醚、羧酸、酯、醛、酮、分子式≠唯一结构. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 分类至少分两轴：碳骨架（链/环等）与官能团（醇/醚/醛/酮/酸/酯等）。；CnH₂n可对应单环饱和烃或单烯烃等相应模型，不能仅由通式唯一判类别。；画结构后核每个C常见四价、O常见二价、H一价；官能团按连接环境识别。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：同式不一定同连接；羧酸OH不画成独立醇；每个C和O满足价键。不得把有机物的分类画成另一知识主题；不得改动醇、醚、羧酸、酯、醛、酮、分子式≠唯一结构的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 同式不一定同连接
- 羧酸OH不画成独立醇
- 每个C和O满足价键
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/chemistry-2e/pages/20-3-aldehydes-ketones-carboxylic-acids-and-esters

旧图复用：现有化学结构图须核官能团后局部复用。实际匹配：无。

## 化学 第26章 · 26.4 有机化学的学习与研究

ID：B05-CHEM26-26-4；优先级：P1；状态：not_produced。

用途：把分离纯化、组成与结构证据分层；由多项资料作有限且可检验的推断。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：混合样；分离；元素分析；相对分子质量；结构候选；色谱板。

关系：Rf为同起点距离比；一个斑点不必纯；分子式不直接唯一连接；产率先扣杂质。

文字：Rf=3/6=0.50、粗样、纯度、最简式、分子式、连接证据。

公式与单位：Rf=d斑点/d前沿，同一起点同一板且前沿距离非零；无量纲。；产率=实际目标产物量/理论目标产物量×100%；粗样质量不一定等于纯产物质量。；研究证据链：纯度与分离 → 元素组成 → 分子式 → 关键连接证据 → 排除候选 → 再验证。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第26章《有机化学》真实小节26.4《有机化学的学习与研究》制作《有机鉴定的证据层级》教学图。学习目的：把分离纯化、组成与结构证据分层；由多项资料作有限且可检验的推断。本图是有条件的科学模型，非实测图或官方考题。必须出现：混合样；分离；元素分析；相对分子质量；结构候选；色谱板。必须保持关系：Rf为同起点距离比；一个斑点不必纯；分子式不直接唯一连接；产率先扣杂质。中文标签逐字采用：Rf=3/6=0.50、粗样、纯度、最简式、分子式、连接证据。公式及条件：Rf=d斑点/d前沿，同一起点同一板且前沿距离非零；无量纲。；产率=实际目标产物量/理论目标产物量×100%；粗样质量不一定等于纯产物质量。；研究证据链：纯度与分离 → 元素组成 → 分子式 → 关键连接证据 → 排除候选 → 再验证。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 26, authentic subsection 26.4. Display the original Chinese title exactly: 有机鉴定的证据层级. Topic-specific scientific requirements and instructional purpose: Show an evidence hierarchy from separation and purity to elemental composition, molecular formula and connectivity tests. Draw a chromatogram with spot travel 3 cm and solvent front 6 cm from the same baseline, Rf=0.50; state that one spot or one matching Rf is not proof of purity or identity. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 混合样；分离；元素分析；相对分子质量；结构候选；色谱板. Preserve the following Chinese label strings exactly: Rf=3/6=0.50、粗样、纯度、最简式、分子式、连接证据. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: Rf=d斑点/d前沿，同一起点同一板且前沿距离非零；无量纲。；产率=实际目标产物量/理论目标产物量×100%；粗样质量不一定等于纯产物质量。；研究证据链：纯度与分离 → 元素组成 → 分子式 → 关键连接证据 → 排除候选 → 再验证。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：Rf为同起点距离比；一个斑点不必纯；分子式不直接唯一连接；产率先扣杂质。不得把有机化学的学习与研究画成另一知识主题；不得改动Rf=3/6=0.50、粗样、纯度、最简式、分子式、连接证据的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- Rf为同起点距离比
- 一个斑点不必纯
- 分子式不直接唯一连接
- 产率先扣杂质
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/chemistry-2e/pages/4-4-reaction-yields
- https://goldbook.iupac.org/terms/view/R05353/html

旧图复用：无整体对应图；色谱距离须精确。实际匹配：无。

## 化学 第26章 · 26.5 有机化学的重要进展

ID：B05-CHEM26-26-5；优先级：P2；状态：not_produced。

用途：从结构性能用途解释技术价值；依据收支和证据评价所谓绿色创新。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：分子结构；性能测试；物料收支；能源输入；使用与处置；证据阶梯。

关系：来源不决定安全；产率不等同完整环境表现；降解条件须标明。

文字：结构—性能、目标产物、副产物、能耗、条件与时间、证据范围。

公式与单位：产率衡量目标产物实际量/理论量；原子利用等工艺指标衡量另一个维度，不能互代。；给定工艺物料收支：输入质量=目标产物+副产物+未反应/损失等相应项，边界要完整。；技术评价：结构与机制 → 可测性能 → 使用条件 → 安全与环境 → 生命周期与证据限制。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第26章《有机化学》真实小节26.5《有机化学的重要进展》制作《有机创新的多指标评价》教学图。学习目的：从结构性能用途解释技术价值；依据收支和证据评价所谓绿色创新。本图是有条件的科学模型，非实测图或官方考题。必须出现：分子结构；性能测试；物料收支；能源输入；使用与处置；证据阶梯。必须保持关系：来源不决定安全；产率不等同完整环境表现；降解条件须标明。中文标签逐字采用：结构—性能、目标产物、副产物、能耗、条件与时间、证据范围。公式及条件：产率衡量目标产物实际量/理论量；原子利用等工艺指标衡量另一个维度，不能互代。；给定工艺物料收支：输入质量=目标产物+副产物+未反应/损失等相应项，边界要完整。；技术评价：结构与机制 → 可测性能 → 使用条件 → 安全与环境 → 生命周期与证据限制。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 26, authentic subsection 26.5. Display the original Chinese title exactly: 有机创新的多指标评价. Topic-specific scientific requirements and instructional purpose: Map organic innovation from molecular structure to measured performance, material balance, energy use and end-of-life conditions. Distinguish natural origin from safety, reaction yield from overall environmental performance, and conditional degradability from universal harmless disappearance. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 分子结构；性能测试；物料收支；能源输入；使用与处置；证据阶梯. Preserve the following Chinese label strings exactly: 结构—性能、目标产物、副产物、能耗、条件与时间、证据范围. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 产率衡量目标产物实际量/理论量；原子利用等工艺指标衡量另一个维度，不能互代。；给定工艺物料收支：输入质量=目标产物+副产物+未反应/损失等相应项，边界要完整。；技术评价：结构与机制 → 可测性能 → 使用条件 → 安全与环境 → 生命周期与证据限制。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：来源不决定安全；产率不等同完整环境表现；降解条件须标明。不得把有机化学的重要进展画成另一知识主题；不得改动结构—性能、目标产物、副产物、能耗、条件与时间、证据范围的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 来源不决定安全
- 产率不等同完整环境表现
- 降解条件须标明
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://www.acs.org/green-chemistry-sustainability/principles/12-principles-of-green-chemistry.html

旧图复用：不需辅助插画替代科学关系；可用清晰结构图。实际匹配：无。

## 化学 第29章 · 29.1 炔烃的通式、同分异构体和命名

ID：B05-CHEM29-29-1；优先级：P0；状态：not_produced。

用途：在限定结构下推导炔烃通式；按三键位置命名并区分同式异类。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：乙炔；1-丁炔；2-丁炔；3-甲基-1-丁炔；二烯同式候选。

关系：三键碳四价；同式不唯一结构；端炔与内炔区分；翻转不新增异构。

文字：CₙH₂ₙ₋₂、n≥2、无环单三键、最低位次、C≡C。

公式与单位：无环单三键烃：CₙH₂ₙ₋₂，n≥2；相对同碳数烷烃少4H。；1-丁炔HC≡C—CH₂—CH₃；2-丁炔CH₃—C≡C—CH₃，均C₄H₆。；命名先核含三键母链及最低相应位次，画图逐碳核四价。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第29章《炔烃》真实小节29.1《炔烃的通式、同分异构体和命名》制作《炔烃命名与通式边界》教学图。学习目的：在限定结构下推导炔烃通式；按三键位置命名并区分同式异类。本图是有条件的科学模型，非实测图或官方考题。必须出现：乙炔；1-丁炔；2-丁炔；3-甲基-1-丁炔；二烯同式候选。必须保持关系：三键碳四价；同式不唯一结构；端炔与内炔区分；翻转不新增异构。中文标签逐字采用：CₙH₂ₙ₋₂、n≥2、无环单三键、最低位次、C≡C。公式及条件：无环单三键烃：CₙH₂ₙ₋₂，n≥2；相对同碳数烷烃少4H。；1-丁炔HC≡C—CH₂—CH₃；2-丁炔CH₃—C≡C—CH₃，均C₄H₆。；命名先核含三键母链及最低相应位次，画图逐碳核四价。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 29, authentic subsection 29.1. Display the original Chinese title exactly: 炔烃命名与通式边界. Topic-specific scientific requirements and instructional purpose: Draw valence-correct ethyne, but-1-yne, but-2-yne and 3-methylbut-1-yne with numbered parent chains. State the acyclic single-triple-bond formula CnH2n-2 for n>=2, and contrast a C4H6 diene to show that a molecular formula is not a unique class identifier. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 乙炔；1-丁炔；2-丁炔；3-甲基-1-丁炔；二烯同式候选. Preserve the following Chinese label strings exactly: CₙH₂ₙ₋₂、n≥2、无环单三键、最低位次、C≡C. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 无环单三键烃：CₙH₂ₙ₋₂，n≥2；相对同碳数烷烃少4H。；1-丁炔HC≡C—CH₂—CH₃；2-丁炔CH₃—C≡C—CH₃，均C₄H₆。；命名先核含三键母链及最低相应位次，画图逐碳核四价。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：三键碳四价；同式不唯一结构；端炔与内炔区分；翻转不新增异构。不得把炔烃的通式、同分异构体和命名画成另一知识主题；不得改动CₙH₂ₙ₋₂、n≥2、无环单三键、最低位次、C≡C的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 三键碳四价
- 同式不唯一结构
- 端炔与内炔区分
- 翻转不新增异构
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/chemistry-2e/pages/20-1-hydrocarbons
- https://openstax.org/books/organic-chemistry/pages/9-1-naming-alkynes

旧图复用：已有烃图需核三键连接后复用，无完整对应。实际匹配：无。

## 化学 第29章 · 29.2 炔烃的结构

ID：B05-CHEM29-29-2；优先级：P0；状态：not_produced。

用途：用sp杂化说明三键的线性几何；区分键总强度π反应性与端氢酸性。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：H—C≡C—H线性骨架；轴向σ；两组正交p侧向重叠；端炔/内炔对比。

关系：180°局部几何；1σ+2π；两π正交；不把电子画成确定小球轨道。

文字：sp、σ、π₁、π₂、180°、端氢。

公式与单位：C≡C=1σ+2π；两个π系统方向相互正交，σ沿核间轴。；三键碳sp模型，连接夹角约180°；整个长分子不必全线性。；端炔R—C≡C—H有相应端氢，内炔R—C≡C—R′没有；弱酸性不等于能被任意弱碱定量去质子。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第29章《炔烃》真实小节29.2《炔烃的结构》制作《炔烃sp与三键结构》教学图。学习目的：用sp杂化说明三键的线性几何；区分键总强度π反应性与端氢酸性。本图是有条件的科学模型，非实测图或官方考题。必须出现：H—C≡C—H线性骨架；轴向σ；两组正交p侧向重叠；端炔/内炔对比。必须保持关系：180°局部几何；1σ+2π；两π正交；不把电子画成确定小球轨道。中文标签逐字采用：sp、σ、π₁、π₂、180°、端氢。公式及条件：C≡C=1σ+2π；两个π系统方向相互正交，σ沿核间轴。；三键碳sp模型，连接夹角约180°；整个长分子不必全线性。；端炔R—C≡C—H有相应端氢，内炔R—C≡C—R′没有；弱酸性不等于能被任意弱碱定量去质子。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 29, authentic subsection 29.2. Display the original Chinese title exactly: 炔烃sp与三键结构. Topic-specific scientific requirements and instructional purpose: Draw linear H-C≡C-H with sp-hybridized carbons, one axial sigma bond and two mutually perpendicular pi systems from unhybridized p orbitals. Contrast a terminal sp-C-H with an internal alkyne; do not draw three equivalent sigma rods or fixed electron trajectories. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: H—C≡C—H线性骨架；轴向σ；两组正交p侧向重叠；端炔/内炔对比. Preserve the following Chinese label strings exactly: sp、σ、π₁、π₂、180°、端氢. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: C≡C=1σ+2π；两个π系统方向相互正交，σ沿核间轴。；三键碳sp模型，连接夹角约180°；整个长分子不必全线性。；端炔R—C≡C—H有相应端氢，内炔R—C≡C—R′没有；弱酸性不等于能被任意弱碱定量去质子。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：180°局部几何；1σ+2π；两π正交；不把电子画成确定小球轨道。不得把炔烃的结构画成另一知识主题；不得改动sp、σ、π₁、π₂、180°、端氢的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 180°局部几何
- 1σ+2π
- 两π正交
- 不把电子画成确定小球轨道
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/chemistry-2e/pages/8-2-hybrid-atomic-orbitals
- https://openstax.org/books/organic-chemistry/pages/9-7-alkyne-acidity-formation-of-acetylide-anions

旧图复用：暂无对应正确轨道图；科学SVG须专门审轨道方向。实际匹配：无。

## 化学 第29章 · 29.3 炔烃的物理性质

ID：B05-CHEM29-29-3；优先级：P1；状态：not_produced。

用途：用分子作用解释状态溶解与沸点趋势；在同温同压模型下计算气体密度。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：乙炔/氢/空气同温同压比较；温度与沸点标尺；水/有机溶剂示意；Vm条件框。

关系：26/2=13；26/29≈.90；0°C101.325kPa才用22.4近似；无自行加压装置图。

文字：同T同P、g/L、g/mol、Vm、相变不等于断三键。

公式与单位：理想气体ρ=m/V=PM/(RT)，单位体系需一致。；同温同压、近理想：ρ₁/ρ₂=M₁/M₂；若空气M按题取29，则乙炔相对空气约26/29。；气体状态与溶解比较须注明温压；汽化通常克服分子间作用，非断开全部分子内三键。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第29章《炔烃》真实小节29.3《炔烃的物理性质》制作《炔烃物性与气体条件》教学图。学习目的：用分子作用解释状态溶解与沸点趋势；在同温同压模型下计算气体密度。本图是有条件的科学模型，非实测图或官方考题。必须出现：乙炔/氢/空气同温同压比较；温度与沸点标尺；水/有机溶剂示意；Vm条件框。必须保持关系：26/2=13；26/29≈.90；0°C101.325kPa才用22.4近似；无自行加压装置图。中文标签逐字采用：同T同P、g/L、g/mol、Vm、相变不等于断三键。公式及条件：理想气体ρ=m/V=PM/(RT)，单位体系需一致。；同温同压、近理想：ρ₁/ρ₂=M₁/M₂；若空气M按题取29，则乙炔相对空气约26/29。；气体状态与溶解比较须注明温压；汽化通常克服分子间作用，非断开全部分子内三键。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 29, authentic subsection 29.3. Display the original Chinese title exactly: 炔烃物性与气体条件. Topic-specific scientific requirements and instructional purpose: Compare acetylene density with hydrogen and air only at identical temperature and pressure, using molar masses 26,2 and29. State 0°C and101.325kPa for the approximate22.4 L/mol example. Distinguish boiling from bond cleavage and do not depict an improvised acetylene compression system. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 乙炔/氢/空气同温同压比较；温度与沸点标尺；水/有机溶剂示意；Vm条件框. Preserve the following Chinese label strings exactly: 同T同P、g/L、g/mol、Vm、相变不等于断三键. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 理想气体ρ=m/V=PM/(RT)，单位体系需一致。；同温同压、近理想：ρ₁/ρ₂=M₁/M₂；若空气M按题取29，则乙炔相对空气约26/29。；气体状态与溶解比较须注明温压；汽化通常克服分子间作用，非断开全部分子内三键。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：26/2=13；26/29≈.90；0°C101.325kPa才用22.4近似；无自行加压装置图。不得把炔烃的物理性质画成另一知识主题；不得改动同T同P、g/L、g/mol、Vm、相变不等于断三键的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 26/2=13
- 26/29≈.90
- 0°C101.325kPa才用22.4近似
- 无自行加压装置图
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/chemistry-2e/pages/9-2-relating-pressure-volume-amount-and-temperature-the-ideal-gas-law

旧图复用：无完全对应；气体摩尔体积旧图需保留温压条件。实际匹配：无。

## 化学 第29章 · 29.4 炔烃的化学性质

ID：B05-CHEM29-29-4；优先级：P0；状态：not_produced。

用途：按试剂与用量追踪三键加成产物；区别端炔反应氧化和脱色的鉴定边界。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：乙炔逐步加氢；HCl一步/两步；乙醛水合终产物；端炔检验条件框；燃烧配平。

关系：H₂全加2当量；HCl一步氯乙烯两步CH₃CHCl₂；水合C₂H₄O非乙醇；金属炔化物不画干燥。

文字：1eq、2eq、催化/条件、CH₃CHO、仅规范示范。

公式与单位：HC≡CH+2H₂→CH₃CH₃（相应催化、充分加氢）；一步停烯需受控条件。；HC≡CH+HCl→CH₂=CHCl；再加HCl可得CH₃CHCl₂，条件与当量分开。；2C₂H₂+5O₂→4CO₂+2H₂O；乙炔水合最终CH₃CHO，非CH₃CH₂OH。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第29章《炔烃》真实小节29.4《炔烃的化学性质》制作《炔烃反应的当量与结构》教学图。学习目的：按试剂与用量追踪三键加成产物；区别端炔反应氧化和脱色的鉴定边界。本图是有条件的科学模型，非实测图或官方考题。必须出现：乙炔逐步加氢；HCl一步/两步；乙醛水合终产物；端炔检验条件框；燃烧配平。必须保持关系：H₂全加2当量；HCl一步氯乙烯两步CH₃CHCl₂；水合C₂H₄O非乙醇；金属炔化物不画干燥。中文标签逐字采用：1eq、2eq、催化/条件、CH₃CHO、仅规范示范。公式及条件：HC≡CH+2H₂→CH₃CH₃（相应催化、充分加氢）；一步停烯需受控条件。；HC≡CH+HCl→CH₂=CHCl；再加HCl可得CH₃CHCl₂，条件与当量分开。；2C₂H₂+5O₂→4CO₂+2H₂O；乙炔水合最终CH₃CHO，非CH₃CH₂OH。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 29, authentic subsection 29.4. Display the original Chinese title exactly: 炔烃反应的当量与结构. Topic-specific scientific requirements and instructional purpose: Draw separate stoichiometric pathways for complete hydrogenation using two H2 per alkyne, one versus two HCl additions to ethyne, and classical hydration ending in acetaldehyde, not ethanol. Balance every atom and label conditions. Do not depict drying or heating hazardous metal acetylide precipitates. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 乙炔逐步加氢；HCl一步/两步；乙醛水合终产物；端炔检验条件框；燃烧配平. Preserve the following Chinese label strings exactly: 1eq、2eq、催化/条件、CH₃CHO、仅规范示范. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: HC≡CH+2H₂→CH₃CH₃（相应催化、充分加氢）；一步停烯需受控条件。；HC≡CH+HCl→CH₂=CHCl；再加HCl可得CH₃CHCl₂，条件与当量分开。；2C₂H₂+5O₂→4CO₂+2H₂O；乙炔水合最终CH₃CHO，非CH₃CH₂OH。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：H₂全加2当量；HCl一步氯乙烯两步CH₃CHCl₂；水合C₂H₄O非乙醇；金属炔化物不画干燥。不得把炔烃的化学性质画成另一知识主题；不得改动1eq、2eq、催化/条件、CH₃CHO、仅规范示范的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- H₂全加2当量
- HCl一步氯乙烯两步CH₃CHCl₂
- 水合C₂H₄O非乙醇
- 金属炔化物不画干燥
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/chemistry-2e/pages/20-1-hydrocarbons
- https://openstax.org/books/organic-chemistry/pages/9-4-hydration-of-alkynes
- https://openstax.org/books/organic-chemistry/pages/9-summary-of-reactions

旧图复用：暂无完整反应图；化学结构需确定性绘制并逐原子核验。实际匹配：无。

## 化学 第29章 · 29.5 炔烃的来源和制取

ID：B05-CHEM29-29-5；优先级：P0；状态：not_produced。

用途：由电石与甲烷反应解释乙炔来源；计算纯度产率与限定温压体积。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：电石水反应方程；纯度/限量/产率三级流程；气路出口与防回吸检查；甲烷工业主反应。

关系：CaC₂:C₂H₂=1:1；放热可燃不密闭积压；气体体积保留温压湿干条件；装置须可靠规范重画。

文字：CaC₂+2H₂O、C₂H₂+Ca(OH)₂、0°C101.325kPa、纯度≠产率、未审核装置不发布。

公式与单位：CaC₂+2H₂O→C₂H₂+Ca(OH)₂；M(CaC₂)按题取64 g/mol。；n理论C₂H₂=min[nCaC₂,nH₂O/2]；实际量需再按给定产率/收集条件。；2CH₄→C₂H₂+3H₂为简化高温主反应；0°C101.325kPa的Vm≈22.4 L/mol不可推广所有温压。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第29章《炔烃》真实小节29.5《炔烃的来源和制取》制作《乙炔来源的计量与装置要求》教学图。学习目的：由电石与甲烷反应解释乙炔来源；计算纯度产率与限定温压体积。本图是有条件的科学模型，非实测图或官方考题。必须出现：电石水反应方程；纯度/限量/产率三级流程；气路出口与防回吸检查；甲烷工业主反应。必须保持关系：CaC₂:C₂H₂=1:1；放热可燃不密闭积压；气体体积保留温压湿干条件；装置须可靠规范重画。中文标签逐字采用：CaC₂+2H₂O、C₂H₂+Ca(OH)₂、0°C101.325kPa、纯度≠产率、未审核装置不发布。公式及条件：CaC₂+2H₂O→C₂H₂+Ca(OH)₂；M(CaC₂)按题取64 g/mol。；n理论C₂H₂=min[nCaC₂,nH₂O/2]；实际量需再按给定产率/收集条件。；2CH₄→C₂H₂+3H₂为简化高温主反应；0°C101.325kPa的Vm≈22.4 L/mol不可推广所有温压。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 29, authentic subsection 29.5. Display the original Chinese title exactly: 乙炔来源的计量与装置要求. Topic-specific scientific requirements and instructional purpose: Show balanced calcium-carbide hydrolysis and separate purity, limiting-reagent and collection-yield steps. Any apparatus drawing must follow an independently verified classroom reference with a gas outlet and backflow/temperature controls, never a sealed pressure-building vessel or untested ignition instruction. Label wet/dry gas and temperature-pressure conditions. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 电石水反应方程；纯度/限量/产率三级流程；气路出口与防回吸检查；甲烷工业主反应. Preserve the following Chinese label strings exactly: CaC₂+2H₂O、C₂H₂+Ca(OH)₂、0°C101.325kPa、纯度≠产率、未审核装置不发布. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: CaC₂+2H₂O→C₂H₂+Ca(OH)₂；M(CaC₂)按题取64 g/mol。；n理论C₂H₂=min[nCaC₂,nH₂O/2]；实际量需再按给定产率/收集条件。；2CH₄→C₂H₂+3H₂为简化高温主反应；0°C101.325kPa的Vm≈22.4 L/mol不可推广所有温压。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：CaC₂:C₂H₂=1:1；放热可燃不密闭积压；气体体积保留温压湿干条件；装置须可靠规范重画。不得把炔烃的来源和制取画成另一知识主题；不得改动CaC₂+2H₂O、C₂H₂+Ca(OH)₂、0°C101.325kPa、纯度≠产率、未审核装置不发布的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- CaC₂:C₂H₂=1:1
- 放热可燃不密闭积压
- 气体体积保留温压湿干条件
- 装置须可靠规范重画
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/chemistry-2e/pages/20-1-hydrocarbons

旧图复用：暂无合格装置图；新实验装置必须用可靠原图依据再定稿。实际匹配：无。

## 化学 第35章 · 35.1 有机高分子化合物的基本概念

ID：B05-CHEM35-35-1；优先级：P0；状态：not_produced。

用途：区分单体重复单元和聚合度；按平均与端基假设计算高分子数量。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：乙烯单体；聚乙烯连续链与括号n；端基；两链长数目分布；链mol/单元mol。

关系：主链双键已消去；端键穿括号且价正确；数均按链数加权；M近似含端基假设。

文字：单体、重复单元、n、端基、数均、0.00050mol链≠0.50mol单元。

公式与单位：简单加成模型忽略端基：M链≈nM重复单元；n须按指定重复结构计。；数均相对分子质量的数值=ΣNᵢMrᵢ/ΣNᵢ；对应数均摩尔质量M_n单位g/mol，Nᵢ为链分子数。；链量n链=m/M_n（m用g、M_n用g/mol）；重复单元量≈聚合度×n链（分布口径和端基假设需明确）。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第35章《有机高分子化合物》真实小节35.1《有机高分子化合物的基本概念》制作《单体重复单元与链长分布》教学图。学习目的：区分单体重复单元和聚合度；按平均与端基假设计算高分子数量。本图是有条件的科学模型，非实测图或官方考题。必须出现：乙烯单体；聚乙烯连续链与括号n；端基；两链长数目分布；链mol/单元mol。必须保持关系：主链双键已消去；端键穿括号且价正确；数均按链数加权；M近似含端基假设。中文标签逐字采用：单体、重复单元、n、端基、数均、0.00050mol链≠0.50mol单元。公式及条件：简单加成模型忽略端基：M链≈nM重复单元；n须按指定重复结构计。；数均相对分子质量的数值=ΣNᵢMrᵢ/ΣNᵢ；对应数均摩尔质量M_n单位g/mol，Nᵢ为链分子数。；链量n链=m/M_n（m用g、M_n用g/mol）；重复单元量≈聚合度×n链（分布口径和端基假设需明确）。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 35, authentic subsection 35.1. Display the original Chinese title exactly: 单体重复单元与链长分布. Topic-specific scientific requirements and instructional purpose: Contrast ethene monomer with connected polyethylene repeat units inside brackets, with continuation bonds and labelled end groups. Show chain-length distribution and number-average weighting, and distinguish0.00050 mol of chains from0.50 mol of repeat units for average DP1000. Do not leave the monomer double bond in the polyethylene backbone. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 乙烯单体；聚乙烯连续链与括号n；端基；两链长数目分布；链mol/单元mol. Preserve the following Chinese label strings exactly: 单体、重复单元、n、端基、数均、0.00050mol链≠0.50mol单元. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 简单加成模型忽略端基：M链≈nM重复单元；n须按指定重复结构计。；数均相对分子质量的数值=ΣNᵢMrᵢ/ΣNᵢ；对应数均摩尔质量M_n单位g/mol，Nᵢ为链分子数。；链量n链=m/M_n（m用g、M_n用g/mol）；重复单元量≈聚合度×n链（分布口径和端基假设需明确）。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：主链双键已消去；端键穿括号且价正确；数均按链数加权；M近似含端基假设。不得把有机高分子化合物的基本概念画成另一知识主题；不得改动单体、重复单元、n、端基、数均、0.00050mol链≠0.50mol单元的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 主链双键已消去
- 端键穿括号且价正确
- 数均按链数加权
- M近似含端基假设
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/organic-chemistry/pages/31-7-polymer-structure-and-physical-properties

旧图复用：暂无对应旧图；聚合链价键和括号端键必须准确。实际匹配：无。

## 化学 第35章 · 35.2 高分子化合物的结构

ID：B05-CHEM35-35-2；优先级：P0；状态：not_produced。

用途：比较线型支链交联及空间结构；由连接与链运动预测性能并说明条件。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：弯曲线型链；甲基侧基；长支链；物理缠结；共价交联网络。

关系：交叉不自动成键；主链连续；交联点须合理价；稀密网络限制链运动不同。

文字：线型拓扑、侧基、支链、缠结、交联、非分子真实比例。

公式与单位：连接层次：主链/侧基/支链/链间交联，图中必须区分共价连接与链间靠近。；同化学家族内可推支化—堆积—结晶/密度趋势，但加工及分布仍会影响。；多官能单体可增加网络可能性；是否成胶/交联需转化与配比等条件。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第35章《有机高分子化合物》真实小节35.2《高分子化合物的结构》制作《线型支链交联的结构区别》教学图。学习目的：比较线型支链交联及空间结构；由连接与链运动预测性能并说明条件。本图是有条件的科学模型，非实测图或官方考题。必须出现：弯曲线型链；甲基侧基；长支链；物理缠结；共价交联网络。必须保持关系：交叉不自动成键；主链连续；交联点须合理价；稀密网络限制链运动不同。中文标签逐字采用：线型拓扑、侧基、支链、缠结、交联、非分子真实比例。公式及条件：连接层次：主链/侧基/支链/链间交联，图中必须区分共价连接与链间靠近。；同化学家族内可推支化—堆积—结晶/密度趋势，但加工及分布仍会影响。；多官能单体可增加网络可能性；是否成胶/交联需转化与配比等条件。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 35, authentic subsection 35.2. Display the original Chinese title exactly: 线型支链交联的结构区别. Topic-specific scientific requirements and instructional purpose: Draw a curved unbranched chain, pendant methyl groups, true long-chain branches, physical entanglement and covalent crosslinks as distinct models. Do not add a bond at every drawn crossing. Mark crosslink density qualitatively and avoid claiming denser networks universally improve softness or recyclability. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 弯曲线型链；甲基侧基；长支链；物理缠结；共价交联网络. Preserve the following Chinese label strings exactly: 线型拓扑、侧基、支链、缠结、交联、非分子真实比例. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 连接层次：主链/侧基/支链/链间交联，图中必须区分共价连接与链间靠近。；同化学家族内可推支化—堆积—结晶/密度趋势，但加工及分布仍会影响。；多官能单体可增加网络可能性；是否成胶/交联需转化与配比等条件。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：交叉不自动成键；主链连续；交联点须合理价；稀密网络限制链运动不同。不得把高分子化合物的结构画成另一知识主题；不得改动线型拓扑、侧基、支链、缠结、交联、非分子真实比例的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 交叉不自动成键
- 主链连续
- 交联点须合理价
- 稀密网络限制链运动不同
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/organic-chemistry/pages/31-7-polymer-structure-and-physical-properties

旧图复用：暂无对应旧图；结构示意必须区分交叉与成键。实际匹配：无。

## 化学 第35章 · 35.3 高分子化合物的物理性质

ID：B05-CHEM35-35-3；优先级：P0；状态：not_produced。

用途：由链运动与结晶解释热机械和溶胀性质；区分玻璃转变熔融及比较指标。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：T_g/T_m温标；无定形/晶区示意；不同截面试条；交联溶胀；测试条件框。

关系：T_g不等于T_m；F/A比较25与10MPa；保形溶胀非均一溶解；热塑与密交联不同。

文字：T_g、T_m、σ=F/A、溶胀、温度/时间/配方。

公式与单位：T_g为无定形链段运动变化的转变，不等于所有材料T_m。；简单拉伸名义应力σ=F/A；1 N/mm²=1 MPa，需同测试口径。；溶胀比需定义是质量或体积口径，吸液不等于全部网络分子溶解。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第35章《有机高分子化合物》真实小节35.3《高分子化合物的物理性质》制作《聚合物热转变与性能口径》教学图。学习目的：由链运动与结晶解释热机械和溶胀性质；区分玻璃转变熔融及比较指标。本图是有条件的科学模型，非实测图或官方考题。必须出现：T_g/T_m温标；无定形/晶区示意；不同截面试条；交联溶胀；测试条件框。必须保持关系：T_g不等于T_m；F/A比较25与10MPa；保形溶胀非均一溶解；热塑与密交联不同。中文标签逐字采用：T_g、T_m、σ=F/A、溶胀、温度/时间/配方。公式及条件：T_g为无定形链段运动变化的转变，不等于所有材料T_m。；简单拉伸名义应力σ=F/A；1 N/mm²=1 MPa，需同测试口径。；溶胀比需定义是质量或体积口径，吸液不等于全部网络分子溶解。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 35, authentic subsection 35.3. Display the original Chinese title exactly: 聚合物热转变与性能口径. Topic-specific scientific requirements and instructional purpose: Distinguish glass transition from crystalline melting, with separate amorphous and crystalline regions. Compare tensile specimens by50N/2mm²=25MPa versus100N/10mm²=10MPa, and show solvent swelling of a connected network without depicting complete dissolution. Label time, temperature and formulation limits. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: T_g/T_m温标；无定形/晶区示意；不同截面试条；交联溶胀；测试条件框. Preserve the following Chinese label strings exactly: T_g、T_m、σ=F/A、溶胀、温度/时间/配方. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: T_g为无定形链段运动变化的转变，不等于所有材料T_m。；简单拉伸名义应力σ=F/A；1 N/mm²=1 MPa，需同测试口径。；溶胀比需定义是质量或体积口径，吸液不等于全部网络分子溶解。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：T_g不等于T_m；F/A比较25与10MPa；保形溶胀非均一溶解；热塑与密交联不同。不得把高分子化合物的物理性质画成另一知识主题；不得改动T_g、T_m、σ=F/A、溶胀、温度/时间/配方的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- T_g不等于T_m
- F/A比较25与10MPa
- 保形溶胀非均一溶解
- 热塑与密交联不同
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/organic-chemistry/pages/31-7-polymer-structure-and-physical-properties

旧图复用：暂无对应旧图；温度标尺和数据须准确。实际匹配：无。

## 化学 第35章 · 35.4.1 加成聚合反应

ID：B05-CHEM35-35-4-1；优先级：P0；状态：not_produced。

用途：由单体双键写价键正确的重复结构；用计量与条件区分加成聚合和简单加成。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：乙烯/氯乙烯/丙烯单体；对应重复结构；主链端键；侧基；质量收支。

关系：C=C改主链单键；Cl和CH₃保留；每碳四价；不画脱水副产物。

文字：适当条件、n、连续主链、端基简写、加成不脱小分子。

公式与单位：nCH₂=CH₂→[—CH₂—CH₂—]ₙ（适当聚合条件，端基简写）。；nCH₂=CHCl→[—CH₂—CH(Cl)—]ₙ；nCH₂=CHCH₃→[—CH₂—CH(CH₃)—]ₙ。；理想加成聚合不脱小分子，M重复=M单体；M链≈nM重复需端基近似。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第35章《有机高分子化合物》真实小节35.4.1《加成聚合反应》制作《乙烯基加成聚合结构》教学图。学习目的：由单体双键写价键正确的重复结构；用计量与条件区分加成聚合和简单加成。本图是有条件的科学模型，非实测图或官方考题。必须出现：乙烯/氯乙烯/丙烯单体；对应重复结构；主链端键；侧基；质量收支。必须保持关系：C=C改主链单键；Cl和CH₃保留；每碳四价；不画脱水副产物。中文标签逐字采用：适当条件、n、连续主链、端基简写、加成不脱小分子。公式及条件：nCH₂=CH₂→[—CH₂—CH₂—]ₙ（适当聚合条件，端基简写）。；nCH₂=CHCl→[—CH₂—CH(Cl)—]ₙ；nCH₂=CHCH₃→[—CH₂—CH(CH₃)—]ₙ。；理想加成聚合不脱小分子，M重复=M单体；M链≈nM重复需端基近似。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 35, authentic subsection 35.4.1. Display the original Chinese title exactly: 乙烯基加成聚合结构. Topic-specific scientific requirements and instructional purpose: Draw ethene, vinyl chloride and propene converting to correct polyethylene, PVC and polypropylene repeat units. Keep chlorine and methyl substituents, replace the participating double bond with the connected backbone, extend bonds through brackets and check carbon valence. Do not invent water byproducts in ideal addition polymerization. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 乙烯/氯乙烯/丙烯单体；对应重复结构；主链端键；侧基；质量收支. Preserve the following Chinese label strings exactly: 适当条件、n、连续主链、端基简写、加成不脱小分子. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: nCH₂=CH₂→[—CH₂—CH₂—]ₙ（适当聚合条件，端基简写）。；nCH₂=CHCl→[—CH₂—CH(Cl)—]ₙ；nCH₂=CHCH₃→[—CH₂—CH(CH₃)—]ₙ。；理想加成聚合不脱小分子，M重复=M单体；M链≈nM重复需端基近似。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：C=C改主链单键；Cl和CH₃保留；每碳四价；不画脱水副产物。不得把加成聚合反应画成另一知识主题；不得改动适当条件、n、连续主链、端基简写、加成不脱小分子的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- C=C改主链单键
- Cl和CH₃保留
- 每碳四价
- 不画脱水副产物
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/organic-chemistry/pages/31-1-chain-growth-polymers

旧图复用：暂无对应图；每个键及括号必须确定性绘制。实际匹配：无。

## 化学 第35章 · 35.4.2 缩合聚合反应

ID：B05-CHEM35-35-4-2；优先级：P0；状态：not_produced。

用途：由官能团连接写聚酯聚酰胺；区分重复单元近似与有限链脱水数。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：二酸二醇聚酯；二酸二胺聚酰胺；水脱除；10对开放链端基；重复近似框。

关系：酯与酰胺原子正确；20单体19连接；10对Mr2278非2260精确值；端基H/OH保留。

文字：C=O、—COO—、—CONH—、2n−1水、226n+18、高n近似。

公式与单位：二酸+二醇→聚酯（酯连接）+相应H₂O；二酸+二胺→聚酰胺（酰胺连接）+H₂O。；己二酸146+己二胺116−2H₂O36=重复单元226（题取近似式量）。；n对单体成一条无环开放链：连接2n−1，水2n−1，链Mr=226n+18；若多链/成环须改计数。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第35章《有机高分子化合物》真实小节35.4.2《缩合聚合反应》制作《缩聚连接与端基精确计数》教学图。学习目的：由官能团连接写聚酯聚酰胺；区分重复单元近似与有限链脱水数。本图是有条件的科学模型，非实测图或官方考题。必须出现：二酸二醇聚酯；二酸二胺聚酰胺；水脱除；10对开放链端基；重复近似框。必须保持关系：酯与酰胺原子正确；20单体19连接；10对Mr2278非2260精确值；端基H/OH保留。中文标签逐字采用：C=O、—COO—、—CONH—、2n−1水、226n+18、高n近似。公式及条件：二酸+二醇→聚酯（酯连接）+相应H₂O；二酸+二胺→聚酰胺（酰胺连接）+H₂O。；己二酸146+己二胺116−2H₂O36=重复单元226（题取近似式量）。；n对单体成一条无环开放链：连接2n−1，水2n−1，链Mr=226n+18；若多链/成环须改计数。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 35, authentic subsection 35.4.2. Display the original Chinese title exactly: 缩聚连接与端基精确计数. Topic-specific scientific requirements and instructional purpose: Draw valence-correct polyester and polyamide links with every carbonyl oxygen retained. Contrast repeat-unit shorthand with a finite open chain of10 diacid and10 diamine molecules:19 water molecules lost and mass2278 using146/116/18, not an exact2260. Show terminal H/OH groups and state assumptions excluding rings and multiple chains. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 二酸二醇聚酯；二酸二胺聚酰胺；水脱除；10对开放链端基；重复近似框. Preserve the following Chinese label strings exactly: C=O、—COO—、—CONH—、2n−1水、226n+18、高n近似. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 二酸+二醇→聚酯（酯连接）+相应H₂O；二酸+二胺→聚酰胺（酰胺连接）+H₂O。；己二酸146+己二胺116−2H₂O36=重复单元226（题取近似式量）。；n对单体成一条无环开放链：连接2n−1，水2n−1，链Mr=226n+18；若多链/成环须改计数。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：酯与酰胺原子正确；20单体19连接；10对Mr2278非2260精确值；端基H/OH保留。不得把缩合聚合反应画成另一知识主题；不得改动C=O、—COO—、—CONH—、2n−1水、226n+18、高n近似的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 酯与酰胺原子正确
- 20单体19连接
- 10对Mr2278非2260精确值
- 端基H/OH保留
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/organic-chemistry/pages/31-4-step-growth-polymers

旧图复用：暂无对应图；必须逐原子核价、端基与小分子数。实际匹配：无。

## 化学 第35章 · 35.5.1 天然橡胶

ID：B05-CHEM35-35-5-1；优先级：P0；状态：not_produced。

用途：联系异戊二烯cis-1,4结构与弹性；区分乳胶凝聚聚合和硫化交联。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：异戊二烯；cis-1,4重复；卷曲伸展链；乳胶颗粒水相；通用硫交联。

关系：每重复保留一C=C；凝聚前已有长链；交联不画超价或唯一产物；卷曲非主链断裂。

文字：C₅H₈、cis-1,4、干胶含量、凝聚≠聚合、交联示意非唯一结构。

公式与单位：异戊二烯CH₂=C(CH₃)—CH=CH₂，1,4重复片段—CH₂—C(CH₃)=CH—CH₂—。；加成重复式量C₅H₈≈68；M链≈68n忽略端基。；干胶质量≈乳胶质量×题给干胶质量分数，分散水不是橡胶链组成。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第35章《有机高分子化合物》真实小节35.5.1《天然橡胶》制作《天然橡胶结构与硫化》教学图。学习目的：联系异戊二烯cis-1,4结构与弹性；区分乳胶凝聚聚合和硫化交联。本图是有条件的科学模型，非实测图或官方考题。必须出现：异戊二烯；cis-1,4重复；卷曲伸展链；乳胶颗粒水相；通用硫交联。必须保持关系：每重复保留一C=C；凝聚前已有长链；交联不画超价或唯一产物；卷曲非主链断裂。中文标签逐字采用：C₅H₈、cis-1,4、干胶含量、凝聚≠聚合、交联示意非唯一结构。公式及条件：异戊二烯CH₂=C(CH₃)—CH=CH₂，1,4重复片段—CH₂—C(CH₃)=CH—CH₂—。；加成重复式量C₅H₈≈68；M链≈68n忽略端基。；干胶质量≈乳胶质量×题给干胶质量分数，分散水不是橡胶链组成。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 35, authentic subsection 35.5.1. Display the original Chinese title exactly: 天然橡胶结构与硫化. Topic-specific scientific requirements and instructional purpose: Draw isoprene and the cis-1,4 polyisoprene repeat retaining one C=C per repeat. Separate latex particle coagulation from polymer formation and from vulcanization. Show only chemically justified or explicitly generic crosslink bridges, with no overvalent atoms or claim of one universal sulfur-crosslink structure. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 异戊二烯；cis-1,4重复；卷曲伸展链；乳胶颗粒水相；通用硫交联. Preserve the following Chinese label strings exactly: C₅H₈、cis-1,4、干胶含量、凝聚≠聚合、交联示意非唯一结构. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 异戊二烯CH₂=C(CH₃)—CH=CH₂，1,4重复片段—CH₂—C(CH₃)=CH—CH₂—。；加成重复式量C₅H₈≈68；M链≈68n忽略端基。；干胶质量≈乳胶质量×题给干胶质量分数，分散水不是橡胶链组成。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：每重复保留一C=C；凝聚前已有长链；交联不画超价或唯一产物；卷曲非主链断裂。不得把天然橡胶画成另一知识主题；不得改动C₅H₈、cis-1,4、干胶含量、凝聚≠聚合、交联示意非唯一结构的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 每重复保留一C=C
- 凝聚前已有长链
- 交联不画超价或唯一产物
- 卷曲非主链断裂
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/organic-chemistry/pages/14-6-diene-polymers-natural-and-synthetic-rubbers

旧图复用：暂无对应正确图；cis连接及硫桥须专项审核。实际匹配：无。

## 化学 第35章 · 35.5.2 合成橡胶

ID：B05-CHEM35-35-5-2；优先级：P0；状态：not_produced。

用途：由单体说明常见合成橡胶结构来源；用共聚组成和性能数据选择材料。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：丁二烯；苯乙烯；丙烯腈；氯丁二烯；统计共聚链；性能对照表。

关系：C≡N不画C≡C；Cl侧基保留；统计链不伪装严格交替；3mol54+1mol104=266g。

文字：丁苯、丁腈、氯丁、摩尔比≠质量比、条件性性能。

公式与单位：丁苯示例单体：1,3-丁二烯C₄H₆（Mr54）+苯乙烯C₈H₈（Mr104）。；完全进入理想加成共聚物时m聚≈ΣnᵢMᵢ；摩尔分数与质量分数一般不同。；丙烯腈CH₂=CH—C≡N含腈基，不属于只含C/H的炔烃；氯丁单体Cl不能丢。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第35章《有机高分子化合物》真实小节35.5.2《合成橡胶》制作《合成橡胶的单体与共聚》教学图。学习目的：由单体说明常见合成橡胶结构来源；用共聚组成和性能数据选择材料。本图是有条件的科学模型，非实测图或官方考题。必须出现：丁二烯；苯乙烯；丙烯腈；氯丁二烯；统计共聚链；性能对照表。必须保持关系：C≡N不画C≡C；Cl侧基保留；统计链不伪装严格交替；3mol54+1mol104=266g。中文标签逐字采用：丁苯、丁腈、氯丁、摩尔比≠质量比、条件性性能。公式及条件：丁苯示例单体：1,3-丁二烯C₄H₆（Mr54）+苯乙烯C₈H₈（Mr104）。；完全进入理想加成共聚物时m聚≈ΣnᵢMᵢ；摩尔分数与质量分数一般不同。；丙烯腈CH₂=CH—C≡N含腈基，不属于只含C/H的炔烃；氯丁单体Cl不能丢。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 35, authentic subsection 35.5.2. Display the original Chinese title exactly: 合成橡胶的单体与共聚. Topic-specific scientific requirements and instructional purpose: Draw correct butadiene, styrene, acrylonitrile and chloroprene structures, retaining CN and Cl substituents. Mark copolymer sequence as statistical unless explicitly controlled. Show3 mol of54 plus1 mol of104 giving266 g and39.1% styrene-derived mass, not25% mass. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 丁二烯；苯乙烯；丙烯腈；氯丁二烯；统计共聚链；性能对照表. Preserve the following Chinese label strings exactly: 丁苯、丁腈、氯丁、摩尔比≠质量比、条件性性能. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 丁苯示例单体：1,3-丁二烯C₄H₆（Mr54）+苯乙烯C₈H₈（Mr104）。；完全进入理想加成共聚物时m聚≈ΣnᵢMᵢ；摩尔分数与质量分数一般不同。；丙烯腈CH₂=CH—C≡N含腈基，不属于只含C/H的炔烃；氯丁单体Cl不能丢。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：C≡N不画C≡C；Cl侧基保留；统计链不伪装严格交替；3mol54+1mol104=266g。不得把合成橡胶画成另一知识主题；不得改动丁苯、丁腈、氯丁、摩尔比≠质量比、条件性性能的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- C≡N不画C≡C
- Cl侧基保留
- 统计链不伪装严格交替
- 3mol54+1mol104=266g
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/organic-chemistry/pages/14-6-diene-polymers-natural-and-synthetic-rubbers

旧图复用：暂无对应图；单体和重复结构逐原子核验。实际匹配：无。

## 化学 第35章 · 35.6 石油和合成高分子化合物

ID：B05-CHEM35-35-6；优先级：P1；状态：not_produced。

用途：追踪石油馏分到单体聚合物的变化层级；评价回收及生命周期声明的结构依据。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：原油混合物；馏分；裂化单体；聚合物产品；机械/化学/能源三路径；外部输入输出。

关系：分馏不画成自动裂化；材料与能源回收分开；PE不画酯水解；60%回收不画100%闭环。

文字：分离、化学转化、结构条件、生物基≠可降解、真实回收率。

公式与单位：分馏=按物性分离混合物；裂化/聚合=改变连接的化学过程。；简化裂化例C₁₀H₂₂→C₂H₄+C₈H₁₈，原子守恒但非唯一产物承诺。；回收路径分机械再加工、化学转化与能源回收；生物基来源不等于可降解性能。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中化学第35章《有机高分子化合物》真实小节35.6《石油和合成高分子化合物》制作《石油到聚合物及回收路径》教学图。学习目的：追踪石油馏分到单体聚合物的变化层级；评价回收及生命周期声明的结构依据。本图是有条件的科学模型，非实测图或官方考题。必须出现：原油混合物；馏分；裂化单体；聚合物产品；机械/化学/能源三路径；外部输入输出。必须保持关系：分馏不画成自动裂化；材料与能源回收分开；PE不画酯水解；60%回收不画100%闭环。中文标签逐字采用：分离、化学转化、结构条件、生物基≠可降解、真实回收率。公式及条件：分馏=按物性分离混合物；裂化/聚合=改变连接的化学过程。；简化裂化例C₁₀H₂₂→C₂H₄+C₈H₁₈，原子守恒但非唯一产物承诺。；回收路径分机械再加工、化学转化与能源回收；生物基来源不等于可降解性能。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high chemistry teaching diagram for chapter 35, authentic subsection 35.6. Display the original Chinese title exactly: 石油到聚合物及回收路径. Topic-specific scientific requirements and instructional purpose: Trace crude-oil mixture through physical fractionation, chemical cracking, monomer purification and polymerization. Separate mechanical recycling, chemical conversion and energy recovery, with explicit losses and external inputs. Do not depict polyethylene as an ester undergoing ordinary hydrolysis or equate bio-based feedstock with biodegradability. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 原油混合物；馏分；裂化单体；聚合物产品；机械/化学/能源三路径；外部输入输出. Preserve the following Chinese label strings exactly: 分离、化学转化、结构条件、生物基≠可降解、真实回收率. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 分馏=按物性分离混合物；裂化/聚合=改变连接的化学过程。；简化裂化例C₁₀H₂₂→C₂H₄+C₈H₁₈，原子守恒但非唯一产物承诺。；回收路径分机械再加工、化学转化与能源回收；生物基来源不等于可降解性能。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：分馏不画成自动裂化；材料与能源回收分开；PE不画酯水解；60%回收不画100%闭环。不得把石油和合成高分子化合物画成另一知识主题；不得改动分离、化学转化、结构条件、生物基≠可降解、真实回收率的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 分馏不画成自动裂化
- 材料与能源回收分开
- PE不画酯水解
- 60%回收不画100%闭环
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://elearning.dongzong.my/pluginfile.php/77540/mod_resource/content/1/高中化学.pdf
- https://openstax.org/books/organic-chemistry/pages/31-chemistry-matters-degradable-polymers

旧图复用：暂无完整图；流程需有收支出口不画永动闭环。实际匹配：无。

## 数学 第1章 · 1.1 直角坐标系与距离公式

ID：B05-MATH01-1-1；优先级：P=0；状态：not_produced。

用途：用坐标和距离描述点的位置；由距离方程求点并核几何条件。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：A(−2,1)；B(4,9)；直角投影点；横差6；纵差8；距离10。

关系：投影点同一横/纵坐标；直角边6与8；斜边10；坐标比例一致。

文字：x、y、Δx=6、Δy=8、AB=10、非负距离。

公式与单位：d(A,B)=√[(x₂−x₁)²+(y₂−y₁)²]≥0，正交轴且单位相容。；同横坐标时d=|y₂−y₁|；同纵坐标时d=|x₂−x₁|。；d(P,A)=d(P,B)可等价平方，展开后再按P的轴/区间限制筛选。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第1章《直角坐标系与直线》真实小节1.1《直角坐标系与距离公式》制作《距离公式的正交分解》教学图。学习目的：用坐标和距离描述点的位置；由距离方程求点并核几何条件。本图是有条件的科学模型，非实测图或官方考题。必须出现：A(−2,1)；B(4,9)；直角投影点；横差6；纵差8；距离10。必须保持关系：投影点同一横/纵坐标；直角边6与8；斜边10；坐标比例一致。中文标签逐字采用：x、y、Δx=6、Δy=8、AB=10、非负距离。公式及条件：d(A,B)=√[(x₂−x₁)²+(y₂−y₁)²]≥0，正交轴且单位相容。；同横坐标时d=|y₂−y₁|；同纵坐标时d=|x₂−x₁|。；d(P,A)=d(P,B)可等价平方，展开后再按P的轴/区间限制筛选。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 1, authentic subsection 1.1. Display the original Chinese title exactly: 距离公式的正交分解. Topic-specific scientific requirements and instructional purpose: Plot A(-2,1) and B(4,9) with equal unit scales, construct horizontal and vertical projections of lengths 6 and 8, and label the hypotenuse 10. Distinguish signed coordinate differences from nonnegative Euclidean distance. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: A(−2,1)；B(4,9)；直角投影点；横差6；纵差8；距离10. Preserve the following Chinese label strings exactly: x、y、Δx=6、Δy=8、AB=10、非负距离. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: d(A,B)=√[(x₂−x₁)²+(y₂−y₁)²]≥0，正交轴且单位相容。；同横坐标时d=|y₂−y₁|；同纵坐标时d=|x₂−x₁|。；d(P,A)=d(P,B)可等价平方，展开后再按P的轴/区间限制筛选。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：投影点同一横/纵坐标；直角边6与8；斜边10；坐标比例一致。不得把直角坐标系与距离公式画成另一知识主题；不得改动x、y、Δx=6、Δy=8、AB=10、非负距离的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 投影点同一横/纵坐标
- 直角边6与8
- 斜边10
- 坐标比例一致
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/2-1-the-rectangular-coordinate-systems-and-graphs

旧图复用：暂无对应旧图；坐标与比例需数学绘图库。实际匹配：无。

## 数学 第1章 · 1.2 定比分点

ID：B05-MATH01-1-2；优先级：P=0；状态：not_produced。

用途：由线性插值推导内分与外分坐标；反求端点并区分中点重心和无有限外分。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：A(1,2)；B(7,8)；内分P(3,4)；外分P(13,14)；A侧外分。

关系：内分1:2靠A；外分2:1越B；权重交叉；m=n外分无有限点。

文字：AP:PB、内分、外分、m,n>0、m≠n。

公式与单位：内分AP:PB=m:n：P=(nA+mB)/(m+n)，m,n>0。；外分同长度比：P=(mB−nA)/(m−n)，m≠n；端点不同。；中点M=(A+B)/2；三角形重心G=(A+B+C)/3，可由中线2:1推导。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第1章《直角坐标系与直线》真实小节1.2《定比分点》制作《内分与外分的权重》教学图。学习目的：由线性插值推导内分与外分坐标；反求端点并区分中点重心和无有限外分。本图是有条件的科学模型，非实测图或官方考题。必须出现：A(1,2)；B(7,8)；内分P(3,4)；外分P(13,14)；A侧外分。必须保持关系：内分1:2靠A；外分2:1越B；权重交叉；m=n外分无有限点。中文标签逐字采用：AP:PB、内分、外分、m,n>0、m≠n。公式及条件：内分AP:PB=m:n：P=(nA+mB)/(m+n)，m,n>0。；外分同长度比：P=(mB−nA)/(m−n)，m≠n；端点不同。；中点M=(A+B)/2；三角形重心G=(A+B+C)/3，可由中线2:1推导。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 1, authentic subsection 1.2. Display the original Chinese title exactly: 内分与外分的权重. Topic-specific scientific requirements and instructional purpose: Place A(1,2), B(7,8), internal P(3,4) with AP:PB=1:2 and external P(13,14) with ratio 2:1 on the same line. Show crossed coordinate weights and distinguish an A-side external point; never draw an equal-ratio finite external division. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: A(1,2)；B(7,8)；内分P(3,4)；外分P(13,14)；A侧外分. Preserve the following Chinese label strings exactly: AP:PB、内分、外分、m,n>0、m≠n. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 内分AP:PB=m:n：P=(nA+mB)/(m+n)，m,n>0。；外分同长度比：P=(mB−nA)/(m−n)，m≠n；端点不同。；中点M=(A+B)/2；三角形重心G=(A+B+C)/3，可由中线2:1推导。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：内分1:2靠A；外分2:1越B；权重交叉；m=n外分无有限点。不得把定比分点画成另一知识主题；不得改动AP:PB、内分、外分、m,n>0、m≠n的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 内分1:2靠A
- 外分2:1越B
- 权重交叉
- m=n外分无有限点
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/2-1-the-rectangular-coordinate-systems-and-graphs

旧图复用：暂无对应旧图；点须按同一标尺精确定位。实际匹配：无。

## 数学 第1章 · 1.3 多边形的面积

ID：B05-MATH01-1-3；优先级：P=0；状态：not_produced。

用途：用坐标推导三角形及多边形面积；保留顶点顺序和绝对值处理参数。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：三角形(1,1)(5,1)(2,4)；底高；有序四边形；自交对照；k正负两点。

关系：三角形面积6；四边形面积12；自交抵消不代表正方形面积0；高用绝对值。

文字：1/2、绝对值、闭合边、边界顺序、平方单位。

公式与单位：S△ABC=| (x₂−x₁)(y₃−y₁)−(y₂−y₁)(x₃−x₁) |/2。；简单多边形按边界顺序：S=|Σ(xᵢyᵢ₊₁−yᵢxᵢ₊₁)|/2，最后点连回第一点。；面积0是共线/退化警示；绝对值方程需按两符号及题设位置筛选。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第1章《直角坐标系与直线》真实小节1.3《多边形的面积》制作《坐标面积与边界顺序》教学图。学习目的：用坐标推导三角形及多边形面积；保留顶点顺序和绝对值处理参数。本图是有条件的科学模型，非实测图或官方考题。必须出现：三角形(1,1)(5,1)(2,4)；底高；有序四边形；自交对照；k正负两点。必须保持关系：三角形面积6；四边形面积12；自交抵消不代表正方形面积0；高用绝对值。中文标签逐字采用：1/2、绝对值、闭合边、边界顺序、平方单位。公式及条件：S△ABC=| (x₂−x₁)(y₃−y₁)−(y₂−y₁)(x₃−x₁) |/2。；简单多边形按边界顺序：S=|Σ(xᵢyᵢ₊₁−yᵢxᵢ₊₁)|/2，最后点连回第一点。；面积0是共线/退化警示；绝对值方程需按两符号及题设位置筛选。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 1, authentic subsection 1.3. Display the original Chinese title exactly: 坐标面积与边界顺序. Topic-specific scientific requirements and instructional purpose: Plot triangle (1,1),(5,1),(2,4) with base 4, height 3 and area 6. Show a boundary-ordered quadrilateral of area 12 and a separate self-intersecting counterexample. Preserve the absolute-value factor 1/2 and distinguish signed area from ordinary area. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 三角形(1,1)(5,1)(2,4)；底高；有序四边形；自交对照；k正负两点. Preserve the following Chinese label strings exactly: 1/2、绝对值、闭合边、边界顺序、平方单位. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: S△ABC=| (x₂−x₁)(y₃−y₁)−(y₂−y₁)(x₃−x₁) |/2。；简单多边形按边界顺序：S=|Σ(xᵢyᵢ₊₁−yᵢxᵢ₊₁)|/2，最后点连回第一点。；面积0是共线/退化警示；绝对值方程需按两符号及题设位置筛选。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：三角形面积6；四边形面积12；自交抵消不代表正方形面积0；高用绝对值。不得把多边形的面积画成另一知识主题；不得改动1/2、绝对值、闭合边、边界顺序、平方单位的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 三角形面积6
- 四边形面积12
- 自交抵消不代表正方形面积0
- 高用绝对值
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/precalculus-2e/pages/9-8-solving-systems-with-cramers-rule

旧图复用：暂无对应旧图；顶点与区域应精确绘制。实际匹配：无。

## 数学 第1章 · 1.4 直线的斜率

ID：B05-MATH01-1-4；优先级：P=0；状态：not_produced。

用途：用坐标差与倾斜角解释斜率；分类处理平行垂直和竖直线。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：A(1,2)到B(4,8)；水平线；竖直线；斜率2/3及−3/2；同斜率重合/平行。

关系：Δy=6/Δx=3=2；竖直无定义水平0；有限非零垂直斜率乘积−1。

文字：Δx、Δy、m、无定义、平行≠必不同。

公式与单位：m=(y₂−y₁)/(x₂−x₁)，要求x₂≠x₁；竖直无实数斜率，水平m=0。；非竖直线平行需m₁=m₂且不重合；互垂直（有限斜率情境）m₁m₂=−1。；三点共线可用(x₂−x₁)(y₃−y₁)=(x₃−x₁)(y₂−y₁)，并注意互异与退化。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第1章《直角坐标系与直线》真实小节1.4《直线的斜率》制作《斜率及例外分类》教学图。学习目的：用坐标差与倾斜角解释斜率；分类处理平行垂直和竖直线。本图是有条件的科学模型，非实测图或官方考题。必须出现：A(1,2)到B(4,8)；水平线；竖直线；斜率2/3及−3/2；同斜率重合/平行。必须保持关系：Δy=6/Δx=3=2；竖直无定义水平0；有限非零垂直斜率乘积−1。中文标签逐字采用：Δx、Δy、m、无定义、平行≠必不同。公式及条件：m=(y₂−y₁)/(x₂−x₁)，要求x₂≠x₁；竖直无实数斜率，水平m=0。；非竖直线平行需m₁=m₂且不重合；互垂直（有限斜率情境）m₁m₂=−1。；三点共线可用(x₂−x₁)(y₃−y₁)=(x₃−x₁)(y₂−y₁)，并注意互异与退化。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 1, authentic subsection 1.4. Display the original Chinese title exactly: 斜率及例外分类. Topic-specific scientific requirements and instructional purpose: Plot a rise of 6 over a run of 3, giving slope 2. Clearly separate horizontal slope zero from undefined vertical slope. Show perpendicular finite slopes 2/3 and -3/2 and distinguish equal-slope parallel lines from coincident lines using labelled equal scales. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: A(1,2)到B(4,8)；水平线；竖直线；斜率2/3及−3/2；同斜率重合/平行. Preserve the following Chinese label strings exactly: Δx、Δy、m、无定义、平行≠必不同. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: m=(y₂−y₁)/(x₂−x₁)，要求x₂≠x₁；竖直无实数斜率，水平m=0。；非竖直线平行需m₁=m₂且不重合；互垂直（有限斜率情境）m₁m₂=−1。；三点共线可用(x₂−x₁)(y₃−y₁)=(x₃−x₁)(y₂−y₁)，并注意互异与退化。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：Δy=6/Δx=3=2；竖直无定义水平0；有限非零垂直斜率乘积−1。不得把直线的斜率画成另一知识主题；不得改动Δx、Δy、m、无定义、平行≠必不同的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- Δy=6/Δx=3=2
- 竖直无定义水平0
- 有限非零垂直斜率乘积−1
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/4-1-linear-functions

旧图复用：暂无对应旧图；同坐标尺度绘制，不用视觉角替数值。实际匹配：无。

## 数学 第1章 · 1.5 直线方程式

ID：B05-MATH01-1-5；优先级：P=0；状态：not_produced。

用途：按已知条件选择直线表达形式；检查竖直线及截距公式的适用条件。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：点斜式图；竖直x=5；截距(4,0)(0,6)；过原点线；一般式。

关系：竖直不写有限m；截距式要求非零；非零倍数同一线。

文字：Ax+By+C=0、(A,B)≠(0,0)、y−y₀=m(x−x₀)、x/a+y/b=1。

公式与单位：一般式Ax+By+C=0，(A,B)≠(0,0)。；点斜式y−y₀=m(x−x₀)，竖直例外x=x₀。；两点交叉式适用于不同两点；截距式x/a+y/b=1要求a,b非零有限。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第1章《直角坐标系与直线》真实小节1.5《直线方程式》制作《直线方程形式与适用条件》教学图。学习目的：按已知条件选择直线表达形式；检查竖直线及截距公式的适用条件。本图是有条件的科学模型，非实测图或官方考题。必须出现：点斜式图；竖直x=5；截距(4,0)(0,6)；过原点线；一般式。必须保持关系：竖直不写有限m；截距式要求非零；非零倍数同一线。中文标签逐字采用：Ax+By+C=0、(A,B)≠(0,0)、y−y₀=m(x−x₀)、x/a+y/b=1。公式及条件：一般式Ax+By+C=0，(A,B)≠(0,0)。；点斜式y−y₀=m(x−x₀)，竖直例外x=x₀。；两点交叉式适用于不同两点；截距式x/a+y/b=1要求a,b非零有限。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 1, authentic subsection 1.5. Display the original Chinese title exactly: 直线方程形式与适用条件. Topic-specific scientific requirements and instructional purpose: Compare point-slope, general and intercept forms with accurate coordinate diagrams. Include x=5 as a vertical exception, a line through (4,0),(0,6), and a line through the origin where nonzero-intercept form is invalid. State that A and B cannot both be zero. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 点斜式图；竖直x=5；截距(4,0)(0,6)；过原点线；一般式. Preserve the following Chinese label strings exactly: Ax+By+C=0、(A,B)≠(0,0)、y−y₀=m(x−x₀)、x/a+y/b=1. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 一般式Ax+By+C=0，(A,B)≠(0,0)。；点斜式y−y₀=m(x−x₀)，竖直例外x=x₀。；两点交叉式适用于不同两点；截距式x/a+y/b=1要求a,b非零有限。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：竖直不写有限m；截距式要求非零；非零倍数同一线。不得把直线方程式画成另一知识主题；不得改动Ax+By+C=0、(A,B)≠(0,0)、y−y₀=m(x−x₀)、x/a+y/b=1的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 竖直不写有限m
- 截距式要求非零
- 非零倍数同一线
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/4-1-linear-functions

旧图复用：暂无对应图；直线与点准确绘制。实际匹配：无。

## 数学 第1章 · 1.6 两条直线的交点

ID：B05-MATH01-1-6；优先级：P=0；状态：not_produced。

用途：以联立方程判交点平行或重合；对参数退化分类并给完整坐标。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：相交(2,3)；不同平行；重合线；参数消元分支。

关系：D非零唯一；D0后查常数比例；k=2,c=2重合而c≠2平行。

文字：D=A₁B₂−A₂B₁、唯一交点、无交点、无限公共点、先分除数0。

公式与单位：D=A₁B₂−A₂B₁；D≠0有唯一交点。；D=0时再查完整系数是否成同一非零比例：是则重合，否则不同平行。；参数消元需先分除数是否0；0=非零无解，0=0需查看剩余独立约束。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第1章《直角坐标系与直线》真实小节1.6《两条直线的交点》制作《两直线三种位置与参数》教学图。学习目的：以联立方程判交点平行或重合；对参数退化分类并给完整坐标。本图是有条件的科学模型，非实测图或官方考题。必须出现：相交(2,3)；不同平行；重合线；参数消元分支。必须保持关系：D非零唯一；D0后查常数比例；k=2,c=2重合而c≠2平行。中文标签逐字采用：D=A₁B₂−A₂B₁、唯一交点、无交点、无限公共点、先分除数0。公式及条件：D=A₁B₂−A₂B₁；D≠0有唯一交点。；D=0时再查完整系数是否成同一非零比例：是则重合，否则不同平行。；参数消元需先分除数是否0；0=非零无解，0=0需查看剩余独立约束。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 1, authentic subsection 1.6. Display the original Chinese title exactly: 两直线三种位置与参数. Topic-specific scientific requirements and instructional purpose: Draw three accurately labelled cases: intersecting lines at (2,3), distinct parallel lines and coincident lines. Explain D=A1B2-A2B1, then separately classify the D=0 cases. Include parameter equation (k-2)x=c-2 without dividing before handling k=2. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 相交(2,3)；不同平行；重合线；参数消元分支. Preserve the following Chinese label strings exactly: D=A₁B₂−A₂B₁、唯一交点、无交点、无限公共点、先分除数0. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: D=A₁B₂−A₂B₁；D≠0有唯一交点。；D=0时再查完整系数是否成同一非零比例：是则重合，否则不同平行。；参数消元需先分除数是否0；0=非零无解，0=0需查看剩余独立约束。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：D非零唯一；D0后查常数比例；k=2,c=2重合而c≠2平行。不得把两条直线的交点画成另一知识主题；不得改动D=A₁B₂−A₂B₁、唯一交点、无交点、无限公共点、先分除数0的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- D非零唯一
- D0后查常数比例
- k=2,c=2重合而c≠2平行
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/11-1-systems-of-linear-equations-two-variables

旧图复用：暂无对应旧图；不同位置须与所示方程一致。实际匹配：无。

## 数学 第1章 · 1.7 点到直线的距离

ID：B05-MATH01-1-7；优先级：P=0；状态：not_produced。

用途：推导并使用垂直距离和垂足公式；统一直线系数后求平行线距离并核绝对值。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：P(3,4)；直线3x+4y−5=0；H(3/5,4/5)；垂线PH；平行线统一系数。

关系：PH沿法向3:4；H在线；PH长4；系数倍乘不改变距离。

文字：d=4、垂足H、直角标、|Ax₀+By₀+C|、√(A²+B²)。

公式与单位：d(P,l)=|Ax₀+By₀+C|/√(A²+B²)，(A,B)≠(0,0)。；t=(Ax₀+By₀+C)/(A²+B²)，H=(x₀−tA,y₀−tB)。；平行线先统一A,B后，d=|C₂−C₁|/√(A²+B²)。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第1章《直角坐标系与直线》真实小节1.7《点到直线的距离》制作《点线距离与垂足》教学图。学习目的：推导并使用垂直距离和垂足公式；统一直线系数后求平行线距离并核绝对值。本图是有条件的科学模型，非实测图或官方考题。必须出现：P(3,4)；直线3x+4y−5=0；H(3/5,4/5)；垂线PH；平行线统一系数。必须保持关系：PH沿法向3:4；H在线；PH长4；系数倍乘不改变距离。中文标签逐字采用：d=4、垂足H、直角标、|Ax₀+By₀+C|、√(A²+B²)。公式及条件：d(P,l)=|Ax₀+By₀+C|/√(A²+B²)，(A,B)≠(0,0)。；t=(Ax₀+By₀+C)/(A²+B²)，H=(x₀−tA,y₀−tB)。；平行线先统一A,B后，d=|C₂−C₁|/√(A²+B²)。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 1, authentic subsection 1.7. Display the original Chinese title exactly: 点线距离与垂足. Topic-specific scientific requirements and instructional purpose: Plot P(3,4), line 3x+4y-5=0 and foot H(3/5,4/5) on equal scales. Draw PH perpendicular to the line with length 4 and normal direction ratio 3:4. Show that parallel-line constant differences require matching A and B first. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: P(3,4)；直线3x+4y−5=0；H(3/5,4/5)；垂线PH；平行线统一系数. Preserve the following Chinese label strings exactly: d=4、垂足H、直角标、|Ax₀+By₀+C|、√(A²+B²). Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: d(P,l)=|Ax₀+By₀+C|/√(A²+B²)，(A,B)≠(0,0)。；t=(Ax₀+By₀+C)/(A²+B²)，H=(x₀−tA,y₀−tB)。；平行线先统一A,B后，d=|C₂−C₁|/√(A²+B²)。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：PH沿法向3:4；H在线；PH长4；系数倍乘不改变距离。不得把点到直线的距离画成另一知识主题；不得改动d=4、垂足H、直角标、|Ax₀+By₀+C|、√(A²+B²)的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- PH沿法向3:4
- H在线
- PH长4
- 系数倍乘不改变距离
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/2-1-the-rectangular-coordinate-systems-and-graphs

旧图复用：暂无对应图；垂足和直角必须精确定位。实际匹配：无。

## 数学 第2章 · 2.1 一元二次方程式的根的判别式

ID：B05-MATH02-2-1；优先级：P=0；状态：not_produced。

用途：由配方推导判别式与实根数；对参数先检次数再分类并回代。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：(2ax+b)²=Δ；三种Δ情境；参数a=0分支；抛物线与x轴。

关系：a≠0才用二次分类；Δ=0仅一个不同值；退化回原式。

文字：Δ=b²−4ac、两不同实根、二重实根、无实根、先查a=0。

公式与单位：a≠0时，配方得(2ax+b)²=Δ=b²−4ac。；Δ>0：两不同实根；Δ=0：二重实根；Δ<0：无实根。；x=(−b±√Δ)/(2a)；参数a=0需回原式另解。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第2章《一元二次方程式与二次函数》真实小节2.1《一元二次方程式的根的判别式》制作《判别式从配方到根数》教学图。学习目的：由配方推导判别式与实根数；对参数先检次数再分类并回代。本图是有条件的科学模型，非实测图或官方考题。必须出现：(2ax+b)²=Δ；三种Δ情境；参数a=0分支；抛物线与x轴。必须保持关系：a≠0才用二次分类；Δ=0仅一个不同值；退化回原式。中文标签逐字采用：Δ=b²−4ac、两不同实根、二重实根、无实根、先查a=0。公式及条件：a≠0时，配方得(2ax+b)²=Δ=b²−4ac。；Δ>0：两不同实根；Δ=0：二重实根；Δ<0：无实根。；x=(−b±√Δ)/(2a)；参数a=0需回原式另解。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 2, authentic subsection 2.1. Display the original Chinese title exactly: 判别式从配方到根数. Topic-specific scientific requirements and instructional purpose: Derive (2ax+b)^2=Delta and show the three real-root cases for a nonzero quadratic coefficient. Include a separate a=0 degeneration branch, distinguish a double root from two distinct roots, and do not infer root signs from Delta alone. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: (2ax+b)²=Δ；三种Δ情境；参数a=0分支；抛物线与x轴. Preserve the following Chinese label strings exactly: Δ=b²−4ac、两不同实根、二重实根、无实根、先查a=0. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: a≠0时，配方得(2ax+b)²=Δ=b²−4ac。；Δ>0：两不同实根；Δ=0：二重实根；Δ<0：无实根。；x=(−b±√Δ)/(2a)；参数a=0需回原式另解。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：a≠0才用二次分类；Δ=0仅一个不同值；退化回原式。不得把一元二次方程式的根的判别式画成另一知识主题；不得改动Δ=b²−4ac、两不同实根、二重实根、无实根、先查a=0的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- a≠0才用二次分类
- Δ=0仅一个不同值
- 退化回原式
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/2-5-quadratic-equations

旧图复用：暂无对应图；三类曲线坐标必须准确。实际匹配：无。

## 数学 第2章 · 2.2 一元二次方程式的根与系数的关系

ID：B05-MATH02-2-2；优先级：P=1；状态：not_produced。

用途：由因式展开推导根的和积；用对称式和实根条件处理新根与参数。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：a(x−α)(x−β)展开；S/P框；平方和；新根平移；参数交集。

关系：S=−b/a；P=c/a；S新=S+2；P新=P+S+1；正实根还需Δ条件。

文字：a≠0、S、P、倒数需P≠0、条件取交集。

公式与单位：S=α+β=−b/a，P=αβ=c/a（a≠0）。；α²+β²=S²−2P；αβ≠0时1/α+1/β=S/P。；新根α+1、β+1：S新=S+2，P新=P+S+1；方程y²−S新y+P新=0。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第2章《一元二次方程式与二次函数》真实小节2.2《一元二次方程式的根与系数的关系》制作《韦达关系与新根》教学图。学习目的：由因式展开推导根的和积；用对称式和实根条件处理新根与参数。本图是有条件的科学模型，非实测图或官方考题。必须出现：a(x−α)(x−β)展开；S/P框；平方和；新根平移；参数交集。必须保持关系：S=−b/a；P=c/a；S新=S+2；P新=P+S+1；正实根还需Δ条件。中文标签逐字采用：a≠0、S、P、倒数需P≠0、条件取交集。公式及条件：S=α+β=−b/a，P=αβ=c/a（a≠0）。；α²+β²=S²−2P；αβ≠0时1/α+1/β=S/P。；新根α+1、β+1：S新=S+2，P新=P+S+1；方程y²−S新y+P新=0。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 2, authentic subsection 2.2. Display the original Chinese title exactly: 韦达关系与新根. Topic-specific scientific requirements and instructional purpose: Derive the root sum -b/a and product c/a by expansion. Show symmetric expressions, the nonzero-product requirement for reciprocal roots, and shifted-root sums/products S+2 and P+S+1. Keep discriminant and sign conditions as a joint intersection. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: a(x−α)(x−β)展开；S/P框；平方和；新根平移；参数交集. Preserve the following Chinese label strings exactly: a≠0、S、P、倒数需P≠0、条件取交集. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: S=α+β=−b/a，P=αβ=c/a（a≠0）。；α²+β²=S²−2P；αβ≠0时1/α+1/β=S/P。；新根α+1、β+1：S新=S+2，P新=P+S+1；方程y²−S新y+P新=0。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：S=−b/a；P=c/a；S新=S+2；P新=P+S+1；正实根还需Δ条件。不得把一元二次方程式的根与系数的关系画成另一知识主题；不得改动a≠0、S、P、倒数需P≠0、条件取交集的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- S=−b/a
- P=c/a
- S新=S+2
- P新=P+S+1
- 正实根还需Δ条件
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/2-5-quadratic-equations

旧图复用：暂无对应旧图；代数关系图确定性排版。实际匹配：无。

## 数学 第2章 · 2.3 二次函数的图像与最值

ID：B05-MATH02-2-3；优先级：P=0；状态：not_produced。

用途：配方确定顶点开口与值域；在给定区间和参数条件下求真正最值。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：2(x−2)²−3图；受限区间；顶点区间外示例；参数t位置三段。

关系：顶点(2,−3)；闭区间比端点顶点；x²在(0,1)无取得最值。

文字：x、y、顶点、合法端点、最近点、空心/实心。

公式与单位：f=a(x+b/(2a))²−Δ/(4a)，a≠0；顶点(−b/(2a),−Δ/(4a))。；闭区间最值候选为合法端点及区间内顶点；开端点不能作为已取到点。；f=(x−t)²在[0,2]的最小值由t到该区间的最近距离平方得到。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第2章《一元二次方程式与二次函数》真实小节2.3《二次函数的图像与最值》制作《抛物线顶点与区间最值》教学图。学习目的：配方确定顶点开口与值域；在给定区间和参数条件下求真正最值。本图是有条件的科学模型，非实测图或官方考题。必须出现：2(x−2)²−3图；受限区间；顶点区间外示例；参数t位置三段。必须保持关系：顶点(2,−3)；闭区间比端点顶点；x²在(0,1)无取得最值。中文标签逐字采用：x、y、顶点、合法端点、最近点、空心/实心。公式及条件：f=a(x+b/(2a))²−Δ/(4a)，a≠0；顶点(−b/(2a),−Δ/(4a))。；闭区间最值候选为合法端点及区间内顶点；开端点不能作为已取到点。；f=(x−t)²在[0,2]的最小值由t到该区间的最近距离平方得到。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 2, authentic subsection 2.3. Display the original Chinese title exactly: 抛物线顶点与区间最值. Topic-specific scientific requirements and instructional purpose: Plot 2(x-2)^2-3 with vertex (2,-3) and equal labelled scales. Contrast unrestricted and restricted-domain extrema, including a vertex outside the interval and open endpoints. Show the closest-point cases for (x-t)^2 on [0,2]. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 2(x−2)²−3图；受限区间；顶点区间外示例；参数t位置三段. Preserve the following Chinese label strings exactly: x、y、顶点、合法端点、最近点、空心/实心. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: f=a(x+b/(2a))²−Δ/(4a)，a≠0；顶点(−b/(2a),−Δ/(4a))。；闭区间最值候选为合法端点及区间内顶点；开端点不能作为已取到点。；f=(x−t)²在[0,2]的最小值由t到该区间的最近距离平方得到。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：顶点(2,−3)；闭区间比端点顶点；x²在(0,1)无取得最值。不得把二次函数的图像与最值画成另一知识主题；不得改动x、y、顶点、合法端点、最近点、空心/实心的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 顶点(2,−3)
- 闭区间比端点顶点
- x²在(0,1)无取得最值
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/5-1-quadratic-functions

旧图复用：暂无对应图；曲线与端点必须数值绘制。实际匹配：无。

## 数学 第2章 · 2.4 一元二次函数的图像与直线的位置关系

ID：B05-MATH02-2-4；优先级：P=0；状态：not_produced。

用途：把交点问题转为二次方程并回到坐标；用判别式讨论割线切线与参数范围。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：y=x²；y=2x+k三位置；切点(1,1)；竖直线例外；双切线参数示例。

关系：k=−1为切线边界；差式Δ非原抛物线Δ；竖直单点不套切线规则。

文字：k>−1、k=−1、k<−1、Δ交、切点坐标。

公式与单位：交点横坐标满足ax²+(b−m)x+(c−n)=0，a≠0。；非竖直线：Δ交=(b−m)²−4a(c−n)；正为两交点、零为相切、负为不交。；求完整交点需y=mx+n；竖直x=d的单交点不套上述切线判据。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第2章《一元二次方程式与二次函数》真实小节2.4《一元二次函数的图像与直线的位置关系》制作《抛物线与非竖直线的交点》教学图。学习目的：把交点问题转为二次方程并回到坐标；用判别式讨论割线切线与参数范围。本图是有条件的科学模型，非实测图或官方考题。必须出现：y=x²；y=2x+k三位置；切点(1,1)；竖直线例外；双切线参数示例。必须保持关系：k=−1为切线边界；差式Δ非原抛物线Δ；竖直单点不套切线规则。中文标签逐字采用：k>−1、k=−1、k<−1、Δ交、切点坐标。公式及条件：交点横坐标满足ax²+(b−m)x+(c−n)=0，a≠0。；非竖直线：Δ交=(b−m)²−4a(c−n)；正为两交点、零为相切、负为不交。；求完整交点需y=mx+n；竖直x=d的单交点不套上述切线判据。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 2, authentic subsection 2.4. Display the original Chinese title exactly: 抛物线与非竖直线的交点. Topic-specific scientific requirements and instructional purpose: Plot y=x^2 with lines y=2x+k for k above, equal to and below -1, showing the tangent at (1,1) when k=-1. Compute intersections from the difference quadratic. Include a clearly separate vertical-line example to prevent equating any single intersection with tangency. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: y=x²；y=2x+k三位置；切点(1,1)；竖直线例外；双切线参数示例. Preserve the following Chinese label strings exactly: k>−1、k=−1、k<−1、Δ交、切点坐标. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 交点横坐标满足ax²+(b−m)x+(c−n)=0，a≠0。；非竖直线：Δ交=(b−m)²−4a(c−n)；正为两交点、零为相切、负为不交。；求完整交点需y=mx+n；竖直x=d的单交点不套上述切线判据。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：k=−1为切线边界；差式Δ非原抛物线Δ；竖直单点不套切线规则。不得把一元二次函数的图像与直线的位置关系画成另一知识主题；不得改动k>−1、k=−1、k<−1、Δ交、切点坐标的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- k=−1为切线边界
- 差式Δ非原抛物线Δ
- 竖直单点不套切线规则
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/5-1-quadratic-functions

旧图复用：暂无对应旧图；线与曲线须精确绘制。实际匹配：无。

## 数学 第3章 · 3.1 多项式

ID：B05-MATH03-3-1；优先级：P=1；状态：not_produced。

用途：按指数与系数判断多项式及次数；以恒等式完成运算和参数分类。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：合法/非合法指数；含参数首项；降幂系数表；F=DQ+R关系。

关系：系数可含常根号；a=1时三次退为二次；余式次数低于除式。

文字：非负整数指数、最高非零项、a−1、商Q、余R。

公式与单位：P(x)=aₙxⁿ+…+a₁x+a₀，aₙ≠0时次数n；零多项式另论。；非零P,Q有deg(PQ)=degP+degQ；deg(P+Q)可能下降。；F=DQ+R，D≠0，R=0或degR<degD；验证用回乘与合并系数。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第3章《多项式》真实小节3.1《多项式》制作《多项式的次数与商余》教学图。学习目的：按指数与系数判断多项式及次数；以恒等式完成运算和参数分类。本图是有条件的科学模型，非实测图或官方考题。必须出现：合法/非合法指数；含参数首项；降幂系数表；F=DQ+R关系。必须保持关系：系数可含常根号；a=1时三次退为二次；余式次数低于除式。中文标签逐字采用：非负整数指数、最高非零项、a−1、商Q、余R。公式及条件：P(x)=aₙxⁿ+…+a₁x+a₀，aₙ≠0时次数n；零多项式另论。；非零P,Q有deg(PQ)=degP+degQ；deg(P+Q)可能下降。；F=DQ+R，D≠0，R=0或degR<degD；验证用回乘与合并系数。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 3, authentic subsection 3.1. Display the original Chinese title exactly: 多项式的次数与商余. Topic-specific scientific requirements and instructional purpose: Distinguish a radical constant coefficient from a fractional variable exponent. Show how the leading coefficient a-1 vanishes at a=1, reducing degree, and illustrate F=DQ+R with the explicit degree restriction on R. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 合法/非合法指数；含参数首项；降幂系数表；F=DQ+R关系. Preserve the following Chinese label strings exactly: 非负整数指数、最高非零项、a−1、商Q、余R. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: P(x)=aₙxⁿ+…+a₁x+a₀，aₙ≠0时次数n；零多项式另论。；非零P,Q有deg(PQ)=degP+degQ；deg(P+Q)可能下降。；F=DQ+R，D≠0，R=0或degR<degD；验证用回乘与合并系数。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：系数可含常根号；a=1时三次退为二次；余式次数低于除式。不得把多项式画成另一知识主题；不得改动非负整数指数、最高非零项、a−1、商Q、余R的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 系数可含常根号
- a=1时三次退为二次
- 余式次数低于除式
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/5-2-power-functions-and-polynomial-functions

旧图复用：无对应旧图；代数关系用文字层。实际匹配：无。

## 数学 第3章 · 3.2 余式定理

ID：B05-MATH03-3-2；优先级：P=1；状态：not_produced。

用途：由除法恒等式推导余式定理；用适当代入求参数或一次余式。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：F=(x−a)Q+r；代入x=a；2x−1根1/2；二次余式ux+v。

关系：一次除式余式常数；二次两不同根可定u,v；重复根只给一个值条件。

文字：r=F(a)、F(c/b)、a≠b、独立条件。

公式与单位：F=(x−a)Q+r，代a得r=F(a)。；对bx−c（b≠0），r=F(c/b)；商的尺度与b有关，但余数代入点由除式零点决定。；对(x−a)(x−b)、a≠b，令R=ux+v：ua+v=F(a)，ub+v=F(b)。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第3章《多项式》真实小节3.2《余式定理》制作《余式定理的消元关系》教学图。学习目的：由除法恒等式推导余式定理；用适当代入求参数或一次余式。本图是有条件的科学模型，非实测图或官方考题。必须出现：F=(x−a)Q+r；代入x=a；2x−1根1/2；二次余式ux+v。必须保持关系：一次除式余式常数；二次两不同根可定u,v；重复根只给一个值条件。中文标签逐字采用：r=F(a)、F(c/b)、a≠b、独立条件。公式及条件：F=(x−a)Q+r，代a得r=F(a)。；对bx−c（b≠0），r=F(c/b)；商的尺度与b有关，但余数代入点由除式零点决定。；对(x−a)(x−b)、a≠b，令R=ux+v：ua+v=F(a)，ub+v=F(b)。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 3, authentic subsection 3.2. Display the original Chinese title exactly: 余式定理的消元关系. Topic-specific scientific requirements and instructional purpose: Derive the remainder theorem from F=(x-a)Q+r by substituting x=a. For divisor 2x-1 use a=1/2. For two distinct linear factors, show how R=ux+v is determined by two independent values; do not count a repeated root twice as independent data. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: F=(x−a)Q+r；代入x=a；2x−1根1/2；二次余式ux+v. Preserve the following Chinese label strings exactly: r=F(a)、F(c/b)、a≠b、独立条件. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: F=(x−a)Q+r，代a得r=F(a)。；对bx−c（b≠0），r=F(c/b)；商的尺度与b有关，但余数代入点由除式零点决定。；对(x−a)(x−b)、a≠b，令R=ux+v：ua+v=F(a)，ub+v=F(b)。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：一次除式余式常数；二次两不同根可定u,v；重复根只给一个值条件。不得把余式定理画成另一知识主题；不得改动r=F(a)、F(c/b)、a≠b、独立条件的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 一次除式余式常数
- 二次两不同根可定u,v
- 重复根只给一个值条件
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/5-4-dividing-polynomials

旧图复用：无合格对应图；公式流程需准确。实际匹配：无。

## 数学 第3章 · 3.3 因式定理

ID：B05-MATH03-3-3；优先级：P=1；状态：not_produced。

用途：以余式定理证明根与一次因式的等价；求参数并核因式重数。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：F(a)=0到x−a因式；根−3与x+3；重复因式链；次数计数。

关系：两个方向等价；重数需反复除；非零n次不同根不超过n。

文字：F(a)=0、x−a、重数、不同实根、非零多项式。

公式与单位：F(a)=0 ⇔ F=(x−a)Q，证明来自F=(x−a)Q+r且r=F(a)。；若Q(a)=0，还可再抽取x−a；重复次数决定该根重数。；非零n次多项式最多n个不同实根；是否存在全部n个实根不能由次数单独保证。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第3章《多项式》真实小节3.3《因式定理》制作《根、一次因式与重数》教学图。学习目的：以余式定理证明根与一次因式的等价；求参数并核因式重数。本图是有条件的科学模型，非实测图或官方考题。必须出现：F(a)=0到x−a因式；根−3与x+3；重复因式链；次数计数。必须保持关系：两个方向等价；重数需反复除；非零n次不同根不超过n。中文标签逐字采用：F(a)=0、x−a、重数、不同实根、非零多项式。公式及条件：F(a)=0 ⇔ F=(x−a)Q，证明来自F=(x−a)Q+r且r=F(a)。；若Q(a)=0，还可再抽取x−a；重复次数决定该根重数。；非零n次多项式最多n个不同实根；是否存在全部n个实根不能由次数单独保证。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 3, authentic subsection 3.3. Display the original Chinese title exactly: 根、一次因式与重数. Topic-specific scientific requirements and instructional purpose: Connect a numerical root a with the linear factor x-a in both directions, including a=-3 and factor x+3. Show repeated division for a double root and distinguish multiplicity from the number of distinct real roots of a nonzero polynomial. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: F(a)=0到x−a因式；根−3与x+3；重复因式链；次数计数. Preserve the following Chinese label strings exactly: F(a)=0、x−a、重数、不同实根、非零多项式. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: F(a)=0 ⇔ F=(x−a)Q，证明来自F=(x−a)Q+r且r=F(a)。；若Q(a)=0，还可再抽取x−a；重复次数决定该根重数。；非零n次多项式最多n个不同实根；是否存在全部n个实根不能由次数单独保证。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：两个方向等价；重数需反复除；非零n次不同根不超过n。不得把因式定理画成另一知识主题；不得改动F(a)=0、x−a、重数、不同实根、非零多项式的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 两个方向等价
- 重数需反复除
- 非零n次不同根不超过n
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/5-5-zeros-of-polynomial-functions

旧图复用：无对应旧图；关系图与可选函数图应准确。实际匹配：无。

## 数学 第3章 · 3.4 一元多项式的因式分解

ID：B05-MATH03-3-4；优先级：P=1；状态：not_produced。

用途：依结构选择提因式、分组或求根方法；在指定数域内完成分解并回乘。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：共同因式示例；四项分组；y=x²代换；数域分支；回乘检查。

关系：x⁴−5x²+4分为四实一次因式；平方和不误用平方差；候选根不等于必存在根。

文字：公因式、分组、代换后换回、有理数/实数、完整回乘。

公式与单位：a²−b²=(a−b)(a+b)；a³−b³=(a−b)(a²+ab+b²)。；整数系数多项式若有既约有理根p/q，则p整除常数项、q整除首项系数（首常项非零等条件下）。；分解流程：公因式 → 恒等结构/分组/代换 → 因式定理找根 → 指定数域继续 → 回乘。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第3章《多项式》真实小节3.4《一元多项式的因式分解》制作《因式分解的方法选择》教学图。学习目的：依结构选择提因式、分组或求根方法；在指定数域内完成分解并回乘。本图是有条件的科学模型，非实测图或官方考题。必须出现：共同因式示例；四项分组；y=x²代换；数域分支；回乘检查。必须保持关系：x⁴−5x²+4分为四实一次因式；平方和不误用平方差；候选根不等于必存在根。中文标签逐字采用：公因式、分组、代换后换回、有理数/实数、完整回乘。公式及条件：a²−b²=(a−b)(a+b)；a³−b³=(a−b)(a²+ab+b²)。；整数系数多项式若有既约有理根p/q，则p整除常数项、q整除首项系数（首常项非零等条件下）。；分解流程：公因式 → 恒等结构/分组/代换 → 因式定理找根 → 指定数域继续 → 回乘。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 3, authentic subsection 3.4. Display the original Chinese title exactly: 因式分解的方法选择. Topic-specific scientific requirements and instructional purpose: Create a method-selection diagram for common factors, identities, grouping, substitution and root-based division. Work x^4-5x^2+4 through y=x^2 to four real linear factors, distinguish rational and real factorization, and require full coefficient verification. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 共同因式示例；四项分组；y=x²代换；数域分支；回乘检查. Preserve the following Chinese label strings exactly: 公因式、分组、代换后换回、有理数/实数、完整回乘. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: a²−b²=(a−b)(a+b)；a³−b³=(a−b)(a²+ab+b²)。；整数系数多项式若有既约有理根p/q，则p整除常数项、q整除首项系数（首常项非零等条件下）。；分解流程：公因式 → 恒等结构/分组/代换 → 因式定理找根 → 指定数域继续 → 回乘。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：x⁴−5x²+4分为四实一次因式；平方和不误用平方差；候选根不等于必存在根。不得把一元多项式的因式分解画成另一知识主题；不得改动公因式、分组、代换后换回、有理数/实数、完整回乘的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- x⁴−5x²+4分为四实一次因式
- 平方和不误用平方差
- 候选根不等于必存在根
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/1-5-factoring-polynomials

旧图复用：无对应图；代数结构关系可用页面图与SVG。实际匹配：无。

## 数学 第3章 · 3.5 解一元高次方程式

ID：B05-MATH03-3-5；优先级：P=0；状态：not_produced。

用途：用因式分解与代换求全部实根；处理重根、参数退化和非等价除法。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：x³=x因式树；x²代换；正零负参数分支；实根集合与重数。

关系：保留x=0分支；负y不回实根；正y给±根；a=0时根合并。

文字：全部实根、y≥0、±√y、原域、不同根/重数。

公式与单位：F=AB=0 ⇔ A=0或B=0（实数代数）；重复因式保留重数但解集去重。；y=x²时y≥0，y>0回得±√y，y=0回得0，y<0无实x。；含变量因子除法：先分该因子为0与非0，或避免除法而用零乘积。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第3章《多项式》真实小节3.5《解一元高次方程式》制作《高次方程的完整解集》教学图。学习目的：用因式分解与代换求全部实根；处理重根、参数退化和非等价除法。本图是有条件的科学模型，非实测图或官方考题。必须出现：x³=x因式树；x²代换；正零负参数分支；实根集合与重数。必须保持关系：保留x=0分支；负y不回实根；正y给±根；a=0时根合并。中文标签逐字采用：全部实根、y≥0、±√y、原域、不同根/重数。公式及条件：F=AB=0 ⇔ A=0或B=0（实数代数）；重复因式保留重数但解集去重。；y=x²时y≥0，y>0回得±√y，y=0回得0，y<0无实x。；含变量因子除法：先分该因子为0与非0，或避免除法而用零乘积。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 3, authentic subsection 3.5. Display the original Chinese title exactly: 高次方程的完整解集. Topic-specific scientific requirements and instructional purpose: Show a complete solution tree for x^3=x retaining x=0, and for an even-power equation using y=x^2 with y>=0 and both square-root signs. Include parameter branches for x(x^2-a)=0, distinguishing root multiplicity from distinct real solutions. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: x³=x因式树；x²代换；正零负参数分支；实根集合与重数. Preserve the following Chinese label strings exactly: 全部实根、y≥0、±√y、原域、不同根/重数. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: F=AB=0 ⇔ A=0或B=0（实数代数）；重复因式保留重数但解集去重。；y=x²时y≥0，y>0回得±√y，y=0回得0，y<0无实x。；含变量因子除法：先分该因子为0与非0，或避免除法而用零乘积。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：保留x=0分支；负y不回实根；正y给±根；a=0时根合并。不得把解一元高次方程式画成另一知识主题；不得改动全部实根、y≥0、±√y、原域、不同根/重数的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 保留x=0分支
- 负y不回实根
- 正y给±根
- a=0时根合并
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/5-5-zeros-of-polynomial-functions

旧图复用：无对应旧图；函数曲线如新增须确定性绘制。实际匹配：无。

## 数学 第4章 · 4.1 根式、无理式

ID：B05-MATH04-4-1；优先级：P=0；状态：not_produced。

用途：以实数范围定义根式与定义域；解释主平方根和绝对值的关系。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：y=√(x²)=|x|图；x²=a的两根；分式号表；排除点。

关系：根号输出非负；偶次根需非负；分母不能零；号表保留x<−2。

文字：√x²=|x|、x=±7为方程解、−2、1、定义域。

公式与单位：实数范围：偶次根要求被开方数≥0，奇次根可为任意实数；分母另需非零。；√(x²)=|x|={x（x≥0），−x（x<0）}。；若√g(x)在分母，需g(x)>0；若分母还含其他项，需直接检查整个分母，而非一律令每项正。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第4章《无理式》真实小节4.1《根式、无理式》制作《主平方根与定义域》教学图。学习目的：以实数范围定义根式与定义域；解释主平方根和绝对值的关系。本图是有条件的科学模型，非实测图或官方考题。必须出现：y=√(x²)=|x|图；x²=a的两根；分式号表；排除点。必须保持关系：根号输出非负；偶次根需非负；分母不能零；号表保留x<−2。中文标签逐字采用：√x²=|x|、x=±7为方程解、−2、1、定义域。公式及条件：实数范围：偶次根要求被开方数≥0，奇次根可为任意实数；分母另需非零。；√(x²)=|x|={x（x≥0），−x（x<0）}。；若√g(x)在分母，需g(x)>0；若分母还含其他项，需直接检查整个分母，而非一律令每项正。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 4, authentic subsection 4.1. Display the original Chinese title exactly: 主平方根与定义域. Topic-specific scientific requirements and instructional purpose: Draw the exact V-shaped graph y=sqrt(x^2)=abs(x), distinguish the principal root sqrt(49)=7 from equation solutions ±7, and show a sign chart for (x-1)/(x+2) with -2 excluded and 1 included. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: y=√(x²)=|x|图；x²=a的两根；分式号表；排除点. Preserve the following Chinese label strings exactly: √x²=|x|、x=±7为方程解、−2、1、定义域. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 实数范围：偶次根要求被开方数≥0，奇次根可为任意实数；分母另需非零。；√(x²)=|x|={x（x≥0），−x（x<0）}。；若√g(x)在分母，需g(x)>0；若分母还含其他项，需直接检查整个分母，而非一律令每项正。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：根号输出非负；偶次根需非负；分母不能零；号表保留x<−2。不得把根式、无理式画成另一知识主题；不得改动√x²=|x|、x=±7为方程解、−2、1、定义域的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 根号输出非负
- 偶次根需非负
- 分母不能零
- 号表保留x<−2
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/1-3-radicals-and-rational-exponents

旧图复用：数学暂无合格对应图；必须确定性绘制。实际匹配：无。

## 数学 第4章 · 4.2 分数指数

ID：B05-MATH04-4-2；优先级：P=0；状态：not_produced。

用途：用根式定义有理指数并注明底数条件；正确处理负指数与指数运算的边界。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：a^(m/n)与根式对应；27^(2/3)；16^(−3/4)；正负底数边界。

关系：分母开根分子幂；负指数取倒数；正底数指数律有条件。

文字：a>0、n为正整数、1/a^r、27^(2/3)=9、实数范围。

公式与单位：a>0时，a^(m/n)=ⁿ√(a^m)，指数先视为约分的有理数，n>0。；a≠0时a^(−r)=1/a^r；a>0时常用指数律在本节有理指数范围成立。；负底数只在相应实根有意义并明确约定时处理；(−8)^(1/3)=−2，而(−8)^(1/2)无实数值。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第4章《无理式》真实小节4.2《分数指数》制作《有理指数与条件》教学图。学习目的：用根式定义有理指数并注明底数条件；正确处理负指数与指数运算的边界。本图是有条件的科学模型，非实测图或官方考题。必须出现：a^(m/n)与根式对应；27^(2/3)；16^(−3/4)；正负底数边界。必须保持关系：分母开根分子幂；负指数取倒数；正底数指数律有条件。中文标签逐字采用：a>0、n为正整数、1/a^r、27^(2/3)=9、实数范围。公式及条件：a>0时，a^(m/n)=ⁿ√(a^m)，指数先视为约分的有理数，n>0。；a≠0时a^(−r)=1/a^r；a>0时常用指数律在本节有理指数范围成立。；负底数只在相应实根有意义并明确约定时处理；(−8)^(1/3)=−2，而(−8)^(1/2)无实数值。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 4, authentic subsection 4.2. Display the original Chinese title exactly: 有理指数与条件. Topic-specific scientific requirements and instructional purpose: Explain rational exponents for positive bases: denominator as root index and numerator as power. Show 27^(2/3)=9 and 16^(-3/4)=1/8. State nonzero conditions for negative exponents and warn that power-of-a-power rules cannot be extended blindly to negative bases and principal even roots. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: a^(m/n)与根式对应；27^(2/3)；16^(−3/4)；正负底数边界. Preserve the following Chinese label strings exactly: a>0、n为正整数、1/a^r、27^(2/3)=9、实数范围. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: a>0时，a^(m/n)=ⁿ√(a^m)，指数先视为约分的有理数，n>0。；a≠0时a^(−r)=1/a^r；a>0时常用指数律在本节有理指数范围成立。；负底数只在相应实根有意义并明确约定时处理；(−8)^(1/3)=−2，而(−8)^(1/2)无实数值。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：分母开根分子幂；负指数取倒数；正底数指数律有条件。不得把分数指数画成另一知识主题；不得改动a>0、n为正整数、1/a^r、27^(2/3)=9、实数范围的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 分母开根分子幂
- 负指数取倒数
- 正底数指数律有条件
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/1-3-radicals-and-rational-exponents

旧图复用：暂无对应旧图；公式需文字层和准确上下标。实际匹配：无。

## 数学 第4章 · 4.3 根式的运算

ID：B05-MATH04-4-3；优先级：P=0；状态：not_produced。

用途：在定义域内化简与合并根式；保留绝对值并解释平方变形风险。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：平方因子分解；√2同类项；完全平方交叉矩形；绝对值分段图；方程候选筛选。

关系：保留2ab交叉项；提出x²为绝对值；平方候选−1需排除。

文字：a,b≥0、√x²=|x|、2√ab、候选≠原解。

公式与单位：a,b≥0时√a√b=√(ab)；a≥0、b>0时√a/√b=√(a/b)。；√(x²)=|x|；(√a+√b)²=a+b+2√(ab)，a,b≥0。；解含根式方程：定义域与符号 → 隔离根式 → 平方求候选 → 代回原式排除增根。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第4章《无理式》真实小节4.3《根式的运算》制作《根式运算的条件与交叉项》教学图。学习目的：在定义域内化简与合并根式；保留绝对值并解释平方变形风险。本图是有条件的科学模型，非实测图或官方考题。必须出现：平方因子分解；√2同类项；完全平方交叉矩形；绝对值分段图；方程候选筛选。必须保持关系：保留2ab交叉项；提出x²为绝对值；平方候选−1需排除。中文标签逐字采用：a,b≥0、√x²=|x|、2√ab、候选≠原解。公式及条件：a,b≥0时√a√b=√(ab)；a≥0、b>0时√a/√b=√(a/b)。；√(x²)=|x|；(√a+√b)²=a+b+2√(ab)，a,b≥0。；解含根式方程：定义域与符号 → 隔离根式 → 平方求候选 → 代回原式排除增根。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 4, authentic subsection 4.3. Display the original Chinese title exactly: 根式运算的条件与交叉项. Topic-specific scientific requirements and instructional purpose: Illustrate extraction of square factors and like radicals, retain the 2ab cross term in a square-area model, and graph abs(x-1)+abs(x+1) with breakpoints -1 and 1. Show why squaring sqrt(x+2)=x gives an extraneous candidate -1 that must be rejected. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 平方因子分解；√2同类项；完全平方交叉矩形；绝对值分段图；方程候选筛选. Preserve the following Chinese label strings exactly: a,b≥0、√x²=|x|、2√ab、候选≠原解. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: a,b≥0时√a√b=√(ab)；a≥0、b>0时√a/√b=√(a/b)。；√(x²)=|x|；(√a+√b)²=a+b+2√(ab)，a,b≥0。；解含根式方程：定义域与符号 → 隔离根式 → 平方求候选 → 代回原式排除增根。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：保留2ab交叉项；提出x²为绝对值；平方候选−1需排除。不得把根式的运算画成另一知识主题；不得改动a,b≥0、√x²=|x|、2√ab、候选≠原解的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 保留2ab交叉项
- 提出x²为绝对值
- 平方候选−1需排除
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/1-3-radicals-and-rational-exponents

旧图复用：无对应旧图；坐标和面积关系应确定性构图。实际匹配：无。

## 数学 第4章 · 4.4 有理化因式及有理化分母

ID：B05-MATH04-4-4；优先级：P=0；状态：not_produced。

用途：用共轭及乘法恒等式有理化；在等价变形中保留原定义域。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：共轭乘法矩形；√3±√2；变量约分；x=1空点；立方差因式。

关系：分子分母同乘非零；平方差3−2=1；取消因子仍保留排除点。

文字：共轭、非零因子、x≥0且x≠1、1/(√x+1)、空点不是原函数值。

公式与单位：a>0：1/√a=√a/a。；m,n≥0且m≠n时，1/(√m+√n)=(√m−√n)/(m−n)；m=n>0时应直接处理2√m。；(a−b)(a²+ab+b²)=a³−b³，可为特定立方根分母构造有理化因式。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第4章《无理式》真实小节4.4《有理化因式及有理化分母》制作《有理化与原定义域》教学图。学习目的：用共轭及乘法恒等式有理化；在等价变形中保留原定义域。本图是有条件的科学模型，非实测图或官方考题。必须出现：共轭乘法矩形；√3±√2；变量约分；x=1空点；立方差因式。必须保持关系：分子分母同乘非零；平方差3−2=1；取消因子仍保留排除点。中文标签逐字采用：共轭、非零因子、x≥0且x≠1、1/(√x+1)、空点不是原函数值。公式及条件：a>0：1/√a=√a/a。；m,n≥0且m≠n时，1/(√m+√n)=(√m−√n)/(m−n)；m=n>0时应直接处理2√m。；(a−b)(a²+ab+b²)=a³−b³，可为特定立方根分母构造有理化因式。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 4, authentic subsection 4.4. Display the original Chinese title exactly: 有理化与原定义域. Topic-specific scientific requirements and instructional purpose: Show rationalization of 1/(sqrt(3)+sqrt(2)) by its nonzero conjugate. For (sqrt(x)-1)/(x-1), retain x>=0 and x!=1 after simplification to 1/(sqrt(x)+1), drawing an open point at x=1 rather than filling in the original undefined value. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 共轭乘法矩形；√3±√2；变量约分；x=1空点；立方差因式. Preserve the following Chinese label strings exactly: 共轭、非零因子、x≥0且x≠1、1/(√x+1)、空点不是原函数值. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: a>0：1/√a=√a/a。；m,n≥0且m≠n时，1/(√m+√n)=(√m−√n)/(m−n)；m=n>0时应直接处理2√m。；(a−b)(a²+ab+b²)=a³−b³，可为特定立方根分母构造有理化因式。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：分子分母同乘非零；平方差3−2=1；取消因子仍保留排除点。不得把有理化因式及有理化分母画成另一知识主题；不得改动共轭、非零因子、x≥0且x≠1、1/(√x+1)、空点不是原函数值的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 分子分母同乘非零
- 平方差3−2=1
- 取消因子仍保留排除点
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/1-3-radicals-and-rational-exponents

旧图复用：暂无对应旧图；代数和函数空点需确定性SVG。实际匹配：无。

## 数学 第5章 · 5.1 函数的定义

ID：B05-MATH05-5-1；优先级：P=0；状态：not_produced。

用途：用定义域陪域与单值对应判断函数；把不同表示法转为可验证的输入输出规则。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：集合A/B箭头；多对一合法例；一对多非法例；分段边界；圆与上半圆。

关系：每输入恰一输出；值域包含于陪域；竖线检验不是水平线。

文字：定义域、陪域、值域、允许多对一、不允许一对多。

公式与单位：f:A→B：对每个x∈A，存在且仅存在一个f(x)∈B。；值域={f(x):x∈A}⊆B；多对一仍是函数。；f(a+1)按整体代入，分段函数按输入条件选择，重叠边界须一致或排除重叠。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第5章《函数》真实小节5.1《函数的定义》制作《函数的单值对应与边界》教学图。学习目的：用定义域陪域与单值对应判断函数；把不同表示法转为可验证的输入输出规则。本图是有条件的科学模型，非实测图或官方考题。必须出现：集合A/B箭头；多对一合法例；一对多非法例；分段边界；圆与上半圆。必须保持关系：每输入恰一输出；值域包含于陪域；竖线检验不是水平线。中文标签逐字采用：定义域、陪域、值域、允许多对一、不允许一对多。公式及条件：f:A→B：对每个x∈A，存在且仅存在一个f(x)∈B。；值域={f(x):x∈A}⊆B；多对一仍是函数。；f(a+1)按整体代入，分段函数按输入条件选择，重叠边界须一致或排除重叠。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 5, authentic subsection 5.1. Display the original Chinese title exactly: 函数的单值对应与边界. Topic-specific scientific requirements and instructional purpose: Show A={1,2,3} mapping to B={a,b}, with 1 and 2 both mapping to a and 3 to b as a valid function. Contrast a conflicting second output for input 1. Separate vertical-line testing of a full circle from a valid upper semicircle and mark piecewise boundary ownership. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 集合A/B箭头；多对一合法例；一对多非法例；分段边界；圆与上半圆. Preserve the following Chinese label strings exactly: 定义域、陪域、值域、允许多对一、不允许一对多. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: f:A→B：对每个x∈A，存在且仅存在一个f(x)∈B。；值域={f(x):x∈A}⊆B；多对一仍是函数。；f(a+1)按整体代入，分段函数按输入条件选择，重叠边界须一致或排除重叠。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：每输入恰一输出；值域包含于陪域；竖线检验不是水平线。不得把函数的定义画成另一知识主题；不得改动定义域、陪域、值域、允许多对一、不允许一对多的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 每输入恰一输出
- 值域包含于陪域
- 竖线检验不是水平线
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-1-functions-and-function-notation

旧图复用：暂无对应旧图；箭头对应须确定性构造。实际匹配：无。

## 数学 第5章 · 5.2 函数的定义域与值域

ID：B05-MATH05-5-2；优先级：P=0；状态：not_produced。

用途：把代数限制与实际输入范围取交集；用结构和反解求值域并检查端点。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：二次函数顶点与[0,3]域；倒数函数空缺；分段输出范围；开闭端点。

关系：(x−2)²+1值域[1,5]；倒数值域不含0；空端点与渐近线不当实点。

文字：定义域、值域、顶点(2,1)、空心点、y≠0。

公式与单位：实数代数域=各分母非零条件∩偶根非负条件∩题给范围。；二次函数a(x−h)²+k，结合a符号与x范围判断输出。；反解法：令y=f(x)，找满足全部原域条件的x；有合法原像的y才在值域。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第5章《函数》真实小节5.2《函数的定义域与值域》制作《定义域与值域的端点》教学图。学习目的：把代数限制与实际输入范围取交集；用结构和反解求值域并检查端点。本图是有条件的科学模型，非实测图或官方考题。必须出现：二次函数顶点与[0,3]域；倒数函数空缺；分段输出范围；开闭端点。必须保持关系：(x−2)²+1值域[1,5]；倒数值域不含0；空端点与渐近线不当实点。中文标签逐字采用：定义域、值域、顶点(2,1)、空心点、y≠0。公式及条件：实数代数域=各分母非零条件∩偶根非负条件∩题给范围。；二次函数a(x−h)²+k，结合a符号与x范围判断输出。；反解法：令y=f(x)，找满足全部原域条件的x；有合法原像的y才在值域。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 5, authentic subsection 5.2. Display the original Chinese title exactly: 定义域与值域的端点. Topic-specific scientific requirements and instructional purpose: Plot y=(x-2)^2+1 restricted to [0,3], with vertex (2,1) and range [1,5]. Separately plot y=1/(x-1) with asymptotes x=1 and y=0, and use correct open/closed endpoints when projecting domains and ranges. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 二次函数顶点与[0,3]域；倒数函数空缺；分段输出范围；开闭端点. Preserve the following Chinese label strings exactly: 定义域、值域、顶点(2,1)、空心点、y≠0. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 实数代数域=各分母非零条件∩偶根非负条件∩题给范围。；二次函数a(x−h)²+k，结合a符号与x范围判断输出。；反解法：令y=f(x)，找满足全部原域条件的x；有合法原像的y才在值域。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：(x−2)²+1值域[1,5]；倒数值域不含0；空端点与渐近线不当实点。不得把函数的定义域与值域画成另一知识主题；不得改动定义域、值域、顶点(2,1)、空心点、y≠0的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- (x−2)²+1值域[1,5]
- 倒数值域不含0
- 空端点与渐近线不当实点
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-2-domain-and-range

旧图复用：暂无对应图；函数必须数学绘图库或SVG准确绘制。实际匹配：无。

## 数学 第5章 · 5.3 函数的图像及其变换

ID：B05-MATH05-5-3；优先级：P=0；状态：not_produced。

用途：由关键点与定义域画函数图；用点坐标映射解释平移伸缩和反射。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：基本抛物线；平移后抛物线；点(6,5)映射；内层输入方程；定义域区间。

关系：顶点(2,−3)；3(x−1)=6得x=3；纵坐标−2×5+4=−6；横向缩放1/|b|。

文字：y=x²、y=(x−2)²−3、(3,−6)、x新=h+x旧/b。

公式与单位：g(x)=f(x−h)+k：(x₀,y₀)→(x₀+h,y₀+k)。；g(x)=a f(b(x−h))+k，b≠0：(x₀,y₀)→(h+x₀/b,k+a y₀)。；先因式提出内层b，例如2x−6=2(x−3)；再变换定义域、值域与空点。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第5章《函数》真实小节5.3《函数的图像及其变换》制作《函数变换的点映射》教学图。学习目的：由关键点与定义域画函数图；用点坐标映射解释平移伸缩和反射。本图是有条件的科学模型，非实测图或官方考题。必须出现：基本抛物线；平移后抛物线；点(6,5)映射；内层输入方程；定义域区间。必须保持关系：顶点(2,−3)；3(x−1)=6得x=3；纵坐标−2×5+4=−6；横向缩放1/|b|。中文标签逐字采用：y=x²、y=(x−2)²−3、(3,−6)、x新=h+x旧/b。公式及条件：g(x)=f(x−h)+k：(x₀,y₀)→(x₀+h,y₀+k)。；g(x)=a f(b(x−h))+k，b≠0：(x₀,y₀)→(h+x₀/b,k+a y₀)。；先因式提出内层b，例如2x−6=2(x−3)；再变换定义域、值域与空点。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 5, authentic subsection 5.3. Display the original Chinese title exactly: 函数变换的点映射. Topic-specific scientific requirements and instructional purpose: Plot y=x^2 and y=(x-2)^2-3 on consistent labelled axes, marking vertex (2,-3) and symmetric points (1,-2),(3,-2). Separately map (6,5) on f to (3,-6) on -2f(3(x-1))+4, solving the inner-input equation rather than multiplying horizontal coordinates by 3. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 基本抛物线；平移后抛物线；点(6,5)映射；内层输入方程；定义域区间. Preserve the following Chinese label strings exactly: y=x²、y=(x−2)²−3、(3,−6)、x新=h+x旧/b. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: g(x)=f(x−h)+k：(x₀,y₀)→(x₀+h,y₀+k)。；g(x)=a f(b(x−h))+k，b≠0：(x₀,y₀)→(h+x₀/b,k+a y₀)。；先因式提出内层b，例如2x−6=2(x−3)；再变换定义域、值域与空点。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：顶点(2,−3)；3(x−1)=6得x=3；纵坐标−2×5+4=−6；横向缩放1/|b|。不得把函数的图像及其变换画成另一知识主题；不得改动y=x²、y=(x−2)²−3、(3,−6)、x新=h+x旧/b的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 顶点(2,−3)
- 3(x−1)=6得x=3
- 纵坐标−2×5+4=−6
- 横向缩放1/|b|
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-5-transformation-of-functions

旧图复用：无对应旧图；必须函数绘图库确定曲线。实际匹配：无。

## 数学 第5章 · 5.4 合成函数

ID：B05-MATH05-5-4；优先级：P=0；状态：not_produced。

用途：按输入顺序求合成函数；在化简后仍保留内外层定义域条件。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：x→g→f流程；反向流程对照；根号与倒数门槛；化简直线空点。

关系：f∘g先g后f；x∈Dg且g(x)∈Df；1/[1/(x−1)]简化后仍排除1。

文字：内层、外层、Dg、Df、x≠1空点。

公式与单位：(f∘g)(x)=f(g(x))，执行顺序x→g→f。；D_(f∘g)={x∈D_g:g(x)∈D_f}。；若合成化简中约去因子，仍保留各层原定义限制；相同表达式但域不同不一定是同一函数。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第5章《函数》真实小节5.4《合成函数》制作《合成函数的顺序与域》教学图。学习目的：按输入顺序求合成函数；在化简后仍保留内外层定义域条件。本图是有条件的科学模型，非实测图或官方考题。必须出现：x→g→f流程；反向流程对照；根号与倒数门槛；化简直线空点。必须保持关系：f∘g先g后f；x∈Dg且g(x)∈Df；1/[1/(x−1)]简化后仍排除1。中文标签逐字采用：内层、外层、Dg、Df、x≠1空点。公式及条件：(f∘g)(x)=f(g(x))，执行顺序x→g→f。；D_(f∘g)={x∈D_g:g(x)∈D_f}。；若合成化简中约去因子，仍保留各层原定义限制；相同表达式但域不同不一定是同一函数。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 5, authentic subsection 5.4. Display the original Chinese title exactly: 合成函数的顺序与域. Topic-specific scientific requirements and instructional purpose: Draw x flowing through g then f, distinct from the reversed order. State both domain tests x in Dg and g(x) in Df. For f(x)=1/x and g(x)=1/(x-1), show the simplified line y=x-1 with an open point at x=1, not a fully defined straight line. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: x→g→f流程；反向流程对照；根号与倒数门槛；化简直线空点. Preserve the following Chinese label strings exactly: 内层、外层、Dg、Df、x≠1空点. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: (f∘g)(x)=f(g(x))，执行顺序x→g→f。；D_(f∘g)={x∈D_g:g(x)∈D_f}。；若合成化简中约去因子，仍保留各层原定义限制；相同表达式但域不同不一定是同一函数。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：f∘g先g后f；x∈Dg且g(x)∈Df；1/[1/(x−1)]简化后仍排除1。不得把合成函数画成另一知识主题；不得改动内层、外层、Dg、Df、x≠1空点的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- f∘g先g后f
- x∈Dg且g(x)∈Df
- 1/[1/(x−1)]简化后仍排除1
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-4-composition-of-functions

旧图复用：暂无对应旧图；映射箭头和函数空点须精确。实际匹配：无。

## 数学 第5章 · 5.5 一对一函数、映成函数及一一映成函数

ID：B05-MATH05-5-5；优先级：P=0；状态：not_produced。

用途：按定义判断单射映成及双射；解释定义域陪域改变怎样影响性质。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：四种有限映射图；平方函数不同域陪域；水平线检验；线性参数分支。

关系：多输入同输出可仍为函数；满射需覆盖陪域；双射同时覆盖且唯一。

文字：一对一/单射、映成/满射、一一映成/双射、值域=陪域、a≠0。

公式与单位：单射：f(x₁)=f(x₂)⇒x₁=x₂；映成：对任意y∈B有x∈A使f(x)=y。；双射=单射且映成；实际值域B′满足B′⊆B。；线性f:R→R、f=ax+b，a≠0时任意y唯一原像x=(y−b)/a；a=0另论。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第5章《函数》真实小节5.5《一对一函数、映成函数及一一映成函数》制作《单射、映成与双射对照》教学图。学习目的：按定义判断单射映成及双射；解释定义域陪域改变怎样影响性质。本图是有条件的科学模型，非实测图或官方考题。必须出现：四种有限映射图；平方函数不同域陪域；水平线检验；线性参数分支。必须保持关系：多输入同输出可仍为函数；满射需覆盖陪域；双射同时覆盖且唯一。中文标签逐字采用：一对一/单射、映成/满射、一一映成/双射、值域=陪域、a≠0。公式及条件：单射：f(x₁)=f(x₂)⇒x₁=x₂；映成：对任意y∈B有x∈A使f(x)=y。；双射=单射且映成；实际值域B′满足B′⊆B。；线性f:R→R、f=ax+b，a≠0时任意y唯一原像x=(y−b)/a；a=0另论。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 5, authentic subsection 5.5. Display the original Chinese title exactly: 单射、映成与双射对照. Topic-specific scientific requirements and instructional purpose: Construct separate finite-set diagrams for injective-only, surjective-only, bijective and neither, with exactly one outgoing arrow per domain element. Compare x^2 on R versus nonnegative domains/codomains, and distinguish horizontal-line testing from vertical-line testing. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 四种有限映射图；平方函数不同域陪域；水平线检验；线性参数分支. Preserve the following Chinese label strings exactly: 一对一/单射、映成/满射、一一映成/双射、值域=陪域、a≠0. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 单射：f(x₁)=f(x₂)⇒x₁=x₂；映成：对任意y∈B有x∈A使f(x)=y。；双射=单射且映成；实际值域B′满足B′⊆B。；线性f:R→R、f=ax+b，a≠0时任意y唯一原像x=(y−b)/a；a=0另论。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：多输入同输出可仍为函数；满射需覆盖陪域；双射同时覆盖且唯一。不得把一对一函数、映成函数及一一映成函数画成另一知识主题；不得改动一对一/单射、映成/满射、一一映成/双射、值域=陪域、a≠0的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 多输入同输出可仍为函数
- 满射需覆盖陪域
- 双射同时覆盖且唯一
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-7-inverse-functions

旧图复用：暂无对应图；每个箭头必须核对定义。实际匹配：无。

## 数学 第5章 · 5.6 反函数

ID：B05-MATH05-5-6；优先级：P=0；状态：not_produced。

用途：在一一对应范围内求反函数；交换定义域值域并用合成和对称验证。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：线性受限函数及反函数；抛物线左支；反向根式；y=x对称轴；空点。

关系：(2,7)到(7,2)；原左支反式2−√(x−1)；原域与反值域交换；倒数另论。

文字：f⁻¹、不是1/f、y=x、x≤2、反域x≥1。

公式与单位：f:A→B双射时，f⁻¹:B→A，f⁻¹∘f=id_A，f∘f⁻¹=id_B。；求法：y=f(x) → 在原域解x → 交换字母 → 标反函数域和值域 → 双向合成验证。；原图(a,b)反射为(b,a)，对称轴y=x；f⁻¹(x)≠1/f(x)一般成立。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中数学第5章《函数》真实小节5.6《反函数》制作《反函数与定义域值域交换》教学图。学习目的：在一一对应范围内求反函数；交换定义域值域并用合成和对称验证。本图是有条件的科学模型，非实测图或官方考题。必须出现：线性受限函数及反函数；抛物线左支；反向根式；y=x对称轴；空点。必须保持关系：(2,7)到(7,2)；原左支反式2−√(x−1)；原域与反值域交换；倒数另论。中文标签逐字采用：f⁻¹、不是1/f、y=x、x≤2、反域x≥1。公式及条件：f:A→B双射时，f⁻¹:B→A，f⁻¹∘f=id_A，f∘f⁻¹=id_B。；求法：y=f(x) → 在原域解x → 交换字母 → 标反函数域和值域 → 双向合成验证。；原图(a,b)反射为(b,a)，对称轴y=x；f⁻¹(x)≠1/f(x)一般成立。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high mathematics teaching diagram for chapter 5, authentic subsection 5.6. Display the original Chinese title exactly: 反函数与定义域值域交换. Topic-specific scientific requirements and instructional purpose: Plot a restricted function and its inverse as reflections across y=x using equal axis scales. For f(x)=(x-2)^2+1 on x<=2, draw inverse 2-sqrt(x-1) on x>=1, not the positive branch. Swap (2,7) to (7,2) and distinguish inverse notation from reciprocal. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 线性受限函数及反函数；抛物线左支；反向根式；y=x对称轴；空点. Preserve the following Chinese label strings exactly: f⁻¹、不是1/f、y=x、x≤2、反域x≥1. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: f:A→B双射时，f⁻¹:B→A，f⁻¹∘f=id_A，f∘f⁻¹=id_B。；求法：y=f(x) → 在原域解x → 交换字母 → 标反函数域和值域 → 双向合成验证。；原图(a,b)反射为(b,a)，对称轴y=x；f⁻¹(x)≠1/f(x)一般成立。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：(2,7)到(7,2)；原左支反式2−√(x−1)；原域与反值域交换；倒数另论。不得把反函数画成另一知识主题；不得改动f⁻¹、不是1/f、y=x、x≤2、反域x≥1的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- (2,7)到(7,2)
- 原左支反式2−√(x−1)
- 原域与反值域交换
- 倒数另论
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/1058092101/数学-高一上册
- https://openstax.org/books/algebra-and-trigonometry-2e/pages/3-7-inverse-functions

旧图复用：暂无对应旧图；曲线与反射必须确定性绘制。实际匹配：无。

## 物理 第1章 · 1.1 什么是物理学

ID：B05-PHYS01-1-1；优先级：P2；状态：not_produced。

用途：用物理量与条件描述现象；区分模型预测、测量与结论。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：实际物体；质点近似；可测量量；含误差数据；模型预测。

关系：近似由问题决定；证据比较有条件；不画成一次吻合终结验证。

文字：数值×单位、对象与条件、预测、测量与不确定性。

公式与单位：物理量Q=数值×单位；换单位时量保持不变，数值按换算改变。；平均速度定义为位移/对应时间间隔；路程/时间是平均速率，不能仅凭单位相同便当作同量。；模型有效性检验：明确条件 → 给可测预测 → 与含不确定性的结果比较 → 保留或修正。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第1章《物理学简介》真实小节1.1《什么是物理学》制作《从现象到可检验模型》教学图。学习目的：用物理量与条件描述现象；区分模型预测、测量与结论。本图是有条件的科学模型，非实测图或官方考题。必须出现：实际物体；质点近似；可测量量；含误差数据；模型预测。必须保持关系：近似由问题决定；证据比较有条件；不画成一次吻合终结验证。中文标签逐字采用：数值×单位、对象与条件、预测、测量与不确定性。公式及条件：物理量Q=数值×单位；换单位时量保持不变，数值按换算改变。；平均速度定义为位移/对应时间间隔；路程/时间是平均速率，不能仅凭单位相同便当作同量。；模型有效性检验：明确条件 → 给可测预测 → 与含不确定性的结果比较 → 保留或修正。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 1, authentic subsection 1.1. Display the original Chinese title exactly: 从现象到可检验模型. Topic-specific scientific requirements and instructional purpose: Show observation, physical quantities, a question-specific model, measurable predictions and uncertainty-aware comparison. Contrast treating a bus as a particle for a long journey with retaining its size at a narrow doorway. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 实际物体；质点近似；可测量量；含误差数据；模型预测. Preserve the following Chinese label strings exactly: 数值×单位、对象与条件、预测、测量与不确定性. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 物理量Q=数值×单位；换单位时量保持不变，数值按换算改变。；平均速度定义为位移/对应时间间隔；路程/时间是平均速率，不能仅凭单位相同便当作同量。；模型有效性检验：明确条件 → 给可测预测 → 与含不确定性的结果比较 → 保留或修正。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：近似由问题决定；证据比较有条件；不画成一次吻合终结验证。不得把什么是物理学画成另一知识主题；不得改动数值×单位、对象与条件、预测、测量与不确定性的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 近似由问题决定
- 证据比较有条件
- 不画成一次吻合终结验证
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/1-1-physics-an-introduction

旧图复用：可用文字关系图，非必须新增插画。实际匹配：无。

## 物理 第1章 · 1.2 物理学的研究方法

ID：B05-PHYS01-1-2；优先级：P1；状态：not_produced。

用途：设计可检验的单因素实验；区分归纳、演绎与因果证据。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：两坐标图；y=2x；y=2x+1；重复读数；零点偏移。

关系：正比图过原点；线性可非零截距；共同偏移平均后仍存在。

文字：x单位、y单位、截距、随机波动、共同偏移。

公式与单位：检验正比y=kx：比较y/x是否近似恒定，并检查图线是否与原点相容；非零截距需解释或改模型。；重复n次取平均x̄=Σxᵢ/n可减小部分随机波动影响，但共同偏移b仍留在x̄中。；设计结构：问题 → 自变量与水平 → 因变量测法 → 控制与对照 → 重复记录 → 处理 → 条件内结论。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第1章《物理学简介》真实小节1.2《物理学的研究方法》制作《正比、线性与实验偏移》教学图。学习目的：设计可检验的单因素实验；区分归纳、演绎与因果证据。本图是有条件的科学模型，非实测图或官方考题。必须出现：两坐标图；y=2x；y=2x+1；重复读数；零点偏移。必须保持关系：正比图过原点；线性可非零截距；共同偏移平均后仍存在。中文标签逐字采用：x单位、y单位、截距、随机波动、共同偏移。公式及条件：检验正比y=kx：比较y/x是否近似恒定，并检查图线是否与原点相容；非零截距需解释或改模型。；重复n次取平均x̄=Σxᵢ/n可减小部分随机波动影响，但共同偏移b仍留在x̄中。；设计结构：问题 → 自变量与水平 → 因变量测法 → 控制与对照 → 重复记录 → 处理 → 条件内结论。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 1, authentic subsection 1.2. Display the original Chinese title exactly: 正比、线性与实验偏移. Topic-specific scientific requirements and instructional purpose: Draw accurately scaled plots of y=2x and y=2x+1 with labelled axes and intercepts. Separately show random scatter around a shifted mean to explain why averaging does not remove a common zero offset. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 两坐标图；y=2x；y=2x+1；重复读数；零点偏移. Preserve the following Chinese label strings exactly: x单位、y单位、截距、随机波动、共同偏移. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 检验正比y=kx：比较y/x是否近似恒定，并检查图线是否与原点相容；非零截距需解释或改模型。；重复n次取平均x̄=Σxᵢ/n可减小部分随机波动影响，但共同偏移b仍留在x̄中。；设计结构：问题 → 自变量与水平 → 因变量测法 → 控制与对照 → 重复记录 → 处理 → 条件内结论。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：正比图过原点；线性可非零截距；共同偏移平均后仍存在。不得把物理学的研究方法画成另一知识主题；不得改动x单位、y单位、截距、随机波动、共同偏移的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 正比图过原点
- 线性可非零截距
- 共同偏移平均后仍存在
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/1-1-physics-an-introduction

旧图复用：未有匹配图，宜确定性坐标绘图。实际匹配：无。

## 物理 第1章 · 1.3 怎样学好高中物理

ID：B05-PHYS01-1-3；优先级：P2；状态：not_produced。

用途：把题干转成对象过程与条件；用多种复核定位解题错误。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：对象与阶段；受力/状态示意；方法选择节点；单位与回代检查；变式自测。

关系：选法由条件决定而非关键词；负号先解释物理意义；复核有多种互补方法。

文字：对象、条件、原理、单位、方向、验算。

公式与单位：解题链：题意与对象 → 已知未知 → 方法条件 → 原理关系 → 符号推导 → 统一单位计算 → 答案解释 → 多项复核。；若同一过程匀加速，v=v₀+at；使用前必须把速度、时间与加速度对应到同一段。；量纲复核以速度为例：[at]=(m/s²)×s=m/s；即使通过仍需核初值、符号和条件。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第1章《物理学简介》真实小节1.3《怎样学好高中物理》制作《条件驱动的物理解题流程》教学图。学习目的：把题干转成对象过程与条件；用多种复核定位解题错误。本图是有条件的科学模型，非实测图或官方考题。必须出现：对象与阶段；受力/状态示意；方法选择节点；单位与回代检查；变式自测。必须保持关系：选法由条件决定而非关键词；负号先解释物理意义；复核有多种互补方法。中文标签逐字采用：对象、条件、原理、单位、方向、验算。公式及条件：解题链：题意与对象 → 已知未知 → 方法条件 → 原理关系 → 符号推导 → 统一单位计算 → 答案解释 → 多项复核。；若同一过程匀加速，v=v₀+at；使用前必须把速度、时间与加速度对应到同一段。；量纲复核以速度为例：[at]=(m/s²)×s=m/s；即使通过仍需核初值、符号和条件。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 1, authentic subsection 1.3. Display the original Chinese title exactly: 条件驱动的物理解题流程. Topic-specific scientific requirements and instructional purpose: Create a decision-oriented physics-solving flow from object and process to model conditions, symbolic equations, unit conversion and independent checks. Show that a negative velocity means direction whereas a negative ordinary mass requires model review. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 对象与阶段；受力/状态示意；方法选择节点；单位与回代检查；变式自测. Preserve the following Chinese label strings exactly: 对象、条件、原理、单位、方向、验算. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 解题链：题意与对象 → 已知未知 → 方法条件 → 原理关系 → 符号推导 → 统一单位计算 → 答案解释 → 多项复核。；若同一过程匀加速，v=v₀+at；使用前必须把速度、时间与加速度对应到同一段。；量纲复核以速度为例：[at]=(m/s²)×s=m/s；即使通过仍需核初值、符号和条件。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：选法由条件决定而非关键词；负号先解释物理意义；复核有多种互补方法。不得把怎样学好高中物理画成另一知识主题；不得改动对象、条件、原理、单位、方向、验算的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 选法由条件决定而非关键词
- 负号先解释物理意义
- 复核有多种互补方法
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/1-2-physical-quantities-and-units

旧图复用：可使用页面文字关系图。实际匹配：无。

## 物理 第2章 · 2.1 物理量的测量和单位

ID：B05-PHYS02-2-1；优先级：P0；状态：not_produced。

用途：以SI单位和操作定义表达测量；由仪器结构选择读数与校正方法。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：主尺；游标；零点对照；面积体积单位框。

关系：指定0.02 mm分度；第7格确实重合；正零偏减去。

文字：12 mm、第7格、0.02 mm、读数12.14 mm、校正12.10 mm。

公式与单位：1 cm=10⁻² m；1 cm²=10⁻⁴ m²；1 cm³=10⁻⁶ m³。；游标读数=主尺值+重合格数×给定分度值；零点校正x=x读−e。；ρ=m/V，若m用kg且V用m³，则ρ单位kg/m³；单位换算先于数值运算。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第2章《物理量的测量、单位和数据处理》真实小节2.1《物理量的测量和单位》制作《卡尺读数与有符号零点校正》教学图。学习目的：以SI单位和操作定义表达测量；由仪器结构选择读数与校正方法。本图是有条件的科学模型，非实测图或官方考题。必须出现：主尺；游标；零点对照；面积体积单位框。必须保持关系：指定0.02 mm分度；第7格确实重合；正零偏减去。中文标签逐字采用：12 mm、第7格、0.02 mm、读数12.14 mm、校正12.10 mm。公式及条件：1 cm=10⁻² m；1 cm²=10⁻⁴ m²；1 cm³=10⁻⁶ m³。；游标读数=主尺值+重合格数×给定分度值；零点校正x=x读−e。；ρ=m/V，若m用kg且V用m³，则ρ单位kg/m³；单位换算先于数值运算。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 2, authentic subsection 2.1. Display the original Chinese title exactly: 卡尺读数与有符号零点校正. Topic-specific scientific requirements and instructional purpose: Construct a mathematically consistent vernier with 0.02 mm least count, main-scale reading 12 mm and seventh matching division. Show a positive 0.04 mm zero offset and corrected result 12.10 mm. Do not improvise incompatible scale spacing. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 主尺；游标；零点对照；面积体积单位框. Preserve the following Chinese label strings exactly: 12 mm、第7格、0.02 mm、读数12.14 mm、校正12.10 mm. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 1 cm=10⁻² m；1 cm²=10⁻⁴ m²；1 cm³=10⁻⁶ m³。；游标读数=主尺值+重合格数×给定分度值；零点校正x=x读−e。；ρ=m/V，若m用kg且V用m³，则ρ单位kg/m³；单位换算先于数值运算。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：指定0.02 mm分度；第7格确实重合；正零偏减去。不得把物理量的测量和单位画成另一知识主题；不得改动12 mm、第7格、0.02 mm、读数12.14 mm、校正12.10 mm的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 指定0.02 mm分度
- 第7格确实重合
- 正零偏减去
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/1-2-physical-quantities-and-units

旧图复用：无完整匹配；精确刻度必须确定性绘图。实际匹配：无。

## 物理 第2章 · 2.2 误差和有效数字

ID：B05-PHYS02-2-2；优先级：P1；状态：not_produced。

用途：区分偏差来源与不确定性表达；按运算与测量限制报告有效数字。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：真值参考；两组读数分布；偏移；绝对范围；科学记数法。

关系：集中不等于无偏；随机散布与系统偏移可并存；前导零不计有效位。

文字：准确性、重复性、Δx、Δx/|x|、4.50×10⁻³。

公式与单位：相对不确定性r=Δx/|x|；百分比为100r%。；例：x=(20.0±0.2) cm，r=0.2/20.0=1%。；小误差最大界限近似：z=xy或x/y时Δz/|z|≈Δx/|x|+Δy/|y|；这不是无条件适用的统计标准差公式。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第2章《物理量的测量、单位和数据处理》真实小节2.2《误差和有效数字》制作《测量离散、偏移与有效位》教学图。学习目的：区分偏差来源与不确定性表达；按运算与测量限制报告有效数字。本图是有条件的科学模型，非实测图或官方考题。必须出现：真值参考；两组读数分布；偏移；绝对范围；科学记数法。必须保持关系：集中不等于无偏；随机散布与系统偏移可并存；前导零不计有效位。中文标签逐字采用：准确性、重复性、Δx、Δx/|x|、4.50×10⁻³。公式及条件：相对不确定性r=Δx/|x|；百分比为100r%。；例：x=(20.0±0.2) cm，r=0.2/20.0=1%。；小误差最大界限近似：z=xy或x/y时Δz/|z|≈Δx/|x|+Δy/|y|；这不是无条件适用的统计标准差公式。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 2, authentic subsection 2.2. Display the original Chinese title exactly: 测量离散、偏移与有效位. Topic-specific scientific requirements and instructional purpose: Show two measurement distributions with independent spread and bias relative to a stated reference. Distinguish absolute uncertainty from relative uncertainty and annotate the three significant figures in 0.00450 without implying an exact universal probability for ± notation. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 真值参考；两组读数分布；偏移；绝对范围；科学记数法. Preserve the following Chinese label strings exactly: 准确性、重复性、Δx、Δx/|x|、4.50×10⁻³. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 相对不确定性r=Δx/|x|；百分比为100r%。；例：x=(20.0±0.2) cm，r=0.2/20.0=1%。；小误差最大界限近似：z=xy或x/y时Δz/|z|≈Δx/|x|+Δy/|y|；这不是无条件适用的统计标准差公式。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：集中不等于无偏；随机散布与系统偏移可并存；前导零不计有效位。不得把误差和有效数字画成另一知识主题；不得改动准确性、重复性、Δx、Δx/|x|、4.50×10⁻³的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 集中不等于无偏
- 随机散布与系统偏移可并存
- 前导零不计有效位
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/1-3-accuracy-precision-and-significant-figures

旧图复用：无完全对应图。实际匹配：无。

## 物理 第2章 · 2.3 科学记数法和数量级

ID：B05-PHYS02-2-3；优先级：P1；状态：not_produced。

用途：规范表示极大极小量并估算；用数量级检查模型结果。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：十进制小数；标准系数；十次幂数轴；√10分界。

关系：系数1至10；对数轴等距表示相同倍数；数量级约定显式标注。

文字：10⁻⁴、10⁰、10⁴、5.60×10⁻⁴、最近十次幂。

公式与单位：(a×10ᵐ)(b×10ⁿ)=ab×10ᵐ⁺ⁿ；相除则系数相除、指数相减。；加减必须先同幂：3×10³+2×10²=(3+0.2)×10³=3.2×10³。；最近十次幂的对数分界：a×10ⁿ到10ⁿ和10ⁿ⁺¹等距时log₁₀a=1/2，即a=√10；若用另一约定须注明。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第2章《物理量的测量、单位和数据处理》真实小节2.3《科学记数法和数量级》制作《科学记数与对数尺度》教学图。学习目的：规范表示极大极小量并估算；用数量级检查模型结果。本图是有条件的科学模型，非实测图或官方考题。必须出现：十进制小数；标准系数；十次幂数轴；√10分界。必须保持关系：系数1至10；对数轴等距表示相同倍数；数量级约定显式标注。中文标签逐字采用：10⁻⁴、10⁰、10⁴、5.60×10⁻⁴、最近十次幂。公式及条件：(a×10ᵐ)(b×10ⁿ)=ab×10ᵐ⁺ⁿ；相除则系数相除、指数相减。；加减必须先同幂：3×10³+2×10²=(3+0.2)×10³=3.2×10³。；最近十次幂的对数分界：a×10ⁿ到10ⁿ和10ⁿ⁺¹等距时log₁₀a=1/2，即a=√10；若用另一约定须注明。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 2, authentic subsection 2.3. Display the original Chinese title exactly: 科学记数与对数尺度. Topic-specific scientific requirements and instructional purpose: Create a labelled logarithmic powers-of-ten scale and illustrate 0.000560=5.60×10^-4. If showing nearest power of ten, explicitly mark the multiplicative midpoint sqrt(10), not an arithmetic midpoint. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 十进制小数；标准系数；十次幂数轴；√10分界. Preserve the following Chinese label strings exactly: 10⁻⁴、10⁰、10⁴、5.60×10⁻⁴、最近十次幂. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: (a×10ᵐ)(b×10ⁿ)=ab×10ᵐ⁺ⁿ；相除则系数相除、指数相减。；加减必须先同幂：3×10³+2×10²=(3+0.2)×10³=3.2×10³。；最近十次幂的对数分界：a×10ⁿ到10ⁿ和10ⁿ⁺¹等距时log₁₀a=1/2，即a=√10；若用另一约定须注明。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：系数1至10；对数轴等距表示相同倍数；数量级约定显式标注。不得把科学记数法和数量级画成另一知识主题；不得改动10⁻⁴、10⁰、10⁴、5.60×10⁻⁴、最近十次幂的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 系数1至10
- 对数轴等距表示相同倍数
- 数量级约定显式标注
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/1-4-approximation

旧图复用：需确定性数轴，无需AI辅助画。实际匹配：无。

## 物理 第2章 · 2.4 物理公式和图象

ID：B05-PHYS02-2-4；优先级：P0；状态：not_produced。

用途：由图象解释斜率截距及面积；辨认变量关系和适用区间。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：x-t直线；v-t正负矩形；y对x²直线。

关系：x-t过(1,3)(5,11)；v-t面积+6和−2给+4；路程取绝对面积8。

文字：t/s、x/m、v/(m/s)、斜率2 m/s、截距1 m、Δx=4 m。

公式与单位：斜率m=Δy/Δx，单位[y]/[x]；截距b在y=mx+b中与y同单位。；v-t图：Δx=图线与时间轴之间的有向面积；负速度部分给负位移。；若y=kx²，令X=x²，则y=kX；X单位为[x]²，斜率k单位[y]/[x]²。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第2章《物理量的测量、单位和数据处理》真实小节2.4《物理公式和图象》制作《图象的斜率、截距与有向面积》教学图。学习目的：由图象解释斜率截距及面积；辨认变量关系和适用区间。本图是有条件的科学模型，非实测图或官方考题。必须出现：x-t直线；v-t正负矩形；y对x²直线。必须保持关系：x-t过(1,3)(5,11)；v-t面积+6和−2给+4；路程取绝对面积8。中文标签逐字采用：t/s、x/m、v/(m/s)、斜率2 m/s、截距1 m、Δx=4 m。公式及条件：斜率m=Δy/Δx，单位[y]/[x]；截距b在y=mx+b中与y同单位。；v-t图：Δx=图线与时间轴之间的有向面积；负速度部分给负位移。；若y=kx²，令X=x²，则y=kX；X单位为[x]²，斜率k单位[y]/[x]²。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 2, authentic subsection 2.4. Display the original Chinese title exactly: 图象的斜率、截距与有向面积. Topic-specific scientific requirements and instructional purpose: Draw three exact coordinate panels: x=2t+1 through (1,3) and (5,11); v=3 for 0–2 s and v=-1 for 2–4 s with signed areas +6 and -2 m; a separate y versus x-squared linearization with squared horizontal units. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: x-t直线；v-t正负矩形；y对x²直线. Preserve the following Chinese label strings exactly: t/s、x/m、v/(m/s)、斜率2 m/s、截距1 m、Δx=4 m. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 斜率m=Δy/Δx，单位[y]/[x]；截距b在y=mx+b中与y同单位。；v-t图：Δx=图线与时间轴之间的有向面积；负速度部分给负位移。；若y=kx²，令X=x²，则y=kX；X单位为[x]²，斜率k单位[y]/[x]²。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：x-t过(1,3)(5,11)；v-t面积+6和−2给+4；路程取绝对面积8。不得把物理公式和图象画成另一知识主题；不得改动t/s、x/m、v/(m/s)、斜率2 m/s、截距1 m、Δx=4 m的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- x-t过(1,3)(5,11)
- v-t面积+6和−2给+4
- 路程取绝对面积8
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/2-8-graphical-analysis-of-one-dimensional-motion

旧图复用：V22运动图可作补充，需避免重复并保持数值一致。实际匹配：无。

## 物理 第5章 · 5.1 共点力作用下物体的平衡

ID：B05-PHYS05-5-1；优先级：P0；状态：not_produced。

用途：由平衡条件建立分量方程；用受力图检查约束与解的可行性。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：结点；两根对称绳；重量；张力分量；水平接触物体。

关系：θ从竖直量；2Tcosθ=mg；静摩擦小于等于上限而非恒取上限。

文字：θ、T、Tcosθ、mg、|fₛ|≤μₛN。

公式与单位：平面共点力平衡：ΣFₓ=0，ΣFᵧ=0。；两对称绳各与竖直夹角θ，2T cosθ=mg，故T=mg/(2 cosθ)，需cosθ>0且绳能承受。；静摩擦先求所需f，再检验|f|≤μₛN；等号只描述临界情况。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第5章《静力学》真实小节5.1《共点力作用下物体的平衡》制作《对称悬吊与静摩擦约束》教学图。学习目的：由平衡条件建立分量方程；用受力图检查约束与解的可行性。本图是有条件的科学模型，非实测图或官方考题。必须出现：结点；两根对称绳；重量；张力分量；水平接触物体。必须保持关系：θ从竖直量；2Tcosθ=mg；静摩擦小于等于上限而非恒取上限。中文标签逐字采用：θ、T、Tcosθ、mg、|fₛ|≤μₛN。公式及条件：平面共点力平衡：ΣFₓ=0，ΣFᵧ=0。；两对称绳各与竖直夹角θ，2T cosθ=mg，故T=mg/(2 cosθ)，需cosθ>0且绳能承受。；静摩擦先求所需f，再检验|f|≤μₛN；等号只描述临界情况。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 5, authentic subsection 5.1. Display the original Chinese title exactly: 对称悬吊与静摩擦约束. Topic-specific scientific requirements and instructional purpose: Draw a symmetric suspension with each rope angle measured from the vertical, showing 2T cos(theta)=mg. In a separate horizontal-contact free-body diagram, distinguish required static friction from its maximum and do not include reaction forces acting on other bodies. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 结点；两根对称绳；重量；张力分量；水平接触物体. Preserve the following Chinese label strings exactly: θ、T、Tcosθ、mg、|fₛ|≤μₛN. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 平面共点力平衡：ΣFₓ=0，ΣFᵧ=0。；两对称绳各与竖直夹角θ，2T cosθ=mg，故T=mg/(2 cosθ)，需cosθ>0且绳能承受。；静摩擦先求所需f，再检验|f|≤μₛN；等号只描述临界情况。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：θ从竖直量；2Tcosθ=mg；静摩擦小于等于上限而非恒取上限。不得把共点力作用下物体的平衡画成另一知识主题；不得改动θ、T、Tcosθ、mg、|fₛ|≤μₛN的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- θ从竖直量
- 2Tcosθ=mg
- 静摩擦小于等于上限而非恒取上限
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/9-1-the-first-condition-for-equilibrium

旧图复用：V22向量图可局部参考，不替代本题受力几何。实际匹配：无。

## 物理 第5章 · 5.2 力矩的平衡 平面力系的平衡

ID：B05-PHYS05-5-2；优先级：P0；状态：not_produced。

用途：用垂直力臂计算力矩；联合平动转动条件求平面刚体平衡。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：支点O；r=0.8 m杆；50 N斜力；垂直力臂0.4 m；双支承杆。

关系：夹角30°；ℓ=r sinθ；力臂画到延长作用线的垂线；反力方向符合约束。

文字：O、r、θ=30°、ℓ=0.4 m、τ=20 N·m。

公式与单位：τ=Fℓ=Fr sinθ，其中ℓ为支点到作用线的垂直距离。；平面静力平衡：ΣFₓ=0，ΣFᵧ=0，Στ_O=0。；力偶大小相等反向平行，间距d时合力0而合力矩Fd；关于不同点力偶矩相同。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第5章《静力学》真实小节5.2《力矩的平衡 平面力系的平衡》制作《力臂与平面杆的平衡》教学图。学习目的：用垂直力臂计算力矩；联合平动转动条件求平面刚体平衡。本图是有条件的科学模型，非实测图或官方考题。必须出现：支点O；r=0.8 m杆；50 N斜力；垂直力臂0.4 m；双支承杆。必须保持关系：夹角30°；ℓ=r sinθ；力臂画到延长作用线的垂线；反力方向符合约束。中文标签逐字采用：O、r、θ=30°、ℓ=0.4 m、τ=20 N·m。公式及条件：τ=Fℓ=Fr sinθ，其中ℓ为支点到作用线的垂直距离。；平面静力平衡：ΣFₓ=0，ΣFᵧ=0，Στ_O=0。；力偶大小相等反向平行，间距d时合力0而合力矩Fd；关于不同点力偶矩相同。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 5, authentic subsection 5.2. Display the original Chinese title exactly: 力臂与平面杆的平衡. Topic-specific scientific requirements and instructional purpose: Draw a 0.8 m position vector and a 50 N force at 30 degrees to it. Construct the perpendicular distance from pivot O to the force line as 0.4 m, giving torque 20 N m. Distinguish the full rod length from the moment arm. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 支点O；r=0.8 m杆；50 N斜力；垂直力臂0.4 m；双支承杆. Preserve the following Chinese label strings exactly: O、r、θ=30°、ℓ=0.4 m、τ=20 N·m. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: τ=Fℓ=Fr sinθ，其中ℓ为支点到作用线的垂直距离。；平面静力平衡：ΣFₓ=0，ΣFᵧ=0，Στ_O=0。；力偶大小相等反向平行，间距d时合力0而合力矩Fd；关于不同点力偶矩相同。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：夹角30°；ℓ=r sinθ；力臂画到延长作用线的垂线；反力方向符合约束。不得把力矩的平衡 平面力系的平衡画成另一知识主题；不得改动O、r、θ=30°、ℓ=0.4 m、τ=20 N·m的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 夹角30°
- ℓ=r sinθ
- 力臂画到延长作用线的垂线
- 反力方向符合约束
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/9-2-the-second-condition-for-equilibrium

旧图复用：现有力图不能代替准确垂距图。实际匹配：无。

## 物理 第5章 · 5.3 平行力系

ID：B05-PHYS05-5-3；优先级：P0；状态：not_produced。

用途：求平行力的合力与作用线；用力矩确定重心并判断稳定性。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：同向10/30 N；反向30/10 N；x轴；合力作用线；支撑区。

关系：同向合力x=1.5 m；反向合力x=−1 m；R=0不强画有限单力。

文字：x/m、40 N、20 N、ΣFᵢxᵢ、支撑范围。

公式与单位：平行力沿共同方向取正：R=ΣFᵢ；当R≠0时，x_R=ΣFᵢxᵢ/R，由力矩等效确定。；均匀重力场：x_G=Σmᵢxᵢ/Σmᵢ；g相同可在分子分母相消。；R=0而ΣFᵢxᵢ≠0时为非零力偶，不能用一个单力等效。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第5章《静力学》真实小节5.3《平行力系》制作《平行力合力位置与重心》教学图。学习目的：求平行力的合力与作用线；用力矩确定重心并判断稳定性。本图是有条件的科学模型，非实测图或官方考题。必须出现：同向10/30 N；反向30/10 N；x轴；合力作用线；支撑区。必须保持关系：同向合力x=1.5 m；反向合力x=−1 m；R=0不强画有限单力。中文标签逐字采用：x/m、40 N、20 N、ΣFᵢxᵢ、支撑范围。公式及条件：平行力沿共同方向取正：R=ΣFᵢ；当R≠0时，x_R=ΣFᵢxᵢ/R，由力矩等效确定。；均匀重力场：x_G=Σmᵢxᵢ/Σmᵢ；g相同可在分子分母相消。；R=0而ΣFᵢxᵢ≠0时为非零力偶，不能用一个单力等效。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 5, authentic subsection 5.3. Display the original Chinese title exactly: 平行力合力位置与重心. Topic-specific scientific requirements and instructional purpose: Construct exact parallel-force diagrams: downward 10 N at x=0 and 30 N at x=2 m give 40 N at x=1.5 m; downward 30 N at x=0 and upward 10 N at x=2 give downward 20 N at x=-1 m. Keep force and moment equivalence visible. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 同向10/30 N；反向30/10 N；x轴；合力作用线；支撑区. Preserve the following Chinese label strings exactly: x/m、40 N、20 N、ΣFᵢxᵢ、支撑范围. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 平行力沿共同方向取正：R=ΣFᵢ；当R≠0时，x_R=ΣFᵢxᵢ/R，由力矩等效确定。；均匀重力场：x_G=Σmᵢxᵢ/Σmᵢ；g相同可在分子分母相消。；R=0而ΣFᵢxᵢ≠0时为非零力偶，不能用一个单力等效。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：同向合力x=1.5 m；反向合力x=−1 m；R=0不强画有限单力。不得把平行力系画成另一知识主题；不得改动x/m、40 N、20 N、ΣFᵢxᵢ、支撑范围的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 同向合力x=1.5 m
- 反向合力x=−1 m
- R=0不强画有限单力
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/9-3-stability

旧图复用：需准确比例和带符号位置的新SVG。实际匹配：无。

## 物理 第7章 · 7.1 功和功率

ID：B05-PHYS07-7-1；优先级：P0；状态：not_produced。

用途：由力与位移判断功的正负；区分平均功率和瞬时功率。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：斜拉力20 N；水平位移5 m；60°夹角；输入输出损耗功率。

关系：沿位移分量10 N；W=50 J；输入1000=输出800+损耗200 W。

文字：θ=60°、Fcosθ、W/J、P/W、η=80%。

公式与单位：恒力功W=Fs cosθ；多个力总功W总=ΣWᵢ。；P平均=W/Δt；瞬时P=Fv cosθ。；η=W有用/W输入=P输出/P输入（同时间边界）；1 kWh=1000 W×3600 s=3.6×10⁶ J。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第7章《功与能》真实小节7.1《功和功率》制作《功的分量与功率边界》教学图。学习目的：由力与位移判断功的正负；区分平均功率和瞬时功率。本图是有条件的科学模型，非实测图或官方考题。必须出现：斜拉力20 N；水平位移5 m；60°夹角；输入输出损耗功率。必须保持关系：沿位移分量10 N；W=50 J；输入1000=输出800+损耗200 W。中文标签逐字采用：θ=60°、Fcosθ、W/J、P/W、η=80%。公式及条件：恒力功W=Fs cosθ；多个力总功W总=ΣWᵢ。；P平均=W/Δt；瞬时P=Fv cosθ。；η=W有用/W输入=P输出/P输入（同时间边界）；1 kWh=1000 W×3600 s=3.6×10⁶ J。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 7, authentic subsection 7.1. Display the original Chinese title exactly: 功的分量与功率边界. Topic-specific scientific requirements and instructional purpose: Show a 20 N force at 60 degrees to a 5 m horizontal displacement, giving 50 J of work. Add a separate power balance of 1000 W input, 800 W useful output and 200 W loss; do not imply uniform motion means zero driving power. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 斜拉力20 N；水平位移5 m；60°夹角；输入输出损耗功率. Preserve the following Chinese label strings exactly: θ=60°、Fcosθ、W/J、P/W、η=80%. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 恒力功W=Fs cosθ；多个力总功W总=ΣWᵢ。；P平均=W/Δt；瞬时P=Fv cosθ。；η=W有用/W输入=P输出/P输入（同时间边界）；1 kWh=1000 W×3600 s=3.6×10⁶ J。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：沿位移分量10 N；W=50 J；输入1000=输出800+损耗200 W。不得把功和功率画成另一知识主题；不得改动θ=60°、Fcosθ、W/J、P/W、η=80%的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 沿位移分量10 N
- W=50 J
- 输入1000=输出800+损耗200 W
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/7-1-work-the-scientific-definition

旧图复用：V22相关功图可核后复用，题值不同须说明。实际匹配：无。

## 物理 第7章 · 7.2 恒力与变力的功

ID：B05-PHYS07-7-2；优先级：P0；状态：reuse_partial_remaining_pending。

用途：由力位移图求有向功；用分段与面积处理变力并核条件。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：2到10 N线性图；正负分段图；弹力/外力对称图。

关系：0至4 m面积24 J；正负面积可抵消；外力与弹力方向相反。

文字：Fₓ/N、x/m、24 J、F外=kx、F弹=−kx。

公式与单位：一维W为Fₓ-x图有向面积；分段功可相加。；线性由F₁变F₂、位移Δx时W=(F₁+F₂)Δx/2；一般非线性不可只取端点平均。；胡克范围：0至x的准静态外力功+kx²/2，弹力功−kx²/2。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第7章《功与能》真实小节7.2《恒力与变力的功》制作《力位移面积与弹簧功》教学图。学习目的：由力位移图求有向功；用分段与面积处理变力并核条件。本图是有条件的科学模型，非实测图或官方考题。必须出现：2到10 N线性图；正负分段图；弹力/外力对称图。必须保持关系：0至4 m面积24 J；正负面积可抵消；外力与弹力方向相反。中文标签逐字采用：Fₓ/N、x/m、24 J、F外=kx、F弹=−kx。公式及条件：一维W为Fₓ-x图有向面积；分段功可相加。；线性由F₁变F₂、位移Δx时W=(F₁+F₂)Δx/2；一般非线性不可只取端点平均。；胡克范围：0至x的准静态外力功+kx²/2，弹力功−kx²/2。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 7, authentic subsection 7.2. Display the original Chinese title exactly: 力位移面积与弹簧功. Topic-specific scientific requirements and instructional purpose: Plot F_x increasing linearly from 2 to 10 N over 0 to 4 m and shade exactly 24 J. In a separate Hookean spring panel distinguish applied quasi-static force +kx from restoring force -kx, with signed work areas. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 2到10 N线性图；正负分段图；弹力/外力对称图. Preserve the following Chinese label strings exactly: Fₓ/N、x/m、24 J、F外=kx、F弹=−kx. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 一维W为Fₓ-x图有向面积；分段功可相加。；线性由F₁变F₂、位移Δx时W=(F₁+F₂)Δx/2；一般非线性不可只取端点平均。；胡克范围：0至x的准静态外力功+kx²/2，弹力功−kx²/2。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：0至4 m面积24 J；正负面积可抵消；外力与弹力方向相反。不得把恒力与变力的功画成另一知识主题；不得改动Fₓ/N、x/m、24 J、F外=kx、F弹=−kx的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 0至4 m面积24 J
- 正负面积可抵消
- 外力与弹力方向相反
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/7-2-kinetic-energy-and-the-work-energy-theorem

旧图复用：V22 P25力位移图可复用经核数值，勿重复展示同图。实际匹配：assets/v22/physics/P25_work_force_displacement_area_c54288d1e.svg。

## 物理 第7章 · 7.3 动能

ID：B05-PHYS07-7-3；优先级：P0；状态：not_produced。

用途：由总功求动能及速度变化；区分动能、动量和参考系依赖。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：同质量不同速度；K对v²直线；恒阻力制动图；停距标记。

关系：速度2倍K4倍；恒阻力停距与初速平方正比；不画负动能实态。

文字：K=mv²/2、W总=ΔK、10 m、40 m、不含反应距离。

公式与单位：由Fs=mas、2as=v²−u²，得W总=m(v²−u²)/2。；K=mv²/2；p=mv时K=p²/(2m)，仅同一经典平动模型。；恒定反向阻力f使物体停止：fs=mu²/2，s=mu²/(2f)，需阻力恒定且不含反应阶段。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第7章《功与能》真实小节7.3《动能》制作《动能平方关系与制动距离》教学图。学习目的：由总功求动能及速度变化；区分动能、动量和参考系依赖。本图是有条件的科学模型，非实测图或官方考题。必须出现：同质量不同速度；K对v²直线；恒阻力制动图；停距标记。必须保持关系：速度2倍K4倍；恒阻力停距与初速平方正比；不画负动能实态。中文标签逐字采用：K=mv²/2、W总=ΔK、10 m、40 m、不含反应距离。公式及条件：由Fs=mas、2as=v²−u²，得W总=m(v²−u²)/2。；K=mv²/2；p=mv时K=p²/(2m)，仅同一经典平动模型。；恒定反向阻力f使物体停止：fs=mu²/2，s=mu²/(2f)，需阻力恒定且不含反应阶段。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 7, authentic subsection 7.3. Display the original Chinese title exactly: 动能平方关系与制动距离. Topic-specific scientific requirements and instructional purpose: Show kinetic energy proportional to speed squared and compare ideal constant-force braking distances 10 m and 40 m for initial speeds 10 and 20 m/s. State that reaction distance and road variability are excluded, and never depict negative kinetic energy as a real state. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 同质量不同速度；K对v²直线；恒阻力制动图；停距标记. Preserve the following Chinese label strings exactly: K=mv²/2、W总=ΔK、10 m、40 m、不含反应距离. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 由Fs=mas、2as=v²−u²，得W总=m(v²−u²)/2。；K=mv²/2；p=mv时K=p²/(2m)，仅同一经典平动模型。；恒定反向阻力f使物体停止：fs=mu²/2，s=mu²/(2f)，需阻力恒定且不含反应阶段。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：速度2倍K4倍；恒阻力停距与初速平方正比；不画负动能实态。不得把动能画成另一知识主题；不得改动K=mv²/2、W总=ΔK、10 m、40 m、不含反应距离的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 速度2倍K4倍
- 恒阻力停距与初速平方正比
- 不画负动能实态
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/7-2-kinetic-energy-and-the-work-energy-theorem

旧图复用：相关V22能量图可补充，需核是否对应本题。实际匹配：无。

## 物理 第7章 · 7.4 势能

ID：B05-PHYS07-7-4；优先级：P0；状态：reuse_partial_remaining_pending。

用途：用保守力功定义势能差；分别求重力与弹性势能并说明零点。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：同高度两零点；初末高度；自然长弹簧；伸长与压缩。

关系：改零点差值不变；伸压同大小U相同；弹力恢复方向相反。

文字：ΔU、W保=−ΔU、x相对自然长、U_s=kx²/2。

公式与单位：W重=mg(h_i−h_f)=−ΔU_g；近地面U_g=mgh+C。；U_s=kx²/2，x为自然长起算的伸长或压缩；W弹=U_s初−U_s末。；改零点只加同一常数，不改势能差、保守力功或可观测运动。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第7章《功与能》真实小节7.4《势能》制作《势能零点和弹簧形变》教学图。学习目的：用保守力功定义势能差；分别求重力与弹性势能并说明零点。本图是有条件的科学模型，非实测图或官方考题。必须出现：同高度两零点；初末高度；自然长弹簧；伸长与压缩。必须保持关系：改零点差值不变；伸压同大小U相同；弹力恢复方向相反。中文标签逐字采用：ΔU、W保=−ΔU、x相对自然长、U_s=kx²/2。公式及条件：W重=mg(h_i−h_f)=−ΔU_g；近地面U_g=mgh+C。；U_s=kx²/2，x为自然长起算的伸长或压缩；W弹=U_s初−U_s末。；改零点只加同一常数，不改势能差、保守力功或可观测运动。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 7, authentic subsection 7.4. Display the original Chinese title exactly: 势能零点和弹簧形变. Topic-specific scientific requirements and instructional purpose: Show two gravitational potential references yielding the same delta U, and an ideal spring at natural length, equal extension and compression. Mark deformation x from natural length and opposite restoring-force arrows with equal stored energies. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 同高度两零点；初末高度；自然长弹簧；伸长与压缩. Preserve the following Chinese label strings exactly: ΔU、W保=−ΔU、x相对自然长、U_s=kx²/2. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: W重=mg(h_i−h_f)=−ΔU_g；近地面U_g=mgh+C。；U_s=kx²/2，x为自然长起算的伸长或压缩；W弹=U_s初−U_s末。；改零点只加同一常数，不改势能差、保守力功或可观测运动。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：改零点差值不变；伸压同大小U相同；弹力恢复方向相反。不得把势能画成另一知识主题；不得改动ΔU、W保=−ΔU、x相对自然长、U_s=kx²/2的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 改零点差值不变
- 伸压同大小U相同
- 弹力恢复方向相反
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/7-3-gravitational-potential-energy

旧图复用：V22 P18弹簧能图可复用，需说明自然长与零点。实际匹配：assets/v22/physics/P18_spring_elastic_energy_7217b0ffd.svg。

## 物理 第7章 · 7.5 机械能守恒定律

ID：B05-PHYS07-7-5；优先级：P0；状态：reuse_partial_remaining_pending。

用途：按做功类别判定机械能是否守恒；用能量收支求速度高度及耗散。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：高低两状态；K/U能量条；摩擦转出箭头；弹簧释放；轨道接触检查。

关系：初机械76末68差8；W其他=ΔE机械；能量可达与N约束分开。

文字：K、U_g、U_s、W其他、N≥0另查。

公式与单位：由W总=ΔK及W保=−ΔU，得Δ(K+U)=W其他。；W其他=0时K初+U初=K末+U末；有摩擦等时保留其功。；近地面无耗散下v²=v₀²+2g(h₀−h)，只给速率关系，接触与方向需另判。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第7章《功与能》真实小节7.5《机械能守恒定律》制作《机械能收支与适用条件》教学图。学习目的：按做功类别判定机械能是否守恒；用能量收支求速度高度及耗散。本图是有条件的科学模型，非实测图或官方考题。必须出现：高低两状态；K/U能量条；摩擦转出箭头；弹簧释放；轨道接触检查。必须保持关系：初机械76末68差8；W其他=ΔE机械；能量可达与N约束分开。中文标签逐字采用：K、U_g、U_s、W其他、N≥0另查。公式及条件：由W总=ΔK及W保=−ΔU，得Δ(K+U)=W其他。；W其他=0时K初+U初=K末+U末；有摩擦等时保留其功。；近地面无耗散下v²=v₀²+2g(h₀−h)，只给速率关系，接触与方向需另判。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 7, authentic subsection 7.5. Display the original Chinese title exactly: 机械能收支与适用条件. Topic-specific scientific requirements and instructional purpose: Draw energy-accounting bars with 76 J initial mechanical energy and 68 J final plus 8 J transferred to other forms. Show conservation only when other work is zero, and keep track-contact force constraints as a separate check. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 高低两状态；K/U能量条；摩擦转出箭头；弹簧释放；轨道接触检查. Preserve the following Chinese label strings exactly: K、U_g、U_s、W其他、N≥0另查. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 由W总=ΔK及W保=−ΔU，得Δ(K+U)=W其他。；W其他=0时K初+U初=K末+U末；有摩擦等时保留其功。；近地面无耗散下v²=v₀²+2g(h₀−h)，只给速率关系，接触与方向需另判。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：初机械76末68差8；W其他=ΔE机械；能量可达与N约束分开。不得把机械能守恒定律画成另一知识主题；不得改动K、U_g、U_s、W其他、N≥0另查的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 初机械76末68差8
- W其他=ΔE机械
- 能量可达与N约束分开
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/7-6-conservation-of-energy

旧图复用：V22 P07可复核复用，需注明具体示例区别。实际匹配：assets/v22/physics/P07_mechanical_energy_conservation_295e7839a.svg。

## 物理 第7章 · 7.6 质量与能量

ID：B05-PHYS07-7-6；优先级：P1；状态：not_produced。

用途：区分静能、动能与系统质量变化；用质能关系换算能量并保持系统边界一致。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：初末静止容器；离开辐射箭头；外部总系统框；单位换算框。

关系：容器能量减少对应质量减少；把辐射计入时不可再漏记；静能与动能分项。

文字：E₀=mc²、ΔE=Δmc²、1 u c²≈931.5 MeV、不是全量可提取承诺。

公式与单位：静能E₀=mc²；同边界前后ΔE=Δmc²，符号需按吸收或释放解释。；本节数值题取c=3.00×10⁸ m/s；1 eV=1.602176634×10⁻¹⁹ J。；题设可用1 u c²≈931.5 MeV；质量差为u时乘该能量因子，不把u直接当kg。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第7章《功与能》真实小节7.6《质量与能量》制作《质能关系的系统边界》教学图。学习目的：区分静能、动能与系统质量变化；用质能关系换算能量并保持系统边界一致。本图是有条件的科学模型，非实测图或官方考题。必须出现：初末静止容器；离开辐射箭头；外部总系统框；单位换算框。必须保持关系：容器能量减少对应质量减少；把辐射计入时不可再漏记；静能与动能分项。中文标签逐字采用：E₀=mc²、ΔE=Δmc²、1 u c²≈931.5 MeV、不是全量可提取承诺。公式及条件：静能E₀=mc²；同边界前后ΔE=Δmc²，符号需按吸收或释放解释。；本节数值题取c=3.00×10⁸ m/s；1 eV=1.602176634×10⁻¹⁹ J。；题设可用1 u c²≈931.5 MeV；质量差为u时乘该能量因子，不把u直接当kg。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 7, authentic subsection 7.6. Display the original Chinese title exactly: 质能关系的系统边界. Topic-specific scientific requirements and instructional purpose: Show a stationary container losing radiation across a defined boundary, with corresponding mass decrease delta E/c squared. Use a larger boundary to include radiation and keep total energy accounting consistent. Separate rest energy from kinetic energy and from practically extractable fuel energy. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 初末静止容器；离开辐射箭头；外部总系统框；单位换算框. Preserve the following Chinese label strings exactly: E₀=mc²、ΔE=Δmc²、1 u c²≈931.5 MeV、不是全量可提取承诺. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 静能E₀=mc²；同边界前后ΔE=Δmc²，符号需按吸收或释放解释。；本节数值题取c=3.00×10⁸ m/s；1 eV=1.602176634×10⁻¹⁹ J。；题设可用1 u c²≈931.5 MeV；质量差为u时乘该能量因子，不把u直接当kg。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：容器能量减少对应质量减少；把辐射计入时不可再漏记；静能与动能分项。不得把质量与能量画成另一知识主题；不得改动E₀=mc²、ΔE=Δmc²、1 u c²≈931.5 MeV、不是全量可提取承诺的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 容器能量减少对应质量减少
- 把辐射计入时不可再漏记
- 静能与动能分项
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/28-6-relativistic-energy

旧图复用：无完全对应旧图；公式应SVG文字层。实际匹配：无。

## 物理 第8章 · 8.1 冲量与动量的关系

ID：B05-PHYS08-8-1；优先级：P0；状态：reuse_partial_remaining_pending。

用途：用方向和时间范围计算冲量；由力时间图求动量变化并反推平均力。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：球向左8后向右6；右正轴；三角形F-t脉冲。

关系：Δp=0.1×(6+8)=1.4；0.04×100/2=2 N·s；峰值与平均值分开。

文字：v_i=−8 m/s、v_f=+6 m/s、Δp、F/N、t/s。

公式与单位：p=mv；Δp=mv_f−mv_i，矢量或带符号分量计算。；J外=Δp；F平均=Δp/Δt，指所选时段的合外力平均值。；三角形F-t脉冲J=底×高/2；单位N·s=kg·m/s。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第8章《动量守恒定律》真实小节8.1《冲量与动量的关系》制作《反弹动量与三角形冲量》教学图。学习目的：用方向和时间范围计算冲量；由力时间图求动量变化并反推平均力。本图是有条件的科学模型，非实测图或官方考题。必须出现：球向左8后向右6；右正轴；三角形F-t脉冲。必须保持关系：Δp=0.1×(6+8)=1.4；0.04×100/2=2 N·s；峰值与平均值分开。中文标签逐字采用：v_i=−8 m/s、v_f=+6 m/s、Δp、F/N、t/s。公式及条件：p=mv；Δp=mv_f−mv_i，矢量或带符号分量计算。；J外=Δp；F平均=Δp/Δt，指所选时段的合外力平均值。；三角形F-t脉冲J=底×高/2；单位N·s=kg·m/s。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 8, authentic subsection 8.1. Display the original Chinese title exactly: 反弹动量与三角形冲量. Topic-specific scientific requirements and instructional purpose: Show signed initial and final velocities for a rebounding ball, then a separate triangular net-force pulse of height 100 N and duration 0.04 s with impulse 2 N s. Explicitly distinguish peak force from average force. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 球向左8后向右6；右正轴；三角形F-t脉冲. Preserve the following Chinese label strings exactly: v_i=−8 m/s、v_f=+6 m/s、Δp、F/N、t/s. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: p=mv；Δp=mv_f−mv_i，矢量或带符号分量计算。；J外=Δp；F平均=Δp/Δt，指所选时段的合外力平均值。；三角形F-t脉冲J=底×高/2；单位N·s=kg·m/s。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：Δp=0.1×(6+8)=1.4；0.04×100/2=2 N·s；峰值与平均值分开。不得把冲量与动量的关系画成另一知识主题；不得改动v_i=−8 m/s、v_f=+6 m/s、Δp、F/N、t/s的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- Δp=0.1×(6+8)=1.4
- 0.04×100/2=2 N·s
- 峰值与平均值分开
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/8-2-impulse

旧图复用：V22 P10可复用原理，具体数值需说明不同例题。实际匹配：assets/v22/physics/P10_impulse_force_time_triangle_2b6e3bd1f.svg。

## 物理 第8章 · 8.2 动量守恒定律

ID：B05-PHYS08-8-2；优先级：P0；状态：not_produced。

用途：判定所选系统能否用动量守恒；由矢量总动量求相互作用后的速度。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：两车系统框；内力成对箭头；外冲量箭头；初末动量条。

关系：内力只在两车都纳入时相消；非零外冲量改变总量；动能另算。

文字：P前、P后、J外、ΔP=J外、同一参考系。

公式与单位：ΔP系统=J合外；J合外=0时P前=P后。；一维：m₁u₁+m₂u₂=m₁v₁+m₂v₂；若黏合，v₁=v₂=v。；分方向守恒只在该方向合外冲量可忽略时使用；动能须独立审查。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第8章《动量守恒定律》真实小节8.2《动量守恒定律》制作《系统边界与动量收支》教学图。学习目的：判定所选系统能否用动量守恒；由矢量总动量求相互作用后的速度。本图是有条件的科学模型，非实测图或官方考题。必须出现：两车系统框；内力成对箭头；外冲量箭头；初末动量条。必须保持关系：内力只在两车都纳入时相消；非零外冲量改变总量；动能另算。中文标签逐字采用：P前、P后、J外、ΔP=J外、同一参考系。公式及条件：ΔP系统=J合外；J合外=0时P前=P后。；一维：m₁u₁+m₂u₂=m₁v₁+m₂v₂；若黏合，v₁=v₂=v。；分方向守恒只在该方向合外冲量可忽略时使用；动能须独立审查。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 8, authentic subsection 8.2. Display the original Chinese title exactly: 系统边界与动量收支. Topic-specific scientific requirements and instructional purpose: Draw a system boundary around two interacting carts, cancel paired internal impulses, and keep external impulse crossing the boundary. Show P_after=P_before+J_external; do not imply kinetic-energy conservation. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 两车系统框；内力成对箭头；外冲量箭头；初末动量条. Preserve the following Chinese label strings exactly: P前、P后、J外、ΔP=J外、同一参考系. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: ΔP系统=J合外；J合外=0时P前=P后。；一维：m₁u₁+m₂u₂=m₁v₁+m₂v₂；若黏合，v₁=v₂=v。；分方向守恒只在该方向合外冲量可忽略时使用；动能须独立审查。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：内力只在两车都纳入时相消；非零外冲量改变总量；动能另算。不得把动量守恒定律画成另一知识主题；不得改动P前、P后、J外、ΔP=J外、同一参考系的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 内力只在两车都纳入时相消
- 非零外冲量改变总量
- 动能另算
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/8-3-conservation-of-momentum

旧图复用：V22 P10原理可补充，不重复同一题材。实际匹配：无。

## 物理 第8章 · 8.3 反冲作用

ID：B05-PHYS08-8-3；优先级：P0；状态：not_produced。

用途：用系统动量解释反冲方向；区分地面速度、相对速度与系统边界。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：小车2 kg；抛出物0.5 kg；地面坐标；速度箭头；相对速度括号。

关系：V=−0.8；v=+3.2；v−V=4；两动量等大反向。

文字：相对地面、相对车4 m/s、P总=0、内部能源。

公式与单位：初静止的一次分离模型：mv+MV=0，v和V必须相对同一参考系。；若给相对速度u=v−V，与mv+MV=0联立，V=−mu/(M+m)，v=Mu/(M+m)。；反冲动能K=m v²/2+M V²/2可大于0，能量来自系统内部或外部做功，不来自动量守恒本身。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第8章《动量守恒定律》真实小节8.3《反冲作用》制作《反冲的参考系与相对速度》教学图。学习目的：用系统动量解释反冲方向；区分地面速度、相对速度与系统边界。本图是有条件的科学模型，非实测图或官方考题。必须出现：小车2 kg；抛出物0.5 kg；地面坐标；速度箭头；相对速度括号。必须保持关系：V=−0.8；v=+3.2；v−V=4；两动量等大反向。中文标签逐字采用：相对地面、相对车4 m/s、P总=0、内部能源。公式及条件：初静止的一次分离模型：mv+MV=0，v和V必须相对同一参考系。；若给相对速度u=v−V，与mv+MV=0联立，V=−mu/(M+m)，v=Mu/(M+m)。；反冲动能K=m v²/2+M V²/2可大于0，能量来自系统内部或外部做功，不来自动量守恒本身。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 8, authentic subsection 8.3. Display the original Chinese title exactly: 反冲的参考系与相对速度. Topic-specific scientific requirements and instructional purpose: For a freely moving 2 kg cart ejecting a 0.5 kg object, show ground velocities -0.8 and +3.2 m/s, with object speed relative to cart 4 m/s. Distinguish relative and ground arrows and show equal opposite momenta, not equal speeds. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 小车2 kg；抛出物0.5 kg；地面坐标；速度箭头；相对速度括号. Preserve the following Chinese label strings exactly: 相对地面、相对车4 m/s、P总=0、内部能源. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 初静止的一次分离模型：mv+MV=0，v和V必须相对同一参考系。；若给相对速度u=v−V，与mv+MV=0联立，V=−mu/(M+m)，v=Mu/(M+m)。；反冲动能K=m v²/2+M V²/2可大于0，能量来自系统内部或外部做功，不来自动量守恒本身。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：V=−0.8；v=+3.2；v−V=4；两动量等大反向。不得把反冲作用画成另一知识主题；不得改动相对地面、相对车4 m/s、P总=0、内部能源的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- V=−0.8
- v=+3.2
- v−V=4
- 两动量等大反向
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/8-7-introduction-to-rocket-propulsion

旧图复用：须用明确参考系的新示意，旧反冲图可核后辅助。实际匹配：无。

## 物理 第8章 · 8.4 碰撞

ID：B05-PHYS08-8-4；优先级：P0；状态：reuse_partial_remaining_pending。

用途：先用动量再按碰撞类型审查能量；求一维碰撞速度并核方向与能量损失。对应M03/04/05及M06模型辅助；例题和练习如引用该模型须保留各自条件和数值，不能机械套图。

对象：等质量初4与0；弹性末0与4；黏合末2与2；动量条；动能条。

关系：两例P均4；弹性K8保持；黏合K由8到4，差为其他形式。

文字：kg、m/s、P/(kg·m/s)、K/J、转为内能等。

公式与单位：一维动量：m₁u₁+m₂u₂=m₁v₁+m₂v₂。；弹性另有m₁u₁²/2+m₂u₂²/2=m₁v₁²/2+m₂v₂²/2，可推出v₂−v₁=u₁−u₂。；黏合共同速度v=(m₁u₁+m₂u₂)/(m₁+m₂)；损失ΔK=K前−K后，不必等于K前。。

构图：2–3个分面，主图和条件/计算框分开；精确方向和连接，48 px安全边距；不以颜色作为唯一编码。 1280×960，4:3，SVG确定性制作。

### 中文Prompt

为UEC高中物理第8章《动量守恒定律》真实小节8.4《碰撞》制作《弹性与黏合碰撞的双重核查》教学图。学习目的：先用动量再按碰撞类型审查能量；求一维碰撞速度并核方向与能量损失。本图是有条件的科学模型，非实测图或官方考题。必须出现：等质量初4与0；弹性末0与4；黏合末2与2；动量条；动能条。必须保持关系：两例P均4；弹性K8保持；黏合K由8到4，差为其他形式。中文标签逐字采用：kg、m/s、P/(kg·m/s)、K/J、转为内能等。公式及条件：一维动量：m₁u₁+m₂u₂=m₁v₁+m₂v₂。；弹性另有m₁u₁²/2+m₂u₂²/2=m₁v₁²/2+m₂v₂²/2，可推出v₂−v₁=u₁−u₂。；黏合共同速度v=(m₁u₁+m₂u₂)/(m₁+m₂)；损失ΔK=K前−K后，不必等于K前。。以2至3个逻辑清楚的面板排列，主结构居左或居上，计算/条件框居右或居下；箭头起止与文字引线不得穿过无关对象，不用颜色单独编码差异。使用浅底深线，必要以线型和形状区分，避免浅灰小字。建议1280×960、4:3，正文等效字号至少24 px，四周留48 px安全边距；手机可整体缩放并放大查看，最小标签不得裁切。科学结构、坐标、数值、曲线、刻度、单位和公式须用SVG或数学绘图库精确构造；若先用AI，只可作构图草稿，不能直接发布。逐项按验收标准复核。

### English Prompt

Create a UEC senior-high physics teaching diagram for chapter 8, authentic subsection 8.4. Display the original Chinese title exactly: 弹性与黏合碰撞的双重核查. Topic-specific scientific requirements and instructional purpose: Compare two 1 kg carts initially at 4 and 0 m/s. Elastic final velocities are 0 and 4; sticking final velocity is 2. Plot momentum total 4 in both and kinetic energies 8 to 8 versus 8 to 4 J. Do not label dissipated kinetic energy as destroyed energy. This is a conditional teaching model, not measured data or an official examination figure. Required Chinese-labelled objects, which must all appear: 等质量初4与0；弹性末0与4；黏合末2与2；动量条；动能条. Preserve the following Chinese label strings exactly: kg、m/s、P/(kg·m/s)、K/J、转为内能等. Typeset the reference formulas, units and conditions below as literal label/annotation content, checking every sign and symbol: 一维动量：m₁u₁+m₂u₂=m₁v₁+m₂v₂。；弹性另有m₁u₁²/2+m₂u₂²/2=m₁v₁²/2+m₂v₂²/2，可推出v₂−v₁=u₁−u₂。；黏合共同速度v=(m₁u₁+m₂u₂)/(m₁+m₂)；损失ΔK=K前−K后，不必等于K前。. Use two or three clearly separated panels, with the principal structure at top or left and condition/calculation boxes below or right. Never cross unrelated structures with arrows or callouts; every arrow must have a scientifically correct start and end. Never rely on colour alone: use shapes and line styles. Render a light background with dark high-contrast lines. Target 1280 by 960 pixels, 4:3, minimum 24-pixel equivalent labels and 48-pixel safe margins. Keep every label inside the viewBox and support mobile zoom. Construct quantitative geometry, curves, tick marks, formulas, apparatus and scientific structures deterministically in SVG or a mathematical plotting library. AI output may only be a composition draft, requiring independent scientific checks before publication. The main figure is a specified model; do not silently transfer its numbers to a different worked example or exercise.

### Negative Prompt

禁止错误或省略以下关系：两例P均4；弹性K8保持；黏合K由8到4，差为其他形式。不得把碰撞画成另一知识主题；不得改动kg、m/s、P/(kg·m/s)、K/J、转为内能等的数值、变量、正负号、上下标和单位。禁止中文乱码、英文替代必要中文、重复面板、无标尺却声称按比例、错误箭头、错误连接、把方向量当大小、把适用条件删去、截断文字、低对比、小字、装饰物遮挡结构、水印、虚构官方标志。不得将全部项目画成单一无条件因果链；不把AI生成的定量内容未经核验作为事实。

### 科学验收与来源

- 两例P均4
- 弹性K8保持
- 黏合K由8到4，差为其他形式
- 全部对象/标签齐全，数值与本文推导逐项一致
- 按明确模型审查条件，区分示例与实测数据
- 手机320/390及桌面1280宽检查，放大可读且无裁切
- 教学图不替代正文及完整解题；科学审阅不等于XML可解析

- https://www.scribd.com/document/896069659/曾国兴-黄宝玉-艺诚文化-高中适用-物理-上册-Dong-Zong-2017
- https://openstax.org/books/college-physics-2e/pages/8-4-elastic-collisions-in-one-dimension

旧图复用：V22 P27优先复核复用，避免与P11重复显示。实际匹配：assets/v22/physics/P27_inelastic_collision_energy_check_ffe70fa4d.svg。
