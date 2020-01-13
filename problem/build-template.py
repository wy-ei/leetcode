import requests
import json
import sys

text_content = json.load(open('./content.json', encoding="utf-8"))
questions = json.load(open('./problems.json', encoding="utf-8"))

difficulty_map = ['', '简单','中等','困难']

def build_question_id_to_question_map():
    mp = {}
    for question in questions['stat_status_pairs']:
        question_id = question['stat']['question_id']
        mp[question_id] = question
    return mp

def build_template(start, end=None):
    if end is None:
        end = start + 1
        
    mp = build_question_id_to_question_map()
    for question_id in range(start, end):
        question = mp[question_id]
        title_slug = question['stat']['question__title_slug']
        url = 'https://leetcode.com/problems/' + title_slug
        title = question['stat']['question__title']
        difficulty = question['difficulty']['level']

        stat = question['stat']
        ac_rate = stat['total_acs'] / stat['total_submitted'] * 100

        text = ''

        if title_slug in text_content and text_content[title_slug]:
            text = text_content[title_slug]
        else:
            print('{} not exist'.format(title_slug))

        markdowm_content = [
            '## {}. {}\n'.format(question_id, title),
            '- 难度： ' + difficulty_map[difficulty],
            '- 通过率： {:.1f}%'.format(ac_rate),
            '- 题目链接：[{}]({})'.format(url, url),
            '\n',
            '## 题目描述\n',
            '来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)\n',
            text,
            '\n## 解法：'
        ]

        markdowm_content = '\n'.join(markdowm_content)

        filename = './{:03}-{}.md'.format(question_id, question['stat']['question__title_slug'])
        with open(filename, mode='w', encoding='utf-8') as fout:
            fout.write(markdowm_content)
      
    
if __name__ == '__main__':
    if len(sys.argv) > 1:
        qid = sys.argv[1]
        build_template(int(qid))