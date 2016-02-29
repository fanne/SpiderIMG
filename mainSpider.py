# /usr/bin/python
#coding:utf-8

__Date__ = "2016-02-29 14:13"
__Author__ = 'eyu Fanne'

from zhihuLogin import LoginFun
from answerSpider import AnswerFun


def main():
    start_login = LoginFun('config.ini')
    start_login.startLogin()
    star_answer = AnswerFun('config.ini')
    star_answer.getAnswer()




if __name__=='__main__':
    main()
