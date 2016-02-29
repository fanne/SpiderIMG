# /usr/bin/python
#coding:utf-8

__Date__ = "2016-02-29 16:46"
__Author__ = 'eyu Fanne'


from bs4 import BeautifulSoup
import configparser
import requests,re,time,os,urllib
import multiprocessing
from requests.packages.urllib3.exceptions import InsecureRequestWarning,InsecurePlatformWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
requests.packages.urllib3.disable_warnings(InsecurePlatformWarning)
import zhihuLogin


class ImgSpider(object):
    def __init__(self,configfile):
        config = configparser.ConfigParser()
        config.read(configfile)
        configname = 'zhihu'
        self.img_url = r'https://www.zhihu.com/question/39863528'
        self.img_dir = r'imgdir'

    def spiderNow(self):
        global answer_url_list
        answer_url_list = []
        answer_text = zhihuLogin.login_session.get(self.img_url,headers=zhihuLogin.headers,verify=False).text
        answer_soup = BeautifulSoup(answer_text,'lxml')
        answer_url = answer_soup.find_all("a",href=re.compile("answer"),class_="internal")
        for answer_i in answer_url:
            #print answer_i.get('href')
            answer_url_list.append(answer_i.get('href'))
        #print  answer_url_list
        return answer_url_list

    def getImg(self,img_url_i):
        img_text = zhihuLogin.login_session.get(img_url_i,headers=zhihuLogin.headers,verify=False).text
        img_soup = BeautifulSoup(img_text,'lxml')
        img_jpg = img_soup.find_all("img",class_="origin_image zh-lightbox-thumb lazy")
        for jpg_i in img_jpg:
            jpg_file = jpg_i.get('data-actualsrc')
            jpg_i = jpg_file.split('/')[-1]
            if not os.path.exists(self.img_dir):
                os.mkdir(self.img_dir)
            jpg_j = self.img_dir+'/'+jpg_i
            print (jpg_j)
            urllib.urlretrieve(jpg_file,jpg_j)

def main():
    spiderMain = zhihuLogin.LoginFun('config.ini')
    spiderMain.startLogin()
    imgMain = ImgSpider('config.ini')

    pool = multiprocessing.Pool(processes=8)
    for jpg in imgMain.spiderNow():
        #pool.apply_async(spiderMain.getImg,(jpg,))  不直接传入类实例的方法，用另一个函数包装一下，将类的实例作为参数传入即可
        spiderThread = imgMain.getImg(jpg)
        pool.apply_async(spiderThread,(jpg,))
    pool.close()
    pool.join()

if __name__=='__main__':
    main()