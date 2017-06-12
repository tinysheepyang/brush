# -*- coding: utf-8 -*-
import urllib2,re,time,urllib,random, os, requests, json
import redis,threading,datetime
from fake_useragent import UserAgent

def getUA():
    ua = UserAgent()
    return ua.random

def proxy(url):
    try:
        data = urllib2.urlopen(url).read()

    except Exception,e:
        print 'proxy 出问题了',e

    s = json.loads(data)
    try:
        if len(s['msg']) == 0:

            return list(set(s['data']['proxy_list']))
        else:
            print '返回None'
            time.sleep(5)
            return proxy(url)
    except Exception,e:
        print e
        time.sleep(10)
        return proxy(url)


def Check(ip_list):
    proxy_ip_list = []
    try:
        for ip in ip_list:
            lock = threading.Lock()
            cookie = "PHPSESSID=5f7mbqghvk1kt5n9illa0nr175; kmsign=56023b6880039; KMUID=ezsEg1YCOzxg97EwAwUXAg=="
            try:
                proxy = 'http://'+ ip

                proxy_support = urllib2.ProxyHandler({'http': proxy})
                opener = urllib2.build_opener(proxy_support, urllib2.HTTPHandler)
                urllib2.install_opener(opener)
                request = urllib2.Request('http://www.baidu.com')
                request.add_header("cookie",cookie)
                request.add_header("User-Agent", getUA())
                content = urllib2.urlopen(request,timeout=3).read()


                if len(content) >= 1000:
                    lock.acquire()
                    proxy_ip_list.append(ip)
                    lock.release()
                else:
                    print '出现验证码或IP被封杀'
            except Exception, error:
                print ip, error
    except Exception, e:
        print 'ip_list', ip_list, e


    return proxy_ip_list

if __name__ == '__main__':
    pool = redis.ConnectionPool(host='redis.lan', port=6379, db=0)
    r = redis.Redis(connection_pool=pool)

    proxy_list = Check(proxy('http://dps.kuaidaili.com/api/getdps/?orderid=996639436139576&num=30&ut=1&format=json&sep=2'))

    if len(r.lrange('proxy_list', 0, -1)) >= 0:
        r.delete('proxy_list')
        print 'delete redis[proxy_list] done'

        for ip in proxy_list:
            r.lpush('proxy_list', ip)
        print 'lpush redis[proxy_list] done'
        print 'proxy_list', len(r.lrange('proxy_list', 0, -1)), random.choice(r.lrange('proxy_list', 0, -1))
    else:
        for ip in proxy_list:
            r.lpush('proxy_list', ip)
        print 'lpush redis[proxy_list] done'
        print 'proxy_list', len(r.lrange('proxy_list', 0, -1)), random.choice(r.lrange('proxy_list', 0, -1))

    print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print 'done'
