# App Store 首屏文章封面示例

原文：《App Store 多了两块新画布，先别急着重做十张截图》。文章讨论新增创意素材后，搜索结果、产品页顶部和截图各自承担的任务。

![微信公众号封面，900 × 383](./cover-wechat.png)

![居中方形裁切预览，383 × 383](./preview-wechat-square.png)

设计选择：用纸页间露出的空白卡片表达“先被看见的一眼”。画面没有 Apple 标志、真实 App Store 界面或具体 App 功能声明。

文件说明：

- `background-wechat.png`：AI 生成的无字背景。
- `background-prompt.md`：背景生成提示词。
- `brief.md`：依据全文整理的设计简报。
- `cover.json`：排版和裁切脚本的输入配置。
- `cover-wechat.png`、`preview-wechat-square.png`：最终封面与中心裁切预览。

在仓库根目录复现排版：

```bash
python3 editorial-cover-skill/scripts/render_cover.py \
  --spec editorial-cover-skill/examples/app-store-first-screen/cover.json \
  --out /tmp/editorial-cover-app-store-first-screen
```

运行前需安装 Pillow，具体方法见 Skill 的 [README](../../README.md)。
