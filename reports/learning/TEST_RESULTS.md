# 实际验证范围

所有下列测试在本轮工作树运行；原Dashboard报告保留历史版本，本轮复测JSON另存于 `regression/`。

| 检查 | 结果与证据 |
| --- | --- |
| 新功能浏览器流程 | PASS：[TEST_RESULTS.json](TEST_RESULTS.json)。诊断与补课、真实章号组卷、答案提交前隐藏、刷新恢复、到时交卷、逐题用时、自评分点、50%自评满分率、本科错题、计划容量与顺延、云端禁用及快照大小限制；四视图×四宽度，共16个无横向溢出检查 |
| 边界流程 | PASS：[EDGE_RESULTS.json](EDGE_RESULTS.json)。深链接切换诊断目标并刷新、已完成旧任务不复活、零时间预算、最新评分覆盖旧失分、高数I/II复盘隔离、其他页面时间不计入单题 |
| 课程/数据保护 | PASS：[STATIC_RESULTS.json](STATIC_RESULTS.json)。1064个既有文件与主线 `baf80ae973dfab525f9de4c5033b60107773615d` 字节一致；依赖图无环，13目标章真实，真实小节链接存在，9节点18题的选项与答案索引有效 |
| 云端事务版本契约 | PASS：[CLOUD_CONTRACT_RESULTS.json](CLOUD_CONTRACT_RESULTS.json)。6个纯函数版本冲突场景；不是已连接Firestore的测试 |
| 原Dashboard回归 | PASS：[regression/DASHBOARD_BROWSER.json](regression/DASHBOARD_BROWSER.json)。40项行为、86个章节/视窗场景、8个科学模型边界；无脚本错误、资源错误或外部网络请求 |
| 原备份/存储回归 | PASS：[regression/STORAGE.json](regression/STORAGE.json)。旧备份迁移、配额失败、恶意键拒绝、专注时间及替换行为 |
| 原功能回归 | PASS：[regression/LEGACY_FUNCTIONS.json](regression/LEGACY_FUNCTIONS.json)。原四周计划、分科完成、今日任务、145个科目入口对应116原章、手机/桌面课程地图 |
| 原静态检查 | `python tests/dashboard_static.py` PASS：591项检查，578个原文件保护 |
| 依赖审查 | [DEPENDENCY_AUDIT.json](DEPENDENCY_AUDIT.json)：本次安装树报告0已知漏洞；固定Firebase 13.4.0与grpc传递依赖版本，不代表将来永无漏洞 |
| 构建与语法 | Firebase本地包构建成功；新UI/引擎脚本语法检查及 `git diff --check` 通过 |

## 复现

```sh
npm ci --ignore-scripts
npm run build:cloud
# 另开终端，从仓库根目录启动测试HTTP服务
python -m http.server 8041 --bind 127.0.0.1
# 下列命令使用本机Chromium，需安装 /usr/bin/chromium
node tests/learning.cjs
node tests/learning-edge.cjs
node tests/learning-static.cjs
node tests/cloud-contract.mjs
python tests/dashboard_static.py
UEC_TEST_BASE=http://localhost:8041/ node tests/dashboard.cjs
```

原回归脚本会重写 `reports/dashboard/` 中的结果；本轮把复测结果复制到 `reports/learning/regression/`，再恢复历史报告，避免覆盖旧交付证据。

## 尚未验证

没有Firebase项目，未进行真实Google OAuth、Firestore规则模拟器、规则部署、真实用户UID隔离或双设备端到端测试。浏览器测试使用Chromium模拟320、390、1440、1920像素宽度，不等于实体手机、Safari、所有浏览器或辅助技术全面认证。18道诊断题与9张桥接卡尚待教师全面复核；自动检查不能代替教学审定。模拟题的人工自评也不是官方阅卷。
