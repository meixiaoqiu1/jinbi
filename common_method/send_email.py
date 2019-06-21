# -*- coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os
# ==========定义发送邮件(带附件)https://www.runoob.com/python/python-email.html============

class SendEmail():

    def send_mail(self,file_new,log_report=None):#默认参数https://www.cnblogs.com/bitpeng/p/4747765.html
        f = open(file_new, 'rb')
        mail_body = f.read()
        f.close()

        FROM = "shemeiqiong@126.com"
        # TO = "cai_j@720wan.com,chang_f@720wan.com, duan_w@720wan.com, li_h@720wan.com"
        TO='xiaomeiqiu111@126.com'

        #创建一个带附件的实例
        message = MIMEMultipart()
        message['From'] = FROM
        message['To'] = TO
        subject = 'login自动化测试报告'
        message['Subject'] = Header(subject, 'utf-8')

        #邮件正文内容
        message.attach(MIMEText(mail_body, 'html', 'utf-8'))

        # 构造附件1
        att1 = MIMEText(open(file_new, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'
        # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
        att1["Content-Disposition"] = 'attachment; filename="login自动化测试报告.html"'
        message.attach(att1)

        # 构造附件2
        if log_report!=None:
            att2 = MIMEText(open(log_report, 'rb').read(), 'base64', 'utf-8')
            att2["Content-Type"] = 'application/octet-stream'
            # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
            att2["Content-Disposition"] = 'attachment; filename="login自动化测试报告.txt"'
            message.attach(att2)
        else:
            pass

        smtp = smtplib.SMTP()
        smtp.connect('smtp.126.com')
        smtp.login('shemeiqiong@126.com','100928she')#https://blog.csdn.net/huochen1994/article/details/51282093
        smtp.sendmail(FROM, TO, message.as_string())
        smtp.quit()
        print('email has send out!')


    # ====查找测试报告目录，找到最新生成的测试报告文件============

    def new_report(self,testreport):
        #列举test_dir目录下的所有文件（名），结果以列表形式返回。https://www.runoob.com/python/os-listdir.html
        """

        :rtype: object
        """
        lists = os.listdir(testreport)
        #sort按key的关键字进行升序排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间，所以最终以文件时间从小到大排序
        lists.sort(key=lambda fn: os.path.getmtime(testreport + '\\' + fn))
        #获取最新文件的绝对路径，列表中最后一个值,文件夹+文件名 https://www.cnblogs.com/Owen-ET/p/8610446.html
        file_new = os.path.join(testreport, lists[-1])
        print(file_new)
        return file_new
