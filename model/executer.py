# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.common.exceptions import WebDriverException
import types, os, datetime, importlib, time, sys
from model import log, env, common
import random
from xvfbwrapper import Xvfb
import platform
import threading
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException
from httplib import BadStatusLine



def launch_browser(url, PROXY_HOST, PROXY_PORT):
    '''
    启动新的浏览器，并且给浏览器设置参数.
    '''
    if platform.uname()[0] =='Windows':
        user_agents = common.getUA()
        fp = FirefoxProfile()
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.http",PROXY_HOST)
        fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.https",PROXY_HOST)
        fp.set_preference("network.proxy.https_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.ssl",PROXY_HOST)
        fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.ftp",PROXY_HOST)
        fp.set_preference("network.proxy.ftp_port",int(PROXY_PORT))
        fp.set_preference("network.proxy.socks",PROXY_HOST)
        fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))
        fp.set_preference("general.useragent.override", user_agents)
        log.step_normal('browser user_agents is %s' % user_agents)
        fp.update_preferences()
        fp.native_events_enabled = False

        try:
            env.THREAD_LOCK.acquire()
            browser = webdriver.Firefox(firefox_profile=fp)
        except:
            log.step_fail('Firefox启动失败')
            return False
        finally:
            env.THREAD_LOCK.release()#unlock
    else:
        if env.threadlocal.TESTING_BROWSER.upper() == 'CHROME':
            if env.DRIVER_OF_CHROME == '':
                print ('DRIVER_OF_CHROME is empty.')
                return False
            PROXY = PROXY_HOST + ':' + PROXY_PORT  # IP:PORT or HOST:PORT
            user_agent = common.getUA()

            try:
                env.THREAD_LOCK.acquire()
                chrome_options = webdriver.ChromeOptions()
                chrome_options.add_argument('--proxy-server=http://%s' % PROXY)
                chrome_options.add_argument('--user-agent=%s' % user_agent)
                os.environ['webdriver.chrome.driver'] = env.DRIVER_OF_CHROME
                browser = webdriver.Chrome(executable_path=env.DRIVER_OF_CHROME,chrome_options=chrome_options)
            except WebDriverException as e:
                log.step_fail('chrome启动失败')
                return False
            finally:
                env.THREAD_LOCK.release()


        elif env.threadlocal.TESTING_BROWSER.upper() == 'IE':
            if env.DRIVER_OF_IE == '':
                print ('DRIVER_OF_IE is empty.')
                return False

            #qiangzhiguanbi IE
            os.popen('TASKKILL /F /IM IEDriverServer.exe')

            dc = DesiredCapabilities.INTERNETEXPLORER.copy()

            dc['nativeEvents'] = False
            dc['acceptSslCerts'] = True

            os.environ['webdriver.ie.driver'] = env.DRIVER_OF_IE

            browser = webdriver.Ie(executable_path=env.DRIVER_OF_IE,
                                       capabilities=dc)


        elif env.threadlocal.TESTING_BROWSER.upper() == 'PHANTOMJS':
            myProxy = PROXY_HOST + ":" + PROXY_PORT
            phantomjslog = os.path.join(env.RESULT_PATH, 'result', 'phantomjs.log')

            service_args = [
            '--ignore-ssl-errors=true',
            '--ssl-protocol=any',
            '--load-images=false',
            '--proxy=' + myProxy,
            '--proxy-type=http',
            ]
            user_agent = common.getUA()
            dcap = dict(DesiredCapabilities.PHANTOMJS)
            dcap["phantomjs.page.settings.userAgent"] = (user_agent)
            """
            dcap["phantomjs.page.settings.resourceTimeout"] = 5000
            dcap["phantomjs.page.settings.userAgent"] = (
                "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/53 "
                "(KHTML, like Gecko) Chrome/15.0.87"
            )
            """

            if platform.uname()[0] =='Windows':
                log.step_normal('OS是 [%s]' % platform.uname()[0])
                try:
                    env.THREAD_LOCK.acquire()
                    browser = webdriver.PhantomJS(env.PHANTOMJS, service_args=service_args, desired_capabilities=dcap, service_log_path =phantomjslog)
                    log.step_normal('phantomjs 启动成功！')
                except Exception , e:
                    log.step_fail('phantomjs启动失败')
                    return False
                finally:
                    env.THREAD_LOCK.release()


            elif platform.uname()[0] =='Linux':
                log.step_normal('OS是 [%s]' % platform.uname()[0])
                try:
                    env.THREAD_LOCK.acquire()
                    browser = webdriver.PhantomJS('/usr/bin/phantomjs', service_args=service_args, desired_capabilities=dcap, service_log_path =phantomjslog)
                    log.step_normal('phantomjs 启动成功！')
                except Exception , e:
                    log.step_fail('phantomjs启动失败')
                    return False
                finally:
                    env.THREAD_LOCK.release()
        elif env.threadlocal.TESTING_BROWSER.upper() == 'XVFB':
            user_agents = common.getUA()
            fp = FirefoxProfile()
            fp.set_preference("network.proxy.type", 1)
            fp.set_preference("network.proxy.http",PROXY_HOST)
            fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
            fp.set_preference("network.proxy.https",PROXY_HOST)
            fp.set_preference("network.proxy.https_port",int(PROXY_PORT))
            fp.set_preference("network.proxy.ssl",PROXY_HOST)
            fp.set_preference("network.proxy.ssl_port",int(PROXY_PORT))
            fp.set_preference("network.proxy.ftp",PROXY_HOST)
            fp.set_preference("network.proxy.ftp_port",int(PROXY_PORT))
            fp.set_preference("network.proxy.socks",PROXY_HOST)
            fp.set_preference("network.proxy.socks_port",int(PROXY_PORT))
            fp.set_preference("general.useragent.override", user_agents)
            log.step_normal('browser user_agents is %s' % user_agents)
            fp.update_preferences()
            fp.native_events_enabled = False
            # try:
            #     env.THREAD_LOCK.acquire()
            #     # size = common.setDisplay()
            #     # env.VDISPLAY = Xvfb(width=size[0], height=size[1])
            #     # env.VDISPLAY.start()
            #     browser = webdriver.Firefox(firefox_profile=fp)
            # except:
            #     log.step_fail('xvfb firefox 启动失败')
            #     return False
            # finally:
            #     env.THREAD_LOCK.release()#unlock

            if env.FIREFOX_BINARY == '':
                try:
                    env.THREAD_LOCK.acquire()
                    browser = webdriver.Firefox(firefox_profile=fp)

                except:
                    if isinstance(env.RESERVED_FIREFOX_BINARY, str) and env.RESERVED_FIREFOX_BINARY != "":
                        browser = webdriver.Firefox(firefox_profile=fp,
                                                    firefox_binary=FirefoxBinary(firefox_path=env.RESERVED_FIREFOX_BINARY))
                    else:
                        try:
                            log.step_warning("try to start firefox again!")
                            time.sleep(20)
                            browser = webdriver.Firefox(firefox_profile=fp)

                        except:
                            log.handle_error()
                            return False
                finally:
                    env.THREAD_LOCK.release()#unlock
            else:
                browser = webdriver.Firefox(firefox_profile=fp,
                                                firefox_binary=FirefoxBinary(firefox_path=env.FIREFOX_BINARY))

        elif env.threadlocal.TESTING_BROWSER.upper() == 'HtmlUnit':
            browser = webdriver.Remote("http://localhost:4444/wd/hub",desired_capabilities=DesiredCapabilities.HTMLUNIT)#DesiredCapabilities.HTMLUNIT可以是Firefox、chrome

    if not env.BROWSER_VERSION_INFO.has_key(env.threadlocal.TESTING_BROWSER):
        env.BROWSER_VERSION_INFO[env.threadlocal.TESTING_BROWSER] = browser.capabilities['version']


    #browser.set_window_size(1366, 758)
    browser.delete_all_cookies()
    size = common.getWindowSize()
    browser.set_window_size(size[0], size[1])
    browser.set_window_position(0, 0)
    browser.set_page_load_timeout(30) #url超时时间
    browser.implicitly_wait(0)

    try:
        browser.get(url)
        log.step_normal('打开url [%s]' % url)
    except (Exception,WebDriverException) as e:
        browser.quit()
        log.step_fail('打开url失败 [%s]' % e)


    return browser



def quit_browser(browser):
    try:
        log.step_normal('退出浏览器并删除cookies！')
        browser.delete_all_cookies()
        browser.close()
        browser.quit()
        # if platform.uname()[0] =='Linux' and env.threadlocal.TESTING_BROWSER.upper() == 'XVFB':
        #     env.VDISPLAY.stop()
        #     log.step_normal('vdisplay 已停止！')
        log.step_normal('执行全部完成！')
    except (Exception,WebDriverException) as e:
        log.step_warning('浏览器退出错误 [%s]' % e)




def __run_test_module(module):
    env.threadlocal.MODULE_NAME = module.__name__.split('.')[-1]
    testcases = []
    for fun in dir(module):
        if (not fun.startswith("__")) and (not fun.endswith("__")) and (isinstance(module.__dict__.get(fun), types.FunctionType)):
            if  module.__dict__.get(fun).__module__ == module.__name__:
                testcases.append(fun)

    for testcase in testcases:
        if testcase == 'before_each_testcase' or testcase == 'after_each_testcase' or testcase == 'before_launch_browser':
            return

        for browser in env.TESTING_BROWSERS.split('|'):
            env.threadlocal.TESTING_BROWSER = browser
            if not hasattr(env.threadlocal, "BROWSER"): env.threadlocal.BROWSER = None

            ###### Run Test Case ######
            try:
                log.start_test(testcase)

                if hasattr(module, 'before_launch_browser'):
                    getattr(module, 'before_launch_browser')()

                if (env.RESTART_BROWSER == True) or (env.threadlocal.BROWSER == None):
                    ip, port = common.praserIP(common.praserJsonFile())
                    env.threadlocal.BROWSER = launch_browser(env.BASE_URL, ip, port)


                if hasattr(module, 'before_each_testcase'):
                    getattr(module, 'before_each_testcase')()

                getattr(module, testcase)()

                if hasattr(module, 'after_each_testcase'):
                    getattr(module, 'after_each_testcase')()

            except:
                log.handle_error()
            finally:
                if env.threadlocal.CASE_PASS == False:
                    env.threadlocal.casepass = False
                else:
                    env.threadlocal.casepass = True

                if env.threadlocal.CASE_PASS == False and env.FAST_FAIL == True:
                    log.stop_test()
                    return "FAST_FAIL"
                else:
                    log.stop_test()

                if (env.RESTART_BROWSER == True):
                    quit_browser(env.threadlocal.BROWSER)
                    env.threadlocal.BROWSER = None


                if (env.RESTART_BROWSER == False) and (env.threadlocal.BROWSER != None) and (env.threadlocal.casepass == False):
                    quit_browser(env.threadlocal.BROWSER)
                    env.threadlocal.BROWSER = None


    if (env.threadlocal.BROWSER != None):
        quit_browser(env.threadlocal.BROWSER)
        env.threadlocal.BROWSER = None





def __run_test_case(case):
    try:
        module   = importlib.import_module(case.__module__) #动态导入case定义所在的模块
    except ImportError:
        log.step_fail("file data/%s.py is not existed. " %case.__module__)
        sys.exit(1)

    env.threadlocal.MODULE_NAME = case.__module__.split('.')[-1]

    for browser in env.TESTING_BROWSERS.split('|'):
        #env.threadlocal.TESTING_BROWSER = browser
        env.threadlocal.__setattr__('TESTING_BROWSER', browser)
        if not hasattr(env.threadlocal, "BROWSER"): env.threadlocal.BROWSER = None #判断env.threadlocal 是否含有BROWSER属性

        ###### Run Test Case ######
        try:
            log.start_test(case.__name__)

            if hasattr(module, 'before_launch_browser'):
                getattr(module, 'before_launch_browser')()

            if (env.RESTART_BROWSER == True) or (env.threadlocal.BROWSER == None):
                ip, port = common.praserIP(common.praserJsonFile())
                env.threadlocal.BROWSER = launch_browser(env.BASE_URL, ip, port)

                #env.threadlocal.BROWSER.maximize_window()


            if hasattr(module, 'before_each_testcase'):
                getattr(module, 'before_each_testcase')()

            case()

            if hasattr(module, 'after_each_testcase'):
                getattr(module, 'after_each_testcase')()

        except:
            log.handle_error()
        finally:
            if env.threadlocal.__getattribute__('CASE_PASS') == False:
                #env.threadlocal.CASE_PASS == False:
                env.threadlocal.casepass = False
            else:
                env.threadlocal.casepass = True

            if env.threadlocal.CASE_PASS == False and env.FAST_FAIL == True:
                log.stop_test()
                return "FAST_FAIL"
            else:
                log.stop_test()

            if (env.RESTART_BROWSER == True):
                quit_browser(env.threadlocal.BROWSER)
                env.threadlocal.BROWSER = None


            if (env.RESTART_BROWSER == False) and (env.threadlocal.BROWSER != None) and (env.threadlocal.casepass == False):
                quit_browser(env.threadlocal.BROWSER)
                env.threadlocal.BROWSER = None


    if (env.threadlocal.BROWSER != None):
        quit_browser(env.threadlocal.BROWSER)
        env.threadlocal.BROWSER = None



def decorator():
    def handle_func(func):
        def handle_args(*args):
            common.parse_conf_class(args[0]) #调用parse_conf_class函数设置env文件属性
            log.start_total_test()
            func(*args)#执行run函数

            log.finish_total_test()

            return env.EXIT_STATUS
        return handle_args
    return handle_func


@decorator()
def run(*args):
    if len(args) < 2:
        print ("Code error! 1st arg => conf; other args => test object(s).")

    for i in range(1, len(args)):
        testobj = args[i]
        threads = []


        if isinstance(testobj, list):

            for item in testobj:
                threads.append(threading.Thread(target=run_test_obj, args=([item])))#实例化一个Thread对象
        else:
            threads.append(threading.Thread(target=run_test_obj, args=([testobj])))
            #run_test_obj(testobj)
        #启动所有线程

        for thread in threads:
            thread.start()

        # 主线程中等待所有子线程退出
        for thread in threads:
            thread.join()



def run_test_obj(testobj):
    if isinstance(testobj, types.ModuleType):#判断testobj类型是否是模块
        __run_test_module(testobj)

    elif isinstance(testobj, types.FunctionType):#判断testobj类型是否是函数
        __run_test_case(testobj)

    elif isinstance(testobj, list):
        for obj in testobj:
            run_test_obj(obj)

    else:
        print ("emao- executer: function [run_test_obj] code error.")








