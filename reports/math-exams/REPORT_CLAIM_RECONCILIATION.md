# 附带研究报告与原卷审计的对应

保留原始导入778条主张不变；网站使用独立逐页转录的1479条计分/题目单元。两者粒度不同，不能比较条目总数来判断题数是否相同。

逐条旧主张→原页单元、章号及分值变化见[REPORT_CLAIM_RECONCILIATION.json](REPORT_CLAIM_RECONCILIATION.json)。自动匹配只用于定位和字段差异，不认证旧报告的公式、答案、难度或“人工核对”标签。

|对应状态|旧主张数|
|---|---:|
|source_fields_replace_report_with_differences|184|
|source_locator_and_chapter_marks_agree_not_answer_certification|589|
|explicit_reviewed_label_correspondence|5|

无法对应的小问保留同大题候选列表，不擅改原编号。旧报告整题单章的归类被原卷逐小问的多章记录取代，旧报告的选答“有效分值”没有作为实际考生权重。

具体数学转录纠错与表述争议仍以[CORRECTIONS.json](CORRECTIONS.json)为准；2024毕业第10题分项采用原题6/4，不采用蓝图5/5。
