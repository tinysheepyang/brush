# -*- coding: utf-8 -*-
from Page.page import homePage
import random
from model import webelement, env
from model import common, log



targetURL = [
    ['http://www.shrxnews.com/info/150202.html', '打通汽车电商任督二脉 一猫汽车网'],
    ['http://news.emao.com/news/201511/16445.html', '一猫汽车网汽车电商'],
    ['http://news.emao.com/news/201506/9824.html', '一猫汽车网选车买车'],
    ['http://mall.emao.com/city/beijing/', '一猫汽车网购车优惠'],
    ['http://news.emao.com/news/201501/4483.html', '一猫汽车网底价买车'],
    ['http://news.emao.com/news/201511/16445.html', '一猫汽车网 汽车电商'],
    ['http://news.emao.com/news/201506/9824.html', '一猫汽车网 选车买车'],
    ['http://mall.emao.com/city/beijing/', '一猫汽车网 购车优惠'],
    ['http://news.emao.com/news/201501/4483.html', '一猫汽车网 底价买车'],
    ['http://www.emao.com', '一猫汽车网'],
    ['http://auto.emao.com', '一猫汽车网'],
    ['http://news.emao.com', '一猫汽车网'],
    ['http://dealer.emao.com', '一猫汽车网'],
    ['http://mall.emao.com', '一猫汽车网'],
    ['http://city.emao.com', '一猫汽车网'],
    ['http://ask.emao.com', '一猫汽车网'],
]

def TestCase_1():
    env.KEYWORD = '一猫汽车网汽车电商,'
    env.TARGET = 'http://news.emao.com/news/201511/16445.html'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_2():
    env.KEYWORD = '打通汽车电商任督二脉 一猫汽车网,'
    env.TARGET = 'http://010xww.com/html/2016/10/28/53021.html'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_3():
    env.KEYWORD = '一猫汽车网选车买车,'
    env.TARGET = 'http://news.emao.com/news/201506/9824.html'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_4():
    env.KEYWORD = '一猫汽车网购车优惠,'
    env.TARGET = 'http://mall.emao.com/city/beijing/'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_5():
    env.KEYWORD = '一猫汽车网底价买车,'
    env.TARGET = 'http://news.emao.com/news/201501/4483.html'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_6():
    env.KEYWORD = '一猫汽车网 汽车电商,'
    env.TARGET = 'http://news.emao.com/news/201511/16445.html'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_7():
    env.KEYWORD = '一猫汽车网 选车买车,'
    env.TARGET = 'http://news.emao.com/news/201506/9824.html'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_8():
    env.KEYWORD = '一猫汽车网 购车优惠,'
    env.TARGET = 'http://mall.emao.com/city/beijing/'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_9():
    env.KEYWORD = '一猫汽车网 底价买车,'
    env.TARGET = 'http://news.emao.com/news/201501/4483.html'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_10():
    env.KEYWORD = '一猫汽车网,'
    env.TARGET = random.choice(env.NEWS)
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_11():
    env.KEYWORD = '一猫汽车网,'
    env.TARGET = random.choice(env.HOMEPAGE)
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_12():
    env.KEYWORD = '一猫汽车网,'
    env.TARGET = random.choice(env.AUTO)
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_13():
    env.KEYWORD = '一猫汽车网,'
    env.TARGET = random.choice(env.DEALER)
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_14():
    env.KEYWORD = '一猫汽车网,'
    env.TARGET = random.choice(env.MALL)
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_15():
    env.KEYWORD = '一猫汽车网,'
    env.TARGET = 'http://ask.emao.com'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_16():
    env.KEYWORD = '一猫汽车网,'
    env.TARGET = random.choice(env.CITY)
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_17():
    env.KEYWORD = '双十一活动 一猫汽车网,'
    env.TARGET = 'http://news.emao.com/news/201511/15283.html'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)

def TestCase_18():
    env.KEYWORD = '一猫汽车网 双11,'
    env.TARGET = 'http://city.emao.com/hangqing/201611/37479.html'
    log.step_normal(">>>>>搜索关键词：[%s], >>>>>目标地址：[%s]" % (env.KEYWORD, env.TARGET))
    homePage.Brush.Serch.TypeIn(env.KEYWORD)
    homePage.Brush.Button.Click()
    webelement.WebElement.clicktarget(env.TARGET)
