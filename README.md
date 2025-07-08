# 恺南的AI工具箱

> 极简 · 高级 · 灵感源自 Apple 官网

## 项目亮点

- **关键词搜索**：支持中英文关键词实时搜索，快速定位所需AI工具。
- **多标签筛选**：可多选标签组合过滤，精准查找。
- **中英文切换**：一键切换中英文界面，所有工具、分组、标签、描述均双语展示。
- **响应式美观UI**：苹果风格设计，适配PC和移动端。
- **本地静态部署**：无需后端，支持 Cloudflare Pages、GitHub Pages 等静态托管。

## 快速预览

- 首页展示所有工具分类，点击进入分组页。
- 分组页支持：
  - 顶部关键词搜索框，输入中英文均可实时筛选工具
  - 多标签筛选，可与搜索叠加
  - 工具卡片展示名称、简介、标签、访问链接
- 右上角语言切换按钮，支持中英文界面一键切换

## 使用方法

1. 克隆或下载本项目
2. 本地预览（推荐用本地服务器）：
   ```bash
   cd ai_tools_web
   python -m http.server 8080
   ```
   然后浏览器访问 http://localhost:8080/index.html
3. 也可直接部署到 Cloudflare Pages、GitHub Pages 等平台

## 数据结构说明

- `ai_tools.json` 为分组结构，支持中英文字段：
  ```json
  [
    {
      "group_zh": "AI内容检测",
      "group_en": "AI Content Detection",
      "tools": [
        {
          "name_zh": "AISEO AI内容检测器",
          "name_en": "AISEO AI Content Detector",
          "desc_zh": "AISEO推出的AI内容检测与SEO优化工具。",
          "desc_en": "AISEO's AI content detection and SEO optimization tool.",
          "tags_zh": ["内容检测", "SEO"],
          "tags_en": ["Content Detection", "SEO"],
          "url": "https://aiseo.ai/AI-tools/ai-content-detection.html"
        }
      ]
    }
  ]
  ```

## 关键词搜索与双语切换演示

- 在分组页顶部输入关键词（如"内容"或"content"），工具列表会实时筛选。
- 点击右上角"English/中文"按钮，界面和数据即时切换中英文。

---

如需批量数据转换、自动翻译脚本或其它定制功能，欢迎联系作者！

---

## 🚀 本地预览 / Local Preview

1. 进入 web 文件夹 / Enter the `web` folder  
   ```bash
   cd web
   ```

2. 启动本地服务器 / Start a local server  
   ```bash
   # Python 3
   python -m http.server 8000
   ```
   然后在浏览器访问 / Then open in browser:  
   [http://localhost:8000](http://localhost:8000)

---

## 🌐 Git 管理 / Git Management

1. 初始化仓库（如未初始化）/ Initialize git repo (if not yet)
   ```bash
   git init
   ```

2. 添加并提交 / Add and commit
   ```bash
   git add .
   git commit -m "初始化 web 文件夹的 Git 仓库 / Init web folder git repo"
   ```

3. 关联远程仓库 / Add remote repository
   ```bash
   git remote add origin https://github.com/你的用户名/你的仓库名.git
   ```

4. 推送到远程 / Push to remote
   ```bash
   git push -u origin master
   ```

---

## 📝 自定义与扩展 / Customization & Extension

- 你可以在 `ai_tools.json` 中添加、修改工具数据。
- 如需添加新分类或标签，直接在 JSON 文件中编辑即可。
- 前端页面支持自适应，移动端体验良好。
- 如需增加搜索、夜间模式等功能，欢迎提 Issue 或 PR。

You can add or modify tool data in `ai_tools.json`.  
To add new categories or tags, simply edit the JSON file.  
The front-end is responsive and mobile-friendly.  
For features like search or dark mode, feel free to open an issue or pull request.

---

## 📷 效果预览 / Preview

![screenshot](screenshot.png)  
（可自行添加网站截图 / You can add your own screenshot here）

---

## 📄 License

MIT
