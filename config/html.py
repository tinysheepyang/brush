# -*- coding: utf-8 -*-

import os, shutil, datetime, sys, inspect
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(inspect.stack()[-1][1])), 'model'))
from model import env, common
import redis,time,datetime

def yester_time():
    today = datetime.date.today()
    return today - datetime.timedelta(days=1)

#头信息
def html_source_header(title="emao Brush Result"):
    return """<!DOCTYPE HTML>
<html>

<head>
    <title>%s</title>

    <style>
        a {
            color: #034CAC;
            overflow: hidden;
            text-decoration: none;
            display: inline; /* do not show the dot of list */
        }

        a:hover {
            text-decoration: underline;
            color: #034CAC;
        }
        a:visited {
            color: #000000;
        }
        button {
            width: 120px;
        }
        body {
            width: 100%%;
            color: #000000;
            font-size: 13px;
            font-family: verdana, Courier New;
            text-align: center;
        }
        table, td, th {
            border: 1px solid black;
            border-collapse: collapse;
            width: 1260px;
            text-align: center;
        }
        .tcaption {
            background-color: #FFCC33;
        }
        .theader {
            background-color: #FFCC00;
        }
        .tfail{
            background-color: #FF6F6F;
        }
        h1{
            text-align: center;
        }

    </style>
</head>
""" % title


def generate_html_brush(test_cases=[]):


    with open("/root/csy/brush.html", "w") as f:
        f.write(html_source_header())
        f.write(html_source_body_brush())

        brands, a, b = brand()
        test_status = [a,b]

        f.write(html_source_table1_brush(test_status))

        f.write(html_source_table2_brush())
        f.write(html_source_test_cases_brush(brands))


def brand():
     a = 0
     b = 0
     c = 0
     brand = []
     for k,v in serch().items():
            a = a + int(v)
            for h,j in click().items():
                if k == h:
                    brand.append((k,v,j))
                    break
                else:
                    continue

     for h,j in click().items():
                b = b + int(j)
	
     for k,v in serch().items():
         if k not in click().keys():
             brand.append((k,v,c))

     return brand,a,b

def serch():
    pool = redis.ConnectionPool(host='192.168.0.75', port=6379, db=1)
    r = redis.Redis(connection_pool=pool)
    pipe = r.pipeline()
    pipe_size = 100000


    len = 0
    key_list = []
    t = '*' + str(yester_time())
    for key in r.scan_iter(match=t,count=100000):
            key_list.append(key)
            pipe.get(key)
            if len < pipe_size:
                len += 1
            else:
                for (k, v) in zip(key_list, pipe.execute()):
                    print k, v
                len = 0
                key_list = []

    serch = {}
    for (k, v) in zip(key_list, pipe.execute()):
        serch[k] = v

    return serch

def click():

    pool = redis.ConnectionPool(host='192.168.0.75', port=6379, db=2)
    r = redis.Redis(connection_pool=pool)
    pipe = r.pipeline()
    pipe_size = 100000

    len = 0
    key_list = []

    t = '*' + str(yester_time())
    for key in r.scan_iter(match=t,count=100000):
	    
            key_list.append(key)
            pipe.get(key)
            if len < pipe_size:
                len += 1
            else:
                for (k, v) in zip(key_list, pipe.execute()):
                    print k, v
                len = 0
                key_list = []

    click = {}
    for (k, v) in zip(key_list, pipe.execute()):
        click[k] = v

    return click

def html_source_body_brush(title="emao Brush Result"):

    return """<body> <h1>%s</h1> </body>""" % title


def html_source_table1_brush(args):
    return """<table>
        <tr class="tcaption"><th colspan="5">Total Result</th></tr>
        <tr class="theader">
            <th>Serch</th>
            <th>Click</th>
        </tr>
        <tr>
            <td>%s</td>
            <td>%s</td>
        </tr>
    </table>""" % tuple(args)


def html_source_table2_brush():
    return """
    <br />
    <br />
    <table>
        <tr class="tcaption"><th colspan="5">Detail Result</th></tr>
        <tr class="theader">
            <th>Brand</th>
            <th>Serch</th>
            <th>Click</th>
        </tr>
"""
def html_source_test_cases_brush(test_cases):
    return_src_code = ""

    for test_case in test_cases:
        return_src_code += """
                <tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                </tr>
         """ % tuple(test_case)

    return return_src_code





if __name__ == "__main__":
    generate_html_brush([])




















