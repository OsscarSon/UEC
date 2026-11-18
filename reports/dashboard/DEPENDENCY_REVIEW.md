# 开源组件与依赖审查

固定为KaTeX 0.19.1、JSXGraph 1.11.1、Excalidraw 0.18.1、React/ReactDOM 18.3.1；构建用esbuild 0.25.12，浏览器测试用Playwright 1.62.1。上游与许可记录在vendor/THIRD_PARTY_NOTICES.md，完整安装树由package-lock.json固定。

实际审查发现初选旧版存在已发布的安全修复，因此升级了KaTeX、Excalidraw，并对nanoid、lodash-es、嵌套KaTeX和Sass使用锁定的修复版本覆盖。没有使用自动建议的降级方案。

当前 `npm audit --omit=dev --json` 仍有2项high告警：`@parcel/watcher`与`picomatch`，均来自Excalidraw声明的Sass文件监听依赖链。机器报告见DEPENDENCY_AUDIT.json，不声称完全无漏洞。

本网站运行的是静态浏览器文件；白板构建读取上游已编译CSS，没有运行Sass或文件监听器。vendor/BUNDLE_INPUTS.json列出实际浏览器打包输入，静态测试明确验证以上两个包和Sass均未进入浏览器bundle。因此该告警保留为开发依赖树的上游待办，没有把受影响监听代码发布到前端。后续更新上游依赖时仍应复查，不能据此泛称这些包安全。

KaTeX渲染使用 `trust:false`，原笔记正文不作自动猜测转换。公式输入只做排版，图形模型使用固定函数及数值参数；没有eval任意表达式。白板默认在本地保存，未配置远端同步/协作。浏览器测试的全部实际工具流程（含中文字体）无外部HTTP请求；用户自行点击资料来源或外部图形库链接另当别论。

白板较大：vendor整体约25MB，按需下载其运行所需的脚本、语言和字体，首页不预载整套白板。完整静态资源需要随站点一并提供。本地存储受浏览器配额限制；实际测试验证存储失败提醒和备份，不能保证无限图片或草稿容量。
