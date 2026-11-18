# UEC 2027 V22 · Codex 专用教学 SVG 精简修订包

**此版本不是新增数量轮：保留 V21 的 149 张 SVG，修正其中 8 张。**

## 修正项目
- `B05_aerobic_respiration_stages_ae90b772e.svg`：重绘四阶段细胞呼吸，修复 FADH2 与 ATP 断裂、调整分阶段生成物
- `C20_carbonate_bicarbonate_acid_consumption.svg`：重新绘制缺失的碳酸盐、碳酸氢盐酸反应式及计量关系
- `P41_uniform_electric_field_forces.svg`：修正物理或生物标注、假设条件或表述精度
- `P43_ideal_transformer_turns_ratio.svg`：修正物理或生物标注、假设条件或表述精度
- `P50_RC_capacitor_charging.svg`：修正物理或生物标注、假设条件或表述精度
- `P57_archimedes_buoyancy_fbd.svg`：修正物理或生物标注、假设条件或表述精度
- `B57_translation_start_stop_codons.svg`：修正物理或生物标注、假设条件或表述精度
- `B59_ADH_water_balance_negative_feedback.svg`：修正物理或生物标注、假设条件或表述精度

## 接入规则

1. 此包内仅有 `assets/`、`manifest.json` 和本说明；没有 PNG 预览、旧 ZIP 或重复报告。
2. 请严格以 manifest 的 `path` 引用，校验 SHA-256；已有同名资源应以 V22 修订版为准，避免保留旧错误文本。
3. 状态 `corrected_pending_independent_scientific_review` 表示**完成技术修正，但还没经过独立学科审核**。其余仍为 `pending_subject_review`。
4. 不要按文件数量宣称已完成 142 项原始任务。task ID 对照和原教材小节映射仍未全部完成。
5. 重点复核：C20 酸性条件与 2:1 氢离子计量；B05 分阶段 ATP、NADH、FADH2 数量；P57 排水体积定义；P43 理想模型与绕组；B59 激素负反馈。
6. 若图片未对应网站已存在的真实章节，不要擅自创建章节或随意发布。
