
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
