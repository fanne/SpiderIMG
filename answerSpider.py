# /usr/bin/python
#coding:utf-8

__Date__ = "2016-02-29 11:37"
__Author__ = 'eyu Fanne'

#from zhihuLogin import LoginFun
import zhihuLogin
from bs4 import BeautifulSoup
import configparser



class AnswerFun(object):
    def __init__(self,configfile):
        config = configparser.ConfigParser()
        config.read(configfile)
        configname = 'zhihu'
        self.answer_url = config.get(configname,'question_url')

    def getAnswer(self):
        #answer_text = LoginFun.startLogin().post(self.answer_url,headers=LoginFun.headers,verify=False).text
        answer_text = zhihuLogin.login_session.get(self.answer_url,headers=zhihuLogin.headers,verify=False).text
        answer_soup = BeautifulSoup(answer_text,'lxml')
        print answer_soup


if __name__=='__main__':
    start_login = zhihuLogin.LoginFun('config.ini')
    start_login.startLogin()
    star_answer = AnswerFun('config.ini')
    star_answer.getAnswer()

