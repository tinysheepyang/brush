# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, UnexpectedAlertPresentException, WebDriverException, StaleElementReferenceException, TimeoutException
import time, sys, os, inspect, requests
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(inspect.stack()[-1][1])), 'model'))
import env, log
import urllib, random, platform
#from http.client import BadStatusLine
from httplib import BadStatusLine
from operator import isNumberType
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(inspect.stack()[-1][1])), 'Page'))
from model import common

class compatiblemethod(object):
    """如果第一个参数(cls)是一个类,设置/使用属性的类。
        如果第一个参数(cls)是一个实例,设置/使用实例的属性.
    
    这是一个延伸版本“@classmethod”,用于多线程问题框架的.
    
    EXAMPLE
    
        class A:
            a = 0
            
            @compatiblemethod
            def test(cls, aaa):
                cls.a = aaa
        
            @compatiblemethod
            def get(cls):
                print "get ", cls.a
    
    
    """
    def __init__(self, method):
        self._method = method
    
    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj) #获取返回对象的类型（返回值本身是一个type对象）
        
        ### this is the different part with "classmethod"
        if isinstance(obj, klass):
            klass = obj
            klass.__name__ = klass.__class__.__name__
    
        
        def newfunc(*args, **kws):
            return self._method(klass, *args, **kws)
        
        return newfunc




class WebBrowser:
    #下拉框滚动
    @compatiblemethod
    def ScrollTo(cls, x, y):
        log.step_normal("Element [%s]: Scroll To [%s, %s]" % (cls.__name__, x, y))
        env.threadlocal.BROWSER.execute_script("window.scrollTo(%s, %s);" % (x, y))

    @compatiblemethod
    def ScrollToPro(cls):
        log.step_normal('Began operating a drop-down box,Pull down 11 times each dropdown for 7 seconds at a time')

        if env.s.exists(env.BRAND.decode("utf-8")):
            env.s.incr(env.BRAND.decode("utf-8"), amount=1)
        else:
            env.s.set(env.BRAND.decode("utf-8"), 1,ex=7776000)

        cls.ScrollTo(0, 'document.body.scrollHeight/6')
        time.sleep(9)
        cls.ScrollTo(0, 'document.body.scrollHeight/5')
        time.sleep(8)
        cls.ScrollTo(0, 'document.body.scrollHeight/4')
        time.sleep(7)
        cls.ScrollTo(0, 'document.body.scrollHeight/3')
        time.sleep(6)
        cls.ScrollTo(0, 'document.body.scrollHeight/2')
        time.sleep(5)
        cls.ScrollTo(0, 'document.body.scrollHeight/1')
        time.sleep(9)
        cls.ScrollTo(0, 'document.body.scrollHeight/2')
        time.sleep(6)
        cls.ScrollTo(0, 'document.body.scrollHeight/3')
        time.sleep(7)
        cls.ScrollTo(0, 'document.body.scrollHeight/4')
        time.sleep(8)
        cls.ScrollTo(0, 'document.body.scrollHeight/5')
        time.sleep(9)
        cls.ScrollTo(0, 'document.body.scrollHeight/6')
        time.sleep(3)

        env.BROWSE = 1
        log.step_normal('drop-down box done')


    
    @compatiblemethod
    def Refresh(cls, times=4):#刷新
        log.step_normal("Element [%s]: Browser Refresh" % (cls.__name__,))
        
        for i in range(times):
            action = webdriver.ActionChains(env.threadlocal.BROWSER)
            action.key_down(Keys.CONTROL).send_keys(Keys.F5).key_up(Keys.CONTROL).perform()
            time.sleep(5)
        
    
    
    @compatiblemethod
    def DeleteAllCookies(cls):#删除cookies
        log.step_normal("Element [%s]: Browser Delete All Cookies" % (cls.__name__,))
        env.threadlocal.BROWSER.delete_all_cookies()
        
        time.sleep(2)

    @compatiblemethod
    def AddCookies(cls, name, value):
        log.step_normal("Element [%s]: Browser Add Cookies name[%s] value[%s]" % (cls.__name__, name, value))
        env.threadlocal.BROWSER.add_cookie({'name':name, 'value':value})
        time.sleep(2)
    

    @compatiblemethod
    def GetCookies(cls):
        log.step_normal("Element [%s]: Browser GetCookies name " % (cls.__name__))
        for cookie in env.threadlocal.BROWSER.get_cookies():
            log.step_normal("Element [%s]: Browser get Cookies name[%s] value[%s]" % (cls.__name__, cookie['name'], cookie['value']))


    @compatiblemethod
    def GetPageSource(cls):
        log.step_normal("Element [%s]: get pagesource [%s]" % (cls.__name__, env.threadlocal.BROWSER.page_source))
        return env.threadlocal.BROWSER.page_source
    
    @compatiblemethod
    def NavigateTo(cls, url):#前往页面
        log.step_normal("Element [%s]: Navigate To [%s]" % (cls.__name__, url))
        env.threadlocal.BROWSER.get(url)
        
        time.sleep(3)
    
    #跳过ie证书错误
    @compatiblemethod
    def IESkipCertError(cls):
        log.step_normal("IE Skip SSL Cert Error.")
        env.threadlocal.BROWSER.get("javascript:document.getElementById('overridelink').click();")
    
    
    @compatiblemethod
    def AlertAccept(cls):#操作Alert弹出框 确认
        log.step_normal("AlertAccept()")
        
        time.sleep(2)
        try:
            log.step_normal("switch_to_alert()")
            alert = env.threadlocal.BROWSER.switch_to_alert()
            alert.accept()
        except NoAlertPresentException:
            log.step_normal("Alert Not Found. ")
        
        try:
            log.step_normal("switch_to_default_content()")
            env.threadlocal.BROWSER.switch_to_default_content()
        except:
            pass
    
    
    @compatiblemethod
    def AlertDismiss(cls): #操作Alert弹出框 取消
        log.step_normal("AlertDismiss()")
        
        time.sleep(2)
        try:
            log.step_normal("switch_to_alert()")
            alert = env.threadlocal.BROWSER.switch_to_alert()
            alert.dismiss()
        except NoAlertPresentException:
            log.step_normal("Alert Not Found.")
        
        try:
            log.step_normal("switch_to_default_content()")
            env.threadlocal.BROWSER.switch_to_default_content()
        except:
            pass
    
    
    @compatiblemethod
    def AlertSendKeys(cls, value): #操作弹出框 输入文字
        log.step_normal("AlertSendKeys [%s]" % value)
        try:
            env.threadlocal.BROWSER.switch_to.alert.send_keys(value)
            env.threadlocal.BROWSER.switch_to.default_content()
        except:
            log.step_warning(str(sys.exc_info()))
    
    
    @compatiblemethod
    def AlertTextHave(cls, txt_value): #操作弹出框 获取提示文字
        log.step_normal("AlertTextHave [%s]" % txt_value)
        alert_text = env.threadlocal.BROWSER.switch_to_alert().text()
        
        if txt_value in alert_text:
            log.step_pass("pass")
        else:
            log.step_fail("fail")
        env.threadlocal.BROWSER.switch_to_default_content()
    
    
    @compatiblemethod
    def SwitchToNewPopWindow(cls): #切换页面焦点
        log.step_normal("切换新窗口！")
        
        t = 0
        while(t < 10):
            t = t + 1
            time.sleep(3)
            
            if len(env.threadlocal.BROWSER.window_handles) < 2:
                log.step_normal("Pop Window Not Found. Wait 3 Seconds then Try Again!")
            else:
                break
        
        env.threadlocal.BROWSER.switch_to.window(env.threadlocal.BROWSER.window_handles[-1])
        
        log.step_normal("Switch To The New Window of : %s" % str(env.threadlocal.BROWSER.title))

        cls.ScrollToPro()
        env.threadlocal.BROWSER.close()
        log.step_normal('当前窗口已关闭')
    
    #切换到默认
    @compatiblemethod
    def SwitchToDefaultWindow(cls):
        log.step_normal("切换到当前窗口")
        
        try:
            env.threadlocal.BROWSER.switch_to.window(env.threadlocal.BROWSER.window_handles[0])
        except:
            log.step_warning("env.threadlocal.BROWSER.switch_to.window(env.threadlocal.BROWSER.window_handles[0])")
            pass

        log.step_normal("Switch To The Default Window of: %s" % str(env.threadlocal.BROWSER.title))
    
    @compatiblemethod
    def SwitchToFrame(cls, frame): #切换frame
        log.step_normal("SwitchToFrame()")
        env.threadlocal.BROWSER.switch_to.frame(frame)
    
    
    @compatiblemethod
    def SwitchToDefaultContent(cls): #将识别的主体切换出frame
        log.step_normal("SwitchToDefaultContent()")
        
        try:
            env.threadlocal.BROWSER.switch_to.default_content()
        except:
            log.step_warning("env.threadlocal.BROWSER.switch_to.default_content()")
            pass

    @compatiblemethod
    def GetStatusCode(cls, url):
        log.step_normal("%s get url %s status_code" % (cls.__name__, url))

        if urllib.urlopen(url).code == '404':
            log.step_normal("url %s status_code is %s" % (url, urllib.urlopen(url).code))

            return '404'

        elif urllib.urlopen(url).code == '503':
            log.step_normal("url %s status_code is %s" % (url, urllib.urlopen(url).code))
            return '503'

        elif urllib.urlopen(url).code == '500':
            log.step_normal("url %s status_code is %s" % (url, urllib.urlopen(url).code))
            return '500'

        elif urllib.urlopen(url).code == '502':
            log.step_normal("url %s status_code is %s" % (url, urllib.urlopen(url).code))
            return '502'

        elif urllib.urlopen(url).code == '200':
            log.step_normal("url %s status_code is %s" % (url, urllib.urlopen(url).code))
            return '200 请检查日志或者查看截图'.decode('utf-8')

        else:
            log.step_normal("url %s status_code is %s" % (url, urllib.urlopen(url).code))
            return urllib.urlopen(url).code



class WebElement:
    (by, value) = (None, None)
    index       = 0
    flag        = False
    count       = 0
    cli        = False
    
    
    
    @compatiblemethod
    def __init__(cls, by=None, value=None):
        cls.by = by
        cls.value = value


    @compatiblemethod
    def Brush(cls, target):
        urls_res = cls.get_search_url()
        real_urls = urls_res[0]
        log.step_normal('搜索出来的可点击着陆页个数: [%s]' % len(real_urls))
        index = common.get_urlIndex(target, real_urls)
        log.step_normal('目标index: [%s]' % index)

        page = 1
        cls.index += 1
        while index == -1 and page <= 10:
            flg, plist = cls.layer()
            if flg and len(plist) != 0:
                try:
                    plist[-1].click()
                    log.step_normal('已点击下一页！')
                    time.sleep(2)
                except TimeoutException as e:
                    log.step_normal('点击下一页失败:[%s]' % e)
                    return cls.Brush(target)

            urls_res = cls.get_search_url()
            real_urls = urls_res[0]
            log.step_normal('搜索出来的可点击着陆页个数: [%s]' % len(real_urls))
            index = common.get_urlIndex(target, real_urls)
            log.step_normal('目标index: [%s]' % index)

            page = page + 1


        if index != -1 and page <= 10:
            log.step_normal('目标url在第[%s]页，第[%s]个' %(page, index))
            try:
                # urls_res = cls.get_search_url()
                urls_res[1][index].click()
                time.sleep(3)
                WebBrowser.SwitchToNewPopWindow()
                WebBrowser.SwitchToDefaultWindow()
                common.data(env.IP, env.KEYWORD, env.TARGET, 1, "success", page, index)
                log.step_normal('ip:[%s],keyword:[%s],target:[%s] 已插入数据库' % (env.IP,env.KEYWORD,env.TARGET))
                log.step_normal('准备跳出！')
                env.threadlocal.BROWSER.get(random.choice(env.JUMP_OUT))
                time.sleep(random.randint(3,8))
                log.step_normal('Brush Done!')
            except (TimeoutException, WebDriverException, NoSuchElementException, StaleElementReferenceException) as e:
                log.step_fail('点击url失败:[%s]' % e)

        if page > 10 and cls.index <= 3:
            log.step_normal('百度搜索结果前10页没有找到目标地址:[%s],放弃搜索' % target)
            cls.Brush('http://baike.emao.com')

    @compatiblemethod
    def layer(cls):
        #print page.homePage.Brush.Serch.by, page.homePage.Brush.Serch.value
        j = 0
        while j < 120:
            j += 1
            ele = env.threadlocal.BROWSER.find_elements_by_css_selector('#_mask')
            elementpages = env.threadlocal.BROWSER.find_elements_by_css_selector('#page a')

            if len(ele) == 0 and len(elementpages) !=0:
                return True, elementpages
            else:
                log.step_normal("元素 _mask elementpages : 等待消失... 发现 [%s] [%s] Element. Tried [%s] Times." % (len(ele), len(elementpages), j))
                time.sleep(1)

        if j == 120:
            log.step_fail('点击链接或者下一页失败，该proxy有问题')

        return False,None

    @compatiblemethod
    def clicktarget(cls, target):
        urls_res = cls.get_search_url()
        real_urls = urls_res[0]
        log.step_normal('搜索出来的可点击着陆页个数: [%s]' % len(real_urls))
        index = common.get_urlIndex(target, real_urls)
        log.step_normal('目标index: [%s]' % index)

        page = 1
        while index == -1 and page <= 25:
            if page == 1:
                items = common.get_random_index(index, len(real_urls))
                log.step_normal('目标url不在不在第一页生成随机数随机点击: [%s]' % items)
                cls.click_search_url(items)

            flg, plist = cls.layer()
            if flg and len(plist) != 0:
                try:
                    plist[-1].click()
                    log.step_normal('已点击下一页！')
                    time.sleep(2)
                except TimeoutException as e:
                    log.step_normal('点击下一页失败:[%s]' % e)
                    return cls.clicktarget(target)

            urls_res = cls.get_search_url()
            real_urls = urls_res[0]
            log.step_normal('搜索出来的可点击着陆页个数: [%s]' % len(real_urls))
            index = common.get_urlIndex(target, real_urls)
            log.step_normal('目标index: [%s]' % index)

            page = page + 1

        if index > 5 and page == 1:
            log.step_normal('目标url在第[%s]页，第[%s]个,随机点击一个或者两个' % (page,index))
            # 第一页，随机点击两个或一个
            int = random.randint(1, 2)
            if int == 2:
                items = common.get_random_index(index, len(real_urls))
            else:
                items = [1]
            log.step_normal('随机数为[%s]' % items)
            cls.click_search_url(items)
            try:
                urls_res[1][index].click()
                time.sleep(3)
                WebBrowser.SwitchToNewPopWindow()
                WebBrowser.SwitchToDefaultWindow()
                log.step_normal('准备跳出！')
                env.threadlocal.BROWSER.get(random.choice(env.JUMP_OUT))
                time.sleep(random.randint(3,8))
                log.step_normal('Brush Done!')
                common.data(env.IP, env.KEYWORD, env.TARGET, 1, "success", page, index)
                log.step_normal('ip:[%s],keyword:[%s],target:[%s] 已插入数据库' % (env.IP,env.KEYWORD,env.TARGET))
            except (TimeoutException, WebDriverException, NoSuchElementException, StaleElementReferenceException) as e:
                log.step_fail('点击url失败:[%s]' % e)

        elif page > 25:
            log.step_normal('百度搜索结果前25页没有找到目标地址:[%s],放弃搜索' % target)

        else:
            log.step_normal('目标url在第[%s]页，第[%s]个' %(page, index))
            try:
                # urls_res = cls.get_search_url()
                urls_res[1][index].click()
                time.sleep(3)
                WebBrowser.SwitchToNewPopWindow()
                WebBrowser.SwitchToDefaultWindow()
                log.step_normal('准备跳出！')
                env.threadlocal.BROWSER.get(random.choice(env.JUMP_OUT))
                time.sleep(random.randint(3,8))
                log.step_normal('Brush Done!')
                common.data(env.IP, env.KEYWORD, env.TARGET, 1, "success", page, index)
                log.step_normal('ip:[%s],keyword:[%s],target:[%s] 已插入数据库' % (env.IP,env.KEYWORD,env.TARGET))
            except (TimeoutException, WebDriverException, NoSuchElementException, StaleElementReferenceException) as e:
                log.step_fail('点击url失败:[%s]' % e)

    # 获取搜素出来的url
    @compatiblemethod
    def get_search_url(cls):
        flg, plist = cls.layer()
        if flg and len(plist) != 0:
            urls = []
            real = []
            real_url = []
            click_link = []
            content = env.threadlocal.BROWSER.find_element_by_css_selector("div[id=\"content_left\"]")
            links = content.find_elements_by_tag_name("a")
            for link in links:
                if link.get_attribute('class') == "c-showurl":
                    real.append(link.text)
                    url = link.get_attribute('href')
                    urls.append(url)

                    # function：解析加密url，剔除竞争对手的url
                    header = requests.head(url).headers

                    is_append = True
                    for out_url in env.out_urls:
                        if 'location' or 'Location' in header.keys():
                            if out_url in header['location']:
                                is_append = False
                                break
                        else:
                            continue
                    if is_append == True:
                        if 'location' or 'Location' in header.keys():
                            real_url.append(header['location'])
                            # a标签对象
                            click_link.append(link)
                        else:
                            pass
            log.step_normal('搜索页面url完成！')
            return [real_url, click_link]
        else:
            log.step_normal('获取页面元素失败')
            return cls.get_search_url()

    # 随机点击
    @compatiblemethod
    def click_search_url(cls, items):

        content = env.threadlocal.BROWSER.find_element_by_css_selector("div[id=\"content_left\"]")
        links = content.find_elements_by_tag_name("a")
        i = 0

        for link in links:
            if link.get_attribute('class') == "c-showurl":
                if i in items:
                    log.step_normal("随机点击item: [%s]" % i)
                    log.step_normal("随机点击url：[%s], 随机点击文本: [%s]" % (link.get_attribute('href'), link.text))

                    try:
                        link.click()
                        random.randint(3, 7)
                        WebBrowser.SwitchToNewPopWindow()
                        WebBrowser.SwitchToDefaultWindow()
                        log.step_normal('本次随机点击完毕！')
                    except (TimeoutException, WebDriverException) as e:
                        log.step_normal('随机点击失败---> %s' % e)
                        WebBrowser.SwitchToDefaultWindow()

                i = i + 1

    #操作浏览器下拉框直到元素出现
    @compatiblemethod
    def ScrollIntoView(cls):
        log.step_normal("Element [%s]: ScrollToView()" % cls.__name__)
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        i = 0
        while not elements[cls.index].is_displayed():
            WebBrowser.ScrollTo(0, i)
            i = i + 10
            
            if i == 1000:
                log.step_normal("still not displayed. break out.")
        
    #设置文本值
    @compatiblemethod
    def Set(cls, value):
        log.step_normal("Element [%s]: Set [%s]." % (cls.__name__, value))
        
        if isNumberType(value):
            value = str(value)
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        if elements[cls.index].tag_name == "select" or elements[cls.index].tag_name == "ul":
            cls.Select(value)
        
        else:
            elements[cls.index].clear()
            action = webdriver.ActionChains(env.threadlocal.BROWSER)
            action.send_keys_to_element(elements[cls.index], value) #键盘操作输入内容
            action.perform()
            
            cls.__clearup()
        
    
    @compatiblemethod
    # 点击页面链接
    def ClickTheLink(cls):
        log.step_normal("Element [%s]: " % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        is_selected = False
        
        if elements[cls.index].tag_name == "ul":

            lis = elements[cls.index].find_elements_by_tag_name('li')
            
            t = 0
            while (len(lis) == 0):
                lis = elements[cls.index].find_elements_by_tag_name('li')
                time.sleep(3)
                t = t + 1
                log.step_normal("Element [%s]: Wait 3 Seconds for [li]" % cls.__name__)
                
                if t == 20 and len(lis) == 0:
                    log.step_fail("Element [%s]: List Count = [%s]." % (cls.__name__, len(lis)))
                    return
                    
            log.step_normal("Element [%s]: List Count = [%s]." % (cls.__name__, len(lis)))

            for li in lis:
                if li.is_displayed():
                    time.sleep(3)
                    li.click()
                    is_selected = True


        elif elements[cls.index].tag_name == 'div':
                alis = elements[cls.index].find_elements_by_tag_name('a')
                imglis = elements[cls.index].find_elements_by_tag_name('img')

                t = 0
                while (len(alis) == 0 or len(imglis) == 0):
                    alis = elements[cls.index].find_elements_by_tag_name('a')
                    imglis = elements[cls.index].find_elements_by_tag_name('img')
                    time.sleep(3)
                    t = t + 1
                    log.step_normal("Element [%s]: Wait 3 Seconds for [a] [img]" % cls.__name__)
                    
                    if t == 20 and (len(alis) == 0 or len(imglis) == 0):
                        log.step_fail("Element [%s]: aList Count = [%s], imgList Count = [%s]." % (cls.__name__, len(alis), len(imglis)))
                        return
                        
                log.step_normal("Element [%s]: aList Count = [%s], imgList Count = [%s]." % (cls.__name__, len(alis), len(imglis)))

                alis.extend(imglis)

                for opt in alis:
                    if opt.is_displayed():
                        opt.click()
                        is_selected = True

        elif elements[cls.index].tag_name == 'a':
            is_selected = True
            elements[cls.index].click()
            
                        
        #### NOT Supported ################
        else:
            log.step_fail("Element [%s]: Tag [%s] NOT support [Select] method" % (cls.__name__, elements[cls.index].tag_name))
        
        
        if is_selected is False:
            log.step_fail("No item selected!")
        
        
        cls.__clearup()

    @compatiblemethod
    # 局部文本匹配
    def SelectByPartial(cls, value):
        log.step_normal("Element [%s]: Select [%s]." % (cls.__name__, value))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        is_selected = False
        
        #### select ################
        if elements[cls.index].tag_name == "select":
            options = elements[cls.index].find_elements_by_tag_name('option')

            if value is not None:

                t = 0
                while (len(options) == 0):
                    options = elements[cls.index].find_elements_by_tag_name('option')
                    time.sleep(3)
                    t = t + 1
                    log.step_normal("Element [%s]: Wait 3 Seconds for [option]" % cls.__name__)
                    
                    if t == 20 and len(options) == 0:
                        log.step_fail("Element [%s]: List Count = [%s]." % (cls.__name__, len(options)))
                        return

                log.step_normal("Element [%s]: List Count = [%s]." % (cls.__name__, len(options)))

                for option in options:
                    if value in option.text:
                        option.click()
                        is_selected = True
                        break
            else:
                log.step_fail("value = [%s], Value Error or value is None." % value)
        
        #### ul ################
        elif elements[cls.index].tag_name == "ul":
            lis = elements[cls.index].find_elements_by_tag_name('li')
            
            if value is not None:

                t = 0
                while (len(lis) == 0):
                    lis = elements[cls.index].find_elements_by_tag_name('li')
                    time.sleep(3)
                    t = t + 1
                    log.step_normal("Element [%s]: Wait 3 Seconds for [li]" % cls.__name__)
                    
                    if t == 20 and len(lis) == 0:
                        log.step_fail("Element [%s]: List Count = [%s]." % (cls.__name__, len(lis)))
                        return
                        
                log.step_normal("Element [%s]: List Count = [%s]." % (cls.__name__, len(lis)))

                for li in lis:
                    if value in  li.text:
                        li.click()
                        is_selected = True
                        break
            else:
                log.step_fail("value = [%s], Value Error or value is None." % value)
        
        #### NOT Supported ################
        else:
            log.step_fail("Element [%s]: Tag [%s] NOT support [Select] method" % (cls.__name__, elements[cls.index].tag_name))
        
        
        if is_selected is False:
            log.step_fail("No item selected!")
        
        
        cls.__clearup()
    
    @compatiblemethod
    # 全文本匹配
    def Select(cls, value):
        log.step_normal("Element [%s]: Select [%s]." % (cls.__name__, value))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        is_selected = False
        
        #### select ################
        
        if elements[cls.index].tag_name == "select":
            options = elements[cls.index].find_elements_by_tag_name('option')
            
            if value is not None:

                t = 0
                while (len(options) == 0):
                    options = elements[cls.index].find_elements_by_tag_name('option')
                    time.sleep(3)
                    t = t + 1
                    log.step_normal("Element [%s]: Wait 3 Seconds for [option]" % cls.__name__)
                    
                    if t == 20 and len(options) == 0:
                        log.step_fail("Element [%s]: List Count = [%s]." % (cls.__name__, len(options)))
                        return

                log.step_normal("Element [%s]: List Count = [%s]." % (cls.__name__, len(options)))

                for option in options:
    #                 log.step_normal("Element [%s]: option [%s]" % (cls.__name__, option.text))
                    
                    if option.text == value:
                        option.click()
                        is_selected = True
                        break
            else:
                log.step_fail("value = [%s], Value Error or value is None." % value)
        
        #### ul ################
        elif elements[cls.index].tag_name == "ul":
            lis = elements[cls.index].find_elements_by_tag_name('li')
            
            if value is not None:

                t = 0
                while (len(lis) == 0):
                    lis = elements[cls.index].find_elements_by_tag_name('li')
                    time.sleep(3)
                    t = t + 1
                    log.step_normal("Element [%s]: Wait 3 Seconds for [li]" % cls.__name__)
                    
                    if t == 20 and len(lis) == 0:
                        log.step_fail("Element [%s]: List Count = [%s]." % (cls.__name__, len(lis)))
                        return
                        
                log.step_normal("Element [%s]: List Count = [%s]." % (cls.__name__, len(lis)))

                for li in lis:
    #                 log.step_normal("Element [%s]: li [%s]" % (cls.__name__, li.text))
                    if li.text == value:
                        
                        li.click()
                        is_selected = True
                        break
            
            else:
                log.step_fail("value = [%s], Value Error or value is None." % value)
        #### NOT Supported ################
        else:
            log.step_fail("Element [%s]: Tag [%s] NOT support [Select] method" % (cls.__name__, elements[cls.index].tag_name))
        
        
        if is_selected is False:
            log.step_fail("No item selected!")
        
        
        cls.__clearup()
    
    
    @compatiblemethod
    #传数值
    def SelectByOrder(cls, order):
        log.step_normal("Element [%s]: Select by Order [%s]" % (cls.__name__, order))
        
        order = int(order)
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        #### ul ################
        if elements[cls.index].tag_name == "ul":
            lis = elements[cls.index].find_elements_by_tag_name('li')
            
            if order > 0:
                
                ### Wait and try more times if NO item found. ###
                t = 0
                while (len(lis) == 0):
                    lis = elements[cls.index].find_elements_by_tag_name('li')
                    time.sleep(3)
                    t = t + 1
                    log.step_normal("Element [%s]: Wait 3 Seconds for [li]" % cls.__name__)
                    
                    if t == 20 and len(lis) == 0:
                        log.step_fail("Element [%s]: List Count = [%s]." % (cls.__name__, len(lis)))
                        return
                
                
                log.step_normal("Element [%s]: List Count = [%s]." % (cls.__name__, len(lis)))
                
                if (order > len(lis)):
                    log.step_fail("Element [%s]: Not so many lists. [%s]" % (cls.__name__, len(lis)))
                else:
                    log.step_normal("Element [%s]: Do Click [%s]" % (cls.__name__, order))
                    action = webdriver.ActionChains(env.threadlocal.BROWSER)
                    
                    # Added to avoid error: "Element is no longer attached to the DOM"
                    elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
                    lis = elements[cls.index].find_elements_by_tag_name('li')
                    
                    action.click(lis[order-1])
                    action.perform()
                    
            else:
                log.step_fail("Order = [%s], Value Error." % order)
                
                
        #### select ################
        #### if elements[cls.index].tag_name == "select":
        else:
            options = elements[cls.index].find_elements_by_tag_name('option')
            
            if order > 0:
                
                ### Wait and try more times if NO item found. ###
                t = 0
                while (len(options) == 0):
                    options = elements[cls.index].find_elements_by_tag_name('option')
                    time.sleep(3)
                    t = t + 1
                    log.step_normal("Element [%s]: Wait 3 Seconds for [option]" % cls.__name__)
                    
                    if t == 20 and len(options) == 0:
                        log.step_fail("Element [%s]: options Count = [%s]." % (cls.__name__, len(options)))
                        return
                
                
                log.step_normal("Element [%s]: options Count = [%s]." % (cls.__name__, len(options)))
                
                if (order > len(options)):
                    log.step_fail("Element [%s]: Not so many options. [%s]" % (cls.__name__, len(options)))
                else:
                    log.step_normal("Element [%s]: Do Click [%s]" % (cls.__name__, order))
                    action = webdriver.ActionChains(env.threadlocal.BROWSER)
                    action.click(options[order-1])
                    action.perform()
            else:
                log.step_fail("Order = [%s], Value Error." % order)
        
        
        cls.__clearup()
    
    
    @compatiblemethod
    #鼠标定位到子元素
    def MouseOver(cls):
        log.step_normal("Element [%s]: MouseOver()" % (cls.__name__))
        
        time.sleep(1)
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.move_to_element(elements[cls.index])
        action.perform()
        
        cls.__clearup()
        
        time.sleep(1)
    
    
    @compatiblemethod
    def Click(cls):
        log.step_normal("Element [%s]: Click()" % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.click(elements[cls.index])
        action.perform()
        
        
        #=======================================================================
        # action = webdriver.ActionChains(env.threadlocal.BROWSER)
        # action.key_up(Keys.CONTROL, elements[cls.index])
        # action.perform()
        # 
        # action.click(elements[cls.index])
        # action.perform()
        #=======================================================================
        
        cls.__clearup()
    
    @compatiblemethod
    #鼠标双击
    def DoubleClick(cls):
        log.step_normal("Element [%s]: DoubleClick()" % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.double_click(elements[cls.index])
        action.perform()
        
        cls.__clearup()
    
    
    @compatiblemethod
    #鼠标悬停
    def ClickAndHold(cls):
        log.step_normal("Element [%s]: ClickAndHold()" % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.click_and_hold(elements[cls.index])
        action.perform()
        
        cls.__clearup()

    @compatiblemethod
    #鼠标移动到目标位置
    def DragAndDropByOffset(cls, xoffset, yoffset):
        '''
        Holds down the left mouse button on the source element,
        then moves to the target offset and releases the mouse button.
        '''
        log.step_normal("Element [%s]: drag_and_drop_by_offset()" % (cls.__name__))
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.drag_and_drop_by_offset(elements[cls.index],xoffset, yoffset)
        action.perform()

        cls.__clearup()
    
    @compatiblemethod
    #鼠标释放
    def ReleaseClick(cls):
        log.step_normal("Element [%s]: ReleaseClick()" % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.release(elements[cls.index])
        action.perform()
        
        cls.__clearup()
    
    
    @compatiblemethod
    #文本框输入内容
    def TypeIn(cls, value):

        '''Input value without clear existing values
        '''
        log.step_normal("Element [%s]: TypeIn [%s]." % (cls.__name__, value))
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        cls.WaitForEnabled()
        elements[cls.index].send_keys(value.decode('utf-8'))
        common.data(env.IP, env.KEYWORD, env.TARGET, 0, "search_Success", -1, -1)
        log.step_normal('搜索信息插入数据库成功！ip:[%s],关键字[%s],url[%s]' % (env.IP, env.KEYWORD, env.TARGET))

        env.BRAND = value
        env.BRAND = env.BRAND + '_' + 'brush' + '_' + common.stamp_date()
        if env.BRAND is None:
            pass
        else:
            if env.r.exists(env.BRAND.decode('utf-8')):
                env.r.incr(env.BRAND.decode('utf-8'), amount=1)
            else:
                env.r.set(env.BRAND.decode("utf-8"), 1, ex=7776000)
        #=======================================================================
        # action = webdriver.ActionChains(env.threadlocal.BROWSER)
        # action.send_keys_to_element(elements[cls.index], value)
        # action.perform()
        #=======================================================================
        
        cls.__clearup()
    
    
    @compatiblemethod
    #模拟鼠标enter
    def SendEnter(cls):
        log.step_normal("Element [%s]: SendEnter()" % (cls.__name__, ))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        action = webdriver.ActionChains(env.threadlocal.BROWSER)
        action.send_keys_to_element(elements[cls.index], Keys.ENTER)
        action.perform()
        
        cls.__clearup()
    
    
    @compatiblemethod
    #得到对象数，有等待
    def GetObjectsCount(cls):
        log.step_normal("Element [%s]: GetObjectsCount." % (cls.__name__))
        
        cls.__wait_for_appearing()
        
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: GetObjectsCount = [%s]" % (cls.__name__, len(elements)))
        
        cls.__clearup()
        return len(elements)
    
    
    @compatiblemethod
    #实时得到对象数，没有等待
    def GetRealTimeObjCount(cls): #### get real time obj counts, without waiting.
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: GetRealTimeObjCount = [%s]" % (cls.__name__, len(elements)))
        
        cls.__clearup()
        return len(elements)
    
    @compatiblemethod
    def GetElementObj(cls): #### get real time obj counts, without waiting.
        log.step_normal("Element [%s]: GetElementObj." % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        cls.__clearup()
        return elements[cls.index]
    
    
    @compatiblemethod
    def GetInnerHTML(cls):
        log.step_normal("Element [%s]: GetInnerHTML()" % (cls.__name__, ))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        log.step_normal("Element [%s]: InnerHTML = [%s]" % (cls.__name__, elements[cls.index].get_attribute('innerHTML')))
        
        cls.__clearup()
        return elements[cls.index].get_attribute('innerHTML')
    
    
    #获取属性值
    @compatiblemethod
    def GetAttribute(cls, attr):
        log.step_normal("Element [%s]: GetAttribute [%s]." % (cls.__name__, attr))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        attr_value = elements[cls.index].get_attribute(attr)
        log.step_normal("Element [%s]: Attribute Value = [%s]." % (cls.__name__, attr_value))
        
        cls.__clearup()
        return attr_value

    @compatiblemethod
    # 获取父元素
    def GetParentElement(cls):
        log.step_normal("Element [%s]: GetParentElement()" % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        return elements[cls.index].parent()


    @compatiblemethod
    def GetText(cls):
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: Gets the text of the element, the content is %s." % (cls.__name__, elements[cls.index].text))
        return elements[cls.index].text
    
    
    @compatiblemethod
    # 获取子元素的xpath
    def FetchSubElementOfXPath(cls, layer):
        return WebElement(cls.by, "/".join(cls.value.split("/")[:layer+2]))
    
    
    @compatiblemethod
    def Wait(cls, seconds):
        log.step_normal("Element [%s]: Wait for [%s] seconds." % (cls.__name__, seconds))
        
        time.sleep(seconds)
    
    
    @compatiblemethod
    # 等待页面attribute加载
    def WaitForAttribute(cls, name, value, method="equal"):

        log.step_normal("Element [%s]: WaitForAttribute [%s] <%s> [%s]." % (cls.__name__, name, method, value))
        
        i = 0
        while True:
            cls.__wait()
            elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
            
            realvalue = elements[cls.index].get_attribute(name)
            
            if method.lower() == 'equal':
                if value.lower() == realvalue.lower():
                    log.step_normal("Yes! real value=[%s]" % realvalue)
                    break
                else:
                    log.step_normal("No! real value=[%s]" % realvalue)
            
            elif method.lower() == 'contain':
                if value.lower() in realvalue.lower():
                    log.step_normal("Yes! real value=[%s]" % realvalue[:150])
                    break
                else:
                    log.step_normal("No! real value=[%s]" % realvalue[:150])
            
            elif method.lower() == 'not contain':
                if value.lower() in realvalue.lower():
                    log.step_normal("Yes! real value=[%s]" % realvalue[:150])
                else:
                    log.step_normal("No! real value=[%s]" % realvalue[:150])
                    break
            
            elif method.lower() == 'in':
                if realvalue.lower() in value.lower():
                    log.step_normal("Yes! real value=[%s]" % realvalue[:150])
                    break
                else:
                    log.step_normal("No! real value=[%s]" % realvalue[:150])
            
            elif method.lower() == 'not equal':
                if value.lower() == realvalue.lower():
                    log.step_normal("No! real value=[%s]" % realvalue)
                else:
                    log.step_normal("Yes! real value=[%s]" % realvalue)
                    break
            
            else:
                log.step_fail("code error.")
            
            
            i = i + 1
            if i > 90:
                log.step_fail("Not Found Expected Value! real value=[%s]" % realvalue)
                break
            
            time.sleep(1)
        
        
        cls.__clearup()
    
    @compatiblemethod
    # __wait_for_appearing() 二次封装等待元素加载出现
    def WaitForAppearing(cls):
        log.step_normal("Element [%s]: WaitForAppearing..." % (cls.__name__))
        
        cls.__wait_for_appearing()
        cls.__clearup()
    
    
    @compatiblemethod
    def WaitForDisappearing(cls):
        log.step_normal("Element [%s]: WaitForDisappearing..." % (cls.__name__))
        
        cls.__wait_for_disappearing()
        cls.__clearup()
    
    
    @compatiblemethod
    # 等待元素加载是否可见
    def WaitForVisible(cls):
        log.step_normal("Element [%s]: WaitForVisible..." % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        t = 0
        while(t < 90):
            if elements[cls.index].is_displayed():
                log.step_normal("Element [%s]: IS visible now." % (cls.__name__))
                break
            else:
                log.step_normal("Element [%s]: Still NOT visible, wait 1 second." % (cls.__name__))
                time.sleep(1)
        
        cls.__clearup()
    
    
    @compatiblemethod
    # 等待元素出现编辑
    def WaitForEnabled(cls):
        log.step_normal("Element [%s]: WaitForEnabled..." % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        t = 0
        while(t < 90):
            if elements[cls.index].is_enabled():
                log.step_normal("Element [%s]: is enabled now." % (cls.__name__))
                break
            else:
                log.step_normal("Element [%s]: still NOT enabled, wait 1 second." % (cls.__name__))
                time.sleep(1)
            
            t = t + 1
        
        cls.__clearup()
    
    
    @compatiblemethod
    def IsEnabled(cls):
        log.step_normal("Element [%s]: Is Enabled?" % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        if elements[cls.index].is_enabled():
            log.step_normal("Yes!")
            cls.__clearup()
            return True
        else:
            log.step_normal("No!")
            cls.__clearup()
            return False
    
    
    @compatiblemethod
    def IsExist(cls):
        log.step_normal("Element [%s]: IsExist?" % (cls.__name__))
        
        time.sleep(2)
        
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: IsExist? Count = [%s]" % (cls.__name__, len(elements)))
        
        cls.__clearup()
        
        if len(elements) > 0:
            return True
        else:
            return False
    
    
    @compatiblemethod
    def IsVisible(cls):
        log.step_normal("Element [%s]: IsVisible?" % (cls.__name__))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        if elements[cls.index].is_displayed():
            cls.__clearup()
            return True
        else:
            cls.__clearup()
            return False
        
    
    @compatiblemethod
    #验证检查点是否存在
    def IsAttribute(cls, name, value, method="contain"):
        log.step_normal("Element [%s]: IsAttribute [%s] <%s> [%s]." % (cls.__name__, name, method, value))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        realvalue = elements[cls.index].get_attribute(name)
        
        if method.lower() == 'equal':
            if value == realvalue:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False
        
        elif method.lower() == 'not equal':
            if not value == realvalue:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False
        
        elif method.lower() == 'contain':
            if value in realvalue:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False
        
        elif method.lower() == 'not contain':
            if not value in realvalue:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False
        
        elif method.lower() == 'in':
            if realvalue in value:
                cls.__clearup()
                return True
            else:
                cls.__clearup()
                return False
        
        
        else:
            log.step_fail("code error.")
        
        cls.__clearup()
    
    
    
    @compatiblemethod
    #验证元素是否存在
    def VerifyExistence(cls, trueORfalse):
        log.step_normal("Element [%s]: Verify Existence = [%s]." % (cls.__name__, trueORfalse))
        
        if trueORfalse == True:
            cls.__wait_for_appearing() #等待元素加载出现
        else:
            cls.__wait_for_disappearing()
        
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: Count = [%s]" % (cls.__name__, len(elements)))
        
        
        cls.__clearup()
        if len(elements) > 0:
            if trueORfalse == True:
                log.step_pass("Exist!")
            else:
                log.step_fail("Exist!")
        else:
            if trueORfalse == False:
                log.step_pass("Not Exist!")
            else:
                log.step_fail("Not Exist!")
    
    
    @compatiblemethod
    #验证元素是否可见
    def VerifyVisible(cls, trueORfalse):
        log.step_normal("Element [%s]: Verify Visible = [%s]." % (cls.__name__, trueORfalse))
        
        cls.__wait()
        
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        log.step_normal("Element [%s]: Count = [%s]" % (cls.__name__, len(elements)))
        
        if elements[cls.index].is_displayed():
            if trueORfalse == True:
                return True
                log.step_pass("Visible!")
            else:
                log.step_fail("Visible!")
        else:
            if trueORfalse == False:
                log.step_pass("Not Visible!")
            else:
                log.step_fail("Not Visible!")

            return False
        
        cls.__clearup()
    
    
    @compatiblemethod
    # 验证元素是否可见 or 验证是否可编辑
    def VerifyEnabled(cls, trueOrfalse):
        log.step_normal("Element [%s]: Verify Enabled = [%s]" % (cls.__name__, trueOrfalse))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        is_disabled = elements[cls.index].get_attribute("disabled")
        log.step_normal("Element [%s]: attribute 'is_disabled' = [%s]" % (cls.__name__, is_disabled))
        
        if is_disabled == "true":
            if trueOrfalse == False:
                log.step_pass("Pass...")
            else:
                log.step_fail("Fail...")
        
        elif elements[cls.index].is_enabled():
            if trueOrfalse == True:
                log.step_pass("Pass")
            else:
                log.step_fail("Fail")
        
        else:
            log.step_fail("Not verified.")
        
        
        cls.__clearup()
    
    
    @compatiblemethod
    # 验证点检查
    def VerifyInnerHTMLContains(cls, contain_content):
        log.step_normal("Element [%s]: VerifyInnerHTMLContains [%s]." % (cls.__name__, str(contain_content)))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        inner_html = elements[cls.index].get_attribute('innerHTML')
        
        if isinstance(contain_content, list):
            for content in contain_content:
                if content in inner_html:
                    log.step_pass("Real inner_hmtl=[%s]" % inner_html)
                else:
                    log.step_fail("Real inner_hmtl=[%s]" % inner_html)
                
        else:
            if contain_content in inner_html:
                log.step_pass("Real inner_hmtl=[%s]" % inner_html)
            else:
                log.step_fail("Real inner_hmtl=[%s]" % inner_html)
        
        cls.__clearup()
    
    @compatiblemethod
    #验证检查点
    def VerifyText(cls, value, method='equal'):
   
        log.step_normal("Element [%s]: VerifyText <%s> [%s]." % (cls.__name__, method, value))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        realvalue = elements[cls.index].text
        
        if method.lower() == 'equal':
            if value == realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s], value=[%s]" % (realvalue, value))
        
        elif method.lower() == 'not equal':
            if not value == realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)
        
        elif method.lower() == 'contain':
            if value in realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)
        
        elif method.lower() == 'not contain':
            if not value in realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)
        
        elif method.lower() == 'in':
            if realvalue in value:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)
        
        else:
            log.step_fail("code error.")
        
        cls.__clearup()



    @compatiblemethod
    #验证检查点
    def VerifyAttribute(cls, name, value, method='equal'):
   
        log.step_normal("Element [%s]: VerifyAttribute [%s] <%s> [%s]." % (cls.__name__, name, method, value))
        
        cls.__wait()
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)

        realvalue = elements[cls.index].get_attribute(name)
        
        if method.lower() == 'equal':
            if value == realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)
        
        elif method.lower() == 'not equal':
            if not value == realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)
        
        elif method.lower() == 'contain':
            if value in realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)
        
        elif method.lower() == 'not contain':
            if not value in realvalue:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)
        
        elif method.lower() == 'in':
            if realvalue in value:
                log.step_pass("real value=[%s]" % realvalue)
            else:
                log.step_fail("real value=[%s]" % realvalue)
        
        else:
            log.step_fail("code error.")
        
        cls.__clearup()
    
    
    @compatiblemethod
    #等待元素可编辑
    def __wait_for_enabled(cls):
        elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
        
        if elements[cls.index].is_enabled():
            return
        else:
            t = 0
            while t < 90:
                if elements[cls.index].is_enabled():
                    break
                
                log.step_normal("Element [%s]: __wait_for_enabled for 1 second, By [%s :: %s :: %s]" % (cls.__name__, cls.by, cls.value, cls.index))
                time.sleep(0.5)
    
    
    @compatiblemethod
    def __wait(cls):
        t = 0
        while t < 120:
            t = t + 1
            
            try:
                elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
            except NoSuchElementException:
                log.step_normal("Element [%s]: NoSuchElementException." % cls.__name__)
                elements = []
            except BadStatusLine:
                log.step_warning("Element [%s]: BadStatusLine." % cls.__name__)
            except UnexpectedAlertPresentException:
                log.step_warning("Element [%s]: UnexpectedAlertPresentException." % cls.__name__)

            if len(elements) == 0:
                time.sleep(0.5)
                log.step_normal("Element [%s]: Wait 0.5 second, By [%s :: %s :: %s]" % (cls.__name__, cls.by, cls.value, cls.index))

            else:
                if len(elements) > 1:
                    log.step_normal("Element [%s]: There are [%s] Elements!" % (cls.__name__, len(elements)))
                
                break
        
        #判断元素索引是否越界
        if len(elements) < cls.index + 1:
            if platform.uname()[0] =='Windows':
                log.step_fail("Element [%s]: Element Index Issue! There are [%s] Elements! Index=[%s]" % (cls.__name__, len(elements), cls.index))


            elif platform.uname()[0] =='Linux':
                log.step_fail("Element [%s]: Element Index Issue! There are [%s] Elements! Index=[%s]" % (cls.__name__, len(elements), cls.index))

            else:
                print '不知道什么系统'

        
        
    
    
    @compatiblemethod
    #等待页面元素消失
    def __wait_for_disappearing(cls):
        
        t = 0
        while t < 120:
            t = t + 1
            
            try:
                elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
            except NoSuchElementException:
                log.step_normal("Element [%s]: NoSuchElementException." % cls.__name__)
                elements = []
            except BadStatusLine:
                log.step_warning("Element [%s]: BadStatusLine." % cls.__name__)
                continue
            except UnexpectedAlertPresentException:
                log.step_warning("Element [%s]: UnexpectedAlertPresentException." % cls.__name__)
            
            if len(elements) == 0:
                return True
            else:
                time.sleep(0.5)
                log.step_normal("Element [%s]: WairForDisappearing... Found [%s] Element. Tried [%s] Times." % (cls.__name__, len(elements), t))
        
        
        return False
    
    
    @compatiblemethod
    #等待第一个元素加载出现，等待时间最大为两分钟
    def __wait_for_appearing(cls):
        
        t = 0
        while t < 120:
            t = t + 1
            
            try:
                elements = env.threadlocal.BROWSER.find_elements(cls.by, cls.value)
            except NoSuchElementException:
                log.step_normal("Element [%s]: NoSuchElementException." % cls.__name__)
                elements = []
            except BadStatusLine:#代理异常
                log.step_warning("Element [%s]: BadStatusLine." % cls.__name__)
                continue
            except UnexpectedAlertPresentException:
                log.step_warning("Element [%s]: UnexpectedAlertPresentException." % cls.__name__)
            
            
            if len(elements) == 0:
                time.sleep(0.5)
                log.step_normal("Element [%s]: WaitForAppearing... Wait 1 second, By [%s]" % (cls.__name__, cls.value))
                WebBrowser.Refresh(1)

            else:
                log.step_normal("Element [%s]: Found [%s] Element. Tried [%s] Times." % (cls.__name__, len(elements), t))
                break
        

    
    @compatiblemethod
    def __clearup(cls):
        if cls.index != 0:
            log.step_normal("Element [%s]: The Operation Element Index = [%s]." % (cls.__name__, cls.index))
        
        
        cls.index = 0





