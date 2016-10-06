#!/usr/bin/env python
# encoding: utf-8


"""
@description: //TODO 

@version: 1.0
@author: BaoQiang
@license: Apache Licence 
@contact: mailbaoqiang@gmail.com
@site: http://www.github.com/githubao
@software: PyCharm
@file: spider_questions.py
@time: 2016/10/6 20:14
"""

from crawl.login_zhihu import log_in
import logging
from settings import *


def demo():
    client = log_in()
    if not client:
        logging.error('log in failed')
        return

    question = client.question(23220398)
    cnt = 0
    sum = question.answer_count
    for ans in question.answers:
        print(ans.author.name)
        ans.save(question.title)

        cnt += 1
        percent = cnt*100 /sum
        if isinstance(percent,int):
            print('processing {} percent, total is {} items'.format(percent,sum))


def main():
    demo()


if __name__ == '__main__':
    main()
