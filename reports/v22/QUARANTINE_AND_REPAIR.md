# 隔离与修图要求

以下两图仅保留于原包归档，不在 `assets/v22/` 中，没有教学页面引用。不得以文件能解析或能显示为由解除隔离。原有5张错误P0图的隔离也保持不变。

## B39 · 线粒体结构

包内ID：`B39_mitochondrion_membranes_matrix`。可确认的真实小节：生物2.3「细胞器——系统内的分工协作」。

原稿把“内膜/嵴”画成悬浮、开放的正弦线，缺少闭合内膜、嵴连续性和膜间隙，不能作为精确结构图。修图必须用确定性SVG，建议1200×800：闭合外膜包围连续闭合的内膜，内膜向基质内折叠形成嵴；膜间隙在两膜之间，基质在内膜内。引线必须终止于实际结构，标“外膜、内膜、嵴、膜间隙、基质”，说明非比例切面。若增加电子链/ATP合成酶，必须放在内膜，并正确表示质子向膜间隙泵送、经ATP合成酶回基质，不能凭装饰箭头补过程。

中文Prompt：制作可审查的线粒体剖面教学SVG，1200×800白底。绘制完整闭合外膜与完整连续闭合内膜，内膜向基质伸入形成多个嵴，膜间隙必须处于两层膜之间，基质位于内膜包围区域。中文标注外膜、内膜、嵴、膜间隙、基质，细引线精确指向结构。保持膜连续性，不用悬浮正弦线代替内膜。注明非比例概念切面。本图只说明结构，不添加未经核对的代谢箭头。

English prompt: Create a verifiable 1200 by 800 SVG teaching cross-section of a mitochondrion on a white background. Draw a closed outer membrane enclosing a continuous closed inner membrane with inward folds forming cristae. The intermembrane space must lie between the two membranes; the matrix must occupy the space enclosed by the inner membrane. Use accurate leader lines with Chinese labels 外膜, 内膜, 嵴, 膜间隙, 基质. State that this is a schematic cross-section, not to scale. Do not add unverified metabolic arrows. Preserve membrane continuity throughout.

Negative Prompt：开放或悬浮的内膜线、嵴与内膜断开、膜间隙放到基质内、文字截断、装饰性代谢箭头、真实照片风格替代结构图；open floating inner membrane, detached cristae, intermembrane space inside matrix, clipped labels, decorative process arrows, photorealistic substitute for structural geometry。

依据：[OpenStax Biology 2e 4.3](https://openstax.org/books/biology-2e/pages/4-3-eukaryotic-cells)。验收时检查膜的闭合/连续、区室与引线，再检查手机放大后的标签。对应原任务 `ILL-ASSET-B2_3B`、`ILL-ASSET-B3_5B` 的结构缺口仍保留。

## B41 · 保卫细胞与气孔

包内ID：`B41_stomatal_guard_cell_turgor_open_closed`。真实小节尚未确认；不虚构编号。现有章级候选为生物6「营养成分的运输」，仅供后续核对。

原稿用两个孤立同心椭圆代替保卫细胞，无法表达细胞两端相接、内外壁差异和弯曲形成孔隙。建议确定性SVG，1200×800，并列典型肾形保卫细胞的开放/关闭状态；两细胞末端相接、气孔位于两者之间，朝孔内壁较厚、外壁较薄。开放时膨压较高且弯曲形成明显孔隙；关闭时膨压较低、孔隙缩小。限定为典型肾形模型，不概括所有植物（禾本科可为哑铃形）。

中文Prompt：绘制1200×800白底科学SVG，比较典型肾形保卫细胞气孔开放和关闭。每个面板含一对末端相接的保卫细胞，气孔在两细胞之间，朝向孔隙的内壁较厚、外壁较薄。开放面板显示较高膨压下细胞弯曲、中央孔隙明显；关闭面板显示膨压较低、孔隙缩小。中文标签包括保卫细胞、气孔、内壁较厚、外壁较薄、膨压较高、膨压较低。注明典型肾形示意、非比例，不代表所有植物。不要将两个分离的圆环当作保卫细胞。

English prompt: Produce a precise 1200 by 800 SVG comparing open and closed stomata in a typical kidney-shaped guard-cell model. Each panel must show two guard cells joined at their ends with the pore between them. Draw thicker pore-facing walls and thinner outer walls. The open panel shows higher turgor and curvature creating a clear central pore; the closed panel shows lower turgor and a narrowed pore. Include Chinese labels 保卫细胞, 气孔, 内壁较厚, 外壁较薄, 膨压较高, 膨压较低. State that the model is schematic and does not represent every plant species. Do not assign a textbook subsection number.

Negative Prompt：孤立圆环、两细胞端点分离、孔隙画在单细胞内、壁厚关系颠倒、所有植物都肾形、未经核对编号、错误水流箭头；isolated rings, disconnected guard-cell ends, pore inside one cell, reversed wall thickness, universal kidney-shape claim, invented subsection number, unverified water-flow arrows。

依据：[OpenStax Biology 2e 30.5](https://openstax.org/books/biology-2e/pages/30-5-transport-of-water-and-solutes-in-plants)。通过结构审核后仍须确认真实小节，才能接入。
