# -*- coding: utf-8 -*-

import os, shutil, datetime, sys, inspect
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(inspect.stack()[-1][1])), 'model'))
from model import env, common
import log

#头信息
def html_source_header(title="emao Web Automation Test Result"):
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


def html_source_body(title="emao Web Automation Test Result", countdown=True):
    if countdown == False:
        return """<body> <h1>%s</h1> <p>[<a href="..\index.html">Last Test</a>]&nbsp;[<a href="..\history.html">History Tests</a>]""" % title
    
    return """
<body>
    <script>
        function countdown(){
            var timer = 9;
            setInterval(function() {
                timer--;
                document.getElementById('timer').innerHTML = timer;
        
            }, 1000);
        }
        function autorefresh(){
            window.location.reload(); 
        } 
        
        countdown();
        window.setTimeout('autorefresh()', 9000);
    </script>
    
    <h1>%s</h1>
    <p style="text-align: center">
    [<a href="index.html">Last Test</a>]&nbsp;[<a href="history.html">History Tests</a>]
    </p>
    <p style="text-align: center">
    Pending to do auto-refresh in [<span id='timer'>9</span>] seconds. &nbsp;&nbsp;&nbsp;&nbsp;<button onclick="window.location.reload();">Refresh Now</button></p>
    
""" % title

#生成test_status
def html_source_table1(args):
    return """
    <table>
        <tr class="tcaption"><th colspan="5">Test Status</th></tr>
        
        <tr class="theader">
            <th>Time</th>
            <th>Duration</th>
            <th>Total Cases</th>
            <th>Passed Cases</th>
            <th>Failed Cases</th>
        </tr>
        <tr>
            <td style='width: 35%%'>%s =&gt; %s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
    </table>
""" % tuple(args)

#历史结果头连接
def html_source_table_history_header():
    return """
    <table>
        <tr class="tcaption"><th colspan="5">History Results (Latest 100 Results)</th></tr>
        
        <tr class="theader">
            <th>Result Folder</th>
            <th>Duration</th>
            <th>Total Cases</th>
            <th>Passed Cases</th>
            <th>Failed Cases</th>
        </tr>
""" 
#历史记录
def html_source_table_history(*args):
    return """
        <tr>
            <td style='width: 36%%'><a href="%s/index.html">%s</a></td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
""" % args

#生成test_cases
def html_source_table2():
    return """
    <br />
    <br />
    <table>
        <tr class="tcaption"><th colspan="5">Test Cases</th></tr>
        <tr class="theader">
            <th>Time</th>
            <th>Case</th>
            <th>Duration</th>
            <th>Browser</th>
            <th>Result</th>
        </tr>

"""
# test_cases结果内容信息
def html_source_test_cases(test_cases):
    return_src_code = ""
    
    for test_case in test_cases:
        return_src_code += """
                <tr>
                    <td style="width: 20%%">%s</td>
                    <td style="width: 52%%; text-align: left;">&nbsp;%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    %s
                </tr>
        """ % tuple(test_case)
    
    return return_src_code

def html_source_end_table():
        return """
        </table>
    <br />
    <br />
    <br />
    """

def html_source_version_info():
    return """
<p style="text-align: center">%s</p>
""" % common.get_version_info()

def html_source_foot():
    return """
<hr />
<p style="text-align: center">@2016 DB emao</p>
<br />
<body>
</html>
"""

# 生成测试报告
def generate_html_report(test_status, test_cases=[], countdown=True):
    
    common.mkdirs(os.path.join(env.RESULT_PATH, "result"))
    
    with open(os.path.join(env.RESULT_PATH, "result", "index.html"), "w") as f:
        f.write(html_source_header())
        f.write(html_source_body(countdown=countdown))
        
        f.write(html_source_table1(test_status))
        f.write(html_source_table2())
         
        f.write(html_source_test_cases(test_cases))
        
        f.write(html_source_end_table())
        f.write(html_source_version_info())
        f.write(html_source_foot())
    

#保存结果到当前存储
def save_current_report_to_repository():
    report_dir = os.path.join(env.RESULT_PATH, 
                              "result", 
                              "%s__%s" % (datetime.datetime.strptime(env.TOTAL_START_TIME, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d_%H%M%S"),
                                         datetime.datetime.strptime(env.TOTAL_STOP_TIME, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d_%H%M%S")))
    common.delete_then_mkdir(report_dir)
    
    common.copy(os.path.join(env.RESULT_PATH, "result", "testcase"), os.path.join(report_dir, "testcase"))
    common.copy(os.path.join(env.RESULT_PATH, "result", "screenshots"), os.path.join(report_dir, "screenshots"))
    common.copy(os.path.join(env.RESULT_PATH, "result", "index.html"), report_dir)
    
    with open(os.path.join(report_dir, "status.ini"), "w") as f:
        f.write("Duration=%s\n" % str(datetime.datetime.strptime(env.TOTAL_STOP_TIME, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(env.TOTAL_START_TIME, "%Y-%m-%d %H:%M:%S")))
        f.write("TotalCases=%s\n" % str(env.TOTAL_TESTCASE_PASS+env.TOTAL_TESTCASE_FAIL))
        f.write("PassedCases=%s\n" % str(env.TOTAL_TESTCASE_PASS))
        f.write("FailedCases=%s\n" % str(env.TOTAL_TESTCASE_FAIL))
        f.write("BRAND=%s\n" % str(env.BRAND))
        f.write("CLICKBRAND=%d\n" % env.CLICKBRAND)
        f.write("BROWSE=%d\n" % env.BROWSE)
    

# 生成历史记录页面
def generate_report_history():
    folders = common.get_sub_folder_names(os.path.join(env.RESULT_PATH, "result"))
    
    reports = []
    for folder in folders:
        if len(folder) == 36:
            reports.append(folder)
    
    
    with open(os.path.join(env.RESULT_PATH, "result", "history.html"), "w") as f:
        f.write(html_source_header(title="emao Web Automation Test History"))
        f.write(html_source_body(title="emao Web Automation Test History"))
        f.write(html_source_table_history_header())
        
        i = 0
        for report in sorted(reports, reverse=True):#倒序排序遍历
            
            Duration     = common.get_value_from_conf(os.path.join(env.RESULT_PATH, "result", report, "status.ini"), "Duration")
            TotalCases   = common.get_value_from_conf(os.path.join(env.RESULT_PATH, "result", report, "status.ini"), "TotalCases")
            PassedCases  = common.get_value_from_conf(os.path.join(env.RESULT_PATH, "result", report, "status.ini"), "PassedCases")
            FailedCases  = common.get_value_from_conf(os.path.join(env.RESULT_PATH, "result", report, "status.ini"), "FailedCases")
            
            f.write(html_source_table_history(report, report, Duration, TotalCases, PassedCases, FailedCases))

            
            i = i + 1
            if i > 100: break
         
        
        f.write(html_source_end_table())
        f.write(html_source_foot())

def generate_html_brush(test_cases=[], countdown=True):

    folders = common.get_sub_folder_names(os.path.join(env.RESULT_PATH, "result"))

    reports = []
    for folder in folders:
        if len(folder) == 36:
            reports.append(folder)
    
    with open(os.path.join(env.RESULT_PATH, "result", "brush.html"), "w") as f:
        f.write(html_source_header())
        f.write(html_source_body_brush(countdown=countdown))
        f.write(html_source_table1_brush())

        i = 0
        car = {}
        for report in sorted(reports, reverse=True):#倒序排序遍历

            BRAND     = common.get_value_from_conf(os.path.join(env.RESULT_PATH, "result", report, "status.ini"), "BRAND")
            CLICKBRAND   = common.get_value_from_conf(os.path.join(env.RESULT_PATH, "result", report, "status.ini"), "CLICKBRAND")
            BROWSE   = common.get_value_from_conf(os.path.join(env.RESULT_PATH, "result", report, "status.ini"), "BROWSE")


            if BRAND is not None and BRAND not in car:
                car[BRAND] = [1,int(CLICKBRAND),int(BROWSE)]

            elif BRAND is not None:
                car[BRAND][0] += 1
                car[BRAND][1] += int(CLICKBRAND)
                car[BRAND][2] += int(int(BROWSE))

            else:
                log.step_warning('该代理ip没有打开百度搜索 [%s]' % env.BRAND)


        for key,value in car.items():
            f.write(html_source_table2_brush((key, value[0], value[1], value[2])))
         
        f.write(html_source_version_info())
        f.write(html_source_foot())




def html_source_body_brush(title="emao brush Result", countdown = True):
    if countdown == False:
        return """<body> <h1>%s</h1> <p>""" % title
    
    return """
    <body>
        <script>
            function countdown(){
                var timer = 9;
                setInterval(function() {
                    timer--;
                    document.getElementById('timer').innerHTML = timer;

                }, 1000);
            }
            function autorefresh(){
                window.location.reload();
            }

            countdown();
            window.setTimeout('autorefresh()', 9000);
        </script>

        <h1>%s</h1>
        <p style="text-align: center">
        [<a href="index.html">Last Test</a>]&nbsp;[<a href="history.html">History Tests</a>]
        </p>
        <p style="text-align: center">
        Pending to do auto-refresh in [<span id='timer'>9</span>] seconds. &nbsp;&nbsp;&nbsp;&nbsp;<button onclick="window.location.reload();">Refresh Now</button></p>

    """ % title


def html_source_table1_brush():
    return """
    <table>
        <tr class="tcaption"><th colspan="5">Brush Status</th></tr>
        
        <tr class="theader">
            <th>Brand</th>
            <th>Search</th>
            <th>Click</th>
            <th>Browse</th>
        </tr>
    </table>
    <style type="text/css">
    table{
        width:1000px;
        height:30px;
        border:#0C9 1px solid;
        border-collapse:collapse;
        }
    </style>
    """


def html_source_table2_brush(args):
    return """
    <table>
        <tr>
            <td style='width: 35%%'>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
        </tr>
    </table>
    <style type="text/css">
    table{
        width:1000px;
        height:30px;
        border:#0C9 1px solid;
        border-collapse:collapse;
        }
    </style>
    """ % tuple(args)




if __name__ == "__main__":
    pass




















