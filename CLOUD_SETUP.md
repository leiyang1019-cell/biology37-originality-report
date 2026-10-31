# Cloud环境设置

建议私有仓库：biology37-originality-report，仅用于此独立报告。

将本目录全部内容（保留cloud_payload目录）放入该私有仓库。在Codex网页或桌面端进入Settings > Codex Cloud > Environments > Create environment，选择仓库，要求执行：

```
python restore_cloud_snapshot.py
python scripts/cloud_data.py verify
python scripts/cloud_data.py summary
```

安装准备阶段完成后发布（Publish）环境。手机端Cloud选择此环境新建任务，并先读取AGENTS.md、WORK_STATE.json及主报告。首次Cloud启动后再次运行summary，核对84,789篇/37校/107名观察作者，才视为云端接入成功。

仓库包含当前报告的便携工作副本。完整备份另存于本仓库的 backup-20261031 Release 附件，包含原始评价表、完整已提取离线数据库、提纲与模板及追溯资料。参见 BACKUP_LOCATION.md。

上传仓库不等于Cloud环境已经创建或验收。请完成恢复、核对和发布后，再在手机新任务中测试。Cloud文件持久性、每个任务独立工作区及发布设置以官方文档为准：https://learn.chatgpt.com/docs/environments/cloud-environments
