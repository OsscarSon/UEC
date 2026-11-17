# UEC 2027 备考系统

给自己用的手机备考网页：课程地图（116 章 × 掌握度 0–3）、今日任务（按学习计划 + 第 1/3/7/14/30 天间隔回忆）、错题本（错因分类，连续重做对 2 次算掌握）、考试日历。

## 部署到 GitHub Pages
1. 新建仓库，把本目录所有文件放到根目录并推送。
2. Settings → Pages → Source 选 `Deploy from a branch`，分支 `main`，目录 `/ (root)`。
3. 几分钟后用手机打开 `https://<用户名>.github.io/<仓库名>/`，可“添加到主屏幕”。

本地预览：`python3 -m http.server`，再开 `http://localhost:8000`。

## 数据与进度
- `data/curriculum.json`：课本章节对照表，来自 `curriculum_map.csv`。`index.html` 里内嵌了同一份数据，改章节时两处一起改。
- 进度存在浏览器 localStorage，只在同一台设备保留。换设备前在“考试日历”页底部导出，在新设备导入。
- 考试日期（期末、预试、毕业考、2027 统考）都待填，不要当作官方日期。

## 内容规则
讲解、例题、模拟题一律原创并标“原创，非官方”，不冒充真题或董总评分标准；不放课本全文；官方纲要为 2026 年版，2027 版出来后要重新核对。

## 讲解内容（lessons/）
每章一个文件，如 `lessons/phys03.js`，写入 `LESSONS["物理3"]`（键 = 科目+章号，数学的科目名是“数学”）。新增后在 `index.html` 里加一行 `<script src="lessons/xxx.js"></script>`。
字段：`syl`（纲要条目）、`status`、`sections`（小节，与课本目录一一对应：id、标题、纲要号、正文、`figs` 插图 `[[路径,图注],…]`、公式、English 术语、易错/易混/记忆提醒）、`method`（考试格式、解题步骤、常见题型、评分点）、`ex`（例题）、`pr`（基础→困难练习）、`vid`（视频搜索入口，待核）。
地图里的“必答区/选答区”标记按 2026 年版纲要的试卷结构推断，分题范围待核。

## 待做
混合卷生成器、进度仪表盘、其余章节讲解、数学纲要对照。当前真实小节为物理3章9节／4章8节，化学3章6节／4章7节／5章4节，生物1章6节／2章5节／3章7节，共52节、73幅SVG。这里统计已有材料，不表示所有内容已通过深度与科学验收。

下一批建议（按学习计划第 3–4 周）：物理第5、6章，化学第6、7、8章，生物第4章，数学第34章（复数）及三角（第8、9、11章）。

## 插图怎么生成
`tools/figlib.py` 是画 SVG 的小工具，`tools/make_*.py` 生成对应章节的图（输出到 `assets/fig/`），`tools/lesson_*.py` 是笔记的原始内容，`tools/build_*.py` 把它们转成 `lessons/*.js`。改图或改笔记时，改 `tools/` 里的文件再运行即可：`python3 tools/make_c5.py && python3 tools/build_chem05.py`。

## 插图
物理等需要精确的图（s–t、v–t、受力图）应由确定性计算生成SVG，放在 `assets/fig/`，并逐图核验数值、模型和标注。现有图仍有待修项，见 [插图需求](ILLUSTRATION_REQUIREMENTS.md)。本轮只审查，不生成任何新图。

## 考试格式的依据
兴华校内安排以用户提供的12/11/2026学校PDF为依据；UEC正式结构以董总当前公开文件为依据，两者分别显示。2027适用版本仍待确认，不能把校内比例泛化为统考要求。

## 本批十二模块笔记与高数入口

物理3、4章，化学3、4章，生物1、2章共41个原有小节已加入十二模块补充，共328个原创题目记录（123例题、164练习、41检测）。内容源为 `data/notes/*.json`；运行 `python tools/build_notes.py` 生成载入文件。原有正文及章级练习仍保留。

高级数学（I）、（II）是独立科目，各自有入口、个人记录、错题筛选与考试资料。**正式课程迁移未完成**：旧35章无真实数学小节表，也缺少学校教材及2027适用对照，全部保留在“数学旧资料 · 待核实映射”。两个新入口暂无已映射章节、题库或模拟卷，不计完工。

完整清单、覆盖率、来源、迁移表和未完成事项见 [本批报告](reports/BATCH_COMPLETION.md)。

2026-11-18补审：十二模块结构存在不代表内容深度充分。已补齐 [完整插图需求](ILLUSTRATION_REQUIREMENTS.md)／[机器清单](illustration-manifest.json) 和 [41节内容深度审核](reports/CONTENT_DEPTH_AUDIT.md)。203条图审查／计划包含73幅现有SVG、41个现有结构图、54项新增需求、35项数学章级待确认计划，另列6个界面素材；本轮没有制作图片或扩写笔记。41节均需局部扩写／检测目标映射，4节另有待修公式分段问题。

复核本次清单：`python tools/audit_illustrations.py`（只生成文本报告，不绘图）。

复核命令（浏览器测试另需本地服务及Playwright）：

```sh
python tools/build_notes.py
node tests/coverage.cjs
python tests/calculations.py
node tests/svg.cjs
# 在另一个终端运行 python -m http.server 8000
node tests/browser.cjs
```

浏览器测试使用本机Chromium，路径可由 `CHROMIUM_PATH` 指定。测试截图默认保存在 `/tmp/uec-qa-screenshots`，可通过 `QA_SCREENSHOT_DIR` 调整。不需要新增网站运行依赖。
