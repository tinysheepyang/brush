# -*- coding: utf-8 -*-
from Page.page import homePage
import random
from model import webelement, env
from model import common, log

def TestCase_1():
	env.KEYWORD = '汽车电商'
	env.TARGET = 'http://auto.sohu.com/20170310/n482959719.shtml'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_2():
	env.KEYWORD = '上海车展一猫汽车'
	env.TARGET = 'http://zt.emao.com/201703/elyqshczzx/detail'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_3():
	env.KEYWORD = '一猫汽车网购车活动'
	env.TARGET = 'http://bang.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_4():
	env.KEYWORD = '一猫12-18万汽车排行榜'
	env.TARGET = 'http://www.emao.com/top/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_5():
	env.KEYWORD = '一猫汽车上海车展2017'
	env.TARGET = 'http://news.emao.com/news/201704/24938.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_6():
	env.KEYWORD = '一猫汽车MPV销量排行榜'
	env.TARGET = 'http://www.emao.com/top/11.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_7():
	env.KEYWORD = '一猫终结4S店垄断售车'
	env.TARGET = 'http://news.cheshi.com/20170421/2166291.shtml'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_8():
	env.KEYWORD = '一猫汽车电商线下交车'
	env.TARGET = 'http://news.emao.com/news/201610/23366.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_9():
	env.KEYWORD = '一猫汽车网开店'
	env.TARGET = 'http://news.emao.com/news/201601/1023962.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_10():
	env.KEYWORD = '一猫网城市加盟'
	env.TARGET = 'http://news.emao.com/news/201612/24104.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_11():
	env.KEYWORD = '一猫汽车网5月购车季'
	env.TARGET = 'http://news.emao.com/news/201601/18539.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_12():
	env.KEYWORD = '一猫网好买车吗'
	env.TARGET = 'http://mall.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_13():
	env.KEYWORD = '一猫创始人'
	env.TARGET = 'http://news.emao.com/news/201511/15961.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_14():
	env.KEYWORD = '一猫新车电商平台'
	env.TARGET = 'http://news.emao.com/news/201704/24940.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_15():
	env.KEYWORD = '买车问问一猫'
	env.TARGET = 'http://news.emao.com/news/197001/1104940.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_16():
	env.KEYWORD = '一猫美系车车排行榜'
	env.TARGET = 'http://news.emao.com/news/201701/24351.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_17():
	env.KEYWORD = '一猫网 特价车'
	env.TARGET = 'http://mall.emao.com/city/shaoxing/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_18():
	env.KEYWORD = '一猫汽车2017战略发布会'
	env.TARGET = 'http://www.iyiou.com/p/37536'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_19():
	env.KEYWORD = '一猫汽车线下店商业模式'
	env.TARGET = 'http://news.emao.com/news/201512/16419.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_20():
	env.KEYWORD = '七台河特价车'
	env.TARGET = 'http://mall.emao.com/city/qitaihe/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_21():
	env.KEYWORD = '一猫汽车店'
	env.TARGET = 'http://city.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_22():
	env.KEYWORD = '一猫汽车买车帮'
	env.TARGET = 'http://news.emao.com/news/201704/24835.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_23():
	env.KEYWORD = '2017年汽车电商的突破口'
	env.TARGET = 'http://www.jianshu.com/p/11f375241a36'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_24():
	env.KEYWORD = '汽车电商价值的核心是'
	env.TARGET = 'http://news.emao.com/news/201604/21309.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_25():
	env.KEYWORD = '一猫汽车加盟开店'
	env.TARGET = 'http://news.emao.com/news/201704/24983.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_26():
	env.KEYWORD = '合肥特价车商城'
	env.TARGET = 'http://mall.emao.com/city/hefei/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_27():
	env.KEYWORD = '2017新车电商行业白皮书'
	env.TARGET = 'http://www.chextx.com/News/news/aid/13567.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_28():
	env.KEYWORD = '一猫汽车试驾视频'
	env.TARGET = 'http://v.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_29():
	env.KEYWORD = '一猫汽车电商网'
	env.TARGET = 'http://mall.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_30():
	env.KEYWORD = '一猫汽车购车季'
	env.TARGET = 'http://news.emao.com/news/201704/24835.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_31():
	env.KEYWORD = '一猫端午购车'
	env.TARGET = 'http://city.emao.com/hangqing/201705/50051.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_32():
	env.KEYWORD = '焦作一猫提车店'
	env.TARGET = 'http://dealer.emao.com/jiaozuo/list-0-0-0_1.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_33():
	env.KEYWORD = '买车帮 一猫买车'
	env.TARGET = 'http://www.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_34():
	env.KEYWORD = '一猫汽车'
	env.TARGET = 'http://app.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_35():
	env.KEYWORD = '汽车贷款一猫贷款'
	env.TARGET = 'http://city.emao.com/gouchejisuanqi/dai.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_36():
	env.KEYWORD = '一猫汽车电子商务'
	env.TARGET = 'http://news.emao.com/news/201610/23366.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_37():
	env.KEYWORD = '一猫买车能贷款吗'
	env.TARGET = 'http://news.emao.com/news/201702/24429.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_38():
	env.KEYWORD = '线下门店类型的新车电商'
	env.TARGET = 'http://news.emao.com/news/201512/16912.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_39():
	env.KEYWORD = '一猫汽车图片大全'
	env.TARGET = 'http://auto.emao.com/pic/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_40():
	env.KEYWORD = '买车问题一猫'
	env.TARGET = 'http://ask.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_41():
	env.KEYWORD = '一猫汽车城市店'
	env.TARGET = 'http://dealer.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_42():
	env.KEYWORD = '汽车内饰清洗一猫'
	env.TARGET = 'http://city.emao.com/hangqing/197001/44881.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_43():
	env.KEYWORD = '一猫汽车新车'
	env.TARGET = 'http://v.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_44():
	env.KEYWORD = '6月份在一猫买车'
	env.TARGET = 'http://mall.emao.com/'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_45():
	env.KEYWORD = '一猫汽车店买车'
	env.TARGET = 'http://mall.emao.com'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_46():
	env.KEYWORD = '新车电商'
	env.TARGET = 'http://auto.cnfol.com/cheshidongtai/20170412/24579453.shtml'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_47():
	env.KEYWORD = '一猫汽车网加盟连锁'
	env.TARGET = 'http://news.emao.com/news/201704/24983.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_48():
	env.KEYWORD = '一猫全场景汽车电商怎么玩'
	env.TARGET = 'http://www.cnautonews.com/qchl/ds/201601/t20160125_443454.htm'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

def TestCase_49():
	env.KEYWORD = '卢伟党一猫'
	env.TARGET = 'http://news.163.com/17/0510/10/CK2NVQF2000187VE.html'
	log.step_normal('>>>>>搜索关键词：[%s], >>>>>目标地址：[%s]' % (env.KEYWORD, env.TARGET))
	homePage.Brush.Serch.TypeIn(env.KEYWORD)
	homePage.Brush.Button.Click()
	webelement.WebElement.clicktarget(env.TARGET)

