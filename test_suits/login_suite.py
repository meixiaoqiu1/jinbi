# -*- coding:utf-8
#该测试套会读取文件夹下所有的用例，并发送邮件
import unittest, time
from HTMLTestRunner_cn import HTMLTestRunner
from common_method.send_email import SendEmail
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver

if __name__ == '__main__':
    test_dir = "..\\test_cases"
    test_report = "..\\test_reports\\"
    log_reports = "..\\log_reports\\"
    #https://www.cnblogs.com/onlyhua/p/7324478.html
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='Login.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试用例情况：')

    runner.run(discover)
    fp.close()
    new_report1= SendEmail().new_report(test_report)
    log_report= SendEmail().new_report(log_reports)
    SendEmail().send_mail(new_report1,log_report)  # 发送测试报告