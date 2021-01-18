# encoding: utf-8

import requests
import json
import sys
import datetime

text_content = json.load(open('./content.json', encoding="utf-8"))
questions = json.load(open('./problems.json', encoding="utf-8"))


difficulty_map = ['', '简单', '中等', '困难']

obj = None

with open("all-tags.json", encoding="utf-8") as fin:
    obj = json.load(fin)


def get_tags(origin_filename):
    while origin_filename[0] == '0':
        origin_filename = origin_filename[1:]

    origin_filename = "./" + origin_filename
    tags = []
    title = ''
    if origin_filename in obj:
        title = obj[origin_filename]['translatedTitle']
        tags = obj[origin_filename]['topicTags']
        s = json.dumps(tags, ensure_ascii=False)
        tags = json.loads(s)
        tags = [item['translatedName'] for item in tags]
        tags = [t for t in tags if t is not None]
    return tags, title



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
        url = 'https://leetcode-cn.com/problems/' + title_slug
        title = question['stat']['question__title']
        difficulty = question['difficulty']['level']

        stat = question['stat']
        ac_rate = stat['total_acs'] / stat['total_submitted'] * 100

        text = ''

        if title_slug in text_content and text_content[title_slug]:
            text = text_content[title_slug]
        else:
            print('{} not exist'.format(title_slug))

        key = "{}-{}.md".format(question_id, title_slug)
        print(key)
        tags, title_zh = get_tags(key)
        if title_zh:
            title = title_zh


        markdowm_content = [
            '---',
            'title: ' + title,
            'qid: ' + str(question_id),
            'tag: [{}]'.format(', '.join(tags)),
            '---\n',
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

        date = datetime.datetime.now()

        # filename = './{:02}-{:02}-{:02}-{:03}-{}.md'.format(
        #     date.year, date.month, date.day, question_id, question['stat']['question__title_slug'])
        filename = './{:02}-{:02}-{:02}-{:03}-{}.md'.format(
            2019,10,20, question_id, question['stat']['question__title_slug'])
        with open(filename, mode='w', encoding='utf-8') as fout:
            fout.write(markdowm_content)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        qid = sys.argv[1]
        build_template(int(qid))
