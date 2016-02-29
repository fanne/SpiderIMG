# /usr/bin/python
#coding:utf-8

__Date__ = "2016-02-29 11:33"
__Author__ = 'eyu Fanne'

from bs4 import BeautifulSoup
import configparser
import requests,re,time,os,urllib
import multiprocessing
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)

login_session = requests.session()
headers = {
            "Host":"www.zhihu.com",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
            "Accept":"*/*",
            "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
            "Accept-Encoding":"gzip, deflate",
            "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
            "X-Requested-With":"XMLHttpRequest",
            "Connection":"keep-alive"
            }

class LoginFun(object):
    #global login_session
    def __init__(self,configfile):
        config = configparser.ConfigParser()
        config.read(configfile)
        configname = 'zhihu'
        self.email = config.get(configname,'email')
        self.password = config.get(configname,'password')
        # self.headers = {
        #     "Host":"www.zhihu.com",
        #     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
        #     "Accept":"*/*",
        #     "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        #     "Accept-Encoding":"gzip, deflate",
        #     "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
        #     "X-Requested-With":"XMLHttpRequest",
        #     "Connection":"keep-alive"
        #     }
        self.login_url = r'https://www.zhihu.com/login/email'

    def startLogin(self):
        #global login_session
        login_text = requests.get(self.login_url,verify=False).text
        login_soup = BeautifulSoup(login_text,'lxml')
        login_xsrf = login_soup.find("input",{"name":"_xsrf"})['value']
        #print ('login_xsrf:%s' %login_xsrf)
        login_data = {
            "_xsrf":login_xsrf,
            "email":self.email,
            "password":self.password,
            "remember_me":"true"
        }
        #s_login = login_session.post(self.login_url,data=login_data,headers=self.headers,verify=False)
        s_login = login_session.post(self.login_url,data=login_data,headers=headers,verify=False)
        if s_login.status_code == 200 and s_login.json()["r"] != 1:
            print ("Login secesse!")
        else:
            print ("Login fail")
            exit(1)
        return login_session
