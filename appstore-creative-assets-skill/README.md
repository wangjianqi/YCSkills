# App Store Creative Assets Skill

一个通用的 App Store 素材生成 Skill，用于创建 Apple App Store 的：

- **Product Page Header（产品页面标题）**
- **Search Results（搜索结果）**

核心目标不是套模板，而是：

> **先理解 App，再生成素材。**

适用于 iOS / iPadOS / macOS 等 App，也可以用于游戏和其他 App Store 产品。

---

## 核心能力

### 1. 自动建立 App 的视觉 DNA

从用户提供的：

- App 截图
- App Icon
- App Store 截图
- 官网
- 品牌规范
- 产品描述

提取：

- 色彩
- 字体气质
- 间距
- 圆角
- Material
- 阴影
- UI 密度
- 图标语言
- 图片 / 3D 语言
- 品牌个性

然后以这些信息作为素材设计依据。

### 2. 支持 Apple 当前创意素材规格

| 展示位置 | 比例 | 分辨率 |
|---|---:|---:|
| Product Page Header | 21:9 | 3840 × 1646 |
| Product Page Header | 16:9 | 5244 × 2950 |
| Search Results | 3:2 | 1920 × 1280 ～ 3840 × 2560 |
| Search Results | 16:9 | 5244 × 2950 |

图片不能包含 Alpha 通道或透明度。

Apple 当前官方规格：
https://developer.apple.com/help/app-store-connect/reference/app-information/creative-assets-specifications

Apple Marketing Resources and Identity Guidelines：
https://developer.apple.com/app-store/marketing/guidelines/

> 以上规范可能随 Apple 更新而变化。正式提交前应重新检查 Apple 官方文档。

### 3. 极简设计，但不是固定黑白

这个 Skill 的默认设计原则是：

**Minimal + Product-led + Brand-consistent**

但不会默认：

- 黑白
- 紫色
- 玻璃
- 霓虹
- 渐变
- 3D
- 手机 Mockup
- 科技感

这些都必须由 App 本身的视觉语言决定。

### 4. 每个版位独立构图

不会简单把一张图拉伸成：

- 21:9
- 16:9
- 3:2

而是保持同一个视觉系统，同时针对不同版位重新构图。

### 5. 多语言

支持：

- English
- 简体中文
- 其他语言

不会简单替换文字，而会重新处理：

- 换行
- 字号
- 字宽
- 间距
- 光学平衡
- 视觉层级

### 6. Apple Marketing QA

Skill 特别限制了 Apple 产品素材的使用方式，避免生成不符合 Apple Marketing Guidelines 的 Apple 产品 3D 模拟图。

---

## 推荐使用方式

### 最佳输入

直接提供：

1. App 截图
2. App Icon
3. App 名称
4. App 核心功能

例如：

```text
这是我的 App。

App 名称：MonoPDF

这是 App 的截图和 Icon。

帮我生成：
1. Product Page Header 21:9
2. Product Page Header 16:9
3. Search Results 3:2
4. Search Results 16:9

风格要求：
极简，但要和 App 本身的 UI 风格一致。
```

Skill 会先分析 App，而不是立即套一个模板。

---

## 推荐工作流

```text
App 截图
   ↓
视觉分析
   ↓
Visual DNA
   ↓
核心卖点
   ↓
标题 / 文案
   ↓
版位构图
   ↓
生成
   ↓
技术检查
   ↓
品牌检查
   ↓
Apple Marketing 检查
```

---

## 开源结构

```text
appstore-creative-assets-skill/
├── SKILL.md
├── README.md
├── LICENSE
├── references/
│   ├── apple-specifications.md
│   └── apple-marketing-guidelines.md
└── examples/
    ├── minimal-app.md
    ├── creative-app.md
    └── utility-app.md
```

---

## 不解决什么

这个 Skill **不是**：

- App Store ASO 关键词工具
- App Store 截图批量模板工具
- 自动生成 App UI 的工具
- Logo 生成 Skill
- 通用广告 Banner Skill
- 单纯的 AI 海报生成 Prompt

它专门解决：

> **如何根据一个真实 App 的产品与视觉系统，生成高质量 App Store Product Page Header / Search Results 素材。**

---

## 版本

**v1.0.0**

第一版重点是建立可靠的通用工作流，而不是堆大量模板。

后续可以考虑：

- 自动生成 3～8 张完整素材系列
- 自动生成不同卖点版本
- ASO 文案与视觉联动
- App Store 截图 + Header + Search Results 统一视觉系统
- 多语言批量生成
- 自动技术规格检查
- 自动生成可编辑的 Figma / SVG 版式
