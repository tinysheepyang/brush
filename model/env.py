# -*- coding: utf-8 -*-
import threading, redis, MySQLdb
from xvfbwrapper import Xvfb

# driver of web browser, such as: webdriver.Firefox()
BROWSER             = None




# path where to save the result log.
RESULT_PATH         = ""
EXCEL_DATA_PATH     = ""
TXT_DATA_PATH       = ""
CSV_DATA_PATH       = ""
XML_DATA_PATH       = ""
SQLITE_DATA_PATH    = ""
MODEL_PATH          = ""



# mysql
conn = MySQLdb.connect(host='db.lan', user='root', passwd='123456', port=3306, charset='utf8')

# test case/module variables.
#===============================================================================
CASE_START_TIME     = "N/A"
CASE_STOP_TIME      = "N/A"
CASE_NAME           = "N/A"
CASE_PASS           = "N/A"
CASE_WARNINGS       = 0
# 
MODULE_NAME         = ""
#===============================================================================


# 启动/停止 测试时间
TOTAL_START_TIME    = '2012-11-14 14:32:30'
TOTAL_STOP_TIME     = '2012-11-14 14:32:30'

TOTAL_TESTCASE_PASS = 0
TOTAL_TESTCASE_FAIL = 0


# 测试页面URl.
BASE_URL            = ""


# TESTING_BROWSER 测试浏览器
TESTING_BROWSER     = ""
TESTING_BROWSERS    = ""


# Data of test result, for generate report in excel.
EXCEL_REPORT_DATA   = []

HTMLREPORT_TESTCASES = []
HTMLREPORT_SCREENSHOT_NAME = ""


FIREFOX_BINARY          = ""
RESERVED_FIREFOX_BINARY = ""

DRIVER_OF_CHROME     = ""
DRIVER_OF_IE         = ""
PHANTOMJS            =""


FAST_FAIL            = False
EXIT_STATUS          = 0


BROWSER_VERSION_INFO = {}


THREAD_LOCK          = threading.Lock()

RESTART_BROWSER      = True


SUPPORT_ANGULARJS    = True

BRAND = ""
CLICKBRAND = 0
BROWSE     = 0

# multi-threading
threadlocal = threading.local()

COOKIE = "PHPSESSID=5f7mbqghvk1kt5n9illa0nr175; kmsign=56023b6880039; KMUID=ezsEg1YCOzxg97EwAwUXAg=="

PROXY =""


JUMP_OUT = ['http://city.emao.com/beijing/','http://city.emao.com/shanghai/','http://city.emao.com/guangzhou/','http://city.emao.com/chengdu/'
'http://city.emao.com/chongqing/','http://city.emao.com/wuhan/','http://city.emao.com/changsha/','http://city.emao.com/changchun/','http://city.emao.com/changzhou/',
'http://city.emao.com/xian/','http://city.emao.com/shijiazhuang/','http://city.emao.com/hefei/','http://city.emao.com/nanchang/','http://city.emao.com/suzhou/',
'http://city.emao.com/guiyang/','http://city.emao.com/hangzhou/','http://city.emao.com/luoyang/','http://city.emao.com/lanzhou/','http://city.emao.com/yinchuan/',
'http://city.emao.com/huhehaote/','http://dealer.emao.com/shenzhen/','http://city.emao.com/zhengzhou/','http://city.emao.com/xining/','http://city.emao.com/foshan/',
'http://city.emao.com/xiamen/']

pooL = redis.ConnectionPool(host='redis.lan', port=6379, db=0)
p = redis.Redis(connection_pool=pooL)

pool = redis.ConnectionPool(host='redis.lan', port=6379, db=1)
r = redis.Redis(connection_pool=pool)

Pool = redis.ConnectionPool(host='redis.lan', port=6379, db=2)
s = redis.Redis(connection_pool=Pool)


out_urls = ['http://www.12gang.com/article_8585.html']

IP = ''
KEYWORD = ''
TARGET = ''


HOMEPAGE = ['http://www.emao.com','http://www.emao.com/about/index.html', 'http://www.emao.com/zt/201503/yearaward/27/', 'http://www.emao.com/zt/201511/autoguangzhou/','http://www.emao.com/about/lianxi.html','http://www.emao.com/zt/201507/cards/45']
NEWS = ['http://mews.emao.com','http://news.emao.com/news/201411/638.html', 'http://news.emao.com/news/201411/637.html', 'http://news.emao.com/shuoba/', 'http://news.emao.com/news/201503/6637_all.html', 'http://news.emao.com/news/201603/19953.html']
AUTO = ['http://auto.emao.com','http://auto.emao.com/pic/', 'http://auto.emao.com/pic/brand-100-0-0-1.html', 'http://auto.emao.com/1620/', 'http://auto.emao.com/pinpai/','http://auto.emao.com/xuanche-2-0-0-0-0-0-0-0_0-0-1.html']
MALL = ['http://mall.emao.com','http://mall.emao.com/city/beijing/','http://mall.emao.com/city/beijing/car-0-0-0-0-0-0-0-1.html','http://mall.emao.com/city/wuhan/car-0-0-0-0-0-0-0-1.html','http://mall.emao.com/city/guangzhou/','http://mall.emao.com/city/xian/']
CITY = ['http://city.emao.com','http://city.emao.com/changchun/','http://city.emao.com/hangqing/201608/32690.html','http://city.emao.com/hangqing/201611/37875.html','http://city.emao.com/beijing/hangqing/list-0-103_1.html']
DEALER = ['http://dealer.emao.com/wuhan/list-0-0-0_1.html','http://dealer.emao.com/','http://dealer.emao.com/news/201601/22944.html','http://dealer.emao.com/23583/']

VDISPLAY = None