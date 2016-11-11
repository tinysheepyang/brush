# -*- coding: utf-8 -*-

import datetime, os, sys, inspect, stat, shutil
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(inspect.stack()[-1][1])), 'model'))
import log, env
import json, urllib2, random, time
from fake_useragent import UserAgent
import random, platform, codecs
from urllib2 import HTTPError, URLError

def stamp_date():
    return datetime.datetime.now().strftime("%Y-%m-%d")

def stamp_datetime():
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def stamp_datetime_coherent():
    return datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")


"""
返回一个列表记录堆栈帧和当前帧之间的帧异常目前在处理。列表中的第一项表示调用者;最后一个条目表示异常出现的地方。
"""
def exception_error():
    error_message = ""
    for i in range(len(inspect.trace())):
        error_line = """
File:      %s - [%s]
Function:  %s
Statement: %s
-------------------------------------------------------------------------------------------""" % (
        inspect.trace()[i][1], 
        inspect.trace()[i][2], 
        inspect.trace()[i][3], 
        inspect.trace()[i][4])
        
        error_message = "%s%s" % (error_message, error_line)
    
    
    error_message = """Error!
%s
%s
======================================== Error Message ====================================%s

======================================== Error Message ======================================================""" % (sys.exc_info()[0], sys.exc_info()[1], error_message)
    
    return error_message

def getUA():
    ua = UserAgent()
    return ua.random

def get_user_agent():
    if platform.uname()[0] =='Windows':
        ua = UserAgent()
        return ua.random
    else:
        with codecs.open('/home/rd/fake_useragent.json', encoding='utf-8', mode='rb',) as fp:
            s = json.load(fp)

        attr = s['randomize'][str(random.randint(0, len(s['randomize']) - 1))]
        return s['browsers'][attr][random.randint(0, len(s['browsers'][attr]) - 1)]



def praserJsonFile():
    n = 0
    while n < 60:
        n = n + 1
        if len(env.p.lrange('proxy_list', 0, -1)) == 0:
            time.sleep(1)
            log.step_normal("proxy : Wait 1 second")
        else:
            return env.p.lrange('proxy_list', 0, -1)
            break

    if n >= 60:
        try:
            data = urllib2.urlopen(env.PROXY).read()
        except Exception,e:
            log.step_warning('urllib2.urlopen error %s' % e)
            data = urllib2.urlopen(env.PROXY).read()

        s = json.loads(data)

        try:
            if len(s['msg']) == 0:
                return Check(s['data']['proxy_list'])
            else:
                return None
        except Exception,e:
            print e


def praserIP(proxy_list):
    proxy_ip = random.choice(proxy_list)
    ip, port = proxy_ip.split(':')
    log.step_normal('proxy ip [%s] port[%s]' % (ip, port))
    return ip, port


def Check(ip_list):
    proxy_ip_list = []
    for ip in ip_list:
        try:
            proxy_support = urllib2.ProxyHandler({'http': 'http://'+ ip})
            opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
            urllib2.install_opener(opener)
            request = urllib2.Request('http://www.baidu.com')
            request.add_header("cookie",env.COOKIE)
            request.add_header("User-Agent", getUA())
            content = urllib2.urlopen(request,timeout=4).read()

            if len(content) >= 1000:
                env.THREAD_LOCK.acquire()
                proxy_ip_list.append(ip)
                log.step_normal('add proxy [%s]' % ip)
                env.THREAD_LOCK.release()
            else:
                log.step_fail( '出现验证码或IP被封杀 [%s]' % ip)
        except (URLError, HTTPError) as e:
            log.step_fail('代理ip无效 [%s]' % ip)

    return proxy_ip_list

def get_local_ip(ip):
    try:
        proxy_support = urllib2.ProxyHandler({'http': 'http://' + ip})
        opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
        urllib2.install_opener(opener)
        request = urllib2.Request('http://ip.chinaz.com/getip.aspx')
        # request.add_header("cookie", env.COOKIE)
        request.add_header("User-Agent", getUA())
        fp = urllib2.urlopen(request)
        mybytes = fp.read()
        # note that Python3 does not read the html code as string
        # but as html code bytearray, convert to string with
        mystr = mybytes.decode('utf-8')
        fp.close()
        ip = mystr.find("ip")
        add = mystr.find("address")
        ip = mystr[ip + 4:add - 2]
        address = mystr[add + 9:-2]
        return [ip, address]

    except (HTTPError, URLError) as e:
        log.step_warning ('获取ip地址失败---> %s' % e)
        return [ip, 'address']

    # 获取随机点击的搜索页random.randint(0


def get_random_index(index, len):
    if index >= 8:
        random_index = [
            random.randint(0, 4), random.randint(5, 8)
        ]
    elif index >= 4:
        random_index = [
            random.randint(0, 3), random.randint(3, index)
        ]
    elif index >= 0:
        random_index = [
            index
        ]
    elif index == -1:
        if len <= 5:
            random_index = [
                random.randint(0, 5)
            ]
        else:
            random_index = [
                # random.randint(0,4),random.randint(5,len)
                random.randint(5, len)
            ]
    return random_index


# function 目标地址是否在某个list中
def get_urlIndex(tagurl, urls):
    i = 0
    has = -1
    for url in urls:
        if tagurl in url:
            has = True
            log.step_normal('url在搜索结果第[%s]个' % i)
            return i
        i = i + 1
    log.step_normal('url不在当前页')
    return has

#插入数据库
def insert_db(ipdate):
    try:
        # 获取一个数据库连接，注意如果是UTF-8类型的，需要制定数据库
        conn = env.conn
        cur = conn.cursor()  # 获取一个游标对象

        cur.execute("USE brush")

        # 插入数据
        ISOTIMEFORMAT = '%Y-%m-%d %X'
        ipdate.append(time.strftime(ISOTIMEFORMAT, time.localtime()))
        cur.execute(
            "INSERT INTO ip_log(ip,address,keyword,url,click,error,page,rank,created_at) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)",
            ipdate)
        cur.close()  # 关闭游标
        conn.commit()  # 向数据库中提交任何未解决的事务，对不支持事务的数据库不进行任何操作
        conn.close()  # 关闭到数据库的连接，释放数据库资源
        log.step_normal('数据沉淀完成！')
    except Exception as e:
        log.step_warning('数据库操作异常:[%s]' % e)


def data(ip, keyword, target, flag, result, page, index):
    data = get_local_ip(ip)
    data.append(keyword)
    data.append(target)
    data.append(flag)
    data.append(result)
    data.append(page)
    data.append(index)
    insert_db(data)

#设置屏幕分辨率
def setDisplay():
    display_size = [
        [1920, 1080],
        [1680, 1050],
        [1600, 900],
        [1440, 900],
        [1400, 1050]
    ]
    d_size = random.choice(display_size)
    return d_size

# 屏幕浏览器窗口大小
def getWindowSize():
    wind_size = [
        [1920, 1080],
        [1600, 900],
        [1280, 720],
        [1366, 758],
        [1440, 900],
        [1400, 1050]
    ]
    headers = random.choice(wind_size)
    return headers

#给文件加一个后缀
def add_unique_postfix(fn):
    '''
    __author__ = 'Denis Barmenkov <denis.barmenkov@gmail.com>'
    __source__ = 'http://code.activestate.com/recipes/577200-make-unique-file-name/'
    
    '''
    fn = unicode(fn)
    
    if not os.path.exists(fn):
        return fn

    path, name = os.path.split(fn)
    name, ext = os.path.splitext(name)

    make_fn = lambda i: os.path.join(path, '%s__%d%s' % (name, i, ext))#定义匿名函数

    for i in xrange(2, sys.maxint):#xrang 每次返回一个值 sys.maxint 最大的Int值
        uni_fn = make_fn(i)
        if not os.path.exists(uni_fn):
            return uni_fn

    return None

# 如果是路径就删除 删除不了就加后缀
def force_delete_file(file_path):
    if os.path.isfile(file_path):#判断路径是否为文件
        try:
            os.remove(file_path)#删除文件
            return file_path
        except:
            '''
            print "delete fail. Kill Processes."
            os.popen("TASKKILL /F /IM excel.exe")
            time.sleep(2)
            '''
            return add_unique_postfix(file_path)
    else:
        return file_path


# 判断目录路径是否存在
def mkdirs(dir_path):
    try:
        if not os.path.exists(dir_path):#判断是否存在这个路径
            os.makedirs(dir_path)
    except:
        log.step_warning(str(sys.exc_info()))


def remove_readonly(fn, path, excinfo):
    if os.path.exists(path):
        try:
            if fn is os.rmdir:
                os.chmod(path, stat.S_IWRITE)
                os.rmdir(path)#删除目录
            elif fn is os.remove:
                os.chmod(path, stat.S_IWRITE)
                os.remove(path)#删除文件
        except:
            log.step_warning(str(sys.exc_info()))

#删除目录
def delete_folder(folder_path):
    try:
        shutil.rmtree(folder_path)#递归删除
    except:
        log.step_warning(str(sys.exc_info()))


def delete_file_or_folder(file_full_path):
    if os.path.exists(file_full_path):
        if os.path.isdir(file_full_path):
            delete_folder(file_full_path)
        else:
            os.remove(file_full_path)

#复制
def copy(src, dst):
    try:
        if os.path.isdir(src):
            shutil.copytree(src, dst)#拷贝目录
        else:
            shutil.copy(src, dst)#拷贝文件
    except:
        log.step_warning(str(sys.exc_info()))

#如果存在就删除，并且新建
def delete_then_mkdir(dir_path):
    if os.path.exists(dir_path):
        delete_folder(dir_path)
    os.makedirs(dir_path)

#从配置文件中取值
def get_value_from_conf(conf_file, key):
    
    if not os.path.exists(conf_file):
        return ""
    
    if not os.path.isfile(conf_file):
        return ""
    
    try:
        with open(conf_file, 'r') as f:
            while True:
                data = f.readline()
                
                if not data:
                    break
                
                if len(data.split('=')) < 2:
                    continue
                
                if data.strip()[0] == "#":
                    continue
                
                if data.split('=')[0].strip() == key:
                    return str(data.split('=', 1)[1].strip())#以'='分割成1+1个字符串，取第一个字符串并忽略空格
    except IOError:
        return ""

# 设置配置文件属性值
def parse_conf_class(conf_class):
    '''
    解析配置文件的所有属性，然后设置env模块的所有属性
    '''
    if sys.getdefaultencoding() != 'utf-8':
        reload(sys)
        sys.setdefaultencoding('utf-8')

    new_conf = []
    for var in dir(conf_class):
        if (not var.startswith("__")) and (not var.endswith("__")):
            new_conf.append(var)
    
    def_conf = []
    for var in dir(env):
        if (not var.startswith("__")) and (not var.endswith("__")):
            def_conf.append(var)
    
    for conf in new_conf:
        if conf in def_conf:
            setattr(env, conf, getattr(conf_class, conf))#设置值
        else:
            log.step_warning("conf [%s] not found in module env." % conf)
    
    # if result path not set in conf, set where the "run.py" file locates.
    if env.RESULT_PATH == "":
        env.RESULT_PATH = os.path.dirname(os.path.abspath(inspect.stack()[-1][1]))#获取当前模块最开始调用路径 '[0][1]上层模块调用路径' '[1][1当前模块路径'
        


def get_sub_folder_names(full_path):
    return [ name for name in os.listdir(full_path) if os.path.isdir(os.path.join(full_path, name)) ]
    # 遍历目录下的所有文件 如果是一个目录便返回

# 获取版本号
def get_version_info():
    from __init__ import __version__ as emao_Automation
    from selenium import __version__ as selenium_version
    
    from sys import version as python_version
    
    browser_version = ""
    #for k, v in env.BROWSER_VERSION_INFO.iteritems():
    for k, v in env.BROWSER_VERSION_INFO.items():
        browser_version += "%s - %s, " % (k, v)
    
    return "Version Info:  Python %s, %semao-Automation %s, Selenium %s" % (python_version.split(" ")[0],
                                                             browser_version, 
                                                             emao_Automation,
                                                             selenium_version)
    

if __name__ == "__main__":
    pass







