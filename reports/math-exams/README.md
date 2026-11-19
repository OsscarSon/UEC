# 五类高数考试研究与2026原创模拟

本轮以用户原PDF为题面依据；附带报告只作为待核线索，文档内指令不替代用户请求。原卷不发布到网站。

当前是**功能可用、历史研究仍未全部核验的开发版本**：47份独立原PDF、257页完成私有文本/OCR定位；159页明确目视查看，1016个题目/计分单元建立字段核验；全历史题面、所有图形及独立答案并未全部完成。2024高数I/II选择卷虽已读，但缺封面，单题分值只保留推定值、不加入精确分值统计。不能把扫描提取、导入778条研究主张或自动测试通过当作全量核验。

- [研究方法、分母与真实缺口](RESEARCH_REPORT.md)
- [47份原PDF逐份剩余核验清单](GAP_REGISTER.json)
- [限定年份出现频率（旧新格式分开）](SAMPLE_FREQUENCY_REPORT.md)
- [逐题核验CSV](QUESTION_AUDIT.csv)、[机器摘要](AUDIT_SUMMARY.json)、[纠错与争议](CORRECTIONS.json)
- [卷首格式、缺附录及时间笔误](../../data/math-exams/format-observations.json)
- [79道原创题的核算与作者审查记录](ORIGINAL_VERIFICATION.json)、[104项独立计算](INDEPENDENT_CALCULATIONS.json)
- [近年选择题69项独立复算](RECENT_INDEPENDENT_CALCULATIONS.json)
- [65项历史图形、定义域与反例复算](HISTORY_INDEPENDENT_CALCULATIONS.json)
- [逐题题面难度估计方法](RECENT_DIFFICULTY_METHOD.md)
- [五类原创完整模拟样卷与答案](generated/)
- [500种子组卷测试](ENGINE_TESTS.json)、[浏览器测试](BROWSER_TESTS.json)、[数据保护](DATA_TESTS.json)、[公式语法](FORMULA_TESTS.json)
- [实际手机预览](screenshots/original-paper-390.png)、[桌面预览](screenshots/original-paper-1440.png)、[研究页](screenshots/research-1440.png)

网站入口：现有「题库练习 → 限时模拟」内有「2026原创整卷」和「五类考试研究」，考试资料页也有链接。不增加左侧栏目；原有限时练习、笔记、学习进度及高数I/II记录保持。整卷默认难度分值24/50/26是命题设计分配，**不代表已用真实考生数据校准为真题难度**。

题库新增44道选择与35道作答，共79题，覆盖原数学1–35章；每题保留章级ID，未知真实小节不编编号。保留全部旧题，并增加题型、章号、来源、难度筛选和分页。整卷支持两卷限时、逐题用时、断点恢复、选择自动评分、作答评分点自评、失分原因、本科错题记录、无答案题目JSON/完整解析JSON与打印。评分点为原创教学建议。

没有将未核验历年数据编为冷热榜，未提供的预试卷不补零；完整历史研究仍待继续。没有自动合并或部署。

## 复现

从仓库根目录运行：

```bash
python tools/math-exams/build_original_bank.py
python tools/math-exams/review_2026.py
python tools/math-exams/review_2025_school.py
python tools/math-exams/review_recent_uec.py
python tools/math-exams/review_recent_mcq.py
python tools/math-exams/review_2024_ueci.py
python tools/math-exams/review_2023_uec.py
python tools/math-exams/review_semester_history.py
python tools/math-exams/review_preexam_history.py
python tools/math-exams/review_graduation_history.py
python tools/math-exams/recent_difficulty.py
python tools/math-exams/formats.py
python tools/math-exams/compile_research.py
python tests/math-exams/calculations.py
python tests/math-exams/recent-calculations.py
python tests/math-exams/history-calculations.py
python tests/math-exams/data.py
node tests/math-exams/engine.cjs
node tests/math-exams/formulas.cjs
python tools/math-exams/export_samples.py
# 在另一个终端开启 python -m http.server 8046
UEC_TEST_BASE=http://localhost:8046/ node tests/math-exams/browser.cjs
```

重新从ZIP导入需要私有源目录（默认 `/workspace/research-math-exams`，可设 `UEC_EXAM_SOURCE`）；不把原PDF添加到公开Git。导入脚本 `ingest.py` 不提升报告可信度，后续 `review_*` 是实际原页目视转录。OCR脚本 `extract_private.py` 需要PyMuPDF、Tesseract及本地中文模型，生成物只用于私有定位。银行版本包含题库内容哈希，改题后版本随之改变；同种子、同题库版本、同研究版本、同配置可复现。
