# -*- coding: utf-8 -*-

from model.webelement import WebElement, WebBrowser
from selenium.webdriver.common.by import By


class HomePage(WebElement):
    (by, value) = (By.CSS_SELECTOR, '.newcar-box .tit a')



class Auto:
    class AutoHomePage(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.information-box h3')
    class AutoList(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.car-tit .active')
    class AutoPic(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.treeMainv1 h2')
    class AutoKouBei(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.car-con .clearfix span')

class News:
    class NewsPage(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.load-more')

    class Newslist(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.read-icon .read-num')
    class NewsDetail(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.d-com-intro span')

class Wemedia(WebElement):
    (by, value) = (By.CSS_SELECTOR, '.icon-pic')

class Mall:
    class MallPage(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.pay-icon dt')
    class MallList(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.sub-wish-box a')
    class MallDetail(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.buy-but')
    class MallActivity(WebElement):
        (by, value) = (By.ID, 'submit')

class Dealer:
    class DealerPage(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.recommend-tittle span')
    class DealerCheshi(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.market-left-btn a')
    class DealerDetail(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.kf-info .kf-tel')
    class DealerCity(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.map-btns')


class EZhuShou:
    class EZhuShouPage(WebElement):
        (by, value) = (By.ID, 'dealerLogin')


class Advertising:
    class Advertising(WebElement, WebBrowser):
        (by, value) = (By.XPATH, '/html/body/h2[2]')
    class AdvertisingClick(WebElement):
        (by, value) = (By.ID, 'emao-ad-13-9-21')

class ZT:
    class ZTPageV1(WebElement):
        (by, value) = (By.CSS_SELECTOR, '.jumpToComment')
    class ZTPageV2(WebElement):
        (by, value) = (By.CSS_SELECTOR, '#section-3 .l-905 .mark i')


class Brush():
    class Serch(WebElement):
        (by, value) = (By.ID, 'kw')
    class Button(WebElement):
        (by, value) = (By.ID, 'su')
    class Brush(WebElement, WebBrowser):
        (by, value) = (By.CSS_SELECTOR, '.result .f13 .c-showurl')
    class BrushLa(WebElement, WebElement):
        (by, value) = (By.CSS_SELECTOR, '.result .t')













