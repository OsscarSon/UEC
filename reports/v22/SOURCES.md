# 来源与科学审核边界

恢复基线为PR1合并后的 `main`：`ce2f44b8cae16aba750ab9c696807599c39f2a5c`。恢复后重新fetch确认远程main仍为该提交。本轮未重复扫描Git历史，未新增或更改教材章节。

|来源|用途与实际核对范围|
|---|---|
|[V22原包清单](../../illustrations/v22/original/manifest.json)、[包内说明](../../illustrations/v22/original/README_FOR_CODEX.md)、149张SVG原件|原包完整保留；逐项重验149个SHA-256。包内声明只是版本/来源记录，不是科学认证。|
|`data/curriculum.json`、`lessons/*.js`、`data/notes/*.json`|真实课程身份及图片位置依据；逐图记录小节名、学习目标和JSON锚点。116章框架与86个已保存小节保留；86不是实际教材总小节数。|
|[原142项任务](../../illustrations/PROMPTS_BATCH_ALL.json)|按必需对象、科学关系、构图及验收要求比对；原ID和完整中英文Prompt不改。|
|原插图主清单的 `scientific_source_register` 和各节来源|逐图继承相关理论出处与原核实状态，不把“部分核实”提升为全面审定。|

上一轮的逐图审查已恢复，包含文字、几何、坐标、单位、箭头、结构、物质/能量流及条件的具体判断。此次通过原件/修订件哈希确认审查对象，并重新运行数值、向量、配平、课程映射、文字边界及浏览器验证；不是从统计截图重建结果。原件与修订图分别记录哈希，修订不覆盖原件。

重点修订的理论依据如下。上轮通过公开教材条目/搜索摘要交叉核对；未声称重新通读整套教材。

|公开教材条目|对应内容|
|---|---|
|[OpenStax College Physics 2e 4.5](https://openstax.org/books/college-physics-2e/pages/4-5-normal-tension-and-other-examples-of-forces)|斜面重力切向/法向分解；另从实际SVG端点独立计算正交、矢量复原和法向力方向。|
|[OpenStax Biology 2e 5.3](https://openstax.org/books/biology-2e/pages/5-3-active-transport)|电化学势、直接ATP泵与次级主动运输的区别；B22高低浓度另以图中粒子数验证。|
|[OpenStax Chemistry 2e 18.9](https://openstax.org/books/chemistry-2e/pages/18-9-occurrence-preparation-and-compounds-of-oxygen)|冷稀条件形成次氯酸盐的语境；C18补冷稀碱条件，反应式另核对原子和电荷。|
|[OpenStax Biology 2e 6.4](https://openstax.org/books/biology-2e/pages/6-4-atp-adenosine-triphosphate)|ATP整体水解、细胞条件与自由能；不将断裂单根键说成直接放能。|
|[OpenStax College Physics 23.1](https://openstax.org/books/college-physics-ap-courses-2e/pages/23-1-induced-emf-and-magnetic-flux)|变磁通可产生电动势；闭合导电回路与感应电流的条件另论。|
|[OpenStax Biology 2e 30.5](https://openstax.org/books/biology-2e/pages/30-5-transport-of-water-and-solutes-in-plants)|叶肉细胞壁蒸发、叶内气隙及经气孔向外扩散；B58修正蒸发位置。|

逐图更多来源见 `ASSET_REVIEW.json` 的 `related_sources`、`source_basis`、`scientific_review`。独立复核涵盖55个数值样本、17条配平式、两张斜面图端点向量、水分子角度与氢键共线、膜运输粒子数、转录互补。定性生物结构的判断另逐图记录，XML通过不算科学通过。

这是工程与内容审核记录，不是教师签审或官方全面审定。本轮没有改变学校安排与董总统考的原有分栏，未新增2027范围、考频或评分细则结论，也没有把V22插图包称为Deep Research报告。
