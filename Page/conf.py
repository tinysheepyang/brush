# -*- coding: utf-8 -*-
class base:
    EXCEL_DATA_PATH = 'G:/Git/TestAutomation/Data-Driven'
    TESTING_BROWSERS = 'xvfb'
    #DRIVER_OF_CHROME = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
    DRIVER_OF_CHROME = 'C:/Users/OPS/AppData/Local/Google/Chrome/Application/chromedriver.exe'
    #PHANTOMJS = 'E:/Program Files/phantomjs-2.1.1-windows/bin/phantomjs.exe'
    PHANTOMJS = 'D:\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe'
    PROXY = "http://dps.kuaidaili.com/api/getdps/?orderid=996639436139576&num=30&ut=1&format=json&sep=2"


class HomePage(base):
    BASE_URL = 'http://www.emao.com'

class Auto:
    class AutoHomePage(base):
        BASE_URL = 'http://auto.emao.com'
    class AutoList(base):
        BASE_URL = 'http://auto.emao.com/xuanche-0-0-0-0-0-0-0-0_0-0-1.html'
    class AutoPic(base):
        BASE_URL = 'http://auto.emao.com/pic/'
    class AutoKouBei(base):
        BASE_URL = 'http://auto.emao.com/185/koubei/'

class News:
    class NewsPage(base):
        BASE_URL = 'http://news.emao.com/'
    class NewsList(base):
        BASE_URL = 'http://news.emao.com/xinche/list.html#3'
    class NewsDetail(base):
        BASE_URL = 'http://news.emao.com/news/201603/19922.html?n_zx1'

class Wemedia(base):
    BASE_URL = 'http://news.emao.com/wemedia/list.html'

class Mall:
    class MallPage(base):
        BASE_URL = 'http://mall.emao.com/city/beijing/'
    class MallList(base):
        BASE_URL = 'http://mall.emao.com/city/beijing/car-0-0-0-0-1-0-0-1.html'
    class MallDetail(base):
        BASE_URL = 'http://mall.emao.com/car/2720.html'
    class MallActivity(base):
        BASE_URL = 'http://huodong.emao.com/mall/tob/tobzs.html'

class Dealer:
    class DealerPage(base):
        BASE_URL = 'http://dealer.emao.com/beijing/'
    class DealerCheshi(base):
        BASE_URL = 'http://dealer.emao.com/beijing/cheshi/'
    class DealerDetail(base):
        BASE_URL = 'http://dealer.emao.com/1307/'
    class DealerCity(base):
        BASE_URL = 'http://dealer.emao.com/beijing/list-0-0-0_1.html'

class EZhuShou:
    class EZhuShouPage(base):
        BASE_URL = 'http://e.emao.com/?c=user&m=login&from=user'

class Advertising:
    class Advertising(base):
        BASE_URL = 'http://zt.emao.com/201505/ggtest/'

class ZT(base):
    BASE_URL = 'http://zt.emao.com/201604/bjcz/detail?ver4_ad1'

class Brush(base):
    BASE_URL = 'http://www.baidu.com'


    
















