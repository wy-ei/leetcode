#encoding: utf-8
import requests
import os
import urllib

def fetch_question_data(slug):
    query = """
        query questionData($titleSlug: String!) {
            question(titleSlug: $titleSlug) {
                translatedTitle
                translatedContent
                questionFrontendId
                difficulty
                titleSlug
            }
        }
    """

    cookie = """
    _ga=GA1.2.521507415.1564918432; _uab_collina=156491843254476020508502; gr_user_id=2e8c28c5-f2b4-4b02-8b8e-1b3cce152956; grwng_uid=9b334909-046d-4114-8564-7e60a8bfdec0; __auc=5f079ae316ecc493a7e3fb5e9eb; csrftoken=FzLIzSZ2T5cuuLgjoEmruDcKLHU3cgl8CaXcLY0UKFTQ9s4DvplojXggpViTW5Po; a2873925c34ecbd2_gr_last_sent_cs1=wy-ei; __atuvc=0%7C10%2C0%7C11%2C0%7C12%2C0%7C13%2C1%7C14; _gid=GA1.2.52836382.1589165921; LEETCODE_SESSION=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJuZXh0X2FmdGVyX29hdXRoIjoiL3Byb2JsZW1zL2xvbmdlc3QtcGFsaW5kcm9taWMtc3Vic3RyaW5nLyIsIl9hdXRoX3VzZXJfaWQiOiI0MDY4NCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiYzI3YTZhYjI0ZTVlMmNkNDFmN2Q3YzM1ODE4ODkzNmQ4ZDlhOGI5MSIsImlkIjo0MDY4NCwiZW1haWwiOiJ3YW5neXVfaXRAeWVhaC5uZXQiLCJ1c2VybmFtZSI6Ind5LWVpIiwidXNlcl9zbHVnIjoid3ktZWkiLCJhdmF0YXIiOiJodHRwczovL2Fzc2V0cy5sZWV0Y29kZS1jbi5jb20vYWxpeXVuLWxjLXVwbG9hZC91c2Vycy93eS1laS9hdmF0YXJfMTU0NjE0NDEyMy5wbmciLCJwaG9uZV92ZXJpZmllZCI6dHJ1ZSwidGltZXN0YW1wIjoiMjAyMC0wNS0xMSAwMzozNjoyMy4xNzM3NTgrMDA6MDAiLCJSRU1PVEVfQUREUiI6IjE3Mi4yMS40LjExMSIsIklERU5USVRZIjoiMjY3YmRlNWJhZGQ1ZjI0NGI4NWI4MzQ1MGFjY2ViYjUifQ.kTPa5bODi8I_pWCWIFtk4QulPD6zbDPsVn21myBNgY4; a2873925c34ecbd2_gr_session_id=6ea305d6-1536-450e-a8f5-b70fd63308bd; a2873925c34ecbd2_gr_last_sent_sid_with_cs1=6ea305d6-1536-450e-a8f5-b70fd63308bd; a2873925c34ecbd2_gr_session_id_6ea305d6-1536-450e-a8f5-b70fd63308bd=true; __asc=9dd0d2b7172082602af63dea44e; Hm_lvt_fa218a3ff7179639febdb15e372f411c=1589165920,1589274567,1589274710,1589274769; a2873925c34ecbd2_gr_cs1=wy-ei; Hm_lpvt_fa218a3ff7179639febdb15e372f411c=1589274884
    """
    
    headers = {
        "accept": "*/*",
        "accept-language": "zh-CN,zh-TW;q=0.9,zh;q=0.8,ko-KR;q=0.7,ko;q=0.6,ja-JP;q=0.5,ja;q=0.4",
        "content-type": "application/json",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "x-csrftoken": "FzLIzSZ2T5cuuLgjoEmruDcKLHU3cgl8CaXcLY0UKFTQ9s4DvplojXggpViTW5Po",
        "x-definition-name": "question",
        "x-operation-name": "questionData",
        'cookie': cookie.strip(),
        'origin': 'https://leetcode-cn.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
    }
    
    payload = {
        "operationName": "questionData",
        "variables": {"titleSlug": slug},
        "query": query.strip()
    }
    
    res = requests.post("https://leetcode-cn.com/graphql/", json=payload, headers=headers)
    content = res.json()
    return content["data"]["question"]

def write_to_file(question):
    url = "https://leetcode-cn.com/problems/{}/".format(question['titleSlug'])
    qid = question['questionFrontendId'][3:]
    markdowm_content = [
        '## {}. {}\n'.format(qid, question['translatedTitle']),
        '- 难度：' + question['difficulty'],
        '- 题目链接：[{}]({})'.format(url, url),
        '\n',
        '## 题目描述\n',
        '来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)\n',
        question['translatedContent'],
        '\n## 解法：'
    ]

    markdowm_content = '\n'.join(markdowm_content)

    filename = './{}-{}.md'.format(qid, question['titleSlug'])
    
    with open(filename, mode='w', encoding='utf-8') as fout:
            fout.write(markdowm_content)
    
def fetch_question_list():
    res = requests.get("https://leetcode-cn.com/api/problems/lcof/")
    content = res.json()
    # print(content['stat_status_pairs'][0])
    slug = [item['stat'] for item in content["stat_status_pairs"]]
    
    return slug

def build_template():
    question_list = fetch_question_list()
    for stat in slug_list:
        slug = stat["question__title_slug"]
        question = fetch_question_data(slug)
        write_to_file(question)

def build_lcof_readme():
    files = os.listdir(path='.')
    md = ''
    for file in files:
        if file.startswith('README'):
            continue
        with open(file, mode="r", encoding="utf-8") as fin:
            first_line = fin.readline()
            title = first_line.strip('# \n')
            file = urllib.parse.quote(file)
            md += '- [{}](./{})\n'.format(title, file)
    
    with open("README.md", mode="w", encoding="utf-8") as fout:
        fout.write(md)


if __name__ == "__main__":
    build_lcof_readme()