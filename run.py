# -*- coding: utf-8 -*-

from Page import conf, testcase
from model import executer,env




def Case3():
    executer.run(conf.Brush, testcase.validations.TestCase_1)
    executer.run(conf.Brush, testcase.validations.TestCase_2)
    executer.run(conf.Brush, testcase.validations.TestCase_3)
    executer.run(conf.Brush, testcase.validations.TestCase_4)
    executer.run(conf.Brush, testcase.validations.TestCase_5)
    executer.run(conf.Brush, testcase.validations.TestCase_6)
    executer.run(conf.Brush, testcase.validations.TestCase_7)
    executer.run(conf.Brush, testcase.validations.TestCase_8)
    executer.run(conf.Brush, testcase.validations.TestCase_9)
    executer.run(conf.Brush, testcase.validations.TestCase_10)
    executer.run(conf.Brush, testcase.validations.TestCase_11)
    executer.run(conf.Brush, testcase.validations.TestCase_12)
    executer.run(conf.Brush, testcase.validations.TestCase_13)
    executer.run(conf.Brush, testcase.validations.TestCase_14)
    executer.run(conf.Brush, testcase.validations.TestCase_15)
    executer.run(conf.Brush, testcase.validations.TestCase_16)
    executer.run(conf.Brush, testcase.validations.TestCase_17)



if __name__ == "__main__":

    Case3()
    # RESULT_PATH = os.path.dirname(os.path.abspath(inspect.stack()[-1][1]))
    # path = RESULT_PATH.split('/')[3]
    # inc = 30
    #
    # if path == 'code7':
    #     Case1()
    #     exit(1)
    #
    # elif path =='code8':
    #     Case2()
    #     exit(1)
    #
    # elif path =='code9':
    #     Case3()
    #     exit(1)
    #
    # elif path =='code10':
    #     Case4()
    #     exit(1)
    #
    # elif path =='code11':
    #     Case5()
    #     exit(1)
    #
    # elif path =='code12':
    #     Case6()
    #     exit(1)
    # elif path =='code13':
    #     Case7()
    #     exit(1)



