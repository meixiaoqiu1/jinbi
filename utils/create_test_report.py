# -*- coding:utf-8 -*-
#wb  w 代表写入 b代表二进制
#verbosity 日志级别，默认为第一级别，日志级别分为1-10.1是最低，10是最高。1执行多条case，只输出一个唯一结果，正确or错误。4条case，一条错误，就会报错误。当全部正确才报pass。
#2级日志，有条少条case，显示几条。一条对应一个结果，错误打印错误结果。10包括调用逻辑都会打印出来
import HTMLTestRunner_cn
class CreatTestReport(object):
    def CreatHtmlReport(self,fileName,revTitle,revDes,revSuite):
        with open("../test_reports/"+fileName+".html","wb")as htmlSteam:
            HTMLTestRunner_cn.HTMLTestRunner(
                stream=htmlSteam,
                verbosity=2,#日志级别
                title=revTitle,#标题，接受变量
                description=revDes#描述，用变量来接受

            ).run(revSuite)