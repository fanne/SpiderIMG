# /usr/bin/python
#coding:utf-8

__Date__ = "2016-02-24 10:05"
__Author__ = 'eyu Fanne'

##爬取知乎https://www.zhihu.com/question/39863528下包含链接的所有图片
##multiprocessing在python2.X中需要实例后再使用



from bs4 import BeautifulSoup
import configparser
import requests,re,time,os,urllib
import multiprocessing
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
import zhihuLogin

# class SpiderWork:
#     def __init__(self,configfile):
#         config = configparser.ConfigParser()
#         config.read(configfile)
#         configname = 'zhihu'
#         self.email = config.get(configname,'email')
#         self.password = config.get(configname,'password')
#         self.headers = {
#             "Host":"www.zhihu.com",
#             "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36",
#             "Accept":"*/*",
#             "Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
#             "Accept-Encoding":"gzip, deflate",
#             "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
#             "X-Requested-With":"XMLHttpRequest",
#             "Connection":"keep-alive"
#             }
#         self.login_url = r'https://www.zhihu.com/login/email'
#         self.img_url = r'https://www.zhihu.com/question/39863528'
#         self.img_dir = r'imgdir'
#
#     def startLogin(self):
#         global login_session
#         login_session = requests.session()
#         login_text = requests.get(self.login_url,verify=False).text
#         login_soup = BeautifulSoup(login_text,'lxml')
#         login_xsrf = login_soup.find("input",{"name":"_xsrf"})['value']
#         print ('login_xsrf:%s' %login_xsrf)
#         login_data = {
#             "_xsrf":login_xsrf,
#             "email":self.email,
#             "password":self.password,
#             "remember_me":"true"
#         }
#         s_login = login_session.post(self.login_url,data=login_data,headers=self.headers,verify=False)
#         if s_login.status_code == 200 and s_login.json()["r"] != 1:
#             print ("Login secesse!")
#         else:
#             print ("Login fail")
#             exit(1)
#
#
    # def spiderNow(self):
    #     global answer_url_list
    #     answer_url_list = []
    #     answer_text = login_session.get(self.img_url,headers=self.headers,verify=False).text
    #     answer_soup = BeautifulSoup(answer_text,'lxml')
    #     answer_url = answer_soup.find_all("a",href=re.compile("answer"),class_="internal")
    #     for answer_i in answer_url:
    #         #print answer_i.get('href')
    #         answer_url_list.append(answer_i.get('href'))
    #     #print  answer_url_list
    #     return answer_url_list
    #
    # def getImg(self,img_url_i):
    #     img_text = login_session.get(img_url_i,headers=self.headers,verify=False).text
    #     img_soup = BeautifulSoup(img_text,'lxml')
    #     img_jpg = img_soup.find_all("img",class_="origin_image zh-lightbox-thumb lazy")
    #     for jpg_i in img_jpg:
    #         jpg_file = jpg_i.get('data-actualsrc')
    #         jpg_i = jpg_file.split('/')[-1]
    #         if not os.path.exists(self.img_dir):
    #             os.mkdir(self.img_dir)
    #         jpg_j = self.img_dir+'/'+jpg_i
    #         print (jpg_j)
    #         urllib.urlretrieve(jpg_file,jpg_j)
#
#
#
# def main():
#     spiderMain = SpiderWork('config.ini')
#     spiderMain.startLogin()
#
#     pool = multiprocessing.Pool(processes=8)
#     for jpg in spiderMain.spiderNow():
#         #pool.apply_async(spiderMain.getImg,(jpg,))  不直接传入类实例的方法，用另一个函数包装一下，将类的实例作为参数传入即可
#         spiderThread = spiderMain.getImg(jpg)
#         pool.apply_async(spiderThread,(jpg,))
#     pool.close()
#     pool.join()
#
#
#
#
# if __name__=='__main__':
#     begintime = time.time()
#     main()
#     endtime = time.time()
#     usetime =  endtime - begintime
#     print ("执行脚本总用时 %s 秒" % usetime)
#
#     # for jpg in answer_url_list:
#     #     loginNow.getImg(jpg)
#     #loginNow.getImg('https://www.zhihu.com/question/27936753/answer/81327730')








