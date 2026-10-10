# 贡献指南

感谢你想为 YCSkills 做贡献！本文档说明如何提交新的 skill 或改进现有 skill。

## 贡献流程

1. Fork 本仓库到你的 GitHub 账号
2. 创建特性分支：`git checkout -b feature/new-skill-name`
3. 提交变更：`git commit -m "feat: add xxx skill"`
4. 推送分支：`git push origin feature/new-skill-name`
5. 发起 Pull Request

## Skill 目录结构

每个 skill 必须作为仓库根目录下的一个独立文件夹存在。推荐使用小写字母 + 连字符命名，如 `editorial-cover-skill`。

```
your-skill-name/
├── SKILL.md              # 必填。核心文件，定义 skill 的名称、描述、工作流
├── README.md             # 必填。面向人类的安装与使用说明
├── requirements.txt      # 可选。Python 依赖
├── package.json          # 可选。Node.js 依赖
├── scripts/              # 可选。辅助脚本（渲染、处理等）
│   └── your_tool.py
├── references/           # 可选。参考资料、规格说明、prompt 模板
│   └── specs.md
├── examples/             # 可选。示例输入输出
│   └── example.json
└── agents/               # 可选。Agent 元信息配置
    └── openai.yaml
```

## SKILL.md 格式

`SKILL.md` 是最关键的文件，智能体通过它理解 skill 的能力边界和工作流程。文件开头必须包含 YAML frontmatter：

```markdown
---
name: your-skill-name
description: 一句话描述这个 skill 能做什么、什么时候使用、什么时候不使用。
---

# Your Skill Name

## 任务工作流

### 1. 第一步
...

### 2. 第二步
...

## 完成时交付
...
```

### Frontmatter 字段说明

- `name`：唯一的 skill 标识，小写字母 + 连字符。与目录名保持一致（去掉 `-skill` 后缀）。
- `description`：必须清晰说明：
  - skill 做什么
  - 何时使用（触发词或场景）
  - 何时**不**使用（避免误用）

### 正文内容建议

1. 逐步的任务工作流（编号列表）
2. 每个步骤的具体操作、约束和检查点
3. 完成时的交付说明
4. 首次调用示例（可选但推荐）

## README.md 要求

面向人类读者，应包含：

- Skill 功能简介
- 安装方法（从仓库复制 / 克隆 / 依赖安装）
- 使用示例
- 目录结构说明（简要列举关键文件）
- 已知限制或注意事项

## 质量检查清单

提交 PR 前请确认：

- [ ] Skill 目录命名符合 `kebab-case-skill` 规范
- [ ] `SKILL.md` 包含正确的 YAML frontmatter（name + description）
- [ ] 工作流步骤清晰、可执行
- [ ] `README.md` 中的安装和使用说明可跑通
- [ ] 不包含运行时产物（outputs/、*.png 等）
- [ ] 不包含第三方字体、图片等非必要二进制文件
- [ ] 依赖声明完整（requirements.txt / package.json）

## 建议

- 先在本地手动测试完整工作流，确认各环节没有遗漏
- 如果有脚本工具，建议在 examples/ 中提供可复现的示例
- 对涉及外部 API 或服务的 skill，请说明鉴权方式和费用
