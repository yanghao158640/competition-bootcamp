# 训练营作品与学习记录

当前个人作品站：https://yanghao158640.github.io/

本仓库保留训练营期间制作的小游戏、课程学习汇报及原始素材。根目录入口跳转至当前作品站，旧作品链接继续使用。

| 内容 | 地址 / 文件 |
| --- | --- |
| 坦克大战 | https://yanghao158640.github.io/competition-bootcamp/tank-game.html |
| 机器学习学习汇报 | https://yanghao158640.github.io/competition-bootcamp/ml-report/ |
| 飞机大战当前版本 | https://yanghao158640.github.io/plane-game/ |
| 历史页面与素材 | `plane-battle.html`、`浪尖.html`、图片、CSS 与脚本 |

坦克大战使用原生 JavaScript / Canvas，含多种坦克、关卡与敌军行为。打开 `tank-game.html` 按页面说明操作；也可从仓库目录运行 `python -m http.server 8000` 后预览。

## 检查与维护

`python gen_harness.py` 会根据当前游戏生成 `tmp/harness.js`，再运行 `node tmp/harness.js` 检查游戏逻辑。生成文件和缓存不提交。

个人简历与作品信息统一在 https://github.com/yanghao158640/portfolio 维护，此仓库不再另存一份简历源码。历史 Netlify 配置保留供已有部署使用。

2026-10-24 清理了内容完全相同的 `浪尖-备份.html`、两份包含旧代码全文的重复说明和一个空文件。清理前版本可从 `maintenance-backup-2026-10-24` 标签恢复。
