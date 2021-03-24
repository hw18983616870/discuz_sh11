"""
============================
@author:多测师-黄sir
@time:2021/3/13:10:34
@email:hw18983616870@163.com
@website:www.duoceshi.com
============================
"""
'''此模块用来执行所有的测试用例'''
import sys

import unittest
from config.Config import *
from public.utils.HTMLTestRunner3_New import HTMLTestRunner
from public.utils.mail3 import SendMail
import time
sys.path.append(path)
def run_all():
    discover = unittest.defaultTestLoader.discover(start_dir=testcase_path,
                                                   pattern='Test*.py')
    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    filename = report_path+'\\'+str(now)+'_UI_report.html'
    f = open(file=filename,mode='wb')
    runner = HTMLTestRunner(
        stream=f,
        title='DISCUZ论坛UI自动化测试报告',
        description='用例执行情况如下：',
        tester='多测师'
    )
    runner.run(discover)
    f.close()
    sm = SendMail(send_msg=filename,attachment=filename)
    sm.send_mail()

run_all()