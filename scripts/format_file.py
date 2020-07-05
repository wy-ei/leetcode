import os
import sys
import datetime
import re
import json


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

def insert_file_head(origin_file, new_file, origin_filename):
    content = ''
    with open(origin_file, mode="r", encoding="utf-8") as fin:
        first_line = fin.readline()
        if len(first_line) > 0 and first_line[0] == '#':
            content = fin.read();
            first_line = first_line.lstrip(' #')
            first_line = first_line.rstrip('\n ')
            ss = first_line.split('. ')
            if len(ss) != 2:
                print(new_file)
                return
            no, title = ss

            tags, title_zh = get_tags(origin_filename)
            if title_zh:
                title = title_zh

            head = [
                "---",
                "title: " + title,
                "qid: " + no
            ]

            if len(tags) > 0:
                tag_info = "tags: [" + (','.join(tags)) + ']'
                head.append(tag_info)

            
            head.append("---")

            content = "\n".join(head) + '\n\n' + content;

    if len(content) == 0:
        return
    with open(new_file, mode="w", encoding="utf-8") as fout:
        fout.write(content)

def rename(dir):
    files = os.listdir(dir)

    no_set = set()

    for file in files:
        if file.startswith('README') or not file.endswith('.md'):
            continue
        origin_file = dir + '/' + file

        spans = file.split("-")
        qid = spans.pop(0)
        filename = '-'.join(spans)

        st = os.stat(origin_file)
        date = datetime.datetime.fromtimestamp(st.st_mtime)
        filename = "{}-{:0>2}-{:0>2}-{}".format(2019, 10, 20, filename)
        new_file = "so" + '/' + filename

        insert_file_head(origin_file, new_file, file)

rename("solution")
