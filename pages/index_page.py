#-*-coding:utf-8-*-
from utils.get_selenium_driver import GetSeleniumDriver
import time
class RES():
    ############################################# 首页头部 #############################################################
    login_link="请登录"
    member_center_link="会员中心"
    ############################################ 纪念币楼层 ###########################################################
    goods14_link="祝寿银盘坯饼短"#第一行第4个商品
class IndexPage(object):
    def __init__(self):
        self.driver=GetSeleniumDriver().driver
    def click_login_link(self):
        try:
            click_login_link=self.driver.find_element_by_link_text("请登录")
            return click_login_link
        except Exception:
            assert False,"未成功点击登录"

    def click_goods14_link(self):
        try:
            click_goods14_link=self.driver.find_element_by_link_text(RES.goods14_link)
            return click_goods14_link
        except Exception:
            assert False,"未能成功点击商品"

    #点击会员中心
    def click_member_center(self):
        try:
            click_member_center=self.driver.find_element_by_link_text(RES.member_center_link)
            return click_member_center
        except Exception:
            assert False,"未能成功点击会员中心"



