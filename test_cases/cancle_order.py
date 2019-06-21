# -*- coding:utf-8 -*-
from robotide.action import action
from utils.get_selenium_driver import GetSeleniumDriver
from common_method.common_def import CommonDef
from utils.logger import Logger
import unittest,time
mylogger = Logger(__name__).getlog()
class CancleOrder(unittest.TestCase):

    def setUp(self):
        self.driver = GetSeleniumDriver().driver
        CommonDef().login(u"http://pftest.ecgci.com/index.html",u"test0135",u"aaaaaa")
    def tearDown(self):
        CommonDef().quit()

    def testcase_cancle_order(self):
        self.driver.find_element_by_link_text(u'我的订单').click()
        time.sleep(1)
        #self.driver.find_element_by_class_name("cancel_order").click()
        self.driver.find_element_by_xpath("//*[@id='list_box']/tr[1]/td[9]/div/div[4]/a").click()
        time.sleep(1)


