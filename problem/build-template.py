import requests
import json

text_content = json.load(open('./content.json', encoding="utf-8"))
problems = json.load(open('./problems.json', encoding="utf-8"))

difficulty_map = ['', '简单','中等','困难']

for problem in problems['stat_status_pairs'][-300:]:
    title_slug = problem['stat']['question__title_slug']
    url = 'https://leetcode.com/problems/' + title_slug
    title = problem['stat']['question__title']
    problem_id = problem['stat']['question_id']
    difficulty = problem['difficulty']['level']
    
    stat = problem['stat']
    ac_rate = stat['total_acs'] / stat['total_submitted'] * 100

    text = ''
    
    if title_slug in text_content and text_content[title_slug]:
        text = text_content[title_slug]
    else:
        print('{} not exist'.format(title_slug))
    
    markdowm_content = [
        '## {}. {}\n'.format(problem_id, title),
        '- 难度： ' + difficulty_map[difficulty],
        '- 通过率： {:.1f}%'.format(ac_rate),
        '- 题目链接：[{}]({})'.format(url, url),
        '\n',
        '### 题目描述\n',
        '来源于 [https://leetcode-cn.com/](https://leetcode-cn.com/)\n',
        text,
        '\n### 解法：'
    ]
    
    markdowm_content = '\n'.join(markdowm_content)
    
    filename = './{:03}-{}.md'.format(problem_id, problem['stat']['question__title_slug'])
    with open(filename, mode='w', encoding='utf-8') as fout:
        fout.write(markdowm_content)