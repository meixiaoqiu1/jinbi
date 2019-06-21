# -*- coding:utf-8
# 该测试套会读取文件夹下所有的用例，并发送邮件
import unittest, time, os
from HTMLTestRunner_cn import HTMLTestRunner
from common_method.send_email import SendEmail
from tomorrow  import threads   #http://www.mamicode.com/info-detail-2284751.html https://www.cnblogs.com/yoyoketang/p/8392471.html
import sys

reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver

# 获取路
casepath = "..\\test_cases"
reportpath = "..\\test_reports\\"
log_reports = "..\\log_reports\\"


def add_case(case_path=casepath, rule="Login.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
                                                   pattern=rule,
                                                   top_level_dir=None)
    return discover
@threads(5)
def run_case(all_case, report_path=reportpath, nth=0):
    '''执行所有的用例, 并把结果写入测试报告'''
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = reportpath + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试用例情况：')
    # 调用add_case函数返回值
    runner.run(all_case)
    fp.close()


if __name__ == "__main__":
    # 用例集合
    cases = add_case()

    # 之前是批量执行，这里改成for循环执行
    for i, j in zip(cases, range(len(list(cases)))):
        run_case(i, nth=j)  # 执行用例，生成报告
    new_report1= SendEmail().new_report(reportpath)
    log_report= SendEmail().new_report(log_reports)
    SendEmail().send_mail(new_report1,log_report)  # 发送测试报告
