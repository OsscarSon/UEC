# Dashboard验证结果

| 检查 | 实际结果 |
| --- | --- |
| `python tests/dashboard_static.py` | 591项静态断言通过；578个已有课程/笔记/作者源/插图文件不变，116章内嵌数组与JSON不变；35张显式KaTeX公式通过实际解析；上游JS文件、资源及许可检查通过。 |
| `node tests/dashboard.cjs` | 40项交互检查通过，86次章节/视窗检查：34个已有章在390、1440像素各检查一次，另6个代表章在320、1024、1920像素检查。另拍摄1280、手机和深色界面。 |
| `node tests/dashboard_storage.cjs` | 专注崩溃恢复、配额失败、旧备份恢复与迁移、完整状态替换、拒绝原型键导入等5项专项通过。 |
| `node tests/dashboard_subpath.cjs` | 在 `/UEC/` 子路径实际加载笔记和KaTeX、JSXGraph、Excalidraw，动态JS、CSS与字体无404。未部署到GitHub Pages。 |
| `node tests/dashboard_legacy.cjs` | 原四周计划、数学计划分科完成、原任务完成记录及课程地图全部字段在320/1440像素回归通过；145个科目条目对应原116个原章。 |
| V22浏览器回归 | 原12章×320/390/1280共36次、142次放大/滚动/Esc/焦点回归、149资源加载通过；隔离图未因此发布。结果在v22-regression/BROWSER_RESULTS.json。 |
| V22静态回归 | 1869项检查通过，345个基线文件保护；原图数值/向量/配平样本检查继续通过。见V22_STATIC_REGRESSION.json。 |
| 前批内容回归 | 原80项科学计算检查、本批既有94节的2550项断言与165项独立数值样本通过。没有改动教学正文。前批详细报告未用本轮界面结果冒充覆盖。 |
| 本地组件重复构建 | 512个vendor输出文件字节一致；固定package-lock，完整SHA256见BUILD_REPRODUCIBILITY.json。 |
| 差异及语法 | JS语法、Python语法与 `git diff --check` 检查通过。旧课程身份、顺序、笔记、题目和资产不变。 |
| 依赖审查 | 保留2项未进入浏览器包的上游构建依赖high告警，详见DEPENDENCY_REVIEW.md；不将此项称为零告警通过。 |

40项交互覆盖：真实零数据首页、数学迁移不覆盖/幂等/29与35边界、无章号错题归属、错题独立重做、计划添加/完成/取消、周目标实时计算、专注计时、全局搜索及文本转义、12模块与KaTeX、阅读位置、收藏、专注模式、解析开合、高数自评隔离、8项科学模型边界、真实画布绘制和中文输入、独立白板与刷新恢复、草稿导出、完整备份和无效导入、手机导航、深色宽度及外部请求。

## 复现

在仓库运行 `npm ci --ignore-scripts`，然后 `npm run build:tools`。浏览器测试需要可执行的Chromium，可通过CHROMIUM_PATH设置；默认 `/usr/bin/chromium`。

在仓库启动 `python -m http.server 8035 --bind 0.0.0.0`，运行：

```sh
python tests/dashboard_static.py
UEC_TEST_BASE=http://localhost:8035/ npm run test:dashboard
UEC_TEST_BASE=http://localhost:8035/ node tests/dashboard_storage.cjs
UEC_TEST_BASE=http://localhost:8035/ UEC_V22_REPORT_DIR=reports/dashboard/v22-regression node tests/v22_browser.cjs
UEC_V22_STATIC_RESULT=reports/dashboard/V22_STATIC_REGRESSION.json python tests/v22_audit.py
```

子路径测试需要在仓库的父目录启动8036端口的静态服务，再运行 `node tests/dashboard_subpath.cjs`；可用UEC_SUBPATH_BASE调整完整前缀。

历史tests/browser.cjs和tests/batch05_browser.cjs中部分导航及“旧进度不复制”的断言对应升级前UI/政策。本轮按用户新授权实施有备份迁移，由新行为测试明确覆盖，未为通过旧断言恢复已移除的旧入口。

## 限制

自动测试为Linux Chromium模拟尺寸，不是实体手机、Safari或Firefox认证；科学模型只是列明的固定模型，不是完整计算机代数系统。KaTeX覆盖35张明确登记的公式卡和公式工作台，不意味着自动修订全部180节旧公式。

测试使用隔离浏览器和明确的虚构学习记录；截图中的67%等数字来自测试任务完成与目标计算，不是网站替真实学生生成的进度。浏览器源文件保护与计算样本通过不等于全部教学内容已获教师或官方审定。
