# 实际测试与检查记录

本轮在PR #1原分支运行；参考基线daa3637。全部命令通过；不把自动通过等同教师或官方全面审定。

| 命令 | 实际覆盖 | 结果 |
| --- | --- | --- |
| python tools/build_base_lessons.py | 当前3章基础源编译 | pass |
| python tools/build_notes.py | 9章58节补充编译 | pass |
| node tests/coverage.cjs | 116章不变、52原节身份顺序不变、6新节有目录证据、696模块、464主问题 | pass |
| python tests/calculations.py | 原80项独立数值/原子守恒样例 | pass |
| python tests/batch02_audit.py --rebuild-check | 新样例计算、466题来源/字段、174例八步、目标映射、114双语Brief、资源/数学冻结、全部生成和兼容命令重建不丢修订 | pass |
| UEC_TEST_BASE=http://127.0.0.1:8011/ node tests/browser.cjs | 3视窗×9章=27；旧进度/掌握/错题/日历/题库/旧URL/导入导出；I/II独立记录与刷新 | pass |
| UEC_TEST_BASE=http://127.0.0.1:8011/ node tests/batch02_browser.cjs | 3视窗×新增模块3章=9；四处公式DOM、目标状态刷新与导入导出、限定PNG接入、隔离拦截、放大与键盘焦点、11新SVG文字边界 | pass |
| node tests/svg.cjs | 原43幅SVG文字边界；文件本身未变 | pass |
| node --check batch-ui.js / data/illustrations.js | JS语法 | pass |
| python -m py_compile（本轮Python构建及审查脚本） | Python语法 | pass |
| python tools/build_illustration_prompts.py（再次生成比较SHA256） | 根/主清单、114双语Prompt、质量表及英文源再次构建逐字节一致 | pass |
| git diff --check | 差异空白检查 | pass |

本地服务示例：`python -m http.server 8011 --bind 127.0.0.1`；这是测试预览，不是部署。

新样例核验涵盖氢能级/波长、粒子计数、电子容量、电离能判断、酶能垒、ATP耦联、呼吸ATP、光解/卡尔文碳账与净光合等，详见AUDIT_RESULTS.json。只核验所列数值/守恒，不宣称全部定性断言、知识点或难度已经独立审定。

原73幅SVG逐字节保留；新11幅为确定性总结/账本图，完整结构/装置图仍需后续制作。图片放大在容器内滚动，整页不横向溢出。正式高数课程无已核实真实小节，未虚称测试了不存在的高数笔记或模拟卷。
