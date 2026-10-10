# Editorial Cover Skill

面向 Codex、Claude Code 等支持 Agent Skills `SKILL.md` 格式的编码智能体：读取中文文章提炼视觉概念，优先使用真实素材，必要时调用智能体可用的图片生成工具制作**无字背景**，最终用 Pillow 做中文排版和多平台裁切检查。

**默认风格：** 克制的黑白灰 / 暖白，留白大，不用科技霓虹/悬浮球/假文字等常见 AI 生图套路。

## 安装

### 方式一：从 YCSkills 仓库获取（推荐）

```bash
git clone https://github.com/wangjianqi/YCSkills.git
mkdir -p ~/.codex/skills
cp -R YCSkills/editorial-cover-skill ~/.codex/skills/
```

### 方式二：直接复制单个 Skill

也可将整个 `editorial-cover-skill` 文件夹单独复制到：

```bash
mkdir -p ~/.codex/skills
cp -R /path/to/editorial-cover-skill ~/.codex/skills/
```

或放到特定项目的 `.agents/skills/editorial-cover/` 下。

### 安装依赖

```bash
python3 -m pip install -r ~/.codex/skills/editorial-cover-skill/requirements.txt
```

注意：若 macOS PEP 668 阻止全局 pip，请使用 venv，例如：

```bash
python3 -m venv ~/.venvs/editorial-cover
~/.venvs/editorial-cover/bin/pip install -r ~/.codex/skills/editorial-cover-skill/requirements.txt
```

Skill 调用示例：

```
$editorial-cover 请读取 /path/to/article.md，为微信公众号、小红书和抖音各做一张简洁封面。默认公众号无字，后两者用极少中文。使用可用的生图工具生成无字背景，然后程序排版；出图后检查安全区。
```

## 无图像生成工具时

可以用纯色背景及排版得到最终 PNG，但这只能算“纯文字封面”，不能假装已经完成摄影/插图；若背景与文字均未提供，脚本会拒绝生成空白图。你也可以提供一张自己拥有版权的背景图。

## 独立运行排版脚本

```bash
~/.venvs/editorial-cover/bin/python scripts/render_cover.py --spec examples/cover.example.json --out /tmp/editorial-cover-preview
```

脚本使用 JSON 中指定的背景（可在顶层及平台级指定 `background`），并分别导出三张封面、方形预览、安全区检查预览；文本由操作系统已有的中文字体绘制，不随 Skill 分发任何字体文件。背景图片路径可相对于 JSON 文件所在目录指定。

## 目录

- `SKILL.md`：能力边界与完整工作流
- `references/platforms.md`：平台画幅及安全区说明
- `references/prompts.md`：无字生图 prompt 原则
- `scripts/render_cover.py`：实际输出 PNG 的程序
- `examples/cover.example.json`：渲染配置示例
- `agents/openai.yaml`：Agent 技能展示元信息

## 关于

本 Skill 是 [YCSkills](https://github.com/wangjianqi/YCSkills) 仓库的一部分。欢迎在该仓库提交 Issue 或 PR。
