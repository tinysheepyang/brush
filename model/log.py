# -*- coding: utf-8 -*-

import datetime, sys, os
import xlwt, inspect
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(inspect.stack()[-1][1])), 'model'))
import common, htmlreport, webelement, env
import subprocess

#启动测试用例
def start_test(case_name):
    #env.threadlocal.CASE_NAME       = case_name
    #env.threadlocal.CASE_START_TIME = datetime.datetime.now().replace(microsecond=0)
    #env.threadlocal.CASE_PASS       = True
    #env.threadlocal.CASE_WARNINGS   = 0
    env.threadlocal.__setattr__('CASE_NAME', case_name)
    env.threadlocal.__setattr__('CASE_START_TIME', datetime.datetime.now().replace(microsecond=0))
    env.threadlocal.__setattr__('CASE_PASS', True)
    env.threadlocal.__setattr__('CASE_WARNINGS', 0)

    #写入测试用例名称及浏览器
    write_log(os.path.join("testcase", "%s.log" % (case_name)), 
              "\n**************  Test Case [%s] [%s]  ***************\n" %(case_name, env.threadlocal.__getattribute__('TESTING_BROWSER')))
    
    
#启动全部测试用例
def start_total_test():
    env.threadlocal.CASE_START_TIME  = ""
    env.threadlocal.CASE_STOP_TIME   = ""
    env.threadlocal.CASE_NAME        = ""
    env.threadlocal.CASE_PASS        = True
    env.threadlocal.CASE_WARNINGS    = 0
    
    env.threadlocal.MODULE_NAME      = ""
    
    env.threadlocal.BROWSER          = None
    
    env.threadlocal.TESTING_BROWSER  = ""

    env.threadlocal.TESTING_BROWSERS = ""
    
    env.TOTAL_TESTCASE_PASS = 0
    env.TOTAL_TESTCASE_FAIL = 0
    env.HTMLREPORT_TESTCASES[:] = []
    
    common.delete_file_or_folder(os.path.join(env.RESULT_PATH, "result", "testcase"))
    common.delete_file_or_folder(os.path.join(env.RESULT_PATH, "result", "screenshots"))
    
    env.TOTAL_START_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")#启动全部时间
    
    print  (">>>>>>  [%s]  =>  start testing......       <<<<<<" %
              (
               env.TOTAL_START_TIME,
               )
           )
    
    htmlreport.generate_html_report([env.TOTAL_START_TIME, "N/A", "N/A", "N/A", "N/A", "N/A"], [])

    


#总共完成
def finish_total_test():
    env.TOTAL_STOP_TIME = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    print (">>>>>>  [%s]  =>  [%s], duration [%s], case [%s], pass [%s], fail [%s]       <<<<<<" %
              (
               env.TOTAL_START_TIME,
               env.TOTAL_STOP_TIME,
               datetime.datetime.strptime(env.TOTAL_STOP_TIME, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(env.TOTAL_START_TIME, "%Y-%m-%d %H:%M:%S"),
               env.TOTAL_TESTCASE_PASS + env.TOTAL_TESTCASE_FAIL, 
               env.TOTAL_TESTCASE_PASS,
               env.TOTAL_TESTCASE_FAIL,
               )
            )
    
    print (
           ">>>>>>  [%s]  =>  [%s]" % (env.TOTAL_START_TIME, common.get_version_info())
           )
    
    htmlreport.generate_html_report([env.TOTAL_START_TIME, env.TOTAL_STOP_TIME, datetime.datetime.strptime(env.TOTAL_STOP_TIME, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(env.TOTAL_START_TIME, "%Y-%m-%d %H:%M:%S"), 
                                     env.TOTAL_TESTCASE_PASS+env.TOTAL_TESTCASE_FAIL, env.TOTAL_TESTCASE_PASS, env.TOTAL_TESTCASE_FAIL], 
                                    env.HTMLREPORT_TESTCASES,
                                    countdown=False)
    htmlreport.save_current_report_to_repository()
    htmlreport.generate_report_history()
    htmlreport.generate_html_report([env.TOTAL_START_TIME, env.TOTAL_STOP_TIME, datetime.datetime.strptime(env.TOTAL_STOP_TIME, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(env.TOTAL_START_TIME, "%Y-%m-%d %H:%M:%S"), 
                                     env.TOTAL_TESTCASE_PASS+env.TOTAL_TESTCASE_FAIL, env.TOTAL_TESTCASE_PASS, env.TOTAL_TESTCASE_FAIL], 
                                    env.HTMLREPORT_TESTCASES,
                                    countdown=True)


    #htmlreport.generate_html_brush([])
    env.TOTAL_TESTCASE_PASS = 0
    env.TOTAL_TESTCASE_FAIL = 0
    env.CLICKBRAND = 0
    env.HTMLREPORT_TESTCASES[:] = []
    
    print ("\n")
    
        

def stop_test():
    
    try:
        env.THREAD_LOCK.acquire()
        
        env.threadlocal.CASE_STOP_TIME = datetime.datetime.now().replace(microsecond=0)
        env.TOTAL_STOP_TIME            = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        if env.threadlocal.CASE_WARNINGS > 0:
            warning_message = ", has [%s] warning(s)!" % env.threadlocal.CASE_WARNINGS
        else:
            warning_message = ""
        
        if env.threadlocal.CASE_PASS == True:
            print (u"%s    [Pass]  =>  [%s] [%s] [%s] [%s]%s" %(common.stamp_datetime(), 
                                                        env.threadlocal.CASE_STOP_TIME - env.threadlocal.CASE_START_TIME, 
                                                        env.threadlocal.MODULE_NAME, 
                                                        env.threadlocal.CASE_NAME, 
                                                        env.threadlocal.TESTING_BROWSER,
                                                        warning_message
                                                        ))
            env.TOTAL_TESTCASE_PASS = env.TOTAL_TESTCASE_PASS + 1
            
            env.HTMLREPORT_TESTCASES.append(["%s =&gt; %s" % (env.threadlocal.CASE_START_TIME.strftime("%m-%d %H:%M:%S"), env.threadlocal.CASE_STOP_TIME.strftime("%m-%d %H:%M:%S")),
                                             '<a href="testcase/%s.log">[%s] - %s</a>' % (env.threadlocal.CASE_NAME, env.threadlocal.MODULE_NAME, env.threadlocal.CASE_NAME),
                                             env.threadlocal.CASE_STOP_TIME - env.threadlocal.CASE_START_TIME, 
                                             env.threadlocal.TESTING_BROWSER, 
                                             '<td>Pass</td>'
                                             ])
            
        else:
            print ("%s    [Fail]  =>  [%s] [%s] [%s] [%s]%s  :( " %(common.stamp_datetime(),
                                                                 env.threadlocal.CASE_STOP_TIME - env.threadlocal.CASE_START_TIME, 
                                                                 env.threadlocal.MODULE_NAME, 
                                                                 env.threadlocal.CASE_NAME, 
                                                                 env.threadlocal.TESTING_BROWSER,
                                                                 warning_message
                                                                 ))
            env.TOTAL_TESTCASE_FAIL = env.TOTAL_TESTCASE_FAIL + 1
            
            env.HTMLREPORT_TESTCASES.append(["%s =&gt; %s" % (env.threadlocal.CASE_START_TIME.strftime("%m-%d %H:%M:%S"),env.threadlocal.CASE_STOP_TIME.strftime("%m-%d %H:%M:%S")),
                                             '<a href="testcase/%s.log">[%s] - %s</a>' % (env.threadlocal.CASE_NAME, env.threadlocal.MODULE_NAME, env.threadlocal.CASE_NAME),
                                             env.threadlocal.CASE_STOP_TIME - env.threadlocal.CASE_START_TIME, 
                                             env.threadlocal.TESTING_BROWSER, 
                                             '<td class="tfail"><a href="screenshots/%s">Fail</a></td>' % env.HTMLREPORT_SCREENSHOT_NAME
                                             ])

        htmlreport.generate_html_report([env.TOTAL_START_TIME, env.TOTAL_STOP_TIME, datetime.datetime.strptime(env.TOTAL_STOP_TIME, "%Y-%m-%d %H:%M:%S") - datetime.datetime.strptime(env.TOTAL_START_TIME, "%Y-%m-%d %H:%M:%S"), 
                                         env.TOTAL_TESTCASE_PASS+env.TOTAL_TESTCASE_FAIL, env.TOTAL_TESTCASE_PASS, env.TOTAL_TESTCASE_FAIL], 
                                        env.HTMLREPORT_TESTCASES)


        env.threadlocal.CASE_PASS     = True
        env.threadlocal.CASE_WARNINGS = 0
    finally:
        env.THREAD_LOCK.release()



#部分通过
def step_section(message):
    write_log(os.path.join("testcase", "%s.log" % (env.threadlocal.CASE_NAME)), 
              "\n%s    Section: %s\n" %(common.stamp_datetime(), message))

#正常
def step_normal(message):
    write_log(os.path.join("testcase", "%s.log" % (env.threadlocal.CASE_NAME)), 
              "%s    Step: %s\n" %(common.stamp_datetime(), message))


def step_pass(message):
    write_log(os.path.join("testcase", "%s.log" % (env.threadlocal.CASE_NAME)), 
              "%s    Pass: %s\n" %(common.stamp_datetime(), message))


def step_fail(message):
    """
    失败或者异常对当前页面截图
    """
    #mail(env.threadlocal.CASE_NAME, env.threadlocal.BROWSER.current_url, common.stamp_datetime_coherent())
    
    screenshot_name = "Fail__%s__%s__%s.png" % (common.stamp_datetime_coherent(), env.threadlocal.CASE_NAME, env.threadlocal.TESTING_BROWSER)
    
    write_log(os.path.join("testcase", "%s.log" % (env.threadlocal.CASE_NAME)),  
              "------------ Fail [%s] -------------------\n"%common.stamp_datetime())
    
    write_log(os.path.join("testcase", "%s.log" % (env.threadlocal.CASE_NAME)), 
              "%s    Fail: %s, Check ScreenShot [%s]\n" %(common.stamp_datetime(), message, screenshot_name))
    
    write_log(os.path.join("testcase", "%s.log" % (env.threadlocal.CASE_NAME)), 
              "------------ Fail [%s] --------------------------------------------\n"%common.stamp_datetime())
    
    try:
        save_screen_shot(screenshot_name)
    except:
        step_normal(str(sys.exc_info()))
    
    env.HTMLREPORT_SCREENSHOT_NAME = screenshot_name
    env.threadlocal.CASE_PASS = False
    env.EXIT_STATUS = -1
    

    raise AssertionError(message)


def step_warning(message):
    screenshot_name = "Warning__%s__%s__%s.png" % (common.stamp_datetime_coherent(), env.threadlocal.CASE_NAME, env.threadlocal.TESTING_BROWSER)
    
    write_log(os.path.join("testcase", "%s.log" % (env.threadlocal.CASE_NAME)), 
              "------------ Warning [%s] -------------------\n"%common.stamp_datetime())
    
    write_log(os.path.join("testcase", "%s.log" % (env.threadlocal.CASE_NAME)), 
              "%s    Warning: %s, Check ScreenShot [%s]\n" %(common.stamp_datetime(), message, screenshot_name))
    
    write_log(os.path.join("testcase", "%s.log" % (env.threadlocal.CASE_NAME)), 
              "------------ Warning [%s] --------------------------------------------\n"%common.stamp_datetime())
    
    try:
        save_screen_shot(screenshot_name)
    except:
        step_normal(str(sys.exc_info()))
    
    env.threadlocal.CASE_WARNINGS = env.threadlocal.CASE_WARNINGS + 1




def write_log(relative_path, log_message):
    log_path = os.path.join(env.RESULT_PATH, "result", relative_path)
    common.mkdirs(os.path.dirname(log_path))


    with open(log_path, 'a') as f:
        f.write(log_message)
    f.close()



def save_screen_shot(image_name):
    image_path = os.path.join(env.RESULT_PATH, "result", "screenshots")
    common.mkdirs(image_path)
    #截图
    env.threadlocal.BROWSER.save_screenshot(os.path.join(image_path, image_name))
    



# 流程错误处理
def handle_error():
    if env.threadlocal.CASE_PASS == False:
        return
    
    
    if sys.exc_info()[0] != None:
        step_normal(common.exception_error())
        
        screenshot_name = "Fail__%s__%s__%s.png" % (common.stamp_datetime_coherent(), env.threadlocal.CASE_NAME, env.threadlocal.__getattribute__('TESTING_BROWSER'))
        
        try:
            save_screen_shot(screenshot_name)
        except:
            step_warning(str(sys.exc_info()))
        
        step_normal("Current step screen short [%s]" % (screenshot_name))
        
        env.HTMLREPORT_SCREENSHOT_NAME = screenshot_name
        
        env.threadlocal.CASE_PASS = False
        env.EXIT_STATUS = -1

def mail(caseID, url, datatime):
    env.MODEL_PATH = os.path.join(env.RESULT_PATH, 'model')
 
  
    cmd = ["python", os.path.join(env.MODEL_PATH, 'mail.py'), "-e", "online", '-c', 
        str(caseID), '-s', "失败".decode('UTF-8'), '-u', url, '-m', str(webelement.WebBrowser.GetStatusCode(url)), '-d', datatime, '-t', 'ops@emao.com']

    sendsms = subprocess.Popen(cmd, 
                              stdout = subprocess.PIPE,
                              stderr = subprocess.PIPE)

    sendsms.wait()
    step_normal('sendsms ret:')
    

    for line in sendsms.stdout.readlines():
        step_pass(line)
        

    for line in sendsms.stderr.readlines():
        step_fail(line)
        
    













