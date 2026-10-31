# 37校生物学原创力报告：Codex Cloud工作副本

## 首次启动

1. 将本项目恢复到Cloud工作目录：`python restore_cloud_snapshot.py`。
2. 校验：`python scripts/cloud_data.py verify`。
3. 核对样本：`python scripts/cloud_data.py summary`，应为84,789篇、37校、107名人才观察作者。
4. 如需查询逐篇数据：`python scripts/cloud_data.py init-db`。
5. 读取 `37_school_formal_report_20261031/report/37校生物学原创力分析报告_20261031.md`，按用户意见修改文字。

基础恢复、校验和SQL查询只用Python标准库，不需要服务器网络、SSH密码或本地大模型。当前Cloud工作副本支持报告编辑、已有数据复核、重新分组和后续配图。新增原始库检索与服务器模型推理需要另外建立服务访问。

## 数据入口

- `37_school_offline_data_20261031/data/papers_enriched.csv.gz`：逐篇评级、标题/DOI/年份/样本学校、引用/JIF、各维度评语。
- `data/cloud_metadata.jsonl.gz`：可匹配论文的摘要、关键词、WoS分类、作者、机构地址与通讯作者信息。
- `37_school_main_outline_20261031/data/17_paper_analysis_features.csv.gz`：逐篇方向、合作形式及作者国家角色。
- `37_school_chapters_1_3_wos_20261031/tables/`：前三章方向及统计表。
- `37_school_formal_report_20261031/analysis/`：已批准的作者贡献、身份/机构关联、方向和人才排名。
- `37_school_formal_report_20261031/audit/`：关键核验记录。

## SQL示例

`python scripts/cloud_data.py sql "SELECT originality_grade, COUNT(*) AS n FROM papers GROUP BY originality_grade"`

`python scripts/cloud_data.py sql "SELECT title,doi,originality_grade,overall_comment FROM papers WHERE wos_id='WOS:000720146700002'"`

`python scripts/cloud_data.py sql "SELECT source_wos_id,json_extract(payload_json,'$.abstract') AS abstract FROM bibliography LIMIT 3"`

CSV转入SQLite的字段以TEXT保存；数字运算请显式转换，先用NULLIF(field,'')处理缺失，不能把空值转换成0。SQL命令为只读，结果最多输出500行；新分析脚本可写独立结果文件。

## 保存工作

Cloud已有任务保留自己的文件；新任务从已发布环境启动。请将重要报告和脚本修改保存到私有仓库，或导出成果。恢复脚本不会覆盖已存在的文件。不要把生成的SQLite数据库或任何登录凭据提交仓库。

原始工作簿及完整WoS/CrossRef底库仍保存在原服务器；本副本不包含服务器认证信息。最新任务约定见AGENTS.md与WORK_STATE.json。
