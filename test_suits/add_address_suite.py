# -*- coding:utf-8
import unittest
from test_cases.test_address import TestAddress


suite = unittest.TestSuite()
suite.addTest(TestAddress('test02'))
for i in range(int(9)):
        print '\n',u'执行第',i+1,u'次测试:'
        suite = unittest.TestSuite()
        suite.addTest(TestAddress('test02'))
        runner = unittest.TextTestRunner()
        runner.run(suite)

#
# if __name__=='__main__':
#     #执行用例
#     runner=unittest.TextTestRunner()
#     runner.run(suite)