# 听途 4.3(a) 文章封面示例

这篇文章讨论一个从零开发的 App 被以 4.3(a) 相似性理由拒审，作者没有拿到具体比对依据。封面只保留真实 App Store 图标和拒审代码 `4.3(a)`；具体经历由文章标题说明。它不描绘苹果内部检测机制。

![公众号横幅封面](./cover-wechat.png)

[查看居中方形预览](./preview-wechat-square.png)

这是使用 Pillow 排版和绘制的封面，不依赖 AI 生图。`app-store-icon.png` 提取自 macOS 系统自带的 `/System/Applications/App Store.app/Contents/Resources/AppIcon.icns`，图标及品牌归 Apple 所有；这里仅用于识别文章主题，不暗示官方关联。`make_background.py` 绘制深色底图、放置真实图标与拒审代码；`cover.json` 交给 Skill 的 `render_cover.py` 完成裁切。

在仓库根目录复现：

```bash
python3 editorial-cover-skill/examples/tingtu-43a/make_background.py
python3 editorial-cover-skill/scripts/render_cover.py \
  --spec editorial-cover-skill/examples/tingtu-43a/cover.json \
  --out /tmp/editorial-cover-tingtu-43a
```
