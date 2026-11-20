# 五类高数：原卷研究、三套冷热榜与智能命题2.0

[本轮实际交付、验证与限制](V2_DELIVERY.md)。上一阶段PR #7已合并，本轮从最新main继续，集中一个Draft PR。没有合并或部署。

47份用户原PDF、257页沿用既有逐页目视记录，1479个计分单元归并为945个独立题号；五类考试独立。题面已查看不等于所有选项、答案、评分细则和教材小节已确认。本轮补全60道选择题与5道作答大题的7个计分单元，修正2022II选择4及10两处旧错误。仍缺1246个计分单元完整答案、379道选择题四项转录、820个单元难度估计；所有已有答案也不代表官方认证。

网站入口：“题库练习→限时模拟”内的“智能命题2.0”和“五类考试研究”；考试资料页亦有入口。不增加左侧栏目，原学习记录、两科隔离、旧限时练习和题库保持。

## 内容与证据

- [三套统计方法、有效/排除年份及分母](HEAT_METHOD.md)
- [逐年格子与三榜数据](../../data/math-exams/heat-statistics.json) · [945道题的原PDF身份/页码](../../data/math-exams/independent-questions.json)
- [本轮65道大题/67单元答案清单](HISTORICAL_COMPLETION_REPORT.md) · [解析与作者评分点](../../data/math-exams/historical-completions.json) · [绑定公式哈希的核算](HISTORICAL_COMPLETION_CHECKS.json)
- [原卷字段方法及争议](RESEARCH_REPORT.md) · [47份PDF剩余核验清单](GAP_REGISTER.json) · [61个所供卷别的题号覆盖](../../data/math-exams/paper-coverage.json)
- [778条报告主张与原卷对照](REPORT_CLAIM_RECONCILIATION.md) · [纠错/争议](CORRECTIONS.json) · [逐单元字段CSV](QUESTION_AUDIT.csv)
- [本轮五类别格式及卷首页码](../../data/math-exams/assembly-profiles.json) · [原卷观察及缺附录记录](../../data/math-exams/format-observations.json)
- [84道原创题作者核算](ORIGINAL_VERIFICATION.json)：44选择、40作答，新增5道，既有79道逐对象保持。
- [五类完整原创样卷、答案、逐步解析、评分点及章节报告](generated/)

热度使用独立大题计数；综合榜每年先标准化再等权平均。2026只一年，零题仅称“本年未考”；缺卷/年份待核使用null。次章、小问另列。主章为作者教学分类，未认证官方教材章标；未掌握真实小节不造编号，原卷高数I超当前章域的冲突保持。旧选答印刷备选分不当实际分。

毕业考/预试没有2026原卷，生成格式按各自2025“四组各选1–2、共6题”，20选择+12印刷作答=160印刷分，但实际只能答100分；2026统考I/II和校内期末分别根据本类别卷首生成15选择+12全答。校内2026卷间60分钟，统考15分钟，原校内时间笔误保持待核。学校章域由学生实际白名单约束，不冒充已确认教学进度。新制难度配额是设计估计，未用考生成绩校准。

## 图表、复习与截图

本地Apache ECharts 6.1.0（**Apache-2.0，非MIT**），按需加载core/热力图/柱状图及所需组件，保留许可证与NOTICE，构建来源见vendor/echarts/BUILD.json。三套榜、年度表、章节排名、新旧标准化对比、点格看原题、PNG/CSV导出，支持深色和手机。

历史热度仅作为个人复习背景；已诊断基础、到期任务和实际失分仍优先。失分补习只能利用计划剩余容量，两科记录不混；未选/未评分不推断薄弱。本轮不引入ts-fsrs或迁移旧记忆记录。

[桌面研究页](screenshots-v2/heat-1440.png) · [手机研究页](screenshots-v2/heat-390.png) · [手机热力图](screenshots-v2/heatmap-390.png) · [深色图](screenshots-v2/heatmap-dark.png) · [桌面选答](screenshots-v2/paper-1440.png) · [手机选答](screenshots-v2/paper-390.png)。视窗模拟，不是物理手机或官方审定。

## 本轮验证

[500种子及12项引擎检查](ENGINE_V2_TESTS.json) · [8722项统计断言](HEAT_CONSISTENCY_TESTS.json) · [53项浏览器流程](BROWSER_V2_TESTS.json) · [7项个人复习/原题保护](STUDY_V2_TESTS.json) · [8218项数据保护](DATA_TESTS.json) · [1589条TeX](FORMULA_TESTS.json)。327项既有具名数学复算重新通过，另有67单元补全核算与84原创作者核算，统计可能交叠，不合算成独立题数。1322份旧文件逐字节保持。原导航68案例、学习流16响应式视图、储存与备份回归通过。

上一阶段[CONTINUATION_DELIVERY](CONTINUATION_DELIVERY.md)、ENGINE_TESTS/BROWSER_TESTS和旧screenshots目录是历史记录；其中“所有五类统一2026模板”已由本轮按类原卷格式替代。[旧制限定样本频率](SAMPLE_FREQUENCY_REPORT.md)也保留为历史分析，当前UI和策略使用HEAT_METHOD的新主榜。

## 本轮复现

在仓库根目录，使用已锁定依赖（`npm ci --ignore-scripts`），需要Python/sympy及Playwright/Chromium：

```bash
python tools/math-exams/build_original_bank.py
python tools/math-exams/review_2022_uec.py
python tools/math-exams/complete_history.py
python tools/math-exams/compile_research.py
python tools/math-exams/build_heat.py
python tools/math-exams/build_profiles.py
python tools/math-exams/reconcile_claims.py
npm run build:exam-charts
python tests/math-exams/calculations.py
python tests/math-exams/recent-calculations.py
python tests/math-exams/history-calculations.py
python tests/math-exams/older-calculations.py
python tests/math-exams/heat-consistency.py
python tests/math-exams/data.py
node tests/math-exams/formulas.cjs
node tests/math-exams/study-v2.cjs
node tests/math-exams/engine-v2.cjs
python tools/math-exams/export_samples.py
# 另开终端 python -m http.server 8049 --bind 127.0.0.1
UEC_TEST_BASE=http://127.0.0.1:8049/ node tests/math-exams/browser-v2.cjs
UEC_TEST_BASE=http://127.0.0.1:8049/ node tests/navigation.cjs
UEC_TEST_BASE=http://127.0.0.1:8049/ node tests/learning.cjs
UEC_TEST_BASE=http://127.0.0.1:8049/ node tests/dashboard_storage.cjs
```

旧`engine.cjs`只测legacy v1快照，会覆盖样卷；若单独运行，之后须重跑engine-v2及export_samples恢复当前格式样卷。完整原页转录仍见上一阶段review_*脚本；重新导入ZIP需要私有原卷目录和OCR环境，不将原PDF/原页截图提交公开Git。报告里的指令不替代用户授权，未证实主张不提升可信度。
