# Kennan's AI Toolbox / 恺南的AI工具箱

> Minimal · Advanced · Inspired by Apple.com / 极简 · 高级 · 灵感源自 Apple 官网

## 🌐 网站信息 / Website Information

- **域名 / Domain**: [https://aitoolbox.uk/](https://aitoolbox.uk/)
- **状态 / Status**: 在线运行 / Online
- **托管平台 / Hosting**: Cloudflare Pages

## Highlights / 项目亮点

- **Keyword Search**: Real-time search in both English and Chinese. / 支持中英文关键词实时搜索。
- **Multi-tag Filtering**: Combine tags for precise filtering. / 可多选标签组合过滤。
- **Bilingual Switch**: One-click switch between English and Chinese. / 一键切换中英文界面。
- **Responsive UI**: Apple-style, works on PC and mobile. / 苹果风格设计，适配PC和移动端。
- **Static Hosting**: No backend needed, supports Cloudflare Pages, GitHub Pages, etc. / 无需后端，支持静态托管。

## Quick Preview / 快速预览

- Homepage shows all categories. / 首页展示所有工具分类。
- Group page supports:
  - Top search bar for real-time filtering. / 顶部关键词搜索框，实时筛选。
  - Multi-tag filtering. / 多标签筛选。
  - Tool cards show name, description, tags, and link. / 工具卡片展示名称、简介、标签、访问链接。
- Top-right language toggle. / 右上角语言切换按钮。

## Usage / 使用方法

1. Clone or download this repo. / 克隆或下载本项目
2. Local preview (recommended):
   ```bash
   cd ai_tools_web
   python -m http.server 8080
   ```
   Then open http://localhost:8080/index.html / 然后浏览器访问
3. Deploy to Cloudflare Pages, GitHub Pages, etc. / 部署到静态平台
4. **Production URL**: [https://aitoolbox.uk/](https://aitoolbox.uk/)

## Data Structure / 数据结构说明

- `ai_tools.json` supports bilingual fields. / 支持中英文字段。
  ```json
  [
    {
      "group_en": "AI Content Detection",
      "group_zh": "AI内容检测",
      "tools": [
        {
          "name_en": "AISEO AI Content Detector",
          "name_zh": "AISEO AI内容检测器",
          "desc_en": "AISEO's AI content detection and SEO optimization tool.",
          "desc_zh": "AISEO推出的AI内容检测与SEO优化工具。",
          "tags_en": ["Content Detection", "SEO"],
          "tags_zh": ["内容检测", "SEO"],
          "url": "https://aiseo.ai/AI-tools/ai-content-detection.html"
        }
      ]
    }
  ]
  ```

## Bilingual Demo / 关键词搜索与双语切换演示

- Enter keywords (e.g. "content" or "内容") to filter tools. / 输入关键词实时筛选。
- Click "English/中文" to switch language. / 点击切换语言。

---

For batch data conversion, translation scripts, or custom features, contact the author! / 如需批量数据转换、自动翻译脚本或其它定制功能，欢迎联系作者！

---

## 🚀 Local Preview

1. Enter the project folder
   ```bash
   cd ai_tools_web
   ```
2. Start a local server
   ```bash
   python -m http.server 8000
   ```
   Then open in browser: [http://localhost:8000](http://localhost:8000)

---

## 🌐 Git Management

1. Initialize git repo (if not yet)
   ```bash
   git init
   ```
2. Add and commit
   ```bash
   git add .
   git commit -m "Init web folder git repo"
   ```
3. Add remote repository
   ```bash
   git remote add origin https://github.com/yourname/yourrepo.git
   ```
4. Push to remote
   ```bash
   git push -u origin main
   ```

---

## 📝 Customization & Extension

- Edit `ai_tools.json` to add/modify tools.
- Add new categories/tags directly in JSON.
- Responsive front-end, mobile-friendly.
- For new features, open an issue or PR.

---

## 📷 Preview

![screenshot](screenshot.png)

---

## 📄 License

MIT
