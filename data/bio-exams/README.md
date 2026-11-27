# 生物科考情与组卷数据目录（预留）

本目录结构与 `data/math-exams/` 保持统一契约，供 `tools/build-exam-data.mjs` 与 `ui/exam-registry.js` 自动发现和加载。

- `exam-config.json`: 科目元数据、章节范围（第 1–19 章）及考试类别清单
- `assembly-profiles.json`: 依据学校文件及董总 2026 纲要（`S10-2026-0623.pdf`）预置的试卷结构
- `heat-statistics.json`: 独立题目冷热统计骨架
- `research-data.json`: 原卷目录与抽样频率骨架
- `original-bank.json`: 核验后的原创组卷题库
