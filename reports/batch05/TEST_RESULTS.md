# 实际测试与回归（2026-11-18）

| 检查 | 实际结果与边界 |
| --- | --- |
| `python tests/batch05_content.py` | PASS：2550项断言；94节、752题的数据完整性与原数据保护；165项独立数值复算、8项元素收支。283个基线文件逐字节保护。详见AUDIT_RESULTS.json。 |
| `node tests/coverage.cjs` | PASS：116章不变；原52节及前批新增34节身份保留；本轮94节有独立证据登记。当前180节、2160模块、1440条主要原创题记录；原有额外目标题不混计。 |
| `python tests/calculations.py` | PASS：原80项数值/原子守恒样本。未改旧科学内容。 |
| `python tests/v22_audit.py` | PASS：1808项检查；284个基线文件保护（数学来源文字与Prompt扩展允许明确授权的元数据变化），55项原数值样本、17个配平方程；149图哈希、结构、映射及原142任务不被覆盖。详见V22_STATIC_REGRESSION.json。 |
| `node tests/batch05_browser.cjs` | PASS：20新章×320/390/1280共60次检查、94节模块与原名顺序、完整解析、图加载、16次复用图放大；高数29/35范围、章35题库边界、独立章进度/复习/掌握/目标自评/错题、模块书签刷新、旧数据及备份往返。无页面异常或本地HTTP错误。 |
| `node tests/browser.cjs` | PASS：原14章×三视窗42次检查；86节模块、原图加载、答案展开、原学习行为、既存掌握度数据、旧数学兼容路由、日历改期、导出导入及错题掌握。详见LEGACY_BROWSER_RESULTS.json。 |
| `node tests/v22_browser.cjs` | PASS：原12章×三视窗36次检查、142次放大/滚动/Esc/焦点回归、149资源加载。隔离图仅作为隔离资源被测试可解析，未解除隔离或发布。详见v22-regression/BROWSER_RESULTS.json。 |
| 重复构建 | PASS：20作者源重建基础/补充数据、JS与绘图清单；68个输出文件字节一致。原编译器跳过新批次，仍构建原14章86节，旧资料保护测试再次通过。见BUILD_REPRODUCIBILITY.json。 |
| 语法及差异 | Python编译、JS语法、`git diff --check`通过。原课程数组与JSON、旧正文及资产、用户ui-polish.css均保持。 |
| 来源连通 | 85个唯一来源URL：81个HTTP200、4个403，无已发现404。403涉及董总两份内容表、教材第三方页及IUPAC条目；来源对照和读取边界见SOURCES.md。HTTP状态不是内容准确性证明。Google表格另为403/401，未读取格子。 |

## 运行命令与报告隔离

先运行 `python -m http.server 8025`。新增测试用 `UEC_TEST_BASE=http://localhost:8025/`；旧浏览器增加 `UEC_LEGACY_RESULT=reports/batch05/LEGACY_BROWSER_RESULTS.json QA_SCREENSHOT_DIR=reports/batch05/legacy-screenshots`；V22静态用 `UEC_V22_STATIC_RESULT=reports/batch05/V22_STATIC_REGRESSION.json`，浏览器用 `UEC_V22_REPORT_DIR=reports/batch05/v22-regression`。历史报告未被新结果冒充覆盖。

旧覆盖检查首次仍只接受前批34个新增小节，已扩展为前批34加本轮94的证据并集，原身份断言保留。旧浏览器首次寻找main已经移除的科学章掌握度按钮，已修正为验证现有学习按钮和原掌握度数据保留；未为通过测试重建无关UI。修正后上述检查全部重跑通过。

## 科学与教学验证限制

独立复算覆盖列明的165个新样本（不是752题全部独立复算），包括参数例外、单位、根式与反函数域、限量试剂、聚合端基、种群/能量收支。8个新元素向量收支与17个历史图配平另计，不能把数目相加宣称全题审定。

新增内容的定性审阅包含生物分裂计数与病毒机制、能流与物质、化学聚合与物态条件、力/力矩和守恒条件、数学主值与定义域；发现的问题已修正，仍需教师全面复核。来源仅对照登记范围，不表示每段已与所有原书逐字校对，尤其生物及有机部分尚需用户实体印本逐页复核。

公式沿用网站现有Unicode/文本显示方式；浏览器检查绝对值、根号、分数括号与溢出，没有声称新增LaTeX排版引擎。测试为Linux Chromium模拟视窗，不是Safari/Firefox或实体设备测试。未进行合并、部署或教师/官方审定。
