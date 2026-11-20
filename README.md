> 考试资料工作区新增「课本资料」与「历届考试资料」，支持将原文件导入浏览器。74章、398节现有笔记已列入逐节教材核对清单，需等待课本原页可读后完成内容核对。[资料库交付与教材核对状态](reports/textbook-review/README.md)。
>
> 最新开发：三套独立冷热榜、Apache ECharts 与按各考试原卷格式的智能命题2.0；补齐65道历史大题解析，完整历史答案仍待继续核验。[本轮实际交付与测试边界](reports/math-exams/V2_DELIVERY.md)。
>
> 导航已按使用场景从16项合并为9个主入口，云同步归入设置、模拟练习归入题库、诊断与错题归入复习。[整合说明与新截图](reports/navigation/DELIVERY.md)。
>
> 最新功能：[前置诊断、限时练习与自适应计划](reports/learning/DELIVERY.md) · [实际测试与边界](reports/learning/TEST_RESULTS.md)。Google登录与云同步代码已接入，因尚无Firebase项目，默认未启用；[配置说明](cloud/SETUP.md)。
>
> 本轮界面升级：[学习Dashboard、十二模块阅读导航与开源工具交付](reports/dashboard/DELIVERY.md)。旧数学入口隐藏，首次加载按已确认范围补齐两科的空缺记录并保留原始备份；不覆盖已有独立学习记录。课程与教学正文保持。
>
> 新工具：KaTeX公式、JSXGraph交互图形、Excalidraw本地白板。[实际测试](reports/dashboard/TEST_RESULTS.md) · [依赖审查及边界](reports/dashboard/DEPENDENCY_REVIEW.md)。开发者运行 `npm ci --ignore-scripts` 和 `npm run build:tools` 生成本地资源；网站仍可直接以静态文件运行。

# UEC 2027 备考系统

保留原有116章课程框架、课程地图、学习记录、错题本、题库、日历和本地备份。学校校内考试资料与正式UEC资料分别展示；当前公开纲要的2027适用性仍待确认。

上一正文批次新增20个原章节、94个真实小节的十二模块笔记，含282道原创例题、376道练习、94道独立检测题。现有笔记合计34个原章节、180小节。模块齐全不等于教师或官方审定，新增内容均保留部分核实状态。

| 科目 | 上一正文批次新增章 | 新增小节 |
| --- | --- | ---: |
| 物理 | 1、2、5、7、8 | 20 |
| 化学 | 1、2、26、29、35 | 30 |
| 生物 | 10、11、13、18、19 | 18 |
| 高级数学 I / II 共用教材内容 | 1–5 | 26 |

高数I按用户确认显示1–29章，高数II显示1–35章。前五章目录来自用户确认一致的2025年10月第1版《数学》高一上册。两科共用教学文本，分别保存进度、掌握度、复习、自评及错题；首次加载仅补齐两科空缺的旧记录字段，既有本科记录优先；原始数学记录和迁移快照保留。统计时共用五章仅计一次，按科目入口则有25个新增章入口。

- [本轮交付与测试](reports/batch05/DELIVERY.md)
- [新增全部章节、小节和题目统计](reports/batch05/CONTENT_DELIVERY.md)
- [十二模块深度与核实边界](reports/batch05/DEPTH_REVIEW.md)
- [116章覆盖表](reports/batch05/COURSE_COVERAGE.csv)
- [尚未编写的82章及具体后续依据](reports/batch05/REMAINING_WORK.md)
- [资料来源](reports/batch05/SOURCES.md) · [高数课程对应](reports/batch05/MATH_COURSE_MAPPING.csv)
- [94项新增中英文绘图任务](illustrations/batch05/PROMPTS.md)

本轮复用8张已审核V22插图，未制作新图；当前V22教学引用为79张。原始142项绘图任务及其3项完整、44项部分、95项无V22对应的历史覆盖记录保留，不以新增需求冒充旧缺口已经补齐。[V22历史交付](reports/v22/DELIVERY.md)、[原142任务清单](illustrations/PROMPTS_BATCH_ALL.md)、[总清单](illustrations/ILLUSTRATION_MASTER_MANIFEST.json)。已隔离错误图片继续隔离。

## 本地使用与数据

运行 `python -m http.server 8025`，打开 `http://localhost:8025`。浏览器本地存储保存学习数据；换设备前使用日历页的导出，在新设备导入。未提供官方日期的考试仍为待填。

课程基准位于 `data/curriculum.json` 和 `index.html` 的原课程数组。本轮不修改其章号、原名、顺序与ID。教学记录仍通过原 `LESSONS` 键查询，高数科目进度另设命名空间。

## 内容构建与验证

新增内容的逐题原稿位于 `data/authoring/`，基础正文、十二模块源与小节证据分别位于 `data/base-lessons/`、`data/notes/`、`data/batch05/`。原批次编译器跳过新批次，避免覆盖既有内容及来源。

```sh
# 重新构建本轮的20个作者文件，明确列出，避免运行其他批次源
for file in phys01 phys02 phys05 phys07 phys08 chem01 chem02 chem26 chem29 chem35 bio10 bio11 bio13 bio18 bio19 math01 math02 math03 math04 math05; do
  python data/authoring/$file.py
done
python tools/batch05/build.py
python tools/batch05/reports.py
python tools/batch05/illustrations.py
python tests/batch05_content.py
python tests/calculations.py
# 另开终端运行上面的本地HTTP服务；需Playwright与Chromium
UEC_TEST_BASE=http://localhost:8025/ npm run test:dashboard
```

详细复核命令、截图和实际测试范围见本轮测试报告。自动检查只覆盖列明的数据保护、结构、独立算例与交互，不代表全部题目、全部教材版本和2027考试要求均已独立或官方审定。

历史记录：[batch04](reports/batch04/DELIVERY.md) · [batch03](reports/batch03/DELIVERY.md) · [最初41节深度审查](reports/CONTENT_DEPTH_AUDIT.md)。历史报告按当时交付范围理解，本页与batch05报告用于当前新增统计。
