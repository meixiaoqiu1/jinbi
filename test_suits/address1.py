# -*- coding:utf-8
#该测试套会读取文件夹下所有的用例，并发送邮件
import unittest, time

from HTMLTestRunner_cn import HTMLTestRunner
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import os
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from selenium import webdriver


# ==========定义发送邮件============

def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    FROM = "shemeiqiong@126.com"
    # TO = "cai_j@720wan.com,chang_f@720wan.com, duan_w@720wan.com, li_h@720wan.com"
    TO='xiaomeiqiu111@126.com'

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("自动化测试报告(邮箱发送测试)", 'utf-8')
    msg['From'] = FROM
    msg['To'] = TO

    smtp = smtplib.SMTP()
    smtp.connect('smtp.126.com')
    smtp.login('shemeiqiong@126.com', '100928she')
    smtp.sendmail(FROM, TO, msg.as_string())
    smtp.quit()
    print('email has send out!')


# ====查找测试报告目录，找到最新生成的测试报告文件============

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
    file_new = os.path.join(testreport, lists[-1])
    print(file_new)
    return file_new


if __name__ == '__main__':
    test_dir = "..\\test_cases"


    test_report = "..\\test_reports\\"
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')

    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + '\\' + now + 'result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='测试报告', description='测试用例情况：')

    runner.run(discover)
    fp.close()
    #
    new_report = new_report(test_report)
    send_mail(new_report)  # 发送测试报告