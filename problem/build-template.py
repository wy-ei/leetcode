import requests

content = requests.get('https://leetcode.com/api/problems/all/')

problems = content.json()

difficulty_map = ['', '简单','中等','困难']

for problem in problems['stat_status_pairs'][-200:]:
    url = 'https://leetcode.com/problems/' + problem['stat']['question__title_slug']
    title = problem['stat']['question__title']
    problem_id = problem['stat']['question_id']
    difficulty = problem['difficulty']['level']
    
    stat = problem['stat']
    ac_rate = stat['total_acs'] / stat['total_submitted'] * 100

    markdowm_content = [
        '## ' + title + '\n',
        '难度： ' + difficulty_map[difficulty],
        '通过率： {:.1f}%'.format(ac_rate),
        '题目链接：[{}]({})'.format(url, url),
        '\n\n',
        '### 解法：'
    ]
    
    markdowm_content = '\n'.join(markdowm_content)
    
    filename = './{:03}-{}.md'.format(problem_id, problem['stat']['question__title_slug'])
    with open(filename, mode='w', encoding='utf-8') as fout:
        fout.write(markdowm_content)