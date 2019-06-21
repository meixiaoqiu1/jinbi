# -*- coding:utf-8 -*-
from robotide.action import action
from utils.get_selenium_driver import GetSeleniumDriver
from common_method.common_def import CommonDef
from utils.logger import Logger
import unittest,time
mylogger = Logger(__name__).getlog()
class AddShoppingCart(unittest.TestCase):

    def setUp(self):
        self.driver = GetSeleniumDriver().driver
        CommonDef().login(u"http://pftest.ecgci.com/index.html",u"test0135",u"aaaaaa")
    def tearDown(self):
        CommonDef().quit()

    def test_add_shoppingcart(self):
        count1=0
        count2=0

        for i in range(1,1100):
            self.driver.get("http://itemtest.ecgci.com/product_detail_%d.html"%i)
            #time.sleep(1)
            try:
                self.driver.find_element_by_id("gwc").click()
            except Exception as error:
                print"%d未能成功加入购物车"%i
                count1+=1
            count2+=1
            count=count2-count1
            while count>50:
                break







