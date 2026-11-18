# 导航整合：16项收敛为9个主入口

沿用现有PR #5和工作分支，按使用场景整合入口，没有删除功能或修改课程正文。左侧只保留学习仪表盘、课程笔记、题库练习、智能复习、学习记录、考试资料、学习工具、我的收藏、设置与备份。

| 主入口 | 页内功能 |
| --- | --- |
| 学习仪表盘 | 今日概览；从首页今日计划进入学习计划；保留原四周计划 |
| 课程笔记 | 章节笔记、课程地图；阅读页继续保留十二模块导航与章节前置诊断提示 |
| 题库练习 | 分层题库、限时模拟 |
| 智能复习 | 到期复习、前置诊断、错题本 |
| 考试资料 | 考试资料、考试日历 |
| 设置与备份 | 偏好与备份、账号与云同步 |

学习记录、学习工具、我的收藏继续作为独立目的地。页内切换采用真实链接，当前项和所属主栏目同时高亮；手机底部快捷入口保持。原 `#view=sync`、`mock`、`diagnose`、`adaptive`、`curriculum`、`err`、`cal` 等链接继续可用，刷新与浏览器返回不丢失所属栏目。

云同步仍未配置，Google登录和上传保持禁用。本轮只调整入口、标题与导航显示，没有改变云端规则、课程ID、笔记、进度、错题、白板或数学迁移逻辑，没有合并或部署。

## 实际验证

- [导航测试结果](TEST_RESULTS.json)：17个路由×320/390/1440/1920四种宽度，共68个场景；9项主导航、父栏目高亮、页内链接、无横向溢出。实际点击验证设置→云同步、题库→模拟、复习→诊断/错题、笔记→地图、首页→学习计划，以及返回、刷新、手机抽屉关闭、浅深色和学习记录保护。
- [新增学习功能回归](regression/LEARNING_FLOWS.json)及[边界测试](regression/LEARNING_EDGES.json)：诊断、定向补课、计时刷新/交卷、自评与错题、计划容量和顺延、两科高数独立复盘保持通过。
- [原Dashboard回归](regression/DASHBOARD_BROWSER.json)：40项行为、86个章节/视窗场景、8个科学模型边界；[备份/储存](regression/STORAGE.json)与[原功能](regression/LEGACY_FUNCTIONS.json)回归通过。
- [数据静态检查](regression/STATIC_RESULTS.json)：1064个既有教学、图像和工具文件保持；原静态检查另通过591项断言、578个文件保护。脚本语法及 `git diff --check` 通过。

截图：[桌面首页](screenshots/dashboard-desktop.png)、[设置内的云同步](screenshots/settings-cloud-desktop.png)、[题库内的模拟练习](screenshots/practice-desktop.png)、[首页学习计划](screenshots/plan-desktop.png)、[手机设置](screenshots/settings-cloud-mobile.png)、[精简手机菜单](screenshots/sidebar-mobile.png)、[手机复习内诊断](screenshots/review-mobile.png)、[深色](screenshots/review-mobile-dark.png)。截图含隔离测试数据，不是用户真实学习统计。

测试使用Linux Chromium模拟视窗，不等于实体设备或所有浏览器认证。真实Google登录/双设备同步仍须配置Firebase后验证，本轮未声称已开通。

## 复现

在仓库根目录启动HTTP服务，再运行：

```sh
python -m http.server 8042 --bind 127.0.0.1
# 在另一终端
UEC_TEST_BASE=http://localhost:8042/ node tests/navigation.cjs
UEC_TEST_BASE=http://localhost:8042/ node tests/learning.cjs
UEC_TEST_BASE=http://localhost:8042/ node tests/learning-edge.cjs
UEC_TEST_BASE=http://localhost:8042/ node tests/dashboard.cjs
UEC_TEST_BASE=http://localhost:8042/ node tests/dashboard_storage.cjs
UEC_TEST_BASE=http://localhost:8042/ node tests/dashboard_legacy.cjs
node tests/learning-static.cjs
node tests/cloud-contract.mjs
python tests/dashboard_static.py
```

原回归脚本会写入旧报告目录；本轮复制复测JSON到此处，恢复旧报告和截图，保留历史交付证据。
