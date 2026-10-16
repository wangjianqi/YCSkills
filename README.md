# YCSkills

一个面向 Codex、Claude Code 等支持 Agent Skills（`SKILL.md` 格式）的编码智能体的 Skill 集合。每个 Skill 独立成目录，按需取用。

## Skill 列表

| Skill | 说明 | 适用场景 |
|---|---|---|
| [editorial-cover](./editorial-cover-skill/) | 从中文文章生成克制、有编辑设计感的封面，支持公众号 / 小红书 / 抖音多平台 | 需要给文章、笔记、视频配封面时 |

## 安装

### 方式一：克隆整个仓库

```bash
git clone https://github.com/wangjianqi/YCSkills.git
```

然后将需要的 skill 文件夹复制到智能体的 skills 目录：

```bash
# Codex (macOS)
mkdir -p ~/.codex/skills
cp -R YCSkills/editorial-cover-skill ~/.codex/skills/

# 或放到特定项目中
cp -R YCSkills/editorial-cover-skill your-project/.agents/skills/
```

### 方式二：只获取单个 Skill

直接下载 skill 文件夹即可，每个 skill 自包含运行所需的一切。

### 安装依赖

部分 skill 有额外依赖（如 Python 包），在各 skill 的 `requirements.txt` 或 `README.md` 中说明。

```bash
pip install -r ~/.codex/skills/editorial-cover-skill/requirements.txt
```

## 使用

Skill 的调用方式取决于你使用的智能体。通常在对话中引用 skill 名称或路径即可。

以 `editorial-cover` 为例：

```
$editorial-cover 请读取 /path/to/article.md，为微信公众号、小红书和抖音各做一张简洁封面。
```

详见各 skill 目录下的 `README.md` 和 `SKILL.md`。

## 贡献

欢迎贡献新的 skill 或改进现有 skill。请阅读 [CONTRIBUTING.md](./CONTRIBUTING.md) 了解目录规范和提交流程。

## License

本仓库采用 [MIT License](./LICENSE)。每个 skill 目录内的脚本和配置文件同样遵循此许可。
