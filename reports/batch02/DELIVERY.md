> 此为上一批历史交付；当前新增5章28节及全课程状态见 [batch04](../batch04/DELIVERY.md)。

# 本轮集中交付：笔记深化、插图接入与全部后续提示词

继续PR #1原分支 `codex/uec-2027-batch-notes-math-split`，不新建PR、不合并、不部署。基线为daa3637。

## 实际完成的实施范围

9个章级记录、58个真实小节已有本轮十二模块内容，共696模块；保留原116章与原52小节ID/名称/顺序，新增化学6的6个有官方目录证据的小节。原41节深化，原11节补齐模块，另6节首次建立。这里是实施范围，不是宣布整章全部标准最终验收通过。

| 科目 | 原章号与章名 | 真实小节数 |
| --- | --- | --- |
| 物理 | 3 直线运动 | 9 |
| 物理 | 4 牛顿运动定律 | 8 |
| 化学 | 3 原子与分子 | 6 |
| 化学 | 4 化学方程式与化学计算 | 7 |
| 化学 | 5 原子结构 | 4 |
| 化学 | 6 元素周期表 | 6 |
| 生物 | 1 生物是由什么组成的 | 6 |
| 生物 | 2 细胞的结构与功能 | 5 |
| 生物 | 3 细胞内物质和能量的转换 | 7 |

58节完整标题与逐节动作见 [COMPLETED_IMPLEMENTATION_SECTIONS.csv](COMPLETED_IMPLEMENTATION_SECTIONS.csv)。原始52节与新增6节分别核对，未用新编号掩盖重排。

## 全课程覆盖与未完成

完整116章A/B/C/D表见 [COURSE_COVERAGE_MASTER.csv](COURSE_COVERAGE_MASTER.csv)。A=全部要求最终验收；B=有真实小节但仍有待补/待验收；C=仅章目录或候选目录需落实；D=归属/教材/适用证据不足。当前保守记A0、B9、C72、D35。没有将696个结构模块等同于A。

物理其余25章未取得可完整核对的同版本小节表；化学其余31章与生物其余16章尚未逐章完成目录对应、原创笔记及科学验收。化学7/8已有公开内容表候选，不能说无来源，但尚未实际编写。数学35章虽有新版标准内容表，仍未得到学校真实教材目录与I/II归属，不迁移或复制进度。

## 内容与题目

[深度改进报告](DEPTH_IMPROVEMENTS.md)列58节方法、核查及待验收点；[逐节后续扩写要求](FOLLOWUP_CONTENT_REQUIREMENTS.csv)明确检测覆盖缺口及需要继续深化的内容。174例均有八步字段，原123例为逐题扩写。十二模块补充层共466条原创题记录（保留的原章级及ext题另计）：174例题、232分层练习、58节检测、2个额外目标检测；相对基线新增138，不将116个目标回链或M07复用例题重复计数。

[696项模块覆盖](SECTION_MODULE_COVERAGE.csv)核实模块存在。原样例的80项数值/原子守恒检查及本轮新增样例检查有明确范围；定性机制不因数值通过自动成为verified。

## 上传图与后续图任务

六张上传PNG逐张检查，3张限定用途接入：物理3.5、化学4.2.3、生物2.3概览。3张隔离：物理4.3向量几何、化学3.6运算箭头/温压/NA、生物2.2主动运输及梯度概括。原文件均保留；原73幅SVG逐字节不变。

[逐张审核JSON](../../illustrations/IMPORT_BATCH01_REVIEW.json)；[完整主清单](../../illustrations/ILLUSTRATION_MASTER_MANIFEST.json)为209项教学记录：60保留、35数学冻结、114制作任务。另列6张导入图、6界面素材和11幅新确定性总结SVG，不混计。

[全部中文/英文Prompt](../../illustrations/PROMPTS_BATCH_ALL.md)／[机器JSON](../../illustrations/PROMPTS_BATCH_ALL.json)按科目及完整章分组；114条中24条为HTML/CSS关系图重构、90条为其他图制作。每条含20项要求、独立中英文Prompt、Negative、来源、验收、复用、优先级及确定性绘图要求。未调用AI生图。

[图像质量检查表](../../illustrations/IMAGE_QUALITY_CHECKLIST.md)区分定量图、结构、装置、函数与辅助画；AI图仍需科学重建/审查，不能因清单齐备就上线。

## 数学与资料准确性

两个数学入口与独立记录保留；仍各0个已归属章节、0题本科题库、0本科模拟卷。旧35章维持math_pending。2026修订标准包含与旧35章相符的主题，但学习结果编号不能直接冒充课本小节；S06正文《高中数学》与末注《高级数学课程标准》的指向冲突仍未解决。

[来源与准确性台账](SOURCE_ACCURACY_REGISTER.csv)分别记录学校、UEC、公开目录、科学原则、403/404与部分可读状态。学校原件与前轮SHA256相同，仍按原件纠正ZIP摘要；两份早先另传Research报告的历史核验见原报告，不声称新ZIP包含它们，也未重做全部64题统计。

## 测试与限制

运行 `python tools/build_notes.py`、`node tests/coverage.cjs`、`python tests/calculations.py`、`python tests/batch02_audit.py --rebuild-check`，本地服务下运行 `node tests/browser.cjs` 与 `node tests/batch02_browser.cjs`。可用UEC_TEST_BASE指定本地端口。

[当前手机策略截图](screenshots/strategy-390.png)／[电脑策略截图](screenshots/strategy-1280.png)／[手机放大图](screenshots/zoom-mobile.png)来自本地验证，不是部署。放大图可在容器内横向滑动，不撑开页面。

[实际测试命令](TEST_COMMANDS.md)、[构建与兼容命令可复现](BUILD_REPRODUCIBILITY.json)、[静态/计算/资源/Prompt结果](AUDIT_RESULTS.json)、[专项UI与SVG边界](UI_RESULTS.json)、[全站回归](../BROWSER_RESULTS.json)提供实际结果。数学I/II记录与错题隔离、原进度、日历、题库、旧链接、导出导入往返，以及3视窗×9章、目标反馈、放大与键盘都需通过；测试通过仍不等于教师/官方全面审定。

剩余：未实施107个章级记录（72科学C、35数学D）；58节的最终知识点/图示/教研验收；114条图制作/修正任务；2027适用及学校真实教材版本；完整官方原卷、评分及考频证据。新内容未以“全科完成”交付。
