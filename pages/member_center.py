#-*-coding:utf-8-*-
from utils.get_selenium_driver import GetSeleniumDriver
import time

class RES():
    ############################################# 账户中心 #############################################################
    address_link="收货地址"
class MemberCenter(object):
    def __init__(self):
        self.driver=GetSeleniumDriver().driver
    #点击收货地址
    def clink_address_link(self):
        try:
            click_address_link=self.driver.find_element_by_link_text(RES().address_link)
            return click_address_link
        except Exception:
            assert False,"未能成功点击收货地址"