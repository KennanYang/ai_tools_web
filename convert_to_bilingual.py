import json
import hashlib
import random
import requests
import time

# baidu translate api
appid = 'xx'
secretKey = 'xx'

def baidu_translate_batch(queries, from_lang='zh', to_lang='en'):
    q = '\n'.join(queries)
    salt = str(random.randint(32768, 65536))
    sign = appid + q + salt + secretKey
    sign = hashlib.md5(sign.encode()).hexdigest()
    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    params = {
        'q': q,
        'from': from_lang,
        'to': to_lang,
        'appid': appid,
        'salt': salt,
        'sign': sign
    }
    for _ in range(10):  # 最多重试10次
        try:
            r = requests.get(url, params=params, timeout=8)
            result = r.json()
            if 'trans_result' in result:
                res = [item['dst'] for item in result['trans_result']]
                # 保证返回条数和输入一致
                if len(res) != len(queries):
                    print(f"警告：翻译返回条数不符，原:{len(queries)}，返:{len(res)}，用原文补齐")
                    while len(res) < len(queries):
                        res.append(queries[len(res)])
                return res
            elif result.get('error_code') == '54003':
                print('QPS超限，等待60秒重试...')
                time.sleep(60)
                continue
            else:
                print('翻译失败:', result)
                return queries
        except Exception as e:
            print('翻译异常:', e)
            time.sleep(10)
    return queries

with open('ai_tools.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# 收集所有 desc_zh
desc_zh_list = []
for group in data:
    for tool in group['tools']:
        desc_zh_list.append(tool['desc_zh'])

# 分批翻译，防止超限（每批20条）
desc_en_list = []
batch_size = 20
for i in range(0, len(desc_zh_list), batch_size):
    batch = desc_zh_list[i:i+batch_size]
    desc_en_list.extend(baidu_translate_batch(batch))
    time.sleep(2)  # 每批之间暂停2秒

print(f"desc_zh_list: {len(desc_zh_list)}, desc_en_list: {len(desc_en_list)}")

# 回填 desc_en
idx = 0
for group in data:
    for tool in group['tools']:
        tool['desc_en'] = desc_en_list[idx]
        idx += 1

with open('ai_tools_bilingual.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print('desc_zh 批量翻译完成，已生成 ai_tools_bilingual.json')