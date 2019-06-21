# -*- coding:utf-8 -*-
from robotide.action import action

from utils.get_selenium_driver import GetSeleniumDriver
from pages.goods_detail import GoodsDetail
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from pages.order_submit import OrderSubmitPage
from common_method.common_def import CommonDef
from selenium.webdriver.common.keys import Keys  #需要引入keys包
from selenium.webdriver.common.action_chains import ActionChains
import unittest,time
from utils.logger import Logger
mylogger = Logger(__name__).getlog()
class OrderSubmit(unittest.TestCase):
    # #继承unnittest初始化方法
    # @classmethod
    # def setUpClass(cls):
    #     cls.driver = GetSeleniumDriver().driver
    #     cls.driver.get("http://pftest.ecgci.com/index.html")
    #     time.sleep(1)
    #     cls.driver.maximize_window()
    #     time.sleep(1)
    #     #点击请登录
    #     IndexPage().click_login_link().click()
    #     time.sleep(1)
    #     #输入用户名
    #     LoginPage().click_username().send_keys(u"test0135")
    #     time.sleep(1)
    #     #输入密码
    #     LoginPage().click_password().send_keys("aaaaaa")
    #     time.sleep(3)
    #     #点击登录按钮
    #     LoginPage().click_login_submit().click()
    #     time.sleep(3)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     cls.driver.quit()
        #继承unnittest初始化方法
    def setUp(self):
        self.driver = GetSeleniumDriver().driver
        self.driver.get("http://pftest.ecgci.com/index.html")
        time.sleep(1)
        self.driver.maximize_window()
        time.sleep(1)
        #点击请登录
        IndexPage().click_login_link().click()
        time.sleep(1)
        #输入用户名
        LoginPage().click_username().send_keys(u"test0135")
        time.sleep(1)
        #输入密码
        LoginPage().click_password().send_keys("aaaaaa")
        time.sleep(3)
        #点击登录按钮
        LoginPage().click_login_submit().click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_order_submit(self):
        #下滑滚动条
        #for i in (0,28):
        action = ActionChains(self.driver).move_to_element(self.driver.find_element_by_id("keyval"))
        action.send_keys(Keys.ARROW_DOWN)#点击键盘向下箭头
        time.sleep(3)
        #获取当前窗口句柄
        nowhandle=self.driver.current_window_handle
        #点击纪念币楼层第一行第4个商品
        IndexPage().click_goods14_link().click()
        time.sleep(3)
        #获取所有handle
        allhandles=self.driver.window_handles
        #循环，当句柄不等于首页句柄时，转换为现在的窗口句柄
        for handle in allhandles:
            if handle!=nowhandle:
                self.driver.switch_to_window(handle)
        #点击立即购买
        GoodsDetail().click_buy_id().click()
        time.sleep(1)
         #滑动滚动条
        CommonDef().huadong_gundongtiao()
        #点击提交订单
        OrderSubmitPage().click_order_submit().click()
        time.sleep(1)








