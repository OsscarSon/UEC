# 恢复后的测试与回归结果

本轮在恢复的原分支重新执行以下检查，结果通过；记录来自实际文件与运行结果，没有从上一轮统计截图推定。测试浏览器为本地headless Chromium，320/390是手机视窗模拟，没有声明真机Safari/iOS验证。

|命令|核对范围与结果|证据|
|---|---|---|
|`python tests/v22_audit.py`|149个原件哈希、147个可用版本哈希、真实目录/小节名/学习目标、137个基线文件、55个数值样本、17条配平、向量/氢键/运输检查通过|[静态与计算明细](STATIC_TEST_RESULTS.json)|
|`node tools/v22/layout.cjs`|147个可用SVG的文字边界通过，考虑文字变换矩阵；隔离2图不算可用版本|[逐图边界](TEXT_BOUNDS.json)|
|`UEC_TEST_BASE=http://localhost:8022/ node tests/v22_browser.cjs`|71图×3视窗加载；36个视窗/章节组合、142次放大/滚动/Esc/焦点回归、149个资源加载通过；浏览器错误/HTTP错误为空|[V22浏览器](BROWSER_RESULTS.json)|
|`node tests/coverage.cjs`|116章框架、原52节与登记新增34节身份/顺序、14章86节、1032模块、688主问题记录保留；另2条目标检测由静态审核核对|[原内容审核快照](regression/CONTENT_AUDIT.json)|
|`python tests/batch02_audit.py`|课程/12模块/目标映射/来源标识/原图保护及当前清单检查通过；不是按字数判定教学质量|[审核明细](regression/CONTENT_AUDIT.json)|
|`python tests/batch04_content.py`|原新增章节53项数值、21条配平、此前58节和资源保护通过|[命令记录](REGRESSION_COMMANDS.json)|
|`python tests/calculations.py`|80项原计算与守恒样本通过|[原计算复跑](regression/CALCULATIONS.json)|
|`python tests/p0_audit.py`|P0来源、原SVG保护及独立样本通过|[命令记录](REGRESSION_COMMANDS.json)|
|`UEC_TEST_BASE=http://localhost:8022/ node tests/browser.cjs`|全站42个视窗/章节组合；学习进度、掌握、错题、日历、题库、导出导入、I/II记录隔离通过|[全站浏览器](regression/CORE_BROWSER.json)|
|`UEC_TEST_BASE=http://localhost:8022/ node tests/batch02_browser.cjs`|9个专项视窗/章节组合；目标反馈保存、备份、绝对值、代表图放大、11幅既有总结SVG边界通过|[旧专项](regression/LEGACY_UI.json)|
|`UEC_TEST_BASE=http://localhost:8022/ node tests/p0_browser.cjs`|15个视窗/章节组合，保留5个限定接入场景（其中2图由V22替代），5个错误P0继续不出现在教学DOM|[P0回归](regression/P0_BROWSER.json)|
|`UEC_TEST_BASE=http://localhost:8022/ node tests/batch04_browser.cjs`|15个视窗/章节组合；新增28节既有例题/检测/题库通过|[化学章节回归](regression/CHAPTER_BROWSER.json)|
|V22修图与清单重建|158个输出逐字节稳定；首次恢复重建只有审查JSON出现差异，其余图文件、运行清单及报告一致，保留首轮记录，随后重建稳定|[稳定复建](REBUILD_RESULTS.json) / [首轮差异记录](RECOVERY_NORMALIZATION.json)|

JavaScript/Python语法、所有本轮Markdown资源链接及最终暂存差异另检查。上游SVG的路径字符串含行末分隔空白；为保留原件和PASS副本哈希，`.gitattributes`仅对V22原包/教学SVG目录关闭代码行尾空白检查，SVG仍接受XML、科学关系和几何验证。原历史报告和历史截图保留，当前复跑输出快照放在本目录 `regression/`；本轮实际教学截图集中在 `screenshots/`。

科学准确性由逐图审查、条件核对和所列独立样本共同支持。自动测试不证明全部科学解释已经得到第二位教师或官方审定；两张结构错误图仍隔离，54张仍缺真实小节对应，原142项任务的真实缺口没有消失。
