import re
import json

def md_to_json(md_path, json_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    data = []
    category = None
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        # 检查分组标题
        if line.startswith('## '):
            category = line.replace('## ', '').strip()
            i += 1
            continue
        # 检查工具条目
        if line.startswith('- **') and line.endswith('**'):
            name = re.sub(r'- \*\*(.+)\*\*', r'\1', line)
            desc = ''
            tags = []
            url = ''
            # 读取后面三行
            if i+1 < len(lines) and lines[i+1].strip().startswith('简介：'):
                desc = lines[i+1].strip().replace('简介：', '').strip()
            if i+2 < len(lines) and lines[i+2].strip().startswith('标签：'):
                tags_line = lines[i+2].strip().replace('标签：', '').strip()
                tags = [tag.replace('#', '').strip() for tag in tags_line.split() if tag.startswith('#')]
            if i+3 < len(lines) and lines[i+3].strip().startswith('链接：'):
                url_match = re.search(r'\[(.*?)\]\((.*?)\)', lines[i+3])
                url = url_match.group(2) if url_match else lines[i+3].strip().replace('链接：', '').strip()
            data.append({
                "category": category,
                "name": name,
                "desc": desc,
                "tags": tags,
                "url": url
            })
            i += 4
        else:
            i += 1

    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    md_to_json('ai_tools.md', 'ai_tools.json')